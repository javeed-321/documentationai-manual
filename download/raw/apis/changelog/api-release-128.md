Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.28

## API Release 1.28

| Release Date      | Status   |
| :---------------- | :------- |
| November 30, 2021 | RELEASED |

## :fireworks:  **Extended Hours Trading** :fireworks:

Extended Hours Trading is now available. For existing Partners, access to Extended Trading Hours requires a signed Product Addendum, API updates, and UAT validation. For more information, please contact your PSG Account Manager.

## Features and Enhancements

### **Bank Account Events Added**

Three new events have been added to notify when a bank account account has been created, updated, or deleted:

* bankAccounts.created
* bankAccounts.updated
* bankAccounts.deleted

View more details on here: [Bank Account Events](https://developer.drivewealth.com/reference/bank-account-events)

### **Identify Accounts Closed due to ACAT and Updates to Edit Account API**

New fields added to capture closing reason and calling user to [Edit Account API](https://developer.drivewealth.com/reference/edit-account)

* `closingReason`
* `closedBy`
* `updatedBy`

```text New Fields
"closingReason": "ACAT", 
    "closedBy": "0ce13aa8-d655-4ba1-9df7-3447546cd178",
    "updatedBy": "0ce13aa8-d655-4ba1-9df7-3447546cd178"
```
```json Sample Request
{
    "status": "CLOSED",
    "closingReason":"ACAT",
    "statusComment":"....."
}
```
```json Sample Response
{
    "id": "211026fc-c5e4-4a3b-a1e4-f4355146b767.1635964659774",
    "accountNo": "DWMQ000074",
    "accountType": {
        "name": "LIVE",
        "description": "Live Account"
    },
    "accountMgmtType": {
        "name": "SELF",
        "description": "Self Directed Account"
    },
    "status": {
        "name": "CLOSED",
        "description": "Closed"
    },
    "tradingType": {
        "name": "CASH",
        "description": "Cash account"
    },
    "leverage": 1,
    "nickname": "Sansa's Self Directed Account",
    "parentIB": {
        "id": "f2be7ebb-1a9e-4b44-933e-49075918259d",
        "name": "CITI investment"
    },
    "commissionID": "449d41b9-3940-41ff-b0e6-334adfb443f8",
    "beneficiaries": false,
    "userID": "211026fc-c5e4-4a3b-a1e4-f4355146b767",
    "restricted": false,
    "goodFaithViolations": 0,
    "patternDayTrades": 0,
    "freeTradeBalance": 0,
    "gfvPdtExempt": false,
    "buyingPowerOverride": false,
    "bod": {
        "moneyMarket": 0,
        "equityValue": 0,
        "cashAvailableForWithdrawal": 0,
        "cashAvailableForTrading": 0,
        "cashBalance": 0
    },
    "sweepInd": true,
    "interestFree": false,
    "createdWhen": "2021-11-03T18:37:39.774Z",
    "openedWhen": "2021-11-03T18:37:39Z",
    "updatedWhen": "2021-11-04T17:12:56.488Z",
    "ignoreMarketHoursForTest": false,
    "closedWhen": "2021-11-04T17:12:56.488Z",
    "flaggedForACATS": true,
    "closingReason": "ACAT", 
    "closedBy": "0ce13aa8-d655-4ba1-9df7-3447546cd178", 
    "updatedBy": "0ce13aa8-d655-4ba1-9df7-3447546cd178" 
}
```

New account closing reasons added:

* ACAT
* LEGAL\_AML
* DUP\_ACCOUNT
* DECEASED
* OTHER

Existing freeform field `statusComment` is required when updating account `status` via API. Use `statusComment` to provide reason for closing/reopening account.\
See [Edit Account API](https://developer.drivewealth.com/reference/edit-account)

User notes added when an account is updated on Edit Account API:

```json User Notes
[
{
        "id": "211026fc-c5e4-4a3b-a1e4-f4355146b767.2021-11-04T17:18:02.218Z",
        "category": "ACCOUNTS",
        "subject": "Account Status Changed",
        "note": "{\"status\":{\"old\":9,\"new\":2},\"flaggedForACATS\":{\"old\":true,\"new\":false}}",
        "partner": {
            "id": "211026fc-c5e4-4a3b-a1e4-f4355146b767",
            "name": "DriveWealth"
        },
        "created": "2021-11-04T17:18:02.218Z",
        "createdBy": "2820b36b-c64b-47d8-9992-88af36f45205",
        "visibility": "EXTERNAL",
        "createdWhen": "2021-11-04T17:18:02.218Z",
        "userNoteID": "211026fc-c5e4-4a3b-a1e4-f4355146b767.2021-11-04T17:18:02.218Z"
    }
```

### **Taxation Related Changes**

* User patch request will capture the flag validTaxForm which will enable to revert back Tefra fintran on account
* New field `taxTreatyWithUS` added to API endpoint to determine if client requests tax treaty benefit between their legal residence country and United States.  Partners may use  `GET /back-office/countries?status=active` to determine if end client's request is from a tax resident country in the list of eligible tax treaty countries or not.
* The `expatsAllowed` field will return a true or false in response when calling the `bo-url/back-office/countries?status=inactive` endpoint

## Bug Fixes

* Validation added to order requests to require quantity or amount to be greater than 0 if not null
* [Get Historical Chart](https://developer.drivewealth.com/reference/get-charts) now correctly honors the supported range of 1-60 days