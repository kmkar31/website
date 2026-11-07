# Critique, 2026-11-07 (cycle 96)

Rendering: `python3 tools/check.py . <scratchpad>/shots` ran in the background (it exceeds a 2-minute tool timeout in the foreground). Every line reported OK for 13 pages x 3 viewports x 2 themes; the only notes are "images not loaded" (sandbox). I viewed index phone light, index desktop dark and snake-robots tablet light. Repo greps: `STATUS = ""` (build/build.py:262); Ferrari claim at raftar-formula-racing.html:48; wixstatic references on 11 of 13 pages (7 on aerobraking-drl); the "As shown below" sentence from last cycle is gone (no regression). No site files edited.

## Sources consulted
WebFetch was refused for every URL this cycle (permission request unanswered), so no page body was read. Only WebSearch result listings were available; I rely on them only for the existence and scope of these pages, and on the repo for everything else:
- WCAG 2.2 Understanding 2.5.8 Target Size (Minimum), https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (listed in search results; AA minimum is 24 CSS px; the site's 44 px targets exceed it).
- web.dev, CSS size-adjust for @font-face, https://web.dev/articles/css-size-adjust (listed in search results only).
- Carried over from cycle 95 (read in full then): web.dev Optimize CLS, https://web.dev/optimize-cls/; UX Design Institute on hiring managers, https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/.
Unverified this cycle: anything about size-adjust specifics, and Search Console behavior.

## Scores
- AI-tell score: 2/10, unchanged. Flat paper, double rules, one hard-offset button, struck-through "three weeks" on amber, double-border stamps, "Fig. 1 / Sheet n of 9" captions, plain first-person lede. No gradients, blur, glow, card trio, stats strip or slogans. Residual: intro, ruled list, dark footer is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Phone and desktop-dark renders hold: clear hierarchy, steady ruled rhythm, dark theme reads as inverted print. Weak spots: row 06 is the only row with a plate, so the list is lopsided (on phone the plate sits above the title and breaks the rhythm); snake-robots page (the lede project) is a big schematic plus one short paragraph, so the page feels unfinished next to the others; About desktop right third empty.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter with absolute og:image 1200x630, JSON-LD, sitemap, 404, one h1. Risks: robots.txt and sitemap live under /website/, not the host root (crawlers ignore robots.txt there); one og:image for all pages; hotlinked figures without dimensions; identical lastmod (2026-11-02) on every URL.
- UX: 6/10. On the phone render, name, field, lede, Resume and LinkedIn are visible without scrolling past the first screen, which is good. Held down by: no current status (graduated or not) and no quantified result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, "For the record" ledger. Home has little beyond the strike-through; project pages carry the character.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met (flat paper, grain, one hard shadow, inverted-print dark mode, no blur).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" against today 2026-11-07; the Status row never renders because STATUS is empty. A recruiter cannot tell graduated, studying or available. Owner must supply one line.
2. Major (UX, 30-second test). The lede leads with snake robots (row 01) but its page has only a schematic, one paragraph and a link out to the lab; "Start here" sits on row 06 (the only row with a plate). Two answers to "strongest project", and the lede one is the thinnest (snake-robots tablet render). Owner to supply a snake result or choose the lead.
3. Major (robustness, CLS). Project photos and the Resume are hotlinked from Wix (wixstatic.com, filesusr.com) on 11 pages; figures carry no width/height (web.dev CLS guidance). If Wix rotates URLs, Resume breaks in header, lede and every footer. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time". Nothing in the repo supports it. Owner to confirm or cut.
5. Minor (SEO). robots.txt and sitemap at a project-site subpath: robots.txt is not honoured there; submit the sitemap in Search Console (owner). lastmod identical across URLs.
6. Minor (SEO). One og:image and og:image:alt ("robotics and controls engineer") on every page; no per-project art exists. Low priority.
7. Minor (looks). Home list lopsided: one plate on row 06. Either accept as the deliberate "lead" or add plates only when real figures exist. Taste.
8. Minor (looks). About desktop: empty right third until a portrait exists. Taste.
9. Minor (fonts). Two Google Fonts, display=swap, no size-adjusted fallback; needs measured metrics.
10. Minor (UX, phone). Header drops Resume and GitHub on phones; Resume remains in lede and footer. Acceptable.
11. Nit (copy). Home blurbs share a verb-led cadence; vary two or three only with facts already on the pages.
12. Nit (looks). Small mono labels (01-09, tags) are the faintest text on tan; passes AA, reads faint on phone. Taste.

Designer-fixable this cycle: none new. No regression from cycle 95.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic, and the cycle 95 fix landed cleanly. Nothing new is designer-fixable. The risks that remain all need the owner: a current status line, a result or a decision on the lead project (the snake page is the thinnest page and sits first), a confirmed or cut Raftar claim, and local copies of the Resume and images with real dimensions. Research was weak this cycle because page fetches were blocked; only search listings were seen, so no new best-practice claims are made.
