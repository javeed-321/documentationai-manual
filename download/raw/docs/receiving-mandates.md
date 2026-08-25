---
updatedAt: 2025-09-05T18:56:06.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Receiving Mandates

To get started, you may need to reach out to Modulr's implementation team to enable your accounts to accept direct debit. Once that has been enabled, merchants such as your local gym, energy, internet or insurance provider can set up direct debit mandates and start making collections from yours or your customers’ accounts.

The merchant needs to create a mandate on the end customer's account before any collections can be done.

1. The merchant will send a request to BACS instructing them to lodge a mandate against one of your Modulr accounts.
2. Modulr will receive the [AUDDIS (Automated Direct Debit Instruction Service)](https://www.bacs.co.uk/services/bacs-schemes/direct-debit/services/auddis/) file from BACS, validate the details and check that the account we’ve received the instructions for is enabled for Direct Debit and exists on our end.
3. If Modulr accepts the AUDDIS the mandate is then lodged and the merchant can start collecting from this account.

A mandate can be rejected for various reasons, more commonly is when the account is not enabled to accept direct debits.\
4\. If Modulr rejects the AUDDIS then it generates a BRAUDDIS (Bank Returned) file to the merchant and no Mandate is lodge.

You can view all existing mandates linked to a specific account id by using the [Enquire Mandate API](https://modulr.readme.io/reference/retrievemandates)

![1242](https://files.readme.io/fe91f02-DD_Outbound_flows-DD_Outbound_General_Mandate_flow.jpg "DD Outbound flows-DD Outbound General Mandate flow.jpg")

## APIs and Webhooks

Utilise the following APIs to manage Direct Debit Mandates

* **[Enquire](https://modulr.readme.io/reference/retrievemandates)** - get a list of direct debit mandates associated with an account.
* **[Cancellation](https://modulr.readme.io/reference/cancelddosmandate)** - cancel a specified mandate.

Available webhook notifications for you to subscribe to:

* **[Direct Debit Mandate Status](https://modulr.readme.io/docs/ddmandate-webhook)** - sends an alert when there has been a change in a Direct Debit Mandate’s status (e.g. Created, Cancelled, Expired)

![1102](https://files.readme.io/7e2038a-API_and_Webhooks.PNG "API and Webhooks.PNG")

## Cancelling Mandates

Your can cancel a Direct Debit mandate at any time. They can do so using our APIs [Cancel a specific Mandate](https://modulr.readme.io/reference/cancelddosmandate) and notice will be **effective immediately**.

Where notice is given by the payer to their bank or PSP (Payment Service Provider), in this instance Modulr, must progress the instruction and notify the service user (via [ADDACS (Automated Direct Debit Amendment and Cancellation Service)](https://www.bacs.co.uk/services/bacs-schemes/direct-debit/services/addacs/)and/or [ARUDD (Automated Return of Unpaid Direct Debits Service)](https://www.bacs.co.uk/services/bacs-schemes/direct-debit/services/) within 3 working days. Whether received via ADDACS or directly from the payer, the PSP (Payment Service Provider) or service users must action an instruction to amend or cancel a Direct Debit Mandate within 3 working days.

Where PSP or service users receive notification via ADDACS, this will be taken as the authority to proceed (in accordance with the advice).

Where there are outstanding funds due, the service user can still use Direct Debit as a collection method with the payer’s permission.

![1242](https://files.readme.io/f915921-DD_Outbound_flows-Page-3.jpg "DD Outbound flows-Page-3.jpg")

## FAQs

> 📘 Direct Debit Guarantee
>
> Checks are performed on companies registering as a Direct Debit service user (a.k.a. the collecting party) by their sponsor. This is the first protection against abuse in the Direct Debit process.
>
> Additionally, if a payer challenges a collection by raising an indemnity claim they will be protected by the Direct Debit guarantee.