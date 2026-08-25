# Migration report — techdocs-akamai-com

https://techdocs.akamai.com/adaptive-media-delivery/docs/welcome-adaptive-media-deliv · readme · page list from llms.txt, plus any sidebar page missing from it

1000 pages · 1000 converted · 0 failed · 15 blockers · 1000 flags

Run finished 2026-08-25T12:16:21.578Z.

> **This run covered 1000 of the site's 1127 pages.** Everything below describes only those — it is not a census of the site. Raise `--limit`, or drop it for the whole site.

> **12 pages will not compile as MDX.** Those pages fail to sync — see the per-page table below.

> **15 pages needed the lenient parser.** Their source has a syntax error, so they received *no component conversions at all*. Repair the source and convert again before reading anything else about them.

## Branding

| Value | Taken from | Source |
|---|---|---|
| Site name | Adaptive Media Delivery | ssr-props |
| Brand colour (light) | #017ac6 | ssr-props |
| Brand colour (dark) | #0187da | derived |
| Logo (light) | https://files.readme.io/6e06488-small-techdocs-akamai-logo.png | ssr-props |
| Favicon | https://files.readme.io/7c45921-favicon.ico | ssr-props |

> 1 value was **computed here, not read from the site** — ReadMe leaves the dark-mode brand colour unset on most projects and lightens it at render time. Check it against the live site before publishing.

Not found, so Documentation.AI's default stands: logoDark.

`heading` and `text` are deliberately left at the Documentation.AI defaults: they are chosen for contrast, and a source site's values were picked against its own background.

## Navigation

| Tab | Groups | Pages |
|---|---:|---:|
| Guide | 16 | 98 |
| API | 7 | 19 |
| Release notes | 1 | 28 |

Tabs with no navigation in them, skipped:

- **Recipes** (`/adaptive-media-delivery/recipes`) — https://techdocs.akamai.com/adaptive-media-delivery/recipes: failed to retrieve nav items from HTML. Could not find the sidebar element. This build only implements ReadMe selectors (nav.rm-Sidebar).

### Pages the sidebar could not reach

982 pages came from `llms.txt` but not the sidebar walk. On ReadMe this is normal — the sidebar omits spec-generated API endpoints, and a tab that fails to load takes its whole subtree with it.

They have been given navigation entries, so nothing ships unreachable:

