# Critique, 2026-11-07 (cycle 95)

Rendering: `python3 tools/check.py` completed (rc=0, every line OK, 13 pages x 3 viewports x 2 themes, only "images not loaded" sandbox notes; screenshots written to the scratchpad because the default run exceeds a 2-minute tool timeout). I viewed index phone light, index desktop dark and aerobraking-drl tablet light. Repo greps: `STATUS = ""` (build/build.py:262), Ferrari claim at raftar-formula-racing.html:48, 7 wixstatic references on the aerobraking page, no width/height on its figures. No site files edited.

## Sources consulted
Read in full:
- web.dev, Optimize Cumulative Layout Shift, https://web.dev/optimize-cls/ ("Always include width and height size attributes on your images"; CSS aspect-ratio is the alternative; wrong attributes still shift less than none).
- UX Design Institute, what hiring managers look for, https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (managers have little time per portfolio; a two to three sentence intro, a clear overview and two or three skimmable case studies).
Search results only (page body not retrieved, claim not relied on):
- Google Search Central robots.txt guide, https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (fetch was refused; the known rule is that robots.txt applies per host at its root).

## Scores
- AI-tell score: 2/10, unchanged. Flat paper, double rules, hard-offset single button, struck-through "three weeks" on amber, stamps, "Fig. 1 / Sheet n of 9" captions, plain first-person lede. No gradients, blur, glow, card trio or stats strip. Residual: intro, ruled list, dark footer is a familiar shape; blurbs share a cadence. No tell moved.
- Looks good: 8/10. Hierarchy, rhythm and the dark inverted-print theme hold at all three sizes. Weak: row 06 is the only row with a plate, so the home list is lopsided (obvious on phone, where the plate sits above the title); About desktop right third empty.
- SEO: 7/10. Distinct titles and descriptions, canonical, OG/Twitter with absolute og:image, JSON-LD, sitemap, 404. Risks: robots/sitemap at a project-site subpath, one og:image for every page, undimensioned hotlinked figures, identical lastmod.
- UX: 6/10. Name, field, projects and LinkedIn are found in seconds on the phone render, matching the "short intro, two or three strong projects" pattern. Held down by no current status and no quantified result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates. Home carries little beyond the strike-through.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met (flat paper, grain, one hard shadow, inverted-print dark).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (content, regression-adjacent). aerobraking-drl.html, Method section: "As shown below, a combination of a continuous and terminal reward function was used..." The cycle 92 fix removed three "figure above/below" phrasings but missed this one. The reward-function figure is a Wix hotlink in a lazy fig-row; with it missing the sentence points at nothing. Fix: "A combination of a continuous and terminal reward function was used...". No fact change. Designer-fixable.
2. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" against today 2026-11-07; the "Status" row never renders because STATUS is empty. A recruiter cannot tell graduated, studying or available. Owner must supply one line.
3. Major (robustness, CLS). Project photos and the Resume link are hotlinked from Wix (static.wixstatic.com, filesusr.com) on every page, figures carry no width/height. web.dev says always set width and height or aspect-ratio; without them each late image shifts the article. If Wix rotates URLs, Resume breaks in header, lede and every footer. Needs owner files and dimensions. Cheap partial mitigation the designer can do without guessing: none safe; do not guess ratios.
4. Major (UX, 30-second test). "Start here" is on row 06 (the only row with a plate) while the lede leads with snake robots (row 01), whose page has no outcome. Two answers to "strongest project", and the lede one is the thinnest. Owner to supply a snake result or choose.
5. Major (credibility). Raftar question: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time". Nothing in the repo supports it. Owner to confirm or cut.
6. Minor (SEO). robots.txt under /website/ is not at the host root and is ignored by crawlers; sitemap needs Search Console submission (owner). lastmod identical across URLs.
7. Minor (SEO). One og:image and og:image:alt ("Karthik Karumanchi, robotics and controls engineer") on every project page; per-project cards would help LinkedIn previews. Low priority, no art exists.
8. Minor (looks). About desktop: empty right third until a portrait exists. Taste.
9. Minor (fonts). Two Google Fonts, display=swap, no size-adjusted fallback.
10. Minor (UX, phone). Header drops Resume and GitHub on phones; Resume remains in lede and footer. Acceptable.
11. Nit (copy). Home blurbs share a verb-led cadence; vary two or three using facts already on each page.
12. Nit (looks). Small mono labels (01-09, tags) are the faintest text on tan; passes AA, reads faint on phone. Taste.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic. This cycle's one designer-fixable defect is the leftover "As shown below" sentence on the aerobraking page, a gap in the cycle 92 cleanup. Everything else that holds the site back needs the owner: a current status line, a snake result, a confirmed or cut Raftar claim, and local copies of the Resume and images with real dimensions. Until then the stale 2023-2025 timeline and Wix hotlinks are the biggest risks. Research this cycle: two sources read in full, one only via search results.
