---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Edit a customer

Edit details of a particular customer using its ID as a reference. Current editable fields: complianceData

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
      "name": "Customers",
      "description": "Operations on Customers"
    }
  ],
  "paths": {
    "/customers/{customerId}": {
      "patch": {
        "tags": [
          "Customers"
        ],
        "summary": "Edit a customer",
        "description": "Edit details of a particular customer using its ID as a reference. Current editable fields: complianceData",
        "operationId": "patchCustomer",
        "parameters": [
          {
            "name": "customerId",
            "in": "path",
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
            "application/json-patch+json": {
              "schema": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/account.Add"
                    },
                    {
                      "$ref": "#/components/schemas/account.Copy"
                    },
                    {
                      "$ref": "#/components/schemas/account.Move"
                    },
                    {
                      "$ref": "#/components/schemas/account.Remove"
                    },
                    {
                      "$ref": "#/components/schemas/account.Replace"
                    },
                    {
                      "$ref": "#/components/schemas/account.Test"
                    }
                  ]
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successfully updated the existing customer",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/account.Customer"
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
      "account.ScreeningResultsResponse": {
        "type": "object",
        "properties": {
          "adverseMedia": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "peps": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "sanctions": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "account.JsonNode": {},
      "account.Copy": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "from": {
                "type": "string",
                "example": "/path/to/originating/field"
              }
            }
          }
        ],
        "description": "Copy field",
        "required": [
          "from",
          "op",
          "path"
        ]
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
      },
      "account.Remove": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          }
        ],
        "description": "Remove field",
        "required": [
          "op",
          "path"
        ]
      },
      "account.Customer": {
        "type": "object",
        "description": "A Customer is a single legal entity that can have 1 or more accounts",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for a Customer. Begins with 'C'",
            "example": "C00000001"
          },
          "name": {
            "type": "string",
            "description": "Customer's company name - must be unique across the Modulr platform."
          },
          "brandNames": {
            "type": "array",
            "description": "The customers brand name(s)",
            "items": {
              "$ref": "#/components/schemas/account.BrandNameResponse"
            }
          },
          "type": {
            "type": "string",
            "description": "Type of the customer, can be one of:\n1. LLC -> limited company\n2. PLC -> publicly listed company\n3. SOLETRADER -> sole trader\n4. OPARTNRSHP -> ordinary partnership\n5. LPARTNRSHP -> limited partnership\n6. LLP -> limited liability partnership\n7. INDIVIDUAL -> individual consumer\n8. PCM_INDIVIDUAL -> partner clearing model individual consumer\n9. PCM_BUSINESS -> partner clearing model business consumer"
          },
          "status": {
            "type": "string",
            "description": "Status of the Customer. Customers must be 'Active' for Accounts to be created for them.",
            "enum": [
              "ACTIVE",
              "CLOSED",
              "BLOCKED"
            ]
          },
          "verificationStatus": {
            "type": "string",
            "description": "How the identity of the Customer has been verified. Can be:\n1. UNVERIFIED -> no verification checks have been completed\n2. VERIFIED -> verification checks completed satisfactorily\n3. EXVERIFIED -> verification completed externally\n4. REFERRED -> verification is pending manual review\n5. DECLINED -> verification is complete with a negative result\n6. REVIEWED -> verification check has been reviewed"
          },
          "companyRegNumber": {
            "type": "string",
            "description": "The company registration / incorporation number of the company. Only applicable for companies registered with Companies House"
          },
          "expectedMonthlySpend": {
            "type": "integer",
            "format": "int32",
            "description": "Indication of the monthly spend of the customer."
          },
          "registeredAddress": {
            "$ref": "#/components/schemas/account.AddressResponse",
            "description": "The address of the company's registered office."
          },
          "tradingAddress": {
            "$ref": "#/components/schemas/account.AddressResponse",
            "description": "The address of the company's day-to-day trading activities."
          },
          "partnerId": {
            "type": "string",
            "description": "The owning partner identifier"
          },
          "associates": {
            "type": "array",
            "description": "Array of associate objects that link to the Customer. For example, this could contain the details of the company directors for a Limited company, or or the partners for a partnership.",
            "items": {
              "$ref": "#/components/schemas/account.AssociateResponse"
            }
          },
          "industryCode": {
            "type": "string"
          },
          "tcsVersion": {
            "type": "integer",
            "format": "int32",
            "description": "Version of the Modulr Account Terms and Conditions the Customer has agreed to."
          },
          "documentInfo": {
            "type": "array",
            "description": "Array of document objects that relate to the Customer being created. Examples of Documents could be proof of a Company Director's identity or address, Articles of Association or a Partnership Agreement.",
            "items": {
              "$ref": "#/components/schemas/account.DocumentInfo"
            }
          },
          "externalReference": {
            "type": "string"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime when the customer was created.Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "delegate": {
            "$ref": "#/components/schemas/account.DelegateResponse",
            "description": "Details of this Customer's linked Delegate"
          },
          "legalEntity": {
            "type": "string",
            "description": "Legal entity of the customer",
            "enum": [
              "GB",
              "NL",
              "IE"
            ]
          },
          "customerTrust": {
            "$ref": "#/components/schemas/account.CustomerTrustResponse",
            "description": "Trust nature for customers of type trust. Mandatory for type Trust, not to be set for non-trust customers."
          },
          "taxProfile": {
            "$ref": "#/components/schemas/account.CustomerTaxProfileResponse",
            "description": "Tax profile for customers of type SOLETRADER. Optional for type SOLETRADER, not to be set for non-SOLETRADER customers."
          },
          "complianceData": {
            "$ref": "#/components/schemas/account.CustomerComplianceDataResponse",
            "description": "Required for customers of type PREQUALIFIED. Not allowed for all other customer types."
          },
          "complianceSector": {
            "type": "string",
            "example": "Agency Lite Consumer"
          },
          "generateStatements": {
            "type": "boolean",
            "description": "True if the customer is configured to generate statements"
          }
        }
      },
      "account.Move": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "from": {
                "type": "string",
                "example": "/path/to/originating/field"
              }
            }
          }
        ],
        "description": "Move field",
        "required": [
          "from",
          "op",
          "path"
        ]
      },
      "account.DelegateResponse": {
        "type": "object",
        "description": "Delegate",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique reference for the Delegate.",
            "example": "D0000001"
          },
          "name": {
            "type": "string",
            "description": "Name for the Delegate"
          },
          "address": {
            "$ref": "#/components/schemas/account.AddressResponse",
            "description": "Address of the Delegate"
          },
          "roleId": {
            "type": "string",
            "description": "The id of the Role assigned to the delegate",
            "example": "R02002M5"
          },
          "externalReference": {
            "type": "string",
            "description": "External system reference for the Delegate"
          },
          "partner": {
            "type": "string",
            "description": "Partner Bid.",
            "example": "R0000001"
          },
          "status": {
            "type": "string",
            "description": "Status of the Delegate."
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime the Delegate was created.Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          },
          "updated": {
            "type": "string",
            "format": "date-time",
            "description": "Datetime the Delegate was last updated.Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000"
          }
        }
      },
      "account.Test": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "value": {
                "$ref": "#/components/schemas/account.JsonNode"
              }
            }
          }
        ],
        "description": "Test field",
        "required": [
          "op",
          "path",
          "value"
        ]
      },
      "account.CustomerComplianceDataResponse": {
        "type": "object",
        "properties": {
          "typeDescription": {
            "type": "string"
          },
          "riskLevel": {
            "type": "string",
            "enum": [
              "LOW",
              "MEDIUM",
              "HIGH",
              "UNDETERMINED"
            ]
          },
          "vulnerabilityReasons": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "LIFE_EVENTS",
                "HEALTH",
                "RESILIENCE",
                "CAPABILITY",
                "FINANCIAL_DIFFICULTY"
              ]
            }
          },
          "business": {
            "$ref": "#/components/schemas/account.BusinessDataResponse"
          },
          "consumer": {
            "$ref": "#/components/schemas/account.ConsumerDataResponse"
          }
        }
      },
      "account.PatchOperation": {
        "type": "object",
        "discriminator": {
          "propertyName": "op",
          "mapping": {
            "add": "#/components/schemas/account.Add",
            "move": "#/components/schemas/account.Move",
            "test": "#/components/schemas/account.Test",
            "replace": "#/components/schemas/account.Replace",
            "copy": "#/components/schemas/account.Copy",
            "remove": "#/components/schemas/account.Remove"
          }
        },
        "properties": {
          "op": {
            "type": "string"
          },
          "path": {
            "type": "string",
            "example": "/path/to/field"
          }
        },
        "required": [
          "op",
          "path"
        ]
      },
      "account.AssociateComplianceDataResponse": {
        "type": "object",
        "properties": {
          "relationship": {
            "type": "string"
          }
        }
      },
      "account.ConsumerDataResponse": {
        "type": "object",
        "properties": {
          "employment": {
            "type": "string"
          },
          "natureOfRelationship": {
            "type": "string"
          },
          "expectedTransactionalActivity": {
            "$ref": "#/components/schemas/account.ExpectedTransactionalActivityResponse"
          },
          "screeningResults": {
            "$ref": "#/components/schemas/account.ScreeningResultsResponse"
          },
          "sourceOfWealth": {
            "$ref": "#/components/schemas/account.SourceOfWealthResponse"
          }
        }
      },
      "account.AdditionalPersonalIdentifierResponse": {
        "type": "object",
        "description": "AdditionalPersonalIdentifier",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of Additional Personal Identifier",
            "enum": [
              "BSN"
            ]
          },
          "value": {
            "type": "string",
            "description": "Additional Personal Identifier value"
          }
        }
      },
      "account.Replace": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "value": {
                "$ref": "#/components/schemas/account.JsonNode"
              }
            }
          }
        ],
        "description": "Replace field",
        "required": [
          "op",
          "path",
          "value"
        ]
      },
      "account.CustomerTrustResponse": {
        "type": "object",
        "properties": {
          "trustNature": {
            "type": "string",
            "enum": [
              "BARE_TRUSTS",
              "INTEREST_IN_POSSESSION_TRUSTS",
              "DISCRETIONARY_TRUSTS",
              "ACCUMULATION_TRUSTS",
              "MIXED_TRUSTS",
              "SETTLOR_INTERESTED_TRUSTS",
              "NON_RESIDENT_TRUSTS",
              "OFFSHORE_TRUSTS",
              "FAMILY_LIVING_TRUST",
              "PILOT_TRUST",
              "VULNERABLE_BENEFICIARY_TRUST",
              "CHARITABLE_TRUSTS",
              "IRREVOCABLE_LIFE_INSURANCE_TRUST",
              "TESTAMENTARY_TRUSTS",
              "OTHER"
            ]
          }
        }
      },
      "account.AddressResponse": {
        "type": "object",
        "description": "Address",
        "properties": {
          "addressLine1": {
            "type": "string"
          },
          "addressLine2": {
            "type": "string"
          },
          "postTown": {
            "type": "string"
          },
          "postCode": {
            "type": "string"
          },
          "country": {
            "type": "string"
          },
          "countrySubDivision": {
            "type": "string"
          }
        }
      },
      "account.Add": {
        "allOf": [
          {
            "$ref": "#/components/schemas/account.PatchOperation"
          },
          {
            "type": "object",
            "properties": {
              "value": {
                "$ref": "#/components/schemas/account.JsonNode"
              }
            }
          }
        ],
        "description": "Add field",
        "required": [
          "op",
          "path",
          "value"
        ]
      },
      "account.BusinessDataResponse": {
        "type": "object",
        "properties": {
          "natureOfRelationship": {
            "type": "string"
          },
          "expectedTransactionalActivity": {
            "$ref": "#/components/schemas/account.ExpectedTransactionalActivityResponse"
          },
          "screeningResults": {
            "$ref": "#/components/schemas/account.ScreeningResultsResponse"
          },
          "sourceOfWealth": {
            "$ref": "#/components/schemas/account.SourceOfWealthResponse"
          }
        }
      },
      "account.ExpectedTransactionalActivityResponse": {
        "type": "object",
        "properties": {
          "sourceOfFunds": {
            "type": "string"
          },
          "monthlyVolume": {
            "type": "integer",
            "format": "int32"
          },
          "outboundPaymentJurisdictions": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "AT",
                "BE",
                "BG",
                "CY",
                "CZ",
                "DK",
                "EE",
                "FI",
                "FR",
                "DE",
                "GR",
                "HR",
                "HU",
                "IS",
                "IE",
                "IT",
                "LV",
                "LI",
                "LT",
                "LU",
                "MT",
                "NL",
                "NO",
                "PL",
                "PT",
                "RO",
                "SK",
                "SI",
                "ES",
                "SE",
                "GB",
                "MQ",
                "YT",
                "GP",
                "GF",
                "RE",
                "MF",
                "GI",
                "GG",
                "IM",
                "JE",
                "MC",
                "CH",
                "AD",
                "SM",
                "VA",
                "AX",
                "PM",
                "BL",
                "AL",
                "MD",
                "ME",
                "MK",
                "RS",
                "AF",
                "DZ",
                "AS",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BQ",
                "BA",
                "BW",
                "BV",
                "BR",
                "IO",
                "VG",
                "BN",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CK",
                "CR",
                "CU",
                "CW",
                "CD",
                "DJ",
                "DM",
                "DO",
                "TL",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "SZ",
                "ET",
                "FK",
                "FO",
                "FJ",
                "PF",
                "TF",
                "GA",
                "GM",
                "GE",
                "GH",
                "GL",
                "GD",
                "GU",
                "GT",
                "GN",
                "GW",
                "GY",
                "HT",
                "HM",
                "HN",
                "HK",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IL",
                "CI",
                "JM",
                "JP",
                "JO",
                "KZ",
                "KE",
                "KI",
                "XK",
                "KW",
                "KG",
                "LA",
                "LB",
                "LS",
                "LR",
                "LY",
                "MO",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MH",
                "MR",
                "MU",
                "MX",
                "FM",
                "MN",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "NF",
                "KP",
                "MP",
                "OM",
                "PK",
                "PW",
                "PS",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PR",
                "QA",
                "CG",
                "RU",
                "RW",
                "SH",
                "KN",
                "LC",
                "VC",
                "WS",
                "ST",
                "SA",
                "SN",
                "SC",
                "SL",
                "SG",
                "SX",
                "SB",
                "SO",
                "ZA",
                "KR",
                "GS",
                "SS",
                "LK",
                "SD",
                "SR",
                "SY",
                "SJ",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "UG",
                "UA",
                "AE",
                "UM",
                "US",
                "UY",
                "UZ",
                "VU",
                "VE",
                "VN",
                "VI",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW"
              ]
            }
          }
        }
      },
      "account.AssociateResponse": {
        "type": "object",
        "description": "Associate",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for the Associate"
          },
          "firstName": {
            "type": "string",
            "description": "Associate's first name(s)"
          },
          "middleName": {
            "type": "string",
            "description": "Associate's middle name"
          },
          "lastName": {
            "type": "string",
            "description": "Associate's surname"
          },
          "email": {
            "type": "string",
            "description": "Associate's email address"
          },
          "phone": {
            "type": "string",
            "description": "Associate's phone number, in international number format"
          },
          "applicant": {
            "type": "boolean",
            "description": "Indicates which Associate originally applied for the Modulr account"
          },
          "ownership": {
            "type": "integer",
            "format": "int32",
            "description": "The Associate's percentage ownership of the Customer"
          },
          "type": {
            "type": "string",
            "description": "Describes the relation between the Associate and the Customer. Can be one of "
          },
          "dateOfBirth": {
            "type": "string",
            "description": "Associate's date of birth in format yyyy-MM-dd, or format yyyy-MM where day is unknown"
          },
          "verificationStatus": {
            "type": "string",
            "description": "How the Associate was verified. Can be one of "
          },
          "homeAddress": {
            "$ref": "#/components/schemas/account.AddressResponse",
            "description": "Home address of the Associate"
          },
          "documentInfo": {
            "type": "array",
            "description": "Documents gathered during Customer Due Diligence checks on an Associate.",
            "items": {
              "$ref": "#/components/schemas/account.DocumentInfo"
            }
          },
          "additionalPersonalIdentifiers": {
            "type": "array",
            "description": "Additional personal identifier(s)",
            "items": {
              "$ref": "#/components/schemas/account.AdditionalPersonalIdentifierResponse"
            }
          },
          "complianceData": {
            "$ref": "#/components/schemas/account.AssociateComplianceDataResponse",
            "description": "Optional for associates of type C_INTEREST and an EU customer legal entity. Mandatory for associates of type PREQUALIFIED. Not to be set for other associate types and/or for UK customer legal entity."
          }
        }
      },
      "account.DocumentInfo": {
        "type": "object",
        "description": "Document",
        "properties": {
          "path": {
            "type": "string",
            "minLength": 1
          },
          "fileName": {
            "type": "string",
            "minLength": 1
          },
          "uploadedDate": {
            "type": "string",
            "description": "Valid date. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' where Z is UTC offset. e.g 2017-01-28T01:01:01+0000",
            "example": "2017-01-28T01:01:01+0000",
            "minLength": 1
          }
        },
        "required": [
          "fileName",
          "path",
          "uploadedDate"
        ]
      },
      "account.BrandNameResponse": {
        "type": "object",
        "description": "BrandName",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique id for the Brand Name"
          },
          "name": {
            "type": "string",
            "description": "The Brand Name"
          }
        }
      },
      "account.CustomerTaxProfileResponse": {
        "type": "object",
        "properties": {
          "taxIdentifier": {
            "type": "string",
            "description": "Tax identifier for customers of type SOLETRADER. Optional for type SOLETRADER, not to be set for non-SOLETRADER customers."
          }
        }
      },
      "account.SourceOfWealthResponse": {
        "type": "object",
        "properties": {
          "standard": {
            "type": "string"
          },
          "pep": {
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