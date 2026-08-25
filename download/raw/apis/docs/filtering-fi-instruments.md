---
updatedAt: 2026-07-13T22:57:09.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Filtering FI Instruments

DriveWealth enables clients to offer tailored Fixed Income investing experiences by offering a powerful filtering API(refer: [Search Instruments](https://developer.drivewealth.com/apis/reference/filterinstruments)). This endpoint supports a wide range of parameters, allowing you to build workflows and user journeys for various bond strategies—across geographies, ratings, maturities, and yields.

This section covers how to get started with filtering, along with some of the most common filtering examples we've seen across DriveWealth’s Fixed Income clients.

### 🇺🇸 Filter for U.S. Government Bonds

Useful for investors looking for exposure to high-quality, low-risk bonds issued by U.S. federal or agency entities.

```json POST /back-office/instruments/filter
[
  {
    "field": "bondType",
    "operator": "=",
    "value1": "GOVERNMENT/AGENCY_BOND"
  },
  {
    "field": "issuer.domicileCountry",
    "operator": "=",
    "value1": "US"
  }
]
```

📌 Combine with maturity filters (e.g., < 2 years) to create Treasury ladders.

### 🌍 Filter for Foreign Corporate Bonds

Target international issuers for diversification or global credit strategies.

```json POST /back-office/instruments/filter
[
  {
    "field": "bondType",
    "operator": "=",
    "value1": "CORPORATE_BOND"
  },
  {
    "field": "issuer.domicileCountry",
    "operator": "!=",
    "value1": "US"
  }
]
```

### 🌐 Investment Grade Foreign Corporate Bonds

A conservative screen on international credit—only includes bonds rated BBB- or higher.

```json POST /back-office/instruments/filter
[
  {
    "field": "bondType",
    "operator": "=",
    "value1": "CORPORATE_BOND"
  },
  {
    "field": "issuer.domicileCountry",
    "operator": "=",
    "value1": "US"
  },
  {
    "field": "spRating",
    "operator": ">=",
    "value1": "BBB-"
  }
]
```

### 💵 U.S. Investment Grade Corporate Bonds with Coupon > 5%

Targets bonds offering 5%+ coupon, often attractive in rising rate environments.

```json POST /back-office/instruments/filter
[
  {
    "field": "bondType",
    "operator": "=",
    "value1": "CORPORATE_BOND"
  },
  {
    "field": "issuer.domicileCountry",
    "operator": "=",
    "value1": "US"
  },
  {
    "field": "spRating",
    "operator": ">=",
    "value1": "BBB-"
  },
  {
    "field": "couponRate",
    "operator": ">",
    "value1": "5"
  }
]
```

### 🕰 U.S. IG Corporate Bonds w/ 5%+ Coupon, Maturing After 2030

Focuses on long-dated income-generating instruments with solid credit backing.

```json POST /back-office/instruments/filter
[
  {
    "field": "bondType",
    "operator": "=",
    "value1": "CORPORATE_BOND"
  },
  {
    "field": "issuer.domicileCountry",
    "operator": "=",
    "value1": "US"
  },
  {
    "field": "spRating",
    "operator": ">=",
    "value1": "BBB-"
  },
  {
    "field": "couponRate",
    "operator": ">",
    "value1": "5"
  },
  {
    "field": "maturityDate",
    "operator": ">=",
    "value1": "2031-01-01"
  }
]
```

📌 `maturityDate` must be in `YYYY-MM-DD` format.

The filtering API supports dozens of fields and operators, enabling plenty of combinations—including filtering by maturity buckets, ratings, coupon attributes, bond indicators and more. Refer to the API documentation for the full list of supported fields.

Once you’ve filtered your target bonds, use their `instrumentId` to retrieve:

💰 Price and yield details<br />📈 Live bid/ask<br />📦 Order sizes

See: [Fixed Income Depth of Book](https://developer.drivewealth.com/apis/docs/fixed-income-depth-of-book)