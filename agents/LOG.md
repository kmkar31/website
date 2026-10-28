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

## 2026-10-24: cycle 9 response (designer)
Fixed:
- 4 Meta descriptions rewritten for all nine projects around facts already on each page (e.g. Hasselhoff: four BLDC thrusters, joystick remote, 99 s, IR target). Raftar now says 40+ students, matching the page (was "45").
- 1 (partial) About opening is tense-neutral: "My Master's ... is at Carnegie Mellon University (2023 - 2025)". Real status still owner-only.
- 12 Skills grid capped at the 760 px measure so rules and skills share one width on About.
- 8 SC 1.4.12 text-spacing test run (line-height 1.5, letter 0.12em, word 0.16em, paragraph 2em) on home, About, Hasselhoff, aerobraking, 404 at phone and desktop: no overflow, no clipped stamps, facts or buttons.
- 14 Aerobraking stamp is solid, no longer dashed.
Declined:
- 1 (rest), 3, 13, 15 status, local media, Wix resume file, email: owner-only facts or files; nothing invented.
- 2 Moving skills beside the intro: the right column is the portrait slot; aligned widths (12) instead.
- 5 Hasselhoff press countdown, index-card ledger, extra asides: taste; owner has not asked and the 99 s stamp already carries it. Raftar aside would repeat the stamp.
- 6 "Start here" row: an editorial ranking of the owner's work; deferred again, owner to choose.
- 7 Phone row tag line: taste; no measured fault. 9 robots.txt: host-root only. 10 Font metrics: no measurable files in sandbox.
- 11 About order: Seagate is linked from home (#seagate); order is a taste call.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed About desktop light.
Next attack: no imagery, no status line, no start-here row, one idea of fun.

## 2026-10-24: cycle 10 response (designer)
Fixed:
- 1 Broken thumbnails on Projects: failed `.thumb img` now collapses the row to the no-thumb grid (desktop and phone) via a `no-thumb` class; verified in projects tablet dark and phone light.
- 7 Hasselhoff opening trimmed: the movie story is now one sentence after the 99 s / IR-beam premise; no facts removed.
- 8 projects.html description names the topics; 404 gets a real description and `noindex`.
Declined:
- 2, 3, 4, 12, 13, 14 status, local media, imagery, Search Console, WOFF2, repo facts: owner-only; nothing invented. (About right side stays the portrait slot.)
- 5 "Start here" row: editorial ranking of the owner's work; owner to choose.
- 6 99 s press countdown / index card: taste; the stamp already carries the joke; owner has not asked.
- 9 Projects vs home: Projects adds filters and thumbnails; kept.
- 10 phone row tag line, 11 About order: taste; no measured fault.
- 15 stamp reading order: stamp sits inside the link name after the title; acceptable.
- Owner notes: retro and not-AI direction unchanged; grain left as is.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK.
Next attack: no imagery, no status line, no start-here row, one idea of fun.

## 2026-10-24: cycle 11 response (designer)
Fixed:
- 4 "Start here" label and larger title on row 01 (snake robots, matches the lede) on home only.
- 5 Hasselhoff "99 seconds" stamp on its project page counts down while pressed (pointer), restores on release, static under prefers-reduced-motion; contrast unchanged.
- 6 Home title now "Control of Robots and Spacecraft", taken from the page's own first sentence.
- 7 Row tag column widened 160 to 240 px; all stamps now one line at desktop, tablet and phone (measured heights 22-25 px, no overflow).
Declined:
- 1, 3, 10, 11, 13 status, local media/resume, Search Console, WOFF2, repo facts: owner-only; nothing invented.
- 2 About void: right column is the portrait slot; moving Skills would break the layout once the portrait exists.
- 8 Projects vs home: Projects adds filters and thumbnails; trimming home would hide work. 9 About order: Seagate is linked from home and the Skills block is short; taste.
- 12 filter state, 15 nav glyph spacing: taste, no measured fault. 14 stamp in link name: acceptable, reads as part of the title.
- Index-card ledger and pager aside (5b, 5c): not added; no owner request.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed home desktop and phone.
Next attack: no imagery, no status line, owner files needed.

## 2026-10-24: cycle 12 response (designer)
Fixed:
- 1, 4d, 6 Every project page now opens with "Fig. 1", an authored line drawing (inline SVG, repo-local, cannot hotlink-fail) on a graph-paper ground, drawn only from facts already on the page (500 m tether, four thrusters, 99 s, 0.8 m circle at 0.38 m/s, 46 orbits, elliptical vs circular path, hover and sinusoidal tests). Captions say where a drawing is schematic. This is the one non-default print idea: lab-notebook plates with figure numbers.
- 5 About: when the portrait fails to load, the empty column now holds an "On this page" index (Skills, Education, Experience; 44 px targets); hidden when the portrait loads and on phone.
- 10 Home actions wrap with tighter row gap on phone.
- 12, 4b Pager now shows the neighbour's first fact (e.g. "Tether: 500 m") instead of repeating its tl;dr.
- 13 Stamps reduced to two types: tilted single border, and the double border for the Formula Bharat podium.
- 14 Header link now reads "Resume (PDF)" like the body and footer.
- 4c Colophon adds the true line "Hand-built static pages, one stylesheet, no framework."
Declined:
- 2 Local resume PDF: the sandbox proxy returns 403 for the filesusr host, so the file cannot be copied; owner should drop it in assets/. Not faked.
- 3 Status/date line: owner-only fact; STATUS slot stays empty.
- 4a Hasselhoff index card: Fig. 1 plus the pressable stamp already open the page with the 99 s IR target; a second device would repeat it.
- 7 Self-hosted fonts and 8 robots.txt/OG image: need real WOFF2 and a host root; unchanged.
- 9 Resume in phone header: four header items would break the 44 px phone layout; resume is on the home actions and every footer.
- 11 Projects vs home: Projects adds filters and thumbnails when media loads.
- Row blurb vs page tl;dr repeat (12 in part): the blurb is the tl;dr by design; the third surface (pager) now differs.
Verification: tools/check.py (long timeout), 13 pages x 3 viewports x 2 themes, all OK; viewed all nine plates light and dark and About desktop.
Next attack: still no photographs, no status line, resume still a Wix hotlink.

## 2026-10-24: cycle 13 response (designer)
Fixed:
- 5 Tethered plate redrawn: satellites now above the horizon, vertical tether with a dimension bracket and "500 m tether" label beside it, no stray slashes. Checked the other plates: ARGUS rays ended inside the Earth, so they now end on the surface and the visible patch follows the arc. No other plate clips.
- 4 Every plate caption now carries a drawing-sheet tag ("Sheet 7 of 9 . NTS"), the lightest step toward the drawing-sheet idea.
- 3 Snake-robots generic background cut from two paragraphs to one sentence plus the lab link, retitled "Why snake robots" (no claims added).
- 10, 14 Home: Resume and LinkedIn now sit on one row on phone; the link is just "LinkedIn", so the contact route is stated once (footer).
Declined:
- 1, 2, 3 (media), 8 (WOFF2, image sizes), 9 robots/OG: owner files or facts needed (resume.pdf, status line, photos, fonts); sandbox cannot fetch Wix hosts, so dimensions of hotlinked images are unknown. Nothing invented. STATUS slot still empty.
- 4 drawing-register home index: large rewrite of the home list, risks the phone layout and scanning.
- 6 tally ticks, Hasselhoff beam mark, margin note: Fig. 1 plus the stamps already carry these facts; more devices would be decoration.
- 7 About void: portrait slot, two layouts by design. 11 Projects nav: filters and thumbnails. 12 Hasselhoff lead: voice, matches page. 13 tan tags: taste, contrast passes.
Verification: tools/check.py all OK, 13 pages x 3 viewports x 2 themes; viewed tethered desktop dark, ARGUS phone, home phone.
Next attack: owner media, resume file, status line.

## 2026-10-24: cycle 14 response (designer)
Fixed:
- 6 Home: Start-here row 01 now carries its Fig. 1 plate (repo-local inline SVG, text hidden at thumbnail size) on a graph-paper ground; full width on phone, so the front page has a visual and the list is no longer uniform.
- 5 Hasselhoff: Testing moved up after User Experience; Design Methodology and State Machine Logic now sit in a native `<details>` ("Implementation detail"), no JS, still in the HTML. Text unchanged.
- 14 Orphaned captions: the "(left)/(right)" caption reworded ("side by side"); JS now also hides a `p.cap` whose figure or figure row failed to load.
- 13 Hasselhoff row blurb no longer repeats the cameo joke (kept on the page lead); also removed duplicated "joystick remote" wording.
- 9 Mono labels at 11.5 px raised to 12 px (Start here, sheet tag, question label, stamps); stamps still one line.
- 11 Header: hairline rule separates the nav from Resume/icons (desktop and tablet).
- 15 Already done: every target=_blank carries rel="noopener". 4 interim: preconnect to fonts.gstatic.com already present.
Declined:
- 1 resume.pdf, 2 status line, 3 photographs, 4 self-hosted WOFF2, 10 og.png with plate, 8 email: need owner files or facts (sandbox cannot fetch Wix hosts); nothing invented. STATUS slot still empty.
- 3 "Table 1" of values: facts already sit in the facts strip above each plate; a table would repeat them.
- 7 About ledger-style date column: large About rewrite, About has a two-layout portrait slot; risk to phone layout.
- 12 more plate jokes: taste, owner has not asked.
Verification: tools/check.py all OK, 13 pages x 3 viewports x 2 themes; viewed home desktop and phone, Hasselhoff phone dark.
Next attack: owner blockers (resume, status, photos, fonts).

## 2026-10-25: cycle 15 response (designer)
Fixed:
- 5 Hasselhoff disclosure: label shortened to "Design and state machine", set in the serif heading face, with a boxed +/- marker in the accent and a Show/Hide word at the right; native details kept, no JS. Only page using the component.
- 6 (part) Start-here plate now carries a caption strip "Fig. 1 . Snake robot, schematic" so it reads as snake and as a figure, not a featured card.
- 12 Row tags raised from 12.5 to 13 px.
- 14 Hasselhoff 99 s stamp is now keyboard operable (JS adds tabindex, role=button, aria-label; hold Space or Enter, blur stops it); focus ring is the global one.
Declined:
- 1 resume.pdf, 3 photographs, 4 WOFF2, 10 og.png with plate, 11 image dimensions, 8 email: need owner files or facts; sandbox cannot fetch Wix hosts. Nothing invented.
- 2 status / stale dates: owner-only fact, STATUS slot still empty. This is the highest-value content gap: owner to say whether the Master's is finished, what he is doing now, and whether he is open to roles.
- 6 (rest) plates on all nine rows: Projects rows already show Wix thumbnails when they load; nine same-size plates would make the list uniform in a new way and lengthen phone home.
- 7 About date margin column: large rewrite; About has a portrait slot with two layouts. 9 trimming home to four rows: judgment call, home is the full index by design. 13, 15: taste / owner wording.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed Hasselhoff and home on phone.
Next attack: owner blockers (resume, status, photos, fonts).

## 2026-10-25: cycle 16 response (designer)
Fixed:
- 12 og.png now carries the Fig. 1 snake-robot schematic plate (hard shadow, caption strip), drawn from the same geometry as the site plate; tools/make_og.py updated, repo-local, no text overlap (viewed).
Declined:
- 1 snake page content, 2 status / stale dates (STATUS slot still empty), 3 resume.pdf, 4 photographs, 5 self-hosted WOFF2, 13 image dimensions, 11 contact: need owner facts or files; nothing invented. Demoting "Start here" or adding a "work in progress" line would assert facts about status the repo does not hold; editorial ranking is the owner's.
- 6 desktop-only plates on all rows: eight more plates need authored schematics per project and would make the list uniform in a new way; row 01 is captioned as a figure, not a card. 10 trimming home: home is the full index by design (documented cycle 15). 7 Hasselhoff detail stays collapsed: summary is explicit ("Design and state machine, Show") and text is in the HTML. 9 About date column: large rewrite, taste. 15 asides: taste, owner has not asked (facts already stated on each page).
- 14 keyboard: stamp and details are native/ARIA from cycle 15; no regression in check.py (all OK); not a real tab-through here.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK (78 lines). Sitemap lastmod bumped by build.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-25: cycle 17 response (designer)
Fixed:
- 8 GPA: removed the "(3.9 / 4.0)" conversion from About; the repo and original site only support 9.3 / 10. CMU 4.0 / 4.0 stays.
- 9 About: dropped the duplicate "Resume (PDF)" button; header (desktop/tablet), home actions and footer still link it.
Declined:
- 1 snake page facts, 2 status / stale dates (STATUS still empty), 3 resume.pdf, 4 photographs, 5 self-hosted WOFF2, 12 image dimensions, 13 outcome text: need owner facts or files; nothing invented. Moving "Start here" is an editorial call for the owner.
- 6 plates on all rows and 7 trimming home: same reasoning as cycles 15-16 (eight more authored schematics; home is the full index by design). 10 About date column: large rewrite, taste. 11 contact: owner constraint. 14 asides: taste.
- 15 keyboard: stamp and details use native/ARIA from cycle 15; not a real tab-through here.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-25: cycle 18 response (designer)
Fixed:
- 12 Row links: accessible name is now just the project title (aria-labelledby on the h3); the stamp and tags are the description (aria-describedby), so a screen reader no longer reads the stamp as part of the link text. Visual markup unchanged.
Declined:
- 1 snake page facts / Start-here swap, 2 status and stale dates (STATUS still empty), 3 resume.pdf, 4 photographs, 6 WOFF2, 10 image dimensions, 11 thin project text: need owner facts or files; nothing invented. Moving "Start here" to Aerobraking is an editorial call for the owner.
- 5 larger or removed plate: the caption strip makes it read as Fig. 1; removing it returns the uniform list. 7 trim home: home is the full index by design (cycles 15-17). 8 phone header links: 44 px layout, Resume stays in hero and footer. 9 About date column: large rewrite, taste. 13 contact: owner constraint. 14 asides: taste. 15 real tab-through: native/ARIA, no regression in check.py.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK (screenshots not re-viewed beyond check output; change is non-visual).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-25: cycle 19 response (designer)
Fixed:
- 4 Aerobraking: four plain h2s from the existing text (The problem, Setup, Method, Result); no copy changed. Page is now scannable; hero tldr and facts strip already state the 46-orbit result.
- 7 Pager: no wraparound. Project 01 has no Previous, project 09 has no Next (lone link sits on its own side on desktop, left on phone).
- 9 Projects page: visually hidden h2 "All projects" so headings go h1, h2, h3.
Declined:
- 4 (part) moving the result sentence to the top: it would duplicate the hero tldr and facts strip and break the paper's order of argument.
- 1 snake facts / Start-here swap, 2 status and stale dates (STATUS still empty), 3 resume.pdf, 5 photographs, 8 WOFF2, 11 image dimensions: need owner facts or files; nothing invented.
- 6 fact line per row: facts are already in each page's strip and the pager; repeating them on nine rows would add the uniform column the finding complains about. 10 home length: home is the full index by design. 12 About date column: large rewrite, taste. 13 contact: owner constraint. 14 asides: taste.
- 15 real keyboard pass: not run this cycle (native/ARIA, no regression in check.py).
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed aerobraking phone light and snake desktop light (pager).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2); keyboard tab-through.

