---
updatedAt: 2026-02-24T14:43:41.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# VRP overview

## Overview

Variable Recurring Payments (VRPs) are a type of payment method that allows users to set up recurring payments which can vary in amount and frequency. The user provides long-lived **consent** for real-time, account-to-account payments to be made within agreed parameters, meaning they do not need to authenticate each payment with their bank. Payments of varying amounts can be swept from the user’s bank account on a continuous, as long the payments remain within certain customer-approved limits (also called parameters).

VRPs are possible thanks to Open Banking regulations, which allow customers to give authorised third parties access to their bank account data to make payments on their behalf, with their consent.

Note – the Open Banking Implementation Entity (OBIE) uses the term “consent” to refer to the contract between the Payment Service User (PSU) and the Third Party Provider (TPP), in this case Modulr. A consent created between a PSU and TPP allows the TPP (i.e. Modulr) to initiate VRPs on behalf of the PSU, subject to agreed parameters.

> 🚧 VRP restrictions
>
> VRP payments can only be made between two UK accounts
>
> VRP payments can only be made in GBP currency
>
> All VRP payments are made via the Faster Payment (FPS) payment rail

## Types of VRP

> 📘 Sweeping vs Non-Sweeping VRP
>
> There are two types of VRP – Sweeping and Commercial (also known as Non-Sweeping)
>
> Modulr only support Sweeping VRP at present

### Sweeping VRP

Payments between two accounts belonging to the same person or business entity.

The Competition and Markets Authority (CMA) have outlined the key features that a payment must have for it to be classified as a sweep:

1. A sweep must be from a UK source account – either a Personal Current Account (PCA) or Business Current
2. Account (BCA) - to a UK destination account (a “Me-To-Me Payment”).
3. The source account and the destination account must belong to the same name or legal entity.
4. Both accounts are UK sterling accounts.
5. A sweep can be an unattended payment, requiring no interaction from the user at the time the sweep is made.

The CMA has permitted the following use cases for sweeping:

1. Sweeping between current accounts
2. Sweeping to destination accounts for unbundling overdrafts
3. Sweeping to destination accounts for loan repayments
4. Sweeping to a credit card account
5. Sweeping to cash savings accounts

### Commercial VRP (also known as Non-Sweeping VRP)

Refers to the use of VRP functionality for making payments which fall outside the scope of Sweeping VRPs, as defined by the CMA.

Commercial VRPs include:

1. *Me-To-Me Payments* where the source and destination accounts are in the same name or legal entity, but where the destination account does not have the features of a current account (or of the other permitted use cases listed above).
2. *Me-To-Them Payments* where the source and destination account are in a different name or legal entity. This is where payments are made to a business for the purchase of goods or services.

Typical use cases for Commercials VRPs include:

* Ecommerce purchases
* Subscriptions or recurring payments such as utility bills
* Investments

> 🚧 Modulr currently only offers Sweeping VRP
>
> Please engage with your Modulr point of contact should you require any support in understanding whether your use case is Sweeping or Commercial VRP

<br />

## Banks supporting Sweeping VRP

Sweeping VRP is currently available with the following banks in the UK:

| Bank                       | Supported account type(s) |
| :------------------------- | :------------------------ |
| Allied Irish Bank          | Personal, Business        |
| Bank of Scotland           | Personal, Business        |
| Bank of Ireland 365 Online | Personal, Business        |
| Barclays                   | Personal, Business        |
| Danske Bank                | Personal, Business        |
| First Direct               | Personal, Business        |
| Halifax                    | Personal, Business        |
| HSBC                       | Personal, Business        |
| Lloyds                     | Personal, Business        |
| Monzo                      | Personal, Business        |
| Nationwide                 | Personal, Business        |
| NatWest                    | Personal, Business        |
| RBS                        | Personal, Business        |
| Santander                  | Personal, Business        |

<br />

## Sweeping VRP - High Level Customer Journey

To set up a Sweeping VRP, your user (the PSU) must authorise a **consent**. This consent acts as an agreement between the PSU and Modulr for Modulr to take payments from the user’s bank account, within the agreed parameters of the consent. This means the user is not required to authenticate individual payments, enabling a more seamless customer journey for both attended and unattended payments.

The customer journey can be separated into the following high-level activities:

1. Consent
   1. Create a VRP consent
   2. Revoke a VRP consent
2. VRP payment
   1. Initiate a VRP payment under the consent
   2. Get a status update on the payment