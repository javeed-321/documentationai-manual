---
updatedAt: 2025-09-05T18:36:24.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Getting started with Physical Cards

Here is what is required to create and manage your very own physical cards

## Physical card creation processing

The process to create a physical card is asynchronous and uses a specific [physical cards end point](https://modulr.readme.io/reference/createphysicalcard). Requests are validated to ensure that they can be processed and if all is good with the request, we’ll acknowledge it by returning a task ID and management token.

**Task ID**\
This is an identifier that will allow you to track the outcome of the request.

**Management token**\
This value should be securely stored by your system as there is no way for this information to be retrieved after this step.\
The management token is required as an additional security step when requesting certain physical card actions e.g. activation, PIN reminder. **The Management Token is provided in the response object of the Create Physical Card Endpoint**

## Creating a valid request

A physical card request needs a few pieces of information to allow us to successfully create your cards.

**Product code**\
Your account manager will provide you with the product code that aligns to the card product that you have been set up to issue.

**Design references**\
You will need to be provided with a card design reference and a packaging design reference before you can create a physical card. These references are unique to you and tell us which of your card artwork and packaging combinations you want to be used for the card creation and subsequent mailing out of the card. Your account manager will be able to provide you with these ahead of go-live.

**Printed name**\
You need to specify how the cardholder name should appear on the card as part of its personalisation.

**Mobile phone number**\
Our physical cards are all enabled for 3DS processing which means a mobile phone number is mandatory as part of the card creation. The mobile number should be in the E.164 standard format e.g. +447XXXXXXXXX.

**Cardholder additional details**\
If your customer type is an “Individual” then you do not need to provide name, address or date of birth information in the create card request. Instead these are sourced by the Modulr platform from the information at the customer level for the purposes of the initial card create.

If however you are requesting a card for someone under a business customer type then you will need to specify the cardholder fields i.e. name, address and date of birth. Title is optional.

> 📘 Shipping Address
>
> Shipping Addresses are optional inputs to the API for physical card creation, this is to be used when the card delivery is not meant to be the Billing Address.
>
> All cards created with no Shipping Address will be delivered to the Billing Address, if a Shipping Address is present then the card will be delivered to that address.

## Tracking request outcome

The task ID returned in the create physical card response can be used to query the outcome of the request using the [get tasks end point](https://modulr.readme.io/reference/getcreatephysicalcardasynctasksbyaccount). Alternatively the task URL which is also provided which can also be used to obtain the task details.

Requests can have several states however in the vast majority of cases they will complete instantaneously and you may not observe all state transitions.

•	Received – initial state, awaiting processing\
•	Running – attempting to process\
•	Error – terminal state, request has failed\
•	Complete – terminal state, request has been successful

A request that is in Complete state will also provide the card identifier for the card that has been created.

There is a [webhook event](https://modulr.readme.io/docs/card-notifications) available that will issue a notification on the request outcome, whether error or completed result, where you have subscribed to this event type.

## Activating a card

Our physical cards are sent out inactive therefore once received by the cardholder you will need to use the [activation end point](https://modulr.readme.io/reference/activatecard) to activate a card.

> 🚧
>
> The activation end point requires the management token to be provided in the header as part of enhanced security.

A card can only be activated if it is in Created state (see [lifecycle status](https://modulr.readme.io/docs/card-lifecycle)).

Please note that 3DS enrolment can take up to 2 hours from card activation.

## PIN Management

Physical cards have PINs associated with them, Modulr have specific endpoints to support PIN management activities for cards.

**Retrieve PIN (API only)**

Modulr do not provide a mailer for PIN retrieval. Instead the [retrieve PIN API](https://modulr.readme.io/reference/retrievepin) must be used to obtain the PIN for the requested card.

A cardholder can change their PIN number at an ATM which means that any stored PIN numbers will not reflect updates that the cardholder has made. It is for this reason that we do not recommend that you store the PIN and instead you use the PIN reminder function to obtain the most current PIN for the card.

**Change PIN (API only)**

A cardholder can change their PIN at an ATM or the API can be used to support PIN [Reset Functionality](https://modulr.readme.io/reference/resetpin) . It is recommended by card schemes that the issuing card program verify the cardholder's newly selected PIN by having them provide it twice and ensuring that the values match ahead of sending the request to Modulr.

> 🚧
>
> The retrieve PIN and change PIN end points require the management token to be provided in the header as part of enhanced security.

**PIN/CVC2 Unblock**

In the event that a cardholder blocks the PIN and/or CVC2 of their card (by entering it wrong 3 times in a row), there is [an endpoint](https://modulr.readme.io/reference/unblockpin) that can be used to unblock these. A single call to this endpoint will process both types of unblock, there is no need to specify which type is required.

This can be used for virtual cards as well in the event of a CVC2 block.

> 📘 Blocked PIN and CVC2/CVV2
>
> Cards with blocked PIN can still be used for online e-commerce transactions but not for POS.\
> Cards with blocked CVC2/CVV2 can be used at POS but will be declined for all e-commerce transactions.

## Update card details

If any cardholder information changes e.g. mobile number or billing address, the [update card endpoint](https://modulr.readme.io/reference/update) can be used to update the details on the card.

This endpoint must be used regardless of customer type (i.e. business or individual) to update the details associated with the card even if the customer information is updated. Similarly updating the card details via this way doesn't update customer information.

To optimise card acceptance where merchants are using 3DS processing or address verification checks it is important that cardholder details are kept up to date.

## Block and unblock a card

You may wish to allow temporary elective blocking of a card e.g. in the event that a cardholder has misplaced their card. The [block](https://modulr.readme.io/reference/blockcard) and [unblock](https://modulr.readme.io/reference/unblockcard) endpoints allow this type of temporary blocking and unblocking.

> 🚧
>
> Whilst a card is blocked new authorisations are prevented against that card. Any already approved authorisations however will not be prevented from settling. This is why it is important that the card is blocked as soon as possible to prevent any fraudulent spend on it.

## Cancel a card

In the event that a card needs to be cancelled e.g. stolen, the [cancel card end point](https://modulr.readme.io/reference/cancelcard) can be used for this purpose. Cancelling a card is an irreversible action and terminal state for the card.

> 📘 Customer Portal and Physical Cards
>
> All of the functions detailed above can be performed in the customer portal with the exception of PIN retrieval which is API only.
>
> Where a function requires the management token in an API request, it is not required for actions performed in the customer portal however it will be provided if the card is created using the customer portal to ensure that it can be managed via API as well.