---
updatedAt: 2026-02-16T15:42:03.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bulk Card Operations

## Overview

Bulk Card Operations enables clients to create, update, or cancel multiple cards in a single request, rather than submitting individual API calls per card.

This functionality is designed to:

* Improve operational efficiency
* Support large-scale card issuance or maintenance activities
* Simplify batch updates and cancellations

<Callout icon="📘" theme="info">
  Bulk Card Operations is a feature that requires enabling first, speak to the account manager in the first instance to get this set up.
</Callout>

<br />

## How it works

There's two ways in which a request can be made:

* API
* CSV Upload

<Callout icon="🚧" theme="warn">
  The CSV template can be downloaded from the Portal if you are a Portal user, if not please upload your own CSV using the Header Descriptions below.
</Callout>

Once the request has been made, the request will be processed asynchronously and you will be notified when completed.

To send the request use either [Bulk Operations Request](https://modulr.readme.io/reference/submitbulkcardoperations) for API requests and [Upload CSV](https://modulr.readme.io/reference/uploadbulkcards) for CSV's requirements, you will get returned an ID that can be used to track Bulk Operation requests as well as the related webhooks for actions completed on cards in the same way you do for standard requests.

<Callout icon="🚧">
  For the API request the details that need to be supplied are as follows:

  * **ExternalRef** - This is the EXTERNALREF from the create card endpoint (required)
  * **ID** - Not required for API
  * **OperationType** - Select the required operation 
  * **Payload** - full payload of that specific request ensuring that the validations for that request are also followed (this would stop errors)
  * **CardID** - This is the VBID for the card (Only required for UPDATE or CANCEL) (required)
  * **Account ID** - This is the ABID required to do any action on cards (required)
</Callout>

<br />

## Headers in CSV

The headers within the CSV will need to be as follows:

* **Operation** - This must be either CREATE, UPDATE or CANCEL (required)
* **Card ID** - This is the VBID for the card (Only required for UPDATE or CANCEL) (required)
* **Usage** - This must be either SINGLE\_USE or MULTI\_USE (default is MULTI\_USE if left blank) (optional)
* **Alias** - This is the EXTERNALREF from the create card endpoint (required)
* **Account ID** - This is the ABID required to do any action on cards (required)
* **Product Code** - This is the OBID relating to the card product that you have been assigned to create cards (required)
* **Limit** - This is the limit you wish the card to be used for (required)
* **Auth Start** - If you are using an Auth Window then add the start date to this header (optional)
* **Auth End** - If you are using an Auth Window then add the end date to this header (optional)
* **Cancel Date** - Date you wish to the card to cancel if earlier than expiry date (optional)
* **Expiry Date** - The expiry date of the card (required)

<Callout icon="🚧" theme="warn">
  If you utilise Custom Fields then you can add extra columns as headers in the csv just ensure that the header is named after the Custom Field key you have created
</Callout>

<Callout icon="📘" theme="info">
  Limitations on any of the headers can be found under the details within the standard API calls
</Callout>

<br />

## Bulk Operations Management

Along with being able to submit the requests for Bulk Operations you can also manage these items with the following endpoints:

* [GET Bulk Operations](https://modulr.readme.io/reference/getactivebulkcardrequests) - to get all active Bulk Operation requests
* [GET Bulk Operations by ID](/bulk-cards/\{bulkRequestId}) - to get back a specific Bulk Operation request
* [DELETE Bulk Operations Request ](https://modulr.readme.io/reference/deletebulkrequest) - to delete a specific request that has been submitted

<br />