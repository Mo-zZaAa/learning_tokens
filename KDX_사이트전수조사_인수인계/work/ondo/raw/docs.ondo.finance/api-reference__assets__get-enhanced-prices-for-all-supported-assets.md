---
url: https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets
title: Get Enhanced Prices for All Supported Assets - Ondo Finance
description: This endpoint retrieves the latest prices along with the price change and percentage change in the last 24 hours of open market for all supported assets. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Enhanced Prices for All Supported Assets

cURL

```
curl --request GET \
  --url 'https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc' \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc")

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
[
  {
    "symbol": "NFLXon",
    "price": "860.66471",
    "priceChange24h": "26.80883",
    "priceChangePct24h": "3.215043587628116264",
    "timestamp": 1769190970623
  },
  {
    "symbol": "QQQon",
    "price": "533.707886795396811068",
    "priceChange24h": "0.175407218134272389",
    "priceChangePct24h": "0.032876577312266724",
    "timestamp": 1769190970623
  },
  "..."
]
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

# Get Enhanced Prices for All Supported Assets

Copy pageCopy page

This endpoint retrieves the latest prices along with the price change and percentage change in the last 24 hours of open market for all supported assets. Assets can be sorted by price in either ascending or descending order.

For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the [Price Streaming](https://docs.ondo.finance/api-reference/price-streaming) endpoint.

Prices are intended for display only. For real-time trading prices, use the [Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote) API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact [support@ondo.finance](mailto:support@ondo.finance).

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

prices

/

latest

/

enhanced

Try it

Get Enhanced Prices for All Supported Assets

cURL

```
curl --request GET \
  --url 'https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc' \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/prices/latest/enhanced?sort=desc")

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
[
  {
    "symbol": "NFLXon",
    "price": "860.66471",
    "priceChange24h": "26.80883",
    "priceChangePct24h": "3.215043587628116264",
    "timestamp": 1769190970623
  },
  {
    "symbol": "QQQon",
    "price": "533.707886795396811068",
    "priceChange24h": "0.175407218134272389",
    "priceChangePct24h": "0.032876577312266724",
    "timestamp": 1769190970623
  },
  "..."
]
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

sort

enum<string>

default:desc

The sort direction for prices.

Available options:

`desc`,

`asc`

#### Response

200

application/json

OK

symbol

string

required

The GM symbol of the asset.

Example:

`"NFLXon"`

price

string

required

The token price, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"836.26176"`

priceChange24h

string

required

The price change in the last 24 hours of open market.

Example:

`"-19.22815"`

priceChangePct24h

string

required

The percentage change in price over the last 24 hours of open market.

Example:

`"-2.247618560457364132"`

timestamp

number

required

The Unix timestamp in milliseconds when the data was last updated.

Example:

`1769125830623`

[Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset)[Get OHLC (Open, High, Low, Close) Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets","name":"Get Enhanced Prices for All Supported Assets","description":"This endpoint retrieves the latest prices along with the price change and percentage change in the last 24 hours of open market for all supported assets. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.453Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Enhanced Prices for All Supported Assets","item":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets#apireference","headline":"Get Enhanced Prices for All Supported Assets","name":"Get Enhanced Prices for All Supported Assets","description":"This endpoint retrieves the latest prices along with the price change and percentage change in the last 24 hours of open market for all supported assets. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets#webpage"},"dateModified":"2026-11-12T23:40:59.453Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```