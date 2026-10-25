# Critique, 2026-10-25 (cycle 19, reviewing main at 706de87)

## Sources
WebFetch of all three pages below was blocked by the permission layer (not answered in time), so none was read this cycle. They are pointers for the designer, not verified quotes; no finding depends on them.
- WCAG 2.2 SC 2.4.11 Focus Not Obscured / 2.4.13 Focus Appearance: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked)
- web.dev, Optimize CLS (image width/height): https://web.dev/articles/optimize-cls (blocked)
- NN/g, how people read long web text (headings, scanning): https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ (blocked)
Topic this cycle: long project pages without structure, heading order, pager logic, CLS from hotlinked figures. Findings 4, 7, 9 and 11 are measured from the repo, not from sources.

Measured: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK (Wix images not loading is a sandbox limit). Screenshots viewed: home desktop light, home phone dark, aerobraking phone light, snake-robots desktop light. Others not re-viewed. Live site not checked. STATUS in build/build.py is still "" (line 253). Wix hotlinks per page: 2 to 9 (aerobraking 9, quadrotor-sysid 7, assistive-tricycle, hasselhoff, tethered 6 each). Resume is still a filesusr URL.

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks" in marker, stamps, Fig./Sheet plates, 404 line, "no framework" colophon, plain lede. Residual: cream + serif + terracotta "editorial" kit; rows 02-09 identical in anatomy. No gradients, blur, glow, badges, sparkle or slogan copy. Nothing moved this cycle (cycle 18 was a non-visual aria change).
- Looks good: 6/10. Calm, aligned, clean ink rules. But the only picture on the home page and on Snake is a six-dot zigzag, and the Snake page at desktop is about half empty paper around one plate. No photograph exists anywhere that renders.
- SEO: 7/10. Unique titles/descriptions, canonical, OG with local 1200x630 image, JSON-LD on every page, sitemap, robots.txt, noindex 404. Weak: render-blocking Google Fonts CSS, hotlinked figures without width/height, thin or unstructured project text, heading skips.
- UX: 6/10. Name, field, resume and LinkedIn are in the first phone screen. Misses: no "now" statement, stale dates, third-party resume URL, featured project has no result.
- Fun: 6/10. Earned touches (holdable 99 s stamp, struck-through weeks, 404, colophon) but seven of nine project pages have none.

## Owner critique (user-critique.md)
1. Retro, matte: met. Flat paper tones, ink borders, hard offset button and stamps, no blur or gradient. Dark theme is near-black plus amber rather than inverted paper; taste, contrast fine.
2. Not AI-looking: mostly met. The remaining risk is the warm-editorial kit and uniform rows (finding 6), which is taste, not a defect.

## Findings (ranked)

1. Major (content/UX). "Start here" points at the thinnest page. Snake robots is the home's featured row and lede focus, yet its page (viewed desktop) has Lab, Advisor, a schematic zigzag whose caption admits "Module count is illustrative", and one two-line paragraph "Why snake robots" that is generic background. Home says "controllers I implemented"; the page never says which gaits, what terrain or result. A recruiter who follows the one pointer reaches a dead end. Owner supplies 2 or 3 facts (gaits, test, result). Until then consider making Aerobraking the "Start here" row (46 orbits is a real result). Editorial call, flagged not dictated.

2. Major (credibility). No "now" statement and dates are stale. Today is 25 Oct 2026; About says the Master's is "at Carnegie Mellon University (2023 - 2025)" and the home subhead is present tense. A reader cannot tell graduated, enrolled or open to roles. The STATUS slot has been empty since cycle 1. One owner sentence is the highest-value change available.

3. Major (robustness). The resume PDF, the main call to action, is a Wix filesusr hotlink in the header, hero and footer on every page. One Wix change breaks it everywhere silently. Owner should add resume.pdf to assets/. Not verifiable offline.

4. Major (UX/SEO, new). Aerobraking page (phone, light) is about 11 unbroken paragraphs under the h1 with no h2 at all (grep: only the h1). It is the site's best result ("46 orbits") and it is buried in the last paragraph. With the Wix figures down it is a wall of text roughly 2 screens deep. Fix with existing text only: add 3 to 4 plain h2s (Problem, Method, Setup, Result) and move the result sentence next to the stats at the top, which already show Training 1.1M steps and Target 46 orbits. Scanning principle: NN/g on headings in long text (pointer, unread).

