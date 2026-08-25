---
updatedAt: 2026-08-12T08:54:07.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Sandbox: Initiating a cVRP consent

## Testing your integration within the sandbox environment

The sandbox environment is preloaded with specific mock data to allow you to simulate defined outcomes, and behaves in a production-like environments.

Responses are driven by the inputs you provide, remember to structure your requests as shown below to trigger each scenario.

Submit a request with a future `validFromDate` and `validToDate`, and all mandatory fields populated.

## Creating a cVRP consent

<Callout icon="📘" theme="info">
  Before submitting, make sure your request adheres to the validation and field requirements set out in [Creating a cVRP Consent](https://modulr.readme.io/docs/creating-a-cvrp-consent).
</Callout>

1. **Select the initiating bank**

   Unlike production, the sandbox does not require you to call the ASPSPs endpoint to retrieve a live list of banks. Sandbox requests are pre-configured to route to a single test institution, "Modulr Bank" with ASPSP id `H210000043` , which skips the redirect/authorisation step so you can test end-to-end without a real bank connection.

   **Use this ASPSP id as the aspspId in your consent request. This is the ASPSP you are initiating the consent from.**
2. **To create a consent** –  use `POST /vrp-consents` and await a return of `vrpConsentInitiationId` with no `redirectUrl`. The consent is automatically set to `AUTHORISED`, so there's no separate authorisation step to complete.

   The destination in a sandbox request is illustrative and you are able to use your existing sort code, account number, and account ID as the `destination` in these requests.

```json Example create consent request
{
  "type": "CVRP1",
  "aspspId": "H210000043",
  "destination": {
    "type": "ACCOUNT",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "GreenWave Energy Ltd"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "GBP",
      "amount": 100
    },
    "periodicLimits": [
      {
        "currency": "GBP",
        "amount": 200,
        "periodAlignment": "CONSENT",
        "periodType": "WEEK"
      }
    ]
  },
  "interactionTypes": ["IN_SESSION", "OFF_SESSION"],
  "validFromDate": "2026-07-29T00:15:13Z",
  "validToDate": "2027-10-05T15:15:13Z",
  "reference": "GWE-VRP-001",
  "ultimateCreditor": {
    "name": "GreenWave Energy Ltd",
    "identification": "12345678",
    "lei": "213800GWENERGY0001AB",
    "postalAddress": {
      "addressType": "BIZZ",
      "department": "Finance",
      "subDepartment": "Accounts Receivable",
      "streetName": "Riverside Way",
      "buildingNumber": "45",
      "buildingName": "GreenWave House",
      "floor": "3",
      "unitNumber": "301",
      "room": "A",
      "postBox": "PO Box 210",
      "townLocationName": "Riverside District",
      "districtName": "Central",
      "careOf": "Accounts Team",
      "postCode": "M1 4WE",
      "townName": "Manchester",
      "countrySubDivision": "Greater Manchester",
      "country": "GB",
      "addressLine": ["45 Riverside Way", "Riverside District"]
    }
  },
  "risk": {
    "merchantCategoryCode": "4900",
    "merchantCustomerIdentification": "CUST-001",
    "contractPresentIndicator": true,
    "beneficiaryPrepopulatedIndicator": true,
    "beneficiaryAccountType": "Business",
    "deliveryAddress": {
      "addressType": "BIZZ",
      "department": "Logistics",
      "subDepartment": "Dispatch",
      "streetName": "Harbour Road",
      "buildingNumber": "12",
      "buildingName": "Harbour Point",
      "floor": "1",
      "unitNumber": "1",
      "room": "Goods In",
      "postBox": "PO Box 118",
      "townLocationName": "Docklands",
      "districtName": "East",
      "careOf": "Warehouse Team",
      "postCode": "M2 5AK",
      "townName": "Manchester",
      "countrySubDivision": "Greater Manchester",
      "country": "GB",
      "addressLine": ["12 Harbour Road", "Docklands"]
    }
  }
}
```
```json Example response
{
  "vrpConsentInitiationId": "E210000BUJ"
}
```

2. **You can also check the consent's status** – `GET /vrp-consents/{id}` returns the consent status.

```json GET/vrp-consents response
{
  "aspspId": "H210000043",
  "destination": {
    "type": "ACCOUNT",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "GreenWave Energy Ltd"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "GBP",
      "amount": 100
    },
    "periodicLimits": [
      {
        "currency": "GBP",
        "amount": 200,
        "periodAlignment": "CONSENT",
        "periodType": "WEEK"
      }
    ]
  },
  "validFromDate": "2026-07-29T00:15:13Z",
  "validToDate": "2027-10-05T15:15:13Z",
  "type": "CVRP1",
  "reference": "GWE-VRP-001",
  "status": "AUTHORISED",
  "interactionTypes": ["OFF_SESSION", "IN_SESSION"]
}
```

## Error scenarios

If you wish to test error states, the sandbox retains the same logic as our production environment when validating an invalid consent scenarios.

Below are some example scenarios you can test with, but note that there may other scenarios you may wish to run through yourself.

## Scenario 1: Validity dates in the past

To simulate a validation failure caused by expired dates, submit a consent where `validFromDate` or `validToDate` fall in the past.

```json Past dates request
{
  "type": "CVRP1",
  "aspspId": "H210000043",
  "destination": {
    "type": "SCAN",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "GreenWave Energy Ltd"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "GBP",
      "amount": 250
    },
    "periodicLimits": [
      {
        "currency": "GBP",
        "amount": 1000,
        "periodAlignment": "CALENDAR",
        "periodType": "MONTH"
      }
    ]
  },
  "interactionTypes": ["InSession", "OffSession"],
  "risk": {
    "merchantCategoryCode": "4900",
    "merchantCustomerIdentification": "CUST-001",
    "contractPresentIndicator": true,
    "beneficiaryPrepopulatedIndicator": true,
    "paymentPurposeCode": "BKDF",
    "categoryPurposeCode": "BONU"
  },
  "validFromDate": "2023-01-01T00:00:00Z",
  "validToDate": "2026-12-01T00:00:00Z",
  "reference": "GWE-VRP-001"
}
```
```json Past dates response
{
  "field": "validToDate",
  "code": "INVALID",
  "message": "validToDate must be a future date"
}
```

## Scenario 2: Individual amount exceeds periodic limit

To simulate a constraint validation failure, submit a consent where `maximumIndividualAmount` is greater than the `periodicLimits` amount. A single payment cannot be permitted to exceed the total period cap.

```json Amount exceeded request
{
  "type": "CVRP1",
  "aspspId": "H210000043",
  "destination": {
    "type": "SCAN",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "GreenWave Energy Ltd"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "GBP",
      "amount": 2000
    },
    "periodicLimits": [
      {
        "currency": "GBP",
        "amount": 1000,
        "periodAlignment": "CALENDAR",
        "periodType": "MONTH"
      }
    ]
  },
  "interactionTypes": ["InSession", "OffSession"],
  "risk": {
    "merchantCategoryCode": "4900",
    "merchantCustomerIdentification": "CUST-001",
    "contractPresentIndicator": true,
    "beneficiaryPrepopulatedIndicator": true,
    "paymentPurposeCode": "BKDF",
    "categoryPurposeCode": "BONU"
  },
  "validFromDate": "2025-01-01T00:00:00Z",
  "validToDate": "2026-01-01T00:00:00Z",
  "reference": "GWE-VRP-001"
}
```
```json Amount exceeded response
{
  "field": "paymentConstraints.maximumIndividualAmount",
  "code": "INVALID",
  "message": "maximumIndividualAmount must not exceed the periodicLimits amount"
}
```