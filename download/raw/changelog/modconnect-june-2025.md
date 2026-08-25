Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ModConnect June 2025

<Callout icon="🌅" theme="default">
  ### Top picks this month

  * Open Banking V4 is live
  * SEPA Verification of Payee coming by October 2025
  * New corporate fraud law takes effect 1 September 2025
</Callout>

![](https://files.readme.io/bfa47e2f8bd741f311dc875bfd8bc63d6af500d13cff430717e7ea0e56a7430f-image.png)

# New this month

## Updates to V4 Open Banking API

In June 2024, the Open Banking Implementation Entity released **Version 4 of the Open Banking API standards**, with a mandate for CMA9 banks to begin migration. As the ecosystem evolves, we want to keep you informed about what this means for your integration with Modulr Payment Initiation Services.

✅ **What’s changing?**

While the technical updates in Open Banking V4 **do not impact existing Modulr client integrations**, there are a few key enhancements worth noting for future:

* **Improved Payment Statuses:** V4 introduces **more granular payment statuses**, offering better visibility into the lifecycle of a payment. While not mandatory, we recommend adopting these new codes to enhance your payment tracking and reconciliation processes.
* Updates apply to both **single immediate payments** and **fixed recurring payments (standing orders).** Some older status codes are being deprecated, and new ones are being introduced with clearer descriptions.
* **New Payment Context Codes** (non mandatory fields): new codes that you are able to adopt as an option.

**🚀 HSBC first to deprecate Open Banking V3**

We’re pleased to share that **HSBC** is the first bank to remove V3 support for its Personal, Business & First Direct brands. This means it is now supporting Open Banking V4 requests only, returning additional payment status where applicable.  Other ASPSPs expected to follow, the next being Lloyds Bank with an expected November date.

🔄 **Backward compatibility**

There is **no confirmed deprecation date** for V3.1 long lived consents at this time. However, several ASPSPs (e.g. HSBC) have indicated that **existing V3.1 consents will remain valid under V4.** This means you can continue to use your existing consents without disrupting the current experience.

You can find further information of the new payment status codes in our updated documentation [Open Banking V4 API Transition Guide.](https://modulr.readme.io/docs/open-banking-v4-api-transition)

## More banks now supported for PIS 🎉

We’ve expanded our Payment Initiation Service (PIS) coverage by onboarding more banks - making it even easier for you to allow your users to initiate payments directly from their accounts.

The following banks are now supported and will appear as enabled under PIS:

Allied Irish Bank Business

Bank of Scotland EU (Commercial)

Bank of Scotland UK (Commercial)

Barclaycard

Barclaycard Commercial Payments

Barclays Wealth

Chase UK

Chelsea Building Society

Cumberland Building Society

Tesco Bank

Ulster Bank Bankline (NI)

Zempler Bank (formerly Cashplus)

We’re continuing to work through the remaining banks and will keep you posted as more go live.

👉 For more on how PIS works, check out our[ PISP documentation.](https://modulr.readme.io/docs/pisp)

📄 For the full list of supported banks, please see [Supported ASPSP (Banks).](https://modulr.readme.io/docs/supported-banks-and-aspsps)

# Upcoming change

## 🔍 Coming soon - Verification of Payee (VoP) for SEPA payments

With the EU’s Verification of Payee planned deadline for Euro area financial institutions to participate by **9 October 2025**, we’re building the tools to help you stay compliant.

🧭 **What’s driving this?**\
The EU’s Instant Payments Regulation (IPR) brings in a number of changes designed to drive the adoption of SEPA payments by consumers, businesses & financial institutions. A key change is the mandatory introduction of an account name checking service (VoP) for all Euro area financial institutions; a notable difference to other schemes is that it requires a name check on **every payment**, not just the first time a beneficiary is set up.

**There will be no additional charge for partners and clients** - in line with regulatory requirements, the name check does not incur any further cost to the end user (PSU).

🛠️ **What is Modulr doing?**\
We’re implementing our VoP service to support SEPA Payments with delivery expected in line with current industry timelines. Here’s what to expect:

Incoming payments to a Euro denominated account: Modulr will provide a VoP service that can confirm account name to any paying bank — no action needed from partners and clients to enable.

Outgoing payments to a Euro-area account: Modulr will provide a specific VoP API for name checks you can use before initiating a payment. This will be a non-breaking additional API endpoint, separate from the existing payment API.

For incoming and outgoing payments to/from a Modulr Euro account, VoP will be included as part of your existing service charges.

**🛠️ How does the request API work?**&#x4D;odulr partners and clients will be able to integrate this new API into their own customer journeys. We’ve made draft API documentation available [EU Verification of Payee (VoP) ](https://modulr.readme.io/docs/eu-verification-of-payee-vop) - for any check, a simple set of results are returned:

✅ Match

❌ No Match

🤔 Close Match - in this case the actual name on the account will also be returned

⚠️ Check not possible

Your payer should be informed of the result, and given opportunity to choose not to proceed with the payment.

**🧪 What do I need to do?**

The **industry** timeline for the VoP network is reliant on key infrastructure that will launch **5th October**. It is not expected that VoP check changes will be able to be made before this date.

To aid our customers in planning, Modulr will make available further documentation and sandbox services over the coming weeks. We ask that you:

* Review the draft [Verification of Payee (VoP) ](https://modulr.readme.io/docs/eu-verification-of-payee-vop) API documentation and plan your roadmap to deliver changes for the October deadline.
* **Prepare** for **Modulr VoP sandbox access**. Expected **mid Q3**, this will allow you to build your integration with a simulated set of responses to requests.
* **Plan** for launch of your revised user experience by **9 October 2025**when the industry launches the VoP infrastructure.

If you have further specific questions about VoP, please reach out to your client service manager.

![](https://files.readme.io/8949a3d7ba53d82ed0f37ab56470e13fe30fabfe92714bef6762ecb435a979c5-image.png)

## New Corporate Fraud Law: What You Need to Know Before 1 September 2025

From 1 September 2025, a major change in UK corporate law will come into effect: the “Failure to Prevent Fraud” offence, introduced under the Economic Crime and Corporate Transparency Act 2023 (ECCTA).

⚖️ **What’s Changing?**

Large organisations will be criminally liable if an employee, agent, subsidiary, or other “associated person” commits fraud for the organisation’s benefit—even if senior leadership was unaware of the wrongdoing.

This is a strict liability offence, meaning intent or knowledge is not required for prosecution. The only defence is being able to demonstrate that your organisation had reasonable fraud prevention procedures in place at the time.

🏢 **Who’s Affected?**

This applies to “large organisations”, defined as those meeting two or more of the following:

* More than 250 employees
* Annual turnover over £36 million
* Balance sheet total over £18 million

It also applies to UK and overseas companies that carry on business in the UK.

🤝 **Who Counts as an “Associated Person”?**

This includes:

* Employees
* Agents (such as consultants, intermediaries, or sales reps, **Modulr’s Partner clients could be considered agents of Modulr)**
* Subsidiaries
* Anyone performing services for or on behalf of the organisation

❗ **Why It Matters**

This offence is designed to shift the burden from investigating fraud after the fact to preventing it proactively. It’s a wake-up call for organisations to review their internal controls, training, and governance structures.

**✅ What Should You Do to Prepare?**

The government’s guidance outlines six principles for “reasonable procedures”: top-level commitment, risk assessment, proportionate procedures, due diligence, communication and training, and monitoring and review.

1. Conduct a fraud risk assessment to identify where your organisation is most vulnerable.
2. Review and update internal policies to ensure they reflect the new legal requirements.
3. Implement proportionate prevention procedures tailored to your size, sector, and risk profile.
4. Train your people, especially those in high-risk roles or with decision-making authority.
5. Monitor and review your controls regularly to ensure they remain effective.

## Compliance in the News: Worldline

🕵️‍♀️ **What Happened?**

A collaborative investigation by 21 European media outlets alleged that Worldline knowingly processed payments for high-risk clients involved in fraudulent activity.

**📉 Financial Impact**\
Following the publication of these reports, Worldline’s share price plummeted by over 40%, wiping out billions in market value in just one day. This has raised concerns about the company’s financial stability

**🧾 Worldline’s Response**\
Worldline has publicly reaffirmed its commitment to compliance, noting that it has:

* Strengthened its merchant risk framework since 2023
* Terminated relationships with non-compliant clients
* Invested in fraud prevention and financial crime compliance

**⚠️ Why It Matters**\
This situation is a stark reminder of how quickly reputational and regulatory risks can translate into financial consequences. For organisations operating in or adjacent to the payments space, the Worldline case highlights the need for:

* Robust due diligence on clients and partners
* Transparent governance and escalation procedures
* Proactive fraud detection and AML controls

🧭 Action Points

* **Modulr has assessed our own exposure to Worldline or its subsidiaries and not identified any connections.** We strongly encourage our partners to **review their own exposure** to Worldline or any of its affiliates.
* Partners operating in similar sectors should be aware of the **potential for high-risk customers to attempt to migrate** from Worldline to other providers. Enhanced onboarding scrutiny and risk assessments are advised.

<br />

# Billing Updates

## Annual Audit & Compliance Fee Invoicing Change (Outsourced KYB / KYC Partners Only)

From the 1st July 2025 we are changing the way that we invoice the annual Audit & Compliance fee for Partners who have CDD responsibility for their Introduced Customers.

Previously this fee was invoiced retrospectively once an audit had been completed. **The annual fee will now be invoiced during the month of anniversary of the contract commencement date.** This will make the process clearer and more streamlined for Partners.

If you have any questions or require any further information on this change then please reach out to your Account Manager.