# 읽기 묶음: docs.ondo.finance / api-reference (4/5)


<<<PAGE https://docs.ondo.finance/api-reference/limits/get-trading-limits>>>
---
url: https://docs.ondo.finance/api-reference/limits/get-trading-limits
title: Get Trading Limits - Ondo Finance
description: Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The "Max Notional Value" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \$1,000,000, and has 30 non-expired, non-filled attestations at a value of \$999,000, they will not be able to request another attestation for \$1000. - The "Remaining Attestations" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: static
plan: read
---

Get Trading Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/trading \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/trading"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/trading', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/trading",
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

	url := "https://api.gm.ondo.finance/v1/limits/trading"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/trading")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/trading")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "timestamp": 1746655938000,
  "symbol": "AAPLon",
  "side": "buy",
  "maxTokens": "100.000000000000000000",
  "maxNotionalValue": "1234.560000000000000000",
  "remainingAttestations": "3",
  "isAssetTradingOpen": false,
  "reason": {
    "message": "Weekend/Holiday",
    "documentation": "https://docs.ondo.finance/",
    "code": "MARKET_CLOSED"
  }
}
```

Limits

# Get Trading Limits

Copy pageCopy page

Provides real-time trading limits based on global, user, and asset-specific exposure limits.

Limits:

* The “Max Notional Value” limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of $1,000,000, and has 30 non-expired, non-filled attestations at a value of $999,000, they will not be able to request another attestation for $1000.
* The “Remaining Attestations” limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another.

If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status).

**Trading Limits Reason Codes**

When trading is not allowed, the response will include a `reason` field which may include one of the following common codes:

* `MARKET_CLOSED`: Market is closed.
* `MARKET_PAUSED`: Market is temporarily paused.
* `ASSET_PAUSED`: Specific asset is paused.
* `ASSET_CLOSED_FOR_SESSION`: The asset is not tradable in this session (e.g., not available overnight; see [Get Market Data](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))
* `ASSET_LIMITED`: Asset can be traded, but order size is more limited than usual.
* `MAX_LIMIT_REACHED`: Maximum limit has been reached.
* `MAX_ATTESTATIONS`: Maximum attestations reached.
* `OFFHOURS_EXPOSURE_LIMIT_REACHED`: The off-hours exposure limit has been reached for the asset during the current off-hours session.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

limits

/

trading

Try it

Get Trading Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/trading \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/trading"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/trading', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/trading",
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

	url := "https://api.gm.ondo.finance/v1/limits/trading"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/trading")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/trading")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "timestamp": 1746655938000,
  "symbol": "AAPLon",
  "side": "buy",
  "maxTokens": "100.000000000000000000",
  "maxNotionalValue": "1234.560000000000000000",
  "remainingAttestations": "3",
  "isAssetTradingOpen": false,
  "reason": {
    "message": "Weekend/Holiday",
    "documentation": "https://docs.ondo.finance/",
    "code": "MARKET_CLOSED"
  }
}
```

#### Authorizations

x-api-key

string

header

required

#### Query Parameters

symbol

string

required

The GM token symbol.

side

enum<string>

required

The trade side
The direction of the trade.

Available options:

`buy`,

`sell`

#### Response

200

application/json

OK

timestamp

number

required

The Unix timestamp in milliseconds when the trading limits were last updated.

Example:

`1746655938000`

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

maxTokens

string

required

The maximum token amount available to trade, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"100.000000000000000000"`

maxNotionalValue

string

required

The maximum notional value available to trade, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1234.560000000000000000"`

remainingAttestations

string

required

The number of remaining attestations for this asset.

Example:

`"3"`

isAssetTradingOpen

boolean

required

Indicates whether the user is currently allowed to trade the asset

Example:

`false`

reason

object

Reason why trading is restricted for the given asset and user.

Show child attributes

