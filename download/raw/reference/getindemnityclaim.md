---
updatedAt: 2026-06-30T10:07:37.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get an Indemnity Claim for a given id

Returns a singular Indemnity Claim based on the ID supplied in the path.

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
      "name": "Direct Debits",
      "description": "Direct Debit operations"
    }
  ],
  "paths": {
    "/indemnity-claims/{indemnityClaimId}": {
      "get": {
        "tags": [
          "Direct Debits"
        ],
        "summary": "Get an Indemnity Claim for a given id",
        "description": "Returns a singular Indemnity Claim based on the ID supplied in the path.",
        "operationId": "getIndemnityClaim",
        "parameters": [
          {
            "name": "indemnityClaimId",
            "in": "path",
            "description": "Id of the indemnityClaim",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/directdebit.IndemnityClaimResponse"
                }
              }
            }
          },
          "400": {
            "description": "Validation Errors",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/directdebit.MessageResponse"
                  }
                }
              }
            }
          },
          "404": {
            "description": "No Indemnity Claim found matching that ID",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/directdebit.MessageResponse"
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
      "directdebit.IndemnityClaimStatusHistoryResponse": {
        "type": "object",
        "properties": {
          "changeDate": {
            "type": "string",
            "format": "date"
          },
          "schemeId": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "NEW",
              "CANCELLED",
              "SETTLED"
            ]
          }
        }
      },
      "directdebit.IndemnityClaimDirectDebitResponse": {
        "type": "object",
        "properties": {
          "amount": {
            "type": "number"
          },
          "collectionDate": {
            "type": "string",
            "format": "date"
          },
          "collectionId": {
            "type": "string"
          }
        }
      },
      "directdebit.IndemnityClaimResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "accountBid": {
            "type": "string"
          },
          "serviceUserReference": {
            "type": "string"
          },
          "ddicReference": {
            "type": "string"
          },
          "reasonCode": {
            "type": "string",
            "enum": [
              "AMOUNT_OR_DATE_DIFFER",
              "NO_ADVANCE_NOTICE",
              "DDI_CANCELLED_BY_BANK",
              "DDI_CANCELLED_WITH_SERVICE_USER",
              "NO_INSTRUCTION",
              "INVALID_SIGNATURE",
              "SERVICE_USER_REQUEST",
              "SERVICE_USER_NAME_DISPUTED"
            ]
          },
          "amount": {
            "type": "number"
          },
          "payingBankName": {
            "type": "string"
          },
          "payingBankSortCode": {
            "type": "string"
          },
          "payingBankAccountNumber": {
            "type": "string"
          },
          "payingBankServiceUserNumber": {
            "type": "string"
          },
          "statusHistory": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/directdebit.IndemnityClaimStatusHistoryResponse"
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "NEW",
              "CANCELLED",
              "SETTLED"
            ]
          },
          "directDebits": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/directdebit.IndemnityClaimDirectDebitResponse"
            }
          }
        }
      },
      "directdebit.MessageResponse": {
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