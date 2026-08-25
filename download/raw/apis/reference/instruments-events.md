---
updatedAt: 2025-09-22T15:01:56.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Instrument Events

## Instruments Created

A new instrument has been added to the instruments list.

```json Created
{
    "id": "event_c4b2c210-ce32-41d4-a9a1-cfad4fdf191c",
    "type": "instruments.created",
    "timestamp": "2019-03-29T07:02:33.200962333Z",
    "payload": {
        "instrumentID": "3fb1e8a9-f7d5-4d90-95e2-43e7326b5636",
        "symbol": "MS",
        "name": "Morgan Stanley",
        "status": "ACTIVE"
    }
}
```
```json Created [options]
{
  "id": "event_5877084c-65c7-417c-96ed-dc901d1fe49b",
  "type": "instruments.created",
  "timestamp": "2023-07-14T17:04:19.522666034Z",
  "payload": {
    "instrumentID": "70f66ac9-c7f6-4f7e-9d9e-3bacb5d0ceeb",
    "symbol": "AAPL231010P00030000",
    "description": "AAPL 0003 DESC",
    "status": "ACTIVE",
    "rootSymbol": "AAPL",
    "rootId": "a67422af-8504-43df-9e63-7361eb0bd99e",
    "type": "OPTION",
    "expirationDate": "2023-10-10",
    "optionType": "PUT",
    "strikePrice": 30,
    "sharesPerContract": 100,
    "exchange": "24"
  }
}
```

## Instruments Updated

An instrument has been updated.

```json Updated [status]
{
    "id": "event_17913550-6db0-4086-9137-3fd728bd6821",
    "type": "instruments.updated",
    "timestamp": "2019-08-21T16:41:53.938331938Z",
    "payload": {
        "instrumentID": "26fa9515-d1c6-44ce-93b2-b94430451508",
        "previous": {
            "status": "ACTIVE"
        },
        "current": {
            "status": "INACTIVE"
        }
    }
}
```
```json Updated [symbol]
{
    "id": "event_ca1fd34b-aa0e-474d-8b43-90acfad88a47",
    "type": "instruments.updated",
    "timestamp": "2019-08-21T16:44:18.756968650Z",
    "payload": {
        "instrumentID": "26fa9515-d1c6-44ce-93b2-b94430451508",
        "previous": {
            "symbol": "ZVZZA"
        },
        "current": {
            "symbol": "ZVZZZ"
        }
    }
}
```