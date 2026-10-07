"""Coverage and row-identity audit for the public UCLA seed scrape."""

import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd


def audit_arecibo_archive(directory: str | Path) -> dict:
    """Audit raw run records and save canonical, atomically written intervals.

    Canonical object IDs are read from each advertised URL's ``AB`` parameter.
    Runid repeats across decades and can identify both a transmit run and a
    timestamp-less calibration row on the same day. The identity therefore
    adds a digest of every raw measurement column to object/date/runid/tx.
    Exact duplicated records are counted and reduced once; differing records
    remain distinct and their simpler-key collisions are reported explicitly.
    Timestamp-less records stay in ``unique_runs.csv`` and are flagged, while
    ``valid_intervals.csv`` includes only explicitly valid transmit windows.
    The resulting summary describes this JPL-seeded retrieval, not the complete
    history of Arecibo or other planetary-radar facilities.
    """
    directory = Path(directory)
    bulk = directory/'bulk_ucla'
    rows = pd.read_csv(bulk/'all_runs.csv',dtype=str,keep_default_na=False)
    assert len(rows)>0 and {'runid','utdate','tx','target','source_url','start_utc','end_utc','transmission_times_available'} <= set(rows.columns)
    rows['ucla_object_id'] = rows.source_url.map(lambda value:parse_qs(urlparse(value).query)['AB'][0])
    raw_columns = ['runid','tx','rx','freq','wvfrm','numpol','txoff','rxoff','dtk','fs',
                   'bits','codelen','baud','smpb','ephdelay','ephgen','ephsol',
                   'utdate','txup','txdown','rxup','rxdown']
    assert set(raw_columns) <= set(rows.columns)
    digest = rows[raw_columns].apply(lambda row: hashlib.sha256(
        json.dumps(row.to_dict(),sort_keys=True).encode()).hexdigest()[:20],axis=1)
    rows['simple_run_key'] = rows.ucla_object_id+':'+rows.utdate+':'+rows.runid+':'+rows.tx
    rows['interval_id'] = rows.simple_run_key+':'+digest
    raw_count = len(rows)
    rows=rows.drop_duplicates('interval_id',keep='first').copy()
    collisions=rows.loc[rows.simple_run_key.duplicated(keep=False)].copy()
    collisions.to_csv(bulk/'simple_run_key_collisions.csv',index=False)
    usable=rows.loc[(rows.transmission_times_available=='True') &
                    (rows.seed_identity_verified=='True') &
                    (rows.canonical_horizons_designation.str.len()>0)].copy()
    assert len(usable)>0
    usable['transmit_year']=pd.to_datetime(usable.start_utc,utc=True).dt.year
    start=pd.to_datetime(usable.start_utc,utc=True)
    end=pd.to_datetime(usable.end_utc,utc=True)
    seconds=(end-start).dt.total_seconds()
    assert seconds.between(0,86400,inclusive='neither').all()
    usable['transmit_seconds']=seconds
    for filename,data in [('unique_runs.csv',rows),('valid_intervals.csv',usable)]:
        temporary=bulk/(filename+'.tmp')
        data.to_csv(temporary,index=False)
        temporary.replace(bulk/filename)
    annual=usable.groupby('transmit_year').agg(transmission_windows=('interval_id','size'),
                                               distinct_target_ids=('ucla_object_id','nunique'),
                                               distinct_utc_dates=('utdate','nunique'),
                                               transmitter_seconds=('transmit_seconds','sum')).reset_index()
    temporary=bulk/'annual_inventory.csv.tmp';annual.to_csv(temporary,index=False);temporary.replace(bulk/'annual_inventory.csv')
    summary={'parsed_raw_runs':raw_count,'canonical_unique_runs':len(rows),'exact_duplicate_rows':raw_count-len(rows),
             'valid_verified_transmit_windows':len(usable),
             'missing_or_invalid_transmit_times':int((rows.transmission_times_available!='True').sum()),
             'unverified_target_identity_runs':int((rows.seed_identity_verified!='True').sum()),
             'canonical_target_ids':int(rows.ucla_object_id.nunique()),
             'simple_run_key_collision_groups':int(collisions.simple_run_key.nunique()),
             'records_in_simple_run_key_collisions':len(collisions),
             'target_ids_with_valid_windows':int(usable.ucla_object_id.nunique()),
             'earliest_transmission_utc':str(start.min()),'latest_transmission_utc':str(end.max()),
             'transmission_hours':float(seconds.sum()/3600),
             'transmitter_codes':rows.tx.value_counts().to_dict(),
             'frequency_hz_counts':rows.freq.value_counts().to_dict(),
             'advertised_archive_run_count':84054,
             'raw_rows_fraction_of_advertised_count':raw_count/84054,
             'fraction_of_advertised_count_recovered':len(rows)/84054,
             'archive_completeness_established':False,
             'run_identity_fields':['ucla_object_id','utdate','runid','tx','digest_of_all_22_raw_measurement_columns'],
             'limitations':['JPL seed completeness for the UCLA archive is not verified.',
                            'Records without advertised run links cannot be recovered by this method.',
                            'Exact transmit windows are preserved but original antenna pointing/power logs are absent.',
                            'First observing year in this archive is not the first year of Arecibo radar operations.']}
    (bulk/'coverage_audit.json').write_text(json.dumps(summary,indent=2))
    return summary
