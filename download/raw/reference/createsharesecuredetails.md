---
updatedAt: 2026-04-21T08:30:35.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Share secure card details via EMAIL or RETURN methods

This endpoint allows the user to create a link to share secure card details for a specific card

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
    "/cards/{cardId}/share-secure-details": {
      "post": {
        "tags": [
          "Share secure card details"
        ],
        "summary": "Share secure card details via EMAIL or RETURN methods",
        "description": "This endpoint allows the user to create a link to share secure card details for a specific card",
        "operationId": "createShareSecureDetails",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card to share secure card details for",
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
                "$ref": "#/components/schemas/card.ShareSecureCardDetailsRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Share secure card details link successfully created",
            "content": {
              "*/*": {
                "schema": {
                  "$ref": "#/components/schemas/card.CreateShareSecureCardDetailsResponse"
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
              "*/*": {
                "schema": {
                  "$ref": "#/components/schemas/card.CreateShareSecureCardDetailsResponse"
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
      "card.ShareSecureCardDetailsRequest": {
        "type": "object",
        "description": "Share secure card details request",
        "properties": {
          "shareCardDetails": {
            "$ref": "#/components/schemas/card.shareDetails"
          }
        }
      },
      "card.shareDetails": {
        "type": "object",
        "properties": {
          "method": {
            "type": "string",
            "description": "Method to share secure card details. Can be one of RETURN or EMAIL. Will default to EMAIL if not provided.",
            "enum": [
              "RETURN",
              "EMAIL"
            ]
          },
          "emails": {
            "type": "array",
            "description": "Emails to share secure card details with. Optional: Required if no method provided or if method EMAIL. Must be null for method RETURN",
            "items": {
              "type": "string",
              "format": "email"
            },
            "maxItems": 50,
            "minItems": 0
          },
          "noOfLinkAccesses": {
            "type": "integer",
            "format": "int64",
            "description": "Number of times token/link shared will be accessible. Default of 3"
          },
          "expiryDate": {
            "type": "string",
            "format": "date",
            "description": "Date of expiry of the secure card details link should be default of 15 days. Must match date format of yyyy-mm-dd and be in the future.",
            "example": "2026-01-01"
          },
          "otherDetailsToShare": {
            "type": "array",
            "description": "List of other card details to share. Will be validated against fields in card response. Default is nothing.",
            "items": {
              "type": "string"
            }
          },
          "message": {
            "type": "string",
            "description": "Message to be shared with the details. Only alphanumeric characters maximum of 200 and allowed chars -/:€$£#¢%().,!@",
            "maxLength": 200,
            "minLength": 0,
            "pattern": "^[a-zA-Z0-9\\-/:€$£#¢%().,!@ ]*$"
          },
          "externalReference": {
            "type": "string",
            "description": "External reference for the shared secure detail link",
            "maxLength": 50,
            "minLength": 1,
            "pattern": "[\\w -]*"
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
      },
      "card.CreateShareSecureCardDetailsResponse": {
        "type": "object",
        "description": "Response for creating a share secure card details link.",
        "properties": {
          "link": {
            "type": "string",
            "description": "Link to secure card details. Only returned for method RETURN"
          },
          "passcode": {
            "type": "string",
            "description": "passcode to view the secured card details. Only returned for method RETURN"
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