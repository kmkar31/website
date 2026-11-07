# Critique, 2026-11-07 (cycle 94)

Rendering: `python3 tools/check.py . agents/shots` completed, every line OK (13 pages x 3 viewports x 2 themes), only "images not loaded" sandbox notes. I viewed index phone light, index desktop light and snake-robots desktop dark. Repo greps: `STATUS = ""` (build/build.py:262); wixstatic/filesusr references on all 13 html files (404 has 2); Ferrari question still at raftar-formula-racing.html:48; robots.txt and sitemap.xml present; sitemap lastmod 2026-11-02. No site files edited.

## Sources consulted (honest note)
WebFetch was blocked again (permission request unanswered) for https://web.dev/articles/optimize-cls. I read no source body, so the three-source rule is NOT met for a third cycle running. Findings rest on renders and repo greps only. Unverified pointers, not relied on:
- https://web.dev/articles/optimize-cls
- https://www.nngroup.com/articles/portfolio-reviews/
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html

## Scores
- AI-tell score: 2/10, unchanged. Paper tone, double rules, a single hard-offset button, struck-through "three weeks" on amber, stamps, "Fig. 1 / Sheet n of 9 / NTS" captions, plain first-person lede. No gradients, blur, glow, card trio or stats strip. Residual tells: intro, ruled list, dark footer is a familiar shape; blurbs share a cadence. No tell moved since last cycle.
- Looks good: 8/10. Hierarchy and rhythm hold on phone and desktop, light and dark. Weak spots: row 06 is the only row with a plate, so the list is lopsided; About desktop right third is empty.
- SEO: 7/10. Distinct titles, descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404 present. Risks: robots/sitemap at a project-site subpath, one shared og:image, hotlinked undimensioned figures, identical lastmod.
- UX: 6/10. Name, field, projects and LinkedIn are found in seconds on the phone render. Held down by no stated current status and no quantified result on the lede project.
- Fun and personality: 7/10. Pressable 99 s stamp, 404 joke, strike-through marker, plates. The home page itself carries little beyond the strike-through.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met (flat paper, grain, hard shadow only on the primary button, inverted-print dark theme).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle says "MS Mechanical Engineering, Carnegie Mellon University" and About shows "2023 - 2025", with today at 2026-11-07. The "Status" row in "For the record" never renders because STATUS is empty. A recruiter cannot tell graduated, studying or available. Owner must supply one line.
2. Major (robustness, CLS). Project photos and the Resume link are still hotlinked from Wix (static.wixstatic.com, filesusr.com) on every page; figures carry no width/height. If Wix rotates URLs, Resume breaks in the header, the lede and every footer. Needs owner files in assets/ and real dimensions.
3. Major (UX, 30-second test). "Start here" sits on row 06 (aerobraking, the only row with a plate), while the lede leads with snake robots (row 01), whose page is a tl;dr, lab, advisor, one schematic and one sentence, with no outcome. Two answers to "strongest project", and the lede one is the thinnest page. Owner to supply a snake result or choose.
4. Major (content credibility). The Raftar page question claims "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time". Original-site copy; nothing in the repo supports it. Owner to confirm a figure or cut it.
5. Minor (looks). About desktop: right third empty beside Skills/Education/Experience until a portrait exists. Taste.
6. Minor (SEO). robots.txt under /website/ is ignored by crawlers; sitemap needs Search Console submission (owner). lastmod identical on every URL.
7. Minor (SEO). One og:image for all pages; per-project cards would help LinkedIn previews. Low priority.
8. Minor (fonts). Two Google Fonts with display=swap and no size-adjusted fallback; self-hosting needs WOFF2 from the owner.
9. Minor (UX, phone). Header drops Resume and GitHub on phones; Resume stays in the lede and footer. Acceptable, documented.
10. Nit (copy). Home blurbs share a verb-led cadence; two or three could vary using only facts already on each page.
11. Nit (looks). Small mono labels (01-09, tags) are the faintest text on tan; passes contrast, reads faint on phone. Taste.
12. Nit (robustness). 404.html's two Wix references are the Resume links; the 404 depends on a third party until the PDF is local.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, so they cannot hotlink-fail.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact; no "as shown in the figure" phrasing.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic, and I found no regression and no designer-fixable defect of weight. What holds it back is missing owner input: a current status line, a result for the snake work, a confirmed or cut Raftar claim, and local copies of the Resume and images. Until then the biggest risks are a stale 2023-2025 timeline and Wix hotlinks that could break the Resume link and every photograph. Web research was blocked again, so best-practice claims rest on renders and greps only.
