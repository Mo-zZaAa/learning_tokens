# 읽기 묶음: docs.ondo.finance / api-reference (2/5)


<<<PAGE https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset>>>
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

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets
title: Get Metadata for All Supported Assets - Ondo Finance
description: Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Metadata for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/metadata \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/metadata"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/metadata', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/metadata",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/metadata"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/metadata")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/metadata")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "symbol": "AAPLon",
    "ticker": "AAPL",
    "underlyingName": "Apple",
    "displayName": "Apple (Ondo Tokenized)",
    "coingeckoId": "apple-ondo-tokenized-stock",
    "coinmarketCapId": "38037",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0x390a684ef9cade28a7ad0dfa61ab1eb3842618c4",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
        "decimals": 18
      }
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0378331005",
    "logoURI": "https://assets.coingecko.com/coins/images/56760/large/aaplon.png",
    "isPortfolio": false
  },
  {
    "symbol": "ABNBon",
    "ticker": "ABNB",
    "underlyingName": "Airbnb",
    "displayName": "Airbnb (Ondo Tokenized)",
    "coingeckoId": "airbnb-ondo-tokenized-stock",
    "coinmarketCapId": "38044",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0xef80743f78d98fc2b47a2253b293152ce8b879ba",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0xb035c3d5083bdc80074f380aebc9fcb68aba0a28",
        "decimals": 18
      }
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0090661010",
    "logoURI": "https://assets.coingecko.com/coins/images/56774/large/abnbon.png",
    "isPortfolio": false
  },
  "..."
]
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

# Get Metadata for All Supported Assets

Copy pageCopy page

Returns all metadata for all symbols including identifiers, addresses, and classification tags.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

assets

/

all

/

metadata

Try it

Get Metadata for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/metadata \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/metadata"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/metadata', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/metadata",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/metadata"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/metadata")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/metadata")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "symbol": "AAPLon",
    "ticker": "AAPL",
    "underlyingName": "Apple",
    "displayName": "Apple (Ondo Tokenized)",
    "coingeckoId": "apple-ondo-tokenized-stock",
    "coinmarketCapId": "38037",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0x390a684ef9cade28a7ad0dfa61ab1eb3842618c4",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
        "decimals": 18
      }
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0378331005",
    "logoURI": "https://assets.coingecko.com/coins/images/56760/large/aaplon.png",
    "isPortfolio": false
  },
  {
    "symbol": "ABNBon",
    "ticker": "ABNB",
    "underlyingName": "Airbnb",
    "displayName": "Airbnb (Ondo Tokenized)",
    "coingeckoId": "airbnb-ondo-tokenized-stock",
    "coinmarketCapId": "38044",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0xef80743f78d98fc2b47a2253b293152ce8b879ba",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0xb035c3d5083bdc80074f380aebc9fcb68aba0a28",
        "decimals": 18
      }
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0090661010",
    "logoURI": "https://assets.coingecko.com/coins/images/56774/large/abnbon.png",
    "isPortfolio": false
  },
  "..."
]
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

#### Authorizations

x-api-key

string

header

required

#### Response

200

application/json

OK

symbol

string

required

Example:

`"AAPLon"`

ticker

string

required

Example:

`"AAPL"`

tags

object

required

Hide child attributes

tags.assetClass

string

required

High-level category of the asset

Example:

`"equities"`

tags.instrumentType

string

required

Instrument type within the asset class

Example:

`"stock"`

tags.sectorIndustry

string[]

Sector and industry classifications for the asset.

Example:

```
["Technology", "Consumer Electronics"]
```

tags.typeFactorRiskProfile

string[]

Type, factor, and risk profile classifications.

Example:

```
["Growth", "Large Cap"]
```

tags.regionMarketExposure

string[]

Region and market exposure classifications.

Example:

```
["US", "Global"]
```

underlyingName

string

Human-readable name of the underlying instrument. Empty string if no name is available for this asset.

