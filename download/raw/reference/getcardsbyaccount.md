---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# View the details of existing cards by account

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
    "/accounts/{accountId}/cards": {
      "get": {
        "tags": [
          "Cards"
        ],
        "summary": "View the details of existing cards by account",
        "operationId": "getCardsByAccount",
        "parameters": [
          {
            "name": "accountId",
            "in": "path",
            "description": "Account ID",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "statuses",
            "in": "query",
            "description": "Statuses of cards to be retrieved",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "enum": [
                "CREATED",
                "ACTIVE",
                "BLOCKED",
                "SUSPENDED",
                "CANCELLED",
                "EXPIRED"
              ]
            }
          },
          {
            "name": "page",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "size",
            "in": "query",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 20
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Cards returned successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/card.CardPageResponse"
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
      "card.CardResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Card identifier. Maximum of 10 alphanumeric characters",
            "example": "V000000001"
          },
          "holder": {
            "$ref": "#/components/schemas/card.CardHolder",
            "description": "CardHolder"
          },
          "expiry": {
            "type": "string",
            "description": "An ISO 8601 date with year & month components only",
            "example": "2018-12"
          },
          "status": {
            "type": "string",
            "description": "The current state of the card."
          },
          "currency": {
            "type": "string",
            "description": "A 3 letter ISO 4217 code representing the card currency",
            "example": "GBP"
          },
          "limit": {
            "type": "string",
            "description": "Total card authorisation limit",
            "example": "1000.00"
          },
          "maxLimit": {
            "type": "string",
            "description": "Maximum limit which can be set on this card and is the maximum lifetime spend the card can have",
            "example": "4000.00"
          },
          "spend": {
            "type": "string",
            "description": "Current total of all authorisations on this card",
            "example": "250.00"
          },
          "externalRef": {
            "type": "string",
            "description": "Client reference for the newly created card. Maximum of 50 characters.",
            "example": "TTQ_51211"
          },
          "maskedPan": {
            "type": "string",
            "description": "Masked card PAN",
            "example": "527095******3544"
          },
          "cardType": {
            "type": "string",
            "description": "Card product type",
            "example": "Business"
          },
          "cardScheme": {
            "type": "string",
            "description": "Card scheme. MASTERCARD or VISA",
            "example": "MASTERCARD"
          },
          "accountBid": {
            "type": "string",
            "description": "Account identifier",
            "example": "A020N8PD"
          },
          "productId": {
            "type": "string",
            "description": "Product identifier",
            "example": "O210003A"
          },
          "format": {
            "type": "string",
            "description": "The format of the card.  PHYSICAL or VIRTUAL",
            "enum": [
              "PHYSICAL",
              "VIRTUAL"
            ],
            "example": "PHYSICAL"
          },
          "constraints": {
            "$ref": "#/components/schemas/card.CardConstraints",
            "description": "CardConstraints"
          },
          "design": {
            "$ref": "#/components/schemas/card.ProductDesignDetail",
            "description": "External reference for card design. Will only be returned for physical cards"
          },
          "printedName": {
            "type": "string",
            "description": "Name printed on the card. Will only be returned for physical cards. Maximum of 20 alphanumeric characters (including full stop, hyphen, apostrophe, caret and space)"
          },
          "cancellationDate": {
            "type": "string",
            "description": "Date card will be cancelled on",
            "example": "2025-01-01"
          },
          "createdDate": {
            "type": "string",
            "format": "date-time"
          },
          "threeDSecureStatus": {
            "type": "string",
            "deprecated": true,
            "description": "The 3DS status of the card, based on the SMS one time password",
            "enum": [
              "NOT_ENROLLED",
              "ENROLLED",
              "UNENROLLED"
            ],
            "example": "ENROLLED"
          },
          "authentication": {
            "$ref": "#/components/schemas/card.CardThreeDSecureAuthentication",
            "description": "The 3DS authentication method statuses"
          },
          "shippingAddress": {
            "$ref": "#/components/schemas/card.AddressDetail",
            "description": "Shipping address"
          },
          "customFields": {
            "type": "array",
            "description": "Custom fields currently defined for card",
            "items": {
              "$ref": "#/components/schemas/card.CardCustomFieldResponse"
            }
          },
          "authWindow": {
            "$ref": "#/components/schemas/card.AuthorisationWindow",
            "description": "Authorisation window defined for card"
          },
          "channelManagerId": {
            "type": "string",
            "description": "Channel Manager identifier",
            "example": "M883412312"
          },
          "frequencyUsage": {
            "type": "string",
            "description": "Enum that specifies the frequency usage of the card",
            "enum": [
              "SINGLE_USE",
              "MULTI_USE"
            ],
            "example": "SINGLE_USE"
          }
        }
      },
      "card.CardThreeDSecureAuthentication": {
        "type": "object",
        "properties": {
          "otpSmsStatus": {
            "type": "string",
            "description": "The SMS one time password authentication status",
            "enum": [
              "NOT_ENROLLED",
              "ENROLLED",
              "UNENROLLED"
            ],
            "example": "ENROLLED"
          },
          "knowledgeBaseStatus": {
            "type": "string",
            "description": "The knowledge based authentication (KBA) status",
            "enum": [
              "NOT_ENROLLED",
              "ENROLLED",
              "UNENROLLED"
            ],
            "example": "ENROLLED"
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
      "card.CardPageResponse": {
        "type": "object",
        "properties": {
          "content": {
            "type": "array",
            "description": "List of responses on the current page",
            "items": {
              "$ref": "#/components/schemas/card.CardResponse"
            }
          },
          "size": {
            "type": "integer",
            "format": "int32",
            "description": "Page size"
          },
          "totalSize": {
            "type": "integer",
            "format": "int64",
            "description": "Total count"
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "description": "Current page number, 0 based; i.e first-page = 0, second-page = 1"
          },
          "totalPages": {
            "type": "integer",
            "format": "int32",
            "description": "Total pages"
          }
        },
        "required": [
          "content",
          "page",
          "size",
          "totalPages",
          "totalSize"
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
      "card.AuthorisationWindow": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "format": "date-time",
            "description": "Authorisation window start date"
          },
          "endDate": {
            "type": "string",
            "format": "date-time",
            "description": "Authorisation window end date"
          }
        }
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
      "card.CardConstraints": {
        "type": "object",
        "properties": {
          "mccWhitelist": {
            "type": "array",
            "description": "mccWhitelist",
            "example": [
              "1000",
              "1002-3000",
              "5060"
            ],
            "items": {
              "type": "string"
            }
          },
          "authorisation": {
            "$ref": "#/components/schemas/card.AuthorisationConstraints",
            "description": "Authorisation constraints"
          }
        },
        "required": [
          "mccWhitelist"
        ]
      },
      "card.CardCustomFieldResponse": {
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