---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List active bulk card requests

Retrieve non-terminated (not processed/archived/deleted) bulk card requests for current user

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
    "/bulk-cards": {
      "get": {
        "tags": [
          "Cards Bulk Operations"
        ],
        "summary": "List active bulk card requests",
        "description": "Retrieve non-terminated (not processed/archived/deleted) bulk card requests for current user",
        "operationId": "getActiveBulkCardRequests",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "Page to retrieve (0 indexed)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Page to retrieve (0 indexed)",
              "example": 0,
              "minimum": 0
            },
            "example": 0
          },
          {
            "name": "size",
            "in": "query",
            "description": "Page size",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "description": "Page size",
              "example": 500,
              "maximum": 500,
              "minimum": 1
            },
            "example": 500
          }
        ],
        "responses": {
          "400": {
            "description": "Invalid request",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/card.MessageResponse"
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden. Incorrect permissions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.BulkRequestPageResponse"
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
      "card.BulkRequestPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/card.BulkRequestResponse"
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
            "description": "Current page number, 0 based; i.e first-page = 0, second-page = 1"
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
      "card.BulkRequestResponse": {
        "type": "object",
        "description": "Bulk card request details",
        "properties": {
          "id": {
            "type": "string",
            "description": "Bulk request ID",
            "example": "B000000001"
          },
          "filename": {
            "type": "string",
            "description": "Filename of the uploaded file",
            "example": "example.csv"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "Date and time when the bulk request was created"
          },
          "createdBy": {
            "type": "string",
            "description": "User ID who created the bulk request",
            "example": "U000001"
          },
          "status": {
            "type": "string",
            "description": "Status of the bulk request",
            "example": "VALIDATED_WITH_ERRORS"
          },
          "totalOperations": {
            "type": "integer",
            "format": "int64",
            "description": "Total number of operations in the bulk request",
            "example": 200
          },
          "successfulOperations": {
            "type": "integer",
            "format": "int64",
            "description": "Number of successful operations",
            "example": 194
          },
          "failedOperations": {
            "type": "integer",
            "format": "int64",
            "description": "Number of failed operations",
            "example": 6
          },
          "processedOperations": {
            "type": "integer",
            "format": "int64",
            "description": "Number of processed operations",
            "example": 142
          },
          "externalRef": {
            "type": "string",
            "description": "External reference",
            "example": "example ref"
          }
        },
        "required": [
          "createdBy",
          "createdDate",
          "failedOperations",
          "id",
          "status",
          "successfulOperations",
          "totalOperations"
        ]
      },
      "card.MessageResponse": {
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