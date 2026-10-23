# Cycle log

Newest entry at the bottom. The designer appends one entry per cycle.

## 2026-10-22: baseline (before cycle 1)
- Site recreated from the Wix original, redesigned (gradient hero, stats strip,
  project cards with tag filters, project pages with key results, timeline on
  About, light/dark toggle, scroll reveal, lightbox).
- Mobile pass done: one-row sticky header, headline before portrait, 44px tap
  targets, static blobs on phones, reveal safety net.
- Known open items for the critic to evaluate: images and resume still hotlinked
  from Wix (media zips in Google Drive were not found by the connector);
  embedded videos and report PDFs from the Wix project pages are missing; no
  contact email by design; hero headline and focus-area copy are rewrites that
  the owner should confirm; no real photo/alt review yet; typography web fonts
  load from Google Fonts.
- Facts available for copy (from the original site only): CMU MS ME 2023-2025,
  GPA 4.0; IIT Madras B.Tech 2019-2023, GPA 9.3/10; Biorobotics Lab with Prof.
  Howie Choset; Raftar Formula Racing captain, RFR23 suspension and brakes,
  podium at Formula Bharat 2023; Seagate intern (3 weeks to 15 minutes, 30
  drives); York University MITACS intern; Tube Investments intern; nine
  projects as listed on the site.

## 2026-10-22: direction change from the owner
- Owner wants a retro matte theme and no AI-generated look. Critic now scores an
  "AI-tell score" each cycle; designer brief carries the direction.
- First retro matte pass applied by hand: warm paper palette, DM Serif Display
  + IBM Plex, flat components with ink borders and hard shadows, gradients,
  blobs, glass blur, pulse dot and floating badges removed, plainer hero copy.

## 2026-10-22: cycle 1 response (designer)
Fixed:
- 1 Home is now a plain index: short intro in running text (Biorobotics, Formula Bharat, Seagate 3 wk to 15 min, GPA), then ruled project rows. Stats strip, "9 projects", and "What I work on" block removed.
- 3 Boxes and hard shadows reserved for the primary button and filter buttons. Timeline, results, pager, projects are ruled text with hairline/heavy/double rules. Double rule under header and above footer. Dark theme is now inverted print: tan ink rules, shadows darker than paper.
- 4 (partly) Results box is now a plain fact list; label-only entries replaced with factual context (lab, advisor, tests). Sysid page now opens with the objective, background moved below. Snake and other duplicate alt text made distinct.
- 6 Dark theme reworked (above). Kept the toggle.
- 7 Body is Source Serif 4; sans only for UI; mono only for dates/tags/captions. Eyebrow removed. Chips replaced by plain "A / B" tags.
- 8 Portrait removed from home; About keeps it with a single 1px border.
- 9 Card blurbs rewritten with specifics taken from the project pages.
- 10 Footer says plainly there is no public email; duplicate resume button removed (resume is a text link on home and a button on About).
- 11 One primary button, resume as text link.
- 12 Scroll reveal removed (CSS, JS, classes).
- 13 Titles are full project names; canonical link added on every page.
- 14 Figure images are links to the full image (work without JS, focusable); lightbox is a modal dialog with focus moved in and returned; filters have aria-pressed and a live count. Zoom links have a 44px minimum height.
- 15 Square serif favicon.
- Grain raised from 7% to 16% alpha (still faint).
Declined / not possible:
- 2 Local images, WebP, width/height, local og:image and resume: the sandbox proxy returns 403 for wixstatic, so nothing can be downloaded and true dimensions are unknown. Project-list thumbnails now have fixed 96x72 boxes so they cannot shift layout. Needs owner to supply a media folder.
- 4 (rest) Role, dates, team size and new outcome numbers: not on the original site; not invented. Owner to supply.
- 5 Videos and report PDFs: not available; owner to supply.
- 9 About line "push forward technological autonomy" kept: original-site wording. "40+" and "less fuel" are on the original project text.
- Critic's cited references were unverified and were not relied on.
Next attack if I were the critic: still all Wix hotlinks; project pages still lead with a question and long prose; Google Fonts dependency; sameness of the 9 rows; no real outcomes for several projects.

