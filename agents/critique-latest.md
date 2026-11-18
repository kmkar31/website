# Critique, 2026-11-18 (HEAD 08416fb; no site files edited)

Method: `python3 tools/check.py . agents/shots` finished with zero FAIL (only "images not loaded" sandbox notes; run with a 10 minute timeout). I viewed index phone-light and desktop-light, and snake-robots phone-light. I grepped the HTML for Wix references (wixstatic counts per page: about 1, aerobraking 7, argus 1, tricycle 4, submarine 4, landing 2, sysid 5, raftar 1, snake 1, tethered 4, projects 1, index 0), the resume URL (still the Wix hotlink), and STATUS (build/build.py line 266 is still `""`). `git status` is clean. The site is unchanged: tenth consecutive cycle with no site change. Wix and Google Fonts are unreachable here, so screenshots show fallback faces and no photos (environment limit).

## Sources consulted
WebFetch was blocked again (PROVENANCE_REQUIRED, permission not answered). I read none of the pages below and no finding depends on them. The "at least three sources" rule was not met for the third cycle running; this is a tooling limit.
- https://web.dev/articles/optimize-cls (blocked; image dimensions and CLS)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (not attempted after the block)
- https://developer.mozilla.org/en-US/docs/Web/CSS/font-display (not attempted after the block)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, coherent flat dark theme. Weak spots: stamps appear only on rows 04 to 07, so the desktop right column is ragged; the Fig. 1 plate on row 06 reads as a stray on phone; empty paper under the sidebar on desktop.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, og:image. Weak: one shared OG card, robots.txt under /website/ is ignored by crawlers (host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or dates. The hero says "MS Mechanical Engineering, Carnegie Mellon University" in present tense and About says 2023 to 2025, but today is 2026-11-18. A recruiter sees an unexplained gap and cannot tell availability. `STATUS` is wired to render a ledger row; the owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the lede, but its page (viewed on phone) has only a question, a one-paragraph "Why snake robots" and a lab link: no method, result or personal contribution. START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond the cited prior work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari but matches its 0-60 time" has no source on the page. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, About, footer and 404. If Wix lapses it breaks everywhere. It needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix images remain on every content page, 1 to 7 references each. No width/height means CLS risk and an outage dependency. It needs local files, then dimensions and fetchpriority="high" on the first visible image.
6. Minor (performance, consistency). Fonts load from Google Fonts, while the footer says "one stylesheet, no framework". Self-host WOFF2 with font-display when files exist.
7. Minor (visual). Ragged Home right column and the lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; the robots.txt path is a host limit. Noted, not pressed.
10. Minor (content). The tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
12. Nit (visual, taste). The About right third is empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; ten design-only cycles have returned nothing. Recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures in the automated check.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact on project pages, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, FIG. 1 schematic with honest "module count is illustrative" caption.

## Verdict
The site is coherent, plain and clearly authored, with AI-tell 2 and a convincing retro matte commitment in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a substantive page behind it, sourced or explained claims, and local copies of the resume, images and fonts. Until those arrive, design-only cycles will return the same findings. Research was blocked again, so none of this rests on newly read sources.
