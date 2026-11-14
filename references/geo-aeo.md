# GEO/AEO — being the cited source

Search engines rank documents. Answer engines assemble passages. The
unit of optimization shifts from the page to the **passage that a
retriever can lift and a model can quote without context**.

## The citability checklist

1. **Self-contained passages**: a reader who sees only the paragraph
   understands it. Named entities, not pronouns. Numbers with units.
2. **Quotable statistics**: "Batch BPC-101A assayed at 99.4% purity
   (HPLC, Janoshik, 2026-08)" beats "our purity is very high". Retrieval
   matches specifics; models quote specifics.
3. **Definitions on first use**, in one sentence, in the page's own
   voice.
4. **Tables over prose for enumerable facts**; numbered steps for
   procedures; both extract cleanly.
5. **Direct answers under question-shaped headings** — 40–60 words,
   then depth.
6. **Freshness in machine-readable form**: `dateModified` in schema,
   real feeds.
7. **Entity clarity**: the site says who it is the same way everywhere
   (Organization schema, `sameAs`, consistent naming).

## llms.txt practice

- `/llms.txt`: short, curated, markdown — the canonical doc map with
  one-line descriptions.
- `/llms-full.txt`: the full corpus where volume warrants.
- Keep both generated from the same source as the docs (a stale llms.txt
  is worse than none — it teaches retrievers the site lies).

## Crawler policy

Training access and retrieval access are **different decisions**:

- Blocking GPTBot does not remove a site from ChatGPT Search (that is
  OAI-SearchBot / ChatGPT-User).
- Blocking Google-Embedded does not affect Google Search or AI
  Overviews (that is the normal index).
- The estate default: **allow all retrieval bots; decide training bots
  per site class**, with the decision and date recorded as a comment in
  robots.txt.

## Measurement

- Monthly: run the target query set in each engine, fresh session,
  record cited-domain share for the estate.
- Track the query set itself as a versioned file; trends only mean
  something against a fixed set.
- Preferred Sources adds a badge surface for opted-in users — adoption
  is measurable via Google's publisher tooling, not via server logs.
