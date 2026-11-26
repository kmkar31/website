# Critique, 2026-11-26 (after designer cycle 204)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, about phone-dark, hasselhoff-submarine tablet-light. Read LOG.md (cycles 193 to 204), user-critique.md and the previous critique. Wix images and Google Fonts are unreachable here, so photos are absent and serifs render as fallbacks (environment limit, not a bug).

## Sources consulted
Research this cycle was blocked. Three WebFetch calls (WCAG 2.2 Target Size Minimum, web.dev optimize-cls, NN/g mobile UX) all came back "permission request not answered" and returned no page text. The links below are pointers the findings lean on as principles, not verified quotes. A reader should not treat them as researched this cycle:
- WCAG 2.2 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (not read; the site's 44 px targets exceed the 24 px floor as far as the CSS shows)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (not read; finding 4)
- NN/g, Mobile UX: https://www.nngroup.com/articles/mobile-ux/ (not read; findings 1 and 2)
- Carried from earlier cycles, also unread this time: NN/g UX portfolios https://www.nngroup.com/videos/ux-portfolios-hiring/

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, Fig. 1 plates with "Sheet N of 9". Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper and ink system. Desktop Home reads cleanly. Weak: right column on desktop Home is ragged (rows 01 to 03, 08, 09 carry no mark); the Hasselhoff spec strip leaves a large empty gap between "Thrusters" and "Time allowed" at tablet width.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og:image with width, height and alt, JSON-LD, sitemap, robots, lang. Weak: one shared OG card; 96 wixstatic references across 13 pages and only 9 `<img>` tags carry width attributes; subpath robots.txt is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy. Weak points are all content the owner has to supply (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The 99 s press-and-hold and the strike-through remain the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, faint grain, both themes.
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
Cycles 199 to 204 changed alt text, tools/focus_check.py and log text only. No regressions in the screenshots or check.py.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no date, while About says 2023 to 2025 and today is 2026-11-26. A recruiter cannot tell whether he has graduated, where he works, or if he is available. Owner fact needed (for example "Class of 2025" plus current role). The STATUS slot in build.py is still empty.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list and the hero lede, but "Start here" sits on row 06 (aerobraking), about two phone screens down. Owner picks the lead, or the label moves, or the order changes.
3. Major (content). The snake page, the lead project, shows no method, result or number for what he implemented. It has the least evidence of any project. Owner must supply method and result.
4. Major (credibility, new detail). Aerobraking is quoted two ways: Home and Projects stamp "46 orbits to target", while the Hasselhoff page's Next link shows "Terminal error: 8.4 km" for the same project (also in the aerobraking page and tethered page text). They may be different metrics, but a reader meets two headline numbers with no label tying them together. Confirm both against the page and state which is the headline; also, the third-person Setup and Method text hides his own contribution, "46 orbits" has no baseline, and Raftar's Ferrari comparison has no source.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, most without width and height (CLS risk, outage dependency). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Whether the filesusr link is live cannot be verified offline.
6. Minor (UX). Aerobraking is long with no pull-out of what Karthik did. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home row 06 stacks stamp, tab and tags in one column; the right column is uneven elsewhere. Previously declined; noted only.
8. Minor (visual). Hasselhoff spec strip: two cells with a wide empty middle at tablet width (about 330 px of nothing). Either set the cells on a tighter grid or add the missing third spec only if a real one exists in the page text.
9. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate, but a third-party dependency; self-host WOFF2 when the files exist.
10. Minor (SEO). Shared OG card for every page; submitting the sitemap in Search Console is an owner action.
11. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
12. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for 13+ cycles and no site change can resolve them. The owner should supply the facts and files or pause the loop.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the press-and-hold hard-shadow press state on the "See the projects" button; check contrast first.

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
The site is coherent, plainly written and clearly authored, and does not look generated. Design work is essentially done; UX stays at 6 because of missing owner input: current status, the lead project and real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. One new item this cycle is the unlabeled pair of aerobraking figures (46 orbits versus 8.4 km). Research was not completed this cycle because the fetch tool was blocked, so the cited sources are unverified pointers.
