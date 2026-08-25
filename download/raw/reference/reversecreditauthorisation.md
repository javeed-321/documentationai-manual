---
updatedAt: 2026-07-06T12:44:20.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Reverse a credit authorisation

Reverse a pending credit authorisation, producing a CREDIT_AUTH_REV activity

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
    "/credit-authorisations/{creditAuthId}/reverse": {
      "post": {
        "tags": [
          "Card Simulator"
        ],
        "summary": "Reverse a credit authorisation",
        "description": "Reverse a pending credit authorisation, producing a CREDIT_AUTH_REV activity",
        "operationId": "reverseCreditAuthorisation",
        "parameters": [
          {
            "name": "creditAuthId",
            "in": "path",
            "description": "ID of the CREDIT_AUTH activity to reverse",
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
            "description": "No Content"
          },
          "400": {
            "description": "Activity is not a CREDIT_AUTH or in PENDING status",
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
            "description": "Activity not found"
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