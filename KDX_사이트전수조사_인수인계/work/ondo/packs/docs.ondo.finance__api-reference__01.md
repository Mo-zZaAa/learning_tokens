# 읽기 묶음: docs.ondo.finance / api-reference (1/5)


<<<PAGE https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks
title: Get All Contract Addresses Across Networks - Ondo Finance
description: This endpoint retrieves all contract addresses for all supported assets across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get All Contract Addresses Across Networks

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/addresses \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/addresses"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/addresses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/addresses",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/addresses"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/addresses")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/addresses")

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
  },
  {
    "symbol": "ABNBon",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0xef80743f78d98fc2b47a2253b293152ce8b879ba",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0xb035c3d5083bdc80074f380aebc9fcb68aba0a28",
        "decimals": 18
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

Assets

# Get All Contract Addresses Across Networks

Copy pageCopy page

This endpoint retrieves all contract addresses for all supported assets across different blockchain networks.

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

addresses

Try it

Get All Contract Addresses Across Networks

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/addresses \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/addresses"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/addresses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/addresses",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/addresses"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/addresses")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/addresses")

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
  },
  {
    "symbol": "ABNBon",
    "addresses": [
      {
        "networkChainId": "bsc-56",
        "address": "0xef80743f78d98fc2b47a2253b293152ce8b879ba",
        "decimals": 18
      },
      {
        "networkChainId": "ethereum-1",
        "address": "0xb035c3d5083bdc80074f380aebc9fcb68aba0a28",
        "decimals": 18
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

The GM symbol associated with the asset.

Example:

`"AAPLon"`

addresses

object[]

required

Hide child attributes

addresses.networkChainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

addresses.address

string

required

The contract address on the specified chain.

Example:

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

addresses.decimals

integer<int64>

required

The number of decimals places for the asset.

Example:

`18`

[Get Dividend Information for an Asset](https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset)[Get Contract Addresses for an Asset](https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset)

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks","name":"Get All Contract Addresses Across Networks","description":"This endpoint retrieves all contract addresses for all supported assets across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.538Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get All Contract Addresses Across Networks","item":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks#apireference","headline":"Get All Contract Addresses Across Networks","name":"Get All Contract Addresses Across Networks","description":"This endpoint retrieves all contract addresses for all supported assets across different blockchain networks. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks#webpage"},"dateModified":"2026-11-12T23:40:59.538Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset>>>
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

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset
title: Get Current Price for an Asset - Ondo Finance
description: This endpoint retrieves the latest price for a specific asset. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Current Price for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest")

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
  "primaryMarket": {
    "symbol": "AAPLon",
    "price": "12.345"
  },
  "underlyingMarket": {
    "ticker": "AAPL",
    "price": "12.345"
  },
  "timestamp": 1746655938
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

# Get Current Price for an Asset

Copy pageCopy page

This endpoint retrieves the latest price for a specific asset. Note that the `primaryMarket` represents the on-chain token while the `underlyingMarket`
represents the off-chain collateralized stock.

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

{symbol}

/

prices

/

latest

Try it

Get Current Price for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/prices/latest")

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
  "primaryMarket": {
    "symbol": "AAPLon",
    "price": "12.345"
  },
  "underlyingMarket": {
    "ticker": "AAPL",
    "price": "12.345"
  },
  "timestamp": 1746655938
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

Price fetched successfully

primaryMarket

object

required

Hide child attributes

primaryMarket.symbol

string

The GM symbol of the asset.

Example:

`"AAPLon"`

primaryMarket.price

string

The token price, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

underlyingMarket

object

required

Hide child attributes

underlyingMarket.ticker

string

The stock ticker associated with the asset.

Example:

`"AAPL"`

underlyingMarket.price

string

The stock price, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

timestamp

number

required

The Unix timestamp in milliseconds, representing the time of the price data retrieval.

Example:

`1746655938`

[Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets)[Get Enhanced Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset","name":"Get Current Price for an Asset","description":"This endpoint retrieves the latest price for a specific asset. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.438Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Current Price for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset#apireference","headline":"Get Current Price for an Asset","name":"Get Current Price for an Asset","description":"This endpoint retrieves the latest price for a specific asset. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.438Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets
title: Get Current Prices for All Supported Assets - Ondo Finance
description: This endpoint retrieves the latest prices for all supported assets. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Current Prices for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/prices/latest \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/prices/latest"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/prices/latest', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/prices/latest",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/prices/latest"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/prices/latest")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/prices/latest")

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
    "primaryMarket": {
      "symbol": "TSLAon",
      "price": "48.516937826065743784"
    },
    "underlyingMarket": {
      "ticker": "TSLA",
      "price": "338.88"
    },
    "timestamp": 1755888858907
  },
  {
    "primaryMarket": {
      "symbol": "AAPLon",
      "price": "171.383708297189751178"
    },
    "underlyingMarket": {
      "ticker": "AAPL",
      "price": "228.330909"
    },
    "timestamp": 1755888858893
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

# Get Current Prices for All Supported Assets

Copy pageCopy page

This endpoint retrieves the latest prices for all supported assets. Note that the `primaryMarket` represents the on-chain token while the `underlyingMarket`
represents the off-chain collateralized stock. Assets can be sorted by price in either ascending or descending order.

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

Try it

Get Current Prices for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/prices/latest \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/prices/latest"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/prices/latest', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/prices/latest",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/prices/latest"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/prices/latest")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/prices/latest")

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
    "primaryMarket": {
      "symbol": "TSLAon",
      "price": "48.516937826065743784"
    },
    "underlyingMarket": {
      "ticker": "TSLA",
      "price": "338.88"
    },
    "timestamp": 1755888858907
  },
  {
    "primaryMarket": {
      "symbol": "AAPLon",
      "price": "171.383708297189751178"
    },
    "underlyingMarket": {
      "ticker": "AAPL",
      "price": "228.330909"
    },
    "timestamp": 1755888858893
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

The sort direction for prices.

Available options:

`desc`,

`asc`

#### Response

200

application/json

OK

primaryMarket

object

required

Hide child attributes

primaryMarket.symbol

string

The GM symbol of the asset.

Example:

`"AAPLon"`

primaryMarket.price

string

The token price, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

underlyingMarket

object

required

Hide child attributes

underlyingMarket.ticker

string

The stock ticker associated with the asset.

Example:

`"AAPL"`

underlyingMarket.price

string

The stock price, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

timestamp

number

required

The Unix timestamp in milliseconds, representing the time of the price data retrieval.

Example:

`1746655938`

[Request a Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote)[Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets","name":"Get Current Prices for All Supported Assets","description":"This endpoint retrieves the latest prices for all supported assets. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.423Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Current Prices for All Supported Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets#apireference","headline":"Get Current Prices for All Supported Assets","name":"Get Current Prices for All Supported Assets","description":"This endpoint retrieves the latest prices for all supported assets. Note that the primaryMarket represents the on-chain token while the underlyingMarket represents the off-chain collateralized stock. Assets can be sorted by price in either ascending or descending order. For real-time price updates as they occur, rather than repeatedly polling this endpoint, use the Price Streaming endpoint. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets#webpage"},"dateModified":"2026-11-12T23:40:59.423Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset
title: Get Dividend Information for an Asset - Ondo Finance
description: This endpoint retrieves the latest dividend information for a specific asset, including dividend yield, payment history, and upcoming payment dates. Dividend Yield The dividend yield is calculated based on the past year's worth of dividend payments and the current stock price. Stock Splits Dividend amounts are adjusted for completed stock splits and stated per current share. Each dividend paid before a split is divided by the split ratio, so pre-split dividends are comparable to the current post-split price. For example, after a 10:1 split, a pre-split dividend of $1.00 is counted as $0.10. This adjustment applies to both dividendYield and lastCashAmount. Payout Frequencies Below outline the day ranges for each payout frequency: | Frequency | Average Days Between Dividends | |-------------------|:------------------------------:| | none | N/A | | monthly | 25-35 days | | quarterly | 80-100 days | | semi-annually | 160-200 days | | yearly | 345-385 days | | irregular | Outside defined ranges | For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Dividend Information for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/dividends \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/dividends', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/dividends")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/dividends")

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
  "ticker": "AAPL",
  "dividendYield": "0.0245",
  "payoutFrequency": "quarterly",
  "lastCashAmount": "1.54",
  "lastPaymentDate": "2025-02-15",
  "timestamp": 1746655938000
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

# Get Dividend Information for an Asset

Copy pageCopy page

This endpoint retrieves the latest dividend information for a specific asset, including dividend yield, payment history, and upcoming payment dates.

**Dividend Yield**

The dividend yield is calculated based on the past year’s worth of dividend payments and the current stock price.

**Stock Splits**

Dividend amounts are adjusted for completed stock splits and stated per current share. Each dividend paid before a split is divided by the split ratio, so pre-split dividends are comparable to the current post-split price. For example, after a 10:1 split, a pre-split dividend of `$1.00` is counted as `$0.10`. This adjustment applies to both `dividendYield` and `lastCashAmount`.

**Payout Frequencies**

Below outline the day ranges for each payout frequency:

| Frequency | Average Days Between Dividends |
| --- | --- |
| **none** | N/A |
| **monthly** | 25-35 days |
| **quarterly** | 80-100 days |
| **semi-annually** | 160-200 days |
| **yearly** | 345-385 days |
| **irregular** | Outside defined ranges |

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

dividends

Try it

Get Dividend Information for an Asset

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/{symbol}/dividends \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/{symbol}/dividends', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends",
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

	url := "https://api.gm.ondo.finance/v1/assets/{symbol}/dividends"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/{symbol}/dividends")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/{symbol}/dividends")

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
  "ticker": "AAPL",
  "dividendYield": "0.0245",
  "payoutFrequency": "quarterly",
  "lastCashAmount": "1.54",
  "lastPaymentDate": "2025-02-15",
  "timestamp": 1746655938000
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

