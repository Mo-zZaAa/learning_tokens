---
url: https://www.kraken.com/features/api-trading
title: Kraken API | REST, WebSocket and FIX APIs
description: Trade spot, futures and margin via Kraken's REST, WebSocket and FIX APIs.
fetched: 2026-11-16
method: render
plan: read
---

# 

Trade algorithmically on Kraken

Build and trade on the APIs that traders, developers, and institutions have trusted since 2011

[Create your API keys](https://pro.kraken.com/app/settings/api)[View API documentation](https://docs.kraken.com/api)

[그림: Decorative bg]

$2T+

Annual transaction volume

640+

Crypto assets

< 1ms

Latency

99.9%

Uptime

## Automate your first trade in minutes

Connect to every Kraken market through dedicated REST, WebSocket
and FIX API built for reliable and ultra-low-latency execution

FIX API

A standardized messaging protocol trusted by institutional traders worldwide, Kraken's FIX API gives you direct, low-latency access to both spot and derivatives markets.

EXAMPLE - NEW ORDER SINGLE

8=FIX.4.49=14035=D34=249=MYCOMPID52=20230707-13:56:08.00056=KRAKEN-TRD11=168873816838=0.0140=244=100054=155=BTC/USD59=160=20230707-13:56:08.27710=222

Websocket API

Real-time, two-way market data and order updates over a persistent connection — eliminating the overhead of continuous polling.

EXAMPLE - ADD ORDER

```
{
 "method": "add_order",
 "params": {
  "order_type": "limit",
  "side": "buy",
  "limit_price": 26500.4,
  "order_userref": 100054,
  "order_qty": 1.2,
  "symbol": "BTC/USD",
  "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
  "req_id": 123456789
  }
}
```

REST API

A reliable HTTP interface for request-response trading workflows — synchronous access to market data, orders, and account management from any language or platform.

EXAMPLE - ADD ORDER

```
curl -L 'https://api.kraken.com/0/private/AddOrder' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'API-Key: <API-Key>' \
-H 'API-Sign: <API-Sign>' \
-d '{
 "nonce": 163245617,
 "ordertype": "limit",
 "type": "buy",
 "volume": "1.25",
 "pair": "XBTUSD",
 "price": "27500",
 "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876"
}'
```

## Exchange trading APIs

Spot

Trade any strategy across 640+ assets with full L3 depth, advanced order types, batch orders and subaccount support.

[그림: Spot trading API]

Margin

Long and short spot exposure with leverage, through the same API keys as spot.

[그림: Margin trading API]

Futures

Run and automate leveraged strategies with full position management, PnL controls and historical data for model development.

[그림: Futures trading API]

[Create your API Keys](https://pro.kraken.com/app/settings/api)

Market data APIs

Order book data

L1, L2 and L3 depth with OrderIDs and microsecond timestamps across spot markets. Built for queue priority analysis, fill probability modelling and microstructure research

[그림: Order book data API]

Trades and price history

Real-time trade ticks and historical OHLCV across multiple intervals for backtesting and signal development

[그림: Trades and price history API]

Ticker and instruments

Best bid and ask, 24-hour stats and instrument reference data updated in real-time.

[그림: Ticker and instruments API]

[View market data documentation](https://docs.kraken.com/exchange/guides/general/l3-data)

## Institutional APIs

[그림: Prime logo] 

Dedicated FIX and WebSocket connectivity for high-volume and segregated order flow across 20+ liquidity providers.

[Learn more](https://docs.kraken.com/api/docs/prime-api/fix/nos-fix)

 [그림: Prime]

[그림: OTC logo] 

Execute large block trades off the public order book with custom pricing via Kraken OTC quote request and execution API.

[Learn more](https://docs.kraken.com/api/docs/otc-api/create-otc-quote-request)

 [그림: OTC trading API]

[그림: Custody logo] 

Secure digital assets with institutional-grade storage and compliance.

[Learn more](https://docs.kraken.com/api/docs/custody-api/list-custody-vaults)

 [그림: Custody API]

[Contact for Institutional API access](https://www.kraken.com/institutions/exchange)

[그림: Kraken API Partner logo] 

Enable crypto and xStocks spot and futures trading through Kraken APIs and earn lifetime commissions

[Apply to the API Partner Program](https://www.kraken.com/institutions/api-partner)

Up to 50% lifetime commission

Earn lifetime commissions reflecting the value your platform delivers to clients through Kraken's infrastructure

Multi-asset trading

Spot, futures and tokenized equities via xStocks. Give your users a complete trading experience backed by deep liquidity.

Strategic growth support

Joint campaigns and co-branded initiatives to accelerate partner growth

Partner dashboard

A real-time partner dashboard for tracking performance and paid commissions.

[그림: API Partner]

## Everything you need to build with Kraken API

From your first API call to advanced trading setup, guides and walkthroughs built for every stage.

[[그림: API Unlocked]](https://blog.kraken.com/product/api/beeks-colocation-one-year)

[### A year of colocation with Beeks: open access to low-latency trading](https://blog.kraken.com/product/api/beeks-colocation-one-year)April 30, 2026

[[그림: API Unlocked]](https://blog.kraken.com/product/api/unlocked-4-fix-4-4-institutional-connectivity)

[### Kraken API Unlocked: FIX 4.4 — institutional connectivity on Kraken](https://blog.kraken.com/product/api/unlocked-4-fix-4-4-institutional-connectivity)April 29, 2026

[[그림: API Unlocked]](https://blog.kraken.com/product/api/unlocked-3-the-market-data-feeds-systematic-traders-use)

[### Kraken API Unlocked — the market data feeds systematic traders use on Kraken](https://blog.kraken.com/product/api/unlocked-3-the-market-data-feeds-systematic-traders-use)April 23, 2026

[[그림: API Unlocked]](https://blog.kraken.com/product/api/unlocked-2-momentum-strategies)

[### Kraken API Unlocked: momentum strategies on Kraken](https://blog.kraken.com/product/api/unlocked-2-momentum-strategies)April 16, 2026

[[그림: API Unlocked]](https://blog.kraken.com/product/api/unlocked-1-strategies-infrastructure-and-where-to-start)

[### Kraken API Unlocked: automated crypto trading on Kraken — strategies, infrastructure and where to start](https://blog.kraken.com/product/api/unlocked-1-strategies-infrastructure-and-where-to-start)April 9, 2026

[[그림: API Unlocked]](https://blog.kraken.com/product/new-features/liquidity-connect-colocation)

[### Announcing colocation access via Liquidity Connect](https://blog.kraken.com/product/new-features/liquidity-connect-colocation)April 8, 2026

## Start building with Kraken API

Trusted by traders, developers and institutions since 2011.
Create your API key, make your first authenticated request, and start building.

[Create your API keys](https://pro.kraken.com/app/settings/api)[View API documentation](https://docs.kraken.com/api)

Trading derivatives and other financial instruments, including leveraged financial instruments, involves significant risks and is not appropriate for all investors. See our [Risk Disclosure](https://support.kraken.com/articles/360022629052-risk-disclosure-derivatives-disclaimers) to learn more.

OTC services, including spot trading, derivatives, and lending, are offered by Payward Oceanic Ltd., a member of the Kraken Group. These products are available only to eligible clients and may not be offered in all jurisdictions. OTC transactions involve risk and may result in the loss of capital. This communication is for informational purposes only and does not constitute investment, legal, or tax advice. Availability is subject to applicable laws and regulatory requirements.

Custody services are provided by Payward Financial, Inc. or Payward Europe Solutions, Ltd, as applicable. Payward Financial, Inc. d/b/a Kraken Financial is not an FDIC-insured bank and deposits are neither insured by nor subject to the protections of the FDIC. Payward Europe Solutions Limited, trading as Kraken, is regulated by the Central Bank of Ireland.

Trading on margin involves significant risk and may not be suitable for all investors. You could lose more than your initial investment. Spot margin trading products are offered by Payward Trading Ltd, incorporated in the British Virgin Islands (BVI). This content is for informational purposes only and does not constitute financial or investment advice. Product availability may vary by jurisdiction. Please ensure you fully understand the risks involved before trading. Past performance is not indicative of future results.

xStocks are issued by Backed Assets (JE) Limited (a Jersey private limited company) and offered to eligible Kraken customers via Payward Digital Solutions Ltd. (“PDSL”), a company licensed to conduct digital asset business by the Bermuda Monetary Authority. xStocks are not nor will be registered with any local securities regulators. PDSL (Kraken) does not provide investment advice and/or recommendations, and, no communication, through any Kraken App or website or otherwise, should be construed as such. Individual investors should make their own decisions or seek professional independent advice if they are unsure as to the suitability / appropriateness of any investment for their circumstances or needs, including potential tax treatment. Investing in xStocks involves an element of risk. The value of an investment may go down as well as up, and past performance is not a reliable indicator of future results. Not available in the U.S. or to U.S. persons. Geo restrictions apply. Read Kraken’s xStocks Risk Disclosure at kraken.com/legal/xstocks as well as the Base Prospectus and related Final Terms for xStocks at <https://assets.backed.fi/legal-documentation> to learn more.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://www.payward.com/#organization","name":"Payward","legalName":"Payward, Inc.","url":"https://www.payward.com/","description":"Payward, Inc. is the parent company behind Kraken and a portfolio of financial-infrastructure businesses spanning trading, custody, payments, lending, onchain finance, and benchmarks.","foundingDate":"2011","subOrganization":{"@id":"https://www.kraken.com/#organization"}},{"@type":["Organization","FinancialService"],"@id":"https://www.kraken.com/#organization","name":"Kraken","url":"https://www.kraken.com/","parentOrganization":{"@id":"https://www.payward.com/#organization"}},{"@type":["Organization","FinancialService"],"@id":"https://pro.kraken.com/#organization","name":"Kraken Pro","url":"https://pro.kraken.com/","description":"Kraken Pro is the advanced cryptocurrency trading platform from Kraken, built for active and professional traders. It brings spot, margin, and futures trading, plus tokenized equities and prop trading, into one consolidated interface with advanced order types, deep liquidity, and programmatic API access.","slogan":"Your all-in command center for trading","parentOrganization":{"@id":"https://www.kraken.com/#organization"},"brand":{"@id":"https://pro.kraken.com/#brand"},"logo":{"@type":"ImageObject","@id":"https://pro.kraken.com/#logo","url":"https://assets-cms.kraken.com/images/51n36hrp/facade/4074096e54aec7c3d3dbd71b24f24b58b324cfb5-900x900.png","contentUrl":"https://assets-cms.kraken.com/images/51n36hrp/facade/4074096e54aec7c3d3dbd71b24f24b58b324cfb5-900x900.png","width":900,"height":900,"caption":"Kraken Pro"},"image":{"@id":"https://pro.kraken.com/#logo"},"knowsAbout":["Cryptocurrency spot trading","Crypto margin trading","Crypto futures trading","Perpetual futures","Tokenized equities","Proprietary (prop) trading","Advanced order types","Trading APIs"],"areaServed":"Worldwide","sameAs":["https://x.com/krakenpro","https://t.me/krakenproofficial"]},{"@type":"Brand","@id":"https://pro.kraken.com/#brand","name":"Kraken Pro","url":"https://pro.kraken.com/","slogan":"Your all-in command center for trading","logo":{"@id":"https://pro.kraken.com/#logo"},"description":"Kraken Pro is Kraken's advanced trading brand for active and professional crypto traders."},{"@type":"WebApplication","@id":"https://pro.kraken.com/#app","name":"Kraken Pro","url":"https://pro.kraken.com/","applicationCategory":"FinanceApplication","operatingSystem":"Web, Windows, macOS, iOS, Android","publisher":{"@id":"https://pro.kraken.com/#organization"},"brand":{"@id":"https://pro.kraken.com/#brand"},"description":"The Kraken Pro trading platform for spot, margin, and futures, with a consolidated portfolio, advanced order types, and REST, FIX, and WebSocket APIs.","featureList":["Spot trading across 1,400+ crypto pairs","Margin trading with up to 10x leverage on 48+ assets","Perpetual futures with 24/7 markets","Advanced order types: limit, stop, stop-limit, OCO, post-only","REST, FIX, and WebSocket APIs for programmatic strategies","Consolidated portfolio across spot, margin, futures, and staking"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free to create an account. Trading incurs maker-taker fees that decrease with 30-day volume."}},{"@type":"WebSite","@id":"https://pro.kraken.com/#website","url":"https://pro.kraken.com/","name":"Kraken Pro","description":"Advanced cryptocurrency trading platform for active and professional traders. Trade spot, margin, and futures in one place.","publisher":{"@id":"https://pro.kraken.com/#organization"},"inLanguage":"en","potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://pro.kraken.com/search?q={query}"},"query":"required"}},{"@type":"BreadcrumbList","@id":"https://www.kraken.com/pro/trading-api#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://www.kraken.com/"},{"@type":"ListItem","position":2,"name":"Pro","item":"https://www.kraken.com/pro"},{"@type":"ListItem","position":3,"name":"Trading Api","item":"https://www.kraken.com/pro/trading-api"}]},{"@type":"WebPage","@id":"https://www.kraken.com/pro/trading-api#webpage","url":"https://www.kraken.com/pro/trading-api","name":"Kraken API | REST, WebSocket and FIX APIs","description":"Trade spot, futures and margin via Kraken's REST, WebSocket and FIX APIs.","isPartOf":{"@id":"https://www.kraken.com/#website"},"publisher":{"@id":"https://www.kraken.com/#organization"},"breadcrumb":{"@id":"https://www.kraken.com/pro/trading-api#breadcrumb"}}]}
```