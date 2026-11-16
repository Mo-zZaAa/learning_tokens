---
url: https://docs.ondo.finance/api-reference/price-streaming
title: Price Streaming - Ondo Finance
description: gRPC endpoint for real-time asset price streaming.
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
  ondo.gm.backend.v1.BackendService/StreamPriceUpdates
```

Streamed

```
{
  "updates": [
    {
      "ticker": "GOOGL",
      "symbol": "GOOGLon",
      "stock_price": "304.915",
      "token_price": "305.39957516982939159",
      "timestamp": "1773350214478735649"
    },
    {
      "ticker": "AAPL",
      "symbol": "AAPLon",
      "stock_price": "256.2475",
      "token_price": "256.791808070580506978",
      "timestamp": "1773350214476688119"
    }
  ]
}
```

Streaming API

# Price Streaming

Copy pageCopy page

gRPC endpoint for real-time asset price streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamPriceUpdates
```

Streamed

```
{
  "updates": [
    {
      "ticker": "GOOGL",
      "symbol": "GOOGLon",
      "stock_price": "304.915",
      "token_price": "305.39957516982939159",
      "timestamp": "1773350214478735649"
    },
    {
      "ticker": "AAPL",
      "symbol": "AAPLon",
      "stock_price": "256.2475",
      "token_price": "256.791808070580506978",
      "timestamp": "1773350214476688119"
    }
  ]
}
```

Streaming is the real-time alternative to repeatedly polling the REST price endpoints. For a single price poll, use [Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) or [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset).

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamPriceUpdates`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more price updates into a single `updates` array.

updates

PriceUpdate[]

Array of price updates.

Hide PriceUpdate

ticker

string

Stock ticker.

symbol

string

Asset symbol.

stock\_price

string

Underlying stock price.

token\_price

string

Token price.

timestamp

uint64

Unix timestamp of the price update (in nanoseconds).

## Errors

Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema)[OHLC Streaming](https://docs.ondo.finance/api-reference/ohlc-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/price-streaming#webpage","url":"https://docs.ondo.finance/api-reference/price-streaming","name":"Price Streaming","description":"gRPC endpoint for real-time asset price streaming.","dateModified":"2026-07-16T20:06:17.217Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/price-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/price-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"Price Streaming","item":"https://docs.ondo.finance/api-reference/price-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/price-streaming#article","headline":"Price Streaming","name":"Price Streaming","description":"gRPC endpoint for real-time asset price streaming.","url":"https://docs.ondo.finance/api-reference/price-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/price-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.217Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```