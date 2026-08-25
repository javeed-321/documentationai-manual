---
updatedAt: 2025-10-03T16:36:10.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Sending verification of payee checks

To send a name check request, please connect to the [Verify Payee API](https://modulr.readme.io/reference/createoutboundvop)

### Note: EU wide VoP roll out 5-9 Oct

**The Verification of Payee (VoP) service rolls out across the EU as a scheme from Sunday 5th Oct from 04:00 (BST).** The Modulr production API endpoints are available shortly and until this point will respond `Check not possible` to any request.

**The roll out and reach of VoP will happen gradually as banks and PSP systems join the network.** From scheme going live on Sunday 5th partners and clients will initially be able to perform name checks on Modulr accounts only, with checks to external accounts at other Banks and PSPs likely to return `check not possible`. From Monday 6th October, this will improve each day leading up to Thursday 9th as the VoP network stabilises in Bank and PSP participation.

As a reminder, the`Check not possible` response does **not** indicate a negative response e.g. any issue with the beneficiary details - only that a check could not be performed (as would be the case before the VoP service launch). It should not be interpreted as payment should be automatically abandoned by your system; if the Payer is present payer should be informed and make a decision if they wish to proceed.

### API fields required

To submit a verification of payee check, a name and IBAN must be provided.  You **must** include **one** of the `paymentAccountID` or `customerID` identifiers - depending on how you're using the service:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        API field
      </th>

      <th>
        status
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `name`
      </td>

      <td>
        required
      </td>

      <td>
        The payee account name.

        This should include both first name(s) and last name(s) and they should be separated by a space. You should not include titles or honorifics. Up to 140 characters and can include diacritics as appropriate.
      </td>
    </tr>

    <tr>
      <td>
        `iban`
      </td>

      <td>
        required
      </td>

      <td>
        The payee's IBAN number, used to identify individual accounts. Made up of up to 34 letters and numbers.
      </td>
    </tr>

    <tr>
      <td>
        `paymentAccountId`
      </td>

      <td>
        optional
      </td>

      <td>
        The Modulr payment account id where your SEPA payment will be initiated from.
      </td>
    </tr>

    <tr>
      <td>
        `customerId`
      </td>

      <td>
        optional
      </td>

      <td>
        The Modulr customer ID you are assigned to.
      </td>
    </tr>
  </tbody>
</Table>

<br />

> ⚠️ Important - `paymentAccountID` or `customerID`
>
> * Only include **one** of the two, submitting more than one will cause the request to fail.
>
> **`paymentAccountId`**
> Use this if the request is linked to a payment from a Modulr account. This is the most typical usage.
>
> **`customerId`**
> Use this if you're using the service *independently* of a payment (using Modulr as a technical VoP provider). Note: you must have a contractual agreement with Modulr for this service; an error will be returned if not in place.

# Testing your integration within the sandbox environment

The sandbox environment is loaded with specific data that allows you to test the four scenarios as listed below by providing the respective inputs for different outcomes.

* `Match`
* `No match`
* `Close match`
* `Check not possible`

**Note**❗️:  The example request below a fictitious account ID. Replace this with your account ID(s) in the sandbox.

* We will always return a MATCH result unless simulating another result using the example name(s) and IBAN(s) below

**MATCH AND CLOSE MATCH**

```json Match request
{
  "name": "Isabelle Marie Dubois",
  "iban": "FR9317569000707197247234A34",
  "paymentAccountId": "A123AAA4"
}
```
```json Match response
{
  "id":"PAV0000001",
  "result": { 
    "code": "MATCH"
    }
}
```
```json Close match request
{
  "name": "Isabelle Marie",
  "iban": "FR9317569000707197247234A34",
  "paymentAccountId": "A123AAA4"
}
```
```json Close match response
{
  "id":"PAV0000001",
  "result": { 
    "code": "CLOSE_MATCH",
    "matchedName": "Isabelle Marie Dubois"
    }
}
```

**NO MATCH AND CHECK NOT POSSIBLE**

```json No match request
{
  "name": "Jhon Nowak",
  "iban": "FR9317569000707197247234A34",
  "paymentAccountId": "A123AAA4"
}
```
```json No match response
{
  "id":"PAV0000001",
  "result": { 
    "code": "NO_MATCH"
    }
}
```
```json Check not possible request
{
  "name": "TinTin",
  "iban": "NL19INGB2128949858",
	"paymentAccountId": "A123AAA4"
}
```
```json Check not possible response
{
  "id":"PAV0000001",
  "result": { 
    "code": "CHECK_NOT_POSSIBLE"
    }
}
```

# Interpreting name check responses

There are four outcomes of a successful request:

**MATCH**

The account details (name and IBAN) provided matched the information held by the payee bank. You can proceed with making your payment if you would like this in scenario.

**NO MATCH**

The account details (name or IBAN) do not match the account details of the payee bank. Proceeding with the payment could lead to the funds being sent to the wrong account and you may not be able to recover the money. You are advised to double check the details of the payment.

If there are updated account details, a new check will be run again.

**CLOSE MATCH**

The provided payee name closely resemble the payee holder name. In this scenario, we will also return the name held at the payer bank. In this case, you should still double check the details of the payment before proceeding. Proceeding with the payment could lead to the funds being sent to the wrong account and you may not be able to recover the money.

**CHECK NOT POSSIBLE**

Payee verification check is not possible or applicable at this time. You may choose to retry later or double check the details of payment before proceeding. Proceeding with the payment could lead to the funds being sent to the wrong account and you may not be able to recover the money.

### Result codes

The table list the possible results of a verification check and the action we recommend you take in each scenario:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        code
      </th>

      <th>
        HTTP status code
      </th>

      <th>
        Description
      </th>

      <th>
        Recommended action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        MATCH
      </td>

      <td>
        200
      </td>

      <td>
        The details provided matched the payee bank details.
      </td>

      <td>
        You can proceed with the payment.

        **Remember, you should still exercise caution when sending payments. The service is an account name checking service and does not protect against all types of fraud.**
      </td>
    </tr>

    <tr>
      <td>
        NO_MATCH
      </td>

      <td>
        200
      </td>

      <td>
        The account details provided do not match the payee bank details.
      </td>

      <td>
        The account details should be checked carefully, you are advised not to proceed with the payment.

        Authorising the payment could result in transferring the funds to a payment account
        not held by your intended recipient.

        **You should edit the details if possible, and submit another account verification check request before proceeding.**
      </td>
    </tr>

    <tr>
      <td>
        CLOSE_MATCH
      </td>

      <td>
        200
      </td>

      <td>
        The name provided is similar to the payee account name. The actual name is provided in matchedName.
      </td>

      <td>
        The account details should be checked carefully.

        **If you decide to continue with the payment you should update the details before proceeding.**
      </td>
    </tr>

    <tr>
      <td>
        CHECK_NOT_POSSIBLE
      </td>

      <td>
        200
      </td>

      <td>
        The verification check is not possible.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>

    <tr>
      <td>
        INVALID
      </td>

      <td>
        400
      </td>

      <td>
        The request was malformed, missing or non-compliant JSON body or URL parameters.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>

    <tr>
      <td>
        GENERAL
      </td>

      <td>
        500
      </td>

      <td>
        There is a technical error when trying to process the request.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Recording of VoP check being made against payment

It’s important to record that a VoP check was completed for each payment, as this may be needed if the requestor raises a challenge in future. Each VoP check generates a unique ID, which Modulr can use to retrieve the check details, including the outcome. It is **highly recommended** you store this ID within your platform regardless in case of future queries by your customers.

The Payments endpoints will be updated shortly after 9th October with an additional optional `nameCheck` field that can accept the unique ID of a VoP/CoP check (or external ID if you use another provider) shortly; this page will be updated when available.

This field when populated is used to allow straightforward linking of a particular VoP check to a payment - as this involves a change to your payment logic in addition, it is recommended (but not mandated) to use **unless you are an identified partner required to implement VoP as part of IPR compliance**. If you are an identified partner you should schedule engineering development to use of this field as soon as reasonably practical following availability

<br />