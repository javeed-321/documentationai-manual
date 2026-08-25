---
updatedAt: 2025-08-20T23:30:30.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Testing in sandbox

In sandbox, Orders are filled by a simulator, instead of an actual execution venue.

## Filling orders after hours

Orders placed outside of market hours, like equities Orders placed overnight, will be filled at market open, like they would be in production. However, if you would like to test an immediate execution, even outside of market hours, set a special flag on the Account you’re testing in:

```json
PATCH /back-office/accounts/{accountID}
{
	"ignoreMarketHoursForTest": true
}
```

This can be particularly helpful for Continuous Integration purposes.

## Magic numbers

To assist in testing specific Order workflows, the following combinations of symbols and quantities can be used to force certain behavior:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Symbol
      </th>

      <th>
        Quantity
      </th>

      <th>
        Handling
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        HL
      </td>

      <td>
        176
      </td>

      <td>
        Execute only half of the quantity, and exchange cancel the remainder
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        177
      </td>

      <td>
        Execute in two fills, at two different prices
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        178
      </td>

      <td>
        Execute in 10 share increments, for a total of 18 fills
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        179
      </td>

      <td>
        Execute in 20 share increments and send a new fill every 1 second
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1019
      </td>

      <td>
        Execute fully, no different from typical execution
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1039
      </td>

      <td>
        Execute 1 share at a time
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1049
      </td>

      <td>
        Execute 100 shares at a time
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1059
      </td>

      <td>
        Returns NOS NAK or failure
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1069
      </td>

      <td>
        Execute a partial amount, exchange cancel remainder
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1079
      </td>

      <td>
        Execute nothing, exchange cancel everything
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        1089
      </td>

      <td>
        Execute nothing, leave open and awaiting cancel
      </td>
    </tr>

    <tr>
      <td>
        HL
      </td>

      <td>
        5089
      </td>

      <td>
        Execute nothing, leave open and await cancel request
      </td>
    </tr>
  </tbody>
</Table>

These quantities can be used for a buy-side order only:

```json
POST /back-office/orders
{
    "accountNo": "DWCU000440",
    "orderType": "MARKET",
    "symbol": "HL",
    "side": "BUY",
    "quantity" : 1011
}
```