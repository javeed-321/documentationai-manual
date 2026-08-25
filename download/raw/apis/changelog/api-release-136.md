Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.36

## API Release 1.36

| Environment | Status                   |
| :---------- | :----------------------- |
| UAT         | RELEASED                 |
| PRODUCTION  | RELEASED- April 12, 2022 |

### **New Feature - 24/7 Cash Rewards**

Added ability to utilize the deposit endpoint for cash promotional purposes. Permission must be granted before partners can access this feature. Please contact your Account Manager for more information.

### **Update - Prior Year Contributions Enabled**

Prior year contributions have been enabled through April 18, 2022 for IRA accounts.

### **Update - GET User Request to Include Extended Hours Disclosure**

The [GET User](https://developer.drivewealth.com/reference/get-user-details) request now includes `ackExtendedHoursAgreement`

### **Update - KYC**

Validation added to `idType` in POST and PATCH User API to check for enum values:

* `OTHER(0, "Other"),`
* `SSN(1,"Social Security Number"),`
* `US_TIN(2, "Tax ID Number"),`
* `FOREIGN_TIN(3, "Foreign Tax ID Number");`

Any legacy value passed will default to `OTHER`

```json Example POST or PATCH Request
{
  "type": "IDENTIFICATION_INFO",
  "data": {
    "value": "551245676",
    "type": "FOREIGN_TIN", ///  validation added for this field
    "citizenship": "IND",
    "usTaxPayer": false
  }
}
```