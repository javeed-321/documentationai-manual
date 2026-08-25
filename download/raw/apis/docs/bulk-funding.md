---
updatedAt: 2026-07-14T16:21:27.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bulk Funding

Bulk Funding enables clients to consolidate multiple customer deposits and withdrawals into a single transfer to DriveWealth. This approach streamlines fund management, reduces transfer costs, and minimizes transaction failures.

<Image src="https://files.readme.io/b63c5cf-group-people.png" align="center" />

<br />

<Callout icon="✅" theme="okay">
  ### Is bulk right for your company?

  Bulk Funding is ideal if your organization or a third-party provider (e.g., a Banking-as-a-Service platform) can aggregate multiple customer transactions into a single transfer. If you have the capability to custody and transfer customer funds, Bulk Funding is likely the optimal solution.
</Callout>

<Callout icon="❗️" theme="error">
  ### Travel Rule Compliance

  For accounts utilizing Bulk Funding, DriveWealth requires Travel Rule information for every deposit and withdrawal request.

  **Requirement:** Include Travel Rule details in each transaction request.<br />**Purpose:** Ensure compliance with regulatory standards for fund transfers

  To learn more about this see: [Travel Rule](https://developer.drivewealth.com/apis/docs/travel-rule)
</Callout>

## Depositing

To initiate a bulk deposit, create a Deposit Request for each customer account, specify the deposit details.

```json
POST /back-office/funding/deposits

{
  "accountNo": "DWBG000052",
  "amount": 100.00,
  "currency": "USD",
  "type": "BULK_FUNDING",
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",
  "settlementProfileID": "settlement-profile-1"  //optional
}
```

Use this API throughout the day to process additional customer deposits.

### ⚡Instant Trading

DriveWealth allows customers to trade on funds that are in transit, known as **Instant Trading**. This feature is available under the following conditions:

**Account Type:** Margin accounts with 1:1 leverage.<br />**Reason:** Cash accounts are subject to Good Faith Violations (GFVs) if assets are sold before funds settle.

**Example:** After initiating a $200 `BULK_FUNDING` deposit, the account's available cash for trading will reflect the deposit, even though the funds haven't settled.

```json
GET /back-office/accounts/{accountID}/summary/money
{
  "accountID": "cc07f91b-7ee1...",
  "accountNo": "DWBG000052",
  "tradingType": "MARGIN",
  "updated": "2022-12-25T18:41:32.440Z",
  "cash": {
    "cashAvailableForTrade": 200.0,
    "cashAvailableForWithdrawal": 0,
    "cashBalance": 0,
    "noBuyingPowerReason": [],
    "cashSettlement": [],
    "pendingPaymentsAmount": 200.0
  },
  "payments": {
    "buyingPower": {
      "pendingDepositsAmountAvailable": 200.0,
      "pendingDepositsAmountNotAvailable": 0
    },
    "redemptions": {
      "amountWithheldFromRedemptions": 0
    }
  }
}
```

## Withdrawing

To process bulk withdrawals, create a Withdrawal Request for each customer account, specify the withdrawal details.

```json
POST /back-office/funding/redemptions
{
  "accountNo": "DWBG000052",
  "amount": 100.00,
  "currency": "USD",
  "type": "BULK_FUNDING",
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",
  "settlementProfileID": "settlement-profile-1"  //optional
}
```

Use this API throughout the day to process additional customer withdrawals.

<Callout icon="📘" theme="info">
  ### Cash Available for Withdrawal

  To process a withdrawal, the requested `amount` must be ≤ `cashAvailableForWithdrawal`.<br />Once settlement is complete on T+1, the settled cash is credited to the customer’s account.

  **For example:**<br />Michael places a deposit for $200, giving him immediate buying power(`cashAvailableForTrade`).

  1. If Michael does not purchase any securities, then on T+1 after settlement:<br />`cashAvailableForTrade`: 200.0<br />`cashAvailableForWithdrawal`: 200
  2. If Michael buys $100 of AAPL, then on T+1 after settlement:<br />`cashAvailableForTrade`: 100.0<br />`cashAvailableForWithdrawal`: 100
  3. If Michael buys $200 of TSLA, then on T+1 after settlement:<br />`cashAvailableForTrade`: 0<br />`cashAvailableForWithdrawal`: 0
</Callout>

**NOTE:** Managed accounts will follow a similar waiting period as described under [Advisor Withdrawal Flow Cycle](https://developer.drivewealth.com/apis/docs/withdrawing#advisory-flow-lifecycle)

## Settlements

Under this settlement method, deposits and withdrawals from multiple customer accounts are aggregated at the organization level. These transactions are then netted to calculate a single daily settlement amount.

<Callout icon="🚧" theme="warn">
  ###

  **NOTE:** Your firm may be using only the bulk deposit or bulk withdrawal side of the settlement process; however, this settlement method applies in either case.

  If only the deposit component is used, DriveWealth will aggregate all deposits and generate the settlement report. Your firm will be responsible for remitting the total settlement amount to DriveWealth on a T+1 basis.

  If only the withdrawal component is used, DriveWealth will aggregate all withdrawals and generate the report. DriveWealth will then remit the total settlement amount to your firm on a T+1 basis.
</Callout>

### Retrieving Settlement Reports

You can retrieve a list of all settlements over a given period by using the [Retrieve Settlements API](https://developer.drivewealth.com/apis/reference/get_settlements)

```json GET /back-office/settlements
{
  "pageSize": 1,
  "limit": 50,
  "settlements": [
    {
      "id": "sett_63ccb073-a7b6-4b33-af77-5baec5cc4494_20221224",
      "settlementDate": "2022-12-25",
      "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
      "status": "APPROVED",
      "totalAmount": -14250,
      "createdAt": "2022-12-11T22:28:21.810Z",
      "updatedAt": "2022-12-11T22:28:21.810Z"
    },
   {
      "id": "sett_63ccb073-a7b6-4b33-af77-5baec5cc4494_20221225",
      "settlementDate": "2022-12-26",
      "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
      "status": "PENDING",
      "totalAmount": -250,
      "createdAt": "2022-12-12T22:28:21.810Z",
      "updatedAt": "2022-12-12T22:28:21.810Z"
    }
  ]
}
```

Further, you can drill down into a particular settlement by using the <Anchor target="_blank" href="https://developer.drivewealth.com/apis/reference/get_settlements-settlementid">Retrieve Settlement by ID API</Anchor> and passing in the settlement `id`from the previous API response.

```json GET /back-office/settlements/{{settlement-id}}
{
  "id": "sett_63ccb073-a7b6-4b33-af77-5baec5cc4494",
  "settlementDate": "2022-12-25",
  "status": "APPROVED",
  "statusComment": "Finished processing breakdown",
  "amount": {
    "total": 5000.45,
    "credits": 6000.45,
    "debits": -1000
  },
  "breakdownReport": "https://du2c4wzqz90h1.cloudfront.net/singleSettlementReport....",
  "partnerID": "80f9b672-120d-4b73-9ccv9-42fb3262c4b9",
  "updatedBy": "SYSTEM",
  "createdAt": "2022-12-11T22:28:21.810Z",
  "updatedAt": "2022-12-11T22:28:21.810Z"
}
```

The `breakdownReport` will provide ALL the underlying deposits & withdrawals in the client accounts.

```json breakdownReport
{
  "id": "sett_90fc14cc-cf3f-448b-ab43-7a9411683d11_20250502",
  "summary": {
    "totalAmount": 1118.23,
    "credits": 2132.82,
    "debits": -1014.59,
    "ancillary": {
      "depositAmounts": 2133.5,
      "withdrawalAmounts": -1015.27
    }
  },
  "breakdown": [
    {
      "accountID": "65a43a7a-b31c-4d97-9663-494fdb0079e9.1715933938944",
      "accountNo": "GTNZ000019",
      "userID": "65a43a7a-b31c-4d97-9663-494fdb0079e9",
      "amount": 0.85,
      "transactions": [
        {
          "amount": 0.17,
          "type": "CREDIT",
          "finTranID": null,
          "details": {
            "orderID": null,
            "orderNo": null,
            "depositID": "GTNZ000019-1746095683497-DU6ZK",
            "withdrawalID": null,
            "originatingFinTranID": null
          },
          "created": "2025-05-01T10:34:43.497Z"
        },
        {
          "amount": 0.17,
          "type": "CREDIT",
          "finTranID": null,
          "details": {
            "orderID": null,
            "orderNo": null,
            "depositID": "GTNZ000019-1746095701894-DVBEF",
            "withdrawalID": null,
            "originatingFinTranID": null
          },
          "created": "2025-05-01T10:35:01.894Z"
        },
        {
          "amount": 0.17,
          "type": "CREDIT",
          "finTranID": null,
          "details": {
            "orderID": null,
            "orderNo": null,
            "depositID": "GTNZ000019-1746097323033-DMBNS",
            "withdrawalID": null,
            "originatingFinTranID": null
          },
          "created": "2025-05-01T11:02:03.033Z"
        },.....
        }
    ]
}
}
}
```

### Simulating Settlements in Sandbox

To simulate an end-to-end settlement in the Sandbox environment, clients can use a Sandbox-only API to “settle” the settlement, which credits settled cash to the underlying customer accounts. This mimics the exact process our Cash Management team follows in Production when they settle the settlement upon receiving the settlement wire on T+1.

```json
PATCH /back-office/settlements/{{settlement-id}}

{
  "status": "Successful"

}
```

### Settlement Statuses, Timelines & Events

1. DriveWealth system starts aggregating deposits and withdrawals under a client environment starting at 8PM ET. As soon as we start the computing process, a settlement object is created with the status `PENDING`.<br />This generates a `settlements.created` event as documented here: [Settlements Created Event](https://developer.drivewealth.com/apis/reference/settlements-events#new-settlement-created) with status `PENDING`.
2. All deposits and withdrawals are aggregated over a 24 hr period (from 8 PM ET to 8 PM ET), following which we compute and publish the `breakdownReport`which can retrieved from the settlement object. The status of the report moves to an `APPROVED`status, also generating a `settlements.updated`event with the `APPROVED`status as documented here: [Settlements Updated Event](https://developer.drivewealth.com/apis/reference/settlements-events#new-settlement-approved). The settlements amounts are finalized at this point and are due for settlement.<br />**Settlement Direction:**<br />If `credits` > `debits`, ie, `total`> 0, the organization owes DriveWealth the net amount.<br />If `credits` < `debits`, ie, `total` < 0 DriveWealth owes the organization the net amount.
3. Once settlement wires are received(latest by 1:30 PM ET) or remitted by DriveWealth(latest by 12 noon ET) , the settlement is deemed completed and the status of the settlement object is moved to `SUCCESSFUL`, which also further generates a `settlements.completed` event with the `SUCCESSFUL`status as documented here: [Settlements Completed Event](https://developer.drivewealth.com/apis/reference/settlements-events#new-settlement-completed). This further creates terminal Deposit(`CSR`) and withdrawal(`CSD`) transactions on the customer accounts

<Callout icon="🇺🇸" theme="default">
  ### Market/Bank holiday schedule

  **Settlements are only processed when U.S. banks are open**

  On market holidays and weekends, deposits and withdrawals made from 8 PM ET on the day before the holiday through the non-business days are aggregated and settled on the next business day.<br />For example, if markets are closed for Memorial Day (the last Monday of May), all transactions from Thursday 8 PM ET through Monday 8 PM ET are combined. The settlement report is generated end-of-day Monday for settlement on Tuesday morning.

  **Double settlement day** - When U.S. banks are closed but markets remain open, you'll receive daily settlement reports as usual, but the actual settlements are deferred.<br />For instance, if Veterans Day falls on a Tuesday, you'll get reports for both Monday and Tuesday. However, since Tuesday is a bank holiday, settlements for both days will occur on Wednesday.
</Callout>

### Bulk Settlement Profiles

DriveWealth allows clients using Bulk Funding to segment customer deposits and withdrawals into distinct settlement profiles based on factors such as lines of business (LOBs), banking relationships, and regions. Each profile receives a unique `settlementID`, separate settlement numbers, and DriveWealth generates a dedicated set of events for each profile.

**Default Profile:** If only one settlement preference is configured, the default profile is used automatically. This applies to most clients.<br />**Custom Profiles:** Clients with multiple regions or business units can request additional settlementProfileIDs to manage settlements independently.<br />❗*Contact DriveWealth Support to set up custom settlement profiles as needed.*

When making deposit requests, ensure you pass the appropriate `settlementProfileID`

```json POST /back-office/funding/deposits
{
  "accountNo": "SPFY0000052",
  "amount": 250.25,
  "currency": "USD",
  "type": "BULK_FUNDING",
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",
  "settlementProfileID": "spendify-mexico"
  ...
}
```

When making withdrawal requests, ensure you pass the appropriate `settlementProfileID`

```json POST /back-office/funding/redemptions
{
  "accountNo": "SPFY000053",
  "amount": 100.25,
  "currency": "USD",
  "type": "BULK_FUNDING",
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",
  "settlementProfileID": "spendify-india"
  ...
}
```

If using Settlement profiles, Settlement reports will  include `settlementProfileID` for each individual settlement profile.

```json GET /back-office/settlements
[
  {
    "id": "DP_cb3321ec-93cc-4b41-b641-0b0c2d44918a_20230816",
    "date": "2023-08-16",
    "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
    "status": "APPROVED",
    "statusComment": "Finished processing breakdown",
    "totalAmount": -14250,
    "created": "2023-08-16T22:28:21.810Z",
    "updated": "2023-08-16T22:28:21.810Z",
    "updatedBy": "SYSTEM",
    "settlementProfileID": "spendify-mexico"
  },
  {
    "id": "DP_cc472507-6aee-4b47-95a8-3b00114042fe_20230816",
    "date": "2023-08-16",
    "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
    "status": "APPROVED",
    "statusComment": "Finished processing breakdown",
    "totalAmount": 2000.10,
    "created": "2023-08-16T22:28:21.810Z",
    "updated": "2023-08-16T22:28:21.810Z",
    "updatedBy": "SYSTEM",
    "settlementProfileID": "spendify-mexico"
  },
  {
    "id": "SM_0f84b177-5f94-4271-9e26-500500159065_20230816",
    "date": "2023-08-16",
    "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
    "status": "APPROVED",
    "statusComment": "Finished processing breakdown",
    "totalAmount": 100,
    "created": "2023-08-16T22:28:21.810Z",
    "updated": "2023-08-16T22:28:21.810Z",
    "updatedBy": "SYSTEM",
    "settlementProfileID": "spendify-india"
  },
  {
    "id": "SM_d19c7418-67ea-4dc7-9453-2cf09f9efe6b_20230816",
    "date": "2023-08-16",
    "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
    "status": "APPROVED",
    "statusComment": "Finished processing breakdown",
    "totalAmount": -1000,
    "created": "2023-08-16T22:28:21.810Z",
    "updated": "2023-08-16T22:28:21.810Z",
    "updatedBy": "SYSTEM",
    "settlementProfileID": "spendify-india"
  }
]
```

<br />