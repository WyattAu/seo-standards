# SEO-CORE: the search and AI-visibility canon

Every page, product, and property the estate operates competes in one
marketplace with three audiences: search engines, AI answer engines, and
the humans behind both. This canon covers every technique we use, admit,
or explicitly refuse, per 2026-11 standards. It is opinionated: things
Google stopped rewarding, or that carry penalty risk, are named as
refused, not merely omitted.

Status: CURRENT. Changes require a dated entry in `CHANGELOG.md` and,
for refusals or pillar changes, an ADR in `adr/`.

Where the truth lives:

| Question | Truth |
|---|---|
| What is required on every estate site? | This file, `SEO-CORE.md` |
| Deep practice per pillar | `references/*.md` |
| Current SERP surfaces and eligibility | `references/surfaces.md` |
| DR/DA doctrine and link acquisition | `references/authority.md` |
| Per-site implementation status | each site's `docs/seo/SEARCH_STANDARDS_SWEEP.md` |
| What changed upstream | Google Search Central "What's new"; this canon updates within one quarter |

## The three audiences are one pipeline

The same crawl, the same render, the same content feeds Google's index,
AI training crawlers, and retrieval-based answer engines (Perplexity,
ChatGPT Search, AI Mode). Optimize all three deliberately; never by
accident. A technique that helps one audience and harms another is
resolved in favor of the human reader, then the index, then the
training surface.

## T: Technical (crawl, index, render)

| # | Technique | Why |
|---|---|---|
| T1 | `robots.txt` + per-page `meta robots` + `X-Robots-Tag` governed by one policy | three layers, one intent; accidental `noindex` on money pages is the classic outage |
| T2 | XML sitemap, fresh, `<50k` URLs or split, referenced from robots.txt | discovery floor for new/deep URLs |
| T3 | IndexNow key + push on sitemap change | instant Bing/Seznam/Yandex discovery; Google ignores it; do not expect parity |
| T4 | Canonical governance: self-canonical default, cross-domain canonicals only for syndication, parameter pages canonical to the clean URL | duplicate consolidation is a ranking input, not decoration |
| T5 | hreflang cluster: reciprocal per-language URLs + `x-default`; directories not files | international targeting without duplicate dilution |
| T6 | Status-code hygiene: soft-404s hunted, `410` for intentionally gone content, `301` (not `302`) for permanence, redirect chains flattened to one hop | wasted crawl budget + lost signals live in the redirects table |
| T7 | Server-render or statically render all indexable content; no indexable content behind interaction | Google renders, but late and imperfectly; answer engines often do not render at all |
| T8 | Core Web Vitals as a floor: LCP < 2.5 s, INP < 200 ms, CLS < 0.1 on **field data** (CrUX), not lab boasts | page experience is a tie-breaker at scale; lab numbers that disagree with field data are self-deception |
| T9 | Edge/CDN caching with a documented TTL + SWR strategy; TTFB measured from real devices | render cost is index cost |
| T10 | HTTPS + HSTS; HTTP/2+; no mixed content | table stakes; also a light ranking signal |
| T11 | URL hygiene: lowercase, hyphenated, stable slugs, no session/tracking params in canonical links | stable URLs accumulate signals; churn resets them |
| T12 | Orphan prevention: every indexable page ≥ 1 internal inlink from a crawled page | orphaned pages decay out of the index silently |
| T13 | Crawl-budget control: faceted/parameter URL rules, sensible robots.txt, no infinite calendars/filters | big-site index coverage is won and lost here |
| T14 | Log-file analysis on large sites: verify bot behavior against assumptions | GSC sampling lies by omission |
| T15 | Image SEO: modern formats, explicit dimensions, descriptive alt, lazy-load except the LCP image | images rank (carousels) and carry CWV |
| T16 | Structured data per page type from the schema catalog (see `references/technical.md` §schema), validated in the rich-results test | eligibility for rich surfaces + machine clarity |
| T17 | Non-production environments `noindex` + credential-gated | staged content leaking into the index is self-inflicted |
| T18 | 404/410 UX: helpful not-found pages; internal links to removed content cleaned within one sprint | rot spreads through link graphs |

## C: Content and intent

