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