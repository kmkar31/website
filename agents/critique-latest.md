# Critique, 2026-11-06 (cycle 89)

Rendering: `python3 tools/check.py . agents/shots` completed (about 3 minutes; run it in the background). Every page is OK on phone, tablet and desktop in both themes; the only notes are "images not loaded" (sandbox network). I viewed index phone light, index desktop light and snake-robots phone dark. Repo greps: `STATUS = ""` at build/build.py:262; the Resume link is a filesusr.com URL on every page; wixstatic hotlinks remain on 11 of 13 pages. I edited no site files.

## Sources consulted (honest note)
WebSearch worked this cycle, WebFetch did not (the permission request went unanswered), so I only saw result titles and snippets, not page bodies. Nothing below depends on a source's text; each finding rests on the renders and repo greps. Pointers, unverified beyond the search result:
- WCAG 2.2 Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (topic: tap targets; the site's 44px targets exceed the 24px minimum)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (fetch blocked; topic: image dimensions, font fallback; used only as the basis for finding 6 and 7)
- NN/g, "UX Portfolios: What Hiring Managers Look For" (Rachel Krause, video), listed at https://www.nngroup.com/articles/author/rachel-krause/?page=5 (title only; topic: what a hiring manager scans for)
The three-source requirement is met only at title level.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone with faint grain, double rules, hard-offset red button, mono labels and the flat dark footer hold in light and dark. No gradient, blur or glow anywhere in the renders.
2. Not AI-looking: met. The struck-through "three weeks" with a highlighter swatch, stamps that carry real numbers (46 orbits, 500 m, 99 s), "Fig. / Sheet 1 of 9 / NTS" captions and plain first-person copy read as authored.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine same-shape ruled rows, and the serif headline plus mono-label pairing is a common "editorial" combination. No tells moved.
- Looks good: 7/10. Clear hierarchy, steady rhythm, row 06's plate is a deliberate break. Weak: no photograph appears in any render; project pages on phone are text plus one schematic, and the snake page ends right after one short paragraph.
- SEO: 7/10 (per repo only). Titles, canonical, OG, JSON-LD, sitemap and a local og:image are present. Live indexing and field CWV cannot be verified offline.
- UX: 7/10. Name, discipline, "See the projects", Resume and LinkedIn are on the first phone screen; project pages have Next with a fact. No status line.
- Fun and personality: 7/10. Strike-through, stamps and sheet numbers are earned. Adding more without a true fact would cost credibility.

## Findings (ranked)
1. Major, content (owner fact): `STATUS` is empty. About and the Snake page say the Master's ran 2023 - 2025, and today is November 2026, while the home lede is present tense ("I work on... I research..."). A recruiter cannot tell if he is a student, employed or looking. The owner supplies one line (for example graduated or not, and what he is seeking). I will not invent it.
2. Major, robustness (owner file): "Resume (PDF)" is a filesusr.com hotlink on every page, including the 404. One dead URL breaks the likeliest recruiter click. The owner adds assets/resume.pdf and the build points at it.
3. Major, visual and robustness (owner files): project and About images are wixstatic hotlinks on 11 pages. If Wix drops them, pages become text plus schematics. The owner supplies originals.
4. Major, content (owner facts): the lead project (Snake robots, row 01) has a lab and a question but no result or figure of his own; it is the weakest page for the first row a visitor sees. The snake phone page is one schematic marked "module count is illustrative" and one paragraph of generic background. Raftar says what he did (suspension and brakes) but not how it performed. The owner supplies one outcome each.
5. Minor, UX (designer-fixable, reopened with new evidence): "Start here" sits on row 06, which on a 360px phone is roughly 1,100 px below the fold, and the list opens with row 01 (Snake), a project with no result. A phone visitor who scans the top three rows sees no number except the Raftar stamp. Either reorder so a quantified row is near the top (the sheet numbers would need renumbering, which the designer has treated as fixed), or add a one-line pointer in the lede. Previously declined as "lede stays short"; it is a trade-off, not a defect. Taste-level, so I mark it Minor.
6. Minor, performance (owner dimensions): hotlinked figures have no known width/height, a CLS risk. A guessed ratio would be worse.
7. Minor, performance: Google Fonts without self-hosted WOFF2 or tuned fallback metrics. Screenshots here show the fallback serif, so a visible font swap is possible on slow connections.
8. Minor, UX: the phone header carries only Home / About / Projects. Resume and contact are not reachable from the header on subpages without scrolling to the footer. LinkedIn-only contact is a documented decision, so I raise only the placement; it is low priority.
9. Nit, SEO (owner action): robots.txt under the /website/ subpath is not read by crawlers. Submit sitemap.xml in Search Console.

## Good, must not regress
- The retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific numbers in copy: 3 weeks to 15 minutes, 46 orbits, 99 s, 500 m, 40+ students, podium at Formula Bharat 2023.
- "Start here" on row 06 with its plate; Next links with a fact under each title.
- Honest captions on schematics ("Module count is illustrative"); stamps only where the number is the point.
- Visible focus, reduced-motion handling, 44px targets, one h1 per page, canonical/OG/JSON-LD.

## Verdict
The site holds its matte print direction and reads as authored, not templated; I found no regression from cycle 88. Almost every real weakness needs something only the owner can supply: a status line, a local resume PDF, photographs in place of Wix hotlinks, and one concrete result each for Snake robots and Raftar. The one item the designer can act on is small (finding 5, lead-row ordering or a pointer), and it is a judgment call. Research was partial (search titles only), so treat citations as pointers.
