---
updatedAt: 2026-07-13T22:50:15.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Customer verification

Like with many other types of financial products, customers cannot engage in investing until their personal information is verified. There are several flows supported out-of-the-box by DriveWealth:

1. **DriveWealth Does KYC** (`DO_KYC`) — DriveWealth performs KYC (Know-Your-Customer) checks on all newly created Users.

2. **DriveWealth Relies on client** (`NO_KYC`) — DriveWealth can rely on the client's KYC processes, pending a successful review of KYC policies and procedures.

3. **DriveWealth performs secondary KYC** (`VERIFY_KYC`) — In some cases, DriveWealth can allow accounts to be opened immediately, based on the client's KYC processes, but DriveWealth must also verify all account details after the account is opened.

<Callout icon="📘" theme="info">
  ### Document Upload Guidelines

  For clients required to upload documents for KYC verification, following are some guidelines:

  - DriveWealth DOES NOT accept digital ID cards, the documents uploaded should be copies of the the Physical ID card themselves. Camera clicked pictures or scanned copies of the Physical ID cards are accepted.
  - Names on the ID Document MUST match the name on the Brokerage account. For instance, if the ID document has the name "John Allen Smith", the brokerage account should be opened by inputting the`firstName` as "John" and `lastName` as "Allen Smith" while Creating the User.
</Callout>

One of the three available verification methods will be selected based on the clients geographic location, licenses, and KYC/AML capabilities.

## `DO_KYC`

Once a User is created, its status will be pending, as shown in the following Event:

```json
{
  "id": "event_b84d304f-d434-4610-859a-ebdcda33ffcb",
  "type": "users.created",
  "timestamp": "2019-03-28T22:50:02.073327862Z",
  "payload": {
    "firstName": "John",
    "lastName": "Smith",
    "email" : "jsmith@google.com",
    "userID": "0b06eda0-b7d6-4e4b-8f8f-c46426070957",
    "status": {
      "name": "PENDING",
      "description": "User is pending approval."
    }
  }
}
```

Depending on the region of the customer, you may need to upload physical document proofs as well before validation will begin. Refer back to [Opening accounts](https://developer.drivewealth.com/apis/docs/opening-accounts) for how to do this.

Verification of the customer is initiated automatically, and a determination is made within the next 15 minutes (but usually, within seconds). Once this is complete, the User status is changed, which can be subscribed to via an Event:

```json
{
  "id": "event_4da42927...",
  "type": "users.updated",
  "timestamp": "2019-01-09T12:14:44.155187291Z",
  "payload": {
    "previous": {
      "status": {
        "name": "PENDING",
        "description": "User is pending approval."
      }
    },
    "current": {
      "status": {
        "name": "APPROVED",
        "description": "User is approved."
      }
    },
    "userID": "cc07f91b-7ee1..."
  }
}
```

If not using the Events system, you can alternatively check the [Retrieve KYC status by User](https://developer.drivewealth.com/apis/reference/get_users-userid-kyc-status) API. When something goes wrong, like if the customer cannot be verified, you can also use this API to determine the specific failure and action to take:

```json
GET /back-office/users/:userID/kyc-status
{
  ...
  "kyc": {
    "status": {
      "name": "KYC_INFO_REQUIRED",
      "code": "KS102",
      "description": "User's PII not matched. Please revisit your PII info."
    },
    "approved": null,
    "accepted": null,
    "errors": [{
        "name": "USER_ID_ERROR",
        "code": "K101",
        "description": "SSN/ID number not matched. Please edit your PII info or submit the document for verification."
      },
      {
        "name": "USER_DOB_ERROR",
        "code": "K102",
        "description": "Date of birth not matched."
      }
    ]
  },
  ...
}
```

## `NO_KYC` and `VERIFY_KYC`

With these setups, once you create a User, you’re done! The User status will change to APPROVED within a few seconds.

<Callout icon="🚧" theme="warn">
  ###

  Only customers whose details have been vetted and approved by your firm should be sent to DriveWealth in these models.
</Callout>

## KYC status workflow

The [Retrieve KYC status by User](https://developer.drivewealth.com/apis/reference/get_users-userid-kyc-status) API will return different values based on the current KYC state of the customer. The workflow of statuses looks like this:

<Image src="https://files.readme.io/feed41f-6a18b92-KYC_Status.png" alt="6a18b92-KYC_Status.png" align="center" width="1187" caption="At any point beyond `KYC_PROCESSING`, the User's KYC can be approved or denied." />

| KYC status          | Description                                                                                                                                                                                                     |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `KYC_NOT_READY`     | All required data document fields have not been submitted.                                                                                                                                                      |
| `KYC_READY`         | All required data document fields have been submitted successfully and user is ready to be KYC'ed.                                                                                                              |
| `KYC_PROCESSING`    | The user's data submitted has been sent to our vendor to verify the user.                                                                                                                                       |
| `KYC_APPROVED`      | The user's data has been verified by our vendor and the vendor has signed on the legitimacy of the user.                                                                                                        |
| `KYC_INFO_REQUIRED` | The user's data that has been submitted to DriveWealth and thus our vendor has one or many errors in it. To have the KYC process rerun, once the user updates their information, call a PATCH on /users.        |
| `KYC_DOC_REQUIRED`  | A physical document like a passport, driver's license, utilities bill, etc. is required to be uploaded to uploaded. Once the physical document has been uploaded this will automatically rerun the KYC process. |
| `KYC_MANUAL_REVIEW` | The user's KYC is under additional review after additional data and documents have been submitted.                                                                                                              |
| `KYC_DENIED`        | The user's KYC was denied by our vendor automatically by the system or by a human operator.                                                                                                                     |

## Ongoing account monitoring

In all of these models, DriveWealth will perform some level of continuing checks on the customer throughout the lifecycle of the Account. If DriveWealth finds information that would prohibit further trading, the Account may change in status to prevent further trading. This can be captured via an Event:

```json
{
  "id": "event_773a8a45-75fc...",
  "type": "accounts.updated",
  "timestamp": "2019-03-28T22:46:47.821071506Z",
  "payload": {
    "previous": {
      "status": {
        "name": "OPEN",
        "description": "Open"
      }
    },
    "current": {
      "status": {
        "name": "CLOSED",
        "description": "Closed"
      }
    },
    "accountID": "711c012d-7a3c...",
    "accountNo": "ABCD000001",
    "userID": "711c012d-7a3c..."
  }
}
```

In some cases, Accounts will be restricted from trading while an investigation is done (typically alongside the client). In other cases, an Account may need to be closed with urgency.

## Simulating specific cases

In sandbox, you can test error cases by setting the `lastName` of a User to the specific error condition you want to encounter.

For example, you can create a User with this data:

```json
POST /back-office/users
{
  "userType": "INDIVIDUAL_TRADER",
  "documents": [
    {
      "type": "BASIC_INFO",
      "data": {
        "firstName": "Daryl",
        "lastName": "DOB_NOT_MATCH",
        "username": "DHall",
        "country": "USA",
        "phone": "2914443333",
        "emailAddress": "b@b.com",
        "language": "en_US"
      }
    },
    ...
  ]
}
```

Once the KYC workflow is invoked, this User will be rejected for an invalid date of birth.

Refer to the [full list of KYC error codes](https://developer.drivewealth.com/apis/reference/errors#kyc-document-errors), all of which can be used in this manner.