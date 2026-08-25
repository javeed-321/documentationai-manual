---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get SRD Accounts

Returns a list of all sort codes and account numbers for which Secondary Reference Data must be provided with all account name check requests.

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
      "name": "Confirmation of Payee",
      "description": "Account Name Checks"
    }
  ],
  "paths": {
    "/account-name-check/srd-accounts": {
      "get": {
        "tags": [
          "Confirmation of Payee"
        ],
        "summary": "Get SRD Accounts",
        "description": "Returns a list of all sort codes and account numbers for which Secondary Reference Data must be provided with all account name check requests.",
        "operationId": "getSrdAccounts",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "Page to fetch (0 indexed)",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0,
              "minimum": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "Size of Page to fetch",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 500,
              "maximum": 500,
              "minimum": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved SRD list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/confirmationofpayee.CopPageResponseJsonSrdAccount"
                }
              }
            }
          },
          "400": {
            "description": "Invalid query params provided",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/confirmationofpayee.MessageResponse"
                  }
                }
              }
            }
          },
          "401": {
            "description": "Invalid credentials",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/confirmationofpayee.MessageResponse"
                  }
                }
              }
            }
          },
          "403": {
            "description": "CoP Access denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/confirmationofpayee.MessageResponse"
                  }
                }
              }
            }
          },
          "500": {
            "description": "Unexpected error occurred",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/confirmationofpayee.MessageResponse"
                  }
                }
              }
            }
          },
          "503": {
            "description": "Service outage",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/confirmationofpayee.MessageResponse"
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
      "confirmationofpayee.MessageResponse": {
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
      "confirmationofpayee.CopPageResponseJsonSrdAccount": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/confirmationofpayee.JsonSrdAccount"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Page size"
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total count"
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number, 0 based; i.e first-page = 0, second-page = 1"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total pages"
          }
        },
        "required": [
          "content",
          "page",
          "size",
          "totalPages",
          "totalSize"
        ]
      },
      "confirmationofpayee.JsonSrdAccount": {
        "type": "object",
        "properties": {
          "sortCode": {
            "type": "string",
            "description": "The sort code of one or more accounts that requires Secondary Reference Data to be provided when making account name check requests.\n",
            "example": "123456"
          },
          "accountNumbers": {
            "type": "array",
            "description": "Account numbers that require Secondary Reference Data. If empty, Secondary Reference Data is required for all name check requests for this sort code.",
            "items": {
              "type": "string",
              "description": "The account number of a specific account that requires Secondary Reference Data to be provided when making account name check requests.",
              "example": "11111111"
            }
          }
        },
        "required": [
          "sortCode"
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