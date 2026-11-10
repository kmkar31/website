# Critique, 2026-11-10 (cycle 112)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (all pages, phone/tablet/desktop, light/dark: OK, no FAIL; only "images not loaded, sandbox network" notes). I viewed index phone light, index desktop dark, snake-robots phone light and about tablet light. No site files edited. Worktree clean before and after apart from agents/ output.

## Sources consulted
- WCAG 2.2, Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (search result only; the 24 px minimum is from memory of the spec; the site's 44 px targets exceed it).
- Chrome, fallback fonts and CLS: https://developer.chrome.com/blog/framework-tools-font-fallback (search result; size-adjust and metric overrides for fallbacks).
- Portfolio content for hiring managers: https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (search result only; secondary source, WebFetch not used). The NN/g author listing surfaced but no article was read.
- Carried from earlier cycles: https://web.dev/articles/fetch-priority ; https://developers.google.com/crawling/docs/robots-txt/create-robots-txt
- Caveat: this cycle only read search-result snippets, not full pages. Nothing below depends on them beyond the cited fact.

## Scores
- AI-tell: 2/10, unchanged. Paper and grain, double rules, hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger, DM Serif Display with Source Serif 4, plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Dark desktop confirmed calm and well-measured. Weak spots unchanged: lone plate on row 06; rows 02, 03, 08, 09 carry only number and tags; wide gap between blurbs and tag column on desktop.
- SEO: 7/10. Unchanged (see 5, 6).
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, Fig. 1 plate, ledger. Nothing new supported by repo facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradients, blur or glow in any viewed shot.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-10 with no status line. `STATUS = ""` at build/build.py:262, so the ledger shows only Built, Internships, Toolbox (confirmed in desktop dark and phone light). Recruiters cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page (viewed, phone) states no result, while "Start here" and the only plate sit on row 06 (46 orbits). Two answers to "strongest project". Owner decision: pick one or give the snake work a result.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix with no width/height. If the URLs rotate, Resume breaks in header, lede and footer. Needs owner-supplied local files and real dimensions.
4. Major (credibility). Raftar page question says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (build/build.py, one occurrence). Nothing else in the repo supports it. Owner: source it or cut it.
5. Minor (SEO). robots.txt lives under /website/, so crawlers ignore it and the Sitemap line is not discovered (unverified live; per Google's robots.txt docs it must be at host root). Submit the sitemap in Search Console. All 12 lastmod values are identical.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback (Chrome article above describes the fix). Needs real font metrics; guesses could worsen CLS.
8. Minor (looks, taste). Plate on row 06 only; the bare rows read thin beside it.
9. Minor (looks, taste). About has an empty right side on wide screens (taste; noted on tablet shot too, text spans full width and is fine there).
10. Minor (UX, phone). Header drops Resume and GitHub; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is LinkedIn only; single point of failure, owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
13. Nit (looks). Small mono labels are the faintest text on tan; passed AA in earlier checks, not re-measured.

Designer-fixable this cycle: none.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "schematic" notes.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling, fetchpriority on first figure.

## Verdict
Authored, coherent and not generic, with no regression since the last cycle. Everything material still waits on the owner: a status line, a lead-project decision or snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. Caveat: research this cycle rested on search-result listings rather than fully read pages.
