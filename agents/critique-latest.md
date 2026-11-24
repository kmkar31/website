# Critique, 2026-11-24 (HEAD 811fb5b, after designer cycle 197)

Method: ran `python3 tools/check.py . agents/shots` (zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, projects tablet-dark. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). Edited no site files. Regenerating agents/shots is a side effect of the required check. WebFetch/WebSearch were not used this cycle; sources below are carried over from the previous cycle and are not re-read.

## Sources consulted
- WCAG 2.2 Target Size (Minimum), fetched last cycle: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum (site clears 24 px with 44 px targets).
- NN/g, UX Portfolios: What Hiring Managers Look For (listing only): https://www.nngroup.com/videos/ux-portfolios-hiring/
- web.dev, Optimize CLS (not re-read): https://web.dev/articles/optimize-cls ; https://web.dev/learn/images/performance-issues . Finding 5 rests on their advice to set width/height on images.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio; struck-through "three weeks", stamps and plates are specific. Residual (taste): nine pages share one skeleton. Tells moved: none.
- Looks good: 8/10. Paper and ink palette is coherent. Cycle 197's filled ink "Start here" tab now reads as a mark, not a link (fixed). Weak: on row 06 three marks stack (stamp, tab, tags) beside a plate, the busiest spot on the page; right column still ragged (rows 01 to 03, 08, 09 bare).
- SEO: 7/10, unchanged. Unique titles and descriptions, one h1, canonical, JSON-LD, sitemap, absolute og:image. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Indexing and previews not verifiable offline.
- UX: 6/10, unchanged (Major findings 1 to 4).
- Fun and personality: 7/10, unchanged. Highlighter strike, stamps, 99 s press-and-hold. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, hard offset shadows, no blur).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
Cycle 197 only restyled the "Start here" label. It is legible in light (phone, desktop) and dark (tablet), no overflow, no layout shift. No regression.

## Ranked findings
1. Major (UX, credibility). Home subhead and meta description say "MS Mechanical Engineering, Carnegie Mellon" in the present tense; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell if he has graduated or is available. Owner fact needed (for example "Class of 2025" or "Graduated 2025, open to roles").
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads the list and the lede, while "Start here" sits on row 06 (aerobraking). Row 01's page is thin. Owner picks the lead and supplies snake method and result, or moves the lead row.
3. Major (credibility). Aerobraking Method and Setup narrate Falcone et al.'s work in third person, so Karthik's own contribution is unclear on the "Start here" project. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is still hotlinked from Wix (header on desktop, hero, footer). It is the artifact a recruiter most wants. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on most pages (about 3 to 10 per page) with no known width/height: CLS risk and outage dependency. Needs local files and dimensions.
6. Minor (visual). Row 06 stacks stamp, "Start here" tab and tags (home desktop, projects tablet). Taste: put the tab on the left edge of the row or above the title, so the right column keeps one mark per row.
7. Minor (UX). Only rows 04 to 07 carry a stamp, so rows 01 to 03, 08, 09 cannot be ranked at a glance. Same root as 2 and 3.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (UX, taste). Phone header omits Resume (360 px reasoning accepted; do not reopen).
13. Nit (process). Findings 1 to 5 need owner facts and files; the same list has repeated for many cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure; 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- The new filled "Start here" tab, now the strongest mark in its row.
- Per-page titles, descriptions, canonical and JSON-LD; prev/next on project pages.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and cycle 197 fixed the one design point left open (the quiet "Start here" label). Row 06 is now slightly crowded, a minor taste item. What holds UX at 6 is missing owner input: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Design cycles have little left to improve without them.
