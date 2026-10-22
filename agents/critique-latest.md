# Critique, 2026-10-22 (cycle 2, after the plain-index home and ruled-rows pass)

## Scores
- **AI-tell score: 3/10** (was 5). Home is now a plain intro plus ruled index, which is a real authored move. Remaining tells: the DM Serif + Plex + Source Serif "print revival" kit, uniform ruled rows with identical anatomy, and copy that is accurate but evenly polished.
- **Looks good: 6/10.** Home reads as a calm printed index, and the double rule masthead is good. But it is bare: no image anywhere above the fold, the right 40% of the desktop intro is empty, the project rows are nine identical text rows, and project pages on phone are long walls of prose with broken image boxes. (Wix images are blocked in the sandbox, so I judge layout only; web fonts also fall back to Times here, so headline type is judged from CSS only.)
- **SEO and discoverability: 4/10.** No `sitemap.xml`, no `robots.txt`, no JSON-LD anywhere, og:image is a Wix URL, no `og:url`/`og:site_name`/twitter:title, no `width`/`height` on images, meta description on the home page is the old Wix sentence. Titles, canonicals, one h1 per page and landmarks are fine.
- **UX: 6/10.** Who, where and the resume are findable on home in 3 seconds. But contact is "No public email" plus LinkedIn, the strongest project is not signposted, and project pages have no outcome up top.
- **Fun and personality: 3/10.** Tidy, honest, and dull. One flat button shadow is the only tactile moment.

Tells that moved since last cycle: stats strip, 3-card focus block, card grid, hero band, scroll reveal, uniform boxes: all gone. Remaining: type kit; "X that Y" blurbs ("A PPO agent trained to choose...", "A tricycle for riders with..."); identical row anatomy; tidy triplets in lede ("designing, building and racing").

## Method and limits
- `tools/check.py` ran on all 13 pages x 3 viewports x 2 themes: no failures reported, only "images not loaded" notes. Viewed: index (desktop light, phone light), quadrotor-sysid (phone dark), about (tablet light). Not every screenshot was opened.
- WebFetch to w3.org and web.dev was refused again (permission not answered), and the one web search returned only secondary blogs. The sources below are pointers cited from memory, NOT verified this cycle:
  - Google Search Central, structured data (Person, ProfilePage): https://developers.google.com/search/docs/appearance/structured-data/profile-page
  - Google Search Central, sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
  - Open Graph protocol: https://ogp.me/
  - web.dev, Optimize CLS (image dimensions): https://web.dev/articles/optimize-cls
  - WCAG 2.2 SC 1.4.12 Text Spacing / 1.4.8 line length guidance: https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
  - NN/g, portfolio and hiring-manager scanning: https://www.nngroup.com/articles/portfolios/
  - (Topic varied from cycle 1: SEO/social cards, structured data, content strategy.)

## Owner critique items
1. **Retro matte theme.** Now largely honored: paper tones, double rules, hairlines, hard shadow only on the primary button, dark theme as inverted print. Still short: grain is barely visible; the whole site is one beige field with no second surface or accent block, so "matte print" reads as "plain". A printed page has ink colour moments (a spot-colour rule, a rubber-stamp, an index mark). See finding 6.
2. **No AI-generated look.** Mostly met (3/10). Remaining risk is the font kit and uniform rows; see findings 5 and 9.

## Ranked findings

### 1. No structured data, sitemap or robots; weak social card (Major, SEO)
Where: repo root and every `<head>`. There is no `sitemap.xml`, `robots.txt` or JSON-LD. og:image on every page is a hotlinked Wix URL; no `og:url`, `og:site_name`, `twitter:title/description/image`. Home meta description is a Wix leftover ("Master's Student ... specializing in Robotics and Controls").
Why: a recruiter searching the name, or pasting the link in Slack or LinkedIn, gets a weak card and no rich result; Wix dependency can break the card. See Google structured-data docs (unverified).
Fix: add `sitemap.xml` and `robots.txt` (with Sitemap line); `Person` JSON-LD on home/about (name, alumniOf CMU and IIT Madras, sameAs LinkedIn and GitHub, url); `CreativeWork` per project; a local 1200x630 og:image; per-page `og:url`; rewrite the home description to say what he does in plain words. Have `build/build.py` emit all of it so it stays in sync.

