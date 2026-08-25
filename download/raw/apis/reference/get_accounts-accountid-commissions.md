---
updatedAt: 2026-05-27T16:57:55.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List Commission Schedules

Retrieves a list of Commissions Schedules by accountID.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Core APIs",
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
      "name": "Commission Schedules"
    }
  ],
  "paths": {
    "/accounts/{accountID}/commissions": {
      "get": {
        "tags": [
          "Commission Schedules"
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
        "summary": "List Commission Schedules",
        "description": "Retrieves a list of Commissions Schedules by accountID.",
        "responses": {
          "200": {
            "description": "Retrieving a list of Commissions Schedules was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CommissionsRes"
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
      "wlpID": {
        "type": "string",
        "example": "TTC",
        "description": "The wlpID is a deep backoffice ID that identifies each partner from each other."
      },
      "commissionID": {
        "type": "string",
        "example": "b3e985dd-9679-63dc-5dd5-9bd7982efecd",
        "description": "The unique identifier associated with a specific commission related to the account."
      },
      "assignmentCriteria": {
        "type": "object",
        "properties": {
          "wplID": {
            "$ref": "#/components/schemas/wlpID"
          },
          "countries": {
            "type": "string",
            "example": "USA",
            "description": "Clients from this country will be assigned this commission."
          },
          "defaultStatus": {
            "type": "boolean",
            "example": true,
            "description": "The default commission to be applied if no other criteria matches."
          },
          "accountMgmtType": {
            "type": "string",
            "example": null,
            "description": "NEEDS DESCRIPTION"
          }
        }
      },
      "ratesObject": {
        "type": "object",
        "properties": {
          "rate": {
            "type": "number",
            "example": 1.49,
            "description": "Commission rate in USD."
          },
          "passThroughFees": {
            "type": "boolean",
            "example": true,
            "description": "If true, SEC and TAF fees are passed through to the client."
          },
          "shareAmountRounding": {
            "type": "string",
            "example": "CEIL",
            "description": "Share amount rounding method. Options:`FLOOR` - Share quantity rounded down `CEIL` - Share quantity rounded up `NEAREST` - Share quantity rounded to nearest integer.",
            "enum": [
              "FLOOR",
              "CEIL",
              "NEAREST"
            ]
          },
          "minimumRate": {
            "type": "number",
            "example": 1.49,
            "description": "Minimum commission rate."
          }
        }
      },
      "CommissionsRes": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/CommissionObject"
        }
      },
      "CommissionObject": {
        "type": "object",
        "properties": {
          "active": {
            "type": "boolean",
            "example": true,
            "description": "Commission group status."
          },
          "commissionID": {
            "$ref": "#/components/schemas/commissionID"
          },
          "description": {
            "type": "string",
            "example": "Free",
            "description": "A short description about the commission."
          },
          "assignmentCriteria": {
            "$ref": "#/components/schemas/assignmentCriteria"
          },
          "rates": {
            "type": "object",
            "description": "This object contains the details of the commission rates.",
            "properties": {
              "fractional": {
                "type": "object",
                "description": "Object provides commission rates on order quantities between 0.0001 and 0.9999 (aka fractional shares).",
                "properties": {
                  "schema": {
                    "$ref": "#/components/schemas/ratesObject"
                  }
                }
              },
              "default": {
                "type": "object",
                "description": "Object provided commission rates on full share order quantities.",
                "properties": {
                  "schema": {
                    "$ref": "#/components/schemas/ratesObject"
                  }
                }
              }
            }
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