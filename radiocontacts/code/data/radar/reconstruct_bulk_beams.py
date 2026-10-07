"""Reconstruct dated, outgoing Arecibo beams from public transmit-run records.

Current JPL orbit solutions replace missing historical antenna encoders.
Only actual txup/txdown windows are sampled; missing times remain excluded
with reasons. Direction spacing is verified against real vector samples.
"""

import csv
import hashlib
import json
import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import numpy as np

from data.radar.extract_radar import horizons_vectors


def snapshot_transmit_runs(path: str | Path, require_verified_identity: bool = True) -> tuple[list[dict], dict]:
    """Read a stable scraper checkpoint and identify exact S-band transmit runs.

    A before/after size and nanosecond-mtime comparison detects concurrent
    checkpoint writes. Three attempts are allowed, then reading fails loudly.
    Canonical object identity comes from the advertised UCLA ``AB`` parameter;
    run identity also includes date, runid, transmitter, waveform, frequency
    and transmitter times, because calibration rows can reuse a runid within
    the same object/date. Identical duplicates
    are counted and removed. Records that share one outgoing interval but
    differ in other measurement metadata are counted separately in the audit;
    conflicting transmitter metadata raise an exception.
    """
    path = Path(path)
    for attempt in range(3):
        before = path.stat()
        with path.open(newline="") as handle:
            raw = list(csv.DictReader(handle))
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns):
            break
        time.sleep(0.1)
    else:
        raise RuntimeError(f"Scraper checkpoint kept changing while reading {path}")
    assert raw, f"No runs in {path}"
    if require_verified_identity:
        assert {"canonical_horizons_designation", "seed_identity_verified"} <= raw[0].keys(), "Wait for the audited run-page identity checkpoint"
    canonical, exclusions = {}, []
    raw_fields = ['runid', 'tx', 'rx', 'freq', 'wvfrm', 'numpol', 'txoff', 'rxoff',
                  'dtk', 'fs', 'bits', 'codelen', 'baud', 'smpb', 'ephdelay',
                  'ephgen', 'ephsol', 'utdate', 'txup', 'txdown', 'rxup', 'rxdown']
    measurement_keys = set()
    duplicate_count, metadata_variants = 0, []
    for row in raw:
        query = parse_qs(urlparse(row["source_url"]).query)
        assert len(query.get("AB", [])) == 1, row["source_url"]
        row["canonical_object_id"] = query["AB"][0]
        row["archive_run_key"] = "|".join([row["canonical_object_id"], row["utdate"], row["runid"], row["tx"]])
        row["composite_run_id"] = "|".join([row["archive_run_key"], row["wvfrm"], row["freq"], row["txup"], row["txdown"]])
        key = row["composite_run_id"]
        measurement_key = (row["canonical_object_id"], *(row[field] for field in raw_fields))
        identical_measurement = measurement_key in measurement_keys
        measurement_keys.add(measurement_key)
        if key in canonical:
            original = canonical[key]
            for field in ["start_utc", "end_utc", "freq", "tx", "txup", "txdown"]:
                assert original[field] == row[field], (key, field, original[field], row[field])
            if identical_measurement:
                duplicate_count += 1
            else:
                metadata_variants.append({"composite_run_id": key,
                                          "differing_fields": [field for field in raw_fields if original[field] != row[field]],
                                          "transmission_times_available": row["transmission_times_available"]})
            continue
        canonical[key] = row
    usable = []
    for row in canonical.values():
        if require_verified_identity and row["seed_identity_verified"] not in ["True", "true", "1"]:
            exclusions.append({"composite_run_id": row["composite_run_id"], "reason": "run-page canonical object identity not verified"})
            continue
        if row["transmission_times_available"] not in ["True", "true", "1"]:
            exclusions.append({"composite_run_id": row["composite_run_id"], "reason": "missing or invalid transmitter times"})
            continue
        if row["tx"] != "A":
            exclusions.append({"composite_run_id": row["composite_run_id"], "reason": "transmitter is not Arecibo A"})
            continue
        try:
            frequency = float(row["freq"])
        except ValueError:
            exclusions.append({"composite_run_id": row["composite_run_id"], "reason": "frequency missing or nonnumeric"})
            continue
        if not 2.37e9 <= frequency <= 2.39e9:
            exclusions.append({"composite_run_id": row["composite_run_id"], "reason": f"frequency outside documented S-band scenario: {frequency}"})
            continue
        start, end = datetime.fromisoformat(row["start_utc"]), datetime.fromisoformat(row["end_utc"])
        assert start.tzinfo is not None and end.tzinfo is not None
        assert 0 < (end - start).total_seconds() < 86400
        row["beam_full_width_arcmin"] = 2.0 * 2.38e9 / frequency
        row["beam_width_basis"] = "2-arcmin S-band nominal width scaled inversely with recorded frequency"
        usable.append(row)
    project_root = Path(__file__).resolve().parents[2]
    input_name = str(path.resolve().relative_to(project_root)) if path.resolve().is_relative_to(project_root) else str(path.resolve())
    return usable, {"input_path": input_name, "snapshot_size_bytes": after.st_size,
                    "snapshot_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "snapshot_mtime_ns": after.st_mtime_ns, "raw_rows": len(raw),
                    "canonical_unique_runs": len(canonical), "identical_duplicate_rows": duplicate_count,
                    "unique_archive_measurements": len(measurement_keys),
                    "same_outgoing_interval_metadata_variants": metadata_variants,
                    "receiver_anchored_date_corrected_transmit_runs": sum(float(row.get("transmission_date_shift_days", 0) or 0) != 0 for row in usable),
                    "cross_target_time_conflict_transmit_runs": sum(row.get("cross_target_time_conflict") in ["True", "true", "1"] for row in usable),
                    "usable_s_band_transmit_runs": len(usable), "excluded_runs": exclusions}


