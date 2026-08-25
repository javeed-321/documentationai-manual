---
updatedAt: 2026-05-27T16:58:45.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create Autopilot Run

Create an Autopilot Run.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Advisor APIs",
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
      "name": "AutoPilot"
    }
  ],
  "paths": {
    "/managed/autopilot/{partnerID}": {
      "post": {
        "deprecated": true,
        "tags": [
          "AutoPilot"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "partnerID",
            "schema": {
              "type": "string"
            },
            "required": true,
            "example": "66304da9-3h6f-2234-935f-ac6b7933d706",
            "description": "This is the parentIBID or userID of the registered investment advisor."
          }
        ],
        "summary": "Create Autopilot Run",
        "description": "Create an Autopilot Run.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/autopilotReq"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Creating an Autopilot Run was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/autopilotRes"
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
      "riaID": {
        "type": "string",
        "example": "66304da9-3h6f-2234-935f-ac6b7933d706",
        "description": "This is the parentIBID or userID of the registered investment advisor creating the re-balance run."
      },
      "autopilotReq": {
        "type": "object",
        "required": [
          "reviewOnly",
          "forceRebalance"
        ],
        "properties": {
          "reviewOnly": {
            "type": "boolean",
            "example": true,
            "description": "True, if a review should occur without a forced rebalance."
          },
          "forceRebalance": {
            "type": "boolean",
            "example": true,
            "description": "True, if a forces rebalance should occur."
          },
          "subAccounts": {
            "type": "array",
            "description": "A list of user's accountIDs to be rebalanced.",
            "items": {
              "oneOf": [
                {
                  "$ref": "#/components/schemas/accountID"
                }
              ]
            }
          }
        }
      },
      "autopilotRes": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "ria_rebalance_ebf7e764-e2d6-4b3d-a333-b8ff05b92b89",
            "description": "The unique re-balance run identifier `rebalanceRunID` associated with a specific re-balance."
          },
          "created": {
            "type": "string",
            "example": "2022-12-27T06:06:28.955Z",
            "description": "A timestamp of when the re-balance run was created."
          },
          "status": {
            "type": "string",
            "example": "REBALANCE_NOT_STARTED",
            "description": "Status of the re-balance run. See [Autopilot Run Status](https://developer.drivewealth.com/reference/get-autopilot-run-status) for status values."
          },
          "riaID": {
            "$ref": "#/components/schemas/riaID"
          }
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