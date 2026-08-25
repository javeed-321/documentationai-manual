---
updatedAt: 2026-08-13T16:48:24.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Subscribe to API updates

## Overview

DriveWealth ships on a regular release cadence. Every release — new endpoints, changed fields, deprecations, bug fixes, and breaking changes — is published to a public **RSS feed**. Subscribe once and your team gets notified automatically, wherever you already work: your feed reader, Slack, Microsoft Teams, email, or your CI pipeline.

This guide walks through subscribing in under two minutes, then covers advanced setups for teams that want updates routed into their existing tooling.

> **Why RSS?** RSS is an open, vendor-neutral standard. There's no account to create, no scraping, no polling our changelog by hand, and no dependency on a third-party notification service. Any reader on any platform can consume the same feed, so you stay in control of how and where you receive updates.

***

## Quick start

**1. Copy the feed URL**

<RssCopyButton />

The button above copies the DriveWealth API updates feed URL to your clipboard.

**2. Add it to any RSS reader**

Paste the URL into the "Add feed" or "New subscription" field of your reader of choice. That's it — you'll receive every future release note as soon as it publishes.

## What's in the feed

Each release publishes one `<item>`. Every item contains these elements:

| Element                      | Example value                          | Description                                                                                  |
| ---------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------- |
| `<title>`                    | `Release Notes 2026-08-13`             | The release name — either dated release notes or a version tag (e.g. `API Release v1.82.0`). |
| `<description>`              | `API Release 2026-07-24`               | A short, human-readable summary of the release.                                              |
| `<link>`                     | `…/changelog/release-notes-2026-08-13` | Permalink to the full release note on the developer site.                                    |
| `<guid isPermaLink="false">` | `eecd4354-5af0-3ce9-bdaf-92c4b967f31b` | A stable, unique ID for the release. It is a **UUID, not a URL** — use it to de-duplicate.   |
| `<pubDate>`                  | `Thu, 13 Aug 2026 13:16:22 GMT`        | When the release published (RFC-822). Your reader uses this to sort.                         |
| `<dc:creator>`               | `ReadMe GitHub Action`                 | Who or what authored the note.                                                               |
| `<type>`                     | `added`, `improved`                    | The change category. May be empty on some items.                                             |

At the channel level, the feed also exposes `<lastBuildDate>` (when the feed was last regenerated) and is **paginated** — an `<atom:link rel="next">` points to the next page of older releases (`?page=2`, and so on). Feed readers handle this for you; programmatic consumers reading full history should follow the `next` link.&#x20;

***

## Best practices

* **Subscribe once, per team.** Route the feed into a shared Slack/Teams channel or distribution list so the whole team sees changes — not just one person.
* **Alert loudly on action-required changes.** Set a distinct notification (channel mention, email, or CI failure) for releases whose `<type>` is `deprecated` or `removed`.
* **Automate your safety net.** If you have integration tests, trigger them when a new release publishes so regressions surface before they reach production.
* **Keep a record.** A feed reader or an archived channel gives you a searchable history of every API change — invaluable when debugging behavior that changed between releases.
* **Poll politely.** If you consume the feed programmatically, use conditional requests and cap polling at once per day.