---
url: https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history
title: Differences between ledger and trades history | Kraken
description: Support Center for Kraken.com | Bitcoin & Cryptocurrency Exchange | Bitcoin Trading Platform
fetched: 2026-11-16
method: static
plan: skim
---

Ask AI

All

Filter by:

Select Product

How do I deposit cash into my account?

I need help with account verification

Why can't I access my account?

Are there any crypto withdrawal fees?

I need help signing into my account

1. [Support](/)
2. [Trading](/categories/200187143-trading)
3. [Account History](/sections/360013915192-account-history)
4. [Account History Basics](/sections/360004134812-account-history-basics)

# Differences between ledger and trades history

Last updated: August 24, 2026

There are two main kinds of account history that clients can view or [export](/articles/208267878-How-can-I-export-my-account-history-): Ledger and Trades.

### Ledger history

Ledger history focuses on **changes to account balances**.

It answers questions like:

* •

  How much was **debited** from a currency balance? (and the reason for it, e.g. fees, withdrawal, trading or the result of settled or otherwise closed trades using margin).
* •

  How much was **credited** to a currency balance? (and the reason for it, e.g. deposit, trading or the result of settled or otherwise closed trades using margin).
* •

  How many **fees,** and in which currency, were paid to Kraken?

#### Working with Ledger history:

* •

  [To find balances for a specific date, look at the last change to each balance before the desired date.](/articles/balance-export)
* •

  To find what a currency was traded for, look for a matching *refid*.
* •

  To find which open spot margin position specific rollover fees are associated with, look for a matching *refid*.
* •

  If you see several deductions from different currencies but with the same

  *refid* and type '*margin*', that's likely the result of a liquidation.

For more details, see [explanation of ledger fields](/articles/360001169383-Explanation-of-Ledger-Fields).

### Trades history

Trades history focuses on the **execution details** of spot transactions (the matching of sell orders with buy orders and vice versa) with or without the use of margin.

It answers questions like:

* •

  What was a balance traded for?
* •

  The exchange rate for that trade?
* •

  The order type used?
* •

  Which executions were related to a specific order?
* •

  The fee estimate in terms of the quote currency (NOT necessarily the actual amount that was deducted).
* •

  The level of leverage used (for spot trades made using margin).

> **Note:**

* •

  Trades history only shows **executed** or **partially executed** orders. It does **not** show cancelled/untouched orders.
* •

  Trades history does not include the details of transactions conducted via the [Buy Crypto Widget](/articles/360051144472-The-Buy-Crypto-widget) or [Kraken app.](/articles/360049744652-Kraken-app-frequently-asked-questions) This information will only be present in the **Ledger** history.

For more details, see [explanation of trade fields](/articles/360001184886-Explanation-of-Trade-Fields).

### Example: the same trade in each view

Suppose you buy **0.05 BTC** with EUR at a price of **€60,000 per BTC** (total cost €3,000.00, fee €7.80). Here is how that single transaction appears in each type of history:

**Ledger history** — two entries (one per currency), linked by the same *refid*:

| refid | type | asset | amount | fee |
| --- | --- | --- | --- | --- |
| TSTRD1-EXMPL-000001 | trade | EUR | -3,000.00 | 7.80 |
| TSTRD1-EXMPL-000001 | trade | BTC | +0.05 | 0.00 |

**Trades history** — one entry showing the execution details:

| ordertxid | pair | type | price | cost | fee | volume |
| --- | --- | --- | --- | --- | --- | --- |
| OEXMPL-000001 | BTC/EUR | buy | 60,000.00 | 3,000.00 | 7.80 | 0.05 |

Key differences to notice:

* •

  The **Ledger** records the trade as balance changes: EUR is debited and BTC is credited, each as a separate entry sharing the same *refid*.
* •

  The **Trades** history records the trade as a single execution, including the pair, price, order side and volume — details that do not appear in the Ledger.
* •

  The fee in Trades history is an estimate in the quote currency, while the Ledger shows the fee actually deducted from your balance.

[Ledger history](#acc-ledger-history)[Trades history](#ce5-trades-history)[Example: the same trade in each view](#457-example-the-same-trade-in-each-view)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"WebSite","url":"https://kraken.com","description":"Buy, sell, trade and learn about crypto on Kraken — the simple, powerful crypto platform that grows with you.","potentialAction":{"@type":"RegisterAction","target":"https://www.kraken.com/sign-up"},"publisher":{"@context":"https://schema.org","@type":"Organization","name":"Kraken","alternateName":"Kraken Exchange","url":"https://www.kraken.com/","logo":{"@type":"ImageObject","@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","url":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","contentUrl":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","width":900,"height":900,"caption":"Kraken"},"image":{"@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg"},"sameAs":["https://www.facebook.com/KrakenFX","https://twitter.com/krakenfx","https://www.youtube.com/@KrakenCryptoExchange","https://en.wikipedia.org/wiki/Kraken_(company)","https://www.linkedin.com/company/krakenfx","https://www.instagram.com/krakenfx/","https://www.reddit.com/r/Kraken","https://apps.apple.com/us/app/kraken-buy-crypto-bitcoin/id1481947260","https://play.google.com/store/apps/details?id=com.kraken.invest.app&hl=en_US"],"contactPoint":{"@type":"ContactPoint","url":"https://support.kraken.com/hc/en-us/forms","contactType":"Customer Service"},"address":{"@type":"PostalAddress","streetAddress":"237 Kearny St #102","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94108","addressCountry":"US"}}},{"@type":"BreadcrumbList","@id":"https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://support.kraken.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://support.kraken.com/articles"},{"@type":"ListItem","position":3,"name":"115000302707 Differences Between Ledger And Trades History","item":"https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history"}]},{"@type":"WebPage","@id":"https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history#webpage","url":"https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history","name":"Differences between ledger and trades history | Kraken","description":"Support Center for Kraken.com | Bitcoin & Cryptocurrency Exchange | Bitcoin Trading Platform","isPartOf":{"@id":"https://support.kraken.com/#website"},"publisher":{"@id":"https://support.kraken.com/#organization"},"breadcrumb":{"@id":"https://support.kraken.com/articles/115000302707-differences-between-ledger-and-trades-history#breadcrumb"}}]}
{"@context":"https://schema.org","@graph":[{"@type":"Article","headline":"Differences between ledger and trades history","articleBody":"—  Ledger history \n\nLedger history focuses on changes to account balances.It answers questions like:\n—  Working with Ledger history: \n\n—  Trades history \n\nTrades history focuses on the execution details of spot transactions (the matching of sell orders with buy orders and vice versa) with or without the use of margin.It answers questions like:\n— Example: the same trade in each view\n\nSuppose you buy 0.05 BTC with EUR at a price of €60,000 per BTC (total cost €3,000.00, fee €7.80). Here is how that single transaction appears in each type of history:Ledger history — two entries (one per currency), linked by the same refid:","datePublished":"2026-08-24T00:00:00.000Z","wordCount":165,"timeRequired":"PT1M"}]}
```