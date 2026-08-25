---
updatedAt: 2026-04-21T08:30:35.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve share secure card details

This endpoint allows the user to retrieve the share secure card details for a specific card

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
      "get": {
        "tags": [
          "Share secure card details"
        ],
        "summary": "Retrieve share secure card details",
        "description": "This endpoint allows the user to retrieve the share secure card details for a specific card",
        "operationId": "getShareSecureCardDetails",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card to retrieve share secure card details for",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "excludeTerminated",
            "in": "query",
            "description": "Exclude terminated share secure card details",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "page",
            "in": "query",
            "description": "Page to fetch (0 indexed)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "minimum": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Size of page to fetch",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "maximum": 500
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.ShareSecureCardDetailsPageResponse"
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
                  "$ref": "#/components/schemas/card.ShareSecureCardDetailsPageResponse"
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
      "card.ShareSecureCardDetailsPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/card.ShareSecureCardDetailsResponse"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Page size"
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total count"
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number, 0 based; i.e first-page = 0, second-page = 1"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total pages"
          }
        },
        "required": [
          "content",
          "page",
          "size",
          "totalPages",
          "totalSize"
        ]
      },
      "card.ShareSecureCardDetailsResponse": {
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