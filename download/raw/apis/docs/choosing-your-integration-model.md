---
updatedAt: 2026-07-13T22:45:28.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Choosing your integration model

Before building your funding integration, you need to decide how money moves between your customers and DriveWealth. This decision affects your API architecture, your regulatory obligations, your settlement operations, and what your customers experience.

DriveWealth supports four funding models. The right one depends on whether you custody customer cash, how many customers you're funding at once, and how visible the brokerage layer is to your end users.

***

## **The four models at a glance**

|                               | Individual      | Bulk             | Cashless              | Omnibus                 |
| :---------------------------- | :-------------- | :--------------- | :-------------------- | :---------------------- |
| Customer accounts at DW       | Yes             | Yes              | Yes                   | No — one master account |
| Who holds customer cash       | DriveWealth     | Client           | Client                | Client                  |
| Customer initiates deposit    | Yes             | No — client does | No — no deposit step  | No — no deposit step    |
| DW tracks individual balances | Yes             | Yes              | Yes                   | No                      |
| Settlement method             | Per transaction | Net T+1 wire     | Net T+1 (trades only) | Pre-fund or T+1         |
| Client needs books & records  | No              | No               | No                    | Yes                     |
| DW generates tax docs         | Yes             | Yes              | Yes                   | No                      |
| DW provides market data       | Yes             | Yes              | Yes                   | No                      |
| Travel Rule required          | No              | Yes              | Yes                   | Client responsibility   |

***

## **Individual funding**

**The customer funds their own account directly.**

In this model, each customer links their personal bank account to their DriveWealth brokerage account and initiates their own deposits and withdrawals. DriveWealth handles all cash custody and tracks each customer's balance independently.

There are two transfer methods available:

* **ACH** — typically 4–5 business days. DriveWealth charges $0.25 for outbound ACH transfers. Requires a linked US bank account. Buying power is only available after funds settle.
* **Wire** — same business day if initiated before the bank's cutoff time. Faster but higher fees. Funds are sent to each account's unique Virtual Account number.

❗️ ACH deposits are subject to a seasoning period before funds can be withdrawn — typically 5 days, up to 30 days. Wire deposits carry no seasoning period. These defaults can be customized as part of your integration.

### **When to use it**

Individual funding is best when your customers manage their own banking relationship and you want DriveWealth to handle the full funding lifecycle on your behalf.

### **Key guides**

* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/depositing-1">Depositing</Anchor>
* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/withdrawing-1">Withdrawing</Anchor>
* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/using-plaid">Using Plaid</Anchor>

***

## **Bulk funding**

**The client aggregates customer funds and settles daily with DriveWealth.**

In this model, you custody customer cash yourself (or through a banking-as-a-service provider). You notify DriveWealth about each customer's deposit or withdrawal via API, but the actual money movement between your organization and DriveWealth happens as a single daily net wire.

DriveWealth aggregates all transactions across your client environment over a 24-hour window (8PM–8PM ET), computes a net settlement amount, and publishes a settlement report. Your organization then remits or receives the net amount by T+1.

```shell
curl --request POST \
     --url https://bo-api.drivewealth.io/back-office/funding/deposits \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
     --header 'content-type: application/json' \
     --header 'dw-client-app-key: {{YOUR_APP_KEY}}' \
     --data '{
  "accountNo": "DWBG000052",
  "amount": 100.00,
  "currency": "USD",
  "type": "BULK_FUNDING",
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f"
}'
```

**Instant trading** is available under bulk funding for margin accounts with 1:1 leverage — customers can trade on funds in transit before the settlement wire clears.

❗️ Travel Rule compliance is required for every bulk deposit and withdrawal. You must create a Bank Account object with `bankAccountPurpose: "TRAVEL_RULE"` and pass the resulting `bankAccountID` with each transaction. See <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/travel-rule">Travel Rule</Anchor>.

### **Settlement direction**

* If credits > debits (total > 0): your organization owes DriveWealth the net amount.
* If credits < debits (total < 0): DriveWealth owes your organization the net amount.

Settlement wires are due by 1:30PM ET. DriveWealth remits outbound wires by 12 noon ET.

### **Settlement profiles**

Clients with multiple lines of business, regions, or banking relationships can request additional `settlementProfileID` values to segment settlements independently. Contact DriveWealth Support to configure custom profiles.

### **When to use it**

Bulk funding is best when you already hold customer cash — for example, if you operate a banking-as-a-service platform — and want to control the banking relationship while DriveWealth handles the brokerage layer.

### **Key guides**

* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/bulk-funding">Bulk Funding</Anchor>
* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/travel-rule">Travel Rule</Anchor>

***

## **Cashless settlement**

**The client removes the deposit step entirely — trades settle directly against customer banking balances.**

Cashless is a variant of bulk funding designed for embedded investing products. There are no explicit deposit or withdrawal steps. Customers place orders directly, and you move money behind the scenes to settle trades. The customer never sees a brokerage balance.

* **Purchases** pull funds from the customer's banking balance at your platform.
* **Sales and dividends** return funds directly to that same balance.
* **Buying power validation** is your responsibility — DriveWealth will execute any order regardless of brokerage account balance.

