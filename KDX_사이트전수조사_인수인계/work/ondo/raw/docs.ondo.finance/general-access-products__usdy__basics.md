---
url: https://docs.ondo.finance/general-access-products/usdy/basics
title: USDY Basics - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What is USDY?](https://docs.ondo.finance/general-access-products/usdy/basics)
* [How does it work?](https://docs.ondo.finance/general-access-products/usdy/basics)
  + [Investing](https://docs.ondo.finance/general-access-products/usdy/basics)
  + [Redeeming](https://docs.ondo.finance/general-access-products/usdy/basics)
  + [Minting and Redeeming on Other Networks](https://docs.ondo.finance/general-access-products/usdy/basics)
* [Understanding rUSDY](https://docs.ondo.finance/general-access-products/usdy/basics)

USDY

# USDY Basics

Copy pageCopy page

Copy pageCopy page

## What is USDY?

USDY (**US** **D**ollar **Y**ield Token) is a tokenized note formerly issued by Ondo USDY LLC, which as of December 15, 2025 has been folded into the Ondo Stocks umbrella. Depending on the issuance date, USDY may be secured by either short-term US Treasuries, shares of iShares Short Treasury Bond ETF, or bank demand deposits. USDY is accessible to qualifying non-US individual and institutional investors and is designed to combine the accessibility of a stablecoin with high-quality, US dollar-denominated yield.USDY comes in two versions: an “accumulating” version (USDY) whose per-token price increases as yield accrues, and a “rebasing” version (rUSDY) whose price remains at $1.00. Whereas the price of USDY tokens increases as the value of the underlying assets increase, with rUSDY you simply receive more rUSDY in your wallet; in effect the yield on the underlying assets accrues in the form of additional rUSDY tokens. For example, if you acquired 100 rUSDY tokens when the price per token of USDY was $1.00 – and then the price per token of USDY increased to $1.01, the price per token of rUSDY would remain at $1.00, but your wallet would now hold 101 rUSDY tokens. This ‘rebasing’ happens automatically and continuously as the USDY price grows. The USDY price is calculated continuously on Ethereum, BNB Chain, Mantle and Tempo. On other chains, it is bridged from these four chains.You can easily and instantly convert back and forth between USDY and rUSDY on our [website](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy) at any time.

|  | USDY | rUSDY |
| --- | --- | --- |
| Token Type | Accumulating | Rebasing (distributing) |
| Yield Accrual Profile | Reflected through an increasing redemption price (Reference Token Price) | Reflected as a continuous subdivision of rUSDY tokens into additional rUSDY tokens |
| As Treasury Yield Accrues, the Token Price | Increases | Remains at $1.00 |
| Best Suited for | Buy-and-hold cash management (some custodians only support accumulating tokens), collateral in smart contracts | Yield-bearing means of settlement or exchange |

## How does it work?

### Investing

Once your onboarding is completed, you can mint USDY with USDC at any time. (For deposits of $100K plus, USD bank wires are also possible. Contact us at [support@ondo.finance](mailto:support@ondo.finance) for more information.) You will start earning interest as soon as your transaction is processed. For all current purchases of USDY through the web app, please see the [terms for Ondo Stocks](https://app.ondo.finance/assets/usdy?tab=buy&fromToken=usdc&toToken=usdy).

### Redeeming

Note that to comply with applicable US laws and regulations, Ondo USDY LLC can only redeem USD via bank wire to non-US bank accounts. If you wish to redeem via this method you will be required to provide us with such bank details before we can process a redemption request. To redeem for USDC through Ondo Global Markets (BVI) Limited, please go [here](https://app.ondo.finance/assets/usdy?tab=buy&fromToken=usdc&toToken=usdy).For more information on Ondo Global Markets (BVI) Limited see the [Ondo Stocks section](https://docs.ondo.finance/ondo-stocks/overview) of these docs.

### Minting and Redeeming on Other Networks

To mint and redeem USDY on Sui, Aptos, Stellar, XRP, or Noble, please contact [support@ondo.finance](mailto:support@ondo.finance). Please note that that there is a $5,000 minimum for minting and redeeming on these networks.

## Understanding rUSDY

**rUSDY = A Type of ‘Wrapped’ USDY**It’s important to understand that each rUSDY still corresponds to some amount of “regular” USDY that is locked in a wrapper contract. This wrapper contract locks the USDY in the contract, mints the corresponding amount of rUSDY, and sends that rUSDY to your wallet. For example, if you had 1,000 USDY tokens worth $10 each — so, a total of $10,000 of value — the 1,000 USDY would be locked in the wrapper contract, which would then mint 10,000 rUSDY tokens and then send those to your wallet. Conversely, if you wanted to [convert](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy) your rUSDY tokens back to USDY tokens, your rUSDY tokens would be sent to the wrapper contract. This wrapper would then burn the rUSDY tokens, “unlock” the corresponding number of USDY tokens, and send those USDY tokens to your wallet.This means that the *total* supply of USDY is comprised of two ‘types’ of USDY:

* **Wrapped USDY** - i.e. USDY that is locked in the rUSDY wrapper contract and corresponds to the ‘reserve’ for the corresponding issued rUSDY.
* **Non-Wrapped USDY** — i.e. USDY that *isn’t* locked in the rUSDY wrapper contract.

There are three important implications of this:

* The “dollar value” that is represented by all rUSDY tokens is exactly equal to the amount of “dollar value” represented by all applicable wrapped USDY tokens. In other words, `TVL_rUSDY = TVL_Wrapped_USDY` → `TVL_rUSDY = Num_Wrapped_USDY_Tokens * TokenReferencePrice_per_USDY` (Token Reference Price is the ‘face value’ of the token).
* Because of this, if you were to add up the total amount of USDY and the amount of rUSDY, you would be *double counting the value of the wrapped USDY*, because some of that value is already represented by the rUSDY.
* Therefore, to properly calculate the TVL of USDY, the appropriate calculation is as follows:

`Total USDY TVL (e.g. both versions) = Num_rUSDY_Tokens * $1.00 + Num_Non-Wrapped_USDY_Tokens * TokenReferencePrice_per_USDY`OR`Total USDY TVL (e.g. both versions) = (Num_Wrapped_USDY_Tokens + Num_Non-Wrapped_USDY_Tokens) * TokenReferencePrice_per_USDY`i.e. the two calculations should result in the same number (adjusting for rounding).**rUSDY Price Stability via Rebasing**Rebasing is a mechanism through which the total supply of tokens is adjusted. The basic intuition is that, if we’re trying to keep the price per token at $1.00, as the value of rUSDY’s underlying assets increase in value, we need to increase the number of tokens such that the “value of assets” divided by the number of tokens remains constant. For tokens like USDY and rUSDY, the redemption value of the rUSDY token can be calculated by dividing the TVL of the rUSDY share class by the number of rUSDY tokens`TokenReferencePrice_per_rUSDY = TVL_rUSDY / Num_rUSDY_Tokens`From above, recall that `TVL_rUSDY = Num_Wrapped_USDY_Tokens * TokenReferencePrice_per_USDY`, so we have `TokenReferencePrice_per_rUSDY = (Num_Wrapped_USDY_Tokens * TokenReferencePrice_per_USDY) / Num_rUSDY_Tokens` Therefore, as `TokenReferencePrice_per_USDY` increases continuously based on the current Token yield rate, `TokenReferencePrice_per_rUSDY` would *also* increase…unless we also increased `Num_rUSDY_Tokens`. Since we want to keep `TokenReferencePrice_per_rUSDY` at $1.00, this means that we must increase `Num_rUSDY_Tokens` to keep the price at $1.00.For more technical details on how rebasing works, you can read more [here](https://docs.ondo.finance/general-access-products/usdy/rebasing). For more detailed information about USDY, please refer to the rest of these support docs or reach out to us at [support@ondo.finance](mailto:support@ondo.finance)

[Legal](https://docs.ondo.finance/private-markets/legal)[Comparison to Stablecoins](https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/basics#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/basics","name":"USDY Basics","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/basics#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/basics#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"USDY Basics","item":"https://docs.ondo.finance/general-access-products/usdy/basics"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/basics#article","headline":"USDY Basics","name":"USDY Basics","url":"https://docs.ondo.finance/general-access-products/usdy/basics","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/basics#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```