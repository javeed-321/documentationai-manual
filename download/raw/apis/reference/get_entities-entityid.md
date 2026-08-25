---
updatedAt: 2026-04-21T16:52:26.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve Entity

Retrieves a Entity details by entityId.

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
      "name": "Entities"
    }
  ],
  "paths": {
    "/entities/{entityId}": {
      "get": {
        "tags": [
          "Entities"
        ],
        "summary": "Retrieve Entity",
        "description": "Retrieves a Entity details by entityId.",
        "parameters": [
          {
            "in": "path",
            "name": "entityId",
            "schema": {
              "type": "string"
            },
            "required": true,
            "example": "83096bad-c99b-4d48-9819-364a46c7c2ed",
            "description": "Unique ID of the Entity to fetch."
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieving a Entity was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EntityResponseModel"
                },
                "examples": {
                  "Entity Example": {
                    "value": {
                      "ibID": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
                      "type": "CORPORATION",
                      "subType": "C_CORPORATION",
                      "attributes": {
                        "name": "Better Investment",
                        "dba": "BI",
                        "incorporationCountry": "USA",
                        "incorporationProvince": "NY",
                        "incorporationDate": "2019-01-01"
                      },
                      "identifications": {
                        "EIN": "12-3456789"
                      },
                      "contact": {
                        "addresses": {
                          "PRIMARY": {
                            "street1": "123 Main Street",
                            "street2": "suite 101",
                            "city": "Wilmington",
                            "province": "DE",
                            "zipcode": "19801",
                            "country": "USA"
                          }
                        },
                        "phone": "+12345678911",
                        "email": "hello@acme.com",
                        "website": "www.acme.com"
                      },
                      "metadata": {
                        "myCustomKey": "myCustomValue"
                      },
                      "disclosures": {
                        "termsOfUse": {
                          "agreed": true,
                          "signedBy": "termsOfUse",
                          "signedWhen": "2024-09-17T10:00:00Z"
                        },
                        "customerAgreement": {
                          "agreed": true,
                          "signedBy": "termsOfUse",
                          "signedWhen": "2024-09-17T10:00:00Z"
                        },
                        "rule14b": {
                          "agreed": true,
                          "signedBy": "termsOfUse",
                          "signedWhen": "2024-09-17T10:00:00Z"
                        }
                      },
                      "id": "83096bad-c99b-4d48-9819-364a46c7cqw2",
                      "wlpID": "DW",
                      "directors": [
                        {
                          "id": "684ca44e-1d8d-49f0-bd49-2761eb84df43",
                          "roles": [
                            "CONTROL_PERSON"
                          ],
                          "title": "DevDirector",
                          "firstName": "Manoj",
                          "lastName": "Krishna",
                          "percentage": 0.25,
                          "controlContact": true
                        }
                      ],
                      "kyb": {
                        "status": "KYB_READY",
                        "statusWhen": "2024-12-12T02:40:18.452756Z",
                        "statusBy": "SYSTEM"
                      },
                      "tax": {
                        "status": "TAX_READY",
                        "message": "Entity is ready for tax processing"
                      },
                      "status": "PENDING",
                      "createdAt": "2024-12-12T02:40:18.452756Z",
                      "updatedAt": "2024-12-16T22:51:23.340323Z",
                      "createdBy": "59cf3b9c-6557-4010-b19b-6a3750c4b533",
                      "updatedBy": "59cf3b9c-6557-4010-b19b-6a3750c4b533",
                      "taxData": {
                        "fatcaData": {
                          "applicable": true,
                          "applicableFrom": "2024-12-12T02:40:18.421371Z",
                          "setBy": "SYSTEM"
                        },
                        "vendor": {
                          "COMPLY_EXCHANGE": {
                            "name": "Comply Exchange",
                            "taxFormUrl": "www.tax.com",
                            "formUrlDate": "2023-11-01T12:34:56Z"
                          }
                        },
                        "data": {
                          "W8BENE": {
                            "formType": "W8BENE",
                            "status": "TAX_APPROVED",
                            "statusWhen": "2025-09-29T17:28:31.047Z",
                            "statusBy": "COMPLY_EXCHANGE",
                            "receivedFrom": "Comply Exchange",
                            "receivedWhen": "2025-09-29T17:28:31.047Z",
                            "expiresWhen": "2028-12-31",
                            "taxTreatyBenefitClaimed": true,
                            "chapter3StatusW8": "CORPORATION",
                            "chapter4StatusW8": "ACTIVE_NFFE",
                            "chapter3Status1042S": "15",
                            "chapter4Status1042S": "22"
                          }
                        }
                      },
                      "investorProfile": {
                        "annualRevenue": 1000000,
                        "netWorthTotal": 5000000,
                        "investmentObjective": "GROWTH",
                        "riskTolerance": "HIGH",
                        "liquidityNeeds": "LOW",
                        "investmentExperience": "YRS_5_10",
                        "timeHorizon": "LONG_TERM",
                        "secLargeTraderID": "12345678-1234",
                        "equities": {
                          "monthlyTransactionAmount": "OVER_$1M",
                          "investmentExperience": "NONE"
                        },
                        "fixedIncome": {
                          "monthlyTransactionAmount": "OVER_$1M"
                        }
                      },
                      "financialAffiliations": [
                        "Bank of Narnia",
                        "Gringotts Bank"
                      ],
                      "industryClassification": {
                        "NAICS": {
                          "code": 111110
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Invalid input."
          },
          "401": {
            "description": "Unauthorized - Authentication failed."
          },
          "403": {
            "description": "Forbidden - You do not have permission to access this resource."
          },
          "404": {
            "description": "Not Found - The requested resource was not found."
          },
          "500": {
            "description": "Internal Server Error - An unexpected error occurred."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "parentIBID": {
        "type": "string",
        "example": "80f9b672-120d-4b73-9cc9-42fb3262c4b9",
        "description": "The unique identifier of the firm."
      },
      "directorRoleType": {
        "type": "string",
        "example": "CONTROL_PERSON",
        "description": "The type of director role.",
        "enum": [
          "CONTROL_PERSON",
          "BENEFICIAL_OWNER",
          "TRUSTEE",
          "GRANTOR",
          "BENEFICIARY"
        ]
      },
      "kycProcessStatus": {
        "type": "string",
        "example": "KYC_READY",
        "description": "The status of the KYC process.",
        "enum": [
          "KYC_NOT_READY",
          "KYC_READY",
          "KYC_PROCESSING",
          "KYC_INFO_REQUIRED",
          "KYC_DOC_REQUIRED",
          "KYC_MANUAL_REVIEW",
          "KYC_DENIED",
          "KYC_APPROVED"
        ]
      },
      "businessStatus": {
        "type": "string",
        "example": "PENDING",
        "description": "The status of the business entity.",
        "enum": [
          "PENDING",
          "APPROVED",
          "REJECTED",
          "REVOKED",
          "CLOSED"
        ]
      },
      "factaStatus": {
        "type": "string",
        "example": "ACTIVE_NFFE",
        "description": "The tax chapter4 status.",
        "enum": [
          "ACTIVE_NFFE",
          "PASSIVE_NFFE",
          "PARTICIPATING_FFI",
          "NONPARTICIPATING_FFI",
          "REPORTING_MODEL_1_FFI",
          "REPORTING_MODEL_2_FFI",
          "REGISTERED_DEEMED_COMPLIANT_FFI",
          "SPONSORED_FFI",
          "NOT_FINANCIAL_ACCOUNT",
          "COMPLIANT_NONREGISTERING_LOCAL_BANK",
          "COMPLIANT_FFI_LOW_VALUE_ACCOUNTS",
          "CLOSED_HELD_INVESTMENT_VEHICLE",
          "LIMITED_LIFE_DEBT_INVESTMENT_ENTITY",
          "INVESTMENT_ENTITIES_NO_FINANCIAL_ACCOUNTS",
          "RESTRICTED_DISTRIBUTOR",
          "NONREPORTING_IGA_FFI",
          "FOREIGN_GOVERNMENT_OR_CENTRAL_BANK",
          "INTERNATIONAL_ORGANIZATION",
          "EXEMPT_RETIREMENT_PLANS",
          "ENTITY_WHOLELY_OWNED_BENEFICIAL_OWNERS",
          "TERRITORY_FINANCIAL_INSTITUTION",
          "EXCEPTED_NONFINANCIAL_STARTUP_COMPANY",
          "EXCEPTED_NONFINANCIAL_ENTITY_LIQUIDATION_BANKRUPTCY",
          "ORGANIZATION_501C",
          "NONPROFIT_ORGANIZATION",
          "PUBLICLY_TRADED_NFFE_OR_AFFILIATE",
          "EXCEPTED_TERRITORY_NFFE",
          "EXCEPTED_INTER_AFFILIATE_FFI",
          "DIRECT_REPORTING_NFFE",
          "SPONSORED_DIRECT_REPORTING_NFFE",
          "EXCEPTED_NONFINANCIAL_GROUP_ENTITY",
          "OWNER_DOCUMENTED_FFI",
          "FOREIGN_CENTRAL_BANK_OF_ISSUE",
          "NOT_AVAILABLE"
        ]
      },
      "taxRecipientCode": {
        "type": "string",
        "example": "CORPORATION",
        "description": "The tax chapter3 status.",
        "enum": [
          "UNKNOWN",
          "INDIVIDUAL",
          "CORPORATION",
          "WITHHOLDING_FOREIGN_PARTNERSHIP",
          "WITHHOLDING_FOREIGN_PARTNERSHIP_TRUST",
          "TRUST",
          "GOVERNMENT_INTERNATIONAL_ORGANIZATION",
          "TAX_EXEMPT_ORGNIZATION",
          "PRIVATE_FOUNDATION",
          "ARTIST_ATHLETE",
          "ESTATE",
          "US_BRANCH_TREATED_PERSON",
          "QUALIFIED_INTERMEDIARY",
          "PRIVATE_INTERMEDIARY_WITHHOLDING_GENERAL",
          "PRIVATE_INTERMEDIARY_WITHHOLDING_EXEMPT_ORG",
          "QUALIFIED_INTERMEDIARY_WITHHOLDING_GENERAL",
          "QUALIFIED_INTERMEDIARY_WITHHOLDING_EXEMPT_ORG",
          "AUTHORIZED_FOREIGN_AGENT",
          "PUBLIC_PENSION_FUND",
          "UNKNOWN_RECIPIENT",
          "QUALIFIED_SECURITIES_LENDER_INTERMEDIARY",
          "QUALIFIED_SECURITIES_LENDER_OTHER",
          "SIMPLE_TRUST",
          "CENTRAL_BANK_OF_ISSUE",
          "GRANTOR_TRUST",
          "TAX_EXEMPT_ORGANIZATION",
          "DISREGARDED_ENTITY",
          "COMPLEX_TRUST",
          "INTERNATIONAL_ORGANIZATION",
          "PARTNERSHIP",
          "FOREIGN_GOVERNMENT_CONTROLLED_ENTITY",
          "FOREIGN_GOVERNMENT_INTEGRAL_PART",
          "QI",
          "NONQUALIFIED_INTERMEDIARY",
          "TERRITORY_FINANCIAL_INSTITUTION",
          "US_BRANCH",
          "FOREIGN_PARTNERSHIP_WITHHOLDING",
          "WITHHOLDING_FOREIGN_TRUST",
          "NONWITHHOLDING_FOREIGN_PARTNERSHIP",
          "NONWITHHOLDING_FOREIGN_SIMPLE_TRUST",
          "NONWITHHOLDING_FOREIGN_GRANTOR_TRUST"
        ]
      },
      "taxStatusCode": {
        "type": "string",
        "description": "The tax form type.",
        "enum": [
          "W8BEN",
          "W8BENE",
          "W8ECI",
          "W8EXPL",
          "W8IMY",
          "W9"
        ]
      },
      "EntityResponseModel": {
        "type": "object",
        "description": "Entity representation returned by the API. Note the key casing differs from the request body: `identifications` keys are returned uppercase (EIN, FTIN, GIIN, FTNLO, SSN) and address types are returned uppercase (PRIMARY), whereas requests use lowercase (ein, ftin, ..., primary).",
        "properties": {
          "id": {
            "type": "string",
            "example": "83096bad-c99b-4d48-9819-364a46c7cqw2",
            "description": "The unique identifier of the entity."
          },
          "ibID": {
            "$ref": "#/components/schemas/parentIBID"
          },
          "wlpID": {
            "type": "string",
            "example": "DW",
            "description": "The WLP identifier of the entity."
          },
          "type": {
            "type": "string",
            "example": "CORPORATION",
            "description": "The type of the entity.",
            "enum": [
              "CORPORATION",
              "LLC",
              "TRUST",
              "PARTNERSHIP"
            ]
          },
          "subType": {
            "type": "string",
            "example": "C_CORPORATION",
            "description": "The subtype of the entity.",
            "enum": [
              "S_CORPORATION",
              "C_CORPORATION",
              "LLC_SINGLE_MEMBER",
              "LLC_C_CORPORATION",
              "LLC_S_CORPORATION",
              "LLC_PARTNERSHIP",
              "PARTNERSHIP_GENERAL",
              "PARTNERSHIP_LIMITED",
              "SMSF"
            ]
          },
          "attributes": {
            "$ref": "#/components/schemas/EntitiesAttributesRequestModel"
          },
          "identifications": {
            "$ref": "#/components/schemas/IdentificationsResponse"
          },
          "contact": {
            "$ref": "#/components/schemas/AddressResponseModel"
          },
          "metadata": {
            "type": "object",
            "example": {
              "myCustomKey": "myCustomValue"
            },
            "description": "Additional metadata for the entity."
          },
          "disclosures": {
            "$ref": "#/components/schemas/EntityDisclosuresModel"
          },
          "financialAffiliations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "Bank of Narnia",
              "Gringotts Bank"
            ],
            "description": "List of financial affiliations."
          },
          "industryClassification": {
            "type": "object",
            "properties": {
              "NAICS": {
                "type": "object",
                "properties": {
                  "code": {
                    "type": "integer",
                    "example": 111110,
                    "description": "The NAICS code representing the industry classification."
                  }
                }
              },
              "OTHER": {
                "type": "object",
                "properties": {
                  "code": {
                    "type": "string",
                    "example": "ENERGY",
                    "description": "The industry classification code that is not part of NAICS."
                  }
                }
              }
            },
            "description": "Industry classification details."
          },
          "directors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EntityDirectorsResponseModel"
            },
            "description": "A list of directors of the entity."
          },
          "taxData": {
            "$ref": "#/components/schemas/TaxData"
          },
          "investorProfile": {
            "$ref": "#/components/schemas/EntityInvestorProfile"
          },
          "kyb": {
            "$ref": "#/components/schemas/EntityKybResponseModel"
          },
          "tax": {
            "type": "object",
            "properties": {
              "status": {
                "type": "string",
                "example": "TAX_READY",
                "description": "The tax status of the entity."
              },
              "message": {
                "type": "string",
                "example": "Entity is ready for tax processing",
                "description": "A message providing additional information about the tax status."
              }
            }
          },
          "status": {
            "$ref": "#/components/schemas/businessStatus"
          },
          "createdAt": {
            "type": "string",
            "example": "2024-12-12T02:40:18.452756Z",
            "description": "The date and time when the entity was created."
          },
          "updatedAt": {
            "type": "string",
            "example": "2024-12-16T22:51:23.340323Z",
            "description": "The date and time when the entity was last updated."
          },
          "createdBy": {
            "type": "string",
            "example": "59cf3b9c-6557-4010-b19b-6a3750c4b533",
            "description": "The user who created the entity."
          },
          "updatedBy": {
            "type": "string",
            "example": "59cf3b9c-6557-4010-b19b-6a3750c4b533",
            "description": "The user who last updated the entity."
          }
        }
      },
      "TaxData": {
        "type": "object",
        "properties": {
          "fatcaData": {
            "$ref": "#/components/schemas/FATCAData"
          },
          "vendor": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/Vendor"
            },
            "example": {
              "COMPLY_EXCHANGE": {
                "name": "Comply Exchange",
                "taxFormUrl": "www.tax.com",
                "formUrlDate": "2023-11-01T12:34:56Z"
              }
            },
            "description": "A map of vendor name to vendor information."
          },
          "data": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/TaxInformation"
            },
            "example": {
              "W8BENE": {
                "formType": "W8BENE",
                "status": "TAX_APPROVED",
                "statusWhen": "2025-09-29T17:28:31.047Z",
                "statusBy": "COMPLY_EXCHANGE",
                "receivedFrom": "Comply Exchange",
                "receivedWhen": "2025-09-29T17:28:31.047Z",
                "expiresWhen": "2028-12-31",
                "taxTreatyBenefitClaimed": true,
                "chapter3StatusW8": "CORPORATION",
                "chapter4StatusW8": "ACTIVE_NFFE",
                "chapter3Status1042S": "15",
                "chapter4Status1042S": "22"
              }
            },
            "description": "A map of tax status code to tax information."
          }
        }
      },
      "FATCAData": {
        "type": "object",
        "properties": {
          "applicable": {
            "type": "boolean",
            "example": true,
            "description": "Indicates if FATCA data is applicable."
          },
          "applicableFrom": {
            "type": "string",
            "example": "2024-12-12T02:40:18.421371Z",
            "description": "The date and time when FATCA data became applicable."
          },
          "setBy": {
            "type": "string",
            "example": "SYSTEM",
            "description": "The source that set the FATCA data."
          }
        }
      },
      "Vendor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "example": "Comply Exchange",
            "description": "The name of the vendor."
          },
          "taxFormUrl": {
            "type": "string",
            "example": "www.tax.com",
            "description": "The URL to the tax form."
          },
          "formUrlDate": {
            "type": "string",
            "example": "2023-11-01T12:34:56Z",
            "description": "The date when the URL was set."
          }
        }
      },
      "TaxInformation": {
        "type": "object",
        "properties": {
          "formType": {
            "$ref": "#/components/schemas/taxStatusCode"
          },
          "status": {
            "type": "string",
            "example": "TAX_READY",
            "description": "The status of the tax information."
          },
          "statusWhen": {
            "type": "string",
            "example": "2024-08-08",
            "description": "The date and time when the status was set."
          },
          "statusBy": {
            "type": "string",
            "example": "COMPLY_EXCHANGE",
            "description": "The entity that set the status."
          },
          "statusMessage": {
            "type": "string",
            "example": "tax form received",
            "description": "The message associated with the status."
          },
          "receivedFrom": {
            "type": "string",
            "example": "Comply Exchange",
            "description": "The entity from which the information was received."
          },
          "receivedWhen": {
            "type": "string",
            "example": "2014-10-19",
            "description": "The date and time when the information was received."
          },
          "expiresWhen": {
            "type": "string",
            "example": "2027-10-18",
            "description": "The date and time when the information expires."
          },
          "taxTreatyBenefitClaimed": {
            "type": "boolean",
            "example": true,
            "description": "Indicates if a tax treaty benefit was claimed."
          },
          "chapter3Status": {
            "$ref": "#/components/schemas/taxRecipientCode"
          },
          "chapter4Status": {
            "$ref": "#/components/schemas/factaStatus"
          }
        }
      },
      "EntityDirectorsResponseModel": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "684ca44e-1d8d-49f0-bd49-2761eb84df43",
            "description": "The ID of the director"
          },
          "roles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/directorRoleType"
            },
            "description": "List of director roles"
          },
          "title": {
            "type": "string",
            "example": "DevDirector",
            "description": "Title of the director"
          },
          "firstName": {
            "type": "string",
            "example": "Manoj",
            "description": "First name of the director"
          },
          "lastName": {
            "type": "string",
            "example": "Krishna",
            "description": "Last name of the director"
          },
          "percentage": {
            "type": "number",
            "example": 0.25,
            "description": "The percentage of ownership the director has in the institution. Value must be greater than 0 and up to 1 (representing 0-100%), with a maximum of 2 decimal places."
          },
          "controlContact": {
            "type": "boolean",
            "example": true,
            "description": "Indicates if the director is a control contact."
          },
          "kycStatus": {
            "$ref": "#/components/schemas/kycProcessStatus"
          }
        }
      },
      "EntitiesAttributesRequestModel": {
        "type": "object",
        "required": [
          "name",
          "incorporationCountry"
        ],
        "properties": {
          "name": {
            "type": "string",
            "example": "Better Investment",
            "description": "The name of the entity."
          },
          "dba": {
            "type": "string",
            "example": "BI",
            "description": "The doing business as (DBA) name of the entity."
          },
          "incorporationCountry": {
            "type": "string",
            "example": "USA",
            "description": "The country of incorporation."
          },
          "incorporationProvince": {
            "type": "string",
            "example": "NY",
            "description": "The province or state of incorporation."
          },
          "incorporationDate": {
            "type": "string",
            "format": "date",
            "example": "2019-01-01",
            "description": "The date of incorporation."
          }
        }
      },
      "PrimaryAddressRequestModel": {
        "type": "object",
        "required": [
          "street1",
          "city",
          "province",
          "zipcode",
          "country"
        ],
        "properties": {
          "street1": {
            "type": "string",
            "example": "105 Main Street",
            "description": "The first line of the street address."
          },
          "street2": {
            "type": "string",
            "example": "suite 101",
            "description": "The second line of the street address."
          },
          "city": {
            "type": "string",
            "example": "Wilmington",
            "description": "The city of the address."
          },
          "province": {
            "type": "string",
            "example": "DE",
            "description": "The province of the address."
          },
          "zipcode": {
            "type": "string",
            "example": "19801",
            "description": "The postal code of the address."
          },
          "country": {
            "type": "string",
            "example": "USA",
            "description": "The country of the address."
          }
        }
      },
      "AddressResponseModel": {
        "type": "object",
        "description": "Contact details as returned in responses. Address types are keyed uppercase (e.g. PRIMARY), unlike the lowercase keys used in requests.",
        "required": [
          "addresses",
          "phone",
          "email"
        ],
        "properties": {
          "addresses": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/PrimaryAddressRequestModel"
            },
            "example": {
              "PRIMARY": {
                "street1": "123 Main Street",
                "street2": "suite 101",
                "city": "Wilmington",
                "province": "DE",
                "zipcode": "19801",
                "country": "USA"
              }
            },
            "description": "A map of address type to address details. Keys are returned uppercase (e.g. PRIMARY)."
          },
          "phone": {
            "type": "string",
            "example": "+12345678911",
            "description": "The phone number associated with the entity in E.164 format."
          },
          "email": {
            "type": "string",
            "example": "hello@acme.com",
            "description": "The email address associated with the entity."
          },
          "website": {
            "type": "string",
            "example": "www.acme.com",
            "description": "The website associated with the entity."
          }
        }
      },
      "IdentificationsResponse": {
        "type": "object",
        "description": "Entity identification numbers as returned in responses. Keys are uppercase, unlike the lowercase keys used in requests.",
        "properties": {
          "EIN": {
            "type": "string",
            "description": "The Employer Identification Number of the entity.",
            "example": "12-3456789"
          },
          "FTIN": {
            "type": "string",
            "description": "The Foreign Tax Identification Number of the entity.",
            "example": "12-3456789"
          },
          "GIIN": {
            "type": "string",
            "description": "The Global Intermediary Identification Number of the entity.",
            "example": "123456.12345.12.12.123"
          },
          "FTNLO": {
            "type": "boolean",
            "description": "indicates if FTIN is not legally required for the entity.",
            "example": false
          },
          "SSN": {
            "type": "string",
            "description": "Social Security Number of the grantor for trust entity (must be exactly 9 digits with no hyphens).",
            "example": "891234589",
            "pattern": "^\\d{9}$"
          }
        }
      },
      "DisclosureRequestModel": {
        "type": "object",
        "properties": {
          "agreed": {
            "type": "boolean",
            "example": true,
            "description": "Indicates if the disclosure has been agreed to."
          },
          "signedBy": {
            "type": "string",
            "example": "John Doe",
            "description": "The name of the person who signed the disclosure."
          },
          "signedWhen": {
            "type": "string",
            "example": "2024-09-09T15:20:05Z",
            "description": "The date and time when the disclosure was signed."
          }
        }
      },
      "EntityKybResponseModel": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string",
            "example": "KYB_APPROVED",
            "description": "The KYB status of the entity."
          },
          "statusWhen": {
            "type": "string",
            "example": "2024-09-09T15:20:05Z",
            "description": "The date and time when the KYB was done."
          },
          "verificationKey": {
            "type": "string",
            "example": "VERIFICATION_KEY_12345",
            "description": "The verification key provided by the KYB vendor."
          },
          "statusBy": {
            "type": "string",
            "example": "{{partner ID}}",
            "description": "The UUID of who set the KYB status."
          },
          "reasons": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "string",
                  "example": "P201",
                  "description": "The reason code for the KYB status."
                },
                "description": {
                  "type": "string",
                  "example": "KYB has been approved based on information provided by the partner.",
                  "description": "A descriptive message about the reason."
                }
              }
            },
            "description": "A list of reasons associated with the KYB status."
          }
        }
      },
      "EntityDisclosuresModel": {
        "type": "object",
        "properties": {
          "termsOfUse": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "customerAgreement": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "rule14b": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "extendedHoursAgreement": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "marginAgreement": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "fpslAgreement": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          },
          "privacyPolicy": {
            "$ref": "#/components/schemas/DisclosureRequestModel"
          }
        }
      },
      "MonthlyTransactionAmount": {
        "type": "string",
        "example": "$50K_TO_$250K",
        "description": "Anticipated monthly transaction volumes in dollar amount per instrument.",
        "enum": [
          "UNDER_$1K",
          "$1K_TO_$10K",
          "$10K_TO_$50K",
          "$50K_TO_$250K",
          "$250K_TO_$1M",
          "OVER_$1M"
        ]
      },
      "InvestmentExperience": {
        "type": "string",
        "example": "YRS_5_10",
        "description": "The investment experience in years.",
        "enum": [
          "NONE",
          "YRS_1_2",
          "YRS_3_5",
          "YRS_5_10",
          "YRS_10_"
        ]
      },
      "EntityInvestorProfile": {
        "type": "object",
        "properties": {
          "annualRevenue": {
            "type": "number",
            "minimum": 0,
            "example": 1000000,
            "description": "The annual revenue of the entity in USD."
          },
          "netWorthTotal": {
            "type": "number",
            "minimum": 0,
            "example": 5000000,
            "description": "The total net worth of the entity in USD."
          },
          "investmentObjective": {
            "type": "string",
            "example": "GROWTH",
            "description": "The investment objective of the entity.",
            "enum": [
              "CAPITAL_PRESERVATION",
              "INCOME",
              "GROWTH",
              "SPECULATION"
            ]
          },
          "riskTolerance": {
            "type": "string",
            "example": "HIGH",
            "description": "The risk tolerance of the entity.",
            "enum": [
              "LOW",
              "MODERATE",
              "HIGH",
              "SPECULATION"
            ]
          },
          "liquidityNeeds": {
            "type": "string",
            "example": "LOW",
            "description": "The degree to which the entity requires the ability to quickly and easily convert investments into cash without significant loss of value, penalties, or costs.",
            "enum": [
              "IMMEDIATE",
              "SHORT_TERM",
              "MODERATE_TERM",
              "LONG_TERM"
            ]
          },
          "investmentExperience": {
            "$ref": "#/components/schemas/InvestmentExperience"
          },
          "timeHorizon": {
            "type": "string",
            "example": "LONG_TERM",
            "description": "Expected investment duration",
            "enum": [
              "SHORT_TERM",
              "MEDIUM_TERM",
              "LONG_TERM"
            ]
          },
          "equities": {
            "type": "object",
            "properties": {
              "monthlyTransactionAmount": {
                "$ref": "#/components/schemas/MonthlyTransactionAmount"
              },
              "investmentExperience": {
                "$ref": "#/components/schemas/InvestmentExperience"
              }
            },
            "description": "Equity investment profile"
          },
          "fixedIncome": {
            "type": "object",
            "properties": {
              "monthlyTransactionAmount": {
                "$ref": "#/components/schemas/MonthlyTransactionAmount"
              },
              "investmentExperience": {
                "$ref": "#/components/schemas/InvestmentExperience"
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