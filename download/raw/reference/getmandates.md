---
updatedAt: 2026-06-11T13:31:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get Mandates based on search criteria.

If trying to find one or several particular mandates, then you can narrow down your search by using the filters available here. These include the mandate id, either the submitted or created date range, the account name on the mandate, etc...

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
    "/mandates": {
      "get": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Get Mandates based on search criteria.",
        "description": "If trying to find one or several particular mandates, then you can narrow down your search by using the filters available here. These include the mandate id, either the submitted or created date range, the account name on the mandate, etc...",
        "operationId": "getMandates",
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/directdebit.id"
            }
          },
          {
            "name": "accountId",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/directdebit.accountId"
            }
          },
          {
            "name": "q",
            "in": "query",
            "description": "Query parameter. ID, name or reference of mandate to search for",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Query parameter. ID, name or reference of mandate to search for"
            }
          },
          {
            "name": "fromCreatedDate",
            "in": "query",
            "description": "Mandates created on or after this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Mandates created on or after this date."
            }
          },
          {
            "name": "toCreatedDate",
            "in": "query",
            "description": "Mandates created on or before this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Mandates created on or before this date."
            }
          },
          {
            "name": "fromSubmittedDate",
            "in": "query",
            "description": "Mandates submitted on or after this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Mandates submitted on or after this date."
            }
          },
          {
            "name": "toSubmittedDate",
            "in": "query",
            "description": "Mandates submitted on or before this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Mandates submitted on or before this date."
            }
          },
          {
            "name": "status",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/directdebit.status"
            }
          },
          {
            "name": "name",
            "in": "query",
            "description": "Account Name on the Mandate",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Account Name on the Mandate"
            }
          },
          {
            "name": "reference",
            "in": "query",
            "description": "reference of the Mandate",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "reference of the Mandate"
            }
          },
          {
            "name": "externalReference",
            "in": "query",
            "description": "externalReference of the Mandate",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "externalReference of the Mandate"
            }
          },
          {
            "name": "bulkCreateRequestId",
            "in": "query",
            "description": "Bulk create request ID",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Bulk create request ID"
            }
          },
          {
            "name": "bulkCancelRequestId",
            "in": "query",
            "description": "Bulk cancel request ID",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Bulk cancel request ID"
            }
          },
          {
            "name": "sortField",
            "in": "query",
            "description": "Sort by field",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Sort by field",
              "pattern": "id|createdDate|submittedDate|status|name|reference|externalReference"
            }
          },
          {
            "name": "sortOrder",
            "in": "query",
            "description": "Sort order",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Sort order",
              "enum": [
                "ASC",
                "DESC"
              ],
              "example": "asc"
            },
            "example": "asc"
          },
          {
            "name": "page",
            "in": "query",
            "description": "Page to fetch (zero-indexed)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Page to fetch (zero-indexed)",
              "minimum": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Size of page to fetch.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Size of page to fetch.",
              "exclusiveMinimum": 0,
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
                  "$ref": "#/components/schemas/directdebit.MandatePageResponse"
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
      "directdebit.MandatePageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/directdebit.Mandate"
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
      "directdebit.id": {
        "type": "array",
        "description": "Id(s) of Mandate(s) to fetch.",
        "items": {
          "type": "string",
          "description": "Id(s) of Mandate(s) to fetch."
        }
      },
      "directdebit.accountId": {
        "type": "array",
        "description": "Id(s) of account to fetch Mandates for.",
        "items": {
          "type": "string",
          "description": "Id(s) of account to fetch Mandates for."
        }
      },
      "directdebit.Mandate": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for direct-debit-mandate.",
            "example": "G0000001"
          },
          "accountId": {
            "type": "string",
            "description": "Unique id for account for this mandate.",
            "example": "A0000001"
          },
          "reference": {
            "type": "string",
            "description": "DDI reference that was used during creation."
          },
          "externalReference": {
            "type": "string",
            "description": "External reference that was used during creation (appears on the bank statement)."
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when direct-debit-mandate was created.Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "status": {
            "type": "string",
            "description": "Status of the direct-debit-mandate. mandates must be 'ACTIVE' to make collections. Can be one of ",
            "example": "ACTIVE"
          },
          "nextValidCollectionDate": {
            "type": "string",
            "description": "The earliest date a collection can be created. Format is yyyy-MM-dd.",
            "example": "2018-01-10"
          },
          "name": {
            "type": "string"
          },
          "address": {
            "$ref": "#/components/schemas/directdebit.Address"
          },
          "sortCode": {
            "type": "string",
            "description": "Sort Code of the account for which direct-debit-mandate has been created.",
            "example": "123456"
          },
          "accountNumber": {
            "type": "string",
            "description": "Account Number for which direct-debit-mandate has been created.",
            "example": "87654321"
          },
          "payeeAccountBid": {
            "type": "string",
            "description": "Unique id for individual recipient account used for internal transfers",
            "example": "A0000001"
          },
          "bulkCreateRequestId": {
            "type": "string",
            "description": "Id associate to the bulk create request of this mandate.",
            "example": "R210000005"
          },
          "bulkCancelRequestId": {
            "type": "string",
            "description": "Id associate to the bulk cancel request of this mandate.",
            "example": "R210000006"
          }
        },
        "required": [
          "accountId",
          "accountNumber",
          "createdDate",
          "externalReference",
          "id",
          "nextValidCollectionDate",
          "reference",
          "sortCode",
          "status"
        ]
      },
      "directdebit.status": {
        "type": "array",
        "description": "Status of the Mandate",
        "items": {
          "type": "string",
          "description": "Status of the Mandate",
          "enum": [
            "PENDING",
            "SUBMITTED",
            "ACTIVE",
            "SUSPENDED",
            "REJECTED",
            "CANCELLED",
            "INVALID_REQUEST"
          ]
        }
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