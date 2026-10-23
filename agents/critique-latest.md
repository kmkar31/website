# Critique, cycle 4 (2026-10-23)

Rendered with `tools/check.py` (all pages, phone/tablet/desktop, light/dark): zero automated failures. I looked at home (desktop light, phone light), About (desktop dark), snake-robots (phone dark). External media is blocked in the sandbox, so broken images are not counted as bugs; the hotlink dependency is.

Sources: I had no live web access this cycle (search/fetch tools unavailable), so the references below are standards and guidance I know, cited by URL but NOT re-fetched. Treat them as unverified pointers.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/TR/WCAG22/#target-size-minimum
- WCAG 2.2 SC 1.4.3 Contrast, 2.4.7 Focus Visible: https://www.w3.org/TR/WCAG22/
- web.dev, Optimize LCP / CLS and image dimensions: https://web.dev/articles/optimize-lcp , https://web.dev/articles/optimize-cls
- web.dev, Best practices for fonts (self-hosting, font-display): https://web.dev/articles/font-best-practices
- Google Search Central, robots.txt must live at the host root: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Google Search Central, Person / structured data guidance: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- NN/g, how recruiters/hiring managers read portfolios and "F-pattern" scanning: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ and their writing on credibility signals (dates, specifics).

## Scores

AI-tell score: **3 / 10** (was ~5 implied after cycle 1). The stock layout is gone: no stats strip, no card trio, no gradient, no blobs, no glass. The ruled index, the struck-through "three weeks" marker, the mono "For the record" ledger and the 99-second 404 read as authored. What still reads as template: (a) every project row has the identical anatomy of title, two-line blurb, index, tag pair, with no row ever breaking pattern; (b) the paper palette plus DM Serif Display plus terracotta button plus amber highlight is a very current "warm editorial" template look; (c) the dark theme is a near-black brown with amber links, which is the stock "dark mode of the warm theme". Moved since last cycle: stats strip and "What I work on" (gone), slogan About line (gone), uniform rows (partly, via index numbers and varied blurbs), footer band (added, good).

| Axis | Score | One-line evidence |
|---|---|---|
| Looks good | **6** | Home and About are calm and well set, but there is not one image anywhere in the first 3 seconds, About desktop leaves a dead right half, project pages are walls of text plus broken-image boxes. |
| SEO | **6** | Meta, canonical, OG, JSON-LD, sitemap all present; but robots.txt is at a path crawlers ignore, Google Fonts and Wix hotlinks hurt LCP/CLS, images have no width/height. |
| UX | **6** | Contact and resume are findable, rows are scannable; but dates are stale, resume is a Wix hotlink, no email, and the strongest project is not distinguished. |
| Fun / personality | **6** | The strike-through and 404 are real; nothing else is. Hasselhoff, the tumbler robot and the 99-second brief are unexploited. |

Four axes at 6 each: each gets a Major finding below.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like: **mostly met.** Flat surfaces, hard offset shadow only on the primary button, double rules, ink footer band, faint grain. Drift risk: none toward glossy. Remaining gap is that it is retro in palette and rules but not in content structure (no colophon-like marginalia, no specimen-style captions, no real printed-object details). Fine, but see finding 8.
2. Must not look AI-generated: see AI-tell score above. Honest answer: the layout no longer does; the remaining tell is sameness plus an absence of visible human specifics (no photo, no first-person asides, nothing uneven). A site with no images and no voice reads generated even when the CSS is hand-set.

## Findings, ranked

**1. Major (UX/credibility). Dates and status are stale and contradict "today".** Today is 2026-10-23; About lists "MS Mechanical Engineering 2023 to 2025" and home says "I research" in present tense. A recruiter reading this cannot tell if he has graduated, is job-hunting, or is still a student; that is the first question a hiring manager has. Both agent cycles have deferred this to the owner, correctly not inventing facts, but it remains the single biggest credibility gap. Action for owner: state current status (graduated or not, availability, where now). Designer: reserve a one-line status slot in the ledger ("Status: ...") ready for the fact, and do not claim anything until supplied. Source: NN/g on credibility and currency of information.

**2. Major (Looks good / UX). No imagery in the first screen and project pages open on broken figures.** Home desktop and phone have zero visual proof of work; project rows are text-only. On phone, snake-robots shows three bordered alt-text boxes where the media should be (environment limit, but also the real failure mode if Wix ever drops them). For a robotics portfolio, a person scanning 30 seconds wants to see a robot. Owner must supply a media folder (images and a few stills of videos). Until then, designer could set text-first project pages to not render empty bordered boxes when an image errors (`onerror` hide, or reserve aspect ratio with a caption) so the page degrades into a clean text page.

**3. Major (Performance/SEO/robustness). All media, the resume PDF and portrait are hotlinked from Wix (11 pages reference wixstatic/filesusr).** Single point of failure, no `width`/`height` on figures (CLS risk, web.dev), no `loading="lazy"`/`decoding` hints visible, no modern formats. A resume link that rots is the worst possible failure on a job-seeking page. Reopening because the designer's blocker (sandbox 403) is an environment fact, not a site fix: the owner must drop files into `assets/`. Until then, add `loading="lazy"` and an explicit `aspect-ratio` per figure so layout cannot jump, and verify the resume link from the owner's machine.

**4. Major (SEO). robots.txt is at `/website/robots.txt`.** Crawlers only read `/robots.txt` at the host root (kmkar31.github.io/robots.txt), which this project site cannot control; the file here is ignored. Harmless since it only allows, but the sitemap line in it will not be discovered that way. Fix: submit sitemap.xml in Search Console / Bing Webmaster and drop the pretense that robots.txt does anything (or keep it, but do not count it). Also consider a custom domain, which fixes the root issue and gives a cleaner URL. Source: Google Search Central robots.txt intro.

