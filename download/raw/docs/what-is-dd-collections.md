---
updatedAt: 2025-09-05T18:56:10.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Getting started

With the Direct Debit Collection API

## Starting out on Sandbox

To test the Direct Debit Collection API, you will need to get set up in our Sandbox environment. To do this [contact us](https://www.modulrfinance.com/contact).

We will:

* Set you up with a dedicated collection account.
* Make sure your users have permission to access Direct Debits.

Once this has been done you can start to experiment in Sandbox with the Direct Debit collection API, which is detailed [here](https://modulr.readme.io/reference/getmandates).

## Starting out on Production

To onboard you will need to go through an additional process, as the Direct Debit scheme has specific requirements that need to be met. These requirements focus on the way the agreement is made with the payer and there are also different fees that need to be paid to Modulr for these type of payments.

Onboarding steps (after Sandbox steps above):

* You provide the documentation needed for signing off your DD collections experience.
* The documentation gets signed off and you get a BACS Service User Number (SUN).
* We set you up on production with users and accounts.
* We enable your specified account on production to act as the collection account (N.B. this should not be used for any other inbound payments).
* You integrate with our production environment.
* You test & go live.

A Direct Debit collection account, which is just a normal Modulr eMoney account, needs to be connected to a Service User Number, which you will receive once on-boarded to the Direct Debit service. Once this has been connected you will be able to set up mandates with the payers you want to receive payments from. These payments then need to be scheduled and then eventually they will be paid into the collection account - all explained in the next section.