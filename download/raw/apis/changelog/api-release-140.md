Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.40

## API Release 1.40

| Environment | Release Date                 |
| :---------- | :--------------------------- |
| UAT         | RELEASED                     |
| Production  | Release Date - July 21, 2022 |

<br />

### **Error Code Updates**

The following error codes have been updated. Please see [Common Order Gateway Errors](https://developer.drivewealth.com/reference/common-order-gateway-errors) for more details on current error codes.

<br />

#### **URL :`{{bo-url}}/back-office/orders`**

| Previous Error Code | New Error Code | Status                     | Description                                    |
| :------------------ | :------------- | :------------------------- | :--------------------------------------------- |
| `custom`            | `O101`         | ERROR\_INSTRUMENT\_UNKNOWN | Invalid `instrumentID` provided in the request |

```json Sample Response - O101
{
    "errorCode": "O101",
    "message": "Invalid Symbol. Refer to the API documentation for details. Details: Instrument lookup failed for [symbol=	APPL]",
    "errorDetails": {
        "detail": "Instrument lookup failed for [symbol= APPL]",
        "field": "symbol",
        "type": "STRING"
    }
}
```

<br />

#### **URL :`{{bo-url}}/back-office/orders`**

| Previous Error Code | New Error Code | Status               | Description                      |
| :------------------ | :------------- | :------------------- | :------------------------------- |
| `E032`              | `O403`         | ERROR\_ACCOUNT\_NULL | `accountID`/ `accountNo` is null |

```json Sample Response O403
{
    "errorCode": "O403",
    "message": "Account Number is missing in the request Details: Account Number is missing in the request",
    "errorDetails": {
        "detail": "Account Number is missing in the request",
        "field": "accountNo",
        "type": "STRING"
    }
}
```