**5. Major (Fun / personality). The strongest personality is hidden.** Facts already in the repo that nobody sees on the first pass: the submarine is named after David Hasselhoff's cameo; the brief gave 99 seconds to land on target; the quadrotor lands on a balancing Tumbller; the 46-orbit result. Only the 404 uses the 99 seconds. Concrete, factual ideas in the print direction:
- On the Hasselhoff page, set the 99 seconds as a stamped "TIME ALLOWED: 99 s" in the fact list (it is a real constraint), plus a plain dry caption about the cameo.
- Replace tag pair "Robotics / Build" on one or two rows with a rubber-stamp style outlined label for a real status ("Podium, Formula Bharat 2023") so rows stop being identical.
- A press state on rows that shifts 2px with the hard shadow (already partly there); add the same to the "See the projects" button only if not already (verify).
Trade-off: motion-based fun must respect `prefers-reduced-motion` (rule at style.css:177 exists); prefer static, typographic jokes.

**6. Major (Looks good). About desktop is unbalanced.** At 1366 the text column is about 280px wide with the portrait box floating far right at about 160px width, leaving large dead margins either side while the first paragraph is narrow and tall; skills are then a single narrow column of one-word rows, and the whole About reads as a long thin strip. The h1 "About" sits over empty space. Suggest: let the two intro paragraphs run at the 60-65ch measure beside the portrait on a two-column grid at 960px+, put skills in three columns (the three groups already exist), and keep the timeline column narrow. Source: reading comfort guidance (45-75 characters) is taste-adjacent; the dead space is measurable in the screenshot.

**7. Major (SEO/performance). Google Fonts are render-blocking third-party requests** (`preconnect` + stylesheet, `display=swap` is set, good) for two families. Cost: extra DNS/TLS, FOUT between serif fallbacks and DM Serif Display on the h1, and a privacy-ish dependency on a site that otherwise advertises "no framework". Self-host WOFF2 with `preload` on the display font and `size-adjust` fallbacks when files are available. Not downloadable in sandbox; owner/dev machine task. Source: web.dev font best practices.

**8. Minor (AI-tell). Every row is the same.** Same anatomy ×9 with the same index column. It is clean, but sameness is the remaining generated signature. Humans leave one row longer, one flagged "start here", and one with a single plain line. Suggest marking one project as the recommended first read (owner choice) with a stronger rule or short extra sentence, and promoting results (46 orbits, 40+ students, 500 m tether) to the row where they exist.

**9. Minor (UX). No obvious "best project" and no direct email.** A professor or recruiter with 30 seconds gets nine equally weighted rows. Contact is LinkedIn only (owner decision, accepted); but the footer line "To get in touch, message me on LinkedIn" is reasonable. Reopen only to ask the owner to choose a featured project.

**10. Minor (Accessibility). Dark theme secondary text.** Blurb text on the dark about/project pages (grey-tan on near-black, e.g. org lines, pager summaries) looks dim in the screenshot; automated check passes at AA, so this is only taste. Consider raising blurb contrast to about 7:1 for long reading. Source: WCAG 1.4.3 and 1.4.6 (AAA).

**11. Minor (UX). Phone header and home.** Phone home is solid: headline first, tap targets 44px, no overflow. But the ledger "For the record" repeats the lede almost verbatim (Seagate 3 weeks to 15 minutes, podium, Biorobotics Lab appear in both). It reads as padding on phone where both stack. Trim the ledger on phone (hide) or give it facts not in the lede (courses, GPA, location), but only existing facts.

**12. Minor (SEO). Heading and schema detail.** Home h1 is the name only; the document title carries "Robotics and Controls Engineer". Fine. Person JSON-LD lacks `sameAs` verification only if LinkedIn/GitHub are not listed; confirm they are and add `alumniOf`/`affiliation` from existing facts. Cannot verify with Rich Results offline.

**13. Nit. Colophon says "No framework, one stylesheet."** It is accurate and charming but also a mild "look at me" line that a template would also add; keep, or replace with something only true of this site.

**14. Nit. Footer on phone** wraps the colophon across 3 lines of mono; shorten for phone.

**15. Nit. Lightbox markup is present on pages with no images** (home and About include an empty `.lightbox` dialog). Harmless; remove from pages that have no zoomable figures.

## Regressions check
None found. Cycle 3 changes (tldr lead, numbered index, ink footer, ledger, shared left edge) rendered correctly in all viewports; no overflow, no failing contrast, one h1 per page.

## Good, must not regress
- Ruled plain index with real, specific blurbs; no stats strip, cards, gradients, glass, glow.
- Struck-through "three weeks" in the amber marker, linked to About#seagate: the best authored detail on the site.
- Pager showing neighbour summaries; project pages leading with the one-sentence result.
- Ink footer band and the double-rule header; inverted-print dark theme consistency.
- 404 copy (99 seconds), focus-visible outline, skip link, accessible lightbox and filters, 44px tap targets.
- Honest content discipline: nothing invented; open items are flagged for the owner.

## Verdict
The site has genuinely left the AI-template look and has a coherent retro-print point of view; its remaining problems are not styling problems but missing human material. It has no photos, no current status, no voice beyond a few good lines, and its media and resume depend on a third party. Four scored axes at 6 means "competent and tidy," not yet "memorable." What the designer can still do alone: tidy About's layout, make image failure degrade gracefully with reserved aspect ratios, lazy loading, break the sameness of rows, and stage the Hasselhoff and 99-second facts as typographic jokes. What only the owner can do, and what will move the score most: supply current status and dates, a local media folder with the resume, one or two real photos of the robots, and pick the featured project.
