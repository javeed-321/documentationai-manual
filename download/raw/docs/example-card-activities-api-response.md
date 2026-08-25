---
updatedAt: 2025-09-05T18:36:32.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Card Activities Simulation

Using the Card Simulator, it is possible to create test transactions against cards created in Sandbox, meaning that you will be able to see the results from the [View card activities](https://modulr.readme.io/reference/getcardactivities) API.

First, you'd like to create a card authorization using [Create an Authorisation for a card](https://modulr.readme.io/reference/createauthorisation). This endpoint let us parametrize the authorization with several attributes like the currency and amount, the foreign exchange conversion rate (if the currency is different than the currency of the card) and so on.

Then, you can try either reversing the authorization with [Reverse the card authorisation](https://modulr.readme.io/reference/reverseauthorisation) or settling it with [Settle the card authorisation](https://modulr.readme.io/reference/settleauthorisation).

We are constantly adding new features to the card simulator so tell us your feedback and what you'd like to see in the future.

Also, you can refer to the below examples of how each different Transaction Lifecycle example would be represented via this API:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        ORDER ID
      </th>

      <th>
        Scenario
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        8
      </td>

      <td>
        * \*Declined \*\*Authorisation
      </td>
    </tr>

    <tr>
      <td>
        11
      </td>

      <td>
        * \*Fully Reversed \*\*Authorisation
      </td>
    </tr>

    <tr>
      <td>
        12
      </td>

      <td>
        * \*Partially Reversed\*\* Authorisation (pending settlement)
      </td>
    </tr>

    <tr>
      <td>
        13
      </td>

      <td>
        * \*Approved \*\*Authorisation (pending settlement)
      </td>
    </tr>

    <tr>
      <td>
        19
      </td>

      <td>
        * \*Settled \*\* Authorisation
      </td>
    </tr>

    <tr>
      <td>
        20
      </td>

      <td>
        * \*Fully Reversed\*\* Authorisation due to automatic "Expiry" after 7 days
      </td>
    </tr>

    <tr>
      <td>
        21
      </td>

      <td>
        **Refund** 
      </td>
    </tr>

    <tr>
      <td>
        22
      </td>

      <td>
        **Settled**Authorisation in a **different currency** 
      </td>
    </tr>
  </tbody>
</Table>

```xml
{
  "content": [
    {
      "id": "X11000000Z",
      "orderId": "22",
      "cardId": "V110000001",
      "type": "SETTLEMENT",
      "createdDate": "2019-01-28T12:18:14.857+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "EUR",
      "billingAmount": 45.08,
      "billingCurrency": "GBP",
      "fxRate": 0.90163,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000Y",
      "orderId": "22",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "SETTLED",
      "createdDate": "2019-01-28T12:14:37.091+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "EUR",
      "billingAmount": 43.41,
      "billingCurrency": "GBP",
      "fxRate": 0.868252,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000V",
      "orderId": "21",
      "cardId": "V110000001",
      "type": "REFUND",
      "createdDate": "2019-01-28T12:18:15.794+0000",
      "transactionAmount": 4.99,
      "transactionCurrency": "GBP",
      "billingAmount": 4.99,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5912"
    },
    {
      "id": "X11000000T",
      "orderId": "20",
      "cardId": "V110000001",
      "type": "REVERSAL",
      "createdDate": "2019-01-28T12:18:14.857+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "GBP",
      "billingAmount": 50.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5912"
    },
    {
      "id": "X11000000N",
      "orderId": "20",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "EXPIRED",
      "createdDate": "2019-01-28T12:14:37.091+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "GBP",
      "billingAmount": 50.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5912",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000T",
      "orderId": "19",
      "cardId": "V110000001",
      "type": "SETTLEMENT",
      "createdDate": "2019-01-28T12:18:14.857+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "GBP",
      "billingAmount": 50.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000N",
      "orderId": "19",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "SETTLED",
      "createdDate": "2019-01-28T12:14:37.091+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "GBP",
      "billingAmount": 50.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000M",
      "orderId": "13",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "APPROVED",
      "createdDate": "2019-01-28T12:14:36.668+0000",
      "transactionAmount": 100.00,
      "transactionCurrency": "GBP",
      "billingAmount": 100.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000K",
      "orderId": "12",
      "cardId": "V110000001",
      "type": "REVERSAL",
      "createdDate": "2019-01-28T12:14:36.276+0000",
      "transactionAmount": 50.00,
      "transactionCurrency": "GBP",
      "billingAmount": 50.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000J",
      "orderId": "12",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "APPROVED",
      "createdDate": "2019-01-28T12:14:36.134+0000",
      "transactionAmount": 100.00,
      "transactionCurrency": "GBP",
      "billingAmount": 100.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000H",
      "orderId": "11",
      "cardId": "V110000001",
      "type": "REVERSAL",
      "createdDate": "2019-01-28T12:14:35.624+0000",
      "transactionAmount": 100.00,
      "transactionCurrency": "GBP",
      "billingAmount": 100.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000G",
      "orderId": "11",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "APPROVED",
      "createdDate": "2019-01-28T12:14:35.458+0000",
      "transactionAmount": 100.00,
      "transactionCurrency": "GBP",
      "billingAmount": 100.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    },
    {
      "id": "X11000000D",
      "orderId": "8",
      "cardId": "V110000001",
      "type": "AUTHORISATION",
      "status": "DECLINED",
      "createdDate": "2019-01-28T12:14:10.357+0000",
      "transactionAmount": 100.00,
      "transactionCurrency": "GBP",
      "billingAmount": 100.00,
      "billingCurrency": "GBP",
      "fxRate": 1.000000,
      "mcc": "5814",
      "reason": "Authorisation would exceed card limit",
      "merchantName": "Spaces Cafe",
      "merchantCountry": "GBR"
    }
  ],
  "size": 13,
  "totalSize": 13,
  "page": 0,
  "totalPages": 1
}
```