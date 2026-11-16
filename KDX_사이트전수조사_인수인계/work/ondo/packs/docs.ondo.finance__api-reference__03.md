# 읽기 묶음: docs.ondo.finance / api-reference (3/5)


<<<PAGE https://docs.ondo.finance/api-reference/chains/get-token-info>>>
---
url: https://docs.ondo.finance/api-reference/chains/get-token-info
title: Get Token Info - Ondo Finance
description: This endpoint retrieves contract information about a token on a GM chain. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Token Info

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info",
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

	url := "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info")

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
  "token": {
    "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
    "tokenName": "Apple (Ondo Tokenized)",
    "tokenSymbol": "AAPLon",
    "tokenDecimals": 18,
    "tokenSupply": {
      "value": "72.428346190773568025"
    }
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

# Get Token Info

Copy pageCopy page

This endpoint retrieves contract information about a token on a GM chain.

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

tokens

/

{tokenAddress}

/

info

Try it

Get Token Info

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info",
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

	url := "https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/chains/{chainId}/tokens/{tokenAddress}/info")

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
  "token": {
    "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
    "tokenName": "Apple (Ondo Tokenized)",
    "tokenSymbol": "AAPLon",
    "tokenDecimals": 18,
    "tokenSupply": {
      "value": "72.428346190773568025"
    }
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

tokenAddress

string

required

The token contract address

#### Response

200

application/json

OK

token

object

required

Hide child attributes

token.tokenAddress

string

required

The address of the token contract.

token.tokenName

string

required

The name of the token.

token.tokenSymbol

string

required

The symbol of the token.

token.tokenDecimals

integer

required

The number of decimal places the token can be divided into.

token.tokenSupply

object

required

Show child attributes

[Get Token Balances for a User or Token](https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token)[Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- integerrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/chains/get-token-info#webpage","url":"https://docs.ondo.finance/api-reference/chains/get-token-info","name":"Get Token Info","description":"This endpoint retrieves contract information about a token on a GM chain. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.663Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/chains/get-token-info#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/chains/get-token-info#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Chains","item":"https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token"},{"@type":"ListItem","position":3,"name":"Get Token Info","item":"https://docs.ondo.finance/api-reference/chains/get-token-info"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/chains/get-token-info#apireference","headline":"Get Token Info","name":"Get Token Info","description":"This endpoint retrieves contract information about a token on a GM chain. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/chains/get-token-info","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/chains/get-token-info#webpage"},"dateModified":"2026-11-12T23:40:59.663Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/endpoint-caching>>>
---
url: https://docs.ondo.finance/api-reference/endpoint-caching
title: Endpoint Caching - Ondo Finance
description: Caching durations for GM Backend API endpoints.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Default Behavior](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Latest Prices](https://docs.ondo.finance/api-reference/endpoint-caching)
* [OHLC](https://docs.ondo.finance/api-reference/endpoint-caching)
* [All Metadata](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Shares Multiplier](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Trading Limits](https://docs.ondo.finance/api-reference/endpoint-caching)
* [ITN Limits](https://docs.ondo.finance/api-reference/endpoint-caching)

References

# Endpoint Caching

Copy pageCopy page

Caching durations for GM Backend API endpoints.

Copy pageCopy page

This page outlines caching durations for various GM Backend API endpoints, establishing performance parameters while balancing freshness requirements.

## Default Behavior

Unless otherwise specified, all GET endpoints default to:

* **Cache Duration:** 1 minute

## Latest Prices

**Endpoints:** [Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) | [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset) | [Get Enhanced Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets)

* **Cache Duration:** 1 second

For real-time price streaming updates, see [Price Streaming Endpoint](https://docs.ondo.finance/api-reference/price-streaming).

## OHLC

**Endpoint:** [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset)

* **Cache Duration:** 1 second
* **Data Delay:** Underlying OHLC data may itself be delayed by up to 5-10 seconds
* **Effective Lag:** Up to 11 seconds

For real-time OHLC updates, see [OHLC Streaming Endpoint](https://docs.ondo.finance/api-reference/ohlc-streaming).

## All Metadata

**Endpoint:** [Get Metadata for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets)

* **Cache Duration:** 5 minutes
* **Note:** Metadata changes infrequently,

## Shares Multiplier

**Endpoint:** [Get Shares Multiplier History for an Asset](https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset)

* **Cache Duration:** 1 second
* **Note:** Shares multipliers change infrequently, so a 1 second cache supports near-real-time discovery.

## Trading Limits

**Endpoint:** [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits)

* **Cache Duration:** None (response is always up to date)

## ITN Limits

**Endpoint:** [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)

* **Cache Duration:** None (response is always up to date)

[Smart Contract Reference](https://docs.ondo.finance/api-reference/smart-contracts)[Error Codes](https://docs.ondo.finance/api-reference/error-codes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/endpoint-caching#webpage","url":"https://docs.ondo.finance/api-reference/endpoint-caching","name":"Endpoint Caching","description":"Caching durations for GM Backend API endpoints.","dateModified":"2026-11-07T00:34:22.072Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/endpoint-caching#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"Endpoint Caching","item":"https://docs.ondo.finance/api-reference/endpoint-caching"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#article","headline":"Endpoint Caching","name":"Endpoint Caching","description":"Caching durations for GM Backend API endpoints.","url":"https://docs.ondo.finance/api-reference/endpoint-caching","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#webpage"},"dateModified":"2026-11-07T00:34:22.072Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/error-codes>>>
---
url: https://docs.ondo.finance/api-reference/error-codes
title: Error Codes - Ondo Finance
description: Reference for all error codes returned by the GM Backend API.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Error Codes](https://docs.ondo.finance/api-reference/error-codes)
  + [MARKET\_CLOSED](https://docs.ondo.finance/api-reference/error-codes)
  + [MARKET\_PAUSED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_PAUSED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_LIMITED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_CLOSED\_FOR\_SESSION](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_REDEEM\_ONLY](https://docs.ondo.finance/api-reference/error-codes)
  + [READ\_ONLY\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SYMBOL](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_SYMBOL](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_NOT\_FOUND](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SIDE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_DURATION](https://docs.ondo.finance/api-reference/error-codes)
  + [MAX\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [SESSION\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [MAX\_ATTESTATIONS](https://docs.ondo.finance/api-reference/error-codes)
  + [OFFHOURS\_EXPOSURE\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [INSUFFICIENT\_LIQUIDITY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_NOTIONAL\_VALUE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_TOKEN\_AMOUNT](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_TOKEN\_OR\_NOTIONAL](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_CHAIN\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_SIDE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [UNSUPPORTED\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [PAUSED\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SORT](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_INTERVAL](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_RANGE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_INTERVAL\_RANGE\_PAIR](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_TICKER\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_TICKER\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [RESOURCE\_NOT\_FOUND](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_USER\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_USER\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [GAS\_FEE\_EXCEEDS\_ORDER\_VALUE](https://docs.ondo.finance/api-reference/error-codes)
  + [ITN\_ACCOUNT\_NOT\_ELIGIBLE](https://docs.ondo.finance/api-reference/error-codes)
  + [ITN\_UNAVAILABLE](https://docs.ondo.finance/api-reference/error-codes)
  + [RATE\_LIMITED](https://docs.ondo.finance/api-reference/error-codes)
  + [INTERNAL\_ERROR](https://docs.ondo.finance/api-reference/error-codes)

References

# Error Codes

Copy pageCopy page

Reference for all error codes returned by the GM Backend API.

Copy pageCopy page

The Ondo Stocks & Intelligent Portfolios APIs return structured error messages with three key fields:

* **code**: Machine-readable identifier (e.g., `MARKET_CLOSED`)
* **message**: Human-readable description
* **documentation**: URL linking to relevant documentation

## Error Codes

### MARKET\_CLOSED

**Status**: 403 Forbidden

```
{
  "code": "MARKET_CLOSED",
  "message": "market is closed"
}
```

The market is closed due to weekends, holidays, or scheduled/unscheduled closures from maintenance or exchange outages.

---

### MARKET\_PAUSED

**Status**: 403 Forbidden

```
{
  "code": "MARKET_PAUSED",
  "message": "market is paused"
}
```

Trading is temporarily paused, either during scheduled session transitions (09:29-09:31 ET) or unscheduled halts (circuit breaker triggers).

---

### ASSET\_PAUSED

**Status**: 403 Forbidden

```
{
  "code": "ASSET_PAUSED",
  "message": "asset trading is paused"
}
```

Trading for a specific asset is paused, possibly due to corporate actions, symbol migration, or market volatility.

---

### ASSET\_LIMITED

**Status**: 200 OK

```
{
  "code": "ASSET_LIMITED",
  "message": "Earnings event in progress"
}
```

Returned as a reason code within asset status responses (not as an error). Indicates the asset has limited trading capacity, typically during earnings events. Trading is still permitted, but quantity may be restricted.

---

### ASSET\_CLOSED\_FOR\_SESSION

**Status**: 403 Forbidden

```
{
  "code": "ASSET_CLOSED_FOR_SESSION",
  "message": "asset is not available for trading during the current session"
}
```

The asset isn’t tradable in the current session (“premarket”, “regular”, “postmarket”, “overnight”, or “offhours”).

---

### ASSET\_REDEEM\_ONLY

**Status**: 403 Forbidden

```
{
  "code": "ASSET_REDEEM_ONLY",
  "message": "asset is redeem-only"
}
```

The asset can only be redeemed (sold), not minted (bought).

---

### READ\_ONLY\_API\_KEY

**Status**: 403 Forbidden

```
{
  "code": "READ_ONLY_API_KEY",
  "message": "read-only API key cannot perform write operations"
}
```

The API key used is read-only and cannot create attestations or perform other write operations.

---

### MISSING\_API\_KEY

**Status**: 401 Unauthorized

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key"
}
```

No API key was provided in the `x-api-key` request header.

---

### INVALID\_API\_KEY

**Status**: 401 Unauthorized

```
{
  "code": "INVALID_API_KEY",
  "message": "invalid API key"
}
```

The provided API key is not valid or has been revoked.

---

### INVALID\_SYMBOL

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SYMBOL",
  "message": "invalid symbol; must be at least 3 characters long and end with 'on'"
}
```

The symbol is invalid, unrecognized, or improperly formatted. Use valid namespaced symbols (e.g., `TSLAon`, `AAPLon`).

---

### MISSING\_SYMBOL

**Status**: 400 Bad Request

```
{
  "code": "MISSING_SYMBOL",
  "message": "missing symbol"
}
```

The required `symbol` parameter was not provided.

---

### ASSET\_NOT\_FOUND

**Status**: 404 Not Found

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "asset not found"
}
```

The specified asset does not exist in the system.

---

### INVALID\_SIDE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SIDE",
  "message": "invalid side; side must be either 'buy' or 'sell'"
}
```

The `side` parameter must be either `buy` or `sell`.

---

### INVALID\_DURATION

**Status**: 400 Bad Request

```
{
  "code": "INVALID_DURATION",
  "message": "invalid duration; duration must be either 'long' or 'short'"
}
```

The `duration` parameter must be either `long` or `short`.

---

### MAX\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "MAX_LIMIT_REACHED",
  "message": "exceeded the active notional value limit"
}
```

The order exceeds user-based notional caps. Limits reset when attestations expire.

---

### SESSION\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "SESSION_LIMIT_REACHED",
  "message": "exceeded the session's notional value limit"
}
```

The order exceeds session-based notional caps, which reset after each session transition.

---

### MAX\_ATTESTATIONS

**Status**: 400 Bad Request

```
{
  "code": "MAX_ATTESTATIONS",
  "message": "exceeded the active attestations limit"
}
```

Maximum concurrent attestation requests reached. Wait for some to settle before requesting more.

---

### OFFHOURS\_EXPOSURE\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "OFFHOURS_EXPOSURE_LIMIT_REACHED",
  "message": "off-hours exposure limit reached"
}
```

The off-hours exposure limit has been reached for the asset during the current off-hours session. Wait for the next session to open, or trade a different asset.

---

### INSUFFICIENT\_LIQUIDITY

**Status**: 400 Bad Request

```
{
  "code": "INSUFFICIENT_LIQUIDITY",
  "message": "insufficient liquidity for the requested operation"
}
```

An attestation cannot be created due to insufficient funds, typically during sparse overnight trading.

---

### INVALID\_NOTIONAL\_VALUE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_NOTIONAL_VALUE",
  "message": "invalid notional value; value must be a string representing a positive decimal value"
}
```

The amount is below minimum requirements, above user limits, or malformed/non-numeric.

---

### INVALID\_TOKEN\_AMOUNT

**Status**: 400 Bad Request

```
{
  "code": "INVALID_TOKEN_AMOUNT",
  "message": "invalid token amount; amount must be a string representing a positive decimal value"
}
```

The token amount is malformed or not a positive decimal value.

---

### MISSING\_TOKEN\_OR\_NOTIONAL

**Status**: 400 Bad Request

```
{
  "code": "MISSING_TOKEN_OR_NOTIONAL",
  "message": "either token amount or notional value must be provided"
}
```

The request must include either `tokenAmount` or `notionalValue`, but neither was provided.

---

### INVALID\_ADDRESS

**Status**: 403 Forbidden

```
{
  "code": "INVALID_ADDRESS",
  "message": "user_address is not on the allow list"
}
```

The provided wallet address is not whitelisted for trading.

---

### MISSING\_CHAIN\_ID

**Status**: 400 Bad Request

```
{
  "code": "MISSING_CHAIN_ID",
  "message": "chainId is required"
}
```

The required `chainId` parameter was not provided in the request.

---

### MISSING\_SIDE

**Status**: 400 Bad Request

```
{
  "code": "MISSING_SIDE",
  "message": "side is required"
}
```

The required `side` parameter was not provided in the request.

---

### INVALID\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "INVALID_GM_CHAIN",
  "message": "invalid chain; supported chains: ethereum-1, bsc-56, solana-900"
}
```

The specified chain is not a valid GM chain identifier.

---

### UNSUPPORTED\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "UNSUPPORTED_GM_CHAIN",
  "message": "unsupported chain"
}
```

The specified chain is recognized but not currently supported for the requested operation.

---

### PAUSED\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "PAUSED_GM_CHAIN",
  "message": "chain is paused"
}
```

The specified chain is temporarily paused and not accepting requests.

---

### INVALID\_SORT

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SORT",
  "message": "invalid sort order; must be 'asc' or 'desc'"
}
```

The `sort` query parameter is invalid. Valid values are `asc` or `desc`.

---

### INVALID\_INTERVAL

**Status**: 400 Bad Request

```
{
  "code": "INVALID_INTERVAL",
  "message": "invalid interval format: 2hour"
}
```

The `interval` query parameter is not a valid value. Valid intervals are `1min`, `5min`, `15min`, `1hour`, `4hour`, `12hour`, and `1day`.

---

### INVALID\_RANGE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_RANGE",
  "message": "invalid time range: 2month; valid ranges: 1day, 1month, 3month, 6month, 1year, all"
}
```

The `range` query parameter is not a valid value. Valid ranges are `1day`, `1month`, `3month`, `6month`, `1year`, and `all`.

---

### INVALID\_INTERVAL\_RANGE\_PAIR

**Status**: 400 Bad Request

```
{
  "code": "INVALID_INTERVAL_RANGE_PAIR",
  "message": "invalid interval/range pair: 1min/1year; valid pairs: 1min/1day, 5min/1day, 15min/1day, 1hour/1month, 4hour/3month, 12hour/6month, 1day/1year, 1day/all"
}
```

The combination of `interval` and `range` parameters is not supported. See the OHLC endpoint documentation for valid pairs.

---

### MISSING\_TICKER\_ID

**Status**: 400 Bad Request

```
{
  "code": "MISSING_TICKER_ID",
  "message": "missing ticker ID"
}
```

The required `tickerId` parameter was not provided.

---

### INVALID\_TICKER\_ID

**Status**: 400 Bad Request

```
{
  "code": "INVALID_TICKER_ID",
  "message": "invalid ticker ID"
}
```

The provided `tickerId` is not a valid ticker identifier. Ticker IDs are formatted as `<base>_<target>` (e.g., `AAPLon_USDon`).

---

### RESOURCE\_NOT\_FOUND

**Status**: 404 Not Found

```
{
  "code": "RESOURCE_NOT_FOUND",
  "message": "resource not found"
}
```

The requested resource does not exist.

---

### MISSING\_USER\_ADDRESS

**Status**: 400 Bad Request

```
{
  "code": "MISSING_USER_ADDRESS",
  "message": "missing user address"
}
```

The `user_address` field is required for firm attestation requests on Solana chains but was not provided.

---

### INVALID\_USER\_ADDRESS

**Status**: 400 Bad Request

```
{
  "code": "INVALID_USER_ADDRESS",
  "message": "invalid user address"
}
```

The `user_address` provided for a firm attestation request on a Solana chain is not a valid Solana public key.

---

### GAS\_FEE\_EXCEEDS\_ORDER\_VALUE

**Status**: 400 Bad Request

```
{
  "code": "GAS_FEE_EXCEEDS_ORDER_VALUE",
  "message": "gas fee exceeds order value: increase your order size or try again later"
}
```

The estimated gas fee for executing the order on-chain exceeds the total value of the order. Increase your order size or try again when gas fees are lower.

---

### ITN\_ACCOUNT\_NOT\_ELIGIBLE

**Status**: 403 Forbidden

```
{
  "code": "ITN_ACCOUNT_NOT_ELIGIBLE",
  "message": "account or wallet is not eligible for ITN"
}
```

Your account or wallet is not eligible for ITN. See the [ITN prerequisites](https://docs.ondo.finance/api-reference/itn-integration).

---

### ITN\_UNAVAILABLE

**Status**: 503 Service Unavailable

```
{
  "code": "ITN_UNAVAILABLE",
  "message": "ITN operation is temporarily unavailable"
}
```

ITN minting or redeeming is temporarily unavailable, either platform-wide or for a specific asset. [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status) reports this code as a `reason` when a side is closed. Retry the request after a short time.

---

### RATE\_LIMITED

**Status**: 429 Too Many Requests

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded"
}
```

The account has exceeded its request rate limits. Wait briefly and retry with exponential backoff.

---

### INTERNAL\_ERROR

**Status**: 500 Internal Server Error

```
{
  "code": "INTERNAL_ERROR",
  "message": "internal error"
}
```

An unexpected server error occurred. If this persists, contact your account manager.
The [portfolio endpoints](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios) return this code with status `503 Service Unavailable` when portfolio data is temporarily unavailable. Retry the request after a short time.

---

This list is non-exhaustive. For unresolved issues, consult request documentation or contact us at [support@ondo.finance](mailto:support@ondo.finance).

[Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/error-codes#webpage","url":"https://docs.ondo.finance/api-reference/error-codes","name":"Error Codes","description":"Reference for all error codes returned by the GM Backend API.","dateModified":"2026-11-07T00:34:22.075Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/error-codes#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/error-codes#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"Error Codes","item":"https://docs.ondo.finance/api-reference/error-codes"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/error-codes#article","headline":"Error Codes","name":"Error Codes","description":"Reference for all error codes returned by the GM Backend API.","url":"https://docs.ondo.finance/api-reference/error-codes","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/error-codes#webpage"},"dateModified":"2026-11-07T00:34:22.075Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/itn-integration>>>
---
url: https://docs.ondo.finance/api-reference/itn-integration
title: ITN Integration - Ondo Finance
description: Integrate Alpaca's Instant Tokenization Network with Ondo Stocks on Ethereum and BNB Chain.
fetched: 2026-11-16
method: render
plan: read
---

## On this page

Back to top

* [Choose an environment](https://docs.ondo.finance/api-reference/itn-integration)
* [Prerequisites](https://docs.ondo.finance/api-reference/itn-integration)
* [Supported assets](https://docs.ondo.finance/api-reference/itn-integration)
* [Rate limits](https://docs.ondo.finance/api-reference/itn-integration)
* [Fees](https://docs.ondo.finance/api-reference/itn-integration)
* [Check asset availability](https://docs.ondo.finance/api-reference/itn-integration)
* [Mint Ondo Stocks](https://docs.ondo.finance/api-reference/itn-integration)
* [Check request status](https://docs.ondo.finance/api-reference/itn-integration)
* [Redeem Ondo Stocks](https://docs.ondo.finance/api-reference/itn-integration)
  + [Find the token contract address](https://docs.ondo.finance/api-reference/itn-integration)
  + [Submit the redemption](https://docs.ondo.finance/api-reference/itn-integration)

References

# ITN Integration

Copy pageCopy page

Integrate Alpaca’s Instant Tokenization Network with Ondo Stocks on Ethereum and BNB Chain.

Copy pageCopy page

Alpaca’s Instant Tokenization Network (ITN) allows authorized participants to convert supported underlying securities into Ondo Stocks and redeem Ondo Stocks for the underlying securities.
For the complete ITN workflow and API details, see Alpaca’s [Tokenization Guide for Authorized Participants](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant).

## Choose an environment

* Production
* Staging

Production connects Ondo’s production environment with Alpaca’s live environment.

| Service | Base URL |
| --- | --- |
| Ondo Global Markets | `https://api.gm.ondo.finance` |
| Alpaca Broker API | `https://broker-api.alpaca.markets` |

Production ITN transactions involve assets with real value. On-chain transactions are irreversible and require ETH or BNB for gas.

Staging connects Ondo’s staging environment with Alpaca’s sandbox.

| Service | Base URL |
| --- | --- |
| Ondo Global Markets | `https://api.gm-staging.ondo.finance` |
| Alpaca Broker API | `https://broker-api.sandbox.alpaca.markets` |

Staging contracts are deployed on Ethereum and BNB Chain mainnet. Tokens minted through the sandbox flow have no monetary value, but on-chain transactions require real ETH or BNB for gas.

## Prerequisites

Complete these steps before submitting an ITN request:

When signing up for an Alpaca account and an Ondo account, you must use the **same email address**. The handshake process will fail to complete if there is a mismatch.

1. Complete onboarding with Alpaca for a [BrokerAPI account](https://docs.alpaca.markets/us/docs/getting-started-with-broker-api). Contact Ondo for an introduction to the Alpaca team, or coordinate directly with Alpaca if you already have a relationship. A TradingAPI account alone does not currently meet ITN onboarding requirements. Use an Alpaca sandbox account for staging and a live Alpaca account for production.
2. Complete the [Ondo Stocks onboarding and KYC process](https://docs.ondo.finance/ondo-stocks/onboarding-and-kyc) to establish your Ondo account. **Use the same email address as your Alpaca account**.
3. Request access to the Ondo API and obtain an API key for your selected environment.
4. Confirm that your Alpaca and Ondo accounts use the same email address before requesting the handshake. Provide the Alpaca team with this shared email address and your corresponding **Alpaca account number**. The account number is different from the Alpaca account ID used in API paths.
5. Wait for Alpaca to coordinate with Ondo regarding the linking of your accounts.
6. Provide the Ondo team with the wallet address that you plan to use for ITN requests.
7. Wait for Ondo to enable ITN access for the wallet(s) you provided.

Mint requests will fail if the Alpaca and Ondo accounts are not linked or if the destination wallet has not been enabled for ITN.

## Supported assets

ITN supports the assets below on Ethereum and BNB Chain. Use the stock ticker when submitting an Alpaca request.

* Production
* Staging

| Ondo token symbol | Stock ticker |
| --- | --- |
| `AAPLon` | `AAPL` |
| `AMDon` | `AMD` |
| `AMZNon` | `AMZN` |
| `ARMon` | `ARM` |
| `ASMLon` | `ASML` |
| `AVGOon` | `AVGO` |
| `COINon` | `COIN` |
| `CRCLon` | `CRCL` |
| `CRWVon` | `CRWV` |
| `DRAMon` | `DRAM` |
| `FUTUon` | `FUTU` |
| `GLWon` | `GLW` |
| `GMEon` | `GME` |
| `GOOGLon` | `GOOGL` |
| `HOODon` | `HOOD` |
| `INTCon` | `INTC` |
| `LLYon` | `LLY` |
| `METAon` | `META` |
| `MRVLon` | `MRVL` |
| `MSFTon` | `MSFT` |
| `MSTRon` | `MSTR` |
| `MUon` | `MU` |
| `NFLXon` | `NFLX` |
| `NVDAon` | `NVDA` |
| `ORCLon` | `ORCL` |
| `OXYon` | `OXY` |
| `PDDon` | `PDD` |
| `PLTRon` | `PLTR` |
| `PYPLon` | `PYPL` |
| `QCOMon` | `QCOM` |
| `QQQon` | `QQQ` |
| `RDDTon` | `RDDT` |
| `SKHYon` | `SKHY` |
| `SLVon` | `SLV` |
| `SNDKon` | `SNDK` |
| `SOFIon` | `SOFI` |
| `SPCXon` | `SPCX` |
| `SPYon` | `SPY` |
| `STRCon` | `STRC` |
| `TQQQon` | `TQQQ` |
| `TSLAon` | `TSLA` |
| `TSMon` | `TSM` |

| Ondo token symbol | Stock ticker |
| --- | --- |
| `AAPLon` | `AAPL` |
| `AMZNon` | `AMZN` |
| `MSFTon` | `MSFT` |
| `NVDAon` | `NVDA` |
| `TSLAon` | `TSLA` |

## Rate limits

The following USD notional limits apply independently to mint and redemption requests during each [market session](https://docs.ondo.finance/ondo-stocks/market-hours-and-trading-availability). Each request must meet the minimum per request, and the combined value of your requests must not exceed the maximum total per account for that session.

* Production
* Staging

| Market session | Minimum per request | Maximum total per account |
| --- | --- | --- |
| Pre-market | $1,000 | $1,000,000 |
| Regular | $1,000 | $5,000,000 |
| Post-market | $1,000 | $1,000,000 |
| Overnight | $1,000 | $1,000,000 |
| Off-hours | $1,000 | $500,000 |

| Market session | Minimum per request | Maximum total per account |
| --- | --- | --- |
| Pre-market | $1 | $500,000 |
| Regular | $1 | $1,000,000 |
| Post-market | $1 | $500,000 |
| Overnight | $1 | $250,000 |
| Off-hours | $1 | $100,000 |

Additional system-wide and asset-level limits apply. During periods of high traffic, these limits may prevent a mint from being accepted or delay a redemption until capacity becomes available.

To see your current limits and remaining capacity for an asset on each network, use [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset).

## Fees

Ondo charges a fee for minting and redeeming assets. See the table below for each direction’s fee in basis points.

* Production
* Staging

| Direction | Fee |
| --- | --- |
| Mint | 0 bps (0%) |
| Redeem | 5 bps (0.05%) |

| Direction | Fee |
| --- | --- |
| Mint | 0 bps (0%) |
| Redeem | 5 bps (0.05%) |

Alpaca may charge its own fees for mint and redemption requests. The response from Alpaca’s [List Tokenization Requests endpoint](https://docs.ondo.finance/api-reference/itn-integration) includes any fees associated with each request. See Alpaca’s [Tokenization Guide for Authorized Participants](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant) for its current fee schedule.

## Check asset availability

Before minting or redeeming, use the ITN endpoints to check availability and limits.

* [List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets) returns each ITN asset with its networks, token addresses, and fees.
* [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status) reports whether minting and redeeming are open, globally and for each asset on each network.
* [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset) returns your session limits and how much you can still mint and redeem on each network.

* Production
* Staging

```
curl --request GET \
  "https://api.gm.ondo.finance/v1/itn/status" \
  --header "x-api-key: ${GM_API_KEY}"

curl --request GET \
  "https://api.gm.ondo.finance/v1/itn/assets/AAPLon/limits" \
  --header "x-api-key: ${GM_API_KEY}"
```

```
curl --request GET \
  "https://api.gm-staging.ondo.finance/v1/itn/status" \
  --header "x-api-key: ${GM_API_KEY}"

curl --request GET \
  "https://api.gm-staging.ondo.finance/v1/itn/assets/AAPLon/limits" \
  --header "x-api-key: ${GM_API_KEY}"
```

Ondo does not continue redemption settlement while a relevant `MARKET_PAUSED`, `PAUSED_GM_CHAIN`, or `ASSET_PAUSED` status is active. `ASSET_LIMITED` does not pause ITN. If no pause is reported and a request remains pending, contact [support@ondo.finance](mailto:support@ondo.finance).

## Mint Ondo Stocks

To mint Ondo Stocks, submit a request through [Alpaca’s Mint Request endpoint](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant). Set `issuer` to `ondo`. The only supported `network` values are `ethereum` for Ethereum and `binance` for BNB Chain.

* Production
* Staging

```
curl --request POST \
  "https://broker-api.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/mint" \
  --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}" \
  --header "Content-Type: application/json" \
  --data '{
    "underlying_symbol": "AAPL",
    "qty": "1",
    "issuer": "ondo",
    "network": "ethereum",
    "wallet_address": "0xYOUR_ENABLED_WALLET"
  }'
```

Use your live Alpaca credentials for production ITN requests.

```
curl --request POST \
  "https://broker-api.sandbox.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/mint" \
  --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}" \
  --header "Content-Type: application/json" \
  --data '{
    "underlying_symbol": "AAPL",
    "qty": "1",
    "issuer": "ondo",
    "network": "ethereum",
    "wallet_address": "0xYOUR_ENABLED_WALLET"
  }'
```

Use your Alpaca sandbox credentials for staging ITN requests.

The `qty` field is the number of underlying shares to tokenize and may contain up to nine decimal places. Ondo calculates the corresponding Ondo Stock token amount and delivers it to the enabled wallet after the underlying shares settle.
To mint on BNB Chain, change `network` to `binance`.

## Check request status

Use Alpaca’s [List Tokenization Requests endpoint](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant) to monitor your mint and redemption requests:

* Production
* Staging

```
curl \
  "https://broker-api.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/requests" \
  --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}"
```

```
curl \
  "https://broker-api.sandbox.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/requests" \
  --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}"
```

Each request has a `status` of `pending`, `completed`, or `rejected`. The response also includes identifiers, quantities, network information, transaction hashes, and any fees associated with the requests.

## Redeem Ondo Stocks

Redemptions begin on-chain. From the wallet enabled during onboarding, first approve the ITN issuer contract to spend the Ondo Stocks you want to redeem. Then call `redeem(address,uint256)` on the issuer contract. A successful redemption burns the tokens. Ondo detects the burn and works with Alpaca to transfer the corresponding underlying shares to your linked Alpaca account. See Alpaca’s [Redeem Workflow](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant) for more information.

### Find the token contract address

Use [Get Contract Addresses for an Asset](https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset) with the Ondo Stock symbol:

* Production
* Staging

```
curl --request GET \
  "https://api.gm.ondo.finance/v1/assets/${TOKEN_SYMBOL}/addresses" \
  --header "x-api-key: ${GM_API_KEY}"
```

```
curl --request GET \
  "https://api.gm-staging.ondo.finance/v1/assets/${TOKEN_SYMBOL}/addresses" \
  --header "x-api-key: ${GM_API_KEY}"
```

Select the address whose `networkChainId` is `ethereum-1` or `bsc-56`. Use the returned `decimals` value when converting a human-readable token amount into the integer passed to the contract.

### Submit the redemption

The flow is the same on Ethereum and BNB Chain. Use an RPC endpoint for your selected network and the corresponding ITN issuer contract:

* Production
* Staging

| Network | ITN issuer contract |
| --- | --- |
| Ethereum | [`0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E`](https://etherscan.io/address/0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E) |
| BNB Chain | [`0x341f9e6463161f0c90037cbc0150dc54e6d1e06e`](https://bscscan.com/address/0x341f9e6463161f0c90037cbc0150dc54e6d1e06e) |

| Network | ITN issuer contract |
| --- | --- |
| Ethereum | [`0x46c65333cea9a3c6357c4f075e9f67aaef0639df`](https://etherscan.io/address/0x46c65333cea9a3c6357c4f075e9f67aaef0639df) |
| BNB Chain | [`0x194e4db0a165c4108db08534564196d915eadcf3`](https://bscscan.com/address/0x194e4db0a165c4108db08534564196d915eadcf3) |

These contracts are deployed on mainnet even though staging uses Alpaca’s sandbox. The tokens have no monetary value, but transactions require real ETH or BNB for gas.

The approval and redemption transactions must both be sent from the wallet that Ondo enabled for ITN.
The example below uses Foundry’s [`cast`](https://getfoundry.sh/cast/overview) command. Ondo Stocks use 18 decimal places, so convert the human-readable token amount before submitting it. This amount represents the Ondo Stocks being redeemed, not the number of underlying shares.

```
TOKEN_ADDRESS="0xTOKEN_ADDRESS"
ISSUER_ADDRESS="0xITN_ISSUER_ADDRESS"
TOKEN_AMOUNT="1.5"
AMOUNT_WEI="$(cast to-wei "${TOKEN_AMOUNT}")"
RPC_URL="https://YOUR_NETWORK_RPC_URL"

# Approve the ITN issuer contract to spend the tokens being redeemed.
cast send "${TOKEN_ADDRESS}" \
  "approve(address,uint256)" "${ISSUER_ADDRESS}" "${AMOUNT_WEI}" \
  --rpc-url "${RPC_URL}" \
  --private-key "${PRIVATE_KEY}"

# Transfer and burn the tokens to begin settlement through Alpaca.
cast send "${ISSUER_ADDRESS}" \
  "redeem(address,uint256)" "${TOKEN_ADDRESS}" "${AMOUNT_WEI}" \
  --rpc-url "${RPC_URL}" \
  --private-key "${PRIVATE_KEY}"
```

After the redemption transaction is confirmed, use the [request status endpoint](https://docs.ondo.finance/api-reference/itn-integration) to follow settlement. It may take time for a newly observed redemption to appear in Alpaca. Do not resubmit a successful on-chain redemption while it is being processed. The request remains `pending` until Alpaca transfers the underlying shares and the redemption completes.

[Upcoming API changes](https://docs.ondo.finance/api-reference/upcoming-changes)[Smart Contract Reference](https://docs.ondo.finance/api-reference/smart-contracts)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Ondo Global Markets	https://api.gm-staging.ondo.finance
- Alpaca Broker API	https://broker-api.sandbox.alpaca.markets
- Pre-market	$1	$500,000
- Regular	$1	$1,000,000
- Post-market	$1	$500,000
- Overnight	$1	$250,000
- Off-hours	$1	$100,000
- Ethereum	0x46c65333cea9a3c6357c4f075e9f67aaef0639df
- BNB Chain	0x194e4db0a165c4108db08534564196d915eadcf3

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/itn-integration#webpage","url":"https://docs.ondo.finance/api-reference/itn-integration","name":"ITN Integration","description":"Integrate Alpaca's Instant Tokenization Network with Ondo Stocks on Ethereum and BNB Chain.","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/itn-integration#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/itn-integration#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"ITN Integration","item":"https://docs.ondo.finance/api-reference/itn-integration"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/itn-integration#article","headline":"ITN Integration","name":"ITN Integration","description":"Integrate Alpaca's Instant Tokenization Network with Ondo Stocks on Ethereum and BNB Chain.","url":"https://docs.ondo.finance/api-reference/itn-integration","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/itn-integration#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset>>>
---
url: https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset
title: Get ITN Limits for an Asset - Ondo Finance
description: This endpoint returns your ITN mint and redeem limits for an asset on each network it is deployed on, and how much you can still mint and redeem in the current session. All amounts are USD notional values. Your Ondo account must be linked to an Alpaca account for ITN. See the prerequisites in ITN Integration. Limits: - sessionLimits lists your limit for each market session. A limit of "0" means that side is closed during the session. - remaining is the amount you can still mint or redeem on the network in the current session. Your account limit is shared across networks. - minMintNotional is the smallest mint request accepted. This endpoint does not report pauses. To check whether minting or redeeming is open, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.
fetched: 2026-11-16
method: render
plan: read
---

Get ITN Limits for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits",
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

	url := "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits")

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

403

404

429

500

```
{
  "timestamp": 1759777200000,
  "symbol": "AAPLon",
  "currentSession": "regular",
  "minMintNotional": "1000",
  "networks": [
    {
      "networkChainId": "ethereum-1",
      "alpacaNetwork": "ethereum",
      "sessionLimits": [
        {
          "session": "premarket",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "regular",
          "mint": "2000000",
          "redeem": "2000000"
        },
        {
          "session": "postmarket",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "overnight",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "offhours",
          "mint": "500000",
          "redeem": "500000"
        }
      ],
      "remaining": {
        "mint": "1880000",
        "redeem": "2000000"
      }
    },
    "..."
  ]
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
  "code": "ITN_ACCOUNT_NOT_ELIGIBLE",
  "message": "account or wallet is not eligible for ITN",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#itn_account_not_eligible"
}
```

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "asset not found",
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

ITN

# Get ITN Limits for an Asset

Copy pageCopy page

This endpoint returns your ITN mint and redeem limits for an asset on each network it is deployed on, and how much you can still mint and redeem in the current session. All amounts are USD notional values.

Your Ondo account must be linked to an Alpaca account for ITN. See the prerequisites in [ITN Integration](https://docs.ondo.finance/api-reference/itn-integration).

Limits:

* `sessionLimits` lists your limit for each market session. A limit of `"0"` means that side is closed during the session.
* `remaining` is the amount you can still mint or redeem on the network in the current session. Your account limit is shared across networks.
* `minMintNotional` is the smallest mint request accepted.

This endpoint does not report pauses. To check whether minting or redeeming is open, see [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status).

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

For the complete ITN workflow, see [ITN Integration](https://docs.ondo.finance/api-reference/itn-integration).

Copy pageCopy page

GET

/

v1

/

itn

/

assets

/

{symbol}

/

limits

Try it

Get ITN Limits for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits",
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

	url := "https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/assets/{symbol}/limits")

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

403

404

429

500

```
{
  "timestamp": 1759777200000,
  "symbol": "AAPLon",
  "currentSession": "regular",
  "minMintNotional": "1000",
  "networks": [
    {
      "networkChainId": "ethereum-1",
      "alpacaNetwork": "ethereum",
      "sessionLimits": [
        {
          "session": "premarket",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "regular",
          "mint": "2000000",
          "redeem": "2000000"
        },
        {
          "session": "postmarket",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "overnight",
          "mint": "1000000",
          "redeem": "1000000"
        },
        {
          "session": "offhours",
          "mint": "500000",
          "redeem": "500000"
        }
      ],
      "remaining": {
        "mint": "1880000",
        "redeem": "2000000"
      }
    },
    "..."
  ]
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
  "code": "ITN_ACCOUNT_NOT_ELIGIBLE",
  "message": "account or wallet is not eligible for ITN",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#itn_account_not_eligible"
}
```

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "asset not found",
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

#### Response

200

application/json

OK

timestamp

number

required

The Unix timestamp in milliseconds when the limits were evaluated.

Example:

`1759777200000`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

currentSession

enum<string>

required

The current market session. `remaining` applies to this session.

Available options:

`premarket`,

`regular`,

`postmarket`,

`overnight`,

`offhours`

Example:

`"regular"`

minMintNotional

string

required

The minimum USD notional value of a mint request, represented as a string-encoded decimal with up to 2 digits after the decimal point.

Example:

`"1000"`

networks

object[]

required

Your limits for the asset on each network it is deployed on.

Hide child attributes

networks.networkChainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

networks.alpacaNetwork

string

required

Alpaca's name for the network.

Example:

`"ethereum"`

networks.sessionLimits

object[]

required

Your mint and redeem limit for each market session.

Show child attributes

networks.remaining

object

required

The USD notional value you can still mint or redeem on the network in the current session.

Show child attributes

[Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status)[Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- Available options: ethereum-1, bsc-56, solana-900
- objectrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset","name":"Get ITN Limits for an Asset","description":"This endpoint returns your ITN mint and redeem limits for an asset on each network it is deployed on, and how much you can still mint and redeem in the current session. All amounts are USD notional values. Your Ondo account must be linked to an Alpaca account for ITN. See the prerequisites in ITN Integration. Limits: - sessionLimits lists your limit for each market session. A limit of \"0\" means that side is closed during the session. - remaining is the amount you can still mint or redeem on the network in the current session. Your account limit is shared across networks. - minMintNotional is the smallest mint request accepted. This endpoint does not report pauses. To check whether minting or redeeming is open, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","dateModified":"2026-11-12T23:40:59.771Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"ITN","item":"https://docs.ondo.finance/api-reference/itn/list-itn-assets"},{"@type":"ListItem","position":3,"name":"Get ITN Limits for an Asset","item":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset#apireference","headline":"Get ITN Limits for an Asset","name":"Get ITN Limits for an Asset","description":"This endpoint returns your ITN mint and redeem limits for an asset on each network it is deployed on, and how much you can still mint and redeem in the current session. All amounts are USD notional values. Your Ondo account must be linked to an Alpaca account for ITN. See the prerequisites in ITN Integration. Limits: - sessionLimits lists your limit for each market session. A limit of \"0\" means that side is closed during the session. - remaining is the amount you can still mint or redeem on the network in the current session. Your account limit is shared across networks. - minMintNotional is the smallest mint request accepted. This endpoint does not report pauses. To check whether minting or redeeming is open, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","url":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.771Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/itn/get-itn-status>>>
---
url: https://docs.ondo.finance/api-reference/itn/get-itn-status
title: Get ITN Status - Ondo Finance
description: This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.
fetched: 2026-11-16
method: render
plan: read
---

Get ITN Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/status \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/status"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/status",
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

	url := "https://api.gm.ondo.finance/v1/itn/status"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/status")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/status")

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
{
  "timestamp": 1759777200000,
  "currentSession": "regular",
  "mint": {
    "isOpen": true,
    "reason": null
  },
  "redeem": {
    "isOpen": true,
    "reason": null
  },
  "assets": [
    {
      "symbol": "AAPLon",
      "networks": [
        {
          "networkChainId": "bsc-56",
          "alpacaNetwork": "binance",
          "mint": {
            "enabled": false,
            "reason": {
              "code": "PAUSED_GM_CHAIN",
              "message": "chain is paused",
              "documentation": "https://docs.ondo.finance/api-reference/error-codes#paused_gm_chain"
            }
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        },
        {
          "networkChainId": "ethereum-1",
          "alpacaNetwork": "ethereum",
          "mint": {
            "enabled": true,
            "reason": null
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        }
      ]
    },
    "..."
  ]
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

ITN

# Get ITN Status

Copy pageCopy page

This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network.

**Global Status**

The top-level `mint` and `redeem` objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side.

**Per-Network Availability**

Each entry in `assets[].networks` reports whether minting and redeeming are enabled for that asset on that network.

**ITN Status Reason Codes**

When a side is closed or unavailable, `reason` is set. Otherwise, `reason` is `null`.

`reason.code` is one of:

* `ITN_UNAVAILABLE`: ITN is temporarily unavailable, either platform-wide or for the asset.
* `MARKET_PAUSED`: ITN minting or redeeming is paused for all assets.
* `PAUSED_GM_CHAIN`: ITN minting or redeeming is paused on the network. Only returned per network.
* `ASSET_PAUSED`: The asset is paused for ITN. Only returned per network.

For limits on how much you can mint or redeem, see [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset).

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

For the complete ITN workflow, see [ITN Integration](https://docs.ondo.finance/api-reference/itn-integration).

Copy pageCopy page

GET

/

v1

/

itn

/

status

Try it

Get ITN Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/status \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/status"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/status",
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

	url := "https://api.gm.ondo.finance/v1/itn/status"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/status")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/status")

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
{
  "timestamp": 1759777200000,
  "currentSession": "regular",
  "mint": {
    "isOpen": true,
    "reason": null
  },
  "redeem": {
    "isOpen": true,
    "reason": null
  },
  "assets": [
    {
      "symbol": "AAPLon",
      "networks": [
        {
          "networkChainId": "bsc-56",
          "alpacaNetwork": "binance",
          "mint": {
            "enabled": false,
            "reason": {
              "code": "PAUSED_GM_CHAIN",
              "message": "chain is paused",
              "documentation": "https://docs.ondo.finance/api-reference/error-codes#paused_gm_chain"
            }
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        },
        {
          "networkChainId": "ethereum-1",
          "alpacaNetwork": "ethereum",
          "mint": {
            "enabled": true,
            "reason": null
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        }
      ]
    },
    "..."
  ]
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

#### Response

200

application/json

OK

timestamp

number

required

The Unix timestamp in milliseconds when the status was evaluated.

Example:

`1759777200000`

currentSession

enum<string>

required

The current market session.

Available options:

`premarket`,

`regular`,

`postmarket`,

`overnight`,

`offhours`

Example:

`"regular"`

mint

object

required

Whether ITN minting is open globally.

Hide child attributes

mint.isOpen

boolean

required

Indicates whether the side is open globally.

Example:

`true`

mint.reason

object | null

required

The reason the side is closed. `null` when the side is open.

Show child attributes

redeem

object

required

Whether ITN redeeming is open globally.

Hide child attributes

redeem.isOpen

boolean

required

Indicates whether the side is open globally.

Example:

`true`

redeem.reason

object | null

required

The reason the side is closed. `null` when the side is open.

Show child attributes

assets

object[]

required

The availability of each ITN asset on each network.

Hide child attributes

assets.symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

assets.networks

object[]

required

The asset's availability on each network.

Show child attributes

[List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets)[Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- booleanrequired
- object | nullrequired
- The reason the side is closed. null when the side is open.
- stringrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#webpage","url":"https://docs.ondo.finance/api-reference/itn/get-itn-status","name":"Get ITN Status","description":"This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","dateModified":"2026-11-12T23:40:59.756Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"ITN","item":"https://docs.ondo.finance/api-reference/itn/list-itn-assets"},{"@type":"ListItem","position":3,"name":"Get ITN Status","item":"https://docs.ondo.finance/api-reference/itn/get-itn-status"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#apireference","headline":"Get ITN Status","name":"Get ITN Status","description":"This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","url":"https://docs.ondo.finance/api-reference/itn/get-itn-status","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#webpage"},"dateModified":"2026-11-12T23:40:59.756Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/itn/list-itn-assets>>>
---
url: https://docs.ondo.finance/api-reference/itn/list-itn-assets
title: List ITN Assets - Ondo Finance
description: This endpoint lists every asset available through Alpaca's Instant Tokenization Network (ITN) and the networks each asset is deployed on. For each network, it returns the token contract address, the token decimals, and the ITN mint and redeem fees. For current mint and redeem availability, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.
fetched: 2026-11-16
method: render
plan: read
---

List ITN Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/assets",
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

	url := "https://api.gm.ondo.finance/v1/itn/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/assets")

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
    "networks": [
      {
        "networkChainId": "bsc-56",
        "evmChainId": 56,
        "alpacaNetwork": "binance",
        "tokenAddress": "0x390a684ef9cade28a7ad0dfa61ab1eb3842618c4",
        "decimals": 18,
        "mintFeeBps": 0,
        "redeemFeeBps": 5
      },
      {
        "networkChainId": "ethereum-1",
        "evmChainId": 1,
        "alpacaNetwork": "ethereum",
        "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
        "decimals": 18,
        "mintFeeBps": 0,
        "redeemFeeBps": 5
      }
    ]
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

ITN

# List ITN Assets

Copy pageCopy page

This endpoint lists every asset available through Alpaca’s Instant Tokenization Network (ITN) and the networks each asset is deployed on. For each network, it returns the token contract address, the token decimals, and the ITN mint and redeem fees.

For current mint and redeem availability, see [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status).

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

For the complete ITN workflow, see [ITN Integration](https://docs.ondo.finance/api-reference/itn-integration).

Copy pageCopy page

GET

/

v1

/

itn

/

assets

Try it

List ITN Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/assets",
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

	url := "https://api.gm.ondo.finance/v1/itn/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/assets")

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
    "networks": [
      {
        "networkChainId": "bsc-56",
        "evmChainId": 56,
        "alpacaNetwork": "binance",
        "tokenAddress": "0x390a684ef9cade28a7ad0dfa61ab1eb3842618c4",
        "decimals": 18,
        "mintFeeBps": 0,
        "redeemFeeBps": 5
      },
      {
        "networkChainId": "ethereum-1",
        "evmChainId": 1,
        "alpacaNetwork": "ethereum",
        "tokenAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
        "decimals": 18,
        "mintFeeBps": 0,
        "redeemFeeBps": 5
      }
    ]
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

The GM token symbol.

Example:

`"AAPLon"`

ticker

string

required

The stock ticker associated with the asset.

Example:

`"AAPL"`

networks

object[]

required

The networks the asset is available on through ITN.

Hide child attributes

networks.networkChainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

networks.alpacaNetwork

string

required

Alpaca's name for the network. Use this value when submitting a request to Alpaca.

Example:

`"ethereum"`

networks.tokenAddress

string

required

The token contract address on the network.

Example:

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

networks.decimals

integer<int64>

required

The number of decimal places for the token on the network.

Example:

`18`

networks.mintFeeBps

integer<int64>

required

The ITN mint fee, in basis points.

Example:

`0`

networks.redeemFeeBps

integer<int64>

required

The ITN redeem fee, in basis points.

Example:

`5`

networks.evmChainId

integer<int64>

The EVM chain ID of the network. Omitted for non-EVM networks.

Example:

`1`

[Get Asset Statuses](https://docs.ondo.finance/api-reference/status/get-asset-statuses)[Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status)

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/itn/list-itn-assets#webpage","url":"https://docs.ondo.finance/api-reference/itn/list-itn-assets","name":"List ITN Assets","description":"This endpoint lists every asset available through Alpaca's Instant Tokenization Network (ITN) and the networks each asset is deployed on. For each network, it returns the token contract address, the token decimals, and the ITN mint and redeem fees. For current mint and redeem availability, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","dateModified":"2026-11-12T23:40:59.740Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/itn/list-itn-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/itn/list-itn-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"List ITN Assets","item":"https://docs.ondo.finance/api-reference/itn/list-itn-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/itn/list-itn-assets#apireference","headline":"List ITN Assets","name":"List ITN Assets","description":"This endpoint lists every asset available through Alpaca's Instant Tokenization Network (ITN) and the networks each asset is deployed on. For each network, it returns the token contract address, the token decimals, and the ITN mint and redeem fees. For current mint and redeem availability, see Get ITN Status. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","url":"https://docs.ondo.finance/api-reference/itn/list-itn-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/itn/list-itn-assets#webpage"},"dateModified":"2026-11-12T23:40:59.740Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/limits/get-session-limits>>>
---
url: https://docs.ondo.finance/api-reference/limits/get-session-limits
title: Get Session Limits - Ondo Finance
description: Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The "Max Attestation Count" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The "Max Active Notional Value" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \$1,000,000, and has 30 non-expired, non-filled attestations at a value of \$999,000, they will not be able to request another attestation for \$1000. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Session Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/session \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/session"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/session', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/session",
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

	url := "https://api.gm.ondo.finance/v1/limits/session"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/session")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/session")

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
[
  {
    "limits": [
      {
        "symbol": "AAPLon",
        "premarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "10000"
        },
        "regular": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "postmarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "overnight": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "offhours": {
          "tradable": false,
          "maxAttestationCount": "0",
          "maxActiveNotionalValue": "0"
        }
      },
      "..."
    ],
    "timestamp": 1769192550134
  }
]
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
  "message": "asset not found",
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

Limits

# Get Session Limits

Copy pageCopy page

Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo’s statically defined limits; for dynamic, real-time values, see [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits).

Limits are returned for each session: `premarket`, `regular`, `postmarket`, `overnight`, and `offhours`. The `offhours` block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (`tradable: false`).

Limits:

* The “Max Attestation Count” limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another.
* The “Max Active Notional Value” limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of $1,000,000, and has 30 non-expired, non-filled attestations at a value of $999,000, they will not be able to request another attestation for $1000.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

limits

/

session

Try it

Get Session Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/session \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/session"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/session', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/session",
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

	url := "https://api.gm.ondo.finance/v1/limits/session"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/session")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/session")

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
[
  {
    "limits": [
      {
        "symbol": "AAPLon",
        "premarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "10000"
        },
        "regular": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "postmarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "overnight": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "offhours": {
          "tradable": false,
          "maxAttestationCount": "0",
          "maxActiveNotionalValue": "0"
        }
      },
      "..."
    ],
    "timestamp": 1769192550134
  }
]
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
  "message": "asset not found",
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

#### Query Parameters

symbol

string

The GM token symbol.

#### Response

200

application/json

OK

limits

object[]

required

Hide child attributes

limits.symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

limits.premarket

object

required

Show child attributes

limits.regular

object

required

Show child attributes

limits.postmarket

object

required

Show child attributes

limits.overnight

object

required

Show child attributes

limits.offhours

object

required

Trading limits that apply when the US equities market is closed for the day (e.g., weekends and holidays).

Show child attributes

timestamp

number

required

The Unix timestamp in milliseconds when the trading limits were last updated.

Example:

`1769116067536`

[Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits)[Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- stringrequired
- objectrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#webpage","url":"https://docs.ondo.finance/api-reference/limits/get-session-limits","name":"Get Session Limits","description":"Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The \"Max Attestation Count\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The \"Max Active Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.694Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Limits","item":"https://docs.ondo.finance/api-reference/limits/get-trading-limits"},{"@type":"ListItem","position":3,"name":"Get Session Limits","item":"https://docs.ondo.finance/api-reference/limits/get-session-limits"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#apireference","headline":"Get Session Limits","name":"Get Session Limits","description":"Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The \"Max Attestation Count\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The \"Max Active Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/limits/get-session-limits","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#webpage"},"dateModified":"2026-11-12T23:40:59.694Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```