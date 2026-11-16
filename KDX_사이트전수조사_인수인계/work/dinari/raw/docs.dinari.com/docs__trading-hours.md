---
url: https://docs.dinari.com/docs/trading-hours
title: Trading Hours
description: Information about Dinari trading hours and the differences in trading sessions.
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

# Trading Hours

Information about Dinari trading hours and the differences in trading sessions.

# Dinari Trading Sessions Overview

dShares™ are backed 1:1 by real stock and are traded in real-time on the U.S. stock markets including the New York Stock Exchange (NYSE), the NASDAQ and other exchanges. In addition to regular trading sessions on these exchanges, Dinari also operates on the extended, overnight and weekend/open sessions.

While Dinari generally abstracts these trading sessions away with our APIs and smart contracts, it's important to understand the differences with how orders are placed and the varying amount of available liquidity.

---

## Sessions Overview

Dinari operates across four distinct trading sessions. The accepted order types and available liquidity vary by session, so it's important to know which session is active when placing trades.

Regular

**9:30 a.m. - 4:00 p.m. (ET)**

🛒 Market & Limit.  
  
🗒️ *Primary session; best prices and liquidity*

Extended

**Pre-market 4:00 a.m. - 9:30 a.m. (ET)**  
**After-hours 4:00 p.m. - 8:00 p.m. (ET)**  
  
🛒 Limit only\*  
  
