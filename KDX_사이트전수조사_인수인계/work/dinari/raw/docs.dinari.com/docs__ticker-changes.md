---
url: https://docs.dinari.com/docs/ticker-changes
title: Ticker Changes
description: How Dinari handles issuer symbol, name, and CUSIP changes.
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

# Ticker Changes

How Dinari handles issuer symbol, name, and CUSIP changes.

# Ticker Changes

A ticker change, or more precisely a name change, is a rebranding event. The company changes its name, ticker symbol, and/or CUSIP, in any combination. No balances move and no cash is paid; only the identity changes.

Two things to know:

* A name change sometimes arrives alongside a reverse stock split, so both events can hit the same security in the same week.
* A CUSIP change matters even when the ticker looks identical, because the CUSIP is what follows the security through settlement.

---

## What changes at Dinari

When the symbol or CUSIP changes, Dinari swaps in new internal records for the security and updates the dShare™ token name.

| Property | Changes? |
| --- | --- |
| Share quantity held | ❌ No |
| Position value | ❌ No |
| Displayed symbol | ✅ Possibly |
| Displayed company name | ✅ Possibly |
| Underlying CUSIP | ✅ Possibly |
| Dinari `stock_id` you reference | ❌ No — Dinari maintains continuity |

### The asset goes quiet for a while

When the identifier changes, the old asset dShare is disabled and a new one is issued. Until Dinari re-points its records at the new identifier, the asset is disabled on the platform and all orders for it will be rejected.

---

## How it works, from your side

```
sequenceDiagram
    autonumber
    participant D as Dinari
    participant P as Partner
    participant U as End user
 
    Note over D: Name / symbol / CUSIP change — asset disabled
    D->>D: Verify the new asset,<br/>check for affected orders
 
    Note over D,P: Asset unavailable — orders rejected
    P->>D: Order submission
    D-->>P: Rejected — asset disabled
    P->>U: Show "temporarily unavailable"
 
    D->>D: Re-point records to the new asset,<br/>update token name, re-enable
 
    Note over D: Asset re-enabled — trading resumes
    D->>P: Confirmation of new symbol
    P->>D: Read portfolio
    D-->>P: Same amount, updated symbol<br/>and token metadata
    P->>U: Refresh mapping, display new symbol
```

Before re-enabling, Dinari validates that the asset is active again, all records reference the current asset, no orders or positions were affected, and share quantities are unchanged.

---

## Recommendations

1. **Key off** `stock_id`**, never the ticker symbol.** Treat `symbol` as a display field you refresh from the API. This is critical to ensuring that you are not impacted by ticker changes.
2. **Automatically handle rejections gracefully during the window.** Show "temporarily unavailable" rather than a raw error, and back off on retries.
3. **Refresh metadata afterwards.** Re-read the portfolio and update your cached `stock_id` → `symbol` and `token_address` mapping.
4. **Don't adjust balances.** Quantities don't move in a name change. If one did, check for a reverse split in the same window and contact your Dinari representative.

Updated about 1 month ago

---

[Stock Splits](https://docs.dinari.com/docs/stock-split-handling)[Mergers](https://docs.dinari.com/docs/mergers)

Did this page help you?

Yes

No

Copy Page

* + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + - [What changes at Dinari](https://docs.dinari.com/docs/ticker-changes)
    - * [The asset goes quiet for a while](https://docs.dinari.com/docs/ticker-changes)
    - [How it works, from your side](https://docs.dinari.com/docs/ticker-changes)
    - [Recommendations](https://docs.dinari.com/docs/ticker-changes)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Ticker Changes","dateModified":"2026-10-14T11:29:11.000Z"}
```