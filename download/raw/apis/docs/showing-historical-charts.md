---
updatedAt: 2025-08-20T23:55:22.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Showing historical charts

DriveWealth offers historical charts for Equities securities.

A key feature of any investing platform is displaying a historical chart of a selected security. DriveWealth provides historical data in pipe delineated form, based on the time and compression range indicated in the API request.

For example, retrieving daily pricing details over the last 30 trading days for an asset would be requested in the following manner:

```javascript
GET /back-office/bars?instrumentID=675cc7c2-e24b-42fa-9d1f-4b3a97ae8d2f&tradingDays=30
{
  "instrumentID": "675cc7c2-e24b-42fa-9d1f-4b3a97ae8d2f",
  "compression": 0,
  "dateStart": "2022-12-06T00:00:00Z",
  "dateEnd": "2023-01-16T23:59:59Z",
  "data": "2022-12-06T20:00:00Z,8.8,8.8,8.8,8.8,182|2022-12-10T19:43:00Z,8.96,8.96,8.96,8.96,100|.....|2023-01-17T19:59:00Z,8.96,8.96,8.95,8.95,210|"
}
```

The `data` always follows the same structure and is what should be utilized to build a chart: \{timestamp}, open, high, low, close, volume). When consuming the data it’s generally recommended to plot the chart given the `close` price of that given day.

## Choosing different compressions

To determine which compression value to use will depend on what timeframe your user wants displayed. For example, if a user wants to see how a particular security did for a single day, use a smaller compression value, like 5 minutes or even 1 minute. When a user views a longer time frame, like one week, using a 30 minute or 1 hour compression rate is more suitable. The lower the compression value the more data you will receive for a given period.

Use the following table to determine which compression value is used most commonly:

| Compression Value | Time Increment |
| :---------------- | :------------- |
| 0                 | 1 Day          |
| 1                 | 1 Minute       |
| 4                 | 5 Minutes      |
| 8                 | 30 Minutes     |
| 9                 | 1 Hour         |
| 10                | 1 Week         |