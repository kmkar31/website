# Critique, cycle 11 (2026-10-24)

Method: ran `tools/check.py` (13 pages x 3 viewports x 2 themes; all OK, only "images not loaded" sandbox notes). Viewed home phone light and desktop light, About desktop light, Projects tablet dark. Grepped titles, canonical, wixstatic counts. No site files edited.

Sources: WebFetch was blocked this run (permission request unanswered) for all three attempts, so these are unverified pointers, not fetched. No decision should rest on them alone.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- web.dev, Optimize CLS (web fonts): https://web.dev/articles/optimize-cls (blocked)
- NN/g, How users read on the web: https://www.nngroup.com/articles/how-users-read-on-the-web/ (blocked)
Topic this cycle: scanning and first-screen content, font-swap CLS, target size.

## Scores
AI-tell: **3 / 10** (unchanged). No gradients, glass, glow, slogans. Remaining tells: nine same-anatomy rows; warm cream/rust/amber "editorial" palette; hero order name, subtitle, lede, button, ledger, list. Authored: struck-through "three weeks", 99 s stamp, SpongeBob/Hasselhoff blurb, 404 line. Moved since cycle 10: nothing; the thumbnail collapse removed a broken look, not a tell.
Looks good: **6 / 10**. Type, rules and footer band are good; still no image anywhere above the fold, so first impression is a well-set text document. Projects page now collapses cleanly without thumbnails (cycle 10 fix verified in screenshot) but then is just home with filters.
SEO: **7 / 10**. Unique titles, descriptions, canonical, JSON-LD, sitemap. Gaps: media hotlinks (LCP/weight), robots.txt location, home title "Robotics and Controls Engineer" is a claim not stated on the site.
UX: **6 / 10**. Identity, resume and LinkedIn are findable on phone. No status, no start-here.
Fun and personality: **5 / 10**. Stamps only; nothing responds to touch.

## Owner critique (user-critique.md)
- Retro matte: honoured (flat, one hard shadow, double rules, ink footer). Taste: grain is almost invisible in the screenshots.
- Not AI-looking: honoured at 3/10. Residual risk is sameness and absence of first-person voice, not any effect.

## Findings, ranked

1. **Major, Credibility/UX: no current status (owner-only).** Today is 2026-10-24; About says MS 2023 - 2025 and home has no status line (STATUS slot empty). A recruiter cannot tell whether he has graduated or is available. One owner answer fixes it: graduated or enrolled, where now, open to roles. Not fixable by the designer.
2. **Major, Looks good: no imagery above the fold.** Home desktop and phone show no robot, satellite or car; the About right two-fifths is empty (portrait failed to load and collapsed, intro stays at ~38em with a large void to the right on desktop). Until media exists, make the void deliberate: move the Skills block beside the intro on desktop, or widen the intro. Taste on layout; measured fact that the right of About is blank.
3. **Major, Robustness/Performance: 31 wixstatic references remain** (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, one each on about, argus, projects, raftar, snake) plus the Wix resume. Outage or hotlink block means no figures and a dead resume link, which is the single most important file. No local copies, no dimensions. Owner must supply a media folder and the resume PDF.
4. **Major, UX: no "start here" project.** Nine equal rows; a 30-second visitor guesses. Deferred five times. Default recommendation: give row 01 (matches the lede, Biorobotics Lab) a larger title and a "Start here" mono label, or row 04 for the podium. It also breaks the even rhythm, which is the main remaining AI tell.
5. **Major, Fun: one idea only.** Stamps are good, three rows have them, none respond to touch. Grounded, nothing invented: (a) Hasselhoff "TIME ALLOWED: 99 S" stamp counts down only while pressed (:active or JS), static under prefers-reduced-motion; (b) ledger set as a typed index card with a slightly off-register heading; (c) one plain aside in the pager. Trade-off: keep 4.5:1 contrast and no motion for reduced-motion users. This has been declined as "taste" repeatedly; the axis score below 7 makes it a standing Major.
6. **Minor, Content/SEO: home title says "Robotics and Controls Engineer"** while the page itself says MS student. Either say "MS student" or use a descriptor already on the site. Also "Karthik Karumanchi | ..." puts the name first, fine.
7. **Minor, Looks good: phone home is a ~5700 px even scroll.** Rows with stamps (04, 05, 06) are taller because the stamp wraps above the tag line, and the Raftar and aerobraking stamps wrap to two lines on desktop and tablet ("PODIUM, FORMULA / BHARAT 2023"). Shorten to "PODIUM, FORMULA BHARAT" is not an option without losing the fact; widen the column slightly (about 200px) so each stamp fits one line.
8. **Minor, UX: Projects duplicates home.** Same nine blurbs and order; Projects adds filter buttons only. With no thumbnails (broken state) the pages are nearly identical. Either give Projects a different job (grouped by topic) or drop the list from home to the top three after the start-here pick.
9. **Minor, Content: About order.** Skills (generic list) come before Education and Experience; the strongest fact, 3 weeks to 15 minutes, is the last section. Taste; Experience first is the usual reading order for hiring managers.
10. **Minor, SEO: robots.txt and sitemap sit under /website/**, where crawlers do not read robots.txt on a project site. Owner: submit sitemap in Search Console.
11. **Minor, Performance: Google Fonts without size-adjusted fallbacks** (swap CLS risk on the h1). Needs owner WOFF2 to self-host. Source pointer (blocked): web.dev/articles/optimize-cls.
12. **Minor, Looks good: filter buttons are the only boxes on Projects** and the gap between the h1/filters and the first row (about 60px) is bigger than between rows; fine, but the "All" active state in dark theme (cream block) is the heaviest object on the page and competes with the title. Taste.
13. **Nit, Content: Hasselhoff "Source Code" is a bare "GitHub repo" link** with no context. Needs owner facts.
14. **Nit, Accessibility: stamps sit inside the home row link name**, so the accessible name ends "Podium, Formula Bharat 2023". Probably fine; verify with a screen reader.
15. **Nit, Looks good: nav "Resume" arrow is a text glyph next to LinkedIn and GitHub icons**; spacing between the text link and icons is uneven on desktop. Minor polish.

## Good, do not regress
- Plain intro with the struck-through "three weeks" marker; "For the record" ledger.
- Project pages lead with the large tl;dr, then facts; pager shows neighbour summaries.
- Concrete meta descriptions and unique titles; canonical, OG, JSON-LD, sitemap lastmod; 404 noindex with voice ("failed to land on the target").
- Retro system: flat surfaces, hard shadow on the primary button only, double rules, ink footer, inverted dark theme, no gradient or blur.
- Failed thumbnails, figures and portrait collapse cleanly; scroll-padding under sticky header; text-spacing test passed.
- Footer carries resume and LinkedIn on every page.

## Verdict
The site is coherent, honest and does not read as generated; the retro direction is committed to and cycle 10's broken-thumbnail fix holds. What caps it is content only the owner can give: a status line, locally hosted images and resume, and a chosen starting project. The designer can still act on three things without new facts: a "Start here" row (default row 01), one earned interaction (the 99 s press), and making the blank right side of About and the wrapped stamps look intentional. Until media arrives the ceiling is about 6 on looks and UX.
