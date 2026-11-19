# Critique, 2026-11-19 (HEAD abb9b42; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion with zero FAIL (only "images not loaded" sandbox notes). I viewed index desktop-light, index phone-dark and about tablet-light. I grepped the HTML: wixstatic references per page are about 1, aerobraking 7, argus 1, tricycle 4, submarine 4, landing 2, sysid 5, raftar 1, snake 1, tethered 4, projects 1, index 0. `STATUS = ""` is still at build/build.py:266. The site has not changed for eleven consecutive cycles. Wix and Google Fonts are unreachable here, so screenshots show fallback faces and no photos (environment limit, not a design bug).

## Sources consulted
WebSearch worked this cycle but returned only titles and URLs. WebFetch was not used, so I read none of the pages. No finding depends on them; they are pointers, not evidence.
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (NN/g, what hiring managers look for in portfolios; supports findings 1 to 3)
- https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (secondary; same topic)
- https://aem.live/developer/font-fallback (font fallback and CLS; supports finding 6)
- https://unlighthouse.dev/learn-lighthouse/cls/web-fonts-causing-foit (secondary; web fonts and layout shift)
The "three primary sources" rule was not met: only one is a primary source and none were read. This is a tooling limit.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific: three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether. Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. The large serif name, mono credential line, ledger sidebar, ruled list and single hard-offset button hold together in light and dark. Weak spots: stamps appear only on rows 04 to 07, so the desktop right column is ragged; the Fig. 1 plate on row 06 reads as a stray on phone; there is empty paper under the sidebar on desktop and in the right third of About.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD and a local og:image. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images have no dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, the "For the record" ledger, the 404 joke, the pressable 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. The remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). There is no status or date line, and the dates are now a clear gap. The hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense. About says "2023 – 2025", yet today is 2026-11-19, so the degree ended about a year ago. A recruiter cannot tell whether he has graduated, what he does now, or whether he is available. Likely graduated, but I cannot confirm that. `STATUS` is wired to render a ledger row; the owner must supply the fact. This is the highest-value gap (NN/g hiring-manager guidance as a pointer, unread).
2. Major (UX). The site gives two answers to "strongest project". Row 01 (snake) leads and matches the lede, but its page has only a question, a short "Why snake robots" paragraph and a lab link, with no method, result or personal contribution. START HERE sits on row 06 (aerobraking). The owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari but matches its 0-60 time" has no source on the page. The owner should give a sentence and a source, or cut the claim.
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, footer and 404, and there is no local assets/resume.pdf. If Wix lapses it breaks everywhere. It needs the owner's PDF.
5. Major (performance). Wix images remain on every content page, 1 to 7 per page, with no width/height. That risks CLS and an outage dependency. It needs local files, then dimensions and `fetchpriority="high"` on the first visible image.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host the WOFF2 files with a metric-adjusted fallback once they exist (pointer: aem.live font-fallback, unread).
7. Minor (visual). The Home right column is ragged, and the lone Fig. 1 plate on row 06 looks stray on phone. The caption helps; the root is finding 2.
8. Minor (visual, About tablet). The "Resume (PDF)" link under the intro sits about 3 px right of the text edge and is followed by a large empty gap before "Skills & tools" (about 70 px at 820 wide). It looks unfinished. Align the link and trim the spacing.
9. Minor (SEO). All pages share one OG card, and the robots.txt path is a host limit. Noted, not pressed.
10. Minor (content). The tricycle page voice is passive with no subheads. This is the owner's call.
11. Minor (UX). Contact is LinkedIn only, and the footer states it. This is an owner constraint.
12. Nit (visual, taste). The About right third is empty on wide screens, and the skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files. Eleven design-only cycles have returned nothing. I recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures in check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, the Fig. 1 schematics with honest captions, the struck-through "three weeks".

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. Without those the design cycles will keep returning the same findings. The only designer-fixable item this cycle is the About spacing (finding 8). Research was shallow because search returned only links, so none of this rests on newly read sources.
