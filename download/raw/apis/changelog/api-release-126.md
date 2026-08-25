Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.26

## API Release 1.26

| Release Date     | Status   |
| :--------------- | :------- |
| October 19, 2021 | RELEASED |

## Features and Enhancements

### **Reject redemptions if cash available for withdrawal is less than or equal to fees**

An error message will be returned and redemption will be rejected if cash available for withdrawal is less than or equal to fees.

Endpoint: \{bo-url}}/back-office/funding/redemptions **POST**

```json Sample Response
{
 "errorCode": "Y075",
 "message": "The redemption amount is more than the cash available. Details: Available balance: 25.00, Fees: 25"
}
```