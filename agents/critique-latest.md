# Critique, 2026-10-31 (cycle 52)

Rendering: `python3 tools/check.py` hit the 2-minute tool timeout in this run, so I did not get its pass/fail summary. It had written screenshots for 12 of 13 pages (tethered-nanosatellite desktop-light is missing). I viewed home phone-light, home desktop-light and aerobraking phone-dark. Repo state unchanged since cycle 51 (no site changes since cycle 47 CSS/JS and cycle 49). No regressions seen. No site files edited.

## Sources consulted
Web research was attempted but WebFetch permission requests went unanswered, so NO source was actually read this cycle. The "three sources" rule is NOT met. Blocked URLs:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://web.dev/articles/optimize-cls
- https://www.nngroup.com/articles/how-people-read-online/
Claims below that lean on them (24 px minimum target in WCAG 2.5.8; unsized images cause layout shift; users scan) are from prior knowledge and unverified here.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Flat paper, ink rules, hard-offset button, inverted-print dark theme. Seen in screenshots.
2. Must not look AI-generated: met.

## Scores
- AI-tell score: 2/10, unchanged. No gradients, glass, blobs, card trio or stats strip. Authored: struck-through "three weeks" on a highlighter band, "For the record" ledger, stamps tied to real numbers, sheet-tagged figure plates, colophon. Remaining faint tell: nine identically ruled rows. Hero copy "I work on control of robots and spacecraft" is plain and specific. No tells moved.
- Looks good: 7/10. Coherent and even. Held back by having no photograph of a real object or person; the only visual on home is a small schematic on row 01, so rows 02-09 are text only and the desktop list reads long and uniform.
- SEO: 7/10. Head tags, JSON-LD, sitemap, robots and noindex 404 are present per prior cycles. LCP/CLS on hotlinked Wix images cannot be verified offline.
- UX: 7/10. Phone first screen answers who, where, what and next step. No status line; LinkedIn is the only contact route.
- Fun and personality: 7/10. Highlighter strike-through, stamps and 404 voice are earned. Little else is memorable.

## Ranked findings
1. Major, content: no status line. CMU MS is listed as 2023-2025 and today is 2026-10-31; a recruiter cannot tell whether he has graduated, where he is, or if he is available. Needs one owner sentence (STATUS slot in build/build.py). Not designer-fixable.
2. Major, robustness: Resume (PDF), the primary call to action, points to a Wix filesusr.com URL in the header, hero and footer. assets/ has no resume.pdf. If Wix moves it, the main CTA breaks. Owner must supply the file.
3. Major, content: "Start here" (Snake robots) is the thinnest project page: schematic, question, lab and advisor, but no result and no statement of what he did. Aerobraking (46 orbits) is stronger. Owner to supply outcomes or move the label.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). Owner files needed. Until then the site is type and drawings only.
5. Minor, performance: Wix figures lack width/height; the 220 px placeholder will not match real aspect ratios, so some shift remains. Real fix is local images.
6. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and the project page with no specifics. Ferrari weight / 0-60 claim awaits owner confirmation.
7. Minor, readability: Aerobraking phone view (about 9,200 px tall) is long dense prose before the result; the result is the 3-number summary at top, which helps, but the "Problem" section is one wall of text. Splitting it is a designer-fixable text-layout option only if wording is untouched.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4; font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: Wix figure alt text is generic ("figure 1 of 3").
10. Nit: contact is LinkedIn only (owner constraint). Phone header shows only the K mark; the H1 name sits directly below, so harmless.
11. Nit: stamps on four of nine rows; add none without real numbers.
12. Nit: on desktop About leaves the right third empty (documented taste).

Findings 1 to 4 move only with owner-supplied facts or files. Further designer cycles will churn.

## Good, must not regress
Plain-prose home intro with the highlighted "three weeks to 15 minutes"; ruled project index with real-number stamps; "For the record" ledger; graph-paper figure plate with sheet tags; warm paper and inverted-print dark themes; hard-offset button; 404 voice; colophon; clear previous/next links and the key-numbers strip at the top of project pages.

## Verdict
The site commits coherently to the retro matte direction and reads as authored, not generated. What holds it at 7s is not design craft but missing owner inputs: a status sentence, a local resume, a result for the "Start here" project, and real photographs. This cycle also had no working web research, so its standards claims are unverified. The designer has little left to fix alone.
