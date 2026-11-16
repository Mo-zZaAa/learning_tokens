---
url: https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset
title: Get Market Data for an Asset - Ondo Finance
description: This endpoint retrieves comprehensive market data for a specific asset, containing both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The "Tradable Sessions" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Market Data for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/market",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/market")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

429

500

```
{
  "primaryMarket": {
    "symbol": "ADBEon",
    "price": "361.986667",
    "priceChange24h": "8.76",
    "priceChangePct24h": "2.479993958100564361",
    "priceHistory24h": [
      {
        "timestamp": 1755802800000,
        "price": "353.226667"
      },
      {
        "timestamp": 1755803700000,
        "price": "353.216667"
      },
      "..."
    ],
    "totalHolders": 7,
    "sharesMultiplier": "1",
    "tradableSessions": [
      "premarket",
      "regular",
      "postmarket",
      "overnight"
    ]
  },
  "underlyingMarket": {
    "ticker": "ADBE",
    "name": "Adobe Inc.",
    "price": "361.986667",
    "priceHigh52w": "587.75",
    "priceLow52w": "330.04",
    "volume": "1851321",
    "averageVolume": "3610882",
    "sharesOutstanding": "424200000",
    "marketCap": "149925006000"
  },
  "constituentTokens": [],
  "timestamp": 1755890061815
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "invalid symbol; must be at least 3 characters long and end with 'on'",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#invalid_symbol"
}
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "The provided asset symbol does not exist and cannot be found.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_not_found"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Assets

# Get Market Data for an Asset

Copy pageCopy page

This endpoint retrieves comprehensive market data for a specific asset, containing both primary market (on-chain token) and underlying market (off-chain stock) information.

Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization.

This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio.

The “Tradable Sessions” parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status).

Prices are intended for display only. For real-time trading prices, use the [Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote) API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact [support@ondo.finance](mailto:support@ondo.finance).

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

assets

/

{symbol}

/

market

Try it

Get Market Data for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/market",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/market")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

429

500

```
{
  "primaryMarket": {
    "symbol": "ADBEon",
    "price": "361.986667",
    "priceChange24h": "8.76",
    "priceChangePct24h": "2.479993958100564361",
    "priceHistory24h": [
      {
        "timestamp": 1755802800000,
        "price": "353.226667"
      },
      {
        "timestamp": 1755803700000,
        "price": "353.216667"
      },
      "..."
    ],
    "totalHolders": 7,
    "sharesMultiplier": "1",
    "tradableSessions": [
      "premarket",
      "regular",
      "postmarket",
      "overnight"
    ]
  },
  "underlyingMarket": {
    "ticker": "ADBE",
    "name": "Adobe Inc.",
    "price": "361.986667",
    "priceHigh52w": "587.75",
    "priceLow52w": "330.04",
    "volume": "1851321",
    "averageVolume": "3610882",
    "sharesOutstanding": "424200000",
    "marketCap": "149925006000"
  },
  "constituentTokens": [],
  "timestamp": 1755890061815
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "invalid symbol; must be at least 3 characters long and end with 'on'",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#invalid_symbol"
}
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "The provided asset symbol does not exist and cannot be found.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_not_found"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Market data behaves differently by asset type. For standard tokens, `underlyingMarket` is populated and `constituentTokens` is an empty array. For Ondo Intelligent Portfolios (OIPs), `underlyingMarket` is `null` and `constituentTokens` lists the portfolio’s constituent GM token symbols.

#### Authorizations

x-api-key

string

header

required

#### Path Parameters

symbol

string

required

The GM token symbol

#### Response

200

application/json

OK

primaryMarket

object

required

Hide child attributes

primaryMarket.symbol

string

The GM symbol of the asset.

Example:

`"AAPLon"`

primaryMarket.price

string

The current price of the asset, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

primaryMarket.priceChange24h

string

The price change in the last 24 hours of open market.

Example:

`"0.123"`

primaryMarket.priceChangePct24h

string

The percentage change in price over the last 24 hours of open market.

Example:

`"5.45"`

primaryMarket.priceHistory24h

object[]

Historical price data for the last 24 hours of open market.

Show child attributes

primaryMarket.totalHolders

number

The total number of holders for the asset

Example:

`1234`

primaryMarket.sharesMultiplier

string

The number of shares each token is equivalent to, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1.25"`

primaryMarket.tradableSessions

enum<string>[]

The trading sessions during which this asset is available for trading. Includes `offhours` for assets that opt in to off-hours trading (weekends, the window after the Friday postmarket close, or eligible holidays). `offhours` is only included when off-hours trading is enabled.

Available options:

`premarket`,

`regular`,

`postmarket`,

`overnight`,

`offhours`

Example:

```
[  
  "premarket",  
  "regular",  
  "postmarket",  
  "overnight",  
  "offhours"  
]
```

underlyingMarket

object | null

required

The off-chain stock that backs the token. This is `null` for tokens that represent several underlying assets rather than a single stock; for those, see `constituentTokens`. For a token backed by a single stock, this object is populated as shown.

Hide child attributes

underlyingMarket.ticker

string

The stock ticker associated with the asset.

Example:

`"AAPL"`

underlyingMarket.name

string

The company's name.

Example:

`"Apple Inc"`

underlyingMarket.price

string

The current price of the underlying stock, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"195.34"`

underlyingMarket.priceHigh52w

string

The highest trading price in the past 52 weeks, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"259.47"`

underlyingMarket.priceLow52w

string

The lowest trading price in the past 52 weeks, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"168.99"`

underlyingMarket.volume

string

The total trading volume in the past 24 hours, represented as a string-encoded integer.

Example:

`"43020691"`

underlyingMarket.averageVolume

string

The average trading volume over the past year, represented as a string-encoded integer.

Example:

`"38390632"`

underlyingMarket.sharesOutstanding

string

The total number of shares outstanding, represented as a string-encoded integer.

Example:

`"14935800000"`

underlyingMarket.marketCap

string

The total market capitalization in USD, represented as a string-encoded integer.

Example:

`"2934137946000"`

constituentTokens

string[]

required

GM token symbols of the underlying assets that make up this token, for tokens that represent several underlying assets rather than a single stock. Each symbol can be looked up individually via the market endpoints. For a token backed by a single stock this is an empty array (`[]`), and `underlyingMarket` is populated instead.

Example:

```
["AAPLon", "MSFTon", "NVDAon"]
```

timestamp

number

required

The Unix timestamp in milliseconds when the data was last updated.

Example:

`1746655938000`

[Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets)[Get Dividend Information for an Asset](https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The trading sessions during which this asset is available for trading. Includes offhours for assets that opt in to off-hours trading (weekends, the window after the Friday postmarket close, or eligible holidays). offhours is only included when off-hours trading is enabled.
- Available options: premarket, regular, postmarket, overnight, offhours

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset","name":"Get Market Data for an Asset","description":"This endpoint retrieves comprehensive market data for a specific asset, containing both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The \"Tradable Sessions\" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.501Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Market Data for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset#apireference","headline":"Get Market Data for an Asset","name":"Get Market Data for an Asset","description":"This endpoint retrieves comprehensive market data for a specific asset, containing both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The \"Tradable Sessions\" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.501Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```