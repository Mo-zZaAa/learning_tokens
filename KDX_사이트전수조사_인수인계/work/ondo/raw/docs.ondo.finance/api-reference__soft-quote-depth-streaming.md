---
url: https://docs.ondo.finance/api-reference/soft-quote-depth-streaming
title: Soft Quote Depth Streaming - Ondo Finance
description: gRPC endpoint for real-time, synthetic soft-quote market depth streaming.
fetched: 2026-11-16
method: render
plan: read
---

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth
```

Streamed

```
{
  "updates": [
    {
      "symbol": "AAPLon",
      "ticker": "AAPL",
      "sessionType": "regular",
      "timestamp": "1773350214476688119",
      "bids": [
        { "price": "256.700000000000000000", "quantity": "100.000000000000000000" },
        { "price": "256.500000000000000000", "quantity": "250.000000000000000000" }
      ],
      "asks": [
        { "price": "256.900000000000000000", "quantity": "100.000000000000000000" },
        { "price": "257.100000000000000000", "quantity": "250.000000000000000000" }
      ]
    },
    {
      "symbol": "GOOGLon",
      "ticker": "GOOGL",
      "sessionType": "regular",
      "error": "market closed",
      "timestamp": "1773350214478735649",
      "bids": [],
      "asks": []
    }
  ]
}
```

Streaming API

# Soft Quote Depth Streaming

Copy pageCopy page

gRPC endpoint for real-time, synthetic soft-quote market depth streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth
```

Streamed

```
{
  "updates": [
    {
      "symbol": "AAPLon",
      "ticker": "AAPL",
      "sessionType": "regular",
      "timestamp": "1773350214476688119",
      "bids": [
        { "price": "256.700000000000000000", "quantity": "100.000000000000000000" },
        { "price": "256.500000000000000000", "quantity": "250.000000000000000000" }
      ],
      "asks": [
        { "price": "256.900000000000000000", "quantity": "100.000000000000000000" },
        { "price": "257.100000000000000000", "quantity": "250.000000000000000000" }
      ]
    },
    {
      "symbol": "GOOGLon",
      "ticker": "GOOGL",
      "sessionType": "regular",
      "error": "market closed",
      "timestamp": "1773350214478735649",
      "bids": [],
      "asks": []
    }
  ]
}
```

Soft quote depth is a synthetic, indicative market-depth view (bids and asks) derived from the soft-quote price ladder for each asset. It lets clients track quotable size at multiple price levels without polling the REST [Request a Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote) endpoint per price for hundreds of assets. Depth is recomputed and pushed as the underlying ladder changes.

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more `SoftQuoteDepth` entries (one per symbol that updated since the last send) into a single `updates` array.
Each entry holds the marginal depth ladder for a single asset: `asks` represent the buy (mint) side ordered best (lowest) price first, and `bids` represent the sell (redeem) side ordered best (highest) price first. Each level’s `quantity` is the incremental token size available at the level’s marginal `price`. Prices and quantities are decimal strings in human units. When `error` is set, `bids` and `asks` are empty.

updates

SoftQuoteDepth[]

Array of soft-quote depth updates.

Hide SoftQuoteDepth

symbol

string

GM asset symbol.

ticker

string

Underlying stock ticker.

session\_type

string

Trading session the depth was computed for. One of `premarket`, `regular`, `postmarket`, `overnight`, or `offhours`.

error

string

Asset-level failure (e.g. paused, market closed, stale price). When set, `bids` and `asks` are empty.

timestamp

uint64

Unix timestamp of the underlying computation (in nanoseconds).

bids

SoftQuoteDepthLevel[]

Sell side (redeem), best (highest) price first.

Hide SoftQuoteDepthLevel

price

string

Marginal price for this level.

quantity

string

Token quantity available at this level.

asks

SoftQuoteDepthLevel[]

Buy side (mint), best (lowest) price first.

Hide SoftQuoteDepthLevel

price

string

Marginal price for this level.

quantity

string

Token quantity available at this level.

## Streaming behavior

* **Snapshot on subscribe.** On connect, you receive the current depth for each subscribed symbol (when a fresh book is available), followed by live updates as the underlying ladder changes.
* **Batching.** Updates are flushed at most once every ~250 ms per stream. Within a window, only the latest book per symbol is kept, so a newer update supersedes an earlier one buffered in the same window.

## Errors

Asset-level problems (for example, a paused asset or a closed market) are reported inline: the affected `SoftQuoteDepth` entry carries a human-readable `error` with empty `bids` and `asks`, and the stream stays open (see the `GOOGLon` entry in the example).
Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[OHLC Streaming](https://docs.ondo.finance/api-reference/ohlc-streaming)[Upcoming API changes](https://docs.ondo.finance/api-reference/upcoming-changes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- session_type
- Trading session the depth was computed for. One of premarket, regular, postmarket, overnight, or offhours.
- Asset-level failure (e.g. paused, market closed, stale price). When set, bids and asks are empty.
- Show SoftQuoteDepthLevel

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#webpage","url":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming","name":"Soft Quote Depth Streaming","description":"gRPC endpoint for real-time, synthetic soft-quote market depth streaming.","dateModified":"2026-07-16T20:06:17.232Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"Soft Quote Depth Streaming","item":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#article","headline":"Soft Quote Depth Streaming","name":"Soft Quote Depth Streaming","description":"gRPC endpoint for real-time, synthetic soft-quote market depth streaming.","url":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.232Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```