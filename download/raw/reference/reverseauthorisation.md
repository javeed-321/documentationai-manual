---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Reverse the card authorisation

Simulate a reversal of an authorization for a card

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
    "/authorisations/{authId}/reverse": {
      "post": {
        "tags": [
          "Card Simulator"
        ],
        "summary": "Reverse the card authorisation",
        "description": "Simulate a reversal of an authorization for a card",
        "operationId": "reverseAuthorisation",
        "parameters": [
          {
            "name": "authId",
            "in": "path",
            "description": "Card authorisation id to be reversed",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            },
            "example": "A00000000X"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/cardsimulator.ReverseAuthorizationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "No Content"
          },
          "400": {
            "description": "Validation errors",
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
      "cardsimulator.ReverseAuthorizationRequest": {
        "type": "object",
        "description": "Partial reversal amount. Omit body for full reversal",
        "properties": {
          "reversalAmount": {
            "type": "number",
            "description": "Amount to reverse. If absent or equal to the open amount, a full reversal is performed. Must not exceed the open amount.",
            "example": "3.00"
          }
        }
      },
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