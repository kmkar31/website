# Critique, cycle 5 (2026-10-23)

Rendered with `tools/check.py` (13 pages, phone/tablet/desktop, light/dark): zero automated failures. I looked at home (desktop light, tablet dark, phone dark), About (desktop light), snake-robots (phone light). Wix media is blocked in the sandbox, so broken images are not counted as bugs; the hotlink dependency is (11 of 13 pages still reference wixstatic/filesusr).

Sources: WebFetch was blocked this cycle (permission not granted for web.dev, w3.org, MDN), and I did not run searches. The references below are cited by URL from prior knowledge and NOT re-fetched; treat them as unverified pointers. Topics this cycle, varied from last: CLS/image dimensions, target size, robots/sitemap on project sites, dark-mode design, hiring-manager scanning.
- web.dev, Optimize CLS (image dimensions, font swap shifts): https://web.dev/articles/optimize-cls
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), 1.4.3 Contrast, 2.4.11 Focus Not Obscured: https://www.w3.org/TR/WCAG22/
- web.dev, Font best practices: https://web.dev/articles/font-best-practices
- MDN, prefers-color-scheme (default to OS, offer override): https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
- NN/g, F-shaped reading pattern / how people scan: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
- Google Search Central, robots.txt intro: https://developers.google.com/search/docs/crawling-indexing/robots/intro

## Scores

AI-tell score: **3 / 10** (same as cycle 4; the lede/ledger/stamp changes helped, but see below). The stock layout is gone. Specific, authored things: struck-through "three weeks" in an amber marker, mono ledger, stamped labels ("Time allowed: 99 s"), Hasselhoff/SpongeBob blurb, the 99-second 404. Still reading as template: (a) the palette and type (cream paper, DM Serif Display, terracotta button, amber highlight, near-black brown dark mode) is the current "warm editorial" look; (b) the three stamps are the same rectangle in the same red, so they now form a second repeated pattern; (c) no photo, no first-person aside, nothing uneven or personal, so the site would look the same with another engineer's facts swapped in. Moved since cycle 4: uniform rows (improved, stamps), ledger repetition (fixed), About layout (fixed, three skill columns), dark muted text (raised).

| Axis | Score | Evidence |
|---|---|---|
| Looks good | **6** | Home is calm, well ruled and well set; but no image or visual proof of work anywhere above or below the fold, and the portrait/figures are broken boxes in render. First 3 seconds: a nicely typeset text page, nothing to remember. |
| SEO | **6** | Titles, meta, canonical, OG/Twitter, JSON-LD, sitemap all good. Gaps: robots.txt ineffective on a project path, no width/height on Wix images, Google Fonts third-party dependency, og.png is text only. |
| UX | **6** | Contact, resume and projects reachable on phone in one screen, tap targets pass. But status/dates stale, resume hotlinked to Wix, no featured project, no email. |
| Fun / personality | **6** | Stamps and strike-through are real; the stamps are decoration-plus-fact, fine. Nothing interactive or tactile beyond press states. |

Four axes at 6, so each has a Major finding below (1, 2, 3, 8).

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like: **met on surface.** Flat fills, ink rules, double rule under the header, hard shadow only on the primary button, ink footer band, faint grain, no gradients, blur or glow (I saw none in any screenshot). Dark mode is a coherent inverted print. Gap is depth, not drift: the retro is palette and rules, not printed-object details (see finding 8).
2. Must not look AI-generated: **mostly, with a caveat.** Layout and copy are plain and specific now. The remaining generated signature is the absence of a human: zero photos, zero first-person voice beyond the lede, and a very trend-current palette. I disagree that further hero tinkering helps; only real media and one or two personal specifics will move this number.

## Findings, ranked (taste is labelled)

**1. Major (Looks good / UX / AI-tell). No image of any kind on the site that actually loads from the repo.** Home desktop and phone: text only. About desktop: the portrait slot renders as a wide empty bordered box with alt text (environment-caused, but the box is the full 220px column, so if Wix drops the file the right of About is a labelled hole). A robotics portfolio is judged on seeing the robot; NN/g scanning research says visual anchors are what people fix on first. Action for owner: supply a media folder (one still per project plus the portrait, ideally with true dimensions). Designer, meanwhile: the broken-figure fallback already drops figures; do the same for the portrait (collapse the column and let the intro run full width when the image fails).

**2. Major (UX / credibility). Status and dates are still stale.** Today is 2026-10-23; About says "MS ... 2023 to 2025" and home says "I research ... " in present tense. A recruiter cannot tell whether he has graduated, is available, or where he works now. The `STATUS` slot exists in build.py but is empty, so nothing renders. Owner must supply one line ("Graduated May 2025; now at ..." or "Seeking ..."). Until then, consider changing "I research" to a tense that does not assert current enrolment? Only the owner can say; do not invent.

