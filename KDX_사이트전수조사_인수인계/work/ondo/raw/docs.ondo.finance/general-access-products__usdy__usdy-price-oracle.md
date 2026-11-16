---
url: https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle
title: USDY Price Oracle - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [How the price is calculated](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [Rate changes](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [What changed](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [For integrators](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)

USDY

# USDY Price Oracle

Copy pageCopy page

Copy pageCopy page

Starting November 1, 2026 at 00:00 UTC, the USDY price on Ethereum, BNB Chain, Mantle and Tempo comes from the `ContinuousPriceOracle` contract and rises continuously instead of once a day.

**Important for integrators:** The new oracle does not support `getPriceHistorical`. The `USDYOracleWrapper` has never supported it, so nothing changes if you read the wrapper. If your integration calls `getPriceHistorical` on the previous oracle directly, you will need another way to get USDY prices from November 1, 2026 onward.

## How the price is calculated

The oracle stores a price and a yearly rate (APY). Each time the price is read, the oracle calculates it: the stored price, grown continuously at that rate since it was stored. USDY therefore earns yield throughout the day, and rUSDY and mUSD balances grow at the same pace.

## Rate changes

The rate stays in force until Ondo changes it, so the price continues to accrue at that rate without a daily update. Ondo can schedule a new rate to start at a future time. A routine change is limited on-chain to 10% of the current rate (for example, at 3.75% APY, about 0.375 percentage points) and to once every 8 hours. Changes larger than this, or sooner than 8 hours after the last one, can only be made through a timelock.The `ContinuousPriceOracle` contract was audited by Spearbit (March 2025) and Cyfrin (October 2026). See [Smart Contract Audits](https://docs.ondo.finance/audits).

## What changed

Before November 1, 2026, the USDY price came from the Dynamic Rate Oracle, which added a full day of yield at 00:00 UTC and needed a new rate range every month.

|  | Previous oracle (Dynamic Rate Oracle) | New oracle (ContinuousPriceOracle) |
| --- | --- | --- |
| How the price moves | Once a day, at 00:00 UTC | Continuously |
| How the rate is set | Daily rate for a fixed date range | Yearly rate that stays until changed |
| If no update is made | Price stops growing at the end of the range | Price continues to accrue at the current rate |

## For integrators

Read the USDY price from the `USDYOracleWrapper` for your chain, listed on [Smart Contract Addresses](https://docs.ondo.finance/addresses). The wrapper always points to the current USDY oracle, so integrators reading it don’t need to do anything at the switchover or at any future oracle change. The `ContinuousPriceOracle` addresses are listed there for reference. If you calculate the USDY price off-chain, switch to the continuous calculation.The new oracle supports `getPrice()` and `getPriceData()`, which never revert. It does not support `getPriceHistorical`.The previous oracle is expected to be deprecated on December 31, 2026. After that it receives no new rate and is paused, so `getPrice()` and `getPriceData()` on it will fail instead of returning an outdated price. Integrators that read it directly should move to the `USDYOracleWrapper` before then.

[Rebasing](https://docs.ondo.finance/general-access-products/usdy/rebasing)[Eligibility](https://docs.ondo.finance/general-access-products/usdy/eligibility)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle","name":"USDY Price Oracle","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"USDY Price Oracle","item":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#article","headline":"USDY Price Oracle","name":"USDY Price Oracle","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```