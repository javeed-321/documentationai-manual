---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager Replace card 

Replace a card, with a reason STOLEN, DAMAGED, LOST, RENEW

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
  "paths": {
    "/channel-managers/cards/{cardId}/replace": {
      "post": {
        "tags": [
          "Channel Manager Card"
        ],
        "summary": "Channel Manager Replace card ",
        "description": "Replace a card, with a reason STOLEN, DAMAGED, LOST, RENEW",
        "operationId": "channelManagerReplaceCard",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The ID of the card",
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
                "$ref": "#/components/schemas/channelmanager.CardReplacementRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Card replaced successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/channelmanager.CardReplacementResponse"
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
                    "$ref": "#/components/schemas/channelmanager.MessageResponse"
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
      "channelmanager.MessageResponse": {
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
      "channelmanager.ProductDesignDetail": {
        "type": "object",
        "properties": {
          "cardRef": {
            "type": "string",
            "description": "Design reference for card",
            "minLength": 1
          },
          "packagingRef": {
            "type": "string",
            "description": "Design reference for card packaging",
            "minLength": 1
          }
        },
        "required": [
          "cardRef",
          "packagingRef"
        ]
      },
      "channelmanager.AddressDetail": {
        "type": "object",
        "description": "Address details for the cardholder. Optional for individual customers whose partner has verification type EXTERNAL.",
        "properties": {
          "addressLine1": {
            "type": "string",
            "description": "First line of address",
            "example": "Floor 10",
            "maxLength": 50,
            "minLength": 1
          },
          "addressLine2": {
            "type": "string",
            "description": "Second line of address",
            "example": "80 George Street",
            "maxLength": 50,
            "minLength": 0
          },
          "postTown": {
            "type": "string",
            "description": "Post town",
            "example": "EDINBURGH",
            "maxLength": 20,
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "description": "Postcode",
            "example": "EH2 3BU",
            "maxLength": 10,
            "minLength": 1
          },
          "country": {
            "type": "string",
            "description": "Country (ISO 3166 alpha-2 country code)",
            "enum": [
              "AT",
              "BE",
              "BG",
              "CY",
              "CZ",
              "DK",
              "EE",
              "FI",
              "FR",
              "DE",
              "GR",
              "HR",
              "HU",
              "IS",
              "IE",
              "IT",
              "LV",
              "LI",
              "LT",
              "LU",
              "MT",
              "NL",
              "NO",
              "PL",
              "PT",
              "RO",
              "SK",
              "SI",
              "ES",
              "SE",
              "AX",
              "AW",
              "BL",
              "CW",
              "GF",
              "GL",
              "GP",
              "ME",
              "MF",
              "MQ",
              "NC",
              "PF",
              "PM",
              "RE",
              "SX",
              "TF",
              "WF",
              "YT",
              "AI",
              "BM",
              "FK",
              "GB",
              "GG",
              "GI",
              "GS",
              "IO",
              "JE",
              "KY",
              "MS",
              "PN",
              "SH",
              "TC",
              "VG"
            ],
            "example": "GB",
            "minLength": 1
          }
        },
        "required": [
          "addressLine1",
          "country",
          "postCode",
          "postTown"
        ]
      },
      "channelmanager.CardReplacementRequest": {
        "type": "object",
        "description": "Replacement",
        "properties": {
          "reason": {
            "type": "string",
            "description": "The reason for replacing the card. Can be one of DAMAGED (physical only), LOST, STOLEN, RENEW",
            "enum": [
              "STOLEN",
              "DAMAGED",
              "LOST",
              "RENEW"
            ],
            "example": "STOLEN"
          },
          "externalRef": {
            "type": "string",
            "description": "Client reference for the newly created card. Maximum of 50 alphanumeric characters (including underscore, hyphen and space).",
            "maxLength": 50,
            "minLength": 1,
            "pattern": "[\\w-\\s]*"
          },
          "design": {
            "$ref": "#/components/schemas/channelmanager.ProductDesignDetail",
            "description": "Design references for physical card and packaging"
          },
          "expiry": {
            "type": "string",
            "description": "ISO 8601 date with year & month components only. The supplied value must be in the future (cannot be the current month) and is _inclusive_ of the specified month. If no expiry is selected, the standard product expiry date will be set",
            "example": "2026-12"
          },
          "shippingAddress": {
            "$ref": "#/components/schemas/channelmanager.AddressDetail",
            "description": "Shipping address details for card. Optional for individual customers whose partner has verification type EXTERNAL"
          }
        },
        "required": [
          "reason"
        ]
      },
      "channelmanager.CardReplacementResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Card identifier. Maximum of 10 alphanumeric characters."
          },
          "cvv2": {
            "type": "string",
            "description": "Card CVV2 number."
          },
          "pan": {
            "type": "string",
            "description": "Full card PAN."
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "The creation date of the card",
            "example": "2019-01-29T11:01:54.826+0000"
          },
          "externalRef": {
            "type": "string",
            "description": "Client reference for the newly created card."
          },
          "expiry": {
            "type": "string",
            "description": "An ISO 8601 date with year & month components only",
            "example": "2018-12"
          },
          "maxLimit": {
            "type": "string",
            "description": "Maximum limit which can be set on this card and is the maximum lifetime spend the card can have",
            "example": "4000.00"
          },
          "managementToken": {
            "type": "string",
            "description": "Card Management Token required for API users for additional security when managing sensitive card data"
          }
        },
        "required": [
          "createdDate",
          "cvv2",
          "expiry",
          "externalRef",
          "id",
          "maxLimit",
          "pan"
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