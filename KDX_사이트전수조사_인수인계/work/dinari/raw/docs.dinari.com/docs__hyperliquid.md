---
url: https://docs.dinari.com/docs/hyperliquid
title: Hyperliquid
description: Learn how dShares and wrapped dShares work across HyperEVM and HyperCore in the Hyperliquid ecosystem.
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Hyperliquid

Learn how dShares and wrapped dShares work across HyperEVM and HyperCore in the Hyperliquid ecosystem.

Dinari dShares™ are available in the Hyperliquid ecosystem and are supported in both HyperEVM and HyperCore, with special considerations for tokens deployed in each environment.

## HyperEVM

HyperEVM is Hyperliquid’s EVM-compatible execution layer. HyperEVM is the primary environment where Dinari deploys the underlying tokenized asset representation for Hyperliquid-related flows. For each supported asset on HyperEVM, Dinari deploys a **dShare** and its corresponding **wrapped dShare**.

### HyperEVM limitations and considerations

Before integrating with dShares on HyperEVM, keep the following in mind:

* Both token types exist on HyperEVM, but they are used differently.
* Wrapped dShares are primarily used for HyperCore-linked flows.
* Availability is asset-specific; not every asset will necessarily be deployed at the same time.

## HyperCore

HyperCore is Hyperliquid's order book layer. Tokens on HyperCore are explicitly linked to their corresponding wrapped dShare on HyperEVM; they are not separate or independently wrapped tokens.

This means:

* HyperCore support is **not automatic** when an asset exists on HyperEVM.
* Wrapped dShares are the asset form used for HyperCore connectivity.

### Special considerations for HyperCore

* On HyperCore, users interact with a wrapped representation of a dShare rather than the base HyperEVM dShare itself.
* HyperCore support depends on an additional deployment and linking process beyond deploying a dShare on HyperEVM.

### HyperCore limitations and considerations

The main limitations on HyperCore are structural:

* Each asset requires explicit registration and linkage,
* HyperCore and only bridge to HyperEVM. To bridge to any other chain you need to bridge to HyperEVM and then to your target chain.

## Key takeaways

When interacting with dShares on Hyperliquid, the most important points are:

* **dShares** are the primary bridgeable asset form.
* **Wrapped dShares** are required for HyperCore-linked usage.

Updated about 1 month ago

---

[Wrapping dShares™](https://docs.dinari.com/docs/wrapping)[dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)

Did this page help you?

Yes

No

Copy Page

* + [HyperEVM](https://docs.dinari.com/docs/hyperliquid)
  + - [HyperEVM limitations and considerations](https://docs.dinari.com/docs/hyperliquid)
  + [HyperCore](https://docs.dinari.com/docs/hyperliquid)
  + - [Special considerations for HyperCore](https://docs.dinari.com/docs/hyperliquid)
    - [HyperCore limitations and considerations](https://docs.dinari.com/docs/hyperliquid)
  + [Key takeaways](https://docs.dinari.com/docs/hyperliquid)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Hyperliquid","dateModified":"2026-10-14T11:27:27.000Z"}
```