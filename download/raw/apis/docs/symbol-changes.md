---
updatedAt: 2025-08-20T23:39:04.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Symbol changes

A Symbol change can occur for a variety of reasons, but a symbol change does not have a conversion component, impacting underlying share number, price, etc. of the underlying symbol. Note: a symbol and instrument changes are used interchangeably.

## Operational sequencing

After the market close, on the last day of trading under the prior symbol, the Instrument will be marked as “Inactive” in DriveWealth’s system. By marking it inactive, will ensure that any orders being received or queued under the prior symbol are rejected, rendering them unable to be executed.

> 📘
>
> Corporate Actions with only a symbol change typically trade on the open. More complex Corporate Actions, like symbol change plus a conversion merger or acquisition, are not guaranteed to trade on the open right at 9:30am, as a result of an SEC or Exchange halt.
>
> While DriveWealth will attempt to update all relevant information at the same time, to the extent any information is not available (e.g. RIC), and the symbol and company name information is updated, with the RIC being updated when available; this would produce 2 events.

All other operational processes occur on DriveWealth’s side, which fundamentally ensure that the Instrument information is available via API and that the market data is active for when the symbol begins trading.