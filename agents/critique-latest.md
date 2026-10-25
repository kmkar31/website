# Critique, 2026-10-25 (cycle 17, reviewing commit 696d69e "Cycle 16")

## Sources
WebFetch (web.dev optimize-cls) was refused by the permission layer and I have no search tool, so I read NO source this cycle. Pointers are unverified; no finding depends on them.
- web.dev CLS and images without dimensions: https://web.dev/articles/optimize-cls (blocked)
- WCAG 2.2 SC 3.2.6 / 2.4.4 link purpose: https://www.w3.org/WAI/WCAG22/Understanding/ (unverified)
- NN/g on recruiter scanning of portfolios: https://www.nngroup.com/ (unverified)
Topic this cycle: staleness and credibility, repetition, page weight on phone, derived figures.

Measured: tools/check.py ran 13 pages x 3 viewports x 2 themes, every page OK (Wix images not loaded = sandbox). STATUS in build/build.py is still "". Wix/filesusr hotlinks remain on all pages (2 to 9 each). Every page has one JSON-LD block except 404. Titles are unique. Home phone is about 6150 px tall. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks", stamps, Fig./Sheet plates, 404 game line, "no framework" colophon. Residual: warm-cream, serif, terracotta kit; eight identical rows; name-only hero.
- Looks good: 6/10. Calm and aligned, but no photograph anywhere; project pages are a plate plus prose. On home desktop only row 01 has a plate, so it reads as a featured card.
- SEO: 7/10. Titles, descriptions, canonical, OG, JSON-LD, sitemap, noindex 404 in place. Weak: render-blocking Google Fonts, hotlinked images without dimensions, project pages carry little unique text.
- UX: 6/10. Name, field, resume, LinkedIn are in the first phone screen. Misses: stale dates, no "now" statement, third-party resume URL, featured project has no result.
- Fun/personality: 6/10. Earned touches exist (99 s stamp you can hold, 404) but seven of nine pages have none of their own.

## Owner critique (user-critique.md)
1. Retro, matte: met. No blur, glow or gradient; hard-offset button; ink rules; dark theme is near-black plus amber rather than paper (taste).
2. Not AI-looking: mostly met; remaining risk is the kit and uniform rows (finding 6).

## Findings (ranked)

1. Major (content/UX). The featured project is the thinnest page. Snake robots is "Start here" and the lede's research focus, yet the page (phone, 1 screen of content) is lab, advisor, a schematic zigzag and one generic "Why snake robots" sentence. Home says "controllers I implemented"; the page never says which gaits, what was tested, or what happened. A recruiter who follows our one pointer hits a dead end. Fix: owner supplies 2-3 facts (gaits, terrain/test, result, status). Until then consider moving "Start here" to a page with a result (Aerobraking: 46 orbits). Editorial call; flagged, not dictated.

2. Major (credibility). No "now" statement, dates look stale. About says the Master's "is at Carnegie Mellon University (2023 - 2025)" and Education shows 2023 - 2025; today is 25 Oct 2026. Reader cannot tell graduated, enrolled or open to roles. STATUS slot is empty (open since cycle 1). Owner needs one sentence.

3. Major (robustness). Resume PDF, the main call to action, is a Wix filesusr hotlink in the header, hero, About and every footer. One rotation breaks it on all 13 pages silently. Owner should put resume.pdf in assets/. Not verifiable offline.

4. Major (looks good, 6). No photograph or real result image. Wix figures drop out on failure, so pages read as plate plus prose. A robotics portfolio is expected to show the robot. Needs owner media with real width/height.

5. Major (performance/SEO). Google Fonts stylesheet is render-blocking and third-party with no fallback metrics. Self-host two WOFF2 with font-display: swap and preload. Needs owner files; sandbox cannot fetch.

6. Major (AI-tell: kit). Home desktop: only row 01 has a plate, so it looks like the stock "featured card" over a list. Rows 02-09 are identical in anatomy. Options: plates on every row at tablet/desktop only (local SVG, cannot fail) or drop the plate and let "Start here" and the stamps do the work. Taste.

7. Minor (UX, phone length). Home on phone is about 6150 px: lede, ledger, nine rows, each 4-5 lines. Home duplicates the Projects page. Consider home showing Start here plus the three stamped rows and a link "All nine projects". Judgment call.

8. Minor (credibility). About shows "GPA: 9.3 / 10 (3.9 / 4.0)". The 3.9 is a conversion; the site does not say who computed it or by what scale. If it is not from the owner's transcript or resume, flag as unsupported or remove it. Owner to confirm.

9. Minor (repetition/a11y). "Resume (PDF)" appears four times on desktop (header, hero, About button, footer) and "LinkedIn" three times. Same link text for one destination is fine for SC 2.4.4, but the About button plus header link adds nothing; dropping the About button would quiet the page. Taste.

10. Minor (layout). About desktop: below the intro, the right 28% is empty from Skills to the footer (about 1700 px in the 1366 shot). Reads as a plain CV. Dates in a left margin column would use the width. Taste, large rewrite.

11. Minor (UX). Contact is LinkedIn only (owner constraint; flag only). The footer sentence is the sole contact line.

12. Minor (SEO/CLS). Wix `<img>` tags have no width/height, so late-loading figures shift layout. Cannot measure offline; needs owner files.

13. Minor (SEO). Project pages hold little unique text, so each ranks on its title alone. Owner-supplied outcome sentences would help SEO and findings 1 and 4 at once.

14. Nit (fun). Facts already in the repo that could carry one plain aside per page: Aerobraking 46 orbits, Tricycle 12 km/h, Tethered 500 m. Designer has declined as taste; acceptable unless owner asks.

15. Nit (a11y). Hasselhoff stamp (tabindex, role=button) and the details control were not driven with a real tab-through in this run (screenshots only).

## Good, do not regress
- Struck-through "three weeks" in marker highlight (home, About).
- Fig. N plates with sheet tags and honest "schematic / NTS" captions; repo-local and robust.
- Two stamp types; the holdable 99 s stamp.
- Hasselhoff disclosure bar (boxed +, "Show", native details).
- Honest empty-state handling: failed figures, thumbnails and portrait collapse without orphan captions.
- Plain, specific home lede with the "For the record" ledger; ink-rule hierarchy and dark theme contrast.

## Verdict
The design is now coherent, matte and fairly authored (AI-tell 3), and the designer has run out of safe moves inside the repo. What holds the site back is content only the owner can supply: a status sentence, outcomes for the Start-here project, a local resume.pdf and real photographs. Until those arrive, scores for looks, UX and fun stay at 6. Next cycle the useful design work is limited to the home length and row sameness (findings 6 and 7); everything else is waiting on Karthik.
