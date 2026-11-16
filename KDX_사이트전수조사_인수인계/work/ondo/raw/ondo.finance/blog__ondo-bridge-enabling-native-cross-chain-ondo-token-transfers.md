---
url: https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers
title: Ondo Bridge: Enabling Native, Cross-Chain RWA Transfers | Ondo Finance
description: Today, we're excited to unveil Ondo Bridge, a mechanism for seamlessly transferring Ondo tokens across blockchains. Ondo is partnering with Axelar, incorpor…
fetched: 2026-11-16
method: static
plan: skim
---

In this article

* [Native tokens, many chains](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [State-of-the-art risk management](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [Easy-to-use interface](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [Easy to integrate](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [Learn more](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [About Axelar](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)
* [About Ondo](https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers)

USDY • Nov 13, 2023 • 3 min

# Ondo Bridge: Enabling Native, Cross-Chain RWA Transfers

[Ondo Finance

Official Blog](https://ondo.finance/blog)

[그림: Ondo Bridge: Enabling Native, Cross-Chain RWA Transfers]

Today, we're excited to unveil [Ondo Bridge](https://app.ondo.finance/bridge), a mechanism for seamlessly transferring Ondo tokens across blockchains. Ondo is partnering with [Axelar](https://axelar.network/), incorporating its state-of-the-art, multi-chain communication primitives together with a novel Ondo risk management layer to help investors in Ondo products bridge assets in a safe and efficient manner.

We are launching the Ondo Bridge to allow for seamless transfers of USDY between Ethereum and [Mantle](https://www.mantle.xyz/). USDY is a tokenized note secured by short-term US Treasuries that functions similarly to stablecoins while paying a variable yield to its holders, currently 5.1% APY.

### **Native tokens, many chains**

Tokens transferred via Ondo Bridge are **native** tokens, meaning tokens on both the source and destination chain are issued by Ondo and are not a wrapped replica. This method eliminates the risk associated with custodying tokens on the source chain, while allowing token holders to enjoy the benefits of Ondo assets, such as yield and composability, regardless of the chain they use. Similarly, native bridging promotes unified secondary market liquidity across chains; traders can utilize the bridge to arbitrage token prices across decentralized exchanges (DEXs) on various chains, helping to deliver price stability. Lastly, there is no slippage when transferring tokens; users receive the full amount they transferred on the destination chain.

### **State-of-the-art risk management**

The design of Ondo Bridge employs a meticulously-architected, multi-layer approach, leveraging cross-chain messaging technologies to ensure the secure transfer of tokens across blockchains.

The first layer of this architecture is powered by Axelar, a leader in decentralized cross-chain communication, which provides a solid foundation for the bridge's operations. Axelar's technology orchestrates the preliminary validation and communication between the chains involved.

The second layer, engineered by Ondo, augments the bridge's security by adding a multi-validation mechanism.

The number of total validations depends on the bridge transfer limit parameters, such as transaction size. For instance, a $10,000 transaction requires two validations (one from Axelar and one from Ondo), whereas a multi-million-dollar transaction requires three validations (one from Axelar and two from Ondo). This multi-tiered validation approach adds a dynamic extra security layer while ensuring a strong baseline risk management for any transfer. Over time, more messaging protocols will be added to complement Axelar’s technology.

### **Easy-to-use interface**

Ondo Bridge abides by the permissions of each token; for instance, holders of permissionless tokens and even smart contracts can initiate cross-chain transfers seamlessly.

Using the Ondo Bridge is easy and intuitive, both on desktop and mobile:

1. Connect your wallet to load your balances
2. Select the transfer parameters: the amount of tokens, the source chain, and the destination chain(s). Additional information, like the cross-chain gas fee, is displayed
3. When finalized, you can approve and initiate the token transfer

From there, you can conveniently track the status of your transfer.

### **Easy to integrate**

Bridge aggregators and cross-chain swap technologies can easily integrate Ondo Bridge into their offerings. Please get in touch with [support@ondo.finance](mailto:support@ondo.finance) if you would like to learn more. We are here to help.

### **Learn more**

<https://app.ondo.finance/bridge>

<https://docs.ondo.finance/ondo-bridge>

### **About Axelar**

Axelar is the full-stack interoperability layer for Web3. The network enables blockchain as a new kind of development platform, integrating diverse networks into a seamless “Internet of blockchains.”  Axelar is programmable and decentralized, secured by a proof-of-stake token, AXL. Application users access any digital asset or application, with one click. Developers work with a simple API and access an ecosystem of tools and service providers.

More about Axelar: [axelar.network](https://axelar.network/).

### **About Ondo**

Ondo Finance provides institutional-grade, blockchain-enabled investment products and services. Ondo has an asset management arm that creates and manages tokenized financial products as well as a technology arm that develops decentralized finance protocols and blockchain solutions.

Ondo’s first core products are tokenized cash equivalents that deliver very low risk, high quality yield from U.S. Treasuries, money market funds, and similar instruments, offering on-chain investors an alternative to stablecoins where holders rather than issuers earn the vast majority of the underlying asset yield.

For more information on our products, please reach out to us at [support@ondo.finance](mailto:support@ondo.finance) or check out the following resources:

[Website](https://ondo.finance/) | [X/Twitter](https://twitter.com/ondofinance) | [Blog](https://ondo.finance/blog)

Next

[[그림: Protecting Investors: What Happens if Ondo goes Bankrupt?]

USDY•Sep 7, 2023

### Protecting Investors: What Happens if Ondo goes Bankrupt?](https://ondo.finance/blog/protecting-investors-what-happens-if-ondo-goes-bankrupt)

[[그림: Introducing Ondo USD Yield (USDY)]

USDY•Aug 3, 2023

### Introducing Ondo USD Yield (USDY)](https://ondo.finance/blog/introducing-ondo-usd-yield-usdy)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BlogPosting","headline":"Ondo Bridge: Enabling Native, Cross-Chain RWA Transfers","description":"Today, we're excited to unveil Ondo Bridge, a mechanism for seamlessly transferring Ondo tokens across blockchains. Ondo is partnering with Axelar, incorpor…","articleBody":"Today, we're excited to unveil Ondo Bridge, a mechanism for seamlessly transferring Ondo tokens across blockchains. Ondo is partnering with Axelar, incorporating its state-of-the-art, multi-chain communication primitives together with a novel Ondo risk management layer to help investors in Ondo products bridge assets in a safe and efficient manner.\n\nWe are launching the Ondo Bridge to allow for seamless transfers of USDY between Ethereum and Mantle. USDY is a tokenized note secured by short-term US Treasuries that functions similarly to stablecoins while paying a variable yield to its holders, currently 5.1% APY.\nNative tokens, many chains\n\nTokens transferred via Ondo Bridge are native tokens, meaning tokens on both the source and destination chain are issued by Ondo and are not a wrapped replica. This method eliminates the risk associated with custodying tokens on the source chain, while allowing token holders to enjoy the benefits of Ondo assets, such as yield and composability, regardless of the chain they use. Similarly, native bridging promotes unified secondary market liquidity across chains; traders can utilize the bridge to arbitrage token prices across decentralized exchanges (DEXs) on various chains, helping to deliver price stability. Lastly, there is no slippage when transferring tokens; users receive the full amount they transferred on the destination chain.\nState-of-the-art risk management\n\nThe design of Ondo Bridge employs a meticulously-architected, multi-layer approach, leveraging cross-chain messaging technologies to ensure the secure transfer of tokens across blockchains.\n\nThe first layer of this architecture is powered by Axelar, a leader in decentralized cross-chain communication, which provides a solid foundation for the bridge's operations. Axelar's technology orchestrates the preliminary validation and communication between the chains involved.\n\nThe second layer, engineered by Ondo, augments the bridge's security by adding a multi-validation mechanism.\n\nThe number of total validations depends on the bridge transfer limit parameters, such as transaction size. For instance, a $10,000 transaction requires two validations (one from Axelar and one from Ondo), whereas a multi-million-dollar transaction requires three validations (one from Axelar and two from Ondo). This multi-tiered validation approach adds a dynamic extra security layer while ensuring a strong baseline risk management for any transfer. Over time, more messaging protocols will be added to complement Axelar’s technology.\nEasy-to-use interface\n\nOndo Bridge abides by the permissions of each token; for instance, holders of permissionless tokens and even smart contracts can initiate cross-chain transfers seamlessly.\n\nUsing the Ondo Bridge is easy and intuitive, both on desktop and mobile:\nConnect your wallet to load your balances\nSelect the transfer parameters: the amount of tokens, the source chain, and the destination chain(s). Additional information, like the cross-chain gas fee, is displayed\nWhen finalized, you can approve and initiate the token transfer\n\nFrom there, you can conveniently track the status of your transfer.\nEasy to integrate\n\nBridge aggregators and cross-chain swap technologies can easily integrate Ondo Bridge into their offerings. Please get in touch with support@ondo.finance if you would like to learn more. We are here to help.\nLearn more\n\n\nAbout Axelar\n\nAxelar is the full-stack interoperability layer for Web3. The network enables blockchain as a new kind of development platform, integrating diverse networks into a seamless “Internet of blockchains.”  Axelar is programmable and decentralized, secured by a proof-of-stake token, AXL. Application users access any digital asset or application, with one click. Developers work with a simple API and access an ecosystem of tools and service providers.\n\nMore about Axelar: axelar.network.\nAbout Ondo\n\nOndo Finance provides institutional-grade, blockchain-enabled investment products and services. Ondo has an asset management arm that creates and manages tokenized financial products as well as a technology arm that develops decentralized finance protocols and blockchain solutions. \n\nOndo’s first core products are tokenized cash equivalents that deliver very low risk, high quality yield from U.S. Treasuries, money market funds, and similar instruments, offering on-chain investors an alternative to stablecoins where holders rather than issuers earn the vast majority of the underlying asset yield. \n\nFor more information on our products, please reach out to us at support@ondo.finance or check out the following resources:\n\nWebsite X/Twitter Blog","datePublished":"2023-11-13T19:26:24.000Z","dateModified":"2025-12-16T13:06:18Z","mainEntityOfPage":{"@type":"WebPage","@id":"https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers"},"image":"https://cdn.sanity.io/images/8k2tqa6n/production/bfc7a7b7b45a28d8c7466bd514e423ea58d768ba-1600x900.png","publisher":{"@id":"https://ondo.finance/#organization"},"url":"https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers"}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://ondo.finance/blog"},{"@type":"ListItem","position":3,"name":"Ondo Bridge: Enabling Native, Cross-Chain RWA Transfers","item":"https://ondo.finance/blog/ondo-bridge-enabling-native-cross-chain-ondo-token-transfers"}]}
```