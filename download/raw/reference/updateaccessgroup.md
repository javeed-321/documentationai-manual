---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Update access group

The ability to update an access group's name and add or remove an account

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
      "name": "Access Group",
      "description": "Operations on Access Group"
    }
  ],
  "paths": {
    "/access-groups/{accessGroupId}/content": {
      "put": {
        "tags": [
          "Access Group"
        ],
        "summary": "Update access group",
        "description": "The ability to update an access group's name and add or remove an account",
        "operationId": "updateAccessGroup",
        "parameters": [
          {
            "name": "accessGroupId",
            "in": "path",
            "description": "Access group ID",
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
                "$ref": "#/components/schemas/account.AccessGroupRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/account.AccessGroupResponse"
                }
              }
            }
          },
          "400": {
            "description": "Validation errors",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/account.MessageResponse"
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
      "account.AccessGroupResponse": {
        "type": "object",
        "description": "AccessGroup",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique ID for the access group",
            "example": "G0000001"
          },
          "name": {
            "type": "string",
            "description": "Access group name"
          },
          "type": {
            "type": "string",
            "description": "The type of access group",
            "enum": [
              "SERVICE_PARTNER",
              "SERVICE_CUSTOMER",
              "DELEGATE",
              "USER_DEFINED"
            ]
          },
          "typeId": {
            "type": "string",
            "description": "The identifier of the linked entity implied by the type, e.g. the partner ID"
          },
          "status": {
            "type": "string",
            "description": "Status of the access group",
            "enum": [
              "ACTIVE",
              "DELETED"
            ]
          },
          "countOfAccounts": {
            "type": "integer",
            "format": "int64",
            "deprecated": true,
            "description": "The number of accounts in this group"
          }
        }
      },
      "account.AccessGroupRequest": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "description": "Action to apply for the supplied account bid",
            "enum": [
              "ADD",
              "REMOVE"
            ]
          },
          "accountIds": {
            "type": "array",
            "description": "Bids of the accounts to be added/removed",
            "items": {
              "type": "string"
            }
          },
          "beneficiaryIds": {
            "type": "array",
            "description": "Bids of the beneficiaries to be added/removed",
            "items": {
              "type": "string"
            }
          },
          "name": {
            "type": "string",
            "description": "The name of the account group to create. Must match: [\\w \\-]*",
            "maxLength": 50,
            "minLength": 0,
            "pattern": "[\\w \\-]*"
          }
        }
      },
      "account.MessageResponse": {
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