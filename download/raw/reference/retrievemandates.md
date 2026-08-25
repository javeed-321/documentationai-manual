---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve all Mandates for an account

Used to get all the Mandates for a specific account.

Learn more about implementing these endpoints with our below guides

* [Payment Collection Use Cases](https://modulr.readme.io/docs/collecting-payments-with-modulr-use-case-guides)
* [Set Up Recurring Collections](https://modulr.readme.io/docs/set-up-recurring-collections)
* [Failed Payments Recovery](https://modulr.readme.io/docs/failed-payment-recovery-direct-debit-pay-by-bank)

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
  "paths": {
    "/directdebits/enquire/{accountId}": {
      "get": {
        "tags": [
          "Direct Debit Outbound Mandate Operations"
        ],
        "summary": "Retrieve all Mandates for an account",
        "description": "Used to get all the Mandates for a specific account.",
        "operationId": "retrieveMandates",
        "parameters": [
          {
            "name": "accountId",
            "in": "path",
            "description": "Account Id",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "All Mandates were successfully retrieved",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/directdebitoutbound.EnquiryMandatesResponse"
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
                    "$ref": "#/components/schemas/directdebitoutbound.MessageResponse"
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
      "directdebitoutbound.EnquiryMandatesResponse": {
        "type": "object",
        "properties": {
          "accountId": {
            "type": "string",
            "description": "Account Id"
          },
          "mandatesList": {
            "type": "array",
            "description": "List of Mandates",
            "items": {
              "$ref": "#/components/schemas/directdebitoutbound.EnquiryMandateResponse"
            }
          }
        },
        "required": [
          "accountId",
          "mandatesList"
        ]
      },
      "directdebitoutbound.EnquiryMandateResponse": {
        "type": "object",
        "properties": {
          "mandateId": {
            "type": "string",
            "description": "Mandate Id"
          },
          "merchantNumber": {
            "type": "string",
            "description": "Merchant Number"
          },
          "merchantName": {
            "type": "string",
            "description": "Merchant Name"
          },
          "merchantAccountNumber": {
            "type": "string",
            "description": "Merchant Account Number"
          },
          "merchantSortCode": {
            "type": "string",
            "description": "Merchant Sort Code"
          },
          "mandateStatus": {
            "type": "string",
            "description": "Status"
          },
          "auddisIndicator": {
            "type": "string",
            "description": "AUDDIS Flag (AUDDIS / Non-AUDDIS)",
            "enum": [
              "A",
              "N",
              "T"
            ]
          },
          "setupDate": {
            "type": "string",
            "description": "Setup date"
          },
          "mandateReference": {
            "type": "string",
            "description": "Mandate Reference"
          }
        },
        "required": [
          "auddisIndicator",
          "mandateId",
          "mandateReference",
          "mandateStatus",
          "merchantAccountNumber",
          "merchantName",
          "merchantNumber",
          "merchantSortCode",
          "setupDate"
        ]
      },
      "directdebitoutbound.MessageResponse": {
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