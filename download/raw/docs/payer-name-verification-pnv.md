---
updatedAt: 2025-09-05T18:47:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Payer Name Verification (PNV)

Confirming a link between the payer and the bank account details provided when creating DDIs (Mandates)

Payer Name Verification is an service closely related to and based on the UK Confirmation of Payee system.  It is available to any Direct Debit Collections client to be used when capturing a Direct Debit Instruction (Mandate) from a payer to establish a link between the Payer and the bank account provided. The [payer name check API ](https://modulr.readme.io/reference/createoutboundcheckforpnv)provides a match or alternate no-match/close match/mismatch indicators that should be integrated into your Direct Debit Instruction capture Customer Experience (CX)

![](https://files.readme.io/9b1f624fee010237da9adc96b90c4a17eeb9b405680d4dfdf7ede85f8cd481b3-image.png)

*An example DDI Capture screen incorporating Payer Name Verification.*

Updated signup experience recommendations are available in the guide **Direct Debit Collections DDI setup CX - A guide for Sponsored Customers** available from your Modulr account or implementation contact. When updating your customer experience (CX) please be aware that the overall journey and flow must be approved by Modulr as you Sponsoring PSP; this is done by submitting draft or final process to your account and/or implementation contacts for review.

> 📘 How do I access Payer Name Verification?
>
> PNV was introduced for all Direct Debit Collections clients on 1st June 2025. New clients after this date will automatically have access. Existing clients will need a small contract amend to access the service, this is available via your Modulr account manager.

# Important Information

## Use of the service

The service must only be used with the sole intention of creating a Direct Debit Instruction for future Direct Debits to be collected into a Modulr account. The use of the service for any other purpose is forbidden and is a violation of the terms and conditions of the service, usage of the service in relation to volumes Direct Debit Instructions is actively monitored by Modulr & scheme.

## Recording of PNV check ID

Each call to the [Payer Name Check API](https://modulr.readme.io/reference/createoutboundcheckforpnv) returns a unique ID, the endpoint is not idempotent and multiple checks with the same details will return an ID for each check. It is important that you store this ID within your system as evidence of the check, as it can be used in any future Direct Debit Indemnity Claim (DDIC) to confirm a check took place & the result by passing this ID to Modulr in a support enquiry.

# Interpreting Payer Name Verification responses

The table below illustrates the

| result.code                      | HTTP Status Code | Result Description                                                                                                                                                  | Recommended Action                                                                                                                                                                                                                                                                 |
| :------------------------------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MATCHED                          | 201              | The account name and account type match the name and accountType provided.                                                                                          | You can proceed with the creation of the Direct Debit Instruction                                                                                                                                                                                                                  |
| NOT\_MATCHED                     | 201              | The account name and account type do not match the name and accountType provided.                                                                                   | The account details should be checked carefully, and you are advised not to proceed with the creation of the Direct Debit instruction. The Payer should edit the details if possible, and submit another account name check request before proceeding.                             |
| CLOSE\_MATCH                     | 201              | The name provided is similar to the account name. The actual account name is provided in result.name.                                                               | The account details were similar but not wholly correct, you should update the DDI with the result provided or ask the Payer to amend & try again.                                                                                                                                 |
| BUSINESS\_ACCOUNT\_NAME\_MATCHED | 201              | The account name matches the name provided but the account is a business account, not a personal account.                                                           | The account details were matched but indicated as the wrong type of account. You should confirm with the Payer before proceeding with the DDI                                                                                                                                      |
| PERSONAL\_ACCOUNT\_NAME\_MATCHED | 201              | The account name matches the name provided but the account is a personal account, not a business account.                                                           | The account details were matched but indicated as the wrong type of account. You should confirm with the Payer before proceeding with the DDI                                                                                                                                      |
| BUSINESS\_ACCOUNT\_CLOSE\_MATCH  | 201              | The name provided is similar to the account name and the account is a business account, not a personal account. The actual account name is provided in result.name. | The account details were similar but not wholly correct, you should update the DDI with the result provided or ask the Payer to amend & try again.                                                                                                                                 |
| PERSONAL\_ACCOUNT\_CLOSE\_MATCH  | 201              | The name provided is similar to the account name and the account is a personal account, not a business account. The actual account name is provided in result.name. | The account details were matched but indicated as the wrong type of account. You should confirm with the Payer & update to actual name before proceeding with the DDI                                                                                                              |
| ACCOUNT\_DOES\_NOT\_EXIST        | 201              | The account does not exist.                                                                                                                                         | Account does not exist at the Paying Bank. You should not proceed with creation of the DDI as this will result in a Bank Rejected AUDDIS advice.                                                                                                                                   |
| ACCOUNT\_NOT\_SUPPORTED          | 201              | The account does not support account name check requests.                                                                                                           | You should check the account details carefully, potentially using other tools such as Open Banking AIS and proceed only if you are satisfied that they are correct                                                                                                                 |
| ACCOUNT\_SWITCHED                | 201              | The account has been switched using the Current Account Switching Service.                                                                                          | You should ideally not proceed & ask the Payer the new account details if possible. Under CASS, DDIs to the old account details will be redirected, but this involves additional messages from the old paying bank that may delay creation of the DDI (Mandate) on the new account |
| WRONG\_PARTICIPANT               | 500              | The account name check cannot be completed for the account number and sort code provided.                                                                           | You should check the account details carefully, potentially using other tools such as Open Banking AIS and proceed only if you are satisfied that they are correct                                                                                                                 |
| NO\_RESPONSE                     | 201              | The bank did not respond to the account name check request.  Try again later.                                                                                       | You should check the account details carefully, potentially using other tools such as Open Banking AIS and proceed only if you are satisfied that they are correct                                                                                                                 |
| NOT\_ENROLLED                    | 201              | The account name check could not be completed as the bank does not accept account name check requests.                                                              | You should check the account details carefully, potentially using other tools such as Open Banking AIS and proceed only if you are satisfied that they are correct                                                                                                                 |

# Testing your integration within the sandbox environment

* **You must always use sort code 000000**
* We will always return a MATCHED result

To test other scenarios as listed below, you can provide the desired result in the secondaryAccountId field prefixed with a percent sign. For some results, we will append "z" to the end of the name string.

```json Example 1 Request
{
  "accountNumber": "12345678",
  "accountType": "PERSONAL",
  "name": "Joe Bloggs",
  "paymentAccountId": "A123AAA4",
  "sortCode": "000000"
}
```
```json Example 1 Response
{
  "id": "C12001569Z",
  "result": {
    "code": "MATCH"
  }
}
```
```json Example 2 Request
{
  "accountNumber": "12345678",
  "accountType": "PERSONAL",
  "name": "Joe Bloggs",
  "paymentAccountId": "A123AAA4",
  "sortCode": "000000",
  "secondaryAccountId": "%CLOSE_MATCH"
}
```
```json Example 2 Response
{
  "id": "C12001569Z",
  "result": {
    "code": "CLOSE_MATCH",
    "name": "Joseph Bloggsz"
  }
}
```