---
updatedAt: 2026-08-23T15:59:36.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# DriveWealth MCP server

## Overview

DriveWealth MCP Server is a Model Context Protocol (MCP) gateway that provides AI-native access to DriveWealth APIs and API documentation.

Instead of building custom REST wrappers for each AI platform, Correspondent Clients connect once to the MCP endpoint and use standard MCP methods to discover and invoke tools, prompts and resources.

## Typical Correspondent Client Use Cases

Below are a few practical use cases for connecting to DriveWealth MCP Server.

### Correspondent Client Internal Operations

Support and operations teams can ask AI applications to retrieve account details, KYC status, positions, and order history in a single natural-language interaction.

### Client-Facing Product Features

Correspondent Clients can embed AI chat capabilities so end-users can ask portfolio and account questions that map to position, order, statement, and account tools.

### Compliance and Risk

Compliance and risk teams can automate periodic checks by chaining transaction, account, and order history tools and applying local policy logic.

### Developer Productivity

Engineers connect IDE AI applications to describe workflows in plain language, and validate integration behavior quickly without manually assembling every request.

## Architecture at a Glance

* Your AI client (Copilot, Claude, Kiro, Cursor and custom AI agents) sends MCP requests.
* DriveWealth MCP validates auth and permission scope.
* MCP routes the request to the correct DriveWealth API operation.
* Response is returned in MCP tool output format.

MCP transport and protocol are separate concepts:

* **Protocol:** MCP method contract and JSON-RPC request/response format.
* **Transport:** HTTP, Streamable HTTP.

## Authentication & Security

### Credentials

Correspondent Clients use:

* A new set of credentials (`client-id` + `client-secret`, and `client-app-key`) provisioned with MCP access and a list of permissioned endpoints.
* A bearer token obtained from the existing DriveWealth API auth flow.
* A client application key sent in the `dw-client-app-key` header.

### Permission Model

* MCP enforces permissions at the tool level.
* `tools/list` returns only tools authorized for your credential scope.
* Unauthorized tool calls are denied even if the tool name is known.

### Network Controls

* IP allowlisting is supported for connections.
* MCP IP allowlisting is separate from API IP allowlisting.
* TLS is required for hosted HTTP transport.

## Environments

### UAT

UAT is the starting environment for all Correspondent Clients onboarding.

| Setting   | UAT Value                                 |
| :-------- | :---------------------------------------- |
| MCP URL   | `https://mcp-api.drivewealth.io/mcp`      |
| Transport | Streamable HTTP                           |
| Protocol  | JSON-RPC 2.0 over MCP methods             |
| Auth      | Bearer token + `dw-client-app-key` header |
| Data      | Test data only                            |

### Production

For production access and timelines, please contact your DriveWealth Relationship Management representative

## Quickstart: Verify Your Connection

Once connected, confirm the connection with a natural-language prompt rather than a raw protocol call:

`”List all the tools”`

This prompt should return all the entitled tool calls for your keys.

## Sample Prompts

These map each prompt to the specific tool(s) it should invoke, based on the tool catalog.

### Control-plane (operate on accounts and orders)

| `"Find the account for accountID A123456789 and summarize its cash, margin, and current positions."` |
| :--------------------------------------------------------------------------------------------------- |
| `"Show me this account's resting orders and anything that filled in the last 30 days."`              |
| `"Place a market order to buy 10 shares of AAPL on account DW1234567."`                              |
| `"Cancel order O987654 if it's still resting."`                                                      |
| `"What's the current quote for AAPL and MSFT?"`                                                      |
| `"Initiate a $500 ACH deposit into account DW1234567 from bank account B4567."`                      |
| `"Transfer all positions from account A to account B under the same owner."`                         |

### Data-plane (understand the API)

| `"What fields are required to create an account, and what account management types are supported?"` |
| :-------------------------------------------------------------------------------------------------- |
| `"Which tool do I use to cancel a resting order, and what does it need?"`                           |
| `"What's the difference between an ACATS transfer and an internal asset transfer?"`                 |
| `"What countries are currently supported for onboarding?"`                                          |