| # | Technique | Why |
|---|---|---|
| C1 | One primary intent per URL, decided before writing (informational / commercial / transactional / navigational) | intent mismatch is unrankable by effort |
| C2 | Answer-first structure: the conclusion in the first screen; detail below | human bounce and AI citation share the same preference |
| C3 | Format matched to the SERP: if rivals rank with tables/tools/lists, build the better table/tool/list | the SERP is the requirement document |
| C4 | E-E-A-T evidence on every claim-bearing page: named bylines, credentials, first-hand testing, cited sources | YMYL and competitive queries are won by demonstrable experience |
| C5 | Honest freshness: real `dateModified`, real updates; never fake-touched | freshness is a query-dependent winner and a spam-policy surface |
| C6 | Topic clusters: hub pages + spoke pages, deliberately interlinked | topical breadth is a ranking input at the site level |
| C7 | Internal links with descriptive anchors from hubs to spokes and back | internal PageRank and topical reinforcement |
| C8 | Content pruning: consolidate or `410` thin/duplicated pages on a schedule | site-wide quality signals dilute across junk |
| C9 | Titles/metas: keyword-bearing, CTR-tested, unique; no boilerplate duplication | CTR at position is real, measurable, and compounding |
| C10 | One H1; logical H2/H3 outline | cheap clarity for humans, renderers, and extractors |
| C11 | Original data: studies, benchmarks, statistics no one else publishes | the highest-yield link asset in existence (see A2) |
| C12 | Gap closure: cover the subtopics the SERP rewards that rivals miss | information gain is Google's stated preference |
| C13 | AI-assisted writing allowed, **scaled unreviewed generation refused**: quality and information gain are the policy lines, not origin | 2026 spam policy: scaled content abuse is site-wide |
| C14 | Multimedia where intent demands it (images, video, tools) | surface diversity in the SERP |
| C15 | UGC (forums, comments) only with moderation and structured markup | Google surfaces moderated UGC; unmoderated UGC is a spam vector |

## G: GEO/AEO (AI-engine visibility)

| # | Technique | Why |
|---|---|---|
| G1 | `llms.txt` at the root listing canonical docs; `llms-full.txt` where content volume warrants | emerging convention; cheap, honest |
| G2 | Per-bot crawler policy decided deliberately (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot): training vs retrieval surfaces are different decisions | blocking training does not block retrieval, and vice versa |
| G3 | Citability: self-contained passages, named statistics, quotable definitions | answer engines lift passages, not pages |
| G4 | Machine-readable freshness: dates in schema and feeds | retrieval favors recency for time-sensitive queries |
| G5 | Entity clarity: Organization schema + `sameAs` + consistent name/address across the footprint | the entity graph is the citation address |
| G6 | Preferred Sources participation: standard publisher button + deeplinks (see `references/surfaces.md`) | opted-in readers get your badge in Top Stories and AI Mode/Overviews |
| G7 | Citation-share tracking per engine per target query | visibility you do not measure does not compound |
| G8 | Passages engineered for extraction (definitions, tables, numbered methods) | RAG retrieval is passage-level |

## A: Authority (DR/DA and links)

DR (Ahrefs), DA (Moz), TF (Majestic) are **third-party proxies computed
from link indexes**; none are Google inputs, and chasing the meter
instead of the referential reality produces the wrong links. Google's
own public position: it uses no domain-authority metric. What actually
compounds: independent pages choosing to cite you.

