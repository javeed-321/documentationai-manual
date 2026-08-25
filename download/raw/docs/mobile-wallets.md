---
updatedAt: 2025-09-05T18:57:00.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Tokenisation - Overview

## Background

Tokenisation provides cardholders with a secure and convenient way to store and use their cards by replacing the sensitive card data with a unique identifier called a token, this token can then be used for transactions without revealing the original sensitive card data.

There are two types of tokenisation, Acquirer and Issuer based.

Acquirer based is where the merchant requests the card details they use to make payment on to be converted to a token, this is usually for merchants like streaming services, online shopping etc.

> 📘 Acquirer Token Management
>
> These tokens are set up by the acquirer and they request authorisations through these tokens, whilst Modulr does set these up with a unique token identifier the management for these are with the merchant.

Issuer based are in the form of digital wallets, also known as mobile wallets, which use tokenisation to secure payment data, as tokens are less vulnerable to fraud than the original data.  The digital wallets available for use at Modulr are Apple Pay and Google Pay, and both of which instead of containing a card's PAN, CVV, and expiry date, will only contain the token.

> 📘 Transactions on Issuer Tokens
>
> As the card details have been converted to a token its worth noting that it will be the token details used for transaction purposes however, these will still be able to be matched to a card at Modulr to support you in your transaction matching.

## Provisioning a card

Provisioning is the process of setting up a card on a digital device, such as a smartphone or tablet, for use in mobile payments. There are two ways that a cardholder can provision their card to a device, Wallet (sometimes referred to as camera capture) and Push Provisioning (sometimes referred to as in-app provisioning).

Wallet based provisioning allows the cardholder to add their card to the devices wallet app, either by scanning their card using the camera when prompted or by manually adding the card details.  The card will need to be authenticated which will be completed either via SMS or Email, once authenticated the card is tokenised and the token is placed into the wallet.

> 📘 Card Authentication
>
> To authenticate the card in this method a One Time Passcode will need to be generated and sent to the cardholder to add the code into the device wallet.
>
> Details on how to mange OTP requests is in the section **OTP Management**

Push Provisioning is where the cardholder goes though the Partner / Customer digital app and selects "Add card to Wallet", by doing this the authentication for the card is taken from the client accessing the app in the first place (either passcode or FaceID).

> 🚧 Push Provisioning Prioritisation
>
> For both Apple Pay and Google Pay, it is a requirement that if a card program has a mobile app then Push Provisioning has to be implemented.  If there is no mobile app then it needs to be stated upfront for both token providers to approve before any implementation can be started.

## Client Setup

Cards are not automatically enabled to be used with physical wallets and need to go through the enablement project. Contractual arrangements between Modulr, the wallet providers, and card networks that are specific to mobile wallets will need to be defined.

Once all the legal documentation has been agreed, documentation detailing the next part of the process will be sent out.  This will include how to set up tokenisation for the card program, marketing and branding requirements and launch processes.

It can take approximately four months end to end to complete the onboarding process.

> 📘 Crypto Card programs
>
> It is worth noting that all crypto card programs looking to be set up for Tokenisation will require a crypto licence  prior to application, there will be separate licence required for the UK and EU.
>
> Legal review of these licences by the wallet providers can add extra time to the onboarding process.