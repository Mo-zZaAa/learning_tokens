---
url: https://docs.dinari.com/docs/order-type
title: Order Types & Behaviors
description: Market and limit order types across Dinari's order-placement APIs, including required fields, pricing logic, and order controls.
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

# Order Types & Behaviors

Market and limit order types across Dinari's order-placement APIs, including required fields, pricing logic, and order controls.

Dinari abstracts most market-structure complexity behind a single set of order-placement APIs. This page explains the order types Dinari supports, the fields each requires, and how order type affects pricing and order controls.

## Order Types

| `order_type` | Behavior |
| --- | --- |
| `MARKET` | Executes at the prevailing market price.1 |
| `LIMIT` | Executes only at the specified `limit_price` or better. |

* 1 Market order behavior may change depending on the available trading sessions. See [Marketable Limit](https://docs.dinari.com/docs/order-type) documentation for additional information.

> ℹ️
>
> ### Stop, stop-limit, trailing order types are not supported at this time.

`order_side` is either `BUY` or `SELL`.

## Order Placement

The method of placing an order depends primarily on the wallet type.

| Method | Wallet type | Description | Endpoint(s) |
| --- | --- | --- | --- |
| **Managed Orders** | Dinari-managed wallet | Dinari places the order on your behalf. | `POST /api/v2/accounts/{account_id}/order_requests/{market_buy | market_sell | limit_buy | limit_sell}` |
| **Order Request (EIP-155)** | Self-custodied wallet | Generate a permit, sign it, then either submit it on-chain yourself or have Dinari submit it for you. | `POST /api/v2/accounts/{account_id}/order_requests/eip155/permit` `POST /api/v2/accounts/{account_id}/order_requests/eip155/submit` |

Every order flows through the same v2 `OrderRequest` → `Order` model. An `OrderRequest` must be created first, which is submitted on-chain to create an `Order`.

```
flowchart LR
  ManagedWallet --> OrderRequest
  SelfWallet[Self-custodied wallet] --> OrderRequestEIP155
  OrderRequest -- auto submitted--> Blockchain
  OrderRequestEIP155 -- Dinari sponsored<br/>eip155/submit --> Blockchain
  OrderRequestEIP155 -- self-sponsored submission --> Blockchain
  Blockchain --> Order
```

Go to [Placing Orders](https://docs.dinari.com/docs/placing-dshare-orders) for more detail on placing orders.

### Required fields by order type

| **Order Type** | **Required Fields** | **Precision** |
| --- | --- | --- |
| Market buy | `payment_amount` (USD notional) | ≤ 2 decimals |
| Market sell | `asset_quantity` | ≤ 6 decimals |
| Limit buy / sell | `asset_quantity` + `limit_price` | quantity ≤ 4 decimals, price ≤ 2 decimals |

## Order Behavior

While the order interface is simple, it's important to understand the behavior of each `order_type` which is dependent primarily on the available trading sessions when the order was submitted.

| Trading Session1 *(times in ET)* | Hours | Availability | `order_type` | Behavior |
| --- | --- | --- | --- | --- |
| **Regular** | Weekdays *9:30a-4:00pm* | All tickers, high liquidity. | `market` | Market |
| `limit` | Limit |
| **Extended** | Weekdays *4:00am-9:30am* *4:00pm-8:00pm* | Most tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |
| **Overnight** | Weekdays2 *8:00pm(T-1)-4:00am* | Most tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |
| **Open (24/7)** | *All other times.3* | Limited tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |

* 1 See [Trading Hours](https://docs.dinari.com/docs/trading-hours) for more detailed information.
* 2 From 8:00pm the previous day to 4:00am of days with a regular trading session. See [Trading Hours](https://docs.dinari.com/docs/trading-hours) for more detailed information.
* 3 The Open (24/7) trading session is open when other trading sessions are closed for limited tickers. This includes weekends and holidays.

### Marketable Limit Orders

When a market order cannot be routed as a plain market instruction — primarily outside regular U.S. market hours — Dinari converts it into a **marketable limit** order to attempt to fill the order at the best available price similar to true market orders.

* **Buys** are priced at the latest **ASK**.
* **Sells** are priced at the latest **BID**.

Because the result is a limit order, it may fill fully, partially, or not at all. Any unfilled remainder is refunded.

### Non-fractionable Assets

Market buy orders placed for non-fractional assets in all trading sessions are treated similarly and converted to marketable limit orders. In the background, Dinari calculates the maximum number of shares that can be bought before placing a quantity order.

After the order is filled or cancelled, the remainder is refunded.

## Time in Force

The order Time in Force determines how long an order remains eligible for execution.

### Supported values

| `order_tif` | Meaning |
| --- | --- |
| `DAY` (default) | Active until the next end of extended trading hours.1 |
| `GTC` | Good 'til cancelled (up to 90 days). |
| `IOC` | Immediate or cancel. Fills what it can immediately, then cancels any remainder; partial fills allowed. |
| `FOK` | Fill or kill. Must fill in full immediately or the entire order is cancelled; no partial fills. |

* 1 Note: `DAY` orders placed on the weekend will be valid until the next end of extended trading hours (i.e. 8:00pm ET on Monday)

## Guidance For Partners

* **Outside regular hours, submit limit orders with an explicit** `limit_price`**.** This is the most predictable path.
* **Expect partial fills and refunds** when placing market orders outside of the Regular Trading Session. Reconcile against `Order` status and the associated `OrderFulfillment` records rather than assuming a single terminal fill.
* **A weekend order shown as** `PENDING``SUBMITTED` **is usually correct, not stuck.** It may be resting on the Dinari order book or waiting to re-route to the broker when the weekend session ends.

Updated about 1 month ago

---

[Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)[Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)

Did this page help you?

Yes

No

Copy Page

* + [Order Types](https://docs.dinari.com/docs/order-type)
  + [Order Placement](https://docs.dinari.com/docs/order-type)
  + - [Required fields by order type](https://docs.dinari.com/docs/order-type)
  + [Order Behavior](https://docs.dinari.com/docs/order-type)
  + - [Marketable Limit Orders](https://docs.dinari.com/docs/order-type)
    - [Non-fractionable Assets](https://docs.dinari.com/docs/order-type)
  + [Time in Force](https://docs.dinari.com/docs/order-type)
  + - [Supported values](https://docs.dinari.com/docs/order-type)
  + [Guidance For Partners](https://docs.dinari.com/docs/order-type)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Order Types & Behaviors","dateModified":"2026-10-14T11:28:42.000Z"}
```