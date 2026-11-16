# Critique, 2026-11-16 (cycle 146)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc=0, no FAIL, only "images not loaded, sandbox network" notes). I looked at index phone-light and desktop-dark, about phone-dark, snake-robots tablet-light and projects phone-dark. Repo greps: wixstatic occurrences per page (about 1, aerobraking 7, tricycle 4, submarine 4, sysid 5, tethered 4, landing 2, others 1; index has none); `STATUS = ""` still at build/build.py:266; og:image is one shared absolute URL (assets/og.png); no mailto anywhere; `.btn:active`, `.row:active`, `.filter:active` press states exist; a reduced-motion block disables transitions (assets/style.css:247). No site files edited.

## Sources consulted
- https://web.dev/articles/optimize-cls (read): always put width and height on images, or reserve space with CSS aspect-ratio; mismatched attributes still shift a little, but less than none. Applies to every Wix img in the project pages (e.g. snake-robots.html line 55 has no width or height).
- https://nngroup.com/articles/ux-design-portfolios/ (read; it is about UX portfolios, so applied by analogy to an engineering one): show 3 to 5 strong projects rather than many, state your own role, show process and whether it worked, keep it scannable because reviewers give little time.
- https://developers.google.com/search/docs/appearance/structured-data/profile-page (search result pointer only, body not read; no finding depends on it).
Topic this cycle: image dimensions and layout shift, and portfolio case-study content. Both are new compared with the dark-mode and focus topics of last cycle.

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, chips, stats strip or card trio. The page reads as authored: plain first-person lede, struck-through "three weeks", stamps that carry real numbers, "Time allowed: 99 s". Residual tells: every project page uses the same skeleton (back link, tag, big title, standfirst, "The question", two-cell meta, figure, sections, next link), and the ledger line "Seagate, York University, Tube Investments". Nothing moved since last cycle.
- Looks good: 8/10, unchanged. Index desktop-dark has a clear hierarchy: large serif name, mono role line, ruled ledger aside, numbered rows, one amber button. Held back by uneven Home rows (02, 03, 08, 09 have no plate or stamp, so the right column goes ragged) and by large bare areas on the snake page (below).
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, OG and JSON-LD per page, sitemap, robots. Held down by Wix hotlinks without dimensions, one shared OG card for all 12 pages, and sitemap/robots under the /website/ subpath (crawlers only read robots.txt at the host root; a host limit).
- UX: 6/10, unchanged. In 30 seconds on a phone I can find name, school, advisor, Resume and LinkedIn (index phone-light). I cannot tell whether he is graduated, employed or available, and "strongest project" has two answers. Below 7, so Major.
- Fun and personality: 7/10, unchanged. Stamps, strike-through, 99 s submarine, 404 joke, press-down states on rows and buttons. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper and umber palette, double rules, hard offset shadow on the primary button only, no blur. Dark theme (amber on umber) stays matte and flat in index desktop-dark.
2. Must not look AI-generated: met. Only caveat, labelled taste: the repeated page skeleton.

## Ranked findings
1. Major (UX, credibility). No status or dates on Home. Phone-light shows "MS Mechanical Engineering, Carnegie Mellon University" with no years, while About says 2023 to 2025 and today is 2026-11-16. A recruiter cannot tell whether he is a student, graduate or available. `STATUS` is empty although the template already supports a Status row. Needs an owner fact.
2. Major (credibility). Tense mismatch tied to 1: the lede says "I research compliant control of snake robots" (present) but the CMU range on About is closed. Resolves with 1.
3. Major (UX, content). Two answers to "strongest project". Row 01 (snake) leads Home yet has the thinnest page; the only START HERE mark is on row 06 (aerobraking). The snake tablet-light page is a schematic figure, one paragraph ("Why snake robots") and a lab link, with no method or result. NN/g (above) says reviewers want your role and whether it worked. Owner picks the lead and supplies the snake method and result.
4. Major (credibility). Aerobraking: what Karthik contributed versus cited prior work (Falcone et al.) is not stated. Raftar page line 48 still claims "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" with no source. Owner source, or cut.
5. Major (SEO, performance, robustness). Roughly 30 Wix hotlinks remain with no width/height. web.dev (above) says unsized images cause layout shift; a Wix outage or URL change blanks the project pages. The designer can reduce CLS without guessing by adding `aspect-ratio` containers per figure row once the owner supplies files or sizes. Until then this stays open.
6. Minor (content). Nine projects on Home. NN/g suggests 3 to 5 strong ones. Taste, but the lack of any tiering is why finding 3 exists. Owner decides.
7. Minor (content). Tricycle page is passive voice with no subheads, unlike pages with Problem, Setup, Method, Result. Owner call on first person.
8. Minor (visual). Uneven Home rows (see Looks good). Stamps only where a real number exists is the right rule; accept the ragged column or find real figures.
9. Minor (SEO). One shared OG card for all pages. Per-page cards need real imagery.
10. Minor (UX). Contact is LinkedIn only; footer says so. Owner constraint, noted not pressed.
11. Nit (visual, taste). About desktop leaves the right third empty and skills are 5/3/3. Calm measure is defensible.
12. Nit (process). Cycles 139 to 145 declined the same owner-fact items. The site is near its ceiling without owner input.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadow on one button, no blur or gradient, flat dark theme.
- Specific copy: "three weeks" struck to "15 minutes", "Time allowed: 99 s", "46 orbits to target", "500 m of tether", the plain "For the record" ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, 44px targets, readable measure.
- Projects filter buttons and numbered rows with press states; the 404 joke; per-page JSON-LD, canonical and OG; reduced-motion block; focus ring.
- Figure plates (orbit and snake schematics) labelled "Fig. 1" and "Sheet 1 of 9" are drawn, not stock.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, fun 7. It is held to a 6 on UX by facts only the owner can supply: a status line, a lead project with a real snake method and result, the aerobraking contribution and a source for the Ferrari claim. The one designer-side risk left is unsized Wix images; once the owner provides files or dimensions, add width/height or aspect-ratio and self-host them. Until the owner answers findings 1 to 5, further cycles will mostly repeat.
