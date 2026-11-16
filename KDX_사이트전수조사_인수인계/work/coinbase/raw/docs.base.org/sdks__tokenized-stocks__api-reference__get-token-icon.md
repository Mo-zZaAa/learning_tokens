---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon
title: Get Token Icon - Base Documentation
description: Redirect to a tokenized stock's icon using its ticker symbol.
fetched: 2026-11-16
method: render
plan: read
---

Get token icon

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/images/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

404

503

```
404 page not found
```

```
<string>
```

Tokenized Stocks API

# Get Token Icon

Copy pageCopy page

Redirect to a tokenized stock’s icon using its ticker symbol.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

images

/

{symbol}

Get token icon

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/images/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

404

503

```
404 page not found
```

```
<string>
```

## Example

Use the token symbol, including its token suffix. Symbols are case-insensitive; the `.png` suffix is optional.

cURL

```
curl -L https://api.coinbase.com/v1/tokenized-stocks/images/TSLAc.png --output TSLAc.png
```

The endpoint returns HTTP `302` with the image URL in the `Location` header. The `-L` flag follows the redirect to download the image. This endpoint does not return a JSON metadata document.
An unknown symbol returns HTTP `404`. Token data that is temporarily unavailable returns HTTP `503`. These errors have plain-text bodies.

#### Path Parameters

symbol

string

required

The token ticker symbol, optionally followed by .png.

#### Response

302

Redirect to the current asset URL. Follow the Location header; the response is not a JSON document.

Was this page helpful?

YesNo

[Get Token Metadata

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata)[Get Token Prospectus

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {symbol}
- Copied

### Report incorrect code 누른 뒤

- 503
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- <string>
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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon","name":"Get Token Icon","description":"Redirect to a tokenized stock's icon using its ticker symbol.","dateModified":"2026-10-16T16:44:12.420Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Icon","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#apireference","headline":"Get Token Icon","name":"Get Token Icon","description":"Redirect to a tokenized stock's icon using its ticker symbol.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#webpage"},"dateModified":"2026-10-16T16:44:12.420Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```