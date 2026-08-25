Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Your Modulr Product Update May 2026

<br />

<Image align="center" width="600px" src="https://files.readme.io/c806c32a1e1f8d958d6b133f07bf730184c7487ac2607f302edb83b882f59c4b-image.png" />

<br />

<Image align="center" width="600px" src="https://files.readme.io/6180500c9af673242159c47d94224b4f78c269a5bfc35eb1589999a63c4118fd-image.png" />

<br />

# API

## Payment File Upload | new status values in file upload API

We are making changes to the file upload processing flow for the Payment File Upload service. As part of this update, the `GET /payment-file-upload-service/payment-files/{fileId}` endpoint will return two new status values that you may observe when polling for file status.

## What's changing

**PROCESSING**- your file has been picked up and is actively being validated. This is not a terminal state; you should continue polling until a final status is returned.

**ERROR\_RETRYABLE**- a system error occurred during processing. This is a terminal state; you should retry the upload.

Also note: the `POST /payment-file-upload-service/payment-files` endpoint now returns a 500 in two additional scenarios: an object store failure or a queue publish failure during the upload phase. In either case, no pollable file record is created, so a 500 from this endpoint always means the upload did not go through and should be retried.

If you are handling status values exhaustively in your integration, make sure to account for these additions to avoid unexpected failures.

**What you need to do**

Review your integration against the updated status lifecycle and ensure your polling logic handles the two new values. For full API reference, see <https://modulr.readme.io/reference/upload-payment-file>

# API

## Direct Debit Indemnity Claim (DDIC)

To improve visibility of Direct Debit Indemnity Claims (DDIC), we are introducing a webhook to notify incoming claims and status changes.

This webhook will be available for new claims from **June 30th** and supplements your existing DDIC process.

What’s changing:

The new webhook `DD_INDEMNITY_CLAIM_STATUS` triggers whenever a claim changes status:

1. NEW - a claim has been raised against your account. You have until working day 9 to challenge it via the BACS Payment Service Website (PSW).
2. CANCELLED - Customer successfully challenged the claim. No settlement will occur.

SETTLED - the claim amount has been debited from the customer’s collateral account (14 working days after initial advice). The settlement entry now includes the service user reference for easier reconciliation.

Claim status can be checked on demand using two new endpoints:

`GET/direct-debit-service/indemnity-claims`

and

`GET/direct-debit-service/indemnity-claims/{id}.`

## Action required:

Review API documentation and subscribe to the `DD_INDEMNITY_CLAIM_STATUS` webhook to receive notifications.

**Reminder:** Direct Service Users’ authorised contacts can challenge a DDIC via the [BACS Payment Services Website (PSW)](https://paymentservices.bacs.co.uk/online/newbacs/loginBrowser.do?dts=0E9BED9F5D7D95F1CD9BFD47421E8A6F598371ED) up to working day 9. For customers where Modulr is the Service User (FM-DD), challenges must be processed through Modulr support.

## Read our guides to learn more:

<https://modulr.readme.io/docs/managing-direct-debit-indemnity-claims-ddic#/>

<https://modulr.readme.io/docs/webhook-direct-debit-collections-ddic#/>