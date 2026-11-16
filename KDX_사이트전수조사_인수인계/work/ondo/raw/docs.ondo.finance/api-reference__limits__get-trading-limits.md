---
url: https://docs.ondo.finance/api-reference/limits/get-trading-limits
title: Get Trading Limits - Ondo Finance
description: Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The "Max Notional Value" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \$1,000,000, and has 30 non-expired, non-filled attestations at a value of \$999,000, they will not be able to request another attestation for \$1000. - The "Remaining Attestations" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: static
plan: read
---

Get Trading Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/trading \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/trading"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/trading', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/trading",
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

	url := "https://api.gm.ondo.finance/v1/limits/trading"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/trading")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/trading")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "timestamp": 1746655938000,
  "symbol": "AAPLon",
  "side": "buy",
  "maxTokens": "100.000000000000000000",
  "maxNotionalValue": "1234.560000000000000000",
  "remainingAttestations": "3",
  "isAssetTradingOpen": false,
  "reason": {
    "message": "Weekend/Holiday",
    "documentation": "https://docs.ondo.finance/",
    "code": "MARKET_CLOSED"
  }
}
```

Limits

# Get Trading Limits

Copy pageCopy page

Provides real-time trading limits based on global, user, and asset-specific exposure limits.

Limits:

* The “Max Notional Value” limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of $1,000,000, and has 30 non-expired, non-filled attestations at a value of $999,000, they will not be able to request another attestation for $1000.
* The “Remaining Attestations” limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another.

If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status).

**Trading Limits Reason Codes**

When trading is not allowed, the response will include a `reason` field which may include one of the following common codes:

* `MARKET_CLOSED`: Market is closed.
* `MARKET_PAUSED`: Market is temporarily paused.
* `ASSET_PAUSED`: Specific asset is paused.
* `ASSET_CLOSED_FOR_SESSION`: The asset is not tradable in this session (e.g., not available overnight; see [Get Market Data](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))
* `ASSET_LIMITED`: Asset can be traded, but order size is more limited than usual.
* `MAX_LIMIT_REACHED`: Maximum limit has been reached.
* `MAX_ATTESTATIONS`: Maximum attestations reached.
* `OFFHOURS_EXPOSURE_LIMIT_REACHED`: The off-hours exposure limit has been reached for the asset during the current off-hours session.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

limits

/

trading

Try it

Get Trading Limits

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/limits/trading \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/limits/trading"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/limits/trading', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/limits/trading",
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

	url := "https://api.gm.ondo.finance/v1/limits/trading"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/limits/trading")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/limits/trading")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "timestamp": 1746655938000,
  "symbol": "AAPLon",
  "side": "buy",
  "maxTokens": "100.000000000000000000",
  "maxNotionalValue": "1234.560000000000000000",
  "remainingAttestations": "3",
  "isAssetTradingOpen": false,
  "reason": {
    "message": "Weekend/Holiday",
    "documentation": "https://docs.ondo.finance/",
    "code": "MARKET_CLOSED"
  }
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

required

The GM token symbol.

side

enum<string>

required

The trade side
The direction of the trade.

Available options:

`buy`,

`sell`

#### Response

200

application/json

OK

timestamp

number

required

The Unix timestamp in milliseconds when the trading limits were last updated.

Example:

`1746655938000`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

side

enum<string>

required

The direction of the trade.

Available options:

`buy`,

`sell`

maxTokens

string

required

The maximum token amount available to trade, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"100.000000000000000000"`

maxNotionalValue

string

required

The maximum notional value available to trade, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"1234.560000000000000000"`

remainingAttestations

string

required

The number of remaining attestations for this asset.

Example:

`"3"`

isAssetTradingOpen

boolean

required

Indicates whether the user is currently allowed to trade the asset

Example:

`false`

reason

object

Reason why trading is restricted for the given asset and user.

Show child attributes

[Get Token Info](https://docs.ondo.finance/api-reference/chains/get-token-info)[Get Session Limits](https://docs.ondo.finance/api-reference/limits/get-session-limits)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#webpage","url":"https://docs.ondo.finance/api-reference/limits/get-trading-limits","name":"Get Trading Limits","description":"Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The \"Max Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. - The \"Remaining Attestations\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.680Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Trading Limits","item":"https://docs.ondo.finance/api-reference/limits/get-trading-limits"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#apireference","headline":"Get Trading Limits","name":"Get Trading Limits","description":"Provides real-time trading limits based on global, user, and asset-specific exposure limits. Limits: - The \"Max Notional Value\" limit is based on the dollar value of outstanding attestations. That is, if a user has a limit of \\$1,000,000, and has 30 non-expired, non-filled attestations at a value of \\$999,000, they will not be able to request another attestation for \\$1000. - The \"Remaining Attestations\" limits the number of non-expired, non-executed attestations. For example if the limit is 50, and a user has 50 outstanding attestations, they must wait for one to execute or expire before requesting another. If the market is closed or paused, the response will indicate that trading is not allowed and provide the reason. For more information on market hours, see Get Current Market Status. Trading Limits Reason Codes When trading is not allowed, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. - ASSET_PAUSED: Specific asset is paused. - ASSET_CLOSED_FOR_SESSION: The asset is not tradable in this session (e.g., not available overnight; see Get Market Data) - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. - MAX_LIMIT_REACHED: Maximum limit has been reached. - MAX_ATTESTATIONS: Maximum attestations reached. - OFFHOURS_EXPOSURE_LIMIT_REACHED: The off-hours exposure limit has been reached for the asset during the current off-hours session. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/limits/get-trading-limits","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/limits/get-trading-limits#webpage"},"dateModified":"2026-11-12T23:40:59.680Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```