---
updatedAt: 2025-09-22T15:02:03.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Statement Events

## Statements Created

A new statement document has been created for the user's account.

```json Created
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "statements.created",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "statement": {
            "displayName": "Apr 28, 2017 Statement",
            "fileKey": "2017042802"
        },
        "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
        "accountNo": "DPKU000001",
        "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932"
    }
}
```

## Trade Confirmation Created

A new trade confirmation document has been created.

```json Created
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "tradeconfirms.created",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "tradeConfirm": {
            "displayName": "Jun 02, 2017 Trade Confirm",
            "fileKey": "2017060201"
        },
        "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
        "accountNo": "DPKU000001",
        "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932"
    }
}
```

## Tax Form Created

A new tax form document has been created for the user's account.

```json Created
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "taxforms.created",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "taxForm": {
            "displayName": "2015 Tax Year 1099-B",
            "fileKey": "2015123103"
        },
        "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
        "accountNo": "DPKU000001",
        "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932"
    }
}
```