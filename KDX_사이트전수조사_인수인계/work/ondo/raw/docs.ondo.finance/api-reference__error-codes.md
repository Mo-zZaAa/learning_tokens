---
url: https://docs.ondo.finance/api-reference/error-codes
title: Error Codes - Ondo Finance
description: Reference for all error codes returned by the GM Backend API.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Error Codes](https://docs.ondo.finance/api-reference/error-codes)
  + [MARKET\_CLOSED](https://docs.ondo.finance/api-reference/error-codes)
  + [MARKET\_PAUSED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_PAUSED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_LIMITED](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_CLOSED\_FOR\_SESSION](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_REDEEM\_ONLY](https://docs.ondo.finance/api-reference/error-codes)
  + [READ\_ONLY\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_API\_KEY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SYMBOL](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_SYMBOL](https://docs.ondo.finance/api-reference/error-codes)
  + [ASSET\_NOT\_FOUND](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SIDE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_DURATION](https://docs.ondo.finance/api-reference/error-codes)
  + [MAX\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [SESSION\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [MAX\_ATTESTATIONS](https://docs.ondo.finance/api-reference/error-codes)
  + [OFFHOURS\_EXPOSURE\_LIMIT\_REACHED](https://docs.ondo.finance/api-reference/error-codes)
  + [INSUFFICIENT\_LIQUIDITY](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_NOTIONAL\_VALUE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_TOKEN\_AMOUNT](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_TOKEN\_OR\_NOTIONAL](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_CHAIN\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_SIDE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [UNSUPPORTED\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [PAUSED\_GM\_CHAIN](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_SORT](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_INTERVAL](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_RANGE](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_INTERVAL\_RANGE\_PAIR](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_TICKER\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_TICKER\_ID](https://docs.ondo.finance/api-reference/error-codes)
  + [RESOURCE\_NOT\_FOUND](https://docs.ondo.finance/api-reference/error-codes)
  + [MISSING\_USER\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [INVALID\_USER\_ADDRESS](https://docs.ondo.finance/api-reference/error-codes)
  + [GAS\_FEE\_EXCEEDS\_ORDER\_VALUE](https://docs.ondo.finance/api-reference/error-codes)
  + [ITN\_ACCOUNT\_NOT\_ELIGIBLE](https://docs.ondo.finance/api-reference/error-codes)
  + [ITN\_UNAVAILABLE](https://docs.ondo.finance/api-reference/error-codes)
  + [RATE\_LIMITED](https://docs.ondo.finance/api-reference/error-codes)
  + [INTERNAL\_ERROR](https://docs.ondo.finance/api-reference/error-codes)

References

# Error Codes

Copy pageCopy page

Reference for all error codes returned by the GM Backend API.

Copy pageCopy page

The Ondo Stocks & Intelligent Portfolios APIs return structured error messages with three key fields:

* **code**: Machine-readable identifier (e.g., `MARKET_CLOSED`)
* **message**: Human-readable description
* **documentation**: URL linking to relevant documentation

## Error Codes

### MARKET\_CLOSED

**Status**: 403 Forbidden

```
{
  "code": "MARKET_CLOSED",
  "message": "market is closed"
}
```

The market is closed due to weekends, holidays, or scheduled/unscheduled closures from maintenance or exchange outages.

---

### MARKET\_PAUSED

**Status**: 403 Forbidden

```
{
  "code": "MARKET_PAUSED",
  "message": "market is paused"
}
```

Trading is temporarily paused, either during scheduled session transitions (09:29-09:31 ET) or unscheduled halts (circuit breaker triggers).

---

### ASSET\_PAUSED

**Status**: 403 Forbidden

```
{
  "code": "ASSET_PAUSED",
  "message": "asset trading is paused"
}
```

Trading for a specific asset is paused, possibly due to corporate actions, symbol migration, or market volatility.

---

### ASSET\_LIMITED

**Status**: 200 OK

```
{
  "code": "ASSET_LIMITED",
  "message": "Earnings event in progress"
}
```

Returned as a reason code within asset status responses (not as an error). Indicates the asset has limited trading capacity, typically during earnings events. Trading is still permitted, but quantity may be restricted.

---

### ASSET\_CLOSED\_FOR\_SESSION

**Status**: 403 Forbidden

```
{
  "code": "ASSET_CLOSED_FOR_SESSION",
  "message": "asset is not available for trading during the current session"
}
```

The asset isn’t tradable in the current session (“premarket”, “regular”, “postmarket”, “overnight”, or “offhours”).

---

### ASSET\_REDEEM\_ONLY

**Status**: 403 Forbidden

```
{
  "code": "ASSET_REDEEM_ONLY",
  "message": "asset is redeem-only"
}
```

The asset can only be redeemed (sold), not minted (bought).

---

### READ\_ONLY\_API\_KEY

**Status**: 403 Forbidden

```
{
  "code": "READ_ONLY_API_KEY",
  "message": "read-only API key cannot perform write operations"
}
```

The API key used is read-only and cannot create attestations or perform other write operations.

---

### MISSING\_API\_KEY

**Status**: 401 Unauthorized

```
{
  "code": "MISSING_API_KEY",
  "message": "missing API key"
}
```

No API key was provided in the `x-api-key` request header.

---

### INVALID\_API\_KEY

**Status**: 401 Unauthorized

```
{
  "code": "INVALID_API_KEY",
  "message": "invalid API key"
}
```

The provided API key is not valid or has been revoked.

---

### INVALID\_SYMBOL

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SYMBOL",
  "message": "invalid symbol; must be at least 3 characters long and end with 'on'"
}
```

The symbol is invalid, unrecognized, or improperly formatted. Use valid namespaced symbols (e.g., `TSLAon`, `AAPLon`).

---

### MISSING\_SYMBOL

**Status**: 400 Bad Request

```
{
  "code": "MISSING_SYMBOL",
  "message": "missing symbol"
}
```

The required `symbol` parameter was not provided.

---

### ASSET\_NOT\_FOUND

**Status**: 404 Not Found

```
{
  "code": "ASSET_NOT_FOUND",
  "message": "asset not found"
}
```

The specified asset does not exist in the system.

---

### INVALID\_SIDE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SIDE",
  "message": "invalid side; side must be either 'buy' or 'sell'"
}
```

The `side` parameter must be either `buy` or `sell`.

---

### INVALID\_DURATION

**Status**: 400 Bad Request

```
{
  "code": "INVALID_DURATION",
  "message": "invalid duration; duration must be either 'long' or 'short'"
}
```

The `duration` parameter must be either `long` or `short`.

---

### MAX\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "MAX_LIMIT_REACHED",
  "message": "exceeded the active notional value limit"
}
```

The order exceeds user-based notional caps. Limits reset when attestations expire.

---

### SESSION\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "SESSION_LIMIT_REACHED",
  "message": "exceeded the session's notional value limit"
}
```

The order exceeds session-based notional caps, which reset after each session transition.

---

### MAX\_ATTESTATIONS

**Status**: 400 Bad Request

```
{
  "code": "MAX_ATTESTATIONS",
  "message": "exceeded the active attestations limit"
}
```

Maximum concurrent attestation requests reached. Wait for some to settle before requesting more.

---

### OFFHOURS\_EXPOSURE\_LIMIT\_REACHED

**Status**: 400 Bad Request

```
{
  "code": "OFFHOURS_EXPOSURE_LIMIT_REACHED",
  "message": "off-hours exposure limit reached"
}
```

The off-hours exposure limit has been reached for the asset during the current off-hours session. Wait for the next session to open, or trade a different asset.

---

### INSUFFICIENT\_LIQUIDITY

**Status**: 400 Bad Request

```
{
  "code": "INSUFFICIENT_LIQUIDITY",
  "message": "insufficient liquidity for the requested operation"
}
```

An attestation cannot be created due to insufficient funds, typically during sparse overnight trading.

---

### INVALID\_NOTIONAL\_VALUE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_NOTIONAL_VALUE",
  "message": "invalid notional value; value must be a string representing a positive decimal value"
}
```

The amount is below minimum requirements, above user limits, or malformed/non-numeric.

---

### INVALID\_TOKEN\_AMOUNT

**Status**: 400 Bad Request

```
{
  "code": "INVALID_TOKEN_AMOUNT",
  "message": "invalid token amount; amount must be a string representing a positive decimal value"
}
```

The token amount is malformed or not a positive decimal value.

---

### MISSING\_TOKEN\_OR\_NOTIONAL

**Status**: 400 Bad Request

```
{
  "code": "MISSING_TOKEN_OR_NOTIONAL",
  "message": "either token amount or notional value must be provided"
}
```

The request must include either `tokenAmount` or `notionalValue`, but neither was provided.

---

### INVALID\_ADDRESS

**Status**: 403 Forbidden

```
{
  "code": "INVALID_ADDRESS",
  "message": "user_address is not on the allow list"
}
```

The provided wallet address is not whitelisted for trading.

---

### MISSING\_CHAIN\_ID

**Status**: 400 Bad Request

```
{
  "code": "MISSING_CHAIN_ID",
  "message": "chainId is required"
}
```

The required `chainId` parameter was not provided in the request.

---

### MISSING\_SIDE

**Status**: 400 Bad Request

```
{
  "code": "MISSING_SIDE",
  "message": "side is required"
}
```

The required `side` parameter was not provided in the request.

---

### INVALID\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "INVALID_GM_CHAIN",
  "message": "invalid chain; supported chains: ethereum-1, bsc-56, solana-900"
}
```

The specified chain is not a valid GM chain identifier.

---

### UNSUPPORTED\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "UNSUPPORTED_GM_CHAIN",
  "message": "unsupported chain"
}
```

The specified chain is recognized but not currently supported for the requested operation.

---

### PAUSED\_GM\_CHAIN

**Status**: 400 Bad Request

```
{
  "code": "PAUSED_GM_CHAIN",
  "message": "chain is paused"
}
```

The specified chain is temporarily paused and not accepting requests.

---

### INVALID\_SORT

**Status**: 400 Bad Request

```
{
  "code": "INVALID_SORT",
  "message": "invalid sort order; must be 'asc' or 'desc'"
}
```

The `sort` query parameter is invalid. Valid values are `asc` or `desc`.

---

### INVALID\_INTERVAL

**Status**: 400 Bad Request

```
{
  "code": "INVALID_INTERVAL",
  "message": "invalid interval format: 2hour"
}
```

The `interval` query parameter is not a valid value. Valid intervals are `1min`, `5min`, `15min`, `1hour`, `4hour`, `12hour`, and `1day`.

---

### INVALID\_RANGE

**Status**: 400 Bad Request

```
{
  "code": "INVALID_RANGE",
  "message": "invalid time range: 2month; valid ranges: 1day, 1month, 3month, 6month, 1year, all"
}
```

The `range` query parameter is not a valid value. Valid ranges are `1day`, `1month`, `3month`, `6month`, `1year`, and `all`.

---

### INVALID\_INTERVAL\_RANGE\_PAIR

**Status**: 400 Bad Request

```
{
  "code": "INVALID_INTERVAL_RANGE_PAIR",
  "message": "invalid interval/range pair: 1min/1year; valid pairs: 1min/1day, 5min/1day, 15min/1day, 1hour/1month, 4hour/3month, 12hour/6month, 1day/1year, 1day/all"
}
```

The combination of `interval` and `range` parameters is not supported. See the OHLC endpoint documentation for valid pairs.

---

### MISSING\_TICKER\_ID

**Status**: 400 Bad Request

```
{
  "code": "MISSING_TICKER_ID",
  "message": "missing ticker ID"
}
```

The required `tickerId` parameter was not provided.

---

### INVALID\_TICKER\_ID

**Status**: 400 Bad Request

```
{
  "code": "INVALID_TICKER_ID",
  "message": "invalid ticker ID"
}
```

The provided `tickerId` is not a valid ticker identifier. Ticker IDs are formatted as `<base>_<target>` (e.g., `AAPLon_USDon`).

---

### RESOURCE\_NOT\_FOUND

**Status**: 404 Not Found

```
{
  "code": "RESOURCE_NOT_FOUND",
  "message": "resource not found"
}
```

The requested resource does not exist.

---

### MISSING\_USER\_ADDRESS

**Status**: 400 Bad Request

```
{
  "code": "MISSING_USER_ADDRESS",
  "message": "missing user address"
}
```

The `user_address` field is required for firm attestation requests on Solana chains but was not provided.

---

### INVALID\_USER\_ADDRESS

**Status**: 400 Bad Request

```
{
  "code": "INVALID_USER_ADDRESS",
  "message": "invalid user address"
}
```

The `user_address` provided for a firm attestation request on a Solana chain is not a valid Solana public key.

---

### GAS\_FEE\_EXCEEDS\_ORDER\_VALUE

**Status**: 400 Bad Request

```
{
  "code": "GAS_FEE_EXCEEDS_ORDER_VALUE",
  "message": "gas fee exceeds order value: increase your order size or try again later"
}
```

The estimated gas fee for executing the order on-chain exceeds the total value of the order. Increase your order size or try again when gas fees are lower.

---

### ITN\_ACCOUNT\_NOT\_ELIGIBLE

**Status**: 403 Forbidden

```
{
  "code": "ITN_ACCOUNT_NOT_ELIGIBLE",
  "message": "account or wallet is not eligible for ITN"
}
```

Your account or wallet is not eligible for ITN. See the [ITN prerequisites](https://docs.ondo.finance/api-reference/itn-integration).

---

### ITN\_UNAVAILABLE

**Status**: 503 Service Unavailable

```
{
  "code": "ITN_UNAVAILABLE",
  "message": "ITN operation is temporarily unavailable"
}
```

ITN minting or redeeming is temporarily unavailable, either platform-wide or for a specific asset. [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status) reports this code as a `reason` when a side is closed. Retry the request after a short time.

---

### RATE\_LIMITED

**Status**: 429 Too Many Requests

```
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded"
}
```

The account has exceeded its request rate limits. Wait briefly and retry with exponential backoff.

---

### INTERNAL\_ERROR

**Status**: 500 Internal Server Error

```
{
  "code": "INTERNAL_ERROR",
  "message": "internal error"
}
```

An unexpected server error occurred. If this persists, contact your account manager.
The [portfolio endpoints](https://docs.ondo.finance/api-reference/portfolios/get-all-portfolios) return this code with status `503 Service Unavailable` when portfolio data is temporarily unavailable. Retry the request after a short time.

---

This list is non-exhaustive. For unresolved issues, consult request documentation or contact us at [support@ondo.finance](mailto:support@ondo.finance).

[Endpoint Caching](https://docs.ondo.finance/api-reference/endpoint-caching)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/error-codes#webpage","url":"https://docs.ondo.finance/api-reference/error-codes","name":"Error Codes","description":"Reference for all error codes returned by the GM Backend API.","dateModified":"2026-11-07T00:34:22.075Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/error-codes#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/error-codes#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"References","item":"https://docs.ondo.finance/api-reference/upcoming-changes"},{"@type":"ListItem","position":2,"name":"Error Codes","item":"https://docs.ondo.finance/api-reference/error-codes"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/error-codes#article","headline":"Error Codes","name":"Error Codes","description":"Reference for all error codes returned by the GM Backend API.","url":"https://docs.ondo.finance/api-reference/error-codes","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/error-codes#webpage"},"dateModified":"2026-11-07T00:34:22.075Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```