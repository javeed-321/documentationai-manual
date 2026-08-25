---
updatedAt: 2026-08-14T09:43:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Customer Verification: Integration Guide

This guide walks through the full integration step by step, with example code for each stage. All code examples reference KYC (Know Your Customer) scenarios, but the same pattern applies to KYB (Know Your Business) applications.

***

## Step 1: <Anchor target="_blank" href="https://modulr.readme.io/reference/createapplication">Create an Application</Anchor>

Before the SDK can be invoked, create an application instance for each customer via the Create Application API. Store the returned `id` against your customer record - it is used in all subsequent API calls and webhooks.

> **Note:** Create a separate application for each business a customer wishes to onboard, even if ownership is identical across businesses.

```http
POST /applications
```

```json
{
  "legalEntity": "MFBV"
}
```

**Response (201 Created)**

```json
{
  "id": "APP21000MG"
}
```

***

## Step 2: Submit KYC/KYB Data via API (Optional)

Skip this step if you are using the SDK-only route. Jump straight to [Step 5](https://modulr.readme.io/docs/customer?isFramePreview=true#step-5-create-a-short-lived-token).

If you hold verified customer data already and want to reduce friction in the onboarding journey, you can pre-populate compliance data via the API before invoking the SDK.

### <Anchor target="_blank" href="https://modulr.readme.io/reference/createapplicationassociate">Create a Compliance Associate</Anchor>

Submit identity data for each individual (the primary customer or associated individuals for a business application).

```http
POST /applications/{applicationId}/compliance/associates
```

```json
{
  "types": ["INDIVIDUAL"],
  "firstName": "Clara",
  "middleName": "Optional",
  "lastName": "Burt",
  "dateOfBirth": "1942-01-02",
  "contactDetails": {
    "email": "clara@example.com",
    "phone": "07415626822"
  },
  "homeAddress": {
    "addressLine1": "1 House Street",
    "addressLine2": "Optional",
    "country": "GB",
    "postCode": "E147HG",
    "postTown": "Edinburgh"
  }
}
```

**Response (201 Created)**

```json
{
  "id": "ASS0000001"
}
```

**Associate types:** Use `INDIVIDUAL` for KYC. For business applications, available types include `DIRECTOR`, `PARTNER`, `BENE_OWNER`, and `SOLETRADER`.

### <Anchor target="_blank" href="https://modulr.readme.io/reference/updateknowyourcustomerbyapplicationid">Submit KYB/KYC Data</Anchor>

Provide expected activity details for the customer's Modulr account.

```http
PUT /applications/APP0000001/compliance/know-your-customer
```

```json
{
  "expectedMonthlySpend": 10000,
  "expectedMonthlyTransactions": 50
}
```

**Response: 204 No Content**

### <Anchor target="_blank" href="https://modulr.readme.io/reference/updatepersonalinformationforassociate_1">Submit Associate Personal Info</Anchor>

Provide nationality data for the associate.

```http
PUT /applications/{applicationId}/compliance/associates/{associateId}/personal-info
```

```json
{
  "nationalities": ["GB", "CA"]
}
```

**Response: 204 No Content**

### <Anchor target="_blank" href="https://modulr.readme.io/reference/updatetaxresidenciesforassociate_1">Submit Associate Tax Residencies</Anchor>

```http
PUT /applications/{applicationId}/compliance/associates/{associateId}/tax-residencies
```

```json
{
  "taxResidencies": ["ES", "FR"]
}
```

**Response: 204 No Content**

***

## Step 3: Handle APPLICATION\_STATUS\_CHANGE Webhooks

Once the customer starts entering data, Modulr sends `APPLICATION_STATUS_CHANGE` webhook events to your registered endpoint. You must process these throughout the entire application lifecycle.

See the full webhook reference: <Anchor target="_blank" href="https://modulr.readme.io/docs/webhook-application-status-change">Webhook - Application Status Change</Anchor>

Your webhook handler must be **idempotent** - the same event may be delivered more than once. Respond with `HTTP 200` to acknowledge receipt. Modulr will retry on failure.

***

## Step 4 (optional): [Upload ID verification docs / biometric selfie image](https://modulr.readme.io/reference/uploaddocument)

We would generally always recommend that any documents that are used as part of the KYB/C application are being uploaded via our Customer Verification SDK (steps 6-9) to maximise the best chance of an automated approval, however, if you are already capturing these documents through your own providers for other purposes, you have the optional route of providing these documents/selfie captured images via API.

```http
POST /applications/{applicationId}/compliance/associates/{associateId}/documents
```

```json
{
  "fileName": "string",
  "content": "string",
  "type": "DRIVING_LICENCE",
  "side": "FRONT"
}
```

**Response (201 Created)**

```json
{
  "id": "ACD0000001"
}
```

***

## Step 5: <Anchor target="_blank" href="https://modulr.readme.io/reference/verifyapplication">Initiate Application Verification</Anchor>

If you submitted data via the API in Step 2, call the verify endpoint to trigger Modulr's CDD orchestration. If you used the SDK-only route, the SDK makes this call automatically.

```http
POST /applications/{applicationId}/verify
```

No request body required.

**Response: 200 OK**

After this call, monitor `APPLICATION_STATUS_CHANGE` webhooks. The application will transition to one of:

* `APPROVED` - all KYB/KYC checks passed
* `PENDING_STEP_UP` - further information required from the customer
* `MANUAL_REVIEW` - application queued for human review

***

## Step 6: <Anchor target="_blank" href="https://modulr.readme.io/reference/createsdkkey">Create a Short-lived Token</Anchor>

Before initialising the SDK, request a short-lived token and HMAC from the Modulr keys endpoint.

> **Important:** This call must be made server-side. Never expose the token or HMAC in client-side code or logs.

```http
POST /keys/applications/{applicationId}
```

**Response (201 Created)**

```json
{
  "expires": "2026-04-06 12:31:58",
  "hmac": "sdk::hmac_052c3013012e",
  "token": "token_6e5522ad78ff"
}
```

The token has a short TTL. Request a fresh token immediately before each SDK initialisation.

***

## Step 7: Initialise the Customer Verification SDK

Use the token, HMAC, and application ID from the previous steps to initialise the SDK.

```javascript
const sdkInstance = await ModulrCustomerVerificationSdk.init({
  token,
  hmac,
  applicationId: 'APP21000MG',

  onInit: (result) => {
    console.log('SDK initialised:', result.status, result.message);
  },
  onError: (error) => {
    console.error('SDK error:', error);
  }
});
```

### Custom Styling (Optional)

The SDK supports visual customisation to match your product's design system. All styling properties are optional - omit the block entirely to use Modulr defaults.

```javascript
const sdkInstance = await ModulrCustomerVerificationSdk.init({
  token,
  hmac,
  applicationId: 'APP21000MG',

  customStyle: {
    theme: {
      primaryColor: '#111111',
      backgroundColor: '#FFFFFF',
      textColor: '#111111',
      borderRadius: '4px',
      iconColor: '#111111',
      successColor: '#008756',
      errorColor: '#D91E18'
    },
    componentOverride: {
      PrimaryButton: {
        default: {
          backgroundColor: '#111111',
          textColor: '#FFFFFF',
          borderRadius: '4px',
          border: '#111111',
          boxShadow: '0'
        },
        hover: {
          backgroundColor: '#78808F',
          textColor: '#FFFFFF',
          borderRadius: '4px',
          border: '#78808F',
          boxShadow: '0'
        }
      }
    }
  },

  onInit: (result) => {
    console.log('SDK initialised:', result.status, result.message);
  },
  onError: (error) => {
    console.error('SDK error:', error);
  }
});
```

Only call `open()` (Step 7) after `onInit` fires successfully.

***

## Step 8: Open the Customer Verification SDK

Call `open()` once the SDK has initialised. The SDK can be displayed as a modal (default) or embedded inline in a container element.

### Modal mode (default)

```javascript
await sdkInstance.open({
  onResult: (data) => console.log('Result:', data),
  onError: (error) => console.error('Error:', error),
  onClose: () => console.log('Closed')
});
```

### Inline / embedded mode

```javascript
await sdkInstance.open({
  containerId: 'your-container-element-id',
  onResult: (data) => console.log('Result:', data),
  onError: (error) => console.error('Error:', error),
  onClose: () => console.log('Closed')
});
```

`containerId` must reference a visible DOM element. Use `onClose` to clean up your UI when the customer exits the SDK.

***

## Step 9: Close the SDK

The SDK can be closed programmatically at any time.

```javascript
ModulrCustomerVerificationSdk.close();
```

The `onClose` callback registered in `open()` fires whether the SDK is closed by the user or programmatically.

***

## Step 10: Handle PENDING\_STEP\_UP

If further information is required after initial submission, Modulr sends an `APPLICATION_STATUS_CHANGE` webhook with status `PENDING_STEP_UP`.

When you receive this:

1. Notify your customer that further information is required.
2. Re-invoke the SDK (repeat <Anchor target="_blank" href="https://modulr.readme.io/docs/customer?isFramePreview=true#step-5-create-a-short-lived-token">Steps 6-9</Anchor>) using the same `applicationId`. A fresh short-lived token is required for each invocation.
3. The SDK will automatically surface the step-up form for the outstanding requirements.

This applies both after automated CDD checks and after a manual review decision - meaning these notifications could come back within a few seconds for automated step-ups, or hours/days after the initial submission depending on the complexity of the manual review.

***

## Step 11: Receive CUSTOMER\_CREATED

Once the application reaches `APPROVED` status, Modulr sends a `CUSTOMER_CREATED` webhook containing the new `customerId`.

Store the `customerId` against your customer record. Use it in subsequent <Anchor target="_blank" href="https://modulr.readme.io/reference/createaccount">Account Creation API</Anchor> calls.

See the full webhook reference: <Anchor target="_blank" href="https://modulr.readme.io/docs/webhook-customer-created">Webhook - Customer Created</Anchor>

***

## Step 12: Monitor CUSTOMER\_STATUS\_CHANGE

Once a customer is live on Modulr, monitor the `CUSTOMER_STATUS_CHANGE` webhook to track ongoing lifecycle events, including `BLOCKED` status which prevents payment processing.

See the full webhook reference: <Anchor target="_blank" href="https://modulr.readme.io/docs/customer-status">Webhook - Customer Status Change</Anchor>

***

## Integration Checklist

| Step | Item                                                 | Required?                        |
| ---- | ---------------------------------------------------- | -------------------------------- |
| 1    | Create Application                                   | Yes                              |
| 2    | Submit KYC/KYB Data via API                          | Optional                         |
| 3    | Handle APPLICATION\_STATUS\_CHANGE webhook           | Yes                              |
| 4    | Upload ID verification docs / biometric selfie image | Optional                         |
| 5    | Initiate Application Verification                    | Only if using API pre-population |
| 6    | Create Short-lived Token                             | Yes                              |
| 7    | Initialise SDK                                       | Yes                              |
| 8    | Open SDK                                             | Yes                              |
| 9    | Close SDK                                            | Yes                              |
| 10   | Handle PENDING\_STEP\_UP                             | Yes                              |
| 11   | Handle CUSTOMER\_CREATED webhook                     | Yes                              |
| 12   | Handle CUSTOMER\_STATUS\_CHANGE webhook              | Yes                              |