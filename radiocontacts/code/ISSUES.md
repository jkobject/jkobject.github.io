# Data and analysis issues

## Published encounters are not logged transmissions

The referenced chat described 1,296 Deep Space Network (DSN) encounters as trajectories already sent. The primary study instead assumes continuous uplinks beginning at spacecraft launch, includes future ephemerides, and counts star–spacecraft pairs. Preserve the published model separately from observations, deduplicate Gaia identifiers, and filter modeled emission dates against 2026-10-07. Exact exposure requires real uplink logs.

## Calendar arrival dates cannot be recovered from rounded arrival years

The upstream reach_year field discards the first-emission month/day and uses a rounded parsec/light-year conversion. Compute arrival from its complete emission date and distance with an exact unit conversion; label underlying temporal and astrometric uncertainty.

## Public Goldstone blocks contain reception intervals

The public 2025 master logs describe configuration/reception spans and counts of transmit–receive cycles, rather than timestamps for every outgoing pulse. Treat reconstructed tracking within these blocks as a possible angular envelope. Do not claim continuous emission throughout reception intervals or interpret an envelope as a measured pulse log.

## Observation counts are not unique directions

Individual runs and asteroid detections can repeat the same sky footprint. Count the union of beam disks and express its solid angle in units of one beam disk. This gives an equivalent angular coverage, not a number of independent observing sessions.

## The local volume around the Sun is not uniformly populated

A homogeneous density would predict fractional stars within a newly transmitted cone shorter than a light-year. There are no other stellar systems within approximately 4.24 light-years. Report this deterministic near-neighbor constraint separately from the large-scale density expectation.

## Current operations differ from the 2025 sample

The live JPL schedule lists DSS-14 modernization during 2026-03-01–2028-05-01. Historical sample coverage must not be extrapolated as a measured 2026 global transmission rate. Other antennas and facilities require separate logs.

## Long forecasts exceed nanosecond datetime limits

Pandas' nanosecond timestamps cannot represent arrivals after April 2262. The input contains legitimate dates into the 24th century. Validate complete ISO timestamps using Python datetime and compare their chronological ISO representations for the DSN timeline. Calculate geometric time intervals using floating-point epoch seconds, rather than requesting out-of-range nanoseconds. No source rows are discarded.

## Interpolated pointing timestamps contain fractional seconds

Source timestamps have integer seconds; dense-track interpolation adds fractional seconds. Pandas inferred an integer-only format from the first row and rejected valid subsequent rows. Use the explicit ISO8601 parser for all pointing timestamps. Do not coerce failures to missing values.

## Catalogue astrometric epochs refer to light arrival

Gaia's apparent astrometry is referenced to light arriving at the Solar-System barycentre, not a simultaneous distant physical star position. The selected model includes this incoming light delay and solves the positive outgoing moving-star interception. Missing radial velocities are set to zero and counted; beam-width and epoch variants remain available. The DSN source directions are still incoming geocentric spacecraft coordinates, whereas the radar reconstruction uses ground-site outgoing point-ahead directions.

## Archive identities and duplicate representations require separate audits

Some historic packed target aliases require a numeric permanent-number fallback. Only returned page headers agreeing with a canonical JPL identity are accepted. A run identifier alone is not unique across years or waveform/calibration records. The final audit distinguishes raw rows, exact 22-column measurement duplicates, and outgoing-interval representations. Receiver metadata variations in missing-transmitter records do not change usable interval counts.

## Reconstructed orbit solutions are not original pointing logs

UCLA transmit start/end times are actual recorded transmitter windows, but pointing directions are reconstructed from current JPL orbital solutions and nominal tracking. Historical antenna offsets, old orbit predicts, power, waveform detectability, and exact beam contours remain uncertain. Sampling is at most 15 arcseconds apart for a 60-arcsecond beam radius; a grazing-edge sensitivity addresses discretization, not all historical pointing uncertainty.

## Source completeness cannot scale the geometric result

The ratio of recovered runs to the UCLA advertised 84,054 describes retrieval coverage. It is not a contact multiplier: unrecovered records can repeat already illuminated directions or have different ages and target distributions. The recovered archive begins in 2001 and does not establish Arecibo's earlier angular history.

## UTC dates are anchored at receiver start

UCLA defines `utdate` as the UT date at `RXup`, not at `TXup`. The transmitter clocks must be placed relative to that receiver-date anchor; 72 midnight-crossing windows were initially one day late. Their raw clocks are preserved and corrected geometry is rebuilt. Run identifiers are not used to infer a date without documented semantics. Residual overlapping records require a source-conflict audit; summed run durations differ from the UTC union and are not independent transmitter-on hours.

## API retrieval follows the primary service's fair-use rule

JPL documents one request at a time. The bulk reconstruction uses a shared process lock, a product/version/contact User-Agent, cached responses, and bounded backoff for selected server/throttling failures. Early parallel requests were stopped and replaced with serialized retrieval. No final geometry is accepted from an HTTP error response.

## Combined volume is a population projection with conditional source models

The mixed-width union includes continuous modeled DSN tracks and assumed message contours alongside recorded/reconstructed radar windows. It integrates earliest dates on each ray, rather than adding source-specific counts or session counts. The density projection and named-host estimator are separate and must not be added. Targeting known stars violates the random-direction premise of a density estimate; individual star classifications supply a separate conditional check.

## Historical radar extrapolation replaces the recovered radar component

The annual JPL detected-target-apparition proxy is calibrated from modern recovered geometry. A uniform first-coverage hazard in the empirical95% Arecibo ecliptic band extrapolates the dated angular history. It is an alternative radar estimator, not a missing-data increment added on top of all recovered radar beams. Min-front overlap with the retained DSN/message union is subtracted. Missing interior years are interpolated and saved; activity before the first record and uncalibrated transmitter classes remain omitted. The partially populated2026 source catalogue does not establish2026 operational activity.

Historical antenna diameters/frequencies changed. The explicit0.5/1/2 area-transfer scenarios do not guarantee bounds for those changes, failed-echo observations, lunar/planetary radar, military/aircraft radar, omitted messages, or other transmitters. The dominant DSN continuous-duty and70-m beam assumptions also lie outside that band.

## Planet definitions and source uncertainties remain separate

Cassan's mean1.6 (quoted endpoints0.71–2.32) counts planets of5 Earth masses–10 Jupiter masses at0.5–10AU around predominantlyK/M microlensing hosts. Local population transfer is an assumption; this is not an exhaustive all-planet count. Small-HZ occurrence is a separate population and cannot be added. Neither fractional expected planets nor primary occurrence-error endpoints establish actual inhabited or habitable worlds.
