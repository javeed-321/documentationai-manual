---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve secure card details (PAN + CVV + PIN)

Receives the secure card details token as a parameter. This call is meant to be done from the cardholder device and not directly by the partner

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
    "/cards/secure-details": {
      "get": {
        "tags": [
          "Cards"
        ],
        "summary": "Retrieve secure card details (PAN + CVV + PIN)",
        "description": "Receives the secure card details token as a parameter. This call is meant to be done from the cardholder device and not directly by the partner",
        "operationId": "getSecureCardDetails",
        "responses": {
          "200": {
            "description": "Secure card details retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.SecureCardDetails"
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
          },
          "403": {
            "description": "Forbidden. Token may be missing or invalid",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.SecureCardDetails"
                }
              }
            }
          }
        },
        "security": []
      }
    }
  },
  "components": {
    "schemas": {
      "card.SecureCardDetails": {
        "type": "object",
        "properties": {
          "pan": {
            "type": "string",
            "description": "PAN",
            "example": "4567123412341234"
          },
          "cvv2": {
            "type": "string",
            "description": "CVV",
            "example": "123"
          },
          "pin": {
            "type": "string",
            "description": "PIN",
            "example": "1234"
          }
        },
        "required": [
          "cvv2",
          "pan"
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
      }
    }
  },
  "x-readme": {
    "proxy-enabled": false
  }
}
```