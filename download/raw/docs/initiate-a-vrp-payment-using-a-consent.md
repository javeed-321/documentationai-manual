---
updatedAt: 2026-08-12T09:21:13.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Initiate a VRP payment

Initiate a sweeping VRP payment using the authorised consent

<Callout icon="🚧" theme="warn">
  ### VRP payments

  VRP payments can only be initiated once the user has successfully set up their consent
</Callout>

## Initiating a VRP payment

The diagram below provides a high-level overview of the VRP payment process.

![](https://files.readme.io/deb0658-image.png)

<br />

## Step 1: Initiate a VRP payment

This [API request ](https://modulr.readme.io/reference/initiatevrppayment)initiates a new Variable Recurring Payment using an existing authorised consent.

VRP Payment initiation will only be available against an Authorised consent. Request that are made when the consent is in Awaiting Authorisation / Revoke / Rejected / Error state will return an unsuccessful response.

A user will only be able to use the consent ID that belongs to them. If an incorrect consent ID is used, the VRP payment initiation will return an unsuccessful response.

```json POST /vrp
{
  "consentId": "string",
  "payment": {
    "currency": "string",
    "amount": 0,
    "reference": "string"
}
```

### Consent parameter definitions

<Table align={["left","left","left","left"]}>
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
        Validation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        consentId
      </td>

      <td>
        The id of the consent being used to make this payment. Note that if the consent is not authorised, the payment will not be initiated.
      </td>

      <td>
        String 10
      </td>

      <td>
        Consent id specified must belong to the user making the API call and also be in an authorised state (per the status in our DB).
      </td>
    </tr>

    <tr>
      <td>
        Payment
      </td>

      <td>
        Payment amount and currency.
      </td>

      <td>
        Object
      </td>

      <td>
        -
      </td>
    </tr>

    <tr>
      <td>
        payment.amount
      </td>

      <td>
        Amount.
      </td>

      <td>
        String
      </td>

      <td>
        Positive amounts with a maximum of two decimal places.
      </td>
    </tr>

    <tr>
      <td>
        payment.currency
      </td>

      <td>
        Currency of the payment, specified in ISO 4217 format.
      </td>

      <td>
        String
      </td>

      <td>
        Only allowable value is GBP.

        Must be specified in ISO 4217 format.
      </td>
    </tr>

    <tr>
      <td>
        payment.reference
      </td>

      <td>
        A reference used to unambiguously refer to the payment transaction. Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space.
      </td>

      <td>
        String
      </td>

      <td>
        Min 6 to max 18 characters. Can contain alphanumeric, '-', '.', '&', '/' and space.

        If the reference field on the consent is present, this field has to match it.
      </td>
    </tr>
  </tbody>
</Table>

Example showing when VRP has been initiated:

```json POST /vrp
{
  "id": "string",
  "status": "SUBMITTED"
}
```

Example showing when the payment has not been processed because the consent does not exist:

```json POST /vrp
{
  "field": "string",
  "code": "GENERAL",
  "errorCode": "string",
  "message": "string",
  "sourceService": "string"
}
```

### Modulr status codes

The following codes are returned from the Modulr service using the POST/ endpoint:

| Name        | Completion state? | Description                                                                                      |
| ----------- | ----------------- | ------------------------------------------------------------------------------------------------ |
| SUBMITTED   | No                | Payment instruction submitted, status pending                                                    |
| ER\_GENERAL | No                | Generic error occurred when processing the payment initiation.                                   |
| ER\_EXTSYS  | No                | The payment initiation failed because there was a problem communicating with the bank's systems. |

### Confirm the availability of funds in an account (optional)

<Callout icon="📘" theme="info">
  ### Availability of funds

  This is an optional step, however confirming funds in the account that money is being swept from prior to making the payment reduces the likelihood of a failed payment due to lack of funds.
</Callout>

Use the **Consent ID** to confirm the availability of funds in an account via the [confirmation API](https://modulr.readme.io/reference/confirmfunds), prior to initiating a Variable Recurring Payment.

```json POST /vrp-consents/{consentId}/fund-confirmation
{
"currency": "GBP",
"amount": "1.00"
}
```

If the fund availability request is successful, you’ll get a response with the following fields:

```json POST /vrp-consents/{consentId}/funds-confirmation
{
  "fundsAvailable": true,
  "fundsAvailabilityCheckDateTime": "2024-04-25T12:00:50.047Z"
}
```

<Callout icon="🚧" theme="warn">
  ### External balance

  Note - the user is not able to view the balance of the crediting account, only whether the funds are available based on the value the user wishes to sweep.
</Callout>

### Get the status of a VRP payment (optional)

Fetch the details of a payment initiated using VRP based on a unique **Payment ID**.

The [GET /vrp/\{id} endpoint](https://modulr.readme.io/reference/getvrppayment) is used to retrieve the specific VRP payment details. This includes all the information tied to that payment such as consentId, payment and status. The unique payment ID, which is a required path parameter, identifies the specific payment to be retrieved. This API is essential for clients who want to verify the initiated payment and provide their end users with detailed information which will help them track the payment's progress. The endpoint responds with the full payment details in a JSON format if the payment ID is valid and exists in the system.

```json GET /vrp/{id}
{
  "consentId": "string",
  "payment": {
    "currency": "string",
    "amount": 0,
    "reference": "string"
  },
  "status": "string"
}
```

### Payment Status Model

| Name                                       | Completion state? | Description                                                                                                                                                                                                                                                                                                                                                              |
| :----------------------------------------- | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ACCEPTEDSETTLEMENTCOMPLETEDCREDITORACCOUNT | Yes               | Settlement on the creditor's account has been completed.                                                                                                                                                                                                                                                                                                                 |
| ACCEPTEDSETTLEMENTCOMPLETEDDEBITORACCOUNT  | Yes               | Settlement completed. Usage: this can be used by a Market Infrastructure reporting to Infrastructure Participant or an Account Servicer to Account Owner to report that the transaction account entry has been completed. Warning: this status is provided for transaction status reasons, not for financial information. It can only be used after bilateral agreement. |
| ACCEPTEDCUSTOMERPROFILE                    | No                | Preceding check of technical validation was successful. Customer profile check was also successful.                                                                                                                                                                                                                                                                      |
| ACCEPTEDSETTLEMENTINPROCESS                | No                | All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution.                                                                                                                                                                                                             |
| ACCEPTTECHNICALVALIDATION                  | No                | Authentication and syntactical and semantical validation are successful.                                                                                                                                                                                                                                                                                                 |
| ACCEPTEDWITHCHANGE                         | No                | Instruction is accepted but a change will be made, such as date or remittance not sent.                                                                                                                                                                                                                                                                                  |
| ACCEPTEDWITHOUTPOSTING                     | No                | Payment instruction included in the credit transfer is accepted without being posted to the creditor customer's account.                                                                                                                                                                                                                                                 |
| BLOCKED                                    | No                | Payment transaction previously reported with status 'AcceptedWithoutPosting' is blocked, for example, funds will neither be posted to the Creditor's account, nor be returned to the Debtor.                                                                                                                                                                             |
| CANCELLED                                  | No                | Payment initiation has been successfully cancelled after having received a request for cancellation. Usage: code to be used in context of AOS only.                                                                                                                                                                                                                      |
| PENDING                                    | No                | Payment initiation or individual transaction included in the payment initiation is pending. Further checks and status update will be performed.                                                                                                                                                                                                                          |
| RECEIVED                                   | No                | Payment instruction has been received.                                                                                                                                                                                                                                                                                                                                   |
| REJECTED                                   | No                | Payment initiation or individual transaction included in the payment initiation has been rejected.                                                                                                                                                                                                                                                                       |

###

### Decprecated v3.1 codes

The following codes will not be supported in v4, this list will be updated if there are more:

`ACCEPTEDSETTLEMENTCOMPLETED`

`ACCEPTEDCREDITSETTLEMENTCOMPLETED`