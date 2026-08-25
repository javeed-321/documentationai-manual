---
updatedAt: 2025-09-05T18:35:22.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Returned Payments

## Background

Outbound payments can be returned to us for a variety of reasons.

When outbound payments are returned to us, they are payments into our platform so we trigger sending the [PAYIN Webhook](https://modulr.readme.io/docs/payin-webhook).

We are normally provided with the reason for the return in the form of a code, with each payment scheme having their own codes. So you can understand the reason why a payment was returned, we map these codes into a consolidated list of return reasons which we provide in the ReturnReason field of the PAYIN webhook.

## Return Reasons

The list of "Return Reasons" with a description as to what each Return Reason means is outlined below:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Return Reason
      </th>

      <th>
        Meaning
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ACCADDRESSINVALID
      </td>

      <td>
        The beneficiaries address was missing or invalid
      </td>
    </tr>

    <tr>
      <td>
        ACCNOCURRENCY
      </td>

      <td>
        The account was not in the currency specified in the payment
      </td>
    </tr>

    <tr>
      <td>
        ACCNOREFINFO
      </td>

      <td>
        The account could not be identified and requires information in the reference field to do so.
      </td>
    </tr>

    <tr>
      <td>
        ACCTRANSFERRED
      </td>

      <td>
        The account has been transferred to another provider
      </td>
    </tr>

    <tr>
      <td>
        BENSCANUNKNOWN
      </td>

      <td>
        The account is unknown
      </td>
    </tr>

    <tr>
      <td>
        BENACCCLOSED
      </td>

      <td>
        The account has been closed
      </td>
    </tr>

    <tr>
      <td>
        BENACCNAMEBENACCNR
      </td>

      <td>
        The beneficiaries name did not match that on the account
      </td>
    </tr>

    <tr>
      <td>
        BENACCSTOPPED
      </td>

      <td>
        The account has been blocked
      </td>
    </tr>

    <tr>
      <td>
        BENDECEASED
      </td>

      <td>
        The beneficiary is deceased
      </td>
    </tr>

    <tr>
      <td>
        BENREQ
      </td>

      <td>
        At the request of the beneficiary
      </td>
    </tr>

    <tr>
      <td>
        BICINVALID
      </td>

      <td>
        The wrong BIC was supplied
      </td>
    </tr>

    <tr>
      <td>
        DUPLICATE
      </td>

      <td>
        The payment was deemed to be a duplicate
      </td>
    </tr>

    <tr>
      <td>
        RECALL
      </td>

      <td>
        As the result of a successful recall request
      </td>
    </tr>

    <tr>
      <td>
        REGULATION
      </td>

      <td>
        A regulatory requirement was not met
      </td>
    </tr>

    <tr>
      <td>
        SENDERREQ
      </td>

      <td>
        At the request of the sender
      </td>
    </tr>

    <tr>
      <td>
        SENSITIVITIES
      </td>

      <td>
        No reason specified due to sensitive nature
      </td>
    </tr>

    <tr>
      <td>
        TANDC
      </td>

      <td>
        The terms & conditions of the account prevented the payment being credited
      </td>
    </tr>

    <tr>
      <td>
        OTHER
      </td>

      <td>
        The precise reason cannot be ascertained
      </td>
    </tr>
  </tbody>
</Table>