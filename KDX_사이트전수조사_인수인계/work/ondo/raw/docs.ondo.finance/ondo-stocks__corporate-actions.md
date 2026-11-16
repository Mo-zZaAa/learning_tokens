---
url: https://docs.ondo.finance/ondo-stocks/corporate-actions
title: Corporate Actions - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What is a corporate action?](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [How do corporate actions affect Ondo tokenized stocks?](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [How are dividends handled?](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [Is trading halted during dividends?](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [Corporate actions and news while the US market is closed](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [What is an ex-dividend date?](https://docs.ondo.finance/ondo-stocks/corporate-actions)
* [What about other corporate actions?](https://docs.ondo.finance/ondo-stocks/corporate-actions)

Ondo Stocks

# Corporate Actions

Copy pageCopy page

Copy pageCopy page

### What is a corporate action?

A corporate action is any event initiated by a company that affects its securities—stocks, bonds, or other instruments—and typically requires updates to records, valuations, or entitlements for investors. Common examples of corporate actions are dividends, stock splits, mergers or acquisitions, spin-offs (creating a new, separate company and giving shares to existing holders), rights offerings (offering existing shareholders the chance to buy more shares at a discount), and (for bonds), bond calls or redemptions.

### How do corporate actions affect Ondo tokenized stocks?

Each type of corporate action has different results. Continue reading for more detailed information.

### How are dividends handled?

Dividends are automatically invested back into the referenced stock and reflected in token pricing. Minting and redemption quotes reflect both price changes and reinvested dividends. For a more detailed example, see the section about [how Ondo tokenized stocks are priced](https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing).On Solana and BNB Chain, wallets and explorers that support display scaling reflect dividend reinvestment in the displayed token balance, with a corresponding adjustment to the price per displayed unit. These adjustments affect only how your holdings are displayed; they do not change your onchain token balance or economic exposure.

### Is trading halted during dividends?

Trading may be paused for a given stock or ETF for a short time immediately before and after the start of the [ex-dividend date](https://docs.ondo.finance/ondo-stocks/corporate-actions). The exact duration of these pauses may change over time as we try to shorten it, but for now you can assume trading may be paused 7:50:00pm-8:10:00pm the day before the dividend ex-date.There is an exception to this rule, however. Unlike traditional stock dividends from individual companies, which are typically declared by the board of directors weeks or even months in advance with a fixed amount, ETF distributions (especially from fixed income funds) are often calculated based on the accrued income from underlying holdings like bonds, which can fluctuate due to interest payments, premium amortization, discount accretion, expenses, and other factors.This means the exact distribution amount is frequently finalized and announced very close to the ex-date—often just 1-2 business days before, or even after hours on the day prior to the ex-date. As a result, the exact amount of this dividend may sometimes not appear in our data feeds for up to 24 hours.In these cases, the platform *will* halt trading until the exact amount of the dividend is known. Trading will resume as soon as the system can incorporate the dividend amount and appropriately increase the number of shares per token.You can always check for upcoming dividends, as well as any tokens that are halted, at [status.ondo.finance](https://status.ondo.finance/)

#### Corporate actions and news while the US market is closed

Corporate actions and material news announced while the traditional US market is closed (including over a weekend or holiday) may not be reflected in token pricing until they can be processed. Affected assets, including those enabled for Off-Hours trading, may be paused until the relevant information is incorporated. You can always check for upcoming dividends and any halted tokens at [status.ondo.finance](https://status.ondo.finance/).

### What is an ex-dividend date?

When a company decides to pay a dividend (a portion of its profits) to its shareholders, it sets a few important dates to organize who gets the money. Two key dates are the **record date** and the **ex-dividend date** (or ex-date). These dates help decide who qualifies for the dividend.

1. **Record Date**: This is the day the company checks its list of shareholders to see who owns the stock and is eligible to receive the dividend. Think of it like the company taking a snapshot of its owners.
2. **Ex-Dividend Date (Ex-Date)**: This is the day when the stock starts trading *without* the dividend included in its price. If you buy the stock on or after this date, you won’t get the upcoming dividend. If you buy it *before* this date, you’re eligible for the dividend.

In the past, stock trades took two business days to “settle” (i.e. “trade + 2 days” or T+2), meaning it took two days for the buyer to officially become the owner of the stock. Because of this delay, the ex-date was set one day *before* the record date to give the trade time to settle, ensuring the buyer was on the company’s list by the record date.Now, with T+1 settlement, trades settle in just one business day. This means if you buy a stock the day before the record date, your purchase settles in time for you to be on the company’s list. As a result, the ex-date and record date are now the same day for most regular dividends.As an example, imagine a company announces it will pay a $1 dividend. It sets:

* **Record Date**: July 10 (the day it checks who owns the stock).
* **Ex-Date**: Also July 10 (because of T+1 settlement)

Here’s how it works:

* If you buy the stock *before* July 10 (say, on July 9 or earlier), your trade settles by July 10, so you’re on the company’s list and get the dividend.
* If you buy the stock *on or after* July 10, you won’t get the dividend because you’re not the official owner until the next day (July 11), after the record date.

### What about other corporate actions?

* Earnings: For a limited period of time around earnings announcements, assets enter a “limited” state, in which the maximum single trade size is reduced. This “limited” state ends shortly after the earnings announcement ends.

More information about other corporate actions will be provided soon.

[Token & Quote Pricing](https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing)[Fees & Taxes](https://docs.ondo.finance/ondo-stocks/fees-and-taxes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/ondo-stocks/corporate-actions#webpage","url":"https://docs.ondo.finance/ondo-stocks/corporate-actions","name":"Corporate Actions","dateModified":"2026-11-07T00:41:58.275Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/ondo-stocks/corporate-actions#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/ondo-stocks/corporate-actions#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Stocks","item":"https://docs.ondo.finance/ondo-stocks/overview"},{"@type":"ListItem","position":2,"name":"Corporate Actions","item":"https://docs.ondo.finance/ondo-stocks/corporate-actions"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/ondo-stocks/corporate-actions#article","headline":"Corporate Actions","name":"Corporate Actions","url":"https://docs.ondo.finance/ondo-stocks/corporate-actions","mainEntityOfPage":{"@id":"https://docs.ondo.finance/ondo-stocks/corporate-actions#webpage"},"dateModified":"2026-11-07T00:41:58.275Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```