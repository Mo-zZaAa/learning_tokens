> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ondo.finance/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating with the USDY_InstantManager contract

> How to programmatically subscribe to and redeem USDY directly on-chain via the USDY_InstantManager contract.

## Overview

USDY is Ondo's yield-bearing token that provides investors a steady return over time. The token price started at \$1.00 in July 2023 and has increased over time at a variable monthly rate. For a product-level introduction, see [USDY Basics](https://docs.ondo.finance/general-access-products/usdy/basics.md).

The `USDY_InstantManager` contract is the on-chain entry point used by the Ondo web app to instantly mint and redeem USDY. You can call it directly from your own contracts or EOA to:

* Convert USDC into USDY via `subscribe` (selector `0x22d4a175`)
* Convert USDY back into USDC via `redeem` (selector `0xd8780161`)

Addresses for `USDY`, `USDY_InstantManager`, and the USDY redemption price oracle are listed in [Smart Contracts → Addresses](https://docs.ondo.finance/addresses.md).

> [!NOTE]
>
> The Ethereum USDC address used in the examples below is `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`.

> [!WARNING]
>
> USDY on Tempo is a TIP-20 token with **6 decimals**, not 18. When you integrate with the `USDY_InstantManager` on Tempo, express USDY amounts in 6 decimals (e.g. `1000000` for 1 USDY).

> [!NOTE]
>
> On Tempo, use OUSD (`0x20c0000000000000000000006a37DA5C996874BE`) as the deposit and redemption token. OUSD is a TIP-20 token with 6 decimals.

## Prerequisites

Before calling `subscribe` or `redeem`, the address that interacts with the contract must be registered in the OndoIDRegistry.

You can whitelist your address at [app.ondo.finance/account/wallets](https://app.ondo.finance/account/wallets). If you run into issues, reach out to [support@ondo.finance](mailto:support@ondo.finance).

> [!WARNING]
>
> Transactions from an address that is not registered in the OndoIDRegistry will revert with `UserNotRegistered`. Contract wallets and smart-contract integrations must whitelist the exact calling address.

### ERC20 approvals

The `USDY_InstantManager` pulls tokens from your wallet via `transferFrom`, so you must approve it to spend the token you are sending **before** calling `subscribe` or `redeem`:

* Before `subscribe`: approve the manager to spend your **deposit token** (e.g. USDC) for at least `depositAmount`.
* Before `redeem`: approve the manager to spend your **USDY** for at least `rwaAmount`.

Each approval is a separate transaction — typically `IERC20(token).approve(usdyInstantManager, amount)`. If you skip this step, the subscribe/redeem call will revert with an ERC20 allowance error such as `ERC20: insufficient allowance`.

## Subscribing: USDC to USDY

### Function signature

```solidity theme={null}
function subscribe(
    address depositToken,
    uint256 depositAmount,
    uint256 minimumRwaReceived
) external returns (uint256 rwaAmountOut);
```

### Parameters

* **`depositToken`**: the token being deposited (typically USDC)
* **`depositAmount`**: the amount of `depositToken` to deposit, in the token's native decimals (e.g. `1000000` for 1 USDC)
* **`minimumRwaReceived`**: slippage protection, denominated in USDY's decimals (18 on most chains, 6 on Tempo). Because you are minting directly with Ondo, there is no front-running or order-size slippage, so `0` is safe.

### Example

```solidity theme={null}
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

```solidity theme={null}
function redeem(
    uint256 rwaAmount,
    address receivingToken,
    uint256 minimumTokenReceived
) external returns (uint256 receiveTokenAmount);
```

### Parameters

* **`rwaAmount`**: the amount of USDY to redeem, in USDY's decimals (e.g. `1000000000000000000` for 1 USDY on most chains, or `1000000` on Tempo)
* **`receivingToken`**: the stablecoin to receive (USDC on Ethereum, USDT on BNB Chain, OUSD on Tempo). Passing a token that isn't accepted on that chain reverts with `TokenNotAccepted`.
* **`minimumTokenReceived`**: the minimum amount of `receivingToken` to accept, in its native decimals. The payout is priced from oracle values, not a market, so it's predictable. Quote it by simulating the call (for example with `eth_call`), then set this slightly below the quote. Passing `0` disables the check.

### Example

```solidity theme={null}
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

The USDY price is published on-chain by the `ContinuousPriceOracle` contract, which integrators and the `USDY_InstantManager` read through the `USDYOracleWrapper` (see [/addresses](https://docs.ondo.finance/addresses.md#usdy)). The oracle stores a price and a yearly rate, and calculates the current price every time it is read, so the price grows continuously instead of once a day. The rate stays in force until Ondo changes it. The `USDY_InstantManager` consults this oracle on every subscription and redemption to convert between USD value and USDY amounts.

All prices are denominated in USD with 18 decimals.

### Get the current price

```solidity theme={null}
function getPrice() external view returns (uint256 price);
function getPriceData() external view returns (uint256 price, uint256 timestamp);
```

* **`getPrice()`**: returns the current USDY price, in USD with 18 decimals.
* **`getPriceData()`**: convenience wrapper that also returns the current block timestamp.

Neither function reverts, including when the oracle is frozen. A frozen oracle keeps returning a price, but the price stops growing.

```solidity theme={null}
uint256 price = usdyOracle.getPrice();
// e.g. 1.087543210000000000 → 1087543210000000000
```

### Converting between USD and USDY

The oracle price represents how many USD one USDY is worth.

```solidity theme={null}
// USDY amount (18 decimals) → USD value (18 decimals)
uint256 usdValue = (usdyAmount * oracle.getPrice()) / 1e18;

// USD value (18 decimals) → USDY amount (18 decimals)
uint256 usdyAmount = (usdValue * 1e18) / oracle.getPrice();
```

On Tempo, USDY has 6 decimals, so replace `1e18` with `1e6` (`10 ** usdy.decimals()`) in the formulas above. The oracle price and all USD values, including contract minimums, rate limits, and event fields, stay at 18 decimals.

## Reference

### Decimal handling

* **USDC**: 6 decimals (1 USDC = 1,000,000 units)
* **USDY**: 18 decimals (1 USDY = 10<sup>18</sup> units) on most chains; 6 decimals (1 USDY = 1,000,000 units) on Tempo
* **Oracle prices**: 18 decimals

### Rate limits and minimums

The manager contract enforces per-user and global rate limits, as well as a configured minimum USD value per subscription and redemption. Very small or unusually large transactions may revert.

### Common errors

| Error | Meaning |
| - | - |
| `SubscriptionsPaused` / `RedemptionsPaused` | Operations are temporarily paused on the manager |
| `TokenNotAccepted` | The specified deposit or receiving token is not supported |
| `UserNotRegistered` | The caller is not registered in the OndoIDRegistry |
| `DepositAmountTooSmall` / `RedemptionAmountTooSmall` | Transaction is below the configured USD minimum |
| `RwaReceiveAmountTooSmall` / `ReceiveAmountTooSmall` | Output is less than the specified minimum |
| Compliance revert | The caller failed the OndoCompliance check (e.g. sanctions, jurisdiction) |
| Rate-limit revert | The transaction exceeds per-user or global rate limits |

### Best practices

1. Ensure the calling address is whitelisted in the OndoIDRegistry before attempting any transaction.
2. Check the contract's pause status (`subscribePaused` / `redeemPaused`) before attempting transactions.
3. Approve the `USDY_InstantManager` for the exact amount being deposited or redeemed.
4. Implement proper error handling for all possible revert conditions.

## Resources

* [Contract addresses](https://docs.ondo.finance/addresses.md)
* [Audits](https://docs.ondo.finance/audits.md)
* [USDY Basics](https://docs.ondo.finance/general-access-products/usdy/basics.md)

<Snippet file="usdy-legal-notice.mdx" />


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.