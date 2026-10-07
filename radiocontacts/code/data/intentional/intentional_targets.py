"""Primary-source inventory of selected deliberate interstellar messages."""

import csv
import json
import math
from datetime import datetime, timedelta, timezone
from pathlib import Path


def build_intentional_target_table(directory: str | Path,
                                 as_of_iso: str = "2026-10-07T00:00:00+00:00") -> dict:
    """Save selected documented target/date sessions and simple arrival arithmetic.

    Source tables and collaborator reports establish dates and intended targets.
    Distances retain the source's rounded light-year estimates. UTC midnight
    is an arithmetic convention because the sources do not give transmitter
    times; resulting timestamps are not accurate physical interception dates.
    This inventory is not exhaustive, and does not reconstruct foreground or
    background beam intersections, point-ahead, stellar motion or detectability.
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    zaitsev = "https://fireras.su/126/docs/classificationofirms.pdf"
    altair = "https://www.asj.or.jp/nenkai/archive/2025b/pdf/Y23c.pdf"
    sonar = "https://www.ieec.cat/en/the-ieec-and-the-s%C3%B3nar-set-the-pace-of-the-universe/"
    source_rows = [
        ("Arecibo Message", "NGC 6205", "1974-11-16", 25000.0, "Arecibo 305m", zaitsev, "globular_cluster"),
        ("Call to the Cosmos '83", "alpha Aql", "1983-08-15", 16.7, "Stanford 46m", altair, "star"),
        ("Cosmic Call 1999", "HD 186408", "1999-05-24", 70.5, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 1999", "HD 190406", "1999-06-30", 57.6, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 1999", "HD 178428", "1999-06-30", 68.3, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 1999", "HD 190360", "1999-07-01", 51.8, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 197076", "2001-08-29", 68.5, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 95128", "2001-09-03", 45.9, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 50692", "2001-09-03", 56.3, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 126053", "2001-09-03", 57.4, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 76151", "2001-09-04", 55.7, "Evpatoria 70m", zaitsev, "star"),
        ("Teen Age Message", "HD 193664", "2001-09-04", 57.4, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 2003", "HIP 4872", "2003-07-06", 32.8, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 2003", "HD 245409", "2003-07-06", 37.1, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 2003", "HD 75732", "2003-07-06", 40.9, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 2003", "HD 10307", "2003-07-06", 41.2, "Evpatoria 70m", zaitsev, "star"),
        ("Cosmic Call 2003", "HD 95128", "2003-07-06", 45.9, "Evpatoria 70m", zaitsev, "star"),
        ("A Message From Earth", "HIP 74995", "2008-10-09", 20.3, "Evpatoria 70m", zaitsev, "star"),
        ("Sonar Calling GJ273b", "GJ 273", "2017-10-16", 12.4, "EISCAT Tromso", sonar, "star"),
        ("Sonar Calling GJ273b", "GJ 273", "2017-10-17", 12.4, "EISCAT Tromso", sonar, "star"),
        ("Sonar Calling GJ273b", "GJ 273", "2017-10-18", 12.4, "EISCAT Tromso", sonar, "star"),
    ]
    rows, first_by_target = [], {}
    for message, target, sent, distance, transmitter, source, target_kind in source_rows:
        emission = datetime.fromisoformat(sent).replace(tzinfo=timezone.utc)
        arrival = emission + timedelta(days=distance * 365.25) if target_kind == "star" else None
        row = {"message": message, "target_primary_identifier": target, "target_kind": target_kind,
               "transmission_date_source": sent, "transmission_time_available": False,
               "date_arithmetic_emission_iso": emission.isoformat(),
               "source_rounded_distance_ly": distance, "transmitter": transmitter,
               "nominal_target_arrival_iso": arrival.isoformat() if arrival else "",
               "nominal_target_arrival_year": arrival.year if arrival else emission.year + int(distance),
               "arrival_evidence": "emission date plus source-rounded distance / c; not a beam intersection solution",
               "source_url": source}
        rows.append(row)
        if arrival and (target not in first_by_target or arrival < first_by_target[target][0]):
            first_by_target[target] = (arrival, row)
    with (directory / "intentional_target_sessions.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    as_of = datetime.fromisoformat(as_of_iso)
    reached = [row for arrival, row in first_by_target.values() if arrival <= as_of]
    horizons = {label: {"cumulative_unique_target_stars": sum(arrival <= end for arrival, _ in first_by_target.values()),
                        "new_unique_target_stars_after_as_of": sum(as_of < arrival <= end for arrival, _ in first_by_target.values())}
                for label, end in [("next_day", as_of + timedelta(days=1)),
                                   ("next_week", as_of + timedelta(days=7)),
                                   ("next_year", as_of + timedelta(days=365.25)),
                                   ("2036-10-07", as_of.replace(year=2036)),
                                   ("2126-10-07", as_of.replace(year=2126))]}
    summary = {"inventory_scope": "selected primary-documented messages; not all terrestrial intentional broadcasts",
               "as_of_iso": as_of_iso, "source_session_rows": len(rows),
               "unique_nearby_target_stars": len(first_by_target),
               "reached_unique_target_stars_nominal": len(reached), "reached_targets": reached,
               "next_target_nominal": sorted((row for arrival, row in first_by_target.values() if arrival > as_of),
                                             key=lambda row: row['nominal_target_arrival_iso'])[:3],
               "horizons": horizons, "precision_caveat": "Rounded source distances and date-only transmissions; show arrival year, not precise day."}
    (directory / "intentional_targets_summary.json").write_text(json.dumps(summary, indent=2))
    return summary


def build_intentional_pointings(directory: str | Path) -> dict:
    """Combine dated target evidence with cached SIMBAD astrometry and widths.

    Coordinates are nominal ICRS directions projected from SIMBAD's J2000
    reference using its measured angular proper motion. They are not original
    transmitter encoder records. Published instrument widths are applied where
    available; Altair's frequency and diffraction width remain an explicitly
    assumed scenario with a factor-two width sensitivity. Intended target
    selection biases stellar populations, so a homogeneous-density cone volume
    is a separate spatial projection, not a census of those named targets.
    """
    directory = Path(directory)
    sessions = list(csv.DictReader((directory / "intentional_target_sessions.csv").open()))
    astrometry = list(csv.DictReader((directory / "simbad_target_astrometry.csv").open()))
    catalog = {" ".join(row['id'].removeprefix('NAME ').split()): row for row in astrometry}
    assert len(catalog) == 18
    astrometry_url = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"
    coordinate_doc = "https://simbad.cds.unistra.fr/Pages/guide/ch15.htx"
    eiscat_width = "https://portal.eiscat.se/jussi/spade/FRIII_26july2006.pdf"
    evpatoria_width = "https://www.astro.uni.torun.pl/~kb/Papers/proc/Molotov-Radar.htm"
    altair_report = "https://www.lemmi.no/p/shouting-at-stars#47"
    reference_epoch = datetime(2000, 1, 1, 12, tzinfo=timezone.utc)
    output = []
    for session in sessions:
        target = session['target_primary_identifier']
        lookup = "Altair" if target == "alpha Aql" else target
        star = catalog[lookup]
        ra, dec = math.radians(float(star['ra'])), math.radians(float(star['dec']))
        unit = [math.cos(dec)*math.cos(ra), math.cos(dec)*math.sin(ra), math.sin(dec)]
        east, north = [-math.sin(ra), math.cos(ra), 0], [-math.sin(dec)*math.cos(ra), -math.sin(dec)*math.sin(ra), math.cos(dec)]
        emission = datetime.fromisoformat(session['date_arithmetic_emission_iso'])
        elapsed = (emission-reference_epoch).total_seconds()/(365.25*86400)
        motion = [(float(star['pmra'])*x + float(star['pmdec'])*y)*math.pi/(180*3600000)
                  for x, y in zip(east, north, strict=True)]
        direction = [x + elapsed*v for x, v in zip(unit, motion, strict=True)]
        norm = math.sqrt(sum(x*x for x in direction))
        direction = [x/norm for x in direction]
        if session['message'] == 'Arecibo Message':
            width, low, high, aperture, frequency = 2.0, 2.0, 2.0, 305, 2380e6
            basis = 'nominal 2-arcmin Arecibo S-band contour scenario; primary message source gives 12.6cm/305m'
            width_source = session['source_url']; frequency_status = 'source-backed rounded S-band wavelength'
        elif session['message'] == "Call to the Cosmos '83":
            aperture, frequency = 46, 423e6
            width = math.degrees(1.02*299792458/frequency/aperture)*60
            low, high = width/2, width*2
            basis = 'explicit assumed 423MHz scenario; ideal aperture HPBW=1.02lambda/D; actual width unknown'
            width_source = altair_report
            frequency_status = 'secondary reported plaque photograph; not independently verified from primary plaque; assumed model'
        elif session['message'] == 'Sonar Calling GJ273b':
            width, low, high, aperture, frequency = 36.0, 30.0, 36.0, 32, 930e6
            basis = 'published UHF instrument full HPBW0.6deg applied to Sonar scenario; 0.5deg lower sensitivity'
            width_source = eiscat_width; frequency_status = 'primary collaborator gives around930MHz; instrument32m'
        else:
            width, aperture, frequency = 3.5, 70, 5010e6
            low, high = math.degrees(1.02*299792458/frequency/aperture)*60, 3.5
            basis = 'published approximate RT70 instrument beamwidth3.5arcmin, adopted as full contour; ideal diffraction lower sensitivity'
            width_source = evpatoria_width; frequency_status = 'primary message source gives6cm/70m; primary instrument paper gives5010MHz'
        output.append({**session, 'epoch_utc': emission.isoformat(), 'emission_utc': emission.isoformat(),
                       'ra_deg': math.degrees(math.atan2(direction[1], direction[0])) % 360,
                       'dec_deg': math.degrees(math.asin(direction[2])),
                       'ux': direction[0], 'uy': direction[1], 'uz': direction[2],
                       'beam_full_width_arcmin': width, 'full_width_arcmin': width,
                       'beam_full_width_low_sensitivity_arcmin': low,
                       'beam_full_width_high_sensitivity_arcmin': high,
                       'beam_width_basis': basis, 'beam_width_source_url': width_source,
                       'aperture_metres': aperture, 'frequency_hz_for_model': frequency,
                       'frequency_evidence_status': frequency_status,
                       'origin_x_pc': 0, 'origin_y_pc': 0, 'origin_z_pc': 0,
                       'simbad_main_id': star['main_id'], 'catalogue_ra_j2000_deg': star['ra'],
                       'catalogue_dec_j2000_deg': star['dec'], 'pmra_cosdec_mas_per_year': star['pmra'],
                       'pmdec_mas_per_year': star['pmdec'], 'parallax_mas': star['plx_value'],
                       'radial_velocity_km_s': star['rvz_radvel'], 'spectral_type': star['sp_type'],
                       'coordinate_bibcode': star['coo_bibcode'], 'proper_motion_bibcode': star['pm_bibcode'],
                       'astrometry_service_url': astrometry_url, 'astrometry_reference_documentation_url': coordinate_doc,
                       'pointing_evidence': 'source named-target direction plus first-order proper-motion projection; no original encoder or point-ahead records',
                       'target_selection_bias': 'deliberately selected stellar destination; homogeneous-density volume projection does not measure target population'})
    destination = directory / 'intentional_nominal_pointings.csv'
    with destination.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader(); writer.writerows(output)
    summary = {'output_csv': str(destination), 'dated_pointings': len(output),
               'unique_named_directions': len({row['target_primary_identifier'] for row in output}),
               'astrometry_objects': len(catalog), 'reference_epoch': 'ICRS J2000.0',
               'widths_arcmin': {row['message']: row['beam_full_width_arcmin'] for row in output},
               'unknown_primary_frequency_messages': ["Call to the Cosmos '83"],
               'limitations': 'Nominal target direction/width models; date-only timestamps; source selection incomplete; no encoder/retarded point-ahead records; named-target bias'}
    (directory / 'intentional_nominal_pointings_summary.json').write_text(json.dumps(summary, indent=2))
    return summary
