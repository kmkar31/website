# Critique, 2026-11-08 (cycle 100)

Rendering: `python3 tools/check.py . agents/shots` finished, rc clean: 13 pages x phone/tablet/desktop x light/dark, every line OK, only "images not loaded" sandbox notes. I viewed index phone light, index desktop dark, snake-robots tablet light. Fonts did not load in the sandbox, so the screenshots show the serif fallback. No site files edited. HEAD 889f7e6 (log-only commit; no site change since cycle 97). No regression seen.

## Sources consulted
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), read: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24x24 CSS px minimum, with spacing and inline-text exceptions; the site's 44 px targets exceed it)
- web.dev, Optimize CLS, read via a mirror: https://tewebdev.pages.dev/optimize-cls (always set width and height on images; wrong dimensions still shift less than none; CSS aspect-ratio is the fallback)
- NN/g, UX Portfolios: What Hiring Managers Look For (survey of 200+ hiring managers), only the summary was readable: https://www.nngroup.com/videos/ux-portfolios-hiring/ . Companion: https://www.nngroup.com/videos/ux-portfolios-interviews/ (a portfolio must first persuade someone to book an interview). I used these only for the general point that the portfolio has to make the case fast, not for any specific number.
- Searches for hiring-manager portfolio guidance returned mostly blog posts; I did not rely on them.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, struck-through "three weeks" on amber, stamps, Fig./Sheet captions, mono ledger, plain first-person lede. No gradients, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer band is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. In both themes the ruled rhythm holds, the dark theme reads as inverted print, and the hierarchy is clear. Weak spots: row 06 is the only row with a plate. On phone its plate sits above the title and breaks the list rhythm. On desktop the plate beside the title is fine. Snake page: a large plate and one sentence, then the pager, so the page is under-filled. About desktop right third is empty.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Unchanged risks: robots.txt and sitemap under a /website/ subpath, one og:image for every page, hotlinked figures with no dimensions, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn all sit on the first phone screen, which is good. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, ledger. Home is otherwise quiet; nothing to add that is not already in the repo.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat surfaces, hard shadow, grain, inverted-print dark).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" read against today (2026-11-08) with no status line rendered. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots. That page (viewed) is one plate, one question and one background sentence, with no result, while "Start here" sits on row 06. Two answers to "strongest project", and the lede's answer is the weakest. NN/g's point is that the portfolio must quickly persuade; this is the first thing a reader opens. Owner: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix (wixstatic.com, filesusr.com), 3 to 9 references per page, with no width/height. web.dev: unsized images shift layout, and wrong dimensions still shift less than none. If the URLs rotate, the Resume link breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar question: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo (raftar-formula-racing.html line 48). Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap live at a project-site subpath; crawlers read robots.txt only at the host root. Submit the sitemap in Search Console (owner). lastmod identical across pages. Not re-verified against Google docs this cycle.
6. Minor (SEO). One og:image for every page; no per-project art.
7. Minor (looks). Plates on one row only; taste. Add plates only with real figures.
8. Minor (looks). About desktop empty right third until a portrait exists; taste.
9. Minor (fonts). Two Google Fonts with swap and no size-adjusted fallback; needs measured metrics or self-hosted files.
10. Minor (UX, phone). Header drops Resume and GitHub on phones; both stay in lede and footer. Acceptable.
11. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
12. Nit (looks). Small mono labels are the faintest text on tan; they pass AA, taste.

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, native color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets (above the WCAG 2.5.8 24 px floor).

## Verdict
The site is authored, coherent and not generic, with no regression and no designer-fixable defect left that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research this cycle confirmed existing practice (target size, image dimensions) and added no new findings.
