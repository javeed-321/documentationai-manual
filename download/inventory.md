# Component inventory — https://modulr.readme.io

371 pages · 4742 blocks · 17 distinct constructs · 20 pages needed the lenient parser

Page list from `llms.txt`.

## What is on the site, and what it becomes

| Construct | Syntax | Uses | Pages | Documentation.AI | Status | Note |
| --- | --- | ---: | ---: | --- | --- | --- |
| `paragraph` | markdown | 1926 | 349 | plain markdown | direct |  |
| `heading` | markdown | 1263 | 371 | plain markdown | direct |  |
| `boilerplate` | markdown | 371 | 371 | plain markdown | drop | ReadMe's injected llms.txt preamble |
| `code` | markdown | 345 | 254 | plain markdown | direct |  |
| `list` | markdown | 248 | 109 | plain markdown | transform | normalise `*`/`+` markers to `-` |
| `Callout` | jsx | 194 | 86 | `<Callout>` | direct | theme/icon -> kind; drop the emoji, Documentation.AI draws its own |
| `Image` | jsx | 106 | 46 | `<Image>` | transform | keep src/alt (+ width/height when real); drop align, border, className, and width="smart" |
| `Table` | markdown | 104 | 59 | plain markdown | direct | GFM table; watch for an empty `| |` header row |
| `br` | html | 93 | 44 | plain markdown | drop | <br /> is not needed — blocks are spaced by the parser |
| `thematicBreak` | markdown | 52 | 12 | plain markdown | direct |  |
| `CodeTabs` | markdown | 17 | 11 | `<CodeGroup>` | transform | tab name goes on BOTH the fence and tabs={["a","b"]} |
| `blockquote` | markdown | 8 | 5 | plain markdown | direct |  |
| `html` | html | 6 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `Accordion` | jsx | 5 | 1 | `<Expandable>` | transform | wrap sibling runs in <ExpandableGroup>; default-open="false" |
| `tbody` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `thead` | html | 1 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `ol` | html | 1 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |

## No direct equivalent — decide before converting

- `html` (6× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. recipes/hmac-authentication#5, recipes/hmac-authentication#8, recipes/hmac-authentication#11
- `tbody` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. docs/managing-direct-debit-indemnity-claims-ddic#31, docs/managing-direct-debit-indemnity-claims-ddic#33
- `thead` (1× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. docs/managing-direct-debit-indemnity-claims-ddic#30
- `ol` (1× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. reference/editcustomer#3

## Not carried over

- `boilerplate` (371×) — ReadMe's injected llms.txt preamble
- `br` (93×) — <br /> is not needed — blocks are spaced by the parser

## Inline syntax

| Kind | Uses | Pages | Examples |
| --- | ---: | ---: | --- |
| absoluteInternalLink | 442 | 121 | `https://modulr.readme.io/docs/mobile-app` `https://modulr.readme.io/docs/api-integration-overview` `https://modulr.readme.io/docs/outbound-payments` `https://modulr.readme.io/docs/card-reports` `https://modulr.readme.io/docs/card-report-notifications` |
| breakTag | 132 | 46 | `<br />` `<br />` `<br />` `<br />` `<br />` |
| handlebars | 96 | 4 | `{{ textAlign: "left" }}` `{{ textAlign: "left" }}` `{{ textAlign: "left" }}` `{{ textAlign: "left" }}` `{{ textAlign: "left" }}` |
| markdownImage | 52 | 26 | `https://files.readme.io/27ccd4f0302cde6d7c04180920c038f44f71c684e5c387df4435993885a810e3-image.png` `https://files.readme.io/952a47c84345fdab6da48e1a7a45dee334dd1bbb3aef8c0fbfbd2a29b82b5cdf-image.png` `https://files.readme.io/18aa3775103e380d03ea6a52f08bc593eace703e3f3327cdab012904ced6ac8e-image.png` `https://files.readme.io/8949a3d7ba53d82ed0f37ab56470e13fe30fabfe92714bef6762ecb435a979c5-image.png` `https://files.readme.io/3e898bcb9f90b80fd370bde715e20ce25bf28d1c96d00a34af0784b2fd76cc0e-image.png` |
| anchorJsx | 13 | 2 | `https://modulr.readme.io/reference/createapplication` `https://modulr.readme.io/reference/createapplicationassociate` `https://modulr.readme.io/reference/updateknowyourcustomerbyapplicationid` `https://modulr.readme.io/reference/updatepersonalinformationforassociate_1` `https://modulr.readme.io/reference/updatetaxresidenciesforassociate_1` |
| refLink | 3 | 1 | `ref:suspendcard` `ref:unsuspendcard` `ref:expireauthorisation` |

## Flagged for repair

| Issue | Occurrences | Examples |
| --- | ---: | --- |
| no alt text — Documentation.AI pages need one | 97 | changelog/modconnect-annual-round-up#3, changelog/modconnect-annual-round-up#18, changelog/modconnect-april-2024#3 |
| reassembled from several raw-HTML chunks — this page needed the lenient parser | 28 | changelog/modconnect-july-2024#2, changelog/modconnect-june-2023#2, changelog/modconnect-quarterly-round-up#2 |
| className="border" is redundant with border={true} | 5 | changelog/modconnect-june-2023#17, changelog/modconnect-june-2023#20, docs/apis-to-aid-with-reconciliation#11 |
| `curl` is not a highlighter language — use bash | 1 | docs/getting-started-with-virtual-cards#13 |
| width="smart" is a legacy RDMD value — drop it | 1 | docs/setting-up-mandates#7 |
| unclosed <br> is invalid MDX | 1 | reference/createcollectionschedule#6 |

## Pages that failed the strict MDX parse

These use ReadMe's lenient MDXish dialect. They are fully blocked out, but the syntax needs
repairing before Documentation.AI will compile them.

- changelog/modconnect-july-2024
- changelog/modconnect-july-2025
- changelog/modconnect-june-2023
- changelog/modconnect-quarterly-round-up
- changelog/modconnect-quarterly-round-up-2024
- changelog/modconnect-september-2024
- changelog/your-modulr-product-update-may-2026
- docs/api-base-urls
- docs/build-with-ai-mcp
- docs/card-transaction-lifecycle
- docs/gaining-use-of-the-api
- docs/implementation-notes
- docs/inbound-payments-via-swift
- docs/managing-direct-debit-indemnity-claims-ddic
- docs/outbound-payments
- docs/provisioning-journey-1
- docs/starting-collections
- docs/third-party-providers-access
- recipes/hmac-authentication
- reference/editcustomer
