---
updatedAt: 2026-07-24T14:24:22.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Setting up Mandates

Before a Direct Debit collection is possible a mandate must be lodged on the Payer's bank account. This is called Direct Debit Instruction (DDI) and is used to authorise future collections against an account.

Direct Debit collections are protected by the [Direct Debit Guarantee](https://www.directdebit.co.uk/DirectDebitExplained/Pages/DirectDebitGuarantee.aspx).

## Mandate Process

Mandates are sent to the Payer's Bank when a Direct Debit is first setup, this shows the Paying Bank that the Service User has authority to withdraw funds from their account. In order to setup a mandate, You should call the [Create DD Mandate API](https://modulr.readme.io/reference/createmandate) and generate a unique Mandate ID for each mandate. If the Partner this before 3.30pm we will send the request the same day. If it is done after 3.30pm the request will be sent on the next working day.

It takes 4 working days to know if a mandate has been successful or unsuccessful.

<Image src="https://files.readme.io/5758594-DD_Mandate_Process.png" align="center" width="smart" />

## Timeline of events for Mandates

If the mandate is successful, the Partner will receive a [DDMandate Webhook](https://modulr.readme.io/docs/ddmandate-webhook) on Day 4 on 2:30PM to let them know that collections are possible and they can send out a collection request on the same day (must be before 3:30PM).

**Happy Path**

Day 1

1. Use our API to create a new mandate. If the mandate is created after 3:30PM it will be lodged the next day.
2. Modulr receives and verifies the request. If the information is correct, the status is changed to ‘Pending’.
3. Modulr processes the file and sends it to the scheme at 5:10 PM. The mandate status is set to ‘Submitted’.

Day 2

1. Scheme processing day.

Day 3

1. Payer's Bank links a Mandate on the Partner's customer's account.

Day 4

1. If Modulr does not receive a BRAUDDIS file then Modulr sets the status to "ACTIVE".
2. Modulr will send DDMandate webhook at 2:30PM to tell the Partner that the mandate is active.

![](https://files.readme.io/167769a-New_Mandate_and_Collection-New_Mandate_-_Happy_1.jpg "New Mandate and Collection-New Mandate - Happy (1).jpg")

**Unhappy Path**<br />The process is similar to the Happy Path until Day 3.

Day 3:

1. The paying bank receives the mandate request and rejects it.
2. The paying bank creates a BRAUDDIS (Bank Returned AUDDIS file) file and then sends it to the scheme.

Day 4:

1. Modulr receives the BRAUDDIS file and processes it. Mandate Status is "REJECTED".
2. Modulr sends the DDMandate Webhook at 10:15AM, 12:15PM, and 2:15PM

The BRAUDDIS contains the reason code for the failed mandate. Naturally, a failed mandate means that collections are not possible.

![](https://files.readme.io/23d4a11-New_Mandate_and_Collection-New_Mandate_-_Unhappy_1.jpg "New Mandate and Collection-New Mandate - Unhappy (1).jpg")

**Checking Mandate Status**<br />Partners can use the [Get Mandate API](https://modulr.readme.io/reference/getmandates) to get a list based on a search criteria such as accountID, creation date, or submission date.

## Mandate Statuses

* **Pending** - The Partner has created a mandate but has not yet been sent to BACS for processing.
* **Submitted** - A mandate has been sent to the BACS scheme.
* **Active** - Mandate successfully lodged against a Payer’s account.
* **Suspended** - The mandate is currently suspended, no collections can be made until reinstated.
* **Rejected** - A mandate has been rejected by the Payer’s Bank. Modulr receives a BRAUDDIS file and sends a DDMandate webhook which includes the reject reason.
* **Cancelled** - An existing mandate was cancelled by the Payer’s bank. Modulr receives an ADDACs file and sends a DDMandate webhook which includes the cancellation reason.

## APIs and Webhooks related to Mandates

![](https://files.readme.io/7e4cb89-DD_Mandate_Webhook_and_APIs.png "DD Mandate Webhook and APIs.png")

[**Create Mandate API**](https://modulr.readme.io/reference/createmandate)<br />[Get Mandates API](https://modulr.readme.io/reference/getmandates)<br />[Cancel Mandate API](https://modulr.readme.io/reference/cancelmandate)<br />[DDMandate Webhook](https://modulr.readme.io/docs/ddmandate-webhook)

## FAQs

<Callout icon="📘" theme="info">
  ### What name will appear on the bank statement of the payer?

  The client's name - which will also appear on the Direct Debit mandate that is set up.
</Callout>

<Callout icon="📘" theme="info">
  ### How "real-time" is the process, can the mandate be changed / cancelled at the last minute? If the customer wants to repay in full 1 day early and logs in to make the payment by debit card through the website, can the customer then cancel the direct debit collection that will otherwise remain scheduled for the next day?

  The mandate is the overarching contract and would only change if the details of the payer changed. For changing collection schedules, this can be done using the '[cancel collection schedule](https://modulr.readme.io/reference/cancelcollectionscheduleusingpost)' endpoint, but after a certain time this cannot be done. This boils down to a 1-3 working day period between the collection being submitted and actually taken from the bank account, during which it can't be reversed.
</Callout>

<Callout icon="📘" theme="info">
  ### If a customer cancels a direct debit mandate directly with their bank. Is the Partner notified by the Sending Bank in any way when they come to collect the payment?

  Yes, the Partner will be informed using the [DD Mandate webhook](https://modulr.readme.io/docs/ddmandate-webhook) after one working day when the customer has cancelled the Mandate from their account.
</Callout>

<Callout icon="📘" theme="info">
  ### Can our customers use online forms to submit mandates?

  Yes, in fact this is the way that is supported by us; the Partner would need to build the pages which would use our API to submit the mandate. These pages need to be approved by Modulr.
</Callout>

<br />