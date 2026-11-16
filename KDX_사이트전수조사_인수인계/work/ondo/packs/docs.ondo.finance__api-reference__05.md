# 읽기 묶음: docs.ondo.finance / api-reference (5/5)


<<<PAGE https://docs.ondo.finance/api-reference/smart-contracts>>>
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

<<<PAGE https://docs.ondo.finance/api-reference/soft-quote-depth-streaming>>>
---
url: https://docs.ondo.finance/api-reference/soft-quote-depth-streaming
title: Soft Quote Depth Streaming - Ondo Finance
description: gRPC endpoint for real-time, synthetic soft-quote market depth streaming.
fetched: 2026-11-16
method: render
plan: read
---

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth
```

Streamed

```
{
  "updates": [
    {
      "symbol": "AAPLon",
      "ticker": "AAPL",
      "sessionType": "regular",
      "timestamp": "1773350214476688119",
      "bids": [
        { "price": "256.700000000000000000", "quantity": "100.000000000000000000" },
        { "price": "256.500000000000000000", "quantity": "250.000000000000000000" }
      ],
      "asks": [
        { "price": "256.900000000000000000", "quantity": "100.000000000000000000" },
        { "price": "257.100000000000000000", "quantity": "250.000000000000000000" }
      ]
    },
    {
      "symbol": "GOOGLon",
      "ticker": "GOOGL",
      "sessionType": "regular",
      "error": "market closed",
      "timestamp": "1773350214478735649",
      "bids": [],
      "asks": []
    }
  ]
}
```

Streaming API

# Soft Quote Depth Streaming

Copy pageCopy page

gRPC endpoint for real-time, synthetic soft-quote market depth streaming.

Copy pageCopy page

grpcurl

```
grpcurl \
  -H "x-api-key: <YOUR_API_KEY>" \
  -d '{"symbols": ["AAPLon", "GOOGLon"]}' \
  grpc.gm.ondo.finance:443 \
  ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth
