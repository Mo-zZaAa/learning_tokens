---
url: https://docs.dinari.com/docs/pricing-quotes
title: Pricing & Quotes
description: Dinari provides realtime prices and quotes for stocks that we cover and it's important to understand the distinction between the two and where this data comes from. Stock Price The realtime stock price is provided by the Get Stock current price API endpoint. This is a singular price denominated in U…
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

# Pricing & Quotes

Dinari provides realtime prices and quotes for stocks that we cover and it's important to understand the distinction between the two and where this data comes from.

## Stock Price

The realtime stock price is provided by the [Get Stock current price](https://docs.dinari.com/reference-link/getstockcurrentprice) API endpoint. This is a singular price denominated in USD representing the "Fair Market Value" of the stock or what a reasonable price point would be. This number is a computed number blending a number of data points including but not limited to the last trade, recent trade price points/volume and resting order book price points and volume.

This price is what should be used in most cases when displaying to the user.

## Stock Quotes

Realtime stock quotes are provided by the [Get Stock Quote](https://docs.dinari.com/reference-link/getstockcurrentquotesroutev2) API endpoint. Stock quotes represent real interest in buying and selling of the stock. Quotes contain a number of standard components:

* Bid Price: The maximum price buyers are willing to pay
* Bid Volume: # of shares resting at this bid price.
* Ask Price: The minimum price sellers are willing to accept
* Ask Volume: # of shares resting at this ask price.

> 🚧
>
> The stock price will be between the bid and ask price, but might not be the midpoint between the bid and ask prices.

Quotes are best provided at stock pre-confirmation pages and when the user wants to execute a trade. For limit orders, there is a higher chance of execution if the limit price is equal to the bid price for stock sell orders and the ask price for stock buy orders.

## Data Sources

The realtime market data feeds provided by Dinari are included as part of the platform. These included data feeds draw data directly from registered US national exchanges redundantly from multiple sources to deliver the highest quality data possible.

> 📘
>
> Dinari only draws and distributes official US exchange data and does not collect or use data from any purely on-chain trading of dShares™.

> 🚧
>
> IMPORTANT - These feeds only represent a fraction of the total traded stock and may not represent the National Best Bid Offer ("NBBO") data. See the below section regarding realtime SIP data.

### Metered Realtime SIP Data

Realtime Securities Information Processor ("SIP") data is available from Dinari and provides "NBBO" data which represents 100% of traded volume on exchanges. **This data is provided under license**, provided for a fee, and metered per request.

Please reach out to [customer support](https://docs.dinari.com/cdn-cgi/l/email-protection) if you are interested in the realtime SIP data feed.

> 📘
>
> Use of metered realtime SIP data is required for U.S. customers. Please see the US customer integration guide for more details.

### Trading Hours

Another consideration is the trading session. **Dinari operates entirely on regulated US exchanges and ATS's** for the regular, pre-market, post-market and overnight trading sessions. Liquidity available during the pre-market, post-market and overnight trading sessions is significantly lower than regular trading hours. Ensure your users are aware of the increased risk in entering trades during these trading hours.

> 📘
>
> IMPORTANT - It's highly recommended to only make LIMIT orders during this time.

Please see the [Trading Hours](https://docs.dinari.com/docs/trading-hours) page for more information regarding the available trading sessions.

Updated about 1 month ago

---

[Stock Data](https://docs.dinari.com/docs/stock-data)[24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)

Did this page help you?

Yes

No

Copy Page

* + [Stock Price](https://docs.dinari.com/docs/pricing-quotes)
  + [Stock Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [Data Sources](https://docs.dinari.com/docs/pricing-quotes)
  + - [Metered Realtime SIP Data](https://docs.dinari.com/docs/pricing-quotes)
    - [Trading Hours](https://docs.dinari.com/docs/pricing-quotes)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Pricing & Quotes","dateModified":"2026-10-14T11:29:03.000Z"}
```