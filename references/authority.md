# Authority — DR/DA doctrine and the acquisition playbook

## How the meters actually work

| Metric | Vendor | Computed from | Range |
|---|---|---|---|
| Domain Rating (DR) | Ahrefs | log-scale link count: unique referring domains (dofollow) pointing at the domain, weighted by their DR | 0–100 |
| Domain Authority (DA) | Moz | link index + MozRank/MozTrust + a machine-learned fit against actual SERPs | 1–100 |
| Page Authority (PA) | Moz | same model, per-URL | 1–100 |
| Trust Flow / Citation Flow | Majestic | TF: topical quality of citations; CF: raw citation volume | 0–100 |
| Authority Score | Semrush | blended link + traffic + spam signals | 0–100 |

None of these are Google inputs. Google's public position (documented
in testimony and creator-content guidance) is that it uses no
site-wide authority score; ranking systems evaluate links at the
document level with relevance weighting. The meters are useful as
**competitive telescopes** — they rank-order the market's link
 realities — and useless as optimization targets.

Consequences that follow from the mechanics:

1. DR is **doflow-only and deduped at the referring-domain level** —
   one link per domain moves it; a thousand site-wide footer links
   move it once.
2. DR is **domain-level**: a strong subfolder does not raise DR, and a
   domain's DR does not guarantee page-level strength. Check PA/UR
   for the actual page you are compared against.
3. DR is **relative, not absolute**: it re-computes as the web changes;
   a static domain's DR drifts down as the index grows.
4. Losing one high-DR link can drop DR visibly while rankings do not
   move — the meter tracks the link graph, rankings track relevance
   and brand.

## The acquisition playbook (in yield order)

| Rank | Technique | Yield | Cost | Refusals |
|---|---|---|---|---|
| 1 | Publish the link asset: original data study, benchmark, tool, calculator, definitive guide | recurring passive links, the only compounding asset | high once, low after | never as a bait-and-switch page |
| 2 | Digital PR: journalist platforms, trade-press commentary, newsworthy launches | high-DR editorial links | medium | no pay-to-play advertorials passed off as coverage |
| 3 | Unlinked-mention reclamation | highest conversion rate per outreach | low | — |
| 4 | Broken-link / outbound-404 reclamation in-niche | medium | medium | — |
| 5 | Relationship links: suppliers, customers, partners, industry bodies, open-source credits | permanent, topical | low | — |
| 6 | Guest contributions behind a real editorial bar | medium | medium | no syndicated filler on content farms |
| 7 | Competitor link-gap intersection (monthly) | roadmap, not links | low | — |
| 8 | Communities you genuinely participate in | slow, high trust | low | no drive-by link drops |

## Outreach discipline

- Personal, specific, one-ask messages; the link target's benefit stated
  in the first sentence.
- Anchor targets: branded or natural phrases. Exact-match keyword
  anchors at scale are a manipulation footprint.
- Velocity: steady. A spike followed by silence reads as a campaign.
- Record everything in the site's link ledger: date, URL, anchor, page.
  The ledger is the evidence base if a manual action ever lands.

## Refusals (spam policy, 2026)

Purchased links; link exchanges at scale ("link to me and I link to
you" rings); PBNs; guest-post farms; parasite hosting (publishing on
someone else's authority to rank content out of step with their site);
automated link schemes; widget/footer link bait with keyword anchors.
The 2026 enforcement class for these is **site-wide**, and recovery
requires proving the whole pattern removed.

## Diagnosing your current authority (order)

1. Referring-domain count and trend (GSC links table + one index).
2. Topical relevance split of referring domains (in-niche vs not).
3. Link-to-page distribution: how many pages carry links? (A domain
   whose links all point at the homepage has one strong page.)
4. Anchor distribution: branded share (should dominate).
5. Competitor gap intersection — this is next quarter's plan.