```

Streamed

```
{
  "updates": [
    {
      "symbol": "AAPLon",
      "ticker": "AAPL",
      "sessionType": "regular",
      "timestamp": "1773350214476688119",
      "bids": [
        { "price": "256.700000000000000000", "quantity": "100.000000000000000000" },
        { "price": "256.500000000000000000", "quantity": "250.000000000000000000" }
      ],
      "asks": [
        { "price": "256.900000000000000000", "quantity": "100.000000000000000000" },
        { "price": "257.100000000000000000", "quantity": "250.000000000000000000" }
      ]
    },
    {
      "symbol": "GOOGLon",
      "ticker": "GOOGL",
      "sessionType": "regular",
      "error": "market closed",
      "timestamp": "1773350214478735649",
      "bids": [],
      "asks": []
    }
  ]
}
```

Soft quote depth is a synthetic, indicative market-depth view (bids and asks) derived from the soft-quote price ladder for each asset. It lets clients track quotable size at multiple price levels without polling the REST [Request a Soft Attestation Quote](https://docs.ondo.finance/api-reference/attestations/request-a-soft-attestation-quote) endpoint per price for hundreds of assets. Depth is recomputed and pushed as the underlying ladder changes.

To generate a typed client for this endpoint, see [Protobuf Schema & Code Generation](https://docs.ondo.finance/api-reference/protobuf-schema).

## Authentication

All requests must include your API key in the `x-api-key` metadata header.

## Request

**Endpoint:** `grpc.gm.ondo.finance:443`
**RPC:** `ondo.gm.backend.v1.BackendService/StreamSoftQuoteDepth`

symbols

string[]

Asset symbols to subscribe to. If empty, you will receive updates for all assets.

## Response

A server stream of messages. Each message batches one or more `SoftQuoteDepth` entries (one per symbol that updated since the last send) into a single `updates` array.
Each entry holds the marginal depth ladder for a single asset: `asks` represent the buy (mint) side ordered best (lowest) price first, and `bids` represent the sell (redeem) side ordered best (highest) price first. Each level’s `quantity` is the incremental token size available at the level’s marginal `price`. Prices and quantities are decimal strings in human units. When `error` is set, `bids` and `asks` are empty.

updates

SoftQuoteDepth[]

Array of soft-quote depth updates.

Hide SoftQuoteDepth

symbol

string

GM asset symbol.

ticker

string

Underlying stock ticker.

session\_type

string

Trading session the depth was computed for. One of `premarket`, `regular`, `postmarket`, `overnight`, or `offhours`.

error

string

Asset-level failure (e.g. paused, market closed, stale price). When set, `bids` and `asks` are empty.

timestamp

uint64

Unix timestamp of the underlying computation (in nanoseconds).

bids

SoftQuoteDepthLevel[]

Sell side (redeem), best (highest) price first.

Hide SoftQuoteDepthLevel

price

string

Marginal price for this level.

quantity

string

Token quantity available at this level.

asks

SoftQuoteDepthLevel[]

Buy side (mint), best (lowest) price first.

Hide SoftQuoteDepthLevel

price

string

Marginal price for this level.

quantity

string

Token quantity available at this level.

## Streaming behavior

* **Snapshot on subscribe.** On connect, you receive the current depth for each subscribed symbol (when a fresh book is available), followed by live updates as the underlying ladder changes.
* **Batching.** Updates are flushed at most once every ~250 ms per stream. Within a window, only the latest book per symbol is kept, so a newer update supersedes an earlier one buffered in the same window.

## Errors

Asset-level problems (for example, a paused asset or a closed market) are reported inline: the affected `SoftQuoteDepth` entry carries a human-readable `error` with empty `bids` and `asks`, and the stream stays open (see the `GOOGLon` entry in the example).
Request-level problems terminate the stream with a gRPC status:

* `InvalidArgument` (`INVALID_SYMBOL`): a malformed symbol (must be at least 3 characters and end with `on`).
* `NotFound` (`ASSET_NOT_FOUND`): an unknown asset symbol.
* `Unauthenticated` (`MISSING_API_KEY` or `INVALID_API_KEY`): a missing or invalid `x-api-key`.
* `ResourceExhausted` (`RATE_LIMITED`): per-account stream rate limits exceeded.

The reason code in parentheses is carried in the gRPC error details. See [Error Codes](https://docs.ondo.finance/api-reference/error-codes).

[OHLC Streaming](https://docs.ondo.finance/api-reference/ohlc-streaming)[Upcoming API changes](https://docs.ondo.finance/api-reference/upcoming-changes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- session_type
- Trading session the depth was computed for. One of premarket, regular, postmarket, overnight, or offhours.
- Asset-level failure (e.g. paused, market closed, stale price). When set, bids and asks are empty.
- Show SoftQuoteDepthLevel

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#webpage","url":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming","name":"Soft Quote Depth Streaming","description":"gRPC endpoint for real-time, synthetic soft-quote market depth streaming.","dateModified":"2026-07-16T20:06:17.232Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Streaming API","item":"https://docs.ondo.finance/api-reference/protobuf-schema"},{"@type":"ListItem","position":2,"name":"Soft Quote Depth Streaming","item":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#article","headline":"Soft Quote Depth Streaming","name":"Soft Quote Depth Streaming","description":"gRPC endpoint for real-time, synthetic soft-quote market depth streaming.","url":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/soft-quote-depth-streaming#webpage"},"dateModified":"2026-07-16T20:06:17.232Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/status/get-asset-statuses>>>
---
url: https://docs.ondo.finance/api-reference/status/get-asset-statuses
title: Get Asset Statuses - Ondo Finance
description: This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. "Limited" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Asset Statuses

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/assets",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/status/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/assets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "symbol": "XOMon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_LIMITED",
      "message": "earnings",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_limited"
    },
    "start": "2026-01-30T10:00:00Z",
    "end": "2026-01-31T00:30:00Z",
    "eventId": "30fd9cb4-1d64-474f-822d-7f281b8f02ee",
    "updateSharesMultiplier": false
  },
  {
    "symbol": "TIPon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_PAUSED",
      "message": "cash_dividend",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_paused"
    },
    "start": "2026-02-02T00:50:00Z",
    "end": "2026-02-03T01:00:00Z",
    "eventId": "d7d42fbe-9161-45af-806c-c0717453099d",
    "updateSharesMultiplier": true
  },
  "..."
]
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Status

# Get Asset Statuses

Copy pageCopy page

This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures.

**Important**:

* When the entire market is closed or paused as indicated by `/v1/status/market`, all asset trading is automatically suspended regardless of individual asset status. (See [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status))
* Certain assets do not trade during the overnight and pre/postmarket session, as indicated by `/v1/assets/{symbol}/market`. (See [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) / [Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))

This endpoint should be used in conjunction with the [Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status) and [Market Data](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) endpoints to get a complete picture of trading availability.

**Market Sessions and Holidays**

Asset trading follows the same schedule as outlined in [Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status). During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading.

**Earnings and Dividends**

Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule:

* **Dividends**: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date.
* **Earnings**: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. “Limited” here means that the quantity which can be minted in one request is reduced. For exact limits, see [Get Trading Limits](https://docs.ondo.finance/api-reference/limits/get-trading-limits). For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform’s discretion.
* **Cash acquisitions**: When the asset’s issuer is acquired for cash, trading is paused with the reason message `acquisition`. The pause starts 10 minutes before the last market session close on or before the acquisition’s effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report `updateSharesMultiplier` as `false`, because the `sharesMultiplier` does not change.
* **Other corporate actions**: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action.

**Asset Status Reason Codes**

`reason.code` is one of:

* `ASSET_PAUSED`: Asset is paused for trading.
* `ASSET_LIMITED`: Asset can be traded, but order size is more limited than usual.

**Asset Status Reason Messages**

`reason.message` is one of:

* `cash_dividend`
* `stock_dividend`
* `stock_split`
* `merger`
* `acquisition`
* `spinoff`
* `earnings`
* `maintenance`

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

status

/

assets

Try it

Get Asset Statuses

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/assets \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/assets"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/assets', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/assets",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/status/assets"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/assets")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/assets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "symbol": "XOMon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_LIMITED",
      "message": "earnings",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_limited"
    },
    "start": "2026-01-30T10:00:00Z",
    "end": "2026-01-31T00:30:00Z",
    "eventId": "30fd9cb4-1d64-474f-822d-7f281b8f02ee",
    "updateSharesMultiplier": false
  },
  {
    "symbol": "TIPon",
    "status": "upcoming",
    "type": "scheduled",
    "reason": {
      "code": "ASSET_PAUSED",
      "message": "cash_dividend",
      "documentation": "https://docs.ondo.finance/api-reference/error-codes#asset_paused"
    },
    "start": "2026-02-02T00:50:00Z",
    "end": "2026-02-03T01:00:00Z",
    "eventId": "d7d42fbe-9161-45af-806c-c0717453099d",
    "updateSharesMultiplier": true
  },
  "..."
]
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

#### Authorizations

x-api-key

string

header

required

#### Response

200

application/json

OK

symbol

string

required

The GM token symbol.

Example:

`"AAPLon"`

status

enum<string>

required

The current status of the pause. ('active' indicates the pause is live, 'upcoming' indicates it is scheduled for the future)

Available options:

`active`,

`upcoming`

Example:

`"active"`

type

enum<string>

required

The type of pause. ('scheduled' indicates a planned pause for events such as dividends, 'unscheduled' indicates an unplanned pause such as emergency maintenance)

Available options:

`scheduled`,

`unscheduled`

Example:

`"unscheduled"`

reason

object

Reason for an asset trading restriction.

Hide child attributes

reason.message

string

required

The human-readable message describing the reason

Example:

`"Weekend/Holiday"`

reason.documentation

string

required

Additional documentation or reference

Example:

`"https://docs.ondo.finance/"`

reason.code

enum<string>

required

The code indicating the reason for the asset status.

Available options:

`ASSET_PAUSED`,

`ASSET_LIMITED`

Example:

```
{  
  "code": "ASSET_PAUSED",  
  "message": "Maintenance",  
  "documentation": "https://docs.ondo.finance/"  
}
```

start

string

The start time of the pause. ('unscheduled' pauses may not provide a start time.)

Example:

`"2025-08-05T10:30:00Z"`

end

string

The end time of the pause. ('unscheduled' pauses may not provide an end time.)

Example:

`"2025-08-05T10:45:00Z"`

eventId

string

The unique id associated with the pause. (Might be empty if the sharesMultiplier will not be updated for the asset during the pause.)

Example:

`"94fe2f8f-e69c-45a5-9e48-dd8226dd8e67"`

updateSharesMultiplier

enum<boolean>

A boolean flag that indicates whether the sharesMultiplier value will be updated for the asset during this pause or not.

Available options:

`true`,

`false`

Example:

`true`

[Get Current Market Status](https://docs.ondo.finance/api-reference/status/get-current-market-status)[List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- Available options: ASSET_PAUSED, ASSET_LIMITED

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#webpage","url":"https://docs.ondo.finance/api-reference/status/get-asset-statuses","name":"Get Asset Statuses","description":"This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. \"Limited\" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.724Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Status","item":"https://docs.ondo.finance/api-reference/status/get-current-market-status"},{"@type":"ListItem","position":3,"name":"Get Asset Statuses","item":"https://docs.ondo.finance/api-reference/status/get-asset-statuses"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#apireference","headline":"Get Asset Statuses","name":"Get Asset Statuses","description":"This endpoint retrieves information about individual asset trading statuses, including the reason and expected duration. Asset trading can be affected for various reasons such as earnings announcements, dividend events, and global market closures. Important: When the entire market is closed or paused as indicated by /v1/status/market, all asset trading is automatically suspended regardless of individual asset status. (See Get Current Market Status) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) This endpoint should be used in conjunction with the Market Status and Market Data endpoints to get a complete picture of trading availability. Market Sessions and Holidays Asset trading follows the same schedule as outlined in Get Current Market Status. During market closures, holidays, or unscheduled downtime, all assets are unavailable for trading. Earnings and Dividends Individual assets may be temporarily suspended or limited during earnings announcements and dividend events according to the following schedule: - Dividends: Trading is paused from 7:50 PM to 8:10 PM ET on the day before the dividend ex-date. - Earnings: Trading is limited for certain assets around earnings announcements, with timing dependent on the announcement schedule. \"Limited\" here means that the quantity which can be minted in one request is reduced. For exact limits, see Get Trading Limits. For pre-market announcements, trading is suspended from 5:00 AM to 9:31 AM ET. For post-market announcements, trading is suspended from 4:00 PM to 7:30 PM ET. Trading may resume earlier at the platform's discretion. - Cash acquisitions: When the asset's issuer is acquired for cash, trading is paused with the reason message acquisition. The pause starts 10 minutes before the last market session close on or before the acquisition's effective date. The reported pause end time is 30 days after the first market session on the effective date, but Ondo may shorten the pause after reviewing the deal. Acquisition pauses report updateSharesMultiplier as false, because the sharesMultiplier does not change. - Other corporate actions: Trading is paused for an indeterminate amount of time as needed for Ondo to process the corporate action. Asset Status Reason Codes reason.code is one of: - ASSET_PAUSED: Asset is paused for trading. - ASSET_LIMITED: Asset can be traded, but order size is more limited than usual. Asset Status Reason Messages reason.message is one of: - cash_dividend - stock_dividend - stock_split - merger - acquisition - spinoff - earnings - maintenance For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/status/get-asset-statuses","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/status/get-asset-statuses#webpage"},"dateModified":"2026-11-12T23:40:59.724Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/status/get-current-market-status>>>
---
url: https://docs.ondo.finance/api-reference/status/get-current-market-status
title: Get Current Market Status - Ondo Finance
description: This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Current Market Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/market",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/status/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/market")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
{
  "timestamp": "2025-08-20T21:03:02Z",
  "isOpen": true,
  "marketStatus": "postmarket",
  "nextOpenSession": "overnight",
  "offhours": {
    "isOpen": false,
    "nextOpen": "2026-06-19T00:05:00Z",
    "nextClose": "2026-06-21T23:55:00Z"
  },
  "nextOpen": "2025-08-21T00:05:00Z",
  "nextClose": "2025-08-20T23:59:00Z",
  "reason": null
}
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Status

# Get Current Market Status

Copy pageCopy page

This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time.

**Typical Market Sessions**

The following table outlines the standard market sessions with brief transitional pauses between each session period.

| **Session** | **Start Time** | **End Time** |
| --- | --- | --- |
| Pause | 3:55 AM ET | 4:01 AM ET |
| **Premarket** | **4:01 AM ET** | **9:29 AM ET** |
| Pause | 9:29 AM ET | 9:31 AM ET |
| **Regular** | **9:31 AM ET** | **3:59 PM ET** |
| Pause | 3:59 PM ET | 4:01 PM ET |
| **Postmarket** | **4:01 PM ET** | **7:59 PM ET** |
| Pause | 7:59 PM ET | 8:05 PM ET |
| **Overnight** | **8:05 PM ET** | **3:55 AM ET** |

**Typical Holidays**

GM observes the same holiday schedule as the [New York Stock Exchange](https://www.nyse.com/markets/hours-calendars). This includes early closes and observed holidays.

**Unscheduled Downtime**

In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM’s functionality.

**Market Status Reason Codes**

When the market is not open, the response will include a `reason` field which may include one of the following common codes:

* `MARKET_CLOSED`: Market is closed.
* `MARKET_PAUSED`: Market is temporarily paused.

**Off-Hours Trading**

The `offhours` object reports the off-hours trading window as a parallel track alongside the conventional sessions. `marketStatus`, `isOpen`, `nextOpenSession`, `nextOpen`, and `nextClose` only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as `closed` on these fields. Off-hours tradability is reported separately via `offhours.isOpen`, `offhours.nextOpen`, and `offhours.nextClose`. The `offhours.nextOpen` and `offhours.nextClose` schedule fields are reported regardless of the off-hours global switch, while `offhours.isOpen` is true only when the off-hours window is tradable.

**Asset Tradability**
This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints:

* Individual assets may pause for dividends and other events, as indicated by `/v1/status/assets`. (See [Get Asset Statuses](https://docs.ondo.finance/api-reference/status/get-asset-statuses))
* Certain assets do not trade during the overnight and pre/postmarket session, as indicated by `/v1/assets/{symbol}/market`. (See [Get Market Data for an Asset](https://docs.ondo.finance/api-reference/assets/get-market-data-for-an-asset) / [Get Market Data for All Supported Assets](https://docs.ondo.finance/api-reference/assets/get-market-data-for-all-supported-assets))

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

status

/

market

Try it

Get Current Market Status

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/status/market \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/status/market"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/status/market', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/status/market",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/status/market"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/status/market")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/status/market")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
{
  "timestamp": "2025-08-20T21:03:02Z",
  "isOpen": true,
  "marketStatus": "postmarket",
  "nextOpenSession": "overnight",
  "offhours": {
    "isOpen": false,
    "nextOpen": "2026-06-19T00:05:00Z",
    "nextClose": "2026-06-21T23:55:00Z"
  },
  "nextOpen": "2025-08-21T00:05:00Z",
  "nextClose": "2025-08-20T23:59:00Z",
  "reason": null
}
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

#### Authorizations

x-api-key

string

header

required

#### Response

200

application/json

OK

timestamp

string

required

The UTC timestamp of the market status check in ISO 8601 format.

Example:

`"2025-08-20T21:03:02Z"`

isOpen

boolean

required

Indicates whether the market is currently open or closed to trading.

Example:

`true`

marketStatus

enum<string>

required

The current status of the market. `offhours` indicates an off-hours session (such as weekends, the window after the Friday postmarket close, or eligible holidays) during which trading is enabled for assets that opt in to off-hours trading. Off-hours is only reported when off-hours trading is enabled; otherwise the same windows report as `closed`.

Available options:

`regular`,

`premarket`,

`postmarket`,

`overnight`,

`offhours`,

`paused`,

`closed`

Example:

`"postmarket"`

nextOpenSession

enum<string>

required

The next market open session of the market. May be `offhours` when the next available trading window is an off-hours session.

Available options:

`regular`,

`premarket`,

`postmarket`,

`overnight`,

`offhours`

Example:

`"overnight"`

offhours

object

required

Status of the off-hours trading window, surfaced as a parallel track alongside the conventional session fields. The off-hours window is reported independently of the conventional sessions: `marketStatus` and `isOpen` reflect only the four conventional sessions (regular, premarket, postmarket, overnight), while this object reports off-hours tradability separately.

Hide child attributes

offhours.isOpen

boolean

required

Indicates whether off-hours trading is currently open. This is true only while the off-hours window is tradable and the off-hours global switch is on.

Example:

`false`

offhours.nextOpen

string

required

The next off-hours window open time in ISO 8601 format (UTC). Reported regardless of the off-hours global switch.

Example:

`"2026-06-19T00:05:00Z"`

offhours.nextClose

string

required

The next off-hours window close time in ISO 8601 format (UTC). Reported regardless of the off-hours global switch.

Example:

`"2026-06-21T23:55:00Z"`

nextOpen

string

The next market open time in ISO 8601 format (UTC).

Example:

`"2025-08-21T00:05:00Z"`

nextClose

string

The next market close time in ISO 8601 format (UTC).

Example:

`"2025-08-20T23:59:00Z"`

reason

object

Reason for market closure or pause.

Hide child attributes

reason.message

string

required

The human-readable message describing the reason

Example:

`"Weekend/Holiday"`

reason.documentation

string

required

Additional documentation or reference

Example:

`"https://docs.ondo.finance/"`

reason.code

enum<string>

required

The code indicating the reason for the market status.

Available options:

`MARKET_CLOSED`,

`MARKET_PAUSED`

Example:

`null`

[Get Session Limits](https://docs.ondo.finance/api-reference/limits/get-session-limits)[Get Asset Statuses](https://docs.ondo.finance/api-reference/status/get-asset-statuses)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby
- Available options: MARKET_CLOSED, MARKET_PAUSED

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#webpage","url":"https://docs.ondo.finance/api-reference/status/get-current-market-status","name":"Get Current Market Status","description":"This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.709Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Current Market Status","item":"https://docs.ondo.finance/api-reference/status/get-current-market-status"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#apireference","headline":"Get Current Market Status","name":"Get Current Market Status","description":"This endpoint retrieves the current status of the market, including whether it is open or closed, and any relevant information about trading pauses or restrictions. When the market is not open, the response provides details about the closure reason and expected reopening time. Typical Market Sessions The following table outlines the standard market sessions with brief transitional pauses between each session period. | Session | Start Time | End Time | |:-----------------|:---------------:|:--------------:| | Pause | 3:55 AM ET | 4:01 AM ET | | Premarket | 4:01 AM ET | 9:29 AM ET | | Pause | 9:29 AM ET | 9:31 AM ET | | Regular | 9:31 AM ET | 3:59 PM ET | | Pause | 3:59 PM ET | 4:01 PM ET | | Postmarket | 4:01 PM ET | 7:59 PM ET | | Pause | 7:59 PM ET | 8:05 PM ET | | Overnight | 8:05 PM ET | 3:55 AM ET | Typical Holidays GM observes the same holiday schedule as the New York Stock Exchange. This includes early closes and observed holidays. Unscheduled Downtime In the case of unscheduled downtime, trading may be paused without prior notice. This includes unexpected outages or maintenance events that impact GM's functionality. Market Status Reason Codes When the market is not open, the response will include a reason field which may include one of the following common codes: - MARKET_CLOSED: Market is closed. - MARKET_PAUSED: Market is temporarily paused. Off-Hours Trading The offhours object reports the off-hours trading window as a parallel track alongside the conventional sessions. marketStatus, isOpen, nextOpenSession, nextOpen, and nextClose only reflect the four conventional sessions (regular, premarket, postmarket, overnight); a weekend or holiday with no active conventional session reads as closed on these fields. Off-hours tradability is reported separately via offhours.isOpen, offhours.nextOpen, and offhours.nextClose. The offhours.nextOpen and offhours.nextClose schedule fields are reported regardless of the off-hours global switch, while offhours.isOpen is true only when the off-hours window is tradable. Asset Tradability This endpoint only returns market-wide closures. For per-asset tradability, use the following endpoints: Individual assets may pause for dividends and other events, as indicated by /v1/status/assets. (See Get Asset Statuses) Certain assets do not trade during the overnight and pre/postmarket session, as indicated by /v1/assets/{symbol}/market. (See Get Market Data for an Asset / Get Market Data for All Supported Assets) For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/status/get-current-market-status","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/status/get-current-market-status#webpage"},"dateModified":"2026-11-12T23:40:59.709Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers>>>
---
url: https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers
title: Get Price and Volume Data for All Supported Tickers - Ondo Finance
description: This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.
fetched: 2026-11-16
method: render
plan: read
---

Get Price and Volume Data for All Supported Tickers

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/tickers \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/tickers"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/tickers', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/tickers",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/tickers"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/tickers")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/tickers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "tickerId": "TSLAon_USDon",
    "baseCurrency": "TSLAon",
    "targetCurrency": "USDon",
    "lastPrice": 338.42375,
    "baseVolume": 72.720573083,
    "targetVolume": 24610.369044819
  },
  {
    "tickerId": "AAPLon_USDon",
    "baseCurrency": "AAPLon",
    "targetCurrency": "USDon",
    "lastPrice": 228.195452051,
    "baseVolume": 2761.011833446,
    "targetVolume": 630050.34345192
  },
  "..."
]
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

Tickers

# Get Price and Volume Data for All Supported Tickers

Copy pageCopy page

This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market.

For caching details on this endpoint, please see: [Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching).

Copy pageCopy page

GET

/

v1

/

tickers

Try it

Get Price and Volume Data for All Supported Tickers

cURL

```
curl --request GET \
  --url https://api.gm.ondo.finance/v1/tickers \
  --header 'x-api-key: <api-key>'
