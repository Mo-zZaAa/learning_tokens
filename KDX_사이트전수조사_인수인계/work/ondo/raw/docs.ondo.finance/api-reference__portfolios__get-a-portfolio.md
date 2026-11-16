---
url: https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio
title: Get a Portfolio - Ondo Finance
description: This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, "0.0009" is 0.09% and "0.1143" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get a Portfolio

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios/{symbol} \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios/{symbol}",
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

	url := "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios/{symbol}")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios/{symbol}")

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

503

```
{
  "symbol": "MAG7Xon",
  "name": "Ondo Magnificent 7 and Crypto Portfolio",
  "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
  "category": "thematic",
  "modelProvider": "ondo",
  "inceptionDate": "2026-08-12T16:35:00Z",
  "netAssetsUsd": "1885406.537181",
  "dividendYield": "0.00198929",
  "afterWithholdingDividendYield": "0.0013925",
  "fees": {
    "serviceFeeRateBeforeWaiver": "0.0009",
    "waiverFraction": "1",
    "serviceFeeRateAfterWaiver": "0"
  },
  "rebalance": {
    "frequency": "Quarterly",
    "reconstitutionType": "Fixed",
    "lastRebalanceDate": "2026-08-12T16:36:00Z"
  },
  "constituentCount": 9,
  "constituents": [
    {
      "symbol": "AAPLon",
      "name": "Apple",
      "quantity": "917.20457",
      "targetWeight": "0.1143",
      "currentWeight": "0.12556912",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Technology"
      ],
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
        },
        {
          "networkChainId": "solana-900",
          "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
          "decimals": 9
        }
      ]
    },
    {
      "symbol": "AMZNon",
      "name": "Amazon",
      "quantity": "905.66388",
      "targetWeight": "0.1143",
      "currentWeight": "0.10877632",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Consumer Discretionary"
      ],
      "addresses": [
        {
          "networkChainId": "bsc-56",
          "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
          "decimals": 18
        },
        {
          "networkChainId": "ethereum-1",
          "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
          "decimals": 18
        },
        {
          "networkChainId": "solana-900",
          "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
          "decimals": 9
        }
      ]
    },
    "..."
  ],
  "timestamp": 1791469800123
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
  "code": "RESOURCE_NOT_FOUND",
  "message": "portfolio not found",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#resource_not_found"
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Portfolios

# Get a Portfolio

Copy pageCopy page

This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio.

The response has the same fields as each entry of [Get All Portfolios](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios). The response sorts the constituents by symbol.

If the symbol is not an active portfolio, the endpoint returns the `RESOURCE_NOT_FOUND` error code with status `404`. Ondo Stocks symbols, such as `AAPLon`, also return this error.

Rates, weights, and yields are decimal fractions. For example, `"0.0009"` is 0.09% and `"0.1143"` is 11.43%. Dates are RFC 3339 timestamps in UTC.

This endpoint does not return prices. To get the price of a portfolio token, use [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset), [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset), or [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) with the portfolio symbol.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

portfolios

/

{symbol}

Try it

Get a Portfolio

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/portfolios/{symbol} \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/portfolios/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/portfolios/{symbol}",
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

	url := "https://api.gm.ondo.finance/v1/portfolios/{symbol}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/portfolios/{symbol}")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/portfolios/{symbol}")

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

503

```
{
  "symbol": "MAG7Xon",
  "name": "Ondo Magnificent 7 and Crypto Portfolio",
  "description": "The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy by pairing the mega-cap technology stocks known as the \"Magnificent Seven\" with leading crypto assets. The portfolio holds an 80% equal-weight allocation to Apple, Microsoft, Alphabet, Amazon, NVIDIA, Meta, and Tesla, with the remaining 20% split between Bitcoin (15%) and Ethereum (5%).",
  "category": "thematic",
  "modelProvider": "ondo",
  "inceptionDate": "2026-08-12T16:35:00Z",
  "netAssetsUsd": "1885406.537181",
  "dividendYield": "0.00198929",
  "afterWithholdingDividendYield": "0.0013925",
  "fees": {
    "serviceFeeRateBeforeWaiver": "0.0009",
    "waiverFraction": "1",
    "serviceFeeRateAfterWaiver": "0"
  },
  "rebalance": {
    "frequency": "Quarterly",
    "reconstitutionType": "Fixed",
    "lastRebalanceDate": "2026-08-12T16:36:00Z"
  },
  "constituentCount": 9,
  "constituents": [
    {
      "symbol": "AAPLon",
      "name": "Apple",
      "quantity": "917.20457",
      "targetWeight": "0.1143",
      "currentWeight": "0.12556912",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Technology"
      ],
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
        },
        {
          "networkChainId": "solana-900",
          "address": "123mYEnRLM2LLYsJW3K6oyYh8uP1fngj732iG638ondo",
          "decimals": 9
        }
      ]
    },
    {
      "symbol": "AMZNon",
      "name": "Amazon",
      "quantity": "905.66388",
      "targetWeight": "0.1143",
      "currentWeight": "0.10877632",
      "assetClass": "Equities",
      "instrumentType": "Stock",
      "sectorIndustry": [
        "Consumer Discretionary"
      ],
      "addresses": [
        {
          "networkChainId": "bsc-56",
          "address": "0x4553cfe1c09f37f38b12dc509f676964e392f8fc",
          "decimals": 18
        },
        {
          "networkChainId": "ethereum-1",
          "address": "0xbb8774fb97436d23d74c1b882e8e9a69322cfd31",
          "decimals": 18
        },
        {
          "networkChainId": "solana-900",
          "address": "14Tqdo8V1FhzKsE3W2pFsZCzYPQxxupXRcqw9jv6ondo",
          "decimals": 9
        }
      ]
    },
    "..."
  ],
  "timestamp": 1791469800123
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
  "code": "RESOURCE_NOT_FOUND",
  "message": "portfolio not found",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#resource_not_found"
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

