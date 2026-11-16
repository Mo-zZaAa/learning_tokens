---
url: https://docs.base.org/sdks/tokenized-stocks/overview
title: Tokenized Stocks API - Base Documentation
description: Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Endpoints](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Wallet Positions and Profit and Loss](https://docs.base.org/sdks/tokenized-stocks/overview)
* [List Tokenized Stocks](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Interpreting Response Fields](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Errors](https://docs.base.org/sdks/tokenized-stocks/overview)

Tokenized Stocks API

# Tokenized Stocks API

Copy pageCopy page

Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.

Copy pageCopy page

Use the public Tokenized Stocks API to retrieve reference data for [Coinbase-issued tokenized stocks on Base](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks). The API is read-only and does not require an API key.

Coinbase tokenized stocks are available only to persons in eligible jurisdictions outside of the United States. This API provides read-only reference data only; it does not provide trading, execution, issuance, minting, redemption, or custody functionality. The availability of any token or related product may be subject to jurisdictional, eligibility, and compliance requirements. Integrators are responsible for applying applicable restrictions.

Base URL

```
https://api.coinbase.com/v1/tokenized-stocks
```

[Browse the API reference](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks) for complete request and response schemas and an interactive request builder.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | [List tokenized-stock records](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks). |
| `GET` | `/chains` | [List protocol contract addresses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses). |
| `GET` | `/total-supply/{contract_address}` | [Get normalized token supply](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply). |
| `GET` | `/metadata/{ticker}` | [Get token metadata](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata). |
| `GET` | `/images/{symbol}` | [Redirect to a token icon](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon). |
| `GET` | `/prospectus/{ticker}` | [Redirect to a prospectus PDF](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus). |
| `GET` | `/prospectuses` | [List cached prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses). |
| `GET` | `/corporate-actions/{id}` | [Get a corporate action](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action). |

## Wallet Positions and Profit and Loss

The API provides reference data, not wallet-specific data. No endpoint accepts a wallet address, and the API does not return a wallet’s positions, cost basis, trade history, or profit and loss.
To show a holder’s current position in share-equivalent units, read the balance onchain with [`balanceOfUI`](https://docs.base.org/specifications/b20/reference/interfaces/ib20-asset/balance-of-ui), which applies the current `multiplier` (see [Multipliers](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks)). A balance does not give you cost basis or profit and loss. To calculate those, you need trade history from every route you want to include. Your app’s own records cover only the trades made through your app.

## List Tokenized Stocks

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks
```

The response includes token contract addresses, symbols, names, descriptions, decimals, ISINs, and multipliers. Depending on the token, it can also include an ADGM ISIN, an icon URL, total supply, first-mint date, paused features, and NAV/reference value data. Presence in the response does not imply trading availability or eligibility.
Results are paginated, so a single request may not return every record. When the response includes `next_page_token`, pass it as the `page_token` query parameter to fetch the next page, and repeat until `next_page_token` is omitted. Keep other request parameters unchanged between pages.
Use `page_size` to set the page size. The default is `100` when omitted or set to `0`. Values above `500` are capped at `500`; negative values return HTTP `400`. Tokens are ordered by contract address.

cURL

```
curl "https://api.coinbase.com/v1/tokenized-stocks?page_token=<next_page_token>"
```

## Interpreting Response Fields

JSON responses omit default-valued scalar fields, empty arrays, and unset timestamps. For example, a zero `total_supply` or empty `paused_features` array can be omitted. Do not assume every field is present, and do not treat missing NAV data as a usable price.

* **`total_supply`** is the token supply normalized by the token’s decimals. It is a token-unit amount, not the number of underlying shares.
* **`multiplier`** is the current scaling factor between token units and underlying shares. It can change for corporate actions such as dividends or stock splits, so always apply the current value when converting token units to shares.
* **`nav_price`** is the most recently published Chainlink-based NAV/reference value for the token. It is not a live bid/ask or execution price.
* **`nav_price_updated_at`** is when `nav_price` was last updated onchain. Feeds update only on price deviation or heartbeat and hold their last value outside market hours, so check this timestamp and apply staleness bounds before relying on `nav_price`.
* **`isin`** is the underlying stock’s ISIN.
* **`adgm_isin`** is the ADGM ISIN of the tokenized security, taken from its approved prospectus. It is distinct from the stock ISIN and can be absent when unavailable.
* **`description`** is a human-readable description of the tokenized stock.
* **`first_mint_date`** is the UTC block timestamp of the first positive ERC-20 mint, not the contract deployment time. It can be absent if the token has never been minted or its first mint has not yet been resolved. Later mints and burns do not change it.

## Errors

JSON endpoints return an error object with `code` and `message`. The code is a service error code, not the HTTP status. For example:

Invalid Page Token

```
{"code": 3, "message": "page_token is invalid"}
```

| HTTP Status | Code | Meaning |
| --- | --- | --- |
| `400` | `3` | Invalid input, such as a malformed page token, negative page size, invalid contract address, or malformed corporate action UUID. |
| `404` | `5` | The requested token, ticker, or corporate action is not supported or not found. |
| `503` | `14` | Required data is temporarily unavailable. |

The icon and prospectus redirect endpoints return HTTP `302` with a `Location` header on success, not JSON. Their lookup and validation errors use plain-text bodies. See each endpoint’s reference for its specific responses.
For integration guidance, price-feed details, and current token contract addresses, see [List Tokenized Stocks](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks).

Was this page helpful?

YesNo

[debug\_traceBlockByNumber

Previous](https://docs.base.org/base-chain/api-reference/debug-api/debug_traceBlockByNumber)[List Tokenized Stocks

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/overview#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/overview","name":"Tokenized Stocks API","description":"Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.","dateModified":"2026-11-13T14:02:19.652Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/overview#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Base Documentation","item":"https://docs.base.org"},{"@type":"ListItem","position":2,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#article","headline":"Tokenized Stocks API","name":"Tokenized Stocks API","description":"Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.","url":"https://docs.base.org/sdks/tokenized-stocks/overview","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#webpage"},"dateModified":"2026-11-13T14:02:19.652Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```