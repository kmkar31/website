# Critique, cycle 8 (2026-10-23)

Method: ran `tools/check.py` (13 pages, 3 viewports, 2 themes; all OK, only "images not loaded" sandbox notes). Viewed home desktop and phone (light), About tablet (light), quadrotor-landing phone (dark). Grepped the repo for scroll-margin, preload, width attributes, titles, alt text. Web fonts did load in this run; Wix media did not (environment limit, judged as dependency only).

Sources consulted (search results; WebFetch not used, so only titles and links are relied on):
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/optimize-cls/
- WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum), how to test: https://vispero.com/resources/how-to-test-2-4-11-focus-not-obscured-minimum/
- TetraLogical, What's new in WCAG 2.2: https://tetralogical.com/blog/2023/10/05/whats-new-wcag-2.2
- NN/g portfolio advice (secondary summary): https://blogs.ulster.ac.uk/bethbuchanan/2021/10/04/ixd301-week-2-the-neilson-norman-groups-portfolio-advice
Topic this cycle (varied): sticky-header focus/anchor obscuring, CLS from images, case-study structure.

## Scores
AI-tell: **3 / 10** (unchanged). No new tells. Remaining: the 9 rows share one anatomy and the page would look much the same with other facts; the only visual gestures are three stamps. Authored: the struck-through "three weeks", Hasselhoff naming, 404 line, mono ledger.

Looks good: **6 / 10**. The print structure is coherent and readable (double rules, ink footer, hard-shadow button). But the home screen is text only; the right third of each row is empty beyond a tiny tag; project pages are long single-column prose with large empty gaps where figures are missing (see quadrotor-landing phone, big blank bands above each caption). First impression: tidy, not memorable.

SEO: **7 / 10**. Unique titles (About and Projects now descriptive), canonical, OG/Twitter, JSON-LD, sitemap with lastmod, 404. Open: no width/height on images (3 matches in aerobraking page, so mostly missing), no preload or fetchpriority, Google Fonts dependency, robots.txt inert under a project path (owner: submit sitemap).

UX: **6 / 10**. Who/what/contact/resume are findable on home and now in the header on tablet and up. Missing still: availability/status, outcomes and role per project, any "best project" signal. On phone the header has no Resume or Contact.

Fun and personality: **5 / 10**. Stamps and marker are the whole show.

## Findings, ranked

### Owner critique
- Retro matte: honoured; no gradient, blur or glow drift. Grain is barely perceptible (taste).
- Not AI-looking: mostly honoured (3/10). The generic risk now is sameness plus absent imagery, not any effect.

1. **Major, UX/credibility: no status, no outcomes, no personal role.** Home ledger, project pages. Recruiters scan for "is he available, what did he do" (NN/g scanning guidance). Owner-only facts; designer has rightly refused to invent. Escalate to owner: graduated or enrolled (About says 2023 - 2025 with no tense), where now, and 2-3 sentences per top project.
2. **Major, Looks good: no imagery above the fold or in the index.** Home desktop: rows are text plus a ~300 px mostly empty right column. Once media is local, use a 96x72 ink-on-paper thumbnail (grayscale + contrast filter, or pre-thresholded file) per row. Blocked on owner media.
3. **Major, Robustness: all figures, portrait and resume still hotlinked from Wix.** A Wix change breaks 9 project pages and the resume link silently; JS drop-out hides the symptom from the owner. Owner must supply a media folder.
4. **Major, Looks good: project-page opening paragraphs read as generic generated prose.** quadrotor-landing: "In the realm of robotics, navigating uncertain real-world environments presents significant challenges... etc." This is a textbook AI/abstract tell, sitting directly under the specific tl;dr. If this is the owner's original text, cut the first two sentences and start at "To address these challenges..."; the Background label approach used on snake-robots and sysid should be applied here too. Check the same pattern on the other pages (taste plus credibility).
5. **Major, Accessibility: sticky header with no scroll-margin-top.** `.site-header{position:sticky}` and no `scroll-margin`/`scroll-padding` anywhere in assets/style.css. The Seagate link goes to About#seagate and in-page anchors and keyboard focus can land under the 5px-double-ruled header (WCAG 2.2 SC 2.4.11 Focus Not Obscured). Fix: `html{scroll-padding-top:72px}` (header height + margin). Verify by tabbing through About on tablet.
6. **Major, Fun: only one idea.** Ideas using facts already in the repo: (a) Hasselhoff row: the 99 s stamp could be a literal press state that counts 99 down only on :active, reduced-motion safe (designer declined twice as a gimmick; it is the only joke the owner's own project invites, so reconsider, but label as taste); (b) ledger styled as a typed index card with slight misregistration; (c) a "Status:" slot filled once owner gives it. Trade-off: keep 4.5:1 contrast and static under reduced motion.
7. **Minor, UX: phone header has no Resume or Contact.** Phone shows Home, About, Projects, theme only; project pages end in the footer with LinkedIn. Acceptable, but add the Resume link to the end of each project page's pager area or footer on phone.
8. **Minor, SEO/CLS: images lack width/height.** web.dev (optimize-cls) lists unsized images as the main CLS cause. Dimensions are unknown until media is local; add them when files arrive; use `aspect-ratio` on `.figure` only if real ratios are consistent.
9. **Minor, Looks good: empty vertical gaps where figures drop out.** quadrotor-landing phone: roughly 80-100 px of blank space above each caption remains while the caption is orphaned ("Tumbller with the small landing pad (left) and the CrazyFlie (right)" refers to a picture that is not there). The row collapses but the caption does not. When all images fail, hide the caption too, or the page reads as broken.
10. **Minor, Looks good: row right column.** Desktop home: tags sit at x~1015 with ~100 px dead space between blurb and tag. Taste; consider placing the index number left of the title.
11. **Minor, Content: About says "I'm pursuing a Master's" with education 2023 - 2025.** Today is October 2026; unresolved tense makes the page look stale. Same as finding 1; fix with owner's status line.
12. **Minor, Performance: Google Fonts, no preload, no fallback metrics.** Reuse the earlier note; self-host WOFF2 when possible. Not actionable in the sandbox.
13. **Nit, SEO: home and Projects index duplicate each other.** Low priority; differentiate with filters visible.
14. **Nit, Fun: Podium and 99 s stamps good; "46 orbits" dashed stamp reads like a form field.** Taste.
15. **Nit, Content: footer sentence "To get in touch, message me on LinkedIn."** is plain and fine; no email is a conscious choice, but a professor may expect one. Owner decision.

## Good, must not regress
- Plain specific home lede and struck-through marker, consistent on About.
- Ruled index, double rule, ink footer, single hard-shadow button; no gradients or blur.
- Varied stamps, 404 line, mono ledger, header Resume link with arrow on tablet and up.
- Titles, canonical, OG/Twitter, JSON-LD, sitemap lastmod, skip link, 44 px targets, no overflow at any viewport, figure/portrait drop-out, pager with summaries.
- Dark theme inverted print with legible muted text (verified on project phone dark).

## Verdict
Clean, honest and coherently retro with a low AI-tell score (3/10), but it remains tidy rather than memorable. The biggest gaps (status, outcomes, media, local files) need the owner. Within the designer's reach this cycle: the scroll-margin fix (real accessibility defect), removing the generic "In the realm of robotics" openings, hiding orphaned captions when figures fail, and one earned interaction. Axes below 7: looks good (6), UX (6), fun (5), raising Major findings 1, 2, 6.
