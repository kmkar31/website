# Critique, cycle 10 (2026-10-24)

Method: ran `tools/check.py` (13 pages x 3 viewports x 2 themes; all OK, only "images not loaded" sandbox notes). Viewed home phone light and desktop light, About desktop dark, Hasselhoff phone light, Projects tablet dark. Grepped meta descriptions, wixstatic counts, thumbnail markup. No site files edited.

Sources: WebSearch/WebFetch were not used this run, so these are unverified pointers, not fetched:
- WCAG 2.2 SC 1.1.1 Non-text Content, SC 1.4.12 Text Spacing: https://www.w3.org/WAI/WCAG22/Understanding/
- web.dev, Optimize LCP / CLS: https://web.dev/articles/optimize-lcp , https://web.dev/articles/optimize-cls
- Google Search Central, snippets and title links: https://developers.google.com/search/docs/appearance/snippet
- NN/g, how users read on the web: https://www.nngroup.com/articles/how-users-read-on-the-web/
- NN/g, portfolio/hiring usability pointers (credibility, current info): https://www.nngroup.com/articles/
Topic this cycle: failure states of hotlinked media, stale-content credibility, snippet quality for list pages.

## Scores
AI-tell: **3 / 10** (unchanged). No gradients, glass, glow or slogan copy. Remaining tells: nine same-anatomy rows; warm cream/rust/amber editorial palette; hero order of name, subtitle, lede, button, ledger, list. Authored: struck-through "three weeks", the 99 s stamp, the SpongeBob/Hasselhoff blurb, the 404 line. Moved: nothing new this cycle; cycle 9 removed no tell and added none.
Looks good: **6 / 10**. Type and rules are good, but the home page is still text only and the Projects page shows broken-image boxes (finding 2).
SEO: **7 / 10**. Unique titles and now concrete descriptions on 11 of 13 pages; canonical, OG, JSON-LD, sitemap. Gaps: projects.html and 404 descriptions, hotlinking.
UX: **6 / 10**. Identity and contact are clear on phone; no status, no start-here.
Fun and personality: **5 / 10**. Stamps only.

## Owner critique (user-critique.md)
- Retro matte: honoured (flat, hard shadow on one button, grain faint). Taste: grain is nearly invisible in screenshots; a bit more would sell the paper.
- Not AI-looking: honoured at 3/10. Residual risk is sameness and no first-person voice, not any effect.

## Findings, ranked