| # | Technique | Why |
|---|---|---|
| A1 | Link assets before campaigns: publish the data study, the tool, the calculator, the definitive guide | assets earn links passively forever; campaigns rent |
| A2 | Digital PR: journalist-source platforms, newsworthy launches, expert commentary in trade press | editorial links are the only links Google cannot discount wholesale |
| A3 | Relevance over DR: a DR 30 domain inside your niche outranks a DR 80 irrelevant one for topical authority | relevance-weighted authority is what actually transfers |
| A4 | Anchor naturalness: branded/URL/natural-phrase anchors; exact-match keyword anchors are a footprint | anchor-text manipulation is the oldest penalty tripwire |
| A5 | Velocity discipline: steady acquisition; spikes look manufactured | flat-link graphs with spikes correlate with manual actions |
| A6 | Unlinked-mention reclamation: find brand mentions without links; ask for the link | highest-conversion, zero-risk acquisition |
| A7 | Broken-link and outbound-404 reclamation in your niche | win-win; scalable with taste |
| A8 | Relationship links: suppliers, customers, partners, industry bodies; real pages about real relationships | permanent, topical, algorithm-proof |
| A9 | Guest contributions only where a real editor reviews real expertise | syndicated filler on content farms is a spam-policy surface |
| A10 | Competitor link-gap analysis (Ahrefs/Majestic intersect) monthly | the acquisition roadmap writes itself |
| A11 | Toxic-link response: most link penalties are self-inflicted; disavow is a last resort with documented evidence | the disavow file is not a magic eraser |
| A12 | **Purchased links, PBNs, link exchanges: refused.** 2026 spam policy violations; one envelope buys a site-wide demotion | the downside is the domain itself |
| A13 | Brand-mention growth as a KPI: brand search volume + mention frequency | brand signals co-move with rankings; Google's own leaks and antitrust testimony support brand as an input |
| A14 | Architecture as authority: hubs absorb and distribute internal authority deliberately | internal link equity is the only equity you control fully |
| A15 | Digital-footprint consistency: same name, address, profile set everywhere | entity trust is the slow compounder |

## S: Surfaces (the 2026 SERP)

| # | Surface | Eligibility lever |
|---|---|---|
| S1 | Preferred Sources (Top Stories + AI Mode/AI Overviews) | user-side selection; promote with Google's publisher button/deeplink; requires fresh content |
| S2 | AI Overviews / AI Mode citations | SGAI inclusion in Search Console + citability (G3) |
| S3 | Discover | feed-worthy visuals + E-E-A-T + mobile experience |
| S4 | Rich results: product/merchant (stars, shipping, returns), recipe, video | structured data validity; **FAQ rich results are restricted to authoritative government/health sites; keep FAQPage markup for structure, expect no SERP real estate** |
| S5 | Featured snippets / PAA | answer-first formatting; PAA rewards question-coverage |
| S6 | Video and image carousels | VideoObject/ImageObject + media quality |
| S7 | Local pack | Google Business Profile (where a physical address exists) |
| S8 | Top Stories | news sitemap + Article schema + Publisher entity |
| S9 | Discussions and forums | moderated UGC (ForumPosting/QAPage) |

## M: Measurement

| # | Practice | Cadence |
|---|---|---|
| M1 | Search Console review: queries, CTR, coverage, enhancements | weekly |
| M2 | Bing Webmaster Tools + IndexNow delivery check | monthly |
| M3 | CrUX field CWV review | monthly |
| M4 | Rank tracking on cluster heads (grid + mobile where local applies) | weekly |
| M5 | AI citation share per engine per target query | monthly |
| M6 | Referring-domain and brand-mention tracking | monthly |
| M7 | Log-file review on large sites | quarterly |
| M8 | Conversion-weighted reporting: rankings are inputs; revenue is the output | every report |

## R: Risk

| # | Rule | Why |
|---|---|---|
| R1 | Know the current spam policies by name: scaled content abuse, site reputation abuse (parasite), expired-domain abuse | each has a site-wide enforcement class |
| R2 | The reviewer test: any tactic you would hide from a reviewer is refused | the only ethics line that scales |
| R3 | Manual actions: documented recovery path (fix → reconsideration); no site relaunches under an active action | repeat violations escalate to listings-wide |
| R4 | Negative-SEO monitoring: link-spike alerts, content-defacement checks, scheduled-index spot checks | cheap insurance; rare but real |
| R5 | Deindexation triage: GSC coverage first, robots/canonical/render second, penalties third | most "deindexations" are self-inflicted technicals |
| R6 | Algorithm-event corroboration: never react to one Twitter thread; corroborate across rank trackers + GSC + peers | volatility weeks reward patience |
| R7 | Refusals are part of the standard: PBNs, purchased links, parasite hosting, cloaking, doorway pages, sneaky redirects; refused by name | a standard that only lists virtues is not a standard |

## Adoption

Estate sites implement T1–T9, C1–C4, G1–G6, A6, A13, M1, M8 as the
**baseline tier** (audit-gated per site via each site's
`docs/seo/SEARCH_STANDARDS_SWEEP.md`). The remaining techniques are
adopted by site class: content sites implement the full C pillar;
commerce sites the full S4 merchant set; large sites add T13–T14.
