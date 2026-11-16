# 읽기 묶음: docs.ondo.finance / developer-guides (1/1)


<<<PAGE https://docs.ondo.finance/developer-guides/limit-order-contracts>>>
---
url: https://docs.ondo.finance/developer-guides/limit-order-contracts
title: Ondo Stocks Limit Orders - Ondo Finance
description: How to create and manage Ondo Stocks limit orders with GMLimitOrder contracts.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Purpose](https://docs.ondo.finance/developer-guides/limit-order-contracts)
* [Creating Limit Orders](https://docs.ondo.finance/developer-guides/limit-order-contracts)
* [Canceling Orders](https://docs.ondo.finance/developer-guides/limit-order-contracts)
* [Order Status](https://docs.ondo.finance/developer-guides/limit-order-contracts)
  + [Events](https://docs.ondo.finance/developer-guides/limit-order-contracts)
* [Contract Addresses](https://docs.ondo.finance/developer-guides/limit-order-contracts)
* [FAQ](https://docs.ondo.finance/developer-guides/limit-order-contracts)

Developer Guides

# Ondo Stocks Limit Orders

Copy pageCopy page

How to create and manage Ondo Stocks limit orders with GMLimitOrder contracts.

Copy pageCopy page

Ondo stocks can be bought or sold using the GMLimitOrder contracts.

## Purpose

Attestations have 30 second expirations on Ethereum mainnet and 15 seconds on Binance Smart chain. Using wallets from custody providers may make ensuring transaction submission difficult depending on how fast custody providers process transactions. The limit order contracts allow users to avoid the challenging time limit by submitting orders on-chain with a limit price, and Ondo will fulfill the order on behalf of the user through the normal attestation process. The contract enforces that an order will always be fulfilled at or better than the user’s set limit price.

## Creating Limit Orders

Use the GMLimitOrder contract. The functions for creating orders are:

| Function | Signature | Parameters |
| --- | --- | --- |
| `createBuyOrderExactIn` | `createBuyOrderExactIn(address,address,uint256,uint256,uint256)` | gmToken (address), quoteToken (address), quoteAmount (uint256), limitPrice (uint256), expiry (uint256) |
| `createBuyOrderExactOut` | `createBuyOrderExactOut(address,address,uint256,uint256,uint256)` | gmToken (address), quoteToken (address), gmAmount (uint256), limitPrice (uint256), expiry (uint256) |
| `createSellOrderExactIn` | `createSellOrderExactIn(address,address,uint256,uint256,uint256)` | gmToken (address), quoteToken (address), gmAmount (uint256), limitPrice (uint256), expiry (uint256) |
| `createSellOrderExactOut` | `createSellOrderExactOut(address,address,uint256,uint256,uint256)` | gmToken (address), quoteToken (address), quoteAmount (uint256), limitPrice (uint256), expiry (uint256) |

ExactIn functions specify the amount of input tokens to spend, ExactOut functions specify the amount of output tokens to receive.

## Canceling Orders

| Function | Signature | Parameters |
| --- | --- | --- |
| `cancelOrder` | `cancelOrder(uint256)` | orderId (uint256) |

## Order Status

| Function | Signature | Parameters |
| --- | --- | --- |
| `orders` | `orders(uint256)` | orderId (uint256) |
| `isOrderActive` | `isOrderActive(uint256)` | orderId (uint256) |
| `isOrderExecuted` | `isOrderExecuted(uint256)` | orderId (uint256) |

### Events

Newly created orders:

```
event OrderCreated(
    uint256 indexed orderId,
    address indexed user,
    address indexed gmToken
  );
```

Order execution:

```
event OrderExecuted(
    uint256 indexed orderId,
    address indexed executor,
    IGMTokenManager.QuoteSide side,
    uint256 attestationId,
    uint256 gmQuantity,
    uint256 quoteTokenAmount
  );
```

Order cancellation:
`event OrderCancelled(uint256 indexed orderId, address indexed cancelledBy);`

## Contract Addresses

GMLimitOrder Ethereum: `0xf0Bc39Fc911F6437C84d16188dD8294F7110f451`
GMLimitOrder BNB: `0xA2aA93cbB069B4BF246258E4D9cD093B914DcDFE`

## FAQ

**Q:** Are my account rate limits affected by submitting limit orders?  
**A:** No. Because the attestation API is not required in this flow, your account rate limits are not affected.
**Q:** Can I submit limit orders on Solana?  
**A:** Currently, the limit order contracts are deployed on Ethereum and BNB only.
**Q:** What addresses can submit limit orders?  
**A:** Onboarded, AllowListed wallets only can submit limit orders.
**Q:** Does submitting limit orders affect my session limits?  
**A:** Limit orders do not require an attestation at the time of submission, so submitting orders does not affect your session limits.
**Q:** What is the maximum duration I can set an order to have?  
**A:** Query the `GMLimitOrder` function `maxOrderDuration` to see the current maximum order duration.

[Integration Guidelines for Protocols Supporting USDY on Mantle](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)[Ondo Token Bridge](https://docs.ondo.finance/tools/ondo-bridge)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/developer-guides/limit-order-contracts#webpage","url":"https://docs.ondo.finance/developer-guides/limit-order-contracts","name":"Ondo Stocks Limit Orders","description":"How to create and manage Ondo Stocks limit orders with GMLimitOrder contracts.","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/developer-guides/limit-order-contracts#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/developer-guides/limit-order-contracts#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Developer Guides","item":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration"},{"@type":"ListItem","position":2,"name":"Ondo Stocks Limit Orders","item":"https://docs.ondo.finance/developer-guides/limit-order-contracts"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/developer-guides/limit-order-contracts#article","headline":"Ondo Stocks Limit Orders","name":"Ondo Stocks Limit Orders","description":"How to create and manage Ondo Stocks limit orders with GMLimitOrder contracts.","url":"https://docs.ondo.finance/developer-guides/limit-order-contracts","mainEntityOfPage":{"@id":"https://docs.ondo.finance/developer-guides/limit-order-contracts#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/developer-guides/mantle-integration-guidelines>>>
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

<<<PAGE https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration>>>
---
url: https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration
title: Integrating with the USDY_InstantManager contract - Ondo Finance
description: How to programmatically subscribe to and redeem USDY directly on-chain via the USDY_InstantManager contract.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Overview](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [Prerequisites](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [ERC20 approvals](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [Subscribing: USDC to USDY](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Function signature](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Parameters](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Example](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [Redeeming: USDY to USDC](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Function signature](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Parameters](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Example](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [USDY price oracle](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Get the current price](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Converting between USD and USDY](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [Reference](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Decimal handling](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Rate limits and minimums](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Common errors](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
  + [Best practices](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)
* [Resources](https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration)

Developer Guides

# Integrating with the USDY\_InstantManager contract

Copy pageCopy page

How to programmatically subscribe to and redeem USDY directly on-chain via the USDY\_InstantManager contract.

Copy pageCopy page

## Overview

USDY is Ondo’s yield-bearing token that provides investors a steady return over time. The token price started at $1.00 in July 2023 and has increased over time at a variable monthly rate. For a product-level introduction, see [USDY Basics](https://docs.ondo.finance/general-access-products/usdy/basics).
The `USDY_InstantManager` contract is the on-chain entry point used by the Ondo web app to instantly mint and redeem USDY. You can call it directly from your own contracts or EOA to:

* Convert USDC into USDY via `subscribe` (selector `0x22d4a175`)
* Convert USDY back into USDC via `redeem` (selector `0xd8780161`)

Addresses for `USDY`, `USDY_InstantManager`, and the USDY redemption price oracle are listed in [Smart Contracts → Addresses](https://docs.ondo.finance/addresses).

The Ethereum USDC address used in the examples below is `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`.

USDY on Tempo is a TIP-20 token with **6 decimals**, not 18. When you integrate with the `USDY_InstantManager` on Tempo, express USDY amounts in 6 decimals (e.g. `1000000` for 1 USDY).

On Tempo, use OUSD (`0x20c0000000000000000000006a37DA5C996874BE`) as the deposit and redemption token. OUSD is a TIP-20 token with 6 decimals.

## Prerequisites

Before calling `subscribe` or `redeem`, the address that interacts with the contract must be registered in the OndoIDRegistry.
You can whitelist your address at [app.ondo.finance/account/wallets](https://app.ondo.finance/account/wallets). If you run into issues, reach out to [support@ondo.finance](mailto:support@ondo.finance).

Transactions from an address that is not registered in the OndoIDRegistry will revert with `UserNotRegistered`. Contract wallets and smart-contract integrations must whitelist the exact calling address.

### ERC20 approvals

The `USDY_InstantManager` pulls tokens from your wallet via `transferFrom`, so you must approve it to spend the token you are sending **before** calling `subscribe` or `redeem`:

* Before `subscribe`: approve the manager to spend your **deposit token** (e.g. USDC) for at least `depositAmount`.
* Before `redeem`: approve the manager to spend your **USDY** for at least `rwaAmount`.

Each approval is a separate transaction — typically `IERC20(token).approve(usdyInstantManager, amount)`. If you skip this step, the subscribe/redeem call will revert with an ERC20 allowance error such as `ERC20: insufficient allowance`.

## Subscribing: USDC to USDY

### Function signature

```
function subscribe(
    address depositToken,
    uint256 depositAmount,
    uint256 minimumRwaReceived
) external returns (uint256 rwaAmountOut);
```

### Parameters

* **`depositToken`**: the token being deposited (typically USDC)
* **`depositAmount`**: the amount of `depositToken` to deposit, in the token’s native decimals (e.g. `1000000` for 1 USDC)
* **`minimumRwaReceived`**: slippage protection, denominated in USDY’s decimals (18 on most chains, 6 on Tempo). Because you are minting directly with Ondo, there is no front-running or order-size slippage, so `0` is safe.

### Example

```
// Swap 100 USDC for USDY
IERC20(USDC).approve(usdyInstantManager, 100e6);
uint256 usdyReceived = usdyInstantManager.subscribe(
    USDC,
    100e6, // 100 USDC (6 decimals)
    0      // no slippage expected when minting directly
);
```

## Redeeming: USDY to USDC

### Function signature

```
function redeem(
    uint256 rwaAmount,
    address receivingToken,
    uint256 minimumTokenReceived
) external returns (uint256 receiveTokenAmount);
```

### Parameters

* **`rwaAmount`**: the amount of USDY to redeem, in USDY’s decimals (e.g. `1000000000000000000` for 1 USDY on most chains, or `1000000` on Tempo)
* **`receivingToken`**: the stablecoin to receive (USDC on Ethereum, USDT on BNB Chain, OUSD on Tempo). Passing a token that isn’t accepted on that chain reverts with `TokenNotAccepted`.
* **`minimumTokenReceived`**: the minimum amount of `receivingToken` to accept, in its native decimals. The payout is priced from oracle values, not a market, so it’s predictable. Quote it by simulating the call (for example with `eth_call`), then set this slightly below the quote. Passing `0` disables the check.

### Example

```
// Redeem 100 USDY on Ethereum for USDC
// (Tempo: amount 100e6 and OUSD; BNB Chain: USDT)
IERC20(USDY).approve(usdyInstantManager, 100e18);
uint256 received = usdyInstantManager.redeem(
    100e18,      // 100 USDY, in USDY decimals
    USDC,        // must be an accepted redemption token on this chain
    minReceived  // quoted amount minus a small tolerance
);
```

## USDY price oracle

The USDY price is published on-chain by the `ContinuousPriceOracle` contract, which integrators and the `USDY_InstantManager` read through the `USDYOracleWrapper` (see [/addresses](https://docs.ondo.finance/addresses)). The oracle stores a price and a yearly rate, and calculates the current price every time it is read, so the price grows continuously instead of once a day. The rate stays in force until Ondo changes it. The `USDY_InstantManager` consults this oracle on every subscription and redemption to convert between USD value and USDY amounts.
All prices are denominated in USD with 18 decimals.

### Get the current price

```
function getPrice() external view returns (uint256 price);
function getPriceData() external view returns (uint256 price, uint256 timestamp);
```

* **`getPrice()`**: returns the current USDY price, in USD with 18 decimals.
* **`getPriceData()`**: convenience wrapper that also returns the current block timestamp.

Neither function reverts, including when the oracle is frozen. A frozen oracle keeps returning a price, but the price stops growing.

```
uint256 price = usdyOracle.getPrice();
// e.g. 1.087543210000000000 → 1087543210000000000
```

### Converting between USD and USDY

The oracle price represents how many USD one USDY is worth.

```
// USDY amount (18 decimals) → USD value (18 decimals)
uint256 usdValue = (usdyAmount * oracle.getPrice()) / 1e18;

// USD value (18 decimals) → USDY amount (18 decimals)
uint256 usdyAmount = (usdValue * 1e18) / oracle.getPrice();
```

On Tempo, USDY has 6 decimals, so replace `1e18` with `1e6` (`10 ** usdy.decimals()`) in the formulas above. The oracle price and all USD values, including contract minimums, rate limits, and event fields, stay at 18 decimals.

## Reference

### Decimal handling

* **USDC**: 6 decimals (1 USDC = 1,000,000 units)
* **USDY**: 18 decimals (1 USDY = 1018 units) on most chains; 6 decimals (1 USDY = 1,000,000 units) on Tempo
* **Oracle prices**: 18 decimals

### Rate limits and minimums

The manager contract enforces per-user and global rate limits, as well as a configured minimum USD value per subscription and redemption. Very small or unusually large transactions may revert.

### Common errors

| Error | Meaning |
| --- | --- |
| `SubscriptionsPaused` / `RedemptionsPaused` | Operations are temporarily paused on the manager |
| `TokenNotAccepted` | The specified deposit or receiving token is not supported |
| `UserNotRegistered` | The caller is not registered in the OndoIDRegistry |
| `DepositAmountTooSmall` / `RedemptionAmountTooSmall` | Transaction is below the configured USD minimum |
| `RwaReceiveAmountTooSmall` / `ReceiveAmountTooSmall` | Output is less than the specified minimum |
| Compliance revert | The caller failed the OndoCompliance check (e.g. sanctions, jurisdiction) |
| Rate-limit revert | The transaction exceeds per-user or global rate limits |

### Best practices

1. Ensure the calling address is whitelisted in the OndoIDRegistry before attempting any transaction.
2. Check the contract’s pause status (`subscribePaused` / `redeemPaused`) before attempting transactions.
3. Approve the `USDY_InstantManager` for the exact amount being deposited or redeemed.
4. Implement proper error handling for all possible revert conditions.

## Resources

* [Contract addresses](https://docs.ondo.finance/addresses)
* [Audits](https://docs.ondo.finance/audits)
* [USDY Basics](https://docs.ondo.finance/general-access-products/usdy/basics)

[Flux Finance](https://docs.ondo.finance/protocols/flux)[Integration Guidelines for Protocols Supporting USDY on Mantle](https://docs.ondo.finance/developer-guides/mantle-integration-guidelines)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration#webpage","url":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration","name":"Integrating with the USDY_InstantManager contract","description":"How to programmatically subscribe to and redeem USDY directly on-chain via the USDY_InstantManager contract.","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Integrating with the USDY_InstantManager contract","item":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration#article","headline":"Integrating with the USDY_InstantManager contract","name":"Integrating with the USDY_InstantManager contract","description":"How to programmatically subscribe to and redeem USDY directly on-chain via the USDY_InstantManager contract.","url":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration","mainEntityOfPage":{"@id":"https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```