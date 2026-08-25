---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Represent collection for given collection id

Represent collection for given collection id

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
  "tags": [
    {
      "name": "Direct Debits",
      "description": "Direct Debit operations"
    }
  ],
  "paths": {
    "/collection/{collectionId}/represent": {
      "post": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Represent collection for given collection id",
        "description": "Represent collection for given collection id",
        "operationId": "representCollection",
        "parameters": [
          {
            "name": "collectionId",
            "in": "path",
            "description": "Id of collection to represent",
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
            "description": "Collection represented"
          },
          "400": {
            "description": "Validation errors.",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/directdebit.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "Not Found",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/directdebit.MessageResponse"
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
      "directdebit.MessageResponse": {
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