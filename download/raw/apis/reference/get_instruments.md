---
updatedAt: 2026-05-27T16:57:55.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List Instruments

Retrives a list of Instruments.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Core APIs",
    "version": "2026-08-25",
    "contact": {
      "email": "producteng@drivewealth.tech"
    }
  },
  "servers": [
    {
      "url": "https://bo-api.drivewealth.io/back-office",
      "description": "Sandbox (No Real World Financial/Trading Impact)"
    },
    {
      "url": "https://bo-api.drivewealth.net/back-office",
      "description": "Production"
    }
  ],
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "headers": [
      {
        "key": "dw-client-app-key",
        "value": "{{yourAppKey}}"
      }
    ]
  },
  "tags": [
    {
      "name": "Instruments"
    }
  ],
  "paths": {
    "/instruments": {
      "get": {
        "tags": [
          "Instruments"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "status",
            "schema": {
              "type": "string"
            },
            "required": false,
            "example": "ACTIVE",
            "description": "The instrument status; to filter by."
          },
          {
            "in": "query",
            "name": "isOptionsEnabled",
            "schema": {
              "type": "boolean"
            },
            "required": false,
            "example": true,
            "description": "The ability to trade options for this instrument; to filter by."
          }
        ],
        "summary": "List Instruments",
        "description": "Retrives a list of Instruments.",
        "responses": {
          "200": {
            "description": "Retrieving a list of Instruments was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Instruments"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "instrumentSymbol": {
        "type": "string",
        "nullable": true,
        "example": "MS",
        "description": "The ticker symbol of the Instrument. Debt Instruments and Global Mutual Funds do not have symbols and are referred to buy their `instrumentID` or `ISIN`."
      },
      "instrumentISIN": {
        "description": "An `International Securities Identification Number` (ISIN) uniquely identifies a security. Its structure is defined in ISO 6166. ISINs are commonly used when an Instrument does not have a `symbol`, such as Debt Instruments and Global Mutual Funds.",
        "type": "string",
        "minLength": 12,
        "maxLength": 14,
        "example": "US023135BX34"
      },
      "instrumentCUSIP": {
        "description": "CUSIP stands for `Committee on Uniform Securities Identification Procedures`.\nA CUSIP number identifies most financial instruments, including: stocks of all registered U.S. and Canadian companies, commercial paper, and U.S. government and municipal bonds.\nThe CUSIP system facilitates the clearance and settlement process of securities.\nCUSIP numbers consist of nine characters (including letters and numbers) that uniquely identify a company or issuer and the type of financial instrument.\nA similar system is used to identify foreign securities (`CUSIP International Numbering System or CINS`).\nCINS employs the same nine character identifier as CUSIP, but also contains a letter in the first position to signify the issuer's country or geographic region.\n",
        "type": "string",
        "minLength": 9,
        "maxLength": 9,
        "example": "E09876AA7"
      },
      "instrumentType": {
        "type": "string",
        "example": "EQUITY",
        "description": "The classification of the instrument.",
        "enum": [
          "EQUITY",
          "ALTERNATIVE_ASSET",
          "MUTUAL_FUND",
          "DEBT",
          "OPTION",
          "CRYPTO"
        ]
      },
      "instrumentStatus": {
        "type": "string",
        "example": "ACTIVE",
        "description": "The current status of the instrument.",
        "enum": [
          "ACTIVE",
          "INACTIVE",
          "CLOSE_ONLY",
          "HALTED"
        ]
      },
      "instrumentID": {
        "type": "string",
        "format": "uuid",
        "example": "3fb1e8a9-f7d5-4d90-95e2-43e7326b5636",
        "description": "A unique ID created by DriveWealth to identify a specific instrument."
      },
      "country": {
        "type": "string",
        "example": "US",
        "description": "The ISO standard country alpha-2 code."
      },
      "Instruments": {
        "type": "array",
        "items": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/InstrumentInList"
            },
            {
              "$ref": "#/components/schemas/DebtInstrumentDetails"
            }
          ]
        }
      },
      "InstrumentInList": {
        "type": "object",
        "required": [
          "id",
          "status"
        ],
        "properties": {
          "id": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "symbol": {
            "type": "string",
            "example": "MS",
            "description": "The ticker symbol of the associated Instrument."
          },
          "name": {
            "type": "string",
            "example": "Morgan Stanley",
            "description": "The official name of the company associated to the Instrument."
          },
          "enableExtendedHoursNotionalStatus": {
            "type": "string",
            "example": "INACTIVE",
            "description": "The Instrument's eligibility for extended hours notional trading. This will default to INACTIVE"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "type": {
            "deprecated": true,
            "type": "string",
            "example": "EQUITY",
            "description": "The classification of the Instrument.",
            "enum": [
              "EQUITY",
              "ETF",
              "ETN",
              "ADR",
              "ALTERNATIVE_ASSET",
              "MUTUAL_FUND",
              "INTEREST_RATE"
            ]
          },
          "status": {
            "type": "string",
            "example": "ACTIVE",
            "description": "The current status of the instrument.",
            "enum": [
              "ACTIVE",
              "INACTIVE",
              "CLOSE_ONLY",
              "HALTED"
            ]
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "isOptionsEnabled": {
            "type": "boolean",
            "example": true,
            "default": false,
            "description": "The ability to trade options for this equity instrument."
          },
          "payFrequency": {
            "$ref": "#/components/schemas/PayFrequency"
          },
          "couponRate": {
            "$ref": "#/components/schemas/CouponRate"
          },
          "maturityDate": {
            "$ref": "#/components/schemas/MaturityDate"
          },
          "spRating": {
            "$ref": "#/components/schemas/SpRating"
          },
          "bondType": {
            "$ref": "#/components/schemas/BondType"
          },
          "domicileCountry": {
            "$ref": "#/components/schemas/country"
          }
        }
      },
      "InstrumentBase": {
        "type": "object",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "name": {
            "type": "string",
            "example": "Morgan Stanley",
            "description": "A friendly name of the Instrument, like the Company name for an equity"
          },
          "orderSizeMax": {
            "type": "number",
            "example": 20000,
            "description": "The maximum share amount for any order of this Instrument."
          },
          "orderSizeMin": {
            "type": "number",
            "example": 0.1,
            "description": "The minimum share amount for any order of this Instrument."
          },
          "orderSizeStep": {
            "type": "number",
            "example": 0.01,
            "description": "Increment amount on order of this Instrument."
          },
          "id": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "exchange": {
            "type": "string",
            "example": "NYQ",
            "description": "The stock exchange the instrument is listed on."
          },
          "status": {
            "$ref": "#/components/schemas/instrumentStatus"
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "CUSIP": {
            "$ref": "#/components/schemas/instrumentCUSIP"
          },
          "settlementDays": {
            "type": "integer",
            "description": "Number of days for the instrument to settle",
            "example": 1
          }
        }
      },
      "DebtInstrumentDetails": {
        "type": "object",
        "allOf": [
          {
            "$ref": "#/components/schemas/InstrumentBase"
          }
        ],
        "properties": {
          "debtData": {
            "$ref": "#/components/schemas/DebtReferenceData"
          }
        }
      },
      "PayFrequency": {
        "description": "The anticipated frequency of scheduled interest payments under the Bonds.",
        "type": "string",
        "enum": [
          "ANNUALLY",
          "SEMI_ANNUALLY",
          "QUARTERLY",
          "MONTHLY",
          "WEEKLY",
          "DAILY",
          "EVERY_X_DAYS",
          "EVERY_X_MONTHS",
          "EVERY_X_WEEKS",
          "EVERY_X_YEARS",
          "AT_MATURITY",
          "SINGLE_DATE",
          "SINGLE_INTEREST_PAYMENT",
          "FLEXIBLE",
          "NOT_APPLICABLE"
        ],
        "example": "SEMI_ANNUALLY",
        "readOnly": true
      },
      "CouponRate": {
        "description": "The annual rate of interest currently applicable to the instrument.",
        "type": "number",
        "format": "double",
        "example": 0.05,
        "readOnly": true
      },
      "MaturityDate": {
        "description": "The date on which the principal amount of the debt instrument becomes due.",
        "type": "string",
        "format": "date",
        "example": "2022-05-10",
        "readOnly": true
      },
      "SpRating": {
        "description": "The long term S&P Rating of the issuer.",
        "type": "string",
        "example": "AAA",
        "readOnly": true
      },
      "SpRatingDate": {
        "description": "The date on which the S&P Rating was last updated.",
        "type": "string",
        "format": "date",
        "example": "2018-05-10",
        "readOnly": true
      },
      "BondType": {
        "description": "The type of bond.",
        "type": "string",
        "enum": [
          "OTHER",
          "CORPORATE_BOND",
          "GOVERNMENT/AGENCY_BOND",
          "US_MUNICIPAL_BOND",
          "COLLATERALIZED_MORTGAGE_OBLIGATION/ASSET-BACKED_SECURITY",
          "MORTGAGE-BACKED_SECURITY",
          "MONEY_MARKET",
          "COMMON_EQUITY",
          "PREFERRED_EQUITY",
          "RIGHT",
          "WARRANT",
          "OPTION",
          "FUTURE",
          "SWAP",
          "CURRENCY",
          "COMMODITY",
          "INDEX",
          "MUTUAL_FUND/UNIT_INVESTMENT_TRUST",
          "MONEY_MARKET_FUND",
          "EXCHANGE_TRADED_FUND",
          "HYBRID",
          "NON-US_MORTGAGE-BACKED_SECURITY",
          "COMPOSITE_UNIT",
          "DEBT/EQUITY_HYBRID",
          "STRATEGY",
          "OVER-THE-COUNTER_(OTC)",
          "BANK_LOAN",
          "MBS_GENERIC"
        ],
        "example": "CORPORATE_BOND",
        "readOnly": true
      },
      "DebtReferenceData": {
        "type": "object",
        "properties": {
          "payFrequency": {
            "$ref": "#/components/schemas/PayFrequency"
          },
          "couponRate": {
            "$ref": "#/components/schemas/CouponRate"
          },
          "maturityDate": {
            "$ref": "#/components/schemas/MaturityDate"
          },
          "spRating": {
            "$ref": "#/components/schemas/SpRating"
          },
          "spRatingDate": {
            "$ref": "#/components/schemas/SpRatingDate"
          },
          "minimumInvestmentAmount": {
            "description": "The minimum initial investment in the security.",
            "type": "integer",
            "format": "int64",
            "example": 1000,
            "readOnly": true
          },
          "incrementalInvestmentAmount": {
            "description": "The minimum additional investment in the security.",
            "type": "integer",
            "format": "int64",
            "example": 1000,
            "readOnly": true
          },
          "issueDate": {
            "description": "The date on which the instrument was first made available to the market.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          },
          "datedDate": {
            "description": "The date of a Bond Issue from which Interest begins to accrue.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          },
          "issueAmount": {
            "description": "The total value of the security at issue.",
            "type": "number",
            "format": "double",
            "example": 1000000,
            "readOnly": true
          },
          "issuePricePercent": {
            "description": "The nominal value associated with a financial instrument at the time of issuance.",
            "type": "number",
            "format": "double",
            "example": 100,
            "readOnly": true
          },
          "accruedInterest": {
            "description": "The amount of interest that has accumulated since the last coupon payment.",
            "type": "number",
            "format": "double",
            "example": 0.05,
            "readOnly": true
          },
          "debtType": {
            "description": "The code for the type fixed income instrument.",
            "type": "integer",
            "readOnly": true
          },
          "bondType": {
            "$ref": "#/components/schemas/BondType"
          },
          "debtTypeDescription": {
            "type": "string",
            "description": "The description for the type fixed income instrument.",
            "enum": [
              "NONE",
              "BANK_LOAN",
              "ASSET-BACKED_SECURITY_(ABS)",
              "BOND",
              "CERTIFICATE_OF_DEPOSIT_(CD)",
              "DEMAND_NOTE",
              "EMPLOYEE_STOCK_OWNERSHIP_PLAN_(ESOP)",
              "FHLMC_REFERENCE_NOTES",
              "GUARANTEED_INVESTMENT_CERTIFICATE_(GIC)",
              "SCHULDSCHEIN",
              "INCOME",
              "MORTGAGE-BACKED_SECURITY_(MBS)",
              "BANKER'S_ACCEPTANCE",
              "COLLATERALISED_LOAN_OBLIGATION_(CLO)",
              "COLLATERALIZED_MORTGAGE_OBLIGATION_(CMO)",
              "NOTE",
              "COLLATERALISED_BOND_OBLIGATION_(CBO)",
              "COMMERCIAL_PAPER",
              "PFANDBRIEF",
              "PROMISSORY_NOTES",
              "STRUCTURED_ASSETS",
              "TRUST_CERTIFICATE",
              "PARTICIPATION_UNIT",
              "SAVINGS_BOND",
              "PASS_THRU_CERTIFICATES",
              "UNKNOWN",
              "STRIP",
              "ANNUITY",
              "BILL",
              "CERTIFICATE",
              "DEPOSIT_NOTE",
              "EQUIPMENT_TRUST_CERTIFICATE",
              "FNMA_BENCHMARK_ISSUES",
              "MORTGAGE/UK_DEBENTURE",
              "SCHATZANWEISUNGEN",
              "DISCOUNT_NOTE",
              "PERMANENT_INTEREST_BEARING_SECURITY",
              "OTHER_MONEY_MARKETS",
              "LOAN_NOTE",
              "MERCHANT_MARINE",
              "MORTGAGE_NOTE",
              "COLLATERALIZED_DEBT_OBLIGATION_(CDO)",
              "PRIVATE_PLACEMENT",
              "EXCHANGE_TRADED_NOTE",
              "PREMIUM_BOND",
              "SECURITY",
              "UNIT",
              "SAVINGS_NOTES",
              "PARTICIPATION_CERTIFICATES",
              "DISCOUNT_DEBENTURE",
              "DEBENTURE_-_UNSECURED",
              "EXCHANGE_TRADED_COMMODITY",
              "ASSET-BACKED_COMMERCIAL_PAPER",
              "SUKUK",
              "DEBENTURE_-_SECURED",
              "LETTER_OF_CREDIT",
              "GLOBAL_DEPOSITORY_NOTE"
            ],
            "example": "BOND",
            "readOnly": true
          },
          "sector": {
            "type": "string",
            "example": "FINANCE_AND_INSURANCE",
            "description": "The categorization of the sector pertaining to the Instrument.",
            "enum": [
              "AGRICULTURE_FORESTRY_FISHING_AND_HUNTING",
              "MINING_QUARRYING_AND_OIL_AND_GAS_EXTRACTION",
              "UTILITIES",
              "CONSTRUCTION",
              "MANUFACTURING",
              "WHOLESALE_TRADE",
              "RETAIL_TRADE",
              "TRANSPORTATION_AND_WAREHOUSING",
              "INFORMATION",
              "FINANCE_AND_INSURANCE",
              "REAL_ESTATE_AND_RENTAL_AND_LEASING",
              "PROFESSIONAL_SCIENTIFIC_AND_TECHNICAL_SERVICES",
              "MANAGEMENT_OF_COMPANIES_AND_ENTERPRISES",
              "ADMINISTRATIVE_AND_SUPPORT_AND_WASTE_MANAGEMENT_AND_REMEDIATION_SERVICES",
              "EDUCATIONAL_SERVICES",
              "HEALTH_CARE_AND_SOCIAL_ASSISTANCE",
              "ARTS_ENTERTAINMENT_AND_RECREATION",
              "ACCOMMODATION_AND_FOOD_SERVICES",
              "OTHER_SERVICES_EXCEPT_PUBLIC_ADMINISTRATION",
              "PUBLIC_ADMINISTRATION"
            ]
          },
          "duration": {
            "description": "The duration of the bond.",
            "type": "number",
            "format": "double",
            "example": "10.5",
            "readOnly": true,
            "nullable": true
          },
          "nextCallDate": {
            "description": "The next call date of the bond.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true,
            "nullable": true
          },
          "debtRankType": {
            "description": "The debt rank type of the bond.",
            "type": "string",
            "example": "SENIOR",
            "readOnly": true,
            "enum": [
              "UNKNOWN",
              "SECOND_MORTGAGE",
              "FIRST_MORTGAGE ",
              "JUNIOR",
              "MEZZANINE",
              "SENIOR_SUBORDINATED",
              "SUBORDINATED",
              "THIRD_MORTGAGE",
              "UNSUBORDINATED",
              "JUNIOR_SUBORDINATED",
              "SENIOR",
              "NOT_APPLICABLE",
              "TIER_I",
              "LOWER_TIER_II",
              "UPPER_TIER_II",
              "TIER_III",
              "SENIOR_SECURED",
              "ALTERNATIVE_ADDITIONAL_TIER_I",
              "SENIOR_NON_PREFERRED"
            ]
          },
          "spRatingType": {
            "type": "string",
            "example": "INVESTMENT_GRADE",
            "description": "The spRating type of the bond.",
            "enum": [
              "INVESTMENT_GRADE",
              "HIGH_YIELD"
            ]
          },
          "coupon": {
            "$ref": "#/components/schemas/Coupon"
          },
          "issuer": {
            "$ref": "#/components/schemas/Issuer"
          },
          "indicators": {
            "$ref": "#/components/schemas/Indicators"
          },
          "denominationAmounts": {
            "$ref": "#/components/schemas/DenominationAmounts"
          }
        }
      },
      "Coupon": {
        "description": "A coupon or coupon payment is the annual interest rate paid on a bond, expressed as a percentage of the face value and paid from issue date until maturity.",
        "type": "object",
        "properties": {
          "couponType": {
            "description": "The method by which the coupon rate of the instrument is determined.",
            "type": "string",
            "enum": [
              "UNKNOWN",
              "SHORT_TERM_DISCOUNT",
              "FIXED_RATE_-_UNCONFIRMED",
              "ADJUSTABLE_RATE",
              "ZERO_COUPON",
              "FLOATING_RATE",
              "INDEX_LINKED",
              "STEPPED_COUPON",
              "FIXED_RATE",
              "STRIPPED_CONVERTIBLE",
              "DEFERRED_INTEREST",
              "FLOATING_RATE_@_FLOOR",
              "STRIPPED_TAX_CREDIT",
              "INVERSE_FLOATING",
              "STRIPPED_COUPON_PRINCIPAL",
              "LINKED_INVERSE_FLOATER",
              "FLEXIBLE_RATE",
              "ORIGINAL_ISSUE_DISCOUNT",
              "STRIPPED_PRINCIPAL",
              "RESERVE_CUSIP",
              "VARIABLE_RATE",
              "STRIPPED_COUPON",
              "FLOATING_AUCTION_RATE",
              "TAX_CREDIT",
              "TAX_CREDIT_OID",
              "STRIPPED_COUPON_PAYMENT",
              "STEPPED_UP_STEPPED_DOWN",
              "CREDIT_SENSITIVE",
              "PAY_IN_KIND",
              "RANGE",
              "DIGITAL",
              "RESET"
            ],
            "example": "FIXED_RATE",
            "readOnly": true
          },
          "currentRateDate": {
            "description": "The annual rate of interest currently applicable to the instrument.",
            "type": "string",
            "format": "date",
            "minLength": 0,
            "maxLength": 10,
            "example": "2018-05-10",
            "readOnly": true
          },
          "dayCount": {
            "description": "The method of calculating interest accrual associated with the instrument.",
            "type": "string",
            "enum": [
              "UNKNOWN_INTEREST_CALCULATION_METHOD",
              "ACTUAL/ACTUAL",
              "ACTUAL/360",
              "30/360",
              "30_DAYS_PER_MONTH_/_ACTUAL",
              "ACTUAL/365_(FIXED)",
              "CHANGEABLE",
              "ACTUAL/365_(366_LEAP_YEAR_-_ISDA)",
              "30/360_(COMPOUNDED_INTEREST)",
              "30/365",
              "FUTURE_DATA_-_NOT_AVAILABLE",
              "HISTORICAL_DATA_-_NOT_AVAILABLE",
              "30/360_(ICMA)",
              "ACTUAL/365_(366_LEAP_YEAR)",
              "ACTUAL/364",
              "BUS/252",
              "365/365",
              "ACTUAL/ACTUAL_(ICMA)",
              "28/360",
              "30/360_US",
              "30/360_US_(NASD)",
              "30/360_BMA",
              "30/360_(ISDA)",
              "30/360_IT",
              "30/360_SIA",
              "30E/360",
              "30E/360_(ISDA)",
              "30E+/360",
              "NL/365_(NO_LEAP_YEAR)",
              "7/360",
              "30/360_WITH_GROSS_UP",
              "NOT_APPLICABLE"
            ],
            "example": "30/360",
            "readOnly": true
          },
          "benchmark": {
            "description": "The identifier the index against which the interest rate for an Index Linked Bond is reset.",
            "type": "string",
            "example": "US CPI",
            "readOnly": true
          },
          "benchmarkFormula": {
            "description": "The multiple in the floating rate formula that is applied to the benchmark in order to calculate the reset rate on a floating rate instrument.",
            "type": "string",
            "example": "1.5",
            "readOnly": true
          },
          "nextResetDate": {
            "description": "The date of the next interest rate reset of the instrument",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          },
          "minimumRate": {
            "description": "The minimum interest rate that an instrument will pay.",
            "type": "number",
            "format": "double",
            "example": 0.05,
            "readOnly": true
          },
          "maximumRate": {
            "description": "The maximum interest rate that an instrument will pay.",
            "type": "number",
            "format": "double",
            "example": 0.05,
            "readOnly": true
          },
          "firstCouponDate": {
            "description": "The date on which the first payment of interest is made.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          },
          "nextCouponDate": {
            "description": "The next date on which a payment of interest will be made.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          },
          "finalCouponDate": {
            "description": "The date on which the final interest payment is scheduled to be made to owners of the security.",
            "type": "string",
            "format": "date",
            "example": "2018-05-10",
            "readOnly": true
          }
        }
      },
      "Issuer": {
        "description": "The entity name (in the XML/Web Service) or organization_id (in the Database) of the insurer who has been contracted to provide payments to bondholders in the event of a default by the issuer. In the Database, the entity name can be looked up by using the organization_id in conjunction with the Organization_Master.primary_name field'",
        "type": "object",
        "properties": {
          "primaryName": {
            "description": "A field containing the root symbol assigned by an exchange to the derivative product.",
            "type": "string",
            "example": "Coca Cola Corp",
            "readOnly": true
          },
          "country": {
            "$ref": "#/components/schemas/country"
          },
          "domicileCountry": {
            "$ref": "#/components/schemas/country"
          }
        }
      },
      "Indicators": {
        "description": "Indicators that provide additional information about the security",
        "example": {
          "callIndicator": false,
          "convertibleIndicator": false,
          "defaultIndicator": false,
          "dtcIndicator": true,
          "oidIndicator": false,
          "putIndicator": false,
          "sinkIndicator": false,
          "tipsIndicator": false,
          "floaterIndicator": false,
          "traceEligible": true,
          "capitalizedIndicator": false,
          "childIndicator": false,
          "defeasanceIndicator": false,
          "equityLinkedNoteIndicator": false,
          "pikIndicator": false,
          "tenderExchangeOfferIndicator": false,
          "warrantsIndicator": false,
          "tradingRestrictionsType": "None"
        },
        "properties": {
          "callIndicator": {
            "description": "Indicates if the security is eligible to be redeemed by the issuer on a call basis",
            "readOnly": true,
            "type": "boolean"
          },
          "convertibleIndicator": {
            "description": "Specifies whether an issue is convertible or exchangeable",
            "readOnly": true,
            "type": "boolean"
          },
          "defaultIndicator": {
            "description": "Specifies whether the security is in default or not",
            "readOnly": true,
            "type": "boolean"
          },
          "dtcIndicator": {
            "description": "Indicates whether the security is acceptable for clearing by the DTCC.",
            "readOnly": true,
            "type": "boolean"
          },
          "oidIndicator": {
            "description": "Specifies whether or not this issue qualifies for Original Issue Discount status",
            "readOnly": true,
            "type": "boolean"
          },
          "putIndicator": {
            "description": "Indicates whether the security carries provisions that allow for redemption at the request of owners of the security",
            "readOnly": true,
            "type": "boolean"
          },
          "sinkIndicator": {
            "description": "Indicates whether the security carries a sinking fund as part of its terms and conditions",
            "readOnly": true,
            "type": "boolean"
          },
          "tipsIndicator": {
            "description": "Indicates whether the security is a Treasury Inflation Protected Security",
            "readOnly": true,
            "type": "boolean"
          },
          "traceEligible": {
            "description": "Indicates whether the security is considered TRACE eligible for price reporting",
            "readOnly": true,
            "type": "boolean"
          },
          "capitalizedIndicator": {
            "description": "Specifies whether a bond issuer has set aside some of the proceeds from a bond sale to cover a certain number of interest payments",
            "readOnly": true,
            "type": "boolean"
          },
          "childIndicator": {
            "description": "Indicates whether the security is created as the result of a corporate action or other event (the child instrument) from a previously issued instrument (the parent)",
            "readOnly": true,
            "type": "boolean"
          },
          "defeasanceIndicator": {
            "description": "Indicates whether the security contains a provision that voids a bond or loan when the borrower sets aside cash or bonds sufficient enough to service the borrower's debt (a process called defeasance)",
            "readOnly": true,
            "type": "boolean"
          },
          "equityLinkedNoteIndicator": {
            "description": "Indicates whether the security is an Equity Linked Note",
            "readOnly": true,
            "type": "boolean"
          },
          "pikIndicator": {
            "description": "Indicates whether the security carries provisions to make Payment In Kind (PIK) to owners of the security",
            "readOnly": true,
            "type": "boolean"
          },
          "tenderExchangeOfferIndicator": {
            "description": "Indicates whether the security has an associated exchange or tender offer",
            "readOnly": true,
            "type": "boolean"
          },
          "warrantsIndicator": {
            "description": "Indicates whether there is a warrant associated with the particular security",
            "readOnly": true,
            "type": "boolean"
          },
          "floaterIndicator": {
            "description": "Indicates whether the security has a floating or adjustable rate issue",
            "readOnly": true,
            "type": "boolean"
          },
          "tradingRestrictionsType": {
            "description": "Indicates whether any trading restrictions are in effect for the security",
            "enum": [
              "None",
              "144A",
              "REG_S",
              "PRIVATE_PLACEMENT",
              "ACCREDITED_INVESTORS",
              "REG_D",
              "SEC_ACT_OF_1933"
            ],
            "readOnly": true,
            "type": "string"
          }
        }
      },
      "DenominationAmounts": {
        "description": "A set of amounts that represent denomination amounts for the security",
        "properties": {
          "incrementAmount": {
            "description": "The increment amount for the security.",
            "readOnly": true,
            "type": "number",
            "format": "double"
          },
          "incrementAmountSecondary": {
            "description": "The secondary increment amount for the security.",
            "readOnly": true,
            "type": "number",
            "format": "double"
          },
          "minimumAmount": {
            "description": " The minimum denomination amount for the security.",
            "readOnly": true,
            "type": "number",
            "format": "double"
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  }
}
```