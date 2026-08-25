---
updatedAt: 2025-09-05T18:36:35.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Card Controls

Card controls allow you to specify rules for when transactions should be approved or declined.

## Spend controls

Spend controls, where set, are checked as part of a new authorisation approval flow and allow you to specify value and volume limits for card transactions.

There are four types of spend limits:

* **Lifetime spend limit** – the total amount that can be spent on a card in its lifetime. This limit is set on card creation and can be changed at any point via the API. This is presented as "limit" in the create a new card functions as well as update a card.
* **Currency** – it possible to specify which currencies the card can transact in. This is set on card creation but cannot be changed subsequently - please consider using this feature carefully as it is intended for single-use Virtual Cards only. This is found under 'constraints > authorisation > spend' in the API.
* **Transaction limit** – the maximum/minimum that can be spent per transaction on a card. This is set per currency on card creation but cannot be changed subsequently - please consider using this feature carefully as it is intended for single-use Virtual Cards only. This is found under 'constraints > authorisation > spend' in the API.

> 🚧 Currency And Transaction Limits
>
> Please note. By setting a min/max limit within a currency constraint, this will cause any transactions with a different transaction currency to fail. So, you only need to specific a Currency constraint if you wish to restrict the card to a specific transaction currency.

* **Velocity limit** – each card is assigned a ‘Velocity Group’ at creation, which has lifetime and rolling weekly/monthly limits, as well as ATM limits, etc. We set some defaults for each card type, but this could be tailored for individual client requirements. This is presented as "SpendConstraintDetail" in the constraints object which is part of the create a new card functions only.

## Merchant category controls

These controls allow you to block or allow certain merchant category codes (MCCs) e.g. gambling transactions. These can be set and modified by your Modulr Customer Success Manager.

A full list of MCCs is available [here](https://github.com/greggles/mcc-codes).