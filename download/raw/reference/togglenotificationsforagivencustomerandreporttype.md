---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Toggled notifications for customer and card report type

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
      "name": "Cards",
      "description": "Cards API"
    }
  ],
  "paths": {
    "/customers/{customerId}/card-report-types/{reportType}/notifications/status": {
      "post": {
        "tags": [
          "Cards"
        ],
        "summary": "Toggled notifications for customer and card report type",
        "operationId": "toggleNotificationsForAGivenCustomerAndReportType",
        "parameters": [
          {
            "name": "customerId",
            "in": "path",
            "description": "Id of customer to toggle notification for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "reportType",
            "in": "path",
            "description": "Type of report customer wants notification toggled for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string",
              "enum": [
                "DAILY_CARD_ACTIVITY",
                "MONTHLY_CARD_ACTIVITY",
                "DAILY_ACCOUNT_FUNDING",
                "MONTHLY_ACCOUNT_FUNDING",
                "DAILY_AUTH_WINDOW"
              ]
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/card.UpdateCardReportNotificationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "Toggled notifications for customer and report type"
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
            "description": "Customer can not edit this data"
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
      "card.UpdateCardReportNotificationRequest": {
        "type": "object",
        "description": "Notification request containing the status of the notification",
        "properties": {
          "status": {
            "type": "string",
            "description": "status",
            "minLength": 1
          }
        },
        "required": [
          "status"
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