## 2026-10-22: cycle 2 response (designer)
Fixed:
- 1 Added sitemap.xml and robots.txt (emitted by build.py); Person JSON-LD on home and About, CreativeWork on each project; og:url, og:site_name, twitter:title/description/image, og:image dimensions on every page; home description rewritten in plain words; og:image is now a local assets/og.png (made by tools/make_og.py, text only).
- 4 (part) Snake blurb rewritten with the concrete thing done (from About text). The Seagate sentence now links to About#seagate, set as a marker highlight (6, 11).
- 6 Amber marker highlight on the Seagate result (dark ink on amber, underlined so it does not rely on colour); press states on rows and filters.
- 8 Footer reads "To get in touch, message me on LinkedIn." instead of a refusal.
- 9 Skills grouped under three plain labels (Control and learning, Analysis, Build and software).
- 11 404 now says "This page failed to land on the target" (99-second game); footer colophon (fonts, no framework, one stylesheet; true).
Declined:
- 2 Local images, resume copy, image width/height: wixstatic is 403 in the sandbox, dimensions unknown, owner must supply media.
- 3 Dates and current status: only the owner can say; not invented.
- 4 (rest) Choosing featured projects: owner decision. 5 Role/When/Team/Result rows: facts not available. The .question is the original site's framing and the .tldr states the method, so both stay; Background reorder skipped because figures are broken until media is local.
- 7 Home image: needs owner media. 10 First-person anecdotes: need owner facts; About slogan is original wording.
- 8 Header Contact link: external link in nav would confuse; contact choice is the owner's.
- 12 Self-hosted fonts: cannot download WOFF2 in the sandbox. 13, 14, 15: no change needed.
Verification: tools/check.py all pages, 3 viewports, 2 themes, no failures.
Next attack: all media still on Wix, stale dates, project pages lack outcomes.

## 2026-10-23: cycle 3 response (designer)
Fixed:
- 3 Project pages now lead with the tldr (large serif); the question is demoted to a small "The question" line under it.
- 4 Rows carry mono index numbers 01 to 09 (fixed-width right column); footer is now a solid ink band (second surface, light and dark tokens).
- 5 Row blurbs rewritten in varied voice using only facts already on the project pages; "push forward technological autonomy" removed from About; GPA removed from the home lede (it stays in Education).
- 6 Home gets a mono "For the record" ledger beside the lede (Seagate, Formula Bharat, Biorobotics Lab; all existing facts). Stacks under the actions on phone.
- 7 Seagate figure now shows "three weeks" struck through inside the marker highlight; pager shows each neighbour's one-line summary instead of bare labels.
- 8 Header, footer and sections share one left edge on desktop.
- 9 About h1 sits in the 760px column; skills are one column; portrait nudged to the first line.
- 10 (part) Dropped IBM Plex Sans and Mono; UI and tags use system stacks (colophon is now accurate: two web fonts).
- 11 "Contact on LinkedIn" added to home actions.
- 12 Canonical, og:url and sitemap use the clean root for home; ItemList JSON-LD on projects.html.
Declined:
- 1 Status and dates: only the owner can say; still the top open item. Question for owner: graduated, or still enrolled, and where now?
- 2 Local media/resume, width/height: wixstatic and filesusr unreachable from the sandbox; owner must supply files.
- 3 (rest) Role/When/Result rows: no facts beyond those already shown; not invented.
- 7 (rest) Hasselhoff 99 s hover counter: JS gimmick with little payoff; "No email form" line: unverified claim.
- 10 (rest) Self-hosted WOFF2: cannot download in the sandbox.
- 12 (rest) robots.txt location: kept; harmless, sitemap should be submitted in Search Console.
- 13 Alt text: owner must say what each figure shows.
- Critic: "about the About slogan" accepted and removed.
Verification: tools/check.py all pages, 3 viewports, 2 themes, no failures; looked at home desktop, home phone dark, snake phone.
Next attack: still no images or voice (owner media needed); all rows still the same anatomy; status/dates.

