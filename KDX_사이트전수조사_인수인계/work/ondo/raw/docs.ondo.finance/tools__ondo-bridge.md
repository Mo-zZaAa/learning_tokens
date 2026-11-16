---
url: https://docs.ondo.finance/tools/ondo-bridge
title: Ondo Token Bridge - Ondo Finance
description: 
fetched: 2026-11-16
method: render
plan: read
---

Tools

# Ondo Token Bridge

Copy pageCopy page

Copy pageCopy page

## Introduction

We have partnered with LayerZero, the leading interoperability protocol that has successfully transmitted over 135 million messages and facilitated the exchange of more than $60 billion in value. The integration of LayerZero V2 alongside our enhanced security measures delivers premier security for our users, all while maintaining a seamless user experience.
Every aspect of the [Ondo Token Bridge](https://app.ondo.finance/bridge) is developed with security in mind:

* We’ve carefully selected a set of off-chain verifiers (a.k.a. DVNs), which guarantee strong security through independent actors (minimizing collusion risk) and disparate verification mechanisms (ensuring that even if a bug were to exist in one verifier, that verifier’s actions are mutually exclusive to the others and cannot compromise the overall system).
* We have worked with LayerZero to develop a custom rate limiting implementation and emergency pause feature.
* We have worked closely with a leading Web3 security firm and LayerZero Labs to vet all aspects of the configuration.

## LayerZero Mechanism

At a high level, the LayerZero protocol is a mechanism to securely transmit messages across blockchains.
Decentralized Verification Networks (DVNs) monitor for bridging events from source blockchains, validate these transactions, then post attestations to the destination chains. An executor submits a payload to the destination chain; if the executor’s payload and the DVN attestations match, the USDY or Ondo Stocks are minted to the recipient.
Ondo has employed LayerZero’s OFT (Omnichain Fungible Token) standard to allow users to burn and mint **native USDY and Ondo Stocks** on all supported chains.
Ondo Stocks assets also use the OFT architecture, but with a custom unified multi-asset configuration allowing all Ondo Stocks to be bridged through a unified framework instead of relying on separate bridge configurations for every token on every chain.

## DVN Selections

Our implementation of the OFT Token Bridge leverages the following independent verification mechanisms as DVNs to provide multiple redundant levels of security:

* Canary DVN
* LayerZero Labs DVN
* Ondo DVN

Our custom Ondo DVN was built with unique validation specifically for bridging USDY and Ondo Stocks.

## Chain Availability

### USDY

We currently support USDY transfers between Arbitrum, BNB Chain, Ethereum, Mantle, Sei, Solana, Stellar, and Tempo. Stay tuned for more chain integrations coming soon.

#### Bridging USDY to Stellar

Stellar connects only to Ethereum. To move USDY between Stellar and another chain, bridge through Ethereum first.
You can bridge USDY from Ethereum to a Stellar account (`G...` address). Before you bridge, make sure the destination account has a trustline to USDY (`USDY-GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6`).

A transfer to a Stellar account without a USDY trustline isn’t delivered until you add one.

Transfers from Ethereum to Stellar take about 15 minutes. Transfers from Stellar to Ethereum take about 7 minutes.

### Ondo Stocks

We currently support Ondo Stocks token transfers between Ethereum, BNB Chain, HyperEVM, and Robinhood Chain. Stay tuned for more chain integrations coming soon.

## Rate Limiting

The bridge implementations contain a built-in rate limit feature in the smart contracts, enforcing both an outbound and an inbound limit. The capacity of the rate limiter refills at a linear rate, and blockchain transactions attempting to exceed the rate limit capacity will revert. This security measure enforces an upper bound on the amount that can be transferred per-pathway over a (configurable) 24 hour period.

### USDY

#### EVM ↔ EVM (Arbitrum, BNB Chain, Ethereum, Mantle, Sei, Tempo)

* The **outbound** limit is **450,000 USDY** per pathway per day.
* The **inbound** limit is **500,000 USDY** per pathway per day.

#### Solana ↔ EVM (Arbitrum, BNB Chain, Ethereum, Mantle, Sei, Tempo)

* The **outbound** limit is **250,000 USDY** per pathway per day.
* The **inbound** limit is **300,000 USDY** per pathway per day.

#### Stellar ↔ Ethereum

* The **outbound** limit is **450,000 USDY** per pathway per day.
* The **inbound** limit is **500,000 USDY** per pathway per day.

### Ondo Stocks

Ondo Stocks transfers are currently supported between Ethereum, BNB Chain, HyperEVM, and Robinhood Chain, and are rate-limited separately from USDY:

* Approximately $450,000 per day, per Ondo Stocks asset, per direction
* Limits apply to each individual asset (e.g., AAPLon, NVDAon, SPYon)
* Hyperliquid routes default to approximately $180,000 per day, except for the select high volume tokens (NVDAon, TSLAon, CRCLon, GOOGLon, SLVon) which get the standard limits.

*Note: DVN and rate limit configurations are subject to change by Ondo Finance with the ever-evolving bridging landscape.*

## FAQ

### Can I specify a different destination address for my transfer?

Yes - Ondo’s bridge webpage allows the user to specify a different destination address.

* First, click the edit (pencil) icon next to the address in the Receive section.

  

[그림: Edit Destination Address]

* Next, input the destination address and click Confirm Address.

  

[그림: Input Destination Address]

### Are there any fees associated with transferring tokens?

Transferring tokens comes at no fee on the USDY or Ondo Stocks token amount — you’ll receive the same amount of tokens on the destination chain as you’re sending from the source chain.
However, there are two types of fees paid in the native token of the source chain (such as ETH):

1. **Standard gas fees:** You will pay for the normal gas cost to publish the transaction to the source chain, just like you would for any other transaction. This is handled automatically by your wallet.
2. **Cross-chain gas fees:** Both LayerZero and the DVNs will receive gas fees for publishing your transaction to the destination chain. This is shown under **Cross-chain Fee** in the Order Summary section.
     

   [그림: Cross-Chain Gas Fee]

### How long do transfers take?

Transactions take between 1 and 30 minutes to complete depending on the selected chain path. The tokens will automatically be sent to the recipient wallet on the destination chain.
In cases of network congestion, this may be delayed up to 24 hours.

### Are there any bridging best practices?

When bridging tokens across blockchains, it’s highly recommended to perform a small test transfer before committing to a larger transaction. This allows you to verify that the bridge is functioning correctly, confirm that you’re using the right address and blockchain network, and ensure any fees or delays are clearly understood. Test transfers reduce the risk of potential loss or issues caused by misconfiguration or unforeseen problems during cross-chain transfers.

### My transaction is pending or has failed. What should I do?

In most cases, you can resolve this on your own.
**Check LayerZero Scan**

1. Check the status on the LayerZero explorer. Paste your source chain transaction hash into the search bar at [https://layerzeroscan.com](https://layerzeroscan.com/).
2. On the right-hand side of the page, there may be an **Execute** button. Click this, and connect your wallet.
     

   [그림: Execute Failed LZ Txn]
3. In the provided window, click **Commit and execute**.
     

   [그림: Commit Failed LZ Txn]

If you are unable to resolve the issue and the transfer has not processed after 24 hours, please contact us at [support@ondo.finance](mailto:support@ondo.finance).

[Ondo Stocks Limit Orders](https://docs.ondo.finance/developer-guides/limit-order-contracts)[USDY and mUSD Conversion](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/tools/ondo-bridge#webpage","url":"https://docs.ondo.finance/tools/ondo-bridge","name":"Ondo Token Bridge","dateModified":"2026-11-11T23:20:18.835Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/tools/ondo-bridge#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/tools/ondo-bridge#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Ondo Token Bridge","item":"https://docs.ondo.finance/tools/ondo-bridge"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/tools/ondo-bridge#article","headline":"Ondo Token Bridge","name":"Ondo Token Bridge","url":"https://docs.ondo.finance/tools/ondo-bridge","mainEntityOfPage":{"@id":"https://docs.ondo.finance/tools/ondo-bridge#webpage"},"dateModified":"2026-11-11T23:20:18.835Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```