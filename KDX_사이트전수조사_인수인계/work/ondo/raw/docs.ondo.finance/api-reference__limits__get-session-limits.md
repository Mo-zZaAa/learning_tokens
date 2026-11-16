---
url: https://docs.ondo.finance/api-reference/limits/get-session-limits
title: Get Session Limits - Ondo Finance
description: Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The "Max Attestation Count" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The "Max Active Notional Value" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \$1,000,000, and has 30 non-expired, non-filled attestations at a value of \$999,000, they will not be able to request another attestation for \$1000. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Session Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/session \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/session"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/session', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/session",
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

	url := "https://api.gm.ondo.finance/v1/limits/session"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/session")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/session")

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
[
  {
    "limits": [
      {
        "symbol": "AAPLon",
        "premarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "10000"
        },
        "regular": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "postmarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "overnight": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "offhours": {
          "tradable": false,
          "maxAttestationCount": "0",
          "maxActiveNotionalValue": "0"
        }
      },
      "..."
    ],
    "timestamp": 1769192550134
  }
]
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

Limits

# Get Session Limits

Copy pageCopy page

Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo’s statically defined limits; for dynamic, real-time values, see [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits).

Limits are returned for each session: `premarket`, `regular`, `postmarket`, `overnight`, and `offhours`. The `offhours` block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (`tradable: false`).

Limits:

* The “Max Attestation Count” limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another.
* The “Max Active Notional Value” limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of $1,000,000, and has 30 non-expired, non-filled attestations at a value of $999,000, they will not be able to request another attestation for $1000.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

limits

/

session

Try it

Get Session Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/session \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/session"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/session', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/session",
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

	url := "https://api.gm.ondo.finance/v1/limits/session"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/session")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/session")

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
[
  {
    "limits": [
      {
        "symbol": "AAPLon",
        "premarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "10000"
        },
        "regular": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "postmarket": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "overnight": {
          "tradable": true,
          "maxAttestationCount": "500",
          "maxActiveNotionalValue": "200000"
        },
        "offhours": {
          "tradable": false,
          "maxAttestationCount": "0",
          "maxActiveNotionalValue": "0"
        }
      },
      "..."
    ],
    "timestamp": 1769192550134
  }
]
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

#### Query Parameters

symbol

string

The GM token symbol.

#### Response

200

application/json

OK

limits

object[]

required

Hide child attributes

limits.symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

limits.premarket

object

required

Show child attributes

limits.regular

object

required

Show child attributes

limits.postmarket

object

required

Show child attributes

limits.overnight

object

required

Show child attributes

limits.offhours

object

required

Trading limits that apply when the US equities market is closed for the day (e.g., weekends and holidays).

Show child attributes

timestamp

number

required

The Unix timestamp in milliseconds when the trading limits were last updated.

Example:

`1769116067536`

[Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits)[Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- stringrequired
- objectrequired

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#webpage","url":"https://docs.ondo.finance/api-reference/limits/get-session-limits","name":"Get Session Limits","description":"Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The \"Max Attestation Count\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The \"Max Active Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.694Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Limits","item":"https://docs.ondo.finance/api-reference/limits/get-trading-limits"},{"@type":"ListItem","position":3,"name":"Get Session Limits","item":"https://docs.ondo.finance/api-reference/limits/get-session-limits"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#apireference","headline":"Get Session Limits","name":"Get Session Limits","description":"Provides theoretical maximum asset-specific trading limits for each trading session. These limits are per-user, not global. This API reflects Ondo's statically defined limits; for dynamic, real-time values, see Get Trading Limits. Limits are returned for each session: premarket, regular, postmarket, overnight, and offhours. The offhours block describes the limits that apply when the US equities market is closed for the day (for example, on weekends and holidays). For most assets, off-hours trading is disabled (tradable: false). Limits: - The \"Max Attestation Count\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. - The \"Max Active Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/limits/get-session-limits","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/limits/get-session-limits#webpage"},"dateModified":"2026-11-12T23:40:59.694Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```