---
title: "RadioContacts"
excerpt: "How many planets have Earth's directed radio beams reached? A dated, overlap-corrected study with interactive forecasts and reproducible Python code."
date: 2026-10-07
tags:
  - astronomy
  - Python
  - data-analysis
toc: false
---

[Open RadioContacts](/radiocontacts/){: .btn .btn--primary}

RadioContacts estimates how many planets Earth's directed radio transmissions have physically reached, and how that number changes as signals travel outward.

The study combines five modeled spacecraft uplink tracks, recovered Arecibo transmit records, Goldstone observing logs and selected intentional interstellar messages. It accounts for overlapping beams and transmission dates, then applies published stellar densities and planet-occurrence estimates.

Interactive figures show cumulative planet estimates, day/week/year arrival forecasts, new sky coverage and average cone volumes. A separate scenario estimates future coverage if Goldstone resumes at its 2025 activity level.

The results are conditional on beam geometry, modeled spacecraft uplink duty and population transfer. Incomplete worldwide transmission histories leave the global total uncertain. Small planets in a modeled habitable zone are not confirmed habitable or inhabited planets.

## Code and data

- [Browse the Python code and bundled renderer](https://github.com/jkobject/jkobject.github.io/tree/master/radiocontacts/code)
- [Download the code and editable report source](/radiocontacts/RadioContacts-code.zip)
- [Download the full reproducibility archive: code, data, results and cached API records](https://github.com/jkobject/jkobject.github.io/releases/download/radiocontacts-2026-10-07/RadioContacts-reproducibility.zip)
- [Download manifest and archive checksums](/radiocontacts/publication_manifest.json)

The full archive is approximately 225 MB compressed. Dependencies are pinned and managed with `uv`; the renderer is included. Original papers and third-party software are linked to their sources, while the scientific data and the study's analytical functions are included.
