---
updatedAt: 2025-09-05T18:57:09.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager - Activities

## Card Activities

This is a self-managed report function that enables you to retrieve the activities that have happened on cards that you have created

When calling [GET/channel-managers/activities](https://modulr.readme.io/reference/channelmanagergetcardactivities) you have a list of parameters that you are able to search by, these are:

**Created Dates** – Both FROM and TO dates are available however the data will only return back cards created in the last 7 days

**Statuses** – This is the specific state the transaction is in (DECLINED, APPROVED, SETTLED, EXPIRED, APPLIED)

**Types** – This is the type of transaction (AUTHORISATION, SETTLEMENT, REVERSAL, REFUND, ORGINIAL CREDIT)

**Card ID** – The cards that you wish to query

**Account ID** – The accounts you wish to query

**Transaction ID** – The specific transaction ID’s that you wish to query

**Order ID** – the specific order number/s that you wish to query

**Channel manager ID** – The unique ID for you (obtained when onboarded to Modulr)