❗️ It is critical to validate that a customer has sufficient funds before submitting an order. If DriveWealth receives a buy order for any amount, it will be executed. Clients must place holds on customer funds at their banking layer before submitting orders to DriveWealth.

Each day, DriveWealth aggregates all trade activity (purchases, sales, dividends, fees) across your client environment and publishes a reconciliation report. You settle the net buy/sell difference by T+1.

❗️ Travel Rule compliance is required. Unlike bulk funding, the Bank Account object must be created *before* creating the brokerage account. API sequencing is: Create User → Create Bank Account (with `bankAccountPurpose: "TRAVEL_RULE"`) → Create Account. See <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/travel-rule">Travel Rule</Anchor>.

🚧 Cashless account functionality must be enabled by DriveWealth for your client environment before these workflows are available.

### **Reconciliation vs. settlement**

Under cashless, the daily report is a **reconciliation** (not a settlement). It is based on trade activity — purchases, sales, dividends, fees, and commissions — not on explicit deposit and withdrawal requests.

```shell
curl --request GET \
     --url https://bo-api.drivewealth.io/back-office/funding/reconciliations/reconciliationID \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

```json
{
  "amounts": {
    "total": -1263.56,
    "purchases": -1680.07,
    "sales": 416.51,
    "dividends": 0,
    "fees": 0,
    "other": 0
  },
  "transferAmounts": {
    "payablesToDW": 1263.56,
    "receivablesFromDW": 0
  }
}
```

* `payablesToDW` — funds DriveWealth expects to receive from you.
* `receivablesFromDW` — funds DriveWealth expects to remit to you.

📘 After settlement, DriveWealth creates `CSR` (deposit) and `CSD` (redemption) transactions on customer accounts for internal accounting. These should be ignored when computing reconciliation numbers on your end.

### **Settlement profiles**

Like bulk funding, cashless clients can segment customers across multiple settlement profiles by region or line of business. Settlement profiles are set at the user level via the `settlementProfileID` field on Create User or Update User.

### **When to use it**

Cashless is best for embedded investing products — neobanks, spend-and-invest apps, or any experience where the brokerage layer is invisible and you fully control the customer's cash.

### **Key guides**

* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/bulk-fundingcashless">Cashless Settlement</Anchor>
* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/travel-rule">Travel Rule</Anchor>

***

## **Omnibus**

**The client operates a single master account at DriveWealth and manages everything customer-facing themselves.**

Under the omnibus model, DriveWealth has no knowledge of your individual customers. You hold a single omnibus account at DriveWealth that represents all of your customers combined. You maintain your own "books and records" — tracking each customer's positions, balances, and cash independently.

DriveWealth provides only the underlying execution and clearing infrastructure. Everything else — KYC, customer onboarding, market data, reporting, tax documents, corporate actions — is your responsibility.

### **Funding an omnibus account**

There are two ways to maintain buying power in your omnibus account:

1. **Pre-funding** — you wire funds to the master account in advance. If the balance is insufficient when a customer attempts to trade, the order will be rejected.

❗️ Under pre-funding, you must track and replenish the omnibus buying power yourself. Insufficient balance = rejected trades.

2. **Cashless reconciliation** — instead of pre-funding, you settle trades on a T+1 basis. See <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/bulk-fundingcashless">Cashless Settlement</Anchor> for details.

### **ClientID requirements**

Every order placed through an omnibus account must include a `clientID` that identifies the originating end customer. DriveWealth enforces three rules:

| Requirement            | Description                                                                  |
| :--------------------- | :--------------------------------------------------------------------------- |
| Coverage               | Populated on every order — no blanks or placeholders                         |
| Stability              | The same customer always sends the same value, across all sessions and days  |
| Per-customer semantics | One value maps to exactly one customer — never a firm-wide or order-level ID |

Accepted formats include stable numeric IDs, stable alphanumeric IDs, and stable per-customer hashes. Rotating hashes, constant firm codes, timestamps, and blank values are not accepted.

### **Client responsibilities under omnibus**

* Customer onboarding and KYC
* Individual customer buying power and balance tracking
* Live market data (DriveWealth does not provide quotes for omnibus setups)
* All customer-level reporting: performance, transaction history, trade confirmations, statements, and tax documents
* Corporate actions handling for each customer

### **When to use it**

Omnibus is best for sophisticated clients — often international — who want to use DriveWealth purely as an execution and clearing layer and have the operational infrastructure to manage the full customer-facing brokerage experience themselves.

### **Key guides**

* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/omnibus-trading">Omnibus Trading</Anchor>
* <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/bulk-fundingcashless">Cashless Settlement</Anchor>

***

## **Holidays and weekends**

All four models are subject to the US bank holiday schedule. Settlements and reconciliations are only processed when US banks are open.

On market holidays and weekends, transactions are aggregated across the non-business days and settled on the next business day. When US banks are closed but markets remain open (for example, Veterans Day), you will receive daily settlement or reconciliation reports as usual — but the actual wire settlement is deferred to the next banking day, resulting in a double settlement on that day.

***

<br />