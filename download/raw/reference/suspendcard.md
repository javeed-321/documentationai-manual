---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# [Restricted] Suspend an existing card

Suspends a card to temporarily prevent any new authorisations as applied by the issuer or the program manager (i.e. not cardholder elective). This means that all new authorisations will be immediately declined. Outstanding authorisations are unaffected and settlement, chargebacks, refunds, etc will continue to function as normal.
Use of this endpoint is `Restricted`, depending on access being granted through contractual setup with Modulr.

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
    },
    {
      "name": "Restricted",
      "description": "Restricted access API calls"
    }
  ],
  "paths": {
    "/cards/{cardId}/suspend": {
      "post": {
        "tags": [
          "Restricted",
          "Cards"
        ],
        "summary": "[Restricted] Suspend an existing card",
        "description": "Suspends a card to temporarily prevent any new authorisations as applied by the issuer or the program manager (i.e. not cardholder elective). This means that all new authorisations will be immediately declined. Outstanding authorisations are unaffected and settlement, chargebacks, refunds, etc will continue to function as normal.\nUse of this endpoint is `Restricted`, depending on access being granted through contractual setup with Modulr.",
        "operationId": "suspendCard",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card which should be suspended",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Card suspended successfully"
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