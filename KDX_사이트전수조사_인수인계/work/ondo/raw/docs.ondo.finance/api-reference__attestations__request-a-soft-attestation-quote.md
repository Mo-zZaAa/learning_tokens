---
url: https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote
title: Request a Soft Attestation Quote - Ondo Finance
description: A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes
fetched: 2026-11-16
method: render
plan: read
---

Request a Soft Attestation Quote

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations/soft \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations/soft"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({symbol: 'AAPLon', tokenAmount: '5.000000000000000000'})
};

fetch('https://api.gm.ondo.finance/v1/attestations/soft', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations/soft",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations/soft"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations/soft")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations/soft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x96F6eF951840721AdBF46Ac996b59E0235CB985C",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535"
}
```

Attestations

# Request a Soft Attestation Quote

Copy pageCopy page

A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the [Request a Mint or Redeem Attestation endpoint](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation), soft quotes:

* Are not eligible for on-chain submission
* Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations)
* Serve as pricing references for quote validation and user interface display
* Do not include authentication fields such as `attestationId`, `userId`, `expiration`, or `signature`

This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments.

See also: [Error Codes](https://docs.ondo.finance/api-reference/error-codes)

Copy pageCopy page

POST

/

v1

/

attestations

/

soft

Try it

Request a Soft Attestation Quote

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations/soft \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations/soft"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {'x-api-key': '<api-key>', 'Content-Type': 'application/json'},
  body: JSON.stringify({symbol: 'AAPLon', tokenAmount: '5.000000000000000000'})
};

fetch('https://api.gm.ondo.finance/v1/attestations/soft', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations/soft",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000'
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/attestations/soft"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-api-key", "<api-key>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations/soft")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations/soft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x96F6eF951840721AdBF46Ac996b59E0235CB985C",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535"
}
```

#### Authorizations

x-api-key

string

header

required

#### Body

application/json

* AttestationByTokenAmountRequest
* AttestationByNotionalValueRequest

Request a soft quote to mint or redeem assets equal to the notional value.

chainId

enum<string>

required

The chain's identifier including the chain name and chain id.

Available options:

`ethereum-1`,

`bsc-56`,

`solana-900`

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

notionalValue

string

required

Total value of assets, represented as a string-encoded decimal with up to 18 digits after the decimal point. Must be greater than 0 and less than 1e20.

Example:

`"500.000000000000000000"`

duration

enum<string>

Specifies the desired validity period for the attestation. Users can specify a duration of 'short'
for a tighter price spread or 'long' for an extended validity period.

Available options:

`short`,

`long`

#### Response

200

application/json

OK

chainId

string

required

The chain's identifier, only including the chain id.

Example:

`"1"`

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

ticker

string

required

The stock ticker associated with this attestation.

Example:

`"AAPL"`

assetAddress

string

required

The contract address of the symbol.

Example:

`"0x96F6eF951840721AdBF46Ac996b59E0235CB985C"`

side

enum<string>

required

The direction of the trade (0 for buy, 1 for sell).

Available options:

`0`,

`1`

tokenAmount

string

required

The number of tokens to mint/redeem represented as a string with 18 decimal places.

Example:

`"5000000000000000000"`

price

string

required

The price per asset in USDon, represented as a string with 18 decimal places.

Example:

`"225273151158540753535"`

[Request a Mint or Redeem Attestation](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation)[Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#webpage","url":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote","name":"Request a Soft Attestation Quote","description":"A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes","dateModified":"2026-11-12T23:40:59.406Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Attestations","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":3,"name":"Request a Soft Attestation Quote","item":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#apireference","headline":"Request a Soft Attestation Quote","name":"Request a Soft Attestation Quote","description":"A soft quote provides pricing information for mint or redeem operations without creating an actual attestation. Unlike the Request a Mint or Redeem Attestation endpoint, soft quotes: - Are not eligible for on-chain submission - Do not count against user limits (Active Notional Value, Session Notional Value, or Active Attestations) - Serve as pricing references for quote validation and user interface display - Do not include authentication fields such as attestationId, userId, expiration, or signature This endpoint can be used to acquire estimated pricing without impacting trading limits or creating binding commitments. See also: Error Codes","url":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote#webpage"},"dateModified":"2026-11-12T23:40:59.406Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```