## Reliability & Operations

Recommended client behavior:

* Implement retry with exponential backoff for transient transport failures.
* Do not retry authorization failures until credentials are refreshed or corrected.
* Apply request timeouts suitable for your user experience target.
* Use read-only tools first when validating new environments.
* Log request ID, tool name, and response status for troubleshooting and audits.

## Error Handling & Troubleshooting

| Symptom                        | Probable Cause                       | Action                                                                |
| :----------------------------- | :----------------------------------- | :-------------------------------------------------------------------- |
| `tools/list` returns empty set | Credential scope has no mapped tools | Confirm entitlement mapping and app key selection.                    |
| `Unauthorized` on `tools/call` | Tool outside permission scope        | Validate Correspondent Clients permission mapping for that operation. |
| Authentication errors          | Expired/invalid bearer token         | Refresh token and retry.                                              |
| Tool not found                 | Tool name mismatch or not entitled   | Re-run `tools/list`; use exact tool name.                             |
| Slow response                  | Upstream dependency latency          | Add timeout and retry policy, then escalate with correlation ID.      |

## AI Action Safety

Several tools in this catalog perform write operations with real financial effect once executed: `create_order`, `create_withdrawal`, `create_acats_transfer`, `create_deposit`, and others across the Orders, Funding, and Asset Transfers categories.

Review any AI-proposed call to one of these tools before it executes — confirm the account, amounts, and instrument are correct, particularly for orders involving non-standard order types (`LIMIT`, `STOP`, `MARKET_IF_TOUCHED`) or transfers moving full-account balances (`FULL`, `ALL_CASH`, `ALL_POSITIONS` transfer types).

## Regulatory Disclosures

**I. Supervision and Supervisory Control Systems (FINRA Rule 3110)**<br />The Correspondent Client is solely responsible for establishing, maintaining, and enforcing written supervisory procedures (WSPs) regarding the use of AI agents accessing the MCP Server. Correspondent Clients must ensure that all AI-generated orders are subject to reasonable supervisory oversight, internal compliance validation, and exception reporting.  Correspondent Clients must ensure that all orders comply with FINRA, SEC, National Securities Exchange, and all U.S. Federal Security Laws. DriveWealth disclaims all liability for the Correspondent Client’s failure to supervise AI-initiated trading activity.

**II. Suitability Obligations (FINRA Rule 2111)**<br />The MCP Server provides technical access to execution endpoints and does not perform suitability, “know your customer” (KYC), or anti-money laundering (AML) checks at the point of order execution. The Correspondent Client assumes full responsibility for ensuring that any AI-generated transaction complies with FINRA Rule 2111 (Suitability) and all other applicable regulatory obligations relevant to the underlying account holder.

**III. Algorithmic and AI-Model Risk (FINRA Rule 2010)**<br />Correspondent Clients acknowledge that AI-based systems can exhibit non-deterministic behavior (“hallucinations”) and may misinterpret natural language instructions. It is incumbent upon the Correspondent Client to test and validate the AI agent’s interpretation of tools and schema before deploying to production. DriveWealth is not liable for unintended order execution resulting from misinterpreted prompts or erroneous AI agent logic.

**IV. Access and Cybersecurity (Regulation S-P; FINRA Rule 4511)**<br />Correspondent Client assumes absolute liability for the security of its API keys, client-app-keys, and bearer tokens. Any transaction executed via valid credentials will be deemed authorized by the Correspondent Client. Correspondent Clients must implement robust credential rotation policies and notify DriveWealth immediately upon any suspected compromise of access credentials.

**V. Execution and Market Integrity (FINRA Rule 5310)**<br />**Mandatory Human-in-the-Loop (HITL) Validation:** For all high-risk operations—including but not limited to create\_order, create\_withdrawal, and create\_acats\_transfer—the Correspondent Client must implement a mandatory review process that requires human authorization of the transaction parameters before the execution call is broadcast to the DriveWealth API. Automated execution of such tools without human review is prohibited.