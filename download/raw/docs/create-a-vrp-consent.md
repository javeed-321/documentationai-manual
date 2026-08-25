---
updatedAt: 2026-08-12T09:15:54.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# VRP consent

Creating a consent and revoking a consent

<Callout icon="📘" theme="info">
  ### Purpose of VRP consent

  The VRP consent defines the parameters within which sweeping VRP payments can be made

  Setting up the VRP consent means a PSU does not have to authenticate individual payments with their bank (as they do with PIS) so long as the payment is within the parameters of the consent

  The consent process generates a Consent ID which is used to make subsequent VRP payments

  Providing VRP consent is the first step in the customer journey. If the PSU has not provided consent, then no VRP payments can be made
</Callout>

## Consent parameters

There are 5 parameters contained in the consent – these are covered in detail further down this page:

1. **Time period** – period during which the ‘Maximum amount per period’ is applied. User must select one of Day, Week, Fortnight, Month, Half-Year, Year
2. **Maximum amount per period** – limit on the cumulative value of payments within the time period. User must populate this parameter
3. **Maximum amount per payment** – limit on the value of an individual payment that can be made. User must populate this parameter
4. **Period start date** – date the consent starts from. This can be left blank; see next slide for further details
5. **Expiry date** – date the consent ends. This can be left blank; see next slide for further details

## Creating a VRP consent

The diagram below provides a high-level overview of the VRP consent creation process.

