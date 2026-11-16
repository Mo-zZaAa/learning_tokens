---
url: https://docs.kraken.com/home/sdks/go
title: Go - Kraken Developers
description: api-go — the official Go module for the Spot and Derivatives APIs
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Install](#install)
* [What it covers](#what-it-covers)
* [Example](#example)

SDKs

# Go

Copy pageCopy page

api-go — the official Go module for the Spot and Derivatives APIs

Copy pageCopy page

[api-go](https://github.com/krakenfx/api-go) is the official Go module for building integrations against the Spot and Derivatives APIs.

## Install

```
go get github.com/krakenfx/api-go/v2/...
```

## What it covers

* Spot and Derivatives REST (public and authenticated endpoints)
* Spot and Derivatives WebSocket (public data streams and private channels)
* Order operations: add, amend, cancel
* Real-time order book construction with CRC32 checksum validation
* Instrument and asset lookups, account data retrieval

## Example

```
client := krakenapi.New(apiKey, apiSecret)
resp, err := client.AddOrder(krakenapi.AddOrderOptions{
    Pair:      "XBTUSD",
    Type:      "buy",
    OrderType: "limit",
    Price:     "60000",
    Volume:    "0.01",
})
```

Was this page helpful?

YesNo

[Overview](/home/sdks)[Rust](/home/sdks/rust)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/sdks/go#webpage","url":"https://docs.kraken.com/home/sdks/go","name":"Go","description":"api-go — the official Go module for the Spot and Derivatives APIs","dateModified":"2026-09-08T06:34:18.012Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/sdks/go#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/sdks/go#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"SDKs","item":"https://docs.kraken.com/home/sdks"},{"@type":"ListItem","position":3,"name":"Go","item":"https://docs.kraken.com/home/sdks/go"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/sdks/go#article","headline":"Go","name":"Go","description":"api-go — the official Go module for the Spot and Derivatives APIs","url":"https://docs.kraken.com/home/sdks/go","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/sdks/go#webpage"},"dateModified":"2026-09-08T06:34:18.012Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```