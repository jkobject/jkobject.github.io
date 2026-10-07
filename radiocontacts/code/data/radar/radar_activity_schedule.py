"""Detection-calibrated radar activity scenarios, distinct from measured cones."""

from pathlib import Path


def radar_activity_schedule(project_directory, start_year=1963, end_year=2026):
    """Save annual angular-area proxies calibrated against recovered beam unions.

    JPL detection rows repeat transmitters, receivers and sometimes months.
    One proxy unit is a distinct calendar-year/target/published-Apparition pair
    within a transmitter family. Missing designations use the exact fullname,
    preserving separately named comets. An apparition spanning two calendar
    years contributes one unit in each year; this is annual activity, not a
    count of independent physical apparitions or independently new directions.

    Arecibo calibration divides recovered 2002--2019 *historically new* angular
    area by all documented annual target-apparitions in that period. Goldstone
    calibration divides the 2025 configuration-envelope union by its 16 target
    apparitions. The latter only removes overlap within the recovered sample;
    transferring it to older decades assumes comparable per-apparition sweeps.
    Other transmitters have no defensible angular calibration and stay null.

    Rates are scenario areas assigned to each recorded calendar year's proxy
    activity, not measured full-year rates or an all-human transmission census.
    Missing detection years are unknown, never inferred zero. Arecibo's years
    after its documented 2020 retirement are structural zeros. End-year rows
    are explicitly snapshot/partial-year. Multipliers 0.5/1/2 vary source rate;
    they are sensitivity scenarios, not statistical confidence intervals.

    No extrapolated area should simply be added to measured cones: subtract
    the recovered component and account for repeated directions across sources
    and decades in the downstream spatial model. Geometry/operation changed,
    successful echo detections omit unsuccessful transmissions, and the input
    catalogue is not asserted complete. The default 1963 start is an explicit
    window choice, not the beginning of all radar transmissions (Goldstone's
    Venus radar predates it). Output includes calibration coverage, source
    hashes and the proxy-unit audit. Returns (annual_dataframe, audit).
    """
    import calendar
    import hashlib
    import json
    import math
    import pandas as pd

    project = Path(project_directory)
    radar = project / "data/radar"
    results = project / "results"
    paths = {
        "detections": radar / "radar_detections.csv",
        "arecibo_area": results / "arecibo_archive_annual_new_directions.csv",
        "arecibo_inventory": radar / "bulk_ucla/annual_inventory.csv",
        "goldstone_intervals": radar / "goldstone_intervals.csv",
        "goldstone_union": results / "summary.json",
    }
    detections = pd.read_csv(paths["detections"], keep_default_na=False)
    detections["year"] = pd.to_datetime(detections["Date"]).dt.year
    assert detections["Apparition"].astype(int).ge(1).all()
    detections["target_key"] = detections["object"].where(
        detections["object"].ne(""), detections["fullname"])
    assert detections["target_key"].ne("").all()
    goldstone_codes = {"G", "DSS13", "DSS24", "DSS25", "DSS26", "DSS24/DSS25/DSS26"}
    detections["family"] = detections["Transmitter"].map(
        lambda code: "Arecibo" if code == "A" else "Goldstone" if code in goldstone_codes else "Other")
    unit_keys = ["family", "year", "target_key", "Apparition"]
    units = detections.sort_values("Date").drop_duplicates(unit_keys).copy()
    arecibo = pd.read_csv(paths["arecibo_area"])
    calibration = arecibo[arecibo["year"].between(2002, 2019)]
    assert set(calibration["year"]) == set(range(2002, 2020))
    a_units = units[(units["family"] == "Arecibo") & units["year"].between(2002, 2019)]
    a_area = float(calibration["new_coverage_sr"].sum())
    a_rate = a_area / len(a_units)
    intervals = pd.read_csv(paths["goldstone_intervals"])
    g_targets = sorted(intervals["target"].unique())
    assert len(g_targets) == 16
    assert pd.to_datetime(intervals["start_utc"]).dt.year.eq(2025).all()
    g_units = units[(units["family"] == "Goldstone") & (units["year"] == 2025)
                    & units["target_key"].isin(g_targets)]
    assert len(g_units) == len(g_targets) and set(g_units["target_key"]) == set(g_targets)
    g_area = float(json.loads(paths["goldstone_union"].read_text())["goldstone_angular"]["coverage_sr"])
    g_rate = g_area / len(g_units)
    one_disk_sr = 4 * math.pi * math.sin(math.radians(1 / 60) / 2) ** 2
    inventory = pd.read_csv(paths["arecibo_inventory"])
    recovered_a = inventory[inventory["transmit_year"].between(2002, 2019)]
    rows = []
    for year in range(start_year, end_year + 1):
        for family in ["Arecibo", "Goldstone", "Other"]:
            raw = detections[(detections["family"] == family) & (detections["year"] == year)]
            annual = units[(units["family"] == family) & (units["year"] == year)]
            proxy = len(annual)
            rate = a_rate if family == "Arecibo" else g_rate if family == "Goldstone" else None
            retired = family == "Arecibo" and year > 2020
            area = 0.0 if retired else proxy * rate if proxy and rate is not None else None
            status = "retired_structural_zero" if retired else "uncalibrated_transmitters" if family == "Other" else "no_detection_records_unknown" if not proxy else "snapshot_partial_year_proxy" if year == end_year else "detection_activity_proxy"
            recovered = arecibo.loc[arecibo["year"].eq(year), "new_coverage_sr"] if family == "Arecibo" else pd.Series(dtype=float)
            rows.append({
                "year": year, "transmitter_family": family, "status": status,
                "raw_station_detection_rows": len(raw),
                "unique_detected_targets": raw["target_key"].nunique(),
                "annual_target_apparition_proxy_units": proxy,
                "calibrated_sr_per_proxy_unit": rate,
                "modeled_angular_area_sr": area,
                "modeled_angular_area_sr_multiplier_0p5": None if area is None else area * 0.5,
                "modeled_angular_area_sr_multiplier_2": None if area is None else area * 2,
                "modeled_2arcmin_disk_equivalents_per_year": None if area is None else area / one_disk_sr,
                "modeled_2arcmin_disk_equivalents_per_calendar_day": None if area is None else area / one_disk_sr / (366 if calendar.isleap(year) else 365),
                "recovered_new_area_sr": None if recovered.empty else float(recovered.iloc[0]),
                "recovered_within_sample_union_sr": g_area if family == "Goldstone" and year == 2025 else None,
            })
    schedule = pd.DataFrame(rows)
    audit = {
        "source_snapshot_date": "2026-10-07", "years": [start_year, end_year],
        "start_year_note": "Explicit analysis window; not the beginning of all human radar. Asteroid detections begin1968; earlier planetary radar is uncalibrated by this history.",
        "reference_disk_full_width_arcmin": 2.0, "reference_disk_solid_angle_sr": one_disk_sr,
        "proxy_unit": "Calendar year + target designation (or exact fullname) + published Apparition + transmitter family; receivers/months collapsed",
        "goldstone_transmitter_codes": sorted(goldstone_codes),
        "source_rows": len(detections), "deduplicated_annual_activity_units": len(units),
        "source_rows_by_family": detections["family"].value_counts().to_dict(),
        "annual_units_by_family": units["family"].value_counts().to_dict(),
        "arecibo_calibration": {
            "years": [2002, 2019], "recovered_historically_new_area_sr": a_area,
            "documented_annual_target_apparitions": len(a_units),
            "sr_per_proxy_unit": a_rate, "disk_equivalents_per_proxy_unit": a_rate / one_disk_sr,
            "recovered_annual_target_id_count": int(recovered_a["distinct_target_ids"].sum()),
            "recovered_transmit_windows": int(recovered_a["transmission_windows"].sum()),
            "coverage_note": "Recovered annual target IDs and JPL annual target-apparitions have different keys; their count ratio is not measured completeness. Numerator is recovered-area only, not scaled by the advertised UCLA run counter.",
        },
        "goldstone_calibration": {
            "year": 2025, "recovered_within_sample_union_area_sr": g_area,
            "recovered_targets_and_annual_apparitions": len(g_units),
            "all_documented_2025_annual_apparitions": int(((units["family"] == "Goldstone") & (units["year"] == 2025)).sum()),
            "sr_per_proxy_unit": g_rate, "disk_equivalents_per_proxy_unit": g_rate / one_disk_sr,
            "recovered_target_keys": g_targets,
            "coverage_note": "123 receive/configuration windows, nominal continuous-transmit envelope, 16 detected targets; not all 2025 activity and not a measured historical-new union.",
        },
        "sensitivity_multipliers": [0.5, 1.0, 2.0],
        "sensitivity_note": "Explicit activity/area transfer scenarios, not confidence limits or a completeness correction.",
        "limitations": [
            "Successful radar detections omit transmissions without detected echoes, planets/Moon observations and unlisted facilities.",
            "Geometry, beamwidth, transmitter power, duty cycle and target mix changed across decades.",
            "Modern station labels do not certify historical antenna/frequency: primary history lists Goldstone1972Toro at13cm, Goldstone1975Eros at3.5and13cm, Arecibo1975Eros at70cm, and Goldstone1983IRAS-Araki-Alcock at13and3.5cm. Annual apparition deduplication collapses those multi-frequency cases.",
            "NASA's history states1968Icarus transmitted from a26m Goldstone dish to a64m receiver; this is not the modern DSS-14 transmitter geometry. Multipliers0.5/1/2 are not guaranteed to bracket historical hardware effects.",
            "Goldstone-family calibration transfers a DSS-14 nominal envelope to other antennas with different beamwidths.",
            "Arecibo recovered-area calibration accounts for known historical revisits only within the recovered 2001--2020 archive.",
            "Unknown years remain null; downstream gap-filling must be an explicit scenario.",
            "Current Goldstone DSS-14 modernization and a partial 2026 catalogue prevent calling this a current observed global rate.",
            "Modeled area overlaps actual recovered cones and other modeled areas; spatial/temporal overlap needs downstream correction.",
        ],
        "sources": {
            "detection_history": "https://echo.jpl.nasa.gov/History/",
            "historical_wavelength_notes": "https://echo.jpl.nasa.gov/asteroids/PDS.asteroid.radar.history.html",
            "nasa_radar_history": "https://ntrs.nasa.gov/api/citations/19960045321/downloads/19960045321.pdf",
            "detection_json": "https://echo.jpl.nasa.gov/data/asteroidradarhistory.json",
            "transmitter_labels": "https://echo.jpl.nasa.gov/data/radartelescopes.json",
            "goldstone_logs": "https://echo.jpl.nasa.gov/data/masterlogs.json",
            "arecibo_archive": "https://mel.epss.ucla.edu/radar/object/info.php",
            "arecibo_operation_dates": "https://pds.nasa.gov/ds-view/pds/viewContext.jsp?identifier=urn%3Anasa%3Apds%3Acontext%3Atelescope%3Aarecibo.305m",
            "goldstone_current_schedule": "https://echo.jpl.nasa.gov/asteroids/goldstone_asteroid_schedule.html",
        },
        "input_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in paths.items()},
    }
    results.mkdir(exist_ok=True)
    schedule.to_csv(results / "radar_activity_schedule.csv", index=False)
    units.to_csv(results / "radar_annual_detection_proxy_units.csv", index=False)
    (results / "radar_activity_calibration.json").write_text(json.dumps(audit, indent=2) + "\n")
    return schedule, audit
