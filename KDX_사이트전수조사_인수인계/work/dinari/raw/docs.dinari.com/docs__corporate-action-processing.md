---
url: https://docs.dinari.com/docs/corporate-action-processing
title: Corporate Actions
description: This page documents what corporate actions Dinari supports, and how they are handled.
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

# Corporate Actions

This page documents what corporate actions Dinari supports, and how they are handled.

When an underlying security undergoes a change like a split, dividend, ticker update, or merger (known as a corporate action), those updates must be reflected on the dShare token and your ledger. This section outlines the corporate actions Dinari supports, how we process them, and how to handle them in your API integration.

## Supported Corporate Actions

We process corporate actions for all supported assets and automatically reflect these events on the Dinari platform. For specific details, refer to the dedicated page for each corporate action type. There you will find our handling procedures, partner integration diagrams, SDK examples, and a readiness checklist.

* [Dividends](https://docs.dinari.com/docs/dividend-payments) - Cash distributions paid to holders
* [Stock Splits](https://docs.dinari.com/docs/stock-split-handling) - Both forward and reverse splits
* [Ticker Changes](https://docs.dinari.com/docs/ticker-changes) - Symbol, Name, and CUSIP changes
* [Mergers](https://docs.dinari.com/docs/mergers) - Cash, Stock, and Mixed-consideration deals

## Monitoring for Corporate Actions

Dinari maintains numerous Market Data endpoints which provide users with news regarding corporate actions for all assets we issue. We advise all partners to regularly check these endpoints to be aware of any upcoming major events to prevent unnecessary downtime.

| What you want to know | Where to look |
| --- | --- |
| Upcoming and in-progress splits | `GET /api/v2/market_data/stocks/splits` |
| Splits for one stock | `GET /api/v2/market_data/stocks/{stock_id}/splits` |
| Announced dividends for a stock | `GET /api/v2/market_data/stocks/{stock_id}/dividends` |
| Dividends actually paid to an account | `GET /api/v2/accounts/{account_id}/dividend_payments` |
| Current positions, per chain | `GET /api/v2/accounts/{account_id}/portfolio` |

> ℹ️
>
> #### The Dinari Team will contact you directly regarding any edge cases for upcoming corporate actions. Examples include **reverse splits with fractional entitlements** or **mergers** that affect your held assets.

Updated about 1 month ago

---

[24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)[Dividends](https://docs.dinari.com/docs/dividend-payments)

Did this page help you?

Yes

No

Copy Page

* + [Supported Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Monitoring for Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Corporate Actions","dateModified":"2026-10-14T11:29:11.000Z"}
```