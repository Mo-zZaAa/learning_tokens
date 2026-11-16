---
url: https://docs.ondo.finance/api-reference/overview
title: Overview - Ondo Finance
description: An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [API Surfaces](https://docs.ondo.finance/api-reference/overview)
* [What the API Supports](https://docs.ondo.finance/api-reference/overview)
* [How It Works](https://docs.ondo.finance/api-reference/overview)
* [Get Access](https://docs.ondo.finance/api-reference/overview)

Home

# Overview

Copy pageCopy page

An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.

Copy pageCopy page

The Ondo API provides programmatic access to two onchain product lines: Ondo Stocks—tokenized publicly-traded US stocks and ETFs—and Ondo Intelligent Portfolios—curated investment portfolios delivered as single onchain transferable tokens.
Ondo Stocks tokenizes publicly-traded US stocks and ETFs, allowing investors outside the United States to mint, transfer, and redeem equity-backed tokens across multiple public blockchains. Ondo Stocks are available on Ethereum, BNB Chain, and Solana. On-chain assets are issued as ERC-20 tokens for EVM-based chains and as SPL Token-2022 tokens on Solana. Each token represents direct exposure to the underlying asset, held with a regulated custodian through a licensed broker-dealer.
Ondo Intelligent Portfolios builds on the foundation of Ondo Stocks: professionally constructed portfolios delivered as single onchain tokens. Each portfolio token provides economic exposure to a weighted basket of Ondo Stocks tokens managed to a defined allocation. Investors mint or redeem a single token to hold the full basket, without buying, weighting, or rebalancing individual positions themselves. Rebalancing back to base weights executes programmatically, and holdings, weights, and every rebalance are visible onchain. Ondo Intelligent Portfolios are available on Ethereum and BNB Chain and issued as ERC-20 tokens for EVM-based chains.
To support integration across the ecosystem, we offer a suite of APIs designed for infrastructure providers such as wallets, exchanges, and fintech applications covering both product lines.

**Terminology:** Throughout the REST and streaming APIs and onchain identifiers, Ondo Stocks & Intelligent Portfolios use the legacy `GM` prefix—for example, the symbol parameter is described as the “GM token symbol” and the REST spec is titled the “GM Backend API”. The smart contract manager depends on the product line: Ondo Stocks use `IGMTokenManager`, while Ondo Intelligent Portfolios use `PortfolioTokenManager`.

## API Surfaces

The API is delivered through two surfaces, alongside the on-chain smart contract layer. The REST API spec can be found at [docs.ondo.finance/openapi.json](https://docs.ondo.finance/openapi.json), and the streaming API’s [Protocol Buffers schema](https://docs.ondo.finance/api-reference/protobuf-schema) is available for generating typed clients.

## REST API

High-performance request/response access to essential pricing, quote generation, token lifecycle, and token contract metadata. The full OpenAPI specification is available for use with code generators and other tooling.

## Streaming API

Low-latency, real-time updates over gRPC so clients can react to market movements as they happen rather than polling. The Protocol Buffers schema is available for generating typed clients.

## What the API Supports

* [Generating mint and redemption attestations](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation) to generate quotes that are fed to the [smart contract layer](https://docs.ondo.finance/api-reference/smart-contracts).
* [Real-time price data](https://docs.ondo.finance/api-reference/assets/get-current-prices-for-all-supported-assets) for Ondo Stocks & Intelligent Portfolios assets.
* [OHLC (Open, High, Low, Close) data](https://docs.ondo.finance/api-reference/assets/get-ohlc-open-high-low-close-data-for-an-asset) to support charting, analytics, and historical views.
* [Portfolio details](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios) for Ondo Intelligent Portfolios, such as constituents, weights, dividend yields, fees, and rebalance data.
* [ITN assets, status, and limits](https://docs.ondo.finance/api-reference/itn/list-itn-assets) for minting and redeeming Ondo Stocks through Alpaca’s Instant Tokenization Network.
* [On chain mints and redemptions](https://docs.ondo.finance/api-reference/smart-contracts) that handle the core logic for minting and redeeming Ondo Stocks & Intelligent Portfolios.

The [smart contract layer](https://docs.ondo.finance/api-reference/smart-contracts) provides the ability to mint and redeem (buy/sell) the tokenized asset.

## How It Works

Here’s the typical flow for Ondo Stocks & Intelligent Portfolios, using the Ondo Stocks token TSLAon as an example:
**Minting Process:**

1. Primary Purchaser requests a mint attestation from the Ondo Stocks & Intelligent Portfolios API.
2. Primary Purchaser broadcasts transaction with the provided mint attestation signature along with a USD stablecoin (such as USDC) to the smart contract to atomically mint TSLAon to their whitelisted address.

**Redeeming Process:**

1. Primary Purchaser requests a redemption attestation from the Ondo Stocks & Intelligent Portfolios API.
2. Primary Purchaser broadcasts transaction with the provided redemption attestation signature along with TSLAon to the smart contract to atomically redeem TSLAon for a USD stablecoin (such as USDC) to their whitelisted address.

## Get Access

If you’re interested in getting access to the Ondo Stocks & Intelligent Portfolios API, reach out to [onboarding@ondo.finance](mailto:onboarding@ondo.finance).

[Quickstart](https://docs.ondo.finance/api-reference/quickstart)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/overview#webpage","url":"https://docs.ondo.finance/api-reference/overview","name":"Overview","description":"An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.","dateModified":"2026-11-07T00:34:22.067Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/overview#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/overview#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Overview","item":"https://docs.ondo.finance/api-reference/overview"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/overview#article","headline":"Overview","name":"Overview","description":"An overview of the Ondo API and smart contract layer for Ondo Stocks and Ondo Intelligent Portfolios.","url":"https://docs.ondo.finance/api-reference/overview","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/overview#webpage"},"dateModified":"2026-11-07T00:34:22.067Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```