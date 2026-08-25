Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ModConnect-July 2024

<Callout icon="👁️‍🗨️" theme="default">
  ### Top picks this month

  * Onboarding Introduced Clients | EEA Support in Modulr Portal
  * Action Required - Customer Record Keeping
  * DD Collections | Dynamic Service User Name
</Callout>

![](https://files.readme.io/dc869c6-image.png)

# New this month

## DD Collections | Dynamic Service User Name

Upon request, as a Direct Debit Collections customer, we can now assign you an abbreviated Service User name. This will allow you to use the (up to 14) remaining characters in the field to convey other collection information.

This feature simplifies the process of identifying transactions, as the Service User (SU) name is displayed by Payment Service Providers (PSPs) on their main transaction view of a bank account. For clients using familiar or widely acknowledged abbreviations, this enhances the reconciliation process, reduces inquiries, and lowers the risk of indemnity claims arising from unidentified transactions.

An example of this could be abbreviating His Majesty’s Revenue & Customs to HMRC. HMRC can be set as the abbreviated SU name. When creating collection schedules, “ VAT APRIL” associated with a VAT payment could be included using the remaining characters. This would create an SU name of “HMRC VAT APRIL” which will appear on the payer’s main bank statement.

For more information please read: <https://modulr.readme.io/reference/createcollectionschedule>

For any inquiries, please reach out to your customer success manager or customer support.

## Cards | Authorisation Window Deletion

If you are using authorisation windows for cards, you can now delete the authorisation window if it is no longer needed.

For further information please see <https://modulr.readme.io/reference/updatecard>

For any inquiries, please reach out to your customer success manager or customer support.

## Onboarding Introduced Clients | EEA Support in Modulr Portal

We’re thrilled to announce new capabilities in the Modulr portal designed to streamline the onboarding process for introduced clients across the EEA.

Our enhanced application journey features pre-fill capabilities, the option to send applications to clients for completion, and an easy-to-use interface, ensuring faster and more efficient onboarding.

Get in touch with your Client Servicing Manager to get started today!

## Action Required - Customer Record Keeping

We have updated our APIs to enable partners to record the compliance risk rating and vulnerabilities of their customers. This is a key requirement for us to better manage financial crime risks and to provide good outcomes for vulnerable customers.

Specifically we have added two customer attributes to the *complianceData* Object of our New and Edit Customer APIs: risk level, and vulnerability reason. 

Note: In future, we will be adding more customer attributes required for businesses who are Micro-enterprises and to support new EU regulatory reporting requirements.

The actions below do not apply to **regulated partners operating under a Payments Clearing Model (PCM) arrangement.**

### Action Required - Record Customer Risk Ratings:

**Partners who complete CDD for their clients (Outsourced KYB/KYC arrangement):**

Partners, who perform KYP/KYC on their clients, must ensure that all customers have a Risk Rating by the **30th September 2024**.

Updating existing customers - This can be done by utilising our **Edit Customer** endpoint (see `complianceData` object), a `RiskLevel` of LOW, MEDIUM, or HIGH should be provided.

New customers - This can be done by utilising our **Create a New Customer** endpoint - a `RiskLevel` of LOW, MEDIUM, or HIGH must be provided with all new create customer requests (see `complianceData` object).

**Partners where Modulr performs CDD for clients (In-house KYB/KYC arrangement)** have no action to take as Modulr will be performing the necessary actions to capture and maintain risk ratings.

### Action Required - Record Customer Vulnerabilities:

This applies to **all Partners** regardless of the KYB/KYC operating model (excluding Partner’s operating under the Payments Clearing Model).

Partners must inform us of all customers with vulnerabilities on our platform by the **30th September 2024**.

Updating existing customers - This can be done by utilising our **Edit Customer** endpoint (see `complianceData `object) and setting the `vulnerabilityReasons` with one or more indicators:  *LIFE\_EVENTS, HEALTH, RESILIENCE, CAPABILITY, FINANCIAL\_DIFFICULTY*. Note setting vulnerabilityReasons to an empty string will clear any previously recorded vulnerabilities.

New customers - This can be done by utilising our  **Create a New Customer**endpoint -`vulnerabilityReasons` should be provided if applicable (see `complianceData` object) and set to one or many of the following indicators:  *LIFE\_EVENTS, HEALTH, RESILIENCE, CAPABILITY, FINANCIAL\_DIFFICULTY.*

Partners who do not have API capability should inform us of any customer vulnerabilities via our support channel - <support@modulrfinance.com.>

Please get in touch with your Client Servicing Manager if you have any questions.