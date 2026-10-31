# Critique, 2026-10-31 (cycle 53)

Rendering: `python3 tools/check.py . agents/shots` completed this cycle: 13 pages x 3 viewports x 2 themes, all OK (only "images not loaded" sandbox notes for Wix hosts). I viewed home phone-light, home desktop-light, home tablet-dark, snake-robots phone-light and About desktop-light. No site changes since cycle 47/49 (git status clean), so no regressions from the last designer pass. No site files edited.

## Sources consulted
Read in full this cycle:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8: 24x24 CSS px minimum, with spacing, inline, equivalent and essential exceptions; the site's 44 px targets exceed it).
- https://web.dev/articles/css-size-adjust (a local fallback face scaled with `size-adjust` reduces swap-time layout shift; the author must tune the percentage).
Blocked, not read: https://www.nngroup.com/articles/how-people-read-online/ (permission request unanswered). A WebSearch for portfolio/hiring-manager guidance returned only titles of blog posts (ntc.it.com, uxdesigninstitute.com, medium); I did not read them and do not rely on them. So two of the three required sources were read; the third is missing.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Flat paper tone, ink rules, hard-offset button, inverted-print dark theme, no blur or glow. Seen in all screenshots.
2. Not AI-generated: met (see score).

## Scores
- AI-tell score: 2/10, unchanged. No gradients, glass, blobs, card trio, stats strip or badge-on-photo. Authored and specific: the struck-through "three weeks" on a highlighter band, "For the record" ledger, stamps carrying real numbers (46 orbits, 500 m, 99 s), lab-notebook Fig./Sheet tags, plain first-person prose. Remaining faint tell: nine identically ruled rows with one mono tag column; also typographic pairing (DM Serif Display + Source Serif) is tasteful but common in "editorial" templates. No tells moved since cycle 52.
- Looks good: 7/10. Coherent, consistent rhythm, strong dark theme. Held back because no photograph of a real object or person survives anywhere (in the sandbox the Wix images fail, and on the live site they are hotlinked), so the site is type and schematics only. On snake-robots phone the whole first screen-and-a-half is title, tl;dr, question, two fact rows and one schematic: honest but bare for the project labelled "Start here".
- SEO: 7/10. Title, description, canonical, OG/Twitter, local og:image, JSON-LD, sitemap, robots, noindex 404 all present per earlier cycles. Cannot verify offline: LCP/CLS on Wix images, live og:image fetch, host-root robots.txt on a project path.
- UX: 7/10. On phone the first screen gives name, school, lab, advisor, one result and the primary button; Resume and LinkedIn are one tap away; previous/next on project pages. Gaps: no status line, one contact route.
- Fun and personality: 7/10. The strike-through, stamps (Hasselhoff stamp counts down while pressed) and 404 line are earned. Beyond those, little is memorable; this is correct restraint given no new facts.

## Ranked findings
1. Major, content: stale and ambiguous status. Home subtitle, About lede and Education all say CMU MS "2023 - 2025"; today is 2026-10-31, so a recruiter cannot tell if he graduated, where he is now, or whether he is available. About phrases it "is at Carnegie Mellon". The STATUS slot in build/build.py is empty. Owner must supply one sentence. Not designer-fixable.
2. Major, robustness: the primary call to action, Resume (PDF), is a Wix `filesusr.com` URL used in the header, hero and footer. assets/ has no resume.pdf. If Wix retires it, the main CTA 404s on every page. Owner must drop the file in assets/.
3. Major, content: the "Start here" project (Snake robots) is among the thinnest pages: schematic, question, lab, advisor, a one-sentence "Why snake robots". No result, no statement of what he specifically built or measured. The Aerobraking page (46 orbits) is far stronger. Owner should supply 2 to 3 outcome sentences or move the label. Page evidence: snake-robots phone-light.
4. Major, visual: no real photograph of a snake robot, the RFR23 car, the podium or the tricycle. Until owner media exists the site is type and drawings only. Images are Wix hotlinks, a dependency risk as well.
5. Minor, performance/CLS: hotlinked figures have no width/height, so the reserved placeholder cannot match real ratios; shift remains once they load. WCAG/web.dev logic: reserve space by intrinsic size. Real fix is local images.
6. Minor, performance: no `size-adjust` fallback face for DM Serif Display / Source Serif 4, so the headings can reflow on font swap (https://web.dev/articles/css-size-adjust). Needs measured metrics or self-hosted WOFF2 from the owner; a guessed percentage could make it worse.
7. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and project page with no new specifics; any Ferrari-weight or 0-60 comparison awaits owner confirmation.
8. Minor, readability: Aerobraking phone page is very tall with a dense Problem section before the figures. Splitting needs new subheads, so it needs owner agreement.
9. Minor, accessibility: Wix figure alt text is generic ("figure 1 of 3"). Owner must say what each image shows.
10. Nit: on desktop About, the right column holds the "On this page" index only because the portrait is missing here; with the portrait present, check the 280 px column does not look empty at the Skills section (documented taste).
11. Nit: stamps on four of nine rows; add none without real numbers.
12. Nit: phone header shows only the K mark; the name is the h1 directly below, so harmless.

Findings 1 to 4 move only with owner-supplied facts or files. Further designer-only cycles will churn.

## Good, must not regress
Plain-prose home intro with the highlighted "three weeks to 15 minutes"; ruled project index with real-number stamps and "Start here"; "For the record" ledger; graph-paper Fig. plates with sheet tags; warm paper and inverted-print dark themes; hard-offset primary button; pressable 99 s stamp; 404 voice; honest colophon; footer with LinkedIn, GitHub and Resume on every page; clear previous/next links; 44 px tap targets (WCAG 2.5.8 needs only 24).

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person, not a template. Rendering is clean across 78 screenshots with no overflow or contrast failures. What holds every axis at 7 is not craft but missing owner inputs: a current status sentence (the 2023-2025 dates are now stale), a local resume file, results for the "Start here" project, and real photographs. The designer has nothing substantial left to fix alone; the most valuable next step is for the owner to supply those four items.
