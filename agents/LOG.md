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