## 2026-10-23: cycle 4 response (designer)
Fixed:
- 1 (part) Added an empty STATUS constant in build.py; it renders a "Status" line in the home ledger only once the owner supplies the fact. Nothing claimed meanwhile.
- 2/3 (part) Figures whose image fails to load now drop out (JS, plus a check for already-failed images); a row with no survivors collapses, captions stay. Images get decoding="async" (lazy was already set).
- 5 Stamped labels on three rows (Podium, Formula Bharat 2023; Time allowed: 99 s; 46 orbits to target), so rows stop being identical. Hasselhoff fact list shows "Time allowed 99 seconds" as a stamp. All values already on the site.
- 6 About: full-width header edge, intro at 38em beside a 280px portrait, skills in three columns (one on phone), timeline stays 760px.
- 10 Dark-theme muted text raised from #b8ab95 to #cdc1aa.
- 11 Ledger no longer repeats the lede: IIT Madras B.Tech 2023, internships, toolbox (all existing facts).
- 12 Person JSON-LD already has sameAs and alumniOf; no change.
- 13/14 Colophon shortened to "Set in DM Serif Display and Source Serif 4."
- 15 Lightbox markup only on pages with zoomable figures.
Declined:
- 1 (rest) Current status/dates: owner must supply (slot is ready).
- 2/3 (rest) Photos, local media, local resume, width/height: owner files needed; dimensions unknown.
- 4 robots.txt: a project site cannot serve host-root robots.txt; kept, harmless. Owner: submit sitemap.xml in Search Console.
- 7 Self-hosted fonts: no way to download WOFF2 in the sandbox.
- 8/9 Featured "start here" project: owner choice; stamps break row sameness meanwhile.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, no overflow, tap-target, contrast, alt or h1 failures; viewed About desktop, home desktop, Hasselhoff phone dark.
Next attack: still no photos or current status; palette still reads "warm editorial".

## 2026-10-23: cycle 5 response (designer)
Fixed:
- 1 (part) About portrait now collapses (column and image) when it fails to load, like figures do; intro runs at its normal measure.
- 6 Stamps varied: Podium gets a 4px double border and no tilt; Hasselhoff tilts the other way (+1.2 deg); aerobraking is dashed and flat. Same ink (contrast unchanged).
- 10 Dark-theme muted text raised from #cdc1aa to #d9cfba.
- 11 Resume wording identical ("Resume (PDF)") on home and About.
- 12 Home meta/OG description trimmed to about 140 characters.
- 13 "here" links replaced with named targets (CMU Biorobotics Lab research page; Raftar Formula Racing website).
Declined:
- 1 (rest), 4 (rest), 9: photos, local media, local resume, self-hosted fonts need owner files; sandbox cannot reach Wix. 
- 2 Status/dates: only the owner can say; STATUS slot still ready. Owner question stands: graduated or enrolled, and where now?
- 3 Hasselhoff joke/crosslink: the caption would be invented content; relation between quadrotor projects is not stated on the site. Static stamp and fact already carry it.
- 4 CSS aspect-ratio on figures: image ratios are unknown and vary (tall/narrow classes); a forced ratio would letterbox or crop real photos. Needs real dimensions.
- 5 robots.txt: host-root only; kept, owner should submit sitemap.xml in Search Console.
- 7 "Start here" tag: owner choice; row 01 is already first.
- 8 Tag column spacing: taste, low priority; tags align to title top on phone and desktop, no overflow.
Note: critic could not fetch its cited sources (WebFetch blocked); citations were treated as unverified pointers, and no decision here relied on them.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed About desktop light (portrait collapsed) and home phone dark (three distinct stamps).
Next attack: no photos or voice, status/dates, palette still "warm editorial".

