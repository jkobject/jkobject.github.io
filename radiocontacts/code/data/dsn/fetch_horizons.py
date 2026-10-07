"""Retrieve reproducible geocentric spacecraft directions from JPL Horizons."""

import csv
import io
import subprocess
import urllib.parse
from pathlib import Path


def fetch_horizons_ephemeris(command: str, start: str, stop: str, output: str | Path,
                             step: str = "6 h") -> int:
    """Save raw JPL response and a date/RA/Dec CSV for a spacecraft.

    Parameters
    ----------
    command : str
        JPL/NAIF object identifier, e.g. ``-31`` for Voyager 1.
    start, stop : str
        UTC dates or timestamps accepted by Horizons.
    output : str or Path
        CSV destination. The unchanged JPL text response is saved alongside it.
    step : str
        Fixed output interval; six hours is the default, to avoid long gaps
        possible with angular ``VAR`` sampling.

    Returns
    -------
    int
        Number of returned ephemeris positions.

    Notes
    -----
    Uses observer astrometric ICRF RA/Dec (quantity 1), geocentric Earth origin,
    and explicitly requests degrees and fractional UTC timestamps. This is a
    position model, not evidence that an uplink was emitted at every timestamp.
    Documentation: https://ssd-api.jpl.nasa.gov/doc/horizons.html
    """
    output = Path(output)
    params = {"format": "text", "COMMAND": command, "CENTER": "500@399",
              "MAKE_EPHEM": "YES", "EPHEM_TYPE": "OBSERVER", "START_TIME": start,
              "STOP_TIME": stop, "STEP_SIZE": step, "QUANTITIES": "1",
              "CSV_FORMAT": "YES", "ANG_FORMAT": "DEG", "TIME_DIGITS": "FRACSEC",
              "EXTRA_PREC": "YES", "TIME_TYPE": "UT", "REF_SYSTEM": "ICRF"}
    encoded = {key: value if key == "format" else f"'{value}'" for key, value in params.items()}
    url = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urllib.parse.urlencode(encoded)
    # macOS curl uses the system trust store, which includes this host's CA.
    # Python's uv-managed SSL trust store does not, so preserve TLS validation
    # with the platform client instead of disabling certificate verification.
    text = subprocess.run(["curl", "--silent", "--show-error", "--fail",
                           "--max-time", "120", url], check=True,
                          capture_output=True, text=True).stdout
    output.parent.mkdir(parents=True, exist_ok=True)
    output.with_suffix(".jpl.txt").write_text(text)
    output.with_suffix(".request_url.txt").write_text(url + "\n")
    assert "$$SOE" in text and "$$EOE" in text, text[-2000:]
    body = text.split("$$SOE", 1)[1].split("$$EOE", 1)[0].strip()
    records = []
    for row in csv.reader(io.StringIO(body)):
        assert len(row) >= 5, row
        records.append({"date": row[0].strip(), "ra": float(row[3]), "dec": float(row[4])})
    assert records
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["date", "ra", "dec"])
        writer.writeheader()
        writer.writerows(records)
    return len(records)


def refine_horizons_tracks(directory: str | Path, threshold_deg: float = 0.00128,
                            step: str = "15 min") -> dict:
    """Refine regions where six-hour JPL tracks show nonlinear sky motion.

    The diagnostic compares each true six-hour sample to the great-circle
    midpoint of its neighbors. Regions with discrepancy above ``threshold_deg``
    (default one percent of the adopted full beamwidth) are fetched afresh at
    15-minute intervals. Original API responses and every request URL remain
    saved. This is an explicit interpolation sensitivity check, not a bound
    on JPL's underlying spacecraft trajectory uncertainty.
    """
    from datetime import datetime

    import numpy as np
    import pandas as pd

    directory = Path(directory)
    assert threshold_deg > 0
    summary = {}
    for source in sorted((directory / "horizons_6h").rglob("*_ephemeris.csv")):
        relative = source.relative_to(directory / "horizons_6h")
        mission = relative.parts[0]
        command = {"voyager1": "-31", "voyager2": "-32", "pioneer10": "-23",
                   "pioneer11": "-24", "new_horizons": "-98"}[mission]
        frame = pd.read_csv(source)
        ra, dec = np.deg2rad(frame.ra.to_numpy()), np.deg2rad(frame.dec.to_numpy())
        unit = np.column_stack([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)])
        midpoint = unit[:-2] + unit[2:]
        midpoint /= np.linalg.norm(midpoint, axis=1)[:, None]
        errors = np.rad2deg(np.arctan2(np.linalg.norm(np.cross(midpoint, unit[1:-1]), axis=1),
                                      np.sum(midpoint * unit[1:-1], axis=1)))
        indices = np.flatnonzero(errors > threshold_deg) + 1
        intervals = []
        for index in indices:
            start, stop = max(0, index - 1), min(len(frame) - 1, index + 1)
            if intervals and start <= intervals[-1][1]:
                intervals[-1][1] = max(stop, intervals[-1][1])
            else:
                intervals.append([start, stop])
        pieces = [frame]
        for number, (start, stop) in enumerate(intervals):
            output = directory / "horizons_refinements" / mission / f"window_{number:02d}.csv"
            first = datetime.strptime(frame.date.iloc[start], "%Y-%b-%d %H:%M:%S.%f").isoformat(sep=" ")
            last = datetime.strptime(frame.date.iloc[stop], "%Y-%b-%d %H:%M:%S.%f").isoformat(sep=" ")
            fetch_horizons_ephemeris(command, first, last, output, step)
            pieces.append(pd.read_csv(output))
        refined = pd.concat(pieces, ignore_index=True).drop_duplicates("date")
        refined["_date"] = pd.to_datetime(refined.date, format="%Y-%b-%d %H:%M:%S.%f")
        refined.sort_values("_date", inplace=True)
        refined.drop(columns="_date", inplace=True)
        target = directory / "horizons_adaptive" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        refined.to_csv(target, index=False)
        summary[mission] = {"six_hour_rows": len(frame), "refined_rows": len(refined),
                            "refinement_windows": len(intervals),
                            "maximum_12_hour_midpoint_discrepancy_deg": float(errors.max())}
        print(f"{mission}: refined {len(intervals)} nonlinear-motion windows; {len(refined)} samples", flush=True)
    return summary
