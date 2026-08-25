---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create payments from one or more uploaded files

Create batch payment requests from valid upload files with a single applicable MFA challenge and send for processing to the payment service

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
    "/payment-files/proceed": {
      "post": {
        "tags": [
          "File Upload"
        ],
        "summary": "Create payments from one or more uploaded files",
        "description": "Create batch payment requests from valid upload files with a single applicable MFA challenge and send for processing to the payment service",
        "operationId": "proceed_1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/paymentfileupload.FilesCreatePaymentsRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "File created response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/paymentfileupload.FilesCreatePaymentsResponse"
                }
              }
            }
          },
          "400": {
            "description": "Invalid payment file",
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
      "paymentfileupload.FileCreatePaymentsResult": {
        "type": "object",
        "description": "Payment creation result for an individual file in a multi-file request",
        "properties": {
          "fileId": {
            "type": "string",
            "description": "Unique ID of the uploaded file",
            "example": "F1100001",
            "minLength": 1
          },
          "status": {
            "type": "string",
            "description": "Status of the uploaded file",
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
            "example": "INVALID"
          },
          "fileName": {
            "type": "string",
            "description": "File name of the uploaded file",
            "example": "file1"
          },
          "batchPaymentId": {
            "type": "string",
            "description": "Optional batch payment ID for successful files",
            "example": "B1100001"
          },
          "reason": {
            "type": "string",
            "description": "Reason, if any, for invalid status",
            "example": "Issue sending Batch payments"
          }
        },
        "required": [
          "fileId",
          "status"
        ]
      },
      "paymentfileupload.FilesCreatePaymentsResponse": {
        "type": "object",
        "description": "Response containing payment creation results for multiple files",
        "properties": {
          "results": {
            "type": "array",
            "description": "Results for each file processed",
            "items": {
              "$ref": "#/components/schemas/paymentfileupload.FileCreatePaymentsResult"
            }
          }
        }
      },
      "paymentfileupload.FilesCreatePaymentsRequest": {
        "type": "object",
        "description": "Request body containing file IDs to process for payment creation",
        "properties": {
          "fileIds": {
            "type": "array",
            "description": "List of fileIds to create payments from",
            "items": {
              "type": "string"
            },
            "maxItems": 10,
            "minItems": 0
          },
          "useDuplicate": {
            "type": "boolean",
            "description": "When true, duplicate files will be processed - Applies to all fileIds in this request"
          }
        },
        "required": [
          "fileIds"
        ]
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