Example:

`"Apple"`

displayName

string

Token name as shown in user interfaces. Empty string if no name is available for this asset.

Example:

`"Apple (Ondo Tokenized)"`

coingeckoId

string | null

Example:

`"apple-ondo-tokenized-stock"`

addresses

object[]

Contract addresses for various chains.

Hide child attributes

addresses.networkChainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

addresses.address

string

required

The contract address on the specified chain.

Example:

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

addresses.decimals

integer<int64>

required

The number of decimals places for the asset.

Example:

`18`

Example:

```
[  
  {  
    "networkChainId": "bsc-56",  
    "address": "0x390a684ef9cade28a7ad0dfa61ab1eb3842618c4",  
    "decimals": 18  
  },  
  {  
    "networkChainId": "ethereum-1",  
    "address": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",  
    "decimals": 18  
  }  
]
```

coinmarketcapId

string | null

Example:

`"38037"`

isin

string

The 12-character International Securities Identification Number (ISIN) for the underlying instrument. Empty string if unknown or not applicable (e.g., non-equity assets).

Example:

`"US0378331005"`

logoURI

string

URL to the asset's logo image. Empty string if no logo is available for this asset.

Example:

`"https://assets.coingecko.com/coins/images/56760/large/aaplon.png"`

isPortfolio

boolean

Example:

`false`

[Get Contract Addresses for an Asset](https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset)[Get Shares Multiplier History for an Asset](https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- enum<string>required
- Available options: ethereum-1, bsc-56, solana-900
- integer<int64>required

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets","name":"Get Metadata for All Supported Assets","description":"Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.569Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Metadata for All Supported Assets","item":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#apireference","headline":"Get Metadata for All Supported Assets","name":"Get Metadata for All Supported Assets","description":"Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#webpage"},"dateModified":"2026-11-12T23:40:59.569Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset
title: Get OHLC (Open, High, Low, Close) Data for an Asset - Ondo Finance
description: This endpoint retrieves historical Open, High, Low, Close (OHLC) price data for both the primary market (on-chain token) and underlying market (off-chain stock) for a specified asset. This endpoint returns historical candles. To receive live, minute-bucketed OHLC updates as they occur, use the OHLC Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. The interval parameter determines the bucket size for data points, while the range parameter determines how far back historically to look for price data. See below for valid interval/range pairs. Valid interval/range pairs: - 1min/1day (rolling 24-hour period of open market data) - 5min/1day - 15min/1day - 1hour/1month - 4hour/1month - 12hour/3month - 1day/3month - 1day/6month - 1day/1year - 1day/all (all historical data) Note on range=1day and off-hours-tradable assets: For assets that are tradable during the off-hours session, the 1day range returns a plain rolling 24-hour calendar window so weekend and off-hours candles are included. For all other assets, the 1day range returns a market-hours-aware rolling 24-hour window over open market data. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get OHLC (Open, High, Low, Close) Data for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc")

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
  "interval": "1day",
  "range": "3month",
  "primaryMarket": {
    "symbol": "BABAon",
    "data": [
      {
        "timestamp": 1750723200000,
        "open": "117.0544",
        "high": "117.3426",
        "low": "117.0544",
        "close": "117.3426"
      },
      {
        "timestamp": 1750809600000,
        "open": "117.87",
        "high": "117.87",
        "low": "114.3677",
        "close": "114.8076"
      },
      "..."
    ]
  },
  "underlyingMarket": {
    "ticker": "BABA",
    "data": [
      {
        "timestamp": 1750723200000,
        "open": "117.0544",
        "high": "117.3426",
        "low": "117.0544",
        "close": "117.3426"
      },
      {
        "timestamp": 1750809600000,
        "open": "117.87",
        "high": "117.87",
        "low": "114.3677",
        "close": "114.8076"
      },
      "..."
    ]
  }
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

# Get OHLC (Open, High, Low, Close) Data for an Asset

Copy pageCopy page

