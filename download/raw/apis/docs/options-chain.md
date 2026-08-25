---
updatedAt: 2026-07-13T16:47:03.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Options chains

Use the <Anchor target="_blank" href="https://developer.drivewealth.com/apis/v1.83.0/reference/get_instruments">Instruments API</Anchor> endpoints to retrieve available options for an underlying instrument — expiration dates first, then the full chain filtered by date, type, or size.

Once you have decided to look further into options on a specific underlying stock, ETF or index fund, we can make a chain request to look through what options are available.

## Get option expiration dates

First, we can request to see the expiration dates for the underlying security.

For the detailed API Reference: <https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid-options-expiration-dates>

You can get `expiration-dates` by root symbol with:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.io/back-office/instruments/AAPL/options/expiration-dates' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'

```

You can also get `expiration-dates` by instrument ID:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.io/back-office/instruments/a67422af-8504-43df-9e63-7361eb0bd99e/options/expiration-dates' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'

```

Response:

```json
{
    "symbol": "AAPL",
    "expiration": [
        "2026-06-03",
        "2026-06-05",
        "2026-06-08",
        "2026-06-10",
        "2026-06-12",
        "2026-07-10",
        "2026-08-21",
        "2027-12-17"
    ]
}
```

## Option chain

There are two primary ways to get an option chain.

For the detailed API Reference: <https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid-options>

### Get around-the-money options chain

Get `N` number of contracts in the money (ITM), `N` number of contracts out of the money/at the money (OTM/ATM), for each `optionType` (`CALL` and `PUT`)  given a root identifier or instrument ID, where `N` = `noOfStrikes`

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.io/back-office/instruments/AAPL/options?noOfStrikes=2' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

Abbreviated response with 2 `CALL` strikes ITM, 2 `CALL` strikes OTM/ATM, 2 `PUT` strikes ITM, and 2 `PUT` strikes OTM/ATM:

```json
{
    "symbol": "AAPL",
    "options": [
        {
            "id": "481c7930-8f94-44d7-b8a3-8ba427bc61f1",
            "symbol": "AAPL260603C00307500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 307.500000,
                ...
            },
            ...
        },
        {
            "id": "86289b51-2e2a-4e83-a283-5baaeba8f1e4",
            "symbol": "AAPL260603C00312500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 312.500000,
                ...
            },
            ...
        },
        {
            "id": "8b03905b-98c1-49fd-b399-b198f075d9cb",
            "symbol": "AAPL260603C00317500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 317.500000,
                ...
            },
            ...
        },
        {
            "id": "9ac5b854-c82d-4307-93b0-7da639373188",
            "symbol": "AAPL260603C00322500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 322.500000,
                ...
            },
            ...
        },
        {
            "id": "a1d53eeb-fa5f-4983-aa67-3c445c4c094e",
            "symbol": "AAPL260603P00307500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "PUT",
                "strikePrice": 307.500000,
                ...
            },
            ...
        },
        {
            "id": "8d894796-6df8-4461-8ca3-e2c87a12661c",
            "symbol": "AAPL260603P00312500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "PUT",
                "strikePrice": 312.500000,
                ...
            },
            ...
        },
        {
            "id": "d1de62dc-399e-437f-89cb-6ce5de319a02",
            "symbol": "AAPL260603P00317500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "PUT",
                "strikePrice": 317.500000,
                ...
            },
            ...
        },
        {
            "id": "d1f1ed4a-d555-492e-8d92-301b74e68f9c",
            "symbol": "AAPL260603P00322500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "PUT",
                "strikePrice": 322.500000,
                ...
            },
            ...
        }
    ]
}
```

You can also specify an `optionType` as a query parameter:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.io/back-office/instruments/AAPL/options?noOfStrikes=2&optionType=CALL' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

Abbreviated response, now with only 2 `CALL` ITM and 2 `CALL` ATM/OTM:

