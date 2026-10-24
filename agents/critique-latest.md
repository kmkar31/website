# Critique, 2026-10-24 (after cycle 13)

## Sources
WebSearch returned titles and URLs only. WebFetch was not used, so I did not read the pages and treat these as pointers, not verified quotes.
- https://web.dev/articles/font-best-practices and https://web.dev/learn/performance/optimize-web-fonts (self-host, preload, font-display, fallback metrics)
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast (SC 1.4.11, used for the stamp and tag contrast checks)
- https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (what hiring managers look for; secondary, UX-slanted, so low weight)
- NN/g portfolio advice: only a search listing was returned, nothing opened.
Findings rest on what I measured and saw.

Measured: `tools/check.py` ran across 13 pages x 3 viewports x 2 themes with no failures. Each page reports 1 to 10 images "not loaded" (sandbox, expected). I looked at home (phone light, desktop light), Hasselhoff (phone dark), About (desktop light) and Projects (tablet dark). Repo grep: every page still hotlinks wixstatic/filesusr (2 to 9 matches each). The resume PDF is a filesusr URL on home, About, header and every footer. `STATUS = ""` in build/build.py:247. Fonts come from the googleapis.com stylesheet. assets/ holds og.png, site.js and style.css only.

## Scores
- AI-tell: 3/10 (unchanged). The Fig. N / "Sheet 5 of 9 . NTS" plates are an authored idea. The stamps (99 s, 46 orbits, podium) and the struck-through "three weeks" are specific. What is left is the kit: cream paper, serif, terracotta and mono labels is the standard "tasteful editorial" template. The home list is uniform title / blurb / index / tag rows. The "For the record" ledger reads as a template device. Nothing moved this cycle. Tethered plate and sheet tags are a small move toward authorship.
- Looks good: 6/10. Home is calm, aligned and well set. Project pages now open well. But there is no photograph anywhere and every project body is a wall of text. Hasselhoff phone shows four long text sections with no figure after the plate (the Wix figures are dropped when they fail). About on desktop has a hollow right column below the "On this page" box, and its sections sit at 760 px in a 1050 px frame.
- SEO: 7/10. Titles, descriptions, canonical, OG/Twitter, local og.png, JSON-LD, sitemap are present. Weak: render-blocking Google Fonts, hotlinked media (so alt text indexes nothing useful), og.png is text only, robots.txt is unusable on a subpath. Cannot verify offline: the live Wix media and PDF, and Search Console submission.
- UX: 6/10. Name, field, Start here, resume and LinkedIn all fit on the first phone screen. Misses: no status or date line while the site says CMU 2023 to 2025 and today is Oct 2026; contact is LinkedIn only; resume depends on a third-party URL; no result or role statements for most projects.
- Fun and personality: 6/10. The plates and the 99 s stamp are good. The rest is a tidy resume; the 404 joke is the one place with real voice.

## Owner critique (user-critique.md)
1. Retro, matte: met. Flat paper, ink rules, one hard-shadowed button, no blur or gradient. Grain is nearly invisible, which is acceptable. The dark theme is a different mood (near-black with amber), so it is less "paper"; taste, not a fault.
2. Not AI-looking: mostly met. The remaining risk is the kit and row uniformity (finding 6).

## Findings (ranked)

1. Major (robustness / UX). The resume PDF, the site's main call to action, is still a hotlink to a Wix filesusr URL on every page. If Wix moves or expires it, the one thing a recruiter wants dies silently, and nobody will see it. Fix: owner puts resume.pdf in assets/ and the designer links it. This has been declined for 10+ cycles because of the sandbox; it is still the top risk. Not verifiable offline.

2. Major (UX / credibility). No status or date. The site says MS 2023-2025 and today is Oct 2026, so a recruiter cannot tell whether he is a student, a graduate, or available. The ledger already has a hidden STATUS slot. The designer cannot invent it. Needs one owner sentence.

3. Major (looks good, score 6). There is no photograph and no real result image on any page; all the media are Wix hotlinks that drop out on failure. For a robotics portfolio, "show the robot" is the first expectation. The plates cover for it but are schematic. Fix (owner media): one image per project into assets/ with true width/height. Until then, give the plate a second, differently shaped element so pages are not text, plate, text (e.g. a measured-values table drawn as a "Table 1" with the facts already on the page).

