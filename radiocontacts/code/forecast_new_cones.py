"""Separate hypothetical future radar directions; no observed forecast."""

import csv
import hashlib
import json
import math
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np


def forecast_new_cones(study_directory: str | Path | None = None) -> dict:
    """Save future first-coverage areas and volumes for a resumed radar scenario.

    Goldstone hypothetically resumes on 2028-05-01 at its calibrated 2025
    angular-area budget, multiplied by 0.5/1/2. Directions are uniform in the
    frozen empirical ecliptic band. Only sky unilluminated in the central
    cutoff model contributes: initial available area is (B - backbone) *
    (1 - historical radar coverage probability). The first-coverage hazard is
    budget/B, so repeated future pointings cannot repeatedly count that area.

    Volumes propagate at one light-year per Julian year outside the adopted
    empty 4.24 light-year sphere. They are swept volumes, not simultaneous
    illumination. A 2-arcmin equivalent is an angular-area unit, not a measured
    number of individual transmitter cones. Density-based population counts
    and the transferred activity budget remain conditional projections.
    """
    root = Path(study_directory or Path(__file__).resolve().parent).resolve()
    inputs = [root / name for name in (
        "results/global_extrapolation_summary.json",
        "results/combined_backbone_union_samples.npz",
        "results/radar_activity_schedule.csv",
        "data/population_parameters.json",
        "data/radar/cassan_2012_planet_occurrence.json")]
    frozen = json.loads(inputs[0].read_text())
    parameters = json.loads(inputs[3].read_text())
    occurrence = json.loads(inputs[4].read_text())
    central = next(row for row in frozen["current_scenarios"]
                   if row["radar_area_multiplier"] == 1.0)
    band_area = float(frozen["band_area_sr"])
    half_band = math.radians(frozen["band_half_width_deg"])
    current_radar_probability = float(central["radar_first_coverage_probability"])
    cutoff = datetime.fromisoformat(frozen["as_of"])
    resume = datetime.fromisoformat("2028-05-01T00:00:00+00:00")
    assert resume > cutoff and 0 <= current_radar_probability <= 1
    assert math.isclose(band_area, 4 * math.pi * math.sin(half_band), rel_tol=1e-12)

    with np.load(inputs[1]) as backbone:
        rays = backbone["sampled_directions"]
        weights = backbone["weights_sr"]
        epoch_ns = backbone["first_epoch_ns"]
        obliquity = math.radians(23.4392911)
        latitude_sine = rays[:, 2] * math.cos(obliquity) - rays[:, 1] * math.sin(obliquity)
        in_band = np.abs(latitude_sine) <= math.sin(half_band)
        emitted = epoch_ns <= round(cutoff.timestamp() * 1e9)
        # Importance weights must be divided by ALL sampled rays, not band rays.
        backbone_band_area = float(weights[in_band & emitted].sum() / len(rays))
    available_area = (band_area - backbone_band_area) * (1 - current_radar_probability)
    assert 0 < available_area <= band_area

    with inputs[2].open(newline="") as handle:
        activity = list(csv.DictReader(handle))
    goldstone = next(row for row in activity
                     if row["year"] == "2025" and row["transmitter_family"] == "Goldstone")
    annual_budget = float(goldstone["modeled_angular_area_sr"])
    assert math.isclose(annual_budget, 0.000886820298, rel_tol=1e-8)
    days_per_year, inner_radius_ly = 365.25, 4.24
    reference_disk_sr = 4 * math.pi * math.sin(math.radians(1 / 60) / 2) ** 2
    stellar_density_ly3 = parameters["stellar_density_pc3"] / 3.2615637771674333 ** 3
    hz_density_ly3 = parameters["hz_planets_density_pc3"] / 3.2615637771674333 ** 3
    reference_mean = occurrence["reference_mean_planets_per_star"]
    elapsed = np.array([0.0, 1.0, inner_radius_ly, 10.0, 50.0, 100.0])
    rows, scenario_summaries = [], []
    maximum_quadrature_difference = 0.0
    for multiplier in (0.5, 1.0, 2.0):
        budget = annual_budget * multiplier
        hazard = budget / band_area
        areas = available_area * (-np.expm1(-hazard * elapsed))
        area_rates = available_area * hazard * np.exp(-hazard * elapsed)
        volumes_by_order = {}
        upper = np.maximum(elapsed - inner_radius_ly, 0)
        for order in (32, 64):
            nodes, gauss_weights = np.polynomial.legendre.leggauss(order)
            emission_ages = upper[:, None] * (nodes[None, :] + 1) / 2
            radii = elapsed[:, None] - emission_ages
            shells = np.maximum(radii ** 3 - inner_radius_ly ** 3, 0) / 3
            integrands = hazard * np.exp(-hazard * emission_ages) * shells
            volumes_by_order[order] = available_area * upper / 2 * (integrands @ gauss_weights)
        volumes = volumes_by_order[64]
        difference = np.abs(volumes_by_order[32] - volumes)
        maximum_quadrature_difference = max(maximum_quadrature_difference, float(difference.max()))
        assert np.allclose(volumes_by_order[32], volumes, rtol=1e-11, atol=1e-12)
        assert areas[0] == 0 and np.all(volumes[elapsed <= inner_radius_ly] == 0)
        assert np.all(np.diff(areas) >= 0) and np.all(areas < available_area)
        assert np.all(np.diff(area_rates) <= 0) and np.all(np.diff(volumes) >= 0)
        saturated_area = available_area * (-math.expm1(-50.0))
        assert math.isclose(saturated_area, available_area, rel_tol=1e-12)
        for i, years in enumerate(elapsed):
            if years not in (1, 10, 50, 100):
                continue
            equivalents = float(areas[i] / reference_disk_sr)
            volume = float(volumes[i])
            rows.append({
                "scenario": "hypothetical Goldstone resume; constant calibrated 2025 activity",
                "hypothetical_resume_utc": resume.isoformat(),
                "elapsed_julian_years": float(years),
                "observation_utc": (resume + timedelta(days=float(years) * days_per_year)).isoformat(),
                "future_area_transfer_multiplier": multiplier,
                "future_angular_area_budget_sr_per_year": budget,
                "initial_unilluminated_area_sr": available_area,
                "first_coverage_hazard_per_year": hazard,
                "new_unique_area_sr": float(areas[i]),
                "new_2arcmin_equivalent_directions": equivalents,
                "new_unique_area_sr_per_year": float(area_rates[i]),
                "new_2arcmin_equivalents_per_year": float(area_rates[i] / reference_disk_sr),
                "new_2arcmin_equivalents_per_day": float(area_rates[i] / reference_disk_sr / days_per_year),
                "new_swept_volume_ly3": volume,
                "average_volume_per_new_2arcmin_equivalent_ly3": volume / equivalents,
                "stars_expected": volume * stellar_density_ly3,
                "bounded_reference_planets_expected": volume * stellar_density_ly3 * reference_mean,
                "hz_planets_expected": volume * hz_density_ly3,
                "volume_quadrature_32_vs_64_absolute_difference_ly3": float(difference[i])})
        scenario_summaries.append({
            "future_area_transfer_multiplier": multiplier,
            "first_coverage_hazard_per_year": hazard,
            "initial_new_2arcmin_equivalents_per_year": available_area * hazard / reference_disk_sr,
            "asymptotic_unique_area_sr": available_area,
            "asymptotic_2arcmin_equivalent_directions": available_area / reference_disk_sr})

    results = root / "results"
    results.mkdir(exist_ok=True)
    output = results / "future_new_cones_scenario.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "output_csv": str(output.relative_to(root)), "cutoff_utc": cutoff.isoformat(),
        "hypothetical_resume_utc": resume.isoformat(), "goldstone_activity_reference_year": 2025,
        "central_goldstone_angular_area_budget_sr_per_year": annual_budget,
        "band_area_sr": band_area, "band_half_width_deg": frozen["band_half_width_deg"],
        "backbone_angular_area_within_band_sr": backbone_band_area,
        "central_historical_radar_coverage_probability": current_radar_probability,
        "initial_unilluminated_area_sr": available_area,
        "reference_full_beam_width_arcmin": 2.0, "reference_disk_sr": reference_disk_sr,
        "empty_inner_radius_ly": inner_radius_ly, "days_per_julian_year": days_per_year,
        "rows": len(rows), "scenarios": scenario_summaries,
        "volume_rule": "A integral_0^max(t-4.24,0) lambda exp(-lambda*s) ((t-s)^3-4.24^3)/3 ds",
        "quadrature_orders_compared": [32, 64],
        "maximum_quadrature_absolute_difference_ly3": maximum_quadrature_difference,
        "validation": "Zero initial area; zero volume through4.24years; increasing area/volume, decreasing new-area rate, asymptotic area=A; 32/64 quadrature agreement.",
        "scope": "Scenario only, not observed operational forecast. Central historical cutoff coverage fixed; future transfer sensitivity varies only Goldstone activity. No other future emissions.",
        "no_double_count_rule": "Count only area unilluminated in the central cutoff model, disjoint from the already-emitted union; repeat future directions contribute only once.",
        "population_caveat": "Homogeneous local density transfer; bounded reference planets use finite Cassan mass/orbit population, HZ means small planets in model habitable zones. These are expectations, not measured planets or proof of habitability/detectability.",
        "input_sha256": {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in inputs}}
    (results / "future_new_cones_scenario_summary.json").write_text(json.dumps(summary, indent=2))
    return summary
