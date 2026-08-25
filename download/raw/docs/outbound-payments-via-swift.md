---
updatedAt: 2026-05-20T10:02:52.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Outbound Payments via SWIFT

> ❗️ Only applicable to customers authorised payments via SWIFT
>
> Payment requests made via SWIFT by customers who are not authorised for SWIFT will be rejected.

# Required information

### Payment Request

To make an outbound payment from your Modulr account via SWIFT, the [Create Payments](https://modulr.readme.io/reference/sendpayment) must be used.

To ensure successful processing, you must chose the correct destination type and supply the required fields based on where the destination country the beneficiary account is located.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Destination Country (or Region)
      </th>

      <th>
        Destination Type
      </th>

      <th>
        Required Payment Request Fields
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        United Kingdom
      </td>

      <td>
        SCAN
      </td>

      <td>
        Sort Code  
        Account Number
      </td>
    </tr>

    <tr>
      <td>
        Europe
      </td>

      <td>
        IBAN
      </td>

      <td>
        IBAN
      </td>
    </tr>

    <tr>
      <td>
        United States
      </td>

      <td>
        ANBRN
      </td>

      <td>
        abaRoutingNumber  
        Account Number
      </td>
    </tr>

    <tr>
      <td>
        Japan and Hong Kong
      </td>

      <td>
        AN
      </td>

      <td>
        Account Number
      </td>
    </tr>
  </tbody>
</Table>

> 🚧 Important
>
> In addition to the above required fields, the SWIFT BIC must also be provided for each destination type
>
> Only the following characters should be used:
>
> * alphabetic letters (a-z & A-Z)
> * numerals (0-9)
> * a limited set of special characters include: space, period, parentheses, hyphen, slash, less than, plus, ampersand, dollar sign, asterisk, semicolon, percent sign, at sign, equal sign, double quote, and backslash

Further, it is highly recommended that you include as much information about the beneficiary as possible in the payment request to help minimise the chance of delays or rejections during the payment journey.

Note: Modulr only supports international payments to specific countries from accounts in a given currency. See [Allowed Destinations for supported currencies](https://modulr.readme.io/docs/allowed-destinations-for-modulr-supported-currencies) for more information.

<br />

# Example Payment Requests

```json SCAN (UK)
{
    "sourceAccountId": "A210000005",
    "destination": {
        "type": "SCAN",
        "sortCode": "000000",
        "accountNumber": "45678958",
        "name": "payee name",
        "address": {
            "addressLine1": "modulr avenue",
            "addressLine2": "1st floor",
            "postTown": "London",
            "countrySubDivision": "London",
            "postCode": "SW126TP",
            "country":"GB"
        },
        "birthdate": "2000-01-01",
        "emailAddress": "ABC@modulrfinance.com",
        "phoneNumber": "00897654",
        "bic": "BARCGB22",
        "countrySpecificDetails": {
            "bankName": "Trusted Bank",
            "bankAddress": "2100 Sideway",
            "bankCity": "London",
            "bankCountry": "GB,
            "bankBranchName": "London",
            "bankBranchCode": "44-55",
            "business": true
        }
    },
    "currency": "EUR",
    "amount": 1.00,
    "reference": "reference field"
  }
```
```json IBAN (EU)
{
    "sourceAccountId": "A210000005",
    "destination": {
        "type": "IBAN",
        "iban": "GB86BARC20038014469149",
        "name": "payee name",
        "address": {
            "addressLine1": "modulr avenue",
            "addressLine2": "1st floor",
            "postTown": "Barcelona",
            "countrySubDivision": "Barcelona",
            "postCode": "22889",
            "country": "ES"
        },
        "birthdate": "2000-01-01",
        "emailAddress": "ABC@modulrfinance.com",
        "phoneNumber": "00897654",
        "bic": "BARCGB22",
        "countrySpecificDetails": {
            "bankName": "Trusted Bank",
            "bankAddress": "3100 XYZ",
            "bankCity": "Barcelona",
            "bankCountry": "ES",
            "bankBranchName": "Barcelona",
            "bankBranchCode": "2100",
            "business": true
        }
    },
    "currency": "DKK",
    "amount": 1.00,
    "reference": "reference field"
}
```
```json ANBRN (US)
{
    "sourceAccountId": "A210000007",
    "destinationType": "ANBRN",
    "destination": {
        "type": "ANBRN",
        "accountNumber": "45678956",
        "name": "Destination ANBRN Beneficiary",
        "address": {
            "addressLine1": "345 Broadway",
            "postTown": "New York",
            "postCode": "08989",
            "country": "US",
            "countrySubDivision":"New York"
        },
        "birthdate": "2000-01-01",
        "emailAddress": "ABC@modulrfinance.com", 
        "phoneNumber": "00897654", 
        "bic": "BARCUS22",
        "countrySpecificDetails": {
            "bankName": "XYZ Bank",
            "bankAddress": "2100 Broadway",
            "bankCity": "New York City",
            "bankBranchName": "New York",
            "bankBranchCode": "44-04",
            "abaRoutingNumber": "123456789",
            "business": true,
            "bankCountry": "US"
        }
    },
    "currency": "USD",
    "amount": 10.00,
    "reference": "Payment 100139005A1104889665"
}
```