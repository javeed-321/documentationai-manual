---
updatedAt: 2026-07-14T16:18:16.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Using Plaid

DriveWealth and Plaid have partnered to allow for a quick and seamless integration between Plaid bank accounts and DriveWealth's money movement APIs. Clients utilizing DriveWealth's ACH pull functionality to fund brokerage accounts can utilize banking tokens already configured at Plaid.

## Getting started

<Callout icon="📘" theme="info">
  ### Get Plaid API keys

  To utilize this integration, you'll need to have a Plaid sandbox account already configured.

  [Sign up on Plaid.com](https://dashboard.plaid.com/signup/drivewealth)
</Callout>

Existing Plaid customers can immediately utilize the combined integration, just by enabling it in the Integrations section of the Plaid dashboard:

![1990](https://files.readme.io/f55cc28-plaid.png "plaid.png")

## Obtaining processor tokens

Communication between Plaid and DriveWealth occurs using processor tokens. These are identifiers that contain banking details and are securely scoped to allow only DriveWealth to view. You may be familiar with other types of tokens issued by Plaid that you use in your product today:

| Token type      | Purpose                                                                                                                                                                                                  |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Public token    | Temporarily stores details about a customer's banking relationship, for use in transit between their device and your infrastructure.                                                                     |
| Access token    | Stores details about a customer's banking relationship, for use from your infrastructure. Typically, a public token from Plaid Link is immediately converted into an access token, which is then stored. |
| Processor token | Allows DriveWealth to access details for a single bank account.                                                                                                                                          |

After a customer connects their bank using [Plaid Link](https://plaid.com/docs/link/web/), a processor token can be generated at any time:

```curl
curl \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": "PLAID_CLIENT_ID",
    "secret": "PLAID_SECRET",
    "access_token": "ACCESS_TOKEN",
    "account_id": "ACCOUNT_ID",
    "processor": "drivewealth"
  }' \
  -X POST \
  https://sandbox.plaid.com/processor/token/create

# Response - this processor token should be sent to DriveWealth
{
  "processor_token": "processor-sandbox-0asd1-a92nc",
  "request_id": "[Unique request ID]"
}
```

Note that the account ID specified above will grant DriveWealth access to view only that individual bank account. As an example, if a customer logs in to Plaid Link using their Chase credentials, and has 4 checking accounts eligible for funding, you'll need to have the customer first specify just one of those accounts to use.

## Processor token best practices

* Continue to store only access tokens, not processor tokens
* Don't generate processor tokens if a customer is not planning to fund a DriveWealth-supported brokerage account

## Step-by-step

After processor tokens are generated, they can be used to create a Linked Bank Account with DriveWealth. The existing Create Bank Account API will accept a Plaid processor token, rather than explicit account and routing numbers:

```json
POST /back-office/bank-accounts
{
      "userID": "bf0b650d-fe95...",
      "bankAccountType": "CHECKING", 
      "bankAccountNickname": "Johns_Bank_Account",
      "plaidProcessorToken": "processor-sandbox-0asd1-a92nc",
      "plaidBankAccountID": "7jHbjgnwBsperkpZqzMPiQwmxKYvPxcgPug8Yt"
}

Response:
{
	...
	"id": "bank_d897...",
	...
}
```

Later, these saved banking details can be referenced to create a deposit:

```json
{
  "accountNo": "DWWP000001",
  "amount": 101,
  "currency": "USD",
  "type": "ACH_MANUAL",
  "bankAccountID": "bank_d897...",
  "note": "ACH Deposit"
}
```

Alternatively, a processor token can be used in this endpoint directly. Refer to the [Create Deposit](https://developer.drivewealth.com/apis/reference/post_funding-deposits) API for full details. The same process works for [Create Withdrawal](https://developer.drivewealth.com/apis/reference/post_funding-redemptions).