```json
{
    "symbol": "AAPL",
    "options": [
        {
            "id": "481c7930-8f94-44d7-b8a3-8ba427bc61f1",
            "symbol": "AAPL260603C00307500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 307.500000,
                ...
            },
            ...
        },
        {
            "id": "86289b51-2e2a-4e83-a283-5baaeba8f1e4",
            "symbol": "AAPL260603C00312500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 312.500000,
                ...
            },
            ...
        },
        {
            "id": "8b03905b-98c1-49fd-b399-b198f075d9cb",
            "symbol": "AAPL260603C00317500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 317.500000,
                ...
            },
            ...
        },
        {
            "id": "9ac5b854-c82d-4307-93b0-7da639373188",
            "symbol": "AAPL260603C00322500",
            "optionsData": {
                "rootSymbol": "AAPL",
                "optionType": "CALL",
                "strikePrice": 322.500000,
                ...
            },
            ...
        }
    ]
}
```

The `expirationDate` parameter is supported as well:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.io/back-office/instruments/AAPL/options?noOfStrikes=2&optionType=CALL&expirationDate=2026-06-03' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

Please note that `minStrikePrice` and `maxStrikePrice` are not supported when getting by moneyness (i.e. with `noOfStrikes`), and neither is pagination.

### Get entire options chain for underlying/strike price range

To get all options, given an underlying and an expiration date range you can leverage the following paginated request:

```shell
curl --request GET \
     --url 'https://bo-api.drivewealth.io/back-office/instruments/AAPL/options?pageSize=20&page=1' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

Abbreviated response:

```json
{
    "symbol": "AAPL",
    "options": [
        {
            "id": "c04b5ea5-6aa8-4298-9ca4-59b3cce82597",
            "symbol": "AAPL260603C00337500",
		...
            "optionsData": {
                "rootSymbol": "AAPL",
                "strikePrice": 337.500000,
			...
            }
        },
        {
            "id": "4b454b6e-497f-4020-863c-2165a302150b",
            "symbol": "AAPL260603C00332500",
		...
                "strikePrice": 332.500000,
			...
            }
        },
	... (18 more elements, 20 total as per pageSize=20 parameter)
    ]
}
```

To retrieve the second page of results, here is the subsequent call:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.net/back-office/instruments/AAPL/options?pageSize=20&page=2&sortOrder=desc' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

You can also get contracts with `minStrikePrice` and/or `maxStrikePrice`:

```shell
curl --request GET \
     --url    'https://bo-api.drivewealth.net/back-office/instruments/AAPL/options?minStrikePrice=300&maxStrikePrice=305' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'dw-client-app-key: {{yourAppKey}}'
```

Response:

```json
{
    "symbol": "AAPL",
    "options": [
        {
            "id": "1838bd6b-6862-4ce3-b08a-7da9250fad43",
            "symbol": "AAPL260603C00302500",
            "type": "OPTIONS",
            "exchange": "27",
            "orderSizeMax": 500,
            "orderSizeMin": 1.0,
            "orderSizeStep": 1.0,
            "name": "AAPL Jun 03 2026 $302.50 Call",
            "optionsData": {
                "rootSymbol": "AAPL",
                "rootId": "a67422af-8504-43df-9e63-7361eb0bd99e",
                "expirationDate": "2026-06-03",
                "optionType": "CALL",
                "strikePrice": 302.500000,
                "multiplier": 100,
                "deliverable": 100
            }
        },
        {
            "id": "d0b8eb5d-5bca-437d-8b59-4ff95b00d50f",
            "symbol": "AAPL260603P00302500",
            "type": "OPTIONS",
            "exchange": "27",
            "orderSizeMax": 500,
            "orderSizeMin": 1.0,
            "orderSizeStep": 1.0,
            "name": "AAPL Jun 03 2026 $302.50 Put",
            "optionsData": {
                "rootSymbol": "AAPL",
                "rootId": "a67422af-8504-43df-9e63-7361eb0bd99e",
                "expirationDate": "2026-06-03",
                "optionType": "PUT",
                "strikePrice": 302.500000,
                "multiplier": 100,
                "deliverable": 100
            }
        }
    ]
}
```

<br />