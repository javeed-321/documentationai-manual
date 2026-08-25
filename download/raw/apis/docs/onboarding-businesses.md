---
updatedAt: 2026-08-24T14:41:42.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Onboarding businesses

This guide is for fully disclosed partners using DriveWealth’s Business Account product to onboard and support corporate/business entities. If your platform only supports individual accounts or you manage customer data independently, you can skip this section.

<br />

A business account is a brokerage account owned by a business entity, such as an LLC or corporation, to hold investments for the business entity. These accounts allow for authorized users to make investments specifically for the business entity and tailored for its investment needs. While a single entity owns the account, the business account structure accommodates multiple beneficial owners of the business entity, who are themselves natural persons.

Business accounts differ from individual accounts in accountholder ownership and information required for compliance and regulatory reasons, including legal entity details, ownership structure, and identification documents.

## Integration path

Your integration path is determined mainly by 2 factors:

### KYB (Know-Your-Business) methods supported:

* **DriveWealth Does KYB (**`DO_KYB`**):** DriveWealth performs KYB checks on new entities (up to 1 week processing time). For KYB approval, DriveWealth requires successful completion of KYC for all directors of the entity, as well as verification of the entity itself.
* **DriveWealth Relies on Partner (**`NO_KYB`**):** DriveWealth relies on the partner’s KYB process, subject to KYB policy and procedure review. The KYB method used depends on your location, licenses, and AML capabilities. Contact your DriveWealth Relationship Manager to discuss the right approach.

### Customer base

* **US Entities Only:** DriveWealth auto-generates W9 forms from entity data.
* **Foreign Entities:** Must provide a valid W8 form via a 3rd party vendor ComplyExchange. You must embed a ComplyExchange white-labeled UI widget for the entity customer to complete the form.

Note that entities cannot begin investing until both KYB verification and W8/W9 validation are complete.

## Key concepts

| Component                   | Description                                                                                       |
| :-------------------------- | :------------------------------------------------------------------------------------------------ |
| Entities API                | Represents the legal business entity                                                              |
| Users API                   | Creates individuals linked to the business (beneficial owner, control person, authorized traders) |
| Documents API               | Uploads legal documents (formation, address proof, etc.)                                          |
| Accounts API                | Creates accounts owned by the business entity                                                     |
| Entities event notification | Receive notification on entities.created and entities.updated events                              |

## Onboarding

### Step 1. Create a business Entity

Collect entity data for onboarding and verification. Field requirements vary by incorporation country.

| Category               | Required | Required Fields                                                                                                                                   |
| :--------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| Entity Type            | ✅        | Type and subtype (US entities require subtype)                                                                                                    |
| Attributes             | ✅        | Name, Incorporation Country, Incorporation Province (US only), Incorporation Date                                                                 |
| Identifications        | ✅        | EIN (US), FTIN/FTNLO (Foreign), GIIN (if applicable)                                                                                              |
| Contact                | ✅        | Business Address (valid physical address in incorporation country), Phone (E164 format), Email, Phone number, Website (optional)                  |
| Disclosures            | ✅        | Customer Agreement, Terms of Use, Privacy Policy, Rule 14b FPSL, Margin Agreement, and other agreement if applicable                              |
| Investment Profile     | :x:      | Optional: Revenue, Net Worth, Investment Objectives, Risk Tolerance, Liquidity Needs, Experience, Time Horizon, transaction volume by asset class |
| Industry               | :x:      | Optional: NAICS if applicable, or other industry classification                                                                                   |
| Financial Affiliations | :x:      | Affiliations with financial institutions or regulated entities, if applicable                                                                     |
| Metadata               | :x:      | Optional custom fields                                                                                                                            |

Create entity sample payload:

