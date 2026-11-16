---
url: https://docs.ondo.finance/api-reference/ohlc-streaming
title: OHLC Streaming - Ondo Finance
description: gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.
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
  ondo.gm.backend.v1.BackendService/StreamOHLC
```

Streamed

```
{
  "updates": [
    {
      "primaryMarket": {
        "symbol": "AAPLon",
        "open": "256.791808070580506978",
        "high": "257.013422018348623853",
        "low": "256.500000000000000000",
        "close": "256.901234567890123456"
      },
      "underlyingMarket": {
        "ticker": "AAPL",
        "open": "256.2475",
        "high": "256.47",
        "low": "255.96",
        "close": "256.36"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    },
    {
      "primaryMarket": {
        "symbol": "GOOGLon",
        "open": "305.39957516982939159",
        "high": "305.812345678901234567",
        "low": "304.900000000000000000",
        "close": "305.612345678901234567"
      },
      "underlyingMarket": {
        "ticker": "GOOGL",
        "open": "304.915",
        "high": "305.33",
        "low": "304.51",
        "close": "305.12"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    }
  ]
}
```

Streaming API

# OHLC Streaming

Copy pageCopy page

gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamOHLC
```

Streamed

```
{
  "updates": [
    {
      "primaryMarket": {
        "symbol": "AAPLon",
        "open": "256.791808070580506978",
        "high": "257.013422018348623853",
        "low": "256.500000000000000000",
        "close": "256.901234567890123456"
      },
      "underlyingMarket": {
        "ticker": "AAPL",
        "open": "256.2475",
        "high": "256.47",
        "low": "255.96",
        "close": "256.36"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    },
    {
      "primaryMarket": {
        "symbol": "GOOGLon",
        "open": "305.39957516982939159",
        "high": "305.812345678901234567",
        "low": "304.900000000000000000",
        "close": "305.612345678901234567"
      },
      "underlyingMarket": {
        "ticker": "GOOGL",
        "open": "304.915",
        "high": "305.33",
        "low": "304.51",
        "close": "305.12"
      },
      "isClosed": false,
      "timestamp": "1773350220000000000"
    }
  ]
}
```

The stream emits only live, in-progress candles; it does not backfill history. Candles are bucketed by minute and updated on every tick within the bucket. To load historical OHLC candles, use the REST [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset) endpoint. Both endpoints are intended to be used together to provide a complete picture. The REST endpoint provides historical candles to build the chart while the streaming endpoint keeps the chart up to date in real time.

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamOHLC`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more `OHLCUpdate` objects into a single `updates` array. Each update is a partial or closed minute candle for a single symbol, covering both the GM token (primary market) and the underlying stock (underlying market).

updates

OHLCUpdate[]

Array of OHLC updates.

Hide OHLCUpdate

primary\_market

object

OHLC candle for the GM token, keyed by `symbol`.

Hide primary\_market

symbol

string

Asset symbol.

open

string

Opening price for the bucket.

high

string

Highest price for the bucket.

low

string

Lowest price for the bucket.

close

string

Most recent price for the bucket.

underlying\_market

object

OHLC candle for the underlying stock, keyed by `ticker`.

Hide underlying\_market

ticker

string

Stock ticker.

open

string

Opening price for the bucket.

high

string

Highest price for the bucket.

low

string

Lowest price for the bucket.

close

string

Most recent price for the bucket.

is\_closed

boolean

Marks the final emission for the bucket (the minute boundary crossed). Subsequent updates with a higher timestamp belong to the next bucket.

timestamp

uint64

Bucket start (minute floor) in nanoseconds since epoch. Stable across all partials and the final closed update for a given bucket.

## Errors

Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[Price Streaming](https://docs.ondo.finance/api-reference/price-streaming)[Soft Quote Depth Streaming](https://docs.ondo.finance/api-reference/soft-quote-depth-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- primary_market
- OHLC candle for the GM token, keyed by symbol.
- Show primary_market
- underlying_market
- OHLC candle for the underlying stock, keyed by ticker.
- Show underlying_market
- is_closed
- Hide primary_market
- Hide underlying_market

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#webpage","url":"https://docs.ondo.finance/api-reference/ohlc-streaming","name":"OHLC Streaming","description":"gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.","dateModified":"2026-07-16T20:06:17.231Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"OHLC Streaming","item":"https://docs.ondo.finance/api-reference/ohlc-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#article","headline":"OHLC Streaming","name":"OHLC Streaming","description":"gRPC endpoint for real-time, minute-bucketed asset OHLC streaming.","url":"https://docs.ondo.finance/api-reference/ohlc-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/ohlc-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.231Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```