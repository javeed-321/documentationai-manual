---
updatedAt: 2025-10-24T15:32:39.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# W-8BEN recertification

W-8BEN forms expire three years after their initial creation. Once expired, the customer is subject to 30% NRA tax withholding on dividends. This is reflected in the `w8expires` field on the User, which will show a date in the past (e.g., < today).

NRA tax on dividend will generate a `DIVNRA` type Transaction, with a comment indicating that 30% withheld was applied. This allows you to programmatically detect increased withholding by inspecting the Transaction type and comment.

To avoid this, you should proactively prompt users to recertify their W-8BEN forms before expiration.

### Step 1: Monitor expiration

To track when a W-8BEN form is due for recertification, you can use the `w8expires` field available in the User object returned by the [Retrieve User](https://developer.drivewealth.com/apis/reference/get_users-userid) API. We recommend storing the expiration date on your end and implementing your own monitoring mechanism.

You may also request a list of users with expiring W-8BEN forms from your Relationship Manager (RM).

### Step 2: Verify User information

Use Retrieve User API to display identity details for customer verification, including the following key identification attributes:

* First/Last name
* Date of birth
* Identification number
* Citizenship
* Address
* `taxTreatyWithUS`

### Step 3A: Update User info (if required)

If the customer identifies any incorrect information, update their profile via [Update User](https://developer.drivewealth.com/apis/reference/patch_users-userid) API.

### Step 3B: Provide attestation (if no changes required)

If the customer affirms their information is correct and chooses not to update it, they must provide attestation and agree to the following terms:

> You are acknowledging, under penalty of perjury, that the information provided is complete and accurate.
>
> You are acknowledging, under penalty of perjury, that the information provided is complete and accurate. You further acknowledge that you will be providing electronic signatures as part of your tax certification process (W-9 for U.S. taxpayers), and that the information you have entered is complete and accurate for IRS filing purposes.

**Sample payload:**

```json
{
  "documents": [
    {
      "type": "TAX_INFO",
      "data": {
        "attestation": {
          "signedBy": "babe99fe-21cc-41e4-aa8a-d13c3c90767a"
        }
      }
    }
  ]
}
```

The `signedBy` field must match the User's `userID`.

DriveWealth will generate a new W-8BEN form only if the resulting form would have a later expiration date than the current one on file.

**Examples:**

* If the existing W-8BEN expires on 12/31/2027 and the user provides an attestation on Sep 29, 2025: a new W-8BEN will be generated with an expiration date of 12/31/2028
* If the existing W-8BEN expires on 12/31/2028 and the user provides an attestation on Sep 29, 2025: this attestation won’t trigger a new W-8BEN form since the new form would have the same expiration date on file.

### Step 4: Display new W-8BEN PDF

When a new W-8BEN form is generated, you should display the PDF form for the customer to review. You can do so by using the [Retrieve Physical Document URL](https://developer.drivewealth.com/apis/reference/get_documents-documentid-url) API or by listening to the `documents.create` event.

#### Using the API:

1. Retrieve a list of documents associated with a user: [List User Physical Documents](https://developer.drivewealth.com/apis/reference/get_users-userid-documents) API
2. Filter for latest tax document: select the document with type `TAX` and the latest `receivedWhen` timestamp
3. Retrieve document URL: [Retrieve Physical Document URL](https://developer.drivewealth.com/apis/reference/get_documents-documentid-url) API
4. Use the returned URL to open and display tax form in PDF format

#### Using the event:

If you subscribe to the `documents.created` event, a notification will be sent to your system once a new W-9 PDF is generated. You can directly open up the PDF from the `s3UrlLink` field returned in the event.

**Sample payload:**

```json
{
  "id": "event_313154b9-6dd6-447d-b7fa-bf0e3e8aa365",
  "type": "documents.created",
  "object": "TAX",
  "timestamp": "2025-09-29T21:19:45.278Z",
  "payload": {
    "userID": "500055f6-2f18-44f4-a69b-b010d74acf58",
    "documentID": "8664bfad-69e5-46b7-9355-22f9123a8163",
    "taxForm": {
      "s3UrlLink": "https://d3fsvf73xdspxh.cloudfront.net/8664bfad-69e5-46b7-9355-22f9123a8163.png?..."
    }
  }
}
```

**Tips:**

* Ensure that the attestation terms are clearly displayed to the User for consent and acknowledgment.
* Verify that the `signedBy` field matches the User’s `userID`.
* Subscribe to relevant event notifications to receive real-time updates on User action requirements.