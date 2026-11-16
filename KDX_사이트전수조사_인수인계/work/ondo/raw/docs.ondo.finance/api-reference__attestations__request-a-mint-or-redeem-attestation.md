---
url: https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation
title: Request a Mint or Redeem Attestation - Ondo Finance
description: An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes
fetched: 2026-11-16
method: render
plan: read
---

Request a Mint or Redeem Attestation

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000",
  "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000",
    "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
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
  body: JSON.stringify({
    symbol: 'AAPLon',
    tokenAmount: '5.000000000000000000',
    userAddress: '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  })
};

fetch('https://api.gm.ondo.finance/v1/attestations', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000',
    'userAddress' => '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
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

	url := "https://api.gm.ondo.finance/v1/attestations"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "attestationId": "229852750420835981756873903928305653446",
  "userId": "0x474d0000000000009310097834e2c7af00000000000000000000000000000000",
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535",
  "expiration": 1746655938,
  "signature": "kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs=",
  "additionalData": ""
}
```

Attestations

# Request a Mint or Redeem Attestation

Copy pageCopy page

An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of `short` for a tighter price spread or `long` for an extended validity period.

Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits) endpoint.

See also: [Error Codes](https://docs.ondo.finance/api-reference/error-codes)

Copy pageCopy page

POST

/

v1

/

attestations

Try it

Request a Mint or Redeem Attestation

cURL

```
curl --request POST \
  --url https://api.gm.ondo.finance/v1/attestations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "symbol": "AAPLon",
  "tokenAmount": "5.000000000000000000",
  "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
}
'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/attestations"

payload = {
    "symbol": "AAPLon",
    "tokenAmount": "5.000000000000000000",
    "userAddress": "7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"
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
  body: JSON.stringify({
    symbol: 'AAPLon',
    tokenAmount: '5.000000000000000000',
    userAddress: '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
  })
};

fetch('https://api.gm.ondo.finance/v1/attestations', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/attestations",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'symbol' => 'AAPLon',
    'tokenAmount' => '5.000000000000000000',
    'userAddress' => '7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2'
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

	url := "https://api.gm.ondo.finance/v1/attestations"

	payload := strings.NewReader("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.gm.ondo.finance/v1/attestations")
  .header("x-api-key", "<api-key>")
  .header("Content-Type", "application/json")
  .body("{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/attestations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["x-api-key"] = '<api-key>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"symbol\": \"AAPLon\",\n  \"tokenAmount\": \"5.000000000000000000\",\n  \"userAddress\": \"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2\"\n}"

response = http.request(request)
puts response.read_body
```

200

Example

```
{
  "attestationId": "229852750420835981756873903928305653446",
  "userId": "0x474d0000000000009310097834e2c7af00000000000000000000000000000000",
  "chainId": "1",
  "symbol": "AAPLon",
  "ticker": "AAPL",
  "assetAddress": "0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c",
  "side": "0",
  "tokenAmount": "5000000000000000000",
  "price": "225273151158540753535",
  "expiration": 1746655938,
  "signature": "kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs=",
  "additionalData": ""
}
```

#### Authorizations

x-api-key

string

header

required

#### Body

application/json

Request a mint or redeem attestation.

* AttestationByTokenAmountRequest
* AttestationByNotionalValueRequest

Request to mint or redeem assets equal to the notional value.

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

userAddress

string

The Solana user address associated with the request. This is only required for Solana attestations.

Example:

`"7YkSgYQ6x7uBv9E3n2Yh6mF5tQ1rZc8Lp4WsXjKd3Ha2"`

#### Response

200

application/json

OK

attestationId

string

required

The attestation's unique identifier.

Example:

`"229852750420835981756873903928305653446"`

userId

string

required

The onchain identifier for an association of wallets.

Example:

`"0x474d0000000000009310097834e2c7af00000000000000000000000000000000"`

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

`"0x14c3abf95cb9c93a8b82c1cdcb76d72cb87b2d4c"`

side

enum<string>

required

The direction of the trade (0 for buy, 1 for sell).

Available options:

`0`,

`1`

Example:

`"0"`

tokenAmount

string

required

The number of tokens to mint/redeem represented as a string with 18 decimal places.

Example:

`"5000000000000000000"`

price

string

required

The price per asset in USDon, represented as a string with up to 18 decimal places.

Example:

`"225273151158540753535"`

expiration

number

required

The epoch timestamp when the attestation will expire.

Example:

`1746655938`

signature

string

required

The base64-encoded signature attesting to the quote.

Example:

`"kMecIrsGFdoAdxzRq2bPo07FWP2QyrxWfjrSMAdIZXNq3bXQnWx27aTKyt9fJiXWrzShYemxA/0RengNqNJ6bBs="`

additionalData

string

required

Base64-encoded additional data to provide within the attestation.

Example:

`""`

[Quickstart](https://docs.ondo.finance/api-reference/quickstart)[Request a Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#webpage","url":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation","name":"Request a Mint or Redeem Attestation","description":"An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes","dateModified":"2026-11-12T23:40:59.389Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Request a Mint or Redeem Attestation","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#apireference","headline":"Request a Mint or Redeem Attestation","name":"Request a Mint or Redeem Attestation","description":"An attestation is a signed payload that authorizes a user to mint or redeem tokens. Each attestation is only valid for a limited time and is determined by the duration in the request. A user can specify a duration of short for a tighter price spread or long for an extended validity period. Note: There are specific user and session limits which can prevent the creation of an attestation. For more information on limits, see the Get Trading Limits endpoint. See also: Error Codes","url":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation#webpage"},"dateModified":"2026-11-12T23:40:59.389Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```