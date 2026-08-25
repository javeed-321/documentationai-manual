---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get card token OTP details

Retrieves the OTP details given the corresponding card token ID

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
    "/card-tokens/{tokenId}/otp": {
      "get": {
        "tags": [
          "Cards"
        ],
        "summary": "Get card token OTP details",
        "description": "Retrieves the OTP details given the corresponding card token ID",
        "operationId": "getOtpDetails",
        "parameters": [
          {
            "name": "tokenId",
            "in": "path",
            "description": "Card token ID",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            },
            "example": "T110000001"
          }
        ],
        "responses": {
          "200": {
            "description": "OTP details retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.OtpDetails"
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
          "404": {
            "description": "Not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.OtpDetails"
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
      },
      "card.OtpDetails": {
        "type": "object",
        "properties": {
          "deliveryDetails": {
            "type": "string",
            "description": "OTP delivery details",
            "example": "+447777123456"
          },
          "deliveryMethod": {
            "type": "string",
            "description": "OTP delivery method",
            "enum": [
              "SMS",
              "EMAIL",
              "CALL_CENTRE",
              "AUTOMATED_CALL_CENTRE",
              "WEB",
              "APP",
              "PHONE_CALL",
              "NONE"
            ],
            "example": "SMS"
          },
          "expiry": {
            "type": "string",
            "format": "date-time",
            "description": "OTP expiry date and time (UTC, ISO 8601 format)",
            "example": "2021-10-31T14:01:55+0000"
          },
          "verificationCode": {
            "type": "string",
            "description": "OTP",
            "example": "393805"
          }
        },
        "required": [
          "deliveryDetails",
          "deliveryMethod",
          "expiry",
          "verificationCode"
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