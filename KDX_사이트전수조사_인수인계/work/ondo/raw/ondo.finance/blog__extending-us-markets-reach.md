---
url: https://ondo.finance/blog/extending-us-markets-reach
title: Anchored Onshore: How Ondo Stocks Extends the Reach of U.S. Capital Markets | Ondo Finance
description: Let’s begin with the obvious point: we at Ondo have a direct interest in how tokenized equities are understood. Readers should judge our perspectives accord…
fetched: 2026-11-16
method: static
plan: skim
---

In this article

* [A better framing](https://ondo.finance/blog/extending-us-markets-reach)
* [The recent research](https://ondo.finance/blog/extending-us-markets-reach)
* [Some implications of design choices](https://ondo.finance/blog/extending-us-markets-reach)
* [The bigger picture](https://ondo.finance/blog/extending-us-markets-reach)
* [Moving forward](https://ondo.finance/blog/extending-us-markets-reach)

Ondo Stocks • Apr 9, 2026 • 5 min

# Anchored Onshore: How Ondo Stocks Extends the Reach of U.S. Capital Markets

Ondo Finance

Official Blog

[그림: Anchored Onshore: How Ondo Stocks Extends the Reach of U.S. Capital Markets]

Let’s begin with the obvious point: we at Ondo have a direct interest in how tokenized equities are understood. Readers should judge our perspectives accordingly, but our interests do not prevent us from making some straightforward observations.

### A better framing

Current claims that tokenization “splits liquidity” are now too blunt and poorly informed to be useful. Market structure questions of this kind have been studied for decades, long before blockchains entered the picture. The relevant literature on fragmented equity markets, cross-listings, ADRs, ETF arbitrage, and linked settlement systems has never treated the mere existence of another venue, or wrapper, or a linkage of one kind or another, as the end of the analysis. The right question has always been narrower: how strong is the link between the new venue and the underlying market, and how does that link behave under ordinary conditions and under stress? Does the new venue deepen the reach of the underlying market, or begin to detach from it?

Those design questions matter because the stakes here are not limited to blockchains. They concern how U.S. capital markets remain the world’s preferred venue for equity fundraising, trading, and ownership in an environment where investors and capital increasingly move on internet time. Ondo’s view is straightforward. The point of our tokenization model is not to relocate U.S. markets offshore or onto blockchains. It is to extend the reach of U.S. markets, U.S.-listed securities, and U.S. dollar-denominated financial products into the digital channels where global demand is increasingly forming.

### The recent research

That is why the recent *Tokenized Stocks* paper is worth taking seriously. It is useful not because it “proves” a single model right, but because it moves the debate away from slogans and back toward the underlying microstructure. Its findings are measured. Tokenized stocks generally track the underlying closely during regular hours. Weekend trading appears, in many cases, to redistribute rather than simply magnify the traditional Monday effect. And the important differences are differences of design: how open the market is, how redemption works, when arbitrage is available, and how much off-hour trading is accommodated when the primary market is closed.

That framing matters because the paper recognizes Ondo as one of two distinct models for tokenized equities, and because the contrast helps clarify the effects of Ondo’s design choices.

* Ondo’s model, representing roughly 70% of tokenized equities today, synchronizes creation and redemption with U.S. market hours, producing a 24/5 structure anchored in the most reliably liquid trading windows, with secondary trading on weekends. This model is designed as a tokenized access layer built on top of traditional market depth and broker-dealer custodial controls. Ondo transactions flow directly into the U.S. national market system, with the underlying securities ultimately settling in DTC.
* The alternative model the *Tokenized Stocks* paper explores, representing roughly 25% of tokenized equities today, is a prefunded inventory pool onchain. This design emphasizes continuous 24/7 trading while allowing for greater divergence in prices.

### Some implications of design choices

Those are different design choices, and they produce different economic outcomes. The *Tokenized Stocks* paper’s own description is telling: Ondo’s design tends to keep prices closer to the underlying during the week, while the alternative design allows more room for drift. That is not evidence that Ondo has severed itself from the underlying market. It is evidence that market design choices shape how tightly those linkages hold at different times. Ondo’s own research on the performance of our recently rebranded Ondo Stocks products has confirmed the principal findings in the paper and consistently found tight links with the underlying market 24/5. The table¹ below highlights the differences between Ondo’s execution price 24/5 vs. the underlying stock market order book for all transactions between February 2nd and April 7th. 75% of transactions observed less than 2bps spread, and 95% observed less than 5bps spread.

| Observations | P5 Spread (bps) | P25 Spread (bps) | Median Spread (bps) | P75 Spread (bps) | P95 Spread (bps) |
| --- | --- | --- | --- | --- | --- |
| 691,078 | 0.00 | 0.61 | 1.00 | 2.00 | 4.93 |

Ondo Stocks products can achieve performance of that kind because they directly inherit their liquidity profile from traditional onshore U.S. markets. When an eligible investor requests a quote, we compute it based on real-time market conditions from traditional markets. That quote is the bridge passing through onchain the same liquidity and market depth the investor would have from accessing the stock markets directly. Once the investor accepts the quote, the smart contract instantly mints or redeems the token against stablecoins at the agreed price. At the same time, the Ondo issuer purchases the underlying securities. All this happens within a few seconds, enabling arbitrage to keep prices onchain and in traditional markets in sync.

### The bigger picture

This approach means our design channels new investor demand into the underlying U.S.-listed assets themselves. Put differently, when tokenization is structured in this way, global access is not a substitute for U.S. capital markets; it is a new route into them. The economic center of gravity remains the U.S.-listed underlying. The token is the access layer. The security listed and traded in U.S. markets remains the reference asset and the anchor.

Some of the most relevant lines in the *Tokenized Stocks* paper are also among its most modest. The authors conclude that tokenized stocks and the actual stocks are “tightly linked markets” with an “absence of sustained large differences.” That is exactly the sort of finding one would expect from a market structure linked by arbitrage and redemption, but not necessarily open in the same way at every hour of every day. Multiple points of access need not imply multiple disconnected markets. Sometimes they do. Sometimes they do not. The difference lies in the quality of the linkage.

That does not mean the remaining design questions are trivial. They are not. One can have a serious discussion about how wide arbitrage bands are when the primary market is closed, how much off-hour price action is informative rather than noisy, how cross-chain distribution should be handled, and what investor protections should follow the asset when the transfer layer becomes more portable. Those are good questions. They are also much more specific than the claim that tokenization “splits liquidity” and therefore needs no further analysis.

### Moving forward

From where things stand today, the broader direction of travel is not mysterious. Capital markets are moving toward more continuous access, more programmable ownership, and more flexible settlement, while policymakers and firms work to preserve the legal clarity, market depth, and operational discipline that make the traditional system valuable in the first place. Well-designed tokenization projects can deepen the global relevance of U.S.-listed assets, broaden the investor base that can reach them, and send more demand back to the onshore U.S. markets where those assets are listed and traded. That is not a departure from the strengths of U.S. capital markets. It is a continuation of the long-running effort to improve and extend them.

Ondo is not the whole story, but we do think our model is a promising catalyst that shines a light on a more expansive frontier: not a separate island, but a stronger connection between onchain distribution and offchain market depth. New systems always need refinement. That is normal. The important point is that we have now reached the stage where the conversation should become more precise, not less. On that score, the recent evidence is encouraging.

**References**
Cong, Landsman, Rabetti, Zhang, and Zhao, *Tokenized Stocks* (Dec. 2025).

*¹ Adjusted to exclude fees and adjustments.*

Next

[[그림: Institutions Can Now Access Ondo Tokenized Stocks via Gate through Talos]

Ondo Stocks•Mar 31, 2026

### Institutions Can Now Access Ondo Tokenized Stocks on Talos via Gate](https://ondo.finance/blog/institutions-can-access-ondo-tokenized-stocks-via-talos-gate)

[[그림: Hyperliquid Ecosystem Gains Access to 260+ Ondo Tokenized Stocks via Felix]

Ondo Stocks•Mar 26, 2026

### Hyperliquid Ecosystem Gains Access to 260+ Ondo Tokenized Stocks via Felix](https://ondo.finance/blog/hyperliquid-ecosystem-gains-access-ondo-tokenized-stocks-via-felix)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://ondo.finance/blog"},{"@type":"ListItem","position":3,"name":"Anchored Onshore: How Ondo Stocks Extends the Reach of U.S. Capital Markets","item":"https://ondo.finance/blog/extending-us-markets-reach"}]}
```