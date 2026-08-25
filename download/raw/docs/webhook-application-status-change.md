---
updatedAt: 2026-06-11T09:56:30.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Application Status Change

Modulr sends this webhook to notify Partners of changes to a customer's application status as it progresses through the verification process.

You will receive this event multiple times across the lifecycle of an application. Your handler must be idempotent - the same event may be delivered more than once.

***

## When it fires

* When a customer starts entering data (transitions to `IN_PROGRESS`)
* When automated CDD checks complete (transitions to `APPROVED`, `PENDING_STEP_UP`, or `MANUAL_REVIEW`)
* When a manual review decision is made
* When a step-up is requested post-submission

***

## Payload

```json
{
  "eventDateTime": "2026-04-27T13:19:34.457092669Z",
  "eventName": "APPLICATION_STATUS_CHANGE",
  "applicationId": "APP21000MG",
  "status": "IN_PROGRESS"
}
```

### Fields

| Field           | Type              | Description                                                                                                              |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `eventDateTime` | string (ISO 8601) | Timestamp of the status change.                                                                                          |
| `eventName`     | string            | Always `APPLICATION_STATUS_CHANGE`.                                                                                      |
| `applicationId` | string            | The application ID associated with the event. Store this against your customer record.                                   |
| `status`        | string            | The new application status. See [Application Statuses](./cv_article_03_application_statuses.md) for all possible values. |

***

## Status values

| Status            | What to do                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| `IN_PROGRESS`     | No action. Store the status against your customer record.                                                   |
| `PENDING_STEP_UP` | Notify your customer that further information is required. Re-invoke the SDK with the same `applicationId`. |
| `MANUAL_REVIEW`   | No action. Await the next status change.                                                                    |
| `APPROVED`        | Await the `CUSTOMER_CREATED` webhook to receive the `customerId`.                                           |
| `DECLINED`        | Notify the customer. They will not be onboarded.                                                            |
| `EXPIRED`         | The customer must restart. Create a new application.                                                        |

***

## Handling PENDING\_STEP\_UP

When you receive a `PENDING_STEP_UP` status:

1. Notify your customer that further action is needed.
2. Request a fresh short-lived token (Step 5 of the integration guide).
3. Re-initialise the SDK with the same `applicationId`.
4. Open the SDK - it will automatically surface the step-up form for the outstanding requirements.

```javascript
// 1. Get fresh token
// POST /onboarding-service/keys/onboarding/{applicationId}

// 2. Re-initialise SDK
const sdkInstance = await ModulrCustomerVerificationSdk.init({
  token,
  hmac,
  applicationId: 'APP21000MG',
  onInit: (result) => { /* ... */ },
  onError: (error) => { /* ... */ }
});

// 3. Open SDK
await sdkInstance.open({
  onResult: (data) => { /* ... */ },
  onError: (error) => { /* ... */ },
  onClose: () => { /* ... */ }
});
```

***

## Implementation notes

* Register your webhook endpoint URL in your Partner configuration.
* Respond with `HTTP 200` to acknowledge receipt. Modulr will retry on failure.
* For update flows (CDD refresh), monitor `APPLICATION_STATUS_CHANGE` events on the **new** Application ID, not the original.

***

## Related

* [Application Statuses](https://modulr.readme.io/docs/customer-verification-application-statuses)
* [Integration Guide](https://modulr.readme.io/docs/customer-verification-integration-guide)
* [Webhook - Customer Created](https://modulr.readme.io/docs/webhook-customer-created)