[Get Token Info](https://docs.ondo.finance/api-reference/chains/get-token-info)[Get Session Limits](https://docs.ondo.finance/api-reference/limits/get-session-limits)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#webpage","url":"https://docs.ondo.finance/api-reference/limits/get-trading-limits","name":"Get Trading Limits","description":"Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The \"Max Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. - The \"Remaining Attestations\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.680Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Trading Limits","item":"https://docs.ondo.finance/api-reference/limits/get-trading-limits"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#apireference","headline":"Get Trading Limits","name":"Get Trading Limits","description":"Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The \"Max Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. - The \"Remaining Attestations\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/limits/get-trading-limits","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#webpage"},"dateModified":"2026-11-12T23:40:59.680Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/ohlc-streaming>>>
---
url: https://docs.ondo.finance/api-reference/ohlc-streaming
title: OHLC Streaming - Ondo Finance
description: gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.
fetched: 2026-11-16
method: render
plan: read
---

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamOHLC
```

Streamed

```
{
  "updates": [
    {
      "primaryMarket": {
        "symbol": "AAPLon",
        "open": "256.791808070580506978",
        "high": "257.013422018348623853",
        "low": "256.500000000000000000",
        "close": "256.901234567890123456"
      },
      "underlyingMarket": {
        "ticker": "AAPL",
        "open": "256.2475",
        "high": "256.47",
        "low": "255.96",
        "close": "256.36"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    },
    {
      "primaryMarket": {
        "symbol": "GOOGLon",
        "open": "305.39957516982939159",
        "high": "305.812345678901234567",
        "low": "304.900000000000000000",
        "close": "305.612345678901234567"
      },
      "underlyingMarket": {
        "ticker": "GOOGL",
        "open": "304.915",
        "high": "305.33",
        "low": "304.51",
        "close": "305.12"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    }
  ]
}
```

Streaming API

# OHLC Streaming

Copy pageCopy page

gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamOHLC
```

Streamed

```
{
  "updates": [
    {
      "primaryMarket": {
        "symbol": "AAPLon",
        "open": "256.791808070580506978",
        "high": "257.013422018348623853",
        "low": "256.500000000000000000",
        "close": "256.901234567890123456"
      },
      "underlyingMarket": {
        "ticker": "AAPL",
        "open": "256.2475",
        "high": "256.47",
        "low": "255.96",
        "close": "256.36"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    },
    {
      "primaryMarket": {
        "symbol": "GOOGLon",
        "open": "305.39957516982939159",
        "high": "305.812345678901234567",
        "low": "304.900000000000000000",
        "close": "305.612345678901234567"
      },
      "underlyingMarket": {
        "ticker": "GOOGL",
        "open": "304.915",
        "high": "305.33",
        "low": "304.51",
        "close": "305.12"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    }
  ]
}
```

The stream emits only live, in-progress candles; it does not backfill history. Candles are bucketed by minute and updated on every tick within the bucket. To load historical OHLC candles, use the REST [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset) endpoint. Both endpoints are intended to be used together to provide a complete picture. The REST endpoint provides historical candles to build the chart while the streaming endpoint keeps the chart up to date in real time.

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamOHLC`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more `OHLCUpdate` objects into a single `updates` array. Each update is a partial or closed minute candle for a single symbol, covering both the GM token (primary market) and the underlying stock (underlying market).

updates

OHLCUpdate[]

Array of OHLC updates.

Hide OHLCUpdate

primary\_market

object

OHLC candle for the GM token, keyed by `symbol`.

Hide primary\_market

symbol

string

Asset symbol.

open

string

Opening price for the bucket.

high

string

Highest price for the bucket.

low

string

Lowest price for the bucket.

close

string

Most recent price for the bucket.

underlying\_market

object

OHLC candle for the underlying stock, keyed by `ticker`.

Hide underlying\_market

ticker

string

Stock ticker.

open

string

Opening price for the bucket.

high

string

Highest price for the bucket.

low

string

Lowest price for the bucket.

close

string

Most recent price for the bucket.

is\_closed

boolean

Marks the final emission for the bucket (the minute boundary crossed). Subsequent updates with a higher timestamp belong to the next bucket.

timestamp

uint64

Bucket start (minute floor) in nanoseconds since epoch. Stable across all partials and the final closed update for a given bucket.

## Errors

Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[Price Streaming](https://docs.ondo.finance/api-reference/price-streaming)[Soft Quote Depth Streaming](https://docs.ondo.finance/api-reference/soft-quote-depth-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- primary_market
- OHLC candle for the GM token, keyed by symbol.
- Show primary_market
- underlying_market
- OHLC candle for the underlying stock, keyed by ticker.
- Show underlying_market
- is_closed
- Hide primary_market
- Hide underlying_market

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#webpage","url":"https://docs.ondo.finance/api-reference/ohlc-streaming","name":"OHLC Streaming","description":"gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.","dateModified":"2026-07-16T20:06:17.231Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"OHLC Streaming","item":"https://docs.ondo.finance/api-reference/ohlc-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#article","headline":"OHLC Streaming","name":"OHLC Streaming","description":"gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.","url":"https://docs.ondo.finance/api-reference/ohlc-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.231Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/overview>>>
---
url: https://docs.ondo.finance/api-reference/overview
title: Overview - Ondo Finance
description: An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [API Surfaces](https://docs.ondo.finance/api-reference/overview)
* [What the API Supports](https://docs.ondo.finance/api-reference/overview)
* [How It Works](https://docs.ondo.finance/api-reference/overview)
* [Get Access](https://docs.ondo.finance/api-reference/overview)

Home

# Overview

Copy pageCopy page

An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.

Copy pageCopy page

The Ondo API provides programmatic access to two onchain product lines: Ondo Stocks—tokenized publicly-traded US stocks and ETFs—and Ondo Intelligent Portfolios—curated investment portfolios delivered as single onchain transferable tokens.
Ondo Stocks tokenizes publicly-traded US stocks and ETFs, allowing investors outside the United States to mint, transfer, and redeem equity-backed tokens across multiple public blockchains. Ondo Stocks are available on Ethereum, BNB Chain, and Solana. On-chain assets are issued as ERC-20 tokens for EVM-based chains and as SPL Token-2022 tokens on Solana. Each token represents direct exposure to the underlying asset, held with a regulated custodian through a licensed broker-dealer.
Ondo Intelligent Portfolios builds on the foundation of Ondo Stocks: professionally constructed portfolios delivered as single onchain tokens. Each portfolio token provides economic exposure to a weighted basket of Ondo Stocks tokens managed to a defined allocation. Investors mint or redeem a single token to hold the full basket, without buying, weighting, or rebalancing individual positions themselves. Rebalancing back to base weights executes programmatically, and holdings, weights, and every rebalance are visible onchain. Ondo Intelligent Portfolios are available on Ethereum and BNB Chain and issued as ERC-20 tokens for EVM-based chains.
To support integration across the ecosystem, we offer a suite of APIs designed for infrastructure providers such as wallets, exchanges, and fintech applications covering both product lines.

**Terminology:** Throughout the REST and streaming APIs and onchain identifiers, Ondo Stocks & Intelligent Portfolios use the legacy `GM` prefix—for example, the symbol parameter is described as the “GM token symbol” and the REST spec is titled the “GM Backend API”. The smart contract manager depends on the product line: Ondo Stocks use `IGMTokenManager`, while Ondo Intelligent Portfolios use `PortfolioTokenManager`.

## API Surfaces

The API is delivered through two surfaces, alongside the on-chain smart contract layer. The REST API spec can be found at [docs.ondo.finance/openapi.json](https://docs.ondo.finance/openapi.json), and the streaming API’s [Protocol Buffers schema](https://docs.ondo.finance/api-reference/protobuf-schema) is available for generating typed clients.

## REST API

High-performance request/response access to essential pricing, quote generation, token lifecycle, and token contract metadata. The full OpenAPI specification is available for use with code generators and other tooling.

## Streaming API

Low-latency, real-time updates over gRPC so clients can react to market movements as they happen rather than polling. The Protocol Buffers schema is available for generating typed clients.

## What the API Supports

* [Generating mint and redemption attestations](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation) to generate quotes that are fed to the [smart contract layer](https://docs.ondo.finance/api-reference/smart-contracts).
* [Real-time price data](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) for Ondo Stocks & Intelligent Portfolios assets.
* [OHLC (Open, High, Low, Close) data](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset) to support charting, analytics, and historical views.
* [Portfolio details](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios) for Ondo Intelligent Portfolios, such as constituents, weights, dividend yields, fees, and rebalance data.
* [ITN assets, status, and limits](https://docs.ondo.finance/api-reference/itn/list-itn-assets) for minting and redeeming Ondo Stocks through Alpaca’s Instant Tokenization Network.
* [On chain mints and redemptions](https://docs.ondo.finance/api-reference/smart-contracts) that handle the core logic for minting and redeeming Ondo Stocks & Intelligent Portfolios.

The [smart contract layer](https://docs.ondo.finance/api-reference/smart-contracts) provides the ability to mint and redeem (buy/sell) the tokenized asset.

## How It Works

Here’s the typical flow for Ondo Stocks & Intelligent Portfolios, using the Ondo Stocks token TSLAon as an example:
**Minting Process:**

1. Primary Purchaser requests a mint attestation from the Ondo Stocks & Intelligent Portfolios API.
2. Primary Purchaser broadcasts transaction with the provided mint attestation signature along with a USD stablecoin (such as USDC) to the smart contract to atomically mint TSLAon to their whitelisted address.

**Redeeming Process:**

1. Primary Purchaser requests a redemption attestation from the Ondo Stocks & Intelligent Portfolios API.
2. Primary Purchaser broadcasts transaction with the provided redemption attestation signature along with TSLAon to the smart contract to atomically redeem TSLAon for a USD stablecoin (such as USDC) to their whitelisted address.

## Get Access

If you’re interested in getting access to the Ondo Stocks & Intelligent Portfolios API, reach out to [onboarding@ondo.finance](mailto:onboarding@ondo.finance).

[Quickstart](https://docs.ondo.finance/api-reference/quickstart)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/overview#webpage","url":"https://docs.ondo.finance/api-reference/overview","name":"Overview","description":"An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.","dateModified":"2026-11-07T00:34:22.067Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/overview#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/overview#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Overview","item":"https://docs.ondo.finance/api-reference/overview"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/overview#article","headline":"Overview","name":"Overview","description":"An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.","url":"https://docs.ondo.finance/api-reference/overview","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/overview#webpage"},"dateModified":"2026-11-07T00:34:22.067Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio>>>
---
url: https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio
title: Get a Portfolio - Ondo Finance
description: This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, "0.0009" is 0.09% and "0.1143" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get a Portfolio

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios/{symbol} \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios/{symbol}",
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

	url := "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios/{symbol}")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios/{symbol}")

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

503

```
{
  "symbol": "MAG7Xon",
  "name": "Ondo Magnificent 7 and Crypto Portfolio",
  "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
  "category": "thematic",
  "modelProvider": "ondo",
  "inceptionDate": "2026-08-12T16:35:00Z",
  "netAssetsUsd": "1885406.537181",
  "dividendYield": "0.00198929",
  "afterWithholdingDividendYield": "0.0013925",
  "fees": {
    "serviceFeeRateBeforeWaiver": "0.0009",
    "waiverFraction": "1",
    "serviceFeeRateAfterWaiver": "0"
  },
  "rebalance": {
    "frequency": "Quarterly",
    "reconstitutionType": "Fixed",
    "lastRebalanceDate": "2026-08-12T16:36:00Z"
  },
  "constituentCount": 9,
  "constituents": [
    {
      "symbol": "AAPLon",
      "name": "Apple",
      "quantity": "917.20457",
      "targetWeight": "0.1143",
      "currentWeight": "0.12556912",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Technology"
      ],
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
        },
        {
          "networkChainId": "solana-900",
          "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
          "decimals": 9
        }
      ]
    },
    {
      "symbol": "AMZNon",
      "name": "Amazon",
      "quantity": "905.66388",
      "targetWeight": "0.1143",
      "currentWeight": "0.10877632",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Consumer Discretionary"
      ],
      "addresses": [
        {
          "networkChainId": "bsc-56",
          "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
          "decimals": 18
        },
        {
          "networkChainId": "ethereum-1",
          "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
          "decimals": 18
        },
        {
          "networkChainId": "solana-900",
          "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
          "decimals": 9
        }
      ]
    },
    "..."
  ],
  "timestamp": 1791469800123
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
  "code": "RESOURCE_NOT_FOUND",
  "message": "portfolio not found",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#resource_not_found"
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Portfolios