This endpoint retrieves historical Open, High, Low, Close (OHLC) price data for both the primary market (on-chain token) and underlying market (off-chain stock) for a specified asset.

This endpoint returns historical candles. To receive live, minute-bucketed OHLC updates as they occur, use the [OHLC Streaming](https://docs.ondo.finance/api-reference/ohlc-streaming) endpoint.

Prices are intended for display only. For real-time trading prices, use the [Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote) API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact [support@ondo.finance](mailto:support@ondo.finance).

The `interval` parameter determines the bucket size for data points, while the `range` parameter determines how far back historically to look for price data. See below for valid interval/range pairs.

Valid `interval`/`range` pairs:

* 1min/1day *(rolling 24-hour period of open market data)*
* 5min/1day
* 15min/1day
* 1hour/1month
* 4hour/1month
* 12hour/3month
* 1day/3month
* 1day/6month
* 1day/1year
* 1day/all *(all historical data)*

**Note on `range=1day` and off-hours-tradable assets:** For assets that are tradable during the off-hours session, the `1day` range returns a plain rolling 24-hour calendar window so weekend and off-hours candles are included. For all other assets, the `1day` range returns a market-hours-aware rolling 24-hour window over open market data.

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

prices

/

ohlc

Try it

Get OHLC (Open, High, Low, Close) Data for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/ohlc")

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
  "interval": "1day",
  "range": "3month",
  "primaryMarket": {
    "symbol": "BABAon",
    "data": [
      {
        "timestamp": 1750723200000,
        "open": "117.0544",
        "high": "117.3426",
        "low": "117.0544",
        "close": "117.3426"
      },
      {
        "timestamp": 1750809600000,
        "open": "117.87",
        "high": "117.87",
        "low": "114.3677",
        "close": "114.8076"
      },
      "..."
    ]
  },
  "underlyingMarket": {
    "ticker": "BABA",
    "data": [
      {
        "timestamp": 1750723200000,
        "open": "117.0544",
        "high": "117.3426",
        "low": "117.0544",
        "close": "117.3426"
      },
      {
        "timestamp": 1750809600000,
        "open": "117.87",
        "high": "117.87",
        "low": "114.3677",
        "close": "114.8076"
      },
      "..."
    ]
  }
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

#### Query Parameters

interval

enum<string>

required

The time interval between data points.

Available options:

`1min`,

`5min`,

`15min`,

`1hour`,

`4hour`,

`12hour`,

`1day`

range

enum<string>

required

The lookback range for historical data.
The look back range for historical data. (Note that '1day' will return a rolling 24-hour period of data and 'all' will return all historical data.)

Available options:

`1day`,

`1month`,

`3month`,

`6month`,

`1year`,

`all`

#### Response

200

application/json

OK

interval

enum<string>

required

The time interval between data points.

Available options:

`1min`,

`5min`,

`15min`,

`1hour`,

`4hour`,

`12hour`,

`1day`

range

enum<string>

required

The look back range for historical data. (Note that '1day' will return a rolling 24-hour period of data and 'all' will return all historical data.)

Available options:

`1day`,

`1month`,

`3month`,

`6month`,

`1year`,

`all`

primaryMarket

object

required

Hide child attributes

primaryMarket.symbol

string

The GM symbol associated with the asset.

Example:

`"AAPLon"`

primaryMarket.data

object[]

Show child attributes

underlyingMarket

object

required

Hide child attributes

underlyingMarket.ticker

string

The stock ticker associated with the asset.

Example:

`"AAPL"`

underlyingMarket.data

object[]

Show child attributes

[Get Enhanced Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets)[Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset","name":"Get OHLC (Open, High, Low, Close) Data for an Asset","description":"This endpoint retrieves historical Open, High, Low, Close (OHLC) price data for both the primary market (on-chain token) and underlying market (off-chain stock) for a specified asset. This endpoint returns historical candles. To receive live, minute-bucketed OHLC updates as they occur, use the OHLC Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. The interval parameter determines the bucket size for data points, while the range parameter determines how far back historically to look for price data. See below for valid interval/range pairs. Valid interval/range pairs: - 1min/1day (rolling 24-hour period of open market data) - 5min/1day - 15min/1day - 1hour/1month - 4hour/1month - 12hour/3month - 1day/3month - 1day/6month - 1day/1year - 1day/all (all historical data) Note on range=1day and off-hours-tradable assets: For assets that are tradable during the off-hours session, the 1day range returns a plain rolling 24-hour calendar window so weekend and off-hours candles are included. For all other assets, the 1day range returns a market-hours-aware rolling 24-hour window over open market data. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.469Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get OHLC (Open, High, Low, Close) Data for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset#apireference","headline":"Get OHLC (Open, High, Low, Close) Data for an Asset","name":"Get OHLC (Open, High, Low, Close) Data for an Asset","description":"This endpoint retrieves historical Open, High, Low, Close (OHLC) price data for both the primary market (on-chain token) and underlying market (off-chain stock) for a specified asset. This endpoint returns historical candles. To receive live, minute-bucketed OHLC updates as they occur, use the OHLC Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. The interval parameter determines the bucket size for data points, while the range parameter determines how far back historically to look for price data. See below for valid interval/range pairs. Valid interval/range pairs: - 1min/1day (rolling 24-hour period of open market data) - 5min/1day - 15min/1day - 1hour/1month - 4hour/1month - 12hour/3month - 1day/3month - 1day/6month - 1day/1year - 1day/all (all historical data) Note on range=1day and off-hours-tradable assets: For assets that are tradable during the off-hours session, the 1day range returns a plain rolling 24-hour calendar window so weekend and off-hours candles are included. For all other assets, the 1day range returns a market-hours-aware rolling 24-hour window over open market data. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.469Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset
title: Get Shares Multiplier History for an Asset - Ondo Finance
description: This endpoint retrieves the shares multiplier history for a specific asset. Note that some asset events do not result in the shares multiplier value changing. This endpoint will show the earliest timestamp for each value change. The range parameter determines how far back historically to look for shares multiplier data. See below for valid range values. Valid range values: - 1day - 1month - 3month - 6month - 1year - all (all historical data) For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Shares Multiplier History for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier")

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
  "history": [
    {
      "sharesMultiplier": "0.481891643381832405",
      "changeTimestamp": 1762736520093,
      "reason": "cash_dividend"
    },
    {
      "sharesMultiplier": "0.481566453805576042",
      "changeTimestamp": 1754870400044,
      "reason": "cash_dividend"
    },
    {
      "sharesMultiplier": "0.481185641420460013",
      "changeTimestamp": 1753992000000,
      "reason": "cash_dividend"
    },
    "..."
  ],
  "timestamp": 1770161184102
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

# Get Shares Multiplier History for an Asset

Copy pageCopy page

This endpoint retrieves the shares multiplier history for a specific asset. Note that some asset events do not result in the shares multiplier value changing. This endpoint will show the earliest timestamp for each value change.

The `range` parameter determines how far back historically to look for shares multiplier data. See below for valid range values.

Valid `range` values:

* 1day
* 1month
* 3month
* 6month
* 1year
* all *(all historical data)*

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

shares-multiplier

Try it

Get Shares Multiplier History for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/shares-multiplier")

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
  "history": [
    {
      "sharesMultiplier": "0.481891643381832405",
      "changeTimestamp": 1762736520093,
      "reason": "cash_dividend"
    },
    {
      "sharesMultiplier": "0.481566453805576042",
      "changeTimestamp": 1754870400044,
      "reason": "cash_dividend"
    },
    {
      "sharesMultiplier": "0.481185641420460013",
      "changeTimestamp": 1753992000000,
      "reason": "cash_dividend"
    },
    "..."
  ],
  "timestamp": 1770161184102
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

#### Query Parameters

range

enum<string>

required

The lookback range for historical data.
The look back range for historical data. (Note that '1day' will return a rolling 24-hour period of data and 'all' will return all historical data.)

Available options:

`1day`,

`1month`,

`3month`,

`6month`,

`1year`,

`all`

#### Response

200

application/json

OK

history

object[]

required

Hide child attributes

history.sharesMultiplier

string

required

The number of shares each token is equivalent to, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1.25"`

history.changeTimestamp

number

required

The Unix timestamp in milliseconds when this `sharesMultiplier` value was first set.

Example:

`1746655938000`

history.reason

enum<string>

required

The cause of this `sharesMultiplier` change. One of:

* `initialization`: The first entry of the asset's full shares multiplier history. This entry always has a `sharesMultiplier` of 1. It only appears when the requested `range` reaches back to the start of the history.
* `cash_dividend`: A cash dividend was reinvested.
* `stock_dividend`: A stock dividend was distributed.
* `stock_split`: A stock split occurred.
* `spinoff`: A spinoff occurred.
* `other`: Any change not attributable to one of the corporate actions above, such as internal updates. If the requested `range` starts after the beginning of the asset's history, the first data point reports `other` unless it corresponds to an actual multiplier change within that range.

Available options:

`initialization`,

`cash_dividend`,

`stock_dividend`,

`stock_split`,

`spinoff`,

`other`

Example:

`"cash_dividend"`

timestamp

number

required

The Unix timestamp in milliseconds when the data point was recorded.

Example:

`1746655938000`

[Get Metadata for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets)[Get All Portfolios](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The Unix timestamp in milliseconds when this sharesMultiplier value was first set.
- The cause of this sharesMultiplier change. One of:
- initialization: The first entry of the asset's full shares multiplier history. This entry always has a sharesMultiplier of 1. It only appears when the requested range reaches back to the start of the history.
- cash_dividend: A cash dividend was reinvested.
- stock_dividend: A stock dividend was distributed.
- stock_split: A stock split occurred.
- spinoff: A spinoff occurred.
- other: Any change not attributable to one of the corporate actions above, such as internal updates. If the requested range starts after the beginning of the asset's history, the first data point reports other unless it corresponds to an actual multiplier change within that range.
- Available options: initialization, cash_dividend, stock_dividend, stock_split, spinoff, other

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset","name":"Get Shares Multiplier History for an Asset","description":"This endpoint retrieves the shares multiplier history for a specific asset. Note that some asset events do not result in the shares multiplier value changing. This endpoint will show the earliest timestamp for each value change. The range parameter determines how far back historically to look for shares multiplier data. See below for valid range values. Valid range values: - 1day - 1month - 3month - 6month - 1year - all (all historical data) For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.585Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Shares Multiplier History for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset#apireference","headline":"Get Shares Multiplier History for an Asset","name":"Get Shares Multiplier History for an Asset","description":"This endpoint retrieves the shares multiplier history for a specific asset. Note that some asset events do not result in the shares multiplier value changing. This endpoint will show the earliest timestamp for each value change. The range parameter determines how far back historically to look for shares multiplier data. See below for valid range values. Valid range values: - 1day - 1month - 3month - 6month - 1year - all (all historical data) For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.585Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation>>>
---
url: https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation
title: Request a Mint or Redeem Attestation - Ondo Finance
description: An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes
fetched: 2026-11-16
method: render
plan: read
---

Request a Mint or Redeem Attestation

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000",
  "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000",
    "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    symbol: 'AAPLon',
    tokenAmount: '5.000000000000000000',
    userAddress: '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  })
};

fetch('https://api.gm.ondo.finance/v1/attestations', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000',
    'userAddress' => '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "attestationId": "229852750420835981756873903928305653446",
  "userId": "0x474d0000000000009310097834e2c7af00000000000000000000000000000000",
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535",
  "expiration": 1746655938,
  "signature": "kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs=",
  "additionalData": ""
}
```

Attestations

# Request a Mint or Redeem Attestation

Copy pageCopy page

An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of `short` for a tighter price spread or `long` for an extended validity period.

Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits) endpoint.

See also: [Error Codes](https://docs.ondo.finance/api-reference/error-codes)

Copy pageCopy page

POST

/

v1

/

attestations

Try it

Request a Mint or Redeem Attestation

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000",
  "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000",
    "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    symbol: 'AAPLon',
    tokenAmount: '5.000000000000000000',
    userAddress: '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  })
};

fetch('https://api.gm.ondo.finance/v1/attestations', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000',
    'userAddress' => '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "attestationId": "229852750420835981756873903928305653446",
  "userId": "0x474d0000000000009310097834e2c7af00000000000000000000000000000000",
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535",
  "expiration": 1746655938,
  "signature": "kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs=",
  "additionalData": ""
}
```

#### Authorizations

x-api-key

string

header

required

#### Body

application/json

Request a mint or redeem attestation.

* AttestationByTokenAmountRequest
* AttestationByNotionalValueRequest

Request to mint or redeem assets equal to the notional value.

chainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

side

enum<string>

required

The direction of the trade.

Available options:

`buy`,

`sell`

notionalValue

string

required

Total value of assets, represented as a string-encoded decimal with up to 18 digits after the decimal point. Must be greater than 0 and less than 1e20.

Example:

`"500.000000000000000000"`

duration

enum<string>

Specifies the desired validity period for the attestation. Users can specify a duration of 'short'
for a tighter price spread or 'long' for an extended validity period.

Available options:

`short`,

`long`

userAddress

string

The Solana user address associated with the request. This is only required for Solana attestations.

Example:

`"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"`

#### Response

200

application/json

OK

attestationId

string

required

The attestation's unique identifier.

Example:

`"229852750420835981756873903928305653446"`

userId

string

required

The onchain identifier for an association of wallets.

Example:

`"0x474d0000000000009310097834e2c7af00000000000000000000000000000000"`

chainId

string

required

The chain's identifier, only including the chain id.

Example:

`"1"`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

ticker

string

required

The stock ticker associated with this attestation.

Example:

`"AAPL"`

assetAddress

string

required

The contract address of the symbol.

Example:

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

side

enum<string>

required

The direction of the trade (0 for buy, 1 for sell).

Available options:

`0`,

`1`

Example:

`"0"`

tokenAmount

string

required

The number of tokens to mint/redeem represented as a string with 18 decimal places.

Example:

`"5000000000000000000"`

price

string

required

The price per asset in USDon, represented as a string with up to 18 decimal places.

Example:

`"225273151158540753535"`

expiration

number

required

The epoch timestamp when the attestation will expire.

Example:

`1746655938`

signature

string

required

The base64-encoded signature attesting to the quote.

Example:

`"kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs="`

additionalData

string

required

Base64-encoded additional data to provide within the attestation.

Example:

`""`

[Quickstart](https://docs.ondo.finance/api-reference/quickstart)[Request a Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#webpage","url":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation","name":"Request a Mint or Redeem Attestation","description":"An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes","dateModified":"2026-11-12T23:40:59.389Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Request a Mint or Redeem Attestation","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#apireference","headline":"Request a Mint or Redeem Attestation","name":"Request a Mint or Redeem Attestation","description":"An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes","url":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#webpage"},"dateModified":"2026-11-12T23:40:59.389Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote>>>
---
url: https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote
title: Request a Soft Attestation Quote - Ondo Finance
description: A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes
fetched: 2026-11-16
method: render
plan: read
---

Request a Soft Attestation Quote

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations/soft \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations/soft"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({symbol: 'AAPLon', tokenAmount: '5.000000000000000000'})
};

fetch('https://api.gm.ondo.finance/v1/attestations/soft', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations/soft",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations/soft"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations/soft")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations/soft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x96F6eF951840721AdBF46Ac996b59E0235CB985C",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535"
}
```

Attestations

# Request a Soft Attestation Quote

Copy pageCopy page

A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the [Request a Mint or Redeem Attestation endpoint](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation), soft quotes:

* Are not eligible for on-chain submission
* Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations)
* Serve as pricing references for quote validation and user interface display
* Do not include authentication fields such as `attestationId`, `userId`, `expiration`, or `signature`

This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments.

See also: [Error Codes](https://docs.ondo.finance/api-reference/error-codes)

Copy pageCopy page

POST

/

v1

/

attestations

/

soft

Try it

Request a Soft Attestation Quote

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations/soft \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations/soft"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({symbol: 'AAPLon', tokenAmount: '5.000000000000000000'})
};

fetch('https://api.gm.ondo.finance/v1/attestations/soft', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations/soft",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations/soft"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations/soft")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations/soft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x96F6eF951840721AdBF46Ac996b59E0235CB985C",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535"
}
```

#### Authorizations

x-api-key

string

header

required

#### Body

application/json

* AttestationByTokenAmountRequest
* AttestationByNotionalValueRequest

Request a soft quote to mint or redeem assets equal to the notional value.

chainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

side

enum<string>

required

The direction of the trade.

Available options:

`buy`,

`sell`

notionalValue

string

required

Total value of assets, represented as a string-encoded decimal with up to 18 digits after the decimal point. Must be greater than 0 and less than 1e20.

Example:

`"500.000000000000000000"`

duration

enum<string>

Specifies the desired validity period for the attestation. Users can specify a duration of 'short'
for a tighter price spread or 'long' for an extended validity period.

Available options:

`short`,

`long`

#### Response

200

application/json

OK

chainId

string

required

The chain's identifier, only including the chain id.

Example:

`"1"`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

ticker

string

required

The stock ticker associated with this attestation.

Example:

`"AAPL"`

assetAddress

string

required

The contract address of the symbol.

Example:

`"0x96F6eF951840721AdBF46Ac996b59E0235CB985C"`

side

enum<string>

required

The direction of the trade (0 for buy, 1 for sell).

Available options:

`0`,

`1`

tokenAmount

string

required

The number of tokens to mint/redeem represented as a string with 18 decimal places.

Example:

`"5000000000000000000"`

price

string

required

The price per asset in USDon, represented as a string with 18 decimal places.

Example:

`"225273151158540753535"`

[Request a Mint or Redeem Attestation](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation)[Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#webpage","url":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote","name":"Request a Soft Attestation Quote","description":"A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes","dateModified":"2026-11-12T23:40:59.406Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Attestations","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":3,"name":"Request a Soft Attestation Quote","item":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#apireference","headline":"Request a Soft Attestation Quote","name":"Request a Soft Attestation Quote","description":"A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes","url":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#webpage"},"dateModified":"2026-11-12T23:40:59.406Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token>>>
---
url: https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token
title: Get Token Balances for a User or Token - Ondo Finance
description: This endpoint retrieves all token balances for a GM Chain. Results can be optionally filtered by tokenAddress, userAddress, or both parameters together. If no filters are provided, all balances on the chain will be returned. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Token Balances for a User or Token

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/chains/{chainId}/balances \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/chains/{chainId}/balances"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/chains/{chainId}/balances', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/chains/{chainId}/balances",
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

	url := "https://api.gm.ondo.finance/v1/chains/{chainId}/balances"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/chains/{chainId}/balances")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/chains/{chainId}/balances")

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

429

500

```
{
  "tokens": [
    {
      "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
      "tokenSymbol": "AAPLon",
      "balances": [
        {
          "holderAddress": {
            "account": "0x13116e8b4ffc8125b859ec60917fba540e59e55e"
          },
          "balance": "0.467583800117038432"
        },
        {
          "holderAddress": {
            "account": "0x1db995cb2b3d9679383f0e597704a41e1521f4e1"
          },
          "balance": "0.641380199330235549"
        }
      ]
    },
    {
      "tokenAddress": "0xf6b1117ec07684d3958cad8beb1b302bfd21103f",
      "tokenSymbol": "TSLAon",
      "balances": [
        {
          "holderAddress": {
            "account": "0x00000688768803bbd44095770895ad27ad6b0d95"
          },
          "balance": "0.030594824589372964"
        },
        {
          "holderAddress": {
            "account": "0x1db995cb2b3d9679383f0e597704a41e1521f4e1"
          },
          "balance": "0.088854297224463519"
        }
      ]
    },
    "..."
  ]
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

Chains

# Get Token Balances for a User or Token

Copy pageCopy page

This endpoint retrieves all token balances for a GM Chain. Results can be optionally filtered by `tokenAddress`, `userAddress`, or both parameters together. If no filters are provided, all balances on the chain will be returned.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

chains

/

{chainId}

/

balances

Try it

Get Token Balances for a User or Token

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/chains/{chainId}/balances \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/chains/{chainId}/balances"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/chains/{chainId}/balances', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/chains/{chainId}/balances",
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

	url := "https://api.gm.ondo.finance/v1/chains/{chainId}/balances"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/chains/{chainId}/balances")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/chains/{chainId}/balances")

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

429

500

```
{
  "tokens": [
    {
      "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
      "tokenSymbol": "AAPLon",
      "balances": [
        {
          "holderAddress": {
            "account": "0x13116e8b4ffc8125b859ec60917fba540e59e55e"
          },
          "balance": "0.467583800117038432"
        },
        {
          "holderAddress": {
            "account": "0x1db995cb2b3d9679383f0e597704a41e1521f4e1"
          },
          "balance": "0.641380199330235549"
        }
      ]
    },
    {
      "tokenAddress": "0xf6b1117ec07684d3958cad8beb1b302bfd21103f",
      "tokenSymbol": "TSLAon",
      "balances": [
        {
          "holderAddress": {
            "account": "0x00000688768803bbd44095770895ad27ad6b0d95"
          },
          "balance": "0.030594824589372964"
        },
        {
          "holderAddress": {
            "account": "0x1db995cb2b3d9679383f0e597704a41e1521f4e1"
          },
          "balance": "0.088854297224463519"
        }
      ]
    },
    "..."
  ]
}
```

```
{
  "code": "INVALID_SYMBOL",
  "message": "One of the request parameters is invalid.",
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

#### Authorizations

x-api-key

string

header

required

#### Path Parameters

chainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

#### Query Parameters

tokenAddress

string

Filter by a token contract address (optional).

userAddress

string

Filter by a user wallet address (optional).

#### Response

200

application/json

OK

tokens

object[]

required

Hide child attributes

tokens.tokenAddress

string

required

The contract address of the token on the specified chain.

tokens.tokenSymbol

string

required

The symbol of the token on the specified chain.

tokens.balances

object[]

required

Show child attributes

[Get Price and Volume Data for All Supported Tickers](https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers)[Get Token Info](https://docs.ondo.finance/api-reference/chains/get-token-info)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- stringrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token#webpage","url":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token","name":"Get Token Balances for a User or Token","description":"This endpoint retrieves all token balances for a GM Chain. Results can be optionally filtered by tokenAddress, userAddress, or both parameters together. If no filters are provided, all balances on the chain will be returned. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.647Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Token Balances for a User or Token","item":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token#apireference","headline":"Get Token Balances for a User or Token","name":"Get Token Balances for a User or Token","description":"This endpoint retrieves all token balances for a GM Chain. Results can be optionally filtered by tokenAddress, userAddress, or both parameters together. If no filters are provided, all balances on the chain will be returned. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token#webpage"},"dateModified":"2026-11-12T23:40:59.647Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```