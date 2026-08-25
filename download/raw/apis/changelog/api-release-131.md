Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.31

## API Release 1.31

| Release Date     | Status   |
| :--------------- | :------- |
| January 18, 2022 | RELEASED |

## Features and Enhancements

### **Enable RIA Partners to Update Payment Status and Amount**

RIA Partners can now change the payment status from `RIA_APPROVED` or `RIA_PENDING` to `RIA_REJECTED`. RIA partners can update payment amounts if payment is in `RIA_APPROVED` or `RIA_PENDING` status.

### **User Update Tracking**

New field `updatedBy` added to `users.updated` event and to [Update User](https://developer.drivewealth.com/reference/update-user) response that captures the userID of the user that made changes. When user information is changed through the Update User API or through DriveHub, the `updatedBy` field is recorded.

### **Reject Corrupted Documents**

[Documents API](https://developer.drivewealth.com/reference/upload-physical-documents) will reject corrupted documents and respond with error code.

### **Reject TEFRA Reversal Fee if Outside Trading Hours**

TEFRA Reversal request will be rejected if request is received outside of trading hours.

### **Pending Limit Orders Deducts CAFW**

For pending limit orders, the cash available for withdrawal (CAFW) will be deducted by the order amount. Cash available for trade (CAFT) will continue to be deducted by the order amount.

### **New KYC Error Codes**

New KYC error codes `INVALID_NAME_TOO_LONG` and `UNSUPPORTED_COUNTRY` added to [KYC Error Mapping](https://developer.drivewealth.com/reference/simulate-kyc-failures). Errors found while submitting the user will update the [KYC Status](https://developer.drivewealth.com/reference/kyc-statuses) to `KYC_NOT_READY` and add message in `statusComment` field.