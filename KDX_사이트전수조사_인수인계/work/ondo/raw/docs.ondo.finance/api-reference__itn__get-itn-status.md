---
url: https://docs.ondo.finance/api-reference/itn/get-itn-status
title: Get ITN Status - Ondo Finance
description: This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.
fetched: 2026-11-16
method: render
plan: read
---

Get ITN Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/status \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/status"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/status",
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

	url := "https://api.gm.ondo.finance/v1/itn/status"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/status")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/status")

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
{
  "timestamp": 1759777200000,
  "currentSession": "regular",
  "mint": {
    "isOpen": true,
    "reason": null
  },
  "redeem": {
    "isOpen": true,
    "reason": null
  },
  "assets": [
    {
      "symbol": "AAPLon",
      "networks": [
        {
          "networkChainId": "bsc-56",
          "alpacaNetwork": "binance",
          "mint": {
            "enabled": false,
            "reason": {
              "code": "PAUSED_GM_CHAIN",
              "message": "chain is paused",
              "documentation": "https://docs.ondo.finance/api-reference/error-codes#paused_gm_chain"
            }
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        },
        {
          "networkChainId": "ethereum-1",
          "alpacaNetwork": "ethereum",
          "mint": {
            "enabled": true,
            "reason": null
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        }
      ]
    },
    "..."
  ]
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

ITN

# Get ITN Status

Copy pageCopy page

This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network.

**Global Status**

The top-level `mint` and `redeem` objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side.

**Per-Network Availability**

Each entry in `assets[].networks` reports whether minting and redeeming are enabled for that asset on that network.

**ITN Status Reason Codes**

When a side is closed or unavailable, `reason` is set. Otherwise, `reason` is `null`.

`reason.code` is one of:

* `ITN_UNAVAILABLE`: ITN is temporarily unavailable, either platform-wide or for the asset.
* `MARKET_PAUSED`: ITN minting or redeeming is paused for all assets.
* `PAUSED_GM_CHAIN`: ITN minting or redeeming is paused on the network. Only returned per network.
* `ASSET_PAUSED`: The asset is paused for ITN. Only returned per network.

For limits on how much you can mint or redeem, see [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset).

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

For the complete ITN workflow, see [ITN Integration](https://docs.ondo.finance/api-reference/itn-integration).

Copy pageCopy page

GET

/

v1

/

itn

/

status

Try it

Get ITN Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/itn/status \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/itn/status"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/itn/status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/itn/status",
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

	url := "https://api.gm.ondo.finance/v1/itn/status"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/itn/status")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/itn/status")

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
{
  "timestamp": 1759777200000,
  "currentSession": "regular",
  "mint": {
    "isOpen": true,
    "reason": null
  },
  "redeem": {
    "isOpen": true,
    "reason": null
  },
  "assets": [
    {
      "symbol": "AAPLon",
      "networks": [
        {
          "networkChainId": "bsc-56",
          "alpacaNetwork": "binance",
          "mint": {
            "enabled": false,
            "reason": {
              "code": "PAUSED_GM_CHAIN",
              "message": "chain is paused",
              "documentation": "https://docs.ondo.finance/api-reference/error-codes#paused_gm_chain"
            }
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        },
        {
          "networkChainId": "ethereum-1",
          "alpacaNetwork": "ethereum",
          "mint": {
            "enabled": true,
            "reason": null
          },
          "redeem": {
            "enabled": true,
            "reason": null
          }
        }
      ]
    },
    "..."
  ]
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

#### Response

200

application/json

OK

timestamp

number

required

The Unix timestamp in milliseconds when the status was evaluated.

Example:

`1759777200000`

currentSession

enum<string>

required

The current market session.

Available options:

`premarket`,

`regular`,

`postmarket`,

`overnight`,

`offhours`

Example:

`"regular"`

mint

object

required

Whether ITN minting is open globally.

Hide child attributes

mint.isOpen

boolean

required

Indicates whether the side is open globally.

Example:

`true`

mint.reason

object | null

required

The reason the side is closed. `null` when the side is open.

Show child attributes

redeem

object

required

Whether ITN redeeming is open globally.

Hide child attributes

redeem.isOpen

boolean

required

Indicates whether the side is open globally.

Example:

`true`

redeem.reason

object | null

required

The reason the side is closed. `null` when the side is open.

Show child attributes

assets

object[]

required

The availability of each ITN asset on each network.

Hide child attributes

assets.symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

assets.networks

object[]

required

The asset's availability on each network.

Show child attributes

[List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets)[Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- booleanrequired
- object | nullrequired
- The reason the side is closed. null when the side is open.
- stringrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#webpage","url":"https://docs.ondo.finance/api-reference/itn/get-itn-status","name":"Get ITN Status","description":"This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","dateModified":"2026-11-12T23:40:59.756Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"ITN","item":"https://docs.ondo.finance/api-reference/itn/list-itn-assets"},{"@type":"ListItem","position":3,"name":"Get ITN Status","item":"https://docs.ondo.finance/api-reference/itn/get-itn-status"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#apireference","headline":"Get ITN Status","name":"Get ITN Status","description":"This endpoint reports whether ITN minting and redeeming are open, both globally and for each asset on each network. Global Status The top-level mint and redeem objects report whether each side is open globally. When a side is closed, every asset on every network is also unavailable for that side. Per-Network Availability Each entry in assets[].networks reports whether minting and redeeming are enabled for that asset on that network. ITN Status Reason Codes When a side is closed or unavailable, reason is set. Otherwise, reason is null. reason.code is one of: - ITN_UNAVAILABLE: ITN is temporarily unavailable, either platform-wide or for the asset. - MARKET_PAUSED: ITN minting or redeeming is paused for all assets. - PAUSED_GM_CHAIN: ITN minting or redeeming is paused on the network. Only returned per network. - ASSET_PAUSED: The asset is paused for ITN. Only returned per network. For limits on how much you can mint or redeem, see Get ITN Limits for an Asset. For caching details on this endpoint, please see: Endpoint Caching. For the complete ITN workflow, see ITN Integration.","url":"https://docs.ondo.finance/api-reference/itn/get-itn-status","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/itn/get-itn-status#webpage"},"dateModified":"2026-11-12T23:40:59.756Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```