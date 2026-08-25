---
updatedAt: 2025-09-22T15:01:57.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# KYC Events

## KYC Created

A user's KYC details have been created, provides details on submitted information.

```json Created
{
    "id": "event_b84d304f-d434-4610-859a-ebdcda33ffcb",
    "type": "kyc.created",
    "timestamp": "2019-03-28T22:50:02.073327862Z",
    "ibID": "cf11ef03-f489-42ec-b263-35f444808f7e",
    "object": "kyc_created",
    "payload": {
        "userID": "104c4f1e-bd1f-4fca-afa7-74aaab0409fa",
        "status": "KYC_APPROVED",
        "statusMessage": "KYC Approved",
        "verificationType": "NON_DOC"
    }
}
```

## KYC Updated

A user's KYC details have been updated, provides details on update reason.

```json Updated
{
    "id": "event_789ca9ba-312b-4480-9f36-3805ceb00f63",
    "type": "kyc.updated",
    "timestamp": "2019-03-28T22:50:02.073327862Z",
    "ibID": "cf11ef03-f489-42ec-b263-35f444808f7e",
    "object": "kyc_updated",
    "payload": {
        "current": {
            "status": "KYC_APPROVED",
            "statusMessage": "KYC Approved"
        },
        "previous": {
            "status": "KYC_PROCESSING",
            "statusMessage": "User is sent for KYC"
        },
        "userID": "104c4f1e-bd1f-4fca-afa7-74aaab0409fa"
    }
}
```
```json Updated [kyc error]
{
    "id": "event_789ca9ba-312b-4480-9f36-3805ceb00f63",
    "type": "kyc.updated",
    "timestamp": "2019-03-28T22:50:02.073327862Z",
    "ibID": "cf11ef03-f489-42ec-b263-35f444808f7e",
    "object": "kyc_updated",
    "payload": {
        "current": {
            "status": "KYC_DOC_REQUIRED",
            "statusMessage": "User needs to submit a document for verification. Please check kyc errors for more detail",
            "errors": ["SSN_NOT_MATCH"]
        },
        "previous": {
            "status": "KYC_PROCESSING",
            "statusMessage": "User is sent for KYC"
        },
        "userID": "104c4f1e-bd1f-4fca-afa7-74aaab0409fa"
    }
}
```