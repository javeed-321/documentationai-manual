Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.29

## API Release 1.29

| Release Date     | Status   |
| :--------------- | :------- |
| December 9, 2021 | RELEASED |

## Features and Enhancements

### **Validation for First and Last Name**

Validation has been added to support only Standard ASCII characters in the first and last name.

### **Added Ability to Upload TOD Form While Creating/Viewing the Beneficiary**

* Added ability to upload a TOD form with document type `BENEFICIARY_DOCUMENT` using endpoint `POST {{bo-url}}/back-office/documents/`
* New optional field `documentID` added to `POST and GET /back-office/accounts/{{acctid}}/beneficiaries`

### **New Endpoint - GET Suspense Payment**

Added new endpoint `GET https://bo-api.drivewealth.io/back-office/funding/deposits/suspense`. See \[Get Suspense Payment API] (<https://developer.drivewealth.com/reference/get-suspense-payment>). Permissions required to utilize this endpoint.

## Bug Fixes

Fixed response returned when patching a linked bank account to now include the correct details and status under `bankAccountDetails` in `PATCH {{bo-url}}/back-office/bank-accounts/` end point