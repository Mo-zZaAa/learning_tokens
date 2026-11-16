---
url: https://docs.ondo.finance/api-reference/status/get-asset-statuses
title: Get Asset Statuses - Ondo Finance
description: This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. "Limited" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Asset Statuses

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/assets",
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

	url := "https://api.gm.ondo.finance/v1/status/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/assets")

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
    "symbol": "XOMon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_LIMITED",
      "message": "earnings",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_limited"
    },
    "start": "2026-01-30T10:00:00Z",
    "end": "2026-01-31T00:30:00Z",
    "eventId": "30fd9cb4-1d64-474f-822d-7f281b8f02ee",
    "updateSharesMultiplier": false
  },
  {
    "symbol": "TIPon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_PAUSED",
      "message": "cash_dividend",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_paused"
    },
    "start": "2026-02-02T00:50:00Z",
    "end": "2026-02-03T01:00:00Z",
    "eventId": "d7d42fbe-9161-45af-806c-c0717453099d",
    "updateSharesMultiplier": true
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

Status

# Get Asset Statuses

Copy pageCopy page

This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures.

**Important**:

* When the entire market is closed or paused as indicated by `/v1/status/market`, all asset trading is automatically suspended regardless of individual asset status. (See [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status))
* Certain assets do not trade during the overnight and pre/postmarket session, as indicated by `/v1/assets/{symbol}/market`. (See [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) / [Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))

This endpoint should be used in conjunction with the [Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status) and [Market Data](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) endpoints to get a complete picture of trading availability.

**Market Sessions and Holidays**

Asset trading follows the same schedule as outlined in [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status). During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading.

**Earnings and Dividends**

Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule:

* **Dividends**: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date.
* **Earnings**: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. “Limited” here means that the quantity which can be minted in one request is reduced. For exact limits, see [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits). For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform’s discretion.
* **Cash acquisitions**: When the asset’s issuer is acquired for cash, trading is paused with the reason message `acquisition`. The pause starts 10 minutes before the last market session close on or before the acquisition’s effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report `updateSharesMultiplier` as `false`, because the `sharesMultiplier` does not change.
* **Other corporate actions**: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action.

**Asset Status Reason Codes**

`reason.code` is one of:

* `ASSET_PAUSED`: Asset is paused for trading.
* `ASSET_LIMITED`: Asset can be traded, but order size is more limited than usual.

**Asset Status Reason Messages**

`reason.message` is one of:

* `cash_dividend`
* `stock_dividend`
* `stock_split`
* `merger`
* `acquisition`
* `spinoff`
* `earnings`
* `maintenance`

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

status

/

assets

Try it

Get Asset Statuses

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/assets",
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

	url := "https://api.gm.ondo.finance/v1/status/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/assets")

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
    "symbol": "XOMon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_LIMITED",
      "message": "earnings",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_limited"
    },
    "start": "2026-01-30T10:00:00Z",
    "end": "2026-01-31T00:30:00Z",
    "eventId": "30fd9cb4-1d64-474f-822d-7f281b8f02ee",
    "updateSharesMultiplier": false
  },
  {
    "symbol": "TIPon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_PAUSED",
      "message": "cash_dividend",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_paused"
    },
    "start": "2026-02-02T00:50:00Z",
    "end": "2026-02-03T01:00:00Z",
    "eventId": "d7d42fbe-9161-45af-806c-c0717453099d",
    "updateSharesMultiplier": true
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

status

enum<string>

required

The current status of the pause. ('active' indicates the pause is live, 'upcoming' indicates it is scheduled for the future)

Available options:

`active`,

`upcoming`

Example:

`"active"`

type

enum<string>

required

The type of pause. ('scheduled' indicates a planned pause for events such as dividends, 'unscheduled' indicates an unplanned pause such as emergency maintenance)

Available options:

`scheduled`,

`unscheduled`

Example:

`"unscheduled"`

reason

object

Reason for an asset trading restriction.

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

The code indicating the reason for the asset status.

Available options:

`ASSET_PAUSED`,

`ASSET_LIMITED`

Example:

```
{  
  "code": "ASSET_PAUSED",  
  "message": "Maintenance",  
  "documentation": "https://docs.ondo.finance/"  
}
```

start

string

The start time of the pause. ('unscheduled' pauses may not provide a start time.)

Example:

`"2025-08-05T10:30:00Z"`

end

string

The end time of the pause. ('unscheduled' pauses may not provide an end time.)

Example:

`"2025-08-05T10:45:00Z"`

eventId

string

The unique id associated with the pause. (Might be empty if the sharesMultiplier will not be updated for the asset during the pause.)

Example:

`"94fe2f8f-e69c-45a5-9e48-dd8226dd8e67"`

updateSharesMultiplier

enum<boolean>

A boolean flag that indicates whether the sharesMultiplier value will be updated for the asset during this pause or not.

Available options:

`true`,

`false`

Example:

`true`

[Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status)[List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- Available options: ASSET_PAUSED, ASSET_LIMITED

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#webpage","url":"https://docs.ondo.finance/api-reference/status/get-asset-statuses","name":"Get Asset Statuses","description":"This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. \"Limited\" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.724Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Status","item":"https://docs.ondo.finance/api-reference/status/get-current-market-status"},{"@type":"ListItem","position":3,"name":"Get Asset Statuses","item":"https://docs.ondo.finance/api-reference/status/get-asset-statuses"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#apireference","headline":"Get Asset Statuses","name":"Get Asset Statuses","description":"This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. \"Limited\" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/status/get-asset-statuses","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#webpage"},"dateModified":"2026-11-12T23:40:59.724Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```