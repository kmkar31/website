# Critique, 2026-11-08 (cycle 99)

Rendering: `python3 tools/check.py . <scratchpad>/shots` completed (13 pages x phone/tablet/desktop x light/dark, about 2 min; the first attempt hit a 2 min tool timeout, the rerun finished). Every line OK, only "images not loaded" sandbox notes. I viewed index phone light, about desktop light, raftar tablet dark. Web fonts did not load in the sandbox, so screenshots show the serif fallback; judged on layout only. No site files edited. HEAD 395f293 (no site change since cycle 97), no regression seen.

## Sources consulted
WebFetch was blocked again (permission request unanswered), so NO source was read this cycle and I make no new cited claims:
- https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt (blocked)
- https://web.dev/articles/optimize-cls (blocked)
Points on robots.txt location and image dimensions below rest on earlier cycles' reading recorded in LOG.md; treat as repeated, not re-verified. Research for this cycle is effectively empty; the owner may want to grant WebFetch.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, struck-through "three weeks", stamps, Fig./Sheet captions, plain first-person lede. No gradients, blur, glow, card trio, stats strip, slogans. Residual: intro / ruled list / dark footer is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Ruled rhythm holds in both themes; dark reads as inverted print. Weak spots: row 06 is the only row with a plate and on phone the plate sits above the title, breaking list rhythm; Raftar page (viewed) is short: one sketch, two paragraphs, one outbound link; About desktop right third beside Skills/Education/Experience is empty.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Unchanged risks: robots.txt/sitemap under the /website/ subpath, one og:image everywhere, hotlinked figures without dimensions, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no quantified result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, "For the record" ledger. Home is otherwise quiet.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat surfaces, hard shadow, grain, no gradients).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" against today 2026-11-08; no status line renders, so a reader cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, but that page has no result; "Start here" is on row 06. Two answers to "strongest project", the lede one weakest. Owner: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume hotlinked from Wix (wixstatic.com, filesusr.com) on 11 pages, no width/height. If URLs rotate the Resume link breaks in header, lede and footers and layout shifts. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap at a project-site subpath; crawlers read robots.txt only at host root. Submit sitemap in Search Console (owner). lastmod identical.
6. Minor (SEO). One og:image for all pages; no per-project art.
7. Minor (looks). Lopsided plates (row 06 only); taste. Add plates only with real figures.
8. Minor (looks). About desktop empty right third until a portrait exists; taste.
9. Minor (fonts). Two Google Fonts with swap and no size-adjusted fallback; needs measured metrics.
10. Minor (UX, phone). Header drops Resume and GitHub on phones; kept in lede and footer. Acceptable.
11. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
12. Nit (looks). Small mono labels are the faintest text on tan; pass AA, taste.

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, native color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic, with no regression and no designer-fixable defect left that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research was blocked again, so this critique adds no new best-practice findings.
