Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.55

## API Release 1.55

## Deployed in UAT - Yes, available to test.

## Deployed in Production - July 11, 2023.

# 🚀New Features - What’s New?

#### None

# 2. 🎉Feature Enhancements - We are making it better for you!!

## 2.1 Enhancement to Travel rules + bankAccountID combo

#### Existing Feature - With the current implementation of the Travel rule, it is required as a mandate for the partners to add the below-mentioned details for INSTANT\_FUNDING deposits/redemptions

1. Bank Account Number
2. Bank Routing Number
3. Bank Name
4. Bank Address
5. Bank Country
6. Account Holder’s name
7. Account Holder’s Address
8. Account Holder’s country

#### What is improving? - Instead of asking partners to add the source details for Travel rules manually for every INSTANT\_FUNDING request, we want to utilize the bank account API to capture the travel rule details.

**POST bank-account changes for Travel Rule + Bank Account ID combo**

```Text POST: {{bo-url}}/back-office/bank-account
{
  "bankAccountNumber":"123456789",
  "bankRoutingNumber":"CHASUS33",
  "userID":"userID",
  "bankAccountNickname": "Kakashi's spending ACRT account",
  "bankAccountPurpose" : "TRAVEL_RULE",
  "beneficiaryDetails" : {
      "accountHolderName" : "Kakashi Hatake",
      "accountHolderAddress" : "Village hidden in sand",
      "accountHolderCountry" : "JPN"
  },
  "bankName" : "Bank of Konoha",
  "bankAddress" : "Village hidden in mist",
  "bankCountry" : "JPN"
}
```

```Text 200 OK response
{
    "id": "bank_2b8c12f1-048b-44a1-ae83-c367972de5b4",
    "userDetails": {
        "userID": "d519fbf6-3a9a-4656-99a2-7e219776c678",
        "username": "test.individual.1688034596",
        "firstName": "Levi",
        "lastName": "Ackermann",
        "email": "b@b.com",
        "parentIB": {
            "id": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
            "name": "DriveWealth"
        },
        "wlpID": "DW"
    },
    "bankAccountDetails": {
        "bankAccountNickname": "Traveller's spending ACRT account",
        "bankAccountNumber": "****0027",
        "bankRoutingNumber": "121141822",
        "bankName": "Bank of Konoha",
        "bankAddress": {
            "addressLine1": "Village hidden in mist",
            "country": "Jpn"
        }
    },
    "default": false,
    "status": "ACTIVE",
    "bankAccountPurpose": "TRAVEL_RULE",
    "beneficiaryDetails": {
        "accountHolderName": "Kakashi Hatake",
        "accountHolderAddress": "Village hidden in sand",
        "accountHolderCountry": "Jpn"
    },
    "created": "2023-06-29T10:30:20.568Z",
    "updated": "2023-06-29T10:30:20.568Z"
}
```

> 🚧 Use the bankAccountID generated for making INSTANT\_FUNDING deposit/Redemptions

```Text POST: {{bo-url}}/back-office/funding/deposits
{
   "accountNo": "DWQT000095",
   "amount": 1000,
   "currency": "USD",
   "type": "INSTANT_FUNDING",
   "note": "Here's some money",
   "bankAccountID": "bank_b47c01cc-bd1c-43df-bf05-512c926c140e"
}
```

```Text POST: {{bo-url}}/back-office/funding/redemptions
{
   "accountNo": "DWQT000095",
   "amount": 100,
   "currency": "USD",
   "type": "INSTANT_FUNDING",
   "note": "Here's some money",
   "bankAccountID": "bank_b47c01cc-bd1c-43df-bf05-512c926c140e"
}
```

**PATCH bank-account changes for Travel Rule + Bank Account ID combo**

```Text PATCH: {{bo-url}}/back-office/bank-account/{{bankAccountID}}
{
  "bankAccountPurpose" : "TRAVEL_RULE",
  "bankAccountDetails": {
        "bankName": "Bank of Konoha",
        "bankAddress": "Village Hidden in the Sand, Sunagakure",
        "bankCountry": "jpn",
        "accountHolderName": "Naruto Uzumaki",
        "accountHolderAddress": "Village Hidden in the Leaves, Konohagakure",
        "accountHolderCountry": "JPN"
    }
}
```

#### Expected change - This update will sit behind a Feature Toggle. When turned on for the partners, it will:

* [x] Rename bankAccountPurpose: TRAVEL\_RULE
* [x] Return mandatory bank and beneficiary details for Travel rule in GET, PATCH, POST API.
* [x] Return bankAccountID in DEPOSIT/REDEMPTION in response for INSTANT\_FUNDING.
* [x] Add all mandatory details in bankAccounts.created and bankAccounts.updated Event

## 2.2 Adding Position Quantity to orders.completed or positions.updated SQS events

#### Existing Feature - Currently, DW is only sending availableForTradingQuantity in the account summary endpoint.

#### What is improving? - Going forward, our partners will be able to consume openQuantity and availableForTradingQuantity within the following endpoint and SQS events.

* getOrderById
* getOrderByNo
* getAuditOrderById
* orders.completed event
* orders.created event

