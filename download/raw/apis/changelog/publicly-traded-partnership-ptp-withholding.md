Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Publicly Traded Partnership (PTP) Withholding

# 🚢 Shipping New Features

We are back with some platform changes that will enable non US customers to be able to trade publicly traded partnership securities. Starting earlier this year (2023), securities that are classified as a publicly traded partnership (PTP) enacted a mandatory 10% tax withholding on the sales of these securities. We’re now automating this process with the new feature release.

Starting on December 8, 2023 customers will be able to transact with these securities just as easily as our other securities on the platform. This tax withholding is seamlessly enacted on sale transactions and any fees (tax) associated are a part of the order confirmation and transaction history. Please note that sales with notional values less than $0.05 will not be charged the tax.

<Callout icon="🤔" theme="default">
  ### What does this look like?

  Harry Wilson, an Englishman currently has a holding of  **3** shares of Black Stone Minerals (BSM) which he purchased 6 weeks ago for **$14.30 each**. The stock price is now **$17.00**. John decides to sell all his holdings of **BSM** securities and his sales proceeds are taxed at 10% so the platform will automatically collect **$5.10**  from the order. Harry will have an instant available buying power of **$45.90**.

  17.00 x 3 = $51.00 => $51.00 x .10 = 5.10 **(tax)**

  $51.00 - $5.10 = $45.90 **(buying power)**
</Callout>

We added a new transaction type called `PTP_WITHHOLDING` which will allow you to understand in the transaction history these withholdings. To learn more about transactions, please see [here](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-transactions).

### List Transactions

```json GET - "accounts/{accountID}/transactions"
[
  {
      "accountAmount": -10.21,
      "accountBalance": -12349.91,
      "accountType": "LIVE",
      "comment": "PTP WITHHOLDING IRS TAX ON SELL 5.59791552 shares of BSM at 18.23",
      "dnb": true,
      "finTranID": "KK.10ab0bf7-80c0-436b-a957-c4de6f838bb9",
      "finTranTypeID": "PTP_WITHHOLDING", //PTP FEES NOW PRESENTED IN TRANSACTIONS
      "feeSec": 0,
      "feeTaf": 0,
      "feeBase": 0,
      "feeXtraShares": 0,
      "feeExchange": 0,
      "fillQty": 5.59791552,
      "fillPx": 18.23,
      "instrument": {
          "id": "9ad10471-feee-4369-9c9a-87db904bfa5a",
          "symbol": "BSM",
          "name": "Black Stone Minerals, L.P."
      },
      ...
  },
  ...
]

```

### Order Details

```json GET - "orders/{orderID}"
{
    "id": "KK.faf8a431-ae8a-43a3-89a1-52aea4b6f3d8",
    "orderNo": "KKXP000471",
    "type": "MARKET",
    "side": "SELL",
    "status": "FILLED",
    "symbol": "BSM",
    "averagePrice": 18.25,
    "averagePriceRaw": 18.25,
    "totalOrderAmount": 273.48,
    "cumulativeQuantity": 14.98520547,
    "quantity": 14.98520547,
    "amountCash": 273.48,
    "fees": 0.02,
    "ptpWithholdingFee": 27.35, //PTP FEES NOW PRESENTED IN ORDER DETAILS
    "orderExpires": "2023-11-03T20:00:00.000Z",
    ...
}
```

### Order Event

```json Orders [Completed]

{
    "id": "event_899a7391-57a7-4577-***",
    "type": "orders.completed",
    "timestamp": "2023-11-03T15:17:07.340258117Z",
    "payload": {
        "id": "KK.faf8a431-ae8a-43a3-89a1-52aea4b6f3d8",
        "orderNo": "KKXP000471",
        "type": "MARKET",
        "side": "SELL",
        "status": "FILLED",
        "symbol": "BSM",
        "averagePrice": 18.25,
        "averagePriceRaw": 18.25,
        "totalOrderAmount": 273.48,
        "cumulativeQuantity": 14.98520547,
        "quantity": 14.98520547,
        "amountCash": 273.48,
        "fees": 0.02,
        "ptpWithholdingFee": 27.35, //PTP FEES NOW PRESENTED IN EVENTS
        "orderExpires": "2023-11-03T20:00:00.000Z",
        ...
    }
}
```

<br />

# 👀 View PTP in DriveHub

