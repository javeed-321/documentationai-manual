Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.54

## API Release 1.54

### Deployed in UAT - Yes, available to test.

### Deployed in Production - June 15, 2023.

# 1. 🚀New Features - What’s New?

## 1.1 Add a new standard document type called KYC\_VERIFICATION\_INFO to the users object on Create User & Update User endpoints

#### **Description -**  We are introducing a dedicated object for KYC as verification information under the /users endpoint where partners will send data to evidence KYC Verification.

## 1.2 Also add an optional fields block customFields to allow adding up to 5 extra custom entries.

#### **Description -**&#x54;he size of these custom entries should follow the same rules as the metadata entries map we use in other places.

#### Feature Toggle? - Yes

#### **Expected Behavior Change -**

> 👍 This new document is optional, however if uploaded, all fields in the object should be mandatory except the custom fields. The custom fields if entered should be used for KYC related information ONLY.

```Text POST /users & PATCH /users
{
  "userType": "INDIVIDUAL_TRADER",
  ...
  "documents": [
    {
      "type": "KYC_VERIFICATION_INFO",
      "data": {
            "verification":"APPROVED/FAILED",
            "verificationIDType":"DRIVER_LICENSE/NATIONAL_ID/RESIDENCE_PERMIT/PASSPORT/VISA/TAX_ID/ VOTER_ID/WORK_PERMIT/TRUST/TRUST_CORP/CORPORATE”,
            "verificationFullName":"{{vendorResponse}}",
            "verificiationTimestamp":"ISO 8601 standard",
            "verificationTransactionID":"{{vendorResponse}}",

            // Allow this only if this is possible or it can be a map of custom fields such as "customeFields": Map<String, String>
            "customField1": "value1",
            "customField2": "value2",
            "customField3": "value3",
            "customField4": "value4",
            "customField5": "value5"
        },
    
    },
    ...
}
```

## 1.3 Add new document types to upload new documents related to ACATS and TOD for a user.

#### **Description -** Currently there are multiple document types such as PROOF\_OF\_ADDRESS, VISA, DRIVERS\_LICENCE etc that can up uploaded from the documents endpoints. We are now introducing 3 new document types:

> 👍 3 new document types. These will be available in DriveHub under the Compliance tab
>
> ACATS\_IN - Transfer log of positions that were moved into an account via ACATS
>
> ACATS\_OUT - Transfer log of positions that were moved out of an account via ACATS
>
> TRANSFER\_ON\_DEATH - Transfer on death deed

# 2. 🎉Feature Enhancements - We are making it better for you!!

## 2.1 Add statusReason whenever DriveWealth or the partner changes the account status

#### Existing Feature - Current account status change feature doesn't capture the process and individual who initiated the status change .

#### For example: The reason behind status change to OPEN\_NO\_NEW\_TRADE is not evident whether it is because of Payment failure, KYC failure or PDT restrictions. Can we re-open the account. Similarly if the account is Frozen we don't know the reason behind the change in status whether it was due to FINRA notice or Asset transfer.

#### What is improving? - As part of the change we are capturing statusReason field in the accounts PATCH API which will track the reason behind the status change. Currently we have a field namely closingReason which is primarily used when we close an account. The closingReason field will be deprecated and statusReason need to be utilized to capture the account closing reason.

#### Expected change - When the account status is changed to Frozen, any recurring deposits and withdrawals will be rejected. The associated error message will look like this

```Text ERROR CODE: 403
{
"errorCode": "A051",
"message": "Account has been restricted. Check account status and notes for details. Forbidden: Account Status: FROZEN"
}
```

> 📘 Good to know
>
> 1. if statusReason is not passed then OTHER should be by default
> 2. If Partner has changed the status then they can change the next status.
> 3. DW ops should have full access to change any status. Even if the status was updated by the partner
> 4. If statusReason=OTHER then statusComment is required.
> 5. Reasons available to Partners to choose from at this time:
>    1. **DUPLICATE\_ACCOUNT**
>    2. **PARTNER\_RESTRICTED**
>    3. **OTHER**

# 3. 🔧Bug Fixes

## 3.1 Quick fix time adjustment to release branch

#### **What is improving?** - This quick fix will improve the time it takes to identify PDT accounts when the market opens. We will be able to identify accounts with PDT violations within 5 minutes delay of market open. Once this threshold is met, the goal is to lower this time to a shorter amount.

# 4. 🎁New API endpoints

## 4.1  GET /accounts/\{accountID}/regulatory-inserts

#### **Description -** This new endpoint  will replace the need for DriveWealth to send several email communications to customers to deliver the annual audited financial statement, privacy notice, BCP, updates to customer agreements, or really any official documentation that should be delivered to the customer for regulatory purposes.

> 👍 Following are the new types of regulatory inserts
>
> * Privacy Policy
> * Account Agreement - Update
> * Audited Financial Statements - Custodian
> * Unaudited Financial Statements - Custodian
> * Trading Disclosure - Update
> * Regulatory Insert
> * Account Notification - Important Information
> * Cyber Security Notification

> 🚧 These regulatory inserts will only be available via API at this time. Not applicable to DriveHub.