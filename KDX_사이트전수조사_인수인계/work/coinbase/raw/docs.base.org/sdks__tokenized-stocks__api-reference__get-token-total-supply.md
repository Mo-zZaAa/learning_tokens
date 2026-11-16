---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply
title: Get Token Total Supply - Base Documentation
description: Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.
fetched: 2026-11-16
method: render
plan: read
---

Get token total supply

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/total-supply/{contract_address}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

default

```
123
```

```
{
  "code": 3,
  "message": "field 'contract_address' must be a 20-byte hex address"
}
```

```
{
  "code": 5,
  "message": "contract_address \"0x0000000000000000000000000000000000000001\" is not a supported tokenized equity token"
}
```

```
{
  "code": 123,
  "message": "<string>",
  "details": [
    {
      "@type": "<string>"
    }
  ]
}
```

Tokenized Stocks API

# Get Token Total Supply

Copy pageCopy page

Return a tokenized stock’s ERC-20 total supply, normalized by the token’s decimals.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

total-supply

/

{contract\_address}

Get token total supply

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/total-supply/{contract_address}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

default

```
123
```

```
{
  "code": 3,
  "message": "field 'contract_address' must be a 20-byte hex address"
}
```

```
{
  "code": 5,
  "message": "contract_address \"0x0000000000000000000000000000000000000001\" is not a supported tokenized equity token"
}
```

```
{
  "code": 123,
  "message": "<string>",
  "details": [
    {
      "@type": "<string>"
    }
  ]
}
```

## Example

This example uses AMDc. For other tokens, use an address returned by [List Tokenized Stocks](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks).

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/total-supply/0xB2000000000000000000000d8Ce462E99ee7A47B
```

The response is a JSON number, not an object with a `total_supply` property. It is normalized by the token’s decimals, so do not divide it again.
A malformed contract address returns HTTP `400` with service code `3`. A correctly formatted address that is not a supported tokenized equity token returns HTTP `404` with service code `5`.

#### Path Parameters

contract\_address

string

required

The address of the ERC-20 token contract on Base. Find token addresses on the [Base assets page](https://www.base.org/assets) or from `GET /v1/tokenized-stocks`.

Pattern: `^0x[a-fA-F0-9]{40}$`

#### Response

200

application/json

The token's total supply, normalized by the token's decimals. This is a token-unit amount, not the number of underlying shares; multiply by `multiplier` to convert to shares.

The response is of type `number<double>`.

Was this page helpful?

YesNo

[List Protocol Contract Addresses

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses)[Get Token Metadata

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {contract_address}
- Copied

### Report incorrect code 누른 뒤

- default
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- 123
- curl https://api.coinbase.com/...

### Yes 누른 뒤

- No
- Great! What worked best for you?
- The guide worked as expected
- It was easy to find the information I needed
- It was easy to understand the product and features
- The documentation is up to date
- Something else
- Cancel
- Submit feedback

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply","name":"Get Token Total Supply","description":"Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.","dateModified":"2026-10-16T16:44:12.419Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Total Supply","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#apireference","headline":"Get Token Total Supply","name":"Get Token Total Supply","description":"Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#webpage"},"dateModified":"2026-10-16T16:44:12.419Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```