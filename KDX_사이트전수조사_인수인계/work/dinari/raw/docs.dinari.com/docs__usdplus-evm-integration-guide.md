---
url: https://docs.dinari.com/docs/usdplus-evm-integration-guide
title: Integration Guide
description: Minting USD+ To mint USD+, a deposit or mint can be performed on the USD+ Minter Contract as seen below: /// @notice calculate USD+ amount to mint for payment /// @param paymentToken payment token /// @param paymentTokenAmount amount of payment token function previewDeposit(IERC20 paymentToken, uint…
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

# Integration Guide

# Minting USD+

To mint USD+, a `deposit` or `mint` can be performed on the [USD+ Minter Contract](https://docs.dinari.com/docs/usdplus-evm) as seen below:

depositmint

```
/// @notice calculate USD+ amount to mint for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
function previewDeposit(IERC20 paymentToken, uint256 paymentTokenAmount)
  external
  view
  returns (uint256 usdPlusAmount);

/// @notice mint USD+ for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token to spend
/// @param receiver recipient
/// @return usdPlusAmount amount of USD+ minted
function deposit(IERC20 paymentToken, uint256 paymentTokenAmount, address receiver)
	external
	returns (uint256 usdPlusAmount);
```

```
/// @notice calculate the payment token amount to spend to mint USD+
/// @param paymentToken payment token
/// @param usdPlusAmount amount of USD+ to mint
function previewMint(IERC20 paymentToken, uint256 usdPlusAmount) 
	external view 
	returns (uint256 paymentTokenAmount);

/// @notice mint USD+ for payment
/// @param paymentToken payment token
/// @param usdPlusAmount amount of USD+ to mint
/// @param receiver recipient
/// @return paymentTokenAmount amount of payment token spent
function mint(IERC20 paymentToken, uint256 usdPlusAmount, address receiver)
	external
	returns (uint256 paymentTokenAmount);
```

# Redeeming USD+

To redeem USD+, a `requestRedeem` or `requestWithdraw`can be performed on the [USD+ Redeem Contract](https://docs.dinari.com/docs/usdplus-evm) as seen below:

requestRedeemrequestWithdraw

```
/// @notice calculate payment token amount received for burning USD+
/// @param paymentToken payment token
/// @param usdplusAmount amount of USD+ to burn
function previewRedeem(IERC20 paymentToken, uint256 usdplusAmount)
	external
	view
	returns (uint256 paymentTokenAmount);

/// @notice create a request to burn USD+ for payment
/// @param paymentToken payment token
/// @param usdplusAmount amount of USD+ to burn
/// @param receiver recipient
/// @param owner USD+ owner
/// @return ticket request ticket number
/// @dev exchange rate fixed at time of request creation
function requestRedeem(IERC20 paymentToken, uint256 usdplusAmount, address receiver, address owner)
	external
	returns (uint256 ticket);
```

```
/// @notice calculate payment token amount received for burning USD+
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
function previewWithdraw(IERC20 paymentToken, uint256 paymentTokenAmount)
	external
	view
	returns (uint256 usdplusAmount);

/// @notice create a request to burn USD+ for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
/// @param receiver recipient
/// @param owner USD+ owner
/// @return ticket request ticket number
/// @dev exchange rate fixed at time of request creation
function requestWithdraw(IERC20 paymentToken, uint256 paymentTokenAmount, address receiver, address owner)
	external
	returns (uint256 ticket);
```

Either of the two methods above will create a redemption request that may take 0-3 days depending on the size of the redemption made.

Updated about 1 month ago

---

[EVM](https://docs.dinari.com/docs/usdplus-evm)[Trading Hours](https://docs.dinari.com/docs/trading-hours)

Did this page help you?

Yes

No

Copy Page

* + [Minting USD+](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
  + [Redeeming USD+](https://docs.dinari.com/docs/usdplus-evm-integration-guide)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Integration Guide","dateModified":"2026-10-14T11:27:32.000Z"}
```