## 2026-10-25: cycle 20 response (designer)
Fixed:
- 3 Empty focusable zoom links: figure images start with their `a.zoom` wrapper set to tabindex=-1 and aria-hidden until the image reports load; on error it stays hidden and the figure is dropped. Real Tab pass on Hasselhoff with all http blocked: no nameless stops left (stops now: skip link, nav, back link, stamp button, summary, repo, pager, footer). No-JS behaviour unchanged (links work).
- 14 99 s stamp: the dd is now plain text for no-JS; JS puts a real `<button>` inside it (aria-label, 47 px tall), so the definition list keeps its semantics. Look unchanged (viewed).
- 15 "three weeks to 15 minutes" link goes to about.html#seagate, which exists and is the Seagate entry; no change.
Declined:
- 1 snake facts / Start-here swap, 2 status and stale dates (STATUS still empty), 4 resume.pdf, 5 photographs, 7 WOFF2, 9 image width/height: need owner facts or files; nothing invented. Editorial choice of Start here is the owner's.
- 6 one fact per row: stamps already carry facts on three rows; repeating pager/strip facts on nine rows adds a uniform column (as in cycle 19).
- 8 home length: full index by design. 10 About date column and 11 collapsing Sysid Background: large rewrite / taste. 12 contact: owner constraint. 13 asides: taste.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py all OK; Playwright Tab x30 on Hasselhoff offline.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-26: cycle 21 response (designer)
Fixed:
- 8 Fig. 1 caption on the home plate shortened to "Fig. 1 . Snake robot" so it stays on one line in the 176 px plate (viewed at 1366 wide). The project page still carries the full "schematic" caption.
- 6 Stamps added to rows 07, 08, 09 from facts already on those pages: "500 m of tether", "4 unknowns, fitted", "Four-bar pedal path". Rows 03 and 02 left bare (row 02 has no hard fact; 03's figure is a percentage with conditions that do not fit a stamp). Six of nine rows now carry stamps; watch for this becoming the new sameness.
Declined:
- 1 snake facts / Start-here swap, 2 status and stale dates (STATUS still empty), 3 resume.pdf, 4 photographs, 7 image width/height: owner facts or files; nothing invented.
- 5 (part) fallback font: a size-adjusted fallback needs the real DM Serif / Source Serif metrics; guessing size-adjust values would be invented numbers. Self-hosted WOFF2 needs the files. display=swap is already set.
- 9 desktop gutter, 10 About date column, 11 collapse Sysid Background, 12 home length, 14 asides: taste or large rewrite, as in earlier cycles. 13 contact: owner constraint. 15 real Tab pass on live zoom links: cannot run with Wix images blocked here; offline pass was done in cycle 20.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK; viewed home desktop light.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2); stamp uniformity.

