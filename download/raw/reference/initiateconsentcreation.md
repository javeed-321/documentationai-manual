---
updatedAt: 2026-05-27T12:27:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create a VRP consent

Create a Variable Recurring Payment (VRP) consent for authorisation by the payment service user. The consent can then be used to initiate one or more payments within the payment constraints specified.

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
  "paths": {
    "/vrp-consents": {
      "post": {
        "tags": [
          "Variable Recurring Payments"
        ],
        "summary": "Create a VRP consent",
        "description": "Create a Variable Recurring Payment (VRP) consent for authorisation by the payment service user. The consent can then be used to initiate one or more payments within the payment constraints specified.",
        "operationId": "initiateConsentCreation",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/pispgateway.CreateVrpConsentCreationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/pispgateway.CreateVrpConsentInitiationResponse"
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
                    "$ref": "#/components/schemas/pispgateway.MessageResponse"
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
      "pispgateway.PeriodicLimit": {
        "type": "object",
        "description": "Maximum amount of all payments that can be initiated using this consent in a given period. If the periodAlignment is “Calendar”, the limit is pro-rated in the first period to the remaining number of days.",
        "properties": {
          "currency": {
            "type": "string",
            "description": "Currency of the maximum amount. Must be specified in ISO 4217 format."
          },
          "amount": {
            "type": "number",
            "description": "The maximum amount of all payments initiated using this consent in the specified period. At least one periodic limit is required - '1' = 1.00 GBP",
            "example": "100.00"
          },
          "periodAlignment": {
            "type": "string",
            "description": "Specifies whether the period starts on the date of consent creation or lines up with a calendar."
          },
          "periodType": {
            "type": "string",
            "description": "Period type. Must be one of “DAY”,”WEEK”,”FORTNIGHT”,”MONTH”,”HALF_YEAR”,”YEAR”."
          }
        },
        "required": [
          "currency",
          "periodAlignment",
          "periodType"
        ]
      },
      "pispgateway.CreateVrpConsentCreationRequest": {
        "type": "object",
        "description": "Request object to Initiate VRP Consent Creation",
        "properties": {
          "aspspId": {
            "type": "string",
            "description": "Identifier of the payer’s ASPSP where the consent will be created. The ASPSP must have the \"SWEEPING\" or \"COMMERCIAL\" capability enabled (which can be checked using our API).",
            "example": "H100000001"
          },
          "destination": {
            "$ref": "#/components/schemas/pispgateway.Destination",
            "description": "Destination account details that will receive variable recurring payments initiated using this consent."
          },
          "paymentConstraints": {
            "$ref": "#/components/schemas/pispgateway.PaymentConstraints",
            "description": "Limits that will apply to payments initiated using this consent."
          },
          "validFromDate": {
            "type": "string",
            "format": "date-time",
            "description": "Start date time from which payments can be initiated using this consent. Must be specified using YYYY-MM-DDTHH:mm:ssZ format.",
            "example": "2022-01-31T20:16:01.90Z"
          },
          "validToDate": {
            "type": "string",
            "format": "date-time",
            "description": "End date time after which payments cannot be initiated using this consent. Must be specified using YYYY-MM-DDTHH:mm:ssZ format.",
            "example": "2022-07-31T20:16:01.90Z"
          },
          "type": {
            "type": "string",
            "description": "Type of VRP consent that will be created.",
            "enum": [
              "SWEEPING",
              "CVRP1"
            ]
          },
          "reference": {
            "type": "string",
            "description": "Reference to be used for the Consent. This will appear on the Account statement/the recipient's bank account. Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space.",
            "example": "Invoice ABC123"
          },
          "interactionTypes": {
            "type": "array",
            "description": "List of PSU interaction types permitted under this consent. Mandatory for CVRP consent type. Must be one or both of IN_SESSION (customer is present), OFF_SESSION (customer is not present)",
            "items": {
              "type": "string",
              "enum": [
                "IN_SESSION",
                "OFF_SESSION"
              ]
            }
          },
          "ultimateCreditor": {
            "$ref": "#/components/schemas/pispgateway.UltimateParty",
            "description": "The ultimate beneficiary of the payment, party to which an amount of money is due. To be provided if different from the immediate creditor."
          },
          "ultimateDebtor": {
            "$ref": "#/components/schemas/pispgateway.UltimateParty",
            "description": "The ultimate payer, party that owes an amount of money to the (ultimate) creditor. To be provided if different from the account holder."
          },
          "risk": {
            "$ref": "#/components/schemas/pispgateway.OBRisk",
            "description": "It is used to specify additional details for risk scoring for Payments."
          }
        },
        "required": [
          "aspspId",
          "destination",
          "paymentConstraints",
          "reference",
          "type"
        ]
      },
      "pispgateway.UltimateParty": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name by which a party is known and which is usually used to identify that party.",
            "maxLength": 140,
            "minLength": 1
          },
          "identification": {
            "type": "string",
            "description": "Identification assigned by an institution.",
            "maxLength": 256,
            "minLength": 1
          },
          "lei": {
            "type": "string",
            "description": "Legal entity identification as an alternate identification for a party. Legal Entity Identifier is a code allocated to a party as described in ISO 17442 Financial Services - Legal Entity Identifier (LEI).",
            "maxLength": 20,
            "minLength": 1
          },
          "postalAddress": {
            "$ref": "#/components/schemas/pispgateway.PostalAddress",
            "description": "Information that locates and identifies a specific address, as defined by postal services."
          }
        }
      },
      "pispgateway.PaymentConstraints": {
        "type": "object",
        "description": "Limits that will apply to payments initiated using this consent. ",
        "properties": {
          "maximumIndividualAmount": {
            "$ref": "#/components/schemas/pispgateway.MaximumIndividualVrPayment",
            "description": "Maximum amount of any single payment initiated using this consent."
          },
          "periodicLimits": {
            "type": "array",
            "description": "Maximum amount of all payments that can be initiated using this consent in a given period. If the periodAlignment is “Calendar”, the limit is pro-rated in the first period to the remaining number of days.",
            "items": {
              "$ref": "#/components/schemas/pispgateway.PeriodicLimit"
            }
          }
        },
        "required": [
          "maximumIndividualAmount"
        ]
      },
      "pispgateway.MessageResponse": {
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
      "pispgateway.MaximumIndividualVrPayment": {
        "type": "object",
        "description": "Maximum amount of any single payment initiated using this consent.",
        "properties": {
          "currency": {
            "type": "string",
            "description": "Currency of the maximum individual amount. Must be specified in ISO 4217 format."
          },
          "amount": {
            "type": "number",
            "description": "Maximum amount of any single payment initiated using this consent - '1' = 1.00 GBP",
            "example": "100.00"
          }
        },
        "required": [
          "currency"
        ]
      },
      "pispgateway.Destination": {
        "type": "object",
        "description": "The destination account for the payment",
        "properties": {
          "type": {
            "type": "string",
            "description": "Indicates the type of destination. Can be one of ACCOUNT, SCAN",
            "enum": [
              "ACCOUNT",
              "SCAN"
            ]
          },
          "id": {
            "type": "string",
            "description": "Identifier of the destination account if using ACCOUNT type",
            "example": "A1100001"
          },
          "accountNumber": {
            "type": "string",
            "description": "Account Number of destination account if using SCAN type",
            "example": "12345678",
            "pattern": "^[0-9]{8}$"
          },
          "sortCode": {
            "type": "string",
            "description": "Sort Code of destination account if using SCAN type",
            "example": "000000",
            "pattern": "^[0-9]{6}$"
          },
          "name": {
            "type": "string",
            "description": "Name of destination account if using SCAN type (this may be truncated)",
            "example": "Test",
            "maxLength": 70,
            "minLength": 0
          }
        },
        "required": [
          "type"
        ]
      },
      "pispgateway.CreateVrpConsentInitiationResponse": {
        "type": "object",
        "description": "Response object to Initiate Vrp Consent",
        "properties": {
          "vrpConsentInitiationId": {
            "type": "string",
            "description": "The unique identifier of the VRP consent initiation request at Modulr",
            "example": "E210000004"
          },
          "redirectUrl": {
            "type": "string",
            "description": "A redirect URL for the user to authorise the payment initiation request at the ASPSP",
            "example": "https://www.bankofmoney.com/authorize"
          }
        }
      },
      "pispgateway.PostalAddress": {
        "type": "object",
        "properties": {
          "addressType": {
            "type": "string",
            "description": "Identifies the nature of the postal address. BIZZ (Business), DLVY (Delivery), MLTO (Mail To), PBOX (PO Box), ADDR (Postal), HOME (Residential), CORR (Correspondence), STAT (Statement).",
            "enum": [
              "BIZZ",
              "DLVY",
              "MLTO",
              "PBOX",
              "ADDR",
              "HOME",
              "CORR",
              "STAT"
            ]
          },
          "department": {
            "type": "string",
            "description": "Identification of a division of a large organisation or building.",
            "maxLength": 70,
            "minLength": 1
          },
          "subDepartment": {
            "type": "string",
            "description": "Identification of a sub-division of a large organisation or building.",
            "maxLength": 70,
            "minLength": 1
          },
          "streetName": {
            "type": "string",
            "description": "Name of a street or thoroughfare.",
            "maxLength": 140,
            "minLength": 1
          },
          "buildingNumber": {
            "type": "string",
            "description": "Number that identifies the position of a building on a street.",
            "maxLength": 16,
            "minLength": 1
          },
          "buildingName": {
            "type": "string",
            "description": "Name of a referenced building.",
            "maxLength": 140,
            "minLength": 1
          },
          "floor": {
            "type": "string",
            "description": "Number that identifies the level within a building.",
            "maxLength": 70,
            "minLength": 1
          },
          "unitNumber": {
            "type": "string",
            "description": "Number that identifies the unit of a specific address.",
            "maxLength": 16,
            "minLength": 1
          },
          "room": {
            "type": "string",
            "description": "Information that locates and identifies a room to form part of an address.",
            "maxLength": 70,
            "minLength": 1
          },
          "postBox": {
            "type": "string",
            "description": "Information that locates and identifies a box in a post office assigned to a person or organization, where letters for them are kept until called for.",
            "maxLength": 16,
            "minLength": 1
          },
          "townLocationName": {
            "type": "string",
            "description": "Name of a built-up area, with defined boundaries, and a local government.",
            "maxLength": 140,
            "minLength": 1
          },
          "districtName": {
            "type": "string",
            "description": "Number that of the regional area, known as a district, which forms part of an address.",
            "maxLength": 140,
            "minLength": 1
          },
          "careOf": {
            "type": "string",
            "description": "The 'care of' address is used whenever sending mail to a person or organisation who does not actually live or work at the address. They will receive the mail for the individual.",
            "maxLength": 140,
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "description": "Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail.",
            "maxLength": 16,
            "minLength": 1
          },
          "townName": {
            "type": "string",
            "description": "Name of a built-up area, with defined boundaries, and a local government.",
            "maxLength": 140,
            "minLength": 1
          },
          "countrySubDivision": {
            "type": "string",
            "description": "Identifies a subdivision of a country such as state, region, county.",
            "maxLength": 35,
            "minLength": 1
          },
          "country": {
            "type": "string",
            "description": "Nation with its own government, as an ISO 3166-1 alpha-2 country code.",
            "example": "GB",
            "pattern": "^[A-Z]{2,2}$"
          },
          "addressLine": {
            "type": "array",
            "description": "Information that locates and identifies a specific address, as defined by postal services, presented in free format text. Maximum 7 lines, each up to 70 characters.",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "pispgateway.OBRisk": {
        "type": "object",
        "properties": {
          "merchantCategoryCode": {
            "type": "string",
            "description": "Category code conforming to ISO 18245, related to the type of services or goods the merchant provides.",
            "maxLength": 4,
            "minLength": 3
          },
          "merchantCustomerIdentification": {
            "type": "string",
            "description": "The unique customer identifier of the PSU with the merchant.",
            "maxLength": 70,
            "minLength": 1
          },
          "contractPresentIndicator": {
            "type": "boolean",
            "description": "Indicates if Payee has a contractual relationship with the PISP."
          },
          "beneficiaryPrepopulatedIndicator": {
            "type": "boolean",
            "description": "Indicates if PISP has immutably prepopulated payment details for the PSU."
          },
          "beneficiaryAccountType": {
            "type": "string",
            "description": "Specifies the extended type of beneficiary account if known.",
            "enum": [
              "Business",
              "BusinessSavingsAccount",
              "Charity",
              "Collection",
              "Corporate",
              "Ewallet",
              "Government",
              "Investment",
              "ISA",
              "JointPersonal",
              "Pension",
              "Personal",
              "PersonalSavingsAccount",
              "Premier",
              "Wealth"
            ]
          },
          "deliveryAddress": {
            "$ref": "#/components/schemas/pispgateway.PostalAddress",
            "description": "Information that locates and identifies a delivery address."
          }
        },
        "required": [
          "beneficiaryPrepopulatedIndicator",
          "contractPresentIndicator",
          "merchantCategoryCode",
          "merchantCustomerIdentification"
        ]
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