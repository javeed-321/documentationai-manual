---
updatedAt: 2025-10-24T12:54:10.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Entity events

## Entity Created

A new entity has been created.

```json Created
{
  "id": "event_ab370465-34d9-4cc8-944e-b7e5e0da8929",
  "type": "entity.created",
  "timestamp": "2025-10-03T16:45:31.848997Z",
  "payload": {
    "id": "0dc2dc5a-09d4-4f86-b8bf-8a93a7dd96d3",
    "createdAt": "2025-10-03T16:45:31.848997Z",
    "type": "CORPORATION",
    "ibID": "417505ee-4a6b-459a-ad9a-9d58029c542a",
    "wlpID": "FRDT",
    "attributes": {
      "name": "Acme Co",
      "dba": "Acme",
      "incorporationCountry": "JPN",
      "incorporationProvince": "NY",
      "incorporationDate": "2019-01-01"
    },
    "identifications": {
      "EIN": "987654321",
      "FTIN": "123456789",
      "FTNLO": "true"
    },
    "contact": {
      "addresses": null,
      "phone": "+81678851066",
      "email": "hello@acme.com",
      "website": "www.acme.com"
    },
    "metadata": {
      "myCustomKey": "foo",
      "bar": "foo"
    },
    "disclosures": {
      "termsOfUse": {
        "agreed": true,
        "signedBy": "name",
        "signedWhen": "2024-09-09T15:20:05.228124050Z",
        "disclosureName": "termsOfUse"
      },
      "customerAgreement": {
        "agreed": true,
        "signedBy": "name",
        "signedWhen": "2024-09-09T15:20:05.228124050Z",
        "disclosureName": "customerAgreement"
      },
      "rule14b": {
        "agreed": true,
        "signedBy": "name",
        "signedWhen": "2024-09-09T15:20:05.228124050Z",
        "disclosureName": "rule14b"
      },
      "marginAgreement": {
        "agreed": true,
        "signedBy": "name",
        "signedWhen": "2024-09-09T15:20:05.228124050Z",
        "disclosureName": "marginAgreement"
      }
    },
    "kyb": {
      "status": "KYB_NOT_READY",
      "statusWhen": "2025-10-03T16:45:31.841852Z",
      "statusBy": "SYSTEM"
    },
    "tax": "TAX_READY",
    "taxData": {
      "fatcaData": {
        "applicable": false,
        "applicableFrom": "2025-10-03T16:45:31.845147Z",
        "setBy": "SYSTEM"
      },
      "data": {}
    },
    "status": "PENDING",
    "investorProfile": {
      "netWorthTotal": 10000
    },
    "financialAffiliations": [
      "ABC",
      "DEF"
    ]
  }
}
```

## Entity Updated

The detail of the entity has been updated. This event will show the previous state and the current state of the object.

```json Updated
{
    "id": "event_7b76b652-9cc4-4f7c-a8d3-80b4c3c0d966",
    "type": "entity.updated",
    "timestamp": "2025-10-03T20:11:05.603Z",
    "payload": {
        "previous": {
            "kyb": {
                "status": "KYB_READY",
                "statusWhen": "2025-10-03T16:55:51.281Z"
            }
        },
        "current": {
            "kyb": {
                "status": "KYB_PROCESSING_DIRECTORS",
                "statusWhen": "2025-10-03T20:11:05.554Z"
            }
        },
        "entityID": "55bc5c83-de46-4581-a21b-c0091373abb5"
    }
}
```