# Critique, 2026-11-22 (HEAD df765a3; no site files changed since cycle 151)

Method: `python3 tools/check.py . agents/shots` finished with zero FAIL (only "images not loaded" sandbox notes; it needs a background run, about 6 minutes). I viewed index phone-light, index desktop-light and snake-robots tablet-dark, and grepped titles, robots.txt, sitemap, `STATUS` in build/build.py and Wix references. Google Fonts and Wix are unreachable here, so screenshots use fallback faces and show no photos (environment limit). No site files edited. The site is visually identical to the previous critique, so I do not re-argue settled points.

## Sources consulted
WebFetch was not used; WebSearch returned listings only, so these are cited by title, not quoted.
- https://www.nngroup.com/articles/ux-design-portfolios/ (portfolio content for hiring managers: show your own role and process, not just outcomes)
- https://web.dev/articles/font-best-practices and https://web.dev/patterns/web-vitals-patterns/fonts/font-self-hosted (self-host fonts, font-display; relevant to finding 6)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum (2.5.8, 24 px minimum; the 44 px targets pass, so no finding)
- Carried from earlier cycles: Google robots.txt spec (root host only), web.dev fetch-priority and optimize-cls.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme. Seen: stamps only on rows 04 to 07 leave the right column ragged; the Fig. 1 plate sits above row 06 on phone like a stray; wide gutter between description and metadata on desktop.
- SEO: 7/10, unchanged. Unique titles (e.g. "Gait-based Control of Modular Snake Robots | Karthik Karumanchi"), canonical and absolute og:image, sitemap with 12 urls, robots.txt, JSON-LD. Weak: one shared OG card, robots.txt under /website/ (ignored by Google, host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "Sheet 1 of 9 NTS" captions, 404 joke, orbit plate. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). Hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; today is 2026-11-22. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` (build/build.py line 266) already renders a Status row when filled. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, yet its page is thin (seen: question, one schematic, two sentences, one link, no method or result); START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result. NN/g advice is to show your own role and outcome.
3. Major (credibility). The aerobraking page describes Method in third person about Falcone et al., then says "our NN state-space model" and "our method"; the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in header, hero, About, footer and 404. If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on 11 pages (line counts: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, others 1 each). No width/height means CLS risk and an outage dependency. Confirm every `alt=""` is truly decorative; not verifiable offline.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 with font-display (web.dev font-best-practices) when files exist.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint. Phone header drops Resume, LinkedIn and GitHub icons; they appear in hero and footer, acceptable.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. This is roughly the eighth consecutive cycle with no site change. Owner should supply the items or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, project next-links, Fig. 1 plates with sheet captions, the aerobraking result block.

## Verdict
The design is finished in the sense that matters: coherent retro matte, specific copy, no AI tells, clean checks. What holds it at UX 6 is not design but missing owner input: status and dates, a chosen lead project with a real method and result, a clear statement of personal contribution on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will keep returning the same list.
