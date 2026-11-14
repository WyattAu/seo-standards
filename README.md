# seo-standards

The WyattAu canon for search and AI-engine visibility: every technique
we use, admit, or explicitly refuse, per 2026-11 standards. Projection
source for the `estate-seo` skill; consumable directly by reading
[`SEO-CORE.md`](SEO-CORE.md).

| Pillar | Section | Techniques |
|---|---|---|
| Technical (crawl/index/render) | `SEO-CORE.md` §T | 18 |
| Content and intent | §C | 15 |
| GEO/AEO (AI-engine visibility) | §G | 8 |
| Authority (DR/DA and links) | §A | 15 |
| Surfaces (the 2026 SERP) | §S | 9 |
| Measurement | §M | 8 |
| Risk and refusals | §R | 7 |

**80 techniques. 8 named refusals.** Deep practice per pillar lives in
[`references/`](references/):

| File | Contents |
|---|---|
| [`references/technical.md`](references/technical.md) | audit order, schema catalog per page type, performance floors, migrations |
| [`references/content.md`](references/content.md) | briefs, E-E-A-T as evidence, information gain, pruning |
| [`references/geo-aeo.md`](references/geo-aeo.md) | citability, llms.txt practice, crawler policy defaults, measurement |
| [`references/authority.md`](references/authority.md) | how DR/DA are computed, the acquisition playbook in yield order, outreach discipline, refusals |
| [`references/surfaces.md`](references/surfaces.md) | Google surfaces catalog + AI-engine answer surfaces + per-bot crawler defaults |
| [`references/measurement.md`](references/measurement.md) | fixed cadence, causality rules |
| [`references/risks.md`](references/risks.md) | 2026 spam policies, recovery paths, standing monitors |

## Status

CURRENT. Changes require a dated `CHANGELOG.md` entry; pillar changes
and new refusals require an ADR in `adr/`.

## Per-site adoption

Each estate site records its implementation state in
`docs/seo/SEARCH_STANDARDS_SWEEP.md` (a projection of this canon's
tables). The baseline tier: T1–T9, C1–C4, G1–G6, A6, A13, M1, M8.
