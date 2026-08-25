Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# 24/7 Cash Rewards

## 24/7 Promotional Cash Rewards

The Promotions (24/7 Cash Rewards) feature can be used if a Partner wishes to use the deposit endpoint for promotional purposes.

New promotional money is not impacted by the existing money movement window by increasing the  `cashAvailableForTrade` and not the `cashBalance` between 1:30EST - 5:00am EST

***Contact your PSG Account Manager to begin the process of granting permissions required to utilize this feature.***

**How To:**

* Partner must always have enough `cashBalance` in their CASH\_PROMOTIONS account to satisfy the promotion requests.
* Use the existing deposit endpoint and enter type = PROMOTION.
  * By selecting the `PROMOTION` type, the partner can instantly give the customer buying power at all times of the day, and have funds sweep from their CASH\_PROMOTION\_ACCOUNT account within the money movement window.
  * Buying power is increased instantly, and cash balance is only increased during money movement window.

```json Request Example
{
     "accountNo": "string",
     "amount": 10,
     "currency": "string",
     "type": "PROMOTION",
     "note": "string"
}
```

**Example- 1**\
**Time of request - 5:00am -> 1:30pm EST**

* Partner request a `PROMOTION` deposit for $10
* $10 is directly debited from Partners CASH\_PROMOTION\_ACCOUNT account
* End user receives a credit for $10 to `cashAvailableForTrade` and `cashBalance` and `cashAvailableForWithdrawal`

**Example- 2**\
**Time of request - 1:30pm -> 5:00am EST**

* Partner requests a `PROMOTION` deposit for $10
* A pending transfer is created under the Partners CASH\_PROMOTION\_ACCOUNT account for $10
* End user receives $10 in `cashAvailableForTrade`
* Upon money movement window opening again at 5:00am EST, the pending transfer is moved to successful
* Immediately following move to successful end user receives credit for $10 in `cashBalance`

<Image align="center" src="https://files.readme.io/8774a87-247.png" />