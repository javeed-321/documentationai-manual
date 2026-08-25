Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.38

## API Release 1.38

| Environment | Release Date            |
| :---------- | :---------------------- |
| UAT         | RELEASED                |
| PRODUCTION  | RELEASED - June 2, 2022 |

### **Update - LPMA Accounts and PDT Counter**

PDT Counter will display correct number of Pattern Day Trades on 5th day. See [API Highlight](https://guides.drivewealth.com/changelog/api-highlights-pdt-for-lpma-accounts) for more information on PDT for LPMA accounts.

### **New - Error Messages**

The following validations and error messages have been implemented:

* When creating a Portfolio with a `RELATIVE_DRIFT` or `ABSOLUTE_DRIFT` that contains an `upperBound` value that is less than the `lowerBound` value, the request will be rejected and a 400 error will be received
* When creating an RIA Fund with a `RELATIVE_DRIFT` or `ABSOLUTE_DRIFT` that contains an `upperBound` value that is less than the `lowerBound` value, the request will be rejected and a 400 error will be received
* Added validation and error message to `{{bo-url}}/back-office/documents/`:
  * Validation to check if `data:[<MIME-type>]` is present in the document. If not present, "Please use correct format : Data URI with base 64 encoding for the document. data:\[;base64],\<data>" error message will be received.