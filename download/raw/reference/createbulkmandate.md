---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bulk request of Direct Debit mandates for the given account-id.

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
    "/mandates/bulk-create": {
      "post": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Bulk request of Direct Debit mandates for the given account-id.",
        "operationId": "createBulkMandate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/directdebit.BulkCreateMandateRequest"
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
                  "$ref": "#/components/schemas/directdebit.BulkCreateResponse"
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
      "directdebit.Address": {
        "type": "object",
        "properties": {
          "addressLine1": {
            "type": "string",
            "maxLength": 150,
            "minLength": 0
          },
          "addressLine2": {
            "type": "string",
            "maxLength": 150,
            "minLength": 0
          },
          "postTown": {
            "type": "string",
            "maxLength": 150,
            "minLength": 0
          },
          "postCode": {
            "type": "string",
            "maxLength": 8,
            "minLength": 0
          },
          "country": {
            "type": "string",
            "minLength": 1
          }
        },
        "required": [
          "addressLine1",
          "country",
          "postCode",
          "postTown"
        ]
      },
      "directdebit.BulkCreateResponse": {
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
          "auddisSubmissionDate": {
            "type": "string",
            "format": "date",
            "description": "auddis submission date for this bulk request."
          }
        },
        "required": [
          "accountId",
          "auddisSubmissionDate",
          "id",
          "migrationType",
          "status",
          "totalMandatesRequested"
        ]
      },
      "directdebit.BulkCreateMandateRequest": {
        "type": "object",
        "description": "List of Details of the Direct Debit mandates.",
        "properties": {
          "accountId": {
            "type": "string",
            "description": "The unique identifier for the account for which the mandates are to be created.",
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
          "auddisSubmissionDate": {
            "type": "string",
            "format": "date",
            "description": "The scheduled date for the AUDDIS (Automated Direct Debit Instruction Service) submission. This is the date when the mandates will be submitted to the AUDDIS system for processing."
          },
          "createMandateRequests": {
            "type": "array",
            "description": "The number of mandate creation requests. Each item in the array represents a request to create an individual mandate with its own set of parameters.",
            "items": {
              "$ref": "#/components/schemas/directdebit.CreateMandateRequest"
            },
            "minItems": 1
          }
        },
        "required": [
          "accountId",
          "createMandateRequests",
          "migrationType"
        ]
      },
      "directdebit.CreateMandateRequest": {
        "type": "object",
        "description": "Details of the Direct Debit mandate.",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name for mandate",
            "maxLength": 40,
            "minLength": 0
          },
          "reference": {
            "type": "string",
            "description": "Mandate reference, should contain only letters, numbers, space, dot, ampersand, forward-slash , hyphen",
            "example": "REFER-1.2",
            "maxLength": 18,
            "minLength": 6,
            "pattern": "^[a-zA-Z 0-9\\.\\&\\/-]+$"
          },
          "externalReference": {
            "type": "string",
            "description": "External reference for mandate",
            "maxLength": 50,
            "minLength": 0,
            "pattern": "[\\w-\\s]*"
          },
          "accountName": {
            "type": "string",
            "description": "Payer's account name",
            "maxLength": 100,
            "minLength": 1
          },
          "sortCode": {
            "type": "string",
            "description": "Payer's sort code of account for which direct-debit-mandate has to be created.",
            "example": "000000",
            "pattern": "\\p{Digit}{6}"
          },
          "accountNumber": {
            "type": "string",
            "description": "Payer's account number for which direct-debit-mandate has to be created.",
            "example": "12345678",
            "pattern": "\\p{Digit}{8}"
          },
          "address": {
            "$ref": "#/components/schemas/directdebit.Address",
            "description": "Payee's address"
          },
          "phone": {
            "type": "string",
            "description": "Payer's phone number",
            "maxLength": 14,
            "minLength": 0,
            "pattern": "\\p{Digit}+"
          },
          "email": {
            "type": "string",
            "description": "Payer's email address",
            "maxLength": 100,
            "minLength": 6,
            "pattern": "[^\\s@]+@[^\\s@]+\\.[^\\s@]+"
          },
          "payeeAccountBid": {
            "type": "string",
            "description": "Distribution accountBid, only used in FM-DD model"
          }
        },
        "required": [
          "accountName",
          "accountNumber",
          "address",
          "externalReference",
          "name",
          "phone",
          "reference",
          "sortCode"
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