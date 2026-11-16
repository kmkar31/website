# Critique, 2026-11-16 (cycle 147)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc=0, no FAIL, only "images not loaded, sandbox network" notes; it needs more than 2 minutes). I looked at index phone-light and desktop-light, aerobraking phone-dark, projects tablet-light and quadrotor-sysid phone-light. Repo checks: resume link target, font loading, JSON-LD types, robots/sitemap, tap-target CSS, wixstatic count (unchanged). No site files edited.

## Sources consulted
Web fetches for these three were blocked in this run (permission request unanswered), so none was read this cycle. I cite them for the principle only and no finding depends on a quotation from them:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (WCAG 2.2 SC 2.5.8, 24 CSS px minimum). Used to confirm that the 44px targets in assets/style.css pass with margin.
- https://web.dev/articles/optimize-lcp (render-blocking CSS and resource load delay). Applied to finding 6.
- https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt (robots.txt belongs at the host root). Applied to finding 9; the designer already declined it as a host limit.
Topic this cycle: third-party dependencies and resilience, tap targets, robots location. Last cycle covered image dimensions and case studies. Honest caveat: with sources unread, treat the web-practice basis as unverified; the repo facts below are verified.

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, chip layers, stats strip or card trio. Moved since last cycle: nothing. Residual tells: identical project-page skeleton; the footer line "Set in DM Serif Display and Source Serif 4" names a pairing that is a common template choice (taste). Per the rules, "would look identical with name swapped": no, because of the stamps and the 99 s/500 m facts.
- Looks good: 8/10, unchanged. Desktop-light has a clear hierarchy and rhythm. Held back by the ragged right column on Home (rows 01, 02, 03, 08, 09 have no stamp, while 04 to 07 do) and by long, unbroken text on sysid and aerobraking (phone), where the Background and Setup sections run as plain paragraphs with no figure for hundreds of pixels.
- SEO: 7/10, unchanged. Unique title and description, canonical, OG, JSON-LD (Person, CreativeWork), sitemap, robots, one h1 on index. Held back by Wix hotlinks without dimensions, one shared OG card, robots/sitemap under a subpath, and no JSON-LD ProfilePage or sameAs check done this cycle.
- UX: 6/10, unchanged. Name, school, Resume, LinkedIn are in the first phone screen. Still no status or dates, and the Resume PDF is hosted on filesusr.com (Wix), see finding 4. Below 7, so Major.
- Fun and personality: 7/10, unchanged. Strike-through, stamps, "Time allowed: 99 s", 404 joke, press states. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, double rules, one hard offset shadow, flat dark theme (aerobraking phone-dark stays matte).
2. Must not look AI-generated: met. Caveat (taste): repeated page skeleton, and the Home page is a tidy ruled list that is slightly template-regular.

## Ranked findings
1. Major (UX, credibility). No status or dates. Index phone-light says "MS Mechanical Engineering, Carnegie Mellon University" with no years; About gives a closed range and today is 2026-11-16. The lede is in present tense ("I research"). Owner fact needed (graduated or not, availability). `STATUS = ""` in build/build.py is ready for it.
2. Major (UX, content). Two answers to "strongest project". Row 01 (snake) leads Home but has the thinnest page; only row 06 carries START HERE. Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page copies the structure and numbers of cited work (Falcone et al.) without saying what Karthik did. The Raftar "Ferrari" comparison has no source. Owner source or cut.
4. Major (robustness, UX). The Resume PDF, the single most-clicked asset for a recruiter, is hotlinked to a Wix file host (`...filesusr.com/ugd/84da68_6a1c...pdf`) from three places on Home alone, plus About and footer. If the Wix account lapses, every Resume link dies and the site has no fallback. Fix needs the PDF file: add `assets/resume.pdf` and point all links at it. Same dependency applies to about 30 Wix images.
5. Major (performance, robustness). About 30 Wix images with no width/height (snake-robots.html line 55 etc.), so layout shift is possible and a Wix outage blanks project pages. Needs owner files or sizes; guessing aspect ratios is correctly avoided.
6. Minor (performance, consistency). Fonts load from Google Fonts: a render-blocking stylesheet from a third origin, yet the footer boasts "one stylesheet, no framework". It is a privacy and resilience dependency too. Self-hosting two WOFF2 files would remove it; needs the font files (owner or designer can download under OFL). `display=swap` is already set, so this is low severity.
7. Minor (visual). Ragged Home right column (see Looks good). The rule "stamp only where a real number exists" is right; accept it or find real numbers for rows 02, 03, 08, 09.
8. Minor (content). Nine projects with no tiering on Home; NN/g advice is 3 to 5 strong ones. Owner decision, causes finding 2.
9. Minor (SEO). robots.txt and sitemap.xml sit under /website/, but crawlers read robots.txt only at the host root. Host limit; the sitemap is still discoverable through Search Console. One shared OG card for all 12 pages.
10. Minor (content). Tricycle page is passive voice and has no subheads. Owner call on who did what.
11. Minor (UX). Contact is LinkedIn only; the footer says so. Owner constraint, noted not pressed.
12. Nit (visual, taste). About desktop leaves the right third empty and skills are 5/3/3.
13. Nit (process). Cycles 139 to 146 declined the same owner-fact items; further design-only cycles will mostly repeat.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadow on one button, flat dark theme.
- Specific copy: "three weeks" struck to "15 minutes", "Time allowed: 99 s", "46 orbits to target", "500 m of tether", the plain "For the record" ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, 44px targets throughout the CSS, comfortable measure.
- Filter buttons and numbered rows with press states; 404 joke; per-page JSON-LD, canonical, OG; reduced-motion block; focus ring.
- Drawn figure plates ("Fig. 1 - Orbits", "Sheet 8 of 9 - NTS") instead of stock imagery; previous/next pager on project pages.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7. UX stays under 7 because of facts only the owner can supply (status line, lead project, snake result, aerobraking contribution, Ferrari source). The new robustness point is that the Resume PDF itself lives on Wix: one local `assets/resume.pdf` would remove the biggest single dependency, ahead of the images. Until the owner supplies those items, designer cycles have little left to fix except optionally self-hosting the two fonts.
