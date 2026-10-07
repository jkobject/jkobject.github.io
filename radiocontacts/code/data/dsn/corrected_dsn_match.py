"""Match GCNS stars to an interpolated, spherical DSN beam model.

This corrects coordinate geometry and stellar reference epochs using cached
fresh/adaptively sampled or original ephemerides, inverse-parallax distances,
and assumed continuous uplinks. It is not an operational transmission-log
reconstruction; the selected variant solves rectilinear stellar interception.
"""

from datetime import datetime, timedelta
import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq, minimize_scalar
from scipy.spatial import cKDTree


EPHEMERIDES = {
    "Voyager 1": "voyager1/voy1_ephemeris.csv",
    "Voyager 2": "voyager2/voy2_ephemeris.csv",
    "Pioneer 10": "pioneer10/pio10_ephemeris.csv",
    "Pioneer 11": "pioneer11/pio11_ephemeris.csv",
    "New Horizons": "new_horizons/nh_ephemeris.csv",
}
PARSEC_METRES = 3.0856775814913673e16
LIGHT_SPEED = 299792458.0
JULIAN_YEAR_SECONDS = 365.25 * 86400.0
REFERENCE_EPOCH = datetime(2016, 1, 1, 12)  # J2016.0: Julian-date definition


def sky_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    """Convert arrays of ICRS angles to Cartesian unit directions."""
    ra, dec = np.deg2rad(ra_deg), np.deg2rad(dec_deg)
    return np.column_stack((np.cos(dec) * np.cos(ra),
                            np.cos(dec) * np.sin(ra), np.sin(dec)))


def propagate_catalog_stars(directions: np.ndarray, velocity: np.ndarray,
                             travel_years: np.ndarray, emission_epoch: float,
                             time_model: str) -> tuple[np.ndarray, np.ndarray]:
    """Return unit encounter directions and outgoing travel time in years.

    Direction and velocity have units of unit vector and inverse Julian years.
    Epoch is measured from J2016.0. Gaia coordinates refer to arrival of stellar
    light at the barycentre; ``linear_intersection`` places the catalogue source
    at physical epoch J2016.0 minus distance/c, then solves the positive moving
    star/light intersection. ``catalog_epoch`` deliberately reproduces the
    simpler single-flight advancement for an audit comparison.
    """
    if time_model == "catalog_epoch":
        target = directions + velocity * (emission_epoch + travel_years)[..., None]
        outgoing_years = travel_years
    elif time_model == "double_light_time_fixed":
        target = directions + velocity * (emission_epoch + 2 * travel_years)[..., None]
        outgoing_years = travel_years
    elif time_model == "linear_intersection":
        source_at_emission = directions + velocity * (emission_epoch + travel_years)[..., None]
        coefficient = 1 / travel_years**2 - np.sum(velocity**2, axis=-1)
        dot = np.sum(source_at_emission * velocity, axis=-1)
        squared_radius = np.sum(source_at_emission**2, axis=-1)
        assert np.all(coefficient > 0)
        outgoing_years = (dot + np.sqrt(dot**2 + coefficient * squared_radius)) / coefficient
        target = source_at_emission + velocity * outgoing_years[..., None]
    else:
        raise ValueError(f"Unknown stellar time model: {time_model}")
    target /= np.linalg.norm(target, axis=-1)[..., None]
    return target, outgoing_years


