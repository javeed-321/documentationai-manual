---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Confirm the availability of funds in an account.

Confirm the availability of funds in account, prior to initiating a Variable Recurring Payment, using an authorised consent.

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
    "/vrp-consents/{consentId}/funds-confirmation": {
      "post": {
        "tags": [
          "Variable Recurring Payments"
        ],
        "summary": "Confirm the availability of funds in an account.",
        "description": "Confirm the availability of funds in account, prior to initiating a Variable Recurring Payment, using an authorised consent.",
        "operationId": "confirmFunds",
        "parameters": [
          {
            "name": "consentId",
            "in": "path",
            "description": "Vrp consent id",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/pispgateway.VrpConfirmationOfFundsRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Confirmation of Funds successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/pispgateway.VrpConfirmationOfFundsResponse"
                }
              }
            }
          },
          "400": {
            "description": "Confirmation of funds request cannot be processed as the consent with the provided ID does not exist.",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/pispgateway.MessageResponse"
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
      "pispgateway.VrpConfirmationOfFundsResponse": {
        "type": "object",
        "properties": {
          "fundsAvailable": {
            "type": "boolean",
            "description": "The result of funds availability check, can be one of 'true' or 'false'"
          },
          "fundsAvailabilityCheckDateTime": {
            "type": "string",
            "format": "date-time",
            "description": "The time that the funds availability check occurred"
          }
        }
      },
      "pispgateway.MessageResponse": {
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
      "pispgateway.VrpConfirmationOfFundsRequest": {
        "type": "object",
        "description": "Request object to confirm the availability of funds in account",
        "properties": {
          "currency": {
            "type": "string",
            "description": "Currency of the maximum individual amount. Must be specified in ISO 4217 format."
          },
          "amount": {
            "type": "number",
            "description": "amount that will be confirmed for availability of funds - '1' = 1.00 GBP",
            "example": "100.00"
          }
        },
        "required": [
          "currency"
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