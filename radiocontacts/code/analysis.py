"""Reproducible geometry for cumulative radio illumination, not detection.

Use ``uv run python -c 'from analysis import run_study; run_study()'``.
All rates are conditional on the specified pointing inventory and population.
"""

from pathlib import Path
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parent
AS_OF = pd.Timestamp("2026-10-07T00:00:00Z")
DAYS_PER_YEAR = 365.25
LY_PER_PC = 3.2615637771674333


def cone_expectation(age_years, full_width_arcmin, stellar_density_pc3,
                     hz_planets_per_star=1.0, inner_radius_ly=0.0):
    """Return expected stars/HZ planets reached by one fixed beam.

    Parameters are explicit: ``age_years`` is time since emission, the beam
    width is its full diameter, density counts stars (not stellar systems),
    and occurrence counts planets per star. A pulse's cumulative swept volume
    is used; the whole volume is not illuminated simultaneously. The spherical
    cap formula is exact, with a uniform spatial population outside the chosen
    empty inner radius. This is a population expectation, not a catalog count.
    """
    if not (0 < full_width_arcmin < 21600 and stellar_density_pc3 >= 0
            and hz_planets_per_star >= 0 and inner_radius_ly >= 0):
        raise ValueError("Invalid width, density, occurrence, or inner radius")
    age = np.maximum(np.asarray(age_years, dtype=float), 0)
    if not np.isfinite(age).all():
        raise ValueError("Nonfinite emission age")
    alpha = math.radians(full_width_arcmin / 120)
    omega = 4 * math.pi * math.sin(alpha / 2) ** 2
    volume_ly3 = omega * np.maximum(age ** 3 - inner_radius_ly ** 3, 0) / 3
    return volume_ly3 * stellar_density_pc3 / LY_PER_PC ** 3 * hz_planets_per_star


def sample_beam_union(pointings, full_width_arcmin=None, samples=120000, seed=7,
                      reference_width_arcmin=2.0):
    """Integrate overlapping beam disks without adding repeated cones.

    ``pointings`` must contain ra_deg, dec_deg, emission_utc. Random directions
    are sampled from a disk mixture. For a constant width, disks are equiprobable;
    otherwise each row's ``beam_full_width_arcmin`` supplies its width and disks
    are chosen in proportion to solid angle. Each ray receives weight
    sum(solid_angles)/multiplicity, making an unbiased angular-union
    integral for this discrete disk inventory. The first emission intersecting
    a ray controls cumulative first arrival. Returns sample weights and first
    emission epochs for later time-dependent volumes; errors describe Monte
    Carlo integration only, not uncertain source data or track reconstruction.
    """
    required = {"ra_deg", "dec_deg", "emission_utc"}
    if not required.issubset(pointings) or len(pointings) == 0:
        raise ValueError("Missing columns or empty pointing inventory")
    coords = pointings[["ra_deg", "dec_deg"]].to_numpy(float)
    if not np.isfinite(coords).all() or np.any(np.abs(coords[:, 1]) > 90):
        raise ValueError("Invalid coordinates")
    epochs = pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).astype("int64").to_numpy()
    if pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).isna().any():
        raise ValueError("Missing emission time")
    ra, dec = np.deg2rad(coords).T
    centers = np.column_stack((np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)))
    widths = (np.full(len(centers), full_width_arcmin, dtype=float) if full_width_arcmin is not None
              else pointings.beam_full_width_arcmin.to_numpy(float))
    if not np.isfinite(widths).all() or (widths <= 0).any() or (widths >= 21600).any():
        raise ValueError("Invalid beam widths")
    alpha = np.deg2rad(widths/120)
    omega = 4*math.pi*np.sin(alpha/2)**2
    chords = 2*np.sin(alpha/2)
    constant_width = np.ptp(widths) == 0
    rng = np.random.default_rng(seed)
    chosen_indices = (rng.integers(len(centers), size=samples) if constant_width
                      else rng.choice(len(centers), size=samples, p=omega/omega.sum()))
    chosen = centers[chosen_indices]
    reference = np.tile([0.0, 0.0, 1.0], (samples, 1))
    reference[np.abs(chosen[:, 2]) > 0.9] = [1.0, 0.0, 0.0]
    tangent = np.cross(reference, chosen)
    tangent /= np.linalg.norm(tangent, axis=1)[:, None]
    tangent2 = np.cross(chosen, tangent)
    cos_theta = 1-rng.random(samples)*2*np.sin(alpha[chosen_indices]/2)**2
    sin_theta = np.sqrt(np.maximum(1 - cos_theta**2, 0))
    phi = rng.uniform(0, 2 * math.pi, samples)
    rays = chosen*cos_theta[:, None] + sin_theta[:, None]*(
        tangent*np.cos(phi)[:, None] + tangent2*np.sin(phi)[:, None])
    # Query each native width separately. A rare broad message beam must not
    # inflate candidate searches around hundreds of thousands of narrow rays.
    groups = []
    for width in np.unique(widths):
        members = np.flatnonzero(widths == width)
        groups.append((members, cKDTree(centers[members]), float(chords[members[0]])))
    multiplicity = np.empty(samples, dtype=int)
    first_epochs = np.empty(samples, dtype=np.int64)
    # Limit temporary neighbor lists for dense, repeatedly observed tracks.
    for start in range(0, samples, 1000):
        stop = min(start+1000, samples)
        neighbors = [[] for _ in range(stop-start)]
        for members, tree, chord in groups:
            local = tree.query_ball_point(rays[start:stop], chord*(1+1e-9))
            for index, contained in enumerate(local):
                neighbors[index].extend(members[contained])
        multiplicity[start:stop] = [len(n) for n in neighbors]
        first_epochs[start:stop] = [epochs[n].min() for n in neighbors]
    if (multiplicity < 1).any():
        raise ArithmeticError("Sampled ray fell outside its parent beam")
    weights = omega.sum()/multiplicity
    reference_sr = (float(omega[0]) if constant_width else
                    4*math.pi*math.sin(math.radians(reference_width_arcmin/120)/2)**2)
    return {"weights_sr": weights, "first_epoch_ns": first_epochs,
            "sampled_directions": rays,
            "one_beam_sr": reference_sr, "reference_width_arcmin": float(widths[0]) if constant_width else reference_width_arcmin,
            "seed": seed, "samples": samples,
            "input_disks": len(centers)}


