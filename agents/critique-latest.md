# Critique, 2026-11-15 (cycle 144)

Method: `python3 tools/check.py . agents/shots` completed, 0 FAIL, only "images not loaded, sandbox network" notes. No site files edited. HEAD 767116b, working tree clean. I viewed index-phone-dark, assistive-tricycle-phone-light and aerobraking-drl-tablet-light (new pages versus last cycle). Grep: 33 wixstatic references over 11 pages; `STATUS = ""` still at build/build.py:266.

## Sources consulted
Search results only; page bodies were not opened, so I cite them as pointers and no finding depends on their text.
- https://web.dev/articles/optimize-cls (explicit width/height on images to avoid layout shift)
- https://nngroup.com/articles/ux-design-portfolios/ (what hiring managers scan for in portfolios)
- https://w3c.github.io/wcag/understanding/pointer-target-spacing (WCAG 2.2 SC 2.5.8 target size)
Topics repeat earlier cycles (CLS, portfolios, target size). Fetching the primary pages was not done this cycle.

## Scores
- AI-tell: 2/10, unchanged. Strike-through "three weeks", stamps carrying real numbers, "Sheet n of 9 . NTS" plates, plain first-person lede, no gradient, blur or glow. Residual: identical project-page skeleton (tl;dr, question, fact list, plate) and the ledger triplets ("Seagate, York University, Tube Investments"). No tell moved.
- Looks good: 8/10, unchanged. Home phone-dark is a clear column: name, role, lede, amber button, ruled ledger, numbered rows. Aerobraking tablet-light reads like a printed sheet. Weak: Home rows are visually uneven (row 06 carries a plate and START HERE, others carry nothing or a stamp), and the tricycle body is a long uniform prose block.
- SEO: 7/10, unchanged. Unique titles, canonical, OG with absolute image, twitter card, sitemap, robots. Held down by 33 hotlinked Wix images with unverified dimensions, one shared OG card, sitemap and robots under the /website/ subpath (host limit).
- UX: 6/10, unchanged. 30 s phone test passes for name, subject, advisor, Resume, LinkedIn. Fails for availability and graduation status; "strongest project" has two answers.
- Fun and personality: 7/10, unchanged. Stamps, struck text, 99 s stamp, 404 joke. Nothing new this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper and umber palette, double rules, hard offset shadow on the button only, no blur. Dark theme is amber on umber and stays matte.
2. Must not look AI-generated: met. The one caveat is taste: the repeated page skeleton.

## Ranked findings
1. Major (UX, credibility). No status or dates on Home. Home phone-dark says "MS Mechanical Engineering, Carnegie Mellon University" with no years; About says 2023-2025; today is 2026-11-15. A recruiter cannot tell student, graduate or available. `STATUS = ""` (build/build.py:266) and the template already supports a Status row. Owner fact needed (e.g. graduation month, availability).
2. Major (credibility). Tense mismatch with 1: Home lede is present tense ("I research compliant control of snake robots") while the About range is closed. Resolves once 1 is answered.
3. Major (UX). Two answers to "strongest project". Row 01 (snake) leads Home and its page is the thinnest (no method, result or duration); the only START HERE mark is on row 06 (aerobraking). Owner picks one; snake needs 2-3 sentences of owner method and result.
4. Major (credibility). Aerobraking page (tablet-light): "Setup" says the project "builds off work done by Falcone et al." and "Method" describes what Falcone et al. did, then switches to "Our method". The reader cannot tell what Karthik contributed (the surrogate network? the PPO policy? the 46-orbit result?). One owner sentence on contribution fixes it. Also the Raftar "Ferrari" claim still needs a source or a cut (per LOG).
5. Major (SEO/performance). 33 hotlinked Wix images (aerobraking 7, sysid 5, tricycle/submarine/tethered 4 each), no local copies, no verified width/height. web.dev's CLS guidance recommends explicit dimensions; a Wix outage or URL change blanks the project pages. Needs owner files; designer should not guess dimensions.
6. Minor (content, voice). Tricycle page (phone-light): after the plate and numbered criteria, five paragraphs in passive voice ("it was determined", "was devised", "was ensured"). It is the only page where the owner's role is invisible in the grammar, which also hurts scanning (no subheads, unlike aerobraking's Problem/Setup/Method/Result). Same skeleton as other pages would help; rewording into first person is an owner decision. Taste plus scanning.
7. Minor (UX). Home rows are uneven: only 06 carries a figure, 04/05/07 carry stamps, 01/02/03/08/09 carry none (index phone-dark). The unevenness is partly authored (stamps carry facts) but reads as unfinished for 02, 03, 08, 09. Owner facts (a number per row) would even it; do not invent.
8. Minor (UX). Contact is LinkedIn only, by owner constraint; footer says so plainly. Fine.
9. Minor (SEO). One shared OG card; sitemap lastmod follows git; per-page cards need real imagery. Host-limited.
10. Nit (taste). About desktop leaves the right third empty and Skills columns are uneven (5/3/3). Previously declined as intended calm measure; I leave it.
11. Nit (process). Nine consecutive cycles of the same owner-fact blockers (findings 1-5). The designer has correctly declined to invent; the owner needs to supply: status line, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files.

## Good, must not regress
- Retro matte system: paper tones, double rules, hard shadow only on the primary button, no blur or gradients, inverted-print dark theme.
- Stamps with real numbers (46 orbits, 99 s, 500 m, Formula Bharat podium) and the amber strike-through "three weeks" to "15 minutes".
- "Sheet n of 9 . NTS" plates and the tethered pull-out about shrapnel.
- Plain first-person lede with specific facts; Previous/Next pager with the key number of the neighbouring project.
- 404 joke; per-page titles, canonical and OG; no-JS-safe static pages; zero FAIL in check.py.

## Overall verdict
The site looks authored, not generated, and the design work is close to finished: the remaining weaknesses are not visual. A recruiter still cannot learn status, which project is best, or what Karthik personally contributed on the aerobraking and snake pages, and the project media still depend on Wix. All five Major items are owner-supplied facts or files; the designer cannot close them without inventing content. Until the owner answers, UX stays at 6 and SEO at 7, and further polish cycles will not move the scores.
