---
updatedAt: 2026-07-14T18:55:06.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Cash interest

<Callout icon="🚧" theme="warn">
  ###

  Details on this page are for enhancements not yet launched. The DriveWealth Bank Sweep Program will be updated according to the below details in October.
</Callout>

The DriveWealth Bank Sweep Program is a cash management solution that automatically sweeps uninvested cash from brokerage accounts into interest-bearing deposit accounts to a network of FDIC-insured banks. The program is designed to help earn interest on idle cash while increasing FDIC coverage by distributing funds across multiple banks.

Customer funds swept into the program are held at FDIC-insured banks and are protected up to $250,000 per depositor, per bank, up to $1 million.

R\&T Deposit Solutions (“R\&T”) administers the program on behalf of DriveWealth. Further Terms and Conditions are available [on our legal site](https://legal.drivewealth.com/cash-management-program-disclosure-statement-bank-sweep) .

## Customer enrollment and opt-out

Clients and their customers who selected the Bank Sweep Program are enrolled automatically upon Account creation. The Program terms and conditions are part of the [standard disclosures](https://developer.drivewealth.com/apis/docs/showing-disclosures)  that all users should be presented and must acknowledge.

Individual customers may opt-out of the sweep program entirely. If a user opts out, idle cash will remain in the brokerage account as a non-interest-bearing cash balance.

Customers can also request to opt out of specific banks. As part of the Program, you must

* Accept and document opt-out requests.
* Coordinate with DriveWealth to update the customer’s bank exclusions.
* Advise customers that opting out may reduce their total FDIC insurance coverage.

All opt-out requests, either for the entire program or individual banks, should be submitted via ticket to DriveWealth.

The `sweepInd` flag when [retrieving an Account](https://developer.drivewealth.com/apis/reference/get_accounts-accountid) denotes whether an Account is enrolled in the Program.

## Interest payments

Interest is calculated daily and paid shortly after month end. Interest may be split among the customer, client, and DriveWealth.

When interest is paid, a Transaction is posted to each Account, like the following:

```json
{
        "accountAmount": 6.18,
        "accountBalance": 1055.71,
        "accountType": "LIVE",
        "comment": "July 2025 Interest",
        "dnb": false,
        "finTranID": "MH.b1680a4b-112d-402a-8840-58a0c3f6021e",
        "finTranTypeID": "INT",
        "feeSec": 0,
        "feeTaf": 0,
        "feeBase": 0,
        "feeXtraShares": 0,
        "feeExchange": 0,
        "fillQty": 0,
        "fillPx": 0,
        "orderID": "0",
        "sendCommissionToInteliclear": false,
        "systemAmount": 0,
        "tranAmount": 6.18,
        "tranSource": "INTE",
        "tranWhen": "2025-08-04T04:24:13.457Z",
        "wlpAmount": 0,
        "wlpFinTranTypeID": "8d5ee61d-8539-4d62-9871-fdcbc1f6f2f4"
}
```

Interest payments are not subject to US tax withholding.

## Statements and confirms

Interest payments do not generate Trade Confirmations. Sweep activity (i.e., movements of idle cash into or out of the DriveWealth Bank Sweep Deposit Program) is considered routine cash management and does not generate individual trade confirmations.

On Monthly Statements, sweep activity will appear as a single line item showing the total balance held in the DriveWealth Bank Sweep Deposit Program. In addition, the monthly statement will include a bank-by-bank breakdown, showing:

* Each program bank where cash is held
* The amount allocated to each bank
* Total FDIC-insured balance

<br />