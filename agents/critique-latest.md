# Critique, 2026-10-28 (cycle 33, reviewing main at f45ff28)

## Sources
- Not fetched this cycle: the WebFetch permission requests for web.dev/articles/optimize-lcp, Google Search Central ProfilePage structured data, and WCAG 2.2 Understanding "Link Purpose (In Context)" all timed out. No web source was read. Carried over from cycle 32 (fetched then): web.dev, Optimize CLS (https://web.dev/articles/optimize-cls): always set width and height on images, and use a close fallback or `size-adjust` for font swaps.
- Findings below rest on measurement and viewing, not on new research. This misses the "three sources each cycle" rule; the caller should know.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit). Viewed: home phone light, home desktop dark, Aerobraking desktop light, Raftar phone light. Repo greps: JSON-LD on 12 of 13 pages (404 has none, correct), og:image absolute, robots.txt lists the sitemap, Resume is a single filesusr.com (Wix) PDF link on 3 spots on home. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan copy. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates. Residual: cream, serif, terracotta and mono small-caps labels is a recognisable editorial kit. Tells moved: none.
- Looks good: 7/10. Home is calm and well ruled in both themes. The cycle 31 ledger was trimmed to a clean two-item "Orbit range" line (desktop view confirms no wrapping or orphan). Snake and Raftar pages are sparse.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, Person JSON-LD, sitemap, noindex 404. Open: no image width/height, generic alt on Wix figures, robots.txt and sitemap at a subpath (cannot be fixed on a GitHub Pages project site), no font fallback metrics.
- UX: 6/10. Phone first screen gives who, where, lab, one concrete result, Resume and LinkedIn. Still missing: status/date, a contact other than LinkedIn, a Resume not hosted on Wix.
- Fun and personality: 6/10. Strike-through, "Time allowed: 99 s", Sheet N of 9 and the 404 are earned. Snake and Aerobraking pages are neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, no blur or gradient.
- Not AI-looking: met at 3/10. Remaining risk is repetition of marks (stamps, mono labels), not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. About says the Master's "is at Carnegie Mellon University (2023 – 2025)", the home lede is present tense, and today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. STATUS in build.py is still empty. One owner sentence fixes it.
2. Major (owner decision). "Start here" (row 01, Snake) points at the thinnest page on the site: one paragraph on why snake robots matter, a general lab link, and a schematic labelled "Module count is illustrative". It states what a snake robot is, not what he implemented or what happened. Either supply what he built and the outcome, or move "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures have no width/height, so layout shift is likely when they load (web.dev CLS guidance). Unmeasured offline.
4. Major (content, owner facts). Few "what I did / what happened" lines. Raftar says "suspension and brakes" with no component, number or result; its plate is a generic car sketch. Do not invent.
5. Minor (verify claim). Raftar question "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?" is striking and unverifiable. Confirm it is the original wording and accurate.
6. Minor. Alt text on Wix figures is generic (WCAG 1.1.1); owner must say what each image shows.
7. Minor. Two Google font families with display=swap and no size-adjusted fallback; needs real font files for metrics. Self-hosting would also drop a third-party request.
8. Minor (taste). Stamps on four of nine rows in two border styles. Add no more.
9. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
10. Nit. "START HERE" is a small mono label under "01", easy to miss on phone. Contrast passes.

Regression check: cycle 32 changes (trimmed ledger, softened "guarantees" sentence) landed correctly. No new regressions found. Previous findings 1 and 6 are resolved.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs stating the specific thing done.
- Aerobraking h2 structure, mono action-space block and the concise Orbit range line.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without becoming costume and does not read as generated. The cycle 32 fixes worked and I found no designer-fixable defect this cycle. What limits the site now needs the owner: a status sentence (pages say 2023 – 2025 in October 2026), a local Resume and images with dimensions, real outcomes for the Snake and Raftar pages, and confirmation of the Ferrari claim. This critique did no web research because the fetches were blocked; treat the findings as measurement-and-viewing only.
