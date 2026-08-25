Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Your Modulr Product Update October 2025

<br />

<Image align="center" border={false} width="600px" src="https://files.readme.io/c806c32a1e1f8d958d6b133f07bf730184c7487ac2607f302edb83b882f59c4b-image.png" />

<br />

<Image align="center" border={false} width="600px" src="https://files.readme.io/94d46d4d9759b9c94ab6332c0c2bb4725cdd68b2e50c73626d1143f26fe6ceca-image.png" />

# The Modulr Portal

## Verification of Payee - SEPA Payments

We’ve added a new feature when making EUR payments: **Payee name checks.**

**Why this matters**

The EU Instant Payments Regulation now requires us to check payee details before sending EUR payments This helps you catch typos and avoid sending money to the wrong account – protecting you from both fraud and costly mistakes. 

**What's changed**

Payment and payee creation: Name checks happen automatically when you create a EUR payment or add a EUR payee. The results are shown immediately. 

Payment approvals: You'll need to make a selection and click the "Check Payees" button before approving individual or batch EUR payments. 

The name check will indicate whether there is a match, close match, no match or check not possible. It will not block the payment, but gives you the opportunity to review before proceeding.  

We encourage you to review the match carefully before proceeding to reduce any risk of misdirected payments. 

**Need help?** 

We've updated five guides in our User Guides to walk you through the new flow: 

[Creating a payee  ](https://knowledge.modulrfinance.com/knowledge-hub/creating-beneficiaries?utm_source=hs_email\&utm_medium=email&_hsenc=p2ANqtz-8jb1SUaIFaOrx4lwLerGhllZbqVu3lNr4030t21QVgPb6hMx0YoeMQ60neGKXZJl-SvIJf)

[Paying a new payee ](https://knowledge.modulrfinance.com/knowledge-hub/pay-a-new-beneficiary?utm_source=hs_email\&utm_medium=email&_hsenc=p2ANqtz-8jb1SUaIFaOrx4lwLerGhllZbqVu3lNr4030t21QVgPb6hMx0YoeMQ60neGKXZJl-SvIJf)

[Paying a saved payee ](https://knowledge.modulrfinance.com/knowledge-hub/pay-a-saved-beneficiary?utm_source=hs_email\&utm_medium=email&_hsenc=p2ANqtz-8jb1SUaIFaOrx4lwLerGhllZbqVu3lNr4030t21QVgPb6hMx0YoeMQ60neGKXZJl-SvIJf)

[Approving individual payments ](https://knowledge.modulrfinance.com/knowledge-hub/approve-or-reject-a-payment?utm_source=hs_email\&utm_medium=email&_hsenc=p2ANqtz-8jb1SUaIFaOrx4lwLerGhllZbqVu3lNr4030t21QVgPb6hMx0YoeMQ60neGKXZJl-SvIJf)

[Approving batch payments ](https://knowledge.modulrfinance.com/knowledge-hub/approving-or-rejecting-a-batch?utm_source=hs_email\&utm_medium=email&_hsenc=p2ANqtz-8jb1SUaIFaOrx4lwLerGhllZbqVu3lNr4030t21QVgPb6hMx0YoeMQ60neGKXZJl-SvIJf)

<Image align="center" border={false} width="600px" src="https://files.readme.io/6180500c9af673242159c47d94224b4f78c269a5bfc35eb1589999a63c4118fd-image.png" />

# The Modulr Portal and API

## Instant Payment Regulations - changes to SEPA payments

Last month we published our enhancements to the platform in line with the Instant Payments Regulation changes. Now that the changes have come into effect, we wanted to remind you of the introduction of Payee account name checks (called Verification of Payee or VoP in the EU) that are now integrated into SEPA payment flows.

## September update

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