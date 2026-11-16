---
url: https://ondo.finance/blog/institutional-grade-bridging-with-layerzero
title: Setting a New Standard for Institutional-Grade Bridging with LayerZero | Ondo Finance
description: Unveiling a First-of-its-Kind Bridging Solution with LayerZero’s Application-Owned Security Model

⚠️ NOTE: Ondo’s tokenized treasuries products, including …
fetched: 2026-11-16
method: static
plan: skim
---

In this article

* [Unveiling a First-of-its-Kind Bridging Solution with LayerZero’s Application-Owned Security Model](https://ondo.finance/blog/institutional-grade-bridging-with-layerzero)
* [Take RWAs Omnichain via LayerZero with the Ondo Bridge: Ethereum, Arbitrum, Mantle, and More.](https://ondo.finance/blog/institutional-grade-bridging-with-layerzero)
* [Institutional-Grade Security with Decentralized Verifier Networks (DVNs)](https://ondo.finance/blog/institutional-grade-bridging-with-layerzero)
* [Building Redundancies for Enhanced Security](https://ondo.finance/blog/institutional-grade-bridging-with-layerzero)
* [What’s Next for Ondo?](https://ondo.finance/blog/institutional-grade-bridging-with-layerzero)

Announcement • Nov 26, 2024 • 6 min

# Setting a New Standard for Institutional-Grade Bridging with LayerZero

[Ondo Finance

Official Blog](https://ondo.finance/blog)

[그림: Setting a New Standard for Institutional-Grade Bridging with LayerZero]

#### **Unveiling a First-of-its-Kind Bridging Solution with LayerZero’s Application-Owned Security Model**

*⚠️ **NOTE**: Ondo’s tokenized treasuries products, including USDY, are not, and may not be, offered, sold, or otherwise made available in the US or to US persons. USDY has not been registered under the US Securities Act ("Act") or pursuant to securities laws of any other jurisdiction, and Act or an exemption or exclusion from the registration requirements thereof is available. Additional restrictions may apply.*

*Nothing herein constitutes any offer to sell, or any solicitation of an offer to buy, any of Ondo’s tokenized treasuries products. Acquiring tokens involves risks. A token holder may incur losses, including total loss of their funding to acquire those tokens. Past performance is not an indication of future results. Ondo does not endorse, Ondo does not make any representation or warranty whatsoever (express or implied, including but not limited to any warranty of merchantability, fitness for a particular purpose, or non-infringement) regarding, and **ONDO SHALL NOT HAVE ANY LIABILITY WHATSOEVER WITH RESPECT TO ANYONE'S USE OF**, any third-party products, services, or technologies referenced herein. Additional terms apply. Visit ondo.finance for details.*

*-*

Ondo is a provider of institutional-grade assets building toward a global market for tokenized securities, and as such, investor protections are paramount. The fragmented, multichain nature of blockchain ecosystems means that onchain tokenized assets must be able to seamlessly bridge across isolated blockchains. This requires solutions that ensure security-first, cross-chain transferability. But existing bridging solutions often rely on a single messaging protocol, creating a centralized point of trust. To meet institutional standards, we developed a solution with redundant security and risk controls at the smart contract level, eliminating single points of failure and enabling a security-first, composable future for tokenized real-world assets.

In collaboration with LayerZero, we built the first institutional-grade RWA bridging solution. LayerZero’s Application-Owned Security Model enables us to configure a security stack with a diverse set of isolated Decentralized Verifier Networks (DVNs), including our own bespoke DVN, that independently verify the integrity of each message sent across chains in what we call Multi-Messaging Aggregation (MMA). We are able to utilize existing bridge solutions as DVNs, compounding each solution’s individual security to provide a best-in-class product for our investors and their assets.

*"Institutional-grade assets demand secure and reliable interoperability to fully unlock the potential of blockchain technology,"* said Nathan Allman, CEO of Ondo Finance. *"Our solution built with LayerZero ensures seamless cross-chain transactions, providing the robust infrastructure necessary for institutions to confidently make their tokenized assets accessible across interconnected blockchains."*

CEO of LayerZero Labs, Bryan Pellegrino shared, *“By adopting the OFT Standard, Ondo has the power to make tokenized T-bills and real-world yield accessible on 90+ chains. This is exactly why LayerZero exists—giving teams the flexibility to bring major assets like USDY to multiple ecosystems without compromising on security.”*

We have implemented Polyhedra’s ZKBridge, Axelar’s PoS Network, and LayerZero Labs’ general DVNs to serve as mandatory message verifiers for all transfers of Ondo’s tokenized treasuries between chains. In addition, to further enhance security, we are implementing our own Ondo DVN with Ondo-specific validation built in as an explicit-use redundancy. We believe this will be *the standard* for institutional-grade bridging.

#### **Take RWAs Omnichain via LayerZero with the Ondo Bridge: Ethereum, Arbitrum, Mantle, and More.**

With this bridge implementation, Ondo asset holders can now securely leverage the yield-bearing capabilities of tokenized US Treasuries with deep liquidity across the largest DeFi ecosystems. The bridge is live today, and Ondo’s USDY tokens are now seamlessly transferable across **Ethereum, Arbitrum,** and **Mantle**. Users can bridge RWAs without the need for complex swapping, or minting new tokens, beginning with USDY via [Ondo’s own bridge](https://ondo.finance/bridge) frontend and the [Stargate Finance](https://stargate.finance/) platform, one of the largest bridge frontends in crypto, with plans to integrate OUSG in the near future.

[[그림: Ondo Bridge]](https://gifyu.com/image/SGnLF)

#### **Institutional-Grade Security with Decentralized Verifier Networks (DVNs)**

Last year we rolled out V1 of the Ondo bridge, which enabled Ethereum to Mantle transfers. With this, we were one of the first MMA Bridge implementations, relying on shared security between the Axelar Network and Ondo Finance’s off-chain systems to relay and attest messages and ensure the validity of transactions being performed. While this was a best-in-class security solution at the time, we want tokenized RWAs to be available *everywhere,* and this scale requires a deeper focus on isolated security without a single point of failure.

In our mission of making tokenized RWAs broadly available, we believe bridging built around MMA with a *diverse* set of verification mechanisms and message passing protocols is the most secure and flexible method. The LayerZero protocol allows applications to leverage immutable smart contracts and configure a custom security stack, utilizing a bespoke selection of DVNs to verify message integrity. This approach enables us to achieve a more scalable and flexible solution, extending across diverse ecosystems.

The new bridge is the first MMA bridge of its kind, aggregating attestations via ZK proofs with Polyhedra, an industry-leading bridge protocol in LayerZero Labs, and a PoS blockchain in Axelar. [Polyhedra](https://docs.zkbridge.com/zkbridge-trustless-cross-chain-bridges-made-practical/introducing-zkbridge-protocol) offers mathematical certainty of bridge events via zero-knowledge proofs, while [Axelar](https://docs.axelar.dev/learn/security) is a battle tested Proof-of-Stake blockchain purpose-built for General Message Passing. Axelar has securely transmitted over 2 billion messages, representing more than $9 billion in volume. The distinct network of isolated DVNs seeks to minimize the risk of any single point of failure and offer robust, adaptable security. The configurability of the OFT framework allows us to evolve alongside the industry, enabling the addition of new verification mechanisms and interoperability protocols as DVNs, when they become available.

#### **Building Redundancies for Enhanced Security**

Beyond the diverse DVN stack and isolated security of the LayerZero implementation, we want security measures that are specific to our institutional-grade products. To this effect, we are implementing additional redundancies to ensure a best-in-class bridging solution, including the Ondo DVN, designed with a focus on client diversity and tailored specifically for validation of Ondo assets.

**Ondo’s Decentralized Verifier Network:** Software diversity and trust alignment are essential principles in blockchain security. When multiple attestors in a security stack run the same software, a single bug or malicious dependency can compromise the entire system, potentially leading to false mints. While the inherent diversity provided by Polyhedra, LayerZero, and Axelar already helps mitigate this risk, we are elevating our security model with the Ondo DVN, which will be built upon our proprietary off-chain verification mechanisms from the original Ondo Bridge.

This DVN will have explicit instructions to verify the burn of bridged Ondo assets (OUSG, USDY) in concurrence with the minting of those assets on the target network, and establishes asset supply integrity for Ondo Finance, a feature not included in other general DVNs.

Given that the entire aggregation stack is required for message attestation, Ondo becomes a necessary signer in the process. In deploying our own DVN, we reduce the trust assumptions involved in omnichain transfers, allowing users to rely on the trust they already place in us for token issuance while minimizing dependence on third parties.

**Rate Limiting at the Smart Contract Layer:** In collaboration with the LayerZero team, we’ve implemented a first-of-its-kind inbound and outbound rate limiting at the smart contract level. These rate limits provide a crucial layer of defense and further mitigate any risk, preventing the overminting of unauthorized tokens, thereby reducing the likelihood of a catastrophic attack on the solvency of the token issuers, in the highly unlikely event of a widespread compromise of the security stack.

**Emergency Freeze:** As an added measure of security, we’ve built an emergency pause feature directly into the contracts to decrease incident response latency in the case of a system malfunction.

#### **What’s Next for Ondo?**

With a premier solution for secure omnichain growth, Ondo will open RWA access to more users and liquidity, setting the stage for Ondo Stocks. Core to the Ondo Stocks vision is remedying the problem of liquidity deserts for tokenized assets. With our LayerZero-enabled bridge design, we are demonstrating how tokenized assets can overcome this challenge by securely tapping into omnichain liquidity environments. Ondo’s tokenized treasuries are already live across 8 chains, and we plan to continue expanding bridge support to make our assets both interoperable and available on more chains in the coming months.

---

Next

[[그림: RWAs You Can Use For Collateral: USDY on Drift]

USDY•Nov 20, 2024

### RWAs You Can Use For Collateral: USDY on Drift](https://ondo.finance/blog/rwas-you-can-use-for-collateral)

[[그림: Introducing 24/7 Conversions Between OUSG and PayPal USD (PYUSD)]

OUSG•Nov 15, 2024

### Introducing 24/7 Conversions Between OUSG and PayPal USD (PYUSD)](https://ondo.finance/blog/introducing-24-7-conversions-between-ousg-and-paypal-usd-pyusd)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://ondo.finance/blog"},{"@type":"ListItem","position":3,"name":"Setting a New Standard for Institutional-Grade Bridging with LayerZero","item":"https://ondo.finance/blog/institutional-grade-bridging-with-layerzero"}]}
```