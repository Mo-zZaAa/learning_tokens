---
url: https://docs.dinari.com/docs/taxes-reporting
title: Taxes & Reporting
description: Taxes Dividends US Dividend Withholding (ex-US Customers) Dinari automatically withholds and remits taxes on dividends for ex-US customers. Under Section 1441 of the U.S. Internal Revenue Code , a 30% withholding tax is imposed on U.S. source income most commonly dividends from U.S. equities paid to…
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

# Taxes & Reporting

# Taxes

## Dividends

### US Dividend Withholding (ex-US Customers)

> ✅
>
> Dinari automatically withholds and remits taxes on dividends for ex-US customers.

Under **[Section 1441 of the U.S. Internal Revenue Code](https://www.irs.gov/individuals/international-taxpayers/nra-withholding)**, a **30% withholding tax** is imposed on U.S. *source income* most commonly **dividends from U.S. equities** paid to non-U.S. persons. Accordingly, Dinari will **automatically withhold and remit 30%** of all applicable U.S. stock dividends to the U.S. Internal Revenue Service (IRS) at the time of payment.

This withholding is handled entirely at the broker level. **Clients are not required to separately report or remit these taxes** to the IRS in the ordinary course.

If you are eligible for a reduced rate or exemption under an applicable U.S. tax treaty, you must provide appropriate documentation (e.g., IRS Form W-8BEN or W-8BEN-E). In some cases, withholding may still occur at the full 30% statutory rate. If excess tax is withheld, you may **seek a refund directly from the IRS by filing Form 1040-NR (U.S. Nonresident Income Tax Return)**.

We recommend consulting with your tax advisor to determine your eligibility for treaty benefits and whether filing a return to reclaim withholding is appropriate.

> ⚠️
>
> Applicable to dividends paid out on or after **2026-03-26**.

### 1099-DIV (US Customers)

For US customers, Dinari Securities LLC (registered broker-dealer) simplifies tax reporting process of clients by tracking all distributions credited to their account throughout the year, including ordinary dividends, qualified dividends, and capital gains distributions.

Following the close of the tax year, we issue Internal Revenue Service (IRS) **Form 1099-DIV**, which provides a detailed breakdown of these earnings and any foreign taxes paid or federal income tax withheld.

# Reporting

Settlement of dShares™ generally happens on the blockchain and you may query the blockchain for current and historical trades.

## Balance Reports

For partners who operate a Dinari-managed omnibus wallet, you may request monthly end-of-month balance reports in CSV format. Please reach out to [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection) to receive these reports.

## Transaction Reporting

Historical transaction reports in CSV format are available to all partners upon request. Please reach out to [[email protected]](https://docs.dinari.com/docs/support@dinari.com) to request this.

Updated about 1 month ago

---

[Restrictions](https://docs.dinari.com/docs/restrictions)[Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)

Did this page help you?

Yes

No

Copy Page

* + [Taxes](https://docs.dinari.com/docs/taxes-reporting)
  + - [Dividends](https://docs.dinari.com/docs/taxes-reporting)
    - * [US Dividend Withholding (ex-US Customers)](https://docs.dinari.com/docs/taxes-reporting)
      * [1099-DIV (US Customers)](https://docs.dinari.com/docs/taxes-reporting)
  + [Reporting](https://docs.dinari.com/docs/taxes-reporting)
  + - [Balance Reports](https://docs.dinari.com/docs/taxes-reporting)
    - [Transaction Reporting](https://docs.dinari.com/docs/taxes-reporting)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Taxes & Reporting","dateModified":"2026-10-14T11:36:33.000Z"}
```