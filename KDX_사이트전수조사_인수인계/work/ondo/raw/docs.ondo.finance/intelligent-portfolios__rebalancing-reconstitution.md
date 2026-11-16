---
url: https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution
title: Rebalancing & Reconstitution - Ondo Finance
description: How portfolios rebalance to base weights and how reconstitution works.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What is rebalancing?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)
* [How often does a portfolio rebalance?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)
* [Do I need to do anything when a portfolio rebalances?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)
* [What is reconstitution?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)
* [How often does reconstitution happen?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)
* [What is the difference between rebalancing and reconstitution?](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution)

Ondo Intelligent Portfolios

# Rebalancing & Reconstitution

Copy pageCopy page

How portfolios rebalance to base weights and how reconstitution works.

Copy pageCopy page

### What is rebalancing?

At each portfolio’s inception, the underlying assets are calibrated to the model’s base weights. As market prices move, the actual weights may naturally drift away from base weights — assets that outperform grow to a larger share of the portfolio, and assets that underperform shrink. This drift is normal and expected. Rebalancing adjusts the portfolio’s holdings back to the model’s base weights. It changes how much of each asset the portfolio holds, not the asset mix in the portfolio.

### How often does a portfolio rebalance?

Portfolios generally follow a quarterly rebalance cadence, returning to their base weights each quarter. Each portfolio’s rebalance approach and frequency are different and set by its model provider.Each portfolio’s rebalance frequency and most recent rebalance date are shown on its product page at [app.ondo.finance](https://app.ondo.finance/).

### Do I need to do anything when a portfolio rebalances?

No. Rebalancing is executed by Ondo on behalf of all holders and requires no action from you. Your token balance does not change when a portfolio rebalances — the composition of the basket backing each token is adjusted, and every rebalance is visible onchain.

### What is reconstitution?

Reconstitution changes which assets are in the model — adding or removing constituents — rather than adjusting the weights of existing ones. Not every portfolio reconstitutes: some portfolio models define a fixed set of assets, while others are dynamic. Any changes to a portfolio’s composition are visible onchain.

### How often does reconstitution happen?

There is no fixed schedule. For dynamic portfolios, reconstitution happens at the model provider’s discretion, when the provider updates its model. Portfolios with a fixed asset set generally do not reconstitute and show a reconstitution of ‘Fixed’ on their product page. The exception is a terminal corporate action, such as a delisting — see [Corporate Actions](https://docs.ondo.finance/intelligent-portfolios/corporate-actions) for how these are handled. Check each portfolio’s product page at [app.ondo.finance](https://app.ondo.finance/) for its reconstitution approach.

### What is the difference between rebalancing and reconstitution?

Rebalancing adjusts how much of each asset the portfolio holds, returning portfolios to the model’s base weights — the assets stay the same.Reconstitution changes which assets are in the model, adding or removing constituents. All portfolios rebalance; only some reconstitute.

[Token Quote & Pricing](https://docs.ondo.finance/intelligent-portfolios/pricing)[Market Hours & Trading Availability](https://docs.ondo.finance/intelligent-portfolios/market-hours)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution#webpage","url":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution","name":"Rebalancing & Reconstitution","description":"How portfolios rebalance to base weights and how reconstitution works.","dateModified":"2026-09-24T00:59:51.970Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Intelligent Portfolios","item":"https://docs.ondo.finance/intelligent-portfolios/overview"},{"@type":"ListItem","position":2,"name":"Rebalancing & Reconstitution","item":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution#article","headline":"Rebalancing & Reconstitution","name":"Rebalancing & Reconstitution","description":"How portfolios rebalance to base weights and how reconstitution works.","url":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution","mainEntityOfPage":{"@id":"https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution#webpage"},"dateModified":"2026-09-24T00:59:51.970Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```