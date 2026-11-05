# Critique, 2026-11-05 (cycle 85)

Rendering: `python3 tools/check.py . agents/shots` completed, all OK (only "images not loaded, likely sandbox network" notes; it needed a longer timeout than 2 minutes). I viewed index phone light, index desktop dark and quadrotor-sysid tablet light. Repo checks by grep: canonical present, `:focus-visible` outline (3px) and a `prefers-reduced-motion` block exist, Wix hotlinks (filesusr/wixstatic) on every page, including 404 (2). `STATUS = ""` still at build/build.py:262. No site files edited. No regression from cycle 84 (it changed nothing).

## Sources consulted (honest note)
WebFetch of WCAG 2.4.13 Focus Appearance and web.dev optimize-lcp were blocked by a permission timeout, so I did not read them. Earlier cycles hit the same block. These are pointers only and no finding depends on them.
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (not read)
- https://web.dev/articles/optimize-lcp (not read)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (not read)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset primary button, mono ledger, boxed stamps, flat dark footer, flat inverted dark theme. No gradient, blur or glow anywhere in the screenshots.
2. Not AI-looking: met. Strike-through marker on "three weeks / 15 minutes", stamps that carry real numbers, plain specific copy, graph-paper Fig. plates with sheet numbers ("Sheet 8 of 9 · NTS"). No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniform ruled rows; DM Serif plus mono labels is a familiar editorial pairing. No tells moved this cycle.
- Looks good: 7/10. Phone and desktop home have clear hierarchy and rhythm; dark desktop is coherent. Weak: one plate among nine rows (row 06 only), no photograph anywhere in the render; the sysid page is text-heavy below the plate (three long Background paragraphs).
- SEO: 7/10 (per repo). Not verifiable offline: live og:image, field LCP/CLS, Search Console indexing.
- UX: 7/10. Name, role, strongest project ("Start here", 06) and LinkedIn are in the first phone screens; Previous/Next on project pages. Missing: status line, email.
- Fun and personality: 7/10. Strike-through, 99-second stamp, 46 orbits, 500 m tether, sheet numbering are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence (`STATUS = ""`). About lists the Master's as 2023 - 2025 and it is November 2026; the lede is present tense ("I research"). A recruiter cannot tell whether he is a student, employed or looking. Owner supplies one line.
2. Major, robustness (owner file): Resume (PDF) is a Wix filesusr.com hotlink repeated in header, lede and footer on every page including the 404. One dead URL breaks every instance. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no photograph; About portrait and most project media are static.wixstatic.com hotlinks (1-9 per page). Third-party dependency the owner does not control; if it fails, project pages are text plus one schematic.
4. Major, content (owner facts): the lead entry, Snake robots (row 01), has a lab, advisor, a question and a generic "why snake robots" paragraph but no result, gait name or figure from his own work. Raftar is similarly thin. The strongest rows (04, 05, 06, 07) carry numbers; row 01 does not. Owner supplies one outcome each.
5. Minor, UX: the phone header has only Home / About / Projects; resume and contact live in lede and footer. LinkedIn-only contact is a documented owner decision, so I raise only the phone header.
6. Minor, performance (owner dimensions): hotlinked figures lack known width/height or aspect-ratio, a CLS risk once they load.
7. Minor, performance: Google Fonts with no self-hosted WOFF2 or tuned fallback metrics; flash of fallback type possible on slow connections.
8. Nit, SEO (owner action): robots.txt and sitemap sit under a project-site subpath (/website/), so crawlers do not read robots.txt there; submit sitemap.xml in Search Console.
9. Nit, visual: sysid page has long Background prose after a short model section; an optional "skip to background" is not needed, but the order (question, result, model, then background) is already right. Taste only; no change required.

## Good, must not regress
- Retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific copy with real numbers (3 weeks to 15 minutes, 46 orbits, 99 s, 500 m).
- "Start here" marker on the strongest project; Previous/Next with a fact under each title.
- Fig./Sheet captions on the schematic plates.
- Visible 3px focus outline, reduced-motion block, 44px tap targets, one h1 per page, canonical/OG/JSON-LD, sitemap and robots.

## Verdict
The site commits to its matte print direction and reads as authored, not templated. All remaining weaknesses are owner-supplied content or files: a status line, a local resume PDF, photographs in place of Wix hotlinks, and one concrete result each for Snake robots and Raftar. There is no designer-fixable defect this cycle; further CSS work would be churn. The most valuable next step is for the owner to supply items 1 to 4.
