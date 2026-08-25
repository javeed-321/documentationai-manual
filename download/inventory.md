# Component inventory — https://techdocs.akamai.com

1000 pages · 6824 blocks · 17 distinct constructs · 16 pages needed the lenient parser

Page list from `llms.txt`.

## What is on the site, and what it becomes

| Construct | Syntax | Uses | Pages | Documentation.AI | Status | Note |
| --- | --- | ---: | ---: | --- | --- | --- |
| `heading` | markdown | 2757 | 1000 | plain markdown | direct |  |
| `list` | markdown | 1750 | 1000 | plain markdown | transform | normalise `*`/`+` markers to `-` |
| `blockquote` | markdown | 982 | 982 | plain markdown | direct |  |
| `boilerplate` | markdown | 917 | 917 | plain markdown | drop | ReadMe's injected llms.txt preamble |
| `paragraph` | markdown | 307 | 101 | plain markdown | direct |  |
| `td` | html | 43 | 2 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `div` | html | 22 | 12 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `tr` | html | 18 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `Callout` | markdown | 11 | 9 | `<Callout>` | direct | theme/icon -> kind; drop the emoji, Documentation.AI draws its own |
| `table` | html | 3 | 2 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `code` | markdown | 2 | 1 | plain markdown | direct |  |
| `caption` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `colgroup` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `col` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `thead` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `th` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |
| `tbody` | html | 2 | 1 | plain markdown | manual | raw HTML — check it against the Documentation.AI components |

## No direct equivalent — decide before converting

- `td` (43× on 2 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/cache-key-query-param-amd#17, adaptive-media-delivery/docs/cache-key-query-param-amd#19, adaptive-media-delivery/docs/cache-key-query-param-amd#21
- `div` (22× on 12 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/best-practices-use-case-based-prov#9, adaptive-media-delivery/docs/best-practices-use-case-based-prov#14, adaptive-media-delivery/docs/cache-key-query-param-amd#7
- `tr` (18× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#36, adaptive-media-delivery/docs/content-charac-amd#39, adaptive-media-delivery/docs/content-charac-amd#42
- `table` (3× on 2 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/cache-key-query-param-amd#15, adaptive-media-delivery/docs/content-charac-amd#28, adaptive-media-delivery/docs/content-charac-amd#108
- `caption` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#29, adaptive-media-delivery/docs/content-charac-amd#30
- `colgroup` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#31, adaptive-media-delivery/docs/content-charac-amd#34
- `col` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#32, adaptive-media-delivery/docs/content-charac-amd#33
- `thead` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#35, adaptive-media-delivery/docs/content-charac-amd#40
- `th` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#37, adaptive-media-delivery/docs/content-charac-amd#38
- `tbody` (2× on 1 pages) — raw HTML — check it against the Documentation.AI components. e.g. adaptive-media-delivery/docs/content-charac-amd#41, adaptive-media-delivery/docs/content-charac-amd#107

## Not carried over

- `boilerplate` (917×) — ReadMe's injected llms.txt preamble

## Inline syntax

| Kind | Uses | Pages | Examples |
| --- | ---: | ---: | --- |
| refLink | 1684 | 138 | `ref:post-revocation-list-ids` `ref:post-unrevoke-revocation-list-ids` `ref:post-revocation-list-ids` `ref:post-unrevoke-revocation-list-ids` `ref:get-active-alert-firings` |
| docLink | 82 | 26 | `doc:get-policy-rules` `doc:put-policy-rapid-rule-action` `doc:put-policy-rapid-rule-action` `doc:put-policy-rapid-rule-action` `doc:post-subscribe` |
| variable | 2 | 2 | `LB` `LB` |
| escapedAngle | 1 | 1 | `\<Media Format>` |

## Pages that failed the strict MDX parse

These use ReadMe's lenient MDXish dialect. They are fully blocked out, but the syntax needs
repairing before Documentation.AI will compile them.

- adaptive-media-delivery/docs/best-practices-use-case-based-prov
- adaptive-media-delivery/docs/cache-key-query-param-amd
- adaptive-media-delivery/docs/client-charac-amd
- adaptive-media-delivery/docs/content-charac-amd
- adaptive-media-delivery/docs/content-provider-code-amd
- adaptive-media-delivery/docs/create-new-prop
- adaptive-media-delivery/docs/define-prop-hn
- adaptive-media-delivery/docs/origin-charac-amd
- adaptive-media-delivery/docs/origin-server-amd
- adaptive-media-delivery/docs/prepare-your-environment
- adaptive-media-delivery/docs/segmented-media-deliv-mode-amd
- adaptive-media-delivery/docs/understand-the-request-flow
- adaptive-media-delivery/docs/welcome-adaptive-media-deliv
- linode-api/reference/identity-and-access/llms.txt
- linode-api/reference/llms.txt
- linode-api/reference/placement-groups/llms.txt
