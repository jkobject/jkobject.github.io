"""Combined beam-volume projections and explicit historical extrapolation."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import json
import math
import hashlib

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

from analysis import ROOT, AS_OF, LY_PER_PC, DAYS_PER_YEAR, sample_beam_union, union_expectation


def first_emission_on_rays(pointings, rays):
    """Find earliest dated disks containing each unit sky direction.

    Each pointing carries its own full width. A spatial index supplies only
    candidates; exact chord distances test the individual half-widths. Return
    nanosecond first-emission epochs and a hit mask. Unhit sentinel epochs must
    never be interpreted as future emissions.
    """
    ra, dec = np.deg2rad(pointings[["ra_deg", "dec_deg"]].to_numpy()).T
    centers = np.column_stack([np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)])
    chords = 2*np.sin(np.deg2rad(pointings.beam_full_width_arcmin.to_numpy()/120)/2)
    epochs = pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).astype("int64").to_numpy()
    groups = []
    for chord in np.unique(chords):
        members = np.flatnonzero(chords == chord)
        groups.append((members, cKDTree(centers[members]), float(chord)))
    first = np.full(len(rays), np.iinfo(np.int64).max, dtype=np.int64)
    for start in range(0, len(rays), 1000):
        for members, tree, chord in groups:
            candidates = tree.query_ball_point(rays[start:start+1000], chord*(1+1e-9))
            for index, neighbors in enumerate(candidates, start):
                if neighbors:
                    first[index] = min(first[index], epochs[members[neighbors]].min())
    return first, first != np.iinfo(np.int64).max


def build_combined_inventory(samples=120000, seed=31):
    """Integrate all recovered/modelled source families into one dated union.

    Repeated angular coverage contributes once, using its earliest emission.
    The primary output is a population volume projection, not observed planets.
    DSN assumes continuous uplinks; intentional widths include explicit models.
    Both the full inventory and the DSN/message backbone are saved, allowing a
    separate radar-history model to replace the incomplete radar inventory.
    """
    columns = ["emission_utc", "ra_deg", "dec_deg", "beam_full_width_arcmin"]
    dsn = pd.read_csv(ROOT/"data/dsn/dsn_historical_dense_pointings.csv", usecols=columns)
    intentional = pd.read_csv(ROOT/"data/intentional/intentional_nominal_pointings.csv", usecols=columns)
    backbone_points = pd.concat([dsn.assign(source_family="DSN"), intentional.assign(source_family="Intentional")], ignore_index=True)
    radar_manifest = json.loads((ROOT/"data/radar/bulk_beams/reconstruction_summary.json").read_text())
    assert radar_manifest["reconstructed_runs"] == 74201 and len(radar_manifest["reconstructed_targets"]) == 762
    assert not radar_manifest["failed_targets"]
    frames = [backbone_points]
    for target in radar_manifest["reconstructed_targets"]:
        frame = pd.read_csv(ROOT/target["output_csv"], usecols=["epoch_utc", "ra_deg", "dec_deg", "beam_full_width_arcmin"])
        assert len(frame) == target["direction_samples"]
        frames.append(frame.rename(columns={"epoch_utc": "emission_utc"}).assign(source_family="Arecibo"))
    goldstone = pd.read_csv(ROOT/"data/radar/goldstone_pointings.csv", usecols=["emission_utc", "ra_deg", "dec_deg"])
    frames.append(goldstone.assign(beam_full_width_arcmin=1.92, source_family="Goldstone"))
    pointings = pd.concat(frames, ignore_index=True).drop_duplicates(subset=columns)
    assert pd.to_datetime(pointings.emission_utc, format="ISO8601", utc=True).max() <= AS_OF
    pointings.to_csv(ROOT/"data/combined_pointings.csv", index=False)
    backbone_points.to_csv(ROOT/"data/combined_backbone_pointings.csv", index=False)
    parameters = json.loads((ROOT/"data/population_parameters.json").read_text())
    occurrence = json.loads((ROOT/"data/radar/cassan_2012_planet_occurrence.json").read_text())
    unions, forecasts = {}, {}
    for label, subset in [("recovered", pointings), ("backbone", backbone_points)]:
        union = sample_beam_union(subset, samples=samples, seed=seed)
        np.savez_compressed(ROOT/"results"/f"combined_{label}_union_samples.npz", **union)
        rows = []
        for year in range(1960, 2327):
            row = union_expectation(union, datetime(year, 10, 7, tzinfo=timezone.utc), parameters["stellar_density_pc3"], parameters["mixed_hz_planets_per_star"])
            row["bounded_reference_planets_expected"] = row["stars_expected"]*occurrence["reference_mean_planets_per_star"]
            row["average_volume_per_2arcmin_equivalent_ly3"] = row["volume_ly3"]/row["equivalent_beam_disks"] if row["equivalent_beam_disks"] else 0
            rows.append(row)
        pd.DataFrame(rows).to_csv(ROOT/"results"/f"combined_{label}_timeline.csv", index=False)
        unions[label] = union
        forecasts[label] = rows
    # Choose the ecliptic-band half-width from95% of recovered Arecibo union area.
    radar_union = np.load(ROOT/"results/arecibo_archive_union_samples.npz")
    epsilon = math.radians(23.4392911)
    rays = radar_union["sampled_directions"]
    latitude = np.rad2deg(np.arcsin(np.clip(rays[:, 2]*math.cos(epsilon)-rays[:, 1]*math.sin(epsilon), -1, 1)))
    order = np.argsort(np.abs(latitude))
    weights = radar_union["weights_sr"][order]
    band = float(np.abs(latitude)[order][np.searchsorted(np.cumsum(weights), .95*weights.sum())])
    summary = {"as_of": AS_OF.isoformat(), "samples": samples, "seed": seed,
               "source_pointings": pointings.source_family.value_counts().to_dict(),
               "ecliptic_band_half_width_95pct_deg": band,
               "reference_planets_per_ordinary_star": 1.6,
               "reference_planet_definition": "5 Earth masses–10 Jupiter masses,0.5–10 AU; K/M-derived calibration transferred to ordinary stars",
               "current_recovered_projection": forecasts["recovered"][2026-1960],
               "current_backbone_projection": forecasts["backbone"][2026-1960],
               "scope": "combined volume-density projection; targeted known-host counts remain a separate conditional estimator"}
    (ROOT/"results/combined_inventory_summary.json").write_text(json.dumps(summary, indent=2))
    return summary


def extrapolate_radar_history(multipliers=(0.5, 1.0, 2.0), quadrature_order=16):
    """Project dated first coverage from the calibrated annual radar history.

    Parameters
    ----------
    multipliers : tuple of float
        Explicit transfer scenarios for area per detected target apparition.
        These are not confidence limits or bounds on omitted transmitters.
    quadrature_order : int
        Gauss--Legendre nodes per calendar-year interval. The model preserves
        exponential survival inside each interval, rather than putting every
        transmission at one arbitrary date.

    Returns
    -------
    dict
        Current estimates, exact horizon differences, and model assumptions.

    Notes
    -----
    Radar rays are distributed uniformly in the empirical95%-coverage ecliptic
    band. Each ray receives a Poisson first-coverage hazard g(year)/band_area.
    Recovered radar geometry is replaced by this scenario; DSN and intentional
    message geometry is retained. Their overlap is subtracted with the saved
    cap-mixture weights. No transmissions after the cutoff are introduced.
    Unknown interior years are linearly interpolated, with no pre-first-record
    activity assumed. All imputation is saved separately for review.
    """
    inventory = json.loads((ROOT/"results/combined_inventory_summary.json").read_text())
    params = json.loads((ROOT/"data/population_parameters.json").read_text())
    occurrence = json.loads((ROOT/"data/radar/cassan_2012_planet_occurrence.json").read_text())
    reference_mean = occurrence["reference_mean_planets_per_star"]
    schedule = pd.read_csv(ROOT/"results/radar_activity_schedule.csv")
    filled = []
    for family in ["Arecibo", "Goldstone"]:
        rows = schedule.loc[schedule.transmitter_family == family].sort_values("year").copy()
        original = rows.modeled_angular_area_sr.copy()
        rows["scenario_area_sr"] = original.interpolate(limit_area="inside").fillna(0)
        rows["gap_filled"] = original.isna() & (rows.scenario_area_sr > 0)
        filled.append(rows[["year", "transmitter_family", "status", "modeled_angular_area_sr", "scenario_area_sr", "gap_filled"]])
    filled = pd.concat(filled, ignore_index=True)
    filled.to_csv(ROOT/"results/global_activity_gapfill.csv", index=False)
    annual = filled.groupby("year").scenario_area_sr.sum()
    band_half_width = inventory["ecliptic_band_half_width_95pct_deg"]
    band_area = 4*math.pi*math.sin(math.radians(band_half_width))
    union = dict(np.load(ROOT/"results/combined_backbone_union_samples.npz"))
    rays = union["sampled_directions"]
    epsilon = math.radians(23.4392911)
    latitude_sine = rays[:, 2]*math.cos(epsilon)-rays[:, 1]*math.sin(epsilon)
    in_band = np.abs(latitude_sine) <= math.sin(math.radians(band_half_width))
    weights = union["weights_sr"][in_band]
    epochs_years = union["first_epoch_ns"][in_band]/1e9/(DAYS_PER_YEAR*86400)
    one_disk = 2*math.pi*(1-math.cos(math.radians(1/60)))
    star_density = params["stellar_density_pc3"]/LY_PER_PC**3
    hz_density = star_density*params["mixed_hz_planets_per_star"]
    empty_radius = 4.24
    nodes, gauss_weights = np.polynomial.legendre.leggauss(quadrature_order)
    readouts = [datetime(year, 10, 7, tzinfo=timezone.utc) for year in range(1960, 2327)]
    horizons = [("day", AS_OF+timedelta(days=1)), ("week", AS_OF+timedelta(days=7)),
                ("year", datetime(2027, 10, 7, tzinfo=timezone.utc))]
    dates = sorted(set(readouts+[date for _, date in horizons]))
    all_rows = []
    for multiplier in multipliers:
        scenario_rows = []
        for date in dates:
            base = union_expectation(union, date, params["stellar_density_pc3"], params["mixed_hz_planets_per_star"])
            observation = date.timestamp()/(DAYS_PER_YEAR*86400)
            ages = np.maximum(observation-epochs_years, 0)
            backbone_front_volume = np.maximum(ages**3-empty_radius**3, 0)/3
            order = np.argsort(backbone_front_volume)
            sorted_volumes, sorted_weights = backbone_front_volume[order], weights[order]
            cumulative_weights = np.r_[0, np.cumsum(sorted_weights)]
            cumulative_volume = np.r_[0, np.cumsum(sorted_weights*sorted_volumes)]
            # The importance estimate uses total sample count, not band count.
            backbone_band_area = float(weights[epochs_years <= observation].sum()/len(rays))
            survival, radar_volume, overlap_volume = 1.0, 0.0, 0.0
            for year, area_budget in annual.items():
                start = datetime(int(year), 1, 1, tzinfo=timezone.utc)
                end = min(datetime(int(year)+1, 1, 1, tzinfo=timezone.utc), AS_OF)
                observed_end = min(end, date)
                if observed_end <= start or area_budget == 0:
                    continue
                duration = (end-start).total_seconds()/(DAYS_PER_YEAR*86400)
                elapsed = (observed_end-start).total_seconds()/(DAYS_PER_YEAR*86400)
                hazard = multiplier*area_budget/band_area/duration
                offsets = (nodes+1)*elapsed/2
                emission_epochs = start.timestamp()/(DAYS_PER_YEAR*86400)+offsets
                probability_weights = gauss_weights*elapsed/2*hazard*survival*np.exp(-hazard*offsets)
                volumes = np.maximum(np.maximum(observation-emission_epochs, 0)**3-empty_radius**3, 0)/3
                radar_volume += band_area*float(probability_weights@volumes)
                indices = np.searchsorted(sorted_volumes, volumes, side="right")
                overlap = (cumulative_volume[indices]+volumes*(cumulative_weights[-1]-cumulative_weights[indices]))/len(rays)
                overlap_volume += float(probability_weights@overlap)
                survival *= math.exp(-hazard*elapsed)
            probability = 1-survival
            volume = base["volume_ly3"]+radar_volume-overlap_volume
            coverage = base["coverage_sr"]+probability*(band_area-backbone_band_area)
            scenario_rows.append({"date_utc": date.isoformat(), "radar_area_multiplier": multiplier,
                                  "volume_ly3": volume, "backbone_volume_ly3": base["volume_ly3"],
                                  "radar_only_volume_ly3": radar_volume, "overlap_volume_ly3": overlap_volume,
                                  "stars_expected": volume*star_density, "hz_planets_expected": volume*hz_density,
                                  "bounded_reference_planets_expected": volume*star_density*reference_mean,
                                  "coverage_sr": coverage, "radar_first_coverage_probability": probability,
                                  "equivalent_beam_disks": coverage/one_disk,
                                  "average_volume_per_2arcmin_equivalent_ly3": volume/(coverage/one_disk) if coverage else 0})
        all_rows.extend(scenario_rows)
    result = pd.DataFrame(all_rows)
    assert (result.volume_ly3 >= result.backbone_volume_ly3-1e-8).all()
    assert (result.overlap_volume_ly3 <= result.radar_only_volume_ly3+1e-8).all()
    result.to_csv(ROOT/"results/global_extrapolated_timeline.csv", index=False)
    current = result.loc[result.date_utc == AS_OF.isoformat()].to_dict("records")
    forecasts = []
    for row in current:
        for label, date in horizons:
            future = result.loc[(result.radar_area_multiplier == row["radar_area_multiplier"]) & (result.date_utc == date.isoformat())].iloc[0]
            forecasts.append({"interval": label, "end_date_utc": date.isoformat(), "radar_area_multiplier": row["radar_area_multiplier"],
                              "new_hz_planets_expected": future.hz_planets_expected-row["hz_planets_expected"],
                              "new_bounded_reference_planets_expected": future.bounded_reference_planets_expected-row["bounded_reference_planets_expected"]})
    pd.DataFrame(forecasts).to_csv(ROOT/"results/global_arrival_rates.csv", index=False)
    # Observed-proxy2025 is a historical benchmark, not current2026 operations.
    budget_2025 = annual.loc[2025]
    benchmark = []
    for row in current:
        prior = result.loc[(result.radar_area_multiplier == row["radar_area_multiplier"]) & (result.date_utc == datetime(2025, 10, 7, tzinfo=timezone.utc).isoformat())].iloc[0]
        new_disks = row["equivalent_beam_disks"]-prior.equivalent_beam_disks
        benchmark.append({"radar_area_multiplier": row["radar_area_multiplier"], "combined_new_2arcmin_equivalents_last_calendar_year": new_disks,
                          "combined_new_equivalents_per_day_last_year": new_disks/365,
                          "radar_2025_budget_2arcmin_equivalents": row["radar_area_multiplier"]*budget_2025/one_disk})
    files = ["data/population_parameters.json", "data/radar/cassan_2012_planet_occurrence.json", "data/radar/bulk_beams/reconstruction_summary.json",
             "data/combined_pointings.csv", "data/combined_backbone_pointings.csv", "results/combined_inventory_summary.json",
             "results/combined_backbone_union_samples.npz", "results/combined_recovered_union_samples.npz",
             "results/radar_activity_schedule.csv", "results/radar_activity_calibration.json", "results/global_activity_gapfill.csv",
             "results/global_extrapolated_timeline.csv", "results/global_arrival_rates.csv", "combined_model.py"]
    summary = {"as_of": AS_OF.isoformat(), "band_half_width_deg": band_half_width, "band_area_sr": band_area,
               "quadrature_order": quadrature_order, "current_scenarios": current, "arrival_forecasts": forecasts, "direction_benchmarks": benchmark,
               "scope": "historical asteroid-radar proxy replacement plus modeled DSN/selected intentional beams; not an exhaustive global transmitter census",
               "unknown_year_rule": "linear interpolation only between first/last recorded activity; zero before first record; retirement zero retained",
               "within_year_rule": "constant annual first-coverage hazard; partial2026 budget distributed only through cutoff",
               "future_rule": "propagate only emissions no later than cutoff; no new future directions",
               "uncertainty": "0.5/1/2 area transfer scenarios do not bound omitted radar classes, historical beam changes, targeted-host bias or occurrence transfer",
               "input_output_sha256": {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in files}}
    (ROOT/"results/global_extrapolation_summary.json").write_text(json.dumps(summary, indent=2))
    return summary
