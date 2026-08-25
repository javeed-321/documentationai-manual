---
updatedAt: 2026-07-13T23:06:22.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Withdrawing

Withdrawing customer funds is the process of transferring money from a customer’s brokerage account to their designated bank account.

<Callout icon="📘" theme="info">
  ### Redemptions vs Withdrawals?

  Redemptions and withdrawals mean the same thing and are used throughout the Guides and API Reference interchangeably.
</Callout>

Each account has a specified balance available for withdrawal, referred to as the Cash Available for Withdrawal. This information can be accessed via the [Retrieve Money Details by Account API](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-summary-money):

```json
GET /back-office/accounts/{accountID}/summary/money
{
  "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
  "accountNo": "DWBG000052",
  "tradingType": "CASH",
  "updated": "2022-12-25T18:41:32.440Z",
  "cash": {
    "cashAvailableForTrade": 400.0,
    "cashAvailableForWithdrawal": 200.0,
    "cashBalance": 400,
    "noBuyingPowerReason": [],
    "cashSettlement": [
      {
        "utcTime": "2021-04-26T13:30:00.001Z",
        "cash": 200.0
      }
    ],
    "pendingPaymentsAmount": 0.00
  },
  ...
}
```

**NOTE:** The Account above has $200 that can be withdrawn.

## Withdrawal Lifecycle Overview

Withdrawals follow a defined lifecycle that allows clients to track and receive updates on the status of each transaction. The stages in this lifecycle provide transparency and help ensure timely processing.

![](https://files.readme.io/301f750-Screen_Shot_2023-01-27_at_4.30.29_PM.png "Screen Shot 2023-01-27 at 4.30.29 PM.png")

## Advisory flow lifecycle

Managing advisory withdrawals differs from regular withdrawals. In self-directed accounts, customers typically sell positions themselves to generate available cash. However, in managed accounts, customers may be fully invested in securities without the ability to initiate sales independently.

If you utilize DriveWealth’s [AutoPilot functionality](https://developer.drivewealth.com/apis/docs/automated-trading), it automates this process by generating sell orders during its next run to raise sufficient funds for the withdrawal, based on the portfolio’s target weights.

Without AutoPilot, advisors must manually sell securities within the individual customer’s brokerage account to free up cash. Once the funds are available, the advisory can submit the withdrawal request.

> Justin requests a $250 withdrawal from his robo-advisory brokerage account on January 3, 2023, before 10:00 AM ET. AutoPilot detects the request and places sell orders at 10:30 AM ET the same day. The securities are successfully sold, raising the required $250. The platform then waits for settlement (Trade Day + 1, or T+1), making the cash available on January 4, 2023. Once settled, the system automatically initiates the withdrawal process.

<Callout icon="🚧" theme="warn">
  ###

  Withdrawals from AutoPilot-enabled accounts require a minimum lead time of one business day. This is because securities must first be sold to generate the necessary funds, and the resulting proceeds must fully settle before the cash becomes available for withdrawal. This settlement process ensures compliance with regulatory requirements and maintains the integrity of the withdrawal process.
</Callout>

![](https://files.readme.io/2d7228b-Withdrawal_AutoPilot_Flow.png "Withdrawal AutoPilot Flow.png")

## ACH Withdrawals

Customers can initiate ACH withdrawals from their brokerage account to a designated U.S. bank account using the [Create Withdrawal API](https://developer.drivewealth.com/apis/reference/post_funding-redemptions).

```json
POST - /back-office/funding/redemptions
{
  "currency": "USD",
  "type": "ACH",
  "accountNo": "DWBG000052",
  "amount": 125.92,
  "bankAccountID": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f"
}
```

## Wire Withdrawals

Customers can initiate Wire withdrawals from their brokerage account using the [Create Withdrawal API](https://developer.drivewealth.com/apis/reference/post_funding-redemptions).

```json
POST - /back-office/funding/redemptions
{
  "currency": "USD",
  "type": "WIRE",
  "details": {
    "beneficiaryName": "Justin Smith",
    "beneficiaryAccountNumber": "00257596002028990212396",
    "beneficiaryRoutingNumber": "021000322",
    "beneficiaryBankName": "Bank of America",
    "beneficiaryBankAddress": "222 BROADWAY",
    "beneficiaryBankCity": "New York City",
    "beneficiaryBankProvince": "New York",
    "beneficiaryBankZip": "10038",
    "beneficiaryBankCountry": "USA"
  },
  "accountNo": "DWBG000052",
  "amount": 125.92
}
```

<br />