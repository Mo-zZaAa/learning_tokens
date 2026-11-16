---
url: https://docs.dinari.com/docs/mergers
title: Mergers
description: How Dinari handles cash, stock, and mixed-consideration mergers affecting dShares
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

# Mergers

How Dinari handles cash, stock, and mixed-consideration mergers affecting dShares

# Mergers

A merger combines multiple companies. For target holders, the key question is what asset they receive at closing. This payout (cash, stock, or a mix) maps directly to Dinari's event classifications.

---

## The three consideration types

The consideration, cash, acquirer stock, or a mix, is fixed by the deal terms, and it maps directly onto Dinari's classification:

| Consideration | What a holder receives |
| --- | --- |
| Cash only | A fixed cash amount per share. The target's shares are extinguished and delisted. |
| Stock only | Acquirer shares at a fixed exchange ratio, preserving market exposure. |
| Cash and stock | A combination of partial liquidity plus continued equity participation. |

---

## Which structure applies

```
flowchart TD
    A["Merger announced"] --> B{"Consideration?"}
 
    B -->|"Cash only"| C["cash_merger"]
    B -->|"Acquirer stock only"| D["stock_merger"]
    B -->|"Cash and stock"| E["stock_and_cash_merger"]
 
    C --> F{"Does Dinari<br/>hold this asset?"}
    D --> F
    E --> F
 
    F -->|"No"| G["No action.<br/>No partner impact."]
    F -->|"Yes"| H["Manual triage.<br/>Dinari contacts you directly."]
```

---

## What that means in practice

Rely on direct communication from Dinari, not the API, to confirm event outcomes, timing, and settlement assets.

***What you can rely on:***

* Dinari detects merger announcements and checks whether it holds the affected asset.
* When a held asset is affected, Dinari will coordinates the resolution and notify you.
* Position and cash changes are observable once resolved.

***What you should not assume:***

* That a merger produces an event object you can poll for.
* That a stock-for-stock merger automatically produces an acquirer dShare.
* That timing matches the deal's closing date to the hour.

---

## Recommendations for Managing Mergers Programmatically

1. **Watch for unexplained position removals.** There is no merger event endpoint, so a position disappearing from the portfolio is your programmatic signal — and your partner channel is the primary notification path.
2. **Snapshot positions before a known effective date.** A before/after diff is the only reliable reconciliation method available.
3. **Reconcile both positions and cash.** A cash merger settles as a cash entitlement; the portfolio alone shows a position vanishing with nothing in its place.

> ℹ️
>
> #### Note: There is no dedicated merger endpoint or SDK method. You detect a merger's effects by reconciling holdings and cash across the effective date.

Updated about 1 month ago

---

[Ticker Changes](https://docs.dinari.com/docs/ticker-changes)[Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)

Did this page help you?

Yes

No

Copy Page

* + [Mergers](https://docs.dinari.com/docs/mergers)
  + - [The three consideration types](https://docs.dinari.com/docs/mergers)
    - [Which structure applies](https://docs.dinari.com/docs/mergers)
    - [What that means in practice](https://docs.dinari.com/docs/mergers)
    - [Recommendations for Managing Mergers Programmatically](https://docs.dinari.com/docs/mergers)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Mergers","dateModified":"2026-10-14T11:29:11.000Z"}
```