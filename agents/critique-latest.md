# Critique, 2026-11-10 (cycle 113)

Rendering: `python3 tools/check.py . agents/shots` completed (all pages, phone/tablet/desktop, light/dark: OK, no FAIL; only "images not loaded, sandbox network" notes). I viewed index phone light, index desktop light, raftar-formula-racing phone dark. No site files edited; no source changed since cycle 112 (git status clean before my output).

## Sources consulted
- WCAG 2.2 Understanding 2.4.11 Focus Not Obscured (fetched and read): https://w3c.github.io/wcag/understanding/focus-not-obscured . Sticky headers must not hide the focused element; `scroll-padding` is the listed technique. Site has `scroll-padding-top:80px` and the sticky header: pass.
- WCAG 2.2 What's New (search result only): https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Hiring-manager portfolio advice (search results only, secondary): https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ , https://uxdesign.cc/what-hiring-managers-look-for-in-a-product-design-portfolio-7b1837360bf9 . NN/g's own article was not surfaced.
- web.dev CLS and image dimensions (search result only): https://web.dev/optimize-cls
- Carried from earlier cycles: https://web.dev/articles/fetch-priority ; https://developer.chrome.com/blog/framework-tools-font-fallback
- Caveat: only the WCAG page was read in full; the others are listings and nothing below depends on them beyond the cited fact.

## Scores
- AI-tell: 2/10, unchanged. Paper and grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger, DM Serif Display with Source Serif 4, plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Warm, calm, well-measured in the screenshots. Weak spots: lone plate on row 06; rows 02, 03, 08, 09 carry only number and tags; wide gap between blurbs and tag column on desktop.
- SEO: 7/10. Unchanged (findings 5, 6).
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, Fig. 1 plate, ledger. Nothing new is supported by repo facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradients, blur or glow in any viewed shot.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-10 with no status line. `STATUS = ""` at build/build.py:262, so the ledger shows only Built, Internships, Toolbox. Recruiters cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page states no result, while "Start here" and the only plate sit on row 06 (46 orbits). Two answers to "strongest project". Owner decision: pick one or give the snake work a result.
3. Major (media dependency, robustness). Images and Resume still hotlinked from Wix; the Resume link is the main recruiter action. Needs owner files (local resume.pdf, photos). Sandbox cannot load them, so not verifiable here.
4. Major (credibility). Raftar page "one-fifth the weight of a Ferrari but matches its 0-60" is unsourced on the page. Owner to source or cut.
5. Minor (SEO). robots.txt and sitemap live under a /website/ subpath on github.io (crawlers only honour robots.txt at host root); all lastmod identical. Owner action: custom domain or Search Console submission.
6. Minor (SEO/CLS). No per-project og:image (no art exists); figures lack width/height, so CLS risk once Wix images load. Needs real dimensions; guessed ratios could worsen CLS. fetchpriority on first figure already landed.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. Needs real metrics.
8. Minor (looks, taste). Plate on row 06 only; bare rows read thin beside it.
9. Minor (looks, taste). About has an empty right side on wide screens.
10. Minor (UX, phone). Header drops Resume and GitHub; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is LinkedIn only; single point of failure, owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
13. Nit (looks). Small mono labels are the faintest text on tan; passed AA earlier, not re-measured.

Designer-fixable this cycle: none. Regressions from last cycle: none.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "schematic" notes.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling, scroll-padding under the sticky header, fetchpriority on first figure.

## Verdict
Authored, coherent and not generic, with no regression since cycle 112. Everything material waits on the owner: a status line, a lead-project decision or snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. Caveat: research rested mostly on search listings; only the WCAG 2.4.11 page was read in full.