ticker

string

required

The stock ticker associated with the asset.

Example:

`"AAPL"`

dividendYield

string

required

The trailing-twelve-month dividend yield, using split-adjusted dividend amounts divided by the current stock price. Represented as a string-encoded decimal with up to 18 digits after the decimal point. ("0.05" is the equivalent of 5%)

Example:

`"0.0245"`

payoutFrequency

enum<string>

required

The frequency at which dividends are paid to shareholders.

Available options:

`monthly`,

`quarterly`,

`semi-annually`,

`annually`,

`irregular`,

`none`

Example:

`"quarterly"`

lastCashAmount

string

required

The last dividend payment amount per current share, adjusted for any completed stock splits since the dividend ex-date, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1.54"`

lastPaymentDate

string<date>

required

The date of last dividend payment in YYYY-MM-DD format.

Example:

`"2025-02-15"`

timestamp

number

required

The Unix timestamp in milliseconds when the data was last updated.

Example:

`1746655938000`

[Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset)[Get All Contract Addresses Across Networks](https://docs.ondo.finance/api-reference/assets/get-all-contract-addresses-across-networks)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset","name":"Get Dividend Information for an Asset","description":"This endpoint retrieves the latest dividend information for a specific asset, including dividend yield, payment history, and upcoming payment dates. Dividend Yield The dividend yield is calculated based on the past year's worth of dividend payments and the current stock price. Stock Splits Dividend amounts are adjusted for completed stock splits and stated per current share. Each dividend paid before a split is divided by the split ratio, so pre-split dividends are comparable to the current post-split price. For example, after a 10:1 split, a pre-split dividend of $1.00 is counted as $0.10. This adjustment applies to both dividendYield and lastCashAmount. Payout Frequencies Below outline the day ranges for each payout frequency: | Frequency | Average Days Between Dividends | |-------------------|:------------------------------:| | none | N/A | | monthly | 25-35 days | | quarterly | 80-100 days | | semi-annually | 160-200 days | | yearly | 345-385 days | | irregular | Outside defined ranges | For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.523Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Dividend Information for an Asset","item":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset#apireference","headline":"Get Dividend Information for an Asset","name":"Get Dividend Information for an Asset","description":"This endpoint retrieves the latest dividend information for a specific asset, including dividend yield, payment history, and upcoming payment dates. Dividend Yield The dividend yield is calculated based on the past year's worth of dividend payments and the current stock price. Stock Splits Dividend amounts are adjusted for completed stock splits and stated per current share. Each dividend paid before a split is divided by the split ratio, so pre-split dividends are comparable to the current post-split price. For example, after a 10:1 split, a pre-split dividend of $1.00 is counted as $0.10. This adjustment applies to both dividendYield and lastCashAmount. Payout Frequencies Below outline the day ranges for each payout frequency: | Frequency | Average Days Between Dividends | |-------------------|:------------------------------:| | none | N/A | | monthly | 25-35 days | | quarterly | 80-100 days | | semi-annually | 160-200 days | | yearly | 345-385 days | | irregular | Outside defined ranges | For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-dividend-information-for-an-asset#webpage"},"dateModified":"2026-11-12T23:40:59.523Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets>>>
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

<<<PAGE https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets>>>
---
url: https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets
title: Get Market Data for All Supported Assets - Ondo Finance
description: This endpoint retrieves comprehensive market data for all supported assets. Each asset includes both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The "Tradable Sessions" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Market Data for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/market",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/market")

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
    "primaryMarket": {
      "symbol": "ADBEon",
      "price": "361.986667",
      "priceChange24h": "8.76",
      "priceChangePct24h": "2.479993958100564361",
      "priceHistory24h": [
        {
          "timestamp": 1755802800000,
          "price": "353.226667"
        },
        {
          "timestamp": 1755803700000,
          "price": "353.216667"
        },
        "..."
      ],
      "totalHolders": 7,
      "sharesMultiplier": "1"
    },
    "underlyingMarket": {
      "ticker": "ADBE",
      "name": "Adobe Inc.",
      "price": "361.986667",
      "priceHigh52w": "587.75",
      "priceLow52w": "330.04",
      "volume": "1851321",
      "averageVolume": "3610882",
      "sharesOutstanding": "424200000",
      "marketCap": "149925006000"
    },
    "constituentTokens": [],
    "timestamp": 1755890061815
  },
  {
    "primaryMarket": {
      "symbol": "APPon",
      "price": "440.094",
      "priceChange24h": "20.824",
      "priceChangePct24h": "4.966727884179645574",
      "priceHistory24h": [
        {
          "timestamp": 1755802800000,
          "price": "419.27"
        },
        {
          "timestamp": 1755803700000,
          "price": "418.55"
        },
        "..."
      ],
      "totalHolders": 7,
      "sharesMultiplier": "1",
      "tradableSessions": [
        "premarket",
        "regular",
        "postmarket",
        "overnight"
      ]
    },
    "underlyingMarket": {
      "ticker": "APP",
      "name": "Applovin Corporation Class A Common Stock",
      "price": "440.094",
      "priceHigh52w": "525.15",
      "priceLow52w": "82.51",
      "volume": "5220144",
      "averageVolume": "6480111",
      "sharesOutstanding": "307636373",
      "marketCap": "139487499535"
    },
    "constituentTokens": [],
    "timestamp": 1755890062869
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

Assets

# Get Market Data for All Supported Assets

Copy pageCopy page

This endpoint retrieves comprehensive market data for all supported assets. Each asset includes both primary market (on-chain token) and underlying market (off-chain stock) information.

Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization.

This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio.

The “Tradable Sessions” parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status).

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