**3. Major (Fun / personality). Fun is typographic only; no earned interactive moment.** The Hasselhoff 99-second brief is stamped but never played with. Ideas grounded in repo facts, no invented content: (a) on the Hasselhoff page, set the 99 seconds as a printed "Time allowed" ticket and, on hover/focus of a single ">" link, nothing animated, just a dry caption about the cameo; (b) a "see also" crosslink between the quadrotor landing and sysid pages ("same quadrotor family, different problem") only if the facts support it; (c) give the 404's 99-second joke a second use in the footer colophon. Trade-off: keep everything static or reduced-motion safe; do not add decorative motion (AI-tell).

**4. Major (Performance / SEO / robustness). All media and the resume are Wix hotlinks.** No `width`/`height` on figure images means layout shift when they load (web.dev CLS guidance), and a single resume link rotting is the worst failure on a job-seeking page. Designer cannot download them from the sandbox (still true). Reopened only to say: set a CSS `aspect-ratio` per figure (e.g. 4/3) on `.fig img` so slots cannot jump even without dimensions, and verify the resume URL from the owner's machine. Owner: drop files into `assets/` and the build can switch paths.

**5. Major (SEO). robots.txt at `/website/robots.txt` is ignored by crawlers** (must be host root). Not a defect to fix in repo; owner action: submit sitemap.xml in Google Search Console / Bing Webmaster, or use a custom domain (also gives a clean URL). Google Search Central robots intro.

**6. Minor (AI-tell, taste). Stamps are now their own template.** Three identical dark-red outlined rectangles with the same mono caps. Humans vary a stamp: a slight rotation (about -1.5 degrees) on only one, a different ink (amber on the Hasselhoff one), a double-border on the podium. Do not rotate on phone if it breaks text; keep contrast at 4.5:1 or better.

**7. Minor (UX). No chosen "start here" project.** Nine rows with equal weight; a professor with 30 seconds does not know which to open. Owner choice; the only evidence in the repo for strength is snake robots (his current research, row 01), so row 01 already acts as the default, but nothing says so. A short "Start here" tag on the owner's chosen row would help.

**8. Minor (Looks good, taste). Home first screen has a heavy empty band.** Desktop: ledger sits in a 270px right column with the lede at about 650px, which is good, but between the Projects rows and the footer there is a very tall bare gap (about 90px) and the projects list's right column (index + tags) is 150px wide with the blurb running to about 920px, which leaves the tag column floating. Fine on phone. Suggest tightening the rule spacing, or aligning tags to the title baseline. Low priority.

**9. Minor (Performance / SEO). Google Fonts two families.** `preconnect` + stylesheet, `display=swap` present (good). Cost: third-party request, fallback-to-DM-Serif swap on the h1 (CLS). Self-host WOFF2 with `size-adjust` fallback when files are available. Owner/dev-machine task. web.dev font best practices.

**10. Minor (Accessibility). Dark-theme muted text is better but still dim at long length** (project blurbs, pager summaries). Passes AA in checks; at about 7:1 reading would be more comfortable. Taste-adjacent (WCAG 1.4.6 is AAA).

**11. Minor (UX). Two "Resume" paths with different wording** ("Resume (PDF)" on home, "Download resume (PDF)" on About). Fine, but both point to Wix; keep wording identical, and mention file size if known.

**12. Nit (SEO). Home meta description is 190+ characters** and will truncate in results (about 155-160 shown). Trim to the control-of-robots-and-spacecraft clause plus CMU.

**13. Nit (Content). "Read more about modular snake robots here."** (snake page): non-descriptive link text "here". Use the target's name. Also the snake page is a short fact list plus one paragraph; the page reads thin next to the others (taste/content, owner to supply results).

## Good and must not regress
- Ruled index with numbered rows and varied stamps; hairline/heavy/double rule vocabulary.
- Struck-through "three weeks" in marker highlight; "For the record" ledger (now non-repeating).
- Project pages leading with the tldr, "The question" demoted, previous/next pager with one-line summaries.
- Flat retro surfaces, hard shadow only on the primary button, no gradients/blur/glow; coherent inverted-print dark theme.
- About: three skill columns, full-width header edge, readable measure.
- Graceful broken-image fallback, 404 copy, skip link, 44px targets, canonical/OG/JSON-LD/sitemap, aria-pressed filters.
- Copy that sticks to facts present on the original site.

## Verdict
The site no longer looks generated: the layout is a plain, ruled, print-style index with a few specific, funny and honest details, and the automated checks are clean. What holds it at 6 on every axis is not CSS but content the designer cannot invent: no photographs or stills, no current status or dates, and media/resume still on Wix. Until the owner supplies a media folder, a status line, and a chosen "start here" project, further design passes will have diminishing returns; the best remaining design-only work is making broken or missing media collapse cleanly (portrait included), reserving aspect ratios, varying the stamps so they are not a second template, and giving the Hasselhoff page one static, dry, specific joke grounded in the 99-second brief. External sources this cycle were not re-fetched (access blocked), so the citations are pointers only.
