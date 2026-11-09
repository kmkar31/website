# Critique, 2026-11-09 (cycle 107)

Rendering: `python3 tools/check.py . agents/shots` completed (about 3 min, run in background): 78 checks OK, no FAIL, only sandbox "images not loaded" notes. I viewed index phone light, index desktop dark and snake-robots tablet light. `git status` was clean at start and the last commit changed only the log, so no regression is possible. No site files edited.

## Sources consulted
- Every fetch was blocked this cycle: WebFetch of https://web.dev/articles/lcp returned a permission-not-answered error, and curl to web.dev, w3.org and nngroup.com all failed with proxy 403. I read no source this cycle and cite none as read.
- Carried from earlier cycles (read then): https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Unverified pointers only: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt placement), https://web.dev/articles/lcp (LCP image priority).
- Topic this cycle: LCP and 30-second scan. Verified from the repo instead: aerobraking-drl.html's first image has `decoding="async"` but no `fetchpriority` and no width/height; later images have `loading="lazy"` (correct). robots.txt is `Allow: /` plus an absolute Sitemap URL; sitemap lastmod is 2026-11-02 for every URL.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, strike-through "three weeks" on amber, stamps, Fig. captions, mono ledger, plain first-person copy. No gradient, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Ruled rhythm holds on phone and desktop; dark mode reads as inverted print. Weak spots: the plate exists on row 06 only (on phone it sits above the title and breaks the list rhythm); the snake page's only figure is a schematic marked illustrative, so the lead project has no real image; About has an empty right side on wide screens.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt and sitemap under /website/, one og:image for all pages, unsized hotlinked figures, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, ledger. Home is otherwise quiet. No new idea that the repo's facts support; a live 99-second countdown on the row 05 stamp would be decorative motion and is not recommended.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-09 with no status line. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result ("Why snake robots" is one general paragraph plus a link), while "Start here" sits on row 06 (aerobraking, "46 orbits to target"). Two answers to "strongest project"; the lede's is the thinnest. Owner decision: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix with no width/height. web.dev says to always set both. If the Wix URLs rotate, the Resume link breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). raftar-formula-racing.html: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap live at a project-site subpath; crawlers read robots.txt only at the host root (unverified, source not read). Submit the sitemap in Search Console (owner). Identical lastmod.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. Needs measured metrics or self-hosted files.
8. Minor (looks). Plate on row 06 only; add plates only with real figures (taste).
9. Minor (looks). About on wide screens: empty right side until a portrait exists (taste). The boxed "podium finish" stamp inside running text opens a gap in its line (taste).
10. Minor (UX, phone). Header drops Resume and GitHub on phones; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is "message me on LinkedIn" only; single point of failure, owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
13. Nit (looks). Small mono labels are the faintest text on tan; they pass AA (taste).
Unverified, to check when sources are readable: LCP risk from the hotlinked first image on project pages; whether the custom focus style meets WCAG 2.2 2.4.13 (AAA, so not required).

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic; no regression and no designer-fixable defect that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research this cycle was again nil: all fetches were blocked, so every source above is unread or carried over. Seen in this cycle's screenshots: on phone the nine-row list has one plate (row 06) and eight text-only rows, and the snake page's figure is a generic schematic; both are content gaps, not CSS faults.
