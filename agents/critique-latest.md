# Critique, 2026-11-08 (cycle 102)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (rc=0; the first attempt hit a 2 minute tool timeout, a rerun with a longer timeout finished). All pages OK, only "images not loaded" sandbox notes. I viewed index phone light, index desktop dark, raftar-formula-racing tablet light. No site files edited. HEAD 6210e27 (log-only; last site change was cycle 97). No regression seen.

## Sources consulted
Honest limit: WebFetch was blocked again (permission request unanswered) for https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html. WebSearch worked but returned only titles and URLs, so none of these were opened. They are pointers; no finding depends on them.
- Search results (not opened): https://web.dev/articles/optimize-cls (width/height on images, font-display, size-adjust)
- Search results (not opened): https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt placement)
- Search results (not opened): https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ and NN/g portfolio advice via https://www.nngroup.com/articles/author/rachel-krause/ (what hiring managers scan for)
- Carried from earlier cycles (read then): WCAG 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Topics this cycle: CLS from unsized images, robots.txt placement, hiring-manager scanning.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, strike-through "three weeks" on amber, stamps, Fig./Sheet captions, mono ledger, plain first-person lede. No gradients, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer band is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Ruled rhythm holds in light and dark. Desktop dark reads as inverted print. Weak spots: row 06 is the only row with a plate (on phone it sits above the title and breaks list rhythm); About desktop right third empty.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Unchanged risks: robots.txt and sitemap under /website/, one og:image for all pages, hotlinked figures without dimensions, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, ledger. Home is otherwise quiet; nothing to add that is not already in the repo.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read against today (2026-11-08) with no status line. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page has a schematic, a question and one sentence, no result. "Start here" sits on row 06 (aerobraking, "46 orbits to target"). Two answers to "strongest project"; the lede's is the thinnest. Owner decision: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix with no width/height. Unsized images shift layout (web.dev optimize-cls, unread); if URLs rotate, the Resume link breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar question (visible in the tablet screenshot): "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap sit at a project-site subpath; crawlers read robots.txt only at the host root. Submit the sitemap in Search Console (owner). Identical lastmod. Not verified against Google docs this cycle.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. Needs measured metrics or self-hosted files.
8. Minor (looks). Plate on row 06 only; on phone it breaks list rhythm. Add plates only with real figures (taste).
9. Minor (looks). About desktop empty right third until a portrait exists (taste).
10. Minor (UX, phone). Header drops Resume and GitHub on phones; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is "message me on LinkedIn" only; no email. Owner's choice by design, but it is a single point of failure for contact.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
13. Nit (looks). Small mono labels are the faintest text on tan; they pass AA (taste).

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic; no regression and no designer-fixable defect that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. External research was again limited (fetch blocked, search returned links only) and added no new findings.
