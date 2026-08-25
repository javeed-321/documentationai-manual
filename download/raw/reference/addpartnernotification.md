---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Set up a Notification for a Partner

Sets up a new notification for a partner using the partner's ID as a reference. Returns a notification ID that should be saved if the notification needs to be amended in the future

Note: Only the Customer Verification Status Change webhook `CUSTVSTAT` is supported as a Partner level webhook, for more info see the ReadMe guide: [Modulr Webhooks](https://modulr.readme.io/docs/notifications-1)

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
      "name": "Notification",
      "description": "Operations on Notifications"
    }
  ],
  "paths": {
    "/partners/{partnerId}/notifications": {
      "post": {
        "tags": [
          "Notification"
        ],
        "summary": "Set up a Notification for a Partner",
        "description": "Sets up a new notification for a partner using the partner's ID as a reference. Returns a notification ID that should be saved if the notification needs to be amended in the future",
        "operationId": "addPartnerNotification",
        "parameters": [
          {
            "name": "partnerId",
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
                "$ref": "#/components/schemas/notification.NotificationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/notification.NotificationResponse"
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
                    "$ref": "#/components/schemas/notification.MessageResponse"
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
      "notification.NotificationResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique Identifier for the notification."
          },
          "customerId": {
            "type": "string",
            "description": "Unique Identifier for the customer of this notification."
          },
          "type": {
            "type": "string",
            "description": "Type of notification",
            "enum": [
              "PAYIN",
              "PAYOUT",
              "BALANCE_LOW",
              "BALANCE_HIGH",
              "BALANCE",
              "DDMANDATE",
              "CUSTVSTAT",
              "ACCOUNT_STATEMENT",
              "PENDING_PAYMENTS",
              "DD_INCOMING_DEBIT",
              "DD_FAILED_CLAIM",
              "DD_FUNDS_RETURNED",
              "CARD_AUTH",
              "CARD_AUTH_OFFLINE",
              "CARD_CREATION",
              "UPCOMING_CREDIT",
              "UPCOMING_COLLECTION_CREDIT",
              "UPCOMING_COLLECTION_DEBIT",
              "CARD_STATUS_UPDATE",
              "CARD_TOKEN_PROVISIONING",
              "PAYMENT_COMPLIANCE_STATUS",
              "DD_COLLECTION_STATUS",
              "ACCOUNT_SWITCH_UPDATE",
              "PAYMENT_FILE_UPLOAD",
              "ACCOUNT_STATUS_CHANGE",
              "PAYMENT_APPROVAL_STATUS_CHANGE",
              "CUSTOMER_BATCH_PAYMENT_APPROVAL_STATUS_CHANGE",
              "CARD_BULK_OPS_COMPLETED",
              "CUSTOMER_STATUS",
              "CREDIT_AUTH",
              "DD_INDEMNITY_CLAIM_STATUS",
              "APPLICATION_STATUS_CHANGE",
              "CUSTOMER_CREATED"
            ]
          },
          "channel": {
            "type": "string",
            "description": "Channel used to send the notification.",
            "enum": [
              "EMAIL",
              "WEBHOOK"
            ]
          },
          "status": {
            "type": "string",
            "description": "Status of notification.",
            "enum": [
              "ACTIVE",
              "INACTIVE"
            ]
          },
          "destinations": {
            "type": "array",
            "description": "A list of emails or url(webhook) used to send the notification. For 'EMAIL' channel this can be a list of comma separated email addresses. For 'WEBHOOK' channel this will be a single URL.",
            "items": {
              "type": "string"
            }
          },
          "config": {
            "$ref": "#/components/schemas/notification.NotificationConfig",
            "description": "Configuration information for this Notification entity."
          }
        },
        "required": [
          "channel",
          "config",
          "customerId",
          "destinations",
          "id",
          "status",
          "type"
        ]
      },
      "notification.NotificationConfig": {
        "type": "object",
        "properties": {
          "threshold": {
            "type": "number",
            "description": "Amount threshold which triggers the notification. This attribute only applies to 'EMAIL' notifications channel, of type 'PAYIN', 'PAYOUT'.",
            "minimum": 0
          },
          "timesToRun": {
            "type": "array",
            "description": "Times of the day when to trigger the notification. This attribute applies only to 'EMAIL' notifications channel, of type 'BALANCE'.",
            "items": {
              "type": "string",
              "enum": [
                "AM",
                "PM"
              ]
            }
          },
          "daysToRun": {
            "type": "array",
            "description": "Days of the week when to trigger the notification. This attribute applies only to 'EMAIL' notifications channel, of type 'BALANCE'.",
            "items": {
              "type": "string",
              "enum": [
                "MONDAY",
                "TUESDAY",
                "WEDNESDAY",
                "THURSDAY",
                "FRIDAY",
                "SATURDAY",
                "SUNDAY"
              ]
            }
          },
          "retry": {
            "type": "boolean",
            "description": "Flag indicating whether failed webhooks should be retried. This attribute applies only to 'WEBHOOK' notifications channel."
          },
          "secret": {
            "type": "string",
            "description": "Mandatory for webhook. Secret that is used in HMAC calculation, for webhooks. This attribute applies only to 'WEBHOOK' notifications channel.",
            "maxLength": 32,
            "minLength": 32
          },
          "hmacAlgorithm": {
            "type": "string",
            "description": "Signing algorithm that is used in Webhook HMAC calculation. This attribute only applies to 'WEBHOOK' notifications channel.",
            "enum": [
              "hmac-sha1",
              "hmac-sha256",
              "hmac-sha384",
              "hmac-sha512"
            ]
          }
        }
      },
      "notification.MessageResponse": {
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
      "notification.NotificationRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of the notification.",
            "enum": [
              "PAYIN",
              "PAYOUT",
              "BALANCE_LOW",
              "BALANCE_HIGH",
              "BALANCE",
              "DDMANDATE",
              "CUSTVSTAT",
              "ACCOUNT_STATEMENT",
              "PENDING_PAYMENTS",
              "DD_INCOMING_DEBIT",
              "DD_FAILED_CLAIM",
              "DD_FUNDS_RETURNED",
              "CARD_AUTH",
              "CARD_AUTH_OFFLINE",
              "CARD_CREATION",
              "UPCOMING_CREDIT",
              "UPCOMING_COLLECTION_CREDIT",
              "UPCOMING_COLLECTION_DEBIT",
              "CARD_STATUS_UPDATE",
              "CARD_TOKEN_PROVISIONING",
              "PAYMENT_COMPLIANCE_STATUS",
              "DD_COLLECTION_STATUS",
              "ACCOUNT_SWITCH_UPDATE",
              "PAYMENT_FILE_UPLOAD",
              "ACCOUNT_STATUS_CHANGE",
              "PAYMENT_APPROVAL_STATUS_CHANGE",
              "CUSTOMER_BATCH_PAYMENT_APPROVAL_STATUS_CHANGE",
              "CARD_BULK_OPS_COMPLETED",
              "CUSTOMER_STATUS",
              "CREDIT_AUTH",
              "DD_INDEMNITY_CLAIM_STATUS",
              "APPLICATION_STATUS_CHANGE",
              "CUSTOMER_CREATED"
            ]
          },
          "channel": {
            "type": "string",
            "description": "Channel used for sending the notification",
            "enum": [
              "EMAIL",
              "WEBHOOK"
            ]
          },
          "destinations": {
            "type": "array",
            "description": "The list of emails or url(webhook) used for sending the notification. For 'EMAIL' channel this can be a list of comma separated email addresses. For 'WEBHOOK' channel this should be a single URL.",
            "items": {
              "type": "string"
            },
            "minItems": 1
          },
          "config": {
            "$ref": "#/components/schemas/notification.NotificationConfig",
            "description": "Configuration information for this Notification entity."
          }
        },
        "required": [
          "channel",
          "config",
          "destinations",
          "type"
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