---
url: https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets
title: Get Metadata for All Supported Assets - Ondo Finance
description: Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Metadata for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/metadata \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/metadata"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/metadata', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/metadata",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/metadata"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/metadata")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/metadata")

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
    "underlyingName": "Apple",
    "displayName": "Apple (Ondo Tokenized)",
    "coingeckoId": "apple-ondo-tokenized-stock",
    "coinmarketCapId": "38037",
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
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0378331005",
    "logoURI": "https://assets.coingecko.com/coins/images/56760/large/aaplon.png",
    "isPortfolio": false
  },
  {
    "symbol": "ABNBon",
    "ticker": "ABNB",
    "underlyingName": "Airbnb",
    "displayName": "Airbnb (Ondo Tokenized)",
    "coingeckoId": "airbnb-ondo-tokenized-stock",
    "coinmarketCapId": "38044",
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
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0090661010",
    "logoURI": "https://assets.coingecko.com/coins/images/56774/large/abnbon.png",
    "isPortfolio": false
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

# Get Metadata for All Supported Assets

Copy pageCopy page

Returns all metadata for all symbols including identifiers, addresses, and classification tags.

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

metadata

Try it

Get Metadata for All Supported Assets

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/assets/all/metadata \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/assets/all/metadata"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/assets/all/metadata', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/assets/all/metadata",
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

	url := "https://api.gm.ondo.finance/v1/assets/all/metadata"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/assets/all/metadata")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/assets/all/metadata")

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
    "underlyingName": "Apple",
    "displayName": "Apple (Ondo Tokenized)",
    "coingeckoId": "apple-ondo-tokenized-stock",
    "coinmarketCapId": "38037",
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
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0378331005",
    "logoURI": "https://assets.coingecko.com/coins/images/56760/large/aaplon.png",
    "isPortfolio": false
  },
  {
    "symbol": "ABNBon",
    "ticker": "ABNB",
    "underlyingName": "Airbnb",
    "displayName": "Airbnb (Ondo Tokenized)",
    "coingeckoId": "airbnb-ondo-tokenized-stock",
    "coinmarketCapId": "38044",
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
    ],
    "tags": {
      "assetClass": "Equities",
      "instrumentType": "Stock"
    },
    "isin": "US0090661010",
    "logoURI": "https://assets.coingecko.com/coins/images/56774/large/abnbon.png",
    "isPortfolio": false
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

Example:

`"AAPLon"`

ticker

string

required

Example:

`"AAPL"`

tags

object

required

Hide child attributes

tags.assetClass

string

required

High-level category of the asset

Example:

`"equities"`

tags.instrumentType

string

required

Instrument type within the asset class

Example:

`"stock"`

tags.sectorIndustry

string[]

Sector and industry classifications for the asset.

Example:

```
["Technology", "Consumer Electronics"]
```

tags.typeFactorRiskProfile

string[]

Type, factor, and risk profile classifications.

Example:

```
["Growth", "Large Cap"]
```

tags.regionMarketExposure

string[]

Region and market exposure classifications.

Example:

```
["US", "Global"]
```

underlyingName

string

Human-readable name of the underlying instrument. Empty string if no name is available for this asset.

Example:

`"Apple"`

displayName

string

Token name as shown in user interfaces. Empty string if no name is available for this asset.

Example:

`"Apple (Ondo Tokenized)"`

coingeckoId

string | null

Example:

`"apple-ondo-tokenized-stock"`

addresses

object[]

Contract addresses for various chains.

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

Example:

```
[  
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
```

coinmarketcapId

string | null

Example:

`"38037"`

isin

string

The 12-character International Securities Identification Number (ISIN) for the underlying instrument. Empty string if unknown or not applicable (e.g., non-equity assets).

Example:

`"US0378331005"`

logoURI

string

URL to the asset's logo image. Empty string if no logo is available for this asset.

Example:

`"https://assets.coingecko.com/coins/images/56760/large/aaplon.png"`

isPortfolio

boolean

Example:

`false`

[Get Contract Addresses for an Asset](https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset)[Get Shares Multiplier History for an Asset](https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset)

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#webpage","url":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets","name":"Get Metadata for All Supported Assets","description":"Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.569Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Assets","item":"https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets"},{"@type":"ListItem","position":3,"name":"Get Metadata for All Supported Assets","item":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#apireference","headline":"Get Metadata for All Supported Assets","name":"Get Metadata for All Supported Assets","description":"Returns all metadata for all symbols including identifiers, addresses, and classification tags. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets#webpage"},"dateModified":"2026-11-12T23:40:59.569Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```