```Text GET : {{bo-url}}/back-office/orders/{{OrderID}}
{
    "id": "KE.64637a12-24f3-478c-a411-02de46f1fdf8",
    "orderNo": "KEWG000012",
    "type": "MARKET",
    "side": "SELL",
    "status": "FILLED",
    "symbol": "AA",
    "averagePrice": 33.66,
    "averagePriceRaw": 33.66,
    "totalOrderAmount": 33.66,
    "cumulativeQuantity": 1,
    "openQuantity": 7,
    "availableForTradingQuantity": 7,
    "quantity": 1,
    "fees": 2.99,
    "orderExpires": "2023-05-18T20:00:00.000Z",
    "createdBy": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "userID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "accountID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684.1682435763668",
    "accountNo": "DWXN000105",
    "created": "2023-05-18T13:24:32.259Z",
    "lastExecuted": "2023-05-18T13:30:02.153Z",
    "extendedHours": false,
    "preventQueuing": false
}
```

```Text GET : {{bo-url}}/back-office/orders/byOrderNo/{{OrderID}}
{
    "id": "KE.64637a12-24f3-478c-a411-02de46f1fdf8",
    "orderNo": "KEWG000012",
    "type": "MARKET",
    "side": "SELL",
    "status": "FILLED",
    "symbol": "AA",
    "averagePrice": 33.66,
    "averagePriceRaw": 33.66,
    "totalOrderAmount": 33.66,
    "cumulativeQuantity": 1,
    "openQuantity": 7,
    "availableForTradingQuantity": 7,
    "quantity": 1,
    "fees": 2.99,
    "orderExpires": "2023-05-18T20:00:00.000Z",
    "createdBy": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "userID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "accountID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684.1682435763668",
    "accountNo": "DWXN000105",
    "created": "2023-05-18T13:24:32.259Z",
    "lastExecuted": "2023-05-18T13:30:02.153Z",
    "extendedHours": false,
    "preventQueuing": false
}
```

```Text GET :  {{bo-url}}/back-office/orders/{{OrderID}}/audit
{
    "id": "KE.64637a12-24f3-478c-a411-02de46f1fdf8",
    "orderNo": "KEWG000012",
    "accountID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684.1682435763668",
    "accountNo": "DWXN000105",
    "quantities": {
        "requestedQuantity": 1,
        "totalFilledQuantity": 1
    },
    "openQuantity": 7,
    "availableForTradingQuantity": 7,
    "amountCash": 0,
    "status": "FILLED",
    "side": "SELL",
    "instrumentID": "1b474cec-97f7-4305-4d6e-f1ac72b8ee71",
    "symbol": "AA",
    "type": "1",
    "pricing": {
        "avgPxRaw": 33.66,
        "avgPx": 33.66,
        "stopPx": 0,
        "mitTriggerPrice": 0
    },
    "expires": "2023-05-18T20:00:00.000Z",
    "commissionOverride": {
        "commissionOverrideType": "NO_OVERRIDE",
        "commissionID": null,
        "commissionOverrideDesc": "Standard Commission"
    },
    "commissionAndFees": {
        "total": 2.99,
        "tefra": 0,
        "ptp": 0
    },
    "auditLog": [
        {
            "status": "NEW",
            "quantities": {
                "cumulativeQuantity": 0,
                "filledQuantity": 0,
                "remainingQuantity": 0
            },
            "pricing": {
                "averagePrice": 0,
                "averagePriceRaw": 0,
                "lastPrice": 0,
                "rateAsk": 0,
                "rateBid": 0
            },
            "commissionAndFees": {
                "commission": 0,
                "feeSec": 0,
                "feeTaf": 0,
                "feeBase": 0,
                "feeXtraShares": 0,
                "feeExchange": 0
            },
            "pnl": 0,
            "transactTime": "2023-05-18T13:24:32.097Z",
            "comment": "NOS started",
            "createdWhen": "2023-05-18T13:24:32.097Z"
        },
        {
            "status": "NEW",
            "quantities": {
                "cumulativeQuantity": 0,
                "filledQuantity": 0,
                "remainingQuantity": 1
            },
            "pricing": {
                "averagePrice": 0,
                "averagePriceRaw": 0,
                "lastPrice": 0,
                "rateAsk": 36.74,
                "rateBid": 36.4
            },
            "commissionAndFees": {
                "commission": 0,
                "feeSec": 0,
                "feeTaf": 0,
                "feeBase": 0,
                "feeXtraShares": 0,
                "feeExchange": 0
            },
            "pnl": 0,
            "transactTime": "2023-05-18T13:24:32.268Z",
            "comment": "NOS accepted",
            "createdWhen": "2023-05-18T13:24:32.268Z"
        },
        {
            "status": "FILLED",
            "quantities": {
                "cumulativeQuantity": 1,
                "filledQuantity": 1,
                "remainingQuantity": 0
            },
            "pricing": {
                "averagePrice": 33.66,
                "averagePriceRaw": 0,
                "lastPrice": 33.66,
                "rateAsk": 36.53,
                "rateBid": 36.29
            },
            "commissionAndFees": {
                "commission": 2.99,
                "feeSec": 0,
                "feeTaf": 0,
                "feeBase": 2.99,
                "feeXtraShares": 0,
                "feeExchange": 0
            },
            "pnl": 0,
            "transactTime": "2023-05-18T13:30:02.153Z",
            "comment": "LQBK01FILLED1fill1",
            "eventID": "event_b2ed6e73-cb30-481c-9b9e-93b57f456344",
            "createdWhen": "2023-05-18T13:30:01.863Z"
        }
    ],
    "violationExempt": false,
    "preventQueuing": false,
    "extendedHours": false
}
```

