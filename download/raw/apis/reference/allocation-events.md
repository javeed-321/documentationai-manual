---
updatedAt: 2025-08-20T23:41:22.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Allocation Events

Allocation events are generated when trading advisors execute a block trade and then use the allocation APIs to distribute the shares to individual customer accounts.

## Allocations Accepted

An allocation was successfully received.

```json Payload
{
  "id": "mam_event_64aa72a3-33c8-442d-aef2-857a1ebfd006",
  "type": "mam.allocationlist.accepted",
  "timestamp": "2025-05-21T15:30:10.151777417Z",
  "payload": {
    "id": "mam_event_64aa72a3-33c8-442d-aef2-857a1ebfd006",
    "status": "mam.allocationlist.accepted",
    "payload": {
      "riaID": "011a3e9a-a703-4dea-9579-d3b1f26a62e7",
      "allocationListID": "ME.allocation.Appreciate.7fff7b15-3487-42df-980d-0ee79c71906a",
      "allocationCount": 4,
      "completedCount": 0,
      "rejectedCount": 0,
      "created": "2025-05-21T15:30:10.143Z",
      "updated": "2025-05-21T15:30:10.143Z"
    },
    "timeStamp": "2025-05-21T15:30:10.143Z",
    "version": 0
  }
}
```

## Allocations Processing

An allocation is processing.

```json Payload
{
  "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
  "type": "mam.allocationlist.processing",
  "timestamp": "2025-05-21T15:30:10.481224417Z",
  "payload": {
    "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
    "status": "mam.allocationlist.processing",
    "payload": {
      "riaID": "011a3e9a-a703-4dea-9579-d3b1f26a62e7",
      "allocationListID": "ME.allocation.Appreciate.7fff7b15-3487-42df-980d-0ee79c71906a",
      "allocationCount": 4,
      "completedCount": 0,
      "rejectedCount": 0,
      "created": "2025-05-21T15:30:10.143Z",
      "updated": "2025-05-21T15:30:10.471Z"
    },
    "timeStamp": "2025-05-21T15:30:10.471Z",
    "version": 0
  }
}
```

## Allocations Complete

An allocation job has successfully completed.

```json Payload
{
  "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
  "type": "mam.allocationlist.complete",
  "timestamp": "2025-05-21T15:30:10.481224417Z",
  "payload": {
    "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
    "status": "mam.allocationlist.complete",
    "payload": {
      "riaID": "011a3e9a-a703-4dea-9579-d3b1f26a62e7",
      "allocationListID": "ME.allocation.Appreciate.7fff7b15-3487-42df-980d-0ee79c71906a",
      "allocationCount": 4,
      "completedCount": 4,
      "rejectedCount": 0,
      "created": "2025-05-21T15:30:10.143Z",
      "updated": "2025-05-21T15:30:10.471Z"
    },
    "timeStamp": "2025-05-21T15:30:10.471Z",
    "version": 0
  }
}
```

## Allocations Rejected

An allocation has been rejected.

```json
{
  "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
  "type": "mam.allocationlist.rejected",
  "timestamp": "2025-05-21T15:30:10.481224417Z",
  "payload": {
    "id": "mam_event_d657b4f7-ddb3-4b54-b6bd-c6bddb1923ed",
    "status": "mam.allocationlist.rejected",
    "payload": {
      "riaID": "011a3e9a-a703-4dea-9579-d3b1f26a62e7",
      "allocationListID": "ME.allocation.Appreciate.7fff7b15-3487-42df-980d-0ee79c71906a",
      "allocationCount": 4,
      "completedCount": 0,
      "rejectedCount": 4,
      "created": "2025-05-21T15:30:10.143Z",
      "updated": "2025-05-21T15:30:10.471Z"
    },
    "timeStamp": "2025-05-21T15:30:10.471Z",
    "version": 0
  }
}
```