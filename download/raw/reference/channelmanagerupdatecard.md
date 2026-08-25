---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager Update card

Update a virtual card

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
    "/channel-managers/cards/{cardId}": {
      "post": {
        "tags": [
          "Channel Manager Card"
        ],
        "summary": "Channel Manager Update card",
        "description": "Update a virtual card",
        "operationId": "channelManagerUpdateCard",
        "parameters": [
          {
            "name": "cardId",
            "in": "path",
            "description": "The card id.",
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
                "$ref": "#/components/schemas/channelmanager.UpdateCardRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "Virtual card updated successfully"
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
      "channelmanager.AuthorisationWindowRequest": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "example": "2025-01-01"
          },
          "endDate": {
            "type": "string",
            "example": "2025-01-01"
          }
        }
      },
      "channelmanager.CardCustomFieldRequest": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Custom field key"
          },
          "value": {
            "type": "string",
            "description": "Custom field value"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
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
      "channelmanager.UpdateCardHolder": {
        "type": "object",
        "properties": {
          "billingAddress": {
            "$ref": "#/components/schemas/channelmanager.AddressDetail",
            "description": "Billing address for the card holder. Must be NULL for individual customers."
          },
          "shippingAddress": {
            "$ref": "#/components/schemas/channelmanager.AddressDetail",
            "description": "Shipping address details for card. Optional for individual customers whose partner has verification type EXTERNAL"
          },
          "dateOfBirth": {
            "type": "string",
            "format": "date",
            "description": "Cardholder date of birth. Must match date format of yyyy-mm-dd. Required for virtual consumer and physical cards. Must be NULL for individual customers.",
            "example": "2001-01-01"
          },
          "mobileNumber": {
            "type": "string",
            "description": "Cardholder mobile number. Must start with a '+', followed by the country code and then the mobile number. Required for virtual consumer and physical cards.",
            "example": "+447123456000"
          },
          "email": {
            "type": "string",
            "format": "email",
            "description": "Cardholder email",
            "example": "cardholder@example.com",
            "maxLength": 50,
            "minLength": 0
          }
        }
      },
      "channelmanager.UpdateCardRequest": {
        "type": "object",
        "description": "Card",
        "properties": {
          "limit": {
            "type": "number",
            "description": "Total card authorisation limit.",
            "example": "1000.00"
          },
          "cancellationDate": {
            "type": "string",
            "description": "ISO 8601 date with year, month & day components only. The supplied value must be in the future and at most 1 day before the expiry date.",
            "example": "2025-01-01"
          },
          "customFields": {
            "type": "array",
            "description": "Custom fields",
            "items": {
              "$ref": "#/components/schemas/channelmanager.CardCustomFieldRequest"
            },
            "maxItems": 20,
            "minItems": 1
          },
          "holder": {
            "$ref": "#/components/schemas/channelmanager.UpdateCardHolder",
            "description": "CardHolder"
          },
          "authWindow": {
            "$ref": "#/components/schemas/channelmanager.AuthorisationWindowRequest",
            "description": "Authorisation Windows allow the card holder to add a period of time where the card can ONLY be used, if an Authorisation Window set then transactions outside this window will decline. ISO 8601 date with year, month & day components only."
          }
        }
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