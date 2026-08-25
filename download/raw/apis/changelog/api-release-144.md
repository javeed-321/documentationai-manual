Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.44

## API Release 1.45

| Environment | Release Date                    |
| :---------- | :------------------------------ |
| UAT         | RELEASED                        |
| Production  | Release Date - November 7, 2022 |

<br />

### **KYC Updates**

When `userType` =`INSTITUTIONAL` such as Trust, SMSF, the user will go through the KYC process.

<br />

### **Validation Update**

First and Last Name fields with a minimum of 1 character will be acceptable and valid.

<br />

### **Tax Forms**

Releasing a fix to correct any invalid or missing tax codes. This will generate `accounts.updated` events. No action is needed by the partners.