4. Major (performance / SEO). Google Fonts is a render-blocking third-party stylesheet and there are no fallback metrics. Self-hosting two WOFF2 files with `font-display: swap` and a preload is the standard fix (web.dev font best practices). Blocked only by the sandbox. Owner action: download the files into assets/fonts and the designer wires them in. Interim, no download needed: add `<link rel="preconnect">` for fonts.gstatic.com if absent.

5. Major (UX, score 6). Project pages are long and still do not answer "what did you do and what happened". Hasselhoff on phone is a long run of prose (User Experience, Design Methodology, State Machine, Testing). Rewriting the whole thing would invent facts, but the existing sections can be reduced: collapse State Machine Logic and Design Methodology under `<details>` ("Implementation detail") so the page is scannable in 30 seconds and the Testing result is closer to the top. No JS needed, and the content stays indexable.

6. Major (AI-tell, kit). Home is a ruled list where every row has the same anatomy, plus the "For the record" ledger, which duplicates facts in the lede (Seagate, internships). Human alternative: break uniformity where the facts are uneven. Give Start-here row 01 a taller treatment with its plate thumbnail (the plates are local and cannot fail), so the first project has an image on the home page. This is the single cheapest way to get a visual on the front page.

7. Minor (looks good). About desktop: below "On this page" the right column is empty for 1400 px, and the 760 px column leaves the page left-weighted. Taste, but the About page reads as a plain CV. An authored fix: set the Education and Experience dates in a left margin column (a ledger) so the page uses its width.

8. Minor (UX). Contact is LinkedIn only and the footer says so plainly. That is honest but a dead end for a professor who does not use LinkedIn. This is a hard owner constraint (no public email), so only flag it: consider a mailto-obfuscated or form-less alternative the owner approves.

9. Minor (a11y). Muted tags and mono labels on the paper ground (about 10 to 11 px mono at low contrast, e.g. "FOR THE RECORD", "ON THIS PAGE") pass the automated check but are small. Taste; raise to 12 px where it costs nothing.

10. Minor (SEO). og.png is text only. A social card carrying one plate would be more distinctive in a link preview and is repo-local.

11. Minor (UX). Header: the Resume link and icons crowd the nav on tablet (Home, About, Projects, then Resume, in, GitHub, theme at 820 px). No overflow, but the nav links and utility links have almost equal weight. Separate them with a rule.

12. Nit (fun). Hasselhoff is the only page with a delightful touch. A comparable one for each of two other projects, taken from facts on the pages (the 46-orbit run, the 500 m tether), would carry the plates' idea. Owner-only decision whether to add more; the designer has declined these three times as "taste", which I accept unless the owner asks.

13. Nit (content). "Hasselhoff's cameo in the SpongeBob Movie" appears on both the row blurb and the page lead; the repeated joke is fine once.

14. Nit (robustness). Image-failure handling hides figures and captions. If the Wix host dies, the pages become text and plates. That degrades gracefully, but confirm that no page then contains a sentence that refers to a missing figure ("left", "right") as Hasselhoff's caption does ("Hasselhoff submarine (left) and remote control (right)" still shows on phone with no image above it in the screenshot). Fix by hiding or rewording the orphaned caption.

15. Nit (SEO). Descriptive link text is good ("Resume (PDF)", "LinkedIn"). Add `rel="noopener"` where `target=_blank` is used (not verified in markup).

## Good, do not regress
- Struck-through "three weeks" in a marker highlight (home and About).
- Fig. N plates with sheet tags and honest "not to scale" captions.
- Stamps limited to two types; the pressable 99 s counter.
- Start here row, plain lede with real specifics, no slogans.
- 404 copy.
- Flat matte palette, hard shadows only on the primary button, dark theme with raised muted text.
- Pager showing the neighbour's first fact; footer band; no-JS figure links; Text-spacing test passed.
- Claims restricted to facts on the original site.

## Verdict
The site has moved from template to a recognizable point of view: it is quiet, specific and honest, and the plates and stamps are what a person remembers. It is held back by things only the owner can supply: a local resume, a status line, and photographs. Until those arrive it is a good-looking text resume with one clever device. The cheapest design-side gains now are a plate on the Start-here row, collapsing long implementation prose into `<details>`, and fixing orphaned captions. If the owner does not supply media in the next cycle, I will stop raising findings 1 to 4 and record them as owner blockers.
