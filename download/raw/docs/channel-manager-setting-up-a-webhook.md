---
updatedAt: 2025-11-05T10:44:30.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager - Setting Up A Webhook 

## Listen and Receive

Firstly, you need to set up the ability for your system to do something and make sure you have a URL ready to listen for any alerts.

Once this has been set up you will need to subscribe to the desired webhook using [Subscribe to a webhook](https://modulr.readme.io/reference/channelmanagercreatewebhooknotification#/) endpoint.

You will need to supply the following:
•	type : webhook type
•	destination : URL destination
•	retry : Flag indicating whether failed webhooks should be retried
•	secret : Mandatory for webhook. Secret that is used in HMAC calculation, for webhooks
•	hmacAlgorithm : Signing algorithm that is used in Webhook HMAC calculation

You should now be all set with the Incoming Webhook configured and waiting for Modulr to message it when receiving the desired webhook.

<br />

## Responding to Modulr Webhooks

When built into your system to acknowledge receipt of a webhook, your endpoint should return a 2XX HTTP status code. Any other information you return in the request headers or request body will be ignored.

If we do not receive a 2XX response to our POST request, we will retry the request with exponential back off, to a maximum of 5 retries.

<br />

| Retry | Time after first failure |
| :---- | :----------------------- |
| 1st   | 1 Minute                 |
| 2nd   | 5 Minutes                |
| 3rd   | 25 minutes               |
| 4th   | 2 hours 5 minutes        |
| 5th   | 10 hours 25 minutes      |

After 5 tries we will not process the event further.

If you wanted to get a list of failures you can call [Webhook Failures](https://modulr.readme.io/reference/channelmanagergetwebhooknotifications_1#/) endpoint which will return all the failures for a specific notification.

<br />

## Webhook Duplicate Checks

As mentioned above we have the ability to retry webhooks up to a maximum of 5 times automatically. This highlights the importance of ensuring you are handling webhooks correctly and checking that each webhook is unique to your system to prevent any undesired behaviours like processing a webhook twice for the same event.

For example we recommend in regards to the PAYIN or PAYOUT webhook to utilise PaymentId as your main duplicate check, as there are times where the EventId could change or in the event of a failed payment the TransactionId would be empty.

Depending on the Payment scheme the PaymentId could following different patterns but will always represent a unique identifier.

<br />

## Webhook Parsing

We recommend all of our clients when implementing handling of webhooks to utilise a lenient json parser.

This is to ensure as we add new functionality and richer information to our webhooks that your system does not start to fail the processing of the webhooks.

<br />

## No longer need your notification?

So, you no longer want to get notified? The easiest way to do this is to inactivate the webhook channel alert.

You will need to know the ID of the webhook that was given to you in the response when creating the notification and use [Update a Webhook](https://modulr.readme.io/reference/channelmanagerupdatewebhooknotification#/) endpoint to change the status from ACTIVE to INACTIVE.

If you change your mind you can always re-activate the webhook using the same endpoint. You'll need to change the status back to ACTIVE and make sure the 'destinations' parameter is set to the URL you have set up to listen out for an alert.

<br />

## Retrieving Configurations

If you wanted to see all the webhook configurations you can use the [Retrieve All Notifications](https://modulr.readme.io/reference/channelmanagergetwebhooknotifications#/) endpoint to get this information, equally if theres a specific configuration you want to check then use [Retrieve Specific Notification](https://modulr.readme.io/reference/channelmanagergetwebhooknotification#/) endpoint.

<br />

<br />