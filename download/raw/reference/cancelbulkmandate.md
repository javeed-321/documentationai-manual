---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bulk mandate cancellation request for the given account-id.

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
    "/mandates/bulk-cancel": {
      "post": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Bulk mandate cancellation request for the given account-id.",
        "operationId": "cancelBulkMandate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/directdebit.BulkCancelMandateRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/directdebit.BulkCancelMandateResponse"
                }
              }
            }
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
      "directdebit.BulkCancelMandateRequest": {
        "type": "object",
        "description": "List of the Direct Debit mandates to cancel",
        "properties": {
          "accountId": {
            "type": "string",
            "description": "The unique identifier for the account for which the mandates are to be cancelled.",
            "minLength": 1
          },
          "migrationType": {
            "type": "string",
            "description": "The type of migration process that is being initiated.",
            "enum": [
              "SCHEDULE_AUDDIS_MIGRATION",
              "TRANSFER_OF_SUN",
              "OFFBOARDING"
            ]
          },
          "auddisCancellationDate": {
            "type": "string",
            "format": "date",
            "description": "The date for the AUDDIS (Automated Direct Debit Instruction Service) cancellation."
          },
          "mandateIds": {
            "type": "array",
            "description": "List of mandate ids to be cancelled.",
            "items": {
              "type": "string"
            },
            "minItems": 1
          }
        },
        "required": [
          "accountId",
          "mandateIds",
          "migrationType"
        ]
      },
      "directdebit.BulkCancelMandateResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for this bulk request.",
            "example": "R210000001"
          },
          "accountId": {
            "type": "string",
            "description": "Unique id for account for this bulk request.",
            "example": "A0000001"
          },
          "status": {
            "type": "string",
            "description": "Status for this bulk request."
          },
          "migrationType": {
            "type": "string",
            "description": "Migration type for this bulk request.",
            "enum": [
              "SCHEDULE_AUDDIS_MIGRATION",
              "TRANSFER_OF_SUN",
              "OFFBOARDING"
            ]
          },
          "totalMandatesRequested": {
            "type": "integer",
            "format": "int64",
            "description": "Total mandates requested for this bulk request."
          },
          "auddisCancellationDate": {
            "type": "string",
            "format": "date",
            "description": "auddis cancellation date for this bulk request."
          }
        },
        "required": [
          "accountId",
          "auddisCancellationDate",
          "id",
          "migrationType",
          "status",
          "totalMandatesRequested"
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