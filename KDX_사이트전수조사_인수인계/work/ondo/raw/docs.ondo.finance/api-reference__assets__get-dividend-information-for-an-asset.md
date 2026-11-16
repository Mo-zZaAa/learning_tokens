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