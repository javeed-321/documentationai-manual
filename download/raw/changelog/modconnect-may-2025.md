Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ModConnect May 2025

<Callout icon="🌻" theme="default">
  ### Top picks this month

  * Extended Customer Search Capabilities
  * Direct Debit Collections - Payer Name Verification
  * Compliance and Regulatory updates
</Callout>

![](https://files.readme.io/27ccd4f0302cde6d7c04180920c038f44f71c684e5c387df4435993885a810e3-image.png)

# New this month

## Extended Customer Search Capabilities

Following our recent update to the Customers View in last month’s Modconnect, we’ve now reintroduced the ability to search by **Customer ID** and **External Reference**!

To search by these new parameters, navigate to the Customers tab, select your preferred option from the dropdown next to the search bar above your Customers table, enter the value and hit the Enter key.

![](https://files.readme.io/7f8905aa83e28cbe4fe96c7d67d85e8d9d41b9ef5b1328d824c4035f97bf4092-image.png)

## Direct Debit Collections - Payer Name Verification

From 1st June, Payer Name Verification is available as a new endpoint for Direct Debit Collections customers.

Payer Name Verification is a service closely related to and based on the UK Confirmation of Payee system.  It is available to any Direct Debit Collections client to be used when capturing a Direct Debit Instruction (Mandate) from a payer to establish a link between the Payer and the bank account provided. The [payer name check API](https://modulr.readme.io/reference/createoutboundcheckforpnv) provides a match or alternative no-match/close match/mismatch indicators that should be integrated into your Direct Debit Instruction capture Customer Experience (CX).

![](https://files.readme.io/7eb0405761eb36211b2eab28217ce16d830b509dad8c0999b475a964c054a4b9-image.png)

*An example DDI Capture screen incorporating Payer Name Verification.*

It is recommended that all Direct Debit Collections clients adopt Payer Name Verification as part of your DDI signup customer experience. Payer Name Verification is a key tool in minimising the risk of Direct Debit fraud, helping prevent any future Direct Debit Indemnity Claims (DDIC) against you.

For existing clients, a contract amendment needs to be completed via your account manager. New CX guidance is available from the implementation team who will complete the Modulr (Sponsoring PSP) approval of new flows (as required for CX changes under Direct Debit scheme rules).

Payer Name Verification must **only** be used with the sole intention of creating a Direct Debit Instruction for future Direct Debits to be collected into a Modulr account. The use of the service for any other purpose is forbidden and is a violation of the terms and conditions of the service. Usage of the service in relation to volumes of Direct Debit Instructions is actively monitored by Modulr & the scheme.

![](https://files.readme.io/8949a3d7ba53d82ed0f37ab56470e13fe30fabfe92714bef6762ecb435a979c5-image.png)

# Compliance and Regulatory Updates

## 📊 UK Finance Annual Fraud Report 2025 – Key Insights

Published by UK Finance, the[ 2025 Annual Fraud Report ](https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/annual-fraud-report-2025)offers a detailed analysis of fraud trends across the UK financial sector, highlighting the evolving threat landscape and the industry’s coordinated response to protect consumers and businesses.

Modulr continually reviews and enhances its fraud controls to help protect customers, working closely with our Partners to monitor risks and implement improvements. If you have any questions about the themes in this article, please reach out to your Oversight Analyst.

### 💷 Total Fraud Losses and Trends

* Total fraud losses across authorised and unauthorised fraud reached £1.17 billion in 2024.
* This figure is broadly similar to 2023 but spread across 12% more cases (3.31 million cases).
* £1.2 billion in fraud was prevented—equivalent to 61p in every £1 of attempted fraud.

### 💸 Authorised Push Payment (APP) Fraud

* APP fraud losses totalled £459.7 million. Both the total value and number of APP fraud cases declined from the previous year but there was a noticeable shift toward higher-value scams, particularly investment fraud.
* 76% of APP fraud cases originated online.
* Investment scams were the highest-value type; purchase scams were the most common by volume.

### 🔐 Unauthorised Fraud

* Remote banking fraud cases fell by 17%, and losses dropped by 7% with fraud prevention increasing by 14%, reaching £250 million.
* Card fraud accounted for £556.3 million in losses. Reversing a 3 year trend card fraud increased by 15% in case volume driven by a 22% increase in remote purchase fraud

### 🔄 Evolving Threats and Industry Response

While the report shows good progress in some aspects of the fight against fraud the report shows how fraudsters preferred methodologies shift as the industry focuses it’s attention on certain aspects of prevention, emphasising the need for constant review and iteration of anti-fraud strategies and industry collaboration.

## 🚨 Emerging Threat: Scattered Spider Targets UK Businesses

A recent cyber-attack on Marks & Spencer (M\&S) has highlighted the growing threat posed by a cybercriminal group known as Scattered Spider. This group is known for its sophisticated use of social engineering—tricking employees rather than exploiting software flaws—to gain access to corporate systems.

### 🕵️‍♂️ What Happened?

On 22 April 2025, Scattered Spider used stolen credentials to infiltrate M\&S’s internal network. They exfiltrated sensitive password data and deployed DragonForce ransomware, disrupting virtual infrastructure and causing widespread outages. The attack forced M\&S to suspend online orders, disrupted in-store payments, and led to a 7% drop in share price—wiping out nearly £700 million in market value.

### ⚠️ Why It Matters to Your Business

Scattered Spider is actively targeting large organisations in the UK and other English-speaking regions. Their tactics include:

* Phishing and voice phishing (vishing)
* SIM swapping
* Exploiting weak or outdated multi-factor authentication (MFA)
* Targeting virtualised infrastructure like VMware ESXi

They are financially motivated and often act as affiliates for ransomware-as-a-service (RaaS) operations, making them both agile and dangerous.

### ✅ What You Can Do

To reduce your organisation’s exposure:

* **Train employees** regularly on phishing and social engineering threats.
* **Implement phishing-resistant MFA** (e.g. FIDO2/WebAuthn) to prevent credential theft.
* **Segment your network** to limit lateral movement if a breach occurs.
* **Patch and harden infrastructure**, especially virtualisation platforms.
* **Monitor for Indicators of Compromise (IoCs)** and integrate threat intelligence into your detection systems.
* **Run table top exercises** to test your: incident management and communications, internal/external data breach response procedures, and recovery plans

The report from CGI, attached to the ModConnect email, contains technical details on attack identifiers and IoCs. **Please share with your Cyber Security leads** but note restrictions on public dissemination.