```json
POST /entities

{
  "type": "LLC",
  "subType": "LLC_S_CORPORATION",
  "attributes": {
    "name": “Testing Co",
    "dba": "Acme",
    "incorporationCountry": "USA",
    "incorporationProvince": "CA",
    "incorporationDate": "2019-01-01"
  },
  "identifications": {
    "ein": "123456789"
  },
  "contact": {
    "addresses": {
      "primary": {
        "street1": "123 Main Street",
        "city": "San Francisco",
        "province": "CA",
        "zipcode": "94105",
        "country": "USA"
      }
    },
    "phone": "+14050001234",
    "email": "hello@testing.com",
    "website": "www.testing.com"
  },
  "disclosures": {
    "termsOfUse": {
      "agreed": true,
      "signedBy": "name",
      "signedWhen": "2024-09-09T15:20:05Z"
    },
    "customerAgreement": {
      "agreed": true,
      "signedBy": "name",
      "signedWhen": "2024-09-09T15:20:05Z"
    },
    "privacyPolicy": {
      "agreed": true,
      "signedBy": "name",
      "signedWhen": "2024-09-09T15:20:05Z"
    },
    "rule14b": {
      "agreed": true,
      "signedBy": "name",
      "signedWhen": "2024-09-09T15:20:05Z"
    }
  },
  "investment_profile": {
    "annualRevenue": 100000000,
    "netWorthTotal": 10000000000,
    "investmentObjectives": "GROWTH",
    "riskTolerance": "MODERATE",
    "liquidityNeeds": "SHORT_TERM",
    "investmentExperience": "YRS_3_5",
    "timeHorizon": "MODERATE_TERM"
  },
  "financialAffiliations":[
	  "Bank of America"
  ],
  "metadata": {
    "myCustomKey": "myCustomValue"
  }
}

```

