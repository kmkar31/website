# Critique, 2026-11-24 (HEAD 336d3c3, after designer cycle 196)

Method: ran `python3 tools/check.py . agents/shots` (rc 0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light and desktop-dark, projects phone-light, aerobraking phone-light. Measured phone (360 px) targets with Playwright: header links and footer links are 44 px tall. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). Edited no site files. Regenerating agents/shots is a side effect of the required check.

## Sources consulted
- WCAG 2.2 Target Size (Minimum), fetched: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum . 24x24 CSS px, or spacing; inline-text links are exempt. The site clears this comfortably (44 px).
- NN/g, UX Portfolios: What Hiring Managers Look For (search listing only, page text not retrieved): https://www.nngroup.com/videos/ux-portfolios-hiring/
- web.dev, Optimize CLS (search listing only, not fetched): https://web.dev/articles/optimize-cls ; and https://web.dev/learn/images/performance-issues . Finding 5 relies on their long-standing advice to set width/height on images; I could not re-read the pages this cycle.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Struck-through "three weeks" on a highlighter is specific. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark footer. Weak: Home right column ragged (rows 01 to 03, 08, 09 have no stamp); on phone the Fig. 1 plate sits tight under the Hasselhoff row; the new "Start here" is a bare underlined mono label, which reads like an unstyled link and does not match the stamps beside it.
- SEO: 7/10, unchanged. Unique titles and descriptions, one h1, canonical, JSON-LD, sitemap, robots, absolute og:image. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Not verifiable offline: indexing, previews.
- UX: 6/10, unchanged (Major, findings 1 to 4). Cycle 196 added "Start here" to Projects, which fixes the signal-consistency half of the old finding; the lead-project conflict remains.
- Fun and personality: 7/10, unchanged. Highlighter strike, stamps, 99 s press-and-hold. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, no blur).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
Cycle 196 changed only the Projects label. No overflow or breakage in the shots. No regression. One visual nit from it (finding 6).

## Ranked findings
1. Major (UX, credibility). Home subhead and meta description use the present tense, "MS Mechanical Engineering at Carnegie Mellon"; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell if he has graduated or is available. Owner fact needed (a "Class of 2025" or "Graduated 2025, open to roles" line).
2. Major (UX). Still two answers to "strongest project": row 01 (snake) leads Home and Projects while "Start here" is on row 06 (aerobraking). Row 01's page is thin. Owner picks the lead and supplies snake method and result, or moves the lead row.
3. Major (credibility). Aerobraking Method and Setup narrate Falcone et al.'s work in third person ("Falcone et al. simulated...", "the authors required..."), so Karthik's own contribution is unclear, while it is the "Start here" project. "46 orbits" has no baseline for comparison. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix (header on desktop, hero, footer). It is the artifact a recruiter most wants. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on most pages (about 3 to 10 per page) with no known width/height: CLS risk and outage dependency. Needs local files and dimensions.
6. Minor (visual consistency). On Projects and Home the "Start here" label is a plain underlined mono word under the stamp, so it looks like a link, not a mark. Give it the stamp treatment (ink border, slight rotation, or a filled ink tab with paper-coloured text) so it is the strongest mark on the page. Taste, but it is the one thing a 30-second scan should catch.
7. Minor (UX). Only rows 04 to 07 carry a stamp, so rows 01 to 03, 08 and 09 cannot be ranked at a glance. Same root as 2 and 3.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (UX, taste). Phone header omits Resume (360 px reasoning accepted; do not reopen).
13. Nit (process). Findings 1 to 5 need owner facts and files; the same list has repeated for over ten cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure; 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Per-page titles, descriptions, canonical and JSON-LD; "More on <tag>" related link; prev/next on project pages.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated. The only new design point is that the freshly added "Start here" label is too quiet to do its job. Everything else holding UX at 6 is missing owner input: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Design cycles have little left to improve without them.