<Image align="center" src="https://files.readme.io/d22352a-Screenshot_2023-11-13_at_1.17.15_PM.png" />

<br />

# 🪙 Securities Withholding Subject To Tax

| Symbol | CUSIP     | ISIN         | Description                                   |
| :----- | :-------- | :----------- | :-------------------------------------------- |
| ET     | 29273V100 | US29273V1008 | ENERGY TRANSFER L P COM UT LTD PTN            |
| EPD    | 293792107 | US2937921078 | ENTERPRISE PRODS PARTNERS L P COM             |
| MPLX   | 55336V100 | US55336V1008 | MPLX LP COM UNIT REP LTD                      |
| IEP    | 451100101 | US4511001012 | ICAHN ENTERPRISES LP DEPOSITARY UNIT          |
| PAA    | 726503105 | US7265031051 | PLAINS ALL AMERN PIPELINE L P UNIT LTD PARTN  |
| MMP    | 559080106 | US5590801065 | MAGELLAN MIDSTREAM PRTNRS LP COM UNIT RP LP   |
| ARLP   | 01877R108 | US01877R1086 | ALLIANCE RESOURCE PARTNERS L P UT LTD PART    |
| AB     | 01881G106 | US01881G1067 | ALLIANCEBERNSTEIN HLDG L P UNIT LTD PARTN     |
| NGL    | 62913M107 | US62913M1071 | NGL ENERGY PARTNERS LP COM UNIT REPST         |
| BSM    | 09225M101 | US09225M1018 | BLACK STONE MINERALS L P COM UNIT             |
| CEQP   | 226344208 | US2263442087 | CRESTWOOD EQUITY PARTNERS LP UNIT LTD PARTNER |
| USAC   | 90290N109 | US90290N1090 | USA COMPRESSION PARTNERS LP COMUNIT LTDPAR    |
| GEL    | 371927104 | US3719271047 | GENESIS ENERGY L P UNIT LTD PARTN             |
| GLP    | 37946R109 | US37946R1095 | GLOBAL PARTNERS LP COM UNITS                  |
| NS     | 67058H102 | US67058H1023 | NUSTAR ENERGY LP UNIT COM                     |
| SUN    | 86765K109 | US86765K1097 | SUNOCO LP/SUNOCO FIN CORP COM UT REP LP       |
| CQP    | 16411Q101 | US16411Q1013 | CHENIERE ENERGY PARTNERS LP COM UNIT          |
| UAN    | 126633205 | US1266332055 | CVR PARTNERS LP COM                           |
| SPH    | 864482104 | US8644821048 | SUBURBAN PROPANE PARTNERS L P UNIT LTD PARTN  |
| DCP    | 23311P100 | US23311P1003 | DCP MIDSTREAM LP COM UT LTD PTN               |
| WES    | 958669103 | US9586691035 | WESTERN MIDSTREAM PARTNERS LP COM UNIT LP INT |
| SMLP   | 866142409 | US8661424098 | SUMMIT MIDSTREAM PARTNERS LP COM UNIT LTD     |
| WLKP   | 960417103 | US9604171036 | WESTLAKE CHEM PARTNERS LP COM UNIT RP LP      |
| HEP    | 435763107 | US4357631070 | HOLLY ENERGY PARTNERS L P COM UT LTD PTN      |
| DMLP   | 25820R105 | US25820R1059 | DORCHESTER MINERALS LP COM UNIT               |
| DKL    | 24664T103 | US24664T1034 | DELEK LOGISTICS PARTNERS LP COM UNT RP INT    |
| CAPL   | 22758A105 | US22758A1051 | CROSSAMERICA PARTNERS LP UT LTD PTN INT       |
| FUN    | 150185106 | US1501851067 | CEDAR FAIR L P DEPOSITRY UNIT                 |
| SPLP   | 85814R107 | US85814R1077 | STEEL PARTNERS HLDGS L P LTD PRTRSHIP U       |
| GHI    | 02364V206 | US02364V2060 | GREYSTONE HOUSING IMPACT INVES BEN UNIT CTF   |
| CLMT   | 131476103 | US1314761032 | CALUMET SPECIALTY PRODS PARTNE UT LTD PARTNER |
| GBLI   | 37959R103 | US37959R1032 | GLOBAL INDEMNITY GROUP LLC COM CL A           |