---
updatedAt: 2026-05-27T10:50:49.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Add an individual/associated entity to an Onboarding Application

Creates a new individual/associated entity with a unique identifier to the specified application, capturing key details such as name, date of birth, address etc.

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
    "/applications/{applicationId}/compliance/associates": {
      "post": {
        "tags": [
          "Customers"
        ],
        "summary": "Add an individual/associated entity to an Onboarding Application",
        "description": "Creates a new individual/associated entity with a unique identifier to the specified application, capturing key details such as name, date of birth, address etc.",
        "operationId": "createApplicationAssociate",
        "parameters": [
          {
            "name": "applicationId",
            "in": "path",
            "description": "ID of application",
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
                "$ref": "#/components/schemas/customercompliance.CreateAssociateRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "CREATED",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/customercompliance.AssociateResponse"
                }
              }
            }
          },
          "400": {
            "description": "Invalid Parameters",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/customercompliance.MessageResponse"
                  }
                }
              }
            }
          },
          "403": {
            "description": "Incorrect permissions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/customercompliance.AssociateResponse"
                }
              }
            }
          },
          "404": {
            "description": "NOT FOUND",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/customercompliance.AssociateResponse"
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
      "customercompliance.AddressRequest": {
        "type": "object",
        "properties": {
          "addressLine1": {
            "type": "string",
            "description": "Address line 1",
            "minLength": 1
          },
          "addressLine2": {
            "type": "string",
            "description": "Address line 2"
          },
          "country": {
            "type": "string",
            "description": "Country alpha2 code",
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "description": "Post code",
            "minLength": 1
          },
          "postTown": {
            "type": "string",
            "description": "Post town",
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
      "customercompliance.ContactDetailsRequest": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "format": "email",
            "description": "Email address",
            "minLength": 1
          },
          "phone": {
            "type": "string",
            "description": "Phone number",
            "minLength": 1
          }
        },
        "required": [
          "email",
          "phone"
        ]
      },
      "customercompliance.MessageResponse": {
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
      "customercompliance.CreateAssociateRequest": {
        "type": "object",
        "properties": {
          "firstName": {
            "type": "string",
            "description": "Associate first name",
            "minLength": 1
          },
          "middleName": {
            "type": "string",
            "description": "Associate middle name"
          },
          "lastName": {
            "type": "string",
            "description": "Associate last name",
            "minLength": 1
          },
          "dateOfBirth": {
            "type": "string",
            "description": "Associate date of birth in YYYY-MM-DD format",
            "minLength": 1,
            "pattern": "^(\\s*|\\d{4}-\\d{2}-\\d{2})$"
          },
          "address": {
            "$ref": "#/components/schemas/customercompliance.AddressRequest",
            "description": "Primary address for the associate"
          },
          "types": {
            "type": "array",
            "description": "Associate type",
            "items": {
              "type": "string",
              "description": "Associate type",
              "enum": [
                "INDIVIDUAL",
                "DIRECTOR",
                "PARTNER",
                "BENE_OWNER",
                "SOLETRADER",
                "AUTHORISED_SIGNER"
              ]
            },
            "minItems": 1
          },
          "contactDetails": {
            "$ref": "#/components/schemas/customercompliance.ContactDetailsRequest",
            "description": "Contact details for the associate"
          },
          "ownershipPercentage": {
            "type": "number",
            "description": "Ownership percentage",
            "maximum": 100,
            "minimum": 0
          }
        },
        "required": [
          "dateOfBirth",
          "firstName",
          "lastName",
          "types"
        ]
      },
      "customercompliance.AssociateResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Associate bid"
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