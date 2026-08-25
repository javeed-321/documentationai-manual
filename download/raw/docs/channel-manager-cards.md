---
updatedAt: 2025-09-05T18:57:08.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager - Cards

## Creating Cards

When creating a card use endpoint [POST/channel-managers/accounts/\{aid}/cards](https://modulr.readme.io/reference/channelmanagercreatecard) and supply the following information as mandatory for creating cards for OTA’s:

**Account ID** – account the card is to be created on, this will be obtained from the OTA

**Limit** – total card authorisation limit available

**Expiry Date** – this must be at minimum one month following the card creation and can be a maximum of 60 months from the date of creation

**Product Code** - this will be the product ID supplied by the OTA, this will also state the currency of the card

**External Reference** – this will be a unique reference for the card which the OTA wishes cards to be created under, you will need this from the OTA

The following are optional details that can be added if required:

**Cancellation Date** – date at which you want the card to automatically cancel

**Authorisation Window** – these are dates in which the card can be used for authorisations not including account status inquiries (ASI’s)

**Custom Fields** – use [POST/channel-managers/custom-fields](https://modulr.readme.io/reference/channelmanagerupdatecardcustomfields) in addition to the create card request to add details that are required by the OTA.  You will need to know the custom field key name and have that input along with the value to successfully add the custom field

Successful creation of a card will result in a 204-response code from Modulr and will include a unique reference that is generated at Modulr (example V21000000) that you can store to use later for any other card related activities.

<br />

## Updating Cards

When there is a need to amend an existing card, there’s two endpoints which need to be used and each will do different things.

[POST/channel-managers/cards/\{id}](https://modulr.readme.io/reference/channelmanagerupdatecard)

You will need to supply the card ID that has previously been generated when creating the card as well as what is being amended, the amendable items are:

**Limit**

**Cancellation Date**

**Authorisation Window**

> 🚧 Incorrect Data
>
> If any other details are incorrect then the card will need to be cancelled by the OTA and a new card set up in place

[PATCH/channel-managers/cards/\{id}](https://modulr.readme.io/reference/channelmanagerupdatecard_1)

Again you will need to supply the card ID and on this call the only permissible actions are fully deleting the cancellation date and the authorisation windows.

> 📘 Blocking / Unblocking Cards
>
> For any blocking or unblocking of cards please use the following endpoints to pass the request through:
>
> [Block Cards](https://modulr.readme.io/reference/blockcard)
>
> [Unblock Cards](https://modulr.readme.io/reference/unblockcard)

<br />

## Retrieving Cards

This is a self-managed report function that operates on set details, more detailed reports will be made available to you (see Reports sections)

When calling [GET/channel-managers/cards](https://modulr.readme.io/reference/channelmanagergetcards) you have a list of parameters that you are able to search by, these are:

**Created Dates** – Both FROM and TO dates are available however the data will only return back cards created in the last 7 days

**Status** – The specific state the card is in (ACTIVE, CANCELLED, EXPIRED, BLOCKED, SUSPENDED)

**Card ID** – The specific card ID of the card you are wanting to query

**Account ID** – The specific account ID you want to retrieve cards for

**External Reference** – The specific external reference for the card

**Currency** – The currency of the card

**Custom Field Key** – Specific key used for populating custom fields

**Custom Field Value** – The specific value that has been input on a card

**Account ID’s** – List of account ID’s you wish to return cards on

**Channel Manager ID** – The unique ID for you (obtained when onboarded to Modulr)

If however, you are just looking to see the specific state a card is in use [POST/channel-managers/enquiry](https://modulr.readme.io/reference/channelmanagercardenquiry) and it will return all current details on the card.