def match_corrected_dsn(directory: str | Path, full_beam_width_deg: float | dict = 0.128,
                        as_of: str = "2026-10-07", suffix: str = "",
                        ephemeris_directory: str = "upstream",
                        maximum_distance_pc: float = 100,
                        sample_stride: int = 1,
                        stellar_time_model: str = "catalog_epoch",
                        selected_spacecraft: list[str] | None = None) -> pd.DataFrame:
    """Save first intersections of stars with five continuous spherical tracks.

    Parameters
    ----------
    directory : str or Path
        Folder with ``gcns_main.csv`` and the author's ``upstream`` ephemerides.
    full_beam_width_deg : float or dict
        Adopted full half-power beamwidth or a mapping keyed by spacecraft.
        Default is the paper's uniform 0.128 degrees. New Horizons actual
        X-band uplink has a 70-m dish HPBW of 0.038 degrees.
    as_of : str
        UTC-midnight historical/future emission boundary as an ISO date.
    suffix : str
        Optional output suffix for sensitivity runs; never overwrites the paper.
    ephemeris_directory : str
        Directory with track CSVs; ``upstream`` reproduces author interpolation,
        while ``horizons_6h`` selects fresh fixed-interval JPL directions.
    maximum_distance_pc : float
        Optional nearby subset for focused verification, at most 100 parsecs.
    sample_stride : int
        Retain every Nth ephemeris sample for a stated resolution comparison.
    stellar_time_model : str
        ``catalog_epoch`` retains the simple audit approximation; use
        ``linear_intersection`` for explicit Gaia apparent-epoch accounting
        and the positive moving-star/outgoing-wave intersection. A fixed
        double-light-time approximation is also available as a sensitivity.
    selected_spacecraft : list of str or None
        Optional mission subset for explicit incremental recalculation. None
        evaluates all five missions. Output filenames must distinguish subsets.

    Returns
    -------
    pandas.DataFrame
        First nominal geometric encounter per spacecraft and Gaia object.

    Notes
    -----
    The stellar-time convention is recorded explicitly in every output row.
    Tangential motion uses Gaia's cosine-corrected RA component. Adopted radial
    velocity is used when supplied; otherwise this model explicitly assumes
    zero radial velocity and marks the row. The 100-pc boundary uses fixed
    inverse-parallax catalogue distance. The audit modes retain fixed travel
    time, while ``linear_intersection`` solves distance changes during flight.
    These JPL observer directions describe received astrometric light, rather
    than each ground antenna's outgoing point-ahead direction. This remains an
    idealized geometric exposure model even with improved stellar propagation.
    Between adjacent ephemeris directions, normalized Cartesian linear
    interpolation follows the short great-circle arc. Timestamp interpolation
    is linear; the track source is selected explicitly with the ephemeris
    directory. Voyager 2's documented 2020 uplink gap is omitted.
    """
    directory = Path(directory)
    widths = full_beam_width_deg if isinstance(full_beam_width_deg, dict) else {
        spacecraft: full_beam_width_deg for spacecraft in EPHEMERIDES}
    assert set(widths) == set(EPHEMERIDES) and all(0 < width < 1 for width in widths.values())
    stars = pd.read_csv(directory / "gcns_main.csv", dtype={"source_id": "string"})
    assert len(stars) == 331312 and stars["source_id"].nunique() == len(stars)
    required = ["ra", "dec", "parallax", "parallax_error", "pmra", "pmdec"]
    assert not stars[required].isna().any().any()
    assert 0 < maximum_distance_pc <= 100 and sample_stride >= 1
    stars = stars.loc[(stars.parallax >= 1000 / maximum_distance_pc) & (stars.parallax_error <= 0.34)].copy()
    stars.reset_index(drop=True, inplace=True)
    stars["distance_pc"] = 1000 / stars.parallax
    ra, dec = np.deg2rad(stars.ra.to_numpy()), np.deg2rad(stars.dec.to_numpy())
    directions = sky_vectors(stars.ra.to_numpy(), stars.dec.to_numpy())
    ra_tangents = np.column_stack((-np.sin(ra), np.cos(ra), np.zeros(len(ra))))
    dec_tangents = np.column_stack((-np.cos(ra) * np.sin(dec),
                                   -np.sin(ra) * np.sin(dec), np.cos(dec)))
    mas_to_rad = np.pi / (180 * 3600000)
    proper_motion = mas_to_rad * (stars.pmra.to_numpy()[:, None] * ra_tangents
                                  + stars.pmdec.to_numpy()[:, None] * dec_tangents)
    radial_velocity = stars.adoptedrv.fillna(0).to_numpy()
    if stellar_time_model == "linear_intersection":
        # Catalog proper motion uses light-arrival time; recover first-order
        # physical tangential velocity using adopted spectroscopic radial RV.
        proper_motion *= (1 + radial_velocity * 1000 / LIGHT_SPEED)[:, None]
    radial_rate = radial_velocity * 1000 * JULIAN_YEAR_SECONDS / PARSEC_METRES / stars.distance_pc.to_numpy()
    velocity = proper_motion + radial_rate[:, None] * directions
    travel_years = stars.distance_pc.to_numpy() * PARSEC_METRES / LIGHT_SPEED / JULIAN_YEAR_SECONDS
    tree = cKDTree(directions)
    records = []
    cutoff = datetime.fromisoformat(as_of)
    gap_start, gap_end = datetime(2020, 3, 9), datetime(2020, 10, 29)

    for spacecraft, relative_path in EPHEMERIDES.items():
        if selected_spacecraft is not None and spacecraft not in selected_spacecraft:
            continue
        full_width = widths[spacecraft]
        half_angle = np.deg2rad(full_width / 2)
        track = pd.read_csv(directory / ephemeris_directory / relative_path).iloc[::sample_stride].copy()
        dates = [datetime.strptime(value, "%Y-%b-%d %H:%M:%S.%f") for value in track.date]
        times = np.array([(date - REFERENCE_EPOCH).total_seconds() / JULIAN_YEAR_SECONDS for date in dates])
        assert np.all(np.diff(times) > 0), spacecraft
        beam = sky_vectors(track.ra.to_numpy(), track.dec.to_numpy())
        # Bound all stellar angular motion before pruning pairs with a KD-tree.
        motion_bound = 0.0
        for epoch in (times[0], times[-1]):
            advanced, _ = propagate_catalog_stars(directions, velocity, travel_years, epoch, stellar_time_model)
            angles = np.arctan2(np.linalg.norm(np.cross(directions, advanced), axis=1),
                                np.sum(directions * advanced, axis=1))
            motion_bound = max(motion_bound, float(np.max(angles)))
        found = set()
        # Batch the broad KD-tree lookup; exact midpoint bounds then remove
        # pairs that cannot intersect before the scalar boundary solver runs.
        midpoints = beam[:-1] + beam[1:]
        midpoints /= np.linalg.norm(midpoints, axis=1)[:, None]
        separations = np.arctan2(np.linalg.norm(np.cross(beam[:-1], beam[1:]), axis=1),
                                  np.sum(beam[:-1] * beam[1:], axis=1))
        radii = half_angle + separations / 2 + motion_bound + 1e-9
        all_candidates = tree.query_ball_point(midpoints, 2 * np.sin(radii / 2))
        for i in range(len(beam) - 1):
            if spacecraft == "Voyager 2" and dates[i] < gap_end and dates[i + 1] > gap_start:
                continue
            midpoint, separation = midpoints[i], separations[i]
            assert separation < np.deg2rad(10), (spacecraft, i, np.rad2deg(separation))
            candidates = np.array([index for index in all_candidates[i] if index not in found], dtype=int)
            if not len(candidates):
                continue
            midpoint_epoch = (times[i] + times[i + 1]) / 2
            target_mid, _ = propagate_catalog_stars(directions[candidates], velocity[candidates], travel_years[candidates], midpoint_epoch, stellar_time_model)
            midpoint_angles = np.arctan2(np.linalg.norm(np.cross(target_mid, midpoint), axis=1),
                                          target_mid @ midpoint)
            target_start, _ = propagate_catalog_stars(directions[candidates], velocity[candidates], travel_years[candidates], times[i], stellar_time_model)
            target_end, _ = propagate_catalog_stars(directions[candidates], velocity[candidates], travel_years[candidates], times[i + 1], stellar_time_model)
            displacement_start = np.arctan2(np.linalg.norm(np.cross(target_start, target_mid), axis=1),
                                              np.sum(target_start * target_mid, axis=1))
            displacement_end = np.arctan2(np.linalg.norm(np.cross(target_end, target_mid), axis=1),
                                            np.sum(target_end * target_mid, axis=1))
            feasible = midpoint_angles <= half_angle + separation / 2 + np.maximum(displacement_start, displacement_end) + 1e-10
            for index in candidates[feasible]:

                def angular_distance(fraction: float) -> float:
                    """Spherical beam/star separation at an interpolated epoch."""
                    epoch = times[i] + fraction * (times[i + 1] - times[i])
                    target, _ = propagate_catalog_stars(directions[index], velocity[index], travel_years[index], epoch, stellar_time_model)
                    pointing = beam[i] + fraction * (beam[i + 1] - beam[i])
                    pointing /= np.linalg.norm(pointing)
                    return float(np.arctan2(np.linalg.norm(np.cross(pointing, target)),
                                             np.dot(pointing, target)))

                minimum = minimize_scalar(angular_distance, bounds=(0, 1), method="bounded",
                                          options={"xatol": 1e-9})
                choices = [(0.0, angular_distance(0)), (1.0, angular_distance(1)),
                           (float(minimum.x), float(minimum.fun))]
                closest_fraction, closest_angle = min(choices, key=lambda pair: pair[1])
                if closest_angle > half_angle:
                    continue
                entry = 0.0 if choices[0][1] <= half_angle else brentq(
                    lambda fraction: angular_distance(fraction) - half_angle,
                    0, closest_fraction, xtol=1e-10)
                emission = dates[i] + (dates[i + 1] - dates[i]) * entry
                emission_epoch = times[i] + entry * (times[i + 1] - times[i])
                _, actual_travel_years = propagate_catalog_stars(directions[index], velocity[index], travel_years[index], emission_epoch, stellar_time_model)
                arrival = emission + timedelta(seconds=float(actual_travel_years) * JULIAN_YEAR_SECONDS)
                star = stars.iloc[index]
                records.append({
                    "spacecraft": spacecraft, "gaia_edr3_source_id": star.source_id,
                    "distance_pc": star.distance_pc, "ra_deg": star.ra, "dec_deg": star.dec,
                    "parallax_mas": star.parallax, "parallax_error_mas": star.parallax_error,
                    "gaia_g_abs_mag": star.phot_g_mean_mag + 5 * np.log10(star.parallax / 1000) + 5,
                    "gaia_bp_rp_mag": star.phot_bp_mean_mag - star.phot_rp_mean_mag,
                    "white_dwarf_probability": star.wd_prob,
                    "adopted_radial_velocity_km_s": star.adoptedrv,
                    "radial_velocity_assumed_zero": bool(pd.isna(star.adoptedrv)),
                    "model_first_emission_iso": emission.isoformat(timespec="seconds"),
                    "recalculated_arrival_iso": arrival.isoformat(timespec="seconds"),
                    "historical_model_emission": emission <= cutoff,
                    "full_beam_width_deg": full_width,
                    "stellar_time_model": stellar_time_model,
                    "outgoing_travel_years": float(actual_travel_years),
                    "minimum_angle_deg_on_entry_segment": np.rad2deg(closest_angle),
                    "ephemeris_segment_index": i,
                    "ephemeris_segment_start": dates[i].isoformat(timespec="seconds"),
                    "ephemeris_segment_end": dates[i + 1].isoformat(timespec="seconds"),
                    "transmission_evidence": "continuous-transmission assumption; not an operational log",
                })
                found.add(index)
        print(f"{spacecraft}: {len(found)} corrected geometric encounters; {len(track)} ephemeris points", flush=True)
    result = pd.DataFrame.from_records(records).sort_values("recalculated_arrival_iso")
    result.to_csv(directory / f"dsn_corrected_encounters{suffix}.csv", index=False)
    unique = result.drop_duplicates("gaia_edr3_source_id", keep="first")
    unique.to_csv(directory / f"dsn_corrected_unique_objects{suffix}.csv", index=False)
    return result


