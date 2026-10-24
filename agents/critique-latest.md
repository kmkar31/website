# Critique, cycle 9 (2026-10-24)

Method: ran `tools/check.py` (13 pages, 3 viewports, 2 themes; all OK, only "images not loaded" sandbox notes; it takes over 2 minutes, run it in the background). Viewed home phone light and tablet dark, About desktop light, Hasselhoff phone light. Grepped the repo for titles, descriptions, alt text, wixstatic counts, scroll-padding, stock phrases. No site files edited.

Sources (WebSearch/WebFetch were not available in this run, so these are pointers from prior knowledge, not fetched this cycle; the designer should treat them as unverified):
- Google Search Central, "Influencing your title links" and "Control your snippets": https://developers.google.com/search/docs/appearance/title-link and https://developers.google.com/search/docs/appearance/snippet
- web.dev, Optimize Largest Contentful Paint and Optimize CLS: https://web.dev/articles/optimize-lcp , https://web.dev/articles/optimize-cls
- NN/g, "How people read online" / F-pattern scanning (credibility and skimming): https://www.nngroup.com/articles/how-users-read-on-the-web/
- WCAG 2.2 SC 1.4.12 Text Spacing and SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/
Topic this cycle (varied): snippet/title SEO per page, stale-date credibility, image weight and hotlinking.

## Scores
AI-tell: **3 / 10** (unchanged). No generic effects. Remaining tells: nine rows of one anatomy; a "warm cream + rust + amber" palette that is tasteful but common among "editorial" templates; the hero reads as name, subtitle, lede, button, ledger, list. Authored: the struck-through "three weeks", Hasselhoff and 99-second stamp, the 404 line, the mono "For the record" ledger. Moved since last cycle: the "In the realm of robotics" opening is gone (tell removed); orphaned captions fixed.

Looks good: **6 / 10**. The home page is clean and the type is good (DM Serif display plus Source Serif body, double rules, ink footer). But on every viewport it is text only: the home page has no image at all, the project pages show captions or blank gaps, and the About page leaves a big empty right third on desktop (portrait gone in the sandbox, and even when present it is the only picture). Hierarchy on project pages is good (tl;dr large, facts, sections). Phone home is a long, even scroll of near-identical rows (about 5700 px).

SEO: **6 / 10**. Unique titles on all 13 pages, canonical, OG/Twitter, JSON-LD, sitemap with lastmod, local og.png: all good. Weak spots below (descriptions, hotlinking, root robots.txt).

UX: **6 / 10**. Who and what are clear in 3 seconds on phone; contact and resume are findable (footer, home actions). But there is no status and no "start here" project; credibility details are stale (see 1).

Fun and personality: **5 / 10**. Stamps and the marker are the whole show; the rest is tidy. Raised as Major below.

## Findings, ranked

### Owner critique (user-critique.md)
- Retro matte theme: honoured. No gradient, blur or glow anywhere; hard shadow only on the primary button; grain is barely visible (taste; a touch more would sell "paper" in the screenshots).
- Must not look AI-generated: mostly honoured at 3/10. The residual risk is sameness and lack of a human voice (no first-person detail beyond the lede), not any visual effect.