def reconstruct_target_beams(runs: list[dict], output_directory: str | Path,
                              max_spacing_arcsec: float = 15.0) -> dict:
    """Save outgoing pointings for one canonical target using cached JPL vectors.

    Exact run endpoints/midpoints establish a conservative angular-speed grid.
    Additional real ephemeris samples are requested as needed, with maximum
    time step 60 seconds. Every final adjacent spherical angle must be no more
    than the requested spacing (normally one quarter of the 1-arcmin radius).
    Arecibo's barycentric origin is obtained from paired geometric relative
    and barycentric target vectors. Linear target velocity supplies outgoing
    light-time point-ahead; this is a nominal target-tracking reconstruction.
    """
    assert runs and 0 < max_spacing_arcsec <= 15
    object_ids = {row["canonical_object_id"] for row in runs}
    assert len(object_ids) == 1
    output_directory = Path(output_directory)
    cache = output_directory / "vectors"
    cache.mkdir(parents=True, exist_ok=True)
    object_id = next(iter(object_ids))
    targets = {row.get("canonical_horizons_designation", row["target"]) for row in runs}
    assert len(targets) == 1, (object_id, targets)
    target = next(iter(targets))
    assert target
    query_target = target
    if target[:4].isdigit() and int(target[:4]) < 1925:
        # Horizons does not resolve these historical provisional designations.
        # Use the permanent number verified from the actual UCLA run title.
        permanent_numbers = {row.get("actual_permanent_number", "") for row in runs}
        assert len(permanent_numbers) == 1 and next(iter(permanent_numbers)).isdigit(), (target, permanent_numbers)
        query_target = next(iter(permanent_numbers))
    timing_fields = ["transmission_date_shift_days", "receiver_date_anchor_available", "timestamp_basis",
                     "previous_unanchored_start_utc", "previous_unanchored_end_utc",
                     "transmit_window_overlap", "cross_target_time_conflict"]
    signature = hashlib.sha256(json.dumps({"schema_version": 2, "runs":
        [(query_target, row["composite_run_id"], row["start_utc"], row["end_utc"], row["freq"],
          {name: row.get(name, "") for name in timing_fields})
         for row in sorted(runs, key=lambda item: item["composite_run_id"])]}, sort_keys=True).encode()).hexdigest()
    metadata_path = output_directory / f"{object_id}.summary.json"
    if metadata_path.exists():
        previous = json.loads(metadata_path.read_text())
        if previous["run_signature"] == signature and previous["max_spacing_arcsec"] == max_spacing_arcsec:
            return previous
    state_path = cache / f"{object_id}.epoch_states.json"
    states = json.loads(state_path.read_text()) if state_path.exists() else {}
    assert all(state["query_target"] == query_target for state in states.values()), "Cached target identity differs from verified run-page identity"
    pointing_cache = {}

    def ensure_epochs(epochs: set[datetime]) -> None:
        """Retrieve only missing timestamps, retaining request/response caches."""
        missing = sorted(epoch for epoch in epochs if epoch.isoformat() not in states)
        for begin in range(0, len(missing), 5000):
            batch = missing[begin:begin + 5000]
            digest = hashlib.sha256((query_target + "|" + "|".join(epoch.isoformat() for epoch in batch)).encode()).hexdigest()[:20]
            relative = horizons_vectors(query_target, batch, "Arecibo@399", cache / f"{object_id}_{digest}_relative")
            absolute = horizons_vectors(query_target, batch, "500@0", cache / f"{object_id}_{digest}_barycentric")
            for epoch, rel, abs_state in zip(batch, relative, absolute, strict=True):
                states[epoch.isoformat()] = {"relative": rel, "barycentric": abs_state, "query_target": query_target}
            temporary = state_path.with_suffix(".tmp")
            temporary.write_text(json.dumps(states))
            temporary.replace(state_path)

    def pointing(epoch: datetime) -> dict:
        """Calculate one outgoing unit direction and the antenna origin."""
        if epoch.isoformat() in pointing_cache:
            return pointing_cache[epoch.isoformat()]
        state = states[epoch.isoformat()]
        relative, absolute = np.array(state["relative"]), np.array(state["barycentric"])
        position, velocity = relative[1:4], absolute[4:7]
        flight = np.linalg.norm(position) / 299792.458
        for _ in range(4):
            outgoing = position + velocity * flight
            flight = np.linalg.norm(outgoing) / 299792.458
        unit = outgoing / np.linalg.norm(outgoing)
        origin = (absolute[1:4] - relative[1:4]) / 3.0856775814913673e13
        transverse = relative[4:7] - position * np.dot(position, relative[4:7]) / np.dot(position, position)
        result = {"epoch_utc": epoch.isoformat(), "ra_deg": math.degrees(math.atan2(unit[1], unit[0])) % 360,
                "dec_deg": math.degrees(math.asin(unit[2])), "ux": unit[0], "uy": unit[1], "uz": unit[2],
                "origin_x_pc": origin[0], "origin_y_pc": origin[1], "origin_z_pc": origin[2],
                "range_km": np.linalg.norm(position), "one_way_light_seconds": flight,
                "angular_speed_arcsec_per_second": np.linalg.norm(transverse) / np.linalg.norm(position) * 206264.806247}
        pointing_cache[epoch.isoformat()] = result
        return result

    run_epochs = {}
    initial = set()
    for row in runs:
        start, end = datetime.fromisoformat(row["start_utc"]), datetime.fromisoformat(row["end_utc"])
        run_epochs[row["composite_run_id"]] = [start, start + (end - start) / 2, end]
        initial.update(run_epochs[row["composite_run_id"]])
    ensure_epochs(initial)
    for row in runs:
        first = run_epochs[row["composite_run_id"]]
        speed = max(pointing(epoch)["angular_speed_arcsec_per_second"] for epoch in first)
        interval = min(60.0, max_spacing_arcsec / (1.5 * max(speed, 1e-12)))
        steps = max(1, math.ceil((first[-1] - first[0]).total_seconds() / interval))
        run_epochs[row["composite_run_id"]] = sorted(set(first + [first[0] + (first[-1] - first[0]) * (step / steps) for step in range(steps + 1)]))
    ensure_epochs({epoch for epochs in run_epochs.values() for epoch in epochs})
    for iteration in range(5):
        required = set()
        for row in runs:
            key = row["composite_run_id"]
            additions = []
            for start, end in zip(run_epochs[key][:-1], run_epochs[key][1:], strict=True):
                first = np.array([pointing(start)[name] for name in ["ux", "uy", "uz"]])
                last = np.array([pointing(end)[name] for name in ["ux", "uy", "uz"]])
                angle = math.atan2(np.linalg.norm(np.cross(first, last)), np.dot(first, last)) * 206264.806247
                if angle > max_spacing_arcsec + 1e-6:
                    additions.append(start + (end - start) / 2)
            if additions:
                required.update(additions)
                run_epochs[key] = sorted(set(run_epochs[key] + additions))
        if not required:
            break
        ensure_epochs(required)
    else:
        raise RuntimeError(f"Adaptive angular spacing did not converge for {target}")
    output_rows, maximum_angle = [], 0.0
    for row in runs:
        track = [pointing(epoch) for epoch in run_epochs[row["composite_run_id"]]]
        for first, last in zip(track[:-1], track[1:], strict=True):
            u, v = np.array([first[name] for name in ["ux", "uy", "uz"]]), np.array([last[name] for name in ["ux", "uy", "uz"]])
            maximum_angle = max(maximum_angle, math.atan2(np.linalg.norm(np.cross(u, v)), np.dot(u, v)) * 206264.806247)
        for sample in track:
            output_rows.append({"composite_run_id": row["composite_run_id"], "canonical_object_id": object_id,
                                "archive_run_key": row["archive_run_key"], "waveform": row["wvfrm"],
                                "target": row["target"], "query_target": query_target, "runid": row["runid"],
                                "seed_target": row.get("seed_target", row["target"]),
                                "seed_identity_verified": row.get("seed_identity_verified", "case source header verified separately"),
                                "tx": row["tx"], "rx": row["rx"], "frequency_hz": float(row["freq"]),
                                "beam_full_width_arcmin": row["beam_full_width_arcmin"],
                                "beam_width_basis": row["beam_width_basis"],
                                "start_utc": row["start_utc"], "end_utc": row["end_utc"],
                                "source_url": row["source_url"],
                                **{name: row.get(name, "") for name in timing_fields}, **sample})
    assert maximum_angle <= max_spacing_arcsec + 1e-6
    output_path = output_directory / f"{object_id}.samples.csv"
    with output_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]))
        writer.writeheader(); writer.writerows(output_rows)
    summary = {"canonical_object_id": object_id, "target": target, "query_target": query_target,
               "run_signature": signature, "schema_version": 2,
               "transmit_runs": len(runs), "direction_samples": len(output_rows),
               "receiver_anchored_date_corrected_runs": sum(float(row.get("transmission_date_shift_days", 0) or 0) != 0 for row in runs),
               "cross_target_time_conflict_runs": sum(row.get("cross_target_time_conflict") in ["True", "true", "1"] for row in runs),
               "max_spacing_arcsec": max_spacing_arcsec, "maximum_verified_step_arcsec": maximum_angle,
               "cached_unique_epochs": len(states), "output_csv": str(output_path),
               "minimum_emission_utc": min(row["epoch_utc"] for row in output_rows),
               "maximum_emission_utc": max(row["epoch_utc"] for row in output_rows)}
    metadata_path.write_text(json.dumps(summary, indent=2))
    return summary


