Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release v1.82.0

Hey, we are back with another release. We are always improving the platform and if you have any questions regarding any release, feel free to contact your relations manager or email us directly at [RMteam@drivewealth.com](mailto:rmteam@drivewealth.com).

| Status           | Environment |
| :--------------- | :---------: |
| ✨💃🏻 Prime Time |     PROD    |

# 🚀 New Features

## Redemption remittance information

We have added support for `remittanceInformation` on funding redemptions. This gives partners additional flexibility when submitting and reviewing redemption details.

## Account funding type

We have added `accountFundingType` to account creation, account updates, and account retrieval endpoints so partners can better classify account funding behavior.

## Expanded identification document support

The documents object on user endpoints now accepts a broader set of ID types and metadata fields, enabling account opening for international and non-citizen users.

New document types: `PASSPORT`, `ALIEN_ID`, and `OTHER` are now valid values for the type field. `FTNLO` has been removed. New metadata fields: `issueDate`, `expiryDate`, `issuingCountry`, `issuingProvince`, and `description` are now accepted on `POST /users and PATCH /users/{userID}`. Read support: `GET /users/{userID}` now returns `idIssueDate`, `idExpiryDate`, `idIssuingCountry`, and `idIssuingProvince` at the top level of the user object.

Affected endpoints: `POST /users`, `PATCH /users/{userID}`, `GET /users/{userID}`

## Trust and entity enhancements

We enhanced our entity and account support for trust workflows, including new trust account management types and expanded entity role modeling.

## Deposits API

We have added a new deposit endpoint to support updates the ACH settlement dates for a deposit by depositID.

New endpoints:

`PATCH /funding/deposits/{depositID}/achSettlement`

# 🎉 Feature Enhancements

## Deposit processing status updates

We expanded deposit status handling to support the new `PROCESSING` state across deposit, recurring deposit, and user funding deposit responses. This gives partners more visibility into in-flight deposit activity.

## Deposit seasoning details

We enhanced deposit retrieval responses by adding `seasoningDetails` to deposit details.

## Funding redemption filtering

We added new query parameters to redemption listing so partners can filter and paginate redemption activity more effectively.

## Remittance information documentation

We corrected and clarified the description for `remittanceInformation` across redemption request and response payloads.

## Account funding and overnight trading support

We improved account configuration support with `accountFundingType`, `overnightHoursEnrolled`, and additional money summary visibility through `cashAvailableForTradeNonMarginable`.

## Instrument data improvements

We enhanced instrument responses with `averageLendingRate` for equities and expanded mutual fund metadata support, including new fields and validation updates.

## Identification and beneficiary cleanup

We removed the legacy `FTNLO` identification type from supported schemas and improved beneficiary modeling with document support and refined request/response structures.

## IRA enum cleanup

We removed unsupported IRA contribution and distribution enum values while also expanding shared enum support for newer retirement use cases.

# 👠🐛 Squashing bugs

We are always squashing bugs, but nothing significant during this release that should be called out.

# 🪵 ChangeLog

