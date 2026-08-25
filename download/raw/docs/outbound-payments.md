---
updatedAt: 2026-06-02T10:06:11.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Outbound Payments

## Outbound Payments Flow

When you request a payment, we perform some initial validation and either accept or reject the request.

If your request is successful you will get a http 2xx response, a unique ID for Modulr for your payment request, and a status of VALIDATED.

At this stage the payment has not been completed, it will shortly be executed by our system, and you should check its status to confirm the payment was successful.

There are a few ways you can do this:

* The most efficient way, if you can support it on your system reliably, is to subscribe to a [notification](https://modulr.readme.io/docs/notifications-1) webhook when the payment has reached a final state, which is a separate topic in this documentation.
* Alternatively you can poll status, which can be done using `GET /payments`, using id you received on the POST request. See the [reference documentation](https://modulr.readme.io/reference/getpayments) for more detail. We do ask that you please use this considerately and not poll continuously. Even though most payments are processed and their status updated within tens of seconds please allow a few minutes before you first check status. If on the rare occasion for some reason it is still pending please wait an increasing number of minutes till you try again, and try a maximum of 5 times. As a suggested example you could try at 3 minutes, 10 minutes, 30 minutes, 2 hours, 4 hours. In the vast majority of cases the first GET should give you the final status, the others are only a precaution in the rare cases there is some delay.
* If the volume of payments is low and you would rather not build this logic in your system, you can sign in to our web portal and check there for any payment failures. It is important that you ensure this is a regular task.

For a list of valid statuses see: [Payment Statuses](https://modulr.readme.io/docs/payment-statuses).

For a list of statuses when payments fail or are returned see: <https://modulr.readme.io/docs/payment-return-reasons>

Whilst the payment is being processed we will reserve the amount for a short period against your available balance to ensure availability of funds, this will be released once the payment is completed. Once the payment has been successfully processed it will generate the appropriate transactions and debit your source account.

You can view transactions posted against your account (debits and credits) using the GET transactions method [Get Transactions for a specific Account](https://modulr.readme.io/reference/gettransactionsbyaccount) .

## Making Outbound Payments

The following outlines how to make payments out of the platform, and within the platform, using the Modulr API.

The API [Create a Payment](https://modulr.readme.io/reference/sendpayment) supports various ways to send funds within and out of the Modulr service:

* To another Modulr account: type `ACCOUNT`
* To an external bank account using the accounts identifier, e.g.
  * A Sort Code and Account number for UK payments: type `SCAN`
  * An IBAN for European (SEPA) payments: type `IBAN`
* To an external bank account already added as a Beneficiary: type `BENEFICIARY`

In each case, you must specify the Modulr Account Id from which you wish the funds to be taken from.

The destination details needed will vary depending on the destination type.

### GBP Payments to UK Sort Code & Account Numbers

These payments will have their sort code & account number validated against the standard UK Modulus check as well as Pay.UK's Extended Industry Sort Code Directory to ensure payments can be successfully made.

For testing purposes, below are some examples:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Examples that will pass this check
      </th>

      <th>
        Examples that will fail this check
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        134020 / 63849203 118765 / 64371389 200915 / 41011166
      </td>

      <td>
        938063 / 15763217  
        118765 / 64371388  
        203099 / 66831036
      </td>
    </tr>
  </tbody>
</Table>

As an alternative, you can use our mock test sort code '000000' to make successful payments to any account number. Using this sort code also allows you to force payments into different status to test your integration further. To do so, please use one of the following as your payment refence when submitting a payment:

| Reference (Case Sensitive) | Payment Status                  |
| :------------------------- | :------------------------------ |
| EXTSYS                     | ER\_EXTSYS                      |
| TIMEOUTER                  | 15 Second Delay then ER\_EXTSYS |
| TIMEOUTOK                  | 15 Second Delay then PROCESSED  |
| TIMEOUTLONGER              | 60 Second Delay then ER\_EXTSYS |
| TIMEOUTLONGOK              | 60 Second Delay then PROCESSED  |
| INVALID                    | ER\_INVALID                     |

For a list of valid statuses see: [Payment Statuses](https://modulr.readme.io/docs/payment-statuses).

### Euro (SEPA) Payments to IBANs

Payments made to an IBAN are validated against the SWIFT IBAN Plus table. Checks are completed on the following aspects:

* Country Code
* Structure of the IBAN for that particular country (including length)
* Bank Code

For testing purposes, below are some examples:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Examples that will pass this check
      </th>

      <th>
        Examples that will fail this check
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        NL57RABO9712139840 BE71096123456769 GB29NWBK60161331926819 GB33BUKB20201555555555 FR0630003000409279659119K54
      </td>

      <td>
        NL57RABO9712139800  
        BE71096123456700  
        GB29NWBK60161331920000  
        GB33BUKB20201555555000  
        FR0630003000409279659119K00
      </td>
    </tr>
  </tbody>
</Table>

## Example Payment Request

```xml Example SEPA Payment
{
	"amount": 999.99,
	"currency": "EUR",
	"destination": {
	  "type": "IBAN",
		"iban": "IE52MODR99035500333832",
	  "name": "Beneficiary Name",
	},
	
	"sourceAccountId": "A1100ABCD1",
	"reference": "Example Reference"
}
```

## Additional Information

Please refrain from using profanities, in reference fields, when completing payments. Use of profanities will result in your payments being blocked

## CHAPS specific rules

A CHAPS payment will only be made on the Modulr platform when the payment value is above £1m AND the CHAPS service is enabled for an account OR if the payment value is more than £10K AND the destination account is not reachable via FPS. CHAPS payments must be made by 4pm GMT/BST, otherwise the payment is made the next bank business day in the CHAPS scheme.

From **1st May 2025** additional rules apply to usage of following parameters:

* **Legal Entity Identifier** – If making a CHAPS payment to a financial institution\*\* the LEI of the institution must be included
* **Payment Purpose Code** – A purpose code for the payment; this must be included in CHAPS property transactions. For all other payments unless a value is specified, default will be “EPAY” (e-payment)
* **Payment Category Code** – Optional category code for the payment. Unless a value is specified, default will be “OTHR” (other)

Refer to[ Purpose and Category Codes](https://modulr.readme.io/docs/uk-payment-purpose-category-codes) for a full list of supported codes

\*\* Defined as a payment to PRA authorised deposit-takers or broker-dealers, or Financial Market Infrastructures supervised by the Bank of England only; for clarity it does not mean an account of a client held at an institution, only a payment to the institution itself.

**Payment purpose codes for property transactions** When making a CHAPS payment (a payment over £1m) related to a property transaction one of the following purpose codes must be used.\
•	 **HLRP**- Property Loan Repayment\
•	 **HLST**- Property Loan Settlement\
•	 **PLDS**- Property Loan Disbursement\
•	 **PDEP**- Property Deposit\
•	 **PCOM**- Property Completion Payment\
•	 **PLRF**- Property Loan Refinancing