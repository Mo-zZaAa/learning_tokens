---
url: https://support.kraken.com/articles/115000364388-trading-glossary
title: Trading glossary | Kraken
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
3. [Kraken Pro](/sections/4402371086484-general)
4. [Getting started with Kraken Pro](/sections/200560573-introduction-to-trading-on-kraken)

# Trading glossary

Last updated: August 24, 2026

### Assets

Cryptocurrency

A [cryptocurrency](/articles/360000673023) is a digital asset designed to facilitate peer-to-peer financial transactions and smart contracts on the internet in a decentralized manner.

Fiat currency

A [fiat currency](/articles/360000380726) has no intrinsic value and is established as legal tender by a government. Examples include the US Dollar (USD) and Euro (EUR).

### Markets

Currency pair (market)

In order to trade one currency for another, there must be [a market (also known as a "currency pair") linking both currencies](/articles/201893658). In a currency pair, [the price indicates how much of the quote currency is required to buy one unit of the base currency](/articles/203053186). For example, a price of 1,000 USD for BTC/USD means that 1,000 USD is required to purchase 1 BTC.

Base currency

The first currency in a currency pair is called the base currency. For example, in the currency pair BTC/USD, BTC is the base currency.

Quote currency

The second currency in a currency pair is called the quote currency. For example, in the currency pair BTC/USD, USD is the quote currency.

### Order options

Minimum order size

Each tradable currency on Kraken has its own [minimum order size](/articles/205893708). An order placed with a volume below the minimum order size will be rejected.

Limit order type

A [limit order](/articles/203325783) will buy (or sell) at a [pre-specified price](/articles/206899287) or better. A limit order can be maker or taker depending on whether it crosses the order book or not.

Market order type

A [market order](/articles/203325783) will buy (or sell) at the best average market price. All market orders are takers.

Maker

A maker (not to be confused with a market order) is a limit order that is **not** immediately matched or filled with an existing order on the order book. Makers add liquidity to the order book.

Taker

A taker is a market or limit order that is immediately matched or filled with an existing order on the order book. Takers remove liquidity from the order book.

Stop loss order type

A [stop loss order](/articles/203325793) is typically used as a closing order to limit your losses or lock in your profits on a long or short position. But it can also be used to open a position.

Take profit order type

A [take profit order](/articles/203053226) can be used to set a target profit price on a long or short position. The profit price can be set in terms of absolute price or as a percentage. As with stop orders, take profit orders can also be used to open positions.

### Order statuses

Open order

Open orders can either be “touched” or “untouched”. An "untouched" open order is an unfilled order. A "touched" open order is an order that is partially, but not completely, filled.

Triggered order

[그림: Trading\_TriggeredStopLossLimitOrder\_09092021.png]

When a [stop loss limit](/articles/360029115592)’s stop price or [take profit limit](/articles/360029116112)’s profit price has been met and the order becomes active, the order will be in the new and open order section with the status of ‘triggered’ until the volume is filled or the order is cancelled by the client.

[그림: Terminal\_TriggeredStopLossLimitOrder\_10072020.png]

On Kraken Terminal, the order will be visible in the Orders section with both prices visible.

When trading using the API, you will not see a ‘Triggered’ status. The misc flag would be either ‘stopped’ for stop loss or ’touched' for take profit.

Filled order

An order can be "partially" or "fully" filled. To fill a buy or sell order is to match it with one or more orders of the opposing type. Buy orders are filled by matching with sell orders; sell orders are filled by matching with buy orders.

Closed order

A completely filled order will be listed as "closed".

Cancelled order

A [cancelled order](/articles/235162907) is an order that has been withdrawn from the order book without being fully filled. A cancelled order will either be untouched or partially filled.

### Order books

Order book

The order book is a list of unfilled buy and sell limit orders. It is used by an exchange to fill market orders at the best available price.

Kraken operates a Central Limit Order Book (CLOB) model, where orders are matched based on Price/Time priority.

Here's an example:

