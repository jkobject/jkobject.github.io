"""Bounded public-page retrieval, with a manifest of every attempted request."""

import csv
import hashlib
import json
import re
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlparse

from .ucla_timing import parse_ucla_transmit_interval


def fetch_arecibo_seed_archive(directory: str | Path, requests_per_second: float = 2.0,
                               max_workers: int = 4) -> dict:
    """Retrieve UCLA object pages and their advertised run links from JPL seeds.

    The seed list contains JPL's distinct Arecibo-detected asteroid designations.
    Its completeness for UCLA is unknown. Opaque UCLA run identifiers are read
    only from advertised links, never constructed. Cache hits make no request;
    every network attempt is recorded with HTTP status and response path.
    At most ``requests_per_second`` requests are started across all workers.

    Parsed records retain raw columns. Missing/malformed transmit timestamps are
    flagged explicitly. This function does not reconstruct pointings or claim
    the archive covers all radar targets, non-detections, or planetary radar.
    """
    assert 0 < requests_per_second <= 2 and 1 <= max_workers <= 4
    directory = Path(directory)
    bulk = directory / 'bulk_ucla'
    bulk.mkdir(exist_ok=True)
    source = json.loads((directory/'radar_history.json').read_text())
    seeds = {}
    for row in source:
        if row['Transmitter'] == 'A':
            seeds.setdefault(row['object'], row['fullname'])
    assert len(seeds) == 988
    raw_seed_count = len(seeds)
    invalid_seeds = [{'target': target, 'jpl_fullname': fullname,
                      'reason': 'Missing nonempty search designation'}
                     for target, fullname in seeds.items() if not target.strip()]
    seeds = {target: fullname for target, fullname in seeds.items() if target.strip()}
    with (bulk/'invalid_seeds.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['target','jpl_fullname','reason'])
        writer.writeheader(); writer.writerows(invalid_seeds)
    limiter_lock = threading.Lock()
    next_start = [0.0]
    manifest = []
    manifest_path = bulk/'request_manifest.jsonl'
    manifest_lock = threading.Lock()

    def retrieve(url: str) -> dict:
        """Cache one public page and record its actual retrieval result."""
        digest = hashlib.sha256(url.encode()).hexdigest()[:20]
        path = bulk/f'{digest}.html'
        meta_path = bulk/f'{digest}.request.json'
        if path.exists() and meta_path.exists():
            previous = json.loads(meta_path.read_text())
            if previous['http_status'] == 200:
                return {**previous, 'cache_hit': True}
        with limiter_lock:
            wait = max(0, next_start[0]-time.monotonic())
            if wait:
                time.sleep(wait)
            next_start[0] = time.monotonic() + 1/requests_per_second
        started = datetime.now(timezone.utc).isoformat()
        result = subprocess.run(['curl','--silent','--show-error','--location',
                                 '--max-time','30','--write-out','\n%{http_code}',url],
                                capture_output=True,text=True)
        response, _, status = result.stdout.rpartition('\n')
        http_status = int(status) if status.isdigit() else 0
        path.write_text(response)
        entry = {'url':url,'response_path':str(path), 'started_utc':started,
                 'http_status':http_status,'curl_exit_code':result.returncode,
                 'bytes':len(response.encode()),'stderr':result.stderr[:500],'cache_hit':False}
        meta_path.write_text(json.dumps(entry,indent=2))
        with manifest_lock:
            with manifest_path.open('a') as handle:
                handle.write(json.dumps(entry)+'\n')
        return entry

    objects, run_links = [], {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(retrieve,'https://mel.epss.ucla.edu/radar/object/info.php?'+urlencode({'search':target})):target for target in sorted(seeds)}
        for done_count, future in enumerate(as_completed(futures),1):
            target = futures[future]
            response = future.result()
            manifest.append(response)
            html = Path(response['response_path']).read_text()
            links = set()
            for groups in re.findall(r'href\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',html,re.I):
                link = next(value for value in groups if value)
                absolute = urljoin(response['url'],unescape(link))
                parsed = urlparse(absolute)
                if parsed.netloc=='mel.epss.ucla.edu' and parsed.path.endswith('/runs.php'):
                    query=parse_qs(parsed.query)
                    assert {'AB','year','month'} <= query.keys(), absolute
                    links.add(absolute)
                    run_links.setdefault(absolute, []).append(target)
            title_match = re.search(r'<strong><font size="5">(.*?)</font></strong>',html,re.S)
            actual_title = unescape(re.sub(r'<[^>]+>','',title_match[1])).strip() if title_match else ''
            lookup_status = ('request_failed' if response['http_status'] != 200 else
                             'no_matching_record' if 'No matching record' in html else
                             'object_record' if actual_title else 'unresolved_or_multiple_results')
            objects.append({'target':target,'jpl_fullname':seeds[target],
                            'index_url':response['url'],'http_status':response['http_status'],
                            'index_response_path':response['response_path'],
                            'actual_index_title':actual_title,'lookup_status':lookup_status,
                            'advertised_run_pages':len(links),
                            'index_html_complete':html.rstrip().endswith('</html>')})
            if done_count % 50 == 0 or done_count==len(seeds):
                print(f'UCLA indexes {done_count}/{len(seeds)}; advertised run pages {len(run_links)}',flush=True)
                with (bulk/'object_index.csv').open('w',newline='') as handle:
                    writer=csv.DictWriter(handle,fieldnames=list(objects[0]))
                    writer.writeheader();writer.writerows(objects)
                (bulk/'advertised_run_links.json').write_text(json.dumps(run_links,indent=2))
    # The public search form also accepts permanent asteroid numbers. Retry
    # only explicit no-match designations, using numbers present in JPL names.
    fallback_objects = []
    fallback_numbers = {}
    for item in objects:
        number = re.match(r'^(\d+)\b',item['jpl_fullname'].strip())
        if item['lookup_status']=='no_matching_record' and number:
            fallback_numbers[item['target']] = number[1]
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(retrieve,'https://mel.epss.ucla.edu/radar/object/info.php?'+
                               urlencode({'search':number})):target
                   for target, number in fallback_numbers.items()}
        for future in as_completed(futures):
            target = futures[future]
            response = future.result()
            manifest.append(response)
            html = Path(response['response_path']).read_text()
            links = set()
            for groups in re.findall(r'href\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',html,re.I):
                link = next(value for value in groups if value)
                absolute = urljoin(response['url'],unescape(link))
                parsed = urlparse(absolute)
                if parsed.netloc=='mel.epss.ucla.edu' and parsed.path.endswith('/runs.php'):
                    query=parse_qs(parsed.query)
                    assert {'AB','year','month'} <= query.keys(), absolute
                    links.add(absolute)
                    if target not in run_links.setdefault(absolute,[]):
                        run_links[absolute].append(target)
            title_match = re.search(r'<strong><font size="5">(.*?)</font></strong>',html,re.S)
            actual_title = unescape(re.sub(r'<[^>]+>','',title_match[1])).strip() if title_match else ''
            lookup_status = ('request_failed' if response['http_status'] != 200 else
                             'no_matching_record' if 'No matching record' in html else
                             'object_record' if actual_title else 'unresolved_or_multiple_results')
            fallback_objects.append({'target':target,'numeric_search':fallback_numbers[target],
                                     'jpl_fullname':seeds[target],'index_url':response['url'],
                                     'http_status':response['http_status'],
                                     'index_response_path':response['response_path'],
                                     'actual_index_title':actual_title,'lookup_status':lookup_status,
                                     'advertised_run_pages':len(links),
                                     'index_html_complete':html.rstrip().endswith('</html>')})
    if fallback_objects:
        with (bulk/'fallback_object_index.csv').open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=list(fallback_objects[0]))
            writer.writeheader();writer.writerows(fallback_objects)
        (bulk/'advertised_run_links.json').write_text(json.dumps(run_links,indent=2))
        print(f'UCLA numeric fallback indexes {len(fallback_objects)}; total run pages {len(run_links)}',flush=True)
    records, pages = [], []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(retrieve,url):url for url in sorted(run_links)}
        for done_count, future in enumerate(as_completed(futures),1):
            url = futures[future]
            response = future.result()
            manifest.append(response)
            html = Path(response['response_path']).read_text()
            declared = re.search(r'List of (\d+) runs for the (\d{4}) detection of\s*(.*?)\s*</b>',html,re.S)
            match = re.search(r'<table class="table".*?</table>',html,re.S)
            actual_title = unescape(re.sub(r'<[^>]+>','',declared[3])).strip() if declared else ''
            number_match = re.match(r'^(\d+)\b',actual_title)
            provisional_match = re.search(r'\(([^()]*)\)',actual_title)
            actual_number = number_match[1] if number_match else ''
            actual_designation = provisional_match[1].strip() if provisional_match else ''
            canonical_designation = actual_designation or actual_number
            normalized_designation = ' '.join(actual_designation.split()).casefold()
            verified_seeds = [seed for seed in run_links[url]
                              if ' '.join(seed.split()).casefold() == normalized_designation
                              or (actual_number and re.match(r'^'+re.escape(actual_number)+r'\b',seeds[seed].strip()))]
            page = {'url':url,'seed_target':';'.join(run_links[url]),'http_status':response['http_status'],
                    'response_path':response['response_path'],
                    'actual_run_page_title':actual_title,'actual_permanent_number':actual_number,
                    'actual_provisional_designation':actual_designation,
                    'canonical_horizons_designation':canonical_designation,
                    'ucla_object_id':parse_qs(urlparse(url).query)['AB'][0],
                    'seed_identity_verified':bool(verified_seeds),
                    'declared_runs':int(declared[1]) if declared else None,
                    'parsed_runs':0,'parse_error':''}
            if response['http_status'] != 200 or declared is None or match is None:
                page['parse_error']='HTTP error or missing/truncated run table'
            else:
                table=[]
                for raw_row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',match[0],re.S):
                    table.append([unescape(re.sub(r'<[^>]+>','',cell)).strip() for cell in re.findall(r'<td\b[^>]*>(.*?)</td>',raw_row,re.S)])
                header=table[0]
                if len(table)-1 != int(declared[1]) or any(len(row)!=len(header) for row in table[1:]):
                    page['parse_error']='Declared count or table row shape mismatch'
                else:
                    for cells in table[1:]:
                        row=dict(zip(header,cells,strict=True))
                        row.update(target=canonical_designation,seed_target=';'.join(run_links[url]),
                                   actual_run_page_title=actual_title,actual_permanent_number=actual_number,
                                   actual_provisional_designation=actual_designation,
                                   canonical_horizons_designation=canonical_designation,
                                   ucla_object_id=page['ucla_object_id'],
                                   seed_identity_verified=bool(verified_seeds),
                                   source_url=url,transmission_times_available=False,
                                   start_utc='',end_utc='',timestamp_error='')
                        if not row.get('txup') or not row.get('txdown'):
                            row['timestamp_error']='Missing txup or txdown'
                        else:
                            try:
                                row.update(parse_ucla_transmit_interval(row),transmission_times_available=True)
                            except ValueError as error:
                                row['timestamp_error']=str(error)
                        records.append(row)
                    page['parsed_runs']=len(table)-1
            pages.append(page)
            if done_count % 25 == 0 or done_count==len(run_links):
                print(f'UCLA run pages {done_count}/{len(run_links)}; parsed runs {len(records)}',flush=True)
                with (bulk/'run_pages.csv').open('w',newline='') as handle:
                    writer=csv.DictWriter(handle,fieldnames=list(pages[0]));writer.writeheader();writer.writerows(pages)
                if records:
                    fields=sorted({key for row in records for key in row})
                    temporary=bulk/'all_runs.csv.tmp'
                    with temporary.open('w',newline='') as handle:
                        writer=csv.DictWriter(handle,fieldnames=fields);writer.writeheader();writer.writerows(records)
                    temporary.replace(bulk/'all_runs.csv')
    summary={'raw_jpl_seed_targets':raw_seed_count,'valid_seed_targets':len(seeds),
             'invalid_missing_designation_seeds':len(invalid_seeds),'retrieved_object_indexes':len(objects),
             'failed_index_requests':sum(row['http_status']!=200 for row in objects),
             'indexes_with_object_record':sum(row['lookup_status']=='object_record' for row in objects),
             'indexes_no_matching_record':sum(row['lookup_status']=='no_matching_record' for row in objects),
             'indexes_unresolved_or_multiple':sum(row['lookup_status']=='unresolved_or_multiple_results' for row in objects),
             'indexes_with_no_run_links':sum(row['advertised_run_pages']==0 for row in objects),
             'numeric_fallback_index_requests':len(fallback_objects),
             'numeric_fallback_object_records':sum(row['lookup_status']=='object_record' for row in fallback_objects),
             'numeric_fallback_no_matching_records':sum(row['lookup_status']=='no_matching_record' for row in fallback_objects),
             'truncated_index_html':sum(not row['index_html_complete'] for row in objects),
             'advertised_unique_run_pages':len(run_links),'parsed_run_pages':sum(not row['parse_error'] for row in pages),
             'failed_or_truncated_run_pages':sum(bool(row['parse_error']) for row in pages),
             'parsed_raw_runs':len(records),'unique_run_ids':len({row.get('runid') for row in records}),
             'valid_transmit_windows':sum(row['transmission_times_available'] for row in records),
             'missing_or_invalid_transmit_times':sum(not row['transmission_times_available'] for row in records),
             'run_pages_with_unverified_seed_identity':sum(not row['seed_identity_verified'] for row in pages),
             'raw_runs_with_unverified_seed_identity':sum(not row['seed_identity_verified'] for row in records),
             'advertised_archive_runs':84054,'seed_completeness_verified':False,
             'limitations':['JPL seed list completeness for UCLA is unverified.','Archive landing-page total includes records absent from this seed/link retrieval if totals differ.','Transmitter encoder pointings/power/offset logs are absent.']}
    (bulk/'retrieval_summary.json').write_text(json.dumps(summary,indent=2))
    return summary
