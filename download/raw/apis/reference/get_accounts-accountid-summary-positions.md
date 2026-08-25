---
updatedAt: 2026-05-27T16:57:55.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# List Account Positions

Retrives a list of Account Positions by accountID

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
      "name": "Positions"
    }
  ],
  "paths": {
    "/accounts/{accountID}/summary/positions": {
      "get": {
        "tags": [
          "Positions"
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
        "summary": "List Account Positions",
        "description": "Retrives a list of Account Positions by accountID",
        "responses": {
          "200": {
            "description": "Retrieving an Account's Positions by accountID was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PositionsRes"
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
      "accountNo": {
        "type": "string",
        "example": "DWBG000052",
        "description": "The user's unique account number, that is human readable."
      },
      "tradingType": {
        "type": "string",
        "example": "CASH",
        "description": "The type of trading the account will participate in.",
        "enum": [
          "CASH",
          "MARGIN"
        ]
      },
      "instrumentSymbol": {
        "type": "string",
        "nullable": true,
        "example": "MS",
        "description": "The ticker symbol of the Instrument. Debt Instruments and Global Mutual Funds do not have symbols and are referred to buy their `instrumentID` or `ISIN`."
      },
      "instrumentISIN": {
        "description": "An `International Securities Identification Number` (ISIN) uniquely identifies a security. Its structure is defined in ISO 6166. ISINs are commonly used when an Instrument does not have a `symbol`, such as Debt Instruments and Global Mutual Funds.",
        "type": "string",
        "minLength": 12,
        "maxLength": 14,
        "example": "US023135BX34"
      },
      "instrumentType": {
        "type": "string",
        "example": "EQUITY",
        "description": "The classification of the instrument.",
        "enum": [
          "EQUITY",
          "ALTERNATIVE_ASSET",
          "MUTUAL_FUND",
          "DEBT",
          "OPTION",
          "CRYPTO"
        ]
      },
      "instrumentID": {
        "type": "string",
        "format": "uuid",
        "example": "3fb1e8a9-f7d5-4d90-95e2-43e7326b5636",
        "description": "A unique ID created by DriveWealth to identify a specific instrument."
      },
      "equityValue": {
        "type": "number",
        "format": "double",
        "example": 34275565.44,
        "description": "The current total market value of the account's open equity positions."
      },
      "optionsValue": {
        "type": "number",
        "format": "double",
        "example": 12345.67,
        "description": "The current total market value of the account's open option positions."
      },
      "debtValue": {
        "type": "number",
        "format": "double",
        "example": 12345.67,
        "description": "The current total market value of the account's open debt positions."
      },
      "positionsValue": {
        "type": "number",
        "format": "double",
        "example": 34287911.11,
        "description": "The current total market value of the account's open positions."
      },
      "equityPositionsObj": {
        "type": "object",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "instrumentID": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "openQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "Quantity of shares owned by the account."
          },
          "costBasis": {
            "type": "number",
            "example": 975.98,
            "description": "Cost basis of the position."
          },
          "marketValue": {
            "type": "number",
            "example": 4540.36,
            "description": "Current market value of the position."
          },
          "side": {
            "type": "string",
            "example": "B",
            "description": "In this case, Side distinguishes the type of position. This will always return 'long'(B).",
            "enum": [
              "B"
            ]
          },
          "priorClose": {
            "type": "number",
            "example": 144.29,
            "description": "The prior closing price of the security."
          },
          "availableForTradingQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "The quantity of the security available for sale."
          },
          "avgPrice": {
            "type": "number",
            "example": 30.84,
            "description": "The average price of the position."
          },
          "mktPrice": {
            "type": "number",
            "example": 143.45,
            "description": "The current market price of the position."
          },
          "unrealizedPL": {
            "type": "number",
            "example": 3564.38,
            "description": "Unrealized profit and loss for position."
          },
          "unrealizedDayPLPercent": {
            "type": "number",
            "example": -0.58,
            "description": "Unrealized day profit and loss for position in percent."
          },
          "unrealizedDayPL": {
            "type": "number",
            "example": -26.59,
            "description": "Unrealized day profit and loss for position."
          }
        }
      },
      "optionsPositionsObj": {
        "type": "object",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "instrumentID": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "openQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "Quantity of shares owned by the account."
          },
          "costBasis": {
            "type": "number",
            "example": 975.98,
            "description": "Cost basis of the position."
          },
          "marketValue": {
            "type": "number",
            "example": 4540.36,
            "description": "Current market value of the position."
          },
          "side": {
            "type": "string",
            "example": "B",
            "description": "In this case, Side distinguishes the type of position. This will always return 'long'(B).",
            "enum": [
              "B"
            ]
          },
          "priorClose": {
            "type": "number",
            "example": 144.29,
            "description": "The prior closing price of the security."
          },
          "availableForTradingQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "The quantity of the security available for sale."
          },
          "avgPrice": {
            "type": "number",
            "example": 30.84,
            "description": "The average price of the position."
          },
          "mktPrice": {
            "type": "number",
            "example": 440.75,
            "description": "The current market price of the position."
          },
          "unrealizedPL": {
            "type": "number",
            "example": 14.24,
            "description": "The unrealized profit and loss for the position."
          },
          "unrealizedDayPLPercent": {
            "type": "number",
            "example": 1.65,
            "description": "The unrealized day profit and loss for position in percent."
          },
          "unrealizedDayPL": {
            "type": "number",
            "example": 0.54,
            "description": "The unrealized day profit and loss for the position."
          }
        }
      },
      "mutualFundsPositionsObj": {
        "type": "object",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "instrumentID": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "openQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "Quantity of shares owned by the account."
          },
          "costBasis": {
            "type": "number",
            "example": 975.98,
            "description": "Cost basis of the position."
          },
          "marketValue": {
            "type": "number",
            "example": 4540.36,
            "description": "Current market value of the position."
          },
          "side": {
            "type": "string",
            "example": "B",
            "description": "In this case, Side distinguishes the type of position. This will always return 'long'(B).",
            "enum": [
              "B"
            ]
          },
          "priorClose": {
            "type": "number",
            "example": 144.29,
            "description": "The prior closing price of the security."
          },
          "availableForTradingQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "The quantity of the security available for sale."
          },
          "avgPrice": {
            "type": "number",
            "example": 30.84,
            "description": "The average price of the position."
          }
        }
      },
      "debtPositionsObj": {
        "type": "object",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "instrumentID": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "ISIN": {
            "$ref": "#/components/schemas/instrumentISIN"
          },
          "instrumentType": {
            "$ref": "#/components/schemas/instrumentType"
          },
          "openQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "Quantity of shares owned by the account."
          },
          "costBasis": {
            "type": "number",
            "example": 975.98,
            "description": "Cost basis of the position."
          },
          "marketValue": {
            "type": "number",
            "example": 4540.36,
            "description": "Current market value of the position."
          },
          "side": {
            "type": "string",
            "example": "B",
            "description": "In this case, Side distinguishes the type of position. This will always return 'long'(B).",
            "enum": [
              "B"
            ]
          },
          "priorClose": {
            "type": "number",
            "example": 144.29,
            "description": "The prior closing price of the security."
          },
          "availableForTradingQty": {
            "type": "number",
            "example": 31.65120151,
            "description": "The quantity of the security available for sale."
          },
          "avgPrice": {
            "type": "number",
            "example": 30.84,
            "description": "The average price of the position."
          },
          "unrealizedPL": {
            "type": "number",
            "example": 3564.38,
            "description": "Unrealized profit and loss for position."
          }
        }
      },
      "PositionsRes": {
        "type": "object",
        "properties": {
          "accountID": {
            "$ref": "#/components/schemas/accountID"
          },
          "accountNo": {
            "$ref": "#/components/schemas/accountNo"
          },
          "tradingType": {
            "$ref": "#/components/schemas/tradingType"
          },
          "updated": {
            "type": "string",
            "example": "2017-06-16T15:35:30.617Z",
            "description": "Time of last update."
          },
          "equityValue": {
            "$ref": "#/components/schemas/equityValue"
          },
          "optionsValue": {
            "$ref": "#/components/schemas/optionsValue"
          },
          "debtValue": {
            "$ref": "#/components/schemas/debtValue"
          },
          "positionsValue": {
            "$ref": "#/components/schemas/positionsValue"
          },
          "equityPositions": {
            "type": "array",
            "description": "An array of the positions in the account.",
            "items": {
              "$ref": "#/components/schemas/equityPositionsObj"
            }
          },
          "optionsPositions": {
            "type": "array",
            "description": "An array of the options positions in the account.",
            "items": {
              "$ref": "#/components/schemas/optionsPositionsObj"
            }
          },
          "mutualFundsPositions": {
            "type": "array",
            "description": "An array of the mutual funds positions in the account.",
            "items": {
              "$ref": "#/components/schemas/mutualFundsPositionsObj"
            }
          },
          "debtPositions": {
            "type": "array",
            "description": "An array of the debt positions in the account.",
            "items": {
              "$ref": "#/components/schemas/debtPositionsObj"
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