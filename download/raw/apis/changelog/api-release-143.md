Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.43

## API Release 1.43

| Environment | Release Date                    |
| :---------- | :------------------------------ |
| UAT         | RELEASED                        |
| Production  | Release Date - October 13, 2022 |

<br />

### **Error Code Updates**

Deposit types `ACH`and `ACH_MANUAL` are the only deposit types that are counted towards the maximum daily limit for the following error code:

`"errorCode": "E032", "message": "Invalid or missing parameters in the request body. Refer to the API documentation for details. Details: Deposit transaction exceeds maximum daily deposit transaction limit of 3" `

<br />

### **Tax Documentation Update - Entity Accounts**

The W-8BEN-E tax document will now populate the organization name for entity accounts.