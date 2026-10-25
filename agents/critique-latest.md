# Critique, 2026-10-25 (after cycle 14)

## Sources
My WebFetch call (w3.org SC 2.5.8) was blocked by the permission layer, and I have no search tool in this run. I therefore did not read any source this cycle. The pointers below are from memory and are UNVERIFIED; no finding depends on them. Findings rest on what I measured and saw.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum) and SC 2.4.11 Focus Not Obscured: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev font best practices (self-host, preload, fallback metrics): https://web.dev/articles/font-best-practices
- MDN `<details>` element (disclosure affordance, accessibility): https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details
- Topic not covered in earlier cycles: disclosure widgets and staleness of dates (credibility). Earlier cycles covered fonts, contrast, tap targets, SEO basics.

Measured: `python3 tools/check.py . agents/shots` ran 13 pages x 3 viewports x 2 themes, all OK (no overflow, tap-target, contrast, alt or h1 failures; 1 to 10 Wix images "not loaded", sandbox). Repo checks: every page still hotlinks wixstatic/filesusr (2 to 9 matches per page, 404 included). `STATUS = ""` in build/build.py. Fonts still load from the Google Fonts stylesheet. assets/ holds only og.png, site.js, style.css. 8 `rel="noopener"` on home. 13 unique titles, sitemap has 12 URLs, robots.txt present. The live site returned 403 to curl from the sandbox proxy, so I could not check it live. I looked at: home phone light and desktop light, About desktop dark, Hasselhoff phone light, Projects tablet light.

## Scores
- AI-tell: 3/10 (unchanged from last cycle). Moved this cycle: the Start-here row now carries a plate, so row 01 is no longer anatomically identical to rows 02 to 09 (small improvement, would be 2.5 if the plate showed a snake). Not moved: cream paper, serif, terracotta and mono labels is still the "tasteful editorial" template, and rows 02 to 09 are identical title / blurb / index / tag rows. Specific, authored things: the struck-through "three weeks", the 99 s stamp, Fig. N plates with sheet tags, the 404 joke, "Pin-puller for a 3U CubeSat, 2022".
- Looks good: 6/10. Home is calm and aligned, and the phone first screen is strong. But there is still no photograph; project pages on phone are plate then walls of serif prose; About on desktop has a hollow right column (about 1000 px of empty space below the "On this page" box); the new collapsed-details bar on Hasselhoff looks unfinished (finding 5).
- SEO: 7/10. Unique titles, descriptions, canonical, OG/Twitter, local absolute og.png, JSON-LD, sitemap, 404 noindex all present. Weak: render-blocking third-party font CSS, hotlinked media means alt text describes images that may vanish, text-only og.png, robots.txt cannot work on a project subpath. Cannot verify offline: live Wix media, Search Console submission, live headers.
- UX: 6/10. Name, field, strongest project, resume and LinkedIn are all on the first phone screen. Misses: the site's time claims look stale (finding 2), resume is a third-party URL, contact is LinkedIn only, no outcome statements on most projects.
- Fun and personality: 6/10. Plates, stamps and the 99 s press counter are earned. The remaining 7 of 9 rows have no distinguishing moment; the 404 is still the only place with real voice.

## Owner critique (user-critique.md)
1. Retro, matte: met. Flat paper, ink rules, one hard-shadowed button, double rules, no blur, glow or gradient anywhere I looked. Dark theme is near-black with amber rather than paper-like; taste, not a fault. The collapsed-details bar (finding 5) is the one component that drifts toward "default browser widget with a border".
2. Not AI-looking: mostly met. Remaining risks: the palette/type kit and the uniform rows 02 to 09 (finding 6).

## Findings (ranked)

1. Major (robustness / UX). The resume PDF, the main call to action, is a hotlink to a Wix filesusr URL on every page (header, hero, About, every footer). It is the one thing a recruiter needs, and if Wix rotates the URL it fails silently on 13 pages. Fix: owner puts resume.pdf in assets/; designer changes one constant. Declined for 10+ cycles because the sandbox cannot fetch it; still the top risk. Not verifiable offline.

2. Major (UX / credibility). The site never says what Karthik is doing now, and its dates look stale. About says his Master's "is at Carnegie Mellon University (2023 - 2025)" and the Education entry says "2023 - 2025"; today is 25 Oct 2026. A reader cannot tell if he has graduated, is still enrolled, or is available, and the tense-neutral rewording hides the question rather than answering it. The hidden STATUS slot exists. Needs one owner sentence (graduated? where now? open to roles?). The designer must not invent it, but it should be named in the owner-facing summary as the highest-value content gap.

3. Major (looks good, score 6). No photograph or real result image on any page; every Wix figure drops out on failure, so project pages on phone read as plate then prose. For a robotics portfolio the first expectation is to see the robot. The plates are authored and honest but schematic. Fix needs owner media (one image per project in assets/ with real width/height). Until then, the cheapest authored change that needs no new facts: give the plates a second measured element drawn from facts already on each page.

4. Major (performance / SEO). Google Fonts is still a render-blocking third-party stylesheet (index.html), with no fallback-metric tuning. Self-hosting two WOFF2 files with `font-display: swap` plus preload is the standard fix (web.dev, unverified link). Blocked by the sandbox; owner to supply the files. Preconnect already present.

