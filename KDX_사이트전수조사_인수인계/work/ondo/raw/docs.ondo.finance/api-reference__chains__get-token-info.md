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