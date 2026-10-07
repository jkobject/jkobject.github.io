"""UTC-date reconstruction from UCLA's documented receiver-start date."""

from datetime import datetime, timedelta, timezone


def parse_ucla_transmit_interval(row: dict) -> dict:
    """Resolve transmitter clocks around the UT date of receiver recording start.

    UCLA defines ``utdate`` as the UT date at ``rxup``:
    https://mel.epss.ucla.edu/radar/object/definition.php?element=utdate
    Thus a TX beginning23:59 and RX beginning00:01 belongs to the previous TX
    calendar day. Transmit start is placed on the nearest day to RXup, within
    12hours; transmit end then follows start with duration strictly below24h.
    The nearest-day convention assumes one short radar cycle, not a day-long
    receiver/transmitter delay. Raw dates/clocks are never modified. No date
    is inferred from runid, whose documentation does not specify day encoding.

    Missing transmitter clocks raise ValueError. Missing RXup leaves the
    provisional source-date placement unchanged and is explicitly flagged as
    unanchored; exactly12h lags are ambiguous and raise ValueError.
    """
    if not row['txup'] or not row['txdown']:
        raise ValueError('Missing txup or txdown')
    start=datetime.fromisoformat(row['utdate']+'T'+row['txup']).replace(tzinfo=timezone.utc)
    shift=0
    if row.get('rxup'):
        reference=datetime.fromisoformat(row['utdate']+'T'+row['rxup']).replace(tzinfo=timezone.utc)
        difference=(reference-start).total_seconds()
        if abs(difference)==43200:
            raise ValueError('Ambiguous12-hour receiver/transmitter date offset')
        shift=round(difference/86400)
        start+=timedelta(days=shift)
        assert abs((reference-start).total_seconds())<43200
    end=datetime.fromisoformat(start.date().isoformat()+'T'+row['txdown']).replace(tzinfo=timezone.utc)
    if end<start:end+=timedelta(days=1)
    duration=(end-start).total_seconds()
    if not 0<duration<86400:
        raise ValueError(f'Invalid transmit duration {duration}')
    return {'start_utc':start.isoformat(),'end_utc':end.isoformat(),
            'transmission_date_shift_days':shift,'receiver_date_anchor_available':bool(row.get('rxup')),
            'timestamp_basis':'utdate atRXup; nearest-day TXup; subsequent TXdown'}


