# Critique, 2026-11-06 (cycle 86)

Rendering: `python3 tools/check.py . agents/shots` finished with 78 OK lines and no failures (only sandbox "images not loaded" notes; it needs more than the 2 minute default timeout). I viewed index phone light, index desktop light and about tablet dark. Repo checks by grep: og:image is the local assets/og.png (absolute URL), Person JSON-LD present, `STATUS = ""` still at build/build.py:262, resume is still a filesusr.com hotlink, about.html still has a wixstatic hotlink. No site files edited. No regression: nothing changed since cycle 85.

## Sources consulted (honest note)
WebFetch of the WCAG 2.2 target-size page was blocked by a permission timeout (same as earlier cycles). A WebSearch for Nielsen Norman Group portfolio advice returned only a list of titles and links; I did not read any of them. These are pointers, and no finding depends on them.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked, not read)
- https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (search result, not read)
- https://blog.adplist.org/post/what-is-a-hiring-manager-looking-for-in-a-design-portfolio (search result, not read)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules under the header, hard-offset red button, mono ledger, boxed stamps, flat dark footer band, inverted dark theme. No gradient, blur or glow in any screenshot.
2. Not AI-looking: met. The struck-through "three weeks" in a marker highlight, stamps that carry real numbers, plain specific copy and the "Fig. 1 / Sheet n of 9" plates are not template moves. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine same-shape ruled rows, and a DM Serif plus mono-label pairing that is familiar editorial territory. No tells moved.
- Looks good: 7/10. Phone and desktop home have a clear hierarchy and steady rhythm. Row 06's plate and larger title make a deliberate break in the list. Weak spots: no photograph anywhere in the render; on desktop the lede stops at about 650px, leaving a wide gap before the ledger; About on tablet is a long single column of short rules.
- SEO: 7/10 (per repo). Titles, descriptions, canonical, OG/Twitter, JSON-LD, sitemap and a local og:image are in place. Not verifiable offline: live og:image fetch, field LCP/CLS, Search Console indexing.
- UX: 7/10. Name, discipline, strongest project ("Start here", 06), Resume and LinkedIn are visible in the first phone screens, and project pages have Previous/Next. Missing: a status line and a phone-header route to resume.
- Fun and personality: 7/10. The strike-through, the 99 s stamp, 46 orbits, the 500 m tether and the sheet numbers are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): there is no current-status sentence (`STATUS = ""`). About lists the Master's as 2023 - 2025 and today is November 2026, while the home lede is in the present tense ("I research", "I work on"). A recruiter cannot tell whether he is a student, employed or looking. The dated text is now more than a year old. Owner supplies one line; the ledger slot already exists.
2. Major, robustness (owner file): "Resume (PDF)" is a single filesusr.com hotlink repeated in the header, lede and footer on every page, including the 404. One dead URL breaks all of them, and a recruiter's most likely click is the resume. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no photograph appears in the render. The About portrait and most project figures are wixstatic hotlinks. If Wix drops them, project pages are text plus one schematic. The owner does not control that dependency.
4. Major, content (owner facts): the lead project, Snake robots (row 01), states a lab and a goal but no result, gait or figure from his own work. In the row list it is the only top-three row with no number, next to rows that carry hard facts (04, 05, 06, 07). Raftar is similarly thin on what he personally did. Owner supplies one outcome each.
5. Minor, UX: the phone header has only Home / About / Projects, so resume and contact sit below the fold in the lede and footer. LinkedIn-only contact is a documented owner decision, so I raise only the header.
6. Minor, performance (owner dimensions): hotlinked figures have no known width/height or aspect-ratio, a CLS risk once they load. A guessed ratio would be worse than none.
7. Minor, performance: Google Fonts with no self-hosted WOFF2 or tuned fallback metrics. Flash of fallback type is possible on slow connections.
8. Nit, SEO (owner action): robots.txt and sitemap.xml sit under the /website/ subpath, where crawlers do not read robots.txt. Submit sitemap.xml in Search Console.
9. Nit, visual (taste): on desktop home the row blurbs run about 700px and the tag column starts at roughly 935px, so mid-width gaps on short-blurb rows (05, 07) look slightly loose. No fault measured; leave unless the designer is looking for something to do.

## Good, must not regress
- Retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific copy with real numbers (3 weeks to 15 minutes, 46 orbits, 99 s, 500 m, 40+ students, podium at Formula Bharat 2023).
- "Start here" on row 06 with its captioned plate; Previous/Next with a fact under each title.
- Fig./Sheet captions on the schematic plates.
- Stamps only where the number is the point.
- Visible focus outline, reduced-motion handling, 44px tap targets, one h1 per page, canonical/OG/JSON-LD, local og:image.

## Verdict
The site commits to its matte print direction and reads as authored, not templated; the screenshots hold up on phone, tablet and desktop in both themes. Every remaining weakness needs something only the owner can supply: a status line (the dates are now stale), a local resume PDF, photographs in place of Wix hotlinks, and one concrete result each for Snake robots and Raftar. There is no designer-fixable defect this cycle, and further CSS work would be churn. The most valuable next step is for the owner to supply items 1 to 4.
