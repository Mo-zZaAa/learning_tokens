---
url: https://ondo.finance/blog/analyzing-return-scenarios
title: Analyzing Return Scenarios | Ondo Finance
description: Case Study using Ondo Alchemix Vaults
Introduction

We often get asked how to compare yields for different farms and how they might compare with the Ondo Tr…
fetched: 2026-11-16
method: static
plan: skim
---

In this article

* [Case Study using Ondo Alchemix Vaults](https://ondo.finance/blog/analyzing-return-scenarios)
* [Introduction](https://ondo.finance/blog/analyzing-return-scenarios)
* [Using the Returns Scenario Calculator](https://ondo.finance/blog/analyzing-return-scenarios)
* [Returns to Variable (aka “Junior”) Tranche](https://ondo.finance/blog/analyzing-return-scenarios)
* [Single asset ALCX pool](https://ondo.finance/blog/analyzing-return-scenarios)
* [Conclusion](https://ondo.finance/blog/analyzing-return-scenarios)
* [Keep up with Ondo](https://ondo.finance/blog/analyzing-return-scenarios)
* [Legal Disclaimers](https://ondo.finance/blog/analyzing-return-scenarios)

Case Study • Aug 13, 2021 • 7 min

# Analyzing Return Scenarios

[Ondo Finance

Official Blog](https://ondo.finance/blog)

[그림: Analyzing Return Scenarios]

#### Case Study using Ondo Alchemix Vaults

#### Introduction

We often get asked how to compare yields for different farms and how they might compare with the Ondo Tranches. We noticed that this is not always straightforward, so we have created a tool to help you with this analysis.

The breakeven yield for an LP should be the mean of the fair single-asset yields of the two assets in the pool plus compensation for expected impermanent loss.

Of course, expectations around future single asset yields and expected impermanent loss vary greatly. Still, the LP yields are often much higher than would be implied by reasonable historical and expected scenarios. In general, this makes sense as a relatively smaller set of investors may be drawn to the complex bundle of exposures that an LP position represents than to the independent single asset yields. Ondo lets users profit from this discrepancy.

As an example let’s say you are contemplating whether to invest in the ALCX-WETH pool or to invest in the single asset ALCX pool.

The ALCX-ETH pool has 113% APR vs. 92% for the ALCX pool (as of August 12, 2021). How should you think about investing between the two pools? How should you think about the Ondo Tranches as an alternative to the single asset staking pool?

With our [Returns Scenario Calculator](https://docs.google.com/spreadsheets/d/1es5HVIvUR8D8Y8ErpMeNd84De5B8zzcgrUs7h5kCnP0/edit?usp=sharing) we enter in our assumptions and understand the expected returns. All one needs to do is make a copy and then enter one’s assumptions in the blue cells of the spreadsheet. Let’s go through an example.

#### Using the Returns Scenario Calculator

What if we are bullish on ALCX and expect it to go up 50% in the next 30 days?

We input in the calculator key assumptions like this 50% increase in the price of ALCX, a 30 day duration, and a 50% APY hurdle rate (pre-set yield) for the Fixed Tranche. Below you can see all of the assumptions we have used:

#### Returns to Variable (aka “Junior”) Tranche

To calculate the returns to the Variable Tranche, we start by calculating the returns to the ETH-ALCX liquidity pool. The returns to the ETH-ALCX liquidity pool breaks down into the following components:

50/50 Portfolio

* The ETH-ALCX liquidity pool returns start with 50% exposure to ETH and 50% exposure to ALCX (the “50/50 Portfolio”). Under the above assumptions the 50/50 Portfolio returns are 25%.

Impermanent Loss (“IL”)

* Impermanent loss erodes the value of the 50/50 Portfolio by -2.5%\*

Trading fee income

* The trading fees automatically get reinvested into the pool. These will scale as the LP grows.
* Let’s assume that daily volume is 10% of the liquidity in the LP pool, this generates a fee APR of 9.13% which is 0.75% yield for our 30 day period.

SUSHI Rewards

* The SUSHI Rewards are relatively small, but since they are a different token than either in the LP pair, they won’t scale as the LP price changes.
* Checking out the [Sushi staking page](https://app.sushi.com/yield) we see that the TVL is $173.8M and the rewards are 308 Sushi per day, and 1,261 ALCX per day. Plugging this into the respective fields in the calculator shows you the duration yield. The Sushi Rewards we assume this dollar amount of rewards at the current Sushi price holds constant which yields 0.06% yield for the 30 day period.

ALCX Rewards

* The ALCX rewards will increase in value if ALCX goes up 50%.
* The ALCX Rewards are the majority of the yield. This is also paid in the token that we assume will go up in price. Though the rewards paid out in the period will depend on the price path over the duration. If we assume a fixed dollar yield like for Sushi Rewards that will likely understate the yield. Therefore we will take the geometric mean of the price (which is more conservative than using the arithmetic mean) and get a 11% yield for the duration.

Adding these together, we get: 25% (50/50 Portfolio) — 2.5% (IL) + 0.70% (Trading fees) + 0.06% (SUSHI rewards) + 10.7% (ALCX rewards) = 34.0% returns to the ETH-ALCX liquidity pool on a dollar basis. If we annualize this we get a 3431% APY.

\*Please note the denominator in this IL calculation is based on the starting capital base, not the 50/50 portfolio ending value as is more commonly done.

Now let’s calculate the returns if you enter into the Variable Tranche specifically. After paying out the 3.4% returns (which is 50% on an annualized basis) to the Fixed Tranche, we are left with 65% returns in the Variable Tranche on a dollar basis, equivalent to 2x the 34% returns to the LP less the 3.4% paid out to the Fixed Tranche (though the 3.4% is paid out on an ETH basis, since we contemplate no change in the ETH price here, it is 3.4% on a dollar basis as well). Now, because ALCX has gone up 50% in price in this scenario, that 65% return on a dollar basis is 10% on an ALCX basis. Annualizing this ALCX return yields a 212% APY.

#### Single asset ALCX pool

Meanwhile, the return for entering into the ALCX single staking pool is 6.5% in ALCX terms for this period (the 77% APR calculated for the 30 day period). Add in the 50% price increase for ALCX and you get 60% total return for ALCX single asset staking. If we annualize this we get 29,857% APY.

The summary section shows you expected returns for the 50% ALCX price scenario. As you can see, the Ondo Variable Tranche would yield 248% APY in ALCX while the single asset ALCX would yield 151% APY.

#### Conclusion

We hope that by sharing our Returns Calculator users will be better informed in deciding which pools or tranches to invest into. This will allow one to see how returns for the Ondo Variable Tranche might improve for instance if the price appreciation in ALCX is over 60 days instead of 30 days. You can easily see that the Ondo Variable Tranche would return 320% APY now compared with 151% APY for the ALCX only pool.

Also if one assumes less price appreciation for ALCX relative to ETH then the returns for the Variable Tranche get even better relative to the Single Asset Staking. For example, if one expects no price appreciation for ALCX over a 60 day duration, then the Variable Tranche’s 521% APY is significantly more than the 151% APY for the Single Asset Staking.

Below is a chart showing how the Variable Tranche performs versus the single asset staking for various ALCX price scenarios. Overall the Variable Tranche performs quite well in most scenarios — only in extreme scenarios cases where the ALCX price drops or rises significantly does it underperform the single asset staking. This is for a 30 day duration.

However, now if we chart these returns for a 365 day duration, we now see that the Variable Tranche will substantially outperform the Single Asset Staking in almost all scenarios.

We hope you will all find this tool useful. Please let us know what you think!

#### Keep up with Ondo

We have a lot of exciting announcements coming up for Ondo, including the second subscription period and the raising of caps on TVL.

Follow us on [Twitter](https://twitter.com/OndoFinance) to stay up to date with announcements.

#### Legal Disclaimers

*This announcement has been written and published by Ondo Finance Inc. and provides no guarantee, commitment, or undertaking to utilize any of its assets, funds, properties or personnel, Ondo Protocol users or other protocol participants. Ondo Finance does not owe, and does not intend to assume, any duties or obligations to Ondo Protocol users or participants, other than duties or obligations arising under laws of general application, such as non-waivable torts.*

*To the maximum extent permitted by applicable law, all software relating to Ondo Protocol is being provided on an as-is, where-is basis, with no representations or warranties being made to Ondo Protocol participants and with no liability to Ondo Finance or any other person involved in the development of Ondo Protocol. The statements set forth in this announcement also are not intended to be representations, warranties, guarantees or assumptions of duty or liability of any kind, and Ondo Finance hereby disclaims the foregoing and will not be liable for any damages arising from use of Ondo Protocol. In the event of any conflict or inconsistency between this announcement or any other communication and the terms of any software license involved in Ondo Protocol, the terms of the software license shall govern to the exclusion of this announcement and such other communications.*

*The forward-looking statements in this announcement are subject to numerous assumptions, risks and uncertainties which are subject to change over time. Such assumptions, risks and uncertainties could cause actual results or developments to differ materially from the results and developments anticipated by us. Even if our anticipated results and developments are realized, such results and developments may nevertheless fail to achieve any or all of the expected benefits anticipated by this announcement. We reserve the right to change the plans, expectations and intentions stated and implied herein at any time and for any reason or no reason, in our sole and absolute discretion, and we undertake no obligation to update publicly or revise any forward-looking statement, whether as a result of new information, future developments or otherwise.*

*This announcement is not intended to provide legal, financial or investment or other advice and we recommend that you do not rely on, and do not make any financial or other decision based on this announcement.*

Next

[[그림: Introducing Ondo Finance]

Announcement•Jul 27, 2021

### Introducing Ondo Finance](https://ondo.finance/blog/introducing-ondo-finance)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://ondo.finance/blog"},{"@type":"ListItem","position":3,"name":"Analyzing Return Scenarios","item":"https://ondo.finance/blog/analyzing-return-scenarios"}]}
```