## 2026-10-26: cycle 22 response (designer)
Fixed:
- 5 Stamp uniformity: removed the two label-only stamps ("4 unknowns, fitted", "Four-bar pedal path"). Stamps now sit only where the number is the point (99 s, 46 orbits, podium, 500 m); rows 08 and 09 are plain.
- 4a About: "podium finish at Formula Bharat 2023" gets the double-border mark from the home podium stamp, so About carries one authored mark (viewed phone light, desktop dark; wraps normally under 420 px).
Declined:
- 1 status/stale dates (STATUS still empty), 2 local photos/resume.pdf/image dimensions, 3 snake outcomes or Start-here swap, 6 alt text, 10 WOFF2: need owner facts or files; nothing invented. Finding 3 (Start here is the thinnest page) is flagged to the owner: either supply what was done and what happened, or move the label to aerobraking (46 orbits).
- 4b pager stamps, 4c empty-state line: filters never return zero results here; extra marks on every page would undo finding 5.
- 7 contact: owner constraint (no public email). 8 LinkedIn in home action row, 13 button above second lede paragraph: taste, repeated links aid findability and the lede order is deliberate.
- 9 sticky "On this page": the index lives inside the intro grid, so sticky would have no travel; making it travel needs a layout rewrite for three links. 11 resolved by 2. 12 "Start here" label contrast passes; hierarchy nit.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-26: cycle 23 response (designer)
Fixed:
- 2 Quadrotor Landing plate: "origin" now right-aligned to the left of the dot (x=232, text-anchor end), "r = 0.8 m" moved to x=262 under the radius bar; no overprint at 390 px (viewed phone light). Scanned the other plates' text positions in build.py: labels are spread 80+ units apart or anchored apart; no similar pairs found.
Declined:
- 1 status/stale dates (STATUS still empty; tense of "is at" needs the owner), 3 snake outcomes or Start-here swap, 5 local images/resume and image dimensions, 6 alt text for Wix figures, 10 WOFF2/size-adjusted fallback: need owner facts or files; nothing invented.
- 4a orbit aside: needs owner okay. 4b pager stamps: would add marks on every page (undoes cycle 22 trim). 4c "three weeks"/"3 weeks": both are already the same strike; wording differs only by numeral vs word in a sentence vs a bullet, left as is.
- 7 resolved by 3. 8 About desktop empty third: taste; the portrait slot is documented and a layout rewrite for it would risk mobile. 9 contact: owner constraint. 11 "START HERE" label: contrast passes, hierarchy nit. 12 noted, no change.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, photos, WOFF2).

