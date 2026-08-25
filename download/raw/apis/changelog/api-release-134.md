Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.34

## API Release 1.34

| Environment | Status                   |
| :---------- | :----------------------- |
| UAT         | RELEASED                 |
| Production  | RELEASED - March 8, 2022 |

### **New Field Added - averagePriceRaw**

New field `averagePriceRaw` has been added to the following endpoints:

* `{bo-url}}/back-office/orders/{{orderID}}`
* `{{bo-url}}/back-office/orders/byOrderNo/{{orderNo}}`
* `{{bo-url}}/back-office/accounts/{{acctid}}/reports/order-history`
* Added `averagePriceRaw` field to `TicketAuditReport`\
  The field applies to all order types. It is as six decimal field and partners may apply desired precision on their end.

### **Performance Enhancement - Deposit Job**

Optimized the processing time of the daily deposit job.

### **Enhancement to GET Account API**

`taxStatusCode` and `taxRecipientCode` will display on [Get Account API](https://developer.drivewealth.com/reference/get-account-details)

```json
{
.....
"taxProfile":{
    "taxStatusCode": ENUM
    "taxRecipientCode": ENUM
  }
}
```

### **Error Code Update**

Error code updated to 400 when `taxTreatyWithUS` is set to `true` when \[country = USA] as USA is not eligible for Tax Treaty.

### **New Error Code for Redemptions API**

New error code `E032` added to `{{bo-url}}/back-office/funding/redemptions/{redemptionID}` for missing or invalid parameters.