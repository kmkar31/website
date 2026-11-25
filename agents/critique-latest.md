# Critique, 2026-11-25 (after designer cycle 202)

Method: ran `python3 tools/check.py . agents/shots` (zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, about tablet-dark. Read LOG.md (baseline plus cycles 190 to 202), user-critique.md and the previous critique. `git status` is clean: no site file edited. Wix images and Google Fonts are unreachable here, so photos are absent and serifs render as fallbacks (environment limit).

## Sources consulted
Research limit persists. WebFetch of the WCAG page below returned PROVENANCE_REQUIRED (permission not answered), so no page was read; these are principles the findings rest on, not verified quotes:
- BLOCKED: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8; the 44 px targets in the shots look fine)
- WCAG 2.2 Focus Not Obscured: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (covered by tools/focus_check.py)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (finding 5)
- NN/g, Mobile UX: https://www.nngroup.com/articles/mobile-ux/ (findings 1, 2)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, Fig. 1 plates. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system is coherent in both themes (About dark reads well). Weak: the right column on Home desktop is ragged (rows 01 to 03, 08, 09 carry no mark); row 06 stacks stamp, tab and tags; on phone the single plate and "Start here" tab sit sixth of nine, about two screens down.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD, sitemap (12 urls), robots.txt. Weak: one shared OG card; about 96 Wix image references and a filesusr resume link, none with dimensions; robots.txt under a subpath is ignored by crawlers (host limit). Search Console behaviour cannot be verified offline.
- UX: 6/10, unchanged. Findings 1 to 5 are blocked on owner facts.
- Fun and personality: 7/10, unchanged. No new moment; the 99 s press-and-hold and strike-through remain the memorable ones.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, faint grain).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
Cycles 199 to 202 changed only alt text, tools/focus_check.py and log text. No regressions in the shots or check.py.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" with no date; About says 2023 to 2025. Today is 2026-11-25, so a recruiter cannot tell whether he has graduated, is available, or where he works. Owner fact needed (for example "Class of 2025" plus current role or availability). STATUS slot in build.py is still empty.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list and hero lede; "Start here" sits on row 06 (aerobraking). On phone a skimmer sees the snake row first and the tab only after about two screens. Owner picks the lead, or the label moves to row 01 / the order changes.
3. Major (content). The snake page, the lead project, has an "illustrative" schematic, a "Why snake robots" paragraph and a lab link, but no method, result or number for what he implemented. The lead project has the least evidence. Owner must supply method and result.
4. Major (credibility). Aerobraking Setup and Method describe prior work in the third person, so his contribution on the "Start here" project is unclear; "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
5. Major (robustness, performance). Resume PDF (filesusr) and nearly all project images are hotlinked from Wix with no width/height (CLS risk, outage dependency). Resume appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner.
6. Minor (UX). Aerobraking is long (about 1,500 words) with no pull-out of what Karthik did; add a two-line "My part" box once the owner supplies it (ties to 4).
7. Minor (visual). Home desktop row 06 stacks stamp, tab and tags in one column beside the plate; the right column is uneven elsewhere. Taste; previously declined, noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; accurate but a third-party dependency. Self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card for every page; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for 12+ cycles with no possible site change. Owner should supply the facts and files or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on Hasselhoff.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and the design work is essentially done. UX stays at 6 because of missing owner input: current status, the lead project (and real content for the snake page that currently leads), what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until the owner supplies those, further design cycles polish a finished surface.
