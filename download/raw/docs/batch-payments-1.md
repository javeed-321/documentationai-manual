---
updatedAt: 2025-09-05T18:35:33.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Batch Payments

You can use our batch payment endpoints to handle multiple payments in a single request. Payment batches can contain up to 10,000 payments in a single request.

To submit a payment batch via the API, use [Make a batch payment](https://modulr.readme.io/reference/submitbatchpayments).

The request must at a minimum contain an array of payments. The format of these is the same as [Create a payment](https://modulr.readme.io/reference/sendpayment).

The request can also contain an optional externalReference, you may want to use this to keep track of the payment batch in case you need to review or cancel it in future.

You can also include the 'strictProcessing' flag - this setting will determine what should happen to the batch in the event that one or more payments within the batch fail to process. If strict processing is enabled, then one failed payment within a batch will cause the entire batch to fail. If strict processing is not enabled, then the successfully processed payments within the batch will send even if there are some failures.

## How do I cancel a batch of payments with APIs?

### If your batch contains 10,000 payments or less

Use [Get batch payments by a given set of parameters](https://modulr.readme.io/reference/getbatchpayments) and query using parameters, such as an *externalReference* that you might have provided for the batch, to retrieve the batch's *batchId* value.

Then, use [Cancel the batch payment](https://modulr.readme.io/reference/cancelbatchpayments) with the *batchId* value, to cancel all applicable payments\
within that specific batch.

### If instead, your batch contains more than 10,000 payments

The maximum number of payments that can be currently processed as a batch is 10,000. If you have a\
batch of payments that exceeds this limit, you will first need to split them into smaller batches before\
submitting for processing.

However, you would be able to identify which smaller batches of payments belong to the original batch\
by assigning the smaller batches with the same *externalReference* string value of your own choosing, to\
manage them as a group later on.

To cancel all the payments within the original group of batch payments, use [Get batch payments by a given set of parameters](https://modulr.readme.io/reference/getbatchpayments) and query using the *externalReference* that was provided to the group of batch payments, and receive all the relevant *batchId*'s

For each of the *batchId* obtained in Step 1,  use the [Cancel the batch payment](https://modulr.readme.io/reference/cancelbatchpayments) to cancel all applicable payments within the batch

> 📘 Cancelling batch payments
>
> Note: When cancelling a batch of payments, only payments that have non-final statuses, such as\
> 'Validated', 'Pending\_For\_Date', 'Pending\_For\_Funds' will be cancelled.