5. Major (looks good, 6). No photograph or real result image anywhere that loads; the robotics portfolio shows no robot. Owner media needed, with true width and height.

6. Major (AI-tell: kit). Home: row 01 has a small boxed zigzag plate; rows 02-09 share one anatomy (title, two-line blurb, number, tag). Stamps appear on three of them. Reads as a featured card above a uniform list. Taste. Options: leave as is, or give every row a one-line "fact" in the right column (46 orbits, 500 m, 12 km/h, Four thrusters), which the repo already holds and which uses the existing stamp idea without new art.

7. Minor (UX, new). Project pager wraps around the list in odd order: Snake's Previous is "Design of an Assistive Tricycle" (row 09) and Aerobraking's Previous is Hasselhoff. Wraparound from the first project to the last reads as an error to a first-time visitor. Hide Previous on 01 and Next on 09, or label the wrap ("Back to the start"). Verified in snake-robots desktop screenshot.

8. Major (performance/SEO). Google Fonts stylesheet is render-blocking and third-party; no fallback metric overrides (check.py blocks it so screenshots show fallback Times). Self-host two WOFF2 with font-display: swap and preload. Owner files needed. Also the colophon names "DM Serif Display and Source Serif 4"; if fonts fail, visitors see Times and the colophon is wrong.

9. Minor (a11y/SEO, new). Heading order: projects.html goes h1 straight to h3 for the nine rows (no h2). Add a visually hidden h2 ("All projects") or promote the row titles to h2. About is fine (h1, h2, h3). Source: WCAG 1.3.1 / common heading-order guidance; low risk but trivial.

10. Minor (UX, phone length). Home on phone is about 6150 px (viewed): lede, ledger, nine rows. Duplicates the Projects page. Designer documents "home is the full index by design"; I accept it but note the 30-second reader sees only rows 01 to 03 on a first scroll.

11. Minor (SEO/CLS). Hotlinked `<img>` tags on project pages have no width/height (only the Projects thumbnails do, 96x72), so late figures shift layout. Cannot measure offline. Needs owner files. web.dev pointer above.

12. Minor (layout). About desktop: right 28% is empty below the intro for roughly 1700 px when the portrait fails. Dates in a margin column would use it. Taste, large rewrite; reopened only because the portrait is a Wix hotlink and may fail for real visitors too.

13. Minor (contact). Contact is LinkedIn only (owner constraint). The single footer sentence is the only contact line. Flag only.

14. Nit (fun). One plain aside per page from facts already in the repo (46 orbits, 12 km/h, 500 m). Declined as taste in earlier cycles; acceptable unless the owner asks.

15. Nit (a11y). The 99 s stamp (tabindex, role=button) and the Hasselhoff details control have not been driven with a real keyboard tab-through in any cycle; the log admits this. Run it once with Playwright keyboard.press("Tab") and assert focus visibility.

## Good, do not regress
- Struck-through "three weeks" in an amber marker (home, About).
- Fig. N plates with sheet tags and honest "schematic / NTS" captions; repo-local.
- Two stamp types and the holdable 99 s stamp; hard-shadow button.
- Hasselhoff disclosure bar (boxed +, Show, native details).
- Failed figures, thumbnails and portrait collapse without orphan captions.
- Plain, specific home lede and "For the record" ledger; ink-rule hierarchy; dark theme contrast; solid ink footer.
- Local og.png, JSON-LD, canonical, sitemap, noindex 404.
- No framework, no gradient, no blur.

## Verdict
The design is coherent, matte and fairly authored (AI-tell 3) and cycle 18 caused no regression. What caps looks, UX and fun at 6 is still content only the owner can supply: one status sentence, two or three facts for the Snake page (or a different Start-here), a local resume.pdf, photographs and WOFF2 files. Work the designer can do now without new facts: structure the Aerobraking page with headings and surface its result (4), fix the pager wraparound (7), add the missing h2 on Projects (9), consider one fact line per home row (6), and run a real keyboard pass (15).
