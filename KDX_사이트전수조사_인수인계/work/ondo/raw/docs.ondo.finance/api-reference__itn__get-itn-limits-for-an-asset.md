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