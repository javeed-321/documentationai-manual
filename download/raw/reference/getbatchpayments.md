---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get batch payments by a given set of parameters

This endpoint allows for a user who has submitted multiple batch to use some criteria to get the batch payments.

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
      "name": "Payments",
      "description": "Operations on Payments"
    }
  ],
  "paths": {
    "/batchpayments": {
      "get": {
        "tags": [
          "Payments"
        ],
        "summary": "Get batch payments by a given set of parameters",
        "description": "This endpoint allows for a user who has submitted multiple batch to use some criteria to get the batch payments.",
        "operationId": "getBatchPayments",
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "description": "List of batch payment IDs",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/payment.id"
            }
          },
          {
            "name": "externalReference",
            "in": "query",
            "description": "Batch payments External Reference contains this text.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Batch payments External Reference contains this text.",
              "example": "aReference_00001",
              "maxLength": 50,
              "minLength": 0,
              "pattern": "[\\w-\\s]*"
            },
            "example": "aReference_00001"
          },
          {
            "name": "fromCreatedDate",
            "in": "query",
            "description": "Batch payments created date equal or after to this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "format": "date",
              "description": "Batch payments created date equal or after to this date.",
              "example": "2022-05-16"
            },
            "example": "2022-05-16"
          },
          {
            "name": "toCreatedDate",
            "in": "query",
            "description": "Batch payments created date equal or before this date.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "format": "date",
              "description": "Batch payments created date equal or before this date.",
              "example": "2026-06-08"
            },
            "example": "2026-06-08"
          },
          {
            "name": "batchPaymentStatuses",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/payment.batchPaymentStatuses"
            }
          },
          {
            "name": "paymentStatuses",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/payment.paymentStatuses"
            }
          },
          {
            "name": "approvalStatus",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "$ref": "#/components/schemas/payment.approvalStatus"
            }
          },
          {
            "name": "currentUserCanApprove",
            "in": "query",
            "description": "Only return batch payments the current user can approve.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "description": "Only return batch payments the current user can approve.",
              "example": true
            },
            "example": true
          },
          {
            "name": "createdByCustomerId",
            "in": "query",
            "description": "Limit results by the customer which created the batch payment request",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Limit results by the customer which created the batch payment request"
            }
          },
          {
            "name": "submissionType",
            "in": "query",
            "description": "Limit results to batches with submission type specified",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "description": "Limit results to batches with submission type specified",
              "enum": [
                "BATCH",
                "BULK"
              ]
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
              "default": 0,
              "description": "Page to fetch (0 indexed)"
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
              "default": 20,
              "description": "Size of Page to fetch",
              "maximum": 500
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/payment.BatchPaymentsResponse"
                }
              }
            }
          },
          "400": {
            "description": "Validation errors",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/payment.MessageResponse"
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
      "payment.BatchPaymentsResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/payment.BatchPayment"
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
      "payment.PaymentApproval": {
        "type": "object",
        "description": "A single approval against a batch payment request",
        "properties": {
          "approvedBy": {
            "type": "string",
            "description": "ID of user who approved this batch payment request",
            "example": "U2100021"
          },
          "approvedOn": {
            "type": "string",
            "format": "date",
            "description": "Date this approval was applied",
            "example": "2022-06-25"
          }
        }
      },
      "payment.BatchSummary": {
        "type": "object",
        "properties": {
          "total": {
            "type": "integer",
            "format": "int64",
            "description": "Total count of payment requests in this batch"
          },
          "inprogress": {
            "type": "integer",
            "format": "int64",
            "description": "Count of payment requests in progress"
          },
          "invalid": {
            "type": "integer",
            "format": "int64",
            "description": "Count of invalid payment requests"
          },
          "errors": {
            "type": "integer",
            "format": "int64",
            "description": "Count of failed payment requests"
          },
          "cancelled": {
            "type": "integer",
            "format": "int64",
            "description": "Count of cancelled payment requests"
          },
          "completed": {
            "type": "integer",
            "format": "int64",
            "description": "Count of completed payments"
          },
          "info": {
            "type": "string",
            "description": "Additional information or error message regarding this batch payment request"
          }
        }
      },
      "payment.paymentStatuses": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "Current status of payment. Multiple statuses can be specified by repeating the parameter.",
          "enum": [
            "SUBMITTED",
            "SCREENING_REQ",
            "VALIDATED",
            "PENDING_FOR_DATE",
            "PENDING_FOR_FUNDS",
            "EXT_PROC",
            "PROCESSED",
            "RECONCILED",
            "ER_INVALID",
            "ER_EXTCONN",
            "ER_EXTSYS",
            "ER_EXPIRED",
            "ER_GENERAL",
            "ER_BATCH",
            "EXT_SENT",
            "UNALLOCATED",
            "HELD",
            "RETURNED",
            "CANCELLED",
            "REPROCESSING",
            "VOID",
            "CLEARING",
            "HELD_IN_SUSPENSE"
          ]
        }
      },
      "payment.batchPaymentStatuses": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "Current status of batch. Multiple statuses can be specified by repeating the parameter.",
          "enum": [
            "ACCEPTED",
            "REJECTED",
            "SUBMITTED",
            "CANCELLED"
          ]
        }
      },
      "payment.PaymentsSummary": {
        "type": "object",
        "description": "Summary of payments and approvals",
        "properties": {
          "totalPaymentCount": {
            "type": "integer",
            "format": "int32",
            "description": "Total count of payments",
            "example": 10
          },
          "totalAmount": {
            "type": "number",
            "description": "Sum total of payment amounts",
            "example": "100.00"
          },
          "pendingApprovalCount": {
            "type": "integer",
            "format": "int32",
            "description": "Count of payments currently pending approval",
            "example": 5
          },
          "pendingApprovalAmount": {
            "type": "number",
            "description": "Sum total of payment amounts currently pending approval",
            "example": "50.00"
          }
        }
      },
      "payment.id": {
        "type": "array",
        "description": "List of batch payment IDs",
        "items": {
          "type": "string",
          "description": "List of batch payment IDs"
        }
      },
      "payment.approvalStatus": {
        "type": "array",
        "description": "Payment approval status, multiple statuses can be specified by repeating the parameter",
        "items": {
          "type": "string",
          "description": "Payment approval status, multiple statuses can be specified by repeating the parameter",
          "enum": [
            "NOTNEEDED",
            "PENDING",
            "APPROVED",
            "REJECTED",
            "DELETED"
          ]
        }
      },
      "payment.BatchPayment": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for the Batch Payment. 10 characters long",
            "example": "D920000001"
          },
          "externalReference": {
            "type": "string",
            "description": "External reference, if provided",
            "example": "aReference_00001"
          },
          "status": {
            "type": "string",
            "description": "Current status of batch.",
            "enum": [
              "ACCEPTED",
              "REJECTED",
              "SUBMITTED",
              "CANCELLED"
            ],
            "example": "ACCEPTED"
          },
          "totalPayments": {
            "type": "integer",
            "format": "int32",
            "description": "Total count of payments in this batch",
            "example": 9123
          },
          "currentUserCanApprove": {
            "type": "boolean",
            "description": "Whether the user is allowed to approve this batch, based on their approval limits, and applicable configuration",
            "example": true
          },
          "paymentDetails": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/payment.PaymentsSummary"
            },
            "description": "Summary of payments and approvals, per currency (as a 3-alpha currency code)"
          },
          "approvals": {
            "type": "array",
            "description": "List of batch-level approvals",
            "items": {
              "$ref": "#/components/schemas/payment.PaymentApproval"
            }
          },
          "currentUserCanCancel": {
            "type": "boolean",
            "description": "Whether the user is allowed and currently able to cancel at least one of the payments in this batch"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when the batch payment was created. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "createdBy": {
            "type": "string",
            "description": "ID of the user that created the payment"
          },
          "processingDateFrom": {
            "type": "string",
            "format": "date",
            "description": "Earliest processing date in the batch file or the batch creation date if the file does not have any dates. Date format 'yyyy-MM-dd'",
            "example": "2017-01-28"
          },
          "processingDateTo": {
            "type": "string",
            "format": "date",
            "description": "Last processing date in the batch file or empty if the file does not have any dates. Date format 'Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000'",
            "example": "2017-01-28"
          },
          "earliestScheduledPaymentDate": {
            "type": "string",
            "format": "date",
            "description": "Earliest processing date in the batch file or empty if the file does not have any dates. Date format 'Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000'",
            "example": "2017-01-28"
          },
          "requiredApprovalCount": {
            "type": "integer",
            "format": "int32",
            "description": "The number of required approvals for the batch.  Applicable to batch payments of submissionType BATCH"
          },
          "batchSummary": {
            "$ref": "#/components/schemas/payment.BatchSummary",
            "description": "Summary of the state of payment requests in this batch"
          },
          "strict": {
            "type": "boolean",
            "description": "Strict processing flag. Whether the entire batch should fail on any individual payment validation failure"
          }
        }
      },
      "payment.MessageResponse": {
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