```
{
  "code": "INTERNAL_ERROR",
  "message": "portfolio data unavailable",
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

The portfolio token symbol

#### Response

200

application/json

OK

symbol

string

required

The portfolio token symbol.

Example:

`"MAG7Xon"`

name

string

required

The name of the portfolio.

Example:

`"Ondo Magnificent 7 and Crypto Portfolio"`

netAssetsUsd

string

required

The USD value of the constituents that the portfolio holds, represented as a string-encoded decimal with up to 6 digits after the decimal point. The value is the sum of each constituent `quantity` multiplied by its token price. It does not include cash from mints and redemptions that are not yet settled. For this reason, it can be slightly different from the token price multiplied by the total supply. If the portfolio has no supply, the value is `"0"`.

Example:

`"1885406.537181"`

dividendYield

string

required

The dividend yield of the portfolio, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.05" is the equivalent of 5%) The value is the average of the constituent dividend yields, weighted by `currentWeight`. The dividend yield of a constituent is the sum of its cash dividends paid in the last 365 days, divided by the current stock price. A constituent without dividends adds zero.

Example:

`"0.00198929"`

afterWithholdingDividendYield

string

required

The dividend yield of the portfolio after estimated withholding tax, represented as a string-encoded decimal with up to 8 digits after the decimal point. This value uses the same calculation as `dividendYield`, but it first subtracts the withholding tax from each dividend. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Example:

`"0.0013925"`

fees

object | null

required

The annual service fee of the portfolio. The value is `null` if no fee data is available. For more information, see [Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes).

Hide child attributes

fees.serviceFeeRateBeforeWaiver

string

required

The annual service fee rate before the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.0009" is the equivalent of 0.09%)

Example:

`"0.0009"`

fees.waiverFraction

string

required

The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of `"1"` waives the full fee. A value of `"0"` waives no fee.

Example:

`"1"`

fees.serviceFeeRateAfterWaiver

string

required

The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is `serviceFeeRateBeforeWaiver` multiplied by (1 - `waiverFraction`).

Example:

`"0"`

rebalance

object | null

required

The rebalance data of the portfolio. The value is `null` if no rebalance data is available. For more information, see [Rebalancing & Reconstitution](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution).

Hide child attributes

rebalance.frequency

string

required

The rebalance frequency of the portfolio, for example `Quarterly`. The value is free text, not a fixed list. Empty string if no frequency is available.

Example:

`"Quarterly"`

rebalance.reconstitutionType

string

required

The reconstitution approach of the portfolio, for example `Fixed`. The value is free text, not a fixed list. Empty string if no reconstitution type is available.

Example:

`"Fixed"`

rebalance.lastRebalanceDate

string<date-time>

The date of the most recent rebalance, as an RFC 3339 timestamp in UTC. The response omits this field if no rebalance date is available.

Example:

`"2026-08-12T16:36:00Z"`

constituentCount

integer<int32>

required

The number of constituents in `constituents`.

Example:

`9`

constituents

object[]

required

The constituents of the portfolio, sorted by symbol.

Hide child attributes

constituents.symbol

string

required

The GM token symbol of the constituent.

Example:

`"AAPLon"`

constituents.name

string

required

The name of the underlying asset. Empty string if no name is available.

Example:

`"Apple"`

constituents.quantity

string

required

The number of constituent tokens that the portfolio holds on all chains, represented as a string-encoded decimal with up to 18 digits after the decimal point.

Example:

`"917.20457"`

constituents.targetWeight

string

required

The target weight of the constituent in the portfolio model, represented as a string-encoded decimal with up to 8 digits after the decimal point. ("0.1143" is the equivalent of 11.43%)

Example:

`"0.1143"`

constituents.currentWeight

string

required

The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent `quantity` multiplied by its token price, divided by `netAssetsUsd`. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to `targetWeight`.

Example:

`"0.12556912"`

constituents.assetClass

string

required

High-level category of the asset. Empty string if not available.

Example:

`"Equities"`

constituents.instrumentType

string

required

Instrument type within the asset class. Empty string if not available.

Example:

`"Stock"`

constituents.sectorIndustry

string[]

required

Sector and industry classifications for the asset. Empty array if not available.

Example:

```
["Technology"]
```

constituents.addresses

object[]

required

The contract addresses of the constituent token, sorted by `networkChainId`.

Show child attributes

timestamp

number

required

The Unix timestamp in milliseconds when the API last refreshed the data of this portfolio. Each portfolio has its own timestamp.

Example:

`1791469800123`

description

string

A description of the portfolio strategy. The response omits this field if no description is available.

Example:

`"The Ondo Magnificent 7 and Crypto Portfolio implements an aggressive growth strategy ..."`

category

string

The category of the portfolio, for example `thematic`, `income`, or `allocation`. The value is free text, not a fixed list. The response omits this field if no category is available.

Example:

`"thematic"`

modelProvider

string

The [model provider](https://docs.ondo.finance/intelligent-portfolios/model-providers) that develops the portfolio strategy, for example `ondo` or `blackrock`. The value is free text, not a fixed list. The response omits this field if no model provider is available.

Example:

`"ondo"`

inceptionDate

string<date-time>

The inception date of the portfolio, as an RFC 3339 timestamp in UTC. The response omits this field if no inception date is available.

Example:

`"2026-08-12T16:35:00Z"`

[Get All Portfolios](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios)[Get Price and Volume Data for All Supported Tickers](https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- The fee waiver as a fraction of the service fee, from 0 to 1, represented as a string-encoded decimal with up to 8 digits after the decimal point. A value of "1" waives the full fee. A value of "0" waives no fee.
- The annual service fee rate after the fee waiver, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is serviceFeeRateBeforeWaiver multiplied by (1 - waiverFraction).
- The rebalance frequency of the portfolio, for example Quarterly. The value is free text, not a fixed list. Empty string if no frequency is available.
- The reconstitution approach of the portfolio, for example Fixed. The value is free text, not a fixed list. Empty string if no reconstitution type is available.
- The current weight of the constituent, represented as a string-encoded decimal with up to 8 digits after the decimal point. The value is the constituent quantity multiplied by its token price, divided by netAssetsUsd. The sum of the current weights of a portfolio is 1, before rounding. If the portfolio has no supply, the value is equal to targetWeight.
- string[]required
- The contract addresses of the constituent token, sorted by networkChainId.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#webpage","url":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio","name":"Get a Portfolio","description":"This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.616Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Portfolios","item":"https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios"},{"@type":"ListItem","position":3,"name":"Get a Portfolio","item":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#apireference","headline":"Get a Portfolio","name":"Get a Portfolio","description":"This endpoint returns one Ondo Intelligent Portfolio. The response contains the product metadata, net assets, dividend yields, service fee, rebalance data, and constituents of the portfolio. The response has the same fields as each entry of Get All Portfolios. The response sorts the constituents by symbol. If the symbol is not an active portfolio, the endpoint returns the RESOURCE_NOT_FOUND error code with status 404. Ondo Stocks symbols, such as AAPLon, also return this error. Rates, weights, and yields are decimal fractions. For example, \"0.0009\" is 0.09% and \"0.1143\" is 11.43%. Dates are RFC 3339 timestamps in UTC. This endpoint does not return prices. To get the price of a portfolio token, use Get Current Price for an Asset, Get OHLC Data for an Asset, or Get Market Data for an Asset with the portfolio symbol. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio#webpage"},"dateModified":"2026-11-12T23:40:59.616Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```