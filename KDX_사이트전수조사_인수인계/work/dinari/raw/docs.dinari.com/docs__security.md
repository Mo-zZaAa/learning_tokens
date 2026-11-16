---
url: https://docs.dinari.com/docs/security
title: Security
description: Contact To report a security-related issue, please contact us: Email: security@dinari.com [ PGP Key ] We ask that all communication follow responsible disclosure practices and comply with applicable laws. Security & Data Protection Dinari meets or exceeds industry best practices on infrastructure se…
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

# Security

## Contact

To report a security-related issue, please contact us:

Email: [`[email protected]`](https://docs.dinari.com/cdn-cgi/l/email-protection) [[PGP Key](https://assets.dinari.com/security/security@dinari.com.asc)]

*We ask that all communication follow responsible disclosure practices and comply with applicable laws.*

## Security & Data Protection

Dinari meets or exceeds industry best practices on infrastructure security and data protection including but not limited to:

* We collect only the data we need and protect it with financial industry-standard encryption in transit and at rest.
* Access to production environments and customer data is restricted to authorized staff and audited regularly.
* Our software and infrastructure are built and tested with security in mind, using modern tools and hardened cloud environments.
* We monitor our systems for suspicious activity and have procedures to respond quickly to incidents.
* All vendors and service providers, such as cloud and financial services partners, are audited for strong security and compliance.

## Security Disclosure Policy

We are committed to protecting our customers, partners, and systems, and we welcome responsible reports from the security community.

* If you discover a vulnerability or security issue in any of our products, infrastructure, or services, please notify us as quickly as possible.
* We will acknowledge your report, triage and prioritize it based on impact and likelihood, and keep you informed of our remediation progress where appropriate.
* Once the issue is resolved, we may publish a high-level summary of the vulnerability and our fix, without exposing sensitive implementation details or personal data. With your consent, we may also recognize your contribution publicly.

> ⚠️
>
> As a small company, we are unable to offer a bug bounty program at this time.

## Code Audits

Dinari smart contracts have been subject to a number of audits by reputable audit firms.

| Date | Auditor | Document |
| --- | --- | --- |
| 2023-08-11 | Sherlock | [Audit\_Sherlock\_230811.pdf](https://assets.dinari.com/audits/Audit_Sherlock_230811.pdf) |
| 2023-12-12 | Hacken | [Audit\_Hacken\_231212.pdf](https://assets.dinari.com/audits/Audit_Hacken_231212.pdf) |
| 2024-12-24 | Pashov | [Audit\_Pashov\_241224.pdf](https://assets.dinari.com/audits/Audit_Pashov_241224.pdf) |
| 2024-12-30 | Hacken | [Audit\_Hacken\_241230.pdf](https://assets.dinari.com/audits/Audit_Hacken_241230.pdf) |

Updated about 1 month ago

---

[Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)[Regional Requirements](https://docs.dinari.com/docs/regional-requirements)

Did this page help you?

Yes

No

Copy Page

* + [Contact](https://docs.dinari.com/docs/security)
  + [Security & Data Protection](https://docs.dinari.com/docs/security)
  + [Security Disclosure Policy](https://docs.dinari.com/docs/security)
  + [Code Audits](https://docs.dinari.com/docs/security)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Security","dateModified":"2026-10-14T11:39:59.000Z"}
```