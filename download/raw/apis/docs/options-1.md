---
updatedAt: 2026-08-17T22:24:31.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Options

Corporate actions that affect the underlying security (splits, dividends, mergers, etc.) typically also affect options. In most cases, the original option Instrument is marked with `status` of `"INACTIVE"`, and a new option Instrument is created for existing positions.

Options corporate events consist of a bit more data because of updates that need to be made to the Instrument and option positions.

First, the Instrument is updated to reflect that it has undergone a corporate action. This is commonly done by adding a number after the stock ticker within the option symbol. So, for example, if you owned a contract in the underlying ABCD, this would change to ABCD1 in the option symbol.

When an option corporate action event does occur there will be four (4) events created in cases where an Account holds a position in an impacted contract:

*Two&#x20;*`instruments.updated`*&#x20;events (expiring the pre-existing symbol, and setting the new symbol as active)<br />* Two `positions.updated` (removal of the position in pre-existing symbol and adding a position in the new one).<br />\* Transactions will reflect the change as well

The sequence of events you would see are the following:

## First Instrument event

The first instrument event will update the existing contract to Inactive, since it is no longer trading.

```json
{
    "id": "event_17913550-6db0-4086-9137-3fd728bd6821",
    "type": "instruments.updated",
    "timestamp": "2026-07-14T16:41:53.938331938Z",
    "payload": {
        "instrumentID": "4a59a844-7f0d-43c1-83bf-a0de46507b65",
        "previous": {
            "status": "ACTIVE"
        },
        "current": {
            "status": "INACTIVE"
        }
    }
}
```

## Second Instrument event

The second position update event will be the creation of the new option contract.

```json
{
  "id": "event_5877084c-65c7-417c-96ed-dc901d1fe49b",
  "type": "instruments.created",
  "timestamp": "2026-07-14T17:04:19.522666034Z",
  "payload": {
    "instrumentID": "4a59a844-7f0d-43c1-83bf-a0de46507b65",
    "symbol": "MSFT1270115P00450000",
    "description": "MSFT 0003 DESC",
    "status": "ACTIVE",
    "rootSymbol": "MSFT",
    "rootId": "e234cc98-cd08-4b04-a388-fe5c822beea6",
    "type": "OPTION",
    "expirationDate": "2027-01-15",
    "optionType": "PUT",
    "strikePrice": 450,
    "sharesPerContract": 100,
    "exchange": "24"
  }
}
```

In this example, a new MSFT1 option contract is set to an active status. The 1 in the OSI symbol identifies that this is a non-standard option contract meaning it is not equivalent to 100 underlying shares.

## First Position Update Event

The first position update event will remove the existing contracts.

In this example, the previous `openQty` is 10 and the current `openQty` is 0

```json
remove old shares positions.updated :

{
    "id": "event_3e6287a6-efe8-46a9-82a4-64819cc414a7",
    "type": "positions.updated",
    "timestamp": "2026-08-14T13:33:43.851817261Z",
    "payload": {
      "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
      "accountNo": "OPTN000076",
      "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
      "updateReason": "OPTION_SYMBOL_CHANGE",
      "previous": {
        "costBasis": 0.3,
        "openQty": 10,
        "symbol": "BYND260814C00000500",
        "avgPrice": 0.15
      },
      "current": {
        "costBasis": 0,
        "openQty": 0,
        "symbol": "BYND260814C00000500"
      }
    }
  }
```

## Second Position Update Event

The second position update event will be the addition of the new option contract.

```json
Added new shares position : 
{
  "id": "event_4ea82069-5cd1-4941-ad8f-db85cda32090",
  "type": "positions.updated",
  "timestamp": "2026-08-14T13:33:43.987137347Z",
  "payload": {
    "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
    "accountNo": "OPTN000076",
    "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
    "updateReason": "OPTION_SYMBOL_CHANGE",
    "previous": {
      "openQty": 0,
      "symbol": "BYND1260814C00000500"
    },
    "current": {
      "openQty": 10,
      "symbol": "BYND1260814C00000500"
    }
  }
}
```

<Callout icon="🚧" theme="warn">
  ### Orders in Options Instruments after a corporate action is processed

  Please note that when an option contract undergoes a corporate action change, that instrument is set to Closing Only. This means that the updated instrument will not be discoverable and you will not be able to submit a `BUY_OPEN` order in the instrument.

  If you own a position in the new instrument as a result of the corporate action, you can still sell the contract.
</Callout>

Transactions:<br />These transactions are available through List Account Transactions <https://developer.drivewealth.com/apis/reference/get_accounts-accountid-transactions>

remove old option position:

```json
{
  "id": "event_7616fc21-ce06-48a0-95b0-2f13c229184f",
  "type": "transactions.created",
  "timestamp": "2026-08-14T13:33:43.860701731Z",
  "payload": {
    "accountID": "d9444836-94be-4a7a-8807-2fd5ed81d533.1652286934066",
    "accountNo": "OPTN000076",
    "userID": "d9444836-94be-4a7a-8807-2fd5ed81d533",
    "transaction": {
      "accountAmount": 0,
      "accountBalance": 3845.34,
      "comment": "Removed 10.00000000 shares of BYND260814C00000500",
      "finTranID": "NH.92efc9a6-3a57-45b2-b819-715941167ffc",
      "wlpFinTranTypeID": "0c866a9f-2668-42c4-9e02-25579f109fcb",
      "finTranTypeID": "MERGER_ACQUISITION",
      "feeSec": 0,
      "feeTaf": 0,
      "feeBase": 0,
      "feeXtraShares": 0,
      "feeExchange": 0,
      "positionDelta": -10,
      "instrument": {
        "id": "9311a685-bf72-4b47-8d27-017f9390eda3",
        "symbol": "BYND260814C00000500",
        "name": null
      },
      "mergerAcquisition": {
        "type": "OPTION_SYMBOL_CHANGE"
      }
    }
  }
}
```

Add new option position:

```json
{
  "id": "event_3d375302-bcb1-4c0c-b8e3-cc950708ea1b",
  "type": "transactions.created",
  "timestamp": "2026-08-14T13:33:43.994472428Z",
  "payload": {
    "accountID": "d9444836-94be-4a7a-8807-2fd5ed81d533.1652286934066",
    "accountNo": "OPTN000076",
    "userID": "d9444836-94be-4a7a-8807-2fd5ed81d533",
    "transaction": {
      "accountAmount": 0,
      "accountBalance": 3845.34,
      "comment": "Added 10.00000000 shares of BYND1260814C00000500",
      "finTranID": "NH.0921ec2e-147a-40cd-9954-32c4ca132816",
      "wlpFinTranTypeID": "0c866a9f-2668-42c4-9e02-25579f109fcb",
      "finTranTypeID": "MERGER_ACQUISITION",
      "feeSec": 0,
      "feeTaf": 0,
      "feeBase": 0,
      "feeXtraShares": 0,
      "feeExchange": 0,
      "positionDelta": 10,
      "instrument": {
        "id": "eae1d6b8-5a60-44f1-917a-0dc74e0c8c8f",
        "symbol": "BYND1260814C00000500",
        "name": null
      },
      "mergerAcquisition": {
        "type": "OPTION_SYMBOL_CHANGE"
      }
    }
  }
}
```