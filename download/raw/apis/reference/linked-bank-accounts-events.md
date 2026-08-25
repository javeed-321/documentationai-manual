---
updatedAt: 2025-09-22T15:01:58.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Linked Bank Account Events

## Linked Bank Accounts Created

A new bank account has been linked and the event provides the details.

```json Created
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "bankAccounts.created",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "bankAccountNickname": "Test ABC",
        "bankAccountNumber": "****2227",
        "bankRoutingNumber": "110000000",
        "bankAccountType": "Saving",
        "status": "ACTIVE",
        "created": "2021-09-20T14:26:39.345Z",
        "updated": "2021-09-20T14:26:39.345Z",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38"
    }
}
```
```json Created [plaid link]
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "bankAccount.created",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "bankAccountNickname": "Test ABC",
        "plaidProcessorToken": "processor-sandbox-d0c926da-0dbe-4293-bc2a-41b3049097db",
        "status": "ACTIVE",
        "created": "2021-09-20T14:26:39.345Z",
        "updated": "2021-09-20T14:26:39.345Z",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38"
    }
}
```

## Linked Bank Accounts Updated

A bank account that was linked has been updated and the event provides the details.

```json Updated
{
    "id": "event_13543008-e871-43d0-80ee-cc5fe8c2d370",
    "type": "bankAccounts.updated",
    "timestamp": "2021-11-15T16:17:29.787Z",
    "payload": {
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "bankAccountNickname": "Test ABC",
        "bankAccountNumber": "****2227",
        "bankRoutingNumber": "110000000",
        "status": "ACTIVE",
        "created": "2021-11-15T16:05:45.068Z",
        "updated": "2021-11-15T16:17:29.786Z",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38"
    }
}
```

## Linked Bank Accounts Deleted

A bank account that was linked has been unlinked/deleted and the event provides the details.

```json Deleted
{
    "id": "event_b3d62310-391f-44f2-820c-b69698af0c4a",
    "type": "bankAccounts.deleted",
    "timestamp": "2021-11-15T16:19:53.587Z",
    "payload": {
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "bankAccountNickname": "Test ABC",
        "bankAccountNumber": "****2227",
        "bankRoutingNumber": "110000000",
        "status": "DELETED",
        "created": "2021-11-15T16:05:45.068Z",
        "updated": "2021-11-15T16:19:53.582Z",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38"
    }
}
```