---
updatedAt: 2025-09-05T18:55:34.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Getting started with VRP

VRP functionality can be integrated into your own app, website or using a URL link sent directly to end users.

## Pre-requisites

**For Sandbox Access**

* You have registered with the Modulr Sandbox.
* You have provided our implementation team with your own secure redirect URL, where your end users will be redirected after authenticating with their bank.
* You have received the bank's sandbox login credentials from our implementation team.

> 📘 Sandbox access
>
> Our sandbox is currently connected to RBS for testing purposes. This enables you to simulate the entire end-to-end flow but note that real payments will not be made.

**For Production**

* You have been fully onboarded as Partner or Direct Customer and you have provided us with your secure redirect URL for the production environment.
* We have reviewed and approved your implementation and user interface to ensure it complies with our guidelines and regulatory requirements.

> 📘 Prerequisites of a Sweeping transaction
>
> The Competition and Markets Authority (CMA) have outlined the key features that a payment must have for it to be classified as a sweeping VRP.
>
> 1. The source account needs to be a personal current account (PCA) or business current account (BCA).
> 2. The destination account is an account into which a domestic payment can be made by the payer’s bank’s direct channel.
> 3. Both accounts are UK sterling accounts.
> 4. The payment can be an unattended payment, not requiring any interaction by or presence of the PSU at the time of making the payment.
> 5. The transaction is between two accounts belonging to the same person or legal entity.
>
> See [VRP overview](https://modulr.readme.io/docs/vrp-overview) for further details