- **Adaptive Acceleration** — 10 pages, in a new tab of that name
- **Adaptive Media Delivery** — 13 pages, in a new tab of that name
- **Akamai Functions** — 8 pages, in a new tab of that name
- **Alerts** — 17 pages, in a new tab of that name
- **Adaptive Media Player 2 powered by Bitmovin** — 4 pages, in a new tab of that name
- **API Acceleration** — 6 pages, in a new tab of that name
- **API Definitions** — 17 pages, in a new tab of that name
- **App Platform for LKE** — 9 pages, in a new tab of that name
- **Application Security API** — 10 pages, in a new tab of that name
- **Aura** — 3 pages, in a new tab of that name
- **Client Access Control** — 8 pages, in a new tab of that name
- **Cloud Access Manager** — 13 pages, in a new tab of that name
- **Akamai Cloud** — 11 pages, in a new tab of that name
- **Web Application Security** — 14 pages, in a new tab of that name
- **Cloud Wrapper** — 16 pages, in a new tab of that name
- **Cloudlets** — 21 pages, in a new tab of that name
- **CloudTest** — 26 pages, in a new tab of that name
- **Contract API** — 7 pages, in a new tab of that name
- **Control Center** — 7 pages, in a new tab of that name
- **CP Codes and Reporting Groups Tool** — 11 pages, in a new tab of that name
- **Certificate Provisioning System** — 11 pages, in a new tab of that name
- **DataStream 2** — 13 pages, in a new tab of that name
- **Akamai Developer Center** — 9 pages, in a new tab of that name
- **Akamai Direct Connect** — 6 pages, in a new tab of that name
- **Domain Ownership Manager** — 11 pages, in a new tab of that name
- **Download Delivery** — 10 pages, in a new tab of that name
- **Enterprise Application Access** — 20 pages, in a new tab of that name
- **Enhanced Content Control Utility API** — 8 pages, in a new tab of that name
- **Edge Diagnostics** — 29 pages, in a new tab of that name
- **Edge DNS** — 20 pages, in a new tab of that name
- **Edge IP Binding** — 7 pages, in a new tab of that name
- **EdgeKV** — 17 pages, in a new tab of that name
- **EdgeWorkers** — 25 pages, in a new tab of that name
- **SIA Configuration API** — 17 pages, in a new tab of that name
- **SIA Reporting API** — 17 pages, in a new tab of that name
- **Secure Internet Access Enterprise** — 13 pages, in a new tab of that name
- **Firewall Rules** — 10 pages, in a new tab of that name
- **Build on the cloud** — 6 pages, in a new tab of that name
- **GTM Load Feedback API** — 5 pages, in a new tab of that name
- **GTM Reporting API** — 12 pages, in a new tab of that name
- **Global Traffic Management** — 21 pages, in a new tab of that name
- **Guardicore Platform Agent** — 7 pages, in a new tab of that name
- **Akamai TechDocs** — 2 pages, in a new tab of that name
- **Identity and Access Management API** — 15 pages, in a new tab of that name
- **Invoicing API** — 7 pages, in a new tab of that name
- **Ion** — 13 pages, in a new tab of that name
- **IP Accelerator** — 6 pages, in a new tab of that name
- **Prolexic IP Protect Configuration API** — 6 pages, in a new tab of that name
- **Image and Video Manager** — 16 pages, in a new tab of that name
- **API Keys and Traffic Management** — 11 pages, in a new tab of that name
- **Linode API** — 30 pages, in a new tab of that name
- **Akamai MFA OIDC API** — 4 pages, in a new tab of that name
- **Akamai MFA** — 14 pages, in a new tab of that name
- **mPulse Boomerang** — 10 pages, in a new tab of that name
- **mPulse** — 27 pages, in a new tab of that name
- **MSL5 Powered by Harmonic** — 12 pages, in a new tab of that name
- **Mutual TLS Edge Truststore (Limited Availability)** — 11 pages, in a new tab of that name
- **Mutual TLS Origin Keystore** — 11 pages, in a new tab of that name
- **NetStorage Usage API** — 6 pages, in a new tab of that name
- **NetStorage** — 19 pages, in a new tab of that name
- **Network Lists API** — 7 pages, in a new tab of that name
- **Object Delivery** — 10 pages, in a new tab of that name
- **Deliver your first site** — 7 pages, in a new tab of that name
- **Origin IP Access Control List** — 3 pages, in a new tab of that name
- **Get to Know Akamai** — 3 pages, in a new tab of that name
- **PowerShell** — 38 pages, in a new tab of that name
- **Prolexic Analytics API** — 5 pages, in a new tab of that name
- **Property Manager** — 23 pages, in a new tab of that name
- **Purge Cache** — 12 pages, in a new tab of that name
- **Release Notes** — 3 pages, added to the existing tab
- **Reporting** — 10 pages, in a new tab of that name
- **Script Management** — 11 pages, in a new tab of that name
- **Security Center** — 7 pages, in a new tab of that name
- **Security Notification Settings** — 8 pages, in a new tab of that name
- **SIEM Integration** — 8 pages, in a new tab of that name
- **Site Shield** — 12 pages, in a new tab of that name
- **Single Sign-On Configuration API** — 5 pages, in a new tab of that name
- **Get Started** — 6 pages, in a new tab of that name
- **Terraform** — 24 pages, in a new tab of that name
- **Test Center** — 15 pages, in a new tab of that name
- **TrafficPeak** — 8 pages, in a new tab of that name
- **Zero Trust Client** — 8 pages, in a new tab of that name
- **Zero Trust Security** — 4 pages, in a new tab of that name

