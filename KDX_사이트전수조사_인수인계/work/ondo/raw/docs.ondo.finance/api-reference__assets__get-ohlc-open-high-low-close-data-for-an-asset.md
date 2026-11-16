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