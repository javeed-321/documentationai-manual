---
updatedAt: 2026-05-27T16:58:08.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List Account Statements

Retrives a list of Account Statements by accountID.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Account Management APIs",
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
      "name": "Statements"
    }
  ],
  "paths": {
    "/accounts/{accountID}/statements": {
      "get": {
        "tags": [
          "Statements"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "accountID",
            "schema": {
              "$ref": "#/components/schemas/accountID"
            },
            "required": true
          }
        ],
        "summary": "List Account Statements",
        "description": "Retrives a list of Account Statements by accountID.",
        "responses": {
          "200": {
            "description": "Retrieving a list of Account Statements by accountID was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StatementListRes"
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
      "accountID": {
        "type": "string",
        "example": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
        "description": "The user's unique account identifier."
      },
      "statementObj": {
        "type": "object",
        "properties": {
          "displayName": {
            "type": "string",
            "example": "Apr 28, 2017 Statement",
            "description": "Description of account statement file."
          },
          "fileKey": {
            "type": "string",
            "example": "2017042802",
            "description": "Key to be used to retrieve account statement PDF. Reference [Get Statement File](https://developer.drivewealth.com/reference/get-statement-file) for retrieving an account statement."
          }
        }
      },
      "StatementListRes": {
        "type": "array",
        "description": "An array that holds the reference details to an accounts statements.",
        "items": {
          "oneOf": [
            {
              "$ref": "#/components/schemas/statementObj"
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