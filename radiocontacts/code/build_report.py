"""Build the portable study from frozen result tables and explicit model input."""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import importlib.metadata
import json
import sys

import pandas as pd

from analysis import AS_OF, ROOT


def render_study_report(dsn_catalog: str, dsn_model_label: str, rewrite_source: bool = False):
    """Write editable Markdown and render one offline HTML report.

    Parameters
    ----------
    dsn_catalog : str
        Explicit project-relative CSV for the independently recomputed DSN
        model; no automatic fallback to a different analysis is allowed.
    dsn_model_label : str
        Human-readable definition of the selected model, including bandwidth
        and stellar light-time convention. Outputs remain conditional on
        continuous uplinks and cannot be called recorded exposure counts.
    rewrite_source : bool
        If True, regenerate the initial narrative from the result template.
        The default preserves existing source/report.md narrative edits while
        rebuilding its figures, attachments and both report modes.
    """
    sys.path.insert(0, str(ROOT/"renderer/scripts"))
    from report_builder import render_report

    s = json.loads((ROOT/"results/summary.json").read_text())
    p = s["parameters"]
    d = pd.read_csv(ROOT/dsn_catalog, dtype={"gaia_edr3_source_id": str})
    assert d.gaia_edr3_source_id.is_unique
    d = d.loc[d.historical_model_emission].copy()
    dates = d.recalculated_arrival_iso
    for value in dates:
        datetime.fromisoformat(value)
    reached = d.loc[dates <= "2026-10-07T00:00:00"].copy()
    next_object = d.loc[dates > "2026-10-07T00:00:00"].iloc[0]
    horizon_dates = ["2026-10-08", "2026-10-14", "2027-10-07", "2036-10-07", "2126-10-07"]
    horizon_names = ["Next day", "Next week", "Next calendar year", "Next 10 years", "Next 100 years"]
    horizon_counts = [int((dates <= date+"T00:00:00").sum()) for date in horizon_dates]
    horizon_rows = "\n".join(f"| {name} | {date} | {n} | {n-len(reached)} |"
                             for name, date, n in zip(horizon_names, horizon_dates, horizon_counts))
    reached_rows = "\n".join(f"| {row.spacecraft} | {row.gaia_edr3_source_id} | {row.distance_pc:.2f} | {row.recalculated_arrival_iso[:10]} |"
                             for row in reached.itertuples())
    timeline = [{"date": f"{year}-10-07", "objects": int((dates <= f"{year}-10-07T00:00:00").sum())}
                for year in range(2026, 2351)]
    pd.DataFrame(timeline).to_csv(ROOT/"results/dsn_selected_timeline.csv", index=False)
    angular = pd.read_csv(ROOT/"results/goldstone_angular_timeline.csv")
    area = s["goldstone_angular"]
    days = len(angular)-1
    rate = area["equivalent_beam_disks"]/days
    a = s["arecibo_results"][0]
    g100 = s["goldstone_results"][4]
    direction_forecast = json.loads((ROOT/"results/dsn_future_direction_scenario.json").read_text())
    direction_rows = "\n".join(
        f"| {r['mission']} | {r['full_width_arcmin']:.2f}′ | {r['new_vs_past_beam_disk_equivalents']:.1f} | {r['new_vs_past_equivalent_disks_per_calendar_day']:.3f} |"
        for r in direction_forecast)
    direction_area_deg2 = sum(r["new_vs_past_angular_sr"] for r in direction_forecast)*(180/3.141592653589793)**2
    archive = json.loads((ROOT/"results/arecibo_archive_summary.json").read_text())
    radar_match = json.loads((ROOT/"data/radar/bulk_gcns/match_summary.json").read_text())
    assert archive["archive_geometry_complete"] and radar_match["complete_retrieved_inventory_required"]
    assert radar_match["transmit_windows"] == archive["reconstructed_transmit_intervals"]
    archive_audit = archive["source_audit"]
    archive_now = archive["forecasts"][0]
    archive_future = archive["forecasts"][4]
    annual = pd.DataFrame(archive["annual_new_directions"])
    complete_years = annual.loc[annual.year.between(2002, 2019)]
    annual_mean = complete_years.new_beam_disk_equivalents.mean()
    annual_rows = "\n".join(f"| {int(r.year)} | {r.new_beam_disk_equivalents:,.0f} | {r.average_new_equivalents_per_calendar_day:.1f} |" for r in annual.itertuples())
    radar_forecast_rows = "\n".join(
        f"| {label} | {radar_match['forecasts_new_unique_sources'][key]} | {archive_now['new_stars_next_'+unit]:.2g} | {archive_now['new_hz_planets_next_'+unit]:.2g} |"
        for label, key, unit in [("Next day", "one_day", "day"), ("Next week", "one_week", "week"), ("Next calendar year", "one_year", "year")])
    intentional = json.loads((ROOT/"data/intentional/intentional_targets_summary.json").read_text())
    intentional_sessions = pd.read_csv(ROOT/"data/intentional/intentional_target_sessions.csv")
    intentional_stars = intentional_sessions.loc[intentional_sessions.target_kind == "star"].sort_values("transmission_date_source").drop_duplicates("target_primary_identifier")
    intentional_rows = "\n".join(f"| {r.target_primary_identifier} | {r.transmission_date_source} | {r.source_rounded_distance_ly:.1f} | ~{r.nominal_target_arrival_year} |" for r in intentional_stars.itertuples())
    cases = pd.read_csv(ROOT/"results/historical_fixed_beam_scenarios.csv")
    combined = json.loads((ROOT/"results/combined_inventory_summary.json").read_text())
    global_model = json.loads((ROOT/"results/global_extrapolation_summary.json").read_text())
    global_timeline = pd.read_csv(ROOT/"results/global_extrapolated_timeline.csv")
    recovered_timeline = pd.read_csv(ROOT/"results/combined_recovered_timeline.csv")
    central = global_timeline.loc[global_timeline.radar_area_multiplier == 1].copy()
    global_now = next(row for row in global_model["current_scenarios"] if row["radar_area_multiplier"] == 1)
    global_rates = [row for row in global_model["arrival_forecasts"] if row["radar_area_multiplier"] == 1]
    global_rate_rows = "\n".join(f"| Next {row['interval']} | {row['new_bounded_reference_planets_expected']:.3g} | {row['new_hz_planets_expected']:.3g} |" for row in global_rates)
    global_years = [2026, 2036, 2126, 2326]
    global_rows = central.loc[central.date_utc.str[:4].astype(int).isin(global_years) & central.date_utc.str[5:10].eq("10-07")]
    global_table = "\n".join(f"| {r.date_utc[:4]} | {r.bounded_reference_planets_expected:,.2f} | {r.hz_planets_expected:,.2f} | {r.volume_ly3:,.0f} | {r.average_volume_per_2arcmin_equivalent_ly3:.3g} |" for r in global_rows.itertuples())
    benchmark = next(row for row in global_model["direction_benchmarks"] if row["radar_area_multiplier"] == 1)
    future_cones_summary = json.loads((ROOT/"results/future_new_cones_scenario_summary.json").read_text())
    future_cones = pd.read_csv(ROOT/"results/future_new_cones_scenario.csv")
    future_central = future_cones.loc[future_cones.future_area_transfer_multiplier == 1]
    future_initial_rate = next(row for row in future_cones_summary["scenarios"] if row["future_area_transfer_multiplier"] == 1)["initial_new_2arcmin_equivalents_per_year"]
    future_cone_rows = "\n".join(f"| {int(r.elapsed_julian_years)} | {r.new_2arcmin_equivalent_directions:,.0f} | {r.new_2arcmin_equivalents_per_year:,.0f} | {r.average_volume_per_new_2arcmin_equivalent_ly3:.3g} | {r.bounded_reference_planets_expected:.3g} / {r.hz_planets_expected:.3g} |" for r in future_central.itertuples())
    disk_sr = 2.658288448359426e-7
    future_dsn_2arcmin = direction_area_deg2*(3.141592653589793/180)**2/disk_sr
    case_rows = "\n".join(f"| {int(r.nonoverlapping_fixed_beams):,} | {int(r.age_years)} | {r.stars_expected:.3g} | {r.hz_planets_expected:.3g} | {r.new_stars_next_year:.3g} |"
                           for r in cases.itertuples())
    reference = {
        "dsn": {"label": "Derrick & Isaacson (2023), Earth transmissions to nearby stars", "url": "https://arxiv.org/abs/2304.07400"},
        "dsn-code": {"label": "Author data and code, Transmission-Encounters", "url": "https://github.com/reillyderrick/Transmission-Encounters"},
        "gcns": {"label": "Gaia Collaboration (2021), Gaia Catalogue of Nearby Stars", "url": "https://www.cosmos.esa.int/web/gaia/edr3-gcns"},
        "gaia-time": {"label": "ESA Gaia documentation: astrometric epoch and light arrival", "url": "https://gea.esac.esa.int/archive/documentation/GDR1/Data_processing/chap_cu3ast/sec_cu3ast_intro.html"},
        "g-occ": {"label": "Bryson et al. (2021), rocky HZ planet occurrence", "url": "https://arxiv.org/abs/2010.14812"},
        "m-occ": {"label": "Dressing & Charbonneau (2015), M-dwarf planets", "url": "https://arxiv.org/abs/1501.01623"},
        "census": {"label": "Reylé et al. (2023), the 10-pc census update", "url": "https://arxiv.org/abs/2302.02810"},
        "goldstone": {"label": "JPL Goldstone observing setup logs", "url": "https://echo.jpl.nasa.gov/Obslogs/index.html"},
        "radar-history": {"label": "JPL asteroid radar history", "url": "https://echo.jpl.nasa.gov/History/"},
        "ucla": {"label": "UCLA Small-Body Radar Database", "url": "https://mel.epss.ucla.edu/radar/object/info.php"},
        "arecibo-runs": {"label": "UCLA 2000 DP107: 2008 actual transmit runs", "url": "https://mel.epss.ucla.edu/radar/object/runs.php?AB=a0185851&year=2008&month=09"},
        "schedule": {"label": "JPL current Goldstone schedule and modernization", "url": "https://echo.jpl.nasa.gov/asteroids/goldstone_asteroid_schedule.html"},
        "beam": {"label": "JPL DSN handbook 101E, 70-m beam widths", "url": "https://deepspace.jpl.nasa.gov/dsndocs/810-005/101/101E.pdf"},
        "nh-band": {"label": "NASA: New Horizons 7.2-GHz Earth uplink", "url": "https://science.nasa.gov/blogs/new-horizons/2015/11/13/radio-signals-from-earth-probe-plutos-atmosphere/"},
        "radar-beam": {"label": "Goldstone Solar System Radar improved capabilities", "url": "https://deepspace.jpl.nasa.gov/files/GSSR_improved_capabilities_09452079.pdf"},
        "detectability": {"label": "Sheikh et al. (2025), Earth Detecting Earth", "url": "https://arxiv.org/abs/2502.02614"},
        "horizons": {"label": "NASA/JPL Horizons API documentation", "url": "https://ssd-api.jpl.nasa.gov/doc/horizons.html"},
        "messages": {"label": "Zaitsev (2011), primary interstellar message target/date table", "url": "https://fireras.su/126/docs/classificationofirms.pdf"},
        "altair": {"label": "Narusawa et al. (2025), primary Altair transmission follow-up abstract", "url": "https://www.asj.or.jp/nenkai/archive/2025b/pdf/Y23c.pdf"},
        "sonar": {"label": "IEEC collaborator record of Sónar's October 2017 transmissions", "url": "https://www.ieec.cat/en/the-ieec-and-the-s%C3%B3nar-set-the-pace-of-the-universe/"},
        "altair-type": {"label": "NASA-hosted HST Altair study: A7V spectral class", "url": "https://ntrs.nasa.gov/citations/19950048307"},
        "all-occ": {"label": "Cassan et al. (2012), planets per star in a finite mass/orbit range", "url": "https://arxiv.org/abs/1202.0903"},
        "old-radar": {"label": "JPL primary history of radar frequencies and observing targets", "url": "https://echo.jpl.nasa.gov/asteroids/PDS.asteroid.radar.history.html"},
        "old-aperture": {"label": "NASA history: 1968 Icarus used a 26-m transmitter", "url": "https://ntrs.nasa.gov/api/citations/19960045321/downloads/19960045321.pdf"},
    }
    plots = {"combined-arrivals": {}}
    for metric, label in [("hz_planets_expected", "Small habitable-zone planets"), ("bounded_reference_planets_expected", "Broader reference planet population")]:
        low = global_timeline.loc[global_timeline.radar_area_multiplier == .5]
        high = global_timeline.loc[global_timeline.radar_area_multiplier == 2]
        traces = [
            {"type": "scatter", "mode": "lines", "name": "0.5× radar transfer", "x": low.date_utc.tolist(), "y": low[metric].tolist(), "line": {"width": 0, "color": "#c2d7de"}, "showlegend": False},
            {"type": "scatter", "mode": "lines", "name": "Radar transfer sensitivity", "x": high.date_utc.tolist(), "y": high[metric].tolist(), "line": {"width": 0, "color": "#c2d7de"}, "fill": "tonexty", "fillcolor": "rgba(86,138,155,0.2)"},
            {"type": "scatter", "mode": "lines", "name": "Historical radar extrapolation + DSN/messages", "x": central.date_utc.tolist(), "y": central[metric].tolist(), "line": {"color": "#176b75", "width": 3}},
            {"type": "scatter", "mode": "lines", "name": "Recovered/modelled beam union", "x": recovered_timeline.date_utc.tolist(), "y": recovered_timeline[metric].tolist(), "line": {"color": "#b27546", "width": 2, "dash": "dash"}},
            {"type": "scatter", "mode": "markers", "name": "Cutoff: October 2026", "x": [global_now["date_utc"]], "y": [global_now[metric]], "marker": {"color": "#176b75", "size": 8}, "showlegend": False}]
        visible_max = float(high.loc[high.date_utc.str[:4].astype(int) <= 2126, metric].max())
        plots["combined-arrivals"][metric] = {"label": label, "data": traces,
            "layout": {"xaxis": {"title": "Arrival date", "range": ["1960-10-07", "2126-10-07"]}, "yaxis": {"title": "Expected planets", "range": [0, visible_max*1.08]}, "font": {"size": 16}, "legend": {"orientation": "h", "y": 1.25, "font": {"size": 11}}},
            "caption": "Emissions through2026-10-07; no later transmissions. Shading varies radar transfer (0.5×–2×), excluding DSN duty, beam and occurrence uncertainty. Counts are population projections. The selector changes population; the data table gives exact modeled values." + (" Reference population:5 Earth masses–10 Jupiter masses,0.5–10AU." if metric == "bounded_reference_planets_expected" else "")}
    plots.update({
        "arrivals": {"selected": {"label": "Selected DSN model", "data": [{"type": "scatter", "mode": "lines", "name": "Unique catalogue objects", "x": [r["date"] for r in timeline], "y": [r["objects"] for r in timeline], "line": {"shape": "hv", "color": "#176b75", "width": 3}}], "layout": {"xaxis": {"title": "Date (October 7 each year)"}, "yaxis": {"title": "Cumulative unique Gaia objects"}, "font": {"size": 16}}, "caption": "Model arrivals are discrete. Inventory contains only modeled first emission dates no later than 2026-10-07; no continuing future operations are assumed."}},
        "angular": {"coverage": {"label": "New coverage within the retrieved 2025 inventory", "data": [{"type": "scatter", "mode": "lines", "name": "Cumulative beam-disk equivalents", "x": angular.date.tolist(), "y": angular.equivalent_beam_disks.tolist(), "line": {"color": "#176b75", "width": 3}}], "layout": {"xaxis": {"title": "2025 calendar date"}, "yaxis": {"title": "Unique beam disks"}, "font": {"size": 16}}, "caption": "One equivalent disk has full width 1.92′. The union starts empty for this retrieved subset. Coverage may repeat sky illuminated before 2025; this is not globally new sky."}},
        "scenario": {},
        "archive-directions": {"year": {"label": "New coverage within the recovered Arecibo inventory", "data": [{"type": "bar", "name": "New 2′ beam-disk equivalents", "x": annual.year.tolist(), "y": annual.new_beam_disk_equivalents.tolist(), "marker": {"color": "#176b75"}}], "layout": {"xaxis": {"title": "Transmission year"}, "yaxis": {"title": "New beam disks"}, "font": {"size": 16}}, "caption": "Dated angular union, starting empty in 2001. 2001 and 2020 are partial years; earlier Arecibo and other facilities may already have covered this sky. Full-width disk: 2′."}},
    })
    for metric, label in [("stars_expected", "Expected ordinary stars"), ("hz_planets_expected", "Expected small HZ planets")]:
        traces = []
        for age, color in [(20, "#b9cad1"), (40, "#568a9b"), (60, "#176b75")]:
            rows = cases.loc[cases.age_years == age]
            traces.append({"type": "scatter", "mode": "lines+markers", "name": f"{age}-year-old signals", "x": rows.nonoverlapping_fixed_beams.tolist(), "y": rows[metric].tolist(), "line": {"color": color}})
        plots["scenario"][metric] = {"label": label, "data": traces, "layout": {"xaxis": {"title": "Distinct fixed 2′ beams", "type": "log"}, "yaxis": {"title": label, "rangemode": "tozero"}, "font": {"size": 16}, "legend": {"orientation": "h", "y": 1.15}}, "caption": "Sensitivity scenarios, not an estimate of actual global beam count. Each scenario assumes equal-aged fixed directions and a homogeneous local population outside 4.24 ly."}
    # Plotly 6 does not render shorthand axis title strings in raw layouts.
    # Keep actual unit/quantity labels visible in the exported artifact.
    for variants in plots.values():
        for variant in variants.values():
            for axis in ("xaxis", "yaxis"):
                variant["layout"][axis]["title"] = {"text": variant["layout"][axis]["title"]}
                variant["layout"][axis]["title"]["standoff"] = 18
                variant["layout"][axis]["automargin"] = True
            variant["layout"]["margin"] = {"l": 85, "r": 25, "t": 50, "b": 100}
    plots["angular"]["coverage"]["layout"]["xaxis"].update(
        {"tickformat": "%b %d", "tickangle": 0, "nticks": 4})
    for variant in plots["combined-arrivals"].values():
        variant["layout"]["margin"] = {"l": 65, "r": 20, "t": 45, "b": 55}
    report = f'''<section id="abstract" markdown="1">

## The cone-volume model projects {global_now['bounded_reference_planets_expected']:.1f} reference planets reached so far.

<p class="takeaway">Central projection at the 2026 cutoff: {global_now['bounded_reference_planets_expected']:.1f} broader reference planets or {global_now['hz_planets_expected']:.1f} small habitable-zone planets. Already-emitted signals reach {global_rows.loc[global_rows.date_utc.str.startswith('2126'), 'bounded_reference_planets_expected'].iloc[0]:.0f} reference planets by 2126.</p>

<p class="caveat">Continuous modeled DSN uplinks and 70-m beam widths dominate the volume. Shading excludes these larger uncertainties. This is not a complete transmitter census.</p>

<div data-plot="combined-arrivals" data-default="hz_planets_expected"></div>

<div class="prose" markdown="1">

The first curve combines all included emitted cones through time, counting overlapping directions once. The solid curve extrapolates Arecibo/Goldstone asteroid-radar history from annual detected-target activity; the dashed curve uses recovered radar geometry. Both retain the same five spacecraft tracks and selected intentional messages. No transmissions after the cutoff are assumed. Future growth is caused by light already in flight.

The broader population is calibrated at **1.6 planets per ordinary star**, limited to **5 Earth masses–10 Jupiter masses and 0.5–10 AU**. The source's quoted 0.71–2.32 occurrence endpoints give **{global_now['stars_expected']*.71:.1f}–{global_now['stars_expected']*2.32:.1f} reference planets today**, before beam-history and host-population transfer uncertainty. These are sensitivity endpoints for this extrapolation, not a confidence interval for local contacts. The population is not an exhaustive count of all planets. The HZ estimate uses a separate small-planet occurrence model; the populations overlap and must not be added. Fractional values are expectations over unknown planetary systems. <a data-cite="all-occ"></a><a data-cite="g-occ"></a><a data-cite="m-occ"></a>

</div>
</section>

<section id="total-forecast" markdown="1">

## Already-emitted cones keep reaching more planets.

<p class="takeaway">Central estimate: {global_now['volume_ly3']:,.0f} ly³ reached so far. The next year's propagation adds {global_rates[-1]['new_bounded_reference_planets_expected']:.2f} reference planets or {global_rates[-1]['new_hz_planets_expected']:.3f} small HZ planets in expectation.</p>

| Year (Oct 7) | Reference planets | Small HZ planets | Volume (ly³) | Mean /2′ (ly³) |
|---|---:|---:|---:|---:|
{global_table}

<p class="caveat">These are population expectations; catalogue encounters occur intermittently. Numerical precision supports reproducibility and is not observational certainty.</p>

<div class="prose" markdown="1">

“Average cone volume” is standardized as the combined reached volume divided by unique angular area expressed in full-width **2′ beam-disk equivalents**. The current union is {global_now['equivalent_beam_disks']:,.0f} such equivalents, averaging {global_now['average_volume_per_2arcmin_equivalent_ly3']:.4f} ly³ each. These are units of area, not a count of independent transmitting sessions. Wider beams correspond to many units; a moving beam creates a corridor; revisits add no new direction.

Because the beams have different ages, multiplying every direction by one average age would bias the result. Instead each direction keeps its earliest emission date. A short pulse has passed through the interior of its cone even though its photons now occupy a moving shell.

The radar model places first coverage uniformly within an empirical ±{global_model['band_half_width_deg']:.1f}° ecliptic band, covering 95% of the recovered Arecibo angular union. The annual coverage hazard uses **25.9 reference footprints per Arecibo detected target apparition** and **81.4 per Goldstone apparition**. Repeated radar coverage and overlap with spacecraft/message cones are subtracted. Unknown interior years are explicitly interpolated; activity before the first record is omitted. Other radar classes remain uncalibrated. <a data-cite="radar-history"></a><a data-cite="goldstone"></a><a data-cite="ucla"></a>

Historical hardware also changed: some Goldstone tracks used 13-cm radiation rather than 3.5 cm; Arecibo used 70 cm before its upgrade; the 1968 Icarus transmitter was 26 m. Modern area-per-target calibration cannot certify these earlier footprints. The 0.5×–2× scenarios test transfer sensitivity and do not guarantee bounds on the true total. Intentional Altair's modeled 54′ width is an additional assumption (half/double-width alternatives), and its A7 star is outside the G/M HZ calibration. <a data-cite="old-radar"></a><a data-cite="old-aperture"></a><a data-cite="altair-type"></a>

</div>
</section>

<section id="total-rates" markdown="1">

## Old signals add about {global_rates[-1]['new_bounded_reference_planets_expected']:.2f} reference planets over the next year.

<p class="takeaway">The small-HZ projection adds about {global_rates[-1]['new_hz_planets_expected']:.3f} planets in the same year. These arrivals come from signals already in flight.</p>

| Propagation interval from cutoff | New reference planets | New small HZ planets |
|---|---:|---:|
{global_rate_rows}

<p class="caveat">These smooth density-based increments are expected values, not scheduled discrete contacts. Catalogued stars arrive intermittently. No future transmissions are included.</p>

</section>

<section id="new-cones" markdown="1">

## New sky coverage can be extrapolated in a common beam-area unit.

<p class="takeaway">The 2025 Goldstone activity benchmark extrapolates about {benchmark['radar_2025_budget_2arcmin_equivalents']:,.0f} reference footprints/year, or {benchmark['radar_2025_budget_2arcmin_equivalents']/365:.1f}/day, before overlap with all other source families. This is a historical activity benchmark; current operations require their own logs.</p>

| Estimate and scope | New 2′ area equivalents/year | Average/day |
|---|---:|---:|
| Arecibo recovered historical mean, 2002–2019 | {annual_mean:,.0f} | {annual_mean/365.25:.1f} |
| Goldstone 2025 activity-transfer budget | {benchmark['radar_2025_budget_2arcmin_equivalents']:,.0f} | {benchmark['radar_2025_budget_2arcmin_equivalents']/365:.1f} |
| Goldstone continuation scenario, new versus cutoff coverage | {future_initial_rate:,.0f} | {future_initial_rate/365.25:.1f} |
| Continuing DSN scenario, Oct2026–Oct2027, new versus past DSN | {future_dsn_2arcmin:,.0f} | {future_dsn_2arcmin/365:.2f} |

<p class="caveat">The rows describe different periods and baselines and must not be added. Arecibo stopped in 2020; DSS-14 is offline for modernization during 2026–2028. No defensible observed global current “cones/day” total follows from these public records. <a data-cite="schedule"></a></p>

<div class="prose" markdown="1">

Each new 2′ area equivalent is about 0.00087 square degrees. A useful forecast of volume is obtained by retaining the dates of the new coverage, then propagating its front; it is not a fixed volume added per transmission. The table above reports the resulting average volume through time for the cones already emitted. A continuing-transmission scenario would require a future activity schedule, which is distinct from this primary already-emitted forecast.

</div>
</section>

<section id="future-cones" markdown="1">

## Continuing radar activity could add about {future_initial_rate:,.0f} new reference footprints per year.

<p class="takeaway">Hypothetical Goldstone activity after a May 2028 restart, at its 2025 level, initially adds about {future_initial_rate/365.25:.1f} new 2′ area equivalents/day. After 100 years the new cones alone average 0.022 ly³ per unique reference footprint.</p>

| Years after assumed restart | Cumulative new 2′ equivalents | New equivalents/year then | Mean reached volume per new footprint (ly³) | Extra reference / HZ planets |
|---|---:|---:|---:|---:|
{future_cone_rows}

<p class="caveat">This is a separate future-activity scenario, not an observed operating forecast. It holds the central historical model fixed and varies future area transfer by 0.5×–2×. The worldwide current rate remains unknown.</p>

<div class="prose" markdown="1">

Only sky unilluminated in the cutoff model can become a new direction here. Repeated future coverage is removed with the same uniform-band hazard, and the remaining new-direction rate slowly falls as available sky is used. The assumed restart date follows the scheduled modernization interval; actual activity and dates may differ. No other future transmitter is introduced. <a data-cite="schedule"></a>

Newly emitted cones shorter than4.24 ly cannot reach another known stellar system, so their planet projection remains zero initially. Their average cumulative volume grows with time because their pulses continue crossing new space. These additional volumes occupy new angular directions in the adopted model and may be combined with the old-emission projection only at matching dates and with the same conditional assumptions. They are not included in the first curve.

</div>
</section>

<section id="scope" data-document-only markdown="1">

## Reached means physical illumination under the declared model.

<div class="prose" markdown="1">

“Reached” means a signal's leading front crosses a target; it does not imply detection, communication, life, or confirmed habitability. A small planet in a modeled habitable zone (HZ) receives a suitable range of stellar energy; its atmosphere and surface conditions are unknown. In the catalogue estimator the spacecraft model predicts {len(reached)} arrived objects, and the selected intentional records add distinct Altair. Two eligible red dwarfs imply 0.32 expected small HZ planets; this conditions on known hosts and cannot be added to the volume-density estimate.

The source inventory includes five spacecraft directions in a published Deep Space Network (DSN) study, public JPL Goldstone configuration records, recovered Arecibo asteroid transmit-run pages, and selected primary-documented intentional interstellar messages. The selected intentional records add one distinct named target, Altair, with nominal arrival around 2000. Ordinary leakage, military/aircraft radars, sidelobes, lunar/planetary radar, and other message campaigns require additional histories. <a data-cite="dsn"></a><a data-cite="goldstone"></a><a data-cite="ucla"></a><a data-cite="altair"></a>

</div>
</section>

<section id="arrivals" markdown="1">

## Spacecraft beams reach new objects intermittently.

<p class="takeaway">Next nominal arrival: around {next_object.recalculated_arrival_iso[:4]} via {next_object.spacecraft}. The selected model adds {horizon_counts[-1]-len(reached)} objects over the next 100 years.</p>

| Forecast interval | End date (UTC) | Cumulative objects | Newly reached objects |
|---|---|---:|---:|
{horizon_rows}

<div data-document-only data-plot="arrivals"></div>

<p class="caveat">These are conditional geometric-model forecasts, with uncertain dates. No new arrivals in the next year is specific to this inventory. A 100-year average is not a constant daily arrival rate. <a data-cite="dsn"></a><a data-cite="gcns"></a></p>

<div class="prose" markdown="1">

The 100-year mean is {(horizon_counts[-1]-len(reached))/100:.2f} catalogue objects/year, {(horizon_counts[-1]-len(reached))/100*7/365.25:.3f}/week, or {(horizon_counts[-1]-len(reached))/100/365.25:.4f}/day. Actual arrivals are discrete; all three immediate intervals above contain zero arrivals. Unique Gaia objects are not necessarily independent stellar systems.

Selected model: **{dsn_model_label}**. It assumes continuous uplinks during the adopted mission windows and omits the known 2020 Voyager 2 uplink gap. It reconstructs nominal geometry, rather than proving an uplink occurred during each alignment. All forecast rows first filter emission epochs to the past. Fresh six-hour JPL ephemerides and 15-minute refinements replace the original coarse track; spherical geometry and stellar proper-motion conventions are checked. Remaining limitations include incoming geocentric spacecraft directions instead of ground-site outgoing pointings, missing radial velocities, beam power contours, and launch-time continuous-coverage assumptions. The stellar epoch accounts for the incoming catalogue light delay and the outgoing wavefront flight; the final version solves the moving-star interception rather than keeping distance fixed. <a data-cite="horizons"></a><a data-cite="gaia-time"></a>

The earlier chat's 1,296 figure counted star–mission pairs. The author catalogue has 1,278 unique Gaia identifiers, of which 1,277 have past modeled first-emission epochs at this cutoff. Its calendar dates used rounded arrival years. Those preserved paper-reproduction files are separate from the selected reanalysis. The selected reanalysis uses New Horizons' X-band uplink width of 0.038° for a 70-m antenna; the original paper used the 0.128° S-band width for every mission. <a data-cite="dsn-code"></a><a data-cite="nh-band"></a><a data-cite="beam"></a>

</div>
</section>

<section id="intentional" markdown="1">

## The Altair transmission has a nominal arrival around 2000.

<p class="takeaway">Selected primary records identify 17 nearby intentional stellar targets. Altair is the one whose nominal intended-target arrival predates the cutoff; none of these targets has a new arrival in the next day, week, or year.</p>

| Selected named target | Earliest recorded date | Nominal intended-target arrival |
|---|---|---|
| Altair / α Aql | 1983-08-15 | ~2000 |
| HIP 74995 / Gliese 581 | 2008-10-09 | ~2029 |
| GJ 273 / Luyten's Star | 2017-10-16 | ~2030 |
| HIP 4872 | 2003-07-06 | ~2036 |

<p class="caveat">These are intended-target travel-time estimates from date-only records and rounded distances, not reconstructed beam intersections or observed reception. The selected table is not an exhaustive intentional-message history. <a data-cite="messages"></a><a data-cite="altair"></a><a data-cite="sonar"></a></p>

<div class="prose" markdown="1">

The 1983 record describes a one-hour Stanford 46-m transmission aimed at Altair, approximately 16.7 ly away. Date-plus-distance arithmetic puts its nominal arrival around 2000. Altair is distinct from the four current DSN-model objects, giving **five named/modelled objects** in the combined current inventory under their respective assumptions. The reconstructed Arecibo archive adds no current nearby-catalogue object. This bounded count cannot establish the worldwide total.

The saved intentional table contains 21 date-target sessions, 17 distinct nearby stars and the additional M13 globular-cluster target. Source-rounded arithmetic predicts three additional selected stellar targets over ten years and 16 over 100 years. These should not be added to future DSN or radar catalogue totals without identifier cross-matching. Altair is an A7V star; the Sun-like G-star and M-dwarf HZ occurrence calibrations do not apply to it. <a data-cite="altair-type"></a>

Sónar's actual 2017 transmissions were on October 16–18, preceding the November announcement. The source's 12.4-ly distance places the first nominal arrival around 2030. M13's approximately 25,000-ly travel time places the intended-cluster arrival around year 26,974; foreground beam encounters were not reconstructed here.

| Named stellar target | Earliest transmission date | Rounded source distance (ly) | Nominal arrival year |
|---|---|---:|---:|
{intentional_rows}

</div>
</section>

<section id="planets" markdown="1">

## Host stars need different planet-occurrence estimates.

<p class="takeaway">Conservative estimates give 0.38–0.63 small HZ planets per Sun-like G star and about 0.16 per early M dwarf; these are mean planet counts with broad uncertainty.</p>

| Host / occurrence model | Mean planets per star | Published uncertainty | Planet radius |
|---|---:|---|---|
| G star, lower completeness model | 0.38 | 68% credible interval 0.16–0.88 | 0.5–1.5 Earth radii |
| G star, upper completeness model | 0.63 | 68% credible interval 0.25–1.57 | 0.5–1.5 Earth radii |
| Early M dwarf, conservative HZ | 0.16 | Approximate 68% interval 0.09–0.33 | 1.0–1.5 Earth radii |

<p class="caveat">Different radius definitions prevent interpreting the mixed population as one uniform rocky-planet selection. An occurrence rate is not the fraction of stars that host a planet, nor the fraction with inhabited planets. <a data-cite="g-occ"></a><a data-cite="m-occ"></a></p>

<div class="prose" markdown="1">

The four reached objects in the original model are GJ 1276 (white dwarf), GJ 1154 (M dwarf), 2MASSW J1507476-162738 (brown dwarf), and GJ 359 (M dwarf). Applying the M-dwarf calibration to the two eligible hosts gives **2 × 0.16 = 0.32 expected conservative-HZ planets**; the optimistic-HZ model gives 0.48. White and brown dwarfs are excluded from these occurrence calibrations, rather than asserted incapable of planets. This remains conditional on the modeled exposure and on applying the early-M result to these hosts. <a data-cite="dsn"></a>

Dressing & Charbonneau's selected cool-dwarf sample spans 2,661–3,999 K, with median 3,746 K and mostly early M dwarfs. Transferring its population mean to these M4/M4.5 hosts adds an unquantified population assumption; 0.32 is an expected planet count under that transfer, not a measurement of their planets. <a data-cite="m-occ"></a>

| Probe direction | Gaia identifier | Distance (pc) | Nominal model arrival |
|---|---|---:|---|
{reached_rows}

The local 10-pc census yields {p['stellar_density_pc3']:.4f} ordinary stars/pc³ and {p['stellar_system_density_pc3']:.4f} systems containing ordinary stars/pc³. M-dwarf and F/G/K counts give a central conservative small-HZ-planet density of **{p['hz_planets_density_pc3']:.4f} planets/pc³**, equivalent to about {p['mixed_hz_planets_per_star']:.2f} per ordinary star. The conservative upper median gives {p['hz_planets_density_conservative_upper_median_pc3']:.4f}/pc³. An endpoint sensitivity spans {p['hz_planets_density_low_sensitivity_pc3']:.4f}–{p['hz_planets_density_high_sensitivity_pc3']:.4f}/pc³; this combines marginal source endpoints and is **not a joint credible interval**. Binary suppression, local population transfer, and incomplete classifications are unquantified limitations. <a data-cite="census"></a>

</div>
</section>

<section id="directions" markdown="1">

## Radar runs often revisit the same sky.

<p class="takeaway">The retrieved June–September 2025 Goldstone subset contains 4,323 runs and approximately {area['equivalent_beam_disks']:,.0f} beam-disk equivalents of unique nominal angular coverage.</p>

<div data-plot="angular"></div>

<p class="caveat">This is new coverage within the retrieved subset, starting from an empty inventory. Historical beams may already have covered these directions. Reception/configuration windows give a nominal tracking envelope, rather than every actual pulse. <a data-cite="goldstone"></a><a data-cite="radar-beam"></a></p>

<div class="prose" markdown="1">

A “new direction” is defined here by the incremental union of circular half-power beam footprints. Its area divided by one 1.92-arcminute beam disk is an **equivalent number of beam disks**, which may be fractional. It is not a count of sessions, targets, or disjoint cones. Tracking can sweep many beam widths; repeated pointings can add no new area.

The 123 configuration windows cover 16 targets, 19 observing dates, and 30 target-days. Their total span is 71.1 hours of receive/configuration windows, not 71.1 transmitter-on hours. The angular union is {area['coverage_sr']:.6g} steradians, or {area['coverage_sr']/(4*3.141592653589793)*100:.4f}% of the sky. Monte Carlo integration standard error is {area['coverage_mc_se_sr']:.2g} sr; unresolved pulse gaps and historical pointing offsets produce additional source uncertainty.

Dividing by the {days}-day calendar interval gives **{rate:.1f} equivalent new beam disks/day**, or **{rate*365.25:,.0f}/year if that sparse sample were repeated at the same rate**. This is an illustrative sample-rate scaling, not measured annual global activity. Nine windows with setup/pointing warnings remain in the nominal envelope; their exclusion is provided in the numerical sensitivity results.

</div>
</section>

<section id="archive-arrivals" markdown="1">

## Recovered Arecibo beams have no current catalogue arrivals.

<p class="takeaway">The recovered archive contains {archive['reconstructed_transmit_intervals']:,} usable transmit intervals across {archive['reconstructed_targets']:,} targets. Its nominal nearby-catalogue match has {radar_match['unique_reached_nominal_sources']} arrivals today and {radar_match['forecasts_new_unique_sources']['one_year']} in the next year.</p>

| Forecast interval | New nearby catalogue objects | Expected new ordinary stars, volume model | Expected new small HZ planets, volume model |
|---|---:|---:|---:|
{radar_forecast_rows}

<p class="caveat">Catalogue objects and homogeneous-density expectations are different estimators. Zero catalogue matches is conditional on nominal pointing reconstruction, the chosen beam contour, and catalogue completeness. <a data-cite="ucla"></a><a data-cite="gcns"></a></p>

<div class="prose" markdown="1">

Systematic retrieval recovered {archive_audit['parsed_raw_runs']:,} raw rows from 834 advertised per-object run pages. Removing {archive_audit['exact_duplicate_rows']:,} identical 22-field measurement duplicates leaves {archive_audit['canonical_unique_runs']:,} distinct measurements, of which {archive_audit['valid_verified_transmit_windows']:,} have verified transmitter start/end times. The other {archive_audit['missing_or_invalid_transmit_times']:,} rows remain in the audit. Usable intervals span August 2001–June 2020, all at 2.38 GHz. Their summed duration is {archive_audit['transmission_hours']:,.1f} recorded window-hours; removing UTC overlaps gives {archive['transmit_time_audit']['union_duration_hours']:,.1f} hours of window coverage. Overlapping archive representations are not counted as independent transmitter time. This retrieves {archive_audit['fraction_of_advertised_count_recovered']*100:.1f}% of the advertised run count; no contact estimate is scaled by that percentage.

Ground-site outgoing directions include light-time point-ahead and sample recorded transmit intervals at no more than 15″ spacing for the nominal 60″ radius. UCLA's date is anchored at receiver start; 72 midnight-crossing transmit windows were shifted to the previous day using that documented convention. Current JPL orbit solutions reconstruct the intended tracking; original antenna offsets and power logs are unavailable. Residual simultaneous cross-target records involve 92 interval keys across 13 targets; the nominal archive envelope retains them and an exclusion sensitivity is saved separately. This cannot certify both incompatible pointings occurred. The union contains approximately {archive_now['equivalent_beam_disks']:,.0f} two-arcminute beam-disk equivalents. Its current cumulative volume is {archive_now['volume_ly3']:.2f} ly³, giving **{archive_now['stars_expected']:.3g} expected ordinary stars** and **{archive_now['hz_planets_expected']:.3g} expected small HZ planets** under the local homogeneous-density model. These are spatial expectations, rather than fractional catalogue observations.

The catalogue calculation uses {radar_match['median_distance_within_100pc_rows']:,} GCNS objects with median distance at most 100 pc. It predicts {radar_match['forecasts_new_unique_sources']['ten_years']} new objects over ten years and {radar_match['forecasts_new_unique_sources']['hundred_years']} over 100 years. Eventually {radar_match['unique_eventual_nominal_sources']} nominal catalogue sources intersect the sampled beams; expanding the radius by 15″ gives {radar_match['unique_eventual_grazing_sensitivity_sources']} in a grazing sensitivity. That expansion diagnoses sampling at edges and is not a certified uncertainty interval. White/brown dwarfs and components are included in catalogue-object counts, so multiplying that total by an ordinary-star occurrence rate would be invalid. The density model independently gives {archive_future['stars_expected']:.2f} ordinary stars and {archive_future['hz_planets_expected']:.2f} small HZ planets by 2126.

</div>
</section>

<section id="archive-directions" markdown="1">

## Historical new sky can be measured from dated radar runs.

<p class="takeaway">Within the recovered Arecibo inventory, complete calendar years 2002–2019 averaged {annual_mean:,.0f} new two-arcminute beam-disk equivalents/year, or {annual_mean/365.25:.1f}/day.</p>

<div data-plot="archive-directions"></div>

<p class="caveat">This is a historical subset rate, starting from an empty 2001 inventory. It does not establish globally untouched sky, full-archive activity, or today's operational rate. <a data-cite="ucla"></a></p>

<div class="prose" markdown="1">

| Calendar year | New 2′ beam-disk equivalents | Average/calendar day |
|---:|---:|---:|
{annual_rows}

“New” means sky area first covered within this recovered dated inventory. A continuous tracking sweep creates a ribbon of angular coverage, so the number of cones depends on the declared beam footprint convention. The annual calculation removes angular overlap across years. Individual run counts, target counts, and beam-disk equivalents answer different questions.

</div>
</section>

<section id="radar-arrivals" markdown="1">

## Recent radar fronts cover little interstellar volume.

<p class="takeaway">The 2025 Goldstone sample reaches no other stellar system by today or the next year: its front is still inside the nearest-star distance. The two recovered Arecibo apparitions have zero current catalogue matches.</p>

| Recovered radar inventory | Current catalogue arrivals | Nominal future result |
|---|---:|---|
| Goldstone, 2025 subset | 0; front shorter than 1.4 ly | Density-model expectation ≈{g100['stars_expected']:.2f} stars by 2126 |
| Arecibo, DP107 2008/2016 | 0 | One nearby-catalogue star nominally around 2156 |

<p class="caveat">Arecibo is a selected asteroid case, not the complete archive. A density expectation can be fractional; the actual nearby catalogue is discrete and spatially clustered. <a data-cite="arecibo-runs"></a><a data-cite="gcns"></a></p>

<div class="prose" markdown="1">

The Arecibo case has 449 actual transmit windows, 9.04 transmitter-on hours, and nominal outgoing directions reconstructed with JPL Horizons. Four 2008 rows lacking transmitter times remain in the raw data and are explicitly excluded from the geometric reconstruction. The combined nominal sky union is approximately {a['equivalent_beam_disks']:.0f} two-arcminute beam disks. The current homogeneous-density expectation is only {a['stars_expected']:.2g} ordinary stars and {a['hz_planets_expected']:.2g} small HZ planets; the catalogue finds zero. These values are an expectation under spatial randomization, rather than a claim of fractional observed stars.

Forecast tables provide cumulative ordinary stars, stellar systems, small-HZ planets, G-star-only HZ planets, and increments over the next day, week and calendar year. For example, at 2126 the 2025 Goldstone envelope gives {g100['new_stars_next_year']:.4f} expected new ordinary stars in its following year, {g100['new_stars_next_week']:.2g}/week, or {g100['new_stars_next_day']:.2g}/day; expected HZ planets scale by the defined population mixture. This smooth rate describes a density model, while the DSN table forecasts discrete catalogue arrivals.

</div>
</section>

<section id="scenarios" markdown="1">

## Beam age and angular coverage determine reach.

<p class="takeaway">Even 100,000 distinct fixed two-arcminute beams aged 60 years reach only about 4.6 ordinary stars and 0.9 small HZ planets in a homogeneous local-density model.</p>

<div data-plot="scenario"></div>

<p class="caveat">The number and ages of real independent directions are unknown. These are explicit sensitivity scenarios, not a fitted global estimate or an upper bound on moving beams. <a data-cite="census"></a></p>

<div class="prose" markdown="1">

| Assumed distinct fixed beams | Signal age (years) | Ordinary stars expected | Small HZ planets expected | New ordinary stars in next year |
|---:|---:|---:|---:|---:|
{case_rows}

The full 84,054-run Arecibo count cannot be substituted for the first column. Each run has a different time, duration and swept footprint; runs overlap and one run may traverse many beam widths. An all-source estimate needs the dated angular union, rather than a tally of radar records. Nor can one use a 12,000-ly cone as the current frontier: a 1960s signal has traveled only about 60 ly.

</div>
</section>

<section id="current" markdown="1">

## Today's global transmission rate remains unresolved.

<p class="takeaway">Arecibo sends no new beams. JPL lists Goldstone DSS-14 offline for modernization from March 2026 to May 2028. Other antennas and facilities prevent inferring a zero global rate.</p>

<p class="caveat">The available history counts detections and scheduled observations, not all transmissions or previously untouched directions. <a data-cite="schedule"></a><a data-cite="radar-history"></a></p>

<div class="prose" markdown="1">

The JPL detection history contains 2,082 station–apparition rows across 1968–2026. Goldstone-family distinct detected targets number 55 in 2024, 41 in 2025, and one in the retrieved 2026 snapshot. These are not independent cones, and transmissions producing no echo are absent. Scheduled observations may be cancelled. The worldwide new-direction/day/year quantity remains unresolved for DSN uplinks to all spacecraft, other planetary-radar facilities, and additional radar types.

Even all 84,054 advertised UCLA asteroid runs would omit lunar/planetary targets, failed observations, and other facilities. Required fields are target, UTC transmitter-on/off times, site, frequency/power, original pointing or orbit-predicts, and beam offsets. Actual DSN uplink duty logs are needed to test its continuous-transmission model.

For a conditional estimate of continuing spacecraft beams, the next table assumes continuous tracking from October 7, 2026 to October 7, 2027. New coverage is measured against **all five modeled past spacecraft tracks**, with each mission's own beam width. It is not compared with every historical human transmission.

| Mission | Full beam width | New native beam-disk equivalents/year | Average/day |
|---|---:|---:|---:|
{direction_rows}

The combined increment is approximately **{direction_area_deg2:.2f} square degrees/year**, or {direction_area_deg2/365:.4f} square degrees/day. The mission footprints are widely separated. Native beam-disk equivalents have different widths and cannot simply be summed; sky area provides the common unit. This scenario assumes a 70-m antenna, continuous uplink duty, and geocentric incoming spacecraft directions. It estimates geometry under those assumptions, not a measured current operations rate. <a data-cite="beam"></a><a data-cite="horizons"></a>

</div>
</section>

<section id="methods" data-document-only markdown="1">

## Methods and the meaning of a light cone

For a fixed beam with half-angle α and signal age τ in years:

```
Ω = 2π (1 − cos α)                 solid angle (steradians)
R = τ light-years                 leading-front radius
V_ever = Ω R³ / 3                 cumulative swept volume (ly³)
E[stars] = n_stars × V_union       compatible volume units required
E[HZ planets] = V_union × (n_M η_M + n_FGK η_FGK)
dE[stars]/dt = n_stars × Ω R² c    one nonoverlapping fixed beam
t_arrival ≈ t_emission + distance/c
```

A pulse emitted over an interval occupies a thin radial shell at a given time. “Ever touched” includes the interior through which that shell has already passed. It does not mean those stars are still receiving photons. The volume calculations remove the known empty region within 4.24 ly of the Sun; they are local-population expectations beyond it.

For moving beams, the study samples actual transmit intervals (Arecibo), nominal configuration envelopes (Goldstone), or continuous-tracking models (DSN). Dense points are no more than one quarter of the beam radius apart. A cap-mixture sampler chooses disks in proportion to their individual solid angles and weights each ray by the sum of all disk areas divided by its overlap multiplicity. The earliest included emission on a ray determines its leading front. This removes repeated angular coverage and earlier physical illumination in the defined disk inventory. Numerical integration uses 120,000 samples with analytical identical/disjoint/mixed-width controls, independent-seed checks of the radar union, and beam-width sensitivity. Discretized tracks still differ slightly from continuous tracks.

The radar-history extrapolation uses a first-coverage hazard g(t)/B in an ecliptic band of area B. Its first-emission density is [g(t)/B]exp(−∫g/B). Annual 16-node Gauss–Legendre quadrature integrates this density against the reached volume per ray. The retained DSN/message union is added; the expected minimum of the two fronts is subtracted on shared directions. Thus neither repeated radar coverage nor overlap with the backbone is counted twice. Arecibo's area-per-target calibration already measures new coverage within its recovered history; applying the band hazard is a further explicit cross-family/older-history overlap approximation.

Density-based forecasts describe expectations under a homogeneous local population. Catalogue-based forecasts identify particular modeled targets; they are separate estimators and should not be summed as a global census. A directional Galactic population model is required for kiloparsec projections. A beam's half-power contour is a declared geometric convention, not a hard electromagnetic edge.

The stellar centre is used as a proxy for planets orbiting it. At interstellar distances the nominal footprints are much larger than typical HZ orbits, but a grazing stellar-centre alignment does not guarantee that every planet is inside the chosen contour. Orbital phases and individual planetary positions were not modeled.

Geometric illumination also differs from detectability. Sheikh et al.'s conditional maxima use a receiver in the beam, matched bandwidth, sufficient integration and optimistic near-term telescope sensitivity: approximately 12,000 ly for former Arecibo planetary radar and 65 ly for DSN uplinks. They cannot be assigned to all waveforms/facilities, or mistaken for distances already traveled. <a data-cite="detectability"></a>

</section>

<section id="provenance" data-document-only markdown="1">

## Editable source, data and verification

Analysis cutoff: **2026-10-07 00:00 UTC**. All source archives were retrieved for this study. Numerical results are traceable to saved JSON/CSV exports and documented Python functions managed with uv. The selected DSN source is `{dsn_catalog}`. Independent review covers scientific assumptions, arithmetic, source alignment, rendered layout and controls; unresolved inventory limitations remain explicit.

Download the [source Markdown](report.md), [build manifest](build.json), [combined recovered timeline](data/combined_recovered_timeline.csv), [historical extrapolation timeline](data/global_extrapolated_timeline.csv), [day/week/year arrivals](data/global_arrival_rates.csv), [global model manifest](data/global_extrapolation_summary.json), [future new-cone scenario](data/future_new_cones_scenario.csv), [future-scenario manifest](data/future_new_cones_scenario_summary.json), [annual activity calibration](data/radar_activity_calibration.json), [explicit year imputations](data/global_activity_gapfill.csv), [population parameters](data/population_parameters.json), [DSN arrival forecast](data/dsn_selected_timeline.csv), [intentional target sessions](data/intentional_target_sessions.csv), [Goldstone volume forecasts](data/goldstone_volume_timeline.csv), [Arecibo archive volume forecasts](data/arecibo_archive_volume_timeline.csv), [Arecibo annual new directions](data/arecibo_archive_annual_new_directions.csv), [Arecibo catalogue matches](data/arecibo_earliest_source_arrivals.csv), [Arecibo case forecasts](data/arecibo_volume_timeline.csv), [future DSN direction scenario](data/dsn_future_direction_scenario.json), [historical scenarios](data/historical_fixed_beam_scenarios.csv), and [assumptions and source limitations](data/ISSUES.md).

The complete local project also retains raw archives, cached JPL requests/responses, primary papers, preserved original DSN results, alternative beam-width/epoch models, and the independent review record. No data points were inferred from screenshots. Plotly is embedded so this single HTML works offline; its runtime adds several megabytes.

</section>
'''
    if rewrite_source or not (ROOT/"source/report.md").exists():
        (ROOT/"source/report.md").write_text(report)
    attachments = {"data/population_parameters.json": (ROOT/"data/population_parameters.json").read_bytes(),
                   "data/ISSUES.md": (ROOT/"ISSUES.md").read_bytes(),
                   "data/intentional_target_sessions.csv": (ROOT/"data/intentional/intentional_target_sessions.csv").read_bytes(),
                   "data/arecibo_earliest_source_arrivals.csv": (ROOT/"data/radar/bulk_gcns/earliest_source_arrivals.csv").read_bytes()}
    for name in ["dsn_selected_timeline.csv", "goldstone_volume_timeline.csv", "arecibo_volume_timeline.csv", "historical_fixed_beam_scenarios.csv", "arecibo_archive_volume_timeline.csv", "arecibo_archive_annual_new_directions.csv", "dsn_future_direction_scenario.json", "combined_recovered_timeline.csv", "global_extrapolated_timeline.csv", "global_arrival_rates.csv", "global_extrapolation_summary.json", "radar_activity_calibration.json", "global_activity_gapfill.csv", "future_new_cones_scenario.csv", "future_new_cones_scenario_summary.json"]:
        attachments["data/"+name] = (ROOT/"results"/name).read_bytes()
    metadata = {"title": "RadioContacts", "subtitle": "Dated beam geometry, expected habitable-zone planets, and the limits of the recovered transmission inventory", "author": "Prepared with Codex · public-data study", "date": "2026-10-07", "version": "", "references": reference,
                "analysis_revision_sha256": hashlib.sha256((ROOT/"analysis.py").read_bytes()).hexdigest(),
                "render_revision_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "selected_dsn_catalog": dsn_catalog,
                "selected_dsn_catalog_sha256": hashlib.sha256((ROOT/dsn_catalog).read_bytes()).hexdigest(),
                "arecibo_archive_summary": archive,
                "arecibo_catalogue_match_summary": radar_match,
                "intentional_target_summary": intentional,
                "combined_inventory_summary": combined,
                "global_extrapolation_summary": global_model,
                "future_new_cones_summary": future_cones_summary,
                "future_scenario_code_sha256": hashlib.sha256((ROOT/"forecast_new_cones.py").read_bytes()).hexdigest(),
                "source_sha256": s["source_sha256"],
                "dependencies": {name: importlib.metadata.version(name) for name in ["numpy", "pandas", "scipy", "Markdown", "beautifulsoup4", "plotly"]},
                "verification_scope": "Analytical geometry controls, independent-seed integration, raw-source row audits, model sensitivity, independent scientific and rendered-artifact review; global historical inventory incomplete"}
    output = render_report(ROOT/"source", ROOT/"report.html", metadata, plots, attachments)
    return output
