---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses
title: List Cached Prospectuses - Base Documentation
description: List cached approved prospectus documents by ticker, with ISINs when known.
fetched: 2026-11-16
method: render
plan: read
---

List cached prospectuses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectuses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

```
{
  "prospectuses": [
    {
      "ticker": "SKYDC",
      "isin": "US69932A2042",
      "documents": [
        {
          "type": "primary",
          "approval_date": "2026-10-12",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---prospectus-pskyc---12oct2026_10_12_2026_16-24-26.pdf"
        },
        {
          "type": "supplementary",
          "approval_date": "2026-10-19",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---supplementary-prospectus-pskyc---19oct2026_10_19_2026_13-29-29.pdf"
        }
      ]
    }
  ]
}
```

Tokenized Stocks API

# List Cached Prospectuses

Copy pageCopy page

List cached approved prospectus documents by ticker, with ISINs when known.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

prospectuses

List cached prospectuses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectuses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

```
{
  "prospectuses": [
    {
      "ticker": "SKYDC",
      "isin": "US69932A2042",
      "documents": [
        {
          "type": "primary",
          "approval_date": "2026-10-12",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---prospectus-pskyc---12oct2026_10_12_2026_16-24-26.pdf"
        },
        {
          "type": "supplementary",
          "approval_date": "2026-10-19",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---supplementary-prospectus-pskyc---19oct2026_10_19_2026_13-29-29.pdf"
        }
      ]
    }
  ]
}
```

## Example

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/prospectuses
```

The response contains a `prospectuses` array, sorted alphabetically by uppercase ticker. Each entry includes `ticker`, the underlying equity’s `isin` when known, and a `documents` array. A ticker can have several documents, such as a primary prospectus and a later supplement.
Each document has these fields:

| Field | Description |
| --- | --- |
| `type` | `primary` or `supplementary` |
| `approval_date` | Approval date in `YYYY-MM-DD` format |
| `url` | Direct URL to the approved PDF |

Documents are ordered primary first, then newest approval date, then URL.
To get a single PDF for a ticker, use [Get Token Prospectus](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus), which redirects to the first document in this order.
The prospectus cache refreshes in the background. Before a successful refresh, the cache can be empty and the `prospectuses` field can be omitted. This is a prospectus-availability list, not a list of tokens available for trading.

#### Response

200 - application/json

Cached prospectuses.

The currently cached prospectuses, one entry per uppercase ticker, sorted alphabetically by ticker. The prospectuses field can be omitted when the cache is empty.

prospectuses

object[]

Show child attributes

Was this page helpful?

YesNo

[Get Token Prospectus

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus)[Get Corporate Action

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- object[]
- Hide child attributes
- prospectuses.ticker
- string
- The uppercase token ticker, including its token suffix, such as TSLAC.
- prospectuses.isin
- string
- The underlying equity ISIN. Omitted when not yet known from cached metadata.
- prospectuses.documents
- object[]
- Every cached primary and supplementary document for this ticker, ordered primary first, then newest approval date, then URL.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "prospectuses": [ { ...

### GET 누른 뒤

- prospectuses
- Copied

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses","name":"List Cached Prospectuses","description":"List cached approved prospectus documents by ticker, with ISINs when known.","dateModified":"2026-11-13T14:02:19.652Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"List Cached Prospectuses","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#apireference","headline":"List Cached Prospectuses","name":"List Cached Prospectuses","description":"List cached approved prospectus documents by ticker, with ISINs when known.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#webpage"},"dateModified":"2026-11-13T14:02:19.652Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```