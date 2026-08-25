---
updatedAt: 2026-05-27T16:57:45.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Create Session Token

Creates a session token for an implementer to utilize for subsequent API requests.

> 📘 Authentication FAQs
>
> 1. **What's the TTL?**\
>    Every generated access\_token has a 60min (1hr) expiry time.
>
> 2. **Can i have multiple active auth tokens at the same time?**\
>    Yes, requesting for a new token does not expire the previously retrieved token. Every token's expiry time (60 mins) is always determined by when it was initially requested.
>
> 3. **What's the rate limit?**\
>    Token should be cached and recycled. So no more than 5-10 Api calls per hour is expected.
>
> 4. **Can we get multiple pairs of clientID and clientSecret?**\
>    Due to the nature of the authentication model, you shouldn't be requiring more than 1 pair, however, if absolutely needed, we can provision accordingly. Please contact DriveWealth if this is a requirement.
>
> 5. **How do i use the retrieved auth token?**\
>    You'll pass it into the header of all API calls as "Authorization": "Bearer \{access\_token}"

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Authentication APIs",
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
  "security": [],
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
      "name": "Auth"
    }
  ],
  "paths": {
    "/auth/tokens": {
      "post": {
        "tags": [
          "Auth"
        ],
        "summary": "Create Session Token",
        "description": "Creates a session token for an implementer to utilize for subsequent API requests.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateSessTokenReq"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Creating Session Token was Successful.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateSessToken"
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
      "CreateSessToken": {
        "type": "object",
        "properties": {
          "token_type": {
            "type": "string",
            "example": "Bearer",
            "description": "The type of token that was generated.",
            "enum": [
              "Bearer"
            ]
          },
          "expires_in": {
            "type": "string",
            "example": "3600",
            "description": "The length of time in seconds for which the session token is valid."
          },
          "access_token": {
            "type": "string",
            "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
            "description": "The session token."
          },
          "scope": {
            "type": "string",
            "example": "all_trading",
            "description": "The scope of permission set for the JSON Web Token (JWT)."
          }
        }
      },
      "CreateSessTokenReq": {
        "type": "object",
        "required": [
          "clientID",
          "clientSecret"
        ],
        "properties": {
          "clientID": {
            "type": "string",
            "example": "0oafccTendies67BTx113",
            "description": "The identifier of the client accessing the DriveWealth system."
          },
          "clientSecret": {
            "type": "string",
            "example": "8WfNzC4oTendiesTradingCompanyPuQNwg7BPByWqQOj",
            "description": "The secret of the client accessing the DriveWealth system."
          }
        }
      }
    }
  }
}
```