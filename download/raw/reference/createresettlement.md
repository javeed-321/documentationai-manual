---
updatedAt: 2026-07-06T14:08:13.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Resettlement of a chargeback

Simulate a resettlement (second presentment) for an existing CHARGEBACK activity, producing a RESETTLEMENT activity.

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
      "name": "Card Simulator",
      "description": "Cards Simulator API"
    }
  ],
  "paths": {
    "/activities/{chargebackActivityId}/resettlement": {
      "post": {
        "tags": [
          "Card Simulator"
        ],
        "summary": "Resettlement of a chargeback",
        "description": "Simulate a resettlement (second presentment) for an existing CHARGEBACK activity, producing a RESETTLEMENT activity.",
        "operationId": "createResettlement",
        "parameters": [
          {
            "name": "chargebackActivityId",
            "in": "path",
            "description": "ID of the CHARGEBACK activity to resettle",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            },
            "example": "X000000001"
          }
        ],
        "responses": {
          "204": {
            "description": "Resettlement processed"
          },
          "400": {
            "description": "Activity is not a CHARGEBACK",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/cardsimulator.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "Chargeback activity not found"
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
      "cardsimulator.MessageResponse": {
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