---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Endpoint to mock the credit of an account

Inbound payments - mock (Sandbox only)

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
      "name": "Inbound Payments",
      "description": "Inbound payments"
    }
  ],
  "paths": {
    "/credit": {
      "post": {
        "tags": [
          "Inbound Payments"
        ],
        "summary": "Endpoint to mock the credit of an account",
        "description": "Inbound payments - mock (Sandbox only)",
        "operationId": "createPayments",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/inboundpayment.InboundPaymentRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/inboundpayment.MessageResponse"
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
      "inboundpayment.MessageResponse": {
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
      "inboundpayment.InboundPaymentRequest": {
        "type": "object",
        "description": "Details of credit to the account",
        "properties": {
          "accountId": {
            "type": "string",
            "description": "The account to be credited",
            "minLength": 1
          },
          "payerDetail": {
            "$ref": "#/components/schemas/inboundpayment.PartyDetailRequest",
            "description": "Payer details"
          },
          "payeeDetail": {
            "$ref": "#/components/schemas/inboundpayment.PartyDetailRequest",
            "description": "Payee details"
          },
          "description": {
            "type": "string",
            "description": "Description of the credit",
            "maxLength": 255,
            "minLength": 0
          },
          "amount": {
            "type": "number",
            "description": "Amount of the payment in major current Units - '1' = 1.00 GBP",
            "maximum": 2147483647,
            "minimum": 0.01
          },
          "type": {
            "type": "string",
            "description": " Type of credit, values: ",
            "enum": [
              "PI_BACS",
              "PI_DD",
              "PI_FAST",
              "PI_SECT",
              "PI_SEPA_INST",
              "PI_SWIFT"
            ],
            "minLength": 1
          },
          "transactionDate": {
            "type": "string",
            "description": "Date of credit in yyyy-MM-ddTHH:mm:ssZ format"
          },
          "numberOfTransactions": {
            "type": "integer",
            "format": "int32",
            "description": "Number of credit transactions to create, defaults to 1",
            "maximum": 50,
            "minimum": 1
          },
          "schemeInformation": {
            "$ref": "#/components/schemas/inboundpayment.SchemeInfoRequest",
            "description": "Optional scheme details"
          }
        },
        "required": [
          "accountId",
          "amount",
          "description",
          "payerDetail",
          "type"
        ]
      },
      "inboundpayment.Address": {
        "type": "object",
        "properties": {
          "addressLine1": {
            "type": "string"
          },
          "addressLine2": {
            "type": "string"
          },
          "postTown": {
            "type": "string"
          },
          "postCode": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        }
      },
      "inboundpayment.PartyDetailRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Party name"
          },
          "identifier": {
            "$ref": "#/components/schemas/inboundpayment.AccountIdentifierDetailRequest",
            "description": "Account identifier"
          },
          "address": {
            "$ref": "#/components/schemas/inboundpayment.Address",
            "description": "Party address"
          }
        },
        "required": [
          "identifier",
          "name"
        ]
      },
      "inboundpayment.SchemeInfoRequest": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "unique id that identifies a payment end-to-end within a scheme. If used ensure that its unique"
          }
        }
      },
      "inboundpayment.AccountIdentifierDetailRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Account identifier type",
            "enum": [
              "SCAN",
              "IBAN",
              "DD",
              "INTL",
              "ANBRN",
              "AN"
            ]
          },
          "accountNumber": {
            "type": "string",
            "description": "Account number"
          },
          "sortCode": {
            "type": "string",
            "description": "Sortcode"
          },
          "iban": {
            "type": "string",
            "description": "IBAN"
          },
          "bic": {
            "type": "string",
            "description": "BIC"
          }
        },
        "required": [
          "type"
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