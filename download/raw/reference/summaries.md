---
updatedAt: 2026-06-16T15:15:40.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get paginated summaries of child file uploads

Returns a paginated list of child file upload summaries for a delegate payment file. For delegate users the fileId is the parent bid; for regular users it is the file bid.

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
      "name": "File Upload",
      "description": "Upload payment files"
    }
  ],
  "paths": {
    "/payment-files/{fileId}/summaries": {
      "get": {
        "tags": [
          "File Upload"
        ],
        "summary": "Get paginated summaries of child file uploads",
        "description": "Returns a paginated list of child file upload summaries for a delegate payment file. For delegate users the fileId is the parent bid; for regular users it is the file bid.",
        "operationId": "summaries",
        "parameters": [
          {
            "name": "fileId",
            "in": "path",
            "description": "Payment File ID",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
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
              "minimum": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Page size (max 500)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 20,
              "exclusiveMinimum": 0,
              "maximum": 500
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated file upload summaries response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/paymentfileupload.FileUploadSummariesResponse"
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
                    "$ref": "#/components/schemas/paymentfileupload.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "File not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/paymentfileupload.FileUploadSummariesResponse"
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
      "paymentfileupload.MessageResponse": {
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
      "paymentfileupload.FileUploadSummaryContent": {
        "type": "object",
        "description": "Summary of a single child file upload",
        "properties": {
          "status": {
            "type": "string",
            "description": "Status of the child file upload",
            "enum": [
              "NEW",
              "SUBMITTED",
              "PROCESSING",
              "INVALID",
              "VALID",
              "DUPLICATE",
              "REJECTED",
              "ERROR_RETRYABLE",
              "ACCEPTED",
              "PROCESSED",
              "SENDING",
              "PAYMENT_PROCESSING",
              "SPLIT_FILE",
              "PARTIALLY_ACCEPTED"
            ],
            "example": "ACCEPTED"
          },
          "customerName": {
            "type": "string",
            "description": "Customer name associated with the child file",
            "example": "TestCustomer"
          },
          "batchPaymentId": {
            "type": "string",
            "description": "Batch payment ID, null if not yet processed",
            "example": "D0000001"
          },
          "payments": {
            "type": "array",
            "description": "Aggregated payments grouped by destination account",
            "items": {
              "$ref": "#/components/schemas/paymentfileupload.PaymentSummary"
            }
          }
        }
      },
      "paymentfileupload.FileUploadSummariesResponse": {
        "type": "object",
        "description": "Paginated summaries of child file uploads for a delegate payment file",
        "properties": {
          "fileId": {
            "type": "string",
            "description": "File ID of the parent upload",
            "example": "F1100001"
          },
          "fileName": {
            "type": "string",
            "description": "File name of the parent upload",
            "example": "file"
          },
          "content": {
            "type": "array",
            "description": "Page content — one entry per child file upload",
            "items": {
              "$ref": "#/components/schemas/paymentfileupload.FileUploadSummaryContent"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Number of items in this page",
            "example": 3
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total number of child file uploads",
            "example": 3
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number (0 indexed)",
            "example": 0
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total number of pages",
            "example": 1
          }
        }
      },
      "paymentfileupload.PaymentSummary": {
        "type": "object",
        "description": "Aggregated payment count per destination account",
        "properties": {
          "sortCode": {
            "type": "string",
            "description": "Destination account sort code",
            "example": "111111"
          },
          "accountNumber": {
            "type": "string",
            "description": "Destination account number",
            "example": "11111111"
          },
          "numberOfPayments": {
            "type": "integer",
            "format": "int32",
            "description": "Number of payments to this account",
            "example": 3
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