### 2. Everything visual is still hotlinked from Wix; no image dimensions (Major, robustness/CLS)
Where: all project pages (about 50 images), About portrait, resume PDF, og:image. Phone screenshot of sysid shows 9 broken-image boxes stacked; in production without dimensions each will push content when it loads.
Why: one Wix plan lapse removes all pictures, the portrait and the resume together. Missing `width`/`height` risks CLS (web.dev, unverified).
Fix: owner to supply the media; then host in `assets/img/`, WebP, width/height on every `<img>`. If the owner cannot, at minimum copy the resume PDF into the repo (the single most-clicked asset). Not fixable in the sandbox (403 on wixstatic); keep it open until the owner acts.

### 3. Dates are stale and the tense is wrong (Major, credibility)
Where: `about.html` Education "2023 - 2025", `index.html` lede ("I research compliant control"), About ("I'm pursuing a Master's ... I'm also taking courses"). Today is October 2026.
Why: a recruiter reads either "graduated and never updated the site" or "overstayed". A 30-second visitor cannot tell whether he is a student or available. This is the most damaging accuracy issue on the site.
Fix: owner to confirm status. Then either "MS, graduated May 2025" with current role/location, or the true expected date. Add a one-line status near the name ("Graduated CMU 2025. Open to controls and robotics roles." only if true). Do not invent it.

### 4. Home gives no signal of the best project or a real outcome (Major, UX)
Where: `index.html`, all viewports. Nine equal rows; the order is not explained; the first row (snake robots) is the least documented and its blurb is circular ("Gait-based control for modular snake robots ... aimed at...").
Why: NN/g-style scanning guidance (unverified) is to lead with the strongest two or three pieces. Here the Seagate result (3 weeks to 15 minutes) is the best number on the site and is not tied to any project page.
Fix: pick 3 featured rows (owner chooses) and set them with a heavier rule and a one-line outcome; leave the rest as a plain list under "Also". Rewrite the snake blurb with the concrete thing done. Link the Seagate sentence to a short About anchor.

### 5. Project pages open with a question and textbook background; results still thin (Major, content/UX)
Where: `quadrotor-sysid.html` phone and desktop; same pattern on others. The "fact list" holds "Unknowns: 4 coefficients" and "Tests: hover and sinusoidal rotation", which are method labels, not results. Two long background paragraphs sit before any figure or finding. The rhetorical `.question` ("How do we build accurate yet lightweight...") plus `.tldr` repeat the same idea three times above the fold.
Why: a professor wants the problem, the method and the number. Role, dates, team size and outcome are the standard fields and are absent (owner to supply; not invented).
Fix: drop `.question` where it duplicates `.tldr`; add a "Role / When / Team / Result" row filled only with owner-confirmed facts; collapse Background under a `<details>` or move it after the figures. Until media exists, alt text appears as a broken-image link in a box; set `alt` text that is also a good caption.

### 6. Retro commitment is thin: one colour field, no second surface (Major, looks good, taste)
Where: all pages. Everything sits on the same beige; the only colour is rust on button, links and dates. The grain is invisible at normal zoom. There is no tactile detail beyond one button shadow. Dark mode is competent but the light theme is the whole identity.
Fix (taste): a spot-colour rule or a solid ink band for the masthead date line ("Vol." style issue line: CMU, Pittsburgh, year); use the amber `--hi` as a marker highlight on key numbers ("3 weeks to 15 minutes"); give filter buttons and project-row hover a printed "press" state (shadow drops to 0 and the row shifts 2px). Keep contrast; do not add boxes back around prose.

### 7. Desktop home leaves the right 40% of the intro empty and has no image (Minor to Major, looks good)
Where: `index.html` desktop. The lede column is about 650px of a 1000px frame with nothing beside it, then a long list. No picture of him or his work on home; the portrait lives only on About (and is broken in the sandbox).
Fix: put one real working photo or a project figure (snake robot, racecar) in the right column at a fixed aspect ratio with a single hairline border and a printed-style caption ("Figure 1. ..."). Needs owner media; otherwise tighten the measure and leave it.

### 8. Contact path is weak (Major, UX)
Where: footer on every page: "No public email. LinkedIn is the best way to reach me." Header has icon-only LinkedIn and GitHub links.
Why: stated deliberately by the owner, so not a bug, but the sentence reads as a refusal and is the last thing on every page. Icon-only links have `aria-label` (good) but no visible words.
Fix: phrase positively ("Reach me on LinkedIn"), put a visible "Contact" text link in the header nav pointing at it, and consider a `mailto` or form-forward address if the owner changes his mind. Taste/owner decision.

