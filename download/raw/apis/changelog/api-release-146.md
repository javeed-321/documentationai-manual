Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.46

## API Release 1.46

| Environment | Release Date                     |
| :---------- | :------------------------------- |
| UAT         | RELEASED                         |
| Production  | Release Date - December 13, 2022 |

<br />

### **API Update - Tax ID Information**

Beginning December 13, 2022, `FOREIGN_TIN` will no longer be accepted.

Please begin using the following values for `data.type` when a creating user:

`"SSN"` – Social Security Number

`"EIN"` - Employer Identification Number

`"FTIN"` - Foreign Tax ID Number

`"FTNLO"` - Foreign TIN Not Legally Required

Please see [Tax ID Info](https://developer.drivewealth.com/reference/national-identification-number-document-object) for additional details.

Additional communications to follow regarding implementation deadlines

<br />

### **API Update - Instruments and Extended Hours**

In preparation for future enhancements for extended hours, the [instruments.created](https://developer.drivewealth.com/reference/instrument-created) and [instruments.updated](https://developer.drivewealth.com/reference/instrument-updated) events will now display a new value:

`enableForExtendedHoursNotional`

The value will show as `INACTIVE` at this time.

`enableExtendedHoursNotionalStatus` will display in the [List All Instruments](https://developer.drivewealth.com/reference/list-all-instruments) and [Get Instrument Details](https://developer.drivewealth.com/reference/get-instrument-details). This value will also show as `INACTIVE` at this time. Further updates will be provided on Extended Hours - Notional in the future.

<br />

### **Event Update - KYC**

KYC events will only generate for `INDIVIDUAL` and `INSTITUTIONAL` user types

<br />

### **Enhancement - Pattern Day Trading (PDT)**

Please see [this notice](https://guides.drivewealth.com/changelog/pattern-day-trading-enhancements) for information on upcoming enhancements to the Pattern Day Trading logic