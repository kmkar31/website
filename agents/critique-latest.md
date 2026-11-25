# Critique, 2026-11-25 (after designer cycle 203)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and desktop-dark, and snake-robots phone-light. Read LOG.md (cycles 193 to 203), user-critique.md and the previous critique. `git status` showed no site file changed in cycles 199 to 203 apart from alt text and tools. Wix images and Google Fonts are unreachable here, so photos are absent and serifs render as fallbacks (environment limit, not a bug).

## Sources consulted
Research was thin this cycle. WebSearch returned only result titles and no page text, and I did not open the pages. The links below are what the findings lean on as principles, not verified quotes:
- NN/g, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/ (findings 1 to 3: state your role and outcome per project)
- Google Search Central, ProfilePage structured data: https://developers.google.com/search/docs/appearance/structured-data/profile-page (finding 9: optional markup idea, not a defect)
- Google Search Central, basic search visibility checklist: https://developers.google.com/search/docs/basics/basic-search-visibility-checklist.pdf (SEO basics; sitemap and per-page titles already met)
- Carried from the previous cycle, also not read: WCAG 2.2 Focus Not Obscured https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html; web.dev CLS https://web.dev/articles/optimize-cls

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, Fig. 1 plates. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. The paper and ink system is coherent in both themes; the desktop dark Home reads well. Weak: the right-hand column on desktop Home is ragged (rows 01 to 03, 08, 09 carry no mark, rows 04 to 07 do), and the plate and "Start here" tab sit sixth of nine, about two phone screens down.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD (Person, CollegeOrUniversity on Home; CreativeWork on projects), og:image with alt, sitemap, robots.txt, lang set, one h1 on About. Weak: one shared OG card; about 96 hotlinked Wix image references, few with dimensions; robots.txt under a subpath is ignored by crawlers (host limit). Search Console behaviour cannot be verified offline.
- UX: 6/10, unchanged. Findings 1 to 5 are blocked on owner facts. Contact, resume and project navigation are otherwise easy to find.
- Fun and personality: 7/10, unchanged. The 99 s press-and-hold and the strike-through remain the memorable moments. No new idea this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, faint grain, in both themes.
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
Cycles 199 to 203 changed only alt text, tools/focus_check.py and log text. No regressions in the shots or check.py.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" with no date. About says 2023 to 2025, and today is 2026-11-25. A recruiter cannot tell whether he has graduated, is available, or where he works now. Owner fact needed (for example "Class of 2025" plus current role or availability). The STATUS slot in build.py is still empty.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list and the hero lede, but "Start here" sits on row 06 (aerobraking). On phone the skimmer sees the snake row first and the tab only after about two screens. Owner picks the lead, or the label moves, or the order changes.
3. Major (content). The snake page, the lead project, has an "illustrative" schematic (module count not real), a "Why snake robots" paragraph and a lab link, but no method, result or number for what he implemented. The lead project has the least evidence on the site. Owner must supply method and result. NN/g's portfolio guidance is that each project should show your role and outcome.
4. Major (credibility). Aerobraking Setup and Method describe prior work in the third person, so his contribution on the "Start here" project is unclear. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner supplies a sentence and source, or cuts it.
5. Major (robustness, performance). The resume PDF (filesusr) and nearly all project images are hotlinked from Wix, mostly without width/height (CLS risk, outage dependency). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Not verifiable offline whether the filesusr link is live.
6. Minor (UX). Aerobraking runs long with no pull-out of what Karthik did. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home row 06 stacks stamp, tab and tags in one column; the right column is uneven elsewhere. Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate, but it is a third-party dependency. Self-host WOFF2 when the files exist.
9. Minor (SEO). Shared OG card for every page. robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). The tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for 12+ cycles and no site change can resolve them. The owner should supply the facts and files or pause the loop.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page that echoes the 99 s limit (for example how the clock starts), only if that is a true detail the owner confirms.
- Reuse the press-and-hold mechanic's hard-shadow press state on the "See the projects" button; check it against the contrast rule before shipping.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on Hasselhoff.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; "More on" links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test.

## Verdict
The site is coherent, plainly written and clearly authored. It does not look generated, and the design work is essentially done. UX stays at 6 because of missing owner input: current status, the lead project (and real content for the snake page that currently leads), what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until the owner supplies those, further design cycles polish a finished surface. This cycle's research was shallow because the search tool returned titles only, so treat the cited sources as pointers.
