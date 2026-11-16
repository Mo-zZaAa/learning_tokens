---
url: https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs
title: What Are Tokenized Stocks and ETFs? | Ondo Learn | Ondo Finance
description: Explore how tokenized securities are bringing traditional equity markets to the blockchain economy, unlocking global access, programmability, and more.
fetched: 2026-11-16
method: static
plan: read
---

In this article

* [The $100 Trillion Opportunity](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [What Are Tokenized Stocks and ETFs?](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Why Tokenize Stocks and ETFs?](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Types of Tokenized Stocks and ETFs](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Why Tokenization Platform Design Is Critical](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Why Continued Growth Is Likely](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Limitations and Challenges for Tokenized Stocks and ETFs](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [Case Study: Implementing Institutional-Grade Tokenization With Ondo Stocks](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)
* [The Road Ahead](https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs)

[Ondo Learn](https://ondo.finance/learn)

# What Are Tokenized Stocks and ETFs?

Last Updated: Jun 30

5 min read

Share

[그림: Tokenized stocks and ETFs ]

Tokenized RWAs

Key Takeaways

* Tokenized stocks and ETFs are blockchain-based representations of publicly traded securities that provide exposure to traditional equity markets.
* Tokenized equities bring blockchain's benefits to $100+ trillion in traditional equity markets, making them accessible globally.
* Wrapped tokens dominate breadth. Hundreds of tokenized securities are available through wrapped models, while native tokenization remains limited to a handful of individual implementations.
* Quality varies dramatically. Implementation differences create measurable variations in price reliability, asset transferability, composability, and investor protections.
* The category has exceeded $1 billion in circulating value and is rapidly expanding.

## **The $100 Trillion Opportunity**

Global equity markets represent over $100 trillion in market capitalization, per SIFMA. Yet accessing these markets remains surprisingly difficult for billions of people worldwide.

An entrepreneur in West Africa wanting to buy Apple stock faces complex brokerage account requirements, international wire transfers with 3-5 day settlement, currency conversion fees, and geographic restrictions. A developer in South Asia holding Tesla shares cannot borrow against their equity without selling. An investor in Latin America struggles with capital controls that restrict access to dollar-denominated assets.

Tokenized stocks and ETFs address these friction points by bringing publicly traded securities onchain. With just a blockchain wallet and internet connection, investors worldwide can gain exposure to U.S. equities.

> "If we can tokenize bonds and stocks… it will democratize investing in ways we can't imagine." — Larry Fink, CEO of BlackRock

## **What Are Tokenized Stocks and ETFs?**

Tokenized stocks function as digital representations of traditional securities.

Traditional stock ownership requires opening a brokerage account, passing qualification checks, maintaining banking relationships, and operating within market hours. Settlement can take T+2 days and transfers require coordination between multiple parties.

Tokenized stocks provide economic exposure onchain to the same underlying securities. Tokens exist in blockchain wallets rather than brokerage accounts, enabling blockchain-native interactions. However, the specific capabilities vary significantly by platform. Some tokens can be transferred freely between wallets and integrated with DeFi protocols, while others remain locked within single platforms (walled gardens) with restricted movement.

Think of it like this: stablecoins bring dollar exposure onchain. Tokenized stocks bring equities exposure onchain. Both enable blockchain benefits (like 24/7 availability and onchain transparency) while maintaining exposure to high-quality offchain assets. The extent of additional benefits like free transferability and DeFi composability depends on how each platform implements tokenization.

## **Why Tokenize Stocks and ETFs?**

Tokenization can deliver several benefits that traditional brokerage access cannot match. However, the actual benefits realized depend significantly on the implementation choices of each tokenization platform, particularly around transferability and liquidity architecture.

#### **1. Accessibility (Platform-Dependent)**

Traditional access to U.S. stocks requires opening domestic brokerage accounts, meeting qualification criteria, and operating within market hours. International investors also face additional fees and limited selection of assets.

Tokenization can remove these barriers. Investors in regions where opening U.S. brokerage accounts is difficult can access tokenized stocks through platforms operating in their jurisdictions. For freely transferable tokens, users may acquire tokens from secondary markets without onboarding directly with the issuing platform, similar to how anyone can acquire stablecoins without opening an account with Circle (USDC) or Tether (USDT).

While certain geographic restrictions and compliance requirements still apply, tokenization enables platforms to serve markets that traditional brokerages find difficult to reach.

#### **2. Composability (Platform-Dependent)**

In traditional finance, stocks exist in walled gardens. An equity position at Fidelity cannot easily serve as collateral at another brokerage without extensive coordination.

**For freely transferable tokens, composability unlocks new possibilities.** These tokens can serve as collateral in DeFi lending protocols, enabling users to borrow against equity positions without selling. Smart contracts can enable automated portfolio rebalancing, cross-asset yield strategies, or conditional logic like "if my tokenized SPY position exceeds 60% of my portfolio, automatically rebalance into tokenized Treasuries."

However, platforms operating walled gardens do not provide these composability benefits. Tokens that cannot leave the issuing platform cannot integrate with external DeFi protocols or applications.

#### **3. Transferability (Platform-Dependent)**

**For freely transferable tokens,** holders can transfer positions to another wallet instantly, 24/7, without intermediaries. Tokenized stock positions can move between wallets on a Sunday, be deposited into a smart contract managing automated strategies, or remain self-custodied.

While buying and selling tokens on the primary market still requires traditional market hours (when underlying shares can be purchased or sold), peer-to-peer transfers enable movements anytime.

For walled garden platforms, tokens remain locked within the platform ecosystem. Users cannot transfer them to external wallets or move positions without platform approval.

#### **4. Transparency (Platform-Dependent)**

**Tokenization brings enhanced transparency.** Every token issuance, transfer, and burn is recorded onchain with cryptographic certainty. Total circulating supply is publicly verifiable in real-time by observing the blockchain. Anyone can see exactly how many tokens exist at any moment.

This transparency benefits individual holders through better visibility into token supply and enables better market analysis by reducing information asymmetry.

## **Types of Tokenized Stocks and ETFs**

While several implementation models have been attempted, the market has converged around two primary approaches: wrapped and native tokens. Understanding the practical differences between these models (and why one has achieved significantly broader adoption) reveals important principles about what makes tokenization valuable.

#### **Wrapped Stock and ETF Tokens**

Wrapped tokens are backed by actual shares held with regulated broker-dealers. When you acquire a wrapped tokenized stock, the platform purchases the underlying security and holds it in custody, issuing a token that represents that exposure.

**Market position:** Wrapped tokens represent the broadest implementation by number of securities, with hundreds of different stocks and ETFs tokenized across platforms and approximately $1B in total value. More importantly, this approach has demonstrated the fastest path to scaling access across many securities.

**How it works:** The issuer maintains backing between tokens and underlying shares held with licensed custodians. Platforms handle corporate actions differently. Some pass dividends directly to tokenholders, while Ondo Stocks uses total return tracking that reinvests dividends into additional shares to reflect the full economic value of ownership.

**Why this scales faster:** Wrapped tokenization doesn't require permission from the issuing company to tokenize its stock. Platforms simply purchase shares through traditional markets and issue tokens backed by those holdings. This approach works within existing securities frameworks, leverages established custody infrastructure, and can expand across hundreds of securities without requiring individual companies to adopt new technology or manage parallel registries.

**Important context:** Wrapping is not a new or experimental concept in finance. American Depositary Receipts (ADRs) and Global Depositary Receipts (GDRs) have used wrapped structures for decades, where institutions issue tradable instruments backed by foreign equities. In U.S. markets, most investors don't directly own shares. They are beneficial owners, with holdings recorded by brokers, who are recorded by the DTC, whose nominee (Cede & Co.) holds legal title. These layers of intermediation function reliably because they include regulatory oversight, transparency, and legal protections. The question isn't whether wrapping is an effective model. It's whether it's implemented well.

#### **Native Stock and ETF Tokens**

Companies issue shares directly onchain, with the token representing legal ownership from the start rather than being a wrapped representation.

**Market position:** Native tokenized stocks have achieved limited adoption where implemented. Adoption remains especially limited in breadth, with only a handful of stocks issued natively onchain.

**How it works:** The company's shares are issued as tokens on a blockchain, with ownership recorded onchain rather than through traditional transfer agents.

**Why scaling is challenging:** Native tokenization faces several structural obstacles that slow broader adoption:

* **Issuer cooperation required:** Each public company must individually decide to tokenize its shares.
* **Regulatory complexity:** Companies must navigate evolving guidance on how blockchain technology intersects with securities law.
* **Infrastructure burden:** Additional infrastructure requirements and incompatibility with existing financial infrastructure create operational challenges.
* **Parallel registries:** Companies choosing native tokenization often must manage both traditional and onchain share registries, adding operational complexity.

Proponents argue native tokenization provides "true ownership" onchain and eliminates counterparty risk associated with wrapped models. However, for native tokenization to scale to hundreds of securities, thousands of public companies would need to individually adopt the model and overcome these challenges. This represents a much slower path than wrapped tokenization.

### **What Matters: Outcomes Over Labels**

The debate between native and wrapped tokenization often fixates on ideological purity around onchain issuance. What ultimately matters is whether tokenization achieves its core goals: expanding access to securities, maintaining strong investor protections, accessing deep liquidity, scaling across many assets, and enabling DeFi composability.

When evaluated on these criteria, well-designed wrapped tokenization delivers immediate benefits while native tokenization faces structural obstacles that slow broader adoption.

The remainder of this guide focuses on the practical dimensions that determine how tokenization implementation (native or wrapped) can better serve investors.

## **Why Tokenization Platform Design Is Critical**

Not all tokenized stock and ETF implementations are the same. The label "tokenized stock" tells you almost nothing about whether you're receiving strong investor protections, reliable pricing, or composable assets.

Consider this: different platforms can offer "tokenized Apple stock," yet one might show 200+ basis points of price slippage on a $200k trade while another shows just 5 basis points (a 40x difference in capital efficiency). One might issue tokens locked within a single platform that can't interact with DeFi protocols, while another provides freely transferable tokens that can serve as collateral.

Quality varies dramatically across three critical dimensions that determine whether tokenization enhances or degrades the traditional market access experience.

### **Dimension 1: Liquidity Architecture**

**The core question:** How does a tokenized stock maintain price alignment with the underlying security?

This dimension has the most immediate impact on user experience as it affects the price users pay or receive when trading the asset. Two approaches exist, with measurably different outcomes:

**Approach A: Prefunded Market Maker Model**

Market makers maintain inventories of tokens on exchanges. Users trade against this prefunded inventory, with prices determined by supply and demand within available inventory.

*Observable outcomes:*

* Some implementations show 200+ basis points price impact on $200k trades.
* Tokens have traded at 10-15% premiums above underlying share prices when inventory is constrained.
* Limited inventory depth relative to demand creates price divergence.

**Approach B: Instant Mint/Redeem Model**

Tokens are minted and burned in real-time during market hours in exchange for stablecoins, maintaining continuous arbitrage opportunities that keep prices on secondary markets aligned.

*Observable outcomes:*

* Leading implementation Ondo Stocks shows a few basis points price impact on $200k trades during market hours.
* Tight tracking with underlying securities due to continuous arbitrage.
* Price dislocations are rapidly corrected through mint/redeem activity.

**Why this matters:** The approximately 40x difference in price impact between these approaches affects whether tokenized equities are practical for deploying significant capital or remain higher-friction alternatives to traditional access.

This mechanism mirrors how stablecoins maintain dollar parity: when USDC trades above $1.00, arbitrageurs mint new USDC at $1.00 and sell it at the premium. When it trades below $1.00, they buy it cheaply and redeem it for $1.00. The same continuous arbitrage principle applies to tokenized stocks.

### **Dimension 2: Transferability**

**The core question:** Can tokens move freely between wallets and protocols, or are they locked within a single platform?

**Approach A: Walled Garden**

Many platforms operate closed ecosystems where tokens cannot move outside the platform. Users must be onboarded directly and cannot use them in external protocols.

**Approach B: Freely Transferable**

Platforms like Ondo Stocks issue tokens that can move permissionlessly between wallets and integrate with external protocols, similar to how stablecoins function.

### **Dimension 3: Investor Protections**

Even within similar models, platforms differ substantially in protections provided to tokenholders. When holding a tokenized stock, the underlying shares exist offchain in traditional custody. The token is a claim on those shares, and that claim is only as good as the legal protections supporting it.

**The spectrum of protection:**

At one end, some implementations offer minimal transparency about backing, no independent verification, and unclear protections in default scenarios. Tokenholders in these structures effectively rely on issuer promises, possibly without enforceable mechanisms for recovery if things go wrong.

At the other end, institutional-grade implementations include multiple layers of protections:

* **Backing verification:** Independent third-party verification of reserve assets conducted daily, with reports publicly accessible so tokenholders can verify backing.
* **Bankruptcy-remote structures:** Special purpose vehicles that are designed to legally separate token-backing assets from the parent company's other operations. If properly structured and the parent company faces bankruptcy, creditors generally cannot access assets held by the SPV, protecting tokenholders' claims.
* **Perfected security interests:** Public filings with regulatory authorities establishing tokenholders' priority claim on collateral assets. This legal "perfection" helps ensure backing assets aren't promised to multiple parties.
* **Independent enforcement:** Collateral agents or security agents are independent third parties who act on behalf of tokenholders to seize and distribute collateral if defined default events occur, such as failures to maintain required backing levels or honor redemption requests.
* **Regulated custody:** Underlying shares held with regulated custodians, providing standard securities industry protections.
* **Clear redemption rights:** Contractually specified redemption procedures with enforceable mechanisms, not just issuer discretion.

These protections determine what happens when something goes wrong. Without them, tokenholders face potentially lengthy court battles to recover assets, with uncertain outcomes.

## Why Continued Growth Is Likely

The platforms that succeed will be those combining all three critical dimensions: free transferability, efficient liquidity architecture, and institutional-grade protections. As tokenized equities demonstrate practical value at scale, they are reshaping how capital moves globally (with billions onchain today and potentially trillions within the decade).

* **Regulatory clarity increasing:** Jurisdictions worldwide are establishing frameworks for tokenized securities, reducing uncertainty for platforms and investors. The EU's DLT Pilot Regime, Switzerland's DLT Act, and evolving U.S. guidance signal regulatory acceptance of compliant tokenization.
* **Infrastructure maturing:** Cross-chain bridges, custody solutions, and DeFi integrations are making tokenized equities more practical for institutional and retail participants. Each wave of tokenization benefits from infrastructure built by previous waves.
* **Liquidity efficiency improving:** The gap between instant mint/redeem and prefunded market maker models (5 bps vs. 200+ bps) is becoming clearer, with capital flowing toward more efficient architectures.
* **Scale expanding:** Platforms are moving from dozens to hundreds of tokenized securities, demonstrating that tokenization can extend beyond high-demand assets to comprehensive market coverage.
* **Traditional finance integration:** Major asset managers, exchanges, and custodians are building tokenization capabilities, signaling mainstream adoption.

## **Limitations and Challenges for Tokenized Stocks and ETFs**

Despite significant progress, tokenized equities face structural constraints and evolving challenges:

#### Geographic Restrictions

Most tokenized stock platforms implement geographic restrictions, often excluding U.S. persons. This limits accessibility for what would otherwise be a natural user base for accessing domestic equities onchain.

#### Implementation Quality Variance

The wide variance in implementation quality (from price reliability to investor protections) creates information asymmetry for users evaluating platforms. Unlike traditional brokerages, which operate under relatively standardized regulatory frameworks, tokenized stock platforms show substantial structural differences.

#### Market Hours Dependency

While peer-to-peer transfers are possible 24/7, minting and redeeming tokens on the primary market typically requires traditional market hours when underlying shares can be purchased or sold. Outside market hours, secondary market liquidity may exist but with potentially wider spreads. However, Ondo Stocks recently introduced 24/7 minting and redemptions to overcome this barrier.

## Case Study: Implementing Institutional-Grade Tokenization With Ondo Stocks

Examining how the leading platform combines the three quality dimensions illustrates what institutional-grade tokenization looks like in practice.

#### Transferability

Tokens are freely transferable between wallets and compatible with DeFi protocols (outside the U.S., subject to jurisdictional restrictions). This design is comparable to stablecoin functionality rather than walled garden approaches, enabling users to self-custody tokens and use them composably across applications.

#### Liquidity Architecture

The platform implements instant mint/redeem mechanics, with Ondo Stocks becoming the first platform to support [24/7/365 minting and redemptions](https://ondo.finance/blog/real-24-7-trading-for-tokenized-stocks). When onboarded users acquire or redeem tokenized stocks, token minting/burning and underlying share purchase/sale occur simultaneously in atomic transactions. This architecture enables continuous secondary market arbitrage. If tokens trade above fair value on secondary markets, participants mint new tokens at proper value and sell them; if tokens trade below fair value, they purchase and redeem at underlying value.

Observed outcome: approximately 5 basis points price impact on $200k trades during market hours, maintaining tight alignment with underlying securities without requiring market makers to prefund large inventories across hundreds of assets.

#### Investor Protections

The platform implements comprehensive structural safeguards designed to protect tokenholders in various scenarios:

* **Daily verification:** Independent third-party Verification Agent reviews backing every business day and publishes reports, enabling real-time transparency.
* **Bankruptcy-remote structure:** Special purpose vehicle designed to legally separate backing assets from parent company operations.
* **Perfected security interests:** Independent Security Agent holds first-priority security interest in underlying shares (and cash in transit) for tokenholder benefit.
* **Contractual enforcement:** In defined default events (such as backing failures or inability to service redemptions), the Security Agent has contractual authority to foreclose on collateral and distribute proceeds to tokenholders.
* **Regulated custody:** Underlying shares held with U.S.-registered broker-dealers.
* **24/7 redemptions:** On-demand redemption access with instant execution. 24/5 mint/redemption is supported for all assets, with 24/7 support for the [most popular assets](https://ondo.finance/blog/real-24-7-trading-for-tokenized-stocks).
* **Scale and coverage:** 430+ tokenized stocks and ETFs, with infrastructure designed to scale rapidly across many more securities. Dividends are automatically reinvested into additional underlying shares (net of withholding tax), so tokens track total return rather than price-only performance.

The platform launched with [ecosystem](https://ondo.finance/ecosystem) support from major wallets (Trust Wallet, OKX Wallet, Bitget Wallet), exchanges (Gate), custody providers (BitGo, Fireblocks, Ledger), and DeFi protocols (1inch, CoW Protocol).

To summarize, the platform provides broad asset selection, strong protections, reliable liquidity, and rapid scaling.

## **The Road Ahead**

The tokenization of equities is accelerating as infrastructure matures and implementation quality improves. Tokenized stocks are expanding access to equity markets ($1B+ and growing). Yet compared to the $100+ trillion in global equity markets, this remains early-stage adoption. The next phase will be defined less by whether securities can be brought onchain and more by how well platforms deliver the outcomes investors actually need: reliable liquidity, transparent backing, strong legal protections, broad asset coverage, and assets that can move freely across the blockchain economy. With these standards in place, tokenized stocks and ETFs will evolve into a foundational layer for global capital markets.

[그림: This content is provided for informational purposes only. ]

---

Further Reading

[[그림: Real-World Asset Tokenization]

What Is Real-World Asset Tokenization?

Explore what tokenized real-world assets (RWAs) are and how they’re bringing stocks, ETFs, and other financial assets to the blockchain ecosystem.

5 min read](https://ondo.finance/learn/tokenized-rwas/real-world-asset-tokenization)[[그림: Tokenized Treasuries]

What Are Tokenized Treasuries?

Tokenized U.S. Treasuries are blockchain-based representations of U.S. government debt instruments. These tokens provide holders with yield from Treasury bills, notes, or Treasury-focused ETFs.

5 min read](https://ondo.finance/learn/tokenized-rwas/what-are-tokenized-treasuries)[[그림: What Are Stablecoins?]

What Are Stablecoins?

Stablecoins are digital tokens designed to maintain a stable value, most commonly pegged to the U.S. dollar.

5 min read](https://ondo.finance/learn/stablecoins/what-are-stablecoins)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Ondo Learn","item":"https://ondo.finance/learn"},{"@type":"ListItem","position":3,"name":"What Are Tokenized Stocks and ETFs?","item":"https://ondo.finance/learn/tokenized-rwas/tokenized-stocks-and-etfs"}]}
```