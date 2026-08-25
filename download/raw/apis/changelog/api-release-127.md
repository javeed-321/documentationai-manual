Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.27

## API Release 1.27

| Release Date     | Status   |
| :--------------- | :------- |
| November 4, 2021 | RELEASED |

## Features and Enhancements

### **KYC**

New KYC error codes have been added along with description updates:

* AGED\_ACCOUNT
* ACCOUNT\_INTEGRITY
* DOB\_NOT\_MATCH\_ON\_DOC
* NAME\_NOT\_MATCH\_ON\_DOC
* INVALID\_PHONE\_NUMBER
* INVALID\_EMAIL\_ADDRESS
* INVALID\_DOCUMENT\
  View all current KYC error codes and descriptions here: [KYC Error Mapping](https://developer.drivewealth.com/reference/simulate-kyc-failures)

### **Subscription Events Added**

Three new event types have been added to notify the partner when a subscription is created, updated or canceled:

* Subscription.created
* Subscription.updated
* Subscription.removed\
  View Subscription Events here: [Subscription Events](https://developer.drivewealth.com/reference/subscription-events)

## Bug Fixes

* The account nickname will now update when the user's first/last name changes
* Get order status/details by ID endpoint now returns an orderNotfound error message if an invalid order id in single digit is passed by the end user.