# Critique, 2026-10-27 (cycle 32, reviewing main at 24788ad, which adds the Aerobraking result ledger)

## Sources
- web.dev, Optimize Cumulative Layout Shift (https://web.dev/articles/optimize-cls). Fetched this cycle. It says to "always include width and height size attributes on your images and video elements" (or reserve space with CSS aspect-ratio), and that web-font swapping shifts layout unless you use a close fallback, `size-adjust`, `font-display: optional` or preload.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), 24 px: search results only (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). Not fetched. The site's 44 px targets exceed it.
- WCAG 2.2 SC 1.1.1 Non-text Content (https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html). Search pointer only, not fetched.
- NN/g and hiring-manager portfolio advice: search results only (https://www.nngroup.com/articles/author/rachel-krause/; https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/). Not read in full. Findings rest mainly on measurement and viewing.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", sandbox limit). Viewed: home phone light, Aerobraking phone light and desktop dark, Snake phone light, About phone light. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan copy. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates, honest colophon. Residual: cream + serif + terracotta + mono labels is a recognisable editorial kit, and the new ledger plus facts strip leans on small-caps mono labels again. Tells moved: none.
- Looks good: 7/10. Home is calm and well ruled; dark theme holds. The Aerobraking page is better broken up than last cycle, but the new ledger is rough (finding 1). Snake and Raftar pages are sparse.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, Person JSON-LD, sitemap, noindex 404. Open: no image width/height, generic alt on Wix figures, robots.txt and sitemap at a subpath, no font fallback metrics.
- UX: 6/10. The first phone screen answers who, where, lab, one concrete result, Resume and LinkedIn. Still missing: status/date, a contact other than LinkedIn, a Resume not hosted on Wix.
- Fun and personality: 6/10. Strike-through, "Time allowed: 99 s", Sheet N of 9 and the 404 are earned. The Snake and Aerobraking pages are neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, no blur or gradient.
- Not AI-looking: met at 3/10. The remaining risk is repetition of marks (stamps, mono labels), not a template tell.

## Findings (ranked)
1. Major (regression from cycle 31, designer-fixable). The new "Result at a glance" ledger on Aerobraking is badly built and redundant.
   - On desktop (1366, dark) it is five items in a four-column grid. "Training 1.1 million steps" is orphaned on a second row.
   - "Orbits to target (simulator)" wraps to two lines, so its value "46" sits lower than its neighbours' values and the baselines misalign.
   - On phone it is a 2-column grid with the same wrap.
   - The same terminal error 8.4 km, 1.1M steps and 46 orbits already appear in the hero sentence, the facts strip under it and the Result paragraph, so the numbers now appear three or four times.
   - Fix: drop the three duplicated figures. Keep only what the strip lacks (initial apoapsis 10038 km, target apoapsis 4906 km) as a two-item line, or delete the ledger and let the strip carry the result. If kept, use four columns with short labels ("To target, 46 orbits") so nothing wraps.
2. Major (credibility, owner-only). No current status or date. About says "My Master's ... is at Carnegie Mellon University (2023 – 2025)" and the lede is present tense, but today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. One owner sentence fixes it; the STATUS slot exists.
3. Major (owner decision). Row 01 "Start here" (snake robots) is the only row with a plate and the featured label, but its page is one paragraph ("Why snake robots") plus a general research-page link. It says what a snake robot is, not what he built or what happened. The page is the thinnest on the site and sits first. Supply what he implemented and the outcome, or move "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s).
4. Major (robustness, owner files). The Resume link (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures still have no width/height, so layout shift is likely when they load. web.dev says to always set them or reserve space with aspect-ratio. Unmeasured offline.
5. Major (content, owner facts). Few "what I did / what happened" lines. Raftar says "suspension and brakes" with no component, number or result, and its plate is a generic car. Do not invent.
6. Minor (claim, designer-fixable wording). Aerobraking's last sentence says an RL-based method "guarantees a successful aerobraking maneuver with lower fuel consumption and maneuver time compared to traditional human-involved decision making". The evidence on the page is one simulator run (46 orbits, 8.4 km error). "Guarantees" and the fuel and time comparison are not shown. This is carried over from the source report; consider "succeeded in simulation", or ask the owner. Credibility risk for a technical reader.
7. Minor (verify claim). Raftar question "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?" is striking and unverifiable. Confirm it is the original wording and accurate.
8. Minor. Alt text on Wix figures is generic. Owner must say what each image shows (WCAG 1.1.1). Thumbnail and lightbox empty alts are intentional.
9. Minor. Two Google font families with display=swap and no size-adjusted fallback; web.dev lists this as a shift source. Needs real font files for metrics. Self-hosting WOFF2 would also remove a third-party request.
10. Minor (taste). Stamps on four of nine rows in two border styles; the Raftar stamp repeats the lede directly above it. Add no more.
11. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
12. Nit. "START HERE" is a small mono label under bold "01"; easy to miss on phone. Contrast passes. Empty band above the footer on tablet and an empty right third on About desktop are accepted.

Regression check: only the cycle 31 ledger (finding 1) is new. Everything else is unchanged from last cycle.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks" (home and About), "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs stating the specific thing done.
- Aerobraking h2 structure (Problem, Setup, Method, Result) and the mono action-space block.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site still commits to retro matte without becoming costume and does not read as generated. The one new defect is the cycle 31 ledger, which is misaligned on desktop and mostly repeats numbers already shown just above; trim or rebuild it (finding 1), and soften the "guarantees" sentence (6). Everything else that limits the site needs the owner: a status sentence (the pages say 2023 – 2025 in October 2026), a local Resume and images with dimensions, real outcomes for the Snake and Raftar pages, and confirmation of the Ferrari claim. Of the web sources, only web.dev was fetched in full; the others are search results.
