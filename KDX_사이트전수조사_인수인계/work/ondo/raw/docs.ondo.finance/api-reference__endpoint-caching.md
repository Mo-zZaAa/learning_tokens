---
url: https://docs.ondo.finance/api-reference/endpoint-caching
title: Endpoint Caching - Ondo Finance
description: Caching durations for GM Backend API endpoints.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Default Behavior](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Latest Prices](https://docs.ondo.finance/api-reference/endpoint-caching)
* [OHLC](https://docs.ondo.finance/api-reference/endpoint-caching)
* [All Metadata](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Shares Multiplier](https://docs.ondo.finance/api-reference/endpoint-caching)
* [Trading Limits](https://docs.ondo.finance/api-reference/endpoint-caching)
* [ITN Limits](https://docs.ondo.finance/api-reference/endpoint-caching)

References

# Endpoint Caching

Copy pageCopy page

Caching durations for GM Backend API endpoints.

Copy pageCopy page

This page outlines caching durations for various GM Backend API endpoints, establishing performance parameters while balancing freshness requirements.

## Default Behavior

Unless otherwise specified, all GET endpoints default to:

* **Cache Duration:** 1 minute

## Latest Prices

**Endpoints:** [Get Current Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) | [Get Current Price for an Asset](https://docs.ondo.finance/api-reference/assets/get-current-price-for-an-asset) | [Get Enhanced Prices for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-enhanced-prices-for-all-supported-assets)

* **Cache Duration:** 1 second

For real-time price streaming updates, see [Price Streaming Endpoint](https://docs.ondo.finance/api-reference/price-streaming).

## OHLC

**Endpoint:** [Get OHLC Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset)

* **Cache Duration:** 1 second
* **Data Delay:** Underlying OHLC data may itself be delayed by up to 5-10 seconds
* **Effective Lag:** Up to 11 seconds

For real-time OHLC updates, see [OHLC Streaming Endpoint](https://docs.ondo.finance/api-reference/ohlc-streaming).

## All Metadata

**Endpoint:** [Get Metadata for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-metadata-for-all-supported-assets)

* **Cache Duration:** 5 minutes
* **Note:** Metadata changes infrequently,

## Shares Multiplier

**Endpoint:** [Get Shares Multiplier History for an Asset](https://docs.ondo.finance/api-reference/assets/get-shares-multiplier-history-for-an-asset)

* **Cache Duration:** 1 second
* **Note:** Shares multipliers change infrequently, so a 1 second cache supports near-real-time discovery.

## Trading Limits

**Endpoint:** [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits)

* **Cache Duration:** None (response is always up to date)

## ITN Limits

**Endpoint:** [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset)

* **Cache Duration:** None (response is always up to date)

[Smart Contract Reference](https://docs.ondo.finance/api-reference/smart-contracts)[Error Codes](https://docs.ondo.finance/api-reference/error-codes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/endpoint-caching#webpage","url":"https://docs.ondo.finance/api-reference/endpoint-caching","name":"Endpoint Caching","description":"Caching durations for GM Backend API endpoints.","dateModified":"2026-11-07T00:34:22.072Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/endpoint-caching#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"Endpoint Caching","item":"https://docs.ondo.finance/api-reference/endpoint-caching"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#article","headline":"Endpoint Caching","name":"Endpoint Caching","description":"Caching durations for GM Backend API endpoints.","url":"https://docs.ondo.finance/api-reference/endpoint-caching","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/endpoint-caching#webpage"},"dateModified":"2026-11-07T00:34:22.072Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```