def union_expectation(union, when, stellar_density_pc3, hz_planets_per_star,
                      inner_radius_ly=4.24, max_radius_ly=None):
    """Convert the angular union to dated, deduplicated population estimates.

    The earliest signal on each ray has reached R=age in light-years. Returns
    volume, mean stars, mean HZ planets, numerical standard errors, and the
    instantaneous expected new-star rate per year. An optional radius cap
    limits the population; it is not an independently established detection
    horizon. Stellar density and occurrence must use compatible denominators.
    """
    epoch = pd.Timestamp(when)
    if epoch.tzinfo is None:
        epoch = epoch.tz_localize("UTC")
    ages = np.maximum((epoch.timestamp() - union["first_epoch_ns"]/1e9)/86400/DAYS_PER_YEAR, 0)
    radius = ages if max_radius_ly is None else np.minimum(ages, max_radius_ly)
    contributions = union["weights_sr"]*np.maximum(radius**3-inner_radius_ly**3, 0)/3
    volume = float(contributions.mean())
    volume_se = float(contributions.std(ddof=1)/math.sqrt(len(contributions)))
    derivative = union["weights_sr"]*radius**2*(radius > inner_radius_ly)
    if max_radius_ly is not None:
        derivative *= ages < max_radius_ly
    density_ly3 = stellar_density_pc3/LY_PER_PC**3
    active = union["first_epoch_ns"]/1e9 <= epoch.timestamp()
    area = float((union["weights_sr"]*active).mean())
    area_se = float((union["weights_sr"]*active).std(ddof=1)/math.sqrt(len(active)))
    return {"date_utc": epoch.isoformat(), "volume_ly3": volume,
            "volume_mc_se_ly3": volume_se,
            "stars_expected": volume*density_ly3,
            "hz_planets_expected": volume*density_ly3*hz_planets_per_star,
            "new_stars_expected_per_year": float(derivative.mean())*density_ly3,
            "coverage_sr": area, "coverage_mc_se_sr": area_se,
            "equivalent_beam_disks": area/union["one_beam_sr"]}


