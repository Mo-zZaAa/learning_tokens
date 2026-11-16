---
url: https://docs.ondo.finance/api-reference/protobuf-schema
title: Protobuf Schema & Code Generation - Ondo Finance
description: Download the GM streaming API's Protocol Buffers schema and generate a typed client.
fetched: 2026-11-16
method: static
plan: read
---

Streaming API

# Protobuf Schema & Code Generation

Copy pageCopy page

Download the GM streaming API’s Protocol Buffers schema and generate a typed client.

Copy pageCopy page

The streaming API is defined as a [Protocol Buffers](https://protobuf.dev/) schema. Download it below, or copy it into a `grpcapi.proto` file, to generate a typed client with [`buf`](https://buf.build/) or [`protoc`](https://protobuf.dev/installation) in the [language of your choice](https://grpc.io/docs/languages):

grpcapi.proto

```
syntax = "proto3";

package ondo.gm.backend.v1;

option go_package = "github.com/ondoprotocol/gm/pkg/proto/ondo/gm/backend/v1;backendv1";

// This file is the public, client-facing subset of the Ondo Stocks &
// Intelligent Portfolios
// backend gRPC API.
//
// The package and message definitions here are kept wire-compatible with the
// server. Generate clients from this file with `buf generate` or `protoc`.
//
// Request/response access to pricing, quotes, attestations, and token
// metadata is served over the REST API; see the OpenAPI specification at
// https://docs.ondo.finance/openapi.json.

// BackendService exposes the real-time streaming surface of the Ondo Stocks &
// Intelligent Portfolios API. All requests must include an API key in the `x-api-key`
// metadata header.
service BackendService {
  // HealthCheck returns the service status. Does not require authentication.
  rpc HealthCheck(HealthCheckRequest) returns (HealthCheckResponse);

  // StreamPriceUpdates streams real-time price updates for the requested
  // assets. Clients subscribe to one or more symbols and receive price
  // updates as they occur. Updates are batched into each response message.
  rpc StreamPriceUpdates(StreamPriceUpdatesRequest) returns (stream StreamPriceUpdatesResponse);

  // StreamOHLC streams real-time OHLC (open/high/low/close) updates, bucketed
  // by minute and updated per tick. Updates are batched into each response
  // message.
  rpc StreamOHLC(StreamOHLCRequest) returns (stream StreamOHLCResponse);

  // StreamSoftQuoteDepth streams synthetic market depth (bids and asks)
  // derived from the soft-quote price ladder for the requested assets, updated
  // as the underlying ladder changes. Updates are batched into each response
  // message.
  rpc StreamSoftQuoteDepth(StreamSoftQuoteDepthRequest) returns (stream StreamSoftQuoteDepthResponse);
}

// HealthCheckRequest is the request message for the HealthCheck RPC.
message HealthCheckRequest {}

// HealthCheckResponse is the response message for the HealthCheck RPC.
message HealthCheckResponse {
  string status = 1;
}

// StreamPriceUpdatesRequest subscribes to price updates for a set of assets.
message StreamPriceUpdatesRequest {
  // List of asset symbols to subscribe to. If empty, updates for all assets
  // are streamed.
  repeated string symbols = 1;
}

// PriceUpdate is a single price update streamed to clients.
message PriceUpdate {
  // Underlying stock ticker.
  string ticker = 1;
  // GM asset symbol.
  string symbol = 2;
  // Underlying stock price.
  string stock_price = 3;
  // Token price.
  string token_price = 4;
  // Unix timestamp of the price update, in nanoseconds.
  uint64 timestamp = 5;
}

// StreamPriceUpdatesResponse batches one or more price updates into a single
// stream message.
message StreamPriceUpdatesResponse {
  repeated PriceUpdate updates = 1;
}

// StreamOHLCRequest subscribes to OHLC updates for a set of assets.
message StreamOHLCRequest {
  // List of asset symbols to subscribe to. If empty, updates for all assets
  // are streamed.
  repeated string symbols = 1;
}

// OHLCUpdate is one partial or closed minute OHLC update for a single symbol.
message OHLCUpdate {
  message PrimaryMarket {
    string symbol = 1;
    string open = 2;
    string high = 3;
    string low = 4;
    string close = 5;
  }
  message UnderlyingMarket {
    string ticker = 1;
    string open = 2;
    string high = 3;
    string low = 4;
    string close = 5;
  }
  PrimaryMarket primary_market = 1;
  UnderlyingMarket underlying_market = 2;
  // is_closed marks the final emission for the bucket (the minute boundary
  // crossed). Subsequent updates with a higher timestamp belong to the next
  // bucket.
  bool is_closed = 3;
  // timestamp is the bucket start (minute floor) in nanoseconds since epoch.
  // Stable across all partials and the final closed update for a given bucket.
  uint64 timestamp = 4;
}

// StreamOHLCResponse batches one or more OHLC updates into a single stream
// message so subscribers to many assets receive one wire frame per drain
// window rather than one frame per candle.
message StreamOHLCResponse {
  repeated OHLCUpdate updates = 1;
}

// StreamSoftQuoteDepthRequest subscribes to soft-quote depth for a set of
// assets.
message StreamSoftQuoteDepthRequest {
  // List of asset symbols to subscribe to. If empty, depth for all assets is
  // streamed.
  repeated string symbols = 1;
}

// SoftQuoteDepth is the synthetic market depth for one asset, derived from the
// soft-quote price ladder. It is indicative and chain-agnostic (human-decimal
// prices and quantities). bids and asks are empty when error is set.
message SoftQuoteDepth {
  // GM asset symbol.
  string symbol = 1;
  // Underlying stock ticker.
  string ticker = 2;
  // Trading session the depth was computed for: premarket | regular |
  // postmarket | overnight | offhours.
  string session_type = 3;
  // Asset-level failure (e.g. paused, market closed, stale price). When set,
  // bids and asks are empty.
  string error = 4;
  // Unix timestamp of the underlying computation, in nanoseconds.
  uint64 timestamp = 5;
  // Sell side (redeem), best (highest) price first.
  repeated SoftQuoteDepthLevel bids = 6;
  // Buy side (mint), best (lowest) price first.
  repeated SoftQuoteDepthLevel asks = 7;
}

// SoftQuoteDepthLevel is one price level: the marginal price for the
// incremental token quantity available at that depth.
message SoftQuoteDepthLevel {
  // Marginal price for this level.
  string price = 1;
  // Token quantity available at this level.
  string quantity = 2;
}

// StreamSoftQuoteDepthResponse batches one or more depth updates into a single
// stream message.
message StreamSoftQuoteDepthResponse {
  repeated SoftQuoteDepth updates = 1;
}
```

See all 161 lines

For example, to generate a typed gRPC client for Go with `protoc`:

```
protoc \
  --go_out=. --go_opt=paths=source_relative \
  --go-grpc_out=. --go-grpc_opt=paths=source_relative \
  grpcapi.proto
```

For quick, ad-hoc testing you don’t need the schema. Every gRPC endpoint provides an example of how to use [`grpcurl`](https://github.com/fullstorydev/grpcurl) to make a request with reflection.

[Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)[Price Streaming](https://docs.ondo.finance/api-reference/price-streaming)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/protobuf-schema#webpage","url":"https://docs.ondo.finance/api-reference/protobuf-schema","name":"Protobuf Schema & Code Generation","description":"Download the GM streaming API's Protocol Buffers schema and generate a typed client.","dateModified":"2026-09-24T00:59:51.980Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/protobuf-schema#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Protobuf Schema & Code Generation","item":"https://docs.ondo.finance/api-reference/protobuf-schema"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#article","headline":"Protobuf Schema & Code Generation","name":"Protobuf Schema & Code Generation","description":"Download the GM streaming API's Protocol Buffers schema and generate a typed client.","url":"https://docs.ondo.finance/api-reference/protobuf-schema","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/protobuf-schema#webpage"},"dateModified":"2026-09-24T00:59:51.980Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```