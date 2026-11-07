# Critique, 2026-11-07 (cycle 93)

Rendering: `python3 tools/check.py . agents/shots` rc=0, 78 lines OK (13 pages x 3 viewports x 2 themes), only "images not loaded" sandbox notes. I viewed index phone light, index desktop light, about tablet dark, snake-robots phone light. Greps: `STATUS = ""` (build/build.py:262); wixstatic/filesusr references on all 13 html files (404 included, 2); no "as shown in the figure" phrasing left (cycle 92 fix confirmed); Ferrari line still on raftar-formula-racing.html:48. No site files edited.

## Sources consulted (honest note)
WebFetch was blocked again (permission request unanswered) for all three: web.dev/articles/optimize-cls, nngroup.com/articles/portfolio-reviews, w3.org WCAG 2.2 focus-not-obscured-minimum. I read no source body, so the three-source rule is NOT met for a second cycle. Findings rest on renders and repo greps only. Unverified pointers:
- https://web.dev/articles/optimize-cls
- https://www.nngroup.com/articles/portfolio-reviews/
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html

## Scores
- AI-tell score: 2/10, unchanged. Paper tone, double rules, one hard-offset button, struck-through "three weeks" on amber, stamps, "Fig. 1 / Sheet n of 9 / NTS" captions. No gradient, blur, glow, card trio or stats strip. Residual tells: the intro / ruled list / footer index shape; blurbs share a cadence. No tell moved since last cycle.
- Looks good: 8/10. Hierarchy and rhythm hold on phone, tablet and desktop in both themes. Weak spots: one plate among nine rows (row 06) makes the list lopsided; About desktop right third is empty.
- SEO: 7/10. Title, description, canonical, OG/Twitter, JSON-LD, sitemap, 404 all present. Risks: robots/sitemap at a project-site subpath, one shared og:image, hotlinked media, undimensioned figures.
- UX: 6/10. Name, field, projects and LinkedIn are found in seconds. Held down by an unstated current status and no quantified result on the lede project.
- Fun and personality: 7/10. Pressable 99 s stamp, 404 line, struck-through marker, plates. Home carries little beyond the strike-through.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met (flat paper, grain, hard shadow only on the primary button, inverted-print dark theme).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Education shows "2023 - 2025" and the home subtitle reads "MS Mechanical Engineering, Carnegie Mellon University" with today at 2026-11-07. The Status row in "For the record" never renders because STATUS is empty. A recruiter cannot tell graduated, studying or available. Owner must supply one line.
2. Major (robustness, CLS). Project photos and the Resume link are still hotlinked from Wix (static.wixstatic.com, filesusr.com) on every page; figures have no width/height. If Wix rotates URLs, the Resume link on home, header and every footer breaks. Needs owner files in assets/ and real dimensions.
3. Major (UX, 30-second test). "Start here" sits on row 06 (aerobraking, the only row with a plate). The lede leads with snake robots (row 01), whose page is a tl;dr, lab, advisor, one schematic and one "Why snake robots" sentence, with no outcome. Two answers to "strongest project"; the lede one is the thinnest page. Owner needs to supply a snake result, or choose.
4. Major (content). Raftar page still carries the "one-fifth the weight of a Ferrari but matches its 0-60" question. It is original-site copy and the repo has no figure supporting it. Owner to confirm or cut.
5. Minor (looks). About desktop: right third empty beside Skills/Education/Experience until a portrait exists. Taste.
6. Minor (SEO). robots.txt and sitemap.xml under /website/ are ignored by crawlers for robots; submit the sitemap in Search Console (owner). lastmod is the same on every URL.
7. Minor (SEO). One og:image for all pages; per-project share cards would help LinkedIn previews. Low priority.
8. Minor (fonts). Two Google Fonts with display=swap and no size-adjusted fallback; self-hosting needs WOFF2 from the owner.
9. Minor (UX, phone). Header drops Resume and GitHub on phones; Resume stays in the lede and footer. Acceptable and documented.
10. Nit (copy). Home row blurbs share a verb-led construction; two or three could be varied using only facts already on each page.
11. Nit (looks). Small mono labels (01-09, tags) are the faintest text on tan; contrast passes but reads faint on phone.
12. Nit (robustness). 404.html also references Wix hosts (2); confirm what for, since the 404 should not depend on a third party.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact; aerobraking prose now stands without its figures.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic. I found no regression from cycle 92 and no designer-fixable defect of weight. What holds it back is missing owner input: a current status line, a result for the snake work, a confirmed or cut Raftar claim, and local copies of the Resume and images. Until then the biggest risks are a stale 2023-2025 timeline and Wix hotlinks that could break the Resume link and every photograph. Web research was blocked again, so best-practice claims rest on renders and greps only.
