# Pieter Paul Castelein personal website

Public review preview: https://paul-castelein-preview.vercel.app/

This is the personal site only. Skaler is maintained separately. The preview is temporarily hosted in Yi's Vercel project; the company account and formal domain will be configured separately.

## October 19 source and design

`content/paul-final-en-2026-10-19.md`, `content/paul-final-pt-2026-10-19.md` and `content/paul-final-es-2026-10-19.md` preserve the personal-site sections of Paul's final English, Portuguese and Spanish attachments. The locale dictionaries use that copy, retaining his first-person voice and supplied project descriptions. The credentials comparison remains removed following his explicit request. English compound modifiers, Portuguese clitics and Spanish post-software spelling are corrected without rewriting the text. Attachment hashes are recorded in `content/final-copy-provenance-2026-10-19.json`; earlier drafts are excluded from this company handoff.

The latest personal Meta reference (da152857-a176-45d3-980d-4aa4c59501a1, preceded by 93609441-8480-48d2-b351-268c26975023) is the primary layout. The homepage preserves its editorial hero, principle band, static two-by-two venture grid, three cooperation columns, dark Thesis band, economics section, Memos rows and About/contact arrangement. Its original five poster images are served locally. The latest Skaler reference (856073c5-7749-4574-914e-06e4d908a09c) reinforces the same venture relationships; this repository does not change the Skaler website.

`scripts/templates/reference-home.html` is inert, sanitized section markup, localized by `scripts/reference_layout.py`. Its source utility styles are stored in `assets/reference.css`; the source React code, external font import and embedded runtime are not used. Playfair Display and Instrument Sans are self-hosted. Intentional practical differences are language switching, working project links, Paul's real rounded portrait (128px desktop / 144px mobile), readable translated figure captions/descriptions, keyboard navigation and the existing email-draft form. The old autoplay carousel and the prior green concept illustrations are no longer rendered. Historical generators and unused assets are excluded. The navigation stays visible while scrolling. Supporting page URLs remain functional and use the same typography, palette and original figures.
The pages are Home, Thesis, Partnerships, Memos, About, Contact and Privacy. English uses `/`, European Portuguese `/pt/`, and Spanish `/es/`. Each language has all seven pages and its own error page. Language links preserve the current page, enquiry starting point and section. All three language versions now use Paul's supplied final manuscripts. Supporting Spanish interface/form messages follow the formal register of his Spanish copy. Interface and privacy translations remain in place where the manuscripts do not supply them.

## Company repository and deployment

Company source: https://github.com/InspectOS-pt/paul-castelein

Initial handoff copies the approved personal-site implementation from local commit `57f2c01ff1620bf7e6576451023286636bd2f9a5`. The temporary preview remains available at the original link. This repository does not contain the old local Git history, Sites account association, credentials or private chat attachments.

Import this repository into the intended **company Vercel account**, using production branch `main`, repository root as Root Directory and Framework Preset **Other**. `vercel.json` supplies Build Command `python3 scripts/build-site.py`, an empty Install Command and Output Directory `dist`. The build requires Python 3 and Node.js, with no third-party package dependencies. Only the allowlisted `dist/` files are published.

Set Production environment variable `CASTELEIN_SITE_ORIGIN=https://castelein.eu.com` before building. This updates canonical URLs, language alternates, social metadata and the sitemap. No form, database, email API or other application secrets are required. The introduction form prepares a draft in the visitor's email application.

After the company deployment is verified, add **castelein.eu.com** to that company project and use the DNS/ownership values shown for that exact project. Joan registered the domain; coordinate the access details privately. Preserve existing mail and verification records, then verify DNS propagation and HTTPS. Registration transfer is not needed merely to connect the site. Do not detach or repoint Yi's temporary preview project during this handoff.

The English, Portuguese and Spanish privacy notices name Pieter Paul Castelein as the responsible person for his personal site, with Oeiras, Portugal and `paul@skaler.pt` as the public contact details. They explain the local email-draft form, enquiry purposes and legal bases, recipient categories, Vercel hosting and transfers, purpose-based retention and privacy rights. No unverified company, street address, exclusive mailbox access, email-provider name or fixed deletion deadline is asserted. The statement about no CRM/AI processing applies to the website form, not to an uninspected mailbox. Keep the notice aligned with actual enquiry handling and update it when that process changes.

The notice uses the identity/contact, purpose, recipient and retention-criteria structure in [GDPR Article 13](https://eur-lex.europa.eu/eli/reg/2016/679/oj), with hosting information linked to [Vercel's privacy notice](https://vercel.com/legal/privacy-policy) and [data processing addendum](https://vercel.com/legal/dpa), and the [CNPD](https://www.cnpd.pt/) as the Portuguese authority. These references do not verify private mailbox configuration.

Review indexing remains disabled in both metadata and `robots.txt`; any later decision to enable indexing must update the generator and its build validator together.

## Build and local preview

Requires Python 3 and Node.js, without third-party packages:

```sh
CASTELEIN_SITE_ORIGIN=https://paul-castelein-preview.vercel.app python3 scripts/build-site.py
python3 -m http.server 4187 --bind 127.0.0.1 --directory dist
```

The default origin without the environment variable is `https://castelein.eu.com`. Setting the public origin changes canonical, language alternates and social metadata without changing account-specific settings.

The build validates locale structure, page headings, internal resources, indexing rules and JSON metadata, then packages only public files in `dist/`. Manuscripts, chat attachments, source code, QA and credentials are excluded. Former page addresses resolve to the current equivalent through Vercel redirects and local HTML fallbacks. Former homepage anchors remain usable.

The contact form prepares a local email draft addressed to `paul@skaler.pt`. It never submits an enquiry to a server and never reports that a message has been received. Validation, email subjects, errors and copy feedback are translated.

## Before formal publication

- Replace the portrait if Paul supplies a higher-quality approved original.
- The privacy notice has been completed for the current personal site. If company ownership, email handling, tracking or form submission changes during deployment, update the notice to match before enabling those changes.
- Deploy `dist/` in the intended company project, then configure only the records supplied for that project. No formal domain or DNS changes are part of this preview update.
- Enable indexing only when the owner is ready. Review pages currently remain `noindex,nofollow`, with crawling disabled.

No registration credentials, verification codes or private communications are included in source or release files.
