"""Nominal moving-star cross-match for the two exact-timestamp radar cases."""

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


def match_arecibo_gcns(directory: str | Path, gcns_path: str | Path,
                       as_of_utc: str = "2026-10-07T00:00:00+00:00",
                       account_stellar_catalog_light_time: bool = True) -> dict:
    """Match the DP107 transmit tracks against median-distance GCNS sources.

    Gaia position, proper motion and available adopted radial velocity are
    modeled as rectilinear Cartesian motion. The catalogue's J2016 astrometric
    direction refers to a stellar emission epoch earlier by distance/c;
    by default the physical star is advanced from that epoch to J2016. Missing radial
    velocities are explicitly approximated as zero and reported. For each
    emission time, the positive solution of ``|r + v*tau| = c*tau`` gives
    the stellar reception time/direction. Beam origins use Arecibo's barycentric
    location reconstructed from the cached JPL asteroid vectors. Median GCNS
    distances above 100 pc are excluded and counted. No star-completeness claim
    follows from this catalogue match.

    A 30-arcsec enlarged candidate search surrounds the 1-arcmin-radius beam;
    every candidate is checked again against the actual 1-arcmin angular cut.
    Samples occur only inside actual txup/txdown windows. Continuous motion
    between finite samples and historical pointing errors remain limitations.
    """
    directory = Path(directory)
    stars = pd.read_csv(gcns_path, dtype={"source_id": "string"})
    assert stars["source_id"].is_unique
    required = ["ra", "dec", "dist_50", "pmra", "pmdec"]
    assert stars[required].notna().all().all(), stars[required].isna().sum()
    original_count = len(stars)
    stars = stars.loc[stars.dist_50.between(0, 0.1, inclusive="right")].copy()
    assert (stars.dist_50 > 0).all()
    ra, dec = np.deg2rad(stars.ra.to_numpy()), np.deg2rad(stars.dec.to_numpy())
    radius = stars.dist_50.to_numpy() * 1000
    direction = np.column_stack([np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)])
    east = np.column_stack([-np.sin(ra), np.cos(ra), np.zeros(len(ra))])
    north = np.column_stack([-np.cos(ra)*np.sin(dec), -np.sin(ra)*np.sin(dec), np.cos(dec)])
    mas_to_rad = np.deg2rad(1/3600000)
    rv = stars.adoptedrv.fillna(0).to_numpy()
    velocity = radius[:, None] * mas_to_rad * (stars.pmra.to_numpy()[:, None]*east + stars.pmdec.to_numpy()[:, None]*north)
    if account_stellar_catalog_light_time:
        # Observed proper motion uses reception-time increments. Stellar
        # emission-time increments differ by the first-order factor 1+vr/c.
        velocity *= (1 + rv/299792.458)[:, None]
    velocity += rv[:, None] * 1.022712165045695e-6 * direction
    position = radius[:, None] * direction
    light_pc_per_year = 0.30660139378555056
    if account_stellar_catalog_light_time:
        position += velocity * (radius/light_pc_per_year)[:, None]
    a = light_pc_per_year**2 - (velocity**2).sum(axis=1)
    assert (a > 0).all()
    as_of = datetime.fromisoformat(as_of_utc)
    assert as_of.tzinfo is not None
    as_of_year = 2000 + ((as_of.timestamp()/86400+2440587.5)-2451545.0)/365.25
    with (directory / "arecibo_direction_samples.csv").open() as handle:
        pointings = list(csv.DictReader(handle))
    matches, nearest = [], []
    checked_candidates = 0
    half_width = np.deg2rad(1/60)
    for year in [2008, 2016]:
        samples = [row for row in pointings if row["epoch_utc"].startswith(str(year))]
        epochs = sorted({datetime.fromisoformat(row["epoch_utc"]) for row in samples})
        epoch_lookup = {epoch: index for index, epoch in enumerate(epochs)}
        epoch_years = np.array([2000 + ((epoch.timestamp()/86400+2440587.5)-2451545.0)/365.25 for epoch in epochs])
        relative_body = json.loads((directory / f"horizons_DP107_{year}_arecibo_relative.json").read_text())["result"]
        absolute_body = json.loads((directory / f"horizons_DP107_{year}_barycentric.json").read_text())["result"]
        relative = np.array([[float(value) for value in row[2:8]] for row in csv.reader(relative_body.split("$$SOE\n")[1].split("$$EOE")[0].splitlines()) if row])
        absolute = np.array([[float(value) for value in row[2:8]] for row in csv.reader(absolute_body.split("$$SOE\n")[1].split("$$EOE")[0].splitlines()) if row])
        assert relative.shape == absolute.shape == (len(epochs), 6)
        origins = (absolute[:, :3] - relative[:, :3]) / 3.0856775814913673e13
        midpoint_year = float(epoch_years.mean())
        at_emission = position + velocity * (midpoint_year - 2016)
        b = (at_emission * velocity).sum(axis=1)
        tau = (b + np.sqrt(b*b + a*(at_emission**2).sum(axis=1))) / a
        at_reception = at_emission + velocity*tau[:, None]
        midpoint_directions = at_reception / np.linalg.norm(at_reception, axis=1)[:, None]
        tree = cKDTree(midpoint_directions)
        max_pm_time_arcsec = float(np.hypot(stars.pmra,stars.pmdec).max()/1000 * (epoch_years.max()-epoch_years.min()))
        max_origin_arcsec = float(np.linalg.norm(origins,axis=1).max()/radius.min()*206264.806247)
        assert max_pm_time_arcsec + max_origin_arcsec < 30, (max_pm_time_arcsec,max_origin_arcsec)
        candidate_chord = 2*np.sin((half_width+np.deg2rad(30/3600))/2)
        for row in samples:
            index = epoch_lookup[datetime.fromisoformat(row["epoch_utc"])]
            emit_year = epoch_years[index]
            beam = np.array([float(row[key]) for key in ["ux", "uy", "uz"]])
            candidate_ids = np.array(tree.query_ball_point(beam, candidate_chord), dtype=int)
            checked_candidates += len(candidate_ids)
            # The nearest-source diagnostic is broad enough to show the
            # current-front null is separated from the beam by many degrees.
            already_reached = tau + midpoint_year <= as_of_year
            current_ids = np.where(already_reached)[0]
            if len(current_ids):
                dot = midpoint_directions[current_ids] @ beam
                closest_id = current_ids[int(dot.argmax())]
                nearest.append({"apparition": year, "emission_utc": row["epoch_utc"],
                                "source_id": str(stars.iloc[closest_id].source_id),
                                "distance_pc": float(radius[closest_id]),
                                "separation_deg": float(np.rad2deg(np.arccos(np.clip(dot.max(),-1,1))))})
            if not len(candidate_ids):
                continue
            r = position[candidate_ids] + velocity[candidate_ids]*(emit_year-2016) - origins[index]
            v = velocity[candidate_ids]
            aa = a[candidate_ids]
            bb = (r*v).sum(axis=1)
            flight = (bb + np.sqrt(bb*bb + aa*(r*r).sum(axis=1))) / aa
            reception_r = r + v*flight[:, None]
            incoming_directions = reception_r / np.linalg.norm(reception_r,axis=1)[:, None]
            separation = np.arccos(np.clip(incoming_directions @ beam,-1,1))
            selected = np.where(separation <= half_width)[0]
            for chosen in selected:
                star_index = candidate_ids[chosen]
                reception_year = emit_year+float(flight[chosen])
                matches.append({"apparition": year, "interval_id": row["interval_id"],
                                "emission_utc": row["epoch_utc"],
                                "source_id": str(stars.iloc[star_index].source_id),
                                "catalog_distance_pc": float(radius[star_index]),
                                "reception_julian_year": reception_year,
                                "separation_arcsec": float(separation[chosen]*206264.806247),
                                "reached_by_as_of": reception_year <= as_of_year,
                                "missing_radial_velocity": bool(pd.isna(stars.iloc[star_index].adoptedrv)),
                                "wd_prob": float(stars.iloc[star_index].wd_prob)})
    columns = ["apparition","interval_id","emission_utc","source_id","catalog_distance_pc","reception_julian_year","separation_arcsec","reached_by_as_of","missing_radial_velocity","wd_prob"]
    suffix = '' if account_stellar_catalog_light_time else '_without_catalog_light_time'
    with (directory / f"arecibo_gcns_sample_matches{suffix}.csv").open("w",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=columns)
        writer.writeheader()
        writer.writerows(matches)
    summary = {"as_of_utc": as_of_utc, "source_catalog_rows": original_count,
               "median_distance_within_100pc_rows":len(stars), "excluded_median_distance_above_100pc":original_count-len(stars),
               "sampled_transmit_directions":len(pointings), "actual_transmit_windows":449,
               "full_beam_width_arcmin":2.0, "catalog_astrometry_epoch":2016.0,
               "account_stellar_catalog_light_time":account_stellar_catalog_light_time,
               "stellar_catalog_light_time_documentation":"https://gea.esac.esa.int/archive/documentation/GDR1/Data_processing/chap_cu3ast/sec_cu3ast_intro.html",
               "missing_rv_approximation_km_per_s":0,
               "sample_star_matches":len(matches),
               "unique_eventual_catalog_sources":len({row['source_id'] for row in matches}),
               "unique_reached_catalog_sources":len({row['source_id'] for row in matches if row['reached_by_as_of']}),
               "checked_candidate_sample_star_pairs":checked_candidates,
               "per_apparition":{str(year):{"unique_eventual_catalog_sources":len({row['source_id'] for row in matches if row['apparition']==year}),
                                            "unique_reached_catalog_sources":len({row['source_id'] for row in matches if row['apparition']==year and row['reached_by_as_of']}),
                                            "nearest_already_reached_catalog_source":min((row for row in nearest if row['apparition']==year),key=lambda row:row['separation_deg'])} for year in [2008,2016]},
               "limitations":["Current JPL orbit solution is used instead of historical encoder pointings.",
                              "Beam path is sampled; a grazing star between samples could be missed.",
                              "Missing adopted radial velocities are approximated as zero.",
                              "GCNS is incomplete and median distances have uncertainty.",
                              "Stellar emission-time correction uses distance/c and a first-order proper-motion time conversion; no full relativistic astrometric covariance propagation."]}
    (directory / f"arecibo_gcns_summary{suffix}.json").write_text(json.dumps(summary,indent=2))
    return summary
