Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.58

## API Release 1.58

### Deployed in UAT- Yes, available to test

## Deployed in Production - September 28th, 2023.

# 🎉Feature Enhancements - We are making it better for you!!

## New Promotion Deposit Event Notification for Failed Transactions

#### Existing Feature

We currently send a notification for the promotion deposit event when successful.

#### What is improving?

A notification will now be sent for failed promotional deposit transactions. To see additional details on the event payload, please see\
<https://developer.drivewealth.com/apis/reference/deposits-events> and click on deposit. updated \[cash promo]

#### Feature Toggle (Y/N) - Y

## Instant\_Funding for RIA\_Managed Accounts

#### Existing Feature-

Bulk funding is not currently available for RIA Managed accounts.

#### What is improving?

Partners can now submit bulk funding withdrawals for RIA Managed accounts through the API. Please see <https://developer.drivewealth.com/apis/reference/post_funding-redemptions> and click on the right Request Example, see Bulk Funding Withdrawal.