To view the Order Book, sign in to your Kraken account and navigate to the [Trade tab](https://www.kraken.com/u/trade#tab=new-order). Under the **New Orders** tab, you can click on **Order Book**.

Slippage

Slippage is the difference between the price that a trade is expected to cost and the actual price when the trade executes. This can be caused by a market order being placed and the price changing in the time between the order being created and executed. It will also happen when an order is large enough that it is split between many trades in the order book. To protect you from large slippages, we offer a [Fat Finger warning](/articles/360036553832) when filling an order form or a confirmation window with the guaranteed price when using [Instant Buy](/articles/360046777031). For example, using the above image of an order book, if someone placed a market buy of 1.645 BTC, the market price would display as €3,155.6; however, the average price paid would be €3,156.96.

[그림: Trading\_SlippageExample\_02052021.png]

Ask

An order listed on the sell side of the order book.

Bid

An order listed on the buy side of the order book.

Bid/Ask depth

The Bid/Ask Depth represents the cumulative volume of buy and sell orders at a particular price. The bid depth at a given price is the cumulative volume of current buy orders on the book at that price or higher, while the ask depth at a given price is the cumulative volume of current sell orders on the book at that price or lower.

Bid/Ask spread

The difference in price between the highest bid and the lowest ask on the order book.

The bid/ask spread chart available for Kraken markets only shows the spread between the highest limit buy order and the lowest limit sell order (plotted over time). A market order will fill in this gap if there are matching market orders of the opposing type sufficient to fill it. Otherwise, it will fill, at least in part, using limit orders of the opposing type.

Here's an example from the BTC/USD market:

[그림: Trading\_SpreadAndBidsAsks\_04272021.gif]

See: [kraken.com/prices/orderbook](https://www.kraken.com/prices/orderbook)

Depth chart

A visual representation of the demand and supply at different price levels. The bid/ask depth available for Kraken markets only shows the bid and ask depth of limit orders on the order book.

Here's an example from the BTC/USD market:

[그림: Trading\_DepthCharts\_04272021.gif]

See: [kraken.com/prices/orderbook](https://www.kraken.com/prices/orderbook)

Liquidity

A term that describes the amount of activity on a market. High liquidity means a high volume of activity in a market where lots of parties are willing to take the other side of a trade.

Volatility

A market’s volatility is its likelihood of showing rapid and unpredictable price movements.

### Margin Trading

Collateral currency

A sufficient balance in one or more collateral currencies is required to trade using margin.

Leverage

Leverage allows you to place trades in larger amounts than what you have in your trade balance.

For example, a trade balance of 10,000 USD increases your buying power to 50,000 USD when trading using margin and using 5x leverage.

Margin

Availability of margin trading services is subject to certain limitations and eligibility criteria.

When trading using margin, you are using Kraken’s funds to place orders, as opposed to directly using the funds deposited or held in your account.

To open a spot position on margin, you need to select a leverage between 2x and 5x from the Intermediate or Advanced order tab when creating a New Order.

Margin allowance limits

Margin allowance limits determine the maximum amount of margin that Kraken will extend to you in an order for a particular currency. Each currency allowance limit is independent of the others.

[Not all currency pairs on Kraken can be traded using margin.](/articles/227876608) [Availability of margin trading services is subject to certain limitations and eligibility criteria.](/articles/4402532394260)

*The decimal and thousands separators shown in this article may differ from the formats displayed on our trading platforms. Review our article on how we use points and commas for more information.* :)

[Assets](#85a-assets)[Markets](#419-markets)[Order options](#e5f-order-options)[Order statuses](#c1b-order-statuses)[Order books](#c0b-order-books)[Margin Trading](#94f-margin-trading)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"WebSite","url":"https://kraken.com","description":"Buy, sell, trade and learn about crypto on Kraken — the simple, powerful crypto platform that grows with you.","potentialAction":{"@type":"RegisterAction","target":"https://www.kraken.com/sign-up"},"publisher":{"@context":"https://schema.org","@type":"Organization","name":"Kraken","alternateName":"Kraken Exchange","url":"https://www.kraken.com/","logo":{"@type":"ImageObject","@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","url":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","contentUrl":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","width":900,"height":900,"caption":"Kraken"},"image":{"@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg"},"sameAs":["https://www.facebook.com/KrakenFX","https://twitter.com/krakenfx","https://www.youtube.com/@KrakenCryptoExchange","https://en.wikipedia.org/wiki/Kraken_(company)","https://www.linkedin.com/company/krakenfx","https://www.instagram.com/krakenfx/","https://www.reddit.com/r/Kraken","https://apps.apple.com/us/app/kraken-buy-crypto-bitcoin/id1481947260","https://play.google.com/store/apps/details?id=com.kraken.invest.app&hl=en_US"],"contactPoint":{"@type":"ContactPoint","url":"https://support.kraken.com/hc/en-us/forms","contactType":"Customer Service"},"address":{"@type":"PostalAddress","streetAddress":"237 Kearny St #102","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94108","addressCountry":"US"}}},{"@type":"BreadcrumbList","@id":"https://support.kraken.com/articles/115000364388-trading-glossary#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://support.kraken.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://support.kraken.com/articles"},{"@type":"ListItem","position":3,"name":"115000364388 Trading Glossary","item":"https://support.kraken.com/articles/115000364388-trading-glossary"}]},{"@type":"WebPage","@id":"https://support.kraken.com/articles/115000364388-trading-glossary#webpage","url":"https://support.kraken.com/articles/115000364388-trading-glossary","name":"Trading glossary | Kraken","description":"Support Center for Kraken.com | Bitcoin & Cryptocurrency Exchange | Bitcoin Trading Platform","isPartOf":{"@id":"https://support.kraken.com/#website"},"publisher":{"@id":"https://support.kraken.com/#organization"},"breadcrumb":{"@id":"https://support.kraken.com/articles/115000364388-trading-glossary#breadcrumb"}}]}
{"@context":"https://schema.org","@graph":[{"@type":"Article","headline":"Trading glossary","articleBody":"—  Assets \n\n—  Markets \n\n—  Order options \n\n—  Order statuses \n\n—  Order books \n\n—  Margin Trading","datePublished":"2026-08-24T00:00:00.000Z","wordCount":55,"timeRequired":"PT1M"}]}
```