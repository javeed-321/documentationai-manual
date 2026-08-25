---
updatedAt: 2026-07-24T17:25:47.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Automated Options Approval Process

Enrolling an account for options trading is a two-step process: collect and verify all required user data, then submit a request to activate options trading on the account. DriveWealth evaluates each enrollment request against a suitability matrix and returns a decision via the accounts API. This guide is for fully disclosed clients only — contact your Relationship Manager to confirm your client environment is enabled before proceeding.

## User data requirements

The following fields are required for options enrollment. Several are collected during standard account opening — the fields marked as options-specific are additional requirements. All captured user data must be presented to the investor for verification before enrollment proceeds. Any discrepancies must be corrected by the user prior to submission.

Refer to [Create User](https://developer.drivewealth.com/apis/reference/post_users) for expected values for each field.

| Category                                                                                | Fields                                                                                                                                                                                                          |
| :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic personal info                                                                     | Name, tax ID, citizenship, address, date of birth, photo ID (if required)                                                                                                                                       |
| Personal Info required for Options enrollment                                           | Marital status, employment status, employer company (if employed), dependents                                                                                                                                   |
| Investor profile                                                                        | Investment experience, annual income, liquid net worth, total net worth, risk tolerance, investment objectives                                                                                                  |
| Investment experience per asset class (equity, options, fixed income, commodity, other) | Knowledge level, years of experience, average trade size, trades per year, transaction type (required for equities and options only), decline to answer (available for fixed income, commodity, and other only) |
| Disclosures                                                                             | Options Agreement ODD link (Note: specific levels may require additional disclosures)                                                                                                                           |

```shell
curl --request POST \
     --url https: //bo-api.drivewealth.io/back-office/users \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'content-type: application/json' \
     --header 'dw-client-app-key: {{yourAppKey}}' \
     --data '{
    "username": "test.options.1780346670",
    "password": "passw0rd",
    "userType": "INDIVIDUAL_TRADER",
    "documents": [
        {
            "type": "BASIC_INFO",
            "data": {
                "firstName": "options",
                "lastName": "testuser",
                "country": "USA",
                "phone": "2912341122",
                "emailAddress": "b@b.com",
                "language": "en_US"
            }
        },
        {
            "type": "IDENTIFICATION_INFO",
            "data": {
                "value": "123456788",
                "type": "SSN",
                "citizenship": "USA"
            }
        },
        {
            "type": "PERSONAL_INFO",
            "data": {
                "birthDay": 3,
                "birthMonth": 12,
                "birthYear": 1990,
                "marital": "Single"
            }
        },
        {
            "type": "TAX_INFO",
            "data": {
                "usTaxpayer": true
            }
        },
        {
            "type": "ADDRESS_INFO",
            "data": {
                "street1": "123 Main St",
                "city": "Chatham",
                "province": "NJ",
                "postalCode": "09812"
            }
        },
        {
            "type": "EMPLOYMENT_INFO",
            "data": {
                "status": "Employed",
                "broker": false,
                "company": "MyCo",
                "type": "PROFESSIONAL",
                "city": "Gotham",
                "country": "USA",
                "position": "Police"
            }
        },
        {
            "type": "INVESTOR_PROFILE_INFO",
            "data": {
                "annualIncome": 1000000,
                "networthLiquid": 1000000,
                "networthTotal": 1000000,
                "dependents": 1,
                "riskTolerance": "MODERATE",
                "investmentObjectives": "CAPITAL_PRESERVATION",
                "secondaryInvestmentObjectives": [
                    "GROWTH",
                    "SPECULATION"
                ],
                "investmentExperience": "YRS_10_",
                "equitiesExperience": {
                    "knowledge": "GOOD",
                    "yearsOfExperience": 5,
                    "tradesPerYear": 50,
                    "averageTransactionAmount": 5000,
                    "transactionTypes": [
                        "LONG",
                        "SHORT",
                        "MARGIN"
                    ]
                },
                "optionsExperience": {
                    "knowledge": "GOOD",
                    "yearsOfExperience": 4,
                    "tradesPerYear": 15,
                    "averageTransactionAmount": 100,
                    "transactionTypes": [
                        "COVERED"
                    ]
                },
                "fixedIncomeExperience": {
                    "knowledge": "LIMITED",
                    "yearsOfExperience": 0.5,
                    "tradesPerYear": 10,
                    "averageTransactionAmount": 50
                },
                "commodityExperience": {
                    "knowledge": "NONE",
                    "yearsOfExperience": 0,
                    "tradesPerYear": 0,
                    "averageTransactionAmount": 0
                },
                "otherFinancialExperience": {
                    "declinedToAnswer": true
                }
            }
        },
        {
            "type": "DISCLOSURES",
            "data": {
                "termsOfUse": true,
                "customerAgreement": true,
                "marketDataAgreement": true,
                "rule14b": true,
                "findersFee": true,
                "privacyPolicy": true,
                "optionsAgreement": true,
                "oddLinkAgreement": true,
                "signedBy": "Chris Turkelton"
            }
        }
    ]
}'
```

## Enable options on an account

After all required user data has been collected and verified, submit a request to activate options trading on the account. This can be done when creating a new account via `POST /accounts` or on an existing account via [`PATCH back-office/accounts/{accountID}`](https://developer.drivewealth.com/apis/reference/patch_accounts-accountid). The same `accountFeatures` block applies to both.

Before an account is considered for enrollment, DriveWealth validates that all FINRA-mandated user-level information has been collected. Refer to [FINRA Rule 2360(b)(16)](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2360) for a comprehensive understanding of the regulatory requirements for options enrollment.

> **Note:** US broker-dealer clients are required to submit Registered Options Principal (ROP) details, including the license type, license number, and timestamp of approval. DriveWealth's automated approval process applies to all requests regardless of prior ROP approval.

```bash
curl --request POST \
     --url https://bo-api.drivewealth.io/back-office/accounts \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{ACCESS_TOKEN}}' \
     --header 'content-type: application/json' \
     --header 'dw-client-app-key: {{yourAppKey}}' \
     --data '{
  "userID": "{{userID}}",
  "accountType": "LIVE",
  "accountManagementType": "SELF",
  "tradingType": "CASH",
  "accountFeatures": {
    "options": {
      "enrolled": true,
      "optionsLevel": "LEVEL_2",
      "rop": {
        "name": "{{ropName}}",
        "licenseType": "Series 4",
        "licenseNo": "{{licenseNo}}",
        "approvedWhen": "2026-05-29T23:20:09.015Z"
      }
    }
  }
}'
```

## Enrollment decisions

DriveWealth evaluates each enrollment request against a suitability matrix and returns a decision via the accounts API.

| Decision                         | Description                                                                                                                                                          |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Approved`                       | Enrollment is successful.                                                                                                                                            |
| `Downleveled`                    | The account is approved for a lower options level than requested based on the investor's profile.                                                                    |
| `Rejected (Profile Suitability)` | The investment profile does not meet the requirements for any options level.                                                                                         |
| `Rejected (Cooldown)`            | A previous unsuccessful enrollment attempt is within the 180-day waiting period. The request is automatically rejected until the window has elapsed.                 |
| `Rejected (Missing Data)`        | Required data is missing — for example, dependents or options agreement acknowledgment. This triggers an API error and does not initiate the 180-day waiting period. |

```json
{
  "accountFeatures": {
    "options": {
      "enrolled": false,
      "requestedLevel": "LEVEL_2",
      "reason": "Rejected. Options enrollment is restricted due to cooldown policy",
      "evaluatedAt": "2026-05-29T23:46:16.463Z"
    }
  }
}
```

## Ongoing monitoring

DriveWealth actively monitors user profile updates. In the event an investor adjusts their personal data — for example, if a reported reduction in annual earnings falls below the threshold for their existing options level — the system will take corrective action. In these instances, DriveWealth will either automatically adjust the account to a lower level or entirely remove its options trading access to remain compliant with suitability standards.

Consume `accounts.updated` SQS events to receive notifications.