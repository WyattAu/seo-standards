# Risks; the refusal list and the recovery paths

## The 2026 spam policies (know them by name)

| Policy | Pattern | Enforcement |
|---|---|---|
| Scaled content abuse | generating volumes of unreviewed pages for the sake of it | site-wide demotion |
| Site reputation abuse (parasite) | third-party content published on someone else's authority, out of step with their site | page- then site-level |
| Expired-domain abuse | buying aged domains to host content that never lived there | demotion of the abuse |
| Link spam | purchased/exchanged links, PBNs, automated schemes | link devaluation, then manual actions |
| Cloaking / sneaky redirects / doorway pages | serving engines something humans do not see | manual actions |

## The reviewer test

Any tactic you would hide from a reviewer is refused. This is the only
ethics line that scales, and it is also the enforcement predictor:
everything Google penalizes fails the test.

## Recovery paths

| Symptom | First move | Then |
|---|---|---|
| Coverage drop on a section | GSC coverage report → robots/canonical/render audit | fix technicals; penalties are the last hypothesis |
| Site-wide impressions collapse | manual-actions report → spam-policy checklist | file reconsideration only after the pattern is provably gone |
| Link-based manual action | remove/deny per the action's examples; document every step | reconsideration with the ledger attached |
| Ranking volatility | 28-day comparison across trackers + GSC + peers | patience; volatility weeks reward inaction |

## Standing monitors

- Link-spike alerts (new referring domains per week); negative-SEO and
  self-inflicted campaigns both show here first.
- Content-defacement checks (integrity hashes on money pages).
- Scheduled-index spot checks: a fixed query set whose expected page
  must appear; absence is an alarm.