**Check the grouping.** `llms.txt` is a flat list; its `##` heading is the only structure there was to go on, and it is not the sidebar the source site had.

- `adaptive-acceleration/changelog/llms.txt`
- `adaptive-acceleration/docs/llms.txt`
- `adaptive-acceleration/docs/manage-your-reports/llms.txt`
- `adaptive-acceleration/docs/reporting/llms.txt`
- `adaptive-acceleration/docs/welcome/llms.txt`
- `adaptive-acceleration/llms.txt`
- `adaptive-acceleration/recipes/llms.txt`
- `adaptive-acceleration/reference/adaptive-acceleration-report/llms.txt`
- `adaptive-acceleration/reference/api/llms.txt`
- `adaptive-acceleration/reference/llms.txt`
- `adaptive-media-delivery/changelog/llms.txt`
- `adaptive-media-delivery/docs/before-you-begin/llms.txt`
- `adaptive-media-delivery/docs/configuration/llms.txt`
- `adaptive-media-delivery/docs/llms.txt`
- `adaptive-media-delivery/docs/optional-features/llms.txt`
- `adaptive-media-delivery/docs/resources/llms.txt`
- `adaptive-media-delivery/docs/welcome/llms.txt`
- `adaptive-media-delivery/llms.txt`
- `adaptive-media-delivery/recipes/llms.txt`
- `adaptive-media-delivery/reference/access-revocation/llms.txt`
- `adaptive-media-delivery/reference/amds-access-revocation-api/llms.txt`
- `adaptive-media-delivery/reference/llms.txt`
- `adaptive-media-delivery/reference/welcome/llms.txt`
- `akamai-functions/changelog/llms.txt`
- `akamai-functions/docs/limitations/llms.txt`
- `akamai-functions/docs/llms.txt`
- `akamai-functions/docs/manage-applications/llms.txt`
- `akamai-functions/docs/monitor/llms.txt`
- `akamai-functions/docs/technical-resources/llms.txt`
- `akamai-functions/docs/welcome/llms.txt`
- `akamai-functions/llms.txt`
- `alerts-app/changelog/llms.txt`
- `alerts-app/docs/get-started/llms.txt`
- `alerts-app/docs/llms.txt`
- `alerts-app/docs/manage-alerts/llms.txt`
- `alerts-app/docs/troubleshoot/llms.txt`
- `alerts-app/docs/welcome/llms.txt`
- `alerts-app/llms.txt`
- `alerts-app/recipes/llms.txt`
- `alerts-app/reference/access-control-data/llms.txt`
- `alerts-app/reference/alert-definitions/llms.txt`
- `alerts-app/reference/alert-firings/llms.txt`
- `alerts-app/reference/alert-summaries/llms.txt`
- `alerts-app/reference/api/llms.txt`
- `alerts-app/reference/llms.txt`
- `alerts-app/reference/schema/llms.txt`
- `alerts-app/reference/sparklines/llms.txt`
- `alerts-app/reference/templates/llms.txt`
- `amp2-bitmovin/docs/llms.txt`
- `amp2-bitmovin/docs/migration/llms.txt`
- …and 932 more (see `report.json`)

## Blockers

