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