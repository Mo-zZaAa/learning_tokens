---
url: https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq
title: Corporate Actions on xStocks Perpetual Futures FAQ
description: 
fetched: 2026-11-16
method: render
plan: read
---

Ask AI

All

Filter by:

All Products

How do I deposit cash into my account?

I need help with account verification

Why can't I access my account?

Are there any crypto withdrawal fees?

I need help signing into my account

1. [Support](https://support.kraken.com/)

# Corporate Actions on xStocks Perpetual Futures FAQ

Last updated: August 18, 2026

Kraken Futures offers perpetual futures contracts on xStocks assets. Some of the underlying assets may be subject to corporate actions, which will impact the derivatives markets based on those assets.

### What are corporate actions and how do they apply to xStocks perpetual positions?

Corporate actions (CAs) are events on the underlying stock that affect its economic value or share structure, such as cash dividends, splits, and reverse splits. For xStocks perpetuals, CAs fall into two categories:

* **Cashflow events** (e.g. cash dividends), which pay out economic value without changing position size. We realize this economic value via a discrete funding rate payment.
* **Structural events** (e.g. splits, reverse splits), which change the number of shares each contract represents. We realize this change by adjusting positions and orders in real time.

Each category is applied automatically, so positions and orders keep tracking the underlying stock without requiring any action from clients.

### What is the ex-date?

The ex-date is the effective time at which a corporate action takes effect. It's the point from which the CA's impact is applied (e.g. a funding payment for cashflow events, or a position/order rescale for structural events).

### How are cashflow events applied to xStocks perpetual positions?

To capture the economic value of the cashflow event (cash dividend, bonus), the cashflow event is realized as a discrete funding rate payment—that is, a payment from short position holders to long position holders at the time of the cashflow event ex-date. The unrealized funding at the time of the cashflow event is unaffected; it will be realized at the normal cadence at the top of the hour or when there is an update to the position (whichever comes first). There is no adjustment to the position size in cashflow events.

### Who pays for the cashflow events?

The cashflow events are paid in a discrete funding payment by the short position holder.

### Is there a liquidation risk for short position holders if the cashflow event is larger than the required margin?

Yes. Although the likelihood is smaller, it is possible that a cashflow event can trigger a liquidation. Position holders should ensure their positions are sufficiently collateralized.

### How are structural events applied to xStocks perpetual positions?

When there is a structural event such as a split or reverse split, the impacted market will enter post-only mode a second before the ex-date, after which no liquidations or executions can occur. Positions will be adjusted by the multiplier value, including size and average entry price. Resting orders and trigger orders will be adjusted by the multiplier, including size and price. Once the positions and orders are adjusted and the adjusted index and mark price are updated, post-only will be removed and trading will resume.

### Can I place orders during the post-only period during a structural event?

No. Orders placed during post-only will be rejected, and only orders placed before the market enters post-only will be adjusted. The queue of resting orders prior to the ex-date will be preserved as they were prior to the post-only period.

### What are the risks surrounding structural events?

The goal of a structural event is to resize the positions and orders while preserving the economic value of the positions. If, for some reason, the resizing of the positions and orders is unsuccessful, the market will remain in post-only until the resizing can be resolved. The market will only go live once all positions are resized according to the split. In an extreme scenario where a split is unsuccessful, Kraken Derivatives reserves the right to settle and relist a contract.

### What about corporate actions on xStocks as collateral?

For collateral, see [Corporate Actions with xStocks on Kraken](https://support.kraken.com/articles/corporate-actions-xstocks-kraken-app).

[What are corporate actions and how do they apply to xStocks perpetual positions?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[What is the ex-date?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[How are cashflow events applied to xStocks perpetual positions?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[Who pays for the cashflow events?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[Is there a liquidation risk for short position holders if the cashflow event is larger than the required margin?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[How are structural events applied to xStocks perpetual positions?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[Can I place orders during the post-only period during a structural event?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[What are the risks surrounding structural events?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)[What about corporate actions on xStocks as collateral?](https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq)

## Contact us

[Sign in to contact us](https://id.kraken.com/sign-in)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"WebSite","url":"https://kraken.com","description":"Buy, sell, trade and learn about crypto on Kraken — the simple, powerful crypto platform that grows with you.","potentialAction":{"@type":"RegisterAction","target":"https://www.kraken.com/sign-up"},"publisher":{"@context":"https://schema.org","@type":"Organization","name":"Kraken","alternateName":"Kraken Exchange","url":"https://www.kraken.com/","logo":{"@type":"ImageObject","@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","url":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","contentUrl":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","width":900,"height":900,"caption":"Kraken"},"image":{"@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg"},"sameAs":["https://www.facebook.com/KrakenFX","https://twitter.com/krakenfx","https://www.youtube.com/@KrakenCryptoExchange","https://en.wikipedia.org/wiki/Kraken_(company)","https://www.linkedin.com/company/krakenfx","https://www.instagram.com/krakenfx/","https://www.reddit.com/r/Kraken","https://apps.apple.com/us/app/kraken-buy-crypto-bitcoin/id1481947260","https://play.google.com/store/apps/details?id=com.kraken.invest.app&hl=en_US"],"contactPoint":{"@type":"ContactPoint","url":"https://support.kraken.com/hc/en-us/forms","contactType":"Customer Service"},"address":{"@type":"PostalAddress","streetAddress":"237 Kearny St #102","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94108","addressCountry":"US"}}},{"@type":"BreadcrumbList","@id":"https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://support.kraken.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://support.kraken.com/articles"},{"@type":"ListItem","position":3,"name":"Corporate Actions Xstocks Perpetual Futures Faq","item":"https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq"}]},{"@type":"WebPage","@id":"https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq#webpage","url":"https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq","name":"Corporate Actions on xStocks Perpetual Futures FAQ","isPartOf":{"@id":"https://support.kraken.com/#website"},"publisher":{"@id":"https://support.kraken.com/#organization"},"breadcrumb":{"@id":"https://support.kraken.com/articles/corporate-actions-xstocks-perpetual-futures-faq#breadcrumb"}}]}
{"@context":"https://schema.org","@graph":[{"@type":"Article","headline":"Corporate Actions on xStocks Perpetual Futures FAQ","articleBody":"— What are corporate actions and how do they apply to xStocks perpetual positions?\n\nCorporate actions (CAs) are events on the underlying stock that affect its economic value or share structure, such as cash dividends, splits, and reverse splits. For xStocks perpetuals, CAs fall into two categories:\n\n• Cashflow events (e.g. cash dividends), which pay out economic value without changing position size. We realize this economic value via a discrete funding rate payment.\n• Structural events (e.g. splits, reverse splits), which change the number of shares each contract represents. We realize this change by adjusting positions and orders in real time.\n\nEach category is applied automatically, so positions and orders keep tracking the underlying stock without requiring any action from clients.\n\n— What is the ex-date?\n\nThe ex-date is the effective time at which a corporate action takes effect. It's the point from which the CA's impact is applied (e.g. a funding payment for cashflow events, or a position/order rescale for structural events).\n\n— How are cashflow events applied to xStocks perpetual positions?\n\nTo capture the economic value of the cashflow event (cash dividend, bonus), the cashflow event is realized as a discrete funding rate payment—that is, a payment from short position holders to long position holders at the time of the cashflow event ex-date. The unrealized funding at the time of the cashflow event is unaffected; it will be realized at the normal cadence at the top of the hour or when there is an update to the position (whichever comes first). There is no adjustment to the position size in cashflow events.\n\n— Who pays for the cashflow events?\n\nThe cashflow events are paid in a discrete funding payment by the short position holder.\n\n— Is there a liquidation risk for short position holders if the cashflow event is larger than the required margin?\n\nYes. Although the likelihood is smaller, it is possible that a cashflow event can trigger a liquidation. Position holders should ensure their positions are sufficiently collateralized.\n\n— How are structural events applied to xStocks perpetual positions?\n\nWhen there is a structural event such as a split or reverse split, the impacted market will enter post-only mode a second before the ex-date, after which no liquidations or executions can occur. Positions will be adjusted by the multiplier value, including size and average entry price. Resting orders and trigger orders will be adjusted by the multiplier, including size and price. Once the positions and orders are adjusted and the adjusted index and mark price are updated, post-only will be removed and trading will resume.\n\n— Can I place orders during the post-only period during a structural event?\n\nNo. Orders placed during post-only will be rejected, and only orders placed before the market enters post-only will be adjusted. The queue of resting orders prior to the ex-date will be preserved as they were prior to the post-only period.\n\n— What are the risks surrounding structural events?\n\nThe goal of a structural event is to resize the positions and orders while preserving the economic value of the positions. If, for some reason, the resizing of the positions and orders is unsuccessful, the market will remain in post-only until the resizing can be resolved. The market will only go live once all positions are resized according to the split. In an extreme scenario where a split is unsuccessful, Kraken Derivatives reserves the right to settle and relist a contract.\n\n— What about corporate actions on xStocks as collateral?\n\nFor collateral, see Corporate Actions with xStocks on Kraken.","datePublished":"2026-08-18T00:00:00.000Z","wordCount":610,"timeRequired":"PT4M"}]}
```