🗒️ *Opens only if the market is open the following day (e.g., if Monday is a holiday, Sunday's Overnight session does not open)*

Overnight

**8:00 p.m. (T-1) – 4:00 a.m., weekdays (starts Sunday 8:00 p.m.)**

🛒 Limit only\*  
  
🗒️ *Opens only if the market is open the following day (e.g., if Monday is a holiday, Sunday's Overnight session does not open)*

Open (24/7)

**Friday 8:00 p.m. – Sunday 8:00 p.m., and when all other trading sessions are closed**

🛒 Limit only\*, blockchain only

🗒️Limited tickers; lower liquidity

  

**💡 Key Takeaway**

* **Regular Session:** Market and limit orders are accepted.
* **Extended, Overnight, and Open (24/7) Sessions:** Only limit orders are accepted directly. Market orders placed during these sessions are automatically converted to marketable limit orders (see note below).

**🛠️ \* About Market Orders Outside the Regular Session**

Market orders placed outside the Regular session are **not** rejected. Dinari automatically converts them into marketable limit orders:

* **Market Buys** are priced at the latest **ASK** price
* **Market Sells** are priced at the latest **BID** price

Because the converted order functions as a limit order, it may fill **fully, partially, or not at all.** Any unfilled remainder is refunded.

> **💡 Best Practice:** To ensure predictable execution outside Regular hours, submit limit orders with an explicit limit price.

  

---

## Session Details

### Regular Trading Session

The primary trading period for U.S. stock markets, running most weekdays from 9:30 a.m. to 4:00 p.m. ET. All order types are accepted, with the best prices and liquidity available.

### Extended Hours Trading Session

Includes both pre-market (4:00–9:30 a.m. ET) and after-hours (4:00–8:00 p.m. ET) trading. These sessions are only active when there is a Regular trading session the same day. Liquidity is lower and volatility may be higher. Only limit orders are accepted.

### Overnight Trading Session

Runs from 8:00 p.m. (ET, T-1) to 4:00 a.m. (ET) on weekdays, starting at 8:00 p.m. on Sunday. This session opens **only if the market is open the following day.** For example, if Monday is a holiday, the Overnight session will not open on Sunday evening. Trades in this session are booked in the following trading session. Only limit orders are accepted.

### Open (24/7) Trading Session

Runs from 8:00 p.m. (ET) on Friday to 8:00 p.m. (ET) on Sunday, and also opens when all other trading sessions are closed. This session operates on the blockchain only and covers a limited number of tickers with lower liquidity. Only limit orders are accepted.

  

---

## Holidays

  

### Market Holidays

Dinari trading is affected by U.S. stock market holidays. On these days, the Regular, Extended, and Open (24/7) sessions are closed.

For the most up-to-date information, use the **Get Market Hours API:**  
  
`GET /api/v2/market_data/market_hours/`  
  
You may also refer to:

* [NYSE Calendar](https://www.nyse.com/markets/hours-calendars)
* [NASDAQ Calendar](https://www.nasdaqtrader.com/trader.aspx?id=Calendar)

  

### Bank Holidays

Dinari is also affected by U.S. bank holidays, which usually coincide with market holidays but not always. While Dinari attempts to mitigate the impact, large transactions may settle on a T+2 basis on these days.

  

---

### Common Scenarios

**Scenario 1: Market order during Regular hours**

| Aspect | What Happens |
| --- | --- |
| Execution | Executes quickly at the prevailing market place |
| Timing | dShares appear in wallet within 30 minutes |
| Status | **SUBMITTED → FILLED** |

**Scenario 2: Market order during Extended/Overnight/Weekend hours**

| Aspect | What Happens |
| --- | --- |
| Execution | Converted to a marketable limit order |
| Possible outcomes | Fills fully, partially, or not at all; may remain pending until next Regular session |
| Status | May show **SUBMITTED** to extended periods; may eventually be **CANCELLED** |

**Scenario 3: Order shows SUBMITTED for a long time**

| Aspect | What Happens |
| --- | --- |
| What it means | Order is on the order book waiting to be filled |
| Is this normal? | Yes, especially during off-hours sessions |
| When to act | If still **SUBMITTED** after the Regular session opens, contact support |

  

**Scenario 4: Order was cancelled**  
 **Common reasons:**

1. Market order placed off-hours and implied limit price wasn't reached
2. Limit order didn't fill and expired (**TIF** = **DAY**)
3. You cancelled it manually
4. The asset was non-fractionable (limit orders only)

**How to check:** Use List Order Requests endpoint to see the cancel\_message for the specific reason.

  

**Scenario 5: Order shows PARTIALLY\_FILLED**

| Aspect | What Happens |
| --- | --- |
| What it means | Only part of your order executed |
| Is this normal? | Yes. Orders can have multiple fulfillments depending on market conditions |
| What happens next | Remaining portion stays on the order book |
| Can you cancel? | Yes. **PARTIALLY\_FILLED** orders can be cancelled |

  

**Scenario 6: Cancellation attempt doesn't work**

Orders that cannot be cancelled:

* PENDING\_FILL
* PENDING\_ESCROW
* FILLED
* REJECTED
* CANCELLED

**Important:** Order cancellation is not guaranteed and is not immediate. The order may still execute if the cancellation request doesn't reach the order book in time. Always confirm using Get Order by ID.

# NYSE Holidays & Trading Hours: 2026 and 2027

*Source: [NYSE Holidays & Trading Hours](https://www.nyse.com/trade/hours-calendars). All NYSE markets observe the U.S. holidays listed below. All times are Eastern Time (ET).*

## Market Holidays (Full Closures)

| Holiday | 2026 | 2027 |
| --- | --- | --- |
| New Year's Day | Thursday, January 1 | Friday, January 1 |
| Martin Luther King, Jr. Day | Monday, January 19 | Monday, January 18 |
| Washington's Birthday | Monday, February 16 | Monday, February 15 |
| Good Friday | Friday, April 3 | Friday, March 26 |
| Memorial Day | Monday, May 25 | Monday, May 31 |
| Juneteenth National Independence Day | Friday, June 19 | Friday, June 18 (Juneteenth National Independence Day observed) |
| Independence Day | Friday, July 3 (Independence Day observed) | Monday, July 5 (Independence Day observed) |
| Labor Day | Monday, September 7 | Monday, September 6 |
| Thanksgiving Day | Thursday, November 26\* | Thursday, November 25\* |
| Christmas Day | Friday, December 25\*\* | Friday, December 24 (Christmas Day observed) |

## Early Closes (Partial Closures)

| Date | Occasion |
| --- | --- |
| Friday, November 27, 2026 1:00PM EST | Day after Thanksgiving\* |
| Thursday, December 24, 2026 1:00PM EST | Christmas Eve |
| Friday, November 26, 2027 | Day after Thanksgiving\* |

Updated about 1 month ago

---

[Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)[Partner Fees](https://docs.dinari.com/docs/fees)

Did this page help you?

Yes

No

Copy Page

* + [Dinari Trading Sessions Overview](https://docs.dinari.com/docs/trading-hours)
  + - [Sessions Overview](https://docs.dinari.com/docs/trading-hours)
    - [Session Details](https://docs.dinari.com/docs/trading-hours)
    - * [Regular Trading Session](https://docs.dinari.com/docs/trading-hours)
      * [Extended Hours Trading Session](https://docs.dinari.com/docs/trading-hours)
      * [Overnight Trading Session](https://docs.dinari.com/docs/trading-hours)
      * [Open (24/7) Trading Session](https://docs.dinari.com/docs/trading-hours)
    - [Holidays](https://docs.dinari.com/docs/trading-hours)
    - * [Market Holidays](https://docs.dinari.com/docs/trading-hours)
      * [Bank Holidays](https://docs.dinari.com/docs/trading-hours)
      * [Common Scenarios](https://docs.dinari.com/docs/trading-hours)
  + [NYSE Holidays & Trading Hours: 2026 and 2027](https://docs.dinari.com/docs/trading-hours)
  + - [Market Holidays (Full Closures)](https://docs.dinari.com/docs/trading-hours)
    - [Early Closes (Partial Closures)](https://docs.dinari.com/docs/trading-hours)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Trading Hours","dateModified":"2026-10-14T11:34:33.000Z"}
```