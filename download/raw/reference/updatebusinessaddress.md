---
updatedAt: 2026-08-12T11:47:55.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create or Update a business address for an Onboarding Application

Creates or updates a business address, of type REGISTERED or TRADING, for the business linked to the specified application.

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
    "/applications/{applicationId}/compliance/businesses/{businessId}/addresses": {
      "put": {
        "tags": [
          "Customers"
        ],
        "summary": "Create or Update a business address for an Onboarding Application",
        "description": "Creates or updates a business address, of type REGISTERED or TRADING, for the business linked to the specified application.",
        "operationId": "updateBusinessAddress",
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
          },
          {
            "name": "businessId",
            "in": "path",
            "description": "ID of business",
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
                "$ref": "#/components/schemas/customercompliance.BusinessAddressRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "No Content"
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
          },
          "404": {
            "description": "Not Found"
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
      "customercompliance.BusinessAddressRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Business address type",
            "enum": [
              "REGISTERED",
              "TRADING"
            ]
          },
          "address": {
            "$ref": "#/components/schemas/customercompliance.AddressRequest",
            "description": "Business address"
          }
        },
        "required": [
          "address",
          "type"
        ]
      },
      "customercompliance.AddressRequest": {
        "type": "object",
        "properties": {
          "addressLine1": {
            "type": "string",
            "description": "Address line 1",
            "minLength": 1
          },
          "addressLine2": {
            "type": "string",
            "description": "Address line 2"
          },
          "country": {
            "type": "string",
            "description": "Country alpha2 code",
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "description": "Post code",
            "minLength": 1
          },
          "postTown": {
            "type": "string",
            "description": "Post town",
            "minLength": 1
          }
        },
        "required": [
          "addressLine1",
          "country",
          "postCode",
          "postTown"
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