## 2026-10-23: cycle 6 response (designer)
Fixed:
- 1 (part) snake-robots: figures first, then the generic field paragraph under a "Background" label, so the tl;dr and facts lead. Same on the other pages was already the case (Background label exists on sysid).
- 4b The "3 weeks to 15 minutes" bullet on About now uses the same struck-through marker as the home page.
- 8 (part) Hairline rule above each About section heading (a lighter printer's-rule separator). A glyph ornament was tried and removed: its background patch did not match the grain.
- 11 Cut the redundant "taking courses in robot learning and AI" sentence from About (courses stay under Education, no tense claim).
Declined:
- 1 (rest), 2, 5: photos, outcomes sentences, local media, local resume, image dimensions need owner files; owner must supply 2-3 sentences of "what I did and what happened" and one image per project. Nothing invented.
- 3 Status/dates: owner must supply one line (graduated or enrolled, available or not); STATUS slot ready.
- 4a/4c Hasselhoff ticket, footer joke: taste; the stamp already carries 99 seconds, and a new joke would be invented copy.
- 6 Home h1: name-only h1 is deliberate; the lede names robotics and controls.
- 7 Row tag column: taste; no overflow or alignment fault measured, tags align to the title top.
- 9 "Start here": owner choice.
- 10 Text-spacing test not run; no fixed-height text boxes in the CSS.
- 12 Self-hosted fonts: no WOFF2 download possible in sandbox. 13 robots.txt: owner submits sitemap in Search Console.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, no failures; viewed About desktop light.
Next attack: still no imagery, status, or first-person outcomes.

## 2026-10-23: cycle 7 response (designer)
Fixed:
- 4 sysid: "Background" moved after the final model so the tl;dr and tests lead; JS now hides a lead-in paragraph ending in ":" when the figure after it drops out (no dangling "obtained as:").
- 5 About title now "About Karthik Karumanchi: CMU MS, IIT Madras, Seagate intern"; Projects title names robotics, controls and space. Both only use facts already on the site.
- 7 Header "Resume" text link with arrow and sr-only note, tablet and up; hidden on phone (resume stays on home, footer area unchanged).
- 10 Home row blurbs now use the body ink colour; muted stays for tags.
- 11 Ledger "Before CMU" (repeated the lede) replaced by "Built: Pin-puller for a 3U CubeSat, 2022" (from About).
- 13 sitemap has lastmod from git commit date.
Declined:
- 1, 2, 3: status/outcomes, imagery, local media, image width/height: owner-only. Wix file names do not encode dimensions. Nothing invented.
- 6 Hasselhoff 99 s press countdown and index-card restyle: new gimmick with no owner request; the stamp already carries 99 s. Taste.
- 8 Dead desktop column / dotted leaders: tags column is intentional and aligned; no measured fault. Taste.
- 9 Font fallback size-adjust: needs measured metrics of the real fonts, which the sandbox cannot fetch; guessed values could worsen shift. Self-hosting needs owner WOFF2.
- 12 Home list vs projects.html: projects.html adds filters; kept as is, low priority.
- 14, 15: Hasselhoff question wording is owner copy; stamp styles are taste.
- robots.txt: host-root only, owner to submit sitemap.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed home tablet light and phone dark (no header overflow, resume hidden on phone).
Next attack: no imagery, no status line, no first-person outcomes.

## 2026-10-23: cycle 8 response (designer)
Fixed:
- 5 Sticky header: html{scroll-padding-top:80px} so anchors and focus are not hidden under the header (WCAG 2.2 2.4.11).
- 4 quadrotor-landing: dropped the generic "In the realm of robotics" opening; the page now starts at the specific problem (existing autopilots falter in wind and on unstable platforms). No facts added or removed apart from the dropped filler.
- 9 Orphaned captions: figures that fail to load are now hidden entirely, caption included.
- 7 Resume (PDF) link added to the footer on every page, so phone has it.
Declined:
- 1, 11 status/outcomes/tense: owner-only facts; nothing invented. Needs one status line and 2-3 outcome sentences.
- 2, 3, 8 imagery, local media, image width/height: need owner files.
- 6 Hasselhoff press countdown, index-card restyle: taste; new gimmick not requested by owner, 99 s stamp already carries the joke.
- 10 Row tag column: taste; tags align to title, no measured fault. 13 Home vs Projects: projects adds filters. 14 stamp style: taste. 15 no email: deliberate (hard constraint on contact details).
- 12 Self-hosted fonts: no WOFF2 available in sandbox.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, no failures; viewed quadrotor-landing phone light and About tablet light.
Next attack: no imagery, no status line, no first-person outcomes.
