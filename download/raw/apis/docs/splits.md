---
updatedAt: 2025-08-20T23:39:01.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Splits

Stock splits cause the number of shares each shareholder owns to be adjusted by a ratio. For example, a 2-for-1 split means a customer previously holding 100 shares will now hold 200 shares.

Once a split is processed, the customer record will reflect the correct shares, in accordance with the split conversion rate. In the customer account record, you will observe a remove share, and add share at the conversion rate (recording the unique legs of the transaction).

> 📘 Market data caution
>
> If a customer holds 10 shares of ABC security which splits 2:1, the customer will end up with 20 shares. If the pre-split price at market close was $20, the customer at end of day would have a $200 market value (10 shares x $20). Once the split share conversion is processed share quantity will increase from 10 to 20, and share price will decline from $20 to $10. However, post-split price adjustments can be published any time from 6pm – 7am EST. During this period the customer may be displayed $400 market value (20 qty x $20 (unadjusted)). Once the adjusted price is available, it will automatically update.