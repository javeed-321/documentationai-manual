---
updatedAt: 2026-05-27T16:57:55.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create User

Creates a User.

A user on the DriveWealth platform can represent one of the following:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **Individual**
      </td>

      <td style={{ textAlign: "left" }}>
        An individual user represents your customer, who is accessing an investment product with their own funds and assets.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Partner**
      </td>

      <td style={{ textAlign: "left" }}>
        A partner is an organization that interfaces with DriveWealth. DriveWealth provides brokerage services to help firms fulfill the needs of their individual customers.

        Each Partner is also represented by a single User entity, and is created by DriveWealth.
      </td>
    </tr>
  </tbody>
</Table>

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
      "name": "Users"
    }
  ],
  "paths": {
    "/users": {
      "post": {
        "tags": [
          "Users"
        ],
        "summary": "Create User",
        "description": "Creates a User.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UsersReq"
              },
              "examples": {
                "Create US Minor": {
                  "summary": "Beneficiary (minor) user creation",
                  "value": {
                    "username": "test.minor.1780922144",
                    "password": "********",
                    "userType": "BENEFICIARY",
                    "documents": [
                      {
                        "type": "BASIC_INFO",
                        "data": {
                          "firstName": "minor",
                          "lastName": "teen",
                          "country": "USA"
                        }
                      },
                      {
                        "type": "PERSONAL_INFO",
                        "data": {
                          "birthDay": 3,
                          "birthMonth": 12,
                          "birthYear": 2025
                        }
                      },
                      {
                        "type": "IDENTIFICATION_INFO",
                        "data": {
                          "value": "***-**-****",
                          "type": "SSN",
                          "citizenship": "USA"
                        }
                      },
                      {
                        "type": "ADDRESS_INFO",
                        "data": {
                          "street1": "123 Main St",
                          "city": "Chatham",
                          "province": "NJ",
                          "postalCode": "09812",
                          "country": "USA"
                        }
                      }
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Creating a User was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - validation error in the request payload.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseModel"
                },
                "examples": {
                  "Validation Error": {
                    "value": {
                      "errorCode": "E025",
                      "message": "Invalid or badly formatted request. Refer to the API documentation for details."
                    }
                  }
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
      "userID": {
        "type": "string",
        "example": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
        "description": "A unique identifier created for each User on DriveWealth's platform."
      },
      "userType": {
        "type": "string",
        "example": "INDIVIDUAL_TRADER",
        "description": "The type of user being onboarded.",
        "enum": [
          "INDIVIDUAL_TRADER",
          "CUSTODIAL",
          "BENEFICIARY"
        ]
      },
      "firstName": {
        "type": "string",
        "example": "Justin",
        "description": "The first name of the user."
      },
      "lastName": {
        "type": "string",
        "example": "Smith",
        "description": "The last (family) name of the user."
      },
      "email": {
        "type": "string",
        "example": "jj@drivewealth.dev",
        "description": "The user's email address."
      },
      "wlpID": {
        "type": "string",
        "example": "TTC",
        "description": "The wlpID is a deep backoffice ID that identifies each partner from each other."
      },
      "walletSettlementProfileID": {
        "type": "string",
        "example": "bank-profile-1",
        "description": "The walletSettlementProfileID is a identifier that denotes a user's wallet settlement profile for eligible partners."
      },
      "parentIBID": {
        "type": "string",
        "example": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
        "description": "The unique identifier of the firm."
      },
      "date": {
        "type": "string",
        "example": "2022-12-25",
        "description": ""
      },
      "phoneNumber": {
        "type": "string",
        "example": "18004612680",
        "description": "The phone number of the user."
      },
      "userTaxID": {
        "type": "string",
        "example": "1223334444",
        "description": "The user's national identification number or tax identification number."
      },
      "userTaxIDType": {
        "type": "string",
        "example": "SSN",
        "description": "The type of national identification number or tax identification number. **Note:** `FTNLO` is deprecated and should not be used for new integrations.",
        "enum": [
          "SSN",
          "EIN",
          "FTIN",
          "PASSPORT",
          "ALIEN_ID",
          "OTHER"
        ]
      },
      "userCountry": {
        "type": "string",
        "example": "USA",
        "description": "The user's country."
      },
      "userMaritalStatus": {
        "type": "string",
        "example": "SINGLE",
        "description": "The marital status of the user.",
        "enum": [
          "SINGLE",
          "DIVORCED",
          "MARRIED",
          "WIDOWED",
          "PARTNER"
        ]
      },
      "userStreet1": {
        "type": "string",
        "example": "15 Exchange Place",
        "description": "The user's current street address, where they live."
      },
      "userStreet2": {
        "type": "string",
        "example": "Suite 1000",
        "description": "The user's additional details of an address i.e. an apartment number."
      },
      "userCity": {
        "type": "string",
        "example": "Jersey City",
        "description": "The user's current city, where they live."
      },
      "userProvince": {
        "type": "string",
        "example": "NJ",
        "description": "The user's current state/province/territory, where they live."
      },
      "userPostalCode": {
        "type": "string",
        "example": 7302,
        "description": "The user's current postal code (zip code), where they live."
      },
      "userStatus": {
        "type": "string",
        "example": "PENDING",
        "description": "The user's current status.",
        "enum": [
          "PENDING",
          "APPROVED"
        ]
      },
      "firmName": {
        "type": "string",
        "example": "Tendies Trading Company",
        "description": "The firm name."
      },
      "investmentSuitability": {
        "type": "object",
        "properties": {
          "experience": {
            "type": "string",
            "example": "LIMITED",
            "description": "Trading experience level.",
            "enum": [
              "LIMITED",
              "NONE",
              "GOOD",
              "EXCELLENT"
            ]
          },
          "years": {
            "type": "string",
            "example": "YRS_10_PLUS",
            "description": "Number of years equity trading experience.",
            "enum": [
              "YRS_1_LESS",
              "YRS_1_2",
              "YRS_3_5",
              "YRS_6_9",
              "YRS_10_PLUS"
            ]
          },
          "tradesPerYear": {
            "type": "string",
            "example": "YRS_10_14",
            "description": "Total number of trades per year.",
            "enum": [
              "YRS_0_9",
              "YRS_10_14",
              "YRS_15_24",
              "YRS_25_74",
              "YRS_75_PLUS"
            ]
          },
          "averageTradeSize": {
            "type": "string",
            "example": "AVG_0_9999",
            "description": "Average per trade size.",
            "enum": [
              "AVG_0_9999",
              "AVG_10000_24999",
              "AVG_25000_PLUS"
            ]
          }
        }
      },
      "investmentSuitabilityCommon": {
        "type": "object",
        "properties": {
          "knowledge": {
            "type": "string",
            "example": "LIMITED",
            "description": "Trading experience level.",
            "enum": [
              "LIMITED",
              "NONE",
              "GOOD",
              "EXCELLENT"
            ]
          },
          "yearsOfExperience": {
            "type": "number",
            "example": 10,
            "description": "Number of years of trading experience."
          },
          "tradesPerYear": {
            "type": "number",
            "example": 50,
            "description": "Total number of trades per year."
          },
          "averageTradeValue": {
            "type": "number",
            "example": 150.31,
            "description": "Average USD value per trade."
          }
        }
      },
      "investmentSuitabilityEquities": {
        "type": "object",
        "allOf": [
          {
            "$ref": "#/components/schemas/investmentSuitabilityCommon"
          },
          {
            "type": "object",
            "properties": {
              "transactionTypes": {
                "type": "array",
                "description": "The types of transactions the user has experience with.",
                "items": {
                  "type": "string",
                  "enum": [
                    "LONG",
                    "SHORT",
                    "MARGIN"
                  ]
                },
                "example": [
                  "LONG",
                  "MARGIN"
                ]
              }
            }
          }
        ]
      },
      "investmentSuitabilityOptions": {
        "type": "object",
        "allOf": [
          {
            "$ref": "#/components/schemas/investmentSuitabilityCommon"
          },
          {
            "type": "object",
            "properties": {
              "transactionTypes": {
                "type": "array",
                "description": "The types of transactions the user has experience with.",
                "items": {
                  "type": "string",
                  "enum": [
                    "COVERED",
                    "LONG",
                    "SPREADS",
                    "NAKED_PUTS",
                    "NAKED_CALLS"
                  ]
                },
                "example": [
                  "LONG",
                  "NAKED_CALLS"
                ]
              }
            }
          }
        ]
      },
      "investmentSuitabilityDeclineToAnswer": {
        "type": "object",
        "oneOf": [
          {
            "$ref": "#/components/schemas/investmentSuitabilityCommon",
            "title": "Suitability Answers"
          },
          {
            "title": "Decline to Answer",
            "type": "object",
            "properties": {
              "declineToAnswer": {
                "type": "boolean",
                "description": "Indicates whether the user declined to answer the suitability question.",
                "example": true
              }
            }
          }
        ]
      },
      "UsersReq": {
        "required": [
          "userType",
          "documents"
        ],
        "type": "object",
        "properties": {
          "username": {
            "type": "string",
            "example": "sampleuser"
          },
          "password": {
            "type": "string",
            "example": "samplepassword"
          },
          "userType": {
            "$ref": "#/components/schemas/userType"
          },
          "wlpID": {
            "type": "string",
            "example": "TTCC",
            "description": "The wlpID is a deep backoffice ID that identifies each partner from each other.\n\n *⚠️ Only require to pass if your existing partner before **10/1/22**.",
            "deprecated": true
          },
          "parentIBID": {
            "type": "string",
            "example": "95c98ed5-e29e-4d55-90bf-8898fcf6af85",
            "description": "The parentIBID is a identifier that identifies a partners different business segments.\n\n *⚠️ Only require to pass if your existing partner before **10/1/22**.",
            "deprecated": true
          },
          "walletSettlementProfileID": {
            "type": "string",
            "example": "bank-profile-1",
            "description": "The walletSettlementProfileID is a identifier that denotes a user's wallet settlement profile.\n\n *⚠️ This is optional and only users for certain partners are eligible."
          },
          "documents": {
            "type": "array",
            "description": "The personal identifiable information & digital signatures.",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Basic_Info"
                },
                {
                  "$ref": "#/components/schemas/Identification_Info"
                },
                {
                  "$ref": "#/components/schemas/Tax_Info"
                },
                {
                  "$ref": "#/components/schemas/Personal_Info"
                },
                {
                  "$ref": "#/components/schemas/Address_Info"
                },
                {
                  "$ref": "#/components/schemas/KYC_Verification_Info"
                },
                {
                  "$ref": "#/components/schemas/Employment_Info"
                },
                {
                  "$ref": "#/components/schemas/Investor_Profile_Info"
                },
                {
                  "$ref": "#/components/schemas/Disclosures"
                },
                {
                  "$ref": "#/components/schemas/Margin_Disclosure"
                },
                {
                  "$ref": "#/components/schemas/FPSL_Disclosure"
                },
                {
                  "$ref": "#/components/schemas/Custodian_Info"
                },
                {
                  "$ref": "#/components/schemas/Director_Info"
                },
                {
                  "$ref": "#/components/schemas/Institutional_Info"
                },
                {
                  "$ref": "#/components/schemas/Trust_Info"
                }
              ]
            }
          },
          "metadata": {
            "type": "object",
            "example": {
              "myCustomKey": "myCustomValue"
            },
            "description": "The metadata object allows for creating a maximum of 5 keys (max 36 characters) and each value cannot exceed more than 128 bytes."
          }
        }
      },
      "KYC_Verification_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "KYC_VERIFICATION_INFO"
          },
          "data": {
            "type": "object",
            "properties": {
              "verification": {
                "type": "string",
                "example": "APPROVED",
                "enum": [
                  "APPROVED",
                  "FAILED"
                ]
              },
              "verificationIDType": {
                "type": "string",
                "example": "DRIVER_LICENSE",
                "enum": [
                  "DRIVER_LICENSE",
                  "NATIONAL_ID",
                  "RESIDENCE_PERMIT",
                  "PASSPORT",
                  "VISA",
                  "TAX_ID",
                  "VOTER_ID",
                  "WORK_PERMIT",
                  "TRUST",
                  "TRUST_CORP",
                  "CORPORATE"
                ]
              },
              "verificationFullName": {
                "type": "string",
                "example": "Justin Smith",
                "description": "The name of the customer that was passed during the KYC verification."
              },
              "verificationTimestamp": {
                "type": "string",
                "example": "2022-12-22T16:04:46.724Z",
                "description": "The ISO 8601 timestamp of when the KYC verification was completed by the partner."
              },
              "verificationTransactionID": {
                "type": "string",
                "example": "",
                "description": "A unique identifier passed to reference the KYC verification was completed by the partner."
              },
              "customField1": {
                "example": "customFieldValue1"
              },
              "customField2": {
                "example": "customFieldValue2"
              },
              "customField3": {
                "example": "customFieldValue3"
              },
              "customField4": {
                "example": "customFieldValue4"
              },
              "customField5": {
                "example": "customFieldValue5"
              }
            }
          }
        }
      },
      "Trust_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "TRUST_INFO"
          },
          "data": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "example": "Justin's Trust",
                "description": "The name of the trust."
              },
              "dateEstablished": {
                "type": "string",
                "example": "2014-09-29",
                "description": "The inception date of the trust."
              },
              "stateEstablished": {
                "type": "string",
                "example": "NJ",
                "description": "The state or province where the trust was established."
              },
              "street1": {
                "type": "string",
                "example": "15 Exchange Place",
                "description": "The physical street address where the institution is located."
              },
              "street2": {
                "type": "string",
                "example": "Unit 1100"
              },
              "city": {
                "type": "string",
                "example": "NJ",
                "description": "The institutuion physical city."
              },
              "province": {
                "type": "string",
                "example": "New Jersey",
                "description": "The institutuion physical state or province."
              },
              "postalCode": {
                "type": "string",
                "example": "07302",
                "description": "The institutuion physical postal or zip code."
              },
              "primaryTrusteeAuthority": {
                "type": "string",
                "example": "TRUSTEE_ONLY",
                "description": "The permissions the primary trustee has over the trust.",
                "enum": [
                  "TRUSTEE_ONLY",
                  "TRUSTEE_AND_GRANTOR",
                  "MODIFY_TRUSTEES",
                  "MODIFY_TRUST"
                ]
              },
              "tin": {
                "type": "string",
                "example": "123456789",
                "description": "The tax identification number of the trust."
              }
            }
          }
        }
      },
      "Margin_Disclosure": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "MARGIN_DISCLOSURE"
          },
          "data": {
            "type": "object",
            "required": [
              "marginAgreement"
            ],
            "properties": {
              "marginAgreement": {
                "type": "boolean",
                "example": true,
                "description": "A User's acceptance of DriveWealth's Margin Agreement."
              }
            }
          }
        }
      },
      "FPSL_Disclosure": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "FPSL_DISCLOSURE"
          },
          "data": {
            "type": "object",
            "required": [
              "fpslAgreement"
            ],
            "properties": {
              "fpslAgreement": {
                "type": "boolean",
                "example": true,
                "description": "A User's acceptance of DriveWealth's Fully Paid Securities Lending (FPSL) Agreement."
              }
            }
          }
        }
      },
      "Custodian_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "CUSTODIAN_INFO"
          },
          "data": {
            "type": "object",
            "properties": {
              "userID": {
                "$ref": "#/components/schemas/userID"
              }
            }
          }
        }
      },
      "Director_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "DIRECTOR_INFO"
          },
          "data": {
            "type": "object",
            "properties": {
              "directorList": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/directors"
                }
              }
            }
          }
        }
      },
      "directors": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "example": "Chief Innovation Officer",
            "description": "The title of the director."
          },
          "controlContact": {
            "type": "boolean",
            "example": true,
            "description": "True, if the director has control over the account."
          },
          "institutionalID": {
            "type": "string",
            "example": "fa1336af-02a3-2a82-d1a8-ccf11ecea398",
            "description": "The unique identifier of the institution director should assioacted with.."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string",
              "example": "CONTROL_PERSON",
              "enum": [
                "CONTROL_PERSON",
                "BENEFICIAL_OWNER",
                "TRUSTEE",
                "GRANTOR",
                "BENEFICIARY"
              ],
              "description": "The role in which the director serves in the institution."
            }
          },
          "percentage": {
            "type": "number",
            "example": 0.52,
            "description": "The percentage of ownership the director has in the institution. Value must be greater than 0 and up to 1 (representing 0-100%), with a maximum of 2 decimal places."
          }
        }
      },
      "Institutional_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "INSTITUTIONAL_INFO"
          },
          "data": {
            "type": "object",
            "properties": {
              "physicalAddressLine1": {
                "type": "string",
                "example": "15 Exchange Place",
                "description": "The physical street address where the institution is located."
              },
              "physicalAddressLine2": {
                "type": "string",
                "example": "Unit 1100"
              },
              "physicalCity": {
                "type": "string",
                "example": "Jersey City",
                "description": "The institutuion physical city."
              },
              "physicalStateProvince": {
                "type": "string",
                "example": "NJ",
                "description": "The institutuion physical state or province."
              },
              "physicalZipPostalCode": {
                "type": "string",
                "example": "07302",
                "description": "The institutuion physical postal or zip code."
              },
              "physicalCountryID": {
                "type": "string",
                "example": "USA",
                "description": "The institutuion physical country of origin."
              },
              "companyOrganizedAs": {
                "type": "string",
                "example": "LLC",
                "description": "The institutuion orginizational structure.",
                "enum": [
                  "NON_CORP",
                  "INC",
                  "CLUB",
                  "LLC",
                  "LLLP",
                  "LLP",
                  "LP",
                  "PARTNERSHIP",
                  "SOLE_PROPRIETOR"
                ]
              },
              "usaBranch": {
                "type": "boolean",
                "example": true,
                "description": "True, if the institutuion is registered in side of the United States."
              },
              "foreignBank": {
                "type": "boolean",
                "example": false,
                "description": "True, if the institution is a foreign bank."
              },
              "foreignFinancialInstitution": {
                "type": "boolean",
                "example": false,
                "description": "True, if the institution is maintained for a foreign finanical institution."
              },
              "directorCount": {
                "type": "number",
                "example": "15",
                "description": "The number of directors to be added to institutional account."
              }
            }
          }
        }
      },
      "Basic_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of data object.",
            "example": "BASIC_INFO",
            "enum": [
              "BASIC_INFO",
              "IDENTIFICATION_INFO",
              "TAX_INFO",
              "PERSONAL_INFO",
              "ADDRESS_INFO",
              "EMPLOYMENT_INFO",
              "INVESTOR_PROFILE_INFO",
              "DISCLOSURES",
              "MARGIN_DISCLOSURE",
              "FPSL_DISCLOSURE",
              "CUSTODIAN_INFO",
              "DIRECTOR_INFO",
              "INSTITUTIONAL_INFO",
              "TRUST_INFO"
            ]
          },
          "data": {
            "type": "object",
            "required": [
              "firstName",
              "lastName",
              "country",
              "phone",
              "emailAddress"
            ],
            "properties": {
              "firstName": {
                "$ref": "#/components/schemas/firstName"
              },
              "lastName": {
                "$ref": "#/components/schemas/lastName"
              },
              "country": {
                "type": "string",
                "example": "USA",
                "description": "The country where the User is residing."
              },
              "phone": {
                "$ref": "#/components/schemas/phoneNumber"
              },
              "emailAddress": {
                "$ref": "#/components/schemas/email"
              }
            }
          }
        }
      },
      "Identification_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of data object.",
            "example": "IDENTIFICATION_INFO",
            "enum": [
              "BASIC_INFO",
              "IDENTIFICATION_INFO",
              "TAX_INFO",
              "PERSONAL_INFO",
              "ADDRESS_INFO",
              "EMPLOYMENT_INFO",
              "INVESTOR_PROFILE_INFO",
              "DISCLOSURES",
              "MARGIN_DISCLOSURE",
              "FPSL_DISCLOSURE",
              "CUSTODIAN_INFO",
              "DIRECTOR_INFO",
              "INSTITUTIONAL_INFO",
              "TRUST_INFO"
            ]
          },
          "data": {
            "type": "object",
            "required": [
              "value",
              "type",
              "citizenship"
            ],
            "properties": {
              "value": {
                "$ref": "#/components/schemas/userTaxID"
              },
              "type": {
                "$ref": "#/components/schemas/userTaxIDType"
              },
              "citizenship": {
                "$ref": "#/components/schemas/userCountry",
                "description": "The country where the User has citizenship."
              },
              "issuingCountry": {
                "$ref": "#/components/schemas/userCountry",
                "description": "The country where the identification was issued. Only required for PASSPORT, ALIEN_ID, and OTHER id types."
              },
              "issuingProvince": {
                "$ref": "#/components/schemas/userProvince",
                "description": "The state or province where the identification was issued."
              },
              "issueDate": {
                "$ref": "#/components/schemas/date",
                "description": "The date when the identification was issued in YYYY-MM-DD format."
              },
              "expiryDate": {
                "$ref": "#/components/schemas/date",
                "description": "The date when the identification expires in YYYY-MM-DD format."
              },
              "description": {
                "type": "string",
                "example": "Foreign Passport",
                "description": "Additional information about the identification type provided."
              }
            }
          }
        }
      },
      "Tax_Info": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of data object.",
            "example": "TAX_INFO",
            "enum": [
              "BASIC_INFO",
              "IDENTIFICATION_INFO",
              "TAX_INFO",
              "PERSONAL_INFO",
              "ADDRESS_INFO",
              "EMPLOYMENT_INFO",
              "INVESTOR_PROFILE_INFO",
              "DISCLOSURES",
              "MARGIN_DISCLOSURE",
              "FPSL_DISCLOSURE",
              "CUSTODIAN_INFO",
              "DIRECTOR_INFO",
              "INSTITUTIONAL_INFO",
              "TRUST_INFO"
            ]
          },
          "data": {
            "type": "object",
            "required": [
              "taxTreatyWithUS"
            ],
            "properties": {
              "taxTreatyWithUS": {
                "type": "boolean",
                "example": true,
                "description": "True, if the user lives in a treaty country and is claiming tax treaty with the United States."
              },
              "usTaxpayer": {
                "type": "boolean",
                "example": true,
                "description": "True if the party is a US Tax payer"
              }
            }
          }
        }
      },
      "Personal_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of data object.",
            "example": "PERSONAL_INFO",
            "enum": [
              "BASIC_INFO",
              "IDENTIFICATION_INFO",
              "TAX_INFO",
              "PERSONAL_INFO",
              "ADDRESS_INFO",
              "EMPLOYMENT_INFO",
              "INVESTOR_PROFILE_INFO",
              "DISCLOSURES",
              "MARGIN_DISCLOSURE",
              "FPSL_DISCLOSURE",
              "CUSTODIAN_INFO",
              "DIRECTOR_INFO",
              "INSTITUTIONAL_INFO",
              "TRUST_INFO"
            ]
          },
          "data": {
            "type": "object",
            "required": [
              "birthDay",
              "birthMonth",
              "birthYear",
              "politicallyExposedNames"
            ],
            "properties": {
              "birthDay": {
                "type": "number",
                "example": 3,
                "description": "The User's born day."
              },
              "birthMonth": {
                "type": "number",
                "example": 12,
                "description": "The User's born month."
              },
              "birthYear": {
                "type": "number",
                "example": 2000,
                "description": "The User's born year."
              },
              "dateOfDeath": {
                "type": "string",
                "example": "2025-12-04",
                "description": "The User's date of death in YYYY-MM-DD format."
              },
              "politicallyExposedNames": {
                "type": "string",
                "example": "Nancy Pelosi",
                "description": "The names of the people whom are political exposes, separated by a comma.\n\n *⚠️ Can be set to 'NULL' if not politically exposed"
              },
              "marital": {
                "$ref": "#/components/schemas/userMaritalStatus"
              }
            }
          }
        }
      },
      "Address_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of data object.",
            "example": "ADDRESS_INFO",
            "enum": [
              "BASIC_INFO",
              "IDENTIFICATION_INFO",
              "TAX_INFO",
              "PERSONAL_INFO",
              "ADDRESS_INFO",
              "EMPLOYMENT_INFO",
              "INVESTOR_PROFILE_INFO",
              "DISCLOSURES",
              "MARGIN_DISCLOSURE",
              "FPSL_DISCLOSURE",
              "CUSTODIAN_INFO",
              "DIRECTOR_INFO",
              "INSTITUTIONAL_INFO",
              "TRUST_INFO"
            ]
          },
          "data": {
            "type": "object",
            "required": [
              "street1",
              "city",
              "province",
              "postalCode",
              "country"
            ],
            "properties": {
              "street1": {
                "$ref": "#/components/schemas/userStreet1"
              },
              "street2": {
                "$ref": "#/components/schemas/userStreet2"
              },
              "city": {
                "$ref": "#/components/schemas/userCity"
              },
              "province": {
                "$ref": "#/components/schemas/userProvince"
              },
              "postalCode": {
                "$ref": "#/components/schemas/userPostalCode"
              },
              "country": {
                "$ref": "#/components/schemas/userCountry"
              }
            }
          }
        }
      },
      "Employment_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "example": "EMPLOYMENT_INFO"
          },
          "data": {
            "type": "object",
            "required": [
              "status",
              "broker",
              "directorOf"
            ],
            "properties": {
              "status": {
                "type": "string",
                "example": "EMPLOYED",
                "description": "The User current employment status.",
                "enum": [
                  "EMPLOYED",
                  "RETIRED",
                  "STUDENT",
                  "UNEMPLOYED",
                  "SELF_EMPLOYED"
                ]
              },
              "company": {
                "type": "string",
                "example": "DriveWealth LLC",
                "description": "The User's current employer name.\n\n *⚠️ Only required when status equal to EMPLOYED or SELF_EMPLOYED & type is not being provided*"
              },
              "companyID": {
                "type": "string",
                "example": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
                "description": "A unique identifier created for each Institution or entity on DriveWealth's platform.*"
              },
              "from": {
                "type": "string",
                "example": "2014-09-29",
                "description": "The User's start date at the employment."
              },
              "to": {
                "type": "string",
                "example": "2022-12-25",
                "description": "The User's end date at the employment."
              },
              "type": {
                "type": "string",
                "example": "FINANCE",
                "description": "The User's current employer type.\n\n *⚠️ Only required when status equal to EMPLOYED or SELF_EMPLOYED & company is not being provided*",
                "enum": [
                  "AGRICULTURE",
                  "MINING",
                  "UTILITIES",
                  "CONSTRUCTION",
                  "MANUFACTURING",
                  "WHOLESALE",
                  "RETAIL",
                  "TRANSPORT",
                  "INFORMATION",
                  "FINANCE",
                  "REAL_ESTATE",
                  "PROFESSIONAL",
                  "MANAGEMENT",
                  "EDUCATION",
                  "HEALTH",
                  "ART",
                  "FOOD",
                  "PUBLIC",
                  "WASTE"
                ]
              },
              "position": {
                "type": "string",
                "example": "ENGINEER",
                "description": " The User's current role at the employment.\n\n *⚠️ Only required when status equal to EMPLOYED or SELF_EMPLOYED & using Drivewealth's Market Data Offering*",
                "enum": [
                  "ACCOUNTANT",
                  "ACTUARY",
                  "ADJUSTER",
                  "ADMINISTRATOR",
                  "ADVERTISER",
                  "AGENT",
                  "ATC",
                  "AMBASSADOR",
                  "ANALYST",
                  "APPRAISER",
                  "ARCHITECT",
                  "ARTIST",
                  "ASSISTANT",
                  "ATHLETE",
                  "ATTENDANT",
                  "ATTORNEY",
                  "AUCTIONEER",
                  "AUDITOR",
                  "BARBER",
                  "BROKER",
                  "BUSINESS_EXEC",
                  "BUSINESS_OWNER",
                  "CAREGIVER",
                  "CARPENTER",
                  "CASHIER",
                  "CHEF",
                  "CHIROPRACTOR",
                  "CIVIL",
                  "CLERGY",
                  "CLERK",
                  "COMPLIANCE",
                  "CONSULTANT",
                  "CONTRACTOR",
                  "COUNSELOR",
                  "CUSTOMER_SERVICE",
                  "DEALER",
                  "DEVELOPER",
                  "DISTRIBUTOR",
                  "DOCTOR",
                  "DRIVER",
                  "ENGINEER",
                  "EXAMINER",
                  "EXTERMINATOR",
                  "FACTORY",
                  "FARMER",
                  "FINANCIAL",
                  "FISHERMAN",
                  "FLIGHT",
                  "HR",
                  "IMPEX",
                  "INSPECTOR",
                  "INTERN",
                  "INVESTMENT",
                  "INVESTOR",
                  "IT",
                  "JANITOR",
                  "JEWELER",
                  "LABORER",
                  "LANDSCAPER",
                  "LENDING",
                  "MANAGER",
                  "MECHANIC",
                  "MILITARY",
                  "MORTICIAN",
                  "NURSE",
                  "NUTRITIONIST",
                  "OFFICE",
                  "PHARMACIST",
                  "PHYSICAL",
                  "PILOT",
                  "POLICE",
                  "POLITICIAN",
                  "PM",
                  "REP",
                  "RESEARCHER",
                  "SAILOR",
                  "SALES",
                  "SCIENTIST",
                  "SEAMSTRESS",
                  "SECURITY",
                  "SOCIAL",
                  "TEACHER",
                  "TECHNICIAN",
                  "TELLER",
                  "TRADESPERSON",
                  "TRAINER",
                  "TRANSPORTER",
                  "UNDERWRITER",
                  "WRITER"
                ]
              },
              "broker": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User's current employer is broker."
              },
              "directorOf": {
                "type": "string",
                "example": "AAPL, SQ",
                "description": "The company name, ticker of the company; if the user is a director or owns more than 10% of a publicly traded company.\n\n *⚠️ Can be set to 'NULL' if not applicable*"
              }
            }
          }
        }
      },
      "Investor_Profile_Info": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "example": "INVESTOR_PROFILE_INFO"
          },
          "data": {
            "type": "object",
            "required": [
              "investmentExperience",
              "annualIncome",
              "networthTotal",
              "riskTolerance",
              "investmentObjectives",
              "networthLiquid"
            ],
            "properties": {
              "investmentExperience": {
                "type": "string",
                "example": "YRS_10_",
                "description": "The User's current investment expertise.\n\n *⚠️ Can be defaulted to 'YRS_1_2' for all asset classes, except Options.*",
                "enum": [
                  "NONE",
                  "YRS_1_2",
                  "YRS_3_5",
                  "YRS_5_10",
                  "YRS_10_"
                ]
              },
              "annualIncome": {
                "type": "number",
                "example": 1000000,
                "description": "The User's current annalized income over one year."
              },
              "networthTotal": {
                "type": "number",
                "example": 2500000,
                "description": "The user's current networth. This calculation is the User's assets - liabilities."
              },
              "riskTolerance": {
                "type": "string",
                "example": "HIGH",
                "description": "The User's risk ceiling.\n\n *⚠️ Can be defaulted to 'LOW' for all asset classes, except Options.*",
                "enum": [
                  "LOW",
                  "MODERATE",
                  "SPECULATION",
                  "HIGH"
                ]
              },
              "investmentObjectives": {
                "type": "string",
                "example": "CAPITAL_PRESERVATION",
                "description": "The User's current investment objectives. **Deprecated values:** LONG_TERM, INFREQUENT, FREQUENT, ACTIVE_DAILY.\n\n *⚠️ Can be defaulted to 'CAPITAL_PRESERVATION' for all asset classes, except Options.*",
                "enum": [
                  "LONG_TERM",
                  "INFREQUENT",
                  "FREQUENT",
                  "ACTIVE_DAILY",
                  "NEW",
                  "CAPITAL_PRESERVATION",
                  "GROWTH",
                  "INCOME",
                  "SPECULATION"
                ]
              },
              "secondaryInvestmentObjectives": {
                "type": "array",
                "description": "The User's secondary investment objectives. **Deprecated values:** LONG_TERM, INFREQUENT, FREQUENT, ACTIVE_DAILY.",
                "items": {
                  "type": "string",
                  "example": "INCOME",
                  "enum": [
                    "LONG_TERM",
                    "INFREQUENT",
                    "FREQUENT",
                    "ACTIVE_DAILY",
                    "NEW",
                    "CAPITAL_PRESERVATION",
                    "GROWTH",
                    "INCOME",
                    "SPECULATION"
                  ]
                }
              },
              "networthLiquid": {
                "type": "number",
                "example": 300000,
                "description": "The user's liquid net worth. The amount of cash or near cash equivalents of the User's net worth.\n\n *⚠️ Can be defaulted to '-1' for all asset classes, except Options.*"
              },
              "dependents": {
                "type": "number",
                "example": "4",
                "description": "Total number of dependents the account holder has.\n\n *⚠️ Required for Options Onboarding.*"
              },
              "optionsSuitability": {
                "type": "object",
                "deprecated": true,
                "description": "Details about the User's suitability for trading options, including their experience with options and equities.\n\n *⚠️ Required for Options Onboarding.*",
                "properties": {
                  "equitiesExperience": {
                    "$ref": "#/components/schemas/investmentSuitability",
                    "description": "An object containing fields that evaluate the User's experience and suitability for equities trading."
                  },
                  "optionsExperience": {
                    "$ref": "#/components/schemas/investmentSuitability",
                    "description": "An object containing fields that evaluate the User's experience and suitability for options trading."
                  }
                }
              },
              "equitiesExperience": {
                "$ref": "#/components/schemas/investmentSuitabilityEquities",
                "description": "An object containing fields that evaluate the User's experience and suitability for equities trading.\n\n *⚠️ Required for Options Onboarding.*"
              },
              "optionsExperience": {
                "$ref": "#/components/schemas/investmentSuitabilityOptions",
                "description": "An object containing fields that evaluate the User's experience and suitability for options trading.\n\n *⚠️ Required for Options Onboarding.*"
              },
              "fixedIncomeExperience": {
                "$ref": "#/components/schemas/investmentSuitabilityDeclineToAnswer",
                "description": "An object containing fields that evaluate the User's experience and suitability for fixed income trading."
              },
              "commodityExperience": {
                "$ref": "#/components/schemas/investmentSuitabilityDeclineToAnswer",
                "description": "An object containing fields that evaluate the User's experience and suitability for commodity trading."
              },
              "otherFinancialExperience": {
                "$ref": "#/components/schemas/investmentSuitabilityDeclineToAnswer",
                "description": "An object containing fields that evaluate the User's experience and suitability for other financial instruments trading."
              }
            }
          }
        }
      },
      "Disclosures": {
        "type": "object",
        "required": [
          "type",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "example": "DISCLOSURES"
          },
          "data": {
            "type": "object",
            "required": [
              "termsOfUse",
              "marketDataAgreement",
              "customerAgreement",
              "rule14b",
              "privacyPolicy",
              "dataSharing",
              "signedBy"
            ],
            "properties": {
              "extendedHoursAgreement": {
                "type": "boolean",
                "example": false,
                "description": "True, if the User accepts DriveWealth's Extended Hours Agreement."
              },
              "termsOfUse": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Terms of Use."
              },
              "customerAgreement": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Customer Agreement."
              },
              "iraAgreement": {
                "type": "boolean",
                "example": false,
                "description": "True, if the User accepts DriveWealth's Individual Retirement Account (IRA) Agreement. *⚠ Only for opening IRA accounts.*"
              },
              "marketDataAgreement": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Market Data Agreement."
              },
              "optionsAgreement": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Options trading Agreement."
              },
              "oddLinkAgreement": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's ODD Link Agreement."
              },
              "rule14b": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Rule 14b1(c)."
              },
              "privacyPolicy": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Privacy Policy."
              },
              "dataSharing": {
                "type": "boolean",
                "example": true,
                "description": "True, if the User accepts DriveWealth's Data Sharing Policy."
              },
              "signedBy": {
                "type": "string",
                "example": "Justin Smith",
                "description": "The User's digital signature (full name)."
              }
            }
          }
        }
      },
      "UserResponse": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/userID"
          },
          "userType": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/userType"
              },
              "description": {
                "type": "string",
                "example": "Individual Trader",
                "description": "A custom description of the User type."
              }
            }
          },
          "status": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/userStatus"
              },
              "description": {
                "type": "string",
                "example": "User is pending approval.",
                "description": "A custom description of the User's status."
              }
            }
          },
          "parentIBID": {
            "type": "object",
            "properties": {
              "id": {
                "$ref": "#/components/schemas/parentIBID"
              },
              "name": {
                "$ref": "#/components/schemas/firmName"
              }
            }
          },
          "documents": {
            "type": "array",
            "description": "The personal identifiable information & digital signatures.",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Basic_Info"
                },
                {
                  "$ref": "#/components/schemas/Director_Info"
                },
                {
                  "$ref": "#/components/schemas/Identification_Info"
                },
                {
                  "$ref": "#/components/schemas/Tax_Info"
                },
                {
                  "$ref": "#/components/schemas/Personal_Info"
                },
                {
                  "$ref": "#/components/schemas/Address_Info"
                },
                {
                  "$ref": "#/components/schemas/Employment_Info"
                },
                {
                  "$ref": "#/components/schemas/Investor_Profile_Info"
                },
                {
                  "$ref": "#/components/schemas/Disclosures"
                }
              ]
            }
          },
          "wlpID": {
            "$ref": "#/components/schemas/wlpID"
          },
          "walletSettlementProfileID": {
            "$ref": "#/components/schemas/walletSettlementProfileID"
          },
          "referralCode": {
            "type": "string",
            "example": "71J000",
            "description": "The associated referral program associated to the User."
          },
          "createdWhen": {
            "type": "string",
            "example": "2022-12-11T22:28:21.810Z",
            "description": "The createdWhen is the date and time the User was created."
          },
          "updatedWhen": {
            "type": "string",
            "example": "2022-12-11T22:28:21.810Z",
            "description": "The updatedWhen is the last date and time the User was updated."
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