| Page | Line | Rule | Detail |
|---|---:|---|---|
| `adaptive-media-delivery/docs/welcome-adaptive-media-deliv` | 10 | magic-block | [block:html]: raw HTML has no target component — rebuild it as <Iframe>, <Columns>+<Card>, or site CSS (plan §4.3) |
| `adaptive-media-delivery/docs/understand-the-request-flow` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/prepare-your-environment` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/create-new-prop` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/define-prop-hn` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/best-practices-use-case-based-prov` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/origin-server-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/content-provider-code-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/segmented-media-deliv-mode-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/origin-charac-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/content-charac-amd` | 80 | html-table | raw <table> is split across the page rather than parsed as one element — the page is not valid MDX, so repair it first (usually an unclosed tag) and convert again |
| `adaptive-media-delivery/docs/content-charac-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/client-charac-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |
| `adaptive-media-delivery/docs/cache-key-query-param-amd` | 41 | html-table | raw <table> is split across the page rather than parsed as one element — the page is not valid MDX, so repair it first (usually an unclosed tag) and convert again |
| `adaptive-media-delivery/docs/cache-key-query-param-amd` |  | mdx | the converted page will not compile as MDX — Unexpected character `c` (U+0063) before attribute value, expected a character that can start an attribute value, such as `"`, `'`, or `{`. Fix that tag in the source and convert again; everything else on the page is fine |

## Pages

