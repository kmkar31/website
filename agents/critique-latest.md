# Critique, 2026-11-10 (cycle 110)

Rendering: `python3 tools/check.py . agents/shots` hit my 2 minute tool timeout (exit 143), so I have no rc and no check output this cycle. It had already written fresh screenshots (timestamps 04:26-04:28 today), so I judged from those. I viewed index phone light and index desktop light. Dark and tablet shots I did not view this cycle; I rely on cycle 109 for them. `git status` is clean and the last site commit is cycle 108 (fetchpriority on first figure). No regression visible. No site files edited.

## Sources consulted
- Research was blocked. WebFetch permission requests for w3.org (WCAG 2.2 focus appearance), web.dev/articles/optimize-cls and nngroup.com/articles/mobile-ux went unanswered, and I did not retry. I therefore cite nothing new this cycle, which falls short of the three-source rule in critic.md. Topics I intended: CLS (image dimensions, font fallbacks), focus appearance, mobile content prioritization.
- Carried over from cycle 109, read then: https://web.dev/articles/fetch-priority ; https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt must sit at the host root).

## Scores
- AI-tell: 2/10, unchanged. Flat paper with grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger, serif pairing (DM Serif Display with Source Serif 4, not Inter), plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Desktop home is calm, with a clear measure and strong name. Weak spots: row 06 is the only plate, so the list rhythm breaks (phone and desktop); the right metadata column on desktop leaves a wide empty gutter between blurb and tags.
- SEO: 7/10. Unchanged from 109: unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt under subpath, single og:image, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are all on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plate, ledger. Nothing new that repo facts support.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradients, blur or glow seen.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-10 with no status line; STATUS = "" at build/build.py:262, so the ledger omits a Status row (confirmed in the home screenshot: only Built, Internships, Toolbox). A recruiter cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page states no result, while "Start here" and the only plate sit on row 06 (46 orbits to target). Two answers to "strongest project". Owner decision: pick one, or give the snake work a result.
3. Major (robustness, CLS). Figures and Resume hotlinked from Wix with no width/height. If URLs rotate, the Resume link breaks in header, lede and both footers. Needs owner-supplied local files and real dimensions.
4. Major (credibility). raftar-formula-racing.html contains one "Ferrari" comparison ("one-fifth the weight ... matches its 0-60") with no support elsewhere in the repo. Owner: source it or cut it.
5. Minor (SEO). robots.txt is served under /website/, so crawlers ignore it and its Sitemap line is not discovered. Submit the sitemap in Search Console (owner). lastmod is identical on all URLs.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts, swap, no size-adjusted fallback; needs measured metrics or self-hosting. Footer text states "no framework" while still depending on Google Fonts, a small honesty nit.
8. Minor (looks, taste). Plate only on row 06.
9. Minor (looks, taste). About: empty right side on wide screens until a portrait exists. Boxed "podium finish" stamp loosens a line on tablet (seen in 109).
10. Minor (UX, phone). Header drops Resume and GitHub; both remain in lede and footer. Acceptable.
11. Minor (UX). Contact is LinkedIn only; single point of failure, owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
13. Nit (looks). Small mono labels are the faintest text on tan; they passed AA in earlier checks (taste). Not re-measured this cycle because check.py timed out.

Designer-fixable this cycle: none.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent, not generic, and no regression from the fetchpriority change. Everything material still waits on the owner: a status line, a lead-project decision or snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. Caveats on this cycle: the automated check did not complete in time and all external research was blocked, so this critique leans on visual inspection of two screenshots and on cycle 109's measurements.