# Get a Portfolio

Copy pageCopy page

This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio.

The response has the same fields as each entry of [Get All Portfolios](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios). The response sorts the constituents by symbol.

If the symbol is not an active portfolio, the endpoint returns the `RESOURCE_NOT_FOUND` error code with status `404`. Ondo Stocks symbols, such as `AAPLon`, also return this error.

Rates, weights, and yields are decimal fractions. For example, `"0.0009"` is 0.09% and `"0.1143"` is 11.43%. Dates are RFC 3339 timestamps in UTC.

This endpoint does not return prices. To get the price of a portfolio token, use [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset), [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset), or [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) with the portfolio symbol.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

portfolios

/

{symbol}

Try it

Get a Portfolio

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios/{symbol} \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios/{symbol}",
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

	url := "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios/{symbol}")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios/{symbol}")

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

503

```
{
  "symbol": "MAG7Xon",
  "name": "Ondo Magnificent 7 and Crypto Portfolio",
  "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
  "category": "thematic",
  "modelProvider": "ondo",
  "inceptionDate": "2026-08-12T16:35:00Z",
  "netAssetsUsd": "1885406.537181",
  "dividendYield": "0.00198929",
  "afterWithholdingDividendYield": "0.0013925",
  "fees": {
    "serviceFeeRateBeforeWaiver": "0.0009",
    "waiverFraction": "1",
    "serviceFeeRateAfterWaiver": "0"
  },
  "rebalance": {
    "frequency": "Quarterly",
    "reconstitutionType": "Fixed",
    "lastRebalanceDate": "2026-08-12T16:36:00Z"
  },
  "constituentCount": 9,
  "constituents": [
    {
      "symbol": "AAPLon",
      "name": "Apple",
      "quantity": "917.20457",
      "targetWeight": "0.1143",
      "currentWeight": "0.12556912",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Technology"
      ],
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
        },
        {
          "networkChainId": "solana-900",
          "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
          "decimals": 9
        }
      ]
    },
    {
      "symbol": "AMZNon",
      "name": "Amazon",
      "quantity": "905.66388",
      "targetWeight": "0.1143",
      "currentWeight": "0.10877632",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Consumer Discretionary"
      ],
      "addresses": [
        {
          "networkChainId": "bsc-56",
          "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
          "decimals": 18
        },
        {
          "networkChainId": "ethereum-1",
          "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
          "decimals": 18
        },
        {
          "networkChainId": "solana-900",
          "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
          "decimals": 9
        }
      ]
    },
    "..."
  ],
  "timestamp": 1791469800123
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
  "code": "RESOURCE_NOT_FOUND",
  "message": "portfolio not found",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#resource_not_found"
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
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

The portfolio token symbol

#### Response

200

application/json

OK

symbol

string

required

The portfolio token symbol.

Example:

`"MAG7Xon"`

name

string

required

The name of the portfolio.

Example:

`"Ondo Magnificent 7 and Crypto Portfolio"`

netAssetsUsd

string

required

The USD value of the constituents that the portfolio holds, represented as a string-encoded decimal with up to 6 digits after the decimal point. The value is the sum of each constituent `quantity` multiplied by its token price. It does not include cash from mints and redemptions that are not yet settled. For this reason, it can be slightly different from the token price multiplied by the total supply. If the portfolio has no supply, the value is `"0"`.

Example:

`"1885406.537181"`

dividendYield

string

required

The dividend yield of the portfolio, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.05" is the equivalent of 5%) The value is the average of the constituent dividend yields, weighted by `currentWeight`. The dividend yield of a constituent is the sum of its cash dividends paid in the last 365 days, divided by the current stock price. A constituent without dividends adds zero.

Example:

`"0.00198929"`

afterWithholdingDividendYield

string

required

The dividend yield of the portfolio after estimated withholding tax, represented as a string-encoded decimal with up to 8 digits after the decimal point. This value uses the same calculation as `dividendYield`, but it first subtracts the withholding tax from each dividend. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Example:

`"0.0013925"`

fees

object | null

required

The annual service fee of the portfolio. The value is `null` if no fee data is available. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Hide child attributes

fees.serviceFeeRateBeforeWaiver

string

required

The annual service fee rate before the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.0009" is the equivalent of 0.09%)

Example:

`"0.0009"`

fees.waiverFraction

string

required

The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of `"1"` waives the full fee. A value of `"0"` waives no fee.

Example:

`"1"`

fees.serviceFeeRateAfterWaiver

string

required

The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is `serviceFeeRateBeforeWaiver` multiplied by (1 - `waiverFraction`).

Example:

`"0"`

rebalance

object | null

required

The rebalance data of the portfolio. The value is `null` if no rebalance data is available. For more information, see [Rebalancing & Reconstitution](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution).

Hide child attributes

rebalance.frequency

string

required

The rebalance frequency of the portfolio, for example `Quarterly`. The value is free text, not a fixed list. Empty string if no frequency is available.

Example:

`"Quarterly"`

rebalance.reconstitutionType

string

required

The reconstitution approach of the portfolio, for example `Fixed`. The value is free text, not a fixed list. Empty string if no reconstitution type is available.

Example:

`"Fixed"`

rebalance.lastRebalanceDate

string<date-time>

The date of the most recent rebalance, as an RFC 3339 timestamp in UTC. The response omits this field if no rebalance date is available.

Example:

`"2026-08-12T16:36:00Z"`

constituentCount

integer<int32>

required

The number of constituents in `constituents`.

Example:

`9`

constituents

object[]

required

The constituents of the portfolio, sorted by symbol.

Hide child attributes

constituents.symbol

string

required

The GM token symbol of the constituent.

Example:

`"AAPLon"`

constituents.name

string

required

The name of the underlying asset. Empty string if no name is available.

Example:

`"Apple"`

constituents.quantity

string

required

The number of constituent tokens that the portfolio holds on all chains, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"917.20457"`

