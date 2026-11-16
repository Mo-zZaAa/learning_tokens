---
url: https://docs.dinari.com/docs/what-is-usd
title: What is USD+?
description: USD+ is a yield-bearing stablecoin issued by Dinari. It is pegged 1:1 to the US dollar, 100% backed by short-term US treasuries and USD , and it automatically pays yield to anyone holding it — no staking, claiming, or lockups required. Think of USD+ like a brokerage cash sweep . When cash sits idle…
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

# What is USD+?

USD+ is a yield-bearing stablecoin issued by Dinari. It is pegged 1:1 to the US dollar, [100% backed by short-term US treasuries and USD](https://usd.dinari.com/transparency), and it automatically pays yield to anyone holding it — no staking, claiming, or lockups required.

Think of USD+ like a **brokerage cash sweep**. When cash sits idle in a brokerage account, it is automatically swept into short-term US treasuries so it earns yield instead of doing nothing. USD+ works the same way for onchain dollars: it is the default redemption and settlement token across Dinari, and simply holding it earns yield on short-term US treasuries.

# How yield works

USD+ is a **daily rebasing** token. Yield is distributed by increasing every holder's balance directly in their wallet — the number of USD+ you hold grows over time while each USD+ remains redeemable for $1.

* **Automatic** — yield accrues to your wallet without staking, claiming, or any onchain action.
* **Rebasing** — your balance increases on a daily basis; you do not receive a separate reward token.
* **Backed by treasuries** — the dollars backing USD+ are invested in short-term US treasuries, and the interest those treasuries earn is what funds the rebase.

# Minting and redeeming

* **Mint** USD+ by depositing a supported stablecoin (USDC or USDT) of equivalent value.
* **Redeem** USD+ at any time for $1 each, paid in USDC. Redemptions settle in 0–3 days depending on size.

There are two ways to access USD+:

1. **App** — mint, hold, and redeem directly at [usd.dinari.com](https://usd.dinari.com/).
2. **Smart contract** — integrate USD+ programmatically using the Minter and Redeemer contracts. See the [USD+ token & contract addresses](https://docs.dinari.com/docs/usdplus-evm) and the [EVM integration guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide).

# Where USD+ is available

USD+ is deployed on multiple EVM chains, including Ethereum, Avalanche C-Chain, Base, Arbitrum, and Plume (with testnet deployments available for development). The token and contract addresses for each chain are listed in [Blockchain → EVM](https://docs.dinari.com/docs/usdplus-evm).

USD+ is also the default stablecoin across the Dinari [dShares™](https://docs.dinari.com/docs/what-is-dshare) platform — for example, dividends on tokenized equities are paid in USD+, so distributions begin earning yield the moment they land.

Updated about 1 month ago

---

[Deprecation Notices](https://docs.dinari.com/docs/deprecations)[Blockchain](https://docs.dinari.com/docs/blockchain-1)

Did this page help you?

Yes

No

Copy Page

* + [How yield works](https://docs.dinari.com/docs/what-is-usd)
  + [Minting and redeeming](https://docs.dinari.com/docs/what-is-usd)
  + [Where USD+ is available](https://docs.dinari.com/docs/what-is-usd)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"What is USD+?","dateModified":"2026-10-14T11:27:32.000Z"}
```