```markdown
## New endpoints

**`PATCH /funding/deposits/{depositID}/achSettlement`**
  - Added new endpoint

## Modified endpoints

**`POST /funding/redemptions`**
- Request payload:
  - Added property `remittanceInformation`
  - Updated description for `remittanceInformation`
  - Updated description for `amount`
  - Removed IRA distribution values `CONVERSION` and `RECHARACTERIZATION`
- Modified the `200` response:
  - Added property `remittanceInformation`
  - Updated description for `amount`
  - Removed IRA distribution values `CONVERSION` and `RECHARACTERIZATION`

**`GET /funding/redemptions/{redemptionID}`**
- Modified the `200` response:
  - Added property `remittanceInformation`
  - Updated description for `remittanceInformation`
  - Removed IRA distribution values `CONVERSION` and `RECHARACTERIZATION`

**`GET /funding/redemptions`**
- Path parameters:
  - Added query parameters `from`, `to`, `limit`, `direction`, `offset`, and `parentIBID`
- Modified the `200` response:
  - Removed IRA distribution values `CONVERSION` and `RECHARACTERIZATION`

**`GET /funding/deposits`**
- Updated request description
- Updated recurringFrequency description to clarify retirement schedules are CURRENT_YEAR only
- Path parameters:
  - Added query parameter `parentIBID`

**`GET /funding/deposits/{depositID}`**
- Modified the `200` response:
  - Added property `seasoningDetails`
  - Added `PROCESSING` as a supported `status` value
  - Added status history support for status code `17`
  - Added `PROCESSING` as a supported `statusMessage` value
  - Removed IRA contribution values `DIRECT_ROLLOVER`, `INDIRECT_ROLLOVER`, `DIRECT_TRANSFER`, `CONVERSION`, and `RECHARACTERIZATION`

**`POST /funding/deposits`**
- Request payload:
  - Added new `400` response
  - Updated `originatorBankDetails` to use `bankCountry`
  - Removed `bankAccountCountry`
  - Removed IRA contribution values `DIRECT_ROLLOVER`, `INDIRECT_ROLLOVER`, `DIRECT_TRANSFER`, `CONVERSION`, and `RECHARACTERIZATION`
- Modified the `200` response:
  - Added `PROCESSING` as a supported `status` value
  - Removed IRA contribution values `DIRECT_ROLLOVER`, `INDIRECT_ROLLOVER`, `DIRECT_TRANSFER`, `CONVERSION`, and `RECHARACTERIZATION`

**`GET /accounts/{accountID}/funding/deposits`**
- Path parameters:
  - Added query parameters `status`, `type`, `limit`, and `offset`
  - Added new `400` response
- Modified the `200` response:
  - Added status code `17`
  - Added `PROCESSING` as a supported status message

**`GET /accounts/{accountID}/funding/redemptions`**
- Path parameters:
  - Added query parameters `status`, `type`, `limit`, and `offset`
  - Added new `400` response

**`GET /users/{userID}/funding/deposits`**
- Path parameters:
  - Added query parameters `status`, `type`, `limit`, and `offset`
  - Added new `400` response
- Modified the `200` response:
  - Added status code `17`
  - Added `PROCESSING` as a supported status message

**`GET /users/{userID}/funding/redemptions`**
- Path parameters:
  - Added query parameters `status`, `type`, `limit`, and `offset`
  - Added new `400` response

**`DELETE /funding/recurring-deposits/{recurringID}`**
- Modified the `200` response:
  - Added `PROCESSING` as a supported deposit history status

**`GET /funding/recurring-deposits/{recurringID}`**
- Modified the `200` response:
  - Added `PROCESSING` as a supported deposit history status

**`POST /accounts`**
- Request payload:
  - Added property `accountFundingType`
  - Added property `overnightHoursEnrolled` under `accountFeatures.equities`
  - Added trust account management types `TRUST_SELF`, `TRUST_ADVISORY`, and `TRUST_RIA_MANAGED`
- Modified the `200` response:
  - Added property `accountFundingType`
  - Added property `overnightHoursEnrolled` under `accountFeatures.equities`

**`GET /accounts/{accountID}`**
- Modified the `200` response:
  - Added property `accountFundingType`
  - Added property `overnightHoursEnrolled` under `accountFeatures.equities`

**`PATCH /accounts/{accountID}`**
- Request payload:
  - Added property `accountFundingType`
  - Added property `overnightHoursEnrolled` under `accountFeatures.equities`
- Modified the `200` response:
  - Added property `accountFundingType`
  - Added property `overnightHoursEnrolled` under `accountFeatures.equities`

**`GET /accounts/{accountID}/summary`**
- Modified the `200` response:
  - Added property `cashAvailableForTradeNonMarginable`

**`GET /accounts/{accountID}/summary/money`**
- Modified the `200` response:
  - Added property `cashAvailableForTradeNonMarginable`

**`GET /accounts/{accountID}/summary/violations`**
- Modified the `200` response:
  - Updated description for `violations.details`

**`POST /users`**
- Request payload:
  - Added identification document properties `expiryDate`, `issueDate`, `issuingCountry`, `issuingProvince`, and `description`
  - Expanded identification type enum values to include `PASSPORT`, `ALIEN_ID`, and `OTHER`
  - Removed `FTNLO`
  - Updated description for identification `type`
  - Added property `dateOfDeath`
  - Added `walletSettlementProfileID`-related tax model cleanup with `usTaxpayer`
  - Updated director information modeling
- Modified the `200` response:
  - Added identification document properties `expiryDate`, `issueDate`, `issuingCountry`, `issuingProvince`, and `description`
  - Expanded identification type enum values to include `PASSPORT`, `ALIEN_ID`, and `OTHER`
  - Removed `FTNLO`
  - Updated description for identification `type`
  - Added property `dateOfDeath`
  - Added `usTaxpayer`
  - Updated director information modeling

**`GET /users/{userID}`**
- Modified the `200` response:
  - Added properties `idIssuingCountry`, `idIssueDate`, `idIssuingProvince`, and `idExpiryDate`
  - Added property `dateOfDeath`
  - Added properties `w8received` and `w8expires`
  - Added property `institutionalDirectorInfo`

**`PATCH /users/{userID}`**
- Request payload:
  - Added identification document properties `description`, `issueDate`, `issuingProvince`, `issuingCountry`, and `expiryDate`
  - Expanded identification type enum values to include `PASSPORT`, `ALIEN_ID`, and `OTHER`
  - Removed `FTNLO`
  - Updated description for identification `type`
  - Added property `dateOfDeath`
  - Removed `usTaxPayer`
  - Added `usTaxpayer`
  - Updated director information modeling
- Modified the `200` response:
  - Added properties `idIssuingProvince`, `idExpiryDate`, `idIssuingCountry`, and `idIssueDate`
  - Added property `dateOfDeath`
  - Added properties `w8received` and `w8expires`
  - Added property `institutionalDirectorInfo`

**`GET /accounts/{accountID}/beneficiaries`**
- Modified the `200` response:
  - Added property `documentID`
  - Removed `FTNLO` from `idType`
  - Updated description for `idType`

**`POST /accounts/{accountID}/beneficiaries`**
- Request payload:
  - Property `primary` is now required
  - Split beneficiary request modeling into entity and person beneficiary schemas
- Modified the `200` response:
  - Added property `documentID`
  - Removed `FTNLO` from `idType`
  - Updated description for `idType`

**`GET /settlements`**
- Modified the `200` response:
  - Removed `REJECTED` from supported settlement status values

**`GET /settlements/{settlementID}`**
- Modified the `200` response:
  - Removed `REJECTED` from supported settlement status values

**`PATCH /funding/reconciliations/{reconciliationID}`**
- Modified the `200` response:
  - Removed schema `ReconciliationDetails`

**`PATCH /funding/reconciliations/{reconciliationID}/attest`**
- Modified the `200` response:
  - Updated attestation response schema handling
  - Removed previously exposed reconciliation detail properties from the root response

**`PATCH /settlements/{settlementID}/attest`**
- Modified the `200` response:
  - Updated attestation response schema handling
  - Removed previously exposed settlement detail properties from the root response

**`GET /instruments/{symbolOrInstrumentID}`**
- Modified the `200` response:
  - Added property `averageLendingRate`
  - Added mutual fund properties `minimumHoldingAmount` and `subAssetClassCategory`
  - Expanded `mutualFundData.shareClass` to include `OTHER`
  - Updated `mutualFundData.maximumPurchaseAmount` to support decimal values

**`POST /entities`**
- Request payload:
  - Added entity identification property `ssn`
  - Added entity type `TRUST`
  - Updated description for `subType`
- Modified the `201` response:
  - Added entity identification property `ssn`
  - Added entity type `TRUST`
  - Added director properties `percentage` and `controlContact`
  - Expanded supported director roles to include `TRUSTEE`, `GRANTOR`, and `BENEFICIARY`

**`GET /entities/{entityId}`**
- Modified the `200` response:
  - Added entity identification property `ssn`
  - Added entity type `TRUST`
  - Added director properties `percentage` and `controlContact`
  - Expanded supported director roles to include `TRUSTEE`, `GRANTOR`, and `BENEFICIARY`

**`PATCH /entities/{entityId}`**
- Request payload:
  - Added entity identification property `ssn`
  - Added entity type `TRUST`
  - Updated description for `subType`
- Modified the `200` response:
  - Added entity identification property `ssn`
  - Added entity type `TRUST`
  - Added director properties `percentage` and `controlContact`
  - Expanded supported director roles to include `TRUSTEE`, `GRANTOR`, and `BENEFICIARY`

## Documentation updates

**Deposit event documentation**
- Added `depositBuyingPowerHoldExpires`, `seasoningPeriodExpires`, and `recurringDepositID` to deposit created and updated event examples
- Updated expiration field examples to use RFC 3339 / ISO-8601 timestamp formatting
- Added `statusPhase` and `statusPhaseComment` to the `deposits.updated` example payload

**Funding schema documentation**
- Updated `recurringFrequency` description to clarify it is only available for ACH deposits
- Updated withdrawal `amount` description to clarify positive and negative value handling

**Cash presentation updates**
- Reordered cash-related attributes so `cashAvailableForTradeNonMarginable` appears before `cashAvailableForWithdrawal`

**Shared retirement enum updates**
- Expanded shared IRA enum support for additional retirement classifications, including `UNKNOWN` and other new contribution and distribution types

```

<br />