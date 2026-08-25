---
updatedAt: 2026-05-27T16:58:23.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create ACATS Transfer

The Automated Customer Account Transfer Service (ACATS) is a system that facilitates the transfer of securities from one trading account to another at a different brokerage firm or bank.

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
      "name": "Asset Transfer"
    }
  ],
  "paths": {
    "/asset-transfers/acats": {
      "post": {
        "tags": [
          "Asset Transfer"
        ],
        "summary": "Create ACATS Transfer",
        "responses": {
          "200": {
            "description": "Initiating a transfer was successful",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ACATSTransferCreatedResponseModel"
                },
                "examples": {
                  "ACATS Transfer (Full)": {
                    "value": {
                      "id": "acats_41eb5bdd-8ce2-4471-8fc6-9892da089cd1",
                      "source": "BROKER0001",
                      "sourceAccountID": "d6a776bc-be5c-47df-94eb-baf914f1847c.1738660911962",
                      "destination": "DWXR001004",
                      "destinationAccountID": "c815c129-27cd-46f2-b316-ab6bde9aff62.1737384219426",
                      "clearingNo": "0001",
                      "status": {
                        "name": "PENDING",
                        "description": "Asset transfer request is pending"
                      },
                      "type": {
                        "name": "ACAT",
                        "description": "ACAT transfer"
                      },
                      "acatType": {
                        "name": "FULL",
                        "description": "Full Acats Transfer"
                      },
                      "acatTransit": {
                        "name": "ACAT_IN",
                        "description": "Incoming ACAT Transfer"
                      },
                      "sourceAccountType": {
                        "name": "INDIVIDUAL",
                        "description": "Individual Account"
                      },
                      "positions": [],
                      "metadata": {},
                      "auditDetails": [
                        {
                          "timestamp": "2023-07-28T23:56:10.507Z",
                          "status": {
                            "name": "STARTED",
                            "description": "Asset transfer request has been initiated."
                          },
                          "comment": "Transfer request has been submitted in queue"
                        },
                        {
                          "timestamp": "2023-07-28T23:56:10.645Z",
                          "status": {
                            "name": "PENDING",
                            "description": "Asset transfer request is pending"
                          },
                          "comment": "<string>"
                        }
                      ],
                      "created": "2023-07-28T23:56:10.491Z",
                      "updated": "2023-07-28T23:56:10.667Z"
                    }
                  },
                  "ACATS Transfer (Partial)": {
                    "value": {
                      "id": "acats_45dc50ac-3daa-484d-98cb-5264abb51d86",
                      "source": "FOLIO123",
                      "sourceAccountID": "d6a776bc-be5c-47df-94eb-baf914f1847c.1738660911962",
                      "destination": "DWKN000094",
                      "destinationAccountID": "c815c129-27cd-46f2-b316-ab6bde9aff62.1737384219426",
                      "clearingNo": "0001",
                      "status": {
                        "name": "STARTED",
                        "description": "Asset transfer request has been initiated."
                      },
                      "acatType": {
                        "name": "PARTIAL",
                        "description": "Partial Acats Transfer"
                      },
                      "sourceAccountType": {
                        "name": "INDIVIDUAL",
                        "description": "Individual Account"
                      },
                      "cash": 10,
                      "positions": [
                        {
                          "symbol": "META",
                          "instrumentID": "4312a85c-93ba-4adb-b50d-cc7973243a53",
                          "quantity": 1
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseModel"
                },
                "examples": {
                  "Invalid accountNo on request body": {
                    "value": {
                      "errorCode": "A012",
                      "message": "A required accountNo is missing or invalid. Refer to the API documentation for details.",
                      "errorDetails": {
                        "field": "destination",
                        "type": "STRING"
                      }
                    }
                  },
                  "Source and Destination are same": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details. Details: Source can't be DW account"
                    }
                  },
                  "Destination account is not approved": {
                    "value": {
                      "errorCode": "T005",
                      "message": "ACAT Transfer cannot initiate. Destination account is not approved."
                    }
                  },
                  "Invalid Symbol": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details. Details: Symbol is not active or invalid.",
                      "errorDetails": {
                        "field": "positions.symbol",
                        "type": "ARRAY"
                      }
                    }
                  },
                  "Invalid clearing broker": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details.",
                      "errorDetails": {
                        "detail": "Refer supported DTCC Broker list on API documentation. ",
                        "field": "brokerCode",
                        "type": "STRING"
                      }
                    }
                  },
                  "Cash Should be Greater Than 0 400 Bad": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details.",
                      "errorDetails": {
                        "detail": "cash should greater than 0",
                        "field": "cash",
                        "type": "DECIMAL"
                      }
                    }
                  },
                  "Invalid Symbol in Partial Acats Transfer 400 Bad": {
                    "value": {
                      "errorCode": "I019",
                      "message": "Invalid symbol(s) in the request body.",
                      "errorDetails": {
                        "detail": "Invalid value for AMZ",
                        "field": "positions.symbol",
                        "type": "STRING"
                      }
                    }
                  },
                  "Positions Required on Partial Acat Transfer 400 Bad": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details.",
                      "errorDetails": {
                        "field": "positions",
                        "type": "OBJECT"
                      }
                    }
                  },
                  "Acat Type is Missing 400 Bad": {
                    "value": {
                      "errorCode": "E032",
                      "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details.",
                      "errorDetails": {
                        "detail": "PARTIAL, FULL",
                        "field": "type",
                        "type": "ENUM"
                      }
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseModel"
                },
                "examples": {
                  "ACAT Transfer permission has been denied": {
                    "value": {
                      "errorCode": "P075",
                      "message": "User does not have permissions to perform this operation. Contact your administrator. Forbidden: Create ACATS transfer"
                    }
                  }
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AcatsCreateRequestModel"
              },
              "examples": {
                "ACAT Partial": {
                  "value": {
                    "sourceAccountType": "INDIVIDUAL",
                    "acatType": "PARTIAL",
                    "source": "ContraBroker001",
                    "destination": "LKKZ000004",
                    "comment": "Hey! Welcome to DriveWealth Developer Docs!",
                    "metadata": {
                      "myCustomKey": "myCustomValue"
                    },
                    "clearingNo": "0001",
                    "cash": 0,
                    "positions": [
                      {
                        "symbol": "MS",
                        "instrumentID": "3fb1e8a9-f7d5-4d90-95e2-43e7326b5636",
                        "quantity": 1
                      }
                    ]
                  }
                },
                "ACAT Cash Partial": {
                  "value": {
                    "sourceAccountType": "INDIVIDUAL",
                    "acatType": "PARTIAL",
                    "source": "ContraBroker001",
                    "destination": "LKKZ000004",
                    "comment": "Hey! Welcome to DriveWealth Developer Docs!",
                    "metadata": {
                      "myCustomKey": "myCustomValue"
                    },
                    "clearingNo": "0001",
                    "cash": 10000
                  }
                },
                "ACAT Full": {
                  "value": {
                    "sourceAccountType": "INDIVIDUAL",
                    "acatType": "FULL",
                    "source": "ContraBroker001",
                    "destination": "LKKZ000004",
                    "comment": "Hey! Welcome to DriveWealth Developer Docs!",
                    "metadata": {
                      "myCustomKey": "myCustomValue"
                    },
                    "clearingNo": "0001"
                  }
                }
              }
            }
          }
        },
        "description": "The Automated Customer Account Transfer Service (ACATS) is a system that facilitates the transfer of securities from one trading account to another at a different brokerage firm or bank."
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorCode": {
        "type": "string",
        "description": "The error code that is returned when an error occurs.",
        "example": "E032"
      },
      "ErrorCodeMessage": {
        "type": "string",
        "description": "The error message that is returned when an error occurs."
      },
      "ErrorDetails": {
        "type": "object",
        "properties": {
          "field": {
            "type": "string",
            "description": "JSON field name from the request body that caused an error"
          },
          "type": {
            "type": "string",
            "enum": [
              "STRING",
              "ARRAY",
              "INT",
              "DECIMAL",
              "BOOL",
              "TEXT",
              "UUID",
              "DATE",
              "MAP",
              "OBJECT"
            ],
            "description": "Expected data type of the field"
          },
          "allowedValues": {
            "type": "string",
            "description": "Example values which are allowed in the field"
          }
        }
      },
      "ErrorResponseModel": {
        "type": "object",
        "description": "The error response model that is returned when an error occurs.",
        "required": [
          "errorCode",
          "message"
        ],
        "properties": {
          "errorCode": {
            "$ref": "#/components/schemas/ErrorCode"
          },
          "message": {
            "$ref": "#/components/schemas/ErrorCodeMessage"
          },
          "errorDetails": {
            "$ref": "#/components/schemas/ErrorDetails"
          }
        }
      },
      "accountNo": {
        "type": "string",
        "example": "DWBG000052",
        "description": "The user's unique account number, that is human readable."
      },
      "sourceAccountID": {
        "type": "string",
        "example": "d6a776bc-be5c-47df-94eb-baf914f1847c.1738660911962",
        "description": "It's a unique source account id, that is human readable."
      },
      "destinationAccountID": {
        "type": "string",
        "example": "c815c129-27cd-46f2-b316-ab6bde9aff62.1737384219426",
        "description": "It's a unique destination account id, that is human readable."
      },
      "note": {
        "type": "string",
        "example": "Hey! Welcome to DriveWealth Developer Docs!",
        "description": "A way to store a message/comment on the this object."
      },
      "instrumentSymbol": {
        "type": "string",
        "nullable": true,
        "example": "MS",
        "description": "The ticker symbol of the Instrument. Debt Instruments and Global Mutual Funds do not have symbols and are referred to buy their `instrumentID` or `ISIN`."
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
      "metadata": {
        "type": "object",
        "example": {
          "myCustomKey": "myCustomValue"
        },
        "description": "The metadata object allows for creating a maximum of 5 keys (max 36 characters) and each value cannot exceed more than 128 bytes."
      },
      "AssetTransferStatus": {
        "type": "string",
        "enum": [
          "STARTED",
          "PENDING",
          "FAILED",
          "SUCCESSFUL",
          "ON_HOLD"
        ]
      },
      "GenericTransferRequest": {
        "type": "object",
        "properties": {
          "source": {
            "$ref": "#/components/schemas/accountNo"
          },
          "destination": {
            "type": "string",
            "description": "The DriveWealth destination account number where all assets will be transferred to.",
            "example": "LKKZ000004"
          },
          "comment": {
            "$ref": "#/components/schemas/note"
          },
          "metadata": {
            "$ref": "#/components/schemas/metadata"
          }
        }
      },
      "AcatsCreateRequestModelWithoutEnums": {
        "type": "object",
        "properties": {
          "clearingNo": {
            "$ref": "#/components/schemas/ClearingNo"
          },
          "cash": {
            "type": "number",
            "description": "The amount of cash to be moved from the source account.",
            "default": 0
          },
          "positions": {
            "type": "array",
            "minItems": 0,
            "description": "The positions to be moved from the source account to the destination account.",
            "items": {
              "$ref": "#/components/schemas/AcatPositionModel"
            }
          }
        }
      },
      "AcatsTransferEnumValues_SourceAccountType": {
        "type": "string",
        "description": "The type of account the sources account is. If TRUMP_ACCOUNT is selected, The acatType can only be FULL.",
        "enum": [
          "INDIVIDUAL",
          "CORPORATE",
          "JOINT",
          "CUSTODIAL",
          "IRA",
          "RIA_MANAGED",
          "TRUMP_ACCOUNT"
        ]
      },
      "ClearingNo": {
        "type": "string",
        "example": "0001",
        "description": "The DTCC clearing number of the broker. Refer DTCC broker API to fetch full supported list.",
        "minLength": 1,
        "maxLength": 4,
        "externalDocs": {
          "description": "DTCC Broker API",
          "url": "https://developer.drivewealth.com/apis/reference/get_asset-transfers-acats-brokers"
        }
      },
      "AcatsType": {
        "type": "string",
        "description": "The type of ACAT transfer to be performed.",
        "enum": [
          "FULL",
          "PARTIAL"
        ]
      },
      "AcatsTransitType": {
        "type": "string",
        "description": "The transit type of ACAT transfer to be performed.",
        "enum": [
          "ACAT_IN",
          "ACAT_OUT"
        ]
      },
      "AcatsCreateRequestModel": {
        "type": "object",
        "title": "AcatsRequestModel",
        "description": "ACAT Request model",
        "allOf": [
          {
            "$ref": "#/components/schemas/GenericTransferRequest"
          },
          {
            "$ref": "#/components/schemas/AcatsCreateRequestModelWithoutEnums",
            "allOf": [
              {
                "properties": {
                  "acatType": {
                    "$ref": "#/components/schemas/AcatsType"
                  }
                }
              }
            ]
          }
        ],
        "properties": {
          "sourceAccountType": {
            "$ref": "#/components/schemas/AcatsTransferEnumValues_SourceAccountType"
          },
          "acatType": {
            "$ref": "#/components/schemas/AcatsType"
          }
        },
        "required": [
          "source",
          "destination",
          "clearingNo",
          "acatType"
        ]
      },
      "ACATSTransferCreatedResponseModel": {
        "type": "object",
        "properties": {
          "source": {
            "$ref": "#/components/schemas/accountNo",
            "type": "string",
            "description": "The account number of the account on contra broker.",
            "example": "DTCCBROKER1"
          },
          "sourceAccountID": {
            "$ref": "#/components/schemas/sourceAccountID"
          },
          "destination": {
            "$ref": "#/components/schemas/accountNo",
            "type": "string",
            "description": "The DriveWealth destination account number where all assets will be transferred.",
            "example": "LKKZ000004"
          },
          "destinationAccountID": {
            "$ref": "#/components/schemas/destinationAccountID"
          },
          "clearingNo": {
            "$ref": "#/components/schemas/ClearingNo"
          },
          "sourceAccountType": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/AcatsTransferEnumValues_SourceAccountType"
              },
              "description": {
                "type": "string"
              }
            }
          },
          "acatType": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/AcatsType"
              },
              "description": {
                "type": "string"
              }
            }
          },
          "acatTransit": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/AcatsTransitType"
              },
              "description": {
                "type": "string"
              }
            }
          },
          "positions": {
            "$ref": "#/components/schemas/AcatPositionResponseModel"
          },
          "metadata": {
            "$ref": "#/components/schemas/metadata"
          },
          "auditDetails": {
            "type": "array",
            "description": "Audit of Transfer status changes",
            "anyOf": [
              {
                "$ref": "#/components/schemas/AuditDetails"
              }
            ]
          }
        },
        "required": [
          "source",
          "destination",
          "clearingNo",
          "acatType",
          "acatTransit",
          "auditDetails"
        ]
      },
      "AcatPositionModel": {
        "title": "AcatPosition",
        "type": "object",
        "description": "Position Model. Symbol or InstrumentID is required.",
        "properties": {
          "symbol": {
            "$ref": "#/components/schemas/instrumentSymbol"
          },
          "instrumentID": {
            "$ref": "#/components/schemas/instrumentID"
          },
          "quantity": {
            "type": "number",
            "description": "The quantity of shares to be transferred. Assets that are moving to or from an account outside of DriveWealth, can only be whole shares.",
            "minimum": 1
          }
        },
        "required": [
          "quantity"
        ]
      },
      "AcatPositionResponseModel": {
        "type": "array",
        "description": "The positions to be moved from the source account to the destination account.",
        "allOf": [
          {
            "$ref": "#/components/schemas/AcatPositionModel"
          },
          {
            "$ref": "#/components/schemas/instrumentType"
          }
        ]
      },
      "AuditDetails": {
        "type": "object",
        "properties": {
          "status": {
            "$ref": "#/components/schemas/AssetTransferStatus"
          },
          "comment": {
            "$ref": "#/components/schemas/note"
          },
          "updatedBy": {
            "type": "string",
            "description": "The user who updated the status."
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Status update timestamp",
            "example": "2022-12-22T06:07:41Z"
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