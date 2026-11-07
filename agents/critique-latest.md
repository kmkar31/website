# Critique, 2026-11-07 (cycle 92)

Rendering: `python3 tools/check.py . agents/shots` rc=0, 78 lines OK (13 pages x 3 viewports x 2 themes), only "images not loaded" sandbox notes. I viewed index phone light, index desktop dark, aerobraking tablet light, projects phone dark. Greps: `STATUS = ""` (build/build.py:262); wixstatic hotlinks on 11 of 13 pages (about 1 to 7 each). No site files edited.

## Sources consulted (honest note)
WebFetch was blocked this cycle (permission request unanswered) for all three: web.dev/articles/optimize-cls, w3.org WCAG 2.2 focus-appearance understanding page, nngroup.com/articles/portfolio-reviews. I read no source body, so the three-source rule is NOT met; no finding below depends on a citation. Unverified pointers:
- https://web.dev/articles/optimize-cls (image width/height, font fallback)
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (sticky header vs focus; not tested this cycle)
- https://www.nngroup.com/articles/portfolio-reviews/

## Scores
- AI-tell score: 2/10, unchanged. Paper tone, double rules, hard-offset button, struck-through "three weeks" on amber, number stamps, "Fig. 1 / Sheet n of 9 / NTS" captions. No gradient, blur, glow, card trio, stats strip. Residual tells: stock "intro, ruled list, footer" index; blurbs share one cadence. Nothing moved since last cycle.
- Looks good: 8/10. Hierarchy and rhythm hold on all four views. Weak spots: home has one plate among nine rows (row 06), so the list is visually lopsided; About right third empty on desktop.
- SEO: 7/10. Title, description, canonical, OG/Twitter, JSON-LD, sitemap, 404 present. Risks: robots/sitemap at a project-site subpath, one generic og:image, hotlinked media, undimensioned figures.
- UX: 6/10. Identity, projects, LinkedIn found in seconds. Penalised by stale status and no quantified top project.
- Fun and personality: 7/10. Pressable 99 s stamp, 404 game line, struck-through marker, plates. Home has little beyond the strike-through; the rest is one click down.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met (flat paper, grain, hard shadow only on primary button, inverted-print dark theme).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Master's is shown as 2023-2025 / "MS ... Carnegie Mellon" with today 2026-11-07; the Status row in "For the record" never renders because STATUS is empty. A recruiter cannot tell graduated vs studying vs available. Owner fact needed: one line.
2. Major (robustness, CLS). All project photos still hotlinked from static.wixstatic.com and Resume from filesusr.com; figures lack width/height. If Wix rotates URLs, every photo and the Resume link on every page break. Needs owner files in assets/ and real dimensions.
3. Major (UX, 30-second test). "Start here" sits on row 06 (aerobraking, the only row with a plate), while the lede leads with snake robots (row 01), whose page has only a tl;dr and no outcome. Two answers to "strongest project". Fix: owner result for snake; or move the label only when row 01 has a result.
4. Major (content). Raftar "Ferrari" comparison is original-site copy, unverified. Owner to confirm a figure or cut.
5. Minor (content/robustness). Aerobraking Result text says "as shown below" and "as shown in the figure above" for images that are Wix hotlinks; if they fail, prose points at nothing. Same dependency as finding 2; consider rewording to not depend on figures, using only existing facts.
6. Minor (looks). About desktop: right third empty beside Skills/Education/Experience. Taste; reads unfinished until a portrait exists.
7. Minor (SEO). robots.txt and sitemap.xml under /website/ are ignored by crawlers for robots; submit sitemap in Search Console (owner). lastmod is identical on all URLs.
8. Minor (SEO). One og:image for all pages; per-project share cards would help LinkedIn previews. Low priority.
9. Minor (fonts). Two Google Fonts, display=swap, no size-adjusted fallback; self-hosting needs WOFF2 from owner.
10. Minor (UX, phone). Header drops Resume/GitHub on phones; Resume is in lede and footer. Acceptable, documented.
11. Nit (copy). Home row blurbs share one construction (verb-led summary, "so they can ..."); vary two or three using facts already on each page.
12. Nit (looks). Small mono labels (01-09, tags) are the faintest text on tan; contrast passes but reads faint on phone.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; number stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; pager shows neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic; I found no regression and no designer-fixable defect of weight. What holds it back is missing owner input: a current status line, a result for the snake work, a confirmed Raftar claim, and local copies of the resume and images. Until then the biggest risks are a stale 2023-2025 timeline and Wix hotlinks that could break the Resume link and every photograph. This cycle's web research was blocked, so best-practice claims here rest on renders and repo greps only.
