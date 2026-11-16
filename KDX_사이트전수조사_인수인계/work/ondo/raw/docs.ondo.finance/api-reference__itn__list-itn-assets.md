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