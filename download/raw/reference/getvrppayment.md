---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get Variable Recurring Payment

Fetch the details of a payment initiated using Variable Recurring Payment (VRP) based on a unique payment ID.

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
    "/vrp/{vrpPaymentId}": {
      "get": {
        "tags": [
          "Variable Recurring Payments"
        ],
        "summary": "Get Variable Recurring Payment",
        "description": "Fetch the details of a payment initiated using Variable Recurring Payment (VRP) based on a unique payment ID.",
        "operationId": "getVrpPayment",
        "parameters": [
          {
            "name": "vrpPaymentId",
            "in": "path",
            "description": "Vrp Payment Id",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/pispgateway.VrpPaymentDetailsResponse"
                }
              }
            }
          },
          "400": {
            "description": "The payment cannot be retrieved as it does not exist.",
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
      "pispgateway.VrpPaymentDetailsResponse": {
        "type": "object",
        "properties": {
          "consentId": {
            "type": "string",
            "description": "The unique identifier of the VRP consent initiation request at Modulr.",
            "example": "E210000004"
          },
          "payment": {
            "$ref": "#/components/schemas/pispgateway.Payment",
            "description": "Payment details for the VRP payment initiation request."
          },
          "status": {
            "type": "string",
            "description": "The current status of the VRP payment.",
            "enum": [
              "SUBMITTED",
              "ACCEPTEDWITHOUTPOSTING",
              "ACCEPTEDSETTLEMENTINPROCESS",
              "PENDING",
              "REJECTED",
              "ACCEPTEDCREDITSETTLEMENTCOMPLETED",
              "ACCEPTEDSETTLEMENTCOMPLETED",
              "RECEIVED",
              "CANCELLED",
              "BLOCKED",
              "ACCEPTEDTECHNICALVALIDATION",
              "ACCEPTEDCUSTOMERPROFILE",
              "ACCEPTEDFUNDSCHECKED",
              "ACCEPTEDWITHCHANGE",
              "ACCEPTEDSETTLEMENTCOMPLETEDCREDITORACCOUNT",
              "ACCEPTEDSETTLEMENTCOMPLETEDDEBITORACCOUNT",
              "ER_GENERAL",
              "ER_EXTSYS"
            ]
          },
          "statusReasonCodes": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "Specifies the status reason in a code form.",
              "example": "ERIN",
              "maxLength": 4,
              "minLength": 1
            }
          },
          "interactionType": {
            "type": "string",
            "description": "PSU interaction type permitted under this consent. Must be one of: IN_SESSION (customer is present), OFF_SESSION (customer is not present).",
            "enum": [
              "IN_SESSION",
              "OFF_SESSION"
            ]
          }
        },
        "required": [
          "consentId",
          "payment",
          "status"
        ]
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
      "pispgateway.Payment": {
        "type": "object",
        "properties": {
          "currency": {
            "type": "string",
            "description": "Currency of the payment amount. Must be specified in ISO 4217 format."
          },
          "amount": {
            "type": "number",
            "description": "Payment amount",
            "example": "100.00"
          },
          "reference": {
            "type": "string",
            "description": "A reference used to unambiguously refer to the payment transaction. Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space."
          }
        },
        "required": [
          "currency",
          "reference"
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