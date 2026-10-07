# RadioContacts

This local study estimates **geometric illumination**, not detection or communication. Its cutoff is 2026-10-07 at 00:00 UTC. Open `report.html` for the self-contained interactive report; `source/report.md` is its editable scientific source.

The first result is the cumulative planet projection through time across the combined dated beam union. The inventory contains five idealized spacecraft uplink tracks, selected intentional messages, JPL Goldstone configuration logs, and74,201 usable Arecibo asteroid transmit windows. A separate annual-activity extrapolation replaces the incomplete radar geometry, removes overlap with the retained spacecraft/message beams, and reports volume per standardized unique2′ footprint. This is not a complete worldwide transmission census.

## Reproduce the calculations

Use the [full reproducibility bundle](https://github.com/jkobject/jkobject.github.io/releases/download/radiocontacts-2026-10-07/RadioContacts-reproducibility.zip) for the commands below. The smaller code ZIP contains the functions, renderer and editable source, but no scientific datasets.

The project uses uv with pinned dependencies in `pyproject.toml` and `uv.lock`. Run commands from this directory. These commands call documented Python functions; they do not require a standalone analysis script.

```sh
uv sync --locked
uv run python -c 'from analysis import run_study; run_study()'
uv run python -c 'from analysis import analyze_arecibo_archive; analyze_arecibo_archive()'
uv run python -c 'from analysis import forecast_dsn_direction_area; forecast_dsn_direction_area()'
uv run python -c 'from data.radar.radar_activity_schedule import radar_activity_schedule; radar_activity_schedule(".")'
uv run python -c 'from combined_model import build_combined_inventory, extrapolate_radar_history; build_combined_inventory(); extrapolate_radar_history()'
uv run python -c 'from forecast_new_cones import forecast_new_cones; forecast_new_cones()'
uv run python -c 'from build_report import render_study_report; render_study_report("data/dsn/dsn_corrected_unique_objects_mixed_xband_linear_intersection_extended.csv", "Nominal 70-m model: S-band for four probes, X-band for New Horizons; Gaia light-arrival correction, moving-star interception, continuous modeled uplinks")'
```

Rendering uses the bundled Markdown/Plotly renderer in `renderer/`. The exported HTML requires no Python, server, or external JavaScript at runtime. A local HTTP preview is useful when browser policy disallows `file://` URLs.

Edit `source/report.md` and call `render_study_report(...)` to rebuild while preserving your narrative changes. To regenerate the initial narrative from the numerical template, explicitly pass `rewrite_source=True`; this overwrites Markdown edits. Figures, references and downloadable data are supplied by the same render function in either case.

## Functions and evidence

- `analysis.py`: fixed-cone expectations, overlap-corrected dated angular unions, analytical checks, recovered Arecibo volume/annual-direction integration, future DSN direction scenarios, and initial Goldstone/case calculations.
- `combined_model.py`: mixed native-width combined union; historical first-coverage radar hazard; overlap-subtracted cumulative volume, reference/HZ planet timelines, average footprint volume, and day/week/year increments.
- `forecast_new_cones.py`: a separate hypothetical post-modernization Goldstone scenario for future new directions and their average swept volume, excluding sky covered at the historical cutoff.
- `data/radar/radar_activity_schedule.py`: annual target-apparition proxy and calibrated area budgets. The saved imputation table makes unknown-year assumptions explicit.
- `data/dsn/corrected_dsn_match.py`: spherical stellar matching, catalogue epoch conventions, positive moving-wavefront intersections, and explicitly named model variants. `dsn_notes.md` explains deviations from the published model.
- `data/radar/reconstruct_bulk_beams.py`: verified transmitter-interval snapshots and outgoing, ground-site, point-ahead beam reconstruction. Every cached Horizons request retains its query and response.
- `data/radar/match_bulk_gcns.py`: discrete nearby-catalogue matching of the reconstructed Arecibo rays, with a grazing-edge sensitivity.
- `data/population_parameters.json` and `data/occurrence_notes.md`: stellar census denominators, published planet-occurrence definitions, and uncertainty assumptions.
- `data/radar/bulk_ucla/`: raw 22-field run records, target identity checks, request manifests, and the final retrieval audit. Measurement-level duplicates and missing transmitter times are retained and audited.
- `results/`: exact forecast tables, sampled unions, annual increments, and summarized numerical controls.
- `ISSUES.md`: material limitations and implementation repairs. `review/` records the independent scientific and rendered-artifact review.

The final manifest records SHA-256 hashes and dependency versions. Intermediate files whose names contain `checkpoint`, `case_validation`, or `without_catalog_light_time` are diagnostic variants and are not the selected final analysis.

Frozen source contents are checked with SHA-256 rather than requiring the original machine's paths or file timestamps. The full reproducibility archive includes the scientific data and cached API records. Downloaded papers/manuals are linked at their original source URLs instead of redistributed; see `SOURCE_REFERENCES.json` and the report bibliography.

## Interpret the results

A radar pulse occupies a shell now, but “ever touched” counts the cumulative volume its leading front has crossed. Multiple dates and directions must be integrated jointly: repeated runs cannot be added as independent cones. A “beam-disk equivalent” is angular area divided by one declared full-width half-power disk and can be fractional.

Planet occurrence is a **mean number of planets per star**, not the probability of life. Small habitable-zone planets are not confirmed habitable planets. The G-star and M-dwarf calibrations use different radius selections. Catalogue sources include ordinary stars, white dwarfs, and brown dwarfs; they are not automatically independent stellar systems or eligible hosts for the same occurrence calibration.

Future rates in the density model are expectations. Catalogue arrivals are discrete and conditional on source and astrometric assumptions. The worldwide current rate remains undetermined without additional historic pointing records and actual DSN uplink duty logs.

The main forecast propagates only emissions through the cutoff. Its future angular area is constant, while reached volume grows. Continuing DSN directions and the2025 Goldstone annual activity benchmark are reported separately. The broader planet reference uses Cassan's finite5-Earth-mass–10-Jupiter-mass,0.5–10AU population, not an exhaustive all-planet average; it cannot be added to the HZ estimate.
