---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata
title: Get Token Metadata - Base Documentation
description: Return a tokenized stock's contractURI-compatible metadata document.
fetched: 2026-11-16
method: render
plan: read
---

Get token metadata

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/metadata/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

404

503

```
{
  "contract_address": "<string>",
  "name": "<string>",
  "symbol": "<string>",
  "image": "<string>",
  "prospectus_url": "<string>",
  "description": "<string>",
  "adgm_isin": "<string>"
}
```

```
{
  "code": 5,
  "message": "ticker \"UNKNOWNC\" is not a listed tokenized equity token"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

Tokenized Stocks API

# Get Token Metadata

Copy pageCopy page

Return a tokenized stock’s contractURI-compatible metadata document.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

metadata

/

{ticker}

Get token metadata

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/metadata/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

404

503

```
{
  "contract_address": "<string>",
  "name": "<string>",
  "symbol": "<string>",
  "image": "<string>",
  "prospectus_url": "<string>",
  "description": "<string>",
  "adgm_isin": "<string>"
}
```

```
{
  "code": 5,
  "message": "ticker \"UNKNOWNC\" is not a listed tokenized equity token"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

## Example

Use the token symbol, including its token suffix, such as `TSLAc`. Ticker lookup is case-insensitive.

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/metadata/TSLAc
```

The response contains `contract_address`, `name`, `symbol`, `description`, `image`, and `prospectus_url`. It also includes `adgm_isin`, the ADGM ISIN of the tokenized security, when available. The image and prospectus URLs are stable API links that redirect to the current assets. A `prospectus_url` does not guarantee that a PDF is currently cached; check [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) for available tickers.

#### Path Parameters

ticker

string

required

The token ticker symbol, including its token suffix. Lookup is case-insensitive.

#### Response

200

application/json

Token metadata.

A contractURI-compatible metadata document for a listed tokenized stock.

contract\_address

string

The ERC-20 token contract address on Base.

name

string

The name of the underlying equity.

symbol

string

The token ticker symbol.

image

string<uri>

Stable API URL that redirects to the current token icon.

prospectus\_url

string<uri>

Stable API URL that redirects to the approved prospectus when available. Use GET /v1/tokenized-stocks/prospectuses to discover cached prospectuses.

description

string

The same human-readable tokenized-stock description returned in the token list.

adgm\_isin

string

The ADGM ISIN of the tokenized security, taken from its approved primary prospectus. Distinct from the underlying stock's ISIN. Omitted when unavailable.

Was this page helpful?

YesNo

[Get Token Total Supply

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply)[Get Token Icon

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "contract_address": "<stri...

### GET 누른 뒤

- {ticker}
- Copied

### Report incorrect code 누른 뒤

- 503
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "contract_address": "<stri...
- curl https://api.coinbase.com/...

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata","name":"Get Token Metadata","description":"Return a tokenized stock's contractURI-compatible metadata document.","dateModified":"2026-11-09T12:27:23.982Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Metadata","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#apireference","headline":"Get Token Metadata","name":"Get Token Metadata","description":"Return a tokenized stock's contractURI-compatible metadata document.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#webpage"},"dateModified":"2026-11-09T12:27:23.982Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```