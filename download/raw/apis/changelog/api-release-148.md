Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.48

## API Release 1.48

| Environment | Release Date                    |
| :---------- | :------------------------------ |
| UAT         | RELEASED                        |
| Production  | Release Date - February 9, 2023 |

<br />

### **Enhancement - Pattern Day Trade (PDT) Updates**

Please see [Highlight on PDT Enhancements](https://guides.drivewealth.com/changelog/pattern-day-trading-enhancements) for details on updates to logic, new report, and updates to events

<br />

### **Validation Update - First and Last Name**

The a minimum character limit of 1 and a maximum character limit of 500 has been implemented on the user's First Name and Last Name fields.

<br />

### **Validation Update - Email**

Email addresses including the "+" character are now allowed.

<br />

### **Enhancement - KYC**

Custodial and Beneficiary users will be auto approved and no longer pushed through the KYC process.

<br />

### **Bug Fix - KYC**

Upon opening an additional account, KYC will not be re-run for users that already are KYC approved and have an existing account.

<br />

### **Bug Fix - Missing ID Type**

ID Type attribute added to following endpoints:

* GET [https://bo-api.drivewealth.io/back-office/users/`{userID}`](https://developer.drivewealth.com/reference/get_users-userid)
* PATCH [https://bo-api.drivewealth.io/back-office/users/`{userID}`](https://developer.drivewealth.com/reference/patch_users-userid)

An error will be thrown when ID number is not passed in request and not present in database when editing user information with:

PATCH [https://bo-api.drivewealth.io/back-office/users/`{userID}`](https://developer.drivewealth.com/reference/patch_users-userid)