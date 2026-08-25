---
updatedAt: 2025-09-05T18:47:21.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# EU Verification of Payee (VoP)

Information about the VoP service being launched by EU PSPs in October 2025

Verification of Payee is a Europe wide account name checking service [designed by the European Payments Council (EPC) ](https://www.europeanpaymentscouncil.eu/what-we-do/other-schemes/verification-payee)and intended to go live on 5th October ahead of the requirement for PSPs to provide a service under the[ EU Instant Payments Regulation (IPR) ](https://www.ecb.europa.eu/paym/integration/retail/instant_payments/html/instant_payments_regulation.en.html) in line with deadlines.

| Euro-area PSPs                                                                                                        | Non-euro area PSPs                                                                 |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Euro-area PSPs must provide a beneficiary-verification service where they are the payer’s PSP by **9th October 2025** | PSPs located in a Member State whose currency is not the euro by **9th July 2027** |

You will have received communications from Modulr if you are a partner **required** to implement VoP as part of your SEPA payment service usage and will need to implement ahead of the IPR deadline.

For all other types of customers, usage is optional but recommended in your Customer Experience (CX) where SEPA payments are input/approved to help prevent error & misdirected payments.

The VoP service helps ensure payments are sent to the correct recipient by checking the name and account details (IBAN) of the payee match, to be used in your CX before a SEPA payment is made. The VoP service can be used for personal and business SEPA accounts with a valid IBAN, there is no distinction of account type required as part of the check.

### Note on coverage:

It is highly likely that not all Euro area European PSPs will have services available on the 9th October date, and will phase in services across the period following; if a check is made against a PSPs in SEPA area that does not support a 'Check not possible' message will be returned.  A check against a non-Euro area PSP will similarly return a 'Check not possible' message. 'Check not possible'  should **not** be interpreted to prevent execution of the payment in normal circumstances, see guidance below on informing the payer.

### Informing users of the name check & providing advice before proceeding with payment

The VoP service is intended to help Payers make an informed choice about continuing making the payment, and potential risks (with balance). To help guide the payer, we strongly recommend:

#### Making it visually clear to the Payer the state of the check

<Image align="center" src="https://files.readme.io/470b2af5b66beed7dcf4f45214914450e408751747876328d68e37b9b4156992-image.png" />

Use visually distinctive elements such as colour, icons or ‘traffic lights’ to distinguish the types of match that VoP returns and the action a requestor may need to take.

#### Where it’s a close match give the requestor opportunity to correct/proceed

<Image align="center" src="https://files.readme.io/cafb5858d5fcdf9ab3b8ab5d22057db79f3bce4e8b4d88d3e46f9ad124551a28-image.png" />

Use the account name returned in the close match scenario giving the requestor the opportunity to proceed, cancel or go back and correct the name

#### Be clear on the risks of proceeding but **be balanced**

<Image align="center" src="https://files.readme.io/e04c464c7dbc68722e63bde0a3684c43434a4cdb101a7ae9756be614f42524cc-image.png" />

Inform the requestor that proceeding with any non-match carries some risk of paying an unintended recipient; but be balanced to not overstate or dissuade from making valid payments.

#### Don'ts

* Don’t use heavy verbiage such as ‘fraud’ or ‘scam’ that may scare the customer
* Don’t use banking or VOP specific technical jargon ‘VOP’, ‘Payee’, ‘Payer’, ‘Authorise’, 'PSP', 'Responder' etc.
* Don’t include excessive verbiage around liability or legal terms
* Don’t include verbiage implying that the Account Details (rather than the name) entered by the user are incorrect

### For sandbox access:

Ensure you are registered with the Modulr Sandbox; see notes on sandbox test data in [Sending verification of payee checks](https://modulr.readme.io/docs/sending-vop-check-requests)

***

## VoP Request (Sending VoP requests to other PSPs)

A new [API endpoint](https://modulr.readme.io/reference/createoutboundvop) is available in line with the industry timeline that enables a Partner or Client to perform a check on a beneficiary ahead of making payment. Please see [Sending verification of payee checks](https://modulr.readme.io/docs/sending-vop-check-requests) for details of the API usage & sandbox test cases.

## VoP Respond (Respond to incoming VoP requests from other PSPs)

Modulr will enable Verification of Payee checks by other PSPs on or ahead of the Euro-area deadline. This will be for any € denominated account on its European BICs. No action is required from a Modulr partner or client to enable; all accounts will be included as there is no 'opt-out' in VoP.