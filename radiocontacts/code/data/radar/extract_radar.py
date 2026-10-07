"""Small, auditable functions for the public JPL radar data snapshot.

The JPL master log contains receive/configuration windows, not a complete
per-pulse transmitter history. Directions reconstructed below are nominal
target-tracking directions and retain the source log's timing limitations.
"""

import csv
import fcntl
import json
import math
import re
import subprocess
import tempfile
import time
from html import unescape
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .ucla_timing import parse_ucla_transmit_interval


def extract_goldstone_logs(directory: str | Path) -> list[dict]:
    """Validate the downloaded JPL master log and save one row per window.

    Parameters
    ----------
    directory : str or Path
        Directory containing ``goldstone_masterlogs.json``.

    Returns
    -------
    list of dict
        All source rows, with UTC start/end timestamps and provenance. Windows
        crossing midnight are advanced by one day. No observations are removed.
    """
    directory = Path(directory)
    raw = json.loads((directory / "goldstone_masterlogs.json").read_text())
    rows = []
    for index, entry in enumerate(raw):
        assert len(entry["rcsta"]) == len(entry["rcend"]) == 6
        start = datetime.strptime(entry["date"] + entry["rcsta"], "%Y-%m-%d%H%M%S").replace(tzinfo=timezone.utc)
        end = datetime.strptime(entry["date"] + entry["rcend"], "%Y-%m-%d%H%M%S").replace(tzinfo=timezone.utc)
        if end < start:
            end += timedelta(days=1)
        assert 0 <= (end - start).total_seconds() < 86400
        notes = json.dumps(entry["notes"]) if isinstance(entry["notes"], list) else entry["notes"]
        rows.append({
            "interval_id": index,
            "target": entry["object"],
            "fullname": entry["fullname"],
            "start_utc": start.isoformat(),
            "end_utc": end.isoformat(),
            "window_seconds": (end - start).total_seconds(),
            "runs": int(entry["runs"]),
            "waveform": entry["transmission config"],
            "osod_solution": entry["osod solution"],
            "nominal_transmitter": "Goldstone DSS-14",
            "notes": notes,
            "pointing_or_setup_warning": any(word in notes.lower() for word in ("wrong date", "setup error", "bad run", "first 6 runs are bad")),
            "source_url": "https://echo.jpl.nasa.gov/data/masterlogs.json",
        })
    assert len(rows) == len(raw)
    with (directory / "goldstone_intervals.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def horizons_vectors(target: str, epochs: list[datetime], center: str, cache_prefix: Path) -> list[list[float]]:
    """Fetch geometric ICRF vectors at UTC epochs using the documented file API.

    The returned columns are Julian day, x/y/z (km), vx/vy/vz (km/s). Request
    text and JSON response are saved. A cached response is accepted only when
    its request exactly matches. ``center='coord@399'`` uses DSS-14's published
    geodetic position; ``center='500@0'`` is the solar-system barycenter.
    """
    assert epochs and len(epochs) <= 10000
    params = {
        "COMMAND": f"'{target};'" if str(target).isdigit() else f"'DES={target};'", "EPHEM_TYPE": "'VECTORS'",
        "CENTER": f"'{center}'", "VEC_CORR": "'NONE'", "VEC_TABLE": "'2'",
        "REF_PLANE": "'FRAME'", "REF_SYSTEM": "'ICRF'", "OUT_UNITS": "'KM-S'",
        "TIME_TYPE": "'UT'", "CSV_FORMAT": "'YES'", "OBJ_DATA": "'YES'",
        "TLIST_TYPE": "'JD'",
        # Batch-format documentation requires physical lines under 80 chars.
        "TLIST": "\n".join(f"'{epoch.timestamp() / 86400 + 2440587.5:.12f}'" for epoch in epochs),
    }
    if center == "coord@399":
        params.update(COORD_TYPE="'GEODETIC'", SITE_COORD="'-116.88953822,35.42590086,1.00139'")
    request = "!$$SOF\n" + "\n".join(f"{key}={value}" for key, value in params.items()) + "\n!$$EOF\n"
    request_path = cache_prefix.with_suffix(".txt")
    response_path = cache_prefix.with_suffix(".json")
    cache_valid = request_path.exists() and response_path.exists() and request_path.read_text() == request
    if not cache_valid:
        request_path.write_text(request)
        # curl uses the host's working certificate store; uv Python's default
        # certificate store did not recognize the local TLS interception CA.
        # JPL fair use requires one request at a time and an identifying
        # User-Agent. A host-level lock also serializes separate processes.
        lock_path = Path(tempfile.gettempdir()) / "radio-contact-study-jpl-api.lock"
        with lock_path.open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            for attempt in range(3):
                result = subprocess.run([
                    "curl", "--silent", "--show-error", "--max-time", "120",
                    "--user-agent", "radio-contact-study/0.1 (https://github.com/jkobject)",
                    "--write-out", "\n%{http_code}",
                    "-F", "format=json", "-F", f"input=@{request_path}",
                    "https://ssd.jpl.nasa.gov/api/horizons_file.api",
                ], check=True, capture_output=True, text=True)
                body, status = result.stdout.rsplit("\n", 1)
                if status == "200":
                    response_path.write_text(body)
                    break
                failure_path = cache_prefix.with_suffix(".http_error.json")
                failure_path.write_text(json.dumps({"http_status": status, "attempt": attempt + 1,
                                                    "body": body, "stderr": result.stderr}, indent=2))
                if status not in {"429", "500", "502", "503", "504"} or attempt == 2:
                    raise RuntimeError(f"Horizons HTTP {status}; response saved in {failure_path}")
                time.sleep(2 ** (attempt + 1))
    response = json.loads(response_path.read_text())
    assert response["signature"]["version"] == "1.0", response["signature"]
    if "error" in response:
        raise ValueError(response["error"])
    body = response["result"]
    assert "GEOMETRIC cartesian states" in body and "Reference frame : ICRF" in body
    table = body.split("$$SOE\n", 1)[1].split("$$EOE", 1)[0]
    vectors = [[float(row[0]), *map(float, row[2:8])] for row in csv.reader(table.splitlines()) if row]
    assert len(vectors) == len(epochs), (target, len(vectors), len(epochs))
    for epoch, vector in zip(epochs, vectors, strict=True):
        assert abs(vector[0] - epoch.timestamp() / 86400 - 2440587.5) < 1e-8
        assert all(math.isfinite(value) for value in vector)
    return vectors


def reconstruct_goldstone_directions(directory: str | Path, sample_seconds: int = 60) -> list[dict]:
    """Save nominal outgoing target tracks within the logged windows.

    One-minute samples plus exact endpoints are returned by default. Geometric
    site-to-target positions are corrected for outgoing light time using the
    target's barycentric velocity and a constant-velocity fixed-point solution.
    This describes the intended beam path, not a measured transmitter encoder
    log. Receive timestamps and transmit duty-cycle gaps remain unresolved.
    """
    assert sample_seconds > 0
    directory = Path(directory)
    intervals = extract_goldstone_logs(directory)
    samples = []
    for target in sorted({row["target"] for row in intervals}):
        target_intervals = [row for row in intervals if row["target"] == target]
        epochs = set()
        interval_epochs = {}
        for row in target_intervals:
            start, end = datetime.fromisoformat(row["start_utc"]), datetime.fromisoformat(row["end_utc"])
            steps = int((end - start).total_seconds() // sample_seconds)
            times = [start + timedelta(seconds=sample_seconds * index) for index in range(steps + 1)]
            if times[-1] != end:
                times.append(end)
            interval_epochs[row["interval_id"]] = times
            epochs.update(times)
        epochs = sorted(epochs)
        slug = target.replace(" ", "_")
        relative = horizons_vectors(target, epochs, "coord@399", directory / f"horizons_{slug}_relative")
        absolute = horizons_vectors(target, epochs, "500@0", directory / f"horizons_{slug}_barycentric")
        directions = {}
        for epoch, rel, abs_state in zip(epochs, relative, absolute, strict=True):
            position, velocity = rel[1:4], abs_state[4:7]
            distance = math.sqrt(sum(value**2 for value in position))
            light_seconds = distance / 299792.458
            for _ in range(3):
                outgoing = [x + v * light_seconds for x, v in zip(position, velocity, strict=True)]
                light_seconds = math.sqrt(sum(value**2 for value in outgoing)) / 299792.458
            length = math.sqrt(sum(value**2 for value in outgoing))
            unit = [value / length for value in outgoing]
            directions[epoch] = {
                "epoch_utc": epoch.isoformat(),
                "ra_deg": math.degrees(math.atan2(unit[1], unit[0])) % 360,
                "dec_deg": math.degrees(math.asin(unit[2])),
                "ux": unit[0], "uy": unit[1], "uz": unit[2],
                "range_km": distance, "one_way_light_seconds": light_seconds,
                "angular_speed_arcsec_per_second": 206264.806247 * math.sqrt(
                    sum(value**2 for value in rel[4:7]) - (sum(x * v for x, v in zip(position, rel[4:7], strict=True)) / distance)**2
                ) / distance,
            }
        for row in target_intervals:
            for epoch in interval_epochs[row["interval_id"]]:
                samples.append({
                    "interval_id": row["interval_id"], "target": target,
                    "pointing_or_setup_warning": row["pointing_or_setup_warning"],
                    **directions[epoch],
                })
        print(f"{target}: {len(epochs)} distinct ephemeris epochs", flush=True)
    samples.sort(key=lambda row: (row["epoch_utc"], row["interval_id"]))
    with (directory / "goldstone_direction_samples.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(samples[0]))
        writer.writeheader()
        writer.writerows(samples)
    return samples


def extract_radar_history(directory: str | Path) -> list[dict]:
    """Save station–apparition detections and annual counts, preserving rows.

    The source date is only month-precise. Its day 01 field is a database
    representation and must not be used as an actual transmission date.
    Counts represent detections, not runs or previously unilluminated sky.
    """
    directory = Path(directory)
    rows = json.loads((directory / "radar_history.json").read_text())
    with (directory / "radar_detections.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    counts = Counter((int(row["Date"][:4]), row["Transmitter"]) for row in rows)
    with (directory / "radar_detections_by_year.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["year", "transmitter", "station_apparition_detection_rows"])
        writer.writerows((year, transmitter, count) for (year, transmitter), count in sorted(counts.items()))
    return rows


def extract_ucla_runs(html_path: str | Path, target: str, source_url: str) -> list[dict]:
    """Parse a downloaded UCLA per-object run table without losing rows.

    ``txup``/``txdown`` are source transmitter start/end timestamps. They are
    preserved alongside every raw column. This function only parses the supplied
    page and does not imply that all 84,054 advertised archive runs are present.
    """
    html_path = Path(html_path)
    page = html_path.read_text()
    match = re.search(r'<table class="table".*?</table>', page, re.S)
    if match is None:
        raise ValueError(f"No run table in {html_path}")
    table = []
    for raw_row in re.findall(r'<tr\b[^>]*>(.*?)</tr>', match[0], re.S):
        table.append([
            unescape(re.sub(r'<[^>]+>', '', cell)).strip()
            for cell in re.findall(r'<td\b[^>]*>(.*?)</td>', raw_row, re.S)
        ])
    header = table[0]
    assert header == ['runid', 'tx', 'rx', 'freq', 'wvfrm', 'numpol', 'txoff', 'rxoff', 'dtk', 'fs', 'bits', 'codelen', 'baud', 'smpb', 'ephdelay', 'ephgen', 'ephsol', 'utdate', 'txup', 'txdown', 'rxup', 'rxdown']
    rows = []
    for cells in table[1:]:
        assert len(cells) == len(header)
        row = dict(zip(header, cells, strict=True))
        start, end = None, None
        if row['txup'] and row['txdown']:
            row.update(parse_ucla_transmit_interval(row))
            start = datetime.fromisoformat(row['start_utc'])
            end = datetime.fromisoformat(row['end_utc'])
        row.update(target=target, start_utc=start.isoformat() if start else '', end_utc=end.isoformat() if end else '', transmission_times_available=start is not None, source_url=source_url)
        rows.append(row)
    assert len(rows) == int(re.search(r'List of (\d+) runs', page)[1])
    with html_path.with_suffix('.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=sorted({key for row in rows for key in row}))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def sample_nominal_pointings(directory: str | Path, max_spacing_arcsec: float = 14.4,
                            prefix: str = 'goldstone', beam_full_width_deg: float = 0.032,
                            timing_basis: str = 'nominal configuration window; receive times in source') -> list[dict]:
    """Interpolate each separate nominal track at a bounded angular spacing.

    Spherical linear interpolation joins successive one-minute samples only
    within the same configuration window. This does not fill gaps between
    windows. ``emission_utc`` is an approximate configuration timestamp because
    the underlying source supplies receive times rather than per-pulse times.
    """
    assert max_spacing_arcsec > 0
    directory = Path(directory)
    with (directory / f'{prefix}_direction_samples.csv').open() as handle:
        raw = list(csv.DictReader(handle))
    rows = []
    for interval_id in sorted({int(row['interval_id']) for row in raw}):
        track = sorted((row for row in raw if int(row['interval_id']) == interval_id), key=lambda row: row['epoch_utc'])
        for index, first in enumerate(track):
            if index == len(track) - 1:
                fractions = [0.0]
                second = first
                angle = 0.0
            else:
                second = track[index + 1]
                u, v = [float(first[key]) for key in ['ux', 'uy', 'uz']], [float(second[key]) for key in ['ux', 'uy', 'uz']]
                angle = math.acos(max(-1.0, min(1.0, sum(x*y for x,y in zip(u,v,strict=True)))))
                steps = max(1, math.ceil(math.degrees(angle)*3600/max_spacing_arcsec))
                fractions = [step / steps for step in range(steps)]
            start, end = datetime.fromisoformat(first['epoch_utc']), datetime.fromisoformat(second['epoch_utc'])
            u, v = [float(first[key]) for key in ['ux', 'uy', 'uz']], [float(second[key]) for key in ['ux', 'uy', 'uz']]
            for fraction in fractions:
                if angle < 1e-12:
                    unit = u
                else:
                    unit = [(math.sin((1-fraction)*angle)*x + math.sin(fraction*angle)*y)/math.sin(angle) for x,y in zip(u,v,strict=True)]
                epoch = start + (end-start)*fraction
                rows.append({
                    'interval_id': interval_id, 'target': first['target'],
                    'emission_utc': epoch.isoformat(),
                    'ra_deg': math.degrees(math.atan2(unit[1],unit[0])) % 360,
                    'dec_deg': math.degrees(math.asin(unit[2])),
                    'pointing_or_setup_warning': first['pointing_or_setup_warning'],
                    'beam_full_width_deg': beam_full_width_deg,
                    'timing_basis': timing_basis,
                })
    rows.sort(key=lambda row: row['emission_utc'])
    with (directory / f'{prefix}_pointings.csv').open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def reconstruct_arecibo_case(directory: str | Path, sample_seconds: int = 60) -> list[dict]:
    """Reconstruct 2000 DP107's two downloaded apparitions from exact tx windows.

    Four of the 453 source rows lack transmitter timestamps and remain in the
    raw/parsed archive tables but are excluded explicitly from this reconstruction.
    Horizons resolves ``Arecibo@399`` to the radar observatory coordinates. The
    target trajectory is reconstructed with the current JPL orbit solution,
    rather than the original OSOD pointing file.
    """
    directory = Path(directory)
    runs = []
    for filename in ['ucla_dp107_runs.csv', 'ucla_dp107_2016_runs.csv']:
        with (directory / filename).open() as handle:
            runs.extend(csv.DictReader(handle))
    usable = [row for row in runs if row['transmission_times_available'] == 'True']
    assert len(runs) == 453 and len(usable) == 449
    all_samples = []
    intervals = []
    for year in [2008, 2016]:
        selected = [row for row in usable if row['utdate'].startswith(str(year))]
        epochs, run_epochs = set(), {}
        for row in selected:
            start, end = datetime.fromisoformat(row['start_utc']), datetime.fromisoformat(row['end_utc'])
            steps = int((end-start).total_seconds() // sample_seconds)
            times = [start + timedelta(seconds=index*sample_seconds) for index in range(steps+1)]
            if times[-1] != end:
                times.append(end)
            run_epochs[row['runid']] = times
            epochs.update(times)
            intervals.append({'interval_id': row['runid'], 'target': '2000 DP107',
                              'start_utc': row['start_utc'], 'end_utc': row['end_utc'],
                              'transmission_date_shift_days': row['transmission_date_shift_days'],
                              'receiver_date_anchor_available': row['receiver_date_anchor_available'],
                              'timestamp_basis': row['timestamp_basis'],
                              'runs': 1, 'transmitter': 'Arecibo', 'beam_full_width_deg': 2/60,
                              'source_url': row['source_url']})
        epochs = sorted(epochs)
        relative = horizons_vectors('2000 DP107', epochs, 'Arecibo@399', directory / f'horizons_DP107_{year}_arecibo_relative')
        absolute = horizons_vectors('2000 DP107', epochs, '500@0', directory / f'horizons_DP107_{year}_barycentric')
        directions = {}
        for epoch, rel, abs_state in zip(epochs, relative, absolute, strict=True):
            position, velocity = rel[1:4], abs_state[4:7]
            distance = math.sqrt(sum(value**2 for value in position))
            light_seconds = distance / 299792.458
            for _ in range(3):
                outgoing = [x+v*light_seconds for x,v in zip(position,velocity,strict=True)]
                light_seconds = math.sqrt(sum(value**2 for value in outgoing)) / 299792.458
            length = math.sqrt(sum(value**2 for value in outgoing))
            unit = [value/length for value in outgoing]
            directions[epoch] = {'epoch_utc': epoch.isoformat(),
                                 'ra_deg': math.degrees(math.atan2(unit[1],unit[0])) % 360,
                                 'dec_deg': math.degrees(math.asin(unit[2])),
                                 'ux': unit[0], 'uy': unit[1], 'uz': unit[2],
                                 'range_km': distance, 'one_way_light_seconds': light_seconds}
        for row in selected:
            for epoch in run_epochs[row['runid']]:
                all_samples.append({'interval_id': row['runid'], 'target': '2000 DP107',
                                    'pointing_or_setup_warning': False, **directions[epoch]})
        print(f'Arecibo DP107 {year}: {len(selected)} exact tx runs, {len(epochs)} ephemeris epochs', flush=True)
    for filename, rows in [('arecibo_intervals.csv', intervals), ('arecibo_direction_samples.csv', all_samples)]:
        with (directory / filename).open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    return sample_nominal_pointings(directory, max_spacing_arcsec=15.0, prefix='arecibo',
                                   beam_full_width_deg=2/60,
                                   timing_basis='exact txup/txdown in source; nominal reconstructed target pointing')