def audit_ucla_transmit_times(directory) -> dict:
    """Apply documented RX-date anchoring and flag overlapping source windows.

    Every raw date/clock is preserved. Derived times are replaced atomically,
    and previous derived placements are retained for every changed row. The
    audit compares same-transmitter UTC intervals, distinguishes same-target
    overlap from incompatible cross-target overlap, and exports stable IDs for
    exclusion sensitivity. A temporal overlap alone never identifies the true
    observing date or repairs a row from an assumed runid encoding.
    """
    import json
    from pathlib import Path
    import pandas as pd
    from .audit_arecibo_archive import audit_arecibo_archive

    directory=Path(directory);bulk=directory/'bulk_ucla'
    raw=pd.read_csv(bulk/'all_runs.csv',dtype=str,keep_default_na=False)
    records=raw.to_dict('records');changed=[]
    for row in records:
        row.setdefault('previous_unanchored_start_utc','')
        row.setdefault('previous_unanchored_end_utc','')
        if row['transmission_times_available']=='True':
            parsed=parse_ucla_transmit_interval(row)
            if parsed['start_utc']!=row['start_utc']:
                row['previous_unanchored_start_utc']=row['start_utc']
                row['previous_unanchored_end_utc']=row['end_utc']
            if row['previous_unanchored_start_utc']:
                changed.append({'ucla_object_id':row['ucla_object_id'],'runid':row['runid'],
                                'target':row['target'],'old_start_utc':row['previous_unanchored_start_utc'],
                                'new_start_utc':parsed['start_utc'],'source_url':row['source_url']})
            row.update({key:str(value) for key,value in parsed.items()})
    raw=pd.DataFrame(records).fillna('')
    temporary=bulk/'all_runs.csv.tmp';raw.to_csv(temporary,index=False);temporary.replace(bulk/'all_runs.csv')
    inventory=audit_arecibo_archive(directory)
    valid=pd.read_csv(bulk/'valid_intervals.csv',dtype=str,keep_default_na=False)
    valid['composite_run_id']=valid[['ucla_object_id','utdate','runid','tx','wvfrm','freq','txup','txdown']].agg('|'.join,axis=1)
    valid['s']=pd.to_datetime(valid.start_utc,utc=True,format='ISO8601').astype('int64')
    valid['e']=pd.to_datetime(valid.end_utc,utc=True,format='ISO8601').astype('int64')
    active=[];pairs=[];overlap_ids=set();conflict_ids=set()
    union_seconds=0.;union_start=None;union_end=None
    for row in valid.sort_values('s').to_dict('records'):
        if union_end is None or row['s']>union_end:
            if union_end is not None:union_seconds+=(union_end-union_start)/1e9
            union_start,union_end=row['s'],row['e']
        else:union_end=max(union_end,row['e'])
        active=[other for other in active if other['e']>row['s']]
        for other in active:
            overlap=(min(other['e'],row['e'])-row['s'])/1e9
            if overlap<=0:continue
            same_target=other['canonical_horizons_designation']==row['canonical_horizons_designation']
            overlap_ids.update([other['composite_run_id'],row['composite_run_id']])
            if not same_target:conflict_ids.update([other['composite_run_id'],row['composite_run_id']])
            pairs.append({'interval_id1':other['interval_id'],'interval_id2':row['interval_id'],
                          'composite_run_id1':other['composite_run_id'],'composite_run_id2':row['composite_run_id'],
                          'target1':other['target'],'target2':row['target'],
                          'start1':other['start_utc'],'end1':other['end_utc'],
                          'start2':row['start_utc'],'end2':row['end_utc'],
                          'overlap_seconds':overlap,'same_target':same_target})
        active.append(row)
    if union_end is not None:union_seconds+=(union_end-union_start)/1e9
    pd.DataFrame(pairs).to_csv(bulk/'transmission_window_overlaps.csv',index=False)
    for name in ['all_runs.csv','unique_runs.csv','valid_intervals.csv']:
        table=pd.read_csv(bulk/name,dtype=str,keep_default_na=False)
        keys=table[['ucla_object_id','utdate','runid','tx','wvfrm','freq','txup','txdown']].agg('|'.join,axis=1)
        table['transmit_window_overlap']=keys.isin(overlap_ids)
        table['cross_target_time_conflict']=keys.isin(conflict_ids)
        temporary=bulk/(name+'.tmp');table.to_csv(temporary,index=False);temporary.replace(bulk/name)
    conflict_valid=valid.loc[valid.composite_run_id.isin(conflict_ids)]
    summary={'valid_intervals':len(valid),'changed_date_anchored_rows':len(changed),
             'changed_unique_valid_transmit_windows':int((valid.transmission_date_shift_days!='0').sum()),
             'valid_windows_without_receiver_date_anchor':int((valid.receiver_date_anchor_available!='True').sum()),
             'date_corrected_target_ids':len({row['ucla_object_id'] for row in changed}),
             'sum_interval_duration_hours':inventory['transmission_hours'],
             'union_interval_duration_hours':union_seconds/3600,
             'strictly_overlapping_pairs':len(pairs),
             'same_target_overlap_pairs':sum(row['same_target'] for row in pairs),
             'cross_target_overlap_pairs':sum(not row['same_target'] for row in pairs),
             'overlapping_interval_keys':len(overlap_ids),'cross_target_conflict_interval_keys':len(conflict_ids),
             'cross_target_conflict_composite_run_ids':sorted(conflict_ids),
             'cross_target_conflict_interval_ids':sorted(conflict_valid.interval_id),
             'utdate_documentation':'https://mel.epss.ucla.edu/radar/object/definition.php?element=utdate',
             'runid_documentation':'https://mel.epss.ucla.edu/radar/object/definition.php?element=runid',
             'runid_date_inference_used':False,'corrected_rows':changed,
             'limitations':['Cross-target simultaneous source windows cannot establish which row/date is correct.',
                            'Some same-target overlap can represent duplicate or inconsistent observing records.',
                            'Nearest RXup anchoring assumes transmit/receive belong to one cycle within12h.']}
    (bulk/'transmission_time_audit.json').write_text(json.dumps(summary,indent=2))
    return summary
