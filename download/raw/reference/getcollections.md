---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get all collection activities of an account

Once a collection schedule is set up, any past collections (whether successful or not) can be retrieved.
This endpoint supports only paginated responses with the default page size of 20 (min 1, max 500).


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
    "/collections": {
      "get": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Get all collection activities of an account",
        "description": "Once a collection schedule is set up, any past collections (whether successful or not) can be retrieved.\nThis endpoint supports only paginated responses with the default page size of 20 (min 1, max 500).\n",
        "operationId": "getCollections",
        "parameters": [
          {
            "name": "accountId",
            "in": "query",
            "description": "Account Id to fetch collections items for.",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "mandateId",
            "in": "query",
            "description": "Id of mandate whose the collection to fetch.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "type",
            "in": "query",
            "description": "type of collection to fetch",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "startDate",
            "in": "query",
            "description": "Collection activities happened on or after this date",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "endDate",
            "in": "query",
            "description": "Collection item activities happened on or before this date",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
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
            "name": "sortField",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "pattern": "(id|createdDate|activityDate)"
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
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": {
                  "$ref": "#/components/schemas/directdebit.DirectDebitPageResponseCollection"
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
      "directdebit.Collection": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for a direct-debit collection",
            "example": "K000100100"
          },
          "mandateId": {
            "type": "string",
            "description": "Unique id for direct-debit mandate.",
            "example": "G0000001"
          },
          "collectionScheduleId": {
            "type": "string",
            "description": "Unique id for direct-debit collection schedule for which triggered the collection",
            "example": "Q9200001"
          },
          "activityDate": {
            "type": "string",
            "description": "collection or reportRaised date for indemnity???",
            "example": "2018-01-09"
          },
          "amount": {
            "type": "number",
            "description": "Amount of the collection payment",
            "example": "100.00"
          },
          "type": {
            "type": "string",
            "description": "Type of the collection activity.  Can be one of ",
            "example": "COLLECTION"
          },
          "payerName": {
            "type": "string",
            "description": "Name of the payer",
            "example": "Mr John Doe"
          },
          "status": {
            "type": "string",
            "description": "Status of the collection.  Can be one of ",
            "example": "FAILED"
          },
          "message": {
            "type": "string",
            "description": "Failure description of the payment activity",
            "example": "Instruction Cancelled"
          },
          "originalActivityDate": {
            "type": "string",
            "description": "The original scheduled date for a payment to be collected",
            "example": "2018-01-09"
          },
          "reconciliationDate": {
            "type": "string",
            "description": "The reconciled date for a payment to be collected",
            "example": "2018-01-09"
          },
          "reconciliationReference": {
            "type": "string",
            "description": "The reconciled reference that links to a payment",
            "example": "2018-01-09"
          },
          "ddiReference": {
            "type": "string",
            "description": "collectionReference - if present - is appended to the original DDI reference\n(used during mandate creation - referred to as core reference) for the specified scheduled collection\nwithout altering the original mandate core reference. This will be visible to the payer on their account.\nThe reference and collectionReference combined have 18 character limit and can only contain alphanumeric\ncharacters with underscore, hyphen and space permitted",
            "example": "ABCD-EFGH"
          }
        },
        "required": [
          "activityDate",
          "amount",
          "id",
          "mandateId",
          "message",
          "originalActivityDate",
          "payerName",
          "reconciliationDate",
          "reconciliationReference",
          "status",
          "type"
        ]
      },
      "directdebit.DirectDebitPageResponseCollection": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/directdebit.Collection"
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