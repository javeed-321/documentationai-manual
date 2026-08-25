---
updatedAt: 2025-08-20T23:31:02.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Idempotent requests

## Introduction to idempotent requests

All requests that mutate or create data on the DriveWealth platform support an additional `Idempotency-Key` header to help in preventing duplicate submissions of requests. Should a network interruption occur, or you otherwise lost a response from a DriveWealth API, you can safely perform the request provided that you send the same value as the `Idempotency-Key`.

To perform an idempotent request, provide an additional **Idempotency-Key:** header to the request. All `POST` requests accept Idempotency keys. Using Idempotency keys in `GET` or `DELETE` requests should be avoided.

```curl
POST /back-office/orders HTTP/1.1
--header 'dw-client-app-key: ${appKey}'
--header 'Accept: application/json'
--header 'dw-auth-token: ${authKey}'
--header 'Idempotency-Key: 418a5506-256c-4c3c-9d4d-f491522cf7f2'
--header 'dw-request-timestamp: 2019-06-25T23:40:12.345Z'
--data `{
  "accountNo": "DWPH000003",
  "orderType": "MARKET",
  "symbol": "AMZN",
  "side": "BUY",
  "amountCash": 100,
}`
```

## Using DriveWealth Idempotency Keys

DriveWealth Idempotency Keys are saved for 4 days. Within this time period, sending any request with a duplicate key will return the exact same response as the original request, including the same status code and payload.

### **Best practices**

* Use randomly-generated **UUIDs** to prevent collisions.
* Keys must be at least **16 characters** in length.
* Use exponential backoff or a similar pattern of requests for retries.
* Use **dw-request-timestamp** as additional protection against technical failures.

### **dw-request-timestamp**

While idempotency keys will only be stored for 4 days, you may avail yourself of the **dw-request-timestamp** header to help avoid other technical failures that would resubmit old requests. For example, if you have a message-queue-based system for issuing requests to DriveWealth and are concerned about the possibility of repeating old requests, store the original timestamp in each message as this header. When DriveWealth sees this timestamp, it will reject the request if it is older than the 4-day idempotency limit.

Note that when requests are rejected for this reason, the original response contents will no longer have been preserved, and will not be sent back to you.

### **Retrying requests**

Idempotency allows you to create a network layer that automatically retries all DriveWealth requests when you fail to receive a response. Please keep in mind that requests should never be unconditionally retried, as failing to receive a response does not necessarily mean that DriveWealth is not receiving and responding.

Your network layer should have a maximum number of retries before it gives up and follows other failover procedures. More importantly, retrying multiple times immediately may be futile—if there is a network issue or connectivity issue, it may not be resolved within the maximum number of retries if these requests are issued in quick succession. We recommend an exponential backoff or similar pattern of requests, such as:

* (T) : Issue 1st request
* (T+1s): Retry 1
* (T+3s): Retry 2
* (T+10s): Retry 3
* (T+30s): Retry 4

### **dw-request-id**

The **dw-request-id** is a header value that is returned from the platform on any of the APIs available. It is very common to store or dump to a log file the dw-request-id to better assist our support teams with any issues that could arise.