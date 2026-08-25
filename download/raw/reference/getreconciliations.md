---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get Reconciliations based on search criteria.

Use this endpoint to get a list of Reconciliations for a given account and date.

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
    "/reconciliations": {
      "get": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Get Reconciliations based on search criteria.",
        "description": "Use this endpoint to get a list of Reconciliations for a given account and date.",
        "operationId": "getReconciliations",
        "parameters": [
          {
            "name": "accountId",
            "in": "query",
            "description": "Id(s) of account to fetch Reconciliations for.",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Id(s) of account to fetch Reconciliations for."
            }
          },
          {
            "name": "collectionDate",
            "in": "query",
            "description": "Reconciliation entry for date.",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "format": "date",
              "description": "Reconciliation entry for date."
            }
          },
          {
            "name": "sortField",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "pattern": "(id|createdDate)"
            }
          },
          {
            "name": "sortOrder",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "pattern": "(asc|desc)"
            }
          },
          {
            "name": "size",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "maximum": 500
            }
          },
          {
            "name": "page",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": {
                  "$ref": "#/components/schemas/directdebit.ReconciliationPageResponse"
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
      "directdebit.ReconciliationPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/directdebit.ReconciliationResponse"
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
      },
      "directdebit.ReconciliationResponse": {
        "type": "object",
        "properties": {
          "reconciliationId": {
            "type": "string"
          },
          "accountId": {
            "type": "string"
          },
          "collectionDate": {
            "type": "string",
            "format": "date"
          },
          "amount": {
            "type": "number"
          },
          "currency": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "notifiedDate": {
            "type": "string",
            "format": "date-time"
          },
          "schemeDetails": {
            "type": "object",
            "additionalProperties": {}
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