def reconstruct_arecibo_bulk(runs_csv: str | Path, output_directory: str | Path,
                              max_spacing_arcsec: float = 15.0, max_workers: int = 3,
                              require_verified_identity: bool = True) -> dict:
    """Reconstruct all usable targets in a stable archive checkpoint.

    Independent targets use separate caches and output files. Target failures
    are recorded explicitly, printed and included in the saved coverage summary;
    the function does not turn a partial reconstruction into a full-archive
    result. Repeating it as the scrape grows reuses all matching epoch states.
    """
    assert 1 <= max_workers <= 4
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    runs, audit = snapshot_transmit_runs(runs_csv, require_verified_identity)
    groups = {}
    for row in runs:
        groups.setdefault(row["canonical_object_id"], []).append(row)
    audit["requested_targets"] = len(groups)
    results, failures = [], []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(reconstruct_target_beams, rows, output_directory, max_spacing_arcsec): key
                   for key, rows in sorted(groups.items())}
        for index, future in enumerate(as_completed(futures), 1):
            key = futures[future]
            try:
                result = future.result()
                results.append(result)
                print(f"Beam reconstruction {index}/{len(groups)}: {result['target']} / {result['transmit_runs']} runs / {result['direction_samples']} samples", flush=True)
            except Exception as error:
                failure = {"canonical_object_id": key, "target": groups[key][0]["target"],
                           "transmit_runs": len(groups[key]), "error_type": type(error).__name__, "error": str(error)}
                failures.append(failure)
                print(f"Beam reconstruction FAILED: {failure}", flush=True)
            audit.update(reconstructed_targets=results, failed_targets=failures,
                         successful_target_count=len(results), failed_target_count=len(failures),
                         reconstructed_runs=sum(row["transmit_runs"] for row in results),
                         direction_samples=sum(row["direction_samples"] for row in results))
            checkpoint = output_directory / "reconstruction_summary.tmp"
            checkpoint.write_text(json.dumps(audit, indent=2))
            checkpoint.replace(output_directory / "reconstruction_summary.json")
    return audit
