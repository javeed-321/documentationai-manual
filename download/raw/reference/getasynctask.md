---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get a card task

Retrieve the card task. If the task is complete, the resource URL will be provided to allow client to fetch the completed resource.

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
    }
  ],
  "paths": {
    "/card-tasks/{taskId}": {
      "get": {
        "tags": [
          "Async"
        ],
        "summary": "Get a card task",
        "description": "Retrieve the card task. If the task is complete, the resource URL will be provided to allow client to fetch the completed resource.",
        "operationId": "getAsyncTask",
        "parameters": [
          {
            "name": "taskId",
            "in": "path",
            "description": "The ID of the card task",
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
            "description": "Details returned of the card task. If task is complete, response will include link to resource",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.AsyncTaskResponse"
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