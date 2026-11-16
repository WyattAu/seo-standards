# Surfaces; the 2026 SERP catalog

Eligibility levers for every Google surface that matters in 2026, plus
the AI-engine answer surfaces. Verify current requirements against
Google Search Central before relying on any row; this file is the
estate's working map, updated quarterly.

## Google-owned surfaces

| Surface | What it rewards | Estate lever |
|---|---|---|
| **Preferred Sources** (Top Stories + AI Mode + AI Overviews) | user-side selection of a source; fresh content keeps eligibility | Google's standard publisher button (`publisher.js` + `google-add-preferred-source-btn`) at content ends; deeplink (`google.com/preferences/source?q=DOMAIN`) in footers/emails/social; eligibility = domain-level, must appear in the tool; stale sources drop out |
| **AI Overviews / AI Mode** | citability + SGAI inclusion | Search Console → confirm the site is included in Search generative AI features; passage-level clarity (G3/G8) |
| **Discover** | feed-worthy imagery + E-E-A-T + mobile CWV | large images (1200px+), honest dates, entity clarity, no clickbait |
| **Rich results: product/merchant** | valid Product + Offer with price, availability, shipping, **returns** | crawlkit SHIP001/RETURN001 gates; stars only with genuine review mechanics |
| **FAQ rich results** | restricted to authoritative government/health sites | keep FAQPage markup for structure and engines other than Google; expect no SERP real estate |
| **Featured snippets / PAA** | answer-first formatting, question coverage | 40–60-word direct answers under question headings |
| **Video / image carousels** | VideoObject/ImageObject + media quality | only where real media exists |
| **Local pack** | Google Business Profile | where a physical address exists (owner decision); NAP consistency |
| **Top Stories** | news sitemap + Article schema + Publisher entity | only for genuinely time-sensitive coverage |
| **Discussions & forums** | moderated UGC | ForumPosting/QAPage markup; moderation is the prerequisite |

## AI-engine answer surfaces

| Engine | Retrieval model | Estate lever |
|---|---|---|
| Perplexity | live retrieval (theirbot) | allow PerplexityBot; citable passages; llms.txt |
| ChatGPT Search | Bing-backed retrieval + OAI-BoilerBot | allow OAI-SearchBot + ChatGPT-User; llms.txt |
| Google AI Mode / Overviews | Google index + SGAI | index coverage + SGAI inclusion + preferred badge |
| Claude | retrieval (ClaudeBot) + training (Claude-User/Anthropic?) | deliberate per-bot policy |
| Gemini | Google index (+ Google-Extended for training) | index coverage first; training opt-out is a separate decision |

## Crawler policy defaults (decide per site, never by accident)

| Bot | Purpose | Estate default |
|---|---|---|
| GPTBot | OpenAI model training | site-class decision; commerce sites usually block, content sites usually allow |
| OAI-SearchBot / ChatGPT-User | ChatGPT Search retrieval / live fetch | allow (answer-surface presence) |
| ClaudeBot / Claude-User / anthropic-ai | training / retrieval / live fetch | same split as OpenAI |
| PerplexityBot / Perplexity-User | retrieval / live fetch | allow |
| Google-Extended | Gemini training | block if training-surface restraint is the site-class choice; does NOT affect Search |
| CCBot | Common Crawl (training data aggregators) | usually block |
| Amazonbot, Applebot, Meta-ExternalAgent | Alexa+ / Apple Intelligence / Meta AI | site-class decision |

The policy lives in robots.txt with a comment block naming each bot's
decision and date. A policy nobody can explain is a policy nobody
should have.

## Bing and the non-Google index

- Bing Webmaster Tools: import from GSC, verify, submit sitemaps.
- IndexNow: key file at root, push on sitemap change (Bing/Seznam/
  Yandex/Naver instant discovery). Google ignores IndexNow entirely.
- Yandex/Seznam/Naver/Baidu: only where the market demands them.