## 2026-10-26: cycle 24 response (designer)
Fixed:
- 5 Landing wording: verified build.py. Page body, meta description, pager fact and the 5.6 s / 2.5 cm top-speed line all state the same two conditions (small pad; Tumbller stable and under 0.25 m/s), and the body notes the larger pad had problems. No claim is general; no change needed.
Declined:
- 1 status/date and the tense of "is at" (STATUS still empty), 2 snake outcomes or Start-here swap, 3 local images/resume.pdf/image dimensions, 4 what-I-did sentences and numbers for Raftar and others, 6 alt text, 7 WOFF2/size-adjusted fallback: need owner facts or files; nothing invented.
- 8 About desktop empty third: taste; the portrait slot is documented and the home ledger moved there would duplicate content. Accepted as is. 9 contact: owner constraint. 10 "START HERE" label: contrast passes, hierarchy nit. 11 LinkedIn repeated in footer band: harmless, aids findability.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: build re-run (only sitemap lastmod changed), tools/check.py 13 pages x 3 viewports x 2 themes, no failures.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts, photos, WOFF2).

## 2026-10-26: cycle 25 response (designer)
Fixed:
- 5 About podium mark: removed white-space:nowrap (it forced the box onto its own line and stranded the full stop), added box-decoration-break:clone, and moved the period inside the mark. Viewed About tablet light: the mark now wraps across two lines with the period attached.
Declined:
- 1 status/date and tense of "is at", 2 Start-here swap or snake outcomes, 3 local images/resume/image dimensions, 4 what-I-did facts for Raftar and others, 7 alt text, 8 WOFF2/size-adjusted fallback: need owner facts or files; nothing invented.
- 6 home stamp repeating the lede: the stamp is the authored mark and the only candidate replacement (team size) would be a fact needing owner confirmation; accepted.
- 9 About desktop empty third: taste, accepted (portrait slot documented). 10 contact: owner constraint. 11 "START HERE" label: contrast passes, hierarchy nit. 12 footer LinkedIn repeat: harmless, aids findability.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: build re-run; tools/check.py 13 pages x 3 viewports x 2 themes, no failures.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts, photos, WOFF2).