def summarize_dsn_variants(directory: str | Path, as_of: str = "2026-10-07") -> dict:
    """Save finite JSON summaries of every explicitly named geometric variant.

    Reports discrete unique-object arrivals, historical model emissions,
    missing radial velocities, and six-hour/refined membership agreement.
    All dates are nominal idealized-model outputs, not confirmed operational
    exposures. ``mixed_xband_linear_intersection`` is the most complete stellar
    and frequency scenario available here, but retains pointing/duty limits.
    """
    directory = Path(directory)
    cutoff = datetime.fromisoformat(as_of)
    horizons = {"as_of": cutoff, "next_day": cutoff + timedelta(days=1),
                "next_week": cutoff + timedelta(days=7),
                "next_calendar_year": cutoff.replace(year=cutoff.year + 1),
                "next_10_calendar_years": cutoff.replace(year=cutoff.year + 10),
                "next_100_calendar_years": cutoff.replace(year=cutoff.year + 100)}
    summary = {"as_of_utc": cutoff.isoformat(),
               "preferred_variant": "mixed_xband_linear_intersection",
               "scope": "idealized continuous geometric exposure; incoming observer directions; not operational logs",
               "variants": {}}
    for path in sorted(directory.glob("dsn_corrected_encounters_*.csv")):
        variant = path.stem.removeprefix("dsn_corrected_encounters_")
        events = pd.read_csv(path, dtype={"gaia_edr3_source_id": "string"})
        assert not events.duplicated(["spacecraft", "gaia_edr3_source_id"]).any()
        unique = events.sort_values("recalculated_arrival_iso").drop_duplicates("gaia_edr3_source_id")
        dates = [datetime.fromisoformat(date) for date in unique.recalculated_arrival_iso]
        reached = sum(date <= cutoff for date in dates)
        historical = unique.loc[unique.historical_model_emission].copy()
        historical_dates = [datetime.fromisoformat(date) for date in historical.recalculated_arrival_iso]
        historical_reached = sum(date <= cutoff for date in historical_dates)
        finite = unique.astype(object).where(pd.notna(unique), None)
        records = finite.to_dict("records")
        summary["variants"][variant] = {
            "events_csv": path.name, "unique_csv": path.name.replace("encounters", "unique_objects"),
            "star_beam_events": len(events), "unique_gaia_objects": len(unique),
            "per_spacecraft_events": events.spacecraft.value_counts().to_dict(),
            "historical_modeled_events": int(events.historical_model_emission.sum()),
            "historical_modeled_unique_objects": int(events.loc[events.historical_model_emission, "gaia_edr3_source_id"].nunique()),
            "missing_radial_velocity_unique_objects": int(unique.radial_velocity_assumed_zero.sum()),
            "reached_objects": [row for row, date in zip(records, dates) if date <= cutoff],
            "next_three_arrivals": [row for row, date in zip(records, dates) if date > cutoff][:3],
            "horizons": {label: {"end_date": date.date().isoformat(),
                                  "cumulative_count_scope": "all modeled first emissions, including future",
                                  "cumulative_unique_objects": sum(arrival <= date for arrival in dates),
                                  "new_unique_objects_after_as_of": sum(arrival <= date for arrival in dates) - reached,
                                  "historical_emission_cumulative_unique_objects": sum(arrival <= date for arrival in historical_dates),
                                  "historical_emission_new_unique_objects_after_as_of": sum(arrival <= date for arrival in historical_dates) - historical_reached}
                         for label, date in horizons.items()},
        }
    six_hour = pd.read_csv(directory / "dsn_corrected_encounters_fresh6h.csv", dtype={"gaia_edr3_source_id": "string"})
    adaptive = pd.read_csv(directory / "dsn_corrected_encounters_adaptive.csv", dtype={"gaia_edr3_source_id": "string"})
    columns = ["spacecraft", "gaia_edr3_source_id"]
    first_set = set(six_hour[columns].itertuples(index=False, name=None))
    second_set = set(adaptive[columns].itertuples(index=False, name=None))
    unit = np.array([1.0, 0.0, 0.0])
    still, duration = propagate_catalog_stars(unit, np.zeros(3), np.float64(10), 3.0, "linear_intersection")
    assert np.array_equal(still, unit) and duration == 10
    motion = np.array([0.0, 1e-5, 0.0])
    moved, duration = propagate_catalog_stars(unit, motion, np.float64(10), 0.0, "linear_intersection")
    assert np.isclose(np.linalg.norm(unit + motion * (10 + duration)), duration / 10)
    assert np.isclose(np.linalg.norm(moved), 1)
    summary["validation"] = {"fresh_6h_and_refined_membership_equal": first_set == second_set,
                             "membership_differences": len(first_set.symmetric_difference(second_set)),
                             "refinement_threshold_deg": 0.00128,
                             "refinement_interval_minutes": 15,
                             "stationary_star_and_moving_wavefront_equation_checks": "passed"}
    assert "mixed_xband_linear_intersection" in summary["variants"]
    if "mixed_xband_linear_intersection_extended" in summary["variants"]:
        summary["preferred_variant"] = "mixed_xband_linear_intersection_extended"
    (directory / "dsn_model_variants_summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    return summary


def extend_new_horizons_model(directory: str | Path) -> pd.DataFrame:
    """Add the saved 2025–2027 New Horizons trajectory to the central model.

    The other four missions' completed linear-intersection events are reused
    unchanged. New Horizons is recalculated over its entire concatenated track,
    rather than treating the extension as a new independent cone. Results keep
    a distinct ``extended`` filename; historical emission filtering still uses
    2026-10-07, so later forecast directions are not counted as already sent.
    """
    directory = Path(directory)
    original = pd.read_csv(directory / "horizons_adaptive/new_horizons/nh_ephemeris.csv")
    extension = pd.read_csv(directory / "direction_forecast/new_horizons_extension.csv")
    overlap = original.merge(extension, on="date", suffixes=("_old", "_new"))
    if len(overlap):
        assert np.allclose(overlap.ra_old, overlap.ra_new, atol=1e-8)
        assert np.allclose(overlap.dec_old, overlap.dec_new, atol=1e-8)
    combined = pd.concat([original, extension], ignore_index=True).drop_duplicates("date")
    combined["_time"] = pd.to_datetime(combined.date, format="%Y-%b-%d %H:%M:%S.%f")
    combined.sort_values("_time", inplace=True)
    combined.drop(columns="_time", inplace=True)
    target = directory / "horizons_extended/new_horizons/nh_ephemeris.csv"
    target.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(target, index=False)
    widths = {spacecraft: 0.128 for spacecraft in EPHEMERIDES}
    widths["New Horizons"] = 0.038
    new_horizons = match_corrected_dsn(directory, widths, suffix="_nh_extension_component",
                                     ephemeris_directory="horizons_extended",
                                     stellar_time_model="linear_intersection",
                                     selected_spacecraft=["New Horizons"])
    for kind in ["encounters", "unique_objects"]:
        (directory / f"dsn_corrected_{kind}_nh_extension_component.csv").replace(
            directory / f"nh_extended_{kind}_component.csv")
    central = pd.read_csv(directory / "dsn_corrected_encounters_mixed_xband_linear_intersection.csv",
                          dtype={"gaia_edr3_source_id": "string"})
    result = pd.concat([central.loc[central.spacecraft != "New Horizons"], new_horizons], ignore_index=True)
    result.sort_values("recalculated_arrival_iso", inplace=True)
    result.to_csv(directory / "dsn_corrected_encounters_mixed_xband_linear_intersection_extended.csv", index=False)
    result.drop_duplicates("gaia_edr3_source_id").to_csv(
        directory / "dsn_corrected_unique_objects_mixed_xband_linear_intersection_extended.csv", index=False)
    return result


def export_historical_dsn_pointings(directory: str | Path,
                                    as_of: str = "2026-10-07T00:00:00+00:00") -> dict:
    """Export dated, dense past tracks for a variable-width volume calculation.

    This reuses cached adaptive geocentric incoming directions and the existing
    New Horizons extension, with no network requests. Normalized Cartesian
    chords describe each adopted shortest great-circle arc. Additional points
    have linearly interpolated epochs, and their maximum angular step is
    checked against one quarter of the mission's nominal beam radius.
    Continuous transmission and a common volume origin remain model assumptions.
    The known Voyager 2 gap and gaps longer than six hours are never bridged.
    """
    directory = Path(directory)
    cutoff = pd.Timestamp(as_of)
    widths = {mission: (2.28 if mission == "New Horizons" else 7.68) for mission in EPHEMERIDES}
    destination = directory / "dsn_historical_dense_pointings.csv"
    fields = ["mission", "epoch_utc", "emission_utc", "ra_deg", "dec_deg", "ux", "uy", "uz",
              "beam_full_width_arcmin", "full_width_arcmin", "origin_x_pc", "origin_y_pc", "origin_z_pc",
              "parent_ephemeris_segment_index", "pointing_sample_basis", "transmission_evidence"]
    mission_summaries = []
    with destination.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for mission, relative_path in EPHEMERIDES.items():
            frame = pd.read_csv(directory / "horizons_adaptive" / relative_path)
            if mission == "New Horizons":
                frame = pd.concat([frame, pd.read_csv(directory / "direction_forecast/new_horizons_extension.csv")], ignore_index=True)
            frame["epoch"] = pd.to_datetime(frame.date, format="%Y-%b-%d %H:%M:%S.%f", utc=True)
            frame = frame.drop_duplicates("epoch").sort_values("epoch")
            frame = frame.loc[frame.epoch <= cutoff].copy()
            if mission == "Voyager 2":
                frame = frame.loc[~frame.epoch.between(pd.Timestamp("2020-03-09T00:00:00Z"), pd.Timestamp("2020-10-29T00:00:00Z"))]
            dates = list(frame.epoch)
            vectors = sky_vectors(frame.ra.to_numpy(), frame.dec.to_numpy())
            radius = np.deg2rad(widths[mission] / 120)
            maximum_step, exported, interpolated, unbridged_gaps = 0.0, 0, 0, 0
            for index, (epoch, vector) in enumerate(zip(dates, vectors, strict=True)):
                points = [(epoch, vector, "cached source epoch")]
                if index + 1 < len(dates):
                    next_epoch, next_vector = dates[index + 1], vectors[index + 1]
                    angle = float(np.arctan2(np.linalg.norm(np.cross(vector, next_vector)), np.dot(vector, next_vector)))
                    if (next_epoch - epoch).total_seconds() <= 6 * 3600:
                        steps = max(1, int(np.ceil(1.01 * angle / (radius / 4))))
                        fraction = np.arange(steps + 1, dtype=float)[:, None] / steps
                        arc = vector * (1 - fraction) + next_vector * fraction
                        arc /= np.linalg.norm(arc, axis=1)[:, None]
                        adjacent = np.arctan2(np.linalg.norm(np.cross(arc[:-1], arc[1:]), axis=1),
                                              np.sum(arc[:-1] * arc[1:], axis=1))
                        maximum_step = max(maximum_step, float(adjacent.max()))
                        assert adjacent.max() <= radius / 4 + 1e-12, (mission, index, adjacent.max(), radius / 4)
                        points.extend((epoch + (next_epoch - epoch) * (step / steps), arc[step],
                                       "normalized-chord interpolation of cached track") for step in range(1, steps))
                        interpolated += steps - 1
                    else:
                        unbridged_gaps += 1
                for sample_epoch, sample_vector, basis in points:
                    writer.writerow({"mission": mission, "epoch_utc": sample_epoch.isoformat(),
                                     "emission_utc": sample_epoch.isoformat(),
                                     "ra_deg": np.rad2deg(np.arctan2(sample_vector[1], sample_vector[0])) % 360,
                                     "dec_deg": np.rad2deg(np.arcsin(sample_vector[2])),
                                     "ux": sample_vector[0], "uy": sample_vector[1], "uz": sample_vector[2],
                                     "beam_full_width_arcmin": widths[mission], "full_width_arcmin": widths[mission],
                                     "origin_x_pc": 0, "origin_y_pc": 0, "origin_z_pc": 0,
                                     "parent_ephemeris_segment_index": index, "pointing_sample_basis": basis,
                                     "transmission_evidence": "continuous-transmission model; geocentric incoming direction; common volume origin"})
                    exported += 1
            mission_summaries.append({"mission": mission, "full_beam_width_arcmin": widths[mission],
                                      "cached_source_points": len(frame), "exported_points": exported,
                                      "interpolated_points": interpolated,
                                      "maximum_adjacent_step_arcsec": np.rad2deg(maximum_step) * 3600,
                                      "spacing_limit_arcsec": np.rad2deg(radius / 4) * 3600,
                                      "unbridged_time_gaps": unbridged_gaps,
                                      "first_epoch": dates[0].isoformat(), "last_epoch": dates[-1].isoformat()})
    summary = {"as_of_iso": as_of, "output_csv": str(destination), "missions": mission_summaries,
               "total_exported_points": sum(row["exported_points"] for row in mission_summaries),
               "scope": "all five adopted historical DSN tracks; nominal continuous transmission; native mission widths"}
    (directory / "dsn_historical_dense_pointings_summary.json").write_text(json.dumps(summary, indent=2))
    return summary