| Page | Parser | Compiles | Blockers | Flags | Fenced |
|---|---|---|---:|---:|---:|
| `adaptive-acceleration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/docs/manage-your-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/docs/reporting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/reference/adaptive-acceleration-report/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-acceleration/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/before-you-begin/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/optional-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/reference/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/reference/amds-access-revocation-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/reference/access-revocation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `amp2-bitmovin/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `amp2-bitmovin/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `amp2-bitmovin/docs/overview/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `amp2-bitmovin/docs/migration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/platform/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/identity-and-access/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/compute/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/storage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/networking/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/databases/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/monitoring/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/docs/tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-computing/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/get-credentials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/multicloud-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/security-delivery-automation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/workflow-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/docs/diagnostics-testing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `developer/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/docs/requirements/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/docs/configure/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `direct-connect/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/manage-applications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/technical-resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/monitor/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/docs/limitations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `akamai-functions/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/for-administrators/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/for-users/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/docs/administrator-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/reference/email-enrollments/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/reference/users/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/reference/groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa-oidc/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa-oidc/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa-oidc/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mfa-oidc/reference/akamai-mfa-oidc/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/docs/manage-alerts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/access-control-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/templates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/alert-summaries/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/alert-definitions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/alert-firings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/sparklines/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/reference/schema/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `alerts-app/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/docs/plan-your-implementation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/docs/configure/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-acceleration/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/define-and-register-your-apis/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/api-discovery-operation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/api-gateway-setup-and-operation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/docs/api-keys-and-traffic-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/contracts-and-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/categories/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/api-endpoints/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/api-delivery-settings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/multistep-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/reference/resources-and-operations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `api-definitions/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/key-collections/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/throttling-counters/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/keys/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/reference/tags/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `key-traffic-mgmt/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/setup/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/platform-level-usage-for-administrators/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/team-level-usage-for-devs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/docs/labs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `app-platform/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/configuration-settings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/security-policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/evaluation-mode/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/utilities-and-account-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/activation-and-export/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/reference/self-service-onboardings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `application-security/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `aura/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `aura/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `aura/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/docs/user-interface-tutorial/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/docs/api-tutorial/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `get-started-cloud-computing/docs/next-steps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/docs/create-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/docs/view-and-search/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/docs/certificate-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/reference/enrollments/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cps/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/docs/update-the-cidr-block-list/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/reference/configurations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `client-access-control/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/docs/management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/access-keys/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/property-lookups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/access-key-version-status-requests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/reference/access-key-creation-status-requests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-access-mgr/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/best-practices/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/docs/reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/capacity/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/locations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/configurations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/reference/multi-cdn/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-wrapper/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/manage-cloudlets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/configuration-and-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/application-load-balancer/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/api-prioritization/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/audience-segmentation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/edge-redirector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/forward-rewrite/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/phased-release/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/request-control/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/docs/visitor-prioritization/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/cloudlets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/activations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/active-properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/reference/policy-versions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudlets/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/manage-cloudtest/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/reference-topics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/cloudtest-components/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/developer-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/best-practices/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/docs/tutorials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/cloud-servers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/test-environments/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/grid-provisioning/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/compositions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/objects/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/results-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/query-results/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/results-database/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/seed-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/server-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/tenant-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/reference/tokens/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloudtest/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/reference/contracts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/reference/reporting-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `contract-api/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/docs/global-menu/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/docs/homepage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/docs/page-header/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `control-ctr/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/docs/manage-cp-codes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/docs/manage-reporting-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/reference/cp-codes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/reference/reporting-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cp-codes/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/answerx-rdns-logs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/security-logs-siem/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/manage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/reference/datastream-2-configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `datastream2/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/docs/use-control-center/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/docs/use-apis/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/docs/whats-next/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `onboard/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/docs/manage-domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/docs/troubleshooting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/reference/domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `domain-validation/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/before-you-begin/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/optional-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/docs/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/reference/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `download-delivery/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/docs/tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/docs/problem-scenarios/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/docs/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/edge-server-locations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/ip-verification/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/ip-network-location/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/ip-verification-and-location/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/gtm-properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/ipa-hostnames/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/error-translator/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/user-diagnostic-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/error-statistics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/metadata-tracer/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/esi-debugger/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/curl/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/grep/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/arl-translator/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/dig/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/mtr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/url-health-check/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/connectivity-problems/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/reference/content-problems/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-diagnostics/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/configure-and-manage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/manage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/monitor-and-report/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/protect-origin-infrastructure-with-dns-proxy/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/zones/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/zone-versions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/change-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/data-services/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/bulk-zones/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/tsig-keys/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/shield-ns53/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/reference/record-sets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-dns/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/docs/create-edge-ip-binding-in-property-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/docs/the-edge-ip-binding-tool/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/docs/optional-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edge-ip-binding/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/prerequisites/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/technical-resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/administrative-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/debug-and-monitor/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/docs/limitations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/initialize/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/access-tokens/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/authorization/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/reference/namespaces-and-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgekv/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/prerequisites/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/development/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/javascript-api-reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/technical-resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/debug/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/monitor/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/docs/limitations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/resource-tiers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/edgeworker-ids/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/validations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/contracts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/secure-token/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/edgeworkers-customer-log-delivery/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/reference/limits/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `edgeworkers/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/reference/permissions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/reference/properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/reference/requests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eccu/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/secure-your-network/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/authenticate-users/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/create-applications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/connector-and-applications-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/login-portal-customization/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/monitor/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/logs-metrics-and-siem-integration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/create-client-based-applications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/use-eaa-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/eaa-client-for-ubuntu-desktop/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/eaa-client-advanced-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/device-posture/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/performance-optimizations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/docs/non-ga-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `eaa/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/reference/cidr-blocks/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/reference/services/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/reference/subscriptions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `firewall-rules/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/docs/set-up-your-product/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/docs/activate-test-and-go-live/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `start/docs/settings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `platform-basics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `platform-basics/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `platform-basics/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/property-types/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/configure-and-manage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/docs/monitor-and-report/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/gtm-versioned-objects/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/identity/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/cidr-maps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/autonomous-system-maps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/geographic-maps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/data-centers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/status/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/reference/collections/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-load-feedback/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-load-feedback/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-load-feedback/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-load-feedback/reference/global-traffic-management-load-feedback-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-load-feedback/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/domain-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/demand/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/ip-availability/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/latency/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/liveness-tests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/load-feedback/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/traffic/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/reference/diagnostics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `gtm-reporting/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/docs/desktop-agent/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/docs/enterprise-center-for-guardicore-platform-agent/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `guardicore-platform-agent/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/roles/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/users-for-administrators/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/your-user-profile/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/common-resources-for-administrators/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/common-resources-for-users/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/ip-access-control-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/api-clients-administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/reference/api-client-credentials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `iam-api/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/hello-world-tutorials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/administration-and-monitoring/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/use-cases-and-examples/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/images/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/image-video-manager-policy-sets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/reference/log-error-details/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ivm/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/reference/invoices/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/reference/notifications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `invoicing/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/before-you-begin/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/guided-configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/custom-configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/tutorials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/optional-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/docs/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/reference/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/reference/api-tutorials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ion/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/how-tos-knowledge-base/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/troubleshooting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/reference-topics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/docs/developer-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/reference/mpulse-boomerang-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse-boomerang/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/docs/features-and-functionality/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/docs/setup-administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-accelerator/docs/monitoring/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/llms.txt` | markdown | yes | 0 | 1 | 0 |
| `linode-api/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/beta-programs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/databases/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/identity-and-access/llms.txt` | markdown | yes | 0 | 1 | 0 |
| `linode-api/reference/images/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/linode-instances/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/linode-kubernetes-engine-lke/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/linode-stackscripts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/longview/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/maintenance/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/managed/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/marketplace/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/monitor/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/network-transfer-prices/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/networking/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/nodebalancers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/object-storage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/placement-groups/llms.txt` | markdown | yes | 0 | 1 | 0 |
| `linode-api/reference/profile/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/regions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/resource-locking/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/support/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/tags/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/volumes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/reference/vpcs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `linode-api/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/new-ui/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/quick-start/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/customize-your-web-app-configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/explore-mpulse-system-dashboards-and-widgets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/manage-custom-dashboards/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/manage-dashboard-widgets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/track-and-report-performance-activity/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/manage-mpulse-users/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/monitor-application-performance/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/customize-time-zones-and-locales/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/view-your-mpulse-timeline-events/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/manage-your-mpulse-environment-with-boomerang-self-service/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/docs/reference-topics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/tokens/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/objects/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/alerts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/annotations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/queries/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/reference/beacons/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mpulse/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/overview/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/migration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/msl5-user-interface-guide/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/reports-and-logs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/docs/specifications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/reference/media-services-live-api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `msl5-harmonic/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/docs/manage-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/reference/ca-sets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/reference/ca-set-versioning/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/reference/certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-edge-truststore/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/docs/manage-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/reference/account-ca-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/reference/client-certificate-versions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/reference/client-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `mtls-origin-keystore/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/developer-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/best-practices/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/netstorage-cp-codes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/storage-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/upload-accounts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/replication-zones/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/acl-rule-sets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/reference/site-snapshots/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/reference/usage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `netstorage-usage/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/reference/network-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/reference/activations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/reference/notifications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `network-lists/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/before-you-begin/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/configuration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/optional-features/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/docs/resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/reference/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `object-delivery/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `origin-ip-acl/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `origin-ip-acl/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `origin-ip-acl/docs/documentation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/api-definitions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/api-key-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/appsec/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/china-cdn/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/client-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/cloud-access-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/cloud-wrapper/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/cloudlets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/common/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/contracts/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/cp-codes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/datastream/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/domain-ownership/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/edge-diagnostics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/edge-dns/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/edge-hostnames/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/edgekv/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/edgeworkers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/firewall-rules-notification/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/global-traffic-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/identity-access-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/image-video-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/media-services-live/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/mutual-tls-edge-truststore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/mutual-tls-origin-keystore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/netstorage/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/network-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/property/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/purge/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/reporting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/siem/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/site-shield/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/sla/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `powershell/docs/test-center/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `prolexic/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `prolexic/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `prolexic/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `prolexic/reference/prolexic-analytics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `prolexic/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/docs/manage-your-policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/docs/additional-resources/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/reference/insights/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/reference/policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `script-management/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/reference/mapped-ip-addresses/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/reference/policy-domains/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `ip-protect/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/property-hostnames/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/variables/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/property-configuration-settings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/activation-and-testing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/docs/miscellaneous/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/rule-configurations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/prerequisite-data/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/includes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/property-hostnames/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/properties/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/custom-behaviors-and-overrides/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/bulk-search-and-update/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/search/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/rule-formats-schemas-and-utilities/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/reference/domain-ownership-validation-challenges/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `property-mgr/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/docs/fast-purge/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/docs/enhanced-purge/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/reference/invalidations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/reference/deletions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/reference/rate-limit-status/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `purge-cache/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `release-notes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `release-notes/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `release-notes/docs/documentation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/docs/use-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/docs/report-types/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/reference/reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `reporting/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/docs/security-hub/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/docs/web-security-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/docs/web-security-analytics/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-ctr/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/email-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/notification-channels/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/docs/troubleshooting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `security-notification-settings/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/manage-sia/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/manage-sia-proxy/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/manage-etp-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/manage-security-connector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/analyze-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/enterprise-threat-intelligence/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/developer-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/policies/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/data-loss-prevention-dictionary/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/configurations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/security-connectors/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/deployments/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/custom-responses/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/sites/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/client-configurations/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/notifications/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/connection-credentials/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/reference/tenant-and-delegated-access/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-config/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/threat-event-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/aup-event-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/dns-activity-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/security-connector-event-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/idp-systems-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/indicators-of-compromise-ioc-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/deepscan-event-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/threat-metadata-report/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/feedback-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/report-schedules/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/network-traffic-connections-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/proxy-traffic-transactions-reports/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/reference/threat-intelligence/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `etp-reporting/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/reference/security-events/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `siem-integration/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `sso-config/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `sso-config/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `sso-config/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `sso-config/reference/manage-certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `sso-config/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/administration/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/maintenance/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/docs/developer-tools/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/reference/maps/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `site-shield/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/get-started/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/identity-and-access-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/property/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/reporting-groups/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/application-security/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/api-definitions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/bot-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/client-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/network-lists/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/account-protector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/edge-dns/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/certificates/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/image-and-video-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/global-traffic-management/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/cloud-wrapper/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/cloudlets/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/edgeworkers/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/datastream/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/cloud-access-manager/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/mutual-tls-origin-keystore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/mutual-tls-edge-truststore/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `terraform/docs/archive/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/docs/functional-testing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/docs/comparative-testing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/docs/both-tests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/api/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/test-runs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/functional-testing/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/test-catalog-template/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/test-requests/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/reference/functions/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/recipes/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `test-ctr/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/overview/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/dashboards/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/create-dashboards/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/query-interfaces/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/docs/manage-grafana/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `trafficpeak/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/app-api-protector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/app-api-protector-hybrid/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/manage-bots/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/content-protector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/account-protector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/firewall-for-ai/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/client-side-protection-compliance/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/brand-protector/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/protect-your-apis/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/docs/more-info/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `cloud-security/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/desktop-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/mobile-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/enterprise-center-for-zero-trust-client/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/docs/troubleshoot/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-client/changelog/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-security/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-security/docs/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-security/docs/welcome/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `zero-trust-security/docs/akamai-guardicore-segmentation/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `home/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `home/page/llms.txt` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/welcome-adaptive-media-deliv` | mdx | yes | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/key-concepts-and-terms` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/supported-media-formats` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/get-environ-info` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/understand-the-request-flow` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/prepare-your-environment` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/create-new-prop` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/define-prop-hn` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/define-prop-vars-optal` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/define-prop-config-settings` | mdx | yes | 0 | 1 | 0 |
| `adaptive-media-delivery/docs/best-practices-use-case-based-prov` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/origin-server-amd` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/content-provider-code-amd` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/segmented-media-deliv-mode-amd` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/origin-charac-amd` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/content-charac-amd` | markdown | **no** | 2 | 1 | 0 |
| `adaptive-media-delivery/docs/client-charac-amd` | markdown | **no** | 1 | 1 | 0 |
| `adaptive-media-delivery/docs/cache-key-query-param-amd` | markdown | **no** | 2 | 1 | 0 |
