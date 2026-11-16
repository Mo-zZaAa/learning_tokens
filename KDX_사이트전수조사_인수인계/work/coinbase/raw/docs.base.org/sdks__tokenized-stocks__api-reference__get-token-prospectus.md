---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus
title: Get Token Prospectus - Base Documentation
description: Redirect to a tokenized stock's approved prospectus PDF.
fetched: 2026-11-16
method: render
plan: read
---

Get token prospectus

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectus/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

400

404

```
invalid ticker
```

```
404 page not found
```

Tokenized Stocks API

# Get Token Prospectus

Copy pageCopy page

Redirect to a tokenized stock’s approved prospectus PDF.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

prospectus

/

{ticker}

Get token prospectus

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectus/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

400

404

```
invalid ticker
```

```
404 page not found
```

## Example

Use the token ticker, including its token suffix. Tickers are case-insensitive; the `.pdf` suffix is optional. Dotted share-class tickers such as `BRK.Bc` are supported.

cURL

```
curl -L https://api.coinbase.com/v1/tokenized-stocks/prospectus/TSLAc.pdf --output TSLAc.pdf
```

The endpoint returns HTTP `302` with the approved prospectus PDF URL in the `Location` header. When a ticker has several documents, it redirects to the first one in the order that [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) returns: primary first, then newest approval date, then URL. The `-L` flag follows the redirect to download the PDF. This endpoint does not return JSON.
A malformed ticker returns HTTP `400`. A ticker with no available prospectus returns HTTP `404`. These errors have plain-text bodies. Use [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) to discover available tickers.

#### Path Parameters

ticker

string

required

The token ticker symbol, optionally followed by .pdf.

#### Response

302

Redirect to the current asset URL. Follow the Location header; the response is not a JSON document.

Was this page helpful?

YesNo

[Get Token Icon

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon)[List Cached Prospectuses

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {ticker}
- Copied

### Report incorrect code 누른 뒤

- 404
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- 404 page not found
- curl -L https://api.coinbase.c...

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

### No 누른 뒤

- No
- How can we improve our product?
- Help me get started faster
- Make it easier to find what I'm looking for
- Make it easy to understand the product and features
- Update this documentation

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus","name":"Get Token Prospectus","description":"Redirect to a tokenized stock's approved prospectus PDF.","dateModified":"2026-10-29T15:40:34.969Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Prospectus","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#apireference","headline":"Get Token Prospectus","name":"Get Token Prospectus","description":"Redirect to a tokenized stock's approved prospectus PDF.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#webpage"},"dateModified":"2026-10-29T15:40:34.969Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```