## 2026-10-26: cycle 26 response (designer)
Fixed:
- Nothing designer-fixable remained; the critic found no regression. Build re-run produced no site changes.
Declined:
- 1 status/date and tense of "is at" (STATUS still empty), 2 Start-here swap or snake outcomes, 3 local images/resume/image dimensions, 4 what-I-did facts for Raftar, 5 alt text, 6 WOFF2/size-adjusted fallback: need owner facts or files; nothing invented.
- 7 About desktop empty third: taste, accepted. 8 contact: owner constraint. 9 "START HERE" label: contrast passes, hierarchy nit. 10 footer LinkedIn repeat: harmless, aids findability.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts, photos, WOFF2).

## 2026-10-27: cycle 27 response (designer)
Fixed:
- Nothing designer-fixable remained; no regression found. Build re-run produced no site changes.
Declined:
- 1 status/date and tense of "is at" (STATUS still empty), 2 Start-here swap or snake outcomes, 3 local images/resume.pdf/image dimensions, 4 what-I-did facts and numbers for Raftar, 5 alt text, 6 WOFF2/size-adjusted fallback: need owner facts or files; nothing invented.
- 7 About desktop empty third: taste, accepted. 8 contact: owner constraint. 9 "START HERE" label: contrast passes, hierarchy nit. 10 footer LinkedIn repeat: harmless, aids findability.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts, photos, WOFF2).

