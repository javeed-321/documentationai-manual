Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ModConnect- Quarterly Round Up 2024

<Callout icon="🎄" theme="default">
  ### Top picks this month

  * Onboarding | Onfido ID verification for shareholders
  * Compliance updates
    * APP Fraud
    * Safeguarding
    * Partner MI Updates
</Callout>

![](https://files.readme.io/27ccd4f0302cde6d7c04180920c038f44f71c684e5c387df4435993885a810e3-image.png)

# Upcoming Change

## Onboarding | Changes to Modulr Portal application forms

We have improved our application forms for businesses wishing to open a Modulr account. We have added the following data points: Trading Name, Date of Incorporation, Website URL and Description of Business Activities.

**What Does This Mean?**

When completing the new application form, you will see these additional fields in the ‘Business Information’ section. Completing these fields will help us verify your business so that we can open your account.

Going forward, the ‘Description of Business Activities’ field will be mandatory. The ‘Date of Incorporation’ will be pre-populated for most Limited Companies. However, Sole Traders/Proprietorships & non-registered Partnerships will need to provide incorporation dates manually. [We have updated our Information we ask for at sign up guidance article to reflect these changes.](https://knowledge.modulrfinance.com/knowledge-hub/information-we-ask-for-at-signup?__hstc=246196251.3e25a6eb0a6f39f0cd43fbc2d47b15ef.1731936509630.1732193338201.1732532099465.5&__hssc=246196251.1.1732532099465&__hsfp=3343512732)

[Watch this short demo](https://2270724.fs1.hubspotusercontent-na1.net/hubfs/2270724/Onboarding/Application%20Form%20Update.mp4) to see what has changed.

**Who Does This Impact?**

This update impacts our Partners using the Modulr Portal to onboard their introduced clients.

Partners using our API integration to onboard customers will NOT be impacted by these changes. The CreateCustomer API will be updated in the future.

## Onboarding | Onfido ID verification for shareholders

**Onfido ID verification for shareholders**

We will now request identity and proof of address documentation if required as part of the customer application process on Modulr Portal. This means customer applications can be processed more quickly.

**What Does This Mean?**

Before this update, we requested applicants provide significant Shareholder names, dates of birth and home addresses as part of the application process. Where this was found to be insufficient to verify an individual’s identity, we had to request proof of identity and proof of address from you post-application.

Our latest integration with Onfido will still ask for the same names, dates of birth and home addresses, but where this verification check fails, we will now ask for documentation to be uploaded as part of the application.

The document upload can be completed in the application form by the applicant but if they don’t have the documentation, they can copy and share a personal link to each individual requiring verification, allowing them to upload the documentation via their own device.

[Please see our guide](https://knowledge.modulrfinance.com/knowledge-hub/id-verification-for-shareholders) on how our Onfido integration works.

Alternatively you can watch[ this demo](https://2270724.fs1.hubspotusercontent-na1.net/hubfs/2270724/Onboarding/Onfido%20Integration%20Demo.mp4) explaining the new way to verify Ultimate Beneficial Owners / Shareholders.

**Who Does This Impact?**

This update impacts our Partners using the Modulr portal whereby Modulr’s Compliance team complete CDD checks for their introduced clients only.

Partners not within the group mentioned above will see no change in the Ultimate Beneficial Owners section.

API integration Partners will not have access to this integration.

![](https://files.readme.io/8949a3d7ba53d82ed0f37ab56470e13fe30fabfe92714bef6762ecb435a979c5-image.png)

# Compliance Update

We are introducing a regular communication on compliance related updates in addition to product updates.

This will include:

* letting you know about regulatory changes and industry news that may be of interest.
* providing relevant updates on Modulr’s business.
* giving you visibility of upcoming changes or requests that may impact you.

Please do share this newsletter internally, and if there are other members of your organisation who would like to receive it in future, please let your Oversight analyst or our Support team know (<support@modulrfinance.com>).

In this first issue we'll be discussing: APP fraud, updates to our safeguarding policy, and changes to the MI we collect from our Partners.

## APP fraud

Since the introduction of the new Mandatory Reimbursement model for APP scams, we are pleased to say we have not seen a material increase in fraud in the Modulr ecosystem; in fact we continue to drive down fraud rates as we embed and refine new processes and procedures.

The FCA’s Dear CEO letter last month sets out their expectations on Authorised Push Payment Fraud Reimbursement. The full letter can be found here. Alongside emphasising the need for firms to maintain effective governance and controls to prevent APP fraud, the FCA have set out some key expectations for how customer impacts should be managed appropriately:

Firms must avoid causing foreseeable harm. An example of foreseeable harm would include a consumer becoming victim to a scam relating to a firm’s financial products due to the firm’s inadequate systems to detect and prevent scams, or inadequate processes to design, test, tailor and monitor the effectiveness of scam warning messages presented to customers.

If a firm identifies that it has caused customers harm, either through its action or inaction, the firm must act in good faith by taking appropriate action to rectify the situation. This includes considering whether remedial action, such as redress, is appropriate. Firms should ensure their customers are adequately supported throughout the lifecycle of a product or service after the point of sale – in particular, if they want to make a complaint.

Firms should provide information about the availability of alternative dispute resolution procedures for payment service users and how to access them as part of their pre-contractual information. This includes informing eligible customers about the availability of the Financial Ombudsman Service.

Firms should ensure their approach to ‘on us’ APP fraud payments (where both sending and receiving payment accounts are held within the same firm or group) meets obligations under Consumer Duty. If any firm intends to provide a lower level of protection to ‘on us’ APP fraud reimbursement compared to payments made through FPS and CHAPS, the FCA requests that they are contacted and provided with an explanation of the steps being taken to meet those obligations.

Firms should review and adjust their business models and transactions to mitigate against any risk of prudential impact that may result for potential APP fraud reimbursement liabilities.

We recommend that all our customers with access to UK payments should review their own processes and capabilities against these expectations and attest to their compliance at a board level.

In addition to this, please do ensure you are using our Fraud Case Management System to interact with us on your fraud cases. You can find a demo video here. Your relevant team members will have received a log-in link for this, but should you encounter any issues or have any questions, please get in touch with <compliance@modulrfinance.com>.

## Safeguarding

At Modulr we are proud of our rigorous safeguarding approach and it is important that our customers understand the ways in which we keep their money safe. As such we have updated our safeguarding documentation to reflect some upcoming diversification in the way we do so in the UK. [The updated documentation can be found here.](https://www.modulrfinance.com/uk-safeguarding-information) Partners should link to this updated documentation in their website footer to ensure the information is clearly available to our introduced customers.

## Partner MI Updates

We have completed a periodic review of our Management Information (MI) template that our customers complete and will be rolling out some changes in the format and content in early 2025.

Some of the information being requested has been revised to reflect industry changes (such as APP fraud) and we have refined the wording of some questions to improve clarity for the response.  The new template is also designed to automatically calculate some responses currently entered manually to improve accuracy.

We will be sharing the new template with our partners in advance of implementation so they can familiarise themselves with the new format and adapt any existing processes ahead of going live.