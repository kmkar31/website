# Critique, 2026-11-06 (cycle 88)

Rendering: `python3 tools/check.py . agents/shots` completed (it needs more than 2 minutes; run it with a long timeout). All pages are OK in phone, tablet and desktop, light and dark; the only notes are "images not loaded" from the sandbox. I viewed index phone light, index desktop dark and raftar-formula-racing phone light. Repo greps: `STATUS = ""` still at build/build.py:262; the Resume link points at filesusr.com on all 13 pages (27 occurrences). No site files edited by me.

## Sources consulted (honest note)
WebFetch (web.dev/articles/optimize-cls), WebSearch (NN/g portfolio usability) and Bash were all refused by the permission classifier ("no verdict") this cycle, so I read no external source. The three-source requirement is unmet again. No finding below depends on a source; each rests on screenshots and repo greps.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono labels and the flat dark footer hold in both themes. No gradient, blur or glow.
2. Not AI-looking: met. The struck-through "three weeks", stamps that carry real numbers, "Fig./Sheet" plates and plain first-person copy are authored. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine same-shape ruled rows and the serif-plus-mono-label pairing. No tells moved.
- Looks good: 7/10. Clear hierarchy and rhythm; row 06's plate is a deliberate break. Weak: no photograph renders; project pages on phone are text plus one schematic.
- SEO: 7/10 (per repo). Titles, canonical, OG, JSON-LD, sitemap, local og:image present. Live indexing and field CWV cannot be verified offline.
- UX: 7/10. Name, discipline, "See the projects", Resume and LinkedIn are on the first phone screen; project pages have Previous/Next with a fact. The status line is missing.
- Fun and personality: 7/10. Strike-through, stamps and sheet numbers are earned. Add nothing without a true fact.

## Findings (ranked)
1. Major, content (owner fact): `STATUS` is empty. About says the Master's runs 2023 - 2025; today is November 2026 and the home lede is present tense ("I work on... I research..."). A recruiter cannot tell if he is a student, employed or looking. Owner supplies one line.
2. Major, robustness (owner file): "Resume (PDF)" is a filesusr.com hotlink on every page including the 404. One dead URL breaks the likeliest recruiter click. Owner adds assets/resume.pdf.
3. Major, visual and robustness (owner files): project and About images are wixstatic hotlinks on 11 pages. If Wix drops them, pages become text plus schematics.
4. Major, content (owner facts): the lead project (Snake robots, row 01) has a lab and a goal but no result or figure of his own, and is the only top-three row with no number. Raftar says what he did (suspension and brakes) but not how it performed. Owner supplies one outcome each.
5. Minor, UX: the phone header has only Home / About / Projects; Resume and contact are below the fold on the home page. LinkedIn-only contact is a documented decision; I raise only the header, and the first phone screen already shows both links, so this is low priority.
6. Minor, performance (owner dimensions): hotlinked figures have no known width/height, a CLS risk. A guessed ratio would be worse.
7. Minor, performance: Google Fonts without self-hosted WOFF2 or tuned fallback metrics; a flash of fallback type is possible.
8. Nit, SEO (owner action): robots.txt under the /website/ subpath is not read by crawlers. Submit sitemap.xml in Search Console.

## Good, must not regress
- The retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific numbers in copy: 3 weeks to 15 minutes, 46 orbits, 99 s, 500 m, 40+ students, podium at Formula Bharat 2023.
- "Start here" on row 06 with its plate; Previous/Next with a fact under each title.
- Honest captions on schematics; stamps only where the number is the point.
- Visible focus, reduced-motion handling, 44px targets, one h1 per page, canonical/OG/JSON-LD.

## Verdict
The site keeps to its matte print direction and reads as authored, not templated. Every remaining weakness needs something only the owner can supply: a status line, a local resume PDF, photographs instead of Wix hotlinks, and one concrete result each for Snake robots and Raftar. I found no designer-fixable defect and no regression (the tree is unchanged by me and nothing in the renders differs from cycle 87's description). External research was blocked again, so that requirement is unmet.
