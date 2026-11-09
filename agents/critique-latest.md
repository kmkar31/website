# Critique, 2026-11-09 (cycle 104)

Rendering: `python3 tools/check.py . agents/shots` ran (rc=0, about 3 min; it exceeds a 2 min tool timeout, so run it in the background). All pages OK; only "images not loaded" sandbox notes. I viewed index phone light, index desktop dark, about tablet light. No site files edited; no site change since cycle 97, so no new regression is possible.

## Sources consulted
- Read: https://web.dev/articles/optimize-cls (always set width and height on images and video; aspect-ratio can also reserve space; font swaps shift layout, mitigated by a close fallback, `size-adjust`, `font-display: optional`, preload). Supports findings 3 and 7.
- Blocked (permission unanswered): https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt. Finding 5 stays unverified.
- Search only (titles, not read): Nielsen Norman Group and others on what hiring managers look for in portfolios. Nothing cited from them.
- Carried from earlier cycles: WCAG 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Topic this cycle: CLS from unsized images and web fonts.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, strike-through "three weeks" on amber, stamps, Fig. captions, mono ledger, plain first-person copy. No gradient, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Ruled rhythm holds on phone, tablet and desktop; dark mode reads as inverted print. Weak spots: row 06 is the only row with a plate (above the title on phone, it breaks the list rhythm); About on tablet/desktop has a plain text column with an empty right side; the boxed "podium finish" stamp inside About running text pushes its line apart.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt and sitemap under /website/, one og:image for all pages, unsized hotlinked figures, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, ledger. Home is otherwise quiet; nothing to add that is not already in the repo.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-09 with no status line. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page has no stated result, while "Start here" sits on row 06 (aerobraking, "46 orbits to target"). Two answers to "strongest project"; the lede's is the thinnest. Owner decision: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix with no width/height. web.dev says to always set both. If the Wix URLs rotate, the Resume link breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). raftar-formula-racing.html: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap live at a project-site subpath; crawlers read robots.txt only at the host root (unverified, source blocked). Submit the sitemap in Search Console (owner). Identical lastmod.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback (web.dev suggests `size-adjust`, `font-display: optional`, preload). Needs measured metrics or self-hosted files.
8. Minor (looks). Plate on row 06 only; on phone it breaks list rhythm. Add plates only with real figures (taste).
9. Minor (looks). About on tablet/desktop: empty right side until a portrait exists (taste). The inline boxed "podium finish" stamp in a paragraph opens a gap in its line (taste; a stamp suits lists better than prose).
10. Minor (UX, phone). Header drops Resume and GitHub on phones; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is "message me on LinkedIn" only; single point of failure, owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
13. Nit (looks). Small mono labels are the faintest text on tan; they pass AA (taste).

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic; no regression and no designer-fixable defect that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research this cycle: one source read (web.dev CLS), one blocked.
