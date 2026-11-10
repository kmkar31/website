# Critique, 2026-11-10 (cycle 111)

Rendering: `python3 tools/check.py . agents/shots` run in the background to completion (78 lines OK, no FAIL; only "images not loaded, sandbox network" notes). I viewed index phone light and index desktop light from the fresh shots. Dark, tablet and inner pages not re-viewed this cycle; I rely on earlier cycles. No site files edited; git state untouched.

## Sources consulted
- Research was blocked again: the WebFetch permission request for https://web.dev/articles/optimize-cls went unanswered ("do not retry"). No new sources were read, so the three-source rule is not met this cycle. Nothing below depends on an unread source.
- Carried over from cycle 109, read then: https://web.dev/articles/fetch-priority ; https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt must sit at the host root).

## Scores
- AI-tell: 2/10, unchanged. Paper and grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger, DM Serif Display with Source Serif 4, plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Desktop is calm with a strong name and clear measure. Weak spots: row 06 is the only plate, which breaks list rhythm (phone and desktop); on desktop there is a wide empty gutter between blurbs and the tag column; rows 02, 03, 08, 09 carry only a number and tags.
- SEO: 7/10. Unchanged: unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt under a subpath, one og:image, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn all sit on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, Fig. 1 plate, ledger. Nothing new that repo facts support.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradients, blur or glow seen.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). The subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About's "2023 - 2025" are read on 2026-11-10 with no status line. `STATUS = ""` at build/build.py:262, so the ledger shows only Built, Internships, Toolbox (confirmed in both screenshots). A recruiter cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result, while "Start here" and the only plate sit on row 06 (46 orbits). That gives two answers to "strongest project". Owner decision: pick one, or give the snake work a result.
3. Major (robustness, CLS). Figures and the Resume are hotlinked from Wix with no width/height. If the URLs rotate, the Resume link breaks in the header, lede and footer. Needs owner-supplied local files and real dimensions.
4. Major (credibility). The Raftar page question reads "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (build/build.py, `q=`). Nothing else in the repo supports it. Owner: source it or cut it.
5. Minor (SEO). robots.txt is served under /website/, so crawlers ignore it and its Sitemap line is not discovered. Submit the sitemap in Search Console (owner action). lastmod is identical on all URLs.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. The footer says "no framework" while still depending on Google Fonts, a small honesty nit.
8. Minor (looks, taste). A plate on row 06 only; the four bare rows read thin beside it.
9. Minor (looks, taste). About has an empty right side on wide screens until a portrait exists.
10. Minor (UX, phone). The header drops Resume and GitHub; both remain in the lede and footer. Acceptable.
11. Minor (UX). Contact is LinkedIn only; a single point of failure, but the owner's choice.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
13. Nit (looks). Small mono labels are the faintest text on tan. They passed AA in earlier checks; not re-measured this cycle.

Designer-fixable this cycle: none.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "schematic" notes.
- Plain first-person lede with real specifics and no slogan copy.
- Failed images collapse cleanly; the pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic, with no regression since the fetchpriority change. Everything material still waits on the owner: a status line, a lead-project decision or a snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. Caveat: external research was blocked again, so this cycle rests on the full automated check plus two viewed screenshots.
