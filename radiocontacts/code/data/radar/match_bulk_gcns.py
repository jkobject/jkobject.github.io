"""Moving-source geometric cross-match of reconstructed exact radar TX windows."""

import json
import hashlib
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


def match_bulk_gcns(beam_directory: str | Path, gcns_path: str | Path,
                    output_directory: str | Path, as_of_utc: str = '2026-10-07T00:00:00+00:00',
                    grazing_margin_arcsec: float = 15.0,
                    require_complete_inventory: bool = False) -> dict:
    """Match every completed per-target sample file to moving GCNS sources.

    The model advances Gaia's apparent J2016 positions by stellar light time,
    then uses rectilinear proper motion and adopted radial velocity to solve
    the outgoing photon/star intersection. Missing RV is explicitly zero.
    A single spatial index at Julian year2010 is enlarged by a conservative
    velocity/origin bound across the complete emission-time span. Each actual
    sample candidate is then solved and checked against its recorded beam
    radius. A second result expands that radius by15arcsec to diagnose possible
    grazing tracks between samples; it is a sensitivity, not a certified bound.

    Only targets listed in a frozen reconstruction manifest are read; their run
    signatures/counts must agree with individual summaries. Changing or newer
    unlisted files are skipped. ``require_complete_inventory`` also requires
    every requested target, zero failures, and matching input-file contents.
    Results apply to this completed reconstructed subset and median
    catalogue distances<=100pc; neither archive nor stellar completeness follows.
    The outputs preserve every sampled match and earliest arrival per source.
    """
    beam_directory, output_directory = Path(beam_directory), Path(output_directory)
    assert 0<=grazing_margin_arcsec<=60
    output_directory.mkdir(exist_ok=True)
    stars = pd.read_csv(gcns_path, dtype={'source_id':'string'})
    assert stars.source_id.is_unique and stars[['ra','dec','dist_50','pmra','pmdec']].notna().all().all()
    original_count = len(stars)
    stars = stars.loc[stars.dist_50.between(0,.1,inclusive='right')].reset_index(drop=True)
    ra, dec = np.deg2rad(stars.ra.to_numpy()), np.deg2rad(stars.dec.to_numpy())
    radius = stars.dist_50.to_numpy()*1000
    direction = np.column_stack([np.cos(dec)*np.cos(ra),np.cos(dec)*np.sin(ra),np.sin(dec)])
    east = np.column_stack([-np.sin(ra),np.cos(ra),np.zeros(len(ra))])
    north = np.column_stack([-np.cos(ra)*np.sin(dec),-np.sin(ra)*np.sin(dec),np.cos(dec)])
    rv = stars.adoptedrv.fillna(0).to_numpy()
    velocity = radius[:,None]*np.deg2rad(1/3600000)*(stars.pmra.to_numpy()[:,None]*east+stars.pmdec.to_numpy()[:,None]*north)
    velocity *= (1+rv/299792.458)[:,None]
    velocity += rv[:,None]*1.022712165045695e-6*direction
    light_pc_per_year = .30660139378555056
    position = radius[:,None]*direction+velocity*(radius/light_pc_per_year)[:,None]
    speed = np.linalg.norm(velocity,axis=1)
    quadratic_a = light_pc_per_year**2-speed**2
    assert (quadratic_a>0).all()
    midpoint_year = 2010.0
    at_emission = position+velocity*(midpoint_year-2016)
    b = (at_emission*velocity).sum(axis=1)
    tau = (b+np.sqrt(b*b+quadratic_a*(at_emission**2).sum(axis=1)))/quadratic_a
    reception_position = at_emission+velocity*tau[:,None]
    reception_radius = np.linalg.norm(reception_position,axis=1)
    tree = cKDTree(reception_position/reception_radius[:,None])
    as_of = datetime.fromisoformat(as_of_utc)
    assert as_of.tzinfo is not None
    as_of_year = 2000+((as_of.timestamp()/86400+2440587.5)-2451545.0)/365.25
    manifest = json.loads((beam_directory/'reconstruction_summary.json').read_text())
    assert sum(item['transmit_runs'] for item in manifest['reconstructed_targets'])==manifest['reconstructed_runs']
    requested_targets = manifest.get('requested_targets')
    source_path = Path(manifest['input_path'])
    if not source_path.is_absolute():
        source_path = Path(__file__).resolve().parents[2]/source_path
    source_stat = source_path.stat()
    input_matches_manifest = (source_stat.st_size == manifest['snapshot_size_bytes']
                              and hashlib.sha256(source_path.read_bytes()).hexdigest() == manifest['snapshot_sha256'])
    if require_complete_inventory:
        assert requested_targets is not None, 'Reconstruction manifest lacks the requested-target inventory'
        assert input_matches_manifest, 'Reconstruction input changed after its snapshot'
        assert not manifest['failed_targets'] and len(manifest['reconstructed_targets'])==requested_targets
    points, metadata, skipped = [], [], []
    for listed in sorted(manifest['reconstructed_targets'],key=lambda row:row['canonical_object_id']):
        summary_path = beam_directory/(listed['canonical_object_id']+'.summary.json')
        info = json.loads(summary_path.read_text())
        if (info['run_signature'],info['transmit_runs'],info['direction_samples']) != (listed['run_signature'],listed['transmit_runs'],listed['direction_samples']):
            skipped.append({'summary':str(summary_path),'reason':'summary belongs to another inventory version'});continue
        path = Path(info['output_csv'])
        if not path.is_absolute():
            path = Path(__file__).resolve().parents[2]/path
        if not path.exists():
            skipped.append({'summary':str(summary_path),'reason':'missing or incomplete CSV'});continue
        if info.get('output_csv_sha256') and hashlib.sha256(path.read_bytes()).hexdigest() != info['output_csv_sha256']:
            skipped.append({'summary':str(summary_path),'reason':'CSV content differs from frozen summary'});continue
        before = path.stat()
        data = pd.read_csv(path,dtype={'runid':'string'})
        after = path.stat()
        if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):
            skipped.append({'summary':str(summary_path),'reason':'CSV changed during read'});continue
        assert len(data)==info['direction_samples']
        assert {'epoch_utc','ux','uy','uz','origin_x_pc','origin_y_pc','origin_z_pc','beam_full_width_arcmin','composite_run_id'} <= set(data)
        if require_complete_inventory:
            assert 'cross_target_time_conflict' in data, 'Final beam files must preserve source timing-conflict flags'
        if 'cross_target_time_conflict' not in data:
            data['cross_target_time_conflict']=False
        assert data.canonical_object_id.nunique()==1 and data.canonical_object_id.iloc[0]==info['canonical_object_id']
        assert data.composite_run_id.nunique()==info['transmit_runs']
        sample_times=pd.to_datetime(data.epoch_utc,utc=True,format='ISO8601')
        assert ((sample_times>=pd.to_datetime(data.start_utc,utc=True,format='ISO8601')) &
                (sample_times<=pd.to_datetime(data.end_utc,utc=True,format='ISO8601'))).all()
        points.append(data);metadata.append(info)
    assert points, 'No completed reconstructed target samples'
    if require_complete_inventory:
        assert not skipped and len(metadata)==requested_targets
        assert sum(info['transmit_runs'] for info in metadata)==manifest['usable_s_band_transmit_runs']==manifest['reconstructed_runs']
    points = pd.concat(points,ignore_index=True)
    epoch_seconds = pd.to_datetime(points.epoch_utc,utc=True,format='ISO8601').astype('int64').to_numpy()/1e9
    years = 2000+((epoch_seconds/86400+2440587.5)-2451545.0)/365.25
    beams = points[['ux','uy','uz']].to_numpy()
    origins = points[['origin_x_pc','origin_y_pc','origin_z_pc']].to_numpy()
    assert np.isfinite(beams).all() and np.max(abs(np.linalg.norm(beams,axis=1)-1))<1e-8
    assert np.isfinite(origins).all() and np.isfinite(points.beam_full_width_arcmin).all()
    assert (points.beam_full_width_arcmin>0).all()
    max_origin = np.linalg.norm(origins,axis=1).max()
    max_time = np.max(abs(years-midpoint_year))
    reception_delta = (light_pc_per_year*max_time+max_origin)/(light_pc_per_year-speed)
    displacement = speed*reception_delta+max_origin
    minimum_range = reception_radius-displacement
    assert (minimum_range>0).all()
    padding_radians = np.max(np.arcsin(np.clip(displacement/minimum_range,0,1)))
    half_widths = np.deg2rad(points.beam_full_width_arcmin.to_numpy()/120)
    grazing_margin = np.deg2rad(grazing_margin_arcsec/3600)
    candidate_chord = 2*np.sin((half_widths.max()+grazing_margin+padding_radians)/2)
    candidates = tree.query_ball_point(beams,candidate_chord,workers=-1)
    rows = []
    checked = 0
    for sample_index, candidate_ids in enumerate(candidates):
        if not candidate_ids:continue
        candidate_ids=np.array(candidate_ids,dtype=int);checked+=len(candidate_ids)
        r=position[candidate_ids]+velocity[candidate_ids]*(years[sample_index]-2016)-origins[sample_index]
        v=velocity[candidate_ids];aa=quadratic_a[candidate_ids];bb=(r*v).sum(axis=1)
        flight=(bb+np.sqrt(bb*bb+aa*(r*r).sum(axis=1)))/aa
        reception=r+v*flight[:,None]
        unit=reception/np.linalg.norm(reception,axis=1)[:,None]
        separation=np.arctan2(np.linalg.norm(np.cross(unit,beams[sample_index]),axis=1),unit@beams[sample_index])
        selected=np.where(separation<=half_widths[sample_index]+grazing_margin)[0]
        for selected_index in selected:
            star_index=candidate_ids[selected_index]
            sample=points.iloc[sample_index]
            arrival=years[sample_index]+float(flight[selected_index])
            rows.append({'source_id':str(stars.iloc[star_index].source_id),
                         'canonical_object_id':sample.canonical_object_id,'target':sample.target,
                         'composite_run_id':sample.composite_run_id,'emission_utc':sample.epoch_utc,
                         'source_url':sample.source_url,'catalog_distance_pc':float(radius[star_index]),
                         'reception_julian_year':arrival,'separation_arcsec':float(separation[selected_index]*206264.806247),
                         'beam_radius_arcsec':float(half_widths[sample_index]*206264.806247),
                         'inside_nominal_beam':bool(separation[selected_index]<=half_widths[sample_index]),
                         'reached_by_as_of':bool(arrival<=as_of_year),
                         'missing_radial_velocity':bool(pd.isna(stars.iloc[star_index].adoptedrv)),
                         'cross_target_time_conflict':sample.cross_target_time_conflict in [True,'True','true','1'],
                         'wd_prob':float(stars.iloc[star_index].wd_prob)})
    columns=['source_id','canonical_object_id','target','composite_run_id','emission_utc','source_url',
             'catalog_distance_pc','reception_julian_year','separation_arcsec','beam_radius_arcsec',
             'inside_nominal_beam','reached_by_as_of','missing_radial_velocity','cross_target_time_conflict','wd_prob']
    matches=pd.DataFrame(rows,columns=columns)
    matches.to_csv(output_directory/'sample_matches.csv',index=False)
    central=matches.loc[matches.inside_nominal_beam==True].copy()
    earliest=central.sort_values('reception_julian_year').drop_duplicates('source_id')
    grazing_earliest=matches.sort_values('reception_julian_year').drop_duplicates('source_id')
    without_conflicts=central.loc[central.cross_target_time_conflict==False].sort_values('reception_julian_year').drop_duplicates('source_id')
    grazing_without_conflicts=matches.loc[matches.cross_target_time_conflict==False].sort_values('reception_julian_year').drop_duplicates('source_id')
    earliest.to_csv(output_directory/'earliest_source_arrivals.csv',index=False)
    without_conflicts.to_csv(output_directory/'earliest_source_arrivals_without_time_conflicts.csv',index=False)
    grazing_without_conflicts.to_csv(output_directory/'earliest_grazing_source_arrivals_without_time_conflicts.csv',index=False)
    summary={'as_of_utc':as_of_utc,'catalog_rows':original_count,'median_distance_within_100pc_rows':len(stars),
             'excluded_median_distance_above_100pc_rows':original_count-len(stars),
             'completed_target_files':len(metadata),'transmit_windows':sum(info['transmit_runs'] for info in metadata),
             'reconstruction_requested_targets':requested_targets,
             'reconstruction_manifest_transmit_windows':manifest['reconstructed_runs'],
             'reconstruction_manifest_input_path':manifest['input_path'],
             'reconstruction_input_matches_current_file':input_matches_manifest,
             'complete_retrieved_inventory_required':require_complete_inventory,
             'sampled_transmit_directions':len(points),'candidate_sample_star_pairs':checked,
             'candidate_padding_arcsec':float(padding_radians*206264.806247),
             'unique_eventual_nominal_sources':int(central.source_id.nunique()),
             'unique_reached_nominal_sources':int(central.loc[central.reached_by_as_of==True].source_id.nunique()),
             'unique_eventual_sources_excluding_time_conflicts':int(without_conflicts.source_id.nunique()),
             'unique_reached_sources_excluding_time_conflicts':int(without_conflicts.loc[without_conflicts.reached_by_as_of==True].source_id.nunique()),
             'unique_eventual_grazing_sources_excluding_time_conflicts':int(grazing_without_conflicts.source_id.nunique()),
             'unique_reached_grazing_sources_excluding_time_conflicts':int(grazing_without_conflicts.loc[grazing_without_conflicts.reached_by_as_of==True].source_id.nunique()),
             'matched_transmit_intervals_with_time_conflict':int(matches.loc[matches.cross_target_time_conflict==True].composite_run_id.nunique()),
             'eventual_nominal_sources_with_missing_rv':int(earliest.missing_radial_velocity.sum()),
             'eventual_nominal_sources_wd_prob_above_half':int((earliest.wd_prob>.5).sum()),
             'unique_eventual_grazing_sensitivity_sources':int(matches.source_id.nunique()),
             'unique_reached_grazing_sensitivity_sources':int(matches.loc[matches.reached_by_as_of==True].source_id.nunique()),
             'grazing_extra_radius_arcsec':grazing_margin_arcsec,
             'minimum_emission_utc':points.epoch_utc.min(),'maximum_emission_utc':points.epoch_utc.max(),
             'missing_rv_approximation_km_per_s':0,'stellar_catalog_light_time_corrected':True,
             'forecasts_new_unique_sources':{label:int(((earliest.reception_julian_year>as_of_year)&
                                                          (earliest.reception_julian_year<=as_of_year+years_ahead)).sum())
                                             for label,years_ahead in [('one_day',1/365.25),('one_week',7/365.25),('one_year',1),('ten_years',10),('hundred_years',100)]},
             'forecasts_grazing_sensitivity_new_unique_sources':{label:int(((grazing_earliest.reception_julian_year>as_of_year)&
                                                          (grazing_earliest.reception_julian_year<=as_of_year+years_ahead)).sum())
                                             for label,years_ahead in [('one_day',1/365.25),('one_week',7/365.25),('one_year',1),('ten_years',10),('hundred_years',100)]},
             'forecasts_excluding_time_conflicts_new_unique_sources':{label:int(((without_conflicts.reception_julian_year>as_of_year)&
                                                          (without_conflicts.reception_julian_year<=as_of_year+years_ahead)).sum())
                                             for label,years_ahead in [('one_day',1/365.25),('one_week',7/365.25),('one_year',1),('ten_years',10),('hundred_years',100)]},
             'forecasts_grazing_excluding_time_conflicts_new_unique_sources':{label:int(((grazing_without_conflicts.reception_julian_year>as_of_year)&
                                                          (grazing_without_conflicts.reception_julian_year<=as_of_year+years_ahead)).sum())
                                             for label,years_ahead in [('one_day',1/365.25),('one_week',7/365.25),('one_year',1),('ten_years',10),('hundred_years',100)]},
             'skipped_incomplete_files':skipped,'reconstructed_targets':metadata,
             'limitations':['Completed reconstructed subset only; no archive completeness claim.',
                            'Sampled nominal tracking beams, without original encoder/offset/power records.',
                            'Grazing expansion is a sensitivity, not a guaranteed continuous-track bound.',
                            'Missing radial velocities are zero; distance and astrometric covariance not marginalized.',
                            'Catalogue median-distance cut is incomplete for actual stars and planets.']}
    (output_directory/'match_summary.json').write_text(json.dumps(summary,indent=2))
    return summary
