# Critique, 2026-11-10 (cycle 114)

Rendering: `python3 tools/check.py . agents/shots` completed, rc clean, no FAIL (only "images not loaded, sandbox network" notes). I viewed index phone light, about desktop dark, snake-robots tablet light. No site files edited; git status was clean before this file. No source change since cycle 113.

## Sources consulted
- WCAG 2.2 Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html . Only the search listing was seen; the WebFetch was blocked (permission request unanswered). From the criterion as I know it: 24x24 CSS px minimum, which the site's 44 px targets exceed.
- Google Search Central, ProfilePage structured data: https://developers.google.com/search/docs/appearance/structured-data/profile-page . Listing only; fetch blocked. Used only as a pointer for finding 11.
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion . Fetch blocked; not used for any finding.
- Carried from earlier cycles: https://w3c.github.io/wcag/understanding/focus-not-obscured , https://web.dev/articles/fetch-priority , https://web.dev/optimize-cls
- Caveat: no source was read in full this cycle. Nothing below depends on a source beyond well-known facts. Treat the research as thin.

## Scores
- AI-tell: 2/10, unchanged. Paper and grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger, DM Serif Display with Source Serif 4, plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Phone index is calm and well measured. Weak spots: lone plate on row 06; rows 02, 03, 08, 09 carry only number and tags; the snake page (no result, no media loaded in the sandbox) is a large plate plus one paragraph and feels unfinished; About has an empty right third on desktop.
- SEO: 7/10. Unchanged (findings 5, 6, 11).
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, Fig. 1 plate with "Sheet n of 9 / NTS", ledger. Nothing new is supported by repo facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradients, blur or glow in any viewed shot.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-10 with no status line. `STATUS = ""` at build/build.py:262, so the ledger shows only Built, Internships, Toolbox. Recruiters cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page states no result, while "Start here" and the only plate sit on row 06 (46 orbits). Two answers to "strongest project". Owner decision: pick one, or state a result for the snake work.
3. Major (media dependency, robustness). Images and Resume still hotlinked from Wix; the Resume link is the main recruiter action and appears three times on each page. Needs owner files (local resume.pdf, photos). Not verifiable in the sandbox.
4. Major (credibility). Raftar page "one-fifth the weight of a Ferrari but matches its 0-60" is unsourced on the page. Owner to source or cut.
5. Minor (SEO). robots.txt and sitemap sit under the /website/ subpath on github.io; crawlers only honour robots.txt at host root, and all lastmod values are identical. Owner action: custom domain or Search Console submission. Not verifiable offline.
6. Minor (SEO/CLS). No per-project og:image (no art exists); figures lack width/height, so CLS risk once Wix images load. Needs real dimensions; guessed ratios could worsen CLS. fetchpriority on the first figure already landed.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. Needs real metrics.
8. Minor (looks, taste). Plate on row 06 only; bare rows read thin beside it.
9. Minor (looks, taste). About has an empty right side on wide screens below the "On this page" box.
10. Minor (UX). Contact is LinkedIn only; single point of failure, owner's choice. Header on phone drops Resume and GitHub; both remain in lede and footer, acceptable.
11. Nit (SEO). JSON-LD is Person; ProfilePage wrapping on About is optional and low value. Not worth owner time.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
13. Nit (looks). Small mono labels are the faintest text on tan; passed AA in check.py.

Designer-fixable this cycle: none. Regressions from last cycle: none.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "schematic" notes.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling, scroll-padding under the sticky header, fetchpriority on first figure.
- About page: ruled education and experience entries with dated mono labels read cleanly in dark mode.

## Verdict
Authored, coherent and not generic, with no regression since cycle 113. Everything material waits on the owner: a status line, a lead-project decision or snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. Caveat: web research was blocked or listing-only this cycle, so the sourcing is weaker than the brief requires.
