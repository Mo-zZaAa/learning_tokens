---
url: https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers
title: Get Price and Volume Data for All Supported Tickers - Ondo Finance
description: This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Price and Volume Data for All Supported Tickers

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/tickers \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/tickers"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/tickers', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/tickers",
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

	url := "https://api.gm.ondo.finance/v1/tickers"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/tickers")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/tickers")

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
    "tickerId": "TSLAon_USDon",
    "baseCurrency": "TSLAon",
    "targetCurrency": "USDon",
    "lastPrice": 338.42375,
    "baseVolume": 72.720573083,
    "targetVolume": 24610.369044819
  },
  {
    "tickerId": "AAPLon_USDon",
    "baseCurrency": "AAPLon",
    "targetCurrency": "USDon",
    "lastPrice": 228.195452051,
    "baseVolume": 2761.011833446,
    "targetVolume": 630050.34345192
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

Tickers

# Get Price and Volume Data for All Supported Tickers

Copy pageCopy page

This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

tickers

Try it

Get Price and Volume Data for All Supported Tickers

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/tickers \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/tickers"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/tickers', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/tickers",
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

	url := "https://api.gm.ondo.finance/v1/tickers"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/tickers")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/tickers")

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
    "tickerId": "TSLAon_USDon",
    "baseCurrency": "TSLAon",
    "targetCurrency": "USDon",
    "lastPrice": 338.42375,
    "baseVolume": 72.720573083,
    "targetVolume": 24610.369044819
  },
  {
    "tickerId": "AAPLon_USDon",
    "baseCurrency": "AAPLon",
    "targetCurrency": "USDon",
    "lastPrice": 228.195452051,
    "baseVolume": 2761.011833446,
    "targetVolume": 630050.34345192
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

tickerId

string

required

The identifier of a ticker, formatted as `<base>_<target>`.

Example:

`"aaplon_usdon"`

baseCurrency

string

required

The GM symbol of the base asset.

Example:

`"AAPLon"`

targetCurrency

string

required

The GM symbol of the target asset.

Example:

`"USDon"`

lastPrice

number

required

The last transacted price of base currency based on given target currency.

Example:

`12.34`

baseVolume

number

required

The 24 hour trading volume for the pair (unit in base).

Example:

`100`

targetVolume

number

required

The 24 hour trading volume for the pair (unit in target).

Example:

`250`

[Get a Portfolio](https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio)[Get Token Balances for a User or Token](https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#webpage","url":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers","name":"Get Price and Volume Data for All Supported Tickers","description":"This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.632Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Price and Volume Data for All Supported Tickers","item":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#apireference","headline":"Get Price and Volume Data for All Supported Tickers","name":"Get Price and Volume Data for All Supported Tickers","description":"This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#webpage"},"dateModified":"2026-11-12T23:40:59.632Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```