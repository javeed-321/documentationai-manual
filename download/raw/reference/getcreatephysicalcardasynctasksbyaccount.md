---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get physical card create tasks by account

View the details of create physical card tasks by account.  Ordered by createdDate, with the newest entries appearing first

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
      "name": "Async",
      "description": "Asynchronous card task operations"
    },
    {
      "name": "Cards",
      "description": "Cards API"
    }
  ],
  "paths": {
    "/accounts/{accountId}/physical-card-request-tasks": {
      "get": {
        "tags": [
          "Async",
          "Cards"
        ],
        "summary": "Get physical card create tasks by account",
        "description": "View the details of create physical card tasks by account.  Ordered by createdDate, with the newest entries appearing first",
        "operationId": "getCreatePhysicalCardAsyncTasksByAccount",
        "parameters": [
          {
            "name": "accountId",
            "in": "path",
            "description": "The account ID to retrieve create physical card tasks for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "statuses",
            "in": "query",
            "description": "Statuses of tasks to be retrieved",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "enum": [
                "RECEIVED",
                "RUNNING",
                "COMPLETE",
                "ERROR"
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
              "default": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Size of page to fetch",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 20,
              "maximum": 500
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Tasks returned successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.AsyncTaskPageResponse"
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
      "card.AsyncTaskResponse": {
        "type": "object",
        "properties": {
          "taskBid": {
            "type": "string",
            "description": "ID of async task",
            "example": "T110000003"
          },
          "resourceUrl": {
            "type": "string",
            "description": "Url of available resource after task completion",
            "example": "/cards/V110000022"
          },
          "resourceId": {
            "type": "string",
            "description": "ID of resource after task completion. Will only be returned for COMPLETE tasks.",
            "example": "V110000022"
          },
          "type": {
            "type": "string",
            "description": "Type of async task"
          },
          "status": {
            "type": "string",
            "description": "Status of the task"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "The creation date of the task",
            "example": "2020-03-23T11:01:54.826+0000"
          },
          "errorReason": {
            "type": "string",
            "description": "The error reason. Only populated if status is ERROR"
          }
        },
        "required": [
          "createdDate",
          "status",
          "taskBid",
          "type"
        ]
      },
      "card.AsyncTaskPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/card.AsyncTaskResponse"
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