### 9. Type and row anatomy are consistent to the point of sameness (Minor, AI tell, taste)
Where: site-wide. DM Serif Display headings, mono tags, uniform 3-line row pattern and uniform hairline rules; the About skills list is eleven identical rows with no grouping.
Fix: vary the ledger: set year or category as a left-hand column on desktop ("2025 / Space"), group skills under three plain labels (Control, Space, Build/Tools), let one featured row run larger. A faint irregularity is more human than perfect rhythm.

### 10. Copy still has the generated cadence in places (Minor, AI tell)
Where: home blurbs "A X that Y" form in about six rows; "designed, built and raced"; About "push forward technological autonomy" (owner-approved original wording, so not changed; but it is the one slogan on the site).
Fix: write two blurbs in first person with a plain detail ("I tuned the MPC horizon until the quadrotor stopped chasing the Tumbller's wobble" only if true). Only from facts in the repo; ask the owner for anecdotes.

### 11. Fun and personality are nearly absent (Major, axis 4 = 3/10)
Concrete ideas using facts already in the repo (all optional, taste):
- Hasselhoff Submarine has a 99-second landing game: make the 404 page a "99 seconds" joke ("This page failed to land on the IR target. Back to the index.") rather than a generic message.
- Seagate: render "3 weeks" struck through next to "15 minutes" in the lede, as a proofreader's mark.
- Footer colophon: "Set in DM Serif Display and Source Serif 4. No framework. One stylesheet." (true and plain; it is the print-shop signature).
- Pager: label "Next" as "Next in the index" with a hand-set pointing rule.
Trade-off: any strike-through or marker highlight must keep 4.5:1 contrast and remain readable without colour.

### 12. Google Fonts dependency and font-display (Minor, performance/privacy)
Where: every `<head>`. Four families, one third-party request chain. `display=swap` is set (good). Fallback is Georgia/Times, so the headline will visibly jump on slow networks.
Fix: self-host WOFF2 subsets of DM Serif Display and Source Serif 4 with `size-adjust` fallback, drop IBM Plex Sans (used for UI only) in favour of system-ui to cut a family.

### 13. Line length and text size on project pages (Minor)
Where: sysid page on desktop. 18px serif at a narrow column is comfortable; on phone the page is about 7,300px tall mainly because of prose before figures. Fix with finding 5, not by shrinking type.

### 14. Lightbox and filter are fine but untested without images (Nit)
Where: `assets/site.js`. Lightbox traps Tab by always refocusing close, which is correct for a single-control dialog. With broken images (current state) the zoom link shows a broken-image icon; consider `alt` plus a visible "View full size" text fallback. No change needed once media is local.

### 15. Footer repeats the same block on every page (Nit)
The double rule plus "No public email" on a 404 page is fine; on the 404 the next action ("Go to projects") should be the first link, which it is. Leave.

## Good, do not regress
- Plain ruled index on home, with specific blurbs (CrazyFlie on a Tumbller, 99 seconds, 500 m tether, four unknown constants). These are authored and specific.
- Real, concrete lede facts (Biorobotics, Choset, Formula Bharat, Seagate 3 weeks to 15 minutes), no slogan.
- Double-rule masthead and footer; hairline vs heavy rules as the only structure.
- Hard shadow reserved for one primary button; no gradients, blur, glow or reveal animation.
- One h1 per page, skip link, 44px targets, `aria-pressed` filters, canonical links, links that work without JS, distinct alt text.
- Dark theme as inverted print.
- Honest limits (no invented numbers; resume as a text link).

## Verdict
The cycle-1 skeleton problem is solved: the home page now reads like a person's index, and the AI-tell score drops to 3. What remains is not decoration but gaps that only the owner can close: stale dates (finding 3), all media and the resume living on Wix (2), and missing role/outcome data on projects (5). On the designer's side, the biggest open work is discoverability (sitemap, robots, JSON-LD, local og:image, a rewritten description), a signposted "best three" on home, and a few earned retro touches (spot-colour marker, press states, a 99-second 404) so the site has a point of view as well as good manners. Research this cycle could not be verified (fetches refused); treat the links as pointers.
