---
url: https://ondo.finance/learn/stablecoins/what-are-stablecoins
title: What Are Stablecoins? | Ondo Learn | Ondo Finance
description: Discover how tokenizing U.S. dollars and other fiat currencies to create stablecoins is transforming global payments, powering DeFi, and more.
fetched: 2026-11-16
method: static
plan: read
---

In this article

* [Understanding Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [The Dominance of U.S. Dollar Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [Types of Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [Benefits of Fiat-Backed Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [Real-World Utility of Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [Limitations of Fiat-Backed Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [From Stablecoins to Yieldcoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)
* [The Road Ahead for Stablecoins](https://ondo.finance/learn/stablecoins/what-are-stablecoins)

[Ondo Learn](https://ondo.finance/learn)

# What Are Stablecoins?

Last Updated: Jun 30

5 min read

Share

[그림: What Are Stablecoins?]

Stablecoins

Key Takeaways

* Stablecoins are digital tokens designed to maintain a stable value, most commonly pegged to the U.S. dollar. They represent the earliest and most widely adopted form of real-world asset tokenization, serving as a cash equivalent on blockchains like Ethereum.
* Stablecoins dominate blockchain activity. Over $300 billion of stablecoins are in circulation, with trillions settling annually, exceeding Visa and Mastercard combined in recent years.
* USD stablecoins command the market. More than 99% of stablecoin value is denominated in U.S. dollars.
* Fiat-backed models won. After algorithmic stablecoin experiments failed, fully collateralized stablecoins backed by cash and Treasuries emerged as the standard.
* Stablecoins proved the tokenization thesis and paved the way for yieldcoins, which combine USD exposure with yield distribution.

The financial system needed a way to move dollars globally at speed. Traditional payment rails are slow, expensive, and exclude billions who lack access to dollar banking infrastructure. Stablecoins emerged as the solution, bringing the world's most trusted currency onchain while preserving blockchain's core benefits: programmability, accessibility, and 24/7 settlement.

Today, stablecoins form the foundation of onchain finance. They've proven that trusted offchain assets can thrive in blockchain environments, validating the broader thesis of real-world asset tokenization and setting the stage for yield-bearing instruments and tokenized securities.

> "Stablecoins in particular remain the killer app for blockchain technology." — Jeremy Allaire, CEO of Circle

## **Understanding Stablecoins**

Stablecoins solve a fundamental problem: the majority of Web3 users find native cryptocurrencies like BTC and ETH too volatile to serve as reliable mediums of exchange or units of account. A payment denominated in ETH could be worth significantly more or less by the time it settles. Stablecoins eliminate this volatility by maintaining a peg to a stable value, typically the U.S. dollar.

In practice, stablecoins function as digital cash. They enable users to transact in tokens that combine the stability of traditional currencies with the speed and accessibility of blockchain infrastructure. Anyone with internet access and a blockchain wallet can now hold, send, and receive tokenized dollars instantly, all without a U.S. bank account, credit check, or geographic restrictions.

This accessibility has driven explosive adoption. Stablecoins now account for the majority of blockchain settlement activity and represent over $300 billion in circulating value across multiple blockchains.

## **The Dominance of U.S. Dollar Stablecoins**

While stablecoins pegged to euros, yen, and other fiat currencies exist, more than 99% of all stablecoin value is USD-denominated. This dominance reflects the dollar's unique status as the world's reserve currency and its deep integration into global trade, finance, and settlement systems.

By extending the reach of the U.S. dollar into onchain markets, stablecoins have reinforced dollar hegemony, transforming it from the settlement currency of global banking into the settlement currency of onchain markets.

## **Types of Stablecoins**

While all stablecoins share the goal of price stability, the mechanisms used to achieve that goal differ significantly. Understanding these distinctions is essential to assessing stability, transparency, and risk.

#### **Fiat-Backed Stablecoins**

Fiat-backed stablecoins are typically backed 1:1 by reserves of cash and short-term U.S. Treasuries held with regulated financial institutions.

**Examples**: USDC (Circle), USDT (Tether), PYUSD (PayPal)

**Mechanism**: Issuers mint new tokens when users deposit dollars and redeem tokens when users withdraw them. The issuer maintains reserves equal to or greater than the circulating supply.

**Market position**: Fiat-backed stablecoins dominate the market, accounting for over 95% of total stablecoin value and serving as the default medium of exchange across the crypto ecosystem.

USDT (Tether) remains the clear market leader with over $180 billion in circulation, and is larger than all other stablecoins combined. USDC (Circle) follows as the dominant contender with over $70 billion in circulation. Together, these two assets represent the overwhelming majority of the $300 billion market.

#### **Crypto-Collateralized Stablecoins**

Crypto-collateralized stablecoins are backed by other crypto assets such as ETH or BTC rather than fiat reserves. To account for volatility, they are typically overcollateralized, meaning that the value of the collateral exceeds the value of stablecoins issued.

**Examples**: USDS (Sky), sUSD (Synthetix)

**Mechanism**: Users deposit crypto assets as collateral to mint stablecoins. If collateral value falls below required thresholds, liquidation mechanisms activate to restore solvency.

**Limitations**: These models demonstrate the power of smart contracts but also reveal the constraints of crypto-native collateral. During market stress, liquidation cascades can destabilize the peg, and complex governance systems introduce operational risks that fiat-backed models avoid.

#### **Alternative Stablecoin Models**

Beyond the fiat-backed and crypto-collateralized categories, other models have attempted different approaches to maintaining dollar stability, with varying degrees of success.

The algorithmic stablecoin TerraUSD (UST) sought to maintain its one-dollar peg without explicit collateral by algorithmically adjusting its supply through a mint-and-burn mechanism tied to its governance token, LUNA, expanding or contracting supply based on market demand. The collapse of TerraUSD in 2022 underscored the structural fragility of this approach. The death spiral, where falling prices triggered supply expansions that further eroded market confidence, demonstrated that algorithmic mechanisms cannot substitute for real collateral underpinning stablecoins.

More recently, synthetic dollar-like assets like USDe (Ethena) have emerged with a fundamentally different approach. Unlike algorithmic stablecoins that had no backing, synthetic assets maintain dollar-like exposure through derivatives strategies. USDe uses delta-neutral hedging (holding crypto collateral while taking offsetting short positions) to create stable value exposure while generating yield from funding rates. While these assets do maintain collateral, they face different risk profiles than fiat-backed stablecoins, including dependency on derivatives markets, funding rate volatility, and liquidation risks during market stress. Their inclusion in stablecoin market data reflects their functional similarity to stablecoins rather than structural equivalence.

The remainder of this guide focuses primarily on **USD-denominated fiat-backed stablecoins**. While crypto-collateralized and algorithmic models offer interesting design experiments, fiat-backed stablecoins have demonstrated the clearest product-market fit, achieved institutional adoption, and account for over 95% of the market.

## **Benefits of Fiat-Backed Stablecoins**

Fiat-backed stablecoins have proven to be the most successful form of tokenized cash, combining the credibility of fiat currency with the innovation of blockchain infrastructure.

#### **1. Stability**

Backed by real-world reserves of cash and short-term Treasuries, providing confidence in the peg.

#### **2. Accessibility**

Anyone, anywhere can hold and transfer digital dollars instantly and at low cost, without traditional banking relationships.

#### **3. Efficiency**

Transactions settle in seconds, 24/7, with no intermediaries, eliminating the delays and fees of traditional payment rails.

#### **4. Composability**

Deeply integrated across DeFi protocols, exchanges, and payment networks, serving as programmable building blocks for complex financial applications.

## **Real-World Utility of Stablecoins**

The real-world utility of stablecoins extends across multiple use cases, demonstrating why they've achieved product-market fit where many blockchain applications haven't.

#### **1. Cross-Border Payments and Remittances**

Stablecoins enable fast, low-cost international transfers without correspondent banking networks. A user in the Philippines can receive remittances from the U.S. in minutes rather than days, with fees in some cases less than a single cent. Services like MoneyGram and Xoom leverage stablecoin rails to reduce friction in global money movement.

#### **2. DeFi Infrastructure**

Stablecoins serve as the base layer for decentralized finance. In lending protocols like Aave and Compound, they function both as borrowable assets and as collateral for leveraged positions. In automated market makers like Uniswap and Curve, they enable low-volatility trading pairs that minimize impermanent loss. Yield aggregators like Yearn deploy stablecoins across protocols to optimize returns.

#### **3. Corporate Treasury and Settlement**

Enterprises use stablecoins for real-time liquidity management. Transactions that once required multiple banking relationships and days of settlement now occur instantly on blockchain rails. Payment processors like Worldpay are integrating stablecoin settlement to offer merchants instant access to funds, replacing traditional multi-day settlement cycles.

#### **4. Emerging Market Adoption**

In regions with currency instability or limited banking infrastructure, stablecoins provide access to dollar-denominated value. Additionally, users in Argentina, Turkey, and Nigeria hold stablecoins as a hedge against local currency devaluation and as a means to participate in global digital commerce.

These applications demonstrate stablecoins' versatility as both a means of payment and temporary store of value. However, their utility as long-term capital instruments remains constrained by a fundamental limitation: the absence of yield.

## **Limitations of Fiat-Backed Stablecoins**

Despite their success, fiat-backed stablecoins face significant structural limitations that constrain their utility as long-term stores of value. The GENIUS Act, signed into law in July 2025, addressed some historical risks for compliant issuers but introduced new constraints.

#### **1. No Native Yield**

Stablecoin holders receive no yield regardless of compliance status. While issuers hold reserve assets that generate interest (typically U.S. Treasuries), this income flows entirely to issuers. The GENIUS Act explicitly prohibits compliant issuers from paying interest to stablecoin holders, cementing the structural gap between the economic value generated by reserves and the value distributed to stablecoin holders.

#### **2. Regulatory Protections Vary by Issuer**

The GENIUS Act established stronger protections for compliant stablecoins, including bankruptcy-remote reserve accounts, priority claims for holders senior to all other creditors, and mandatory monthly reserve disclosures. However, stablecoins not yet compliant with the Act (including many existing issuances, which have until January 2027 to transition) may still function as unsecured liabilities without these protections.

#### **3. Redemption Dependencies**

The GENIUS Act requires compliant issuers to establish clear redemption procedures and honor redemptions at par, but provides no automatic enforcement mechanisms. If issuers fail to meet redemption requests in a timely manner, tokenholders would still need to pursue regulatory complaints or litigation. The Act provides priority claims in bankruptcy but does not prevent operational delays or temporary redemption suspensions.

These limitations may not significantly undermine stablecoins' effectiveness as a means of payment, but they highlight why stablecoins, even with enhanced regulatory protections, are far from optimal. The prohibition on yield distribution is particularly significant: it represents a deliberate policy choice that ensures stablecoins cannot compete with yield-bearing instruments as stores of value, or accumulate interest similar to bank deposits.

## **From Stablecoins to Yieldcoins**

Stablecoins successfully brought dollars onchain, but they don't pass through the yield generated by the assets backing them. Treasury bills backing fiat-backed stablecoins generate billions annually, yet this income flows entirely to issuers rather than tokenholders. Notably, this business model has made Tether one of the most profitable companies in the world per employee, reportedly generating over $85 million in profit per employee in 2024.

This structural gap created the foundation for the next generation of tokenized assets: yieldcoins.

Yieldcoins (also known as tokenized treasuries) combine the stability of fiat-referenced value with the income generation of yield-bearing instruments. They distribute the returns from underlying Treasury holdings directly to tokenholders, transforming stablecoins' static dollar exposure into productive capital.

Ondo Finance pioneered this category with [**OUSG**](https://ondo.finance/ousg), the first tokenized treasury product to gain material adoption. OUSG provides Qualified Purchasers with permissioned onchain exposure to short-term U.S. Treasury ETFs.

Ondo Finance then introduced [**USDY**](https://ondo.finance/usdy) for non-U.S. persons: a freely transferable yield-bearing token that combines the accessibility of stablecoins with Treasury-backed returns. USDY's quasi-permissionless design has driven broad adoption, with more individual holders than the top 10 tokenized treasuries by TVL combined.

Other institutions have followed. **USYC** (Circle) is the largest tokenized treasury by market cap, while **BUIDL** (BlackRock), **BENJI** (Franklin Templeton), **WTGXX** (WisdomTree), and others have expanded the category.

Collectively, tokenized treasuries have now exceeded $14 billion in circulating value. Notably, tokenized treasuries are being adopted faster than stablecoins were in their early years, demonstrating that the infrastructure and confidence built by stablecoins accelerated adoption of the next wave.

## **The Road Ahead for Stablecoins**

According to the global asset manager Bernstein, the stablecoin market could expand to nearly $3 trillion by 2028, driven by growing roles in payments, settlement, and digital asset markets. As regulation matures and integrations deepen, stablecoins are poised to become a core medium of exchange within the global financial system.

However, stablecoins are not designed to serve as stores of value. While they maintain price stability, they do not distribute the yield generated by backing assets, creating a fundamental limitation for long-term capital deployment.

This is where yieldcoins complement stablecoins. Together, these assets represent two pillars of onchain finance:

* **Stablecoins**: The means of exchange, optimized for transactions, payments, and liquidity
* **Yieldcoins**: The store of value, optimized for capital preservation and income generation

As both categories mature, the onchain financial system increasingly mirrors traditional finance's separation between transaction accounts (checking) and savings instruments (Treasury bills, money market funds). The difference: onchain infrastructure makes both more accessible, more composable, and operational 24/7.

[그림: This content is provided for informational purposes only. ]

---

Further Reading

[[그림: Decentralized Exchange ]

What Is a Decentralized Exchange (DEX)?

Decentralized exchanges (DEXs) are blockchain-based trading platforms that enable peer-to-peer cryptocurrency and tokenized asset trading, using smart contracts instead of centralized order books.

4 min read](https://ondo.finance/learn/defi/decentralized-exchange-dex)[[그림: Tokenized Treasuries]

What Are Tokenized Treasuries?

Tokenized U.S. Treasuries are blockchain-based representations of U.S. government debt instruments. These tokens provide holders with yield from Treasury bills, notes, or Treasury-focused ETFs.

5 min read](https://ondo.finance/learn/tokenized-rwas/what-are-tokenized-treasuries)[[그림: Real-World Asset Tokenization]

What Is Real-World Asset Tokenization?

Explore what tokenized real-world assets (RWAs) are and how they’re bringing stocks, ETFs, and other financial assets to the blockchain ecosystem.

5 min read](https://ondo.finance/learn/tokenized-rwas/real-world-asset-tokenization)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Ondo Learn","item":"https://ondo.finance/learn"},{"@type":"ListItem","position":3,"name":"What Are Stablecoins?","item":"https://ondo.finance/learn/stablecoins/what-are-stablecoins"}]}
```