If you subscribe to the `entities.created` event, you should receive a notification when the entity is successfully created. Please refer to [Entity events](https://developer.drivewealth.com/apis/reference/entity-events) for payload details.

### Step 2. Upload business documents

DriveWealth requires proof of business registration and address. The entity must provide at least one document that shows entity formation and one document that shows business registration. There are multiple types of documents that can show each.  For example, entity formation could be articles of incorporation, an LLC agreement, a partnership agreement etc depending on the entity type.  Business registration documentation will vary by jurisdiction. Acceptable documents include:

* **Entity Formation:** Articles/Certificate of Incorporation, Certificate of Formation (LLCs), Partnership Agreement
* **Business Registration/License:** Government-issued registration certificates, trade licenses
* **Tax ID Proof:** IRS Form SS-4 / EIN Confirmation Letter (US), equivalent foreign tax registration
* **Proof of Address:** Recent utility bill, lease agreement, or bank statement in entity’s name

**Best practices:**

1. Ensure business names provided in account application match with legal documentation
2. Use high-quality document scans—blurry or incomplete uploads can delay KYB processing.
3. Customers should combine all pages of each required business document into a single, multi-page PDF file before uploading. Do not split one document into multiple files.

**Upload Document API example:**

```json
POST /documents

{
  "userID": "{{entityID}}",
  "type": "BUSINESS_DOCUMENT",
  "document": "data:image/png;base64,iVBORw0KGgoAAAANSUh..."
}
```

### Step 3. Add Beneficial Owners & Control Person

The business entity must provide the following individuals for regulatory and compliance purposes:

* **Control Person:** A designated individual with significant authority to manage, control, or direct the entity’s operations (e.g., CEO, Managing Director). Exactly one control person is required.
* **Beneficial Owners:** Any individual who owns more than 10% of the entity, directly or indirectly. Multiple beneficial owners may be provided if applicable. Beneficial owners must be natural persons.

Create Control Person and Beneficial Owner as individuals using the Users API, and link to the Entity using the `DIRECTOR_INFO` section. Required information includes:

* Standard KYC information: name, DOB, citizenship, ID number, address, and Photo ID (If Required)
* Director related information: role (control person or beneficial owner or both)

**API Example:**

```json
POST /users

{
   "username": "test.controlperson",
   "password": "passw0rd",
   "userType": "INDIVIDUAL_TRADER",
   "documents": [
       {
           "type": "BASIC_INFO",
           "data": {
               "firstName": "control",
               "lastName": "person",
               "country": "USA",
               "phone": "2912341122",
               "emailAddress": "b@b.com",
               "language": "en_US"
           }
       },
       {
           "type": "IDENTIFICATION_INFO",
           "data": {
               "value": "123456789",
               "type": "SSN",
               "citizenship": "USA"
           }
       },
       {
           "type": "PERSONAL_INFO",
           "data": {
               "birthDay": 3,
               "birthMonth": 12,
               "birthYear": 1990
           }
       },
       {
           "type": "ADDRESS_INFO",
           "data": {
               "street1": "123 Main St",
               "city": "Chatham",
               "province": "NJ",
               "postalCode": "09812"
           }
       },
       {
           "type": "DIRECTOR_INFO",
           "data": {
               "directorList": [
                   {
                       "title": "Chief Innovation Officer",
                       "roles": [
                           "CONTROL_PERSON",
					 “BENEFICIAL_OWNER”
                       ],
                       "controlContact": true,
                       "institutionalID": "{{entityid}}"
                   }
               ]
           }
       }
   ]
}

```

### Step 4. Create Authorized Traders

Every business account must identify at least one authorized user associated with it. An authorized user can be a Control Person, Ultimate Beneficial Owner, or other additional personnel designated by the company. If there are additional personnel who will act on behalf of the company—beyond the Control Person or UBO—they must be created in the system as individual users, providing all required personal information (e.g., name, date of birth, contact details, and identification). This ensures that all individuals with authority to operate or manage the business account are properly identified. You can use [users API ](https://developer.drivewealth.com/apis/reference/post_users)to create additional authorized users.

### Step 5. Open Business Account

Create business account under the business entity using one of the 3 supported Business Account Management Types:

|                        |                                              |
| :--------------------- | :------------------------------------------- |
| `BUSINESS_SELF`        | Business entity trades on its own behalf     |
| `BUSINESS_RIA_MANAGED` | Registered Investment Advisor manages orders |
| `BUSINESS_ADVISORY`    | Business entity trades with advisory support |

Business accounts must assign at least one authorized user covering the current and future period. You should also provide the authorized user's userID as traderID when placing orders via the [Orders API](https://developer.drivewealth.com/apis/reference/post_orders).

**Create Business Account API Example:**

```json
POST /accounts

{
  "userID": "{{entityID}}",
  "accountType": "LIVE",
  "accountManagementType": "BUSINESS_SELF",
  "tradingType": "cash",
  "interestedParties": [
    {
      "type": "AUTHORIZED_USER",
      "data": [
        {
          "id": "{{controlPersonID}}",
          "reportingRole": "AUTHREP",
          "tradeDiscretion": true,
          "from": "2024-12-01T00:00:00Z"
        }
      ]
    }
  ]
}

```

### Step 6. Foreign Entities: W-8 Form Completion

<Callout icon="🚧" theme="warn">
  Applicable for foreign entities only. US entities can skip this step as W9 forms are auto-generated by DriveWealth.
</Callout>

Foreign entities are required to complete the appropriate W-8 forms through a third-party platform, ComplyExchange. DriveWealth will generate a unique ComplyExchange URL for each entity with certain identification details prefilled. You may either share this URL directly with the entity customer or embed ComplyExchange’s UI within your application to facilitate form completion. An authorized signer from the entity must complete the remaining sections of the form, including critical tax-related information such as Chapter 3 and Chapter 4 status codes.

ComplyExchange offers step-by-step guidance and helpful tools to assist the entity in accurately completing the form. Below is a sample of the ComplyExchange UI. The interface can be customized to align with your branding.

<Image src="https://files.readme.io/e360a48e7657ac6365928df08eed0c3cb0ba970f7799c80ba94f6f109d92349c-Screenshot_2025-10-24_at_11.02.08_AM.png" align="center" />

DriveWealth will generate a ComplyExchange URL only after receiving account creation requests. You can use the [Retrieve Entity](https://developer.drivewealth.com/apis/reference/get_entities-entityid) API to view the Entity’s ComplyExchange URL. Alternatively, you will also receive an `entities.updated` notification if you subscribe to the event.

**Example API response snippet:**

```json
"taxData": {
  "fatcaData": {
    "applicable": true,
    "applicableFrom": "2025-08-26T19:49:58Z",
    "setBy": "SYSTEM"
  },
  "vendor": {
    "COMPLY_EXCHANGE": {
      "name": "Comply Exchange",
      "taxFormUrl": "https://drivewealth.complytaxforms.com/ServiceRedirect.aspx?UUID=xxx&Language=US",
      "formUrlDate": "2025-08-26T19:50:20Z"
    }
  }
}

```

## Entity verification

### `DO_KYB` mode

In `DO_KYB` mode, DriveWealth is responsible for performing KYB checks after receiving business account opening requests.

The KYB object in the [Retrieve Entity](https://developer.drivewealth.com/apis/reference/get_entities-entityid) API is helpful for you to understand the current KYB status and remediation required. You can use [Retrieve Entity](https://developer.drivewealth.com/apis/reference/get_entities-entityid) to view entity’s current KYB status at any given time, or you would receive `entities.updated` notifications if you subscribe to the event to receive real-time KYB updates.

**Example API response snippet:**

```json
"kyb": {
  "status": "KYB_DOC_REQUIRED",
  "statusWhen": "2025-10-06T21:03:29.027Z",
  "reasons": [
    {
      "code": "K003",
      "description": "Abnormal document quality. ID may have obscured data points, obscured security features, a corner removed, punctures, or watermarks obscured by digital text overlay "
    }
  ],
  "notes": [
    "Need more doc"
  ]
}
```

**KYB status and description:**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        KYC status
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `KYB_NOT_READY`
      </td>

      <td>
        The entity has not submitted all required data or documents. The entity must provide all required entity data, business document, control person and UBO information. Entity cannot open an account in this state
      </td>
    </tr>

    <tr>
      <td>
        `KYB_READY`
      </td>

      <td>
        All required entity data, document, control person and UBO information have been submitted. The entity is ready for KYB processing.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_PROCESSING_DIRECTOR`
      </td>

      <td>
        As part of KYB, DriveWealth will perform KYC on all directors including control person and UBO. This state indicates DriveWealth is performing kYC on directors. KYB will only proceed if all directors pass KYC.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_PROCESSING_ENTITY`
      </td>

      <td>
        All directors KYC successful, DriveWealth is now processing entity-level information and documentation
      </td>
    </tr>

    <tr>
      <td>
        `KYB_MANUAL_REVIEW`
      </td>

      <td>
        DriveWealth AML officer is manually reviewing entity information. This process can take up to 1 week.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_DOC_REQUIRED`
      </td>

      <td>
        Application sent back to upload additional business documents - This status occurs when the entity’s registration or formation documents are missing, expired, illegible, or otherwise deemed invalid (e.g., incorrect document type, inconsistent entity name, or incomplete filings). In such cases, the user or partner is required to re-upload valid, clearly legible, and up-to-date documentation that accurately reflects the entity’s legal name and registration details. The KYB process cannot proceed to approval until all required documents are successfully reviewed and verified.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_INFO_REQUIRED`
      </td>

      <td>
        Application sent back for entity data update - Occurs when the user, for example, provides an incomplete or incorrect entity name, enters an invalid or mistyped Tax Identification Number, or includes formatting errors. The partner or user must then submit the corrected business information for review and approval.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_APPROVED`
      </td>

      <td>
        The entity has been successfully verified, and an analyst has reviewed all submitted documents, confirming they are valid and in good order.
      </td>
    </tr>

    <tr>
      <td>
        `KYB_DENIED`
      </td>

      <td>
        KYB has failed due to one or more of the following: failed KYC for UBOs or control persons unverifiable business information invalid or missing documentation matches found on sanctions/watchlists (e.g., World-Check).

        KYB_DENIED will cause the entity transition to a REJECTED state, and all associated business accounts will be moved to FROZEN status. This is a terminal state and cannot be reversed.
      </td>
    </tr>
  </tbody>
</Table>

### `NO_KYB` mode

If you are on `NO_KYB` mode, you are responsible for performing KYB and all necessary due diligence on the entity prior to onboarding the entity with DriveWealth. All entities are automatically placed in the `KYB_APPROVED` status upon creation.

## Ongoing Entity management

Please ensure that entity data in the DriveWealth system is kept up to date whenever entity information changes. Common updates include changes to address, contact information, or company ownership. Use the [Update Entity](https://developer.drivewealth.com/apis/reference/patch_entities-entityid) API to make these updates as needed.

Updates to key entity identification fields such as entity name or identification numbers may trigger additional actions:

* If you are on `DO_KYB` mode, DriveWealth will automatically initiate a new KYB review using the updated entities information. During re-KYB, the accounts will remain in `OPEN` status and open to all activities unless the new KYB came back as failed, which will set the account to `FROZEN` state.
* Foreign entities must complete a new W8 via ComplyExchange. DriveWealth will automatically generate a new ComplyExchange URL upon entity update. You can view the new URL either by the [Retrieve Entity](https://developer.drivewealth.com/apis/reference/get_entities-entityid) API or you should receive a new notification if you subscribe to entities.updated event. Please direct your customer to fill out the form again. The entity can continue trading; however, all tax treaty benefits are removed until the entity submit a new validated W8.

## Need help?

Reach out to the DriveWealth Integrations team for:

* Discussing which KYB integration model is right for your business
* Supported business document types per jurisdiction
* White-label W-8BEN-E/W-8IMY form integration for foreign entities