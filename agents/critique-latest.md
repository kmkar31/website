# Critique, 2026-11-16 (cycle 145)

Method: `python3 tools/check.py . agents/shots` completed, rc=0, 0 FAIL, only "images not loaded, sandbox network" notes. No site files edited. I viewed index phone-light and desktop-light, quadrotor-sysid phone-light, projects tablet-dark and about tablet-dark. Repo greps: 96 `wixstatic` string occurrences across the HTML (33 distinct images per last cycle's count); `STATUS = ""` still at build/build.py (1 match); JSON-LD present on all 12 pages; `<meta name="color-scheme" content="light dark">`, `color-scheme` in CSS, and light/dark `theme-color` present; `:focus-visible` is a 3px solid outline with 3px offset; a `prefers-reduced-motion` block exists (assets/style.css:247); robots.txt allows all and names the sitemap.

## Sources consulted
Limit of this cycle: WebFetch was blocked (permission not answered) for web.dev/articles/prefers-color-scheme, developers.google.com profile-page docs and the w3.org focus-appearance page. I could only run searches, so the links below are search-result pointers whose bodies I did not read. No finding depends on their text; findings rest on repo evidence and screenshots.
- https://web.dev/articles/color-scheme (dark mode default with `color-scheme` CSS and meta; checked in repo, present and correct)
- https://w3c.github.io/wcag/understanding/focus-appearance-enhanced (WCAG 2.2 SC 2.4.13, AAA; the existing 3px outline is consistent with its intent, not verified against its numbers)
- https://developer.chrome.com/docs/modern-web-guidance/guides/visual-design/dark-mode (dark-mode guidance, pointer only)
- Searching NN/g for contact-information findability returned no primary NN/g page. I cite nothing from it.
Topic this cycle: dark mode and focus visibility (new versus earlier CLS, portfolio and target-size cycles). Both already pass on the evidence I can see.

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, floating chips, stats strip or card trio. Plain first-person lede, strike-through "three weeks", stamps that carry real numbers. Residual tells: the identical project-page skeleton and the "Seagate, York University, Tube Investments" ledger triplet. No tell moved since last cycle.
- Looks good: 8/10, unchanged. Index desktop-light has clear hierarchy (large serif name, mono role line, ruled ledger, numbered rows, one red button with the only hard shadow). About tablet-dark is calm and legible. Held back by uneven Home rows (only 06 has a plate; 01, 02, 03, 08, 09 have neither plate nor stamp) and by wide empty right-hand space on desktop About.
- SEO: 7/10, unchanged. Unique titles, canonical, OG, JSON-LD on every page, sitemap, robots. Held down by Wix hotlinks without verified dimensions, one shared OG card, and sitemap/robots living under the /website/ subpath (host limit; crawlers only honour robots.txt at the host root).
- UX: 6/10, unchanged. 30-second phone test passes for name, subject, advisor, Resume and LinkedIn. It fails for status and availability, and "strongest project" still has two answers.
- Fun and personality: 7/10, unchanged. Stamps, struck text, "Time allowed: 99 s", 404 joke. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper and umber palette, double rules, hard shadow on the primary button only, no blur. Dark theme is amber on umber and stays matte (about tablet-dark).
2. Must not look AI-generated: met. Only caveat is taste: the repeated page skeleton.

## Ranked findings
1. Major (UX, credibility). No status or dates on Home. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no years; About (tablet-dark) says 2023 - 2025; today is 2026-11-16. A recruiter cannot tell graduate, employed or available. Build `STATUS` is empty and the template supports a Status row. Owner fact needed.
2. Major (credibility). Tense mismatch with 1: Home lede is present tense ("I research compliant control of snake robots") but the CMU range on About is closed. Resolves with 1.
3. Major (UX). Two answers to "strongest project". Row 01 (snake) leads Home and has the thinnest page; the only START HERE mark is on row 06 (aerobraking). Owner picks one; snake needs owner method and result.
4. Major (credibility). Aerobraking page: what Karthik contributed versus the cited prior work (Falcone et al.) is not stated; the Raftar "Ferrari" claim still needs a source or a cut. Owner facts.
5. Major (SEO, performance, robustness). Wix hotlinks remain (96 string occurrences). No local copies, no verified width/height. A Wix outage or URL change blanks the project pages. Needs owner files; the designer should not guess dimensions.
6. Minor (content). Tricycle page body is passive voice with no subheads, while other pages have Problem/Setup/Method/Result. Owner call on first person.
7. Minor (UX, visual). Uneven Home rows (index desktop-light): rows 02, 03, 08, 09 have no figure or stamp, so the right column looks half-finished for them. Do not invent numbers; owner facts would fix it.
8. Minor (UX). About body has no inline Resume link. The header and footer carry it, so a reader who reaches the Experience section at the bottom of the page on a phone must scroll to the footer. A one-line "Resume (PDF)" link under the intro is purely structural and invents nothing. Designer-fixable.
9. Minor (visual). About tablet-dark: "podium finish" is an outlined, boxed inline highlight that looks like a button or tag but is not interactive (no link). Reads as a control to a scanner. Either make it a link to the Raftar page or drop the box. Designer-fixable, taste plus affordance.
10. Minor (SEO). One shared OG card; per-page cards need real imagery. Sitemap and robots under /website/ are host-limited.
11. Nit (UX). Contact is LinkedIn only by owner constraint; footer says so plainly. Fine.
12. Nit (taste). About desktop leaves the right third empty; Skills columns uneven (5/3/3). Previously declined as calm measure; I leave it.
13. Nit (process). Many consecutive cycles of the same owner-fact blockers (1 to 5). The designer has correctly declined to invent. The owner needs to supply: status line, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files.

## Good, must not regress
- Retro matte system: paper tones, double rules, hard shadow only on the primary button, no blur or gradients, inverted-print dark theme.
- Stamps with real numbers (46 orbits, 99 s, 500 m, Formula Bharat podium) and the amber strike-through "three weeks" to "15 minutes".
- "Sheet n of 9 . NTS" plates and the tethered pull-out.
- Plain first-person lede; Previous/Next pager carrying the neighbouring project's key figure; sysid phone-light reads as a clean sheet (question, unknowns, tests, plate).
- 404 joke; per-page titles, canonical, OG, JSON-LD, `color-scheme` meta and theme-color pair; no-JS-safe static pages; zero FAIL in check.py.

## Overall verdict
The site looks authored, not generated, and the visual work is close to finished. What still holds the scores down is missing owner information: status, best project, what he personally contributed on aerobraking and snake, and local copies of the Wix media. Two small structural items (8 and 9) are the only things the designer can fix without inventing content. Until the owner answers findings 1 to 5, UX stays at 6 and SEO at 7, and more polish cycles will not move them. Research this cycle was limited to search pointers because page fetches were blocked.