def summarize_arecibo_transmit_time():
    """Audit summed versus overlapping UTC transmit-window durations.

    The transmitter is one antenna, so concurrent archive representations
    cannot be added as independent transmitter-on time. The global time union
    is reported alongside the duration sum; neither verifies unresolved gaps
    or original pointing during each recorded interval.
    """
    from data.radar.reconstruct_bulk_beams import snapshot_transmit_runs
    rows, _ = snapshot_transmit_runs(ROOT/"data/radar/bulk_ucla/all_runs.csv")
    intervals = sorted((datetime.fromisoformat(r["start_utc"]), datetime.fromisoformat(r["end_utc"])) for r in rows)
    total, overlapping = 0.0, 0
    start, end = intervals[0]
    for next_start, next_end in intervals[1:]:
        if next_start < end:
            end = max(end, next_end)
            overlapping += 1
        else:
            total += (end-start).total_seconds()
            start, end = next_start, next_end
    total += (end-start).total_seconds()
    result = {"valid_intervals": len(rows),
              "summed_duration_hours": sum((b-a).total_seconds() for a, b in intervals)/3600,
              "union_duration_hours": total/3600,
              "intervals_strictly_overlapping_preceding_union": overlapping}
    (ROOT/"results/arecibo_transmit_time_audit.json").write_text(json.dumps(result, indent=2))
    return result