1. **Major, Robustness/Looks good: Projects page shows broken-image boxes when Wix fails.** projects.html tablet dark (and every viewport): all nine 96x72 thumbnails render the browser's broken-image icon in a bordered box. The cycle 4 drop-out logic hides failed figures on project pages but not these thumbnails, and they have `alt=""` so there is no text fallback. Today the Wix files may fail in the sandbox only, but this is exactly what a Wix outage or hotlink block looks like to a recruiter, and the page looks unfinished. Fix: apply the same onerror/complete check to `.thumb img` and collapse the thumb column (the row grid must not leave a 96px hole). Source: WCAG 1.1.1, https://www.w3.org/WAI/WCAG22/Understanding/
2. **Major, Credibility/UX: status and dates are stale or absent (owner-only).** Today is 2026-10-24; About shows MS 2023 - 2025 and home has no status (STATUS slot still empty). Reads as either abandoned or graduated-and-hidden. Cycle 9 made the wording tense-neutral, which is honest, but a visitor still cannot tell if he is available. Ask the owner once: graduated or enrolled, where now, open to roles or not. Source: NN/g on credibility and current information.
3. **Major, Robustness/Performance: 31 wixstatic references remain** (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, one each on about, argus, projects, raftar, snake) plus the Wix resume. No local copy, no real dimensions, LCP and weight outside the owner's control. Owner must supply a media folder. https://web.dev/articles/optimize-lcp
4. **Major, Looks good: no image on home or About above the fold, so the first impression is a text document.** Desktop home has a good ledger, but the page never shows a robot, satellite or car. With images blocked the About right third is empty too. Not fixable without media; until then the designer can at least make the empty right side of About deliberate (e.g. place the Skills block or a short "Currently" slot there).
5. **Major, UX: no "start here" project.** Nine equal rows; a 30-second visitor must guess. Deferred three times as an owner choice. Recommendation: pick row 01 (it matches the lede: Biorobotics Lab) or Raftar (podium) and give it a larger title plus a "Start here" label, which also breaks the even rhythm (AI-tell). If the owner does not answer, default to row 01.
6. **Major, Fun: one idea only (stamps).** Stamps are good but every row now has one or none, and nothing responds to touch. Grounded ideas, nothing invented: (a) Hasselhoff "TIME ALLOWED: 99 S" counts down only while held (:active), static under prefers-reduced-motion; (b) ledger set as a typed index card with a slightly off-register heading; (c) a plain aside in the pager copy. Declined repeatedly as a gimmick, but it carries meaning (the project's own 99 s rule). Trade-off: keep contrast 4.5:1 and no motion for reduced-motion users.
7. **Minor, Content: Hasselhoff page repeats itself.** Phone: the large tl;dr ("A mini submarine named after David Hasselhoff's cameo ... 99 seconds to land on the target"), then the question line, then the first body paragraph ("The Hasselhoff Bot is a small submarine inspired by ... In the movie, SpongeBob ...") covers the same joke a third time before any engineering. Move the movie story below Design Methodology or trim it to one sentence.
8. **Minor, SEO: projects.html description is generic** ("Projects by Karthik Karumanchi at Carnegie Mellon University and IIT Madras"), and 404 says "Page not found". Rewrite projects to name the nine topics (snake robots, quadrotor landing, aerobraking, tethered satellites, Formula SAE car). Add noindex to 404 if not already. https://developers.google.com/search/docs/appearance/snippet
9. **Minor, SEO/UX: projects.html duplicates home.** Home is already the full index with the same nine blurbs; Projects adds filters and thumbnails. Two near-identical pages compete for the same query and cost a click. Either make Projects the thumbnail/filter view with different framing or point the home "Projects" heading at it.
10. **Minor, Looks good: phone home is a 5700 px even scroll.** Rows 04 to 06 are taller because the stamp stacks above the tag line. Taste; put index number, stamp and tag on one flowing line on phone.
11. **Minor, Content: About order.** Skills precede Education and Experience; the strongest quantified fact (Seagate 3 weeks to 15 minutes) is the last section on desktop. Taste; consider Experience first.
12. **Minor, SEO: robots.txt and sitemap sit under /website/**, which crawlers do not read as robots.txt on a project site. Owner: submit sitemap in Search Console.
13. **Minor, Performance: Google Fonts without fallback metrics** (font-swap CLS on the h1). Needs owner WOFF2 files to self-host; keep listed. https://web.dev/articles/optimize-cls
14. **Nit, Content: "Source Code" section on Hasselhoff is a bare "GitHub repo" link** with no context (what is in it, language). Nit unless the owner supplies facts.
15. **Nit, Accessibility: stamps are decorative rotated bordered text**; confirm screen readers read them in sensible order (they are inside the link name on home rows, so each row's accessible name now ends in "Podium, Formula Bharat 2023"). Probably fine; verify with a screen reader.

## Good, do not regress
- Plain intro with the struck-through "three weeks" marker; the "For the record" ledger.
- Project pages lead with the large tl;dr, then facts, then sections; pager shows neighbour summaries.
- Concrete meta descriptions on the nine project pages; unique titles; canonical, OG, JSON-LD, sitemap lastmod.
- Retro system: flat surfaces, hard shadow only on the primary button, double rules, ink footer, inverted dark theme, no gradient or blur anywhere.
- Failed figures and portrait drop out cleanly on project pages and About; scroll-padding under the sticky header; text-spacing test passed.
- 404 voice ("failed to land on the target").

## Verdict
The site is coherent, honest and no longer reads as generated; the retro direction is committed to. What holds it back is not craft but content that only the owner can supply: a current status line, real images served locally, and a chosen starting project. The one thing the designer can fix now is the broken thumbnail state on Projects (finding 1), then the redundant Hasselhoff opening, the Projects description, and one earned interaction (the 99 s press). Until media arrives the ceiling is about 6 on looks and UX.
