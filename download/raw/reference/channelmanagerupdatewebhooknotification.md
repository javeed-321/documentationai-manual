---
updatedAt: 2026-04-21T08:30:35.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Update a specific Webhook notification configuration for a Channel Manager

Update a specific Webhook notification configuration for a Channel Manager. Replace operations are the only available

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
    "/channel-managers/webhook-notifications/{notificationId}": {
      "patch": {
        "tags": [
          "Channel Manager Webhook Notifications"
        ],
        "summary": "Update a specific Webhook notification configuration for a Channel Manager",
        "description": "Update a specific Webhook notification configuration for a Channel Manager. Replace operations are the only available",
        "operationId": "channelManagerUpdateWebhookNotification",
        "parameters": [
          {
            "name": "notificationId",
            "in": "path",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/channelmanager.Replace"
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "400": {
            "description": "When parameters are invalid parameters",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/channelmanager.MessageResponse"
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
      "channelmanager.MessageResponse": {
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
      "channelmanager.PatchOperation": {
        "type": "object",
        "discriminator": {
          "propertyName": "op",
          "mapping": {
            "add": "#/components/schemas/channelmanager.Add",
            "move": "#/components/schemas/channelmanager.Move",
            "test": "#/components/schemas/channelmanager.Test",
            "replace": "#/components/schemas/channelmanager.Replace",
            "copy": "#/components/schemas/channelmanager.Copy",
            "remove": "#/components/schemas/channelmanager.Remove"
          }
        },
        "properties": {
          "op": {
            "type": "string"
          },
          "path": {
            "type": "string",
            "example": "/path/to/field"
          }
        },
        "required": [
          "op",
          "path"
        ]
      },
      "channelmanager.Replace": {
        "allOf": [
          {
            "$ref": "#/components/schemas/channelmanager.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "value": {}
            }
          }
        ],
        "description": "Replace field",
        "required": [
          "op",
          "path"
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