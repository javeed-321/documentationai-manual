---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get supported ASPSPs

Gets a list of all supported Account Servicing Payment Service Providers (ASPSPs).

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
    "/aspsps": {
      "get": {
        "tags": [
          "Payment Initiations"
        ],
        "summary": "Get supported ASPSPs",
        "description": "Gets a list of all supported Account Servicing Payment Service Providers (ASPSPs).",
        "operationId": "getAspsProviders",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/pispgateway.AspsProviderResponse"
                  }
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
      "pispgateway.AspsProviderResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier (within Modulr) of the ASPSP",
            "example": "H100000001"
          },
          "name": {
            "type": "string",
            "description": "Name of the ASPSP",
            "example": "Bank of Money"
          },
          "capabilities": {
            "type": "array",
            "description": "Capability list of the ASPSP",
            "items": {
              "$ref": "#/components/schemas/pispgateway.Capability"
            }
          }
        }
      },
      "pispgateway.Capability": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of the capability.",
            "enum": [
              "SINGLE_IMMEDIATE",
              "STANDING_ORDER",
              "SWEEPING_VRP",
              "COMMERCIAL_VRP"
            ],
            "example": "SINGLE_IMMEDIATE"
          },
          "status": {
            "type": "string",
            "description": "Status of the capability.",
            "enum": [
              "ENABLED",
              "DISABLED"
            ],
            "example": "ENABLED"
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