# Critique, 2026-11-23 (HEAD 33ee6c5; only change since last critique: Related label now "More on <tag>")

Method: `python3 tools/check.py . agents/shots` ran to completion, 79 lines, zero FAIL (only "images not loaded" sandbox notes); full output saved in `agents/check-latest.txt`. I viewed index phone-light, tablet-light and desktop-dark. I ran a Playwright keyboard probe on aerobraking-drl at 390 px (sticky header is 57 px; `scroll-padding-top:80px` is set; tabbing reaches header links only at the top, no focused element hidden under it). I counted wixstatic references per page and checked the resume href (filesusr.com Wix PDF). I edited no site files. A no-JS probe errored in my script, so no-JS behaviour is not re-verified this cycle. Wix and Google Fonts are unreachable here, so photos are absent and fonts fall back (environment limit).

## Sources consulted
WebSearch returned result lists only; I did not open the pages, so these are pointers, not quoted evidence, and no finding depends on them:
- https://nngroup.com/articles/ux-design-portfolios/ (show role and outcome in project work)
- https://web.dev/articles/optimize-cls (set width/height on images to avoid layout shift)
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured (2.4.11; sticky header check above passes)
Topic this cycle: focus not obscured by sticky header (passes), plus carried-over CLS and portfolio-content points.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Weak spots: stamps on rows 04 to 07 only leave the right column ragged; the Fig. 1 plate on row 06 is the lone picture on Home; on desktop the blurb-to-metadata gap is wide; the tablet screenshot shows the strikethrough highlight appearing correctly but nothing else changed.
- SEO: 7/10, unchanged. Unique titles, canonical, og:image, sitemap, robots.txt, JSON-LD, sane headings. Weak: one shared OG card, robots.txt under /website/ (host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 5).
- Fun and personality: 7/10, unchanged. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink rules, hard shadow, flat dark theme (checked in screenshots).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Previous cycle's change (regression check)
"More on <tag>" label: no regression seen in check output; reads as a topical link rather than a third pager entry. Resolves last cycle's finding 7. Not re-viewed on a project page screenshot beyond check.py passing.

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; today is 2026-11-23. A recruiter cannot tell availability or whether the degree is finished. `STATUS` in build/build.py is empty. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads while START HERE sits on row 06 (aerobraking), visible on phone, tablet and desktop. The snake page has no method or result. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method is third person about prior work and Result switches to "our"; the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix filesusr.com URL in header, hero, About, footer and 404. It is the one artifact a recruiter wants. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance, robustness). Wix image references remain on 10 pages (aerobraking 7, sysid 5, tricycle 4, Hasselhoff 4, tethered 4, landing 2, about, argus, projects, raftar, snake 1 each). No width/height means CLS risk (web.dev link above) and an outage dependency. Needs local files.
6. Minor (UX). Home blurbs 01, 02, 03 and 08 give no outcome; only 04 to 07 carry a hard number. A 30-second scan cannot rank the rows. Same root as 2 and 3.
7. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
8. Minor (visual, taste). Ragged right column on Home and the lone plate on row 06.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive and has no subheads. Owner call.
11. Minor (UX). Contact is LinkedIn only; the footer says so plainly. Owner constraint. Phone header drops Resume, LinkedIn and GitHub icons; they appear in hero and footer.
12. Nit (visual, taste). About leaves the right third empty on wide screens.
13. Nit (process). Findings 1 to 6 need owner facts and files; the loop has returned the same list for many cycles. The owner should supply the items or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Struck-through "three weeks" highlight, stamps, numbered rows, filters, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, the aerobraking result block, the "More on <tag>" line, sticky header that does not hide focus (scroll-padding-top 80 px vs 57 px header).

## Verdict
Design is coherent and finished: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 because of missing owner input: a status and dates line, a chosen lead project with real method and result, a clear statement of personal contribution on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will return the same list.