constituents.targetWeight

string

required

The target weight of the constituent in the portfolio model, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.1143" is the equivalent of 11.43%)

Example:

`"0.1143"`

constituents.currentWeight

string

required

The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent `quantity` multiplied by its token price, divided by `netAssetsUsd`. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to `targetWeight`.

Example:

`"0.12556912"`

constituents.assetClass

string

required

High-level category of the asset. Empty string if not available.

Example:

`"Equities"`

constituents.instrumentType

string

required

Instrument type within the asset class. Empty string if not available.

Example:

`"Stock"`

constituents.sectorIndustry

string[]

required

Sector and industry classifications for the asset. Empty array if not available.

Example:

```
["Technology"]
```

constituents.addresses

object[]

required

The contract addresses of the constituent token, sorted by `networkChainId`.

Show child attributes

timestamp

number

required

The Unix timestamp in milliseconds when the API last refreshed the data of this portfolio. Each portfolio has its own timestamp.

Example:

`1791469800123`

description

string

A description of the portfolio strategy. The response omits this field if no description is available.

Example:

`"The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy ..."`

category

string

The category of the portfolio, for example `thematic`, `income`, or `allocation`. The value is free text, not a fixed list. The response omits this field if no category is available.

Example:

`"thematic"`

modelProvider

string

