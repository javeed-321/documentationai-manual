---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Update card authentication

Support knowledge based authentication (KBA)

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
    "/cards/{cardId}/authentication": {
      "put": {
        "tags": [
          "Cards"
        ],
        "summary": "Update card authentication",
        "description": "Support knowledge based authentication (KBA)",
        "operationId": "updateCardAuthentication",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card which has authentication information to be updated",
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
                "$ref": "#/components/schemas/card.UpdateCardAuthenticationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "Card authentication updated"
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
      "card.UpdateCardAuthenticationRequest": {
        "type": "object",
        "description": "Authentication",
        "properties": {
          "knowledgeBase": {
            "type": "array",
            "description": "3DS Knowledge-Based Authentication (KBA) answers",
            "items": {
              "$ref": "#/components/schemas/card.CardKnowledgeBasedAuthentication"
            }
          }
        },
        "required": [
          "knowledgeBase"
        ]
      },
      "card.CardKnowledgeBasedAuthentication": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "3DS knowledge-based authentication answer type",
            "enum": [
              "FIRST_PET_NAME",
              "MATERNAL_GRANDMOTHER_MAIDEN_NAME",
              "FAVOURITE_CHILDHOOD_FRIEND",
              "FIRST_CAR",
              "CITY_PARENTS_MET"
            ]
          },
          "answer": {
            "type": "string",
            "description": "3DS knowledge-based authentication answer",
            "maxLength": 45,
            "minLength": 1
          }
        },
        "required": [
          "answer",
          "type"
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