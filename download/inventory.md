# Component inventory — https://developer.drivewealth.com

217 pages · 4439 blocks · 17 distinct constructs · 16 pages needed the lenient parser

Page list from `llms.txt`.

## What is on the site, and what it becomes

| Construct | Syntax | Uses | Pages | Documentation.AI | Status | Note |
| --- | --- | ---: | ---: | --- | --- | --- |
| `paragraph` | markdown | 1650 | 211 | plain markdown | direct |  |
| `heading` | markdown | 1369 | 217 | plain markdown | direct |  |
| `code` | markdown | 379 | 139 | plain markdown | direct |  |
| `list` | markdown | 266 | 94 | plain markdown | transform | normalise `*`/`+` markers to `-` |
| `boilerplate` | markdown | 217 | 217 | plain markdown | drop | ReadMe's injected llms.txt preamble |
| `Table` | markdown | 209 | 78 | plain markdown | direct | GFM table; watch for an empty `| |` header row |
| `Callout` | markdown | 121 | 59 | `<Callout>` | direct | theme/icon -> kind; drop the emoji, Documentation.AI draws its own |
| `br` | html | 97 | 55 | plain markdown | drop | <br /> is not needed — blocks are spaced by the parser |
| `Image` | jsx | 42 | 24 | `<Image>` | transform | keep src/alt (+ width/height when real); drop align, border, className, and width="smart" |
| `thematicBreak` | markdown | 42 | 11 | plain markdown | direct |  |
| `CodeTabs` | markdown | 26 | 17 | `<CodeGroup>` | transform | tab name goes on BOTH the fence and tabs={["a","b"]} |
| `blockquote` | markdown | 14 | 13 | plain markdown | direct |  |
| `button` | html | 3 | 3 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `TutorialTile` | jsx | 1 | 1 | plain markdown | manual | deprecated alias of Recipe |
| `Embed` | jsx | 1 | 1 | `<Video>` | transform | YouTube/Vimeo/Loom -> <Video src>; anything else -> <Iframe src width height> |
| `HTMLBlock` | jsx | 1 | 1 | plain markdown | manual | raw HTML+CSS+JS has no equivalent — rebuild with Cards/Columns/Steps, or drop |
| `RssCopyButton` | jsx | 1 | 1 | plain markdown | manual | unrecognised component — not in the ReadMe reference or the Documentation.AI set |

## No direct equivalent — decide before converting

- `button` (3× on 3 pages) — raw HTML — check it against the Documentation.AI components. e.g. apis/changelog/release-notes-2026-08-13#5, apis/changelog/release-notes-2026-08-19#5, apis/changelog/release-notes-2026-08-25#4
- `TutorialTile` (1× on 1 pages) — deprecated alias of Recipe. e.g. apis/docs/fixed-income#3
- `HTMLBlock` (1× on 1 pages) — raw HTML+CSS+JS has no equivalent — rebuild with Cards/Columns/Steps, or drop. e.g. apis/docs/showing-disclosures#2
- `RssCopyButton` (1× on 1 pages) — unrecognised component — not in the ReadMe reference or the Documentation.AI set. e.g. apis/docs/subscribe-to-api-updates#9

## Not carried over

- `boilerplate` (217×) — ReadMe's injected llms.txt preamble
- `br` (97×) — <br /> is not needed — blocks are spaced by the parser

## Inline syntax

| Kind | Uses | Pages | Examples |
| --- | ---: | ---: | --- |
| breakTag | 200 | 59 | `<br />` `<br />` `<br />` `<br />` `<br />` |
| handlebars | 180 | 59 | `{{bo-username}}` `{{bo-password}}` `{{bo-url}}` `{{acctid}}` `{{bo-url}}` |
| absoluteInternalLink | 36 | 17 | `https://developer.drivewealth.com/reference/errors-1` `https://developer.drivewealth.com/reference/simulate-kyc-failures` `https://developer.drivewealth.com/reference/subscription-events` `https://developer.drivewealth.com/reference/bank-account-events` `https://developer.drivewealth.com/reference/edit-account` |
| anchorJsx | 36 | 11 | `https://developer.drivewealth.com/apis/docs/api-lifecycle-guide` `https://developer.drivewealth.com/apis/docs/common-data-types` `https://developer.drivewealth.com/apis/docs/retrieve-account-summary-migration-guide` `https://developer.drivewealth.com/apis/changelog` `https://developer.drivewealth.com/apis/changelog` |
| markdownImage | 20 | 9 | `https://files.readme.io/ce188d1-Screenshot_2023-04-23_at_10.31.49_PM.png` `https://files.readme.io/8b3b462-Screenshot_2023-04-23_at_10.32.13_PM.png` `https://files.readme.io/ee0c936-Screenshot_2023-04-23_at_10.32.23_PM.png` `https://files.readme.io/2e8011b-Screenshot_2023-09-05_at_12.43.18_PM.png` `https://files.readme.io/1e6db6a-Screenshot_2023-09-05_at_12.41.46_PM.png` |
| escapedAngle | 3 | 2 | `\<data>` `\<partnerID>` `\<partnerID>` |

## Flagged for repair

| Issue | Occurrences | Examples |
| --- | ---: | --- |
| no alt text — Documentation.AI pages need one | 38 | apis/changelog/247-cash-rewards#13, apis/changelog/api-release-162#12, apis/changelog/dh-release-2154#10 |
| `curl` is not a highlighter language — use bash | 11 | apis/docs/self-managed-super-fund-smsf-account-onboarding-guide#11, apis/docs/self-managed-super-fund-smsf-account-onboarding-guide#17, apis/docs/self-managed-super-fund-smsf-account-onboarding-guide#21 |
| className="border" is redundant with border={true} | 9 | apis/docs/official-documents#6, apis/docs/official-documents#9, apis/docs/official-documents#10 |
| reassembled from several raw-HTML chunks — this page needed the lenient parser | 4 | apis/docs/creating-an-order#28, apis/docs/options-1#22, apis/docs/single-sign-on-sso#3 |
| string style="…" outside HTMLBlock is invalid MDX | 3 | apis/changelog/release-notes-2026-08-13#5, apis/changelog/release-notes-2026-08-19#5, apis/changelog/release-notes-2026-08-25#4 |
| width="smart" is a legacy RDMD value — drop it | 1 | apis/docs/official-documents#6 |

## Pages that failed the strict MDX parse

These use ReadMe's lenient MDXish dialect. They are fully blocked out, but the syntax needs
repairing before Documentation.AI will compile them.

- apis/changelog/api-release-129
- apis/changelog/api-release-158
- apis/changelog/api-release-160
- apis/changelog/api-release-161
- apis/changelog/api-release-162
- apis/changelog/api-release-1640
- apis/changelog/api-release-1660
- apis/docs/creating-an-order
- apis/docs/delistings-going-private
- apis/docs/options-1
- apis/docs/options-chain
- apis/docs/retirement-accounts
- apis/docs/setting-up-ssowith-okta
- apis/docs/single-sign-on-sso
- apis/reference/accountperformance
- apis/reference/enums