![](https://files.readme.io/7f0ec59-image.png)

## Step 1: Listing the banks that support standing order initiation

As part of the consent authentication process the user will need to select their bank so that they can be directed to the relevant authentication URL.

You should use the [GET ASPSPs API](https://modulr.readme.io/reference/getaspsproviders) to fetch the latest list of banks and their supported capabilities (such as Sweeping VRP, Single Immediate Payments and Standing Order).

Only institutions that support the capability type **SWEEPING\_VRP** and are Enabled should be offered to the end-user.

This list may change from time-to-time, as we add new banks or change their supported capabilities, so you must ensure that your application can handle changes dynamically.

```json GET /aspsps
[
  {
    "type" : "SINGLE_IMMEDIATE",
    "status" : "DISABLED"
  },
  {
    "type" : "STANDING_ORDER",
    "status" : "DISABLED"
  },
  {
    "type" : "SWEEPING_VRP",
    "status" : "ENABLED"
  }
]
```

## Step 2: Create a VRP consent

### Request

This request creates a VRP consent for authorisation by the payment service user. The consent can then be used to initiate one or more payments within the parameters contained in the consent.

When creating a consent, you can set various restrictions like start and end dates, individual payment limits, and periodic limits. Periodic limits let you determine the maximum amount that can be paid through the consent during a certain time period.

```json POST /vrp-consents
{
  "aspspId": "H100000001",
  "destination": {
    "type": "ACCOUNT",
    "id": "A1100001",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "Test"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "string",
      "amount": 100
    },
    "periodicLimits": [
      {
        "currency": "string",
        "amount": 100,
        "periodAlignment": "string",
        "periodType": "string"
      }
    ]
  },
  "validFromDate": "2022-01-31T20:16:01.9Z",
  "validToDate": "2022-07-31T20:16:01.9Z",
  "type": "string",
  "reference": "Invoice ABC123"
}
```

### Response - created

```json POST /vrp-consents
{
  "vrpConsentInitiationId": "I000000001",
  "redirectUrl": "https://www.bankofmoney.com/authorize"
}
```

### Response - bad request

```json POST /vrp-consents
  {
    "field": "string",
    "code": "GENERAL",
    "errorCode": "string",
    "message": "string",
    "sourceService": "string"
  }
```

### Consent Status Model

The following responses are returned from the **/POST vrp-consents** endpoint upon creating a VRP consent:

| Consent State           | Description                                                                                            |
| :---------------------- | :----------------------------------------------------------------------------------------------------- |
| AWAITING\_AUTHORISATION | The consent is awaiting authorisation by the payment service user.                                     |
| AUTHORISED              | The consent has been successfully authorised.                                                          |
| REJECTED                | The consent has been rejected by the payment service user.                                             |
| REVOKED                 | The consent resource has been revoked by the payment service user.                                     |
| EXPIRED                 | The consent has expired - only applicable if a consent expiry date was specified during consent set-up |
| ER\_GENERAL             | Generic error occurred when processing the VRP consent initiation.                                     |
| ER\_EXTSYS              | The VRP consent initiation failed because there was a problem communicating with the bank’s systems.   |

### Consent parameter definitions

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>

      <th>
        Request M/O/C
      </th>

      <th>
        Validation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        aspspId
      </td>

      <td>
        Identifier of the payer’s ASPSP where the consent will be created. The ASPSP must have the “SWEEPING” capability enabled (which can be checked using our API).
      </td>

      <td>
        String 10
      </td>

      <td>
        M
      </td>

      <td>
        ASPSP must have the sweeping capability enabled otherwise the request to create the consent must be rejected.
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        Type of VRP consent that will be created. Must be one of “SWEEPING” or “NON_SWEEPING”. Note that “NON_SWEEPING” is not yet available.
      </td>

      <td>
        Enum
      </td>

      <td>
        M
      </td>

      <td>
        Can be one of:

        - SWEEPING
        - NON_SWEEPING. If NON_SWEEPING is submitted, request should be rejected with forbidden.
      </td>
    </tr>

    <tr>
      <td>
        destination
      </td>

      <td>
        Destination account details that will receive variable recurring payments initiated using this consent.
      </td>

      <td>
        Object
      </td>

      <td>
        M
      </td>

      <td>
        -
      </td>
    </tr>

    <tr>
      <td>
        destination.type
      </td>

      <td>
        Indicates the type of destination account. Use “ACCOUNT” if the destination account is a Modulr account otherwise use “SCAN” and provide the corresponding account details.
      </td>

      <td>
        Enum
      </td>

      <td>
        M
      </td>

      <td>
        Can be one of:

        - ACCOUNT
        - SCAN
      </td>
    </tr>

    <tr>
      <td>
        destination.id
      </td>

      <td>
        Identifier of the Modulr account when using “ACCOUNT” type.
      </td>

      <td>
        String 8 to 10
      </td>

      <td>
        C
      </td>

      <td>
        Must be provided if destination.type is ACCOUNT.
      </td>
    </tr>

    <tr>
      <td>
        destination.accountNumber
      </td>

      <td>
        Account Number of the destination account when using “SCAN” type.
      </td>

      <td>
        String 8
      </td>

      <td>
        C
      </td>

      <td>
        Must be provided if destination.type is SCAN.
      </td>
    </tr>

    <tr>
      <td>
        destination.sortCode
      </td>

      <td>
        Sort Code of the destination account when using “SCAN” type.
      </td>

      <td>
        String 6
      </td>

      <td>
        C
      </td>

      <td>
        Must be provided if destination.type is SCAN.
      </td>
    </tr>

    <tr>
      <td>
        destination.name
      </td>

      <td>
        Name of the destination account when using “SCAN” type.
      </td>

      <td>
        String 70
      </td>

      <td>
        C
      </td>

      <td>
        Must be provided if destination.type is SCAN.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints
      </td>

      <td>
        Limits that will apply to payments initiated using this consent.
      </td>

      <td>
        Object
      </td>

      <td>
        M
      </td>

      <td>
        -
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.maximum<br />IndividualAmount
      </td>

      <td>
        Maximum amount of any single payment initiated using this consent.
      </td>

      <td>
        Object
      </td>

      <td>
        M
      </td>

      <td>
        -
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.maximum<br />IndividualAmount.amount
      </td>

      <td>
        Maximum amount of any single payment initiated using this consent.
      </td>

      <td>
        String
      </td>

      <td>
        M
      </td>

      <td>
        Positive amounts with a maximum of two decimal places.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.maximum<br />IndividualAmount.currency
      </td>

      <td>
        Currency of the maximum individual amount. Must be specified in ISO 4217 format.
      </td>

      <td>
        String
      </td>

      <td>
        M
      </td>

      <td>
        Only allowable value is GBP.<br />Must be specified in ISO 4217 format.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.<br />periodicLimits
      </td>

      <td>
        Maximum amount of all payments that can be initiated using this consent in a given period. If the periodAlignment is “Calendar”, the limit is pro-rated in the first period to the remaining number of days.
      </td>

      <td>
        Object
      </td>

      <td>
        M
      </td>

      <td>
        -
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.<br />periodicLimits.amount
      </td>

      <td>
        The maximum amount of all payments initiated using this consent in the specified period. At least one periodic limit is required.
      </td>

      <td>
        String
      </td>

      <td>
        M
      </td>

      <td>
        There must be at least one periodic limit supplied.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.<br />periodicLimits.currency
      </td>

      <td>
        Currency of the maximum amount. Must be specified in ISO 4217 format.
      </td>

      <td>
        String
      </td>

      <td>
        M
      </td>

      <td>
        Only allowable value is GBP.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.<br />periodicLimits.periodAlignment
      </td>

      <td>
        Specifies whether the period starts on the date of consent creation or lines up with a calendar.
      </td>

      <td>
        Enum
      </td>

      <td>
        M
      </td>

      <td>
        Can be one of:

        - CONSENT
        - CALENDARValidate that only one type is used per consent.
      </td>
    </tr>

    <tr>
      <td>
        paymentContraints.<br />periodicLimits.periodType
      </td>

      <td>
        Period type. Must be one of “DAY”, ”WEEK”, ”FORTNIGHT”, ”MONTH”, ”HALF_YEAR”, ”YEAR”.
      </td>

      <td>
        Enum
      </td>

      <td>
        M
      </td>

      <td>
        Can be one of:

        - DAY
        - WEEK
        - FORTNIGHT
        - MONTH
        - HALF_YEAR
        - YEARValidate that there are no duplicates.
      </td>
    </tr>

    <tr>
      <td>
        validFromDate
      </td>

      <td>
        Start date time from which payments can be initiated using this consent. Must be specified using YYYY-MM-DDTHH:mm:ssZ format.

        If you do not specify a value, the consent will be created using the value provided by the bank.
      </td>

      <td>
        ISODateTime
      </td>

      <td>
        O
      </td>

      <td>
        Must match YYYY-MM-DDTHH:mm:ssZ format.

        Must be equal to, or later to the current date.
      </td>
    </tr>

    <tr>
      <td>
        validToDate
      </td>

      <td>
        End date time after which payments cannot be initiated using this consent. Must be specified using YYYY-MM-DDTHH:mm:ssZ format.

        If you do not specify a value, the consent will be created using the value provided by the bank.
      </td>

      <td>
        ISODateTime
      </td>

      <td>
        O
      </td>

      <td>
        Must match YYYY-MM-DDTHH:mm:ssZ format.

        Must be later than or equal to the valid from date.
      </td>
    </tr>

    <tr>
      <td>
        Reference
      </td>

      <td>
        A reference to be used for the consent.  Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space.
      </td>

      <td>
        String
      </td>

      <td>
        O
      </td>

      <td>
        Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space.
      </td>
    </tr>
  </tbody>
</Table>

Regarding the field **paymentContraints.periodicLimits.periodAlignment** the definitions for `consent` and `calendar` are as follows:

| Period Alignment | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `consent`        | Maximum amount that can be paid during the defined time period (week, month, etc.) starts from the moment the user agrees the consent.                                                                                                                                                                                                                                                                                                                                                                                |
| `calendar`       | Maximum amount that can be paid during the defined time period (week, month, etc.) is based on calendar dates. Should the user give consent halfway through a period, the maximum amount is proportionately adjusted to cover the remaining duration of that time period. For example, if a user sets a maximum amount of £10,000 per month and provides consent halfway through the month, for the remainder of that month they can pay £5,000. This will then reset back to £10,000 at the start of the next month. |

## Retrieve a VRP consent (optional)

Use the **Consent ID** to retrieve information about a given Variable Recurring Payment consent. Only the customer/partner that created the consent has access to read the consent.

```json GET /vrp-consents/{consentId}
{
  "aspspId": "H100000001",
  "destination": {
    "type": "ACCOUNT",
    "id": "A1100001",
    "accountNumber": "12345678",
    "sortCode": "000000",
    "name": "Test"
  },
  "paymentConstraints": {
    "maximumIndividualAmount": {
      "currency": "string",
      "amount": 100
    },
    "periodicLimits": [
      {
        "currency": "string",
        "amount": 100,
        "periodAlignment": "string",
        "periodType": "string"
      }
    ]
  },
  "reference": "Invoice ABC123",
  "validFromDate": "2022-01-31T20:16:01.9Z",
  "validToDate": "2022-07-31T20:16:01.9Z",
  "type": "string",
  "status": "string"
}
```

The [/GET endpoint](https://api-sandbox.modulrfinance.com/api-sandbox-token/vrp/\{vrpPaymentId}) will return a list of the following statuses:

| Status | Description                                            |
| ------ | ------------------------------------------------------ |
| AWAU   | The consent resource is awaiting PSU authorisation.    |
| RJCT   | The consent resource has been rejected.                |
| AUTH   | The consent resource has been successfully authorised. |
| CANC   | The consent resource has been canceled.                |
| EXPD   | The consent resource has expired.                      |

###

## Revoke a VRP consent

Use the **Consent ID** to cancel a VRP consent - this removes the ability to make further variable recurring payments using the consent. Information about the consent can still be retrieved and viewed by the user after the consent has been revoked.

```shell DELETE /vrp-consents/{consentId}
DELETE https://api.modulrfinance.com/vrp-consents/I000000001
```
```Text DELETE response
202 Accepted
```

<Callout icon="🚧" theme="warn">
  ### Warning

  It is important to note that revoked consents cannot be reinstated. The user must create a new VRP consent if they wish to set up recurring payments. See ‘Create VRP consent’ for details.
</Callout>

## Bank Specific Limitations

Some banks have limitations in their VRP behaviour, these can be found below:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Bank
      </th>

      <th>
        Limitation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Monzo
      </td>

      <td>
        The`periodicLimits.periodAlignment` can be of type `CONSENT` only.

        The `periodicLimits.periodtype`can only be defined as `MONTHLY` or `YEARLY`
      </td>
    </tr>
  </tbody>
</Table>