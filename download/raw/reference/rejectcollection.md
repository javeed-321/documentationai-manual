---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Reject Collection

Reject Collection

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
    "/directdebits/reject": {
      "post": {
        "tags": [
          "Direct Debit Outbound Mandate Operations"
        ],
        "summary": "Reject Collection",
        "description": "Reject Collection",
        "operationId": "rejectCollection",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/directdebitoutbound.CollectionRejectRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Collection has been rejected"
          },
          "400": {
            "description": "Collection has not been rejected",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/directdebitoutbound.MessageResponse"
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
      "directdebitoutbound.CollectionRejectRequest": {
        "type": "object",
        "description": "Collection reject request",
        "properties": {
          "claimBId": {
            "type": "string",
            "description": "Collection Claim Business ID",
            "example": "A123456B",
            "pattern": "[A-Za-z]{1}[0-9]{2}([A-Za-z0-9]){5}"
          },
          "rejectCode": {
            "type": "string",
            "enum": [
              "ADVANCE_NOTICE_DISPUTED",
              "AMOUNT_DIFFERS",
              "AMOUNT_NOT_YET_DUE",
              "PRESENTATION_OVERDUE",
              "SKIP_DEBIT_ATTEMPT"
            ]
          }
        },
        "required": [
          "claimBId",
          "rejectCode"
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