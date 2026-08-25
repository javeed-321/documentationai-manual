Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.42

## API Release 1.42

| Environment | Release Date                  |
| :---------- | :---------------------------- |
| UAT         | RELEASED                      |
| Production  | RELEASED - September 15, 2022 |

<br />

### **Error Code Updates**

The following error code has been updated:

`E032` will display message `Bank Routing Number Validation Response: Routing number is invalid` when an invalid `beneficiarySwiftABA` is passed.

<br />

### **Update  - Custodial User Creation**

When creating a user where `userType` = `CUSTODIAL`, the `username` and `password` fields are no longer required.

<br />

### **Update - Maximum Order Quantity**

The maximum order quantity allowed has been increased from 10,000 shares to 20,000 shares.