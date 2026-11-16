---
url: https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset
title: Get Contract Addresses for an Asset - Ondo Finance
description: This endpoint retrieves all contract addresses for a specific asset across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Contract Addresses for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/addresses \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/addresses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/addresses")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/addresses")

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
  "symbol": "AAPLon",
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

# Get Contract Addresses for an Asset

Copy pageCopy page

This endpoint retrieves all contract addresses for a specific asset across different blockchain networks.

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

addresses

Try it

Get Contract Addresses for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/addresses \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/addresses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/addresses"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/addresses")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/addresses")

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
  "symbol": "AAPLon",
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

#### Response

200

application/json

OK

networkChainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

address

string

required

The contract address on the specified chain.

Example:

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

decimals

integer<int64>

required

The number of decimals places for the asset.

Example:

`18`

[Get All Contract Addresses Across Networks](https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks)[Get Metadata for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset","name":"Get Contract Addresses for an Asset","description":"This endpoint retrieves all contract addresses for a specific asset across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.554Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Contract Addresses for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset#apireference","headline":"Get Contract Addresses for an Asset","name":"Get Contract Addresses for an Asset","description":"This endpoint retrieves all contract addresses for a specific asset across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.554Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```