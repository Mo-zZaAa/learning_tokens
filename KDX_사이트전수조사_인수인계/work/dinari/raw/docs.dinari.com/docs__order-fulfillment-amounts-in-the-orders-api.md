---
url: https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api
title: Order Fulfillment Amounts in the Orders API
description: Overview When querying order details via the Orders API endpoints, the returned asset_token_quantity and payment_token_quantity fields represent the placed order quantities , not the actual fulfilled amounts. This is a common point of confusion for integrators. 💡Reference: Get Order Fulfillments Th…
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

# Order Fulfillment Amounts in the Orders API

## Overview

When querying order details via the Orders API endpoints, the returned asset\_token\_quantity and payment\_token\_quantity fields represent the **placed order quantities**, not the actual fulfilled amounts. This is a common point of confusion for integrators.

**💡Reference:** [**Get Order Fulfillments**](https://docs.dinari.com/reference/getaccountorderfulfillments)

---

## The Issue

The asset\_token\_quantity and payment\_token\_quantity fields in the **Orders API** responses reflect the amount the user initially requested at order placement. They do **not** reflect:

* Partial fills
* Final settled amounts
* Adjustments due to market price changes or slippage

Relying on these fields for reconciliation, settlement tracking, or balance updates will lead to inaccuracies.

---

## The Correct Approach

To obtain the **actual fulfillment amounts** for an order, we must query the **Order Fulfillments API** endpoints.

### ⚠️ Important Notes:

* Each order can have **multiple fulfillments** (e.g., partial fills over time).
* The sum of all fulfillments for a given order equals the total settled amount.
* Fulfillment records contain precise, finalized quantities for both the asset and the payment token.

---

## Best Practices

1. **Do not** use `asset_token_quantity` or `payment_token_quantity` from the Orders API for:

* Updating user balances
* Calculating fees
* Confirming order completion

2. **Always** fetch fulfillment records for an order to:

* Determine the net settled quantity
* Handle partial fills correctly
* Reconcile transactions with external systems

3. **Iterate** over all fulfillments associated with an order ID, as a single order may have one or more entries.

---

## Additional Context

| **API** | **Purpose** | **Fields to Use** |
| --- | --- | --- |
| **Orders API** | Order placement and high-level status | For order creation confirmation only |
| **Order Fulfillments API** | Settlement and execution details | For actual transferred amounts |

---

## Related Questions

* Q: Why would an order have multiple fulfillments?  
  A: Due to liquidity fragmentation, market depth, or execution over time, a single limit or market order may be filled across several distinct trades.
* Q: Should I sum all fulfillments to get the total?  
  A: Yes. The sum of all fulfillment amounts equals the final settled quantity for that order.

Updated about 1 month ago

---

[Order Types & Behaviors](https://docs.dinari.com/docs/order-type)[Stock Data](https://docs.dinari.com/docs/stock-data)

Did this page help you?

Yes

No

Copy Page

* + [Overview](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [The Issue](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [The Correct Approach](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + - [⚠️ Important Notes:](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Best Practices](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Additional Context](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Related Questions](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Order Fulfillment Amounts in the Orders API","dateModified":"2026-10-14T11:28:42.000Z"}
```