---
updatedAt: 2025-09-05T18:35:09.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Error handling and duplicate prevention

The vast majority of API requests are processed without any issues, but unfortunately a small number may error due to various reasons, from bad data to internet connectivity. It is important that error handling is efficient to prevent manual effort, but also to ensure that in retrying API requests - particularly payments - duplicates are not processed.

Modulr offers ways within API requests to detect and prevent duplicate requests, but it is key that these are used appropriately (depending on the error conditions). The guide below should assist you in understanding the error scenarios and recommended actions.

This guidance is particularly applicable to operations or endpoints that create new objects / requests (POST requests). Please review how to make idempotent requests in the Modulr API documentation [here](https://modulr.readme.io/docs/limits-and-errors#section-idempotent-requests)  before reading this guide as it uses some of these concepts.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Is experienced as
      </th>

      <th style={{ textAlign: "left" }}>
        Recommendation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        Network, connectivity or system processing errors
      </td>

      <td style={{ textAlign: "left" }}>
        * a timeout or connectivity error (no response received from Modulr), OR
        * a 5XX type error
      </td>

      <td style={{ textAlign: "left" }}>
        * Wait for a while (e.g. a few minutes) to allow issues to resolve and then retry
        * Use SAME nonce as this will prevent duplicates
        * Set x-mod-retry=true
        * If Modulr have not seen this nonce before, Modulr will process the request as a new request. If Modulr has seen the nonce before and completed the request, Modulr will return the original response
        * If you still get a similar error try again after waiting a longer period, suggest up to max 3 retries (see note 1)
        * If still failing after a few retries, stop and contact Modulr support to investigate issue and resolution. Once the cause of the error is understood and resolved offline, and only if the payment has not been processed already, you will need to resend as a new request with a new nonce
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        2
      </td>

      <td style={{ textAlign: "left" }}>
        Forbidden.

        The request was valid, but the [server](https://cybernews.com/resources/web-hosting-glossary/#server) is refusing action. Generally this relates to permission /access issues, but could also occur if nonce is re-used and modulr are not able to return the original response (because it is still processing the original request, or x-mod-retry is not set to true)
      </td>

      <td style={{ textAlign: "left" }}>
        403 error
      </td>

      <td style={{ textAlign: "left" }}>
        * It would be safe to retry with SAME nonce and x-mod-retry=true after a wait (suggest about 5 minutes in case this is a temporary issue to allow it to resolve), but you could get the same error, so only retry a limited number of times (see note 1), suggest up to max 3 retries.
        * Alternatively stop and contact Modulr support to understand the reason
        * Once the cause of the error is understood and resolved offline, and only if the payment has not been processed already, you will need to resend as a new request with a new nonce
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        3
      </td>

      <td style={{ textAlign: "left" }}>
        Bad request, bad data in request\
        The server cannot or will not process the request due to an apparent client error.\
        Example: account does not have enough balance, account number basic checks fail, badly formatted data, key HMAC signature calculation errors
      </td>

      <td style={{ textAlign: "left" }}>
        400 error
      </td>

      <td style={{ textAlign: "left" }}>
        * There is an issue with the request so it requires action first to correct (example bad destination account, no balance etc.)
        * There is no point re-sending the request as is as you will get the same error, the cause first needs to be corrected
        * Stop and correct the cause of the error (business operation), once the cause of the error is understood and resolved offline, you will need to resend as a new request with a new nonce
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        Rate limit or Quota errors

        In order to protect all system clients from the actions of a single client limits are placed on how many requests can be made in a short period (rate limit) and over a longer period (quota)

        You should not experience these errors in the course of normal operations for the vast majority of clients. If you do please look into the volume/pattern of requests you are making and check for any issues. Note: Limits and quotas work across all your requests
      </td>

      <td style={{ textAlign: "left" }}>
        429 error "Rate limit exceeded"

        403 error "Quota exceeded"
      </td>

      <td style={{ textAlign: "left" }}>
        * If you experience the 429 error you can wait a while and retry. It would be safe to retry with SAME nonce and x-mod-retry=true after a wait (in case this is a temporary issue), but you could get the same error, so only retry a limited number of times (see note 1), suggest up to max 3 retries.
        * 403 quota limits can also be treated like any other 403 error (see above issue type 2), but until the quota is renewed you are likely to get the same error
        * If you continue to experience issues please discuss with Modulr who can provide advice
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        *Applicable to payment requests*

        Payment request is accepted/validated when you submit, you get a payment id from Modulr, but payment subsequently errors.\
        This can be due to further error checking in the payments chain, e.g. the sort code is not reachable, account is closed
      </td>

      <td style={{ textAlign: "left" }}>
        2XX successful response on initial submission and initial status of VALIDATED, but on checking payment status later it is an error condition\
        Payment status may be checked by doing a GET (after a wait period), subscribing to webhooks to your system, or checking for errors regularly in the web portal.
      </td>

      <td style={{ textAlign: "left" }}>
        * Depending on the error reason make any correction needed offline (e.g. establish the correct bank account details)
        * The error should have some additional detail as to the reason for the error
        * Stop and correct the cause of the error (business operation), once the cause of the error is understood and resolved offline, you will need to resend as a new request with a new nonce
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        6
      </td>

      <td style={{ textAlign: "left" }}>
        *Applicable to payment requests*

        Outbound payment fully succeeds (PROCESSED status) but is subsequently later returned as a new inbound payment by the receiving bank.\
        Unfortunately with some destinations the receiving bank may accept the payment but subsequently reject and return it
      </td>

      <td style={{ textAlign: "left" }}>
        An unexpected credit on your account. As much detail will be provided as we get to allow you to match it to an outbound payment
      </td>

      <td style={{ textAlign: "left" }}>
        * Monitor your account for credits and reconcile transactions
        * Identify any returned payments and action needed. If you wish to resend will need to be resent as a new payment request
      </td>
    </tr>
  </tbody>
</Table>

### General recommendations

* On error default to either not re-sending a payment request, or re-sending a fixed number of times with the same nonce and x-mod-retry=true
* <sup>1</sup>Retry attempts should use some form of expanding backoff to prevent overloading of requests in cases where multiple requests have failed and are retried
* Only resend as a new payment with a new nonce if you understand the specific error condition and are therefore confident the payment has not succeeded
* If you re-use a nonce you should not change any other contents of a request (i.e. it should be a resend of the same data)
* Idem-potency checking on nonce is valid for 48 hours from the initial submission of a unique nonce. Beyond this time do not retry any requests even using the same nonce unless you are sure it has not succeeded before
* If you also set an "externalReference" field in the body of a request (recommended), you should use a corresponding unique operation/object in your system to allow matching and reconciliation to your system