def analyze_arecibo_archive(samples=120000, seed=23, require_complete=True,
                            output_prefix="arecibo_archive", exclude_composite_ids=()):
    """Integrate dated reconstructed Arecibo beams and historical sky increments.

    Read only the successful targets in the reconstruction manifest. The final
    run requires every usable archived interval to be reconstructed; setting
    ``require_complete=False`` is for explicitly named interim checkpoints.
    ``exclude_composite_ids`` removes explicitly audited interval identities
    for a source-conflict sensitivity, after verifying the complete geometry.
    All recovered records are at 2.38 GHz and use a declared 2-arcminute full
    half-power width. Overlap and earliest emissions are integrated jointly,
    with population densities from the 10-pc census. These expectations use
    a static homogeneous population, not a discrete stellar catalogue.
    """
    directory = ROOT/"data/radar/bulk_beams"
    manifest = json.loads((directory/"reconstruction_summary.json").read_text())
    audit = json.loads((ROOT/"data/radar/bulk_ucla/coverage_audit.json").read_text())
    source_path = Path(manifest["input_path"])
    if not source_path.is_absolute():
        source_path = ROOT/source_path
    snapshot_matches = (source_path.stat().st_size == manifest["snapshot_size_bytes"]
                        and hashlib.sha256(source_path.read_bytes()).hexdigest() == manifest["snapshot_sha256"])
    complete = (not manifest["failed_targets"]
                and manifest["reconstructed_runs"] == audit["valid_verified_transmit_windows"]
                and len(manifest["reconstructed_targets"]) == audit["target_ids_with_valid_windows"]
                and snapshot_matches)
    if require_complete and not complete:
        raise ValueError("Archive geometry is incomplete; final integration refused")
    frames = []
    for target in manifest["reconstructed_targets"]:
        target_summary = json.loads((directory/f"{target['canonical_object_id']}.summary.json").read_text())
        assert target_summary["run_signature"] == target["run_signature"]
        frame = pd.read_csv(ROOT/target["output_csv"],
                            usecols=["composite_run_id", "epoch_utc", "ra_deg", "dec_deg", "beam_full_width_arcmin"])
        assert len(frame) == target["direction_samples"]
        assert frame.composite_run_id.nunique() == target["transmit_runs"]
        assert np.allclose(frame.beam_full_width_arcmin, 2.0, rtol=0, atol=1e-12)
        frames.append(frame.rename(columns={"epoch_utc": "emission_utc"}))
    pointings = pd.concat(frames, ignore_index=True)
    pointings = pointings.loc[~pointings.composite_run_id.isin(exclude_composite_ids)]
    included_intervals = pointings.composite_run_id.nunique()
    pointings = pointings.drop_duplicates(subset=["emission_utc", "ra_deg", "dec_deg"])
    union = sample_beam_union(pointings, 2.0, samples=samples, seed=seed)
    parameters = json.loads((ROOT/"data/population_parameters.json").read_text())
    density = parameters["stellar_density_pc3"]
    eta = parameters["mixed_hz_planets_per_star"]
    forecasts = []
    for years in [0, 1, 10, 50, 100, 300]:
        when = datetime(2026+years, 10, 7, tzinfo=timezone.utc)
        row = union_expectation(union, when, density, eta)
        row["stellar_systems_expected"] = row["volume_ly3"]*parameters["stellar_system_density_pc3"]/LY_PER_PC**3
        row["g_star_hz_planets_expected"] = row["volume_ly3"]*parameters["g_star_density_pc3"]/LY_PER_PC**3*parameters["eta_g_conservative_lower_median"]
        for name, days in [("day", 1), ("week", 7), ("year", None)]:
            later_date = when.replace(year=when.year+1) if days is None else when+timedelta(days=days)
            later = union_expectation(union, later_date, density, eta)
            row[f"new_stars_next_{name}"] = later["stars_expected"]-row["stars_expected"]
            row[f"new_hz_planets_next_{name}"] = later["hz_planets_expected"]-row["hz_planets_expected"]
        forecasts.append(row)
    first_year = pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).min().year
    last_year = pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).max().year
    angular = []
    previous = 0.0
    for year in range(first_year, last_year+1):
        cutoff = pd.Timestamp(f"{year+1}-01-01T00:00:00Z").value
        start_epoch = pd.Timestamp(f"{year}-01-01T00:00:00Z").value
        contribution = union["weights_sr"]*(union["first_epoch_ns"] < cutoff)
        new_contribution = union["weights_sr"]*((union["first_epoch_ns"] >= start_epoch) & (union["first_epoch_ns"] < cutoff))
        area = float(contribution.mean())
        increment = area-previous
        annual_days = (datetime(year+1, 1, 1)-datetime(year, 1, 1)).days
        angular.append({"year": year, "cumulative_coverage_sr": area,
                        "new_coverage_sr": increment,
                        "new_coverage_mc_se_sr": float(new_contribution.std(ddof=1)/math.sqrt(samples)),
                        "new_beam_disk_equivalents": increment/union["one_beam_sr"],
                        "average_new_equivalents_per_calendar_day": increment/union["one_beam_sr"]/annual_days})
        previous = area
    np.savez_compressed(ROOT/"results"/f"{output_prefix}_union_samples.npz",
                        weights_sr=union["weights_sr"], first_epoch_ns=union["first_epoch_ns"],
                        sampled_directions=union["sampled_directions"], one_beam_sr=union["one_beam_sr"])
    pd.DataFrame(forecasts).to_csv(ROOT/"results"/f"{output_prefix}_volume_timeline.csv", index=False)
    pd.DataFrame(angular).to_csv(ROOT/"results"/f"{output_prefix}_annual_new_directions.csv", index=False)
    summary = {"as_of": AS_OF.isoformat(), "archive_geometry_complete": complete,
               "reconstructed_targets": len(frames), "reconstructed_transmit_intervals": manifest["reconstructed_runs"],
               "included_transmit_intervals": int(included_intervals), "excluded_composite_ids": sorted(exclude_composite_ids),
               "pointing_samples_before_exact_deduplication": sum(len(f) for f in frames),
               "pointing_samples": len(pointings), "samples": samples, "seed": seed,
               "full_width_arcmin": 2.0, "forecasts": forecasts, "annual_new_directions": angular,
               "method": "dated angular union; earliest emission on each sampled ray; static homogeneous census density outside 4.24 ly",
               "scope": "new sky relative to the retrieved 2001–2020 Arecibo subset; earlier and other-facility overlap unknown",
               "source_audit": audit}
    summary["transmit_time_audit"] = summarize_arecibo_transmit_time()
    (ROOT/"results"/f"{output_prefix}_summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False))
    return summary


def verify_geometry():
    """Check width conventions, overlap, time dependence, and zero-age limits.

    Independent analytical controls cover identical caps and disjoint caps.
    These checks verify the integration rather than mirroring source parsing.
    """
    p = pd.DataFrame({"ra_deg": [10., 10.], "dec_deg": [20., 20.],
                      "emission_utc": ["1966-10-07T00:00:00Z"]*2})
    u = sample_beam_union(p, 2.0, samples=4000)
    r = union_expectation(u, AS_OF, 0.08, 0.2, inner_radius_ly=0)
    expected = cone_expectation(60.0, 2.0, 0.08)
    assert np.isclose(r["stars_expected"], expected, rtol=1e-12)
    assert np.isclose(r["equivalent_beam_disks"], 1.)
    p.loc[1, "ra_deg"] = 100.
    u2 = sample_beam_union(p, 2.0, samples=4000)
    r2 = union_expectation(u2, AS_OF, 0.08, 0.2, inner_radius_ly=0)
    assert np.isclose(r2["stars_expected"], 2*expected, rtol=1e-12)
    assert np.isclose(r2["equivalent_beam_disks"], 2.)
    assert cone_expectation(0, 2.0, 0.08) == 0
    assert cone_expectation(1, 2.0, 0.08, inner_radius_ly=4.24) == 0
    assert np.isclose(cone_expectation(60, 4.0, 0.08)/expected, 4., rtol=1e-6)
    p["beam_full_width_arcmin"] = [2.0, 4.0]
    mixed = sample_beam_union(p, samples=4000)
    mixed_result = union_expectation(mixed, AS_OF, 0.08, 0.2, inner_radius_ly=0)
    mixed_expected = cone_expectation(60, 2, 0.08)+cone_expectation(60, 4, 0.08)
    assert np.isclose(mixed_result["stars_expected"], mixed_expected, rtol=1e-12)
    return {"identical_caps": "pass", "disjoint_caps": "pass", "zero_age": "pass",
            "empty_solar_neighborhood": "pass", "full_vs_half_angle": "pass",
            "mixed_width_disjoint_caps": "pass"}


def forecast_dsn_direction_area(samples=80000):
    """Estimate next-year angular coverage for three continuous mission tracks.

    This is explicitly a future continuous-transmission scenario, not measured
    activity or globally new sky. Voyager tracks reuse the fresh six-hour
    source trajectories; New Horizons extends its geocentric direction model
    with a cached, documented Horizons query. Each mission retains its own
    nominal 70-m full beamwidth. Per-mission incremental coverage is measured
    against all five missions' modeled past tracks, with their respective beam
    radii. It is not compared to all human transmissions. Past arcs are
    densified to quarter-radius spacing before measuring overlap.
    """
    import sys
    sys.path.insert(0, str(ROOT/"data/dsn"))
    from fetch_horizons import fetch_horizons_ephemeris

    directory = ROOT/"data/dsn/direction_forecast"
    directory.mkdir(exist_ok=True)
    nh_extension = directory/"new_horizons_extension.csv"
    if not nh_extension.exists():
        fetch_horizons_ephemeris("-98", "2024-12-31", "2027-10-08", nh_extension)
    past_trees = []
    tracks = {}
    for mission, folder, filename, width in [
        ("Voyager 1", "voyager1", "voy1_ephemeris.csv", 7.68),
        ("Voyager 2", "voyager2", "voy2_ephemeris.csv", 7.68),
        ("Pioneer 10", "pioneer10", "pio10_ephemeris.csv", 7.68),
        ("Pioneer 11", "pioneer11", "pio11_ephemeris.csv", 7.68),
        ("New Horizons", "new_horizons", "nh_ephemeris.csv", 2.28),
    ]:
        frame = pd.read_csv(ROOT/"data/dsn/horizons_adaptive"/folder/filename)
        if mission == "New Horizons":
            frame = pd.concat([frame, pd.read_csv(nh_extension)], ignore_index=True).drop_duplicates("date")
        frame["epoch"] = pd.to_datetime(frame.date, format="%Y-%b-%d %H:%M:%S.%f", utc=True)
        frame.sort_values("epoch", inplace=True)
        if mission == "Voyager 2":
            frame = frame.loc[~frame.epoch.between(pd.Timestamp("2020-03-09T00:00:00Z"), pd.Timestamp("2020-10-29T00:00:00Z"))]
        tracks[mission] = frame
        past = frame.loc[frame.epoch <= AS_OF]
        ra_p, dec_p = np.deg2rad(past[["ra", "dec"]].to_numpy()).T
        xyz = np.column_stack([np.cos(dec_p)*np.cos(ra_p), np.cos(dec_p)*np.sin(ra_p), np.sin(dec_p)])
        pieces = [xyz]
        alpha = math.radians(width/120)
        gaps = np.arctan2(np.linalg.norm(np.cross(xyz[:-1], xyz[1:]), axis=1), (xyz[:-1]*xyz[1:]).sum(axis=1))
        time_gaps = np.diff(past.epoch.astype("int64").to_numpy())/1e9
        for index in np.flatnonzero((gaps > alpha/4) & (time_gaps <= 6*3600)):
            # A shortest great-circle arc is the declared interpolation model;
            # using fractional Cartesian chord positions then normalizing gives
            # the same arc with slightly nonuniform angular spacing.
            steps = math.ceil(float(gaps[index])/(alpha/4)) + 1
            fraction = np.linspace(0, 1, steps+1)[1:-1, None]
            extra = xyz[index]*(1-fraction)+xyz[index+1]*fraction
            extra /= np.linalg.norm(extra, axis=1)[:, None]
            pieces.append(extra)
        dense_past = np.vstack(pieces)
        past_trees.append((mission, cKDTree(dense_past), 2*math.sin(alpha/2), len(dense_past)))
    results = []
    for mission, folder, filename, width in [
        ("Voyager 1", "voyager1", "voy1_ephemeris.csv", 7.68),
        ("Voyager 2", "voyager2", "voy2_ephemeris.csv", 7.68),
        ("New Horizons", "new_horizons", "nh_ephemeris.csv", 2.28),
    ]:
        frame = tracks[mission].copy()
        frame = frame.loc[frame.epoch <= AS_OF+pd.DateOffset(years=1)]
        all_points = frame.rename(columns={"ra": "ra_deg", "dec": "dec_deg", "epoch": "emission_utc"})
        future_points = all_points.loc[all_points.emission_utc >= AS_OF]
        assert len(future_points) >= 1460
        # Future annual tracks have fine angular spacing: retain original JPL
        # points and validate that the nearest-step cap discretization is small.
        ra, dec = np.deg2rad(future_points[["ra_deg", "dec_deg"]].to_numpy()).T
        xyz = np.column_stack([np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)])
        gaps = np.arctan2(np.linalg.norm(np.cross(xyz[:-1], xyz[1:]), axis=1),
                         (xyz[:-1]*xyz[1:]).sum(axis=1))
        assert gaps.max() <= math.radians(width/120)/4, (mission, np.rad2deg(gaps.max()))
        future_union = sample_beam_union(future_points, width, samples=samples)
        annual_area = union_expectation(future_union, AS_OF+pd.DateOffset(years=1), .08, .2)["coverage_sr"]
        # Importance-sample the future union, then remove rays in any past disk.
        # This has much less noise than sampling the large full mission union
        # to estimate a tiny future increment by subtracting two large areas.
        new_ray = np.ones(samples, dtype=bool)
        for _, past_tree, radius, _ in past_trees:
            nearest, _ = past_tree.query(future_union["sampled_directions"], distance_upper_bound=radius)
            new_ray &= nearest > radius
        new_contributions = future_union["weights_sr"]*new_ray
        new_area = float(new_contributions.mean())
        new_se = float(new_contributions.std(ddof=1)/math.sqrt(samples))
        results.append({"mission": mission, "full_width_arcmin": width,
                        "future_year_unique_angular_sr": annual_area,
                        "future_year_beam_disk_equivalents": annual_area/future_union["one_beam_sr"],
                        "equivalent_beam_disks_per_calendar_day": annual_area/future_union["one_beam_sr"]/365,
                        "new_vs_past_angular_sr": new_area,
                        "new_vs_past_angular_mc_se_sr": new_se,
                        "new_vs_past_beam_disk_equivalents": new_area/future_union["one_beam_sr"],
                        "new_vs_past_equivalent_disks_per_calendar_day": new_area/future_union["one_beam_sr"]/365,
                        "pointing_samples_next_year": len(future_points),
                        "maximum_angular_step_arcsec": float(np.rad2deg(gaps.max())*3600),
                        "reference": "new vs all five modeled prior mission tracks; global other-source overlap unresolved",
                        "past_dense_disks_by_mission": {name: count for name, _, _, count in past_trees},
                        "model": "hypothetical continuous tracking; geocentric incoming direction; 70-m beam"})
    (ROOT/"results/dsn_future_direction_scenario.json").write_text(json.dumps(results, indent=2, allow_nan=False))
    return results