```

```
import requests

url = "https://api.gm.ondo.finance/v1/tickers"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {'x-api-key': '<api-key>'}};

fetch('https://api.gm.ondo.finance/v1/tickers', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.gm.ondo.finance/v1/tickers",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "x-api-key: <api-key>"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.gm.ondo.finance/v1/tickers"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("x-api-key", "<api-key>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.gm.ondo.finance/v1/tickers")
  .header("x-api-key", "<api-key>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.gm.ondo.finance/v1/tickers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["x-api-key"] = '<api-key>'

response = http.request(request)
puts response.read_body
```

200

401

429

500

```
[
  {
    "tickerId": "TSLAon_USDon",
    "baseCurrency": "TSLAon",
    "targetCurrency": "USDon",
    "lastPrice": 338.42375,
    "baseVolume": 72.720573083,
    "targetVolume": 24610.369044819
  },
  {
    "tickerId": "AAPLon_USDon",
    "baseCurrency": "AAPLon",
    "targetCurrency": "USDon",
    "lastPrice": 228.195452051,
    "baseVolume": 2761.011833446,
    "targetVolume": 630050.34345192
  },
  "..."
]
```

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#missing_api_key"
}
```

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#rate_limited"
}
```

```
{
  "code": "INTERNAL_ERROR",
  "message": "An internal server error occurred. Please see the returned message and documentation for details.",
  "documentation": "https://docs.ondo.finance/api-reference/error-codes#internal_error"
}
```

#### Authorizations

x-api-key

string

header

required

#### Response

200

application/json

OK

tickerId

string

required

The identifier of a ticker, formatted as `<base>_<target>`.

Example:

`"aaplon_usdon"`

baseCurrency

string

required

The GM symbol of the base asset.

Example:

`"AAPLon"`

targetCurrency

string

required

The GM symbol of the target asset.

Example:

`"USDon"`

lastPrice

number

required

The last transacted price of base currency based on given target currency.

Example:

`12.34`

baseVolume

number

required

The 24 hour trading volume for the pair (unit in base).

Example:

`100`

targetVolume

number

required

The 24 hour trading volume for the pair (unit in target).

Example:

`250`

[Get a Portfolio](https://docs.ondo.finance/api-reference/portfolios/get-a-portfolio)[Get Token Balances for a User or Token](https://docs.ondo.finance/api-reference/chains/get-token-balances-for-a-user-or-token)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 펼치거나 눌러야 보이던 내용

- Python
- JavaScript
- Java
- Ruby

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#webpage","url":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers","name":"Get Price and Volume Data for All Supported Tickers","description":"This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.","dateModified":"2026-11-12T23:40:59.632Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"REST API","item":"https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation"},{"@type":"ListItem","position":2,"name":"Get Price and Volume Data for All Supported Tickers","item":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#apireference","headline":"Get Price and Volume Data for All Supported Tickers","name":"Get Price and Volume Data for All Supported Tickers","description":"This endpoint retrieves the latest price and volume data for all supported tickers. A ticker represents a specific asset in the market. For caching details on this endpoint, please see: Endpoint Caching.","url":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/tickers/get-price-and-volume-data-for-all-supported-tickers#webpage"},"dateModified":"2026-11-12T23:40:59.632Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/api-reference/upcoming-changes>>>
---
url: https://docs.ondo.finance/api-reference/upcoming-changes
title: Upcoming API changes - Ondo Finance
description: Advance notice of changes to the Ondo Stocks and Ondo Intelligent Portfolios API so you can prepare your integration before they ship.
fetched: 2026-11-16
method: static
plan: read
---

References

# Upcoming API changes

Copy pageCopy page

Advance notice of changes to the Ondo Stocks and Ondo Intelligent Portfolios API so you can prepare your integration before they ship.

Copy pageCopy page

No upcoming changes to take note of.

[Soft Quote Depth Streaming](https://docs.ondo.finance/api-reference/soft-quote-depth-streaming)[ITN Integration](https://docs.ondo.finance/api-reference/itn-integration)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/upcoming-changes#webpage","url":"https://docs.ondo.finance/api-reference/upcoming-changes","name":"Upcoming API changes","description":"Advance notice of changes to the Ondo Stocks and Ondo Intelligent Portfolios API so you can prepare your integration before they ship.","dateModified":"2026-09-24T00:59:51.975Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/upcoming-changes#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/upcoming-changes#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Upcoming API changes","item":"https://docs.ondo.finance/api-reference/upcoming-changes"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/upcoming-changes#article","headline":"Upcoming API changes","name":"Upcoming API changes","description":"Advance notice of changes to the Ondo Stocks and Ondo Intelligent Portfolios API so you can prepare your integration before they ship.","url":"https://docs.ondo.finance/api-reference/upcoming-changes","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/upcoming-changes#webpage"},"dateModified":"2026-09-24T00:59:51.975Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```