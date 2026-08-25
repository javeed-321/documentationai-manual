---
updatedAt: 2026-07-14T18:47:49.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# FTP document access

<Callout icon="📘" theme="info">
  ### Beta functionality

  This functionality is not yet available to all clients. Contact your Relationship Manager to learn more about timing and availability.
</Callout>

The DriveWealth SFTP environment is a secure, centralized file delivery system that provides clients with access to operational, regulatory, and reconciliation reports. Files are delivered in standard formats and are available daily or as specified below.

* **Protocol:** SFTP (SSH File Transfer Protocol)
* **Authentication:** Public-key authentication (details provided during onboarding)
* **Availability:** 24/7 access; files delivered per defined schedule

## Access and authentication

Each client will be granted access to a dedicated SFTP path. Access is controlled via public key authentication and managed through Drivewealth’s DevOps and Security teams. Clients must provide an approved public key (in the form of a `.pub` file) in advance of setup.

Access to UAT and Production files are authorized independently against different public keys.

## File naming conventions

Each delivered file is named consistently using the following structure:
`[Report_Name]_yyyymmdd[_hhmmss].csv` The timestamp at the end is available only for specific report types.

Example: `OpenedAccounts_20250701_080101.csv`

## Report catalog and delivery details

Each report listed below is delivered via SFTP under the structure noted above. All times listed are New York/Eastern time.

### Correspondent reports

* Time: See table below
* Path: `/outbound/data-products/partner-catalog-v1/correspondent/yyyymmdd/[FileName]`

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Report Name
      </th>

      <th>
        Format
      </th>

      <th>
        Description
      </th>

      <th>
        File Name
      </th>

      <th>
        Time
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Account List Report
      </td>

      <td>
        CSV
      </td>

      <td>
        The Account List details the full list of all client names and<br />account numbers in relation to the specified client.
      </td>

      <td>
        `{partner_corr_code}         _ACTLIST_yyyymmdd.csv`
      </td>

      <td>
        4:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Position Report
      </td>

      <td>
        CSV
      </td>

      <td>
        Lists of active positions in client accounts for a specified period with security details such as symbol, security type, and name of security.
      </td>

      <td>
        `{partner_corr_code}         _POS_yyyymmdd.csv`
      </td>

      <td>
        4:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Activity Report
      </td>

      <td>
        CSV
      </td>

      <td>
        The Activity Report outlines the transactions occurring in the client's account for a specific period.
      </td>

      <td>
        `{partner_corr_code}         _ACTIVITY_yyyymmdd.csv`
      </td>

      <td>
        4:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Corporate Action
      </td>

      <td>
        CSV
      </td>

      <td>
        The Corporate Activity Report details all Corporate Action related activities in the customer accounts for the client in the specified period.
      </td>

      <td>
        `{partner_corr_code}         _CORP_ACTIVITY_yyyymmdd.csv`
      </td>

      <td>
        4:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Open Lots Report
      </td>

      <td>
        CSV
      </td>

      <td>
        The Open Lots report indicates the securities in customer accounts with trade and settled dates.
      </td>

      <td>
        `{partner_corr_code}         _OPENLOTS_yyyymmdd.csv`
      </td>

      <td>
        4:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Cash Sale Not Long Report
      </td>

      <td>
        PDF
      </td>

      <td>
        Provide a comprehensive overview of cash accounts with short positions for a specified period.
      </td>

      <td>
        `CASHSALENOTLONG_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        New Accounts Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report aggregates all new accounts opened within a specific time period.
      </td>

      <td>
        `NEWACC_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Cash Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This provides a comprehensive overview of daily balances of all customer accounts with detailed account balances broken out by date.
      </td>

      <td>
        `{partner_corr_code}         _CASH_yyyymmdd.csv`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        90 Day Restriction Report
      </td>

      <td>
        PDF
      </td>

      <td>
        Lists all accounts currently in a 90-day restriction due to a good faith (GF) or pattern day trade (PDT) violation. During this 90-day period, an investor may still purchase securities with cash in the account, but the investor must fully pay for any purchase on the date of the trade
      </td>

      <td>
        `CASH90R_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Cash Call Report
      </td>

      <td>
        PDF
      </td>

      <td>
        Lists accounts that are unable to meet their cash obligations (such as funding a trade, margin requirement, or other debt) and are therefore subject to a cash call.
      </td>

      <td>
        `CASHCALL_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Concentration Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report returns accounts that have (SMV >= $50K or balances >=$50K) and combined MV of top 2 positions exceeds half of the account's margin equity value
      </td>

      <td>
        `CONCENTRATION_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        FINRA R1 Report
      </td>

      <td>
        PDF
      </td>

      <td>
        The FINRA RI report shows margin debits, cash accounts,
        and margin account credit balances for the specified date.
      </td>

      <td>
        `FINRAR1_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Funds Movement Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report shows customer accounts' detailed withdrawal and deposit activity.
      </td>

      <td>
        `FUNDSMOVEMENT_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Large Trader Identification Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report is in compliance with SEC Exchange Act Rule 13h-1, which requires the identification of any large traders with 2 million shares or $20 million in a trading day. This report provides a list of said accounts identified as a large trader and subject to the rule
      </td>

      <td>
        `LTID_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Liquidation Exception Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report returns accounts where positions were liquidated, but the liquidation did not follow the standard margin call, house call, or maintenance margin liquidation procedures.
      </td>

      <td>
        `LIQUIDATIONEXCEPTION_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Margin Account Liquidation Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report returns accounts that failed to meet margin requirements.
      </td>

      <td>
        `MARGINLIQUIDATION_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Minimum Net Equity Report
      </td>

      <td>
        PDF
      </td>

      <td>
        Tracks the Pattern Day Trader (PDT) accounts that fall below the 25K threshold. An account flagged as a PDT is required to maintain a minimum of 25K of equity.
      </td>

      <td>
        `MINEQUITY_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Non-Pattern Day Trader Margin Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report has been replaced with a counter on DriveHub under the Pattern Day Trading tab.
      </td>

      <td>
        `NONPATTERNDT_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        TEFRA Non-Resident Withholding Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report returns accounts that are non-U.S. person with details on types of the payment and the withholding rate.
      </td>

      <td>
        `NRATEFRAWITHHOLDING_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        2% Holding Report
      </td>

      <td>
        PDF
      </td>

      <td>
        This report shows any clients holding 2% of a specific security
      </td>

      <td>
        `TWOPERCENTHOLDINGS_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>

    <tr>
      <td>
        Good Faith Violation
      </td>

      <td>
        PDF
      </td>

      <td>
        This report return the list of account with GFV flags
      </td>

      <td>
        `GOODFAITHVIOLATION_{partner_corr_code}         _mmddyyy.pdf`
      </td>

      <td>
        8:00 am ET
      </td>
    </tr>
  </tbody>
</Table>

### Trade Recap reports

<Callout icon="🚧" theme="warn">
  ###

  This report is only available for DVP accounts.
</Callout>

* Time: Account-specific
* Path: `/outbound/data-products/partner-catalog-v1/TradeRecap/yyyymmdd/TradeRecap_<AccountNo>_<NetOrGross>_yyyymmdd_hhmmss.csv`

### Non-Custody Fails report

<Callout icon="🚧" theme="warn">
  ###

  This report is only available for DVP accounts.
</Callout>

* Time: 4:00 PM
* Path: `/outbound/data-products/partner-catalog-v1/fail_report/yyyymmdd/nc_fail_report_ yyyymmdd_hhmmss.csv`

<br />