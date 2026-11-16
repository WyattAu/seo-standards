# Technical; the non-negotiables, in audit order

Diagnose in this order; technical failures mask everything downstream.

## 1. Crawl and index

- `site:` and GSC coverage first: is the page in the index at all?
- robots.txt + meta robots + X-Robots-Tag agreement (three layers,
  one intent).
- Rendered DOM (View Source ≠ rendered HTML): content present without
  interaction?
- Canonical: self-referencing? Conflicting signals (sitemap vs
  canonical vs internal links)?
- Orphans: pages with zero internal inlinks decay silently.

## 2. The schema catalog (page-type → markup)

| Page type | Required | Optional/high-value |
|---|---|---|
| Home | Organization (+sameAs), WebSite (+SearchAction), LocalBusiness where physical | ProfilePage for founder entities |
| Product/PDP | Product, Offer (price, currency, availability, priceValidUntil), Brand; MerchantReturnPolicy; OfferShippingDetails | AggregateRating (real mechanics only), Review, image gallery |
| Article/guide | Article (+datePublished/dateModified, author ProfilePage) | Speakable, VideoObject where real |
| FAQ | FAQPage |; (rich results restricted; keep for structure) |
| How-to/tool | HowTo (visible steps only) |; |
| Data/dataset pages | Dataset (+variableMeasured) | DataCatalog |
| Collections | ItemList |; |
| Breadcrumbs | BreadcrumbList |; (on every nested page) |
| Events | Event |; |

Validation: rich-results test + schema validator in CI where possible.
Marked-up content must be **visible on the page**; invisible markup is
a policy surface.

## 3. Performance floors (field data, not lab)

LCP < 2.5 s · INP < 200 ms · CLS < 0.1 at p75 in CrUX.

- Render-blocking audit: fonts (swap + preload), critical CSS, no
  synchronous third-party scripts in the head.
- LCP image: preloaded, sized, modern format, never lazy-loaded.
- INP: break long tasks; audit hydration cost on every island.
- CLS: dimensions on all media; no late-injected banners above content.

## 4. International

- hreflang cluster: reciprocal, absolute URLs, `x-default`.
- Locale content that differs, not machine-translated shells.
- One URL structure per locale segment; locale in the path.

## 5. Migrations (where sites die)

- 1:1 URL map, 301s, no chains; sitemap updated at cutover; GSC
  change-of-address; monitor coverage daily for 30 days. The redirect
  map is never deleted.
