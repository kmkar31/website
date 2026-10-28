# Critique, 2026-10-28 (cycle 35, reviewing main)

## Sources
- No web source was read. WebFetch was blocked again this cycle (permission request timed out, told not to retry): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. The "three sources each cycle" rule is not met; treat this as a measurement-and-viewing critique. Standing guidance relied on from earlier cycles: WCAG 1.1.1 (alt text), web.dev Optimize CLS (image width/height), NN/g portfolio guidance (outcomes over description).
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit). It takes more than 2 minutes now; run it with a long timeout. Viewed: home phone light, home desktop dark, Raftar phone light. Web fonts do not load in the sandbox, so the screenshots show the serif fallback, not DM Serif Display. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan copy. Authored specifics: the struck-through "three weeks", the "For the record" ledger, outcome stamps, Fig./Sheet N of 9 plates. Residual risk: cream, serif, terracotta and mono small-caps is a recognisable editorial kit. Tells moved: none.
- Looks good: 7/10. Home is calm and well ruled; hierarchy is clear on phone and desktop. Dark desktop home is balanced. Held back by the placeholder-looking schematics in place of real images, and a tall, uniform project list.
- SEO: 8/10. Titles, descriptions, canonical, OG, JSON-LD, sitemap and 404 are in place. The sitemap and robots.txt sit under a subpath, so crawlers will not read robots.txt (owner: submit the sitemap in Search Console). Not verifiable offline: og:image fetch, Wix image weight.
- UX: 7/10. Contact, resume and strongest project are findable in 30 seconds on phone. Lowered by LinkedIn-only contact, Resume depending on a Wix hotlink, and no status or date.
- Fun and personality: 7/10. The struck-through "three weeks", the Ferrari question, the stamps and the 404 joke carry character. It is quiet; no tactile press state or easter egg beyond that.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, no blur or gradient. Dark theme is inverted print and holds up.
- Not AI-looking: met at 3/10. The remaining risk is repeated marks (stamps, mono labels), not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. The pages say CMU "2023 – 2025" while today is October 2026, so it reads as stale or as graduated with no next step. A recruiter cannot tell whether he is available. STATUS in build.py is empty. One owner sentence fixes it.
2. Major (owner decision). "Start here" (row 01, Snake) points at the page with the least evidence: what a snake robot is, but not what he implemented or what happened. Supply an outcome, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures have no width/height, so layout shift is likely. Unmeasurable offline. Needs local files.
4. Major (content, owner facts). Raftar says "did the suspension and brakes" with no component, number or result; the page body is a generic team description. The figure is a generic car sketch whose caption claims the team "built" this kind of car. Do not invent; the owner should supply one concrete thing he designed.
5. Minor (verify). The Raftar question (one-fifth the weight of a Ferrari, matching its 0-60 time) is striking but unverifiable here. Owner should confirm the wording and numbers.
6. Minor. Alt text on Wix figures is generic (WCAG 1.1.1). The owner must say what each image shows.
7. Minor. Two Google font families, display=swap, no size-adjusted fallback; self-hosting would drop a third-party request. Needs the real font files.
8. Minor (taste). Outcome stamps are on five of nine home rows in two border styles; the four unstamped rows (02, 03, 08, 09) look slightly less finished. Add none; consider none.
9. Minor. Contact is LinkedIn only (owner constraint). Conversion risk, not a defect.
10. Nit (taste). About desktop leaves the right third empty beside Skills, Education and Experience when the portrait is absent. Accepted and documented.

Regression check: none found from cycle 34 (no site diff). check.py is clean.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, the 404 joke, the honest colophon.
- Plain lede with real facts; full project names as titles; blurbs that state the specific thing done.
- Aerobraking structure and mono action-space block.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without becoming costume and does not read as generated. I found no designer-fixable defect this cycle. What limits it needs the owner: a status sentence (pages say 2023 – 2025 in October 2026), a local Resume and images with dimensions, real outcomes for the Snake and Raftar pages, and confirmation of the Ferrari claim. Web research was blocked for the second cycle running, so this critique is measurement and viewing only.
