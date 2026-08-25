---
updatedAt: 2025-09-22T15:01:53.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Asset Transfer Events

## Asset Transfer Created

A new asset transfer was created.

```json Created [ACATs]
{
    "id": "event_541866c6-73dc-4aa1-82dc-8b1fc703fd4d",
    "type": "assets.transfer.created",
    "object": "ACAT",
    "timestamp": "2023-06-23T21:20:21.828Z",
    "payload": {
        "transferID": "acats_65d48ca5-b6ad-4923-b868-ec6887186522",
        "source": "FOLIO123",
        "destination": "LKRY000005",
        "clearingNo": "DTC-001",
        "status": {
            "name": "STARTED",
            "description": "Asset transfer request has been initiated."
        },
        "type": {
            "name": "ACAT",
            "description": "ACAT transfer"
        },
        "acatsType": {
            "name": "FULL",
            "description": "Full Acats Transfer"
        },
        "sourceAccountType": {
            "name": "INDIVIDUAL",
            "description": "Individual Account"
        },
        "positions": {},
        "comment": "comment example",
        "created": "2023-06-23T21:20:21.453Z",
        "createdBy": "c6de775c-82bc-420e-b504-f8b42a072185"
    }
}
```
```json Created [teen]
{
    "id": "event_789ca9ba-312b-4480-9f36-3805ceb00f63",
    "type": "assets.transfer.created",
    "timestamp": "2023-02-28T22:50:02.073327862Z",
    "object": "TEEN",
    "payload": {
        "transferID": "grad_8c583260-ae31-11ed-afa1-0242ac120002",
        "source": "DWST000076",
        "destination": "DWST000077",
        "type": {
            "name": "TEEN",
            "description": "Teen Account Migration"
        },
        "status": {
            "name": "STARTED",
            "description": "Account transfer request has been initiated"
        },
        "comment": "Migrating Teen account to Individual account.",
        "metadata": [{}],
        "created": "2023-02-28T22:50:02.073327862Z",
        "updated": "2023-02-28T22:50:02.073327862Z"
    }
}
```

## Asset Transfer Updated

An asset transfer was updated.

1. Status update event

```json Updated [ACATs]
{
    "id": "event_89394394-6d25-404a-8388-f1ee6a969d12",
    "type": "assets.transfer.updated",
    "object": "ACAT",
    "timestamp": "2023-06-23T21:26:28.216Z",
    "payload": {
        "current": {
            "status": {
                "name": "STARTED",
                "description": "Asset transfer request has been initiated."
            },
            "comment": "comment example"
        },
        "previous": {
            "status": {
                "name": "PENDING",
                "description": "Asset transfer request is pending"
            },
            "comment": "ACAT submitted.",
            "metadata": {},
            "updated": "2023-06-23T21:26:28.207Z",
            "updatedBy": "c6de775c-82bc-420e-b504-f8b42a072185"
        },
        "transferID": "acats_65d48ca5-b6ad-4923-b868-ec6887186522"
    }
}
```

2. Comment update event

```json Updated [ACATs]
{
    "id": "event_89394394-6d25-404a-8388-f1ee6a969d12",
    "type": "assets.transfer.updated",
    "object": "ACAT",
    "timestamp": "2023-06-23T21:26:28.216Z",
    "payload": {
        "current": {
            "comment": "POA:  John Smith and Jane Doe"
        },
        "previous": {
            "comment": "ACAT submitted.",
            "updated": "2023-06-23T21:26:28.207Z"
        },
        "transferID": "acats_65d48ca5-b6ad-4923-b868-ec6887186522"
    }
}
```

3. Settlement status update event