```Text Payload
{
  "id": "event_97d605cb-860a-4161-b208-11d2089b8dc6",
  "type": "orders.created",
  "timestamp": "2023-06-06T17:03:54.522332054Z",
  "payload": {
    "id": "KF.1aaeecf1-2ab5-4f4d-9103-51cb160bda52",
    "orderNo": "KFGJ000002",
    "type": "MARKET",
    "side": "BUY",
    "status": "NEW",
    "symbol": "AA",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "cumulativeQuantity": 0,
    "openQuantity": 7,
    "availableForTradingQuantity": 7,
    "quantity": 1,
    "fees": 0,
    "orderExpires": "2023-06-06T20:00:00.000Z",
    "createdBy": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "userID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "accountID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684.1682435763668",
    "accountNo": "DWXN000105",
    "created": "2023-06-06T11:33:43.105Z"
  }
}
```

```Text Payload
{
  "id": "event_53446c29-13f4-410b-898e-1a9066fa08e7",
  "type": "orders.completed",
  "timestamp": "2023-06-06T17:03:55.108307483Z",
  "payload": {
    "id": "KF.1aaeecf1-2ab5-4f4d-9103-51cb160bda52",
    "orderNo": "KFGJ000002",
    "type": "MARKET",
    "side": "BUY",
    "status": "REJECTED",
    "statusMessage": {
      "errorCode": "O099",
      "message": "Internal error."
    },
    "symbol": "AA",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "cumulativeQuantity": 0,
    "openQuantity": 7,
    "availableForTradingQuantity": 7,
    "quantity": 1,
    "fees": 0,
    "orderExpires": "2023-06-06T20:00:00.000Z",
    "createdBy": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "userID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684",
    "accountID": "9a8cebff-6b1f-4f99-bb9c-f6843626a684.1682435763668",
    "accountNo": "DWXN000105",
    "created": "2023-06-06T11:33:43.105Z"
  }
}
```

## 2.3 POST/PATCH changes to accommodate non-supported countries

#### Expected change - Today, the logic for POST/PATCH changes to accommodate non-supported countries is convoluted, this change will help clean up and make the logic more simple.

In either POST or PATCH on the user

> 📘 For country of residence (country field)
>
> 1. Check country's active flag.
> 2. If country is active > Request Allowed
> 3. If inactive > For POST - block user; for PATCH – allow request but set the account to FROZEN
> 4. For citizenship field
> 5. Always check country active flag first.
>    1. If country is active > let user through
>    2. If inactive > Check expat logic
> 6. Expat logic:
>    1. If expat allowed > Request allowed
>    2. If not allowed > For POST - block user; for PATCH – allow request but set account to FROZEN

## 2.4 Additional SQS queues for events

> ❗️ **Limited Availability**
>
> Partners can now have events sent to multiple SQS queues. Please reach out to your relationship management team if this is something you are interested in.

## 2.5 Change in Cash Promotion Types

**This is for partners who use our cash promotion endpoints**

> 👍 API : \{\{bo-url}}/back-office/transactions/types

#### We are deprecating the type *“PROMOTION”* for cash promotions and are adding a new type called “CASH\_PROMOTION”. Additionally, cash promotions will no longer show as cash journals in the transaction history. The Cash Promotion will show two transactions. One is a disbursement (CSD) from the Cash Promotion account. The second transaction is a receipt (CSR) of the cash promotion into the user's account.

#### Creating a Cash Promotion for a user account.

```Text POST {{bo-url}}/back-office/funding/deposits
{
  "currency": "USD",
  "type": "CASH_PROMOTION"
  "accountNo": "DWBG000052",
  "amount": 250.25,
}
```

## 2.6 Ongoing Enhancement to PDT Calculations

#### We are making improvements to the timing and detection of PDTs to provide a better user experience. More improvements are to come in upcoming releases.

# 3.🔧Bug Fixes

## 3.1 Autopilot redemptions failing due to commission & fees not being deducted.

#### **What is improving?** - Autopilot will now include commissions, SEC, and TAF fees when calculating the liquidation amount for withdrawals. This will eliminate withdrawals failing for “Insufficient Funds” even though there is sufficient money in the user's account.

# 4. 🎁New API endpoints

#### None

# ⭐️ Coming Soon!

#### Due to compliance and regulatory requirements, we will be imposing minimum notional quantity limits on trades for certain instruments like BRK.A (Berkshire Hathaway).

More information and updates to follow in future communications.

### In the meantime, please feel free to ask us any questions that you may have.