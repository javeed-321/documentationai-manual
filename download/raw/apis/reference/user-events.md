---
updatedAt: 2025-09-22T15:02:06.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# User Events

## User Created

A new user has been created, this event provides basic user detail and status.

```json User Created
{
    "id": "event_b84d304f-d434-4610-859a-ebdcda33ffcb",
    "type": "users.created",
    "timestamp": "2019-03-28T22:50:02.073327862Z",
    "payload": {
        "firstName": "John",
        "lastName": "Smith",
        "email": "jsmith@google.com",
        "userID": "0b06eda0-b7d6-4e4b-8f8f-c46426070957",
        "status": {
            "name": "PENDING",
            "description": "User is pending approval."
        }
    }
}
```

## User Updated

Any details in the users object has been updated. This will show the pervious state and the current state of the object.

```json Name Updated
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "users.updated",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "previous": {
            "firstName": "Mike"
        },
        "current": {
            "firstName": "Mikey"
        },
        "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932"
    }
}
```

## User Info Required Created

```json Link Created
{
    "id": "event_215cffec-112b-17fd-8c64-36ef645d9e99",
    "type": "user.inforequired.created",
    "timestamp": "2023-01-12T14:30:02.239726118Z",
    "payload": {
        "userID": "88b65bf4-9b68-4231-93b8-b6839fec110c",
        "accountID": "88b65bf4-9b68-4231-93b8-b6839fec110c.1635269702783",
        "accountNo": "TTC000005",
        "driveClientLink": "https://client.drivewealth.com/"
    }
}
```