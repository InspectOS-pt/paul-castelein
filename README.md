# Pieter Paul Castelein personal website

Public review preview: https://paul-castelein-preview.vercel.app/

This is the personal site only. Skaler is maintained separately. The formal site is https://www.castelein.eu.com/ in the company Vercel workspace; the review preview remains in Yi's separate project.

## October 19 source and design

`content/paul-final-en-2026-10-19.md`, `content/paul-final-pt-2026-10-19.md` and `content/paul-final-es-2026-10-19.md` preserve the personal-site sections of Paul's final English, Portuguese and Spanish attachments. The locale dictionaries use that copy, retaining his first-person voice and supplied project descriptions. The credentials comparison remains removed following his explicit request. English compound modifiers, Portuguese clitics and Spanish post-software spelling are corrected without rewriting the text. Attachment hashes are recorded in `content/final-copy-provenance-2026-10-19.json`; earlier drafts are excluded from this company handoff.

The selected personal Meta reference (da152857-a176-45d3-980d-4aa4c59501a1, preceded by 93609441-8480-48d2-b351-268c26975023) is the primary layout. The homepage preserves its editorial hero, principle band, static two-by-two venture grid, three cooperation columns, dark Thesis band, economics section, Memos rows and About/contact arrangement. The five figures now use Paul's [native component reference](https://www.meta.ai/share/a/19d0d284-7e7b-49a4-8740-c8db183b536e), with [supporting final illustrations](https://meta.ai/share/c/hhkUckNd5X). Static HTML, native SVG and scoped CSS replace raster posters. The flywheel also incorporates Paul's [later minimal reference](https://meta.ai/share/c/2apkDwXuH5): four small black dots, outside labels and an open circular loop, using the personal site's ink palette. A grid keeps translated labels outside the ring; narrow screens use a clear linear sequence. Paper, black ink, thin stone borders and 16px corners follow the reference. All diagram text is translated into English, Portuguese and Spanish. Instrument Serif, Inter and JetBrains Mono are self-hosted with their SIL Open Font License files. `scripts/reference_figures.py`, five inert templates in `scripts/templates/native-figures/`, and `content/native-figure-copy.json` generate them. Provenance is recorded in `content/native-figure-provenance-2026-10-19.json`. The earlier raster sets remain historical source assets and are excluded from the release. The Skaler reference (856073c5-7749-4574-914e-06e4d908a09c) reinforces the same venture relationships; this repository does not change the Skaler website.

`scripts/templates/reference-home.html` is inert, sanitized section markup, localized by `scripts/reference_layout.py`. Its source utility styles are stored in `assets/reference.css`; the source React code, external font import and embedded runtime are not used. Playfair Display and Instrument Sans are self-hosted. Intentional practical differences are language switching, working project links, Paul's real rounded portrait (128px desktop / 144px mobile), translated native diagram text, keyboard navigation and the contact form. Owner-marked identity labels, hero badge, principle sublabel and external diagram captions are removed in all languages. Profile and introduction copy use Operator/Operador. The build checks these constraints to prevent them returning. The old autoplay carousel and the prior green concept illustrations are no longer rendered. Historical generators and unused assets are excluded. The shared header uses the owner-requested bold sans-serif Castelein. wordmark, with a black full stop and locally hosted Inter reused from the figure font assets. The footer description ends at Pieter Paul Castelein, omitting the Founder of Skaler.pt clause in all three languages. The navigation stays visible while scrolling. Supporting page URLs remain functional and use the same typography, palette and native figures. In the homepage Thesis section, the model card and two explanatory paragraphs form a compact top-aligned row; the information-asymmetry figure spans a separate full-width row below it so its desktop panels can sit side by side.
The pages are Home, Thesis, Partnerships, Memos, About, Contact and Privacy. English uses `/`, European Portuguese `/pt/`, and Spanish `/es/`. Each language has all seven pages and its own error page. Language links preserve the current page, enquiry starting point and section. All three language versions now use Paul's supplied final manuscripts. Supporting Spanish interface/form messages follow the formal register of his Spanish copy. Interface and privacy translations remain in place where the manuscripts do not supply them.

## Company repository and deployment

Company source: https://github.com/InspectOS-pt/paul-castelein

Initial handoff copies the approved personal-site implementation from local commit `57f2c01ff1620bf7e6576451023286636bd2f9a5`. The temporary preview remains available at the original link. This repository does not contain the old local Git history, Sites account association, credentials or private chat attachments.

Import this repository into the intended **company Vercel account**, using production branch `main`, repository root as Root Directory and Framework Preset **Other**. `vercel.json` supplies Build Command `python3 scripts/build-site.py`, an empty Install Command and Output Directory `dist`. The build requires Python 3 and Node.js, with no third-party package dependencies. The allowlisted `dist/` files are served as static content; `api/enquiry.py` is deployed separately as a Vercel Python Function. The static bundle contains 71 files; no figure rasters, source templates or provenance are served. The function uses only the Python standard library. Deploy from the repository root so Vercel discovers `api/enquiry.py`; uploading only `dist/` will not provide a working form.

Set Production environment variable `CASTELEIN_SITE_ORIGIN=https://castelein.eu.com` before building. This updates canonical URLs, language alternates, social metadata and the sitemap. Configure the server-side contact variables below separately for Production and Preview; never place them in HTML, JavaScript or public variables.

After the company deployment is verified, add **castelein.eu.com** to that company project and use the DNS/ownership values shown for that exact project. Joan registered the domain; coordinate the access details privately. Preserve existing mail and verification records, then verify DNS propagation and HTTPS. Registration transfer is not needed merely to connect the site. Do not detach or repoint Yi's temporary preview project during this handoff.

The English, Portuguese and Spanish privacy notices name Pieter Paul Castelein as the responsible person for his personal site, with `paul@skaler.pt` as the privacy email. At his request, postal correspondence uses the company address: **Pieter Paul Castelein, c/o Skaler, Rua Salvador Martins 3A, 2740-315 Porto Salvo, Portugal**. The address is published on [RealOS's official contact page](https://www.realos.pt/en/contact/), which identifies Skaler as SCULPTED ECLIPSE LDA. Using this mailing address does not substitute another venture's legal entity as the controller of Pieter's personal site.

The notices explain the server-submitted contact form, email delivery, enquiry purposes and legal bases, recipient categories, Vercel hosting and transfers, purpose-based retention and privacy rights. No unverified exclusive mailbox access, email-provider name or fixed deletion deadline is asserted. The statement about no CRM/AI processing applies to the website form, not to an uninspected mailbox. Keep the notice aligned with actual enquiry handling and update it when that process changes.

The notice uses the identity/contact, purpose, recipient and retention-criteria structure in [GDPR Article 13](https://eur-lex.europa.eu/eli/reg/2016/679/oj), with hosting information linked to [Vercel's privacy notice](https://vercel.com/legal/privacy-policy) and [data processing addendum](https://vercel.com/legal/dpa), and the [CNPD](https://www.cnpd.pt/) as the Portuguese authority. These references do not verify private mailbox configuration.

Production indexing is enabled on the official apex and www origins: public pages use `index,follow`, and `robots.txt` allows crawling with the sitemap advertised. API routes are excluded; error and legacy redirect pages retain `noindex,nofollow`. Preview and development builds retain `Disallow: /` and `noindex,nofollow`, even when their origin defaults to the official domain. A separate preview project remains blocked when its origin is its preview hostname, including Vercel's Production target for that project.

## Build and local preview

Requires Python 3 and Node.js, without third-party packages:

```sh
CASTELEIN_SITE_ORIGIN=https://paul-castelein-preview.vercel.app python3 scripts/build-site.py
python3 scripts/serve-site.py --port 4187
```

The default origin without the environment variable is `https://castelein.eu.com`. Setting the public origin changes canonical, language alternates and social metadata without changing account-specific settings.

Run `python3 scripts/test-indexing.py` to verify all generated pages and the static bundle across official production, Vercel preview/development and separate preview-project builds. The test uses temporary copies and does not deploy or send email.

The build validates locale structure, page headings, internal resources, indexing rules and JSON metadata, then packages only public files in `dist/`. Manuscripts, chat attachments, source code, QA and credentials are excluded. Former page addresses resolve to the current equivalent through Vercel redirects and local HTML fallbacks. Former homepage anchors remain usable.

The contact form submits JSON to the same-origin `/api/enquiry` function. Selecting Other reveals a required Please specify field (maximum 200 characters) in every language. The server validates the explanation and includes it in the email only for Other; hidden explanations are omitted. It preserves input on failure, prevents duplicate clicks while sending, and shows success only after SMTP acceptance. SMTP acceptance does not verify arrival in the inbox. Validation and sending, success, unavailable and failure states are translated. Direct email/copy widgets and email-app fallbacks are removed from the contact pages; the privacy contact remains in the legal notice.

## Contact delivery setup and release check

1. Deploy **the repository root**, with Framework Preset Other, the source `vercel.json`, and Python 3.12 from `.python-version`. The generator preserves the function configuration on every build. Do not deploy `dist/` alone or override the function build with the historical static-only preview upload. A file-based upload must include `api/enquiry.py` and `.python-version` alongside the public static files, and must allow Vercel to build the Python function.
2. In the intended Vercel project, set `SMTP_HOST`, `SMTP_PORT` (`587` for STARTTLS or `465` for implicit TLS), `SMTP_USER`, `SMTP_PASS`, and `SMTP_FROM` (a plain sender address authorized by the provider). These are server secrets. The existing Skaler SMTP service may be reused by the administrator; no new email provider is required.
3. Set `ENQUIRY_PERSONAL_TO` to the approved receiving address; the server default is Paul's existing mailbox. Set `ENQUIRY_FORMS_ENABLED=true` only when SMTP is configured. Missing/disabled configuration returns HTTP 503 and an honest unavailable message; it never reports a sent message.
4. Official apex and www origins and the exact deployment's `VERCEL_URL` / `VERCEL_PROJECT_PRODUCTION_URL` are accepted. For an additional preview alias, set `CONTACT_ALLOWED_ORIGINS` to its exact HTTPS origin (comma-separated if several). No wildcard CORS or arbitrary request-host trust is used. The local server adds only its loopback origins.
5. Redeploy after configuring environment variables. On the deployed preview, test required fields and malformed input, submit one clearly labelled test enquiry, and confirm its arrival with the receiving mailbox owner. Then enable the production environment, redeploy and repeat the controlled delivery check. **A mocked SMTP test or successful build is not inbox-delivery verification.** Production release remains pending this administrator configuration and delivery check.

Run `python3 -m unittest discover -s tests -v` for HTTP validation, exact origins, honeypot, size bounds, disabled/missing configuration, TLS/authentication failures, recipient rejection, and accepted-mail response tests. SMTP is mocked; these tests send no external email. `python3 scripts/serve-site.py --port 4187` serves both static pages and the real handler for browser validation and the HTTP 503 path without credentials. Do not use production SMTP credentials for routine local tests.

The endpoint does not log enquiry payloads or expose server/provider errors. It enforces exact browser origins, a hidden honeypot, input bounds, a five-second body read timeout and TLS-only SMTP on ports 465/587. Apply the existing project firewall/rate-limit policy to `/api/enquiry` before release; honeypots and origin checks alone do not stop automated callers.

## Before formal publication

- Replace the portrait if Paul supplies a higher-quality approved original.
- The privacy notice has been completed for the current personal site. If company ownership, email handling, tracking or form submission changes during deployment, update the notice to match before enabling those changes.
- Deploy from the repository root with the Python function, configure server SMTP variables and confirm a controlled enquiry arrives before merging/releasing the form. Do not replace a functioning production site with a form that has not passed delivery verification. No formal domain or DNS changes are part of this update.
- Production crawling/indexing was authorized on October 21. Preserve the preview restrictions when updating either deployment.

No registration credentials, verification codes or private communications are included in source or release files.
