---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create a new physical card

Asynchronously create a physical card. The response will include a resource to allow the client to check the status of the request.

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
      "name": "Cards",
      "description": "Cards API"
    }
  ],
  "paths": {
    "/accounts/{accountId}/physical-cards": {
      "post": {
        "tags": [
          "Cards"
        ],
        "summary": "Create a new physical card",
        "description": "Asynchronously create a physical card. The response will include a resource to allow the client to check the status of the request.",
        "operationId": "createPhysicalCard",
        "parameters": [
          {
            "name": "accountId",
            "in": "path",
            "description": "The account which card funds will be raised from.",
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
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/card.CreatePhysicalCardRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "description": "Create physical card request received successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.AsyncTaskCreatedResponse"
                }
              }
            }
          },
          "400": {
            "description": "Invalid request",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/card.MessageResponse"
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
      "card.AuthorisationWindowRequest": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "example": "2025-01-01"
          },
          "endDate": {
            "type": "string",
            "example": "2025-01-01"
          }
        }
      },
      "card.AuthorisationConstraints": {
        "type": "object",
        "description": "Authorisation constraints",
        "properties": {
          "spend": {
            "type": "array",
            "description": "Spending constraints",
            "items": {
              "$ref": "#/components/schemas/card.SpendConstraintDetail"
            }
          }
        }
      },
      "card.Constraints": {
        "type": "object",
        "properties": {
          "authorisation": {
            "$ref": "#/components/schemas/card.AuthorisationConstraints",
            "description": "Authorisation constraints"
          }
        }
      },
      "card.CardCustomFieldRequest": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Custom field key"
          },
          "value": {
            "type": "string",
            "description": "Custom field value"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "card.CreatePhysicalCardRequest": {
        "type": "object",
        "description": "Card",
        "properties": {
          "limit": {
            "type": "number",
            "format": "double",
            "description": "Total card authorisation limit.",
            "example": "1000.00",
            "maximum": 99999999.99,
            "minimum": 1
          },
          "expiry": {
            "type": "string",
            "description": "ISO 8601 date with year & month components only. The supplied value must be in the future (cannot be the current month) and is _inclusive_ of the specified month.",
            "example": "2018-12"
          },
          "productCode": {
            "type": "string",
            "description": "Identifies the _type_ of card to create (GBP consumer, GBP business, etc). Modulr will supply a list of possible values."
          },
          "externalRef": {
            "type": "string",
            "description": "Client reference for the newly created card. Maximum of 50 alphanumeric characters (including underscore, hyphen and space).",
            "maxLength": 50,
            "minLength": 1,
            "pattern": "[\\w -]*"
          },
          "constraints": {
            "$ref": "#/components/schemas/card.Constraints",
            "description": "Constraints"
          },
          "authentication": {
            "$ref": "#/components/schemas/card.CardAuthentication",
            "description": "Authentication. Required by default, optional for Virtual Business Travel Cards only"
          },
          "cancellationDate": {
            "type": "string",
            "description": "Date for card to be cancelled on",
            "example": "2025-01-01"
          },
          "customFields": {
            "type": "array",
            "description": "Custom fields of card",
            "items": {
              "$ref": "#/components/schemas/card.CardCustomFieldRequest"
            },
            "maxItems": 20,
            "minItems": 0
          },
          "authorisationWindow": {
            "$ref": "#/components/schemas/card.AuthorisationWindowRequest",
            "description": "Authorisation Windows allow the card holder to add a period of time where the card can ONLY be used, if an Authorisation Window set then transactions outside this window will decline. ISO 8601 date with year, month & day components only."
          },
          "frequencyUsage": {
            "type": "string",
            "enum": [
              "SINGLE_USE",
              "MULTI_USE"
            ]
          },
          "holder": {
            "$ref": "#/components/schemas/card.CardHolder",
            "description": "CardHolder"
          },
          "shippingAddress": {
            "$ref": "#/components/schemas/card.AddressDetail",
            "description": "Add a Shipping address if you wish the card to be sent to an address other than the billing address"
          },
          "design": {
            "$ref": "#/components/schemas/card.ProductDesignDetail",
            "description": "Design references for card and packaging"
          },
          "printedName": {
            "type": "string",
            "description": "Name to be printed on the card. Maximum of 27 alphanumeric characters (including full stop, hyphen, apostrophe, caret and space). Please add business name to this field if you wish to have it on the card.",
            "example": "Joe Bloggs",
            "maxLength": 27,
            "minLength": 1,
            "pattern": "[a-zA-Z 0-9À-ŽȘȚ'’.,^-]{1,27}"
          }
        },
        "required": [
          "design",
          "expiry",
          "externalRef",
          "limit",
          "printedName",
          "productCode"
        ]
      },
      "card.SpendConstraintDetail": {
        "type": "object",
        "description": "Spending constraints",
        "properties": {
          "currency": {
            "type": "string",
            "description": "A 3 letter ISO 4217 code representing the transaction currency",
            "enum": [
              "GBP",
              "EUR",
              "AED",
              "AFN",
              "ALL",
              "AMD",
              "ANG",
              "AOA",
              "ARS",
              "AUD",
              "AWG",
              "AZN",
              "BAM",
              "BBD",
              "BDT",
              "BGN",
              "BHD",
              "BIF",
              "BMD",
              "BND",
              "BOB",
              "BOV",
              "BRL",
              "BSD",
              "BTN",
              "BWP",
              "BYN",
              "BZD",
              "CAD",
              "CDF",
              "CHE",
              "CHF",
              "CHW",
              "CLF",
              "CLP",
              "CNY",
              "COP",
              "COU",
              "CRC",
              "CUC",
              "CUP",
              "CVE",
              "CZK",
              "DJF",
              "DKK",
              "DOP",
              "DZD",
              "EGP",
              "ERN",
              "ETB",
              "FJD",
              "FKP",
              "GEL",
              "GHS",
              "GIP",
              "GMD",
              "GNF",
              "GTQ",
              "GYD",
              "HKD",
              "HNL",
              "HRK",
              "HTG",
              "HUF",
              "IDR",
              "ILS",
              "INR",
              "IQD",
              "IRR",
              "ISK",
              "JMD",
              "JOD",
              "JPY",
              "KES",
              "KGS",
              "KHR",
              "KMF",
              "KPW",
              "KRW",
              "KWD",
              "KYD",
              "KZT",
              "LAK",
              "LBP",
              "LKR",
              "LRD",
              "LSL",
              "LYD",
              "MAD",
              "MDL",
              "MGA",
              "MKD",
              "MMK",
              "MNT",
              "MOP",
              "MRU",
              "MUR",
              "MVR",
              "MWK",
              "MXN",
              "MXV",
              "MYR",
              "MZN",
              "NAD",
              "NGN",
              "NIO",
              "NOK",
              "NPR",
              "NZD",
              "OMR",
              "PAB",
              "PEN",
              "PGK",
              "PHP",
              "PKR",
              "PLN",
              "PYG",
              "QAR",
              "RON",
              "RSD",
              "RUB",
              "RWF",
              "SAR",
              "SBD",
              "SCR",
              "SDG",
              "SEK",
              "SGD",
              "SLE",
              "SLL",
              "SOS",
              "SRD",
              "SSP",
              "STN",
              "SVC",
              "SYP",
              "SZL",
              "SHP",
              "THB",
              "TJS",
              "TMT",
              "TND",
              "TOP",
              "TRY",
              "TTD",
              "TWD",
              "TZS",
              "UAH",
              "UGX",
              "USD",
              "USN",
              "UYI",
              "UYU",
              "UYW",
              "UZS",
              "VES",
              "VND",
              "VUV",
              "WST",
              "XAF",
              "XAG",
              "XAU",
              "XBA",
              "XBB",
              "XBC",
              "XBD",
              "XCD",
              "XDR",
              "XOF",
              "XPD",
              "XPF",
              "XPT",
              "XSU",
              "XTS",
              "XUA",
              "XXX",
              "YER",
              "ZAR",
              "ZMW",
              "ZWL"
            ],
            "example": "GBP"
          },
          "min": {
            "type": "number",
            "description": "Minimum spend amount (inclusive)",
            "example": "5.00"
          },
          "max": {
            "type": "number",
            "description": "Maximum spend amount (inclusive)",
            "example": "2000.00"
          }
        },
        "required": [
          "currency"
        ]
      },
      "card.AddressDetail": {
        "type": "object",
        "description": "Address details for the cardholder. Optional for individual customers whose partner has verification type EXTERNAL.",
        "properties": {
          "addressLine1": {
            "type": "string",
            "description": "First line of address",
            "example": "Floor 10",
            "maxLength": 50,
            "minLength": 1
          },
          "addressLine2": {
            "type": "string",
            "description": "Second line of address",
            "example": "80 George Street",
            "maxLength": 50,
            "minLength": 0
          },
          "postTown": {
            "type": "string",
            "description": "Post town",
            "example": "EDINBURGH",
            "maxLength": 20,
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "description": "Postcode",
            "example": "EH2 3BU",
            "maxLength": 10,
            "minLength": 1
          },
          "country": {
            "type": "string",
            "description": "Country (ISO 3166 alpha-2 country code)",
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
              "AX",
              "AW",
              "BL",
              "CW",
              "GF",
              "GL",
              "GP",
              "ME",
              "MF",
              "MQ",
              "NC",
              "PF",
              "PM",
              "RE",
              "SX",
              "TF",
              "WF",
              "YT",
              "AI",
              "BM",
              "FK",
              "GB",
              "GG",
              "GI",
              "GS",
              "IO",
              "JE",
              "KY",
              "MS",
              "PN",
              "SH",
              "TC",
              "VG"
            ],
            "example": "GB",
            "minLength": 1
          }
        },
        "required": [
          "addressLine1",
          "country",
          "postCode",
          "postTown"
        ]
      },
      "card.ProductDesignDetail": {
        "type": "object",
        "properties": {
          "cardRef": {
            "type": "string",
            "description": "Design reference for card",
            "minLength": 1
          },
          "packagingRef": {
            "type": "string",
            "description": "Design reference for card packaging",
            "minLength": 1
          }
        },
        "required": [
          "cardRef",
          "packagingRef"
        ]
      },
      "card.CardKnowledgeBasedAuthentication": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "3DS knowledge-based authentication answer type",
            "enum": [
              "FIRST_PET_NAME",
              "MATERNAL_GRANDMOTHER_MAIDEN_NAME",
              "FAVOURITE_CHILDHOOD_FRIEND",
              "FIRST_CAR",
              "CITY_PARENTS_MET"
            ]
          },
          "answer": {
            "type": "string",
            "description": "3DS knowledge-based authentication answer",
            "maxLength": 45,
            "minLength": 1
          }
        },
        "required": [
          "answer",
          "type"
        ]
      },
      "card.CardHolder": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "Cardholder title is optional for all card types. Maximum of 4 alphanumeric characters.",
            "example": "Mr",
            "pattern": "^[0-9a-zA-Z]{1,4}$"
          },
          "firstName": {
            "type": "string",
            "description": "Cardholder first name. Maximum of 20 alphanumeric characters including space, hyphen and apostrophe. Optional for individual customers whose partner has verification type EXTERNAL and for Virtual Business customers.",
            "example": "Joe",
            "pattern": "^[A-Za-z0-9ÄÖÜäöü/.'^ -]{1,20}$"
          },
          "lastName": {
            "type": "string",
            "description": "Cardholder last name. Maximum of 20 alphanumeric characters including space, hyphen and apostrophe. Optional for individual customers whose partner has verification type EXTERNAL and for Virtual Business customers.",
            "example": "Bloggs",
            "pattern": "^[A-Za-z0-9ÄÖÜäöü/.'^ -]{1,20}$"
          },
          "billingAddress": {
            "$ref": "#/components/schemas/card.AddressDetail",
            "description": "Billing address for the cardholder. Optional for individual customers whose partner has verification type EXTERNAL."
          },
          "dateOfBirth": {
            "type": "string",
            "format": "date",
            "description": "Cardholder date of birth. Must match date format of yyyy-mm-dd. Required for virtual consumer and physical cards. Optional for individual customers.",
            "example": "2001-01-01"
          },
          "mobileNumber": {
            "type": "string",
            "description": "Cardholder mobile number. Must start with a '+', followed by the country code and then the mobile number. Required for virtual consumer and physical cards.",
            "example": "+447123456000"
          },
          "email": {
            "type": "string",
            "format": "email",
            "description": "Cardholder email",
            "example": "cardholder@example.com",
            "maxLength": 50,
            "minLength": 0
          }
        },
        "required": [
          "firstName",
          "lastName"
        ]
      },
      "card.MessageResponse": {
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
      "card.CardAuthentication": {
        "type": "object",
        "properties": {
          "knowledgeBase": {
            "type": "array",
            "description": "3DS knowledge-based authentication (KBA) answers",
            "items": {
              "$ref": "#/components/schemas/card.CardKnowledgeBasedAuthentication"
            },
            "minItems": 1
          }
        },
        "required": [
          "knowledgeBase"
        ]
      },
      "card.AsyncTaskCreatedResponse": {
        "type": "object",
        "properties": {
          "taskUrl": {
            "type": "string",
            "description": "Url of card task resource"
          },
          "taskId": {
            "type": "string",
            "description": "ID of card task"
          },
          "metaData": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "description": "Meta data associated with async task response"
          }
        },
        "required": [
          "taskId",
          "taskUrl"
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