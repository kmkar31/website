# Critique, 2026-11-06 (cycle 87)

Rendering: `python3 tools/check.py . agents/shots` ran to the end, with all pages OK in phone, tablet and desktop, light and dark. The only notes are "images not loaded" from the sandbox. I viewed index phone light, index desktop dark, snake-robots phone light and about phone dark. Repo greps: `STATUS = ""` is still at build/build.py:262, and the resume is still a filesusr.com hotlink. wixstatic hotlinks remain on 11 pages. og:image is the local absolute URL https://kmkar31.github.io/website/assets/og.png. robots.txt points at the sitemap. No site files edited. The working tree was clean before I wrote this file, and nothing has changed on the site since cycle 86, so no regression is possible.

## Sources consulted (honest note)
WebFetch of https://web.dev/articles/optimize-cls was blocked by a permission timeout, as were earlier cycles' fetches. I could not read any external source this cycle, so I do not meet the three-source requirement. No finding depends on a source; each rests on the screenshots and repo greps. Not read:
- https://web.dev/articles/optimize-cls (blocked)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked earlier)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. The paper tone, double rules, hard-offset button, mono labels and flat dark footer band hold in both themes. There is no gradient, blur or glow.
2. Not AI-looking: met. The struck-through "three weeks", the stamps that carry real numbers, "Fig./Sheet" plates and plain first-person copy are authored. There are no new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells are nine same-shape ruled rows and the DM Serif plus mono-label pairing. No tells moved.
- Looks good: 7/10. Hierarchy and rhythm are clear on phone and desktop, and row 06's plate makes a deliberate break. Weak spots: there is no photograph in the render, and the snake page on phone is text plus one schematic.
- SEO: 7/10 (per repo). Titles, canonical, OG, JSON-LD, sitemap and a local og:image are present. Live fetch, field CWV and indexing cannot be verified offline.
- UX: 7/10. Name, discipline, "Start here", Resume and LinkedIn are visible on the first phone screens, and project pages have Next. The status line is missing.
- Fun and personality: 7/10. The strike-through, the stamps and the sheet numbers are earned. Add nothing without a true fact.

## Findings (ranked)
1. Major, content (owner fact): `STATUS` is empty. About says the Master's runs 2023 - 2025, today is November 2026, and the home lede is in the present tense. A recruiter cannot tell whether he is a student, employed or looking. The owner supplies one line.
2. Major, robustness (owner file): "Resume (PDF)" is a single filesusr.com hotlink on every page, including the 404. One dead URL breaks the recruiter's most likely click. The owner adds assets/resume.pdf.
3. Major, visual and robustness (owner files): project and About images are wixstatic hotlinks on 11 pages. If Wix drops them, the pages become text plus schematics. The owner does not control that.
4. Major, content (owner facts): the lead project, Snake robots (row 01), has a lab and a goal but no result, gait or figure of his own, and it is the only top-three row with no number. The snake page's "Why snake robots" section is generic background that would fit any snake-robot page. Raftar is also thin on what he personally did. The owner supplies one outcome each.
5. Minor, UX: the phone header has only Home / About / Projects, so Resume and contact sit below the fold. LinkedIn-only contact is a documented decision, so I raise only the header.
6. Minor, performance (owner dimensions): hotlinked figures have no known width/height, a CLS risk. A guessed ratio would be worse.
7. Minor, performance: Google Fonts without self-hosted WOFF2 or measured fallback metrics, so a flash of fallback type is possible.
8. Nit, SEO (owner action): robots.txt sits under the /website/ subpath, where crawlers do not read it. Submit sitemap.xml in Search Console.

## Good, must not regress
- The retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific numbers in the copy: 3 weeks to 15 minutes, 46 orbits, 99 s, 500 m, 40+ students, podium at Formula Bharat 2023.
- "Start here" on row 06 with its plate, and Next with a fact under each title.
- "Module count is illustrative" caption on the schematic, which is honest.
- Stamps only where the number is the point.
- Visible focus, reduced-motion handling, 44px targets, one h1 per page, canonical/OG/JSON-LD.

## Verdict
The site keeps to its matte print direction and reads as authored, not templated. Every remaining weakness needs something only the owner can supply: a status line, a local resume PDF, photographs instead of Wix hotlinks, and one concrete result each for Snake robots and Raftar. I found no designer-fixable defect and no regression. This cycle's external research was blocked, so the research requirement is unmet.
