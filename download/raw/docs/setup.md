---
updatedAt: 2025-09-05T18:29:44.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# General Tokenisation Setup

## Visa Metadata Requirements

To ensure a card program is set up correctly for Tokenisation you will need to provide Modulr the following information:

* Digital Card Art
* Digital Icon
* Visa Co-Brand Reference
* Privacy Policy URL
* Terms & Conditions URL
* Terms & Conditions (plain text file)
* Customer Service Contact Number
* Customer Service Email Address
* Website URL
* Fraud Service Contact Number (if different from above)
* iOS Mobile Banking App Launch URL
* iOS Mobile Banking App ID
* iOS Mobile Banking Store ID
* Android Mobile Banking App Name
* Android Mobile Banking URL

> 👍 Digital Card Art
>
> Below are the specifications on how the digital card art will need to be presented:
>
> * Card art should represent the physical card, but should not be a picture/photo of the physical card
> * Card shouldn’t include shading or three-dimensional elements attempting to look like a physical card
> * Card art should not include cardholder name, PAN, BIN or expiry, either generically or the actual values
> * Card art should not include items that only make sense on a physical plastic card, such as labels describing embossed attributes, or EMVchip contacts, or static pictures of dynamic elements like holograms
> * Card art may include the Contactless Indicator, even if the physical card is not contactless enabled
> * Corners on card art must be squared
> * Card art must be landscape orientation, 1536 pixel x 969 pixel (proportional to an ISO ID-1 size card) and submitted as a.PNG file
> * Card art should be in 72 DPIColor format for all sizes is RGB, 16+ color bit depth, non-interlaced
> * Files must be named using the following file structure:D-pixel (propor-ional to a.png
>
> The card program will also need to supply the colouring used for the cards in the following format:
>
> * Background - rgb(rrr, ggg, bbb) ie. rgb(122, 255, 84). Range is 0 to 255.
> * Foreground - rgb(rrr, ggg, bbb) ie. rgb(122, 255, 84). Range is 0 to 255.
> * Label - rgb(rrr, ggg, bbb) ie. rgb(122, 255, 84). Range is 0 to 255.

> 👍 Digital Icon Specifications
>
> * Icon must be 100 x 100 pixels and submitted in a PNG format
> * This icon will be used for things like notifications related to the card.
> * This icon should be the primary brand associated with the card in the wallet, either the bank or the co-brand, if applicable