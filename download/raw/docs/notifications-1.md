---
updatedAt: 2026-03-13T16:05:50.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Notifications (Webhooks & Emails)

Notifications enable your platform to find out about events as they happen.

We currently provide over two notification channels, webhooks and emails.

* Webhook: If you send a request for a notification that is a webhook, then the notifications will be as webhooks and you will need to build a listener
* Email: This will create a notification that will be sent to the email addresses listed. Emails do not need a listener or event handler, as the alert will be sent to all email addresses specified. It is best practice to use group email addresses, as they can be changed when people need to be removed or added without needing to edit the notification itself (Learn more about emails here: [Email Notifications](https://knowledge.modulrfinance.com/knowledge-hub/using-the-modulr-portal#email-notifications))

These are setup at a customer level and apply to all accounts

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Notification Type
      </th>

      <th>
        Description
      </th>

      <th>
        Channel Availability
      </th>

      <th>
        Subscription Level
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Account Statement
      </td>

      <td>
        A notification to alert you that new statements are available for your accounts. This is typically received in the first few days of a new month.
      </td>

      <td>
        Email
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Balance High
      </td>

      <td>
        When one of your Accounts has a balance that goes over a specified amount you are alerted
      </td>

      <td>
        Email
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Balance Low
      </td>

      <td>
        When one of your accounts has a balance that goes below a specified amount you are alerted
      </td>

      <td>
        Email
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Pending Payments
      </td>

      <td>
        When any of your accounts have payments pending to be sent due to needing approval, waiting for funds or waiting for a set date to be sent this email gives a summary of those payments that are pending to be sent.
      </td>

      <td>
        Email
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Scheduled Balance
      </td>

      <td>
        A periodic notification of the balance of your Accounts sent at a specified day and time
      </td>

      <td>
        Email
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Card Authorisation - [CARDAUTH](https://modulr.readme.io/docs/card-notifications#cardauth)
      </td>

      <td>
        A notification to alert you that there has been a new or updated card authorisation
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Card Creation - [CARDCREATION](https://modulr.readme.io/docs/card-notifications#cardcreation)
      </td>

      <td>
        A notification to alert you of the status of a create physical card request, this is only available for Physical cards and not virtual cards.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Customer Verification Status - [CUSTVSTAT](https://modulr.readme.io/docs/custvstat-webhook)
      </td>

      <td>
        As a partner on the Modulr Platform if Modulr handle your KYC/KYB process this webhook will be sent to notify you when there are changes to a customer in this process
      </td>

      <td>
        Webhook
      </td>

      <td>
        Partner
      </td>
    </tr>

    <tr>
      <td>
        Customer Status - <Anchor label="CUSTOMER_STATUS" target="_blank" href="https://modulr.readme.io/update/docs/customer-status">CUSTOMER_STATUS</Anchor>
      </td>

      <td>
        For Partners, to be notified that a Customer is fully Approved as part of the KYC/KYB process.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Partner
      </td>
    </tr>

    <tr>
      <td>
        Direct Debit Mandate Status - [DDMANDATE](https://modulr.readme.io/docs/ddmandate-webhook)
      </td>

      <td>
        A notification to alert you of any changes to the status of a Direct Debit Mandate.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Direct Debit Failed Claim - DD_FAILED_CLAIM
      </td>

      <td>
        A notification to alert you that a DD claim has failed. Sent at around 5pm on the day the collection is due.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Direct Debit Funds Returned - DD_FUNDS_RETURNED
      </td>

      <td>
        A notification to alert partners that the funds associated with a failed DD have been returned by the scheme and credited in their nominated account.

        Returned funds notification is one per nominated account and not per collection.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Direct Debit Incoming Debit - DD_INCOMING_DEBIT
      </td>

      <td>
        A notification to alert partners that a collection has been received, accepted, and a debit of the client account will be attempted in the pre-defined time period.

        We send 1 webhook per collection.
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Inbound Payment - [PAYIN](https://modulr.readme.io/docs/payin-webhook)
      </td>

      <td>
        When one of your accounts is successfully funded you are alerted
      </td>

      <td>
        Email, Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Outbound Payment - [PAYOUT](https://modulr.readme.io/docs/payout-webhook)
      </td>

      <td>
        When one of your Accounts has a successful payment out of it you are alerted
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Payment Approval Status Change - [PAYMENTAPPROVALSTATUSCHANGE](https://modulr.readme.io/docs/payment-approval-rejection-webhook)
      </td>

      <td>
        When a Payment that is awaiting user approval is approved - usually via the Modulr Customer Portal
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Batch Payment Approval Status Change - [BATCHPAYMENTAPPROVALSTATUSCHANGE](https://modulr.readme.io/docs/notifications-1)
      </td>

      <td>
        When a Batch of Payments that is awaiting user approval is approved - usually via the Modulr Customer Portal
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Card Refund - [PAYIN](https://modulr.readme.io/docs/payin-webhook)
      </td>

      <td>
        When there's a new refund in a card that's associated with one of your accounts
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Card Settlement - [PAYOUT](https://modulr.readme.io/docs/payout-webhook)
      </td>

      <td>
        When there's a new settlement in a card that's associated with one of your accounts
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Outbound Reversed Payment -  
        PO_REV -  [PAYIN](https://modulr.readme.io/docs/payin-webhook)
      </td>

      <td>
        A notification to alert that the funds associated with a reversed payment have been returned as a separate operation
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Upcoming BACs Credit - UPCOMING_CREDIT
      </td>

      <td>
        A notification to alert you that there will be a BACs credit applied to the account. This is triggered on Day 2 of the BACs process prior to the actual credit on the account happening on Day 3
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>

    <tr>
      <td>
        Account status change - ACCOUNT_STATUS_CHANGE
      </td>

      <td>
        Notification of change for when an account changes status, e.g. BLOCKED to ACTIVE
      </td>

      <td>
        Webhook
      </td>

      <td>
        Customer
      </td>
    </tr>
  </tbody>
</Table>

Please see the [API Reference section](https://modulr.readme.io/reference/getallcustomernotifications) for more details on how to set up the notifications

So as an example you've decided that it would be really useful for your system to be alerted when you get any funds paid in to your accounts, now what do you do?

## Webhooks - An Introduction

A Webhook, in simple terms, is a user-defined HTTP callback. It is a mechanism for the system to notify you about an event. How does it notify you? By doing an HTTP POST to the Webhook (i.e. the Web URL that you define). In terms of implementation, you can write an API endpoint that is capable of receiving an HTTP POST in an application stack of your choice. Remember in live this must be reliable and resilient if you are to depend on it for information.

The advantage of a Webhook is that there is no persistent open connection to the system where you keep filtering for events that you are interested in. It is an asynchronous mechanism where you will wait for the system to notify you. The HTTP POST payload will contain the details of the event.

## Webhook security

We sign the POST request with an HMAC digest, using a secret that you provide. This can be set when registering the endpoint for the webhook type of notification. ***It is required that you validate this signature, particularly if you are acting upon these events to authorise actions in your system***. The method of calculation of the hmac signature is the same as in [HMAC Signatures / Authorisation header calculation](https://modulr.readme.io/docs/authentication)\
*For webhook requests that are sent from us to you, we use the webhook id as the key and the secret you have provided when creating the webhook to sign the webhook.*

## Setting up a webhook

### Listen and Receive

Firstly, you need to set up the ability for your system to do something and make sure you have a URL ready to listen for any alerts. In a test example here you could post an alert from Modulr in to <a href="https://requestbin.com/" target="_blank">RequestBin</a> but obviously this would be your system listening when you build your endpoint.

In our example for notifications of payments in, once you create an endpoint url, you need to set this webhook up in Modulr for your customer id using [Set up a Notification for a Customer](https://modulr.readme.io/reference/addcustomernotification), using channel WEBHOOK and type PAYIN\
You should now be all set with the Incoming Webhook configured and waiting for Modulr to message it when receiving a payment in.

To test this you can trigger a dummy sandbox payment in using [Pay into an account](https://modulr.readme.io/reference/createpayments)  and then view your RequestBin for the webhook

### Responding to Modulr Webhooks

When built in to your system to acknowledge receipt of a webhook, your endpoint should return a 2XX HTTP status code. Any other information you return in the request headers or request body will be ignored.

If we do not receive a 2XX response to our POST request, we will retry the request with exponential back off, to a maximum of 5 retries.

| Retry     | Time after first failure |
| :-------- | :----------------------- |
| 1st Retry | 1 Minute                 |
| 2nd Retry | 5 Minutes                |
| 3rd Retry | 25 minutes               |
| 4th Retry | 2 hours 5 minutes        |
| 5th Retry | 10 hours 25 minutes      |

After 5 tries we will not process the event further. Therefore you should not rely on webhooks as the sole means for reconciliation of the completeness of financial events into your system, particularly if you are aware of any recent issues you may have had with your webhook listener reliability.

### Webhook duplicate checks

As mentioned above we have the ability to retry webhooks up to a maximum of 5 times automatically. This highlights the importance of ensuring you are handling webhooks correctly and checking that each webhook is unique to your system to prevent any undesired behaviours like processing a webhook twice for the same event.

For example we recommend in regards to the PAYIN or PAYOUT webhook to utilise PaymentId as your main duplicate check, as there are times where the EventId could change or in the event of a failed payment the TransactionId would be empty.

Depending on the Payment scheme the PaymentId could following different patterns but will always represent a unique indentifier.

### Webhook parsing

We recommend all of our clients when implementing handling of webhooks to utilise a lenient json parser. This is to ensure as we add new functionality and richer information to our webhooks that your system does not start to fail the processing of the webhooks.

### No longer need your notification?

So, you no longer want to get notified when money goes into your accounts? The easiest way to do this is to inactivate the webhook channel alert. You will need to know the ID \{id} of the webhook that was given to you in the response when creating the notification and use the PUT endpoint to change the status from ACTIVE to INACTIVE. You will also need to know the customer id \{cid}.

If you change you mind you can always re-activate the webhook using the same endpoint. You'll need to change the status back to ACTIVE and make sure the 'destinations' parameter is set to the URL you have set up to listen out for an alert.

#### Payment type definitions

Payment types information can be found [here](https://modulr.readme.io/docs/payment-types)