---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get a list of access groups

The ability to list all access groups for the customer

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
    "/access-groups": {
      "get": {
        "tags": [
          "Access Group"
        ],
        "summary": "Get a list of access groups",
        "description": "The ability to list all access groups for the customer",
        "operationId": "getAccessGroups",
        "parameters": [
          {
            "name": "ids",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "ID of access group(s) to fetch",
              "items": {
                "type": "string",
                "example": "G0000001"
              },
              "uniqueItems": true
            }
          },
          {
            "name": "types",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "Access group types",
              "items": {
                "type": "string",
                "description": "Access group type",
                "enum": [
                  "SERVICE_PARTNER",
                  "SERVICE_CUSTOMER",
                  "DELEGATE",
                  "USER_DEFINED"
                ]
              },
              "uniqueItems": true
            }
          },
          {
            "name": "statuses",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "Access group statuses",
              "items": {
                "type": "string",
                "description": "Access group status",
                "enum": [
                  "ACTIVE",
                  "DELETED"
                ]
              },
              "uniqueItems": true
            }
          },
          {
            "name": "typeIds",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "Ids of the entity implied by the type(s), e.g. the partner ID",
              "items": {
                "type": "string",
                "description": "Is of the entity implied by the type(s), e.g. the partner ID",
                "example": "C0000001"
              },
              "uniqueItems": true
            }
          },
          {
            "name": "accountIds",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "description": "Account BIDs of access groups to fetch",
              "items": {
                "type": "string",
                "description": "Account BID of access groups to fetch",
                "example": "A0000001"
              },
              "uniqueItems": true
            }
          },
          {
            "name": "accountIdSearchCriteria.matchMode",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "enum": [
                "ALL",
                "ANY"
              ]
            }
          },
          {
            "name": "accountIdSearchCriteria.value",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "object"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/account.AccessGroupResponse"
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