```json Updated [ACAT]
{
  "id": "event_1d09f45d-e392-45ef-a7db-b48d6ca8bca3",
  "type": "assets.transfer.updated",
  "object": "ACAT",
  "timestamp": "2025-04-24T19:36:57.039Z",
  "payload": {
    "current": {
      "comment": "Transfer review accepted",
      "updated": "2025-04-24T19:36:57.032Z",
      "settlementStatus": "ACAT_REVIEW_ACCEPTED",
      "settlementCode": "230"
    },
    "previous": {
      "comment": "Transfer is under review",
      "updated": "2025-04-24T19:32:04.357Z",
      "settlementStatus": "ACAT_UNDER_REVIEW",
      "settlementCode": "200"
    },
    "transferID": "acats_fd6087d2-970a-4d0b-b5a6-1d3fe92d893f"
  }
}

```
```json Updated [Teen]
{
    "id": "event_789ca9ba-312b-4480-9f36-3805ceb00f63",
    "type": "assets.transfer.updated",
    "timestamp": "2023-02-28T22:50:02.073327862Z",
    "object": "TEEN",
    "payload": {
        "current": {
            "status": {
                "name": "PENDING",
                "description": "Account transfer request is pending."
            },
            "updated": "2023-02-28T22:50:02.073327862Z"
        },
        "previous": {
            "status": {
                "name": "STARTED",
                "description": "Account transfer request has been initiated."
            }
        },
        "transferID": "grad_8c583260-ae31-11ed-afa1-0242ac120002"
    }
}
```

## Asset Transfer Completed

An asset transfer was completed.

```json Completed [ACATs Successful]
{
    "id": "event_89394394-6d25-404a-8388-f1ee6a969d12",
    "type": "assets.transfer.completed",
    "object": "ACAT",
    "timestamp": "2023-06-23T21:26:28.216Z",
    "payload": {
        "current": {
            "status": {
                "name": "COMPLETED",
                "description": "Asset transfer request was completed."
            },
            "comment": "comment example"
        },
        "previous": {
            "status": {
                "name": "SUCCESSFUL",
                "description": "Asset transfer request is successful"
            },
            "comment": "ACAT settled",
            "metadata": {},
            "updated": "2023-06-23T21:26:28.207Z"
        },
        "transferID": "acats_65d48ca5-b6ad-4923-b868-ec6887186522"
    }
}
```
```json Completed [ACATs Failed]
{
  "id": "event_5db436cc-0eda-4853-ab9f-2b2ff5c81c51",
  "type": "assets.transfer.completed",
  "object": "ACAT",
  "timestamp": "2025-04-24T19:54:45.607Z",
  "payload": {
    "current": {
      "status": {
        "name": "FAILED",
        "description": "Asset transfer is failed."
      },
      "comment": "Transfer rejected",
      "updated": "2025-04-24T19:54:45.599Z",
      "updatedBy": "ACAT_STATUS_UPDATE_SYSTEM",
      "settlementStatus": "ACAT_REJECTED",
      "settlementCode": "600",
      "rejectionInfo": {
        "rejectionCode": "05",
        "rejectionReason": "Invalid Broker Account Number"
      }
    },
    "previous": {
      "status": {
        "name": "PENDING",
        "description": "Asset transfer request is pending"
      },
      "comment": "Transfer is under review",
      "updated": "2025-03-26T19:33:35.847Z",
      "updatedBy": "ACAT_TRANSFER_SYSTEM",
      "settlementStatus": "ACAT_REVIEW_ERROR",
      "settlementCode": "220",
      "rejectionInfo": null
    },
    "transferID": "acats_f9316eee-0447-40c0-aa27-f8d06e42cce0"
  }
}
```
```json Completed [Teen]
{
    "id": "event_789ca9ba-312b-4480-9f36-3805ceb00f63",
    "type": "assets.transfer.completed",
    "timestamp": "2023-02-28T22:50:02.073327862Z",
    "object": "TEEN",
    "payload": {
        "current": {
            "status": {
                "name": "SUCCESSFUL",
                "description": "Account transfer request has been successfully completed."
            },
            "updated": "2023-02-28T22:50:02.073327862Z"
        },
        "previous": {
            "status": {
                "name": "ON_HOLD",
                "description": "Account transfer request is on Hold."
            },
            "updated": "2023-02-28T22:50:02.073327862Z"
        },
        "transferID": "grad_8c583260-ae31-11ed-afa1-0242ac120002"
    }
}
```