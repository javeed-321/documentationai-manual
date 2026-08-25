---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve failed Webhook Notifications for a Webhook using the Notification ID.

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
    "/integration-notification-webhooks/{notificationId}/failures": {
      "get": {
        "tags": [
          "Integration Notification"
        ],
        "summary": "Retrieve failed Webhook Notifications for a Webhook using the Notification ID.",
        "operationId": "getFailedWebhookNotifications",
        "parameters": [
          {
            "name": "notificationId",
            "in": "path",
            "description": "Id of notification",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "fromDateTime",
            "in": "query",
            "description": "Failed since Date. Needs to be urlEncoded value",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
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
              "format": "int32",
              "default": 0,
              "minimum": 0
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
              "default": 20,
              "maximum": 500,
              "minimum": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/integrationnotification.PaginatedWebhookFailureResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad request",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/integrationnotification.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "Not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/integrationnotification.PaginatedWebhookFailureResponse"
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
      "integrationnotification.MessageResponse": {
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
      "integrationnotification.PaginatedWebhookFailureResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of failed webhook delivery records",
            "items": {
              "$ref": "#/components/schemas/integrationnotification.WebhookFailureResponse"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Number of records returned in the current page"
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total number of matching failure records"
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number (0-based)"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total number of pages available"
          }
        }
      },
      "integrationnotification.WebhookFailureResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Notification bid for which the webhook delivery failed"
          },
          "failureDateTime": {
            "type": "string",
            "format": "date-time",
            "description": "Failure time. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g '2017-01-28T01:01:01+0000'"
          },
          "data": {
            "description": "Payload data that was attempted to be sent to the webhook URL"
          }
        },
        "required": [
          "data",
          "failureDateTime",
          "id"
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