1. **Major, Credibility/UX: stale and ambiguous status.** About (desktop): "I'm pursuing a Master's" with Education "2023 - 2025"; today is Oct 2026. Home gives no status either (the STATUS slot is empty). A recruiter will read this as an abandoned site or a person who has graduated and hides it. Owner-only fact; designer correctly refuses to invent. Escalate: graduated or enrolled, where now, available or not. Until then, at minimum change About's present-tense "I'm pursuing" to a tense-neutral sentence ("MS in Mechanical Engineering at Carnegie Mellon, 2023 - 2025") so it is not false either way. Evidence: NN/g scanning research says readers decide fast on the first lines (https://www.nngroup.com/articles/how-users-read-on-the-web/).
2. **Major, Looks good: no imagery anywhere above the fold; index and About feel bare.** Home tablet and desktop: rows are text plus a mostly empty right column; About desktop has a dead right third. Blocked on owner media, but the designer can reduce the emptiness now: on desktop About, move the Skills block beside the intro (two columns) so the page does not read half-finished when the portrait is absent.
3. **Major, Robustness/Performance: 38 wixstatic references across 9 project pages, About and projects still hotlinked** (counts: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, landing 2, others 1). LCP and image weight are outside the owner's control, there is no width/height, and a Wix change silently blanks the site; the JS drop-out hides the symptom. Owner must supply a media folder (resized WebP, with dimensions). Source: https://web.dev/articles/optimize-lcp
4. **Major, SEO: meta descriptions on several pages are thin.** Hasselhoff: "A fun game using a submarine to navigate to and land on a target." says nothing about who or what (no 99 s, no STM32, no BLDC thrusters) and "fun game" undersells an engineering project. Rewrite every project description (about 120-155 chars) around the concrete fact already on the page: e.g. "Mini submarine with four BLDC thrusters, an STM32 and a joystick remote; the user has 99 seconds to land on an IR target." Check the other eight pages for the same pattern. Source: https://developers.google.com/search/docs/appearance/snippet (taste about exact length, but descriptive vs generic is a fact).
5. **Major, Fun: still one idea (stamps).** Ideas grounded in repo facts, not invented: (a) Hasselhoff stamp "TIME ALLOWED: 99 S" counts down only while pressed (:active), static under prefers-reduced-motion; designer declined three times as a gimmick, but it is the one joke the owner's own project invites. (b) Ledger "For the record" styled as a typed index card with slight misregistration. (c) The 404 is the only place with voice; give the pager or footer one plain aside tied to a real project (e.g. under Raftar: "40+ students, one podium"). Trade-off: keep 4.5:1 contrast and no motion for reduced-motion users.
6. **Major, UX: no "start here".** Nine rows are weighted equally, so a 30-second visitor must guess which is strongest. The data already implies an order: row 01 (snake robots, current lab work) and Raftar (podium) have the strongest facts. Owner decision which; recommendation: give the chosen row a larger title and a one-line "Best place to start" label, and break the even rhythm. This also reduces sameness (AI-tell). Designer has deferred as owner choice twice; ask the owner once, plainly, or pick row 01 by default since it matches the lede.
7. **Minor, Looks good: phone home scroll is long and uniform.** About 5700 px at 780 wide. Row 04, 05, 06 stamps stack under the blurb and the tag line sits below the stamp, so rows 04 to 06 are taller than others (ragged but not unattractive). Taste; consider putting the tag line on the same line as the index number to tighten rows on phone.
8. **Minor, Accessibility: untested text-spacing and 200 percent zoom.** SC 1.4.12 requires no loss of content when line height 1.5, letter spacing 0.12em, word spacing 0.16em are forced; stamps and the ledger have tight boxes and the sticky header is fixed height. The designer noted the test was never run. Run it and fix any clipping. https://www.w3.org/WAI/WCAG22/Understanding/
9. **Minor, SEO: robots.txt and sitemap live under /website/**, which crawlers do not read for a project site (robots only counts at host root). Sitemap is still useful if submitted in Search Console, or referenced from the root site if the owner has a `kmkar31.github.io` user site. Owner action.
10. **Minor, Performance: Google Fonts with preconnect but no fallback metrics, and no preload of the display font.** Risk of font-swap CLS on the h1. Self-hosting needs owner WOFF2 files; `size-adjust` fallback needs measured values. Not actionable in sandbox; keep listed so it is not lost.
11. **Minor, Content: About has a Skills section before Education and Experience.** For a recruiter the Seagate result (strongest quantified outcome) is below the fold on desktop, behind skills. Taste; consider Experience first, or at least link the Seagate marker (already linked from home to #seagate).
12. **Minor, Looks good: About right column empty on desktop even with the 760 px measure.** Same as finding 2; the timeline stays narrow while the skills grid spans 3 columns, giving two different widths on one page (rules end at 732 px, skills run to 918 px). Align them.
13. **Nit, Content: "Resume (PDF)" button on About and a text link on home, plus footer link; resume itself is a Wix-hosted file.** Three entry points to a single point of failure; fine until the file moves.
14. **Nit, Fun: "46 ORBITS TO TARGET" dashed stamp reads like an empty form field.** Taste; solid border, no dash.
15. **Nit, Content: no email.** Conscious owner choice; a professor may still expect one. Owner decision.

## Good, must not regress
- Plain specific home lede, the struck-through "three weeks" in an amber marker (home and About consistent).
- Ruled index with 01 to 09 numbers, double rules, ink footer, single hard-shadow button; no gradients, blur or glow.
- Varied stamps; 404 line; mono ledger; header Resume link on tablet and up; footer Resume on all pages.
- Unique titles, canonical, OG/Twitter, JSON-LD, sitemap lastmod, skip link, 44 px targets, scroll-padding-top for the sticky header, no overflow at any viewport, figure/portrait/caption drop-out, pager with one-line summaries.
- Dark theme as inverted print with legible muted text (verified on home tablet dark: stamps and rules hold up).

## Verdict
A coherent, honest, matte-print portfolio with a low AI-tell score (3/10) and no visual regressions this cycle; the generic openings and orphan captions flagged last time are gone. It is still tidy rather than memorable, and the biggest weaknesses are owner-supplied: status and dates (the page implies he is mid-degree in Oct 2026), outcomes, local media and the Wix dependency. Within the designer's reach now: rewrite thin meta descriptions (Hasselhoff first), tense-neutral About opening, align About's section widths and use the empty column, pick or ask for a "start here" row, run the text-spacing test, and add one earned interaction (the 99-second press state). Axes below 7: looks good 6, SEO 6, UX 6, fun 5, so findings 1 to 6 are Major.