def run_study():
    """Run the local dated inventories and save explicit result tables.

    Requires researcher exports in data/. Preserves DSN paper-reproduction
    results separately from Goldstone reconstructed envelopes and fixed-beam
    historical scenarios; these populations must never be added into a global
    total. Sources and parameters are frozen in the saved result JSON.
    """
    checks = verify_geometry()
    (ROOT/"results").mkdir(exist_ok=True)
    parameters = json.loads((ROOT/"data/population_parameters.json").read_text())
    dsn = pd.read_csv(ROOT/"data/dsn/dsn_unique_objects.csv", dtype={"gaia_edr3_source_id": str})
    assert len(dsn) == 1278 and dsn.gaia_edr3_source_id.is_unique
    dsn = dsn.loc[dsn.historical_model_emission].copy()
    assert len(dsn) == 1277
    # ISO strings sort chronologically here and do not have pandas' 2262
    # nanosecond upper limit. Validate every source timestamp before comparing.
    dates = dsn.recalculated_arrival_iso
    for value in dates:
        datetime.fromisoformat(value)
    timeline = []
    for year in range(2026, 2351):
        when = datetime(year, 10, 7, tzinfo=timezone.utc)
        timeline.append({"date": when.date().isoformat(), "unique_gaia_objects": int((dates <= when.replace(tzinfo=None).isoformat()).sum())})
    pd.DataFrame(timeline).to_csv(ROOT/"results/dsn_timeline.csv", index=False)
    p = pd.read_csv(ROOT/"data/radar/goldstone_pointings.csv")
    assert len(p) > 0
    assert pd.to_datetime(p.emission_utc, format="ISO8601", utc=True).max() < AS_OF
    union = sample_beam_union(p, parameters["goldstone_full_width_arcmin"])
    density = parameters["stellar_density_pc3"]
    eta = parameters["mixed_hz_planets_per_star"]
    # Population density sensitivity is linear; it does not imply Poisson or
    # occurrence confidence intervals for this fixed sparse sky selection.
    results = []
    for years in [0, 1, 10, 50, 100, 300]:
        when = datetime(2026+years, 10, 7, tzinfo=timezone.utc)
        result = union_expectation(union, when, density, eta)
        for name, days in [("day", 1), ("week", 7), ("year", None)]:
            future_date = when.replace(year=when.year+1) if days is None else when+timedelta(days=days)
            future = union_expectation(union, future_date, density, eta)
            result[f"new_stars_next_{name}"] = future["stars_expected"]-result["stars_expected"]
            result[f"new_hz_planets_next_{name}"] = future["hz_planets_expected"]-result["hz_planets_expected"]
        results.append(result)
    pd.DataFrame(results).to_csv(ROOT/"results/goldstone_volume_timeline.csv", index=False)
    angular = []
    for day in pd.date_range(pd.to_datetime(p.emission_utc, format="ISO8601", utc=True).min().floor("D"),
                             pd.to_datetime(p.emission_utc, format="ISO8601", utc=True).max().ceil("D"), freq="D"):
        r = union_expectation(union, day, density, eta)
        angular.append({"date": day.date().isoformat(), "coverage_sr": r["coverage_sr"],
                        "equivalent_beam_disks": r["equivalent_beam_disks"]})
    pd.DataFrame(angular).to_csv(ROOT/"results/goldstone_angular_timeline.csv", index=False)
    repeated = sample_beam_union(p, parameters["goldstone_full_width_arcmin"], seed=17)
    repeat_result = union_expectation(repeated, AS_OF+pd.DateOffset(years=100), density, eta)
    end = union_expectation(union, AS_OF, density, eta)
    usable = p.loc[~p.pointing_or_setup_warning].copy()
    exclude_warnings = union_expectation(sample_beam_union(usable, parameters["goldstone_full_width_arcmin"], samples=60000),
                                        AS_OF+pd.DateOffset(years=100), density, eta)
    sensitivity = []
    for width in [parameters["goldstone_full_width_arcmin"]/2, parameters["goldstone_full_width_arcmin"]*2]:
        sensitivity.append(union_expectation(sample_beam_union(p, width, samples=60000),
                                             AS_OF+pd.DateOffset(years=100), density, eta))
        sensitivity[-1]["full_width_arcmin"] = width
    scenarios = []
    for beams in [1000, 10000, 100000]:
        for age in [20, 40, 60]:
            now = beams*cone_expectation(age, 2.0, density, inner_radius_ly=4.24)
            row = {"nonoverlapping_fixed_beams": beams, "age_years": age,
                   "stars_expected": float(now), "hz_planets_expected": float(now*eta)}
            for name, delta in [("day", 1/365.25), ("week", 7/365.25), ("year", 1.)]:
                increase = beams*cone_expectation(age+delta, 2.0, density, inner_radius_ly=4.24)-now
                row[f"new_stars_next_{name}"] = float(increase)
                row[f"new_hz_planets_next_{name}"] = float(increase*eta)
            scenarios.append(row)
    pd.DataFrame(scenarios).to_csv(ROOT/"results/historical_fixed_beam_scenarios.csv", index=False)
    arecibo_p = pd.read_csv(ROOT/"data/radar/arecibo_pointings.csv")
    arecibo_union = sample_beam_union(arecibo_p, 2.0)
    arecibo_results = []
    for years in [0, 1, 10, 50, 100, 300]:
        when = datetime(2026+years, 10, 7, tzinfo=timezone.utc)
        row = union_expectation(arecibo_union, when, density, eta)
        for name, days in [("day", 1), ("week", 7), ("year", None)]:
            future_date = when.replace(year=when.year+1) if days is None else when+timedelta(days=days)
            later = union_expectation(arecibo_union, future_date, density, eta)
            row[f"new_stars_next_{name}"] = later["stars_expected"]-row["stars_expected"]
            row[f"new_hz_planets_next_{name}"] = later["hz_planets_expected"]-row["hz_planets_expected"]
        arecibo_results.append(row)
    pd.DataFrame(arecibo_results).to_csv(ROOT/"results/arecibo_volume_timeline.csv", index=False)
    # Stellar-system counts are an independent census scaling; the eta factor
    # is per star and must not be multiplied into systems a second time.
    for group in [results, arecibo_results]:
        for row in group:
            row["stellar_systems_expected"] = row["volume_ly3"]*parameters["stellar_system_density_pc3"]/LY_PER_PC**3
            row["g_star_hz_planets_expected"] = row["volume_ly3"]*parameters["g_star_density_pc3"]/LY_PER_PC**3*parameters["eta_g_conservative_lower_median"]
    pd.DataFrame(results).to_csv(ROOT/"results/goldstone_volume_timeline.csv", index=False)
    pd.DataFrame(arecibo_results).to_csv(ROOT/"results/arecibo_volume_timeline.csv", index=False)
    hashed = {}
    for file in sorted((ROOT/"data").rglob("*")):
        if file.is_file() and "upstream/.git/" not in str(file) and "__pycache__" not in file.parts:
            hashed[str(file.relative_to(ROOT))] = hashlib.sha256(file.read_bytes()).hexdigest()
    hashed["analysis.py"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    summary = {"as_of": AS_OF.isoformat(), "parameters": parameters, "checks": checks,
               "pointing_disks": len(p), "goldstone_angular": end,
               "goldstone_results": results,
               "goldstone_exclude_warning_100yr": exclude_warnings,
               "arecibo_results": arecibo_results,
               "arecibo_pointing_disks": len(arecibo_p),
               "integration_repeat_100yr_stars": repeat_result["stars_expected"],
               "integration_primary_100yr_stars": results[4]["stars_expected"],
               "beam_width_sensitivity_100yr": sensitivity, "source_sha256": hashed}
    (ROOT/"results/summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False))
    return summary
