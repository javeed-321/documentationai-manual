---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get bulk cards by id

Get all batch specific information

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
    "/bulk-cards/{bulkRequestId}": {
      "get": {
        "tags": [
          "Cards Bulk Operations"
        ],
        "summary": "Get bulk cards by id",
        "description": "Get all batch specific information",
        "operationId": "getBulkCardsInfo",
        "parameters": [
          {
            "name": "bulkRequestId",
            "in": "path",
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
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.BulkCardsInfoResponse"
                }
              }
            }
          },
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
                  "$ref": "#/components/schemas/card.BulkCardsInfoResponse"
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
      "card.Error": {
        "type": "object",
        "properties": {
          "operationIndex": {
            "type": "integer",
            "format": "int64"
          },
          "operationId": {
            "type": "string"
          },
          "field": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        }
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
      },
      "card.BulkCardsInfoResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "source": {
            "type": "string",
            "enum": [
              "API",
              "FILE_UPLOAD"
            ]
          },
          "originalName": {
            "type": "string"
          },
          "submissionTime": {
            "type": "string",
            "format": "date-time"
          },
          "status": {
            "type": "string",
            "enum": [
              "SUBMITTED",
              "VALIDATED",
              "VALIDATED_WITH_ERRORS",
              "PROCESSING",
              "PARTIALLY_PROCESSED_WITH_ERRORS",
              "PARTIALLY_PROCESSED",
              "PROCESSED",
              "ARCHIVED",
              "DELETED"
            ]
          },
          "totalOperations": {
            "type": "integer",
            "format": "int64"
          },
          "successfulOperations": {
            "type": "integer",
            "format": "int64"
          },
          "failedOperations": {
            "type": "integer",
            "format": "int64"
          },
          "processedOperations": {
            "type": "integer",
            "format": "int64"
          },
          "createdBy": {
            "type": "string"
          },
          "externalRef": {
            "type": "string"
          },
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/card.Error"
            }
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