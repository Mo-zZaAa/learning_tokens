---
url: https://docs.dinari.com/docs/stuck-orders
title: Orders Stuck in SUBMITTED Status
description: Overview / Context In Dinari's system, an order follows a two-stage lifecycle: the OrderRequest (the user's intent) and the Order (the actual on-chain transaction). When an OrderRequest reaches the SUBMITTED status, it means the order has been successfully submitted to the order book and is actively…
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

# Orders Stuck in SUBMITTED Status

## Overview / Context

In Dinari's system, an order follows a two-stage lifecycle: the OrderRequest (the user's intent) and the Order (the actual on-chain transaction). When an OrderRequest reaches the SUBMITTED status, it means the order has been successfully submitted to the order book and is actively waiting to be matched with a counterparty.

This is a normal and active status — not an error or a stuck state. However, customers frequently perceive it as "stuck" because they expect immediate execution. Understanding why orders remain in SUBMITTED is critical for both support teams and customers to set proper expectations and reduce unnecessary escalations.

---

## Process

### Step 1: Confirm the Order Status

First, verify the order is indeed in SUBMITTED status using the Get Order Request by ID endpoint:

http

`GET /api/v2/accounts/`{account\_id}`/order_requests/`{order\_request\_id}

Look for the status field. If it shows SUBMITTED, the order is active on the order book.

If the stock\_order\_id field is populated, you can also retrieve the Order details:

http

`GET /api/v2/accounts/`{account\_id}`/orders/`{order\_id}

### Step 2: Check the Trading Session

Use the Get Market Hours endpoint to determine the current session:

http

`GET /api/v2/market_data/market_hours/`

Compare the order's created\_dt with the session rules:

| **Session** | **Hours (ET)** | **What It Means for Your Order** |
| --- | --- | --- |
| **Regular** | Weekdays 9:30 AM – 4:00 PM | All order types accepted; expect normal execution |
| **Extended** | Pre-market 4:00–9:30 AM; After-hours 4:00–8:00 PM | Limit orders only; may take longer to fill |
| **Overnight** | 8:00 PM – 4:00 AM weekdays | Limit orders only; fills book in following session |
| **Open (24/7)** | Friday 8:00 PM – Sunday 8:00 PM | Blockchain only; limited tickers; lower liquidity |

#### Step 3: Check the Order Type and TIF

| **Parameter** | **What to Check** |
| --- | --- |
| `order_type` | If `MARKET` and placed off-hours → converted to marketable limit order |
| `order_tif` | If `DAY` and placed over weekend → remains eligible through next trading day |
| `limit_price` | If `LIMIT` order, check if price has been reached |

#### Step 4: Check for Partial Fills

  

Call the Get Order Fulfillments endpoint:

http

`GET /api/v2/accounts/`{account\_id}`/orders/`{order\_id}`/fulfillments`

If any fulfillments exist, the order has been partially filled and is waiting for the remainder.

---

### Key Takeaway

SUBMITTED is not an error state. It's the normal, active state for an order waiting to be filled. Most "stuck" orders are simply resting on the order book during off-hours sessions or waiting for a limit price to be reached. Understanding the trading session rules is the key to setting proper expectations and reducing unnecessary escalations.

Updated about 1 month ago

---

[Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)[Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

Did this page help you?

Yes

No

Copy Page

* + [Overview / Context](https://docs.dinari.com/docs/stuck-orders)
  + [Process](https://docs.dinari.com/docs/stuck-orders)
  + - [Step 1: Confirm the Order Status](https://docs.dinari.com/docs/stuck-orders)
    - [Step 2: Check the Trading Session](https://docs.dinari.com/docs/stuck-orders)
    - * [Step 3: Check the Order Type and TIF](https://docs.dinari.com/docs/stuck-orders)
      * [Step 4: Check for Partial Fills](https://docs.dinari.com/docs/stuck-orders)
    - [Key Takeaway](https://docs.dinari.com/docs/stuck-orders)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Orders Stuck in SUBMITTED Status","dateModified":"2026-10-14T11:54:48.000Z"}
```