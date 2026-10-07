"""Recalculate nominal arrival dates from the published DSN encounter catalogue.

These functions audit an existing geometric model. They do not turn the
paper's assumed continuous transmissions into observed transmission logs.
"""

import csv
import json
from datetime import datetime, timedelta
from pathlib import Path


PARSEC_METRES = 3.0856775814913673e16
LIGHT_SPEED_METRES_PER_SECOND = 299792458.0
DAY_SECONDS = 86400.0
SOURCE_FILES = {
    "Voyager 1": "voyager1/voy1_results.csv",
    "Voyager 2": "voyager2/voy2_results.csv",
    "Pioneer 10": "pioneer10/pio10_results.csv",
    "Pioneer 11": "pioneer11/pio11_results.csv",
    "New Horizons": "new_horizons/nh_results.csv",
}


def build_dsn_catalog(directory: str | Path, as_of: str = "2026-10-07") -> list[dict]:
    """Write event and unique-object CSVs from the five author CSVs.

    Parameters
    ----------
    directory : str or Path
        The DSN data directory containing the cloned ``upstream`` repository.
    as_of : str
        ISO date marking the historical/future split, evaluated at UTC midnight.

    Returns
    -------
    list of dict
        All 1,296 star-beam events, sorted by recalculated nominal arrival.

    Notes
    -----
    Arrival equals the complete source ephemeris timestamp plus distance/c.
    Distance is the paper's fixed inverse-parallax distance. The reported
    distance-only one-sigma uncertainty uses linear propagation of parallax
    error; it excludes timing, beam membership, stellar-motion, and duty-cycle
    uncertainty. Fractional dates are computational outputs, not precision
    supported by the observational inputs. Gaia identifiers stay as strings.
    """
    directory = Path(directory)
    cutoff = datetime.fromisoformat(as_of)
    events = []
    expected_rows = {"Voyager 1": 277, "Voyager 2": 272, "Pioneer 10": 222,
                     "Pioneer 11": 386, "New Horizons": 139}
    for spacecraft, relative_path in SOURCE_FILES.items():
        with (directory / "upstream" / relative_path).open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        assert len(rows) == expected_rows[spacecraft], (spacecraft, len(rows))
        assert len({row["source_id"] for row in rows}) == len(rows)
        for row in rows:
            emission = datetime.strptime(row["date"], "%Y-%b-%d %H:%M:%S.%f")
            distance = float(row["dist"])
            parallax = float(row["parallax"])
            parallax_error = float(row["parallax_error"])
            assert 0 < distance <= 100 and 0 < parallax and 0 <= parallax_error <= 0.34
            travel_days = distance * PARSEC_METRES / LIGHT_SPEED_METRES_PER_SECOND / DAY_SECONDS
            arrival = emission + timedelta(days=travel_days)
            events.append({
                "spacecraft": spacecraft,
                "gaia_edr3_source_id": row["source_id"],
                "distance_pc": distance,
                "parallax_mas": parallax,
                "parallax_error_mas": parallax_error,
                "ra_deg": float(row["ra"]),
                "dec_deg": float(row["dec"]),
                "gaia_g_abs_mag": float(row["g_abs"]),
                "gaia_bp_rp_mag": float(row["bp_rp"]),
                "pm_ra_cosdec_mas_per_year": float(row["pmra"]),
                "pm_dec_mas_per_year": float(row["pmdec"]),
                "model_first_emission_iso": emission.isoformat(timespec="milliseconds"),
                "model_first_emission_date": emission.date().isoformat(),
                "published_arrival_decimal_year": float(row["reach_year"]),
                "recalculated_arrival_iso": arrival.isoformat(timespec="seconds"),
                "recalculated_arrival_date": arrival.date().isoformat(),
                "distance_only_arrival_sigma_days": travel_days * parallax_error / parallax,
                "paper_time_in_beam_days": float(row["time_total"]),
                "full_beam_width_deg": 0.128,
                "historical_model_emission": emission <= cutoff,
                "transmission_evidence": "continuous-transmission assumption; not an operational log",
                "source_csv": relative_path,
            })
    events.sort(key=lambda row: row["recalculated_arrival_iso"])
    unique = {}
    for event in events:
        unique.setdefault(event["gaia_edr3_source_id"], event)
    assert len(events) == 1296 and len(unique) == 1278
    for filename, rows in [("dsn_encounters.csv", events),
                           ("dsn_unique_objects.csv", list(unique.values()))]:
        with (directory / filename).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(events[0]))
            writer.writeheader()
            writer.writerows(rows)
    return events


def summarize_dsn(events: list[dict], as_of: str = "2026-10-07") -> dict:
    """Count nominal unique-object arrivals over explicit calendar horizons.

    Cross-spacecraft overlaps count once, using each Gaia object's earliest
    recalculated arrival. Output labels retain the geometric-model assumption.
    Day/week/year counts are discrete events, not a smoothed daily rate.
    """
    cutoff = datetime.fromisoformat(as_of)
    unique = {}
    for event in sorted(events, key=lambda row: row["recalculated_arrival_iso"]):
        unique.setdefault(event["gaia_edr3_source_id"], event)
    horizons = {
        "as_of": cutoff,
        "next_day": cutoff + timedelta(days=1),
        "next_week": cutoff + timedelta(days=7),
        "next_calendar_year": cutoff.replace(year=cutoff.year + 1),
        "next_10_calendar_years": cutoff.replace(year=cutoff.year + 10),
        "next_100_calendar_years": cutoff.replace(year=cutoff.year + 100),
    }
    reached = sum(datetime.fromisoformat(row["recalculated_arrival_iso"]) <= cutoff
                  for row in unique.values())
    summary = {
        "as_of_utc": cutoff.isoformat(),
        "model_assumption": "continuous transmission during source ephemeris; not actual logs",
        "star_beam_events": len(events),
        "unique_gaia_objects": len(unique),
        "historical_modeled_events": sum(row["historical_model_emission"] for row in events),
        "historical_modeled_unique_objects": len({row["gaia_edr3_source_id"] for row in events
                                                  if row["historical_model_emission"]}),
        "future_modeled_events": [row for row in events if not row["historical_model_emission"]],
        "horizons": {},
        "reached_objects": [row for row in unique.values()
                            if datetime.fromisoformat(row["recalculated_arrival_iso"]) <= cutoff],
        "next_unique_arrival": next(row for row in unique.values()
                                    if datetime.fromisoformat(row["recalculated_arrival_iso"]) > cutoff),
    }
    for label, horizon in horizons.items():
        count = sum(datetime.fromisoformat(row["recalculated_arrival_iso"]) <= horizon
                    for row in unique.values())
        summary["horizons"][label] = {"end_date": horizon.date().isoformat(),
                                      "cumulative_unique_objects": count,
                                      "new_unique_objects_after_as_of": count - reached}
    return summary


def save_dsn_summary(directory: str | Path, as_of: str = "2026-10-07") -> dict:
    """Build the audited CSVs and save their reproducible JSON summary."""
    directory = Path(directory)
    summary = summarize_dsn(build_dsn_catalog(directory, as_of), as_of)
    (directory / "dsn_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary
