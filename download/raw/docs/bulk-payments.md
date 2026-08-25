---
updatedAt: 2025-09-05T18:35:34.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bulk payments

Creating multiple single payments with a single file upload

Instead of creating single payments one-by-one, we've made it easier for you to create all of them in one bulk by using the [same batch payment endpoint](https://modulr.readme.io/reference/submitbatchpayments) `/batchpayments`

To instruct the endpoint to treat the series of payments as individual payments instead of a batch, simply indicate the value of '*submissionType: bulk*' in your request body. If no value was provided when making the API call, the default value for *submissionType* field is 'bulk'.

**Default value for*submissionType***

The default value for the *submissionType* field is '*bulk*'. If you want to create a batch payment instead, you have to specify '*submissionType: batch*' in your request body when making the API call.

**Default value for*strictProcessing***

The default value for strictProcessing will depend on the value of submissionType.

* When *submissionType* is set to 'batch', strictProcessing will always be set to true
* When *submissionType* is set to 'bulk' or is not specified, *strictProcessing* can take the value of true/false, depending on your preference.

For more information on what strictProcessing and submissionType is, and what they do, please refer to the [endpoint documentation on our API guide](https://modulr.readme.io/reference/submitbatchpayments).