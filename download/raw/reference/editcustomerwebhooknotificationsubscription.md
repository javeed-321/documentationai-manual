---
updatedAt: 2026-04-21T05:49:14.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Update a specific Webhook Notification Subscription for a Customer.

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
    "/customers/{customerId}/integration-notifications/{notificationId}": {
      "put": {
        "tags": [
          "Integration Notification"
        ],
        "summary": "Update a specific Webhook Notification Subscription for a Customer.",
        "operationId": "editCustomerWebhookNotificationSubscription",
        "parameters": [
          {
            "name": "customerId",
            "in": "path",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
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
                "$ref": "#/components/schemas/integrationnotification.WebhookNotificationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/integrationnotification.WebhookNotificationResponse"
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
                  "$ref": "#/components/schemas/integrationnotification.WebhookNotificationResponse"
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
      "integrationnotification.WebhookNotificationResponse": {
        "type": "object",
        "description": "Response object for integration notification operations. Contains all common fields from WebhookNotificationRequestBase, along with the notification ID and type.",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique Identifier for the notification"
          },
          "url": {
            "type": "string",
            "description": "The URL used for sending the notification.",
            "minLength": 1
          },
          "retry": {
            "type": "boolean",
            "description": "Flag indicating whether failed webhooks should be retried."
          },
          "secret": {
            "type": "string",
            "description": "Secret that is used in HMAC calculation for webhooks.",
            "maxLength": 32,
            "minLength": 32
          },
          "hmacAlgorithm": {
            "type": "string",
            "description": "HMAC signing algorithm used to calculate the webhook signature.",
            "enum": [
              "hmac-sha1",
              "hmac-sha256",
              "hmac-sha384",
              "hmac-sha512"
            ]
          },
          "type": {
            "type": "string",
            "description": "Type of the notification.",
            "enum": [
              "PAYOUT",
              "PAYIN",
              "CARD_AUTH",
              "CARD_AUTH_OFFLINE",
              "CARD_STATUS_UPDATE",
              "PAYMENT_COMPLIANCE_STATUS"
            ]
          },
          "webhookTypeConfiguration": {
            "$ref": "#/components/schemas/integrationnotification.WebhookTypeConfiguration",
            "description": "Value used to determine whether payin webhooks should be sent or not."
          }
        },
        "required": [
          "hmacAlgorithm",
          "id",
          "retry",
          "secret",
          "type",
          "url"
        ]
      },
      "integrationnotification.WebhookNotificationRequest": {
        "type": "object",
        "description": "Request object used to create/update a new integration notification.",
        "properties": {
          "url": {
            "type": "string",
            "description": "The URL used for sending the notification.",
            "minLength": 1
          },
          "retry": {
            "type": "boolean",
            "description": "Flag indicating whether failed webhooks should be retried."
          },
          "secret": {
            "type": "string",
            "description": "Secret that is used in HMAC calculation for webhooks.",
            "maxLength": 32,
            "minLength": 32
          },
          "hmacAlgorithm": {
            "type": "string",
            "description": "HMAC signing algorithm used to calculate the webhook signature.",
            "enum": [
              "hmac-sha1",
              "hmac-sha256",
              "hmac-sha384",
              "hmac-sha512"
            ]
          },
          "type": {
            "type": "string",
            "description": "Type of the notification.",
            "enum": [
              "PAYOUT",
              "PAYIN",
              "CARD_AUTH",
              "CARD_AUTH_OFFLINE",
              "CARD_STATUS_UPDATE",
              "PAYMENT_COMPLIANCE_STATUS"
            ]
          },
          "webhookTypeConfiguration": {
            "$ref": "#/components/schemas/integrationnotification.WebhookTypeConfiguration",
            "description": "Value used to determine whether payin webhooks should be sent or not."
          }
        },
        "required": [
          "hmacAlgorithm",
          "retry",
          "secret",
          "type",
          "url"
        ]
      },
      "integrationnotification.WebhookTypeConfiguration": {
        "type": "object",
        "description": "Optional webhook type specific configuration",
        "properties": {
          "amountThreshold": {
            "type": "number",
            "description": "Amount threshold used to determine whether PAYIN webhooks should be sent.",
            "minimum": 0
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