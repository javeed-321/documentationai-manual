---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get all Rules for a specific Account

The ability to get the details of all rules associated with the specified account using the Account ID as a reference. Can filter by a specific type using the type parameter.

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
      "name": "Rules",
      "description": "Rules"
    }
  ],
  "paths": {
    "/accounts/{id}/rules": {
      "get": {
        "tags": [
          "Rules"
        ],
        "summary": "Get all Rules for a specific Account",
        "description": "The ability to get the details of all rules associated with the specified account using the Account ID as a reference. Can filter by a specific type using the type parameter.",
        "operationId": "getRules",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Account ID of the rules",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
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
              "default": 0
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
              "default": 20
            }
          },
          {
            "name": "rtype",
            "in": "query",
            "description": "Filter to a specific RuleType",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "default": ""
            },
            "example": "SPLIT, SWEEP, FUNDING"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/rule.RulePageResponse"
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
                    "$ref": "#/components/schemas/rule.MessageResponse"
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
      "rule.RulePageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/rule.RuleResponse"
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
            "description": "Current page number, 0-based, i.e first page = 0, second page = 1"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total pages"
          }
        },
        "required": [
          "content",
          "page",
          "size",
          "totalPages",
          "totalSize"
        ]
      },
      "rule.RuleResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for a Rule",
            "example": "R1000001"
          },
          "type": {
            "type": "string",
            "description": "The type of Rule. Can be one of the following {SWEEP, SPLIT, FUNDING}",
            "enum": [
              "SPLIT",
              "SWEEP",
              "FUNDING"
            ]
          },
          "status": {
            "type": "string",
            "enum": [
              "ACTIVE",
              "INACTIVE"
            ]
          },
          "name": {
            "type": "string",
            "description": "Rule's name",
            "example": "My new rule"
          },
          "accountId": {
            "type": "string",
            "description": "The Account which the Rule is created on.",
            "example": "A1000001"
          },
          "accountCurrency": {
            "type": "string",
            "enum": [
              "GBP",
              "EUR",
              "AED",
              "AFN",
              "ALL",
              "AMD",
              "ANG",
              "AOA",
              "ARS",
              "AUD",
              "AWG",
              "AZN",
              "BAM",
              "BBD",
              "BDT",
              "BGN",
              "BHD",
              "BIF",
              "BMD",
              "BND",
              "BOB",
              "BOV",
              "BRL",
              "BSD",
              "BTN",
              "BWP",
              "BYN",
              "BZD",
              "CAD",
              "CDF",
              "CHE",
              "CHF",
              "CHW",
              "CLF",
              "CLP",
              "CNY",
              "COP",
              "COU",
              "CRC",
              "CUC",
              "CUP",
              "CVE",
              "CZK",
              "DJF",
              "DKK",
              "DOP",
              "DZD",
              "EGP",
              "ERN",
              "ETB",
              "FJD",
              "FKP",
              "GEL",
              "GHS",
              "GIP",
              "GMD",
              "GNF",
              "GTQ",
              "GYD",
              "HKD",
              "HNL",
              "HRK",
              "HTG",
              "HUF",
              "IDR",
              "ILS",
              "INR",
              "IQD",
              "IRR",
              "ISK",
              "JMD",
              "JOD",
              "JPY",
              "KES",
              "KGS",
              "KHR",
              "KMF",
              "KPW",
              "KRW",
              "KWD",
              "KYD",
              "KZT",
              "LAK",
              "LBP",
              "LKR",
              "LRD",
              "LSL",
              "LYD",
              "MAD",
              "MDL",
              "MGA",
              "MKD",
              "MMK",
              "MNT",
              "MOP",
              "MRU",
              "MUR",
              "MVR",
              "MWK",
              "MXN",
              "MXV",
              "MYR",
              "MZN",
              "NAD",
              "NGN",
              "NIO",
              "NOK",
              "NPR",
              "NZD",
              "OMR",
              "PAB",
              "PEN",
              "PGK",
              "PHP",
              "PKR",
              "PLN",
              "PYG",
              "QAR",
              "RON",
              "RSD",
              "RUB",
              "RWF",
              "SAR",
              "SBD",
              "SCR",
              "SDG",
              "SEK",
              "SGD",
              "SLE",
              "SLL",
              "SOS",
              "SRD",
              "SSP",
              "STN",
              "SVC",
              "SYP",
              "SZL",
              "SHP",
              "THB",
              "TJS",
              "TMT",
              "TND",
              "TOP",
              "TRY",
              "TTD",
              "TWD",
              "TZS",
              "UAH",
              "UGX",
              "USD",
              "USN",
              "UYI",
              "UYU",
              "UYW",
              "UZS",
              "VES",
              "VND",
              "VUV",
              "WST",
              "XAF",
              "XAG",
              "XAU",
              "XBA",
              "XBB",
              "XBC",
              "XBD",
              "XCD",
              "XDR",
              "XOF",
              "XPD",
              "XPF",
              "XPT",
              "XSU",
              "XTS",
              "XUA",
              "XXX",
              "YER",
              "ZAR",
              "ZMW",
              "ZWL"
            ]
          },
          "masterId": {
            "type": "string",
            "description": "The master rule ID. When a rule is changed, the original is marked as inactive, and a new one created. The master ID enables us to identify those rules which are updates",
            "example": "M1000001"
          },
          "data": {
            "$ref": "#/components/schemas/rule.RuleConfigData"
          }
        },
        "required": [
          "accountCurrency",
          "accountId",
          "data",
          "id",
          "masterId",
          "name",
          "type"
        ]
      },
      "rule.SplitConfig": {
        "type": "object",
        "description": "Configuration for a Split Rule",
        "properties": {
          "destinationId": {
            "type": "string",
            "description": "Id of destination beneficiary. e.g. B1000001."
          },
          "percent": {
            "type": "string",
            "description": "Percentage of payment to be moved to specified destination. e.g. 7.25.",
            "minLength": 1
          }
        },
        "required": [
          "destinationId",
          "percent"
        ]
      },
      "rule.ConditionalSplitConfig": {
        "type": "object",
        "description": "Configuration for a Conditional Split Rule",
        "properties": {
          "destinationId": {
            "type": "string",
            "description": "Id of destination beneficiary. e.g. B1000001."
          },
          "percent": {
            "type": "string",
            "description": "Percentage of payment to be moved to specified destination. e.g. 7.25.",
            "minLength": 1
          },
          "conditionAmount": {
            "type": "number",
            "description": "Amount the conditional split rule should reach before defaulting to the split rule. e.g. 100.",
            "maximum": 2147483647,
            "minimum": 0.01
          },
          "conditionDone": {
            "type": "boolean",
            "description": "Whether the condition amount has been met. e.g. true or false"
          }
        },
        "required": [
          "conditionAmount",
          "destinationId",
          "percent"
        ]
      },
      "rule.RuleConfigData": {
        "type": "object",
        "description": "Configuration fields for all types of rules. To be populated where applicable based on rule type.",
        "properties": {
          "daysToRun": {
            "type": "array",
            "description": "Day(s) of the week the rule is to run. e.g. [\"MONDAY\",\"TUESDAY\",\"WEDNESDAY\",\"THURSDAY\",\"FRIDAY\",\"SATURDAY\",\"SUNDAY\"]. Sweep Rule Only",
            "items": {
              "type": "string",
              "enum": [
                "MONDAY",
                "TUESDAY",
                "WEDNESDAY",
                "THURSDAY",
                "FRIDAY",
                "SATURDAY",
                "SUNDAY"
              ]
            }
          },
          "frequency": {
            "type": "string",
            "description": "Frequency of the rule. Sweep Rule Only",
            "enum": [
              "Daily"
            ]
          },
          "destinationId": {
            "type": "string",
            "description": "Id of destination beneficiary. e.g. B1000001. Sweep Rule Only"
          },
          "balanceToLeave": {
            "type": "number",
            "description": "Balance to be left after the rule has been ran. e.g. 100.00. Sweep Rule Only"
          },
          "triggerBalance": {
            "type": "number",
            "description": "Minimum balance required to trigger the rule. e.g. 100.00. Sweep Rule Only"
          },
          "splits": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/rule.SplitConfig"
            }
          },
          "conditionalSplits": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/rule.SplitConfig"
            }
          },
          "conditionalSplitConfig": {
            "$ref": "#/components/schemas/rule.ConditionalSplitConfig"
          },
          "sourceId": {
            "type": "string",
            "description": "Account to fund the supplied accountId. e.g. A1000002. Funding Rule Only"
          }
        }
      },
      "rule.MessageResponse": {
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