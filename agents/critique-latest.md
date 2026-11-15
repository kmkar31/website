# Critique, 2026-11-15 (cycle 143)

Method: `python3 tools/check.py . agents/shots` ran to completion (in background; the foreground call times out at 2 min): 0 FAIL, only "images not loaded, sandbox network" notes. No site files edited. HEAD a4f42fe. I opened 5 of 78 screenshots: index phone-light, index desktop-light, projects phone-dark, argus-mission tablet-light, about desktop-light. The other 73 were not opened. I read source for og tags, wixstatic counts, STATUS, focus and reduced-motion CSS.

## Sources consulted
Not verified this cycle. All three WebFetch calls were blocked (permission request unanswered, PROVENANCE_REQUIRED) and I did not retry:
- https://web.dev/articles/prefers-reduced-motion
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
- https://www.nngroup.com/articles/dark-mode/
These were the new topics chosen (reduced motion, focus appearance, dark mode) to break the three-cycle run on portfolio content, CLS and target size. No finding below depends on them; they are source-code checks and screenshot observations. Prior-cycle citations (web.dev CLS, WCAG 2.5.8, NN/g portfolios) still stand as recorded in LOG.md.

## Scores
- AI-tell: 2/10, unchanged. Amber strike-through "three weeks", stamps with real numbers, graph-paper "Sheet n of 9 . NTS" plates, plain first-person lede, no gradient/blur/glow. Residual: identical project-page skeleton; triplets in the ledger. Nothing moved.
- Looks good: 8/10, unchanged. Home desktop-light has a clear order (name, role, lede, hard-shadow button, ruled ledger, numbered rows). ARGUS tablet-light is well composed. Weak: about desktop-light leaves the right third empty below the "On this page" box; the Skills grid is uneven (5/3/3).
- SEO: 7/10, unchanged. Unique titles, canonical, OG 1200x630 with alt, twitter card, absolute og:image, sitemap, robots. Held down by 33 wixstatic references over 11 pages (aerobraking 7, quadrotor-sysid 5), one shared OG card, no verified width/height on Wix images, no matched fallback for swapped fonts. LCP/CLS not verifiable offline.
- UX: 6/10, unchanged. 30 s phone test passes for name, subject, advisor, Resume, LinkedIn. Fails for status/availability; flagship page thin.
- Fun and personality: 7/10, unchanged. Stamps, struck text, 99 s stamp, 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all five screenshots (paper tone, double rules, hard offset shadow, amber-on-umber dark, no blur).
2. Must not look AI-generated: met; taste-only caveat is the repeated project-page skeleton.

## Ranked findings
1. Major (UX/credibility). No status or dates on Home. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no years; About says 2023-2025; today is 2026-11-15. `STATUS = ""` at build/build.py:266 (the template already supports a Status row). Recruiter cannot tell student, graduate or available. Owner supplies one line.
2. Major (credibility). Tense mismatch with 1: Home present tense ("I research compliant control of snake robots"), About's range is closed. Follows from 1.
3. Major (UX). Row 01 (snake robots) is the lead on Home and the page behind it is the thinnest (no method, result, duration). The only "START HERE" mark is on row 06 (aerobraking), so two answers to "strongest project". Owner picks one and supplies 2-3 sentences for snake.
4. Major (credibility). Aerobraking page: contribution versus the cited prior work is unstated; "Raftar Ferrari claim" needs a source or a cut (per LOG, still open). Owner facts.
5. Major (SEO/perf). 33 hotlinked Wix images, no local copies, width/height unverified. web.dev CLS guidance (prior cycle) says set dimensions. Needs owner files.
6. Minor (UX). Contact is LinkedIn only by owner constraint. Fine; note the footer says so plainly.
7. Minor (SEO). One shared OG card for all pages; sitemap/robots under /website/ subpath (host limitation); sitemap lastmod follows git.
8. Minor (UX). Rows 02, 03, 08, 09 on Home have no stamp or number, so the list reads unevenly (rows 04-07 carry stamps). Owner facts needed for honest stamps.
9. Minor (design, taste). About desktop: empty right third; uneven Skills columns (5/3/3).
10. Nit (a11y). Focus ring is 3px solid with offset (style.css:37); reduced-motion rule removes transitions only (style.css:247). Both look adequate; I could not confirm against the blocked sources.

## Good, must not regress
- Retro matte system: paper tone, double rules, hard shadows, amber dark mode.
- Real-number stamps and the struck "three weeks" detail.
- Project pager with outcome line (ARGUS tablet), "All projects" back link, graph-paper plates with captions.
- Honest footer ("Hand-built static pages, one stylesheet, no framework"), no-JS handling of filter chips.
- 44 px tap targets, working skip link and focus-visible style.

## Verdict
The design is committed, un-generic and clean; the remaining weakness is content the designer cannot invent: status, snake result, aerobraking contribution, the Ferrari source, local images. This cycle's research was blocked, so variety is still unmet and the findings are observational. Until the owner supplies those facts, further designer cycles will mostly produce churn.
