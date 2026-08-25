---
updatedAt: 2026-05-27T16:58:23.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List User Linked Bank Accounts

Retrieves a list of User Linked Bank Accounts by userID.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Money Movement APIs",
    "version": "2026-08-25",
    "contact": {
      "email": "producteng@drivewealth.tech"
    }
  },
  "servers": [
    {
      "url": "https://bo-api.drivewealth.io/back-office",
      "description": "Sandbox (No Real World Financial/Trading Impact)"
    },
    {
      "url": "https://bo-api.drivewealth.net/back-office",
      "description": "Production"
    }
  ],
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "headers": [
      {
        "key": "dw-client-app-key",
        "value": "{{yourAppKey}}"
      }
    ]
  },
  "tags": [
    {
      "name": "Linked Bank Accounts"
    }
  ],
  "paths": {
    "/users/{userID}/bank-accounts": {
      "get": {
        "tags": [
          "Linked Bank Accounts"
        ],
        "summary": "List User Linked Bank Accounts",
        "description": "Retrieves a list of User Linked Bank Accounts by userID.",
        "parameters": [
          {
            "in": "path",
            "name": "userID",
            "schema": {
              "type": "string"
            },
            "required": true,
            "example": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
            "description": "Unique ID of the User to fetch their stored bank accounts."
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieving a list of User Linked Bank Accounts was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BankAccountsArray"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "bankAccountID": {
        "type": "string",
        "example": "bank_a4656e60-321e-425b-aa0d-a2e75c38885f",
        "description": "The unique DriveWealth identifier that identifies each linked bank account."
      },
      "created": {
        "type": "string",
        "example": "2022-12-11T22:28:21.810Z",
        "description": ""
      },
      "updated": {
        "type": "string",
        "example": "2022-12-11T22:28:21.810Z",
        "description": ""
      },
      "bankAccountNickName": {
        "type": "string",
        "example": "PREFERRED CHECKING",
        "description": "The linked bank account nickname defined by the user."
      },
      "bankRoutingNumber": {
        "type": "string",
        "example": "110000000",
        "description": "The routing number of the user's external bank."
      },
      "bankAccountNumberLastFour": {
        "type": "string",
        "example": "****3174",
        "description": "The last four digits of the user's external bank account number."
      },
      "bankAccountStatus": {
        "type": "string",
        "example": "ACTIVE",
        "description": "The current status of the user's external linked bank account.",
        "enum": [
          "ACTIVE",
          "DELETED",
          "DISABLED"
        ]
      },
      "BankAccount": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/bankAccountID"
          },
          "bankAccountDetails": {
            "type": "object",
            "properties": {
              "bankAccountNickName": {
                "$ref": "#/components/schemas/bankAccountNickName"
              },
              "bankAccountNumber": {
                "$ref": "#/components/schemas/bankAccountNumberLastFour"
              },
              "bankRoutingNumber": {
                "$ref": "#/components/schemas/bankRoutingNumber"
              }
            }
          },
          "default": {
            "type": "string",
            "example": true,
            "description": "True, if this is the default bank account set by the customer."
          },
          "status": {
            "$ref": "#/components/schemas/bankAccountStatus"
          },
          "created": {
            "$ref": "#/components/schemas/created",
            "description": "The date and time the User's bank account was linked."
          },
          "updated": {
            "$ref": "#/components/schemas/updated",
            "description": "The date and time the User's bank account was updated."
          }
        }
      },
      "BankAccountsArray": {
        "type": "array",
        "description": "A list of all the User's linked bank accounts.",
        "items": {
          "oneOf": [
            {
              "$ref": "#/components/schemas/BankAccount"
            }
          ]
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  }
}
```