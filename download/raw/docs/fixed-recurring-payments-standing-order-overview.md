---
updatedAt: 2025-09-05T18:35:44.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Fixed Recurring Payments (Standing Orders)

This page will provide an overview for standing order payment initiations. It includes:

* Listing the banks that support standing order initiation.
* Requesting a new standing order.
* Redirecting the end-user to their bank to authenticate and approve the set-up of the standing order.
* Returning the end-user back to your site or application.
* Retrieving the status of the standing order initiation.
* High level end-to-end flow for standing order initiations.
* Standing order payment initiation lifecycle.
* Complete API specifications.
* Known limitations.

## Step 1: Listing the banks that support standing order initiation

You should use the [GET ASPSPs API](https://modulr.readme.io/reference/getaspsproviders) to fetch the latest list of banks and their supported capabilities (such as Single Immediate Payments and Standing Order).

You should only show banks which support Standing Order and which are Enabled.

Your end-users will need to select their bank so that they can be directed to the relevant authentication URL.

Note - This endpoint should be queried every time you request a standing order initiation, as banks may be temporarily marked as DISABLED if they are currently unavailable.

## Step 2: Requesting a new standing order

> 📘 Note:
>
> Standing orders can be set-up to recur on a monthly or a weekly basis and must have a start date at least three business days in the future.
>
> A standing order can only be cancelled or amended by the payer.
>
> Whilst most banks will process standing orders on a working day, some will mandate that a standing order request be submitted with a start date falling on a working day, otherwise the request will be rejected. Please reference [this table](https://modulr.readme.io/docs/fixed-recurring-payments-standing-order-overview#working-day-limitations-for-standing-orders) for specific restrictions that must be considered when building your integration.

To initiate a standing order request we require:-

* Payer Bank Identifier
* Details of the receiving account
* Start Date
* Frequency
* End Date (optional)
* Payment Amount (GBP)
* Payment Reference - To enable easier reconciliation for you when funds are received in your Modulr account this should be a unique for reference meaningful to your system. The payment reference has a limit of 18 alphanumeric characters

More details for these fields can be found [here](https://modulr.readme.io/reference/initiatestandingorder).

Please consult the Modulr Implementation guide that shows the required information that MUST be displayed to the end-user before initiating any PISP journey.

For a summary of the banks that limit start and end dates of standing orders to working days, please see [this table below](https://modulr.readme.io/docs/fixed-recurring-payments-standing-order-overview#working-day-limitations-for-standing-orders).

Once you have gathered this information, you should use the POST /standing-order-initiations API to request a new standing order.

## Step 3: Redirect the end-user to their bank to authenticate and confirm the set-up of the standing order.

Modulr’s response to the API call in Step 2 will return a unique standing order initiation ID and a unique redirect URL to the end-user’s bank’s authentication portal.

You should immediately redirect the end-user to this URL so that they can authorise the set-up of the standing order.

Notes on this redirect URL:

* The redirect URL will be valid for 5 minutes. After this, if the end-user hasn’t continued with the standing order initiation, we will expire the standing order initiation request. If, after this, you were to retrieve the status of the standing order initiation, it would now have a status of ER\_EXPIRED.
* Whilst the redirect URL does not contain any sensitive information that could be used maliciously in isolation, it does contain data that might facilitate malicious use when paired with information gained elsewhere. It is not intended to be used in other ways, such as being pasted into emails where it can be easily inspected.
* If the end-user is using a mobile device which has the bank’s mobile app installed, the redirect URL may open in the app. This would generally be the desired experience. If the bank’s mobile app is not installed or not correctly setup to open the URL, it will open in a web browser page.

The end-user will have to follow the bank’s process to authenticate and approve the standing order. The process tends to be quite similar for each bank but does vary slightly.

Once the end-user has completed this process, Modulr will finalise the standing order initiation and will then redirect the end-user to the redirect URL that you provided during your onboarding process. The next section explains this part of the process in more detail.

## Step 4: Returning the end-user back to your site or application

As noted in Step 3, once the end-user has approved the standing order, Modulr will redirect them to the redirect URL that you provided during your onboarding process. This URL will contain the standing order initiation identifier and will also contain a parameter to indicate success or failure of the standing order initiation. The purpose of this indication is so that you can display an appropriate message to the end user but you **must not** rely on this as a definitive status, as it could have been tampered with by a malicious user or third party.

## Step 5: Retrieving the status of the standing order initation

To retrieve details of the standing order initiation including a definitive status, you should use the [GET /standing-order-initiations/\{standingOrderInitiationId} API](https://modulr.readme.io/reference/getstandingorderinitiation).

These details include the standing order status as received from the bank (aspspPaymentStatus). The response object will contain the Standing Order status as received from the bank. You should check this as very occasionally, the end-user’s bank may fail to set-up the standing order even after the initiation has been approved.

See the *Standing Order Payment Initiation Lifecycle* section for details of the standing order initiation statuses.

## High level end-to-end flow for Standing Order Initiations

The diagram detailed below shows an overview of the standing order initiation flow.

![](https://files.readme.io/51a7ac3-0a0c2620-740c-4f5f-b06f-498922734d95.png "0a0c2620-740c-4f5f-b06f-498922734d95.png")

## Payment Initiation Status Life Cycle

Each payment initiation request moves through the statuses as detailed below:

![](https://files.readme.io/c2c6224-StateDiagram2.png "StateDiagram2.png")

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Status
      </th>

      <th>
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        AWAITING\_CONSENT
      </td>

      <td>
        Waiting for the end-user to approve the payment initiation at their bank. If not approved/rejected within a certain timeframe, the payment initiation will move to ER\_EXPIRED. Otherwise it will move to EXECUTED or any of the other error statuses.
      </td>
    </tr>

    <tr>
      <td>
        CONSENT\_REJECTED
      </td>

      <td>
        The end-user or bank has rejected the payment initiation.
      </td>
    </tr>

    <tr>
      <td>
        EXECUTED
      </td>

      <td>
        The payment initiation has been accepted by the bank and it is with them to execute.  

        Note that the bank may still on rare occasions have problems fulfilling the payment and fail at the time of execution. You should not assume that the payment has been successful until you check the status of field aspspPaymentStatus.  

        Alternatively you can check if funds have been received into the destination account.
      </td>
    </tr>

    <tr>
      <td>
        ER\_EXTSYS
      </td>

      <td>
        The payment initiation failed because there was a problem communicating with the bank’s systems.
      </td>
    </tr>

    <tr>
      <td>
        ER\_EXPIRED
      </td>

      <td>
        The end-user did not approve or reject the payment initiation within a certain timeframe, for example, by not even logging into their banking app.
      </td>
    </tr>

    <tr>
      <td>
        ER\_GENERAL
      </td>

      <td>
        Generic error occurred when processing the payment initiation.
      </td>
    </tr>
  </tbody>
</Table>

## Additional Standing Order Status (standingOrderStatus)

In addition to the status field on a standing order payment initiation, the standingOrderStatus field gives additional detail as received from the payer’s bank

![](https://files.readme.io/b5b4740-Stading_order_Status.jfif "Stading order Status.jfif")

| Status              | Payment Status Description                                                                                 |
| :------------------ | :--------------------------------------------------------------------------------------------------------- |
| InitiationCompleted | A standing order request has been created at the bank and the initiation of the payment order is complete. |
| InitiationFailed    | A standing order request has been created at the bank and the initiation of the payment order has failed.  |
| InitiationPending   | A standing order request has been created at the bank and the initiation of the payment order is pending.  |

## Working Day Limitations for Standing Orders

Whilst most banks will process standing orders on a working day, some will mandate that a standing order request be submitted with a start date falling on a working day, otherwise the request will be rejected. The following banks have specific restrictions that must be considered when building your integration.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Bank
      </th>

      <th>
        Weekly Frequency
      </th>

      <th>
        Monthly Frequency
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Bank of Ireland
        Revolut
      </td>

      <td>
        Does not support end date
      </td>

      <td>
        Does not support end date
      </td>
    </tr>

    <tr>
      <td>
        Bank of Scotland\
        Halifax\
        Lloyds
      </td>

      <td>
        Must commence on a working day
      </td>

      <td>
        If specifying an end date, must match the starting date.  

        E.g. if starting on the 2nd of the month, the end date must also be the 2nd of the month.
      </td>
    </tr>

    <tr>
      <td>
        Barclays\
        Danske Bank
      </td>

      <td>
        Must commence on a working day
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        first direct\
        HSBC\
        NatWest\
        Royal Bank of Scotland
      </td>

      <td>
        Must commence on a working day
      </td>

      <td>
        Must commence on a working day
      </td>
    </tr>

    <tr>
      <td>
        Santander
      </td>

      <td>
        Must commence on a working day\
        Does not support end date
      </td>

      <td>
        Does not support end date
      </td>
    </tr>
  </tbody>
</Table>