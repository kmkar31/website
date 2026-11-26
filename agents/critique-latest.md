# Critique, 2026-11-26 (after designer cycle 205)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, hasselhoff-submarine tablet-light, snake-robots phone-dark. Read LOG.md (through cycle 205), user-critique.md and the previous critique. Wix images and Google Fonts are unreachable here, so photos are absent and serifs render as fallbacks (environment limit, not a bug).

## Sources consulted
Research was only partly possible. WebFetch of the WCAG 2.2 Focus Appearance page was blocked ("permission request not answered"; same failure as last cycle). One WebSearch worked and returned titles and links only; I did not read the pages. Treat all links as pointers, not verified quotes:
- NN/g, 5 Steps to Creating a UX-Design Portfolio: https://www.nngroup.com/articles/ux-design-portfolios/ (search listing only; supports finding 3 on showing own contribution and results)
- NN/g, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/ (listing only; findings 1 to 3)
- NN/g, How to Maintain a UX Portfolio Over Time: https://www.nngroup.com/articles/maintain-ux-portfolio/ (listing only; finding 1 on stale dates)
- WCAG 2.2 Focus Appearance: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked, not read)
Topic this cycle: portfolio content for hiring managers. This is not new coverage in LOG.md, only a different angle.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, Fig. 1 plates with "Sheet N of 9". Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper and ink system in both themes. Cycle 205 fix verified: the Hasselhoff spec strip now keeps "4 BLDC" and "99 SECONDS" together at tablet width. Remaining weakness: the right column on desktop Home is ragged (rows 01 to 03, 08, 09 carry no mark).
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og:image, JSON-LD, sitemap, robots. Weak: one shared OG card; 31 wixstatic references across 12 pages (aerobraking 7, quadrotor-sysid 5), so the images and resume depend on a third party; subpath robots.txt is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy; the weak points are content only the owner can supply (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The 99 s stamp, the strike-through and the SpongeBob naming note on Hasselhoff remain the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, faint grain, both themes.
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
Cycle 205 changed only the .facts cell sizing. No regressions seen in the screenshots viewed or in check.py.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no date, while About says 2023 to 2025 and today is 2026-11-26. A recruiter cannot tell if he has graduated, where he works, or if he is available. Owner fact needed (for example "Class of 2025" plus current role). The STATUS slot in build.py is still empty. NN/g's maintenance advice points the same way: stale or undated material costs credibility.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list and the hero lede, but "Start here" sits on row 06 (aerobraking). On the phone shot it is about two screens down. Owner picks the lead, or the label moves, or the order changes.
3. Major (content). The snake page, the lead project, shows no method, result or number for what he implemented (Fig. 1 is labelled illustrative; the page is two short paragraphs). It has the least evidence of any project. Owner must supply method and result.
4. Major (credibility). Aerobraking is quoted as "46 orbits to target" on Home and Projects, and as "Terminal error: 8.4 km" in the Hasselhoff page's Next link. The designer says both are labelled on the aerobraking page; that is accepted, but the Next link shows the 8.4 km figure without a label tying it to the 46-orbit headline. Also open: "46 orbits" has no baseline, the third-person Method text hides his own contribution, and Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, most without width and height (CLS risk, outage dependency). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Whether the link is live cannot be verified offline.
6. Minor (UX). Aerobraking is long with no pull-out of what Karthik did. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home row 06 stacks stamp, tab and tags in one column; the right column is uneven elsewhere. Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate, but a third-party dependency; self-host WOFF2 when the files exist.
9. Minor (SEO). Shared OG card for every page; submitting the sitemap in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for 14+ cycles and no site change can resolve them. The owner should supply the facts and files or pause the loop.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the press-and-hold hard-shadow press state on the "See the projects" button; check contrast first.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s stamp on Hasselhoff; the tightened spec strip.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; "More on" links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test.

## Verdict
The site is coherent, plainly written and clearly authored, and does not look generated. The cycle 205 spec-strip fix works. Design work is essentially done; UX stays at 6 because of missing owner input: current status and dates, the lead project, real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Research this cycle was limited again by the blocked fetch tool, so the cited sources are unverified pointers.
