# Critique, 2026-11-22 (HEAD 2018c4c; only change since last critique: "Same subject" Related line)

Method: `python3 tools/check.py . agents/shots` run twice, zero FAIL (only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-light and argus-mission phone-light (the new Related line). I grepped `STATUS` in build/build.py (still `""`, line 266), counted wixstatic references per page, and read the Related markup on snake, sysid, tricycle and Hasselhoff. `git status` is clean; I edited no site files. Wix and Google Fonts are unreachable here, so photos are absent and fonts fall back (environment limit).

## Sources consulted
No pages were fetched this cycle (WebFetch/WebSearch not used). These are unverified pointers carried from earlier cycles; no finding below depends on them:
- https://www.nngroup.com/articles/ux-design-portfolios/ (show your role and outcome)
- https://web.dev/articles/font-best-practices (self-host fonts, font-display)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum (2.5.8; targets pass)
- Google robots.txt spec (root host only)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Weak spots: stamps on rows 04 to 07 only leave the right column ragged; the Fig. 1 plate on row 06 is the one picture on the page; the desktop gap between blurb and metadata column is wide.
- SEO: 7/10, unchanged. Unique titles, canonical, absolute og:image, sitemap, robots.txt, JSON-LD, sane headings. Weak: one shared OG card, robots.txt under /website/ (host limit), Wix images without dimensions. The Related links add useful internal links.
- UX: 6/10, slightly better navigation, same blockers. Below 7, so Major (findings 1 to 5).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. The Related line is plain mono label plus underlined link, no drift.
2. Must not look AI-generated: met, AI-tell 2.

## Previous cycle's change (regression check)
"Same subject" works: aerobraking links to ARGUS and back, snake to landing, sysid to snake. Fine on phone (clear label, 44 px+ link, sits above the pager rule). Two small issues, see finding 7: the label is quieter than the pager and reads like a second pager; and the links are not reciprocal in every case (sysid to snake, but snake to landing; Hasselhoff to snake, tricycle to Raftar), which is acceptable but means the "Same subject" idea is a nearest-tag guess, not a curated grouping.

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; today is 2026-11-22. A recruiter cannot tell availability or whether the degree is finished. `STATUS = ""` renders a Status row once filled. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads the list while START HERE sits on row 06 (aerobraking), as seen on both phone and desktop home. The snake page is thin (no method or result). Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method is third person about prior work, Result switches to "our". The reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in header, hero, About, footer and 404. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on 11 pages (aerobraking 7, sysid 5, tricycle 4, Hasselhoff 4, tethered 4, landing 2, others 1). No width/height means CLS risk and an outage dependency. Needs local files.
6. Minor (UX). Home blurbs for 01, 02, 03 and 08 give no outcome; only 04 to 07 carry a hard number. A reader scanning 30 seconds cannot rank the rows. Same root as 2 and 3.
7. Minor (UX, new). Related line: consider labelling it by the shared tag, e.g. "More on Space", so it is clearly not a third pager entry, and avoid showing the same title twice when it is also the previous or next project (check that the code excludes both, which it appears to).
8. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
9. Minor (visual). Ragged right column on Home and the lone plate on row 06. Taste.
10. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
11. Minor (content). Tricycle page voice is passive and has no subheads. Owner call.
12. Minor (UX). Contact is LinkedIn only; the footer says so plainly. Owner constraint. Phone header drops Resume, LinkedIn and GitHub icons; they appear in hero and footer.
13. Nit (visual, taste). About leaves the right third empty on wide screens.
14. Nit (process). Findings 1 to 6 need owner facts and files. This cycle's only site change came from a design-only idea; the rest of the list is unchanged. The owner should supply the items or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar ("For the record").
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Struck-through "three weeks" highlight, stamps, numbered rows, filters, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates with sheet captions, the aerobraking result block, the new Same subject line.

## Verdict
The design is finished in the sense that matters: coherent retro matte, specific copy, no AI tells, clean checks, and the Related line is a sound small improvement without regressions. UX stays at 6 because of missing owner input: a status and dates line, a chosen lead project with a real method and result, a clear statement of personal contribution on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will return the same list.
