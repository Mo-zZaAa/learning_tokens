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