market

Try it

Get Market Data for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/market",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/market")

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
    "primaryMarket": {
      "symbol": "ADBEon",
      "price": "361.986667",
      "priceChange24h": "8.76",
      "priceChangePct24h": "2.479993958100564361",
      "priceHistory24h": [
        {
          "timestamp": 1755802800000,
          "price": "353.226667"
        },
        {
          "timestamp": 1755803700000,
          "price": "353.216667"
        },
        "..."
      ],
      "totalHolders": 7,
      "sharesMultiplier": "1"
    },
    "underlyingMarket": {
      "ticker": "ADBE",
      "name": "Adobe Inc.",
      "price": "361.986667",
      "priceHigh52w": "587.75",
      "priceLow52w": "330.04",
      "volume": "1851321",
      "averageVolume": "3610882",
      "sharesOutstanding": "424200000",
      "marketCap": "149925006000"
    },
    "constituentTokens": [],
    "timestamp": 1755890061815
  },
  {
    "primaryMarket": {
      "symbol": "APPon",
      "price": "440.094",
      "priceChange24h": "20.824",
      "priceChangePct24h": "4.966727884179645574",
      "priceHistory24h": [
        {
          "timestamp": 1755802800000,
          "price": "419.27"
        },
        {
          "timestamp": 1755803700000,
          "price": "418.55"
        },
        "..."
      ],
      "totalHolders": 7,
      "sharesMultiplier": "1",
      "tradableSessions": [
        "premarket",
        "regular",
        "postmarket",
        "overnight"
      ]
    },
    "underlyingMarket": {
      "ticker": "APP",
      "name": "Applovin Corporation Class A Common Stock",
      "price": "440.094",
      "priceHigh52w": "525.15",
      "priceLow52w": "82.51",
      "volume": "5220144",
      "averageVolume": "6480111",
      "sharesOutstanding": "307636373",
      "marketCap": "139487499535"
    },
    "constituentTokens": [],
    "timestamp": 1755890062869
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

Market data behaves differently by asset type. For standard tokens, `underlyingMarket` is populated and `constituentTokens` is an empty array. For Ondo Intelligent Portfolios (OIPs), `underlyingMarket` is `null` and `constituentTokens` lists the portfolio’s constituent GM token symbols.

#### Authorizations

x-api-key

string

header

required

#### Response

200

application/json

OK

primaryMarket

object

required

Hide child attributes

primaryMarket.symbol

string

The GM symbol of the asset.

Example:

`"AAPLon"`

primaryMarket.price

string

The current price of the asset, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"12.345"`

primaryMarket.priceChange24h

string

The price change in the last 24 hours of open market.

Example:

`"0.123"`

primaryMarket.priceChangePct24h

string

The percentage change in price over the last 24 hours of open market.

Example:

`"5.45"`

primaryMarket.priceHistory24h

object[]

Historical price data for the last 24 hours of open market.

Show child attributes

primaryMarket.totalHolders

number

The total number of holders for the asset

Example:

`1234`

primaryMarket.sharesMultiplier

string

The number of shares each token is equivalent to, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1.25"`

primaryMarket.tradableSessions

enum<string>[]

The trading sessions during which this asset is available for trading. Includes `offhours` for assets that opt in to off-hours trading (weekends, the window after the Friday postmarket close, or eligible holidays). `offhours` is only included when off-hours trading is enabled.

Available options:

`premarket`,

`regular`,

`postmarket`,

`overnight`,

`offhours`

Example:

```
[  
  "premarket",  
  "regular",  
  "postmarket",  
  "overnight",  
  "offhours"  
]
```

underlyingMarket

object | null

required

The off-chain stock that backs the token. This is `null` for tokens that represent several underlying assets rather than a single stock; for those, see `constituentTokens`. For a token backed by a single stock, this object is populated as shown.

Hide child attributes

underlyingMarket.ticker

string

The stock ticker associated with the asset.

Example:

`"AAPL"`

underlyingMarket.name

string

The company's name.

Example:

`"Apple Inc"`

underlyingMarket.price

string

The current price of the underlying stock, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"195.34"`

underlyingMarket.priceHigh52w

string

The highest trading price in the past 52 weeks, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"259.47"`

underlyingMarket.priceLow52w

string

The lowest trading price in the past 52 weeks, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"168.99"`

underlyingMarket.volume

string

The total trading volume in the past 24 hours, represented as a string-encoded integer.

Example:

`"43020691"`

underlyingMarket.averageVolume

string

The average trading volume over the past year, represented as a string-encoded integer.

Example:

`"38390632"`

underlyingMarket.sharesOutstanding

string

The total number of shares outstanding, represented as a string-encoded integer.

Example:

`"14935800000"`

underlyingMarket.marketCap

string

The total market capitalization in USD, represented as a string-encoded integer.

Example:

`"2934137946000"`

constituentTokens

string[]

required

GM token symbols of the underlying assets that make up this token, for tokens that represent several underlying assets rather than a single stock. Each symbol can be looked up individually via the market endpoints. For a token backed by a single stock this is an empty array (`[]`), and `underlyingMarket` is populated instead.

Example:

```
["AAPLon", "MSFTon", "NVDAon"]
```

timestamp

number

required

The Unix timestamp in milliseconds when the data was last updated.

Example:

`1746655938000`

[Get OHLC (Open, High, Low, Close) Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset)[Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The trading sessions during which this asset is available for trading. Includes offhours for assets that opt in to off-hours trading (weekends, the window after the Friday postmarket close, or eligible holidays). offhours is only included when off-hours trading is enabled.
- Available options: premarket, regular, postmarket, overnight, offhours

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets","name":"Get Market Data for All Supported Assets","description":"This endpoint retrieves comprehensive market data for all supported assets. Each asset includes both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The \"Tradable Sessions\" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.484Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Market Data for All Supported Assets","item":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets#apireference","headline":"Get Market Data for All Supported Assets","name":"Get Market Data for All Supported Assets","description":"This endpoint retrieves comprehensive market data for all supported assets. Each asset includes both primary market (on-chain token) and underlying market (off-chain stock) information. Primary market data includes current price, 24-hour price changes, 24-hour historical chart data, and total token holders. Underlying market data provides stock fundamentals like company name, 52-week highs/lows, trading volume, shares outstanding, and market capitalization. This endpoint is useful for dashboard overviews and market analysis across the entire asset portfolio. The \"Tradable Sessions\" parameter indicates the tradability for the asset; for example, some assets are available in the regular and extended stock sessions, but not overnight. Learn more about sessions at Get Current Market Status. Prices are intended for display only. For real-time trading prices, use the Soft Attestation Quote API. We do not recommend using the price feeds as an oracle for these assets. An official oracle is in development and will be documented when available. For questions, contact support@ondo.finance. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets#webpage"},"dateModified":"2026-11-12T23:40:59.484Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```