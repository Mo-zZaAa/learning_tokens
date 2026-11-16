---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks
title: List Tokenized Stocks - Base Documentation
description: Return the Coinbase-issued tokenized-stock records currently exposed through the API.
fetched: 2026-11-16
method: render
plan: read
---

List tokenized stocks

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks?page_size=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

503

default

```
{
  "tokens": [
    {
      "contract_address": "<string>",
      "symbol": "<string>",
      "name": "<string>",
      "decimals": 123,
      "icon_url": "<string>",
      "total_supply": 123,
      "isin": "<string>",
      "adgm_isin": "<string>",
      "multiplier": 123,
      "paused_features": [
        123
      ],
      "nav_price": 123,
      "nav_price_updated_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "first_mint_date": "2023-11-07T05:31:56Z"
    }
  ],
  "next_page_token": "<string>"
}
```

```
{
  "code": 3,
  "message": "page_size must not be negative"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
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

# List Tokenized Stocks

Copy pageCopy page

Return the Coinbase-issued tokenized-stock records currently exposed through the API.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

List tokenized stocks

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks?page_size=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

503

default

```
{
  "tokens": [
    {
      "contract_address": "<string>",
      "symbol": "<string>",
      "name": "<string>",
      "decimals": 123,
      "icon_url": "<string>",
      "total_supply": 123,
      "isin": "<string>",
      "adgm_isin": "<string>",
      "multiplier": 123,
      "paused_features": [
        123
      ],
      "nav_price": 123,
      "nav_price_updated_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "first_mint_date": "2023-11-07T05:31:56Z"
    }
  ],
  "next_page_token": "<string>"
}
```

```
{
  "code": 3,
  "message": "page_size must not be negative"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
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

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks
```

## Pagination

The default page size is `100` when `page_size` is omitted or `0`. Values above `500` are capped at `500`. Negative page sizes and malformed page sizes or cursors return HTTP `400`.
Pass the response’s `next_page_token` as `page_token` to retrieve the next page, keeping other parameters unchanged. Continue until `next_page_token` is omitted. Tokens are ordered by contract address.

## Response Fields

The token schema includes `description` and `first_mint_date`. The first-mint date is the UTC block timestamp of the token’s first positive mint, not its deployment time. It can be absent if never minted or not yet resolved.
Default-valued scalar fields, empty arrays, and unset timestamps can be omitted. For example, a zero supply may be absent from the list. Check the [response field guidance](https://docs.base.org/sdks/tokenized-stocks/overview) before interpreting missing supply or NAV data.

#### Query Parameters

page\_size

integer<int32>

default:100

The maximum number of records to return in one page. Defaults to 100 when omitted or zero. Values above 500 are capped at 500; negative values return HTTP 400.

Required range: `x >= 0`

page\_token

string

The `next_page_token` value from a previous response. Pass it to fetch the next page of records. Keep other request parameters unchanged between pages. A malformed cursor returns HTTP 400.

#### Response

200

application/json

A successful response.

Response message for `TokenizedEquitiesPublicApiService.ListTokenizedEquityTokens`.

tokens

object[]

The tokenized-stock records in this page.

Show child attributes

next\_page\_token

string

A token for fetching the next page. Pass it as `page_token` in the next request. Omitted on the last page.

Was this page helpful?

YesNo

[Tokenized Stocks API

Previous](https://docs.base.org/sdks/tokenized-stocks/overview)[List Protocol Contract Addresses

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- The tokenized-stock records in this page.
- Hide child attributes
- tokens.contract_address
- string
- The address of the ERC-20 token contract on Base.
- tokens.symbol
- string
- The token's ticker symbol.
- tokens.name
- string
- The name of the underlying equity.
- tokens.decimals
- integer<int64>
- The number of decimals used by the token.
- tokens.icon_url
- string
- URL of an icon representing the underlying equity.
- tokens.total_supply
- number<double>
- The token's total supply, normalized by the token's decimals. This is a token-unit amount, not the number of underlying shares; multiply by multiplier to convert to shares.
- tokens.isin
- string
- The ISIN of the underlying equity.
- tokens.adgm_isin
- string
- The ADGM ISIN of the tokenized security, taken from its approved primary prospectus. Distinct from the underlying stock's ISIN. Omitted when unavailable.
- tokens.multiplier
- number<double>
- The token's current scaling factor between token units and underlying shares, adjusted for its 18-decimal fixed-point scale (1.0 means no adjustment). It can change for corporate actions such as dividends or stock splits.
- tokens.paused_features
- integer<int64>[]
- Feature flags currently paused on the token contract.
- tokens.nav_price
- number<double>
- The most recently published Chainlink-based NAV/reference value for the token, read from its Chainlink price feed on Base and adjusted for the feed's decimals. This is a total-return reference value, not a live bid/ask or execution price. Check nav_price_updated_at and apply staleness bounds before relying on it.
- tokens.nav_price_updated_at
- string<date-time>
- The time at which nav_price was last updated onchain, per the Chainlink feed's latestRoundData() updatedAt. Chainlink only publishes a new round when the price moves past a deviation threshold or the heartbeat elapses, and feeds stop updating outside market hours, so this can lag wall-clock time by minutes to many hours. Apply staleness bounds before relying on nav_price.
- tokens.description
- string
- A human-readable description of the tokenized stock, based on its name and symbol.
- tokens.first_mint_date
- string<date-time>
- The UTC block timestamp of the first positive ERC-20 mint (Transfer from the zero address), not the contract deployment time. Omitted if never minted or not yet resolved. Later mints or burns do not change this date.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "tokens": [ { "c...

### GET 누른 뒤

- tokenized-stocks
- Copied

### Report incorrect code 누른 뒤

- default
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "tokens": [ { "c...
- curl https://api.coinbase.com/...

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks","name":"List Tokenized Stocks","description":"Return the Coinbase-issued tokenized-stock records currently exposed through the API.","dateModified":"2026-10-16T16:44:12.418Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"List Tokenized Stocks","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#apireference","headline":"List Tokenized Stocks","name":"List Tokenized Stocks","description":"Return the Coinbase-issued tokenized-stock records currently exposed through the API.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#webpage"},"dateModified":"2026-10-16T16:44:12.418Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```