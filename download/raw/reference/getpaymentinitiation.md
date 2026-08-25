---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get payment initiation request details

Retrieve the details of a specific payment initiation request.

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
    "/payment-initiations/{paymentInitiationId}": {
      "get": {
        "tags": [
          "Payment Initiations"
        ],
        "summary": "Get payment initiation request details",
        "description": "Retrieve the details of a specific payment initiation request.",
        "operationId": "getPaymentInitiation",
        "parameters": [
          {
            "name": "paymentInitiationId",
            "in": "path",
            "description": "Payment initiation ID",
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
            "description": "Payment initiation found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/pispgateway.PaymentInitiationResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
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
          },
          "404": {
            "description": "Payment initiation not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/pispgateway.PaymentInitiationResponse"
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
      "pispgateway.Destination": {
        "type": "object",
        "description": "The destination account for the payment",
        "properties": {
          "type": {
            "type": "string",
            "description": "Indicates the type of destination. Can be one of ACCOUNT, SCAN",
            "enum": [
              "ACCOUNT",
              "SCAN"
            ]
          },
          "id": {
            "type": "string",
            "description": "Identifier of the destination account if using ACCOUNT type",
            "example": "A1100001"
          },
          "accountNumber": {
            "type": "string",
            "description": "Account Number of destination account if using SCAN type",
            "example": "12345678",
            "pattern": "^[0-9]{8}$"
          },
          "sortCode": {
            "type": "string",
            "description": "Sort Code of destination account if using SCAN type",
            "example": "000000",
            "pattern": "^[0-9]{6}$"
          },
          "name": {
            "type": "string",
            "description": "Name of destination account if using SCAN type (this may be truncated)",
            "example": "Test",
            "maxLength": 70,
            "minLength": 0
          }
        },
        "required": [
          "type"
        ]
      },
      "pispgateway.PaymentInitiationResponse": {
        "type": "object",
        "description": "Response object for Get Payment Initiation",
        "properties": {
          "id": {
            "type": "string",
            "description": "The identifier of the payment initiation",
            "example": "I000000001"
          },
          "status": {
            "type": "string",
            "description": "The status of the payment initiation, can be one of SUBMITTED, AWAITING_CONSENT, CONSENT_REJECTED, EXECUTED, ER_EXPIRED, ER_EXTSYS, ER_GENERAL",
            "example": "AWAITING_CONSENT"
          },
          "paymentAmount": {
            "$ref": "#/components/schemas/pispgateway.PaymentAmount",
            "description": "The payment amount"
          },
          "paymentReference": {
            "type": "string",
            "description": "The payment reference"
          },
          "destination": {
            "$ref": "#/components/schemas/pispgateway.Destination",
            "description": "The payment destination"
          },
          "aspspId": {
            "type": "string",
            "description": "The identifier of the ASPSP used for the payment",
            "example": "H100000001"
          },
          "aspspPaymentStatus": {
            "type": "string",
            "description": "The status of the payment at the ASPSP. When available, this is passed through from the ASPSP without modification.",
            "example": "AcceptedSettlementCompleted"
          }
        }
      },
      "pispgateway.PaymentAmount": {
        "type": "object",
        "description": "The amount of the payment",
        "properties": {
          "currency": {
            "type": "string",
            "description": "Currency of the account in ISO 4217 format. Only allowable value is GBP",
            "enum": [
              "GBP"
            ]
          },
          "value": {
            "type": "number",
            "description": "Amount of the payment in Major Currency Units - '1' = 1.00 GBP",
            "example": "100.00",
            "maximum": 2147483647,
            "minimum": 0.01
          }
        },
        "required": [
          "currency",
          "value"
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