The [model provider](https://docs.ondo.finance/intelligent-portfolios/model-providers) that develops the portfolio strategy, for example `ondo` or `blackrock`. The value is free text, not a fixed list. The response omits this field if no model provider is available.

Example:

`"ondo"`

inceptionDate

string<date-time>

The inception date of the portfolio, as an RFC 3339 timestamp in UTC. The response omits this field if no inception date is available.

Example:

`"2026-08-12T16:35:00Z"`

[Get All Portfolios](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios)[Get Price and Volume Data for All Supported Tickers](https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of "1" waives the full fee. A value of "0" waives no fee.
- The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is serviceFeeRateBeforeWaiver multiplied by (1 - waiverFraction).
- The rebalance frequency of the portfolio, for example Quarterly. The value is free text, not a fixed list. Empty string if no frequency is available.
- The reconstitution approach of the portfolio, for example Fixed. The value is free text, not a fixed list. Empty string if no reconstitution type is available.
- The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent quantity multiplied by its token price, divided by netAssetsUsd. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to targetWeight.
- string[]required
- The contract addresses of the constituent token, sorted by networkChainId.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#webpage","url":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio","name":"Get a Portfolio","description":"This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.616Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Portfolios","item":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios"},{"@type":"ListItem","position":3,"name":"Get a Portfolio","item":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#apireference","headline":"Get a Portfolio","name":"Get a Portfolio","description":"This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#webpage"},"dateModified":"2026-11-12T23:40:59.616Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios>>>
---
url: https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios
title: Get All Portfolios - Ondo Finance
description: This endpoint returns all active Ondo Intelligent Portfolios. Each portfolio contains its product metadata, net assets, dividend yields, service fee, rebalance data, and constituents. The response sorts the portfolios by symbol, and it sorts the constituents of each portfolio by symbol. Each entry in the array has the same fields as the response of Get a Portfolio. Rates, weights, and yields are decimal fractions. For example, "0.0009" is 0.09% and "0.1143" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get All Portfolios

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios",
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

	url := "https://api.gm.ondo.finance/v1/portfolios"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios")

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

503

```
[
  {
    "symbol": "MAG7Xon",
    "name": "Ondo Magnificent 7 and Crypto Portfolio",
    "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
    "category": "thematic",
    "modelProvider": "ondo",
    "inceptionDate": "2026-08-12T16:35:00Z",
    "netAssetsUsd": "1885406.537181",
    "dividendYield": "0.00198929",
    "afterWithholdingDividendYield": "0.0013925",
    "fees": {
      "serviceFeeRateBeforeWaiver": "0.0009",
      "waiverFraction": "1",
      "serviceFeeRateAfterWaiver": "0"
    },
    "rebalance": {
      "frequency": "Quarterly",
      "reconstitutionType": "Fixed",
      "lastRebalanceDate": "2026-08-12T16:36:00Z"
    },
    "constituentCount": 9,
    "constituents": [
      {
        "symbol": "AAPLon",
        "name": "Apple",
        "quantity": "917.20457",
        "targetWeight": "0.1143",
        "currentWeight": "0.12556912",
        "assetClass": "Equities",
        "instrumentType": "Stock",
        "sectorIndustry": [
          "Technology"
        ],
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
          },
          {
            "networkChainId": "solana-900",
            "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
            "decimals": 9
          }
        ]
      },
      {
        "symbol": "AMZNon",
        "name": "Amazon",
        "quantity": "905.66388",
        "targetWeight": "0.1143",
        "currentWeight": "0.10877632",
        "assetClass": "Equities",
        "instrumentType": "Stock",
        "sectorIndustry": [
          "Consumer Discretionary"
        ],
        "addresses": [
          {
            "networkChainId": "bsc-56",
            "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
            "decimals": 18
          },
          {
            "networkChainId": "ethereum-1",
            "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
            "decimals": 18
          },
          {
            "networkChainId": "solana-900",
            "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
            "decimals": 9
          }
        ]
      },
      "..."
    ],
    "timestamp": 1791469800123
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Portfolios

# Get All Portfolios

Copy pageCopy page

This endpoint returns all active Ondo Intelligent Portfolios. Each portfolio contains its product metadata, net assets, dividend yields, service fee, rebalance data, and constituents.

The response sorts the portfolios by symbol, and it sorts the constituents of each portfolio by symbol. Each entry in the array has the same fields as the response of [Get a Portfolio](https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio).

Rates, weights, and yields are decimal fractions. For example, `"0.0009"` is 0.09% and `"0.1143"` is 11.43%. Dates are RFC 3339 timestamps in UTC.

This endpoint does not return prices. To get the price of a portfolio token, use [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset), [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset), or [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) with the portfolio symbol.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

portfolios

Try it

Get All Portfolios

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios",
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

	url := "https://api.gm.ondo.finance/v1/portfolios"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios")

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

503

```
[
  {
    "symbol": "MAG7Xon",
    "name": "Ondo Magnificent 7 and Crypto Portfolio",
    "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
    "category": "thematic",
    "modelProvider": "ondo",
    "inceptionDate": "2026-08-12T16:35:00Z",
    "netAssetsUsd": "1885406.537181",
    "dividendYield": "0.00198929",
    "afterWithholdingDividendYield": "0.0013925",
    "fees": {
      "serviceFeeRateBeforeWaiver": "0.0009",
      "waiverFraction": "1",
      "serviceFeeRateAfterWaiver": "0"
    },
    "rebalance": {
      "frequency": "Quarterly",
      "reconstitutionType": "Fixed",
      "lastRebalanceDate": "2026-08-12T16:36:00Z"
    },
    "constituentCount": 9,
    "constituents": [
      {
        "symbol": "AAPLon",
        "name": "Apple",
        "quantity": "917.20457",
        "targetWeight": "0.1143",
        "currentWeight": "0.12556912",
        "assetClass": "Equities",
        "instrumentType": "Stock",
        "sectorIndustry": [
          "Technology"
        ],
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
          },
          {
            "networkChainId": "solana-900",
            "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
            "decimals": 9
          }
        ]
      },
      {
        "symbol": "AMZNon",
        "name": "Amazon",
        "quantity": "905.66388",
        "targetWeight": "0.1143",
        "currentWeight": "0.10877632",
        "assetClass": "Equities",
        "instrumentType": "Stock",
        "sectorIndustry": [
          "Consumer Discretionary"
        ],
        "addresses": [
          {
            "networkChainId": "bsc-56",
            "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
            "decimals": 18
          },
          {
            "networkChainId": "ethereum-1",
            "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
            "decimals": 18
          },
          {
            "networkChainId": "solana-900",
            "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
            "decimals": 9
          }
        ]
      },
      "..."
    ],
    "timestamp": 1791469800123
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
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

The portfolio token symbol.

Example:

`"MAG7Xon"`

name

string

required

The name of the portfolio.

Example:

`"Ondo Magnificent 7 and Crypto Portfolio"`

netAssetsUsd

string

required

The USD value of the constituents that the portfolio holds, represented as a string-encoded decimal with up to 6 digits after the decimal point. The value is the sum of each constituent `quantity` multiplied by its token price. It does not include cash from mints and redemptions that are not yet settled. For this reason, it can be slightly different from the token price multiplied by the total supply. If the portfolio has no supply, the value is `"0"`.

Example:

`"1885406.537181"`

dividendYield

string

required

The dividend yield of the portfolio, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.05" is the equivalent of 5%) The value is the average of the constituent dividend yields, weighted by `currentWeight`. The dividend yield of a constituent is the sum of its cash dividends paid in the last 365 days, divided by the current stock price. A constituent without dividends adds zero.

Example:

`"0.00198929"`

afterWithholdingDividendYield

string

required

The dividend yield of the portfolio after estimated withholding tax, represented as a string-encoded decimal with up to 8 digits after the decimal point. This value uses the same calculation as `dividendYield`, but it first subtracts the withholding tax from each dividend. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Example:

`"0.0013925"`

fees

object | null

required

The annual service fee of the portfolio. The value is `null` if no fee data is available. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Hide child attributes

fees.serviceFeeRateBeforeWaiver

string

required

The annual service fee rate before the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.0009" is the equivalent of 0.09%)

Example:

`"0.0009"`

fees.waiverFraction

string

required

The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of `"1"` waives the full fee. A value of `"0"` waives no fee.

Example:

`"1"`

fees.serviceFeeRateAfterWaiver

string

required

The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is `serviceFeeRateBeforeWaiver` multiplied by (1 - `waiverFraction`).

Example:

`"0"`

rebalance

object | null

required

The rebalance data of the portfolio. The value is `null` if no rebalance data is available. For more information, see [Rebalancing & Reconstitution](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution).

Hide child attributes

rebalance.frequency

string

required

The rebalance frequency of the portfolio, for example `Quarterly`. The value is free text, not a fixed list. Empty string if no frequency is available.

Example:

`"Quarterly"`

rebalance.reconstitutionType

string

required

The reconstitution approach of the portfolio, for example `Fixed`. The value is free text, not a fixed list. Empty string if no reconstitution type is available.

Example:

`"Fixed"`

rebalance.lastRebalanceDate

string<date-time>

The date of the most recent rebalance, as an RFC 3339 timestamp in UTC. The response omits this field if no rebalance date is available.

Example:

`"2026-08-12T16:36:00Z"`

constituentCount

integer<int32>

required

The number of constituents in `constituents`.

Example:

`9`

constituents

object[]

required

The constituents of the portfolio, sorted by symbol.

Hide child attributes

constituents.symbol

string

required

The GM token symbol of the constituent.

Example:

`"AAPLon"`

constituents.name

string

required

The name of the underlying asset. Empty string if no name is available.

Example:

`"Apple"`

constituents.quantity

string

required

The number of constituent tokens that the portfolio holds on all chains, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"917.20457"`

constituents.targetWeight

string

required

The target weight of the constituent in the portfolio model, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.1143" is the equivalent of 11.43%)

Example:

`"0.1143"`

constituents.currentWeight

string

required

The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent `quantity` multiplied by its token price, divided by `netAssetsUsd`. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to `targetWeight`.

Example:

`"0.12556912"`

constituents.assetClass

string

required

High-level category of the asset. Empty string if not available.

Example:

`"Equities"`

constituents.instrumentType

string

required

Instrument type within the asset class. Empty string if not available.

Example:

`"Stock"`

constituents.sectorIndustry

string[]

required

Sector and industry classifications for the asset. Empty array if not available.

Example:

```
["Technology"]
```

constituents.addresses

object[]

required

The contract addresses of the constituent token, sorted by `networkChainId`.

Show child attributes

timestamp

number

required

The Unix timestamp in milliseconds when the API last refreshed the data of this portfolio. Each portfolio has its own timestamp.

Example:

`1791469800123`

description

string

A description of the portfolio strategy. The response omits this field if no description is available.

Example:

`"The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy ..."`

category

string

The category of the portfolio, for example `thematic`, `income`, or `allocation`. The value is free text, not a fixed list. The response omits this field if no category is available.

Example:

`"thematic"`

modelProvider

string

The [model provider](https://docs.ondo.finance/intelligent-portfolios/model-providers) that develops the portfolio strategy, for example `ondo` or `blackrock`. The value is free text, not a fixed list. The response omits this field if no model provider is available.

Example:

`"ondo"`

inceptionDate

string<date-time>

The inception date of the portfolio, as an RFC 3339 timestamp in UTC. The response omits this field if no inception date is available.

Example:

`"2026-08-12T16:35:00Z"`

[Get Shares Multiplier History for an Asset](https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset)[Get a Portfolio](https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of "1" waives the full fee. A value of "0" waives no fee.
- The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is serviceFeeRateBeforeWaiver multiplied by (1 - waiverFraction).
- The rebalance frequency of the portfolio, for example Quarterly. The value is free text, not a fixed list. Empty string if no frequency is available.
- The reconstitution approach of the portfolio, for example Fixed. The value is free text, not a fixed list. Empty string if no reconstitution type is available.
- The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent quantity multiplied by its token price, divided by netAssetsUsd. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to targetWeight.
- string[]required
- The contract addresses of the constituent token, sorted by networkChainId.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios#webpage","url":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios","name":"Get All Portfolios","description":"This endpoint returns all active Ondo Intelligent Portfolios. Each portfolio contains its product metadata, net assets, dividend yields, service fee, rebalance data, and constituents. The response sorts the portfolios by symbol, and it sorts the constituents of each portfolio by symbol. Each entry in the array has the same fields as the response of Get a Portfolio. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.601Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get All Portfolios","item":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios#apireference","headline":"Get All Portfolios","name":"Get All Portfolios","description":"This endpoint returns all active Ondo Intelligent Portfolios. Each portfolio contains its product metadata, net assets, dividend yields, service fee, rebalance data, and constituents. The response sorts the portfolios by symbol, and it sorts the constituents of each portfolio by symbol. Each entry in the array has the same fields as the response of Get a Portfolio. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios#webpage"},"dateModified":"2026-11-12T23:40:59.601Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/price-streaming>>>
---
url: https://docs.ondo.finance/api-reference/price-streaming
title: Price Streaming - Ondo Finance
description: gRPC endpoint for real-time asset price streaming.
fetched: 2026-11-16
method: render
plan: read
---

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamPriceUpdates
```

Streamed

```
{
  "updates": [
    {
      "ticker": "GOOGL",
      "symbol": "GOOGLon",
      "stock_price": "304.915",
      "token_price": "305.39957516982939159",
      "timestamp": "1773350214478735649"
    },
    {
      "ticker": "AAPL",
      "symbol": "AAPLon",
      "stock_price": "256.2475",
      "token_price": "256.791808070580506978",
      "timestamp": "1773350214476688119"
    }
  ]
}
```

Streaming API

# Price Streaming

Copy pageCopy page

gRPC endpoint for real-time asset price streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamPriceUpdates
```

Streamed

```
{
  "updates": [
    {
      "ticker": "GOOGL",
      "symbol": "GOOGLon",
      "stock_price": "304.915",
      "token_price": "305.39957516982939159",
      "timestamp": "1773350214478735649"
    },
    {
      "ticker": "AAPL",
      "symbol": "AAPLon",
      "stock_price": "256.2475",
      "token_price": "256.791808070580506978",
      "timestamp": "1773350214476688119"
    }
  ]
}
```

Streaming is the real-time alternative to repeatedly polling the REST price endpoints. For a single price poll, use [Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) or [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset).

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamPriceUpdates`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more price updates into a single `updates` array.

updates

PriceUpdate[]

Array of price updates.

Hide PriceUpdate

ticker

string

Stock ticker.

symbol

string

Asset symbol.

stock\_price

string

Underlying stock price.

token\_price

string

Token price.

timestamp

uint64

Unix timestamp of the price update (in nanoseconds).

## Errors

Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema)[OHLC Streaming](https://docs.ondo.finance/api-reference/ohlc-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/price-streaming#webpage","url":"https://docs.ondo.finance/api-reference/price-streaming","name":"Price Streaming","description":"gRPC endpoint for real-time asset price streaming.","dateModified":"2026-07-16T20:06:17.217Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/price-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/price-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"Price Streaming","item":"https://docs.ondo.finance/api-reference/price-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/price-streaming#article","headline":"Price Streaming","name":"Price Streaming","description":"gRPC endpoint for real-time asset price streaming.","url":"https://docs.ondo.finance/api-reference/price-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/price-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.217Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/protobuf-schema>>>
---
url: https://docs.ondo.finance/api-reference/protobuf-schema
title: Protobuf Schema & Code Generation - Ondo Finance
description: Download the GM streaming API's Protocol Buffers schema and generate a typed client.
fetched: 2026-11-16
method: static
plan: read
---

Streaming API

# Protobuf Schema & Code Generation

Copy pageCopy page

Download the GM streaming API’s Protocol Buffers schema and generate a typed client.

Copy pageCopy page

The streaming API is defined as a [Protocol Buffers](https://protobuf.dev/) schema. Download it below, or copy it into a `grpcapi.proto` file, to generate a typed client with [`buf`](https://buf.build/) or [`protoc`](https://protobuf.dev/installation) in the [language of your choice](https://grpc.io/docs/languages):

grpcapi.proto

```
syntax = "proto3";

package ondo.gm.backend.v1;

option go_package = "github.com/ondoprotocol/gm/pkg/proto/ondo/gm/backend/v1;backendv1";

// This file is the public, client-facing subset of the Ondo Stocks &
// Intelligent Portfolios
// backend gRPC API.
//
// The package and message definitions here are kept wire-compatible with the
// server. Generate clients from this file with `buf generate` or `protoc`.
//
// Request/response access to pricing, quotes, attestations, and token
// metadata is served over the REST API; see the OpenAPI specification at
// https://docs.ondo.finance/openapi.json.

// BackendService exposes the real-time streaming surface of the Ondo Stocks &
// Intelligent Portfolios API. All requests must include an API key in the `x-api-key`
// metadata header.
service BackendService {
  // HealthCheck returns the service status. Does not require authentication.
  rpc HealthCheck(HealthCheckRequest) returns (HealthCheckResponse);

  // StreamPriceUpdates streams real-time price updates for the requested
  // assets. Clients subscribe to one or more symbols and receive price
  // updates as they occur. Updates are batched into each response message.
  rpc StreamPriceUpdates(StreamPriceUpdatesRequest) returns (stream StreamPriceUpdatesResponse);

  // StreamOHLC streams real-time OHLC (open/high/low/close) updates, bucketed
  // by minute and updated per tick. Updates are batched into each response
  // message.
  rpc StreamOHLC(StreamOHLCRequest) returns (stream StreamOHLCResponse);

  // StreamSoftQuoteDepth streams synthetic market depth (bids and asks)
  // derived from the soft-quote price ladder for the requested assets, updated
  // as the underlying ladder changes. Updates are batched into each response
  // message.
  rpc StreamSoftQuoteDepth(StreamSoftQuoteDepthRequest) returns (stream StreamSoftQuoteDepthResponse);
}

// HealthCheckRequest is the request message for the HealthCheck RPC.
message HealthCheckRequest {}

// HealthCheckResponse is the response message for the HealthCheck RPC.
message HealthCheckResponse {
  string status = 1;
}

// StreamPriceUpdatesRequest subscribes to price updates for a set of assets.
message StreamPriceUpdatesRequest {
  // List of asset symbols to subscribe to. If empty, updates for all assets
  // are streamed.
  repeated string symbols = 1;
}

// PriceUpdate is a single price update streamed to clients.
message PriceUpdate {
  // Underlying stock ticker.
  string ticker = 1;
  // GM asset symbol.
  string symbol = 2;
  // Underlying stock price.
  string stock_price = 3;
  // Token price.
  string token_price = 4;
  // Unix timestamp of the price update, in nanoseconds.
  uint64 timestamp = 5;
}

// StreamPriceUpdatesResponse batches one or more price updates into a single
// stream message.
message StreamPriceUpdatesResponse {
  repeated PriceUpdate updates = 1;
}

// StreamOHLCRequest subscribes to OHLC updates for a set of assets.
message StreamOHLCRequest {
  // List of asset symbols to subscribe to. If empty, updates for all assets
  // are streamed.
  repeated string symbols = 1;
}

// OHLCUpdate is one partial or closed minute OHLC update for a single symbol.
message OHLCUpdate {
  message PrimaryMarket {
    string symbol = 1;
    string open = 2;
    string high = 3;
    string low = 4;
    string close = 5;
  }
  message UnderlyingMarket {
    string ticker = 1;
    string open = 2;
    string high = 3;
    string low = 4;
    string close = 5;
  }
  PrimaryMarket primary_market = 1;
  UnderlyingMarket underlying_market = 2;
  // is_closed marks the final emission for the bucket (the minute boundary
  // crossed). Subsequent updates with a higher timestamp belong to the next
  // bucket.
  bool is_closed = 3;
  // timestamp is the bucket start (minute floor) in nanoseconds since epoch.
  // Stable across all partials and the final closed update for a given bucket.
  uint64 timestamp = 4;
}

// StreamOHLCResponse batches one or more OHLC updates into a single stream
// message so subscribers to many assets receive one wire frame per drain
// window rather than one frame per candle.
message StreamOHLCResponse {
  repeated OHLCUpdate updates = 1;
}

// StreamSoftQuoteDepthRequest subscribes to soft-quote depth for a set of
// assets.
message StreamSoftQuoteDepthRequest {
  // List of asset symbols to subscribe to. If empty, depth for all assets is
  // streamed.
  repeated string symbols = 1;
}

// SoftQuoteDepth is the synthetic market depth for one asset, derived from the
// soft-quote price ladder. It is indicative and chain-agnostic (human-decimal
// prices and quantities). bids and asks are empty when error is set.
message SoftQuoteDepth {
  // GM asset symbol.
  string symbol = 1;
  // Underlying stock ticker.
  string ticker = 2;
  // Trading session the depth was computed for: premarket | regular |
  // postmarket | overnight | offhours.
  string session_type = 3;
  // Asset-level failure (e.g. paused, market closed, stale price). When set,
  // bids and asks are empty.
  string error = 4;
  // Unix timestamp of the underlying computation, in nanoseconds.
  uint64 timestamp = 5;
  // Sell side (redeem), best (highest) price first.
  repeated SoftQuoteDepthLevel bids = 6;
  // Buy side (mint), best (lowest) price first.
  repeated SoftQuoteDepthLevel asks = 7;
}

// SoftQuoteDepthLevel is one price level: the marginal price for the
// incremental token quantity available at that depth.
message SoftQuoteDepthLevel {
  // Marginal price for this level.
  string price = 1;
  // Token quantity available at this level.
  string quantity = 2;
}

// StreamSoftQuoteDepthResponse batches one or more depth updates into a single
// stream message.
message StreamSoftQuoteDepthResponse {
  repeated SoftQuoteDepth updates = 1;
}
```

See all 161 lines

For example, to generate a typed gRPC client for Go with `protoc`:

```
protoc \
  --go_out=. --go_opt=paths=source_relative \
  --go-grpc_out=. --go-grpc_opt=paths=source_relative \
  grpcapi.proto
```

For quick, ad-hoc testing you don’t need the schema. Every gRPC endpoint provides an example of how to use [`grpcurl`](https://github.com/fullstorydev/grpcurl) to make a request with reflection.

[Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)[Price Streaming](https://docs.ondo.finance/api-reference/price-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/protobuf-schema#webpage","url":"https://docs.ondo.finance/api-reference/protobuf-schema","name":"Protobuf Schema & Code Generation","description":"Download the GM streaming API's Protocol Buffers schema and generate a typed client.","dateModified":"2026-09-24T00:59:51.980Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/protobuf-schema#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Protobuf Schema & Code Generation","item":"https://docs.ondo.finance/api-reference/protobuf-schema"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#article","headline":"Protobuf Schema & Code Generation","name":"Protobuf Schema & Code Generation","description":"Download the GM streaming API's Protocol Buffers schema and generate a typed client.","url":"https://docs.ondo.finance/api-reference/protobuf-schema","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#webpage"},"dateModified":"2026-09-24T00:59:51.980Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/quickstart>>>
---
url: https://docs.ondo.finance/api-reference/quickstart
title: Quickstart - Ondo Finance
description: Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Step 1: Onboard to Ondo Stocks & Intelligent Portfolios](https://docs.ondo.finance/api-reference/quickstart)
* [Step 2: Get Your First Price Quote](https://docs.ondo.finance/api-reference/quickstart)
* [Step 3: Request a Soft Quote](https://docs.ondo.finance/api-reference/quickstart)
* [Step 4: Request a Mint Attestation](https://docs.ondo.finance/api-reference/quickstart)
* [Step 5: Submit On-Chain](https://docs.ondo.finance/api-reference/quickstart)
* [Next Steps](https://docs.ondo.finance/api-reference/quickstart)

Home

# Quickstart

Copy pageCopy page

Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.

Copy pageCopy page

## Step 1: Onboard to Ondo Stocks & Intelligent Portfolios

To get started, reach out to [onboarding@ondo.finance](mailto:onboarding@ondo.finance) and let the team know you’re interested in API access. Then head to [app.ondo.finance](https://app.ondo.finance/) to begin the onboarding process. The Ondo team will follow up with instructions to get your API keys.

## Step 2: Get Your First Price Quote

Once you have your API key, try fetching the current price for TSLAon:

```
curl -X GET "https://api.gm.ondo.finance/v1/assets/prices/TSLAon" \
  -H "x-api-key: YOUR_API_KEY"
```

All requests are authenticated via the `x-api-key` header.

## Step 3: Request a Soft Quote

A soft quote provides a non-binding price estimate without impacting your trading limits — useful for displaying pricing in a UI or validating quotes before committing:

```
curl -X POST "https://api.gm.ondo.finance/v1/attestations/soft" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "TSLAon",
    "side": "buy",
    "notionalValue": "1000",
    "duration": "short"
  }'
```

## Step 4: Request a Mint Attestation

When you’re ready to execute, request a binding mint attestation. This creates a signed payload that authorizes an on-chain mint:

```
curl -X POST "https://api.gm.ondo.finance/v1/attestations" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "TSLAon",
    "side": "buy",
    "notionalValue": "1000",
    "duration": "short"
  }'
```

The response includes key fields such as `attestationId`, `signature`, and `expiration` that you’ll need for the on-chain transaction.

## Step 5: Submit On-Chain

Take the attestation `signature` from the response and submit it to the smart contract manager for the asset type, along with USDC or another supported stablecoin, to atomically mint your tokens. See the [smart contract reference](https://docs.ondo.finance/api-reference/smart-contracts) for Ondo Stocks & Intelligent Portfolios contract instructions and addresses.

## Next Steps

* [Error Codes](https://docs.ondo.finance/api-reference/error-codes) — Reference for all API error codes
* [API Caching Strategy](https://docs.ondo.finance/api-reference/endpoint-caching) — Caching durations for each endpoint
* [Smart contract reference](https://docs.ondo.finance/api-reference/smart-contracts) — Contract interface for minting and redeeming
* [Smart contract addresses](https://docs.ondo.finance/addresses) — Contract addresses across supported chains

[Overview](https://docs.ondo.finance/api-reference/overview)[Request a Mint or Redeem Attestation](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/quickstart#webpage","url":"https://docs.ondo.finance/api-reference/quickstart","name":"Quickstart","description":"Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.","dateModified":"2026-09-24T00:59:51.991Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/quickstart#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/quickstart#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://docs.ondo.finance/api-reference/overview"},{"@type":"ListItem","position":2,"name":"Quickstart","item":"https://docs.ondo.finance/api-reference/quickstart"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/quickstart#article","headline":"Quickstart","name":"Quickstart","description":"Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.","url":"https://docs.ondo.finance/api-reference/quickstart","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/quickstart#webpage"},"dateModified":"2026-09-24T00:59:51.991Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```