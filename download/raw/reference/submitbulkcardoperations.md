---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Submit bulk cards operations

Send Card details for Create/Update/Cancel/Patch Cards in bulk. Processing part will be asynchronous

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
      "post": {
        "tags": [
          "Cards Bulk Operations"
        ],
        "summary": "Submit bulk cards operations",
        "description": "Send Card details for Create/Update/Cancel/Patch Cards in bulk. Processing part will be asynchronous",
        "operationId": "submitBulkCardOperations",
        "parameters": [
          {
            "name": "validateOnly",
            "in": "query",
            "description": "Flag of whether to validate batch entries and not submit for processing. Default false.",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "keepOperations",
            "in": "query",
            "description": "Flag of whether to persist operations for batch request. Can only be true if validateOnly is true, default is false.",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/card.BulkCardsOpsRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "description": "Accepted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.BulkCardsOpsResponse"
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
                  "$ref": "#/components/schemas/card.BulkCardsOpsResponse"
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
      "card.BulkCardsOpsResponse": {
        "type": "object",
        "properties": {
          "bulkRequestId": {
            "type": "string"
          },
          "submissionTimestamp": {
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
          }
        }
      },
      "card.BulkCardsOpsRequest": {
        "type": "object",
        "properties": {
          "externalRef": {
            "type": "string"
          },
          "operations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/card.BulkCardsOperation"
            },
            "minItems": 1
          }
        },
        "required": [
          "operations"
        ]
      },
      "card.BulkCardsOperation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "operationType": {
            "type": "string",
            "enum": [
              "CREATE",
              "UPDATE",
              "PATCH",
              "CANCEL"
            ]
          },
          "payload": {},
          "cardId": {
            "type": "string"
          },
          "accountId": {
            "type": "string"
          }
        },
        "required": [
          "operationType",
          "payload"
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