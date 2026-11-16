---
url: https://docs.ondo.finance/developer-guides/mantle-integration-guidelines
title: Integration Guidelines for Protocols Supporting USDY on Mantle - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [USDY & mUSD](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
  + [USDY](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
  + [mUSD](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
* [USDY Oracle (ContinuousPriceOracle)](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
* [Integrating USDY into Your Web3 Application](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
  + [Option 1: Native integration](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
  + [Option 2: Informative integration](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
* [SmartContracts details](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)
* [Resources](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)

Developer Guides

# Integration Guidelines for Protocols Supporting USDY on Mantle

Copy pageCopy page

Copy pageCopy page

## **USDY & mUSD**

### USDY

**USDY (US Dollar Yield Token)**: USDY is a tokenized note secured by short-term US Treasuries and bank demand deposits. USDY holders receive yield generated from the underlying assets in the form of increasing redemption value (accumulating token). USDY contract is an upgradeable (Transparent Upgradeable Proxy) ERC-20 token. To hold, send, and receive USDY, users should not be on the [blocklist](https://github.com/code-423n4/2023-09-ondo/blob/main/contracts/usdy/blocklist/Blocklist.sol).

### mUSD

**mUSD** is the rebasing version of USDY, maintaining a consistent peg to $1. Interest is distributed via new token units. Users can swap freely between USDY and mUSD. A swapper UI will be available in October on [ondo.finance](https://ondo.finance/).
mUSD is heavily based on other rebasing tokens such as `stETH`. Users can acquire mUSD tokens by calling the `wrap(uint256)` function on the contract. While the price of a single USDY token increases over time, the price of a single mUSD token is fixed at a price of 1 Dollar, with yield being accrued in the form of additional mUSD tokens. Similarly when a user wishes to convert their `mUSD` to `USDY` they can call the `unwrap(uint256)` function, and receive their corresponding amount of `USDY`.
In order to determine the USD value of the USDY locked in the contract, mUSD reads the current price from the USDY oracle wrapper, which always points to the current USDY price oracle.
Because `mUSD` is the rebasing variant of `USDY` the same transfer restrictions for `USDY` are also applied to the `mUSD` token in the `beforeTransfer(address,address,uint256)` hook.
`mUSD` rebases continuously: balances are calculated from the current USDY price whenever they are read.

## USDY Oracle (ContinuousPriceOracle)

The `ContinuousPriceOracle` contract publishes the USDY price on chain. It stores a price and a yearly rate (APY), and calculates the current price every time it is read: the stored price, grown continuously at that rate since it was stored. The price therefore rises continuously instead of once a day.
The current rate continues to apply until it is changed, so the price continues to accrue at that rate without a daily update. Rate changes can be scheduled in advance to start at a future time.

## Integrating USDY into Your Web3 Application

As users may hold USDY or mUSD, a good practice is to support both.
Let’s assume a user holds mUSD and wants to supply to your USDY pool.

### Option 1: Native integration

The user can directly use his mUSD to interact with your contracts. This means that your contracts will add an extra call to swap from mUSD to USDY before depositing the USDY in the pool.
Example of a native integration: [Compound pool on curve.fi](https://curve.fi/)

[그림: Curve unwrapped]

[그림: Curve wrapped]

### Option 2: Informative integration

When trying to supply mUSD, your app informs the user they need to swap to USDY before depositing to the pool: “To supply USDY, you must first swap your mUSD for USDY at [ondo.finance](https://ondo.finance/)”
Example of an informative integration: [wstETH on Balancer](https://app.balancer.fi/)

[그림: Balancer guidelines]

## SmartContracts details

* **[rUSDY.sol](https://github.com/code-423n4/2023-09-ondo/blob/main/contracts/usdy/rUSDY.sol)** - This contract serves as the backbone for an interest-bearing token where users can `wrap and unwrap` their `USDY` tokens to earn interest. It also includes features for access control and address management.
* **[rUSDYFactory.sol](https://github.com/code-423n4/2023-09-ondo/blob/main/contracts/usdy/rUSDYFactory.sol)** - This is a factory contract that allows the deployment of upgradable instances of the `mUSD token` contract. It is managed by a guardian address, and the deployment process involves creating an implementation contract, a proxy admin contract, and a proxy contract for the token. The code is designed to facilitate the upgradeability of the `mUSD` token and includes functions for batched external calls.
* [**ContinuousPriceOracle.sol**](https://github.com/ondoprotocol/rwa-contracts/blob/main/contracts/rwaOracles/ContinuousPriceOracle.sol) - This contract provides the price of `USDY`, calculated continuously from a stored price and a yearly rate. Rate changes are limited on chain in size and frequency, and the oracle can be frozen in an emergency without breaking price reads.
* **[IRWADynamicOracle](https://github.com/code-423n4/2023-09-ondo/blob/main/contracts/rwaOracles/IRWADynamicOracle.sol)** - This is an interface that sets a standard for any contract wishing to provide information about the price of `RWA` (Asset-Backed Real World Assets) or similar assets. Contracts that implement this interface must provide a `getPrice()` function that returns the current price of `RWA`. The interface does not contain implementation logic but simply establishes a common structure for communication with dynamic asset price oracles.

## Resources

* [Media Kit](https://www.notion.so/3bc0a5aced014cc4b0ef62f1638bbf8e?pvs=21)
* [Contract addresses](https://docs.ondo.finance/addresses)
* [Audits](https://docs.ondo.finance/audits)
* [USDY github repository](https://github.com/ondoprotocol/usdy)

[Integrating with the USDY\_InstantManager contract](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)[Ondo Stocks Limit Orders](https://docs.ondo.finance/developer-guides/limit-order-contracts)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines#webpage","url":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines","name":"Integration Guidelines for Protocols Supporting USDY on Mantle","dateModified":"2026-11-07T00:41:58.292Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Developer Guides","item":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration"},{"@type":"ListItem","position":2,"name":"Integration Guidelines for Protocols Supporting USDY on Mantle","item":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines#article","headline":"Integration Guidelines for Protocols Supporting USDY on Mantle","name":"Integration Guidelines for Protocols Supporting USDY on Mantle","url":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines","mainEntityOfPage":{"@id":"https://docs.ondo.finance/developer-guides/mantle-integration-guidelines#webpage"},"dateModified":"2026-11-07T00:41:58.292Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```