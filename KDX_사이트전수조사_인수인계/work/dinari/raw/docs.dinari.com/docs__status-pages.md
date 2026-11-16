---
url: https://docs.dinari.com/docs/status-pages
title: Status Pages
description: Dinari Status Page Managed by Dinari. Provides updates on platform availability, API incidents, and maintenance notices. Dinari Status When to check Before Placing Large or Time-Sensitive Orders If you are about to submit a high-value order or a batch of orders during market hours, check the status…
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

# Status Pages

## Dinari Status Page

Managed by Dinari. Provides updates on platform availability, API incidents, and maintenance notices.

[Dinari Status](https://status.dinari.com/)

---

## When to check

* **Before Placing Large or Time-Sensitive Orders**  
  If you are about to submit a high-value order or a batch of orders during market hours, check the status page first to confirm that ordering, market data, and settlement services are fully operational.

* **During Regular U.S. Market Hours (9:30 AM – 4:00 PM ET)**  
  Market data feeds (current\_price, current\_quote, WebSocket) are most active during regular trading hours. If you observe stale prices, missing OHLC candles, or delayed quotes, check here first to see whether a known data feed issue is already being tracked.
* **During Overnight and Weekend Sessions**  
  Dinari supports 24/7 trading through Flow Traders. Liquidity is lower outside regular hours, and only limit orders are accepted. If you see wide spreads, zero bid/ask values, or delayed fills, this may be expected session behavior rather than an incident. The status page will confirm whether any infrastructure issues are affecting overnight or weekend sessions.
* **When API Requests Return Unexpected Errors**  
  If you receive 5xx errors (500, 502, 503) or the 423 "Account in use" error on multiple requests, check the status page to see if a broader API incident is in progress before troubleshooting your own integration.
* **Before Scheduled Maintenance Windows**  
  Planned maintenance will be announced in advance. Check this page before maintenance windows to confirm the scope, affected components, and expected duration.
* **After Deploying to Production**  
  If you have recently deployed an integration change and observe degraded performance, check the status page to rule out a platform-side issue before rolling back your change.

Updated 10 days ago

---

[FAQs](https://docs.dinari.com/docs/faqs)

Did this page help you?

Yes

No

Copy Page

* + [Dinari Status Page](https://docs.dinari.com/docs/status-pages)
  + [When to check](https://docs.dinari.com/docs/status-pages)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Status Pages","dateModified":"2026-11-06T16:53:06.000Z"}
```