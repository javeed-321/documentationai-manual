---
updatedAt: 2025-09-05T18:56:28.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Replacing a card

In the event that something has happened to your card and you would like a new one to replace it, the [Replace a card](https://modulr.readme.io/reference/replacecard) can be used.

By replacing a card, you are creating the next card in that chain of cards and this can continue throughout the lifecycle of the card.  Creating a new card will create a new chain replacements can work through..

> 📘
>
> If the card being replaced is a PHYSICAL card then there is a requirement to use the [Active Physical Card ](https://modulr.readme.io/reference/activatecard) endpoint once the card has been activated.
>
> Regardless of the card type, once the replacement has been activated the the old card will be marked as Restricted Card.

> 👍
>
> When a card is replaced, if you have enrolled the old card with 3D Secure credentials, then the new card is automatically enrolled with the same 3D Secure credentials.

## Replacement Card Options

**Damaged**

If your physical card has been damaged in some way, and it either still works but needs replacing or it no longer can be used, then select this reason as a replacement.

The existing card will remain active until the new card has been activated at which point the old card will no longer be able to be used.

**Renew**

If your card is coming up to expiry and you require a new card (both virtual and physical) then select this reason for replacement, the existing card will continue to work (unless already expired) and will remain active until the new card has been activated.

If the card has already expired, then this reason can also be given to replace the card.

**Lost**

If you have lost your card and require a new one then select this reason for the replacement, the card will be deactivated immediately and will no longer be able to be used if found at a later time.

**Stolen**

If the card has been stolen, or where the card details have been fraudulently used, but you still require a new card then use this reason for replacement.

The card will be deactivated immediately and will no longer able to be used.

> 📘
>
> Modulr will provide the new card details to any merchants that store your card details in a tokenised format upon replacement of the card automatically.

> 🚧
>
> Cards in a SUSPENDED state are unable to be replaced however all other states are able to be replaced, best practice is to only allow replacements on cards in an ACTIVE state.

> 📘
>
> Its possible to be able to replace a card that's already in a CANCELLED state as long as the underlying account is still ACTIVE and its the next card in the chain, just select the most appropriate reason.

## Optional Changes

There are three optional changes that can be added to the replacement card which are:

External Reference\
Design (Physical only)\
Packaging Reference (Physical only)

These will remain the same as the previous card if the fields are empty, only change if required.

See [Getting started with Physical Cards](https://modulr.readme.io/docs/physical-cards-overview) for detail.

> ❗️
>
> All replacement cards will be sent to the billing address stored at Modulr, with no option to select another address for the card to be delivered to.
>
> Prior to any replacement card application please ensure the address details are correct and where the new replacement card should be sent to, any changes made after a replacement card has been ordered will not effect the card destination.

## PIN management

With all options to replace the card, the PIN will remain the same as previously set and a separate request will need to be made to make any amendments to the PIN.\
If the PIN is required to be changed then use the [Reset card PIN](https://modulr.readme.io/reference/resetpin) end point after the [Replace a card](https://modulr.readme.io/reference/replacecard) end point has been completed.