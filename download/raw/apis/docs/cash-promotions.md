---
updatedAt: 2026-08-03T19:23:01.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Cash Promotions

DriveWealth offers our clients to run Cash Promotional Campaigns, enabling them to deposit funds directly into customer accounts through a Cash Promotion Account. This account is created by DriveWealth but is fully funded, owned, and managed by the clients.

To deposit funds into a customer’s account as part of a promotion, you can use the API endpoint outlined below.

If you're interested in setting up a Cash Promotional Campaign, please contact your DriveWealth representative to get started.

```json
POST /back-office/funding/deposits

{
  "accountNo": "DWBG000052",
  "amount": 5.00,
  "currency": "USD",
  "type": "CASH_PROMOTION" 
}
```

If initiated during DriveWealth’s money movement window (4:00 AM ET to 2:00 PM ET), the transaction will immediately increase both `CashAvailableForTrade` and `CashAvailableForWithdrawal` on the account. If submitted outside this window, only `CashAvailableForTrade` is updated immediately, while `CashAvailableForWithdrawal` will be incremented during the next open window.

<Callout icon="❗️" theme="error">
  **Note:** Cash promotions are not supported for accounts in a "Cashless" setup, as these accounts do not hold cash from DriveWealth’s perspective. However, clients may still offer promotions independently by crediting promotional funds directly to customer wallets on their platform.
</Callout>