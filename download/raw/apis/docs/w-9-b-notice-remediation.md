---
updatedAt: 2025-10-24T15:24:38.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# W-9 B-Notice remediation

When a customer receives a B Notice from the IRS, it indicates a mismatch between the customer's name and Taxpayer Identification Number. In such cases, DriveWealth will send the required communication to your customers in accordance with IRS regulations.

Customers have approximately 15 business days to respond to the B notice. At the end of the grace period, DriveWealth will flag any users who did not respond and send an event notification to your system. Failure to take action within this window will result in TEFRA backup withholding.

For the W-9 B Notice remediation process, you can either direct users to DriveClient for self-service recertification, or build your own UI following the steps outlined below.

### Step 1: Monitor Users with B notice due

To determine if user remediation is required, you can check if `validTaxForm` is `false` on the [Retrieve User](https://developer.drivewealth.com/apis/reference/get_users-userid) API.

**Sample response:**

```json
{
...
  "validTaxForm": false,
  "validTaxFormWhen": "2025-09-30T18:48:55Z",
...
}
```

Alternatively, you can also subscribe to the user.inforequired.created event to be notified when remediation is needed.  Please refer to User Info Required Created [event](https://developer.drivewealth.com/apis/reference/user-events) documentation for payload details.

### Step 2: Verify User Information

Use [Retrieve User](https://developer.drivewealth.com/apis/reference/get_users-userid) API to retrieve and display key identity details for customer verification, including the following key user identification attributes:

* first name, last name
* ID type, ID number
* citizenship

### Step 3A: Update User info (if required)

If the customer identifies any incorrect information, update their profile via the [Update User](https://developer.drivewealth.com/apis/reference/patch_users-userid) API.

**Sample payload:**

```json
{
  "documents": [
    {
      "type": "BASIC_INFO",
      "data": {
        "firstName": "New",
        "lastName": "Name"
      }
    }
  ]
}
```

### Step 3B: Provide attestation (if no changes required)

In rare cases, the IRS may have outdated or incorrect data but the customer's profile with DriveWealth is accurate. If the customer affirms their information is correct and chooses not to update it, they must provide attestation and agree to the following terms:

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

The `signedBy` field must match the user's `userID`.

### Step 4: Display New W-9 PDF

After user info update or attestation submission, a new W-9 PDF is generated and you should display the PDF form for the customer to review. You can do so by using the [Retrieve Physical Document URL](https://developer.drivewealth.com/apis/reference/get_documents-documentid-url) API or by listening to the `documents.create` event.

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

<br />