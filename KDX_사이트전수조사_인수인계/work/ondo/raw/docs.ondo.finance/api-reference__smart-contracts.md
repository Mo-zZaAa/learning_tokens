---
url: https://docs.ondo.finance/api-reference/smart-contracts
title: Smart Contract Reference - Ondo Finance
description: Smart contract interface for buying and selling Ondo Stocks with attestations.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [IGMTokenManager](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Buying GM Tokens](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Selling GM Tokens](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Functions](https://docs.ondo.finance/api-reference/smart-contracts)
  + [mintWithAttestation](https://docs.ondo.finance/api-reference/smart-contracts)
  + [redeemWithAttestation](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Structs](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Quote](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Enums](https://docs.ondo.finance/api-reference/smart-contracts)
  + [QuoteSide](https://docs.ondo.finance/api-reference/smart-contracts)
* [IPortfolioTokenManager](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Buying Portfolio Tokens](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Selling Portfolio Tokens](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Functions](https://docs.ondo.finance/api-reference/smart-contracts)
  + [mintWithAttestation](https://docs.ondo.finance/api-reference/smart-contracts)
  + [redeemWithAttestation](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Structs](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Quote](https://docs.ondo.finance/api-reference/smart-contracts)
  + [Enums](https://docs.ondo.finance/api-reference/smart-contracts)
  + [QuoteSide](https://docs.ondo.finance/api-reference/smart-contracts)
* [Contract Addresses](https://docs.ondo.finance/api-reference/smart-contracts)

References

# Smart Contract Reference

Copy pageCopy page

Smart contract interface for buying and selling Ondo Stocks with attestations.

Copy pageCopy page

## `IGMTokenManager`

The IGMTokenManager interface may be used by external parties to buy and sell Ondo Stocks using attestations. The general flow for each side is:

### Buying GM Tokens

1. User gets a signed quote (off‑chain)
   * The attestation service prepares a `Quote` whose side is `BUY`, signs its EIP‑712 digest, and returns the quote and signature to the user
   * Price is expressed in USD with 18 decimals (e.g., $12.34 →12340000000000000000)
   * Quantity is the number of GM tokens the user wishes to receive
2. User pre‑authorizes USDon or USDC/USDT
   * GMTokenManager must have a sufficient allowance of USDon, USDC (Ethereum) or USDT (BNB Chain) before the call
   * Allowance ≥ price × quantity
     > 🚧 Notes on USDon
     > + USDon will be Ondo’s permissionless ERC20 stablecoin representing USD held in Ondo’s brokerage account (which buys equities/ETFs backing GM tokens). Users can convert stablecoins to USDon with zero slippage by specifying it as the deposit token below.
     > + We accept USDC on Ethereum, and USDT on BNB Chain.
     > + If you would like to convert stablecoins to USDon *directly*, outside of a GM token swap, reach out to us and we can provide instructions for our USDonConverter contract.
3. User calls `mintWithAttestation(quote, signature, depositToken, depositTokenAmount)`, which will atomically:
   Verify the quote
   * Re‑computes the EIP‑712 digest and verifies the signature against the attestation signer
   * Confirm that the caller is whitelisted and their stored `userID` matches the one received in the quote
   * Ensures the `attestationId` has not been used and that `block.timestamp ≤ expiration`
   * Confirms side == `BUY`
   * Ensure the value of the transaction is greater than `minimumDepositUSD` but does not exceed per-user and per-token rate limitsSettle the tokens
   * If the `depositToken` specified is not USDon, first swap `depositTokenAmount` for USDon
   * Burns price × quantity of USDon (either after receiving from `msg.sender` or swapping)
   * Mints quantity of GM tokens to `msg.sender`
   * Refund USDon to the user if any is leftoverPost‑process the quote
   * Marks `attestationId` as consumed to prevent replayReturn the tokens received
   * `receivedGmTokenAmount` equals quantity

### Selling GM Tokens

1. User gets a signed quote (off‑chain)
   * Attestation service issues a `Quote` whose side is `SELL`, signs it, and returns quote and signature
   * Price still uses 18‑decimal USD format
   * Quantity is the GM amount the user will sell
2. User pre‑authorizes GM tokens
   * GMTokenManager must have allowance ≥ quantity of the specific GM token (asset) described in the quote
3. User calls `redeemWithAttestation(quote, signature, receiveToken, minimumReceiveAmount)`, which will atomically:
   Verify the quote
   * Same as subscribe, but checks that side == `SELL` instead and that the transaction value is greater than `minimumRedemptiUSDon`Settle the tokens
   * Transfers quantity of GM tokens from user to manager and burns them
   * Mints out price × quantity of USDon to the GMTokenManager
   * If the caller specifies a non-USDon token as the receiveToken, it will swap all the USDon received for the receiveToken (note: the call will revert if the swap doesn’t result in >= `minimumReceiveAmount` being received)
   * All tokens received are transferred to the callerPost‑process the quote
   * Marks `attestationId` as usedReturn the tokens received
   * `receivedUSDonAmount` equals price × quantity

### Functions

#### `mintWithAttestation`

Called by users to mint GM tokens with a quote attestation using either USDon, USDC on Ethereum, or USDT on Binance Smart Chain.
*If the deposit token is not USDon and the depositTokenAmount is not enough to swap for USDon  
worth quantity \* price as specified in the quote, the transaction will fail as the `mintUSDonValue` is passed in to the minimum RWA received field in `subscribe`.*

```
function mintWithAttestation(
    Quote calldata quote,
    bytes memory signature,
    address depositToken,
    uint256 depositTokenAmount
) public override whenMintingNotPaused(quote.asset) returns (uint256);
```

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `quote` | `Quote` | The quote to mint GM tokens with |
| `signature` | `bytes` | The signature of the quote attestation |
| `depositToken` | `address` | The token the user would like to deposit in return for GM Tokens. If not USDon, this will be reliant on the ability to swap for USDon in the USDonManager |
| `depositTokenAmount` | `uint256` | The amount of depositToken the user wishes to spend to purchase USDon atomically in the transaction |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The amount of GM tokens minted to the user |

#### `redeemWithAttestation`

Called by users to redeem GM tokens for USDon.

```
function redeemWithAttestation(
    Quote calldata quote,
    bytes memory signature,
    address receiveToken,
    uint256 minimumReceiveAmount
) public override whenRedeemNotPaused(quote.asset) returns (uint256);
```

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `quote` | `Quote` | The quote to redeem GM tokens with |
| `signature` | `bytes` | The signature of the quote attestation |
| `receiveToken` | `address` | The token the user would like to receive. If it is not USDon, transaction success will depend on liquidity in USDonManager |
| `minimumReceiveAmount` | `uint256` | The minimum amount of tokens the user would like to receive - ONLY applicable if the user requests a non-USDon otoken |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The amount of USDon minted |

### Structs

#### `Quote`

Quote struct that is signed by the attestation signer

```
struct Quote {
    uint256 chainId;
    uint256 attestationId;
    bytes32 userId;
    address asset;
    uint256 price;
    uint256 quantity;
    uint256 expiration;
    QuoteSide side;
    bytes32 additionalData;
}
```

**Properties**

| Name | Type | Description |
| --- | --- | --- |
| `chainId` | `uint256` | The chain ID of the quote is intended for |
| `attestationId` | `uint256` | The ID of the quote |
| `userId` | `bytes32` | The user ID the quote is intended for |
| `asset` | `address` | The address of the GM token being bought or sold |
| `price` | `uint256` | The price of the GM token in USD with 18 decimals |
| `quantity` | `uint256` | The quantity of GM tokens being bought or sold |
| `expiration` | `uint256` | The expiration of the quote in seconds since the epoch |
| `side` | `QuoteSide` | The direction of the quote (BUY or SELL) |
| `additionalData` | `bytes32` | Any additional data that is needed for the quote |

### Enums

#### `QuoteSide`

Enum for the side of the quote

```
enum QuoteSide {
    BUY,
    SELL
}
```

## `IPortfolioTokenManager`

`IPortfolioTokenManager` supports minting and redeeming Ondo Intelligent Portfolios (OIPs) with attestations. OIPs provide exposure to a basket of tokenized stocks and ETFs. They use `PortfolioTokenManager`, not the `IGMTokenManager` used for Ondo Stocks.

### Buying Portfolio Tokens

1. User gets a signed quote off-chain
   * The attestation service prepares a `BUY` quote, signs its EIP-712 digest, and returns the quote and signature
   * Price and quantity use 18 decimals
   * Quotes are only available when the full underlying basket is open for trading
2. User pre-authorizes the stablecoin
   * `PortfolioTokenManager` uses USDC on Ethereum and USDT on BNB Chain, as returned by `stablecoin()`
   * The manager does not accept USDon or other deposit tokens
   * The allowance must cover `ceil((quantity × price / 1e18) / 10^(18 - stablecoin decimals))`
   * Mint charges round up to the stablecoin’s native decimals
3. User calls `mintWithAttestation(quote, signature)`, which will atomically:
   **Verify the quote**
   * Verifies the EIP-712 signature, caller, `userId`, chain ID, side, and expiration
   * Confirms the `attestationId` is unused
   * Confirms the portfolio token is registered, minting is active, and the price passes the oracle check
   * Enforces minimums and rate limits**Settle the tokens**
   * Transfers the stablecoin charge through the token router
   * Mints `quote.quantity` portfolio tokens to the caller**Post-process the quote**
   * Marks the `attestationId` as consumed**Return the tokens received**
   * Returns `quote.quantity`

### Selling Portfolio Tokens

1. User gets a signed quote off-chain
   * The attestation service prepares a `SELL` quote, signs its EIP-712 digest, and returns the quote and signature
   * Price and quantity use 18 decimals
   * Quotes are only available when the full underlying basket is open for trading
2. User pre-authorizes the portfolio tokens
   * `PortfolioTokenManager` must have an allowance of at least `quote.quantity` for the portfolio token
3. User calls `redeemWithAttestation(quote, signature)`, which will atomically:
   **Verify the quote**
   * Verifies the EIP-712 signature, caller, `userId`, chain ID, side, and expiration
   * Confirms the `attestationId` is unused
   * Confirms the portfolio token is registered, redemption is active, and the price passes the oracle check
   * Enforces the minimum redemption value and rate limits**Settle the tokens**
   * Transfers `quote.quantity` portfolio tokens from the caller and burns them
   * Pays the chain’s stablecoin through the token router
   * Rounds the payment down to the stablecoin’s native decimals**Post-process the quote**
   * Marks the `attestationId` as consumed**Return the tokens received**
   * Returns the stablecoin amount paid in its native decimals

### Functions

#### `mintWithAttestation`

Mints portfolio tokens using a quote attestation and the chain’s configured stablecoin. The caller must approve the rounded-up stablecoin charge first.

```
function mintWithAttestation(
    Quote calldata quote,
    bytes memory signature
) external override nonReentrant whenMintingNotPaused(quote.asset) returns (uint256);
```

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `quote` | `Quote` | The quote to mint portfolio tokens with |
| `signature` | `bytes` | The signature of the quote attestation |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The amount of portfolio tokens minted to the user (equal to `quote.quantity`, 18 decimals) |

#### `redeemWithAttestation`

Redeems portfolio tokens for the chain’s configured stablecoin.

```
function redeemWithAttestation(
    Quote calldata quote,
    bytes memory signature
) external override nonReentrant whenRedeemNotPaused(quote.asset) returns (uint256);
```

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `quote` | `Quote` | The quote to redeem portfolio tokens with |
| `signature` | `bytes` | The signature of the quote attestation |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The amount of stablecoin sent to the user, in the stablecoin’s native decimals |

### Structs

#### `Quote`

`PortfolioTokenManager` uses the same `Quote` struct as `IGMTokenManager`. For OIPs, `asset` is the portfolio token address. `price` and `quantity` refer to the portfolio token.
Portfolio quotes use a separate EIP-712 domain with `name = "OndoPortfolioTokenManager"`, `version = "1"`, the chain ID, and the `PortfolioTokenManager` address. GM and portfolio signatures are not interchangeable. Use `getDomainSeparator()` to read the domain separator.

```
bytes32 public constant QUOTE_TYPEHASH = keccak256(
    "Quote(uint256 chainId,uint256 attestationId,bytes32 userId,address asset,uint256 price,uint256 quantity,uint256 expiration,uint8 side,bytes32 additionalData)"
);
```

### Enums

#### `QuoteSide`

The PortfolioTokenManager uses the same `QuoteSide` enum as the IGMTokenManager above.

## Contract Addresses

Contract addresses for `GMTokenManager` and `PortfolioTokenManager` are available on the [smart contract addresses page](https://docs.ondo.finance/addresses).

[ITN Integration](https://docs.ondo.finance/api-reference/itn-integration)[Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/smart-contracts#webpage","url":"https://docs.ondo.finance/api-reference/smart-contracts","name":"Smart Contract Reference","description":"Smart contract interface for buying and selling Ondo Stocks with attestations.","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/smart-contracts#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/smart-contracts#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"Smart Contract Reference","item":"https://docs.ondo.finance/api-reference/smart-contracts"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/smart-contracts#article","headline":"Smart Contract Reference","name":"Smart Contract Reference","description":"Smart contract interface for buying and selling Ondo Stocks with attestations.","url":"https://docs.ondo.finance/api-reference/smart-contracts","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/smart-contracts#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```