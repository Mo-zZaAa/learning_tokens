---
url: https://docs.ondo.finance/api-reference/status/get-current-market-status
title: Get Current Market Status - Ondo Finance
description: This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Current Market Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/market",
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

	url := "https://api.gm.ondo.finance/v1/status/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/market")

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
  "timestamp": "2025-08-20T21:03:02Z",
  "isOpen": true,
  "marketStatus": "postmarket",
  "nextOpenSession": "overnight",
  "offhours": {
    "isOpen": false,
    "nextOpen": "2026-06-19T00:05:00Z",
    "nextClose": "2026-06-21T23:55:00Z"
  },
  "nextOpen": "2025-08-21T00:05:00Z",
  "nextClose": "2025-08-20T23:59:00Z",
  "reason": null
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

Status

# Get Current Market Status

Copy pageCopy page

This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time.

**Typical Market Sessions**

The following table outlines the standard market sessions with brief transitional pauses between each session period.

| **Session** | **Start Time** | **End Time** |
| --- | --- | --- |
| Pause | 3:55 AM ET | 4:01 AM ET |
| **Premarket** | **4:01 AM ET** | **9:29 AM ET** |
| Pause | 9:29 AM ET | 9:31 AM ET |
| **Regular** | **9:31 AM ET** | **3:59 PM ET** |
| Pause | 3:59 PM ET | 4:01 PM ET |
| **Postmarket** | **4:01 PM ET** | **7:59 PM ET** |
| Pause | 7:59 PM ET | 8:05 PM ET |
| **Overnight** | **8:05 PM ET** | **3:55 AM ET** |

**Typical Holidays**

GM observes the same holiday schedule as the [New York Stock Exchange](https://www.nyse.com/markets/hours-calendars). This includes early closes and observed holidays.

**Unscheduled Downtime**

In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM’s functionality.

**Market Status Reason Codes**

When the market is not open, the response will include a `reason` field which may include one of the following common codes:

* `MARKET_CLOSED`: Market is closed.
* `MARKET_PAUSED`: Market is temporarily paused.

**Off-Hours Trading**

The `offhours` object reports the off-hours trading window as a parallel track alongside the conventional sessions. `marketStatus`, `isOpen`, `nextOpenSession`, `nextOpen`, and `nextClose` only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as `closed` on these fields. Off-hours tradability is reported separately via `offhours.isOpen`, `offhours.nextOpen`, and `offhours.nextClose`. The `offhours.nextOpen` and `offhours.nextClose` schedule fields are reported regardless of the off-hours global switch, while `offhours.isOpen` is true only when the off-hours window is tradable.

**Asset Tradability**
This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints:

* Individual assets may pause for dividends and other events, as indicated by `/v1/status/assets`. (See [Get Asset Statuses](https://docs.ondo.finance/api-reference/status/get-asset-statuses))
* Certain assets do not trade during the overnight and pre/postmarket session, as indicated by `/v1/assets/{symbol}/market`. (See [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) / [Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

status

/

market

Try it

Get Current Market Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/market",
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

	url := "https://api.gm.ondo.finance/v1/status/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/market")

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
  "timestamp": "2025-08-20T21:03:02Z",
  "isOpen": true,
  "marketStatus": "postmarket",
  "nextOpenSession": "overnight",
  "offhours": {
    "isOpen": false,
    "nextOpen": "2026-06-19T00:05:00Z",
    "nextClose": "2026-06-21T23:55:00Z"
  },
  "nextOpen": "2025-08-21T00:05:00Z",
  "nextClose": "2025-08-20T23:59:00Z",
  "reason": null
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

string

required

The UTC timestamp of the market status check in ISO 8601 format.

Example:

`"2025-08-20T21:03:02Z"`

isOpen

boolean

required

Indicates whether the market is currently open or closed to trading.

Example:

`true`

marketStatus

enum<string>

required

The current status of the market. `offhours` indicates an off-hours session (such as weekends, the window after the Friday postmarket close, or eligible holidays) during which trading is enabled for assets that opt in to off-hours trading. Off-hours is only reported when off-hours trading is enabled; otherwise the same windows report as `closed`.

Available options:

`regular`,

`premarket`,

`postmarket`,

`overnight`,

`offhours`,

`paused`,

`closed`

Example:

`"postmarket"`

nextOpenSession

enum<string>

required

The next market open session of the market. May be `offhours` when the next available trading window is an off-hours session.

Available options:

`regular`,

`premarket`,

`postmarket`,

`overnight`,

`offhours`

Example:

`"overnight"`

offhours

object

required

Status of the off-hours trading window, surfaced as a parallel track alongside the conventional session fields. The off-hours window is reported independently of the conventional sessions: `marketStatus` and `isOpen` reflect only the four conventional sessions (regular, premarket, postmarket, overnight), while this object reports off-hours tradability separately.

Hide child attributes

offhours.isOpen

boolean

required

Indicates whether off-hours trading is currently open. This is true only while the off-hours window is tradable and the off-hours global switch is on.

Example:

`false`

offhours.nextOpen

string

required

The next off-hours window open time in ISO 8601 format (UTC). Reported regardless of the off-hours global switch.

Example:

`"2026-06-19T00:05:00Z"`

offhours.nextClose

string

required

The next off-hours window close time in ISO 8601 format (UTC). Reported regardless of the off-hours global switch.

Example:

`"2026-06-21T23:55:00Z"`

nextOpen

string

The next market open time in ISO 8601 format (UTC).

Example:

`"2025-08-21T00:05:00Z"`

nextClose

string

The next market close time in ISO 8601 format (UTC).

Example:

`"2025-08-20T23:59:00Z"`

reason

object

Reason for market closure or pause.

Hide child attributes

reason.message

string

required

The human-readable message describing the reason

Example:

`"Weekend/Holiday"`

reason.documentation

string

required

Additional documentation or reference

Example:

`"https://docs.ondo.finance/"`

reason.code

enum<string>

required

The code indicating the reason for the market status.

Available options:

`MARKET_CLOSED`,

`MARKET_PAUSED`

Example:

`null`

[Get Session Limits](https://docs.ondo.finance/api-reference/limits/get-session-limits)[Get Asset Statuses](https://docs.ondo.finance/api-reference/status/get-asset-statuses)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- Available options: MARKET_CLOSED, MARKET_PAUSED

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#webpage","url":"https://docs.ondo.finance/api-reference/status/get-current-market-status","name":"Get Current Market Status","description":"This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.709Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Current Market Status","item":"https://docs.ondo.finance/api-reference/status/get-current-market-status"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#apireference","headline":"Get Current Market Status","name":"Get Current Market Status","description":"This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/status/get-current-market-status","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#webpage"},"dateModified":"2026-11-12T23:40:59.709Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```