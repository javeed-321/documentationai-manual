---
updatedAt: 2026-07-14T16:19:40.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Travel Rule

To meet the US [Travel Rule](https://www.sec.gov/about/offices/ocie/aml2007/fincen-advissu7.pdf) requirement, clients utilizing a Bulk Funding or Cashless Settlement model, are required to collect the account details of their customer’s external bank account from where they are funding their Brokerage Account.

## Travel rule for Bulk Funding

For clients using Bulk Funding, Travel Rule bank account objects must be created and linked to all deposit and withdrawal transactions.<br />The steps below outline how to ensure compliance with the Travel Rule.

### Create a Bank account Object

Clients will need to capture these details prior to the user initiating the transfer and pass along the details to DriveWealth using the [Bank Account API.](https://developer.drivewealth.com/apis/reference/post_bank-accounts)

```javascript JSON
POST /back-office/bank-accounts
{
  userID: "e84d9703-984f-4a05-8859-ac6979dec7ba",
  bankAccountPurpose: "TRAVEL_RULE",
  bankAccountNickname: "PREFERRED CHECKING",
  bankAccountNumber: "7442393174",
  bankAccountType: "CHECKING",
  bankRoutingNumber: "110000000",
  bankName: "Bank of America",
  bankAddress: "222 Broadway New York City NY 10038",
  bankCountry: "USA",
  beneficiaryDetails: {
    accountHolderName: "John Smith",
    accountHolderAddress: "123 Rodent street, New York, NY 10001",
    accountHolderCountry: "USA",
  },
}

```

The above will return a `bankAccountID` which will be a unique identifier for the above object.<br />Eg: `bank_a4656e60-321e-425b-aa0d-a2e75c38885f`

**Note:** Every NEW external bank account the customer uses to create a deposit/withdrawal would need to have a corresponding bank account object established before creating the subsequent deposit/withdrawal requests. If using an existing bank account, clients can reuse the existing`bankAccountID`created previously.

<Callout icon="🚧" theme="warn">
  ###

  International clients should include the bank SWIFT code as the value for`bankRoutingNumber`
</Callout>

### Creating a Deposit request with Travel Rule

Endpoint: [Deposits API](https://developer.drivewealth.com/apis/reference/post_funding-deposits)

```javascript JSON
POST /back-office/funding/deposits
{  
  "currency": "USD",  
  "type": "BULK_FUNDING",  
  "accountNo": "DWBG000052",  
  "amount": 250.25,  
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",  
  "note": "Here's my money!"  
}

```

### Creating a Redemption request with Travel Rule

Endpoint: [Redemptions API](https://developer.drivewealth.com/apis/reference/post_funding-redemptions)

```javascript JSON
POST /back-office/funding/redemptions
{  
  "currency": "USD",  
  "type": "BULK_FUNDING",  
  "accountNo": "DWBG000052",  
  "amount": 250.25,  
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",  
  "note": "Give me my money!"  
}

```

## Travel rule for Cashless Settlement

For clients utilizing a Cashless model, Travel Rule bank account objects must be created before establishing the Brokerage account. DriveWealth ties the travel rule bank account object to customer transactions on the backend.

<Callout icon="❗️" theme="error">
  ### API sequencing

  An account cannot be created until a Bank Account object with `"bankAccountPurpose": "TRAVEL_RULE"` has been established.

  Be sure to sequence your API calls in the following order: first create the User, then the Bank Account, and only after that proceed with Account creation.
</Callout>

Below are the steps to adhere to Travel Rule requirements.

### Create a Bank account Object

```javascript JSON
POST /back-office/bank-accounts
{
  userID: "e84d9703-984f-4a05-8859-ac6979dec7ba",
  bankAccountPurpose: "TRAVEL_RULE",
  bankAccountNickname: "PREFERRED CHECKING",
  bankAccountNumber: "7442393174",
  bankAccountType: "CHECKING",
  bankRoutingNumber: "110000000",
  bankName: "Bank of America",
  bankAddress: "222 Broadway New York City NY 10038",
  bankCountry: "USA",
  beneficiaryDetails: {
    accountHolderName: "John Smith",
    accountHolderAddress: "123 Rodent street, New York, NY 10001",
    accountHolderCountry: "USA",
  },
}

```

<br />

## Travel Rule Attestation

To confirm that funds received from DriveWealth are delivered by clients to their customers. We have implemented an Attestation endpoint to make this process efficient for our clients.<br />Depending on your current settlement process, the endpoint utilized differs.

### Attest Settlement (Bulk funding clients)

Endpoint: [Attest Settlement](https://developer.drivewealth.com/apis/reference/patch_settlements-settlementid-attest)

Successful response

```json
{
  "id": "sett_63ccb073-a7b6-4b33-af77-5baec5cc4494_settle-profile-usa_20221224",
  "settlementDate": "2022-12-25",
  "status": "SUCCESSFUL",
  "statusComment": "Finished processing breakdown",
  "amount": {
    "total": 5000.45,
    "credits": 6000.45,
    "debits": -1000
  },
  "breakdownReport": "https://du2c4wzqz90h1.cloudfront.net/singleSettlementReport....",
  "partnerID": "80f9b672-120d-4b73-9ccv9-42fb3262c4b9",
  "settlementProfileID": "settlement-profile-bank-account-1",
  "updatedBy": "SYSTEM",
  "createdAt": "2022-12-11T22:28:21.810Z",
  "updatedAt": "2022-12-11T22:28:21.810Z",
  "attestedBy": "66304da9-3h6f-2234-935f-ac6b7933d706",
  "attestedAt": "2024-04-17T22:28:21.810Z"
}
```

### Attest Cashless Reconciliation (Cashless Settlement clients)

Endpoint: [Attest Cashless Reconciliation](https://developer.drivewealth.com/apis/reference/attestreconciliation)

Successful response

```json
{
  "id": "80f9b672-120d-4b73-9cc9-42fb3262c4b9_20240417",
  "date": "2024-04-17",
  "status": "SUCCESSFUL",
  "statusComment": "Finished processing breakdown",
  "amounts": {
    "total": -1263.56,
    "purchases": -1680.07,
    "sales": 416.51,
    "dividends": 0,
    "fees": 0,
    "other": 0
  },
  "transferAmounts": {
    "currency": "USD",
    "payablesToDW": 1263.56,
    "receivablesFromDW": 0
  },
  "reconciliationBreakdown": "string",
  "partnerID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
  "settlementProfileID": "settlement-profile-bank-account-1",
  "created": "2024-04-15T22:28:21.810Z",
  "updated": "2024-04-17T22:28:21.810Z",
  "updatedBy": "SYSTEM",
  "attestedBy": "66304da9-3h6f-2234-935f-ac6b7933d706",
  "attestedAt": "2024-04-17T22:28:21.810Z"
}
```

<br />