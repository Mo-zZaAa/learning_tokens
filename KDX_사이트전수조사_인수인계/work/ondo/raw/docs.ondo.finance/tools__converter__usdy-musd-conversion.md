---
url: https://docs.ondo.finance/tools/converter/usdy-musd-conversion
title: USDY and mUSD Conversion - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What is the difference between USDY and mUSD?](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)
* [How can I convert between USDY and mUSD?](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)
* [Convert from the Ondo Finance website](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)
* [Convert from the Mantle Explorer](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)
  + [From USDY to mUSD](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)
  + [From mUSD to USDY](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)

Tools

# USDY and mUSD Conversion

Copy pageCopy page

Copy pageCopy page

# What is the difference between USDY and mUSD?

USDY exists in two forms on Mantle. USDY is the accumulating form, and mUSD is the distributing form.

* USDY: an accumulating ERC-20 token with a redemption value that increases continuously.
* mUSD: a distributing ERC-20 token pegged to $1. mUSD holders automatically receive their yield in their wallet via additional mUSD tokens.

Users receive the same amount of interest regardless of the token they hold.
Users can convert anytime from USDY to mUSD and from mUSD to USDY using the Ondo Token Converter.

# How can I convert between USDY and mUSD?

## Convert from the Ondo Finance website

You can use the Ondo Token Converter on [ondo.finance/convert](https://ondo.finance/convert), where you can connect your wallet and convert your USDY to mUSD and vice-versa.

## Convert from the Mantle Explorer

You will need to interact with two contracts:

* [USDY](https://explorer.mantle.xyz/address/0x5bE26527e817998A7206475496fDE1E68957c5A6/contracts?contract-tab=read-proxy)
* [mUSD](https://explorer.mantle.xyz/address/0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3/contracts?contract-tab=write-proxy)

### From USDY to mUSD

This is a two-transaction process.
**First transaction: Approve mUSD to spend your USDY**
Open the [USDY address in the Mantle explorer](https://explorer.mantle.xyz/address/0x5bE26527e817998A7206475496fDE1E68957c5A6).

* [그림: Click on Contract]
* [그림: Click on Write Proxy]
* [그림: Identify the 'approve' function, and expand it]
* [그림: Insert 0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3 in the spender address. This is the mUSD token address.]
* [그림: Insert the amount of USDY you wish to convert for mUSD, and click on the 10^18 button. In this example, 1 USDY is about to be converted for mUSD.]
* [그림: Click on Write. You will be prompted to connect your wallet, and sign a transaction.]
* [그림: Once the transaction signed, you will see a Success message.]

**Second transaction: Convert USDY to mUSD**

* Open the [mUSD address in the Mantle Explorer](https://explorer.mantle.xyz/address/0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3).
* Similarly to the previous step, click on ‘Contract’, and ‘Write Proxy’.
* Scroll down to identify and expand the wrap function.
* Insert the amount of tokens you wish to convert to mUSD, and click on the 10^18 button.

* [그림: Click Write to sign the transaction (your wallet should already be connected to the explorer)]
* [그림: After confirming in your wallet, you can open the transaction hash in the explorer, and observe the amount of mUSD you received]

### From mUSD to USDY

Open the [mUSD address in the Mantle Explorer](https://explorer.mantle.xyz/address/0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3).

* [그림: Click on Contract]
* [그림: Click on Write Proxy]
* [그림: Scroll down to identify the 'unwrap' function]
* [그림: Insert the amount of mUSD you wish to convert to USDY, and click on the 10^18 button. In this example, 1 mUSD is about to be converted to USDY]
* [그림: Click on Write. You will be prompted to connect your wallet and sign a transaction]
* [그림: Once the transaction is signed, you will see a Success message]
* [그림: Clicking on the transaction link shows you the amount of USDY that you received in your wallet. In this example, 1 mUSD got converted to 0.9882 USDY]

[Ondo Token Bridge](https://docs.ondo.finance/tools/ondo-bridge)[Smart Contract Addresses](https://docs.ondo.finance/addresses)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion#webpage","url":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion","name":"USDY and mUSD Conversion","dateModified":"2026-11-07T00:41:58.082Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.ondo.finance/tools/ondo-bridge"},{"@type":"ListItem","position":2,"name":"USDY and mUSD Conversion","item":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion#article","headline":"USDY and mUSD Conversion","name":"USDY and mUSD Conversion","url":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion","mainEntityOfPage":{"@id":"https://docs.ondo.finance/tools/converter/usdy-musd-conversion#webpage"},"dateModified":"2026-11-07T00:41:58.082Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```