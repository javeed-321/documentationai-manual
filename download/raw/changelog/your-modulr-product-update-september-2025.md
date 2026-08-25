Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Your Modulr Product Update September 2025

<Image align="center" border={false} width="600px" src="https://files.readme.io/c806c32a1e1f8d958d6b133f07bf730184c7487ac2607f302edb83b882f59c4b-image.png" />

<br />

<Image align="center" border={false} width="600px" src="https://files.readme.io/6180500c9af673242159c47d94224b4f78c269a5bfc35eb1589999a63c4118fd-image.png" />

# API

## Product ID now available via the Get an Account API

You can now retrieve the Product ID (Product Code) for any Modulr account directly via the Get an Account API.

Each Modulr account is assigned a Product ID at onboarding. This ID determines which product(s) the account is used for, for example, whether it supports Direct Debit Outbound or CHAPS.

This update means you can track and identify which product functionality is enabled on each account you’ve opened on the Modulr platform.

It’s especially useful for customers managing multiple accounts with varying configurations.

For any questions, our support team is here to help.

<br />

# The Modulr Portal and API

## New Webhooks for Payment Approvals

We’ve introduced new webhook notifications for Batch and Individual Payment Approvals via the Modulr Portal - **available to Partners and Integration Partners only.**

This means you can:

* Receive real-time updates when a user approves a payment
* Streamline your approval tracking across both batch and individual payments
* Reduce manual follow-ups and improve operational efficiency

Once enabled, these webhooks trigger automatically when a user completes an approval in the Portal.

To get started, check out the implementation guides:

[Individual Payment Approvals](https://modulr.readme.io/docs/payment-approval-rejection-webhook)

[Batch Payment Approvals](https://modulr.readme.io/docs/webhook-batch-payment-approval-status-change)

<Image align="center" border={false} width="600px" src="https://files.readme.io/8904e4a35990d0b88d542f180beacaa66080c193b89194fb0a175eb1848737fe-image.png" />

<br />

<Image align="center" border={false} width="600px" src="https://files.readme.io/802485802d9e913ca6f289879f3cb88f6391d0ca53ad88dd9b7f059065dece45-image.png" />

# The Modulr Portal and API

## Changes ahead of the Instant Payments Regulation

As part of preparations for the upcoming European Instant Payments Regulation (IPR), we’re introducing several enhancements and changes to the platform. These changes are required for Eurozone PSPs and will go live on 9 October 2025, in line with the regulation deadline.

From this date, an important change is the introduction of Payee account name checks (called Verification of Payee or VoP in the EU) that will be integrated into SEPA payment flows in the Modulr Customer Portal.

**✅ Account name-checks in the Modulr Portal**

From 9 October, Verification of Payee (VoP) will be integrated into SEPA payment flows in the Modulr Customer Portal.

* VoP checks are advisory - customers will still be able to proceed with payments after reviewing the result.
* 📘 Updated [portal user guides](https://knowledge.modulrfinance.com/knowledge-hub/using-the-modulr-portal) will be published in early October to support these changes.

**✅ Account name-checks when making payments via API**

If you’re a customer using **the Modulr API integration** to make payments:

* A new optional endpoint will be available to perform VoP checks when capturing account details or initiating payments to new beneficiaries.
* 🧪 The VoP service is available now to test in our [sandbox environment.](https://modulr.readme.io/docs/eu-verification-of-payee-vop)
* 💸 There is no additional charge for using VoP when making payments from a Modulr account, and we encourage adopting it as a best practice.

You can find out more in our[ VoP API documentation](https://modulr.readme.io/docs/eu-verification-of-payee-vop#/):

*You will have received separate communications from Modulr if you are **a European partner required** to implement VoP as part of your SEPA payment service usage by the October deadline.*

**💶 SEPA Payment Limits**

We’re increasing the maximum transaction limit for SEPA payments and making them the same for any type of payment:

* ⬆️ The current scheme limit of €100k for SEPA Instant will be removed
* Modulr will support payments up to €10m per item for both SEPA Instant and SEPA Credit Transfers.

**🔁 SEPA Payment routing updates**

We’re updating how SEPA payments are routed to improve transparency and control:

* ⚡ Modulr will send Euro payments as SEPA Instant where supported and, and where recipient bank does not support Instant Payments we’ll automatically send SEPA Credit Transfer
* However, now in cases where a the recipient bank does support SEPA Instant, but the SEPA Instant payment execution is rejected, the payment on the Modulr platform will reflect this instead of automatically converting to SEPA Credit Transfer.
* 🔧 This gives you a more immediate result and the option to resubmit another SEPA Instant payment, or explicitly instruct a SEPA Credit Transfer via a new *permittedScheme*[parameter in the Payment API](https://modulr.readme.io/docs/sepa-payment-changes-instant-payments-regulation#/).

<br />

# API

## Notification Webhooks available for Channel Managers

We’ll soon be enabling **CARDAUTH, PAYIN**, and **PAYOUT** webhook notifications for **Channel Managers**, helping you manage card usage more effectively.

This means you can:

* Monitor card authorisations, inbound payments, and outbound transactions in real time
* Improve visibility and control across your card programmes
* Reduce reliance on manual checks and support queries

These webhooks will be available from **25th September.**