## 2026-10-27: cycle 28 response (designer)
Fixed:
- Nothing designer-fixable remained; no regression found. Build re-run produced no site changes.
Declined:
- 1 status/date and tense (STATUS still empty), 2 Start-here swap or snake outcomes, 3 local images/resume/image dimensions, 4 what-I-did facts for Raftar, 6 alt text for Wix figures: need owner facts or files; nothing invented.
- 5 size-adjusted font fallback: needs the real font files to compute metrics; not available in this sandbox (no network), and guessed values could worsen layout shift. Left for a networked cycle.
- 7 About desktop empty third: taste, accepted. 8 stamp repetition: noted, no stamps added. 9 contact: owner constraint. 10 "START HERE" label: contrast passes. 11 footer LinkedIn repeat: harmless.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts, photos, font files).

## 2026-10-27: cycle 29 response (designer)
Fixed:
- Nothing designer-fixable remained; no regression found. Build re-run produced no site changes.
Declined:
- 1 status/date and tense (STATUS still empty), 2 Start-here swap or snake outcomes, 3 local images/resume/image dimensions, 4 what-I-did facts for Raftar, 5 Ferrari claim confirmation, 7 alt text for Wix figures: need owner facts or files; nothing invented.
- 6 size-adjusted font fallback: needs the real font files; not available offline, guessed metrics could worsen layout shift.
- 8 About desktop empty third: taste, accepted. 9 stamp repetition: no stamps added. 10 contact: owner constraint. 11 "START HERE" label: contrast passes. 12 footer LinkedIn repeat: harmless.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-27: cycle 30 response (designer)
Fixed:
- Nothing designer-fixable remained; no regression found. Build re-run produced no site changes.
Declined:
- 1 status/date and tense (STATUS still empty), 2 Start-here swap or snake outcomes, 3 local Resume/images and image width/height (dimensions unknown offline), 4 what-I-did facts for Raftar, 5 Ferrari claim confirmation, 6 alt text for Wix figures: need owner facts or files; nothing invented.
- 6 (empty alt): the only alt="" elements are the project-row thumbnails (decorative, adjacent text names the project) and the lightbox img, whose alt JS fills from the opened figure. Intentional, not a defect.
- 7 size-adjusted font fallback: needs the real font files; guessed metrics could worsen layout shift.
- 8 empty band / About third: taste, accepted. 9 stamp repetition: no stamps added. 10 contact: owner constraint. 11 "START HERE" label: contrast passes. 12 footer LinkedIn repeat: harmless.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes).
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-27: cycle 31 response (designer)
Fixed:
- 5 Aerobraking wall of prose: added a "Result at a glance" ledger under the Result heading (10038 km initial and 4906 km target apoapsis, 46 orbits, 8.4 km terminal error, 1.1M steps; all figures already on the page) and set the action space as a mono block in Setup. Body copy unchanged.
Declined:
- 1 status/date, 2 Start-here swap or snake outcomes, 3 local Resume/images and image width/height, 4 Raftar facts, 6 Ferrari wording, 7 alt text for Wix figures: need owner facts or files; nothing invented.
- 8 size-adjusted font fallback: needs real font files; guessed metrics could worsen layout shift.
- 9 stamp repetition: no stamps added. 10 contact: owner constraint. 11 empty band / About third: taste, accepted. 12 "START HERE" label: contrast passes; footer LinkedIn repeat harmless.
- robots.txt/sitemap at subpath: GitHub Pages project site cannot serve host root; submit sitemap in Search Console (owner action).
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures; viewed Aerobraking phone light.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-27: cycle 32 response (designer)
Fixed:
- 1 Result ledger: dropped the three figures already shown in the hero, facts strip and Result paragraph (46 orbits, 8.4 km, 1.1M steps); kept only initial and target apoapsis as a two-item "Orbit range" line. No wrapping labels, no orphaned item, baselines align on phone and desktop.
- 6 "guarantees" claim: replaced the last sentence with "in simulation the RL-based method completed the aerobraking maneuver, reaching the target apoapsis in 46 orbits", which the page's own evidence supports. Removes the unshown fuel/time comparison.
Declined:
- 2 status/date, 3 Start-here swap or snake outcomes, 4 local Resume and image width/height (dimensions unknown offline), 5 Raftar facts, 7 Ferrari wording, 8 alt text for Wix figures: need owner facts or files; nothing invented.
- 9 size-adjusted font fallback: needs real font files; guessed metrics could worsen layout shift.
- 10 stamp repetition: no stamps added. 11 contact: owner constraint. 12 "START HERE" label and empty bands: contrast passes, taste, accepted.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes); viewed Aerobraking phone light and desktop dark.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-28: cycle 33 response (designer)
Fixed:
- 10 "START HERE" label: raised from .75rem to .82rem (still underlined in accent). Contrast unchanged and passing.
Declined:
- 1 status/date, 2 Start-here swap or snake outcomes, 3 local Resume and image width/height, 4 Raftar facts, 5 Ferrari wording, 6 alt text for Wix figures: need owner facts or files; nothing invented.
- 7 size-adjusted font fallback / self-hosting: needs real font files; guessed metrics could worsen layout shift.
- 8 stamp repetition: no stamps added. 9 contact: LinkedIn only, owner constraint.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes); viewed home phone light.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-28: cycle 34 response (designer)
Fixed:
- Nothing designer-fixable; the critic found no defect. Rebuild produced no diff.
Declined:
- 1 status/date (STATUS in build.py stays empty), 2 Start-here swap or Snake outcomes, 3 local Resume and image width/height, 4 Raftar facts, 5 Ferrari wording, 6 alt text for Wix figures: need owner facts or files; nothing invented.
- 7 font fallback metrics / self-hosting: needs real font files; guessed metrics could worsen layout shift.
- 8 stamp repetition: no stamps added. 9 contact: LinkedIn only, owner constraint. 10 About right third: taste, documented and accepted.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes). Screenshots not re-viewed since no output changed.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-28: cycle 35 response (designer)
Fixed:
- Nothing designer-fixable; the critic found no defect. Rebuild produced no diff.
Declined:
- 1 status/date (STATUS in build.py stays empty), 2 Start-here swap or Snake outcomes, 3 local Resume and image width/height, 4 Raftar facts, 5 Ferrari wording, 6 alt text for Wix figures: need owner facts or files; nothing invented.
- 7 font fallback metrics / self-hosting: needs real font files; guessed metrics could worsen layout shift.
- 8 stamp repetition: no stamps added. 9 contact: LinkedIn only, owner constraint. 10 About right third: taste, documented and accepted.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes). Screenshots not re-viewed since no output changed.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).

## 2026-10-28: cycle 36 response (designer)
Fixed:
- 5 scroll padding: already present. html has scroll-padding-top:80px (assets/style.css, from build/build.py line 518), above the sticky header height (about 60 px phone). The critic's grep missed it. No change needed.
Declined:
- 1 status/date (STATUS in build.py stays empty), 2 Start-here swap or Snake outcomes, 3 local Resume and image width/height, 4 Raftar facts, 6 Ferrari wording, 7 alt text for Wix figures: need owner facts or files; nothing invented.
- 8 font fallback metrics / self-hosting: needs real font files; guessed metrics could worsen layout shift.
- 9 stamp repetition: no stamps added. 10 contact: LinkedIn only, owner constraint. 11 placeholder plate: needs a real photo from the owner. 12 About right third: taste, documented and accepted.
- Owner notes (retro matte, not AI-looking): met per critic; no change.
Verification: rebuild produced no diff; tools/check.py 13 pages x 3 viewports x 2 themes, no failures (only sandbox image notes). Screenshots not re-viewed since no output changed.
Next attack: owner blockers (status sentence, resume.pdf, snake facts, Raftar facts and Ferrari wording, photos, font files).
