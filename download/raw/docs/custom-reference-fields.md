---
updatedAt: 2025-09-05T18:36:30.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Custom Reference Fields

How to set up and manage Custom Reference Fields

Custom Reference Fields are the ability to add extra information to cards, at either the creation stage or whether you are updating a card, this can be for whatever extra detail you require for managing cards.

**Note** - this is available on both Physical and Virtual cards

This is split into two different parts - the key and the key-value, below goes into detail about each aspects.

A total of 20 Custom Reference keys can be created and managed.

## Custom Reference Field Keys

Custom Reference Field keys are required be set up in the first instance as these are what decides what extra information is required on the card, these are able to be created in bulk so if there's more than one that's required on the cards these can all be created in one go.

An example would be adding Booking References to cards.

```Text JSON
customFields: [
  {
    "key": "bookingRef",
    "required": "true"
  },
  {
    "key": "carRentalNo",
    "required": "false"
  }
]
```

The endpoints needed to create the keys are:

* [Bulk Create Partner Custom Field Keys](https://modulr.readme.io/reference/bulkcreatepartnercustomfieldkeys)
* [Bulk Create Customer Custom Field Keys](https://modulr.readme.io/reference/bulkcreatecustomercustomfieldkeys)

> 🚧 Limitations
>
> Below is a list of the limitations that are set on the endpoints:
>
> * Maximum of 20 ACTIVE keys (active is defined as "true" on the request)
> * 30 character length of only Alphanumeric
> * Required can only be "true" or "false"
> * No duplicate key names allowed, bad request will be the response if a duplicate is provided

If a key is no longer needed or created in error then they can be deleted by using one of the following links:

* [Delete Partner Custom Field Key](https://modulr.readme.io/reference/deletepartnercustomfieldkey)
* [Delete Customer Custom Field Key](https://modulr.readme.io/reference/deletecustomercustomfieldkey)

> 📘 Can I amend a Key?
>
> No, keys can not be amended once created.  A new key would be required to be set up and the one that needs changing is to be deleted.

## Custom Reference Field Key-Values

When creating a card or updating a card, and you have created Custom Reference Field keys you will need to add the key and the key-value in the requests.

The following endpoints are needed to complete these requests:

[Create Virtual Card](https://modulr.readme.io/reference/createcard)

[Create a Physical Card](https://modulr.readme.io/reference/createphysicalcard)

[Update a Card](https://modulr.readme.io/reference/update)

> ❗️ Required Keys
>
> If a Custom Reference Field key has been created and required is set to "true" then you must include this on the above requests, if not the request will fail.

## Managing Custom Reference Fields

If a key-value is needed to be deleted then use [Delete Custom Field](https://modulr.readme.io/reference/deletecardcustomfield)

All existing endpoints used for retrieving cards now include the Custom Reference Fields as well, please use these if more detail is needed on what Custom Reference Fields have been set up.