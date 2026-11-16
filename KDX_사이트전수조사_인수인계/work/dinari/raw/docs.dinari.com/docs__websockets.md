---
url: https://docs.dinari.com/docs/websockets
title: Websockets for Order Data (BETA)
description: Subscribe to real-time market data and order updates via websockets.
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

# Websockets for Order Data (BETA)

Subscribe to real-time market data and order updates via websockets.

> ⚠️
>
> ### DRAFT
>
> The websocket feature is currently in **beta** and the implementation may change.

Dinari's Websocket API provides real-time market data and order updates, allowing you to receive instant pricing and quotes as well as notifications about order status changes, fulfillments, and other order-related events without polling the REST API.

# Key Features

* **Real-time Updates**: Receive order status changes as they happen
* **Efficient**: Eliminate the need for constant polling of the REST API
* **Scalable**: Handle multiple subscriptions per connection
* **Reliable**: Automatic reconnection and message acknowledgments

# Usage

| Environment | Hostname |
| --- | --- |
| Production | `wss://ws.api.dinari.com` |
| Sandbox | `wss://ws.api.sandbox.dinari.com` **(coming soon)** |

## Authentication

WebSocket connections require authentication using your API credentials. Please use the correct credentials for your environment (sandbox or production).

**Authentication Request**

JSON

```
{
  "command": "authenticate",
  "data": {
    "api_key": "your api key",
    "api_secret": "your api key secret"
  }
}
```

**Response**

JSON

```
{
  "event_type": "authentication",
  "data": {
    "status": "authenticated",
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b"
  }
}
```

## Market Data

| Available Data Types | Description |
| --- | --- |
| `stock_dfn_l2` | DFN Level 2 order book data |
| `stock_dfn_quotes` | DFN top-of-book quotes |

**Subscription**

Subscribe to market data with the `market_data_subscribe` command. This command may be reissued at anytime to update the subscription. All requested `stock_ids` must be listed.

> `stock_ids` can be fetched from the [🔗 Get Stocks](https://docs.dinari.com/reference/getstocks) API endpoint.

JSON

```
{
  "command": "market_data_subscribe",
  "data": {
    "stock_dfn_l2": ["stock_id or * for all"], 
    "stock_dfn_quotes": ["stock_id or * for all"]
  }
}
```

### Data Types

**Level 2 Data**

JSON

```
{
  "event_type": "market_data:l2_data",
  "data": {
    "Symbol": "AAPL",
    "MaxDepth": 30,
    "Bids": [
      {
        "Price": 0.01,
        "Size": 150,
        "Depth": 1,
        "NumOrders": 1
      }
    ],
    "Asks": [],
    "LastMatch": null,
    "Timestamp": "2025-12-12T17:54:44.382483808Z",
    "SchemaVersion": "1.0.0"
  }
}
```

**DFN Quote**

JSON

```
{
  "event_type": "market_data:dfn_quote",
  "data": {
    "Symbol": "AAPL",
    "BidExchange": "DFN",
    "BidPrice": 0.01,
    "BidSize": 150,
    "AskExchange": "DFN",
    "AskPrice": 0,
    "AskSize": 0,
    "TimeStamp": "2025-12-11T17:17:54.141119146Z",
    "Conditions": null,
    "Tape": ""
  }
}
```

## Order Data

Use the `order_data_subscribe` command with an empty data map to subscribe to real-time updates for your customer's orders account.

> ⚠️
>
> ### Cursor support coming soon

**Subscription Request**

JSON

```
{
  "command": "order_data_subscribe",
  "data": {}
}
```

**Response**

JSON

```
{
  "event_type": "order_data_subscription",
  "data": {
    "status": "subscribed"
  }
}
```

### Data Types

**Order Request**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order_request": {
      "id": "019b1384-2fc9-7485-ab0b-01eefe126151",
      "account_id": "0198862c-61ec-7375-bd98-4e306ab177c9",
      "recipient_account_id": "0198862c-61ec-7375-bd98-4e306ab177c9",
      "status": "QUOTED",
      "order_side": "SELL",
      "order_type": "LIMIT",
      "order_tif": "DAY",
      "order_id": null,
      "created_dt": "2025-12-12T17:03:08.724979Z"
    }
  }
}
```

**Order Data**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order": {
      "id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "status": "SUBMITTED",
      "order_contract_address": "0x1f96D1656a6500e526E92B19EAA894A6A7647ABa",
      "order_transaction_hash": "0x0e36a82c5fe36075f2badc1b787ffc929a317a8ce02200ef4c72a95e46c70e29",
      "cancel_transaction_hash": null,
      "order_side": "SELL",
      "order_type": "LIMIT",
      "order_tif": "DAY",
      "order_request_id": "019b1384-2fc9-7485-ab0b-01eefe126151",
      "stock_id": "0196d545-d8a8-7210-8cd1-a49e82c31e53",
      "asset_token_quantity": 0.001000000000000000,
      "payment_token_quantity": 0,
      "payment_token": "0xd54c40022500D88BbE0262FA9ffdf3D9921B24e8",
      "limit_price": 100.000000000000000000,
      "created_dt": "2025-12-12T17:04:17.223274Z",
      "chain_id": "eip155:202110",
      "asset_token": "0x83EBfbC73e60c45380426acc66725405A4EF7D61",
      "fees": 0
    }
  }
}
```

**Order Fulfillment**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order_fulfillment": {
      "id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "order_id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "chain_id": "eip155:202110",
      "transaction_hash": "0xc488f4fcc8ee5163766935dfba7cf6b50a862b67eeeda7e01b6d5dab59746c2f",
      "transaction_dt": "2025-12-12T17:04:17.223274Z",
      "asset_token_filled": 0,
      "asset_token_spent": 0.001,
      "payment_token_filled": 0.279014000000000000,
      "payment_token_spent": 0,
      "payment_token_fee": 0.201395070000000000
    }
  }
}
```

Updated 10 days ago

---

[Mergers](https://docs.dinari.com/docs/mergers)[Troubleshooting & Known Issues](https://docs.dinari.com/docs/troubleshooting-known-issues)

Did this page help you?

Yes

No

Copy Page

* + [Key Features](https://docs.dinari.com/docs/websockets)
  + [Usage](https://docs.dinari.com/docs/websockets)
  + - [Authentication](https://docs.dinari.com/docs/websockets)
    - [Market Data](https://docs.dinari.com/docs/websockets)
    - * [Data Types](https://docs.dinari.com/docs/websockets)
    - [Order Data](https://docs.dinari.com/docs/websockets)
    - * [Data Types](https://docs.dinari.com/docs/websockets)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Websockets for Order Data (BETA)","dateModified":"2026-11-06T16:53:49.000Z"}
```