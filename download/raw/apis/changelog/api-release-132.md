Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.32

## API Release 1.32

| Environment | Status                      |
| :---------- | :-------------------------- |
| UAT         | RELEASED                    |
| Production  | RELEASED - February 3, 2022 |

## Features and Enhancements

### **Update to Virtual Account Payments**

Added enhancements to process efficiency and timing for virtual account deposits.

### **Improvement to RIA Managed Cash Transfers**

For partners with RIA Managed accounts, improved approval logic for cash transfer redemptions that accounts for seasoning periods and frequent deposits.

### **New Field Added to Beneficiaries Endpoint**

New field `created` has been added to the [Create Beneficiary](https://developer.drivewealth.com/reference/create-account-beneficiaries) and [List Beneficiaries](https://developer.drivewealth.com/reference/list-all-account-beneficiaries) endpoint responses. Date displayed will reflect the date and time the beneficiary was added.