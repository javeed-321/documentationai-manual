---
updatedAt: 2026-04-21T08:30:35.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve a single share secure card details record

This endpoint retrieves a specific share secure card details record for a given card and share details token id

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
      "name": "Share secure card details",
      "description": "Share secure card details operations"
    }
  ],
  "paths": {
    "/cards/{cardId}/share-secure-details/{shareSecureDetailsId}": {
      "get": {
        "tags": [
          "Share secure card details"
        ],
        "summary": "Retrieve a single share secure card details record",
        "description": "This endpoint retrieves a specific share secure card details record for a given card and share details token id",
        "operationId": "getShareSecureCardDetailsById",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card to retrieve the share secure card details for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "shareSecureDetailsId",
            "in": "path",
            "description": "The id of the token whose share secure card details is being retrieved",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "includeActivity",
            "in": "query",
            "description": "Flag whether to include the activities of the token",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.ShareSecureCardDetailSummaryResponse"
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
            "description": "Invalid permissions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.ShareSecureCardDetailSummaryResponse"
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
      "card.ShareSecureCardDetailSummaryResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "createdBy": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "expiryDate": {
            "type": "string",
            "format": "date-time"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time"
          },
          "lastRevealedDate": {
            "type": "string",
            "format": "date-time"
          },
          "noOfAccessesLeft": {
            "type": "integer",
            "format": "int64"
          },
          "maxAccessesAllowed": {
            "type": "integer",
            "format": "int64"
          },
          "message": {
            "type": "string"
          },
          "externalReference": {
            "type": "string"
          },
          "otherDetails": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "activity": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/card.ShareSecureCardDetailsActivity"
            }
          },
          "customerId": {
            "type": "string"
          },
          "customerName": {
            "type": "string"
          },
          "cardScheme": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          }
        }
      },
      "card.ShareSecureCardDetailsActivity": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time"
          },
          "createdBy": {
            "type": "string"
          },
          "shareMethod": {
            "type": "string",
            "description": "Method to share secure card details",
            "enum": [
              "RETURN",
              "EMAIL"
            ]
          }
        }
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