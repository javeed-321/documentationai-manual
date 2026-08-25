---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get transactions for a specific Account

Retrieves the last 6 months of transactions (successful payments in & out) of an account, specified by a unique account reference.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Modulr API",
    "description": "Modulr API",
    "license": {
      "name": "© Modulr Finance",
      "url": "https://www.modulrfinance.com"
    },
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api-sandbox.modulrfinance.com/api-sandbox-token"
    }
  ],
  "security": [
    {
      "modulo_security": []
    }
  ],
  "tags": [
    {
      "name": "Transactions",
      "description": "Operations on Transactions"
    }
  ],
  "paths": {
    "/accounts/{accountId}/transactions": {
      "get": {
        "tags": [
          "Transactions"
        ],
        "summary": "Get transactions for a specific Account",
        "description": "Retrieves the last 6 months of transactions (successful payments in & out) of an account, specified by a unique account reference.",
        "operationId": "getTransactionsByAccount",
        "parameters": [
          {
            "name": "accountId",
            "in": "path",
            "description": "ID of account to fetch transactions for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "q",
            "in": "query",
            "description": "Partial description text to search for",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Partial description text to search for"
            }
          },
          {
            "name": "minAmount",
            "in": "query",
            "description": "Transactions with amount equal or more than this amount",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "description": "Transactions with amount equal or more than this amount",
              "minimum": 0
            }
          },
          {
            "name": "maxAmount",
            "in": "query",
            "description": "Transactions with amount equal or less than this amount",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "description": "Transactions with amount equal or less than this amount",
              "minimum": 0.01
            }
          },
          {
            "name": "fromPostedDate",
            "in": "query",
            "description": "Transactions with posted date equal or after to this date",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Transactions with posted date equal or after to this date"
            }
          },
          {
            "name": "toPostedDate",
            "in": "query",
            "description": "Transactions with posted date equal or before to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Transactions with posted date equal or before to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000"
            }
          },
          {
            "name": "type",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "Transaction types",
              "items": {
                "type": "string",
                "description": "Transaction type",
                "enum": [
                  "PI_BACS",
                  "PI_BACS_CONTRA",
                  "PI_FAST",
                  "PI_CHAPS",
                  "PI_DD",
                  "PI_SECT",
                  "PI_SEPA_INST",
                  "PI_REV",
                  "PI_FAST_REV",
                  "PO_FAST",
                  "PO_CHAPS",
                  "PO_DD",
                  "PO_SECT",
                  "PO_SEPA_INST",
                  "PO_REV",
                  "INT_INTERC",
                  "INT_INTRAC",
                  "ADHOC",
                  "FE_TXN",
                  "FE_ACMNT",
                  "FE_ACOPN",
                  "FE_REV",
                  "PO_MASTER",
                  "PI_MASTER",
                  "PO_REV_MASTER",
                  "PO_VISA",
                  "PI_VISA",
                  "PI_SWIFT",
                  "PO_SWIFT",
                  "PI_DD_PEND",
                  "PO_DD_PEND",
                  "DDIC_RETURN",
                  "ARUDD_RETURN",
                  "PO_FX",
                  "PI_FX",
                  "PI_FXFEE"
                ]
              }
            }
          },
          {
            "name": "credit",
            "in": "query",
            "description": "If true only credit transactions will be returned, if false, only debit transactions will be returned",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "description": "If true only credit transactions will be returned, if false, only debit transactions will be returned"
            }
          },
          {
            "name": "sourceId",
            "in": "query",
            "description": "Transactions with this sourceId",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Transactions with this sourceId"
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Size of Page to fetch",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Size of Page to fetch",
              "maximum": 500
            }
          },
          {
            "name": "showAvailableBalance",
            "in": "query",
            "description": "Show available balance",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "description": "Show available balance"
            }
          },
          {
            "name": "fromTransactionDate",
            "in": "query",
            "description": "Transactions with transaction date equal or after to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Transactions with transaction date equal or after to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000"
            }
          },
          {
            "name": "toTransactionDate",
            "in": "query",
            "description": "Transactions with transaction date equal or before to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Transactions with transaction date equal or before to this date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000"
            }
          },
          {
            "name": "page",
            "in": "query",
            "description": "Page to fetch (0 indexed)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Page to fetch (0 indexed)"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/account.TransactionPageResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/account.MessageResponse"
                  }
                }
              }
            }
          }
        },
        "security": [
          {
            "HMAC": []
          },
          {
            "TOKEN": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "account.IdentifierResponse": {
        "type": "object",
        "description": "Account Identifier",
        "properties": {
          "type": {
            "type": "string"
          },
          "accountNumber": {
            "type": "string",
            "description": "Bank account Sort Code",
            "example": "12345678"
          },
          "accountType": {
            "type": "string",
            "description": "Bank account type like PERSONAL/BUSINESS",
            "enum": [
              "PERSONAL",
              "BUSINESS"
            ]
          },
          "sortCode": {
            "type": "string",
            "description": "Bank account Sort Code",
            "example": "000000"
          },
          "iban": {
            "type": "string",
            "example": "GB20MODR04001401100000"
          },
          "bic": {
            "type": "string",
            "example": "MODRGB21"
          },
          "currency": {
            "type": "string",
            "example": "GBP"
          },
          "countrySpecificDetails": {
            "$ref": "#/components/schemas/account.IdentifierCountrySpecificDetailsResponse",
            "example": {
              "branchCode": "123456789"
            }
          },
          "productId": {
            "type": "string",
            "example": "O2100001"
          }
        }
      },
      "account.MessageResponse": {
        "type": "object",
        "properties": {
          "field": {
            "type": "string"
          },
          "code": {
            "type": "string",
            "enum": [
              "GENERAL",
              "BUSINESSRULE",
              "MFASTATUS",
              "MFAERROR",
              "MFATIMEOUT",
              "MFADEVICEMM",
              "MFAMESSAGEINVALID",
              "NOTFOUND",
              "DUPLICATE",
              "INVALID",
              "CONNECTION",
              "RETRY",
              "RATELIMIT",
              "PERMISSION",
              "NOTACCEPTABLE",
              "MFAVERIFICATION",
              "TOKENEXPIRED"
            ]
          },
          "errorCode": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "sourceService": {
            "type": "string"
          }
        }
      },
      "account.IdentifierCountrySpecificDetailsResponse": {
        "type": "object",
        "properties": {
          "bankName": {
            "type": "string",
            "description": "The name of the destination bank.",
            "example": "Apple Bank"
          },
          "bankAddress": {
            "type": "string",
            "description": "The address of the destination bank.",
            "example": "2100 Broadway"
          },
          "bankCity": {
            "type": "string",
            "description": "The city in which the destination bank resides.",
            "example": "New York City"
          },
          "bankBranchName": {
            "type": "string",
            "description": "The name of the destination bank's branch.",
            "example": "New York"
          },
          "bankBranchCode": {
            "type": "string",
            "description": "The code of the destination bank's branch.",
            "example": "44-04"
          },
          "bankCode": {
            "type": "string",
            "description": "The code identifying the target bank on its respective national network. This is not the BIC/SWIFT code. This is known as the 'ABA code' in the U.S., 'ISFC' in India, 'routing number' in Canada, and so on."
          },
          "chineseId": {
            "type": "string",
            "description": "The 18 digit identification code of the beneficiary. Applies to Chinese beneficiaries only.",
            "example": "01101201901018889"
          },
          "province": {
            "type": "string",
            "description": "The province in which the beneficiary resides. Applies only to beneficiaries residing in China.",
            "example": "Zhejiang"
          },
          "business": {
            "type": "boolean",
            "description": "The type of the beneficiary. 'true' for businesses, 'false' otherwise.",
            "example": true
          },
          "bankCodeType": {
            "type": "string",
            "description": "The code type identifying the target bank on its respective national network.\nThis is known as the 'ABA code' in the U.S., 'ISFC' in India, 'routing number' in Canada, and so on.",
            "enum": [
              "ABA",
              "CHIPS"
            ],
            "example": "ABA"
          },
          "bankCountry": {
            "type": "string",
            "description": "The country in which the destination bank resides.",
            "enum": [
              "AT",
              "BE",
              "BG",
              "CY",
              "CZ",
              "DK",
              "EE",
              "FI",
              "FR",
              "DE",
              "GR",
              "HR",
              "HU",
              "IS",
              "IE",
              "IT",
              "LV",
              "LI",
              "LT",
              "LU",
              "MT",
              "NL",
              "NO",
              "PL",
              "PT",
              "RO",
              "SK",
              "SI",
              "ES",
              "SE",
              "GB",
              "MQ",
              "YT",
              "GP",
              "GF",
              "RE",
              "MF",
              "GI",
              "GG",
              "IM",
              "JE",
              "MC",
              "CH",
              "AD",
              "SM",
              "VA",
              "AX",
              "PM",
              "BL",
              "AL",
              "MD",
              "ME",
              "MK",
              "RS",
              "AF",
              "DZ",
              "AS",
              "AO",
              "AI",
              "AQ",
              "AG",
              "AR",
              "AM",
              "AW",
              "AU",
              "AZ",
              "BS",
              "BH",
              "BD",
              "BB",
              "BY",
              "BZ",
              "BJ",
              "BM",
              "BT",
              "BO",
              "BQ",
              "BA",
              "BW",
              "BV",
              "BR",
              "IO",
              "VG",
              "BN",
              "BF",
              "BI",
              "KH",
              "CM",
              "CA",
              "CV",
              "KY",
              "CF",
              "TD",
              "CL",
              "CN",
              "CX",
              "CC",
              "CO",
              "KM",
              "CK",
              "CR",
              "CU",
              "CW",
              "CD",
              "DJ",
              "DM",
              "DO",
              "TL",
              "EC",
              "EG",
              "SV",
              "GQ",
              "ER",
              "SZ",
              "ET",
              "FK",
              "FO",
              "FJ",
              "PF",
              "TF",
              "GA",
              "GM",
              "GE",
              "GH",
              "GL",
              "GD",
              "GU",
              "GT",
              "GN",
              "GW",
              "GY",
              "HT",
              "HM",
              "HN",
              "HK",
              "IN",
              "ID",
              "IR",
              "IQ",
              "IL",
              "CI",
              "JM",
              "JP",
              "JO",
              "KZ",
              "KE",
              "KI",
              "XK",
              "KW",
              "KG",
              "LA",
              "LB",
              "LS",
              "LR",
              "LY",
              "MO",
              "MG",
              "MW",
              "MY",
              "MV",
              "ML",
              "MH",
              "MR",
              "MU",
              "MX",
              "FM",
              "MN",
              "MS",
              "MA",
              "MZ",
              "MM",
              "NA",
              "NR",
              "NP",
              "AN",
              "NC",
              "NZ",
              "NI",
              "NE",
              "NG",
              "NU",
              "NF",
              "KP",
              "MP",
              "OM",
              "PK",
              "PW",
              "PS",
              "PA",
              "PG",
              "PY",
              "PE",
              "PH",
              "PN",
              "PR",
              "QA",
              "CG",
              "RU",
              "RW",
              "SH",
              "KN",
              "LC",
              "VC",
              "WS",
              "ST",
              "SA",
              "SN",
              "SC",
              "SL",
              "SG",
              "SX",
              "SB",
              "SO",
              "ZA",
              "KR",
              "GS",
              "SS",
              "LK",
              "SD",
              "SR",
              "SY",
              "SJ",
              "TW",
              "TJ",
              "TZ",
              "TH",
              "TG",
              "TK",
              "TO",
              "TT",
              "TN",
              "TR",
              "TM",
              "TC",
              "TV",
              "UG",
              "UA",
              "AE",
              "UM",
              "US",
              "UY",
              "UZ",
              "VU",
              "VE",
              "VN",
              "VI",
              "WF",
              "EH",
              "YE",
              "ZM",
              "ZW"
            ],
            "example": "US"
          },
          "abaRoutingNumber": {
            "type": "string",
            "description": "The 9 digit identification code of the beneficiary. Applies to US beneficiaries only.",
            "example": "123456789"
          }
        }
      },
      "account.AccountResponse": {
        "type": "object",
        "description": "Account",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for the account",
            "example": "A0000001"
          },
          "name": {
            "type": "string",
            "description": "Name for the account"
          },
          "balance": {
            "type": "string",
            "description": "Balance of the account in format 'NN.NN'",
            "example": "10000.00"
          },
          "availableBalance": {
            "type": "string",
            "description": "The current available balance of the Account. Calculated by subtracting any pending payments from the current balance",
            "example": "10000.00"
          },
          "currency": {
            "type": "string",
            "description": "Currency of the account in ISO 4217 format",
            "example": "GBP"
          },
          "status": {
            "type": "string",
            "description": "Status of the account. Accounts must be 'ACTIVE' to make and receive payments. Can be one of ",
            "example": "ACTIVE"
          },
          "identifiers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/account.IdentifierResponse"
            }
          },
          "customerId": {
            "type": "string",
            "description": "Unique id of the Customer",
            "example": "C0000001"
          },
          "customerName": {
            "type": "string",
            "description": "Customer Name"
          },
          "externalReference": {
            "type": "string",
            "description": "Your reference for an account",
            "example": "aReference_00001"
          },
          "accessGroups": {
            "type": "array",
            "description": "Ids of Access Groups this account belongs to",
            "items": {
              "type": "string"
            }
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when the account was created. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "directDebit": {
            "type": "boolean",
            "description": "Direct Debit Enabled"
          },
          "securedFundingLimit": {
            "type": "string",
            "description": "Limit of funds available below a balance of zero"
          }
        }
      },
      "account.TransactionPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/account.TransactionResponse"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Page size"
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total count"
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number, 0 based; i.e first-page = 0, second-page = 1"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total pages"
          },
          "pageStartBalance": {
            "type": "number",
            "description": "The sum of the transactions up to this page.\nThis is only present if there are no filters other than page and size defined",
            "example": "250.30"
          }
        }
      },
      "account.TransactionResponse": {
        "type": "object",
        "description": "Transaction",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for the Transaction",
            "example": "T000000001"
          },
          "amount": {
            "type": "number",
            "description": "Amount of the transaction in Major Currency Units"
          },
          "currency": {
            "type": "string",
            "description": "Currency of the account in ISO 4217 format",
            "example": "GBP"
          },
          "description": {
            "type": "string",
            "description": "Description of the transaction. Contains Payer/ Payee details and reference"
          },
          "transactionDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when the transaction took place. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "postedDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when the transaction was posted to the Modulr system. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "credit": {
            "type": "boolean",
            "description": "Indicates if the transaction was a Credit or a Debit"
          },
          "type": {
            "type": "string",
            "description": "Enumerated type indicating the type of the transaction"
          },
          "sourceId": {
            "type": "string"
          },
          "sourceExternalReference": {
            "type": "string"
          },
          "additionalInfo": {
            "description": "any extra information available on transaction."
          },
          "account": {
            "$ref": "#/components/schemas/account.AccountResponse",
            "description": "Account information"
          }
        }
      }
    },
    "securitySchemes": {
      "modulo_security": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
      },
      "TOKEN": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
      }
    }
  },
  "x-readme": {
    "proxy-enabled": false
  }
}
```