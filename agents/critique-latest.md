# Critique, 2026-11-26 (after designer cycle 206)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and desktop-dark, aerobraking-drl tablet-light, about phone-dark. Read LOG.md (through cycle 206), user-critique.md and the previous critique. Cycle 206 changed no site files (log only), so there is nothing new to regress. Wix images and Google Fonts are unreachable here, so photos are absent and serifs render as fallbacks (environment limit, not a bug).

## Sources consulted
Research was again limited. I ran two WebSearch queries, which returned titles and links only. I did not open any page, so none of the points below are quoted from the sources. They are pointers.
- NN/g, UX Design Portfolios: https://nngroup.com/articles/ux-design-portfolios/ (listing only; supports findings 1 to 3 on showing own role and results)
- ACM Interactions, what a junior designer should have in a portfolio: https://interactions.acm.org/archive/view/november-december-2025/what-should-a-junior-user-experience-designer-have-in-their-portfolio (listing only; finding 3)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (listing only; finding 5, width and height on images)
Topic this cycle: portfolio content and CLS. Neither is new coverage; the topic has not changed in many cycles.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Authored touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, "Fig. 1" plates with "Sheet N of 9". Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system holds in both themes. Desktop dark Home: tidy, but the right column is ragged (rows 01 to 03, 08, 09 have no mark), and row 06 is the only row with a thumbnail, so it reads as a different kind of row.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og:image (absolute, assets/og.png), JSON-LD, sitemap, robots. Weak: one shared OG card; 31 wixstatic references across 11 pages (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4); subpath robots.txt is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy. The weak points are content only the owner can supply (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The 99 s stamp, the strike-through and the "Start here" tab remain the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, both themes.
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed in cycle 206. Screenshots match the previous cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" with no date. About says 2023 to 2025, and today is 2026-11-26. A recruiter cannot tell whether he has graduated, what he does now, or whether he is available. The STATUS slot in build/ (STATUS = "") is still empty. Owner fact needed, for example class year plus current role. NN/g's portfolio guidance, as I understand it from the listing, favors current and dated material (taste plus unread source).
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list and hero, but "Start here" sits on row 06 (aerobraking). On the phone shot it is about two screens down. Owner picks the lead, or the label moves, or the order changes.
3. Major (content). The snake page, the lead project, has no method, result or number for what he implemented. It has the least evidence of any project. Owner must supply method and result.
4. Major (credibility). Aerobraking is quoted as "46 orbits to target" on Home and Projects, and as "Terminal error 8.4 km" on the Next link from Hasselhoff. Both are labelled on the aerobraking page (accepted), but "46 orbits" has no baseline, the Method text is third person ("Falcone et al. ... Our method") and hides his own contribution, and Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, most without width and height (CLS risk, outage dependency). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Link liveness cannot be verified offline.
6. Minor (UX). Aerobraking runs about 3,300 px at tablet with no pull-out of his own part. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven; row 06 stacks stamp, tab and tags. Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate but a third-party dependency; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card for every page; submitting the sitemap in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume are also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 15 cycles and no site change can resolve them. The last several cycles were log-only. The owner should supply the facts and files, or the loop should pause.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the hard-shadow press state from "See the projects" on the "Start here" tab.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s stamp; tightened spec strip.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; "More on" links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test (tools/focus_check.py).

## Verdict
The site is coherent, plainly written and clearly authored, and does not look generated. Design work is essentially done. UX stays at 6 because of missing owner input: current status and dates, the lead project, real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Research was limited again (search listings only, no pages opened), so cited sources are unverified pointers.
