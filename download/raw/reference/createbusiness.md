---
updatedAt: 2026-08-05T15:17:38.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Add a business entity to an Onboarding Application

Creates a new business entity with a unique identifier to the specified application, capturing key details such as business name, type and company registration number.

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
    "/applications/{applicationId}/compliance/businesses": {
      "post": {
        "tags": [
          "Customers"
        ],
        "summary": "Add a business entity to an Onboarding Application",
        "description": "Creates a new business entity with a unique identifier to the specified application, capturing key details such as business name, type and company registration number.",
        "operationId": "createBusiness",
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
                "$ref": "#/components/schemas/customercompliance.BusinessRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/customercompliance.CreateBusinessResponse"
                }
              }
            }
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
            "description": "Incorrect permissions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/customercompliance.CreateBusinessResponse"
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
      "customercompliance.CreateBusinessResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Business ID"
          }
        }
      },
      "customercompliance.BusinessRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Business type",
            "enum": [
              "LLC",
              "PLC",
              "LLP",
              "PARTNERSHIP",
              "SOLETRADER"
            ]
          },
          "registeredName": {
            "type": "string",
            "description": "Registered business name",
            "maxLength": 100,
            "minLength": 0
          },
          "registrationNumber": {
            "type": "string",
            "description": "Company registration number",
            "maxLength": 40,
            "minLength": 0
          }
        },
        "required": [
          "registeredName",
          "type"
        ]
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