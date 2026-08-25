---
updatedAt: 2026-05-29T12:45:51.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create or Update Know Your Customer Data for a Customer Application

Creates or updates the Know Your Customer data for the specified application, including expected transaction values,  expected transaction volumes or trading name, incorporation date, business activities for business entities only.

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
      "name": "Customers",
      "description": "Operations on Customers"
    }
  ],
  "paths": {
    "/applications/{applicationId}/compliance/know-your-customer": {
      "put": {
        "tags": [
          "Customers"
        ],
        "summary": "Create or Update Know Your Customer Data for a Customer Application",
        "description": "Creates or updates the Know Your Customer data for the specified application, including expected transaction values,  expected transaction volumes or trading name, incorporation date, business activities for business entities only.",
        "operationId": "updateKnowYourCustomerByApplicationId",
        "parameters": [
          {
            "name": "applicationId",
            "in": "path",
            "description": "ID of application",
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
                "$ref": "#/components/schemas/customercompliance.KnowYourCustomer"
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
            "description": "Invalid Parameters",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/customercompliance.MessageResponse"
                  }
                }
              }
            }
          },
          "403": {
            "description": "Incorrect permissions"
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
      "customercompliance.KnowYourCustomer": {
        "type": "object",
        "properties": {
          "tradingName": {
            "type": "string",
            "description": "The trading name of the business"
          },
          "incorporationDate": {
            "type": "string",
            "format": "date",
            "description": "Incorporation Date of the business"
          },
          "businessActivities": {
            "type": "string",
            "description": "The business activities of the business"
          },
          "onlinePresenceUrl": {
            "type": "string",
            "description": "The online presence URL of the business"
          },
          "expectedMonthlyTransactions": {
            "type": "integer",
            "format": "int64",
            "description": "Expected Monthly Transactions of the business"
          },
          "expectedMonthlySpend": {
            "type": "integer",
            "format": "int64",
            "description": "Expected Monthly Spend of the business"
          },
          "industryCode": {
            "type": "string",
            "description": "The industry code of the business",
            "maxLength": 6,
            "minLength": 0
          }
        }
      },
      "customercompliance.MessageResponse": {
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