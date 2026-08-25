---
updatedAt: 2026-08-23T15:59:36.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# MCP examples

### Worked Example: `get_instrument`

This section pairs real request/response examples with the underlying MCP protocol reference. Worked examples show an actual tools/call request built from a tool's schema alongside its captured response, so you can see the full round trip for that tool.

**Request**, built from `inputSchema` — the only required field is `symbolOrInstrumentID`:

```json
{
  "jsonrpc": "2.0",
  "id": "5",
  "method": "tools/call",
  "params": {
    "name": "get_instrument",
    "arguments": {
      "symbolOrInstrumentID": "AAPL"
    }
  }
}
```

**Response** (captured live against UAT):

```json
{
  "symbol": "AAPL",
  "reutersPrimaryRic": "AAPL.O",
  "name": "Apple, Inc.",
  "description": "Apple Inc. designs, manufactures and markets smartphones, personal computers, tablets, wearables and accessories, and sells a variety of related services. Its product categories include iPhone, Mac, iPad, Wearables, Home and Accessories. Its services include advertising, AppleCare, cloud services, digital content, and payment services. The Company operates various platforms, including the App Store, that allow customers to discover and download applications and digital content, such as books, music, video, games and podcasts. It also offers digital content through subscription-based services, including Apple Arcade, Apple Fitness+, Apple Music, Apple News+, and Apple TV+. Its wearables include smartwatches, wireless headphones, and spatial computers. Its products include iPhone 16 Pro, iPhone 16, iPhone 15, iPhone 14, iPhone SE, MacBook Air, MacBook Pro, iMac, Mac mini, Mac Studio, Mac Pro, iPad Pro, iPad Air, AirPods, AirPods Pro, AirPods Max, Apple TV, Apple Vision Pro and others.",
  "sector": "Technology",
  "longOnly": true,
  "orderSizeMax": 10000,
  "orderSizeMin": 1e-8,
  "orderSizeStep": 1e-8,
  "exchangeNickelSpread": false,
  "close": 337,
  "descriptionChinese": "Apple Inc设计、制造和销售智能手机、个人电脑、平板电脑、可穿戴设备和配件，并销售各种相关服务。该公司产品类别包括iPhone、Mac、iPad以及可穿戴设备、家居和配件。该公司软件平台包括iOS、iPadOS、macOS、watchOS、visionOS和tvOS。该公司服务包括广告、AppleCare、云服务、数字内容和支付服务。该公司运营包括App Store在内的各种平台，允许客户发现和下载应用程序和数字内容，例如图书、音乐、视频、游戏和播客。该公司还通过基于订阅的服务提供数字内容，包括Apple Arcade、Apple Fitness+、Apple Music、Apple News+和Apple TV+。该公司产品包括iPhone 16 Pro、iPhone 16、iPhone 15、iPhone 14、iPhone SE、MacBook Air、MacBook Pro、iMac、Mac mini、Mac Studio、Mac Pro、iPad Pro、iPad Air、AirPods、AirPods Pro、AirPods Max、Apple TV和Apple Vision Pro。",
  "enableExtendedHoursNotionalStatus": "ACTIVE",
  "overnightTradingStatus": "INACTIVE",
  "isOptionsEnabled": true,
  "industry": "Communications Equipment",
  "trbc2012": "Phones & Smart Phones",
  "indexMemberships": [
    "Dow Industry",
    "NASDAQ 100 Index",
    "S&P 500",
    "TR Equity United States Index"
  ],
  "incorporatedCountry": "USA",
  "international": false,
  "priceBufferPctMOC": 0,
  "marketTier": "Q",
  "isPTP": false,
  "averageLendingRate": 0.0175,
  "id": "a67422af-8504-43df-9e63-7361eb0bd99e",
  "type": "EQUITY",
  "exchange": "NSQ",
  "url": "http://investor.apple.com",
  "status": "ACTIVE",
  "closePrior": 333.02,
  "image": "https://uat-drivewealth.imgix.net/symbols/aapl.png?fit=fillmax&w=125&h=125&bg=FFFFFF",
  "ISIN": "US0378331005",
  "CUSIP": "037833100",
  "SEDOL": "2046251",
  "overrideReutersFieldsEnabled": false,
  "VOL10DAVG": 47546591,
  "871mEligible": true
}
```

***

## Protocol Reference

This section pairs real request/response examples with the underlying MCP protocol reference. Worked examples show an actual tools/call request built from a tool's schema alongside its captured response, so you can see the full round trip for that tool.

### `tools/list` Request

```json
{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "tools/list",
    "params": {}
}
```

### `tools/list` Response (Shape Example)

```json
{
    "jsonrpc": "2.0",
    "id": "1",
    "result": {
        "tools": [
            {
                "name": "get_account",
                "description": "Retrieve account details",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string"
                        }
                    },
                    "required": ["account_id"]
                }
            }
        ]
    }
}
```

### `tools/call` Request

```json
{
    "jsonrpc": "2.0",
    "id": "2",
    "method": "tools/call",
    "params": {
        "name": "get_account",
        "arguments": {
            "account_id": "A123456789"
        }
    }
}
```

### `tools/call` Error Example

```json
{
    "content": [
        {
            "type": "text",
            "text": "[drivewealth-api] The DriveWealth API returned an error (HTTP 400).\n{\"errorCode\":\"A011\",\"message\":\"A required accountID is missing or invalid. Refer to the API documentation for details.\"}"
        }
    ],
    "isError": true
}

```

### `tools/call` Auth Error Example

```json
{
    "content": [
        {
            "type": "text",
            "text": "[drivewealth-api] The DriveWealth back-office API returned an error (HTTP 401).\n{\"errorCode\":\"L025\",\"message\":\"Auth Token expired. Please log in Again. Details: Auth Token expired. Please log in Again.\"}"
        }
    ],
    "isError": true
}
```