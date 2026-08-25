---
updatedAt: 2025-09-05T18:56:07.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Receiving DD Collections

Once an account has been enabled to accept Direct Debit collections and has an active mandate, Merchants can start sending collection requests to Modulr and we will send those funds from the account.

Below is the high level flow for DD Outbound collections, it starts from Day 1 to Day 3, these are the flow for successful collections and the unsuccessful flow happens from Day 3 to Day 5.

![](https://files.readme.io/3eb956c-DD_Outbound_Collection_flow.PNG "DD Outbound Collection flow.PNG")

## Collection Process

**Day 1:**

1. Merchant sends the collection request to BACS.

**Day 2:**

1. BACS sends the collection request to Modulr at 22:30 and Modulr sends the Incoming Debit Notification Webhook to let the Partner know which collection has been received and which account will be debited.
2. Modulr checks if the collection is valid (please check the FAQs for the validations).

**Day 3:**

1. Partner informs Modulr if they want to reject collections by their customers.
2. If the collection is valid, then Modulr debits the Customer's account at 4:00 at first attempt. If the collection was successful then Modulr sends out a PayOut webhook to the Partner to let them know that the collection has been debited.
3. If the collection is valid and the 1st attempt fails, Modulr retries to debit the Customer's account at 15:00 for a second time. Same applies, if the collection was successful, the PayOut webhook is triggered to the Partner.

**Start of Unpaid Collections**

4. Modulr will treat collections that failed to debit or rejected debit as unpaid and change their status to Rejected. Modulr allows Partners to reject payment using the [Reject Collection](https://modulr.readme.io/reference/rejectcollection).\
   5\. Modulr debits the unpaid collections from the Partner's Account.\
   6\. Modulr generates [ARUDDs](https://www.bacs.co.uk/resources/reason-codes/) to return the unpaid collection funds and sends it to BACS.

Collections can be rejected by partners at any point during the cycle until 5pm on Day 3 by calling the "Reject Collection" endpoint. Even if the payer account was already debited, by calling the reject endpoint, Modulr will immediately return the funds back to the account if requested before the cut-off time. Modulr also allows partners to skip debit attempts if needed via this endpoint. All refund requests made by the customer or the partner after 5pm, will have to be requested through the Direct Debit Indemnity Claim Service (DDIC).

The SKIP\_DEBIT\_ATTEMPT reason code is utilised by Partners to request Modulr to alter the debit order in cases in which there are 2 or more collections to be processed against the same account on the same day. Processing order of collections is first arrived first processed. Partners will be able to find the order of processing by ordering the ClaimId field in Incoming Collection Notification.

**Day 5 (for Returned Collections):**

1. Modulr receives the returned funds from the merchant's bank and Modulr sends the funds to the Partner's account.

![](https://files.readme.io/b2a4ca0-image.png)

## API and Webhooks

Utilise the following APIs to manage Direct Debits\
**[Reject](https://modulr.readme.io/reference/rejectcollection)**– reject a Direct Debit collection or confirm that the next debit attempt should be skipped.

The collection processing notifications are sent using the existing Notification Service

* **[Webhook - Direct Debit, Incoming Collection](https://modulr.readme.io/docs/webhook-direct-debit-incoming-collection)** Notification informs Partner that debit will be attempted.
* **[Webhook - Direct Debit, Unpaid Collection](https://modulr.readme.io/docs/webhook-direct-debit-unpaid-collection)** Notification informs Partner that their nominated account will be debited.
* **[Webhook - Direct Debit, Return Funds](https://modulr.readme.io/docs/webhook-direct-debit-return-funds)** Notification informs Partner that funds associated with unpaid collections have be credited.
* **[Webhook - Outbound Payments](https://modulr.readme.io/docs/payout-webhook)** and **[Webhook - Inbound Payments](https://modulr.readme.io/docs/payin-webhook)** notify when an account is debited or credited – these notifications apply to all payment types.

![](https://files.readme.io/8bd388b-Capture.PNG "Capture.PNG")

## FAQs

> 📘 Do you validate incoming both Mandates and Collections?
>
> Yes we do. We check if the account exist, the account is active, account is enabled to accept Direct Debits, and received mandate or collection belong to a Direct Debit Partner.

> 📘 Validations for Mandates only
>
> We match if the incoming mandate is unique for the same payer and merchant.

> 📘 Validations for Collection only
>
> We check if the account has an active mandate lodged.