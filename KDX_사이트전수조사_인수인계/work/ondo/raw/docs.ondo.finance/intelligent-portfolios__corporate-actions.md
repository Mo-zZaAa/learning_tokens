---
url: https://docs.ondo.finance/intelligent-portfolios/corporate-actions
title: Corporate Actions - Ondo Finance
description: How corporate actions on underlying assets affect portfolio tokens.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [How do corporate actions affect Ondo Intelligent Portfolio tokens?](https://docs.ondo.finance/intelligent-portfolios/corporate-actions)
* [Is minting and redemption paused during corporate actions?](https://docs.ondo.finance/intelligent-portfolios/corporate-actions)
* [What happens if an asset in a portfolio is delisted, acquired, or otherwise ceases to trade?](https://docs.ondo.finance/intelligent-portfolios/corporate-actions)
* [Where can I learn more about how specific corporate actions work?](https://docs.ondo.finance/intelligent-portfolios/corporate-actions)

Ondo Intelligent Portfolios

# Corporate Actions

Copy pageCopy page

How corporate actions on underlying assets affect portfolio tokens.

Copy pageCopy page

### How do corporate actions affect Ondo Intelligent Portfolio tokens?

A corporate action is any event initiated by a company that affects its securities — such as dividends, stock splits, mergers or acquisitions, spin-offs, and rights offerings.Because each portfolio is backed by a basket of Ondo tokenized stocks and ETFs, corporate actions are handled at the constituent level. See [corporate actions handling](https://docs.ondo.finance/ondo-stocks/corporate-actions) for Ondo tokenized stocks.Price changes from corporate actions at the constituent level flow through to the portfolio token’s price. There is nothing you need to do, and your portfolio token balance does not change.

### Is minting and redemption paused during corporate actions?

It can be. If a corporate action pauses trading in any constituent asset — for example, around an ex-dividend date, or while an ETF distribution amount is being finalized — minting and redemption are paused for every portfolio holding that asset, until the constituent is trading again.These pauses affect minting and redemption only. Your tokens remain transferable and tradable on secondary markets. You can always check the current status of each portfolio and its constituents at [app.ondo.finance](https://app.ondo.finance/).

### What happens if an asset in a portfolio is delisted, acquired, or otherwise ceases to trade?

It depends on whether the portfolio has a fixed or dynamic asset set:

* **Fixed portfolios** (reconstitution shown as “Fixed”): if a constituent is affected by a terminal corporate action — such as a delisting, cash acquisition, or liquidation — the asset is removed and its weight will be rebalanced among the remaining constituents.
* **Dynamic portfolios**: the portfolio model may be adjusted at the model provider’s discretion — including whether the affected asset is replaced or its weight redistributed.

Any resulting change to a portfolio’s composition is reflected on its product page at [app.ondo.finance](https://app.ondo.finance/) and visible onchain. Minting and redemption for the affected portfolio may be paused while the change is processed.

### Where can I learn more about how specific corporate actions work?

For detailed treatment of dividends, ex-dividend dates, trading pauses, and other corporate action mechanics at the asset level, see [Corporate Actions](https://docs.ondo.finance/ondo-stocks/corporate-actions) under Ondo Stocks.

[Transferability](https://docs.ondo.finance/intelligent-portfolios/transferability)[Fees & Taxes](https://docs.ondo.finance/intelligent-portfolios/fees-taxes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions#webpage","url":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions","name":"Corporate Actions","description":"How corporate actions on underlying assets affect portfolio tokens.","dateModified":"2026-09-24T00:59:51.976Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Intelligent Portfolios","item":"https://docs.ondo.finance/intelligent-portfolios/overview"},{"@type":"ListItem","position":2,"name":"Corporate Actions","item":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions#article","headline":"Corporate Actions","name":"Corporate Actions","description":"How corporate actions on underlying assets affect portfolio tokens.","url":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions","mainEntityOfPage":{"@id":"https://docs.ondo.finance/intelligent-portfolios/corporate-actions#webpage"},"dateModified":"2026-09-24T00:59:51.976Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```