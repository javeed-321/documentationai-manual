---
updatedAt: 2026-08-23T16:01:35.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# MCP Tool Catalog

This catalog is generated directly from the `tools/list` response. Grouping is by REST endpoint root as stated in each tool's `description` field 17 categories, \~100 tools.

**Status legend:**

| Label          | Meaning                                                                   |
| :------------- | :------------------------------------------------------------------------ |
| *(blank)*      | No restriction stated in schema                                           |
| `Deprecated`   | Schema states a replacement tool exists; avoid for new integrations       |
| `Sandbox only` | Schema states this tool is registered only in dev/qa/sandbox environments |

## Contents

* [Accounts](#accounts)
* [Orders](#orders)
* [Instruments & Quotes](#instruments--quotes)
* [Funding — Deposits & Withdrawals](#funding--deposits--withdrawals)
* [Asset Transfers](#asset-transfers)
* [Trade Allocations & Advisor Views](#trade-allocations--advisor-views)
* [Exchanges (Instrument-to-Instrument)](#exchanges-instrument-to-instrument)
* [Users & Onboarding](#users--onboarding)
* [Entities (Business/Trust Accounts)](#entities-businesstrust-accounts)
* [Bank Accounts](#bank-accounts)
* [Documents](#documents)
* [Statements, Confirms & Tax Forms](#statements-confirms--tax-forms)
* [Transactions](#transactions)
* [Settlements & Reconciliation](#settlements--reconciliation)
* [Reports](#reports)
* [Reference Data](#reference-data)
* [Documentation Search](#documentation-search)

***

## Accounts

| Tool                             | Endpoint                                                 | Status     | Description                                                                                                                                                                                                        |
| :------------------------------- | :------------------------------------------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_account`                 | `POST /accounts`                                         |            | Creates a trading Account.                                                                                                                                                                                         |
| `get_account`                    | `GET /accounts/{accountID}`                              |            | Retrieves Account details by accountID.                                                                                                                                                                            |
| `update_account`                 | `PATCH /accounts/{accountID}`                            |            | Updates Account details by accountID.                                                                                                                                                                              |
| `get_account_summary`            | `GET /accounts/{accountID}/summary`                      | Deprecated | The full Account Summary API is now deprecated. Schema states: use the individual APIs for Positions, Transactions, or Orders instead (`list_account_positions`, `list_account_transactions`, or the order tools). |
| `list_account_statements`        | `GET /accounts/{accountID}/statements`                   |            | Retrieves a list of Account Statements by accountID.                                                                                                                                                               |
| `list_account_positions`         | `GET /accounts/{accountID}/summary/positions`            |            | Retrieves a list of Account Positions by accountID.                                                                                                                                                                |
| `get_account_cash`               | `GET /accounts/{accountID}/summary/money`                |            | Retrieves an Account Cash details by accountID.                                                                                                                                                                    |
| `get_account_margin`             | `GET /accounts/{accountID}/summary/margin`               |            | Retrieves Account Margin details by accountID.                                                                                                                                                                     |
| `list_account_lots`              | `GET /accounts/{accountID}/position-details`             |            | Retrieves an Account Lots details by accountID.                                                                                                                                                                    |
| `list_account_options_positions` | `GET /accounts/{accountID}/options/positions`            |            | Retrieves Account Option Positions.                                                                                                                                                                                |
| `list_commission_schedules`      | `GET /accounts/{accountID}/commissions`                  |            | Retrieves a list of Commissions Schedules by accountID.                                                                                                                                                            |
| `get_account_performance`        | `GET /accounts/{accountID}/performance-returns`          |            | Retrieves end of day account performance including balances, cash flows, rate of return, and other attributes.                                                                                                     |
| `get_account_virtual_bank`       | `GET /accounts/{accountID}/funding/deposit-instructions` |            | Retrieves an Account Virtual Bank Account details by accountID.                                                                                                                                                    |
| `list_account_deposits`          | `GET /accounts/{accountID}/funding/deposits`             |            | Retrieves a list of Account Deposits by accountID.                                                                                                                                                                 |
| `list_account_withdrawals`       | `GET /accounts/{accountID}/funding/redemptions`          |            | Retrieves a list of Account Withdrawals by accountID.                                                                                                                                                              |
| `create_account_beneficiaries`   | `POST /accounts/{accountID}/beneficiaries`               |            | Creates an Account Beneficiary by accountID.                                                                                                                                                                       |
| `get_account_beneficiaries`      | `GET /accounts/{accountID}/beneficiaries`                |            | Retrieves a list of Account Beneficiaries by accountID.                                                                                                                                                            |
| `delete_account_beneficiaries`   | `DELETE /accounts/{accountID}/beneficiaries`             |            | Removes all Account Beneficiaries by accountID.                                                                                                                                                                    |
| `list_account_violations`        | `GET /accounts/{accountID}/violations`                   |            | Retrieves a list of Account Violations by accountID (good-faith violations, PDT violations, and an account equity breakdown, per schema).                                                                          |
| `get_account_violations_summary` | `GET /accounts/{accountID}/summary/violations`           |            | Retrieves Account Violations Summary details by accountID.                                                                                                                                                         |

## Orders

| Tool                             | Endpoint                                          | Status | Description                                                                                                      |
| :------------------------------- | :------------------------------------------------ | :----- | :--------------------------------------------------------------------------------------------------------------- |
| `create_order`                   | `POST /orders`                                    |        | Create an Order — equity, fractional, options, fixed income, or mutual fund.                                     |
| `get_order`                      | `GET /orders/{orderID}`                           |        | Retrieves an Order details by orderID.                                                                           |
| `update_order`                   | `PATCH /orders/{orderID}`                         |        | Updates an Order by orderID. Schema states current use is to cancel a resting order via `method: CANCEL`.        |
| `list_account_resting_orders`    | `GET /accounts/{accountID}/summary/orders`        |        | Retrieves a list of Account Orders by accountID; returns currently pending Orders awaiting fill or cancellation. |
| `list_account_historical_orders` | `GET /accounts/{accountID}/reports/order-history` |        | Retrieves a list of Account Orders by accountID; returns orders that have been closed (filled or canceled).      |
| `get_order_by_order_no`          | `GET /orders/byOrderNo/{orderNo}`                 |        | Retrieves an Order by OrderNo.                                                                                   |

## Instruments & Quotes

| Tool                                     | Endpoint                                                           | Status | Description                                                                                                                                   |
| :--------------------------------------- | :----------------------------------------------------------------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_instruments`                       | `GET /instruments`                                                 |        | Retrieves a list of Instruments.                                                                                                              |
| `get_instrument`                         | `GET /instruments/{symbolOrInstrumentID}`                          |        | Retrieves an Instrument details by symbol or instrumentID.                                                                                    |
| `get_instrument_options_chain`           | `GET /instruments/{symbolOrInstrumentID}/options`                  |        | Retrieves an Instrument Options Chain by symbol or instrumentID.                                                                              |
| `get_instrument_option_expiration_dates` | `GET /instruments/{symbolOrInstrumentID}/options/expiration-dates` |        | Retrieve an Instrument Option Expiration details by symbol or instrumentID.                                                                   |
| `search_instruments`                     | `POST /instruments/filter`                                         |        | Searches Instruments based on filter criteria. Schema states these filter fields are oriented toward fixed-income/debt instrument attributes. |
| `get_quote`                              | `GET /quotes`                                                      |        | Fetch the realtime or 15-minute delayed referential quote details for a specific security.                                                    |
| `get_quote_vdr`                          | `GET /quotes/vdr`                                                  |        | Fetch the NBBO quote details for a specific security.                                                                                         |
| `get_quote_depth`                        | `POST /quotes/depth`                                               |        | Get the Depth of Book for an Instrument. Schema states this API currently only works with debt instruments.                                   |

## Funding — Deposits & Withdrawals

| Tool                            | Endpoint                                            | Status       | Description                                                                                                                               |
| :------------------------------ | :-------------------------------------------------- | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `create_deposit`                | `POST /funding/deposits`                            |              | Creates a Deposit. Schema states supported methods: ACH, BULK\_FUNDING, CASH\_PROMOTION, CASH\_TRANSFER.                                  |
| `list_deposits`                 | `GET /funding/deposits`                             |              | Retrieves a list of Deposits across all accounts.                                                                                         |
| `get_deposit`                   | `GET /funding/deposits/{depositID}`                 |              | Retrieves Deposit details by depositID.                                                                                                   |
| `update_deposit_ach_settlement` | `PATCH /funding/deposits/{depositID}/achSettlement` | Sandbox only | Schema states: "NON-PROD / SANDBOX ONLY. Sensitive non-production financial operation... registered only in dev/qa/sandbox environments." |
| `get_recurring_deposit`         | `GET /funding/recurring-deposits/{recurringID}`     |              | Retrieves Recurring Deposits details by recurringID.                                                                                      |
| `update_recurring_deposit`      | `PATCH /funding/recurring-deposits/{recurringID}`   |              | Updates Recurring Deposit details by recurringID.                                                                                         |
| `delete_recurring_deposit`      | `DELETE /funding/recurring-deposits/{recurringID}`  |              | Deactivates Recurring Deposit details by recurringID.                                                                                     |
| `create_withdrawal`             | `POST /funding/redemptions`                         |              | Creates a Withdrawal. Schema states supported methods: ACH, WIRE, CASH\_TRANSFER, BULK\_FUNDING.                                          |
| `list_withdrawals`              | `GET /funding/redemptions`                          |              | Retrieves a list of Withdrawals across all accounts.                                                                                      |
| `get_withdrawal`                | `GET /funding/redemptions/{redemptionID}`           |              | Retrieves a Withdrawal by redemptionID.                                                                                                   |

## Asset Transfers

| Tool                             | Endpoint                                 | Status | Description                                                                                                                       |
| :------------------------------- | :--------------------------------------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `create_acats_transfer`          | `POST /asset-transfers/acats`            |        | ACATS transfer — the Automated Customer Account Transfer Service, for moving securities to/from an external brokerage per schema. |
| `update_acat_transfer`           | `PATCH /asset-transfers/acats`           |        | Review ACAT transfer request; used to reject securities from the transfer.                                                        |
| `list_acats_brokers`             | `GET /asset-transfers/acats/brokers`     |        | Retrieve a list of available ACATS brokers.                                                                                       |
| `create_minor_graduation`        | `POST /asset-transfers/minor-graduation` |        | Transfers assets from a minor's custodial account to their own named account once they reach the age of majority, per schema.     |
| `create_internal_asset_transfer` | `POST /asset-transfers/transfers`        |        | Transfers cash and/or securities between accounts at DriveWealth under the same ownership.                                        |
| `get_transfer`                   | `GET /asset-transfers/{assetTransferID}` |        | Get a Transfer's current details.                                                                                                 |
| `list_transfers`                 | `GET /asset-transfers`                   |        | Lists all Transfers across all Accounts; filterable by Transfer type.                                                             |

## Trade Allocations & Advisor Views

| Tool                                | Endpoint                                     | Status | Description                                                          |
| :---------------------------------- | :------------------------------------------- | :----- | :------------------------------------------------------------------- |
| `create_trade_allocation`           | `POST /managed/allocations`                  |        | Create a Trade Allocation.                                           |
| `get_trade_allocation`              | `GET /managed/allocations/{allocationID}`    |        | Retrieves Trade Allocation by allocationID.                          |
| `list_allocations_by_advisor`       | `GET /users/{userID}/managed/orders`         |        | Fetches a user's sub-account order allocations by userID.            |
| `list_orders_by_advisor`            | `GET /users/{userID}/managed/orders/summary` |        | Fetches a User's sub-account order allocations summary by date.      |
| `list_trade_allocations_by_advisor` | `GET /users/{userID}/managed/allocations`    |        | Fetches a list of a User's allocations.                              |
| `get_bod_by_advisor`                | `GET /users/{userID}/managed/bod`            |        | Fetches a list of sub-accounts' beginning-of-day holdings by userID. |

## Exchanges (Instrument-to-Instrument)

| Tool                           | Endpoint                                             | Status | Description                                                                         |
| :----------------------------- | :--------------------------------------------------- | :----- | :---------------------------------------------------------------------------------- |
| `create_exchange`              | `POST /exchanges`                                    |        | Creates an Instrument Exchange — sale of a held instrument and purchase of another. |
| `update_exchange`              | `PATCH /exchanges`                                   |        | Updates an Instrument Exchange; currently used to cancel via `method: CANCEL`.      |
| `get_exchange`                 | `GET /exchanges/{exchangeIdentifier}`                |        | Retrieves specific exchange details.                                                |
| `list_account_exchanges`       | `GET /accounts/{accountID}/summary/exchanges`        |        | Retrieves a list of Account Instrument Exchanges by accountID.                      |
| `get_account_exchange_history` | `GET /accounts/{accountID}/reports/exchange-history` |        | Retrieves a list of Account Instrument Exchange History by accountID.               |

## Users & Onboarding

| Tool                             | Endpoint                                  | Status | Description                                              |
| :------------------------------- | :---------------------------------------- | :----- | :------------------------------------------------------- |
| `create_user`                    | `POST /users`                             |        | Creates a User.                                          |
| `get_user`                       | `GET /users/{userID}`                     |        | Retrieves a User details by userID.                      |
| `update_user`                    | `PATCH /users/{userID}`                   |        | Updates a User details by userID.                        |
| `get_user_kyc_status`            | `GET /users/{userID}/kyc-status`          |        | Retrieves a User KYC by userID.                          |
| `list_user_accounts`             | `GET /users/{userID}/accounts`            |        | Retrieves a list of User Accounts by userID.             |
| `list_user_physical_documents`   | `GET /users/{userID}/documents`           |        | Retrieves a list of User Physical Documents by userID.   |
| `list_user_linked_bank_accounts` | `GET /users/{userID}/bank-accounts`       |        | Retrieves a list of User Linked Bank Accounts by userID. |
| `list_user_recurring_deposits`   | `GET /users/{userID}/recurring-deposits`  |        | Retrieves a list of User Recurring Deposits by userID.   |
| `list_user_deposits`             | `GET /users/{userID}/funding/deposits`    |        | Retrieves a list of User Deposits by userID.             |
| `list_user_withdrawals`          | `GET /users/{userID}/funding/redemptions` |        | Retrieves a list of User Withdrawals by userID.          |

## Entities (Business/Trust Accounts)

| Tool            | Endpoint                     | Status | Description                                                                      |
| :-------------- | :--------------------------- | :----- | :------------------------------------------------------------------------------- |
| `create_entity` | `POST /entities`             |        | Creates an Entity — a business or trust (CORPORATION, LLC, or TRUST) per schema. |
| `get_entity`    | `GET /entities/{entityId}`   |        | Retrieves an Entity details by entityId.                                         |
| `update_entity` | `PATCH /entities/{entityId}` |        | Updates an Entity.                                                               |

## Bank Accounts

| Tool                           | Endpoint                                | Status | Description                                       |
| :----------------------------- | :-------------------------------------- | :----- | :------------------------------------------------ |
| `link_bank_account`            | `POST /bank-accounts`                   |        | Links an external Bank Account.                   |
| `retrieve_linked_bank_account` | `GET /bank-accounts/{bankAccountID}`    |        | Retrieves a Linked Bank Account by bankAccountID. |
| `update_linked_bank_account`   | `PATCH /bank-accounts/{bankAccountID}`  |        | Updates a Linked Bank Account by bankAccountID.   |
| `delete_linked_bank_account`   | `DELETE /bank-accounts/{bankAccountID}` |        | Removes a Linked Bank Account by bankAccountID.   |

## Documents

| Tool                             | Endpoint                          | Status | Description                                                                                                     |
| :------------------------------- | :-------------------------------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| `upload_physical_document`       | `POST /documents`                 |        | Uploads a Physical Document — per schema, for KYC identity verification or asset-transfer supporting paperwork. |
| `retrieve_physical_document_url` | `GET /documents/{documentID}/url` |        | Retrieves a Physical Document by documentID; returns a short-lived download URL per schema.                     |

## Statements, Confirms & Tax Forms

| Tool                               | Endpoint                                | Status | Description                                                                                         |
| :--------------------------------- | :-------------------------------------- | :----- | :-------------------------------------------------------------------------------------------------- |
| `get_statement`                    | `GET /statements/{accountID}/{fileKey}` |        | Retrieves an Account Statement (Monthly, Trade Confirms, Tax Forms, etc.) by accountID and fileKey. |
| `list_account_tax_statements`      | `GET /accounts/{accountID}/taxforms`    |        | Retrieves a list of Account Tax Statements by accountID.                                            |
| `list_account_trade_confirmations` | `GET /accounts/{accountID}/confirms`    |        | Retrieves a list of Account Trade Confirmations by accountID.                                       |

## Transactions

| Tool                              | Endpoint                                         | Status     | Description                                                                                                                             |
| :-------------------------------- | :----------------------------------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| `get_account_transaction_summary` | `GET /accounts/{accountID}/summary/transactions` | Deprecated | Schema states: deprecated; use `list_account_transactions` for historical transactions and `list_account_historical_orders` for orders. |
| `list_account_transactions`       | `GET /accounts/{accountID}/transactions`         |            | Retrieves a list of Account Transactions by accountID.                                                                                  |

## Settlements & Reconciliation

| Tool                    | Endpoint                                                   | Status       | Description                                                                                                                                                                     |
| :---------------------- | :--------------------------------------------------------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `get_settlements`       | `GET /settlements`                                         |              | Retrieves a list of Settlements.                                                                                                                                                |
| `get_settlement`        | `GET /settlements/{settlementID}`                          |              | Retrieves Settlement by settlementID.                                                                                                                                           |
| `update_settlement`     | `PATCH /settlements/{settlementID}`                        |              | Updates Settlement by settlementID.                                                                                                                                             |
| `attest_settlement`     | `PATCH /settlements/{settlementID}/attest`                 |              | Attests a Settlement if in a successful state and not already attested; schema notes this is only available if the attestation feature is enabled for the Correspondent Client. |
| `list_reconciliations`  | `GET /funding/reconciliations`                             |              | Fetches a list of daily reconciliations for a firm using cashless settlement.                                                                                                   |
| `get_reconciliation`    | `GET /funding/reconciliations/{reconciliationID}`          |              | Fetches reconciliation details for a firm using cashless settlement.                                                                                                            |
| `update_reconciliation` | `PATCH /funding/reconciliations/{reconciliationID}`        | Sandbox only | Schema states: "NON-PROD / SANDBOX ONLY. Sensitive non-production financial operation... registered only in dev/qa/sandbox environments."                                       |
| `attest_reconciliation` | `PATCH /funding/reconciliations/{reconciliationID}/attest` |              | Attests a reconciliation report if successful and not already attested; schema notes this is only available if the attestation feature is enabled for the Correspondent Client. |

## Reports

| Tool                         | Endpoint                                                           | Status | Description                                                                                                                        |
| :--------------------------- | :----------------------------------------------------------------- | :----- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `get_correspondent_reports`  | `GET /correspondantReport`                                         |        | Fetches daily reports (positions, account activity, balances, etc.) in file format; returns a short-lived download URL per schema. |
| `create_daily_trade_summary` | `POST /accounts/{accountID}/reports/daily-trade-summary`           |        | Creates a job to generate a DVP/RVP Report.                                                                                        |
| `list_daily_trade_summaries` | `GET /accounts/{accountID}/reports/daily-trade-summary`            |        | Lists DVP/RVP reports.                                                                                                             |
| `get_daily_trade_summary`    | `GET /accounts/{accountID}/reports/daily-trade-summary/{reportID}` |        | Retrieves a DVP/RVP report by reportID.                                                                                            |

## Reference Data

| Tool                       | Endpoint         | Status | Description                                                                                                          |
| :------------------------- | :--------------- | :----- | :------------------------------------------------------------------------------------------------------------------- |
| `list_supported_countries` | `GET /countries` |        | Retrieves a list of allowed countries for onboarding. `status` (`ACTIVE`/`INACTIVE`) is a required input per schema. |

## Documentation Search

| Tool          | Endpoint        | Status | Description                                                                                                                          |
| :------------ | :-------------- | :----- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `search_docs` | *(none stated)* |        | Search the DriveWealth API documentation for endpoint details, request/response shapes, required parameters, and field descriptions. |