---
updatedAt: 2026-07-14T18:53:50.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Escheatments

<Callout icon="📘" theme="info">
  ### What is Escheatment?

  Escheatment is the process by which unclaimed assets are turned over to a state.  When property reaches the end of a dormancy period (established by each state) with no owner contact, then—by law—the organization must identify and report the unclaimed property.

  Organizations must make a good-faith effort to reach the owner of the property before turning it over to the state for safekeeping. Attempts may be made by letter, phone call, electronic communication, or other methods.

  If no contact with the owner has been made, the organization must prepare and submit an unclaimed property report to the state. Most states require the reporter to follow the National Association of Unclaimed Property Administrators (NAUPA) standard format and specifications. NAUPA’s website is extensive and provides comprehensive assistance with the process:  [https://unclaimed.org/state-reporting/](https://unclaimed.org/state-reporting/)

  The SEC recognizes the NAUPA and also provides guidance about escheatment for shareholders: [https://www.sec.gov/oiea/investor-alerts-and-bulletins/ib\_escheatment](https://www.sec.gov/oiea/investor-alerts-and-bulletins/ib_escheatment)
</Callout>

As part of our Escheatment process, DriveWealth reviews all customer accounts to identify those eligible for escheatment, based on account activity and in compliance with the applicable state regulations governing each account.

## Updating Last Activity on Accounts

To prevent accounts from being mistakenly flagged for Escheatment, we **strongly recommend** regularly updating DriveWealth with customer activity data. This ensures our records remain current.
For example, you may choose to send daily or weekly updates whenever a customer logs into your application by updating the `lastActivityDate`, provided this complies with our API rate limits.

All updates must be submitted via API to ensure an efficient review process and to allow for the exclusion of accounts with recent activity.

Please use the [Update Account API](https://developer.drivewealth.com/apis/reference/patch_accounts-accountid) to submit the `lastActivityDate` for account updates.

```javascript JSON
PATCH /back-office/accounts/{accountID}
{
  "lastActivityDate": "2024-07-23"
}
```

<br />

<Callout icon="📘" theme="info">
  ### FAQs

  1. **What counts as account activity?**
     Account activity includes any user engagement, such as wallet transactions within your app, activity on linked bank accounts, or simply logging into the application.

  2. **Is there a rate limit for the Update Accounts API?**
     Yes, the Update Accounts API is limited to 50 requests per second.

  3. **Are international customers subject to the Escheatment process?**<br />No, Escheatment applies only to U.S.-based customers. However, if an international client serves U.S.-based clients, those specific accounts will be included in the Escheatment process.
</Callout>

## What happens to Escheated Accounts?

Once accounts identified for Escheatment have been finalized through analysis, DriveWealth initiates a three-step process:

### **Step 1:** Liquidate Fractional Positions

All fractional share positions held in the account are liquidated. This action triggers [Order events](https://developer.drivewealth.com/apis/reference/orders-events)

### **Step 2:** Transfer Whole Shares and Cash to the Escheatment Account

* **Cash Transfers**
  Cash in the account is withdrawn and moved to a DriveWealth Escheatment account. This generates a `CSD` transaction:

```json

{  
        "accountAmount": -33.2,  
        "accountBalance": 0,  
        "accountType": "LIVE",  
        "comment": "From: CXXX006369 To: DXXX009999",  
        "dnb": false,  
        "finTranID": "MD.b8100b3e-1264-4143-bcb4-44591c613c50",  
        "finTranTypeID": "CSD",  
        "feeSec": 0,  
        "feeTaf": 0,  
        "feeBase": 0,  
        "feeXtraShares": 0,  
        "feeExchange": 0,  
        "fillQty": 0,  
        "fillPx": 0,  
        "sendCommissionToInteliclear": false,  
        "systemAmount": 0,  
        "tranAmount": -33.2,  
        "tranSource": "B",  
        "tranWhen": "2025-04-25T16:52:14.276Z",  
        "wlpAmount": 0,  
        "wlpFinTranTypeID": "f8543b34-8125-4c87-8ade-4f627788a68f"  
    },
```

* **Whole Share Transfers**
  Whole shares are transferred out of the account, resulting in an `XTRF` (External Transfer) transaction:

```json
{
        "accountAmount": 0,
        "accountBalance": 0,
        "accountType": "LIVE",
        "comment": "XTRF Stock Transfer: account=CXXX006369, symbol=APA, qty=-1, px=17.65",
        "dnb": true,
        "finTranID": "MD.6b9ebbdc-7c75-4a47-a277-e26def35b5cc",
        "finTranTypeID": "XTRF",
        "feeSec": 0,
        "feeTaf": 0,
        "feeBase": 0,
        "feeXtraShares": 0,
        "feeExchange": 0,
        "fillQty": -1,
        "fillPx": 17.65,
        "instrument": {
            "id": "50158bb2-5440-468a-99f5-7cb41eb6499e",
            "symbol": "APA",
            "name": "Apache Corp."
        },
        "orderID": "na",
        "orderNo": "na",
        "sendCommissionToInteliclear": false,
        "systemAmount": 0,
        "tranAmount": 0,
        "tranSource": "INTE",
        "tranWhen": "2025-04-28T04:17:23.585Z",
        "wlpAmount": 0,
        "wlpFinTranTypeID": "e2f6e89d-0f5c-4b5c-8764-5403d71a6409"
    }
```

### **Step 3:** Exclude Accounts from Reconciliations (If Applicable)

Eligible accounts are marked for exclusion from reconciliations. This triggers a [Account Exclusion events](https://developer.drivewealth.com/apis/reference/settlements-events#reconciliation-account-exclusions-created)

```json
{
  "id": "event_11eba312-529f-43ea-a8b2-3251637b567e",
  "type": "account.exclusions.created",
  "timestamp": "2024-03-20T08:55:27.096Z",
  "payload": {
    "current": {
      "reason": "ESCHEATMENT",
      "comment": "ESCHEATMENT_EARLY_SPRING_2025"
    },
    "accountID": "8e714a37-ece1-4af2-a2d8-b30dc727e530.1688760093299",
    "accountNo": "DWQU000080",
    "partnerID": "ac5de50f-2297-e2e7-7b31-2c54872ae231"
  }
}
```

<br />

<Callout icon="📘" theme="info">
  ### Additional Resources

  - NAUPA state-by-state at a glance: [https://unclaimed.org/state-reporting/](https://unclaimed.org/state-reporting/)
  - NAUPA webinar “Fundamentals of Unclaimed Property Reporting for Holders” costs $50. To register: [https://member.nast.org/store/ViewProduct.aspx?id=13539990](https://member.nast.org/store/ViewProduct.aspx?id=13539990)
  - NAUPA-approved (free) reporting software can be obtained here:  [https://hrspro.unclaimedproperty.com/](https://hrspro.unclaimedproperty.com/)
  - Due dates by state at-a-glance: [https://sovos.com/blog/trr/unclaimed-property-due-dates-by-state/](https://sovos.com/blog/trr/unclaimed-property-due-dates-by-state/)
  - Sample of Due Diligence Letter (Kentucky): [https://treasury.ky.gov/unclaimedproperty/Documents/Sample%20Due-Diligence%20Letter.pdf](https://treasury.ky.gov/unclaimedproperty/Documents/Sample%20Due-Diligence%20Letter.pdf)
</Callout>

<br />