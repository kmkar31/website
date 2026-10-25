# Critique, 2026-10-25 (cycle 18, reviewing main after cycle 17)

## Sources
WebSearch returned result lists only (titles and URLs); WebFetch was not used, so I did not read page bodies. Pointers, not verified quotes; no finding depends on them.
- web.dev, font best practices (self-host, font-display, preload): https://web.dev/articles/font-best-practices
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), summaries: https://tabnav.com/academy/wcag/success-criterion-2.5.8 (primary: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- NN/g on how hiring managers read portfolios (search listing only): https://www.nngroup.com/articles/author/rachel-krause/?page=5
Topic this cycle: staleness and credibility, home length on phone, row sameness, font loading.

Measured: tools/check.py ran 13 pages x 3 viewports x 2 themes, all OK (Wix images not loaded = sandbox limit). STATUS in build/build.py is still "". Wix/filesusr hotlinks remain on every page (2 to 9 each, 404 included); the resume is a filesusr URL in header, hero and footer. Home phone is 6148 px tall. Live site not checked. Screenshots viewed: home desktop and phone (light), snake-robots phone (light), About desktop (dark).

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks" in a marker, stamps, Fig./Sheet plates, 404 game line, "no framework" colophon, plain lede. Residual: warm-cream, serif, terracotta kit; eight rows of identical anatomy; name-only hero. No gradients, blur, glow, badges or "I build X that Y" slogans found. Nothing moved this cycle (cycle 17 removed a GPA conversion and a duplicate button).
- Looks good: 6/10. Calm, aligned, readable, good ink-rule hierarchy. But no photograph anywhere, and the only image is a six-dot zigzag; the front page is text in a nice frame.
- SEO: 7/10. Unique titles and descriptions, canonical, OG with local image, JSON-LD, sitemap, noindex 404. Weak: render-blocking third-party font CSS, hotlinked images without width/height, thin project text.
- UX: 6/10. Name, field, resume and LinkedIn are in the first phone screen. Misses: no "now" statement, dates stale, third-party resume URL, featured project has no result.
- Fun/personality: 6/10. Earned touches (holdable 99 s stamp, 404, struck-through weeks) but seven of nine project pages have none of their own.

## Owner critique (user-critique.md)
1. Retro, matte: met. Flat paper tones, ink rules, hard offset button, no blur or gradient. Dark theme is near-black plus amber, not inverted paper (taste; it reads fine and contrast is good).
2. Not AI-looking: mostly met. Remaining risk is the "warm editorial kit" plus uniform rows (finding 5). Taste, not a defect.

## Findings (ranked)

1. Major (content/UX). The "Start here" project is the thinnest page. Snake robots is the lede's research focus and the home's featured row, yet its page (phone, about 3300 px, mostly whitespace and a plate) has lab, advisor, a schematic zigzag and one generic sentence "Why snake robots". Home says "controllers I implemented"; the page never says which gaits, what terrain, what result. A recruiter who follows the one pointer hits a dead end, and the "Module count is illustrative" caption underlines that the figure carries no real data. Fix: owner supplies 2-3 facts (gaits, test, result). Until then, consider moving "Start here" to Aerobraking (46 orbits is a real result). Editorial call, flagged not dictated. Principle: hiring readers scan for evidence of outcomes (NN/g portfolio guidance, unverified pointer above).

2. Major (credibility). No "now" statement and dates are stale. Today is 25 Oct 2026; About says the Master's "is at Carnegie Mellon University (2023 - 2025)" and Education reads 2023 - 2025. Reader cannot tell graduated, enrolled or open to roles. STATUS slot has been empty since cycle 1. Owner needs one sentence. Highest-value change available.

3. Major (robustness). The resume PDF, the main call to action, is a Wix filesusr hotlink in the header, hero and footer on all 13 pages. One Wix rotation breaks it everywhere silently. Owner should put resume.pdf in assets/. Not verifiable offline.

4. Major (looks good, 6). No photograph or real result image; Wix figures drop out on failure so pages read as plate plus prose, and a robotics portfolio is expected to show the robot. Needs owner media with true width/height.

5. Major (AI-tell: kit / looks good). Home desktop and phone: only row 01 has a plate (a small boxed zigzag), rows 02-09 are the same title/blurb/tag anatomy. It reads as a featured card over a list, and the zigzag at 175 px is too small to read as a snake. Options: drop the plate and let "Start here" plus stamps work, or render the plate larger. Taste.

6. Major (performance/SEO). Google Fonts stylesheet is render-blocking and third-party; no fallback metric overrides. Self-host the two WOFF2 files with font-display: swap and a preload (web.dev pointer above). Needs files the sandbox cannot fetch; owner can drop them in assets/.

7. Minor (UX, phone length). Home on phone is about 6150 px: lede, ledger, nine rows of 4-5 lines. Home duplicates the Projects page. Consider home showing Start here plus the three stamped rows and "All nine projects". Judgment call; designer has documented "home is the full index by design".

8. Minor (UX). Phone header drops Resume and LinkedIn/GitHub (only Home, About, Projects, theme). Resume is reachable from the hero and footer, so the 30-second test passes, but on a project page the phone user must scroll to the footer to reach it. Taste versus 44 px layout; a footer-only route is acceptable.

9. Minor (layout). About desktop (1366): below the intro the right 28% is empty from Skills to the footer, about 1700 px, apart from the "On this page" index that only appears when the portrait fails to load. With the portrait working the layout differs from what I reviewed; with it broken (current Wix state) the column is mostly void. Dates in a margin column would use the width. Taste, large rewrite.

10. Minor (SEO/CLS). Hotlinked `<img>` tags have no width/height, so late-loading figures shift layout. Cannot measure offline; needs owner files.

11. Minor (SEO). Project pages hold little unique text; Snake in particular has about 40 words of body copy, so each page ranks on its title alone. Owner outcome sentences help findings 1, 4 and 11 at once.

12. Minor (a11y). Row stamps sit inside the link name after the title, so a screen reader announces "Hasselhoff Submarine ... Time allowed: 99 s ..." as the link text. Acceptable under SC 2.4.4 but long; tags could sit outside the anchor. Nit-level on a nine-row list.

13. Minor (contact). Contact is LinkedIn only (owner constraint). The footer sentence is the sole contact line and the hero has no email. Flag only.

14. Nit (fun). Facts already in the repo that could carry one plain aside per page: Aerobraking 46 orbits, Tricycle 12 km/h, Tethered 500 m. Declined as taste in earlier cycles; acceptable unless the owner asks.

15. Nit (a11y). The Hasselhoff stamp (tabindex, role=button) and details control were not driven with a real keyboard tab-through in this run; screenshots only.

## Good, do not regress
- Struck-through "three weeks" in an amber marker (home, About).
- Fig. N plates with sheet tags and honest "schematic / NTS" captions; repo-local and robust.
- Two stamp types and the holdable 99 s stamp.
- Hasselhoff disclosure bar (boxed +, "Show", native details).
- Honest empty-state handling: failed figures, thumbnails and portrait collapse without orphan captions.
- Plain, specific home lede with the "For the record" ledger; ink-rule hierarchy; dark theme contrast; solid ink footer.
- No-framework, no-gradient, hard-shadow restraint across both themes.

## Verdict
The design is coherent, matte and fairly authored (AI-tell 3), and the designer has run out of safe moves inside the repo; cycle 17's trims were correct and caused no regression. What holds the site at 6 on looks, UX and fun is content only the owner can supply: one status sentence, two or three outcome facts for the Start-here project (or a different Start-here), a local resume.pdf, real photographs, and two WOFF2 files. Without those, the only remaining design work is the home's length and row sameness (findings 5 and 7), which are judgment calls rather than defects.