5. Major (looks good / UX, new this cycle). The `details.impl` disclosure on Hasselhoff (phone) reads "Implementation detail: design and state machine" in bold mono, wrapped on two lines, between a heavy top rule and a hairline. There is no visible marker (triangle or +/-), so it reads as a heading, not as something to open. This is the only place the mono bold weight is used as a button label, and it is visually louder than the Testing section above it. Why it matters: undiscoverable disclosure hides content (MDN, unverified); it also looks unfinished. Fix: keep the native element, add a visible marker via `summary::before` ("+" / "-" in the tan accent), set the label to normal-weight serif or the 12 px mono label style used elsewhere, shorten it to "Design and state machine (open)" so it stays on one line at 390 px. Check the same component on any other page that uses it.

6. Major (AI-tell, kit). Rows 02 to 09 on home and Projects are identical in anatomy (title, blurb, index, tag); the only variation is stamps on three rows. A human-made index would let the uneven facts set the layout. Alternative using existing facts only: show the same plate thumbnail on every row (all local and cannot fail) at the row's right edge on desktop, or drop it for all and keep row 01 plain; as it stands, one plate on one row reads as a "featured card", a template pattern. Also the Start-here plate on phone is a plain zigzag line with circles and a dashed arrow; it does not say "snake" and could be any signal. Add a caption-sized label or draw module links so it is recognisable.

7. Minor (looks good). About desktop: the 760 px column plus the "On this page" box leave a large empty right side from Skills downward in both themes; it reads as a plain CV. Authored option: set the dates (2023 - 2025, May - Aug 2024) in a left margin column on desktop only so the page uses its width, as in a printed CV. Taste; the designer has declined this as a large rewrite, which is fair, but the void is measurable (right 28% of the frame empty for roughly 2000 px).

8. Minor (UX). Contact is LinkedIn only. The owner has set the no-public-email constraint, so this is flagged only; consider whether the owner will approve a non-scraped alternative.

9. Minor (UX). Home and Projects now show the same nine rows with only filters and thumbnails differing. A visitor who clicks "See the projects" gets a page that looks like the one they left. Suggestion: on home show Start here plus the three stamped rows and link "All nine projects"; that also shortens the phone home page (roughly 6000 px tall). Taste/IA; the designer has argued the opposite, so label it a judgment call.

10. Minor (SEO). og.png is text only (40 KB). A social card carrying one plate would be more distinctive in link previews and is repo-local. Owner can verify the card in a share preview; I could not offline.

11. Minor (robustness). Nine pages' worth of Wix hotlinks plus `.thumb` images on Projects (9 not loaded in sandbox) mean the page's LCP/CLS behaviour with real images is unknown: no width/height attributes were found for the Wix figures (designer states dimensions unknown). Risk of layout shift when images arrive late; cannot be measured offline.

12. Minor (a11y / readability). The 12 px mono labels ("FOR THE RECORD", "START HERE", tags) pass the automated contrast check but are small on the grainy paper ground; the tags (muted tan on cream) are the weakest. Taste; raise tags to 13 px or darken one step.

13. Nit (fun). Most of the nine pages have no personality beyond the plate. The designer rejects extra gags as "taste" and nothing is invented; I accept it unless the owner asks. One idea grounded in facts already present: a small printed "colophon" line on each plate sheet is already there; leave it.

14. Nit (a11y). Check that the pressable Hasselhoff stamp is reachable by keyboard and announces its state change; I did not verify this from the screenshots.

15. Nit (content). The Hasselhoff page lead and the row blurb no longer repeat the joke (good); but the page still has "THE QUESTION" repeating what the lead already says ("How do we develop a submarine for underwater target detection?"). It is owner/original wording; leave.

## Good, do not regress
- Struck-through "three weeks" in a marker highlight (home and About).
- Fig. N plates with sheet tags and honest "not to scale" captions; they are repo-local and cannot hotlink-fail.
- Two stamp types only; the pressable 99 s stamp.
- Plain lede with real specifics, no slogans; the "For the record" ledger with the pin-puller line.
- Phone first screen: name, one-sentence field, resume and LinkedIn visible without scrolling.
- Failed-image collapse for figures, captions, thumbnails and the portrait; no empty boxes in any screenshot.
- Double rules, flat surfaces, hard-shadow button; no gradients, blur or glow.

## Verdict
The site has an authored point of view (print-era plates, stamps, a real-fact lede) and no longer reads as a generated template; the remaining AI-tell is the cream/serif/terracotta kit and nine same-shaped rows. It is not yet a good portfolio for a 30-second reader, for reasons the designer cannot fix alone: the resume is a third-party link, nothing says what he is doing now while the dates read as stale (it is October 2026 and the Master's is listed as 2023 - 2025), and there is not one photograph. Within the designer's reach: the new Hasselhoff disclosure needs a visible marker and a shorter label; row 01's plate should say "snake" and the rows should be treated consistently; and the About page should use its width. Scores: AI-tell 3, looks good 6, SEO 7, UX 6, fun 6.
