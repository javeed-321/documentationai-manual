---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# [Restricted] Expire an existing authorisation

[Restricted] Expire an existing authorisation. Note: CREDIT_AUTH and CREDIT_AUTH_REV activities cannot be expired via this endpoint.

This Endpoint will allow you to cancel any pending authorisations so that you can release the reserved funds back to the available balance. Authorisations expired automatically after 7 days, pre-authorisations after 10 days.  This endpoint **should not** be exposed within a Cardholder UI to allow them to release funds. Providing access within Cardholder UI poses a serious risk of accounts becoming overdrawn as transactions may be authorised without the necessary funds to clear and settle back to the merchant. Any overdrawn balances would be the liability of the partner and not Modulr.

The endpoint should ideally be connected to your internal admin/CRM Service as a manual check should will be required before releasing the funds.

The Cardholder should provide some evidence that the merchant has declined the authorisation or will not take payment.

* screenshot of decline message for e-commerce
* copy of void/decline receipt for POS

Once you have confirmed that the payment will not be taken, the funds can be released back to the cardholder.

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
    "/authorisations/{authId}/expire": {
      "post": {
        "tags": [
          "Restricted",
          "Cards"
        ],
        "summary": "[Restricted] Expire an existing authorisation",
        "description": "[Restricted] Expire an existing authorisation. Note: CREDIT_AUTH and CREDIT_AUTH_REV activities cannot be expired via this endpoint.",
        "operationId": "expireAuthorisation",
        "parameters": [
          {
            "name": "authId",
            "in": "path",
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
            "description": "Authorisation expired successfully"
          },
          "400": {
            "description": "Bad Request",
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
            "description": "Authorisation not found"
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