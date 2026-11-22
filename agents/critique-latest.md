# Critique, 2026-11-22 (HEAD d282ab4; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran in the background and finished: 78 lines, zero FAIL, only "images not loaded, likely sandbox network" notes. I viewed index desktop-light, snake-robots phone-dark and raftar desktop-light in full. Last site-file commit is cycle 163 (e7e4f75); every cycle since touched only LOG.md and critiques, so no regression is possible. Wix and Google Fonts are unreachable in the sandbox (environment limit); the fallback serif and missing figures are not design bugs. Wix hotlinks counted by grep: filesusr (resume) on all 11 content pages plus 404, wixstatic images on 9 pages (about 83 references).

## Sources consulted
- WebFetch of https://web.dev/articles/optimize-cls, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and https://www.nngroup.com/articles/ux-hiring-insights/ : all three blocked (permission request unanswered). Not read.
- WebSearch "web.dev optimize cumulative layout shift image width height font-display" returned only a listing (web.dev/articles/optimize-cls, web.dev/articles/css-web-vitals). Titles only; no page content read.
- Honest summary: zero external pages read this cycle (third cycle running). Claims about CLS, target size and hiring-manager scanning below come from general knowledge and are unverified; the repo facts are verified. Tooling limit, not a design judgement.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Specific copy (struck-through "three weeks", 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Seen: serif name, mono credential line, ruled index, hard-offset button, flat dark footer, authored Fig. 1 plates. Weak: stamps on rows 04 to 07 only, so the desktop right column is ragged; a lone plate on row 06; the snake page (phone dark) is short and ends in a large empty gap before the pager; the Raftar plate (desktop) is a schematic car that reads a little crude next to the type.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute og:image. Weak: one shared OG card; robots.txt under a subpath is ignored by crawlers (host limit); most content depends on Wix hotlinks.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through marker, stamps, "For the record" ledger, 404 joke, 99 s press-and-hold stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer; confirmed in screenshots).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. Hero reads "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025; today is 2026-11-22. Nothing says what he does now or whether he is available. `STATUS = ""` (build/build.py:266) so the ledger row never renders. Needs an owner fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero, but its page (seen, phone dark) is a stub: one-line summary, question, lab, advisor, one schematic, one generic paragraph, no method, result or personal contribution. "START HERE" sits on row 06 (aerobraking, seen) with no stated reason. Owner: pick the lead and supply snake method and result, or move the label.
3. Major (credibility). Raftar's question (seen on the page) sets the car against a Ferrari ("one-fifth the weight ... matches its 0-60") with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: source or cut, plus one sentence of contribution each.
4. Major (robustness). The Resume PDF is a filesusr hotlink in header, hero, About, footer and 404; it is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance, unverified offline). Wix images on 9 content pages likely lack width and height (CLS risk, outage dependency). Needs local files first.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06 (root cause is finding 2).
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit the sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only (footer says so). Owner constraint.
11. Nit (visual, taste). About right third empty on wide screens.
12. Nit (process). Findings 1 to 5 need owner facts or files. Cycles 169 to 180 produced no site change and this list repeats until the owner supplies input or the loop pauses. My own source fetches are blocked, so the research requirement is unmet.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero check.py failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, one h1 per page, honest Fig. 1 captions ("Module count is illustrative"), the struck-through "three weeks".
- About page: dated, scannable education and experience.

## Overall verdict
The site is coherent, specific and convincingly hand-made, AI-tell 2. Its weakness is missing owner-supplied content: a current status, a clear lead project with method and result, a sourced Raftar claim, a local resume and local images. Design work has hit its ceiling and UX stays at 6. The highest-value next step is owner input, not another design pass. This critique is again unresearched (source fetches blocked), so treat external claims as unverified.
