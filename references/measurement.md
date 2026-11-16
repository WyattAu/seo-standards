# Measurement; fixed cadence, readable causality

| Signal | Source | Cadence |
|---|---|---|
| queries, impressions, CTR, coverage, enhancements | Search Console | weekly |
| CWV field data (p75) | CrUX / Search Console | monthly |
| Bing coverage + IndexNow delivery | Bing Webmaster Tools | monthly |
| organic sessions, conversions | server logs / privacy-first analytics | weekly |
| rank positions for cluster heads (grid/mobile) | rank tracker or manual p1–p10 | weekly |
| AI citation share per target query per engine | direct engine asks, fresh session | monthly |
| referring domains, anchor mix, brand mentions | link index + mention search | monthly |
| preferred-source adoption | Google publisher tooling | monthly |
| log-file bot behavior | server logs | quarterly (large sites) |

## Causality rules

1. Corroborate algorithm events across ≥ 2 independent sources
   (rank trackers + GSC + peer reports) before changing anything.
2. Changes ship one variable per page-group where possible; grouped
   launches record the grouping, or the readout is noise.
3. Rankings are inputs, revenue is the output; every report ends in
   conversion-weighted terms.
4. Volatility weeks reward patience: 7-day windows are noise, 28-day
   comparisons are signal.
