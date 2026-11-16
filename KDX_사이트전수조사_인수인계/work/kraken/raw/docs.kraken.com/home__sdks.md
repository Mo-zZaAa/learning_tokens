---
url: https://docs.kraken.com/home/sdks
title: SDKs - Kraken Developers
description: Official Kraken SDKs for Spot and Derivatives, plus community libraries
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Which one to use](#which-one-to-use)
* [Other tools](#other-tools)
* [Community libraries](#community-libraries)

SDKs

# SDKs

Copy pageCopy page

Official Kraken SDKs for Spot and Derivatives, plus community libraries

Copy pageCopy page

## Go

api-go. Spot and Derivatives, REST and WebSocket. The most complete coverage.

## Rust

kraken-sdk. Spot REST and WebSocket v2, plus Derivatives streams and order entry over the Unified WebSocket. Async-native.

## Which one to use

|  | Go | Rust |
| --- | --- | --- |
| Spot | Yes | Yes |
| Derivatives | Yes | Yes |
| Status | Stable | Stable |

## Other tools

## kraken-cli

One install, three binaries: `kraken`, `kraken-mcp` and `kraken-shell`. 188 commands for Spot and Derivatives trading, paper trading, scripting, and AI agent support.

## MCP server

`kraken-mcp` serves 152 of the CLI’s commands as MCP tools for LLM agents.

## Community libraries

These libraries are not officially maintained by Kraken. Review before using in production.

| Library | Language | Scope | Repository |
| --- | --- | --- | --- |
| kraken-wsclient-py | Python | WebSocket only (Spot) | [github.com/krakenfx/kraken-wsclient-py](https://github.com/krakenfx/kraken-wsclient-py) |
| kraken-api-client | PHP | REST (example only) | [github.com/krakenfx/kraken-api-client](https://github.com/krakenfx/kraken-api-client) |

Was this page helpful?

YesNo

[MCP Server](/home/mcp)[Go](/home/sdks/go)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/sdks#webpage","url":"https://docs.kraken.com/home/sdks","name":"SDKs","description":"Official Kraken SDKs for Spot and Derivatives, plus community libraries","dateModified":"2026-11-12T15:11:30.326Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/sdks#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/sdks#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"SDKs","item":"https://docs.kraken.com/home/sdks"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/sdks#article","headline":"SDKs","name":"SDKs","description":"Official Kraken SDKs for Spot and Derivatives, plus community libraries","url":"https://docs.kraken.com/home/sdks","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/sdks#webpage"},"dateModified":"2026-11-12T15:11:30.326Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```