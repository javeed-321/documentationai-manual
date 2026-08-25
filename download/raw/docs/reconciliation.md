---
updatedAt: 2025-09-30T09:33:34.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Combining Webhooks and APIs

Making best use of the Modulr APIs and webhooks combined

## Connected Data Fields

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>
        Get Payments
      </th>

      <th style={{ textAlign: "left" }}>
        Get Transactions
      </th>

      <th style={{ textAlign: "left" }}>
        PAYIN Webhook
      </th>

      <th style={{ textAlign: "left" }}>
        PAYOUT Webhook
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Modulr Payment ID (Pbid)
      </td>

      <td style={{ textAlign: "left" }}>
        id
      </td>

      <td style={{ textAlign: "left" }}>
        sourceId
      </td>

      <td style={{ textAlign: "left" }}>
        PaymentId
      </td>

      <td style={{ textAlign: "left" }}>
        PaymentId
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Modulr Transaction ID (Tbid)
      </td>

      <td style={{ textAlign: "left" }}>
        N/a
      </td>

      <td style={{ textAlign: "left" }}>
        id
      </td>

      <td style={{ textAlign: "left" }}>
        TransactionId
      </td>

      <td style={{ textAlign: "left" }}>
        TransactionId
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Receiving Account (ABid)\
        Inbound Payment
      </td>

      <td style={{ textAlign: "left" }}>
        accountNumber
      </td>

      <td style={{ textAlign: "left" }}>
        account / id
      </td>

      <td style={{ textAlign: "left" }}>
        AccountId
      </td>

      <td style={{ textAlign: "left" }}>
        N/a
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payment External Reference
      </td>

      <td style={{ textAlign: "left" }}>
        externalReference
      </td>

      <td style={{ textAlign: "left" }}>
        N/a
      </td>

      <td style={{ textAlign: "left" }}>
        SourceExternalReference
      </td>

      <td style={{ textAlign: "left" }}>
        ExternalReference
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payment Scheme Identifier
      </td>

      <td style={{ textAlign: "left" }}>
        schemeId
      </td>

      <td style={{ textAlign: "left" }}>
        schemeInfo / id
      </td>

      <td style={{ textAlign: "left" }}>
        schemeId
      </td>

      <td style={{ textAlign: "left" }}>
        schemeInfo / Id
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payment Scheme Reference
      </td>

      <td style={{ textAlign: "left" }}>
        originalReference\
        paymentDescription\
        (part of) Description
      </td>

      <td style={{ textAlign: "left" }}>
        (part of) Description
      </td>

      <td style={{ textAlign: "left" }}>
        (part of) PaymentReference
      </td>

      <td style={{ textAlign: "left" }}>
        Reference
      </td>
    </tr>
  </tbody>
</Table>

Where information appears above as “(part of)”, it means that the field is concatenated with other data items. Payment scheme reference appears after the name of who the payment is from/to.

* Inbound example: “Payment from Hermione Grainger: For herbs”. Hermione Grainger is the Payer’s name on the account and the payment scheme reference used was “For herbs”.

## Combining APIs and Webhooks

**Internal Transfers**

The [Create a Payment](https://modulr.readme.io/reference/sendpayment) endpoint is used to move money from one Modulr account to another Modulr account.

On the sending account (payer) there will be a payment and debit transaction and the PAYOUT webhook will trigger.

On the receiving account (payee) there will be a payment and a credit transaction and the PAYIN webhook will trigger.

Information is available via Get Payments for types of payments, status, etc.

Get Transactions provides all processed credits / debits against a single accountId.

**Payments Out**

The same [Create a Payment](https://modulr.readme.io/reference/sendpayment) endpoint is used to make a payment from a Modulr account to an external bank account.

On the sending Modulr account (payer) there will be a payment and debit transaction and the PAYOUT webhook will trigger via an update from the Faster Payment or SEPA scheme confirming success of each individual payment made. The Payment record is updated with the scheme reference.

Information is available via Get Payments for types of payments, status, etc.

Get Transactions provides all processed credits / debits against a single accountId.