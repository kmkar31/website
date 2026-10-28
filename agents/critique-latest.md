# Critique, 2026-10-28 (cycle 34, reviewing main at 7cc94e6)

## Sources
- No web source was read. WebFetch was blocked this cycle (permission requests timed out, told not to retry) for: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, https://web.dev/articles/optimize-cls, https://www.nngroup.com/articles/portfolio-reviews/. This misses the "three sources each cycle" rule. Findings rest on measurement and viewing. The CLS and alt-text points below are the standard guidance (web.dev Optimize CLS; WCAG 1.1.1) and were last fetched in cycle 32.
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit). Viewed: home phone light, home desktop light, About desktop dark, Snake phone light. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan copy. Authored specifics: the struck-through "three weeks", the "For the record" ledger, stamps, Fig./Sheet N of 9 plates. Residual: cream, serif, terracotta and mono small-caps labels is a recognisable editorial kit. Tells moved since last cycle: none.
- Looks good: 7/10. Home is calm and well ruled in both themes. Weak spots: the Snake page is mostly a plate and one paragraph, and About desktop has an empty right third under the intro.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, noindex 404. Open: no image width/height, generic alt on Wix figures, no font fallback metrics. robots.txt and sitemap at a subpath cannot be fixed on a GitHub Pages project site.
- UX: 6/10. The phone first screen gives who, where, the lab, one concrete result, Resume and LinkedIn. Still missing: status/date, a Resume that is not hosted on Wix, any contact beyond LinkedIn.
- Fun and personality: 6/10. The strike-through, "Time allowed: 99 s", the press-to-count stamp, Sheet N of 9 and the 404 are earned. The Snake and Raftar pages are neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, no blur or gradient. The dark theme is inverted print and holds up (About desktop dark viewed).
- Not AI-looking: met at 3/10. The remaining risk is repeated marks (stamps, mono labels), not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). There is no status or date. About says the Master's "is at Carnegie Mellon University (2023 – 2025)" and the Education block lists "2023 – 2025". Today is October 2026, so the dates read as past or the page as stale. A recruiter cannot tell whether he has graduated or is open to roles. STATUS in build.py is still empty. One owner sentence fixes it.
2. Major (owner decision). "Start here" (row 01, Snake) points at the thinnest page. The page shows a tl;dr, lab and advisor, an illustrative schematic, and one generic "Why snake robots" paragraph. It says what a snake robot is, not what he implemented or what happened. Either supply the outcome or move "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures have no width/height, so layout shift is likely when they load. This is unmeasurable offline.
4. Major (content, owner facts). Few "what I did / what happened" lines. Raftar says "suspension and brakes" with no component, number or result. Do not invent.
5. Minor (verify claim). The Raftar question compares the car to a Ferrari on weight and 0-60 time. The wording is striking and unverifiable here. The owner should confirm the wording and the numbers.
6. Minor. Alt text on Wix figures is generic (WCAG 1.1.1). The owner must say what each image shows.
7. Minor. Two Google font families with display=swap and no size-adjusted fallback. Self-hosting would also drop a third-party request. It needs the real font files.
8. Minor (taste). Stamps sit on four of nine rows in two border styles. Add no more.
9. Minor. Contact is LinkedIn only (owner constraint). This is conversion risk, not a defect.
10. Nit. About desktop leaves the right third empty beside Skills, Education and Experience when the portrait is absent. It is accepted and documented, but it looks unfinished in the screenshot. Taste.

Regression check: no regressions from cycle 33. The enlarged "START HERE" label reads better on phone, and finding 10 from last cycle is resolved. check.py is clean.

## Good, must not regress
- The retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: the struck-through "three weeks", the "For the record" ledger, stamps, Fig./Sheet N of 9 plates, the 404 joke, the honest colophon.
- A plain lede with real facts. Full project names as titles. Blurbs that state the specific thing done.
- The Aerobraking h2 structure and its mono action-space block.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- The SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without becoming costume and does not read as generated. I found no designer-fixable defect this cycle. What limits it now needs the owner: a status sentence (the pages say 2023 – 2025 in October 2026), a local Resume and images with dimensions, real outcomes for the Snake and Raftar pages, and confirmation of the Ferrari claim. This critique did no web research because the fetches were blocked, so treat it as measurement-and-viewing only.
