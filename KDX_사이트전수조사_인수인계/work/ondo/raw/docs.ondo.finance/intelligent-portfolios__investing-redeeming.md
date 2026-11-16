---
url: https://docs.ondo.finance/intelligent-portfolios/investing-redeeming
title: Investing & Redeeming - Ondo Finance
description: How investing and redeeming work, and how base and current weights differ.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What are base weights and current weights?](https://docs.ondo.finance/intelligent-portfolios/investing-redeeming)
* [Are mints and redemptions processed at base weights or current weights?](https://docs.ondo.finance/intelligent-portfolios/investing-redeeming)

Ondo Intelligent Portfolios

# Investing & Redeeming

Copy pageCopy page

How investing and redeeming work, and how base and current weights differ.

Copy pageCopy page

Investing in and redeeming Ondo Intelligent Portfolio tokens generally works the same way as Ondo tokenized stocks. See [Investing & Redeeming](https://docs.ondo.finance/ondo-stocks/investing-and-redeeming) under Ondo Stocks for details.

### What are base weights and current weights?

Base weights are the model’s target allocations: the percentage of the portfolio that each asset is intended to represent, as defined by the model provider. Current weights are the percentage each asset actually represents at a given moment, based on the current market value of the portfolio’s holdings.At each portfolio’s inception, the underlying assets are calibrated to the model’s base weights. As market prices move, the actual weights may naturally drift away from base weights — assets that outperform grow to a larger share of the portfolio, and assets that underperform shrink. This drift is normal and expected. Each portfolio is designed to [rebalance](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution) back to its base weights approximately every quarter.Portfolio weights are shown on each portfolio’s product page at [app.ondo.finance](https://app.ondo.finance/).

### Are mints and redemptions processed at base weights or current weights?

They differ.When you mint, your investment is put to work according to the model’s target allocations — Ondo invests your funds into the portfolio’s assets at the model’s base weights.When you redeem, your redemption is processed against the portfolio’s current weights — redemptions return your share of the existing portfolio, which reflects how weights have drifted since the last rebalance.

[Model Providers](https://docs.ondo.finance/intelligent-portfolios/model-providers)[Token Quote & Pricing](https://docs.ondo.finance/intelligent-portfolios/pricing)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming#webpage","url":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming","name":"Investing & Redeeming","description":"How investing and redeeming work, and how base and current weights differ.","dateModified":"2026-09-24T00:59:51.971Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Intelligent Portfolios","item":"https://docs.ondo.finance/intelligent-portfolios/overview"},{"@type":"ListItem","position":2,"name":"Investing & Redeeming","item":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming#article","headline":"Investing & Redeeming","name":"Investing & Redeeming","description":"How investing and redeeming work, and how base and current weights differ.","url":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/intelligent-portfolios/investing-redeeming#webpage"},"dateModified":"2026-09-24T00:59:51.971Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```