---
url: https://docs.dinari.com/docs/faqs
title: FAQs
description: Overview What is Dinari? Dinari provides infrastructure for trading traditional securities, like stocks and exchange-traded funds (ETFs), on the blockchain. It uses smart contracts (programs that run on a blockchain) to represent these securities as tokens, called dShares, and automates buying and s…
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

# FAQs

## Overview

**What is Dinari?**

Dinari provides infrastructure for trading traditional securities, like stocks and exchange-traded funds (ETFs), on the blockchain. It uses smart contracts (programs that run on a blockchain) to represent these securities as tokens, called dShares, and automates buying and selling them.

**What are dShares?**

dShares are tokenized representations of traditional equities that are backed 1:1 by the underlying securities. When you hold a dShare, you hold the same economic rights you would get by holding the underlying stock through a traditional broker, such as dividends and stock splits.

**Do I own the actual shares?**

No, Dinari holds the underlying stocks in custody through a third-party custodial broker. When you purchase a dShare, you receive a separate security. The corresponding shares back that security, but you are not a direct shareholder in the company.

**Are dShares physically backed?**

Yes, one real share in a custodial brokerage account backs each dShare in circulation. A third-party custodial broker holds the underlying assets. An independent Big Four accounting firm audits the reserves to confirm this 1:1 backing.

---

## **Getting Started: KYC & Wallets**

**How can I purchase dShares?**

Before you purchase dShares:

1. Set up a wallet compatible with the Ethereum Virtual Machine (EVM), the environment that runs Ethereum smart contracts.
2. Fund your wallet with enough supported stablecoin (a token designed to maintain a stable value) for your purchase.
3. Complete Know Your Customer (KYC), the identity verification process.

**What do I need for the KYC verification process?**

Prepare a government-issued identity document (like a driver's license or passport) and proof of residency (such as a current utility bill or bank statement).

**Can I purchase dShares without performing a KYC check?**

No, Dinari requires you to complete KYC verification before purchasing dShares.

**Which countries does Dinari support?**

Dinari offers dShares in over 85 jurisdictions outside the United States under Regulation S. Check Dinari's documentation for the list of unsupported countries.

**Can I connect an existing smart contract wallet?**

Yes, Dinari supports self-custody smart contract wallets (wallets you control through on-chain code) for proxied orders. Dinari identifies these as EIP-155 orders; EIP-155 uses chain IDs to protect transaction signatures from reuse on another chain.

Connect the wallet using its contract address and chain ID (the network identifier, such as `eip155:8453` for Base). Use ERC-1271, the standard for validating smart contract wallet signatures, when signing messages.

---

## **Trading & Orders**

**What order types are supported?**

Dinari supports two order types: **MARKET** and **LIMIT**. Dinari does not support stop, stop-limit, or trailing orders.

**Can I trade outside of U.S. market hours?**

Yes, Dinari operates across four distinct trading sessions, including extended, overnight, and weekend sessions. During extended, overnight, and weekend sessions, Dinari accepts only **limit orders** directly. It automatically converts market orders to marketable limit orders (limit orders priced to execute against available offers).

**How does settlement work?**

Settlement occurs on-chain in a single step once an order is filled. A buy mints dShares to your wallet, and a sell burns dShares and releases the proceeds. Partially settled orders are not possible.

**Does Dinari support short selling?**

No, native short selling of dShares is not supported. The only way to get short exposure is through tokenized inverse ETFs that Dinari supports.

**What is the maximum order size?**

There is no single fixed maximum order size. Precision limits and partner-configurable caps constrain order sizes. For example, the payment amount for a market buy supports 2 decimal places. Orders above $5,000 USD may take 1–2 days to execute.

---

## **Dividends & Corporate Actions**

**How are dividends paid?**

Dinari supports fully automated cash dividends. Dinari pays them in stablecoins (like USD+) directly to your wallet on the same schedule as the underlying stock.

**What corporate actions are supported?**

Dinari processes dividends, stock splits (forward and reverse), ticker changes, and mergers. Dinari automatically reflects these changes on the dShare token and your ledger.

**Do I need to do anything for a stock split?**

No, a stock split mirrors automatically on your dShare balance. For example, a 10-for-1 split means your 5 shares become 50, with the total value remaining unchanged.

---

## **Fees & Costs**

**How much does it cost to use Dinari?**

Fees vary by network. Issuance orders bear a fee of $1 plus 0.25% to 0.50% on Ethereum, or $0.20 plus 0.25% to 0.50% on Layer 2 (L2) networks, plus network fees. Layer 2 networks process transactions on top of a base blockchain.

**Can transaction fees be paid in stablecoins?**

Yes, Dinari allows transaction fees to be paid in stablecoins rather than ETH, improving the user experience.

---

## **Supported Assets & Networks**

**Which stocks are supported?**

Dinari supports over 724 tokenized U.S. stocks and ETFs, including all S&P 500 companies. A full list is available on the Dinari platform.

**Which blockchains are supported?**

Dinari supports Ethereum, Base, Arbitrum, Avalanche C-Chain, and Plume.

**Can dShares be bridged between chains?**

Yes, you can transfer dShares between supported blockchain networks using LayerZero V2, a protocol for sending messages between blockchains. The transfers use the Omnichain Fungible Token (OFT) standard, which maintains a unified token supply across networks.

---

## **Technical Integration (For Developers)**

**What is the order lifecycle?**

Every order moves through four stages: **Validation**, **Preparation**, **Execution**, and **Settlement**. A buy converts payment tokens into dShares, and a sell converts dShares back into payment tokens.

**How do I place an order via the API?**

You can place orders through three methods:

* **Managed Orders:** For Dinari-managed wallets.
* **Proxied Orders (EIP-155):** For self-custody wallets.
* **Direct smart contract calls:** Interact with the contracts directly.

**What is the difference between** `/permit` **and** `/permit_transaction`**?**

The `/permit` endpoint generates an EIP-2612 permit (a signed token-spending approval) for an **externally owned account (EOA)**, which you control with a private key.

The `/permit_transaction` endpoint prepares a transaction for **smart contract wallets** using ERC-1271 and Permit2. ERC-1271 validates smart contract wallet signatures. Permit2 is a contract system for signature-based token-spending permissions.

**What should I do if an order fails with a 423 error?**

A 423 error ("Account is currently in use") means a concurrent request is already being processed for that account. You should serialize your requests per account and implement a request queue.

**How should I handle a 404 "Account not found" error?**

This typically means you are using an account ID from a different environment (sandbox vs. production). Verify your client's `environment` setting matches where the account was created.

**Can I reuse a** `client_order_id` **after a failed order?**

No, a 409 conflict indicates that an existing order already uses the `client_order_id`. Generate a new, unique ID for each retry attempt.

Updated 4 days ago

---

[Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)[Status Pages](https://docs.dinari.com/docs/status-pages)

Did this page help you?

Yes

No

Copy Page

* + [Overview](https://docs.dinari.com/docs/faqs)
  + [Getting Started: KYC & Wallets](https://docs.dinari.com/docs/faqs)
  + [Trading & Orders](https://docs.dinari.com/docs/faqs)
  + [Dividends & Corporate Actions](https://docs.dinari.com/docs/faqs)
  + [Fees & Costs](https://docs.dinari.com/docs/faqs)
  + [Supported Assets & Networks](https://docs.dinari.com/docs/faqs)
  + [Technical Integration (For Developers)](https://docs.dinari.com/docs/faqs)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"FAQs","dateModified":"2026-11-12T18:23:06.000Z"}
```