---
url: https://docs.dinari.com/docs/hosted-trading
title: Hosted Trading
description: Dinari offers a hosted trading interface for compatible web and mobile interfaces.
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

# Hosted Trading

Dinari offers a hosted trading interface for compatible web and mobile interfaces.

As an alternative to a standard API integration, Dinari offers a white-label and theme-able fully-hosted or self-hosted trading web UI that can be used in your mobile or web application.

  
  
  

# Features

* Fully-managed or self-hosted options available.
* Compatible with all major web-based wallet interfaces.
* Supports mobile webview-based wallet integrations including [Base](https://join.base.app/), [Coinbase Wallet](https://wallet.coinbase.com/), [Metamask](https://metamask.io/download) etc.
* Supports multiple blockchains
* Integrates directly with the Dinari Enterprise API for trading and market data functionality.
* Includes both the front-end and back-end services.
* [*optional*] Hosted KYC flows by our identity verification provider [Persona](https://withpersona.com/).

# Hosting Options

## Dinari Hosting

Trading interfaces may be fully-hosted by Dinari which offers whitelabel turnkey integration with existing web trading interfaces or mobile applications.

* Fully-managed and dedicated hosting infrastructure with 99.99% SLA uptime.
* Automated container-based updates, testing and green/blue deployment.
* Deployable in any major AWS region.
* Completely independent AWS account and runtime environment including private networking, database and capacity isolation.
* Utilizes industry best practices for secure deployment.
* Logs and readonly-access to AWS account is available.
* Additional restricted staging environments are available.

### Integration Instructions

1. Partner submits logo and color scheme.
2. Dinari builds and deploys an isolated instance of the trading interface to `[PARTNER_ID].dinari-hosted.com`.
3. Integrate a webview in your mobile app or redirect users to this site.

*Initial integration support for the hosted option is included.*

> ✅
>
> All Dinari-hosted trading interfaces are available as separate subdomains on the `dinari-hosted.com` domain ensuring isolation of cookies and other domain-specific data.

## Self-hosting

* Fully customizable with source-code and containerized versions available.
* Host on your own infrastructure with unlimited use and perpetual licensing without royalties.
* Can be hosted on a root domain or any subdomain.
* `Makefile`-based development, build and run scripts.
* Multi-arch containers available for both x86\_64 and ARMv8 architectures.
* Fully-automated DB migrations.
* Terraform provisioning code available upon request.

### Requirements

* Node.JS 24 runtime or general container runtime.
* PostgreSQL 16 database

Updated about 1 month ago

---

[Deploy to production](https://docs.dinari.com/docs/deploy-to-production)[What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)

Did this page help you?

Yes

No

Copy Page

* + [Features](https://docs.dinari.com/docs/hosted-trading)
  + [Hosting Options](https://docs.dinari.com/docs/hosted-trading)
  + - [Dinari Hosting](https://docs.dinari.com/docs/hosted-trading)
    - * [Integration Instructions](https://docs.dinari.com/docs/hosted-trading)
    - [Self-hosting](https://docs.dinari.com/docs/hosted-trading)
    - * [Requirements](https://docs.dinari.com/docs/hosted-trading)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Hosted Trading","dateModified":"2026-10-14T11:25:12.000Z"}
```