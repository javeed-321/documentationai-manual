Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.51

## API Release 1.51

### Deployed in UAT - Yes, available to test.

### Deployed in Production - Yes.

## 1. 🚀New Features & New API endpoints- What’s New?

Teen Account Graduation and Frozen status

##### **Description -**  We are introducing Assets Transfer APIs which includes all of sets of transfers i.e Teen/Custodial, Cash, Stock, Rewards and Promotions.

##### **Expected Behavior Change -** In 1.0.0, we are introducing Teen/Custodial transfers which is called as Minor Graduation Assets Transfer. Partners can transfer all custodian assets under Teen/Custodial's individual account. By providing source and destination account details, API will take care of all pending settlements, account statuses, events and all type of other required validations for the transfers. With these Assets transfer APIs, we are introducing FROZEN account status which helps us to manage the operations on account activity. FROZEN account is similar to CLOSED account status where we are blocking all activities on the account. Now onwards, CLOSED status will be the end state of the account.

> 👍 New endpoints -
>
> 1. add-authorized-user\
>    [PATCH https://bo-api.drivewealth.io](https://bo-api.drivewealth.io)/back-office/accounts/\{account-id}
> 2. Minor Graduation Asset Transfers\
>    [POST https://bo-api.drivewealth.io](https://bo-api.drivewealth.io)/back-office/asset-transfers/minor-graduation
> 3. Get Minor Account Transfer\
>    [GET https://bo-api.drivewealth.io](https://bo-api.drivewealth.io)/back-office/asset-transfers/\{id}
> 4. List Minor Account Transfers\
>    [GET https://bo-api.drivewealth.io](https://bo-api.drivewealth.io)/back-office/asset-transfers/

##### Requires code change? - Yes, to integrate the APIs and the Frozen status for these accounts.

##### What action is required - If you would like to offer or are currently offering teen accounts to your user base, utilize these transfer endpoints. Also ensure that your systems recognize FROZEN accounts in addition to CLOSED.

##### Available to Test in UAT - Yes

##### Feature Toggle (Y/N) - N

## 2.  🎉Feature Enhancements - We are making it better for you!!

Travel Rule changes for IFA

> 📘 Only applicable to partners using Instant Funding.

##### Existing Feature - Currently, whenever there is Instant Funding involved (Deposits or Redemption) we collect and store some required information in a CSV format outside of the API architecture.

##### What is improving? - Going forward, we will be collecting this information via the APIs itself. Partners / Partner's bank will be required to pass this information for both Instant Funding Deposits and Redemptions.

> 👍 Required fields
>
> 1. Bank Account Number
> 2. Bank Routing Number
> 3. Bank Name
> 4. Bank Address
> 5. Bank Country
> 6. Account Holder’s name
> 7. Account Holder’s Address
> 8. Account Holder’s country

```Text IFA Deposits payload
{
   "accountNo": "DWMW000095",
   "amount": 1000,
   "currency": "USD",
   "type": "INSTANT_FUNDING",
   "note": "Here's some money",
   "originatorBankDetails": {
       "bankAccountNumber": "127361827",
       "bankRoutingNumber": "256074974",
       "bankName": "Bank of Ninja",
       "bankAddress": "Village Hidden in the Sand, Sunagakure",
       "bankCountry": "JPN",
       "accountHolderName": "Naruto Uzumaki",
       "accountHolderAddress": "Village Hidden in the Leaves, Konohagakure",
       "accountHolderCountry": "JPN"
   }
}
```

```Text IFA Redemptions payload
{
   "accountNo": "DWMW000095",
   "amount": 1000,
   "currency": "USD",
   "type": "INSTANT_FUNDING",
   "note": "Here's some money",
   "receivingBankDetails": {
       "bankAccountNumber": "127361827",
       "bankRoutingNumber": "256074974",
       "bankName": "Bank of Ninja",
       "bankAddress": "Village Hidden in the Sand, Sunagakure",
       "bankCountry": "JPN",
       "accountHolderName": "Naruto Uzumaki",
       "accountHolderAddress": "Village Hidden in the Leaves, Konohagakure",
       "accountHolderCountry": "JPN"
   }
}
```

##### Available to Test in UAT  - Yes

##### Feature Toggle (Y/N) - Yes