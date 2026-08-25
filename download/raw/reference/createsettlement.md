---
updatedAt: 2026-06-02T13:36:01.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create a settlement without prior authorisation

Submit a settlement directly to the reconciliation pipeline without a prior authorisation

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
      "name": "Card Simulator",
      "description": "Cards Simulator API"
    }
  ],
  "paths": {
    "/cards/{cardId}/settlements": {
      "post": {
        "tags": [
          "Card Simulator"
        ],
        "summary": "Create a settlement without prior authorisation",
        "description": "Submit a settlement directly to the reconciliation pipeline without a prior authorisation",
        "operationId": "createSettlement",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "Card ID to settle against",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            },
            "example": "V000000001"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/cardsimulator.CardSettlementRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created"
          },
          "400": {
            "description": "Validation errors",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/cardsimulator.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "Card not found"
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
      "cardsimulator.CardSettlementRequest": {
        "type": "object",
        "description": "Optional settlement details. Omit body for full settlement.",
        "properties": {
          "transactionAmount": {
            "type": "number",
            "description": "The transaction amount",
            "example": "5.45"
          },
          "transactionCurrency": {
            "type": "string",
            "description": "The transaction currency",
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
            ],
            "example": "GBP"
          },
          "fxRate": {
            "type": "number",
            "description": "The foreign exchange rate",
            "example": "0.8"
          },
          "mcc": {
            "type": "string",
            "description": "Merchant Category Code",
            "example": "5812"
          }
        },
        "required": [
          "fxRate",
          "mcc",
          "transactionAmount",
          "transactionCurrency"
        ]
      },
      "cardsimulator.MessageResponse": {
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