---
url: https://ondo.finance/blog/apy-calculations-methodology
title: APY Calculations Methodology | Ondo Finance
description: There are so many ways to calculate projected APY, after all estimating the future is hard! In this post we will briefly go over our methodology for calcula…
fetched: 2026-11-16
method: static
plan: skim
---

In this article

* [Upcoming Vaults](https://ondo.finance/blog/apy-calculations-methodology)
* [Active Vaults](https://ondo.finance/blog/apy-calculations-methodology)
* [Keep up with Ondo](https://ondo.finance/blog/apy-calculations-methodology)
* [Legal Disclaimers](https://ondo.finance/blog/apy-calculations-methodology)

Aug 20, 2021 • 4 min

# APY Calculations Methodology

[Ondo Finance

Official Blog](https://ondo.finance/blog)

[그림: APY Calculations Methodology]

There are so many ways to calculate projected APY, after all estimating the future is hard! In this post we will briefly go over our methodology for calculating APYs.

#### Upcoming Vaults

To calculate the APY for upcoming vaults we take the previous 7 day yield and extrapolate that for the duration of the vault.

We calculate the daily yield from fees. In the case below it would be 0.0025 given the 0.25% trading fee earned by SUSHI LPs.

We calculate the daily rewards yield

We take the yield daily from the fees and rewards and then calculate the 7 day compounded todal.

Why use 7 days? We know that these fees and rewards can vary quite a bit day to day, so we would not want to use something like 1 days since that would cause large changes in displayed APY. We also don’t want to use too long a period such as a month since that could incorporate yields that are significantly different than current rates.

This yield over the last 7 days is then extrapolated for the duration of the vault to determine the combined returns of the vault.

We then split the returns into the Fixed and Variable Yield Components.

Finally in order to calculate the APY from the yield we apply the following formula

This same methodology would be used for Uniswap, except that the rewards there would be zero. Also the trading fee would be 0.30% instead of the 0.25%.

#### Active Vaults

For active vaults the calculation is a bit more complicated. We want to take the existing returns for the vault so far, and then also project out the future fee and reward yields.

Reward returns are calculated using the rewards for the vault so far, and then extrapolated for the duration of the vault.

Remaining fees are calculated assuming the fee yield since vault start are constant for the remaining duration.

Calculate LP returns since the vault started.

Finally, we compound these three return components together to get the total returns for the vault.

We then split them into the fixed and variable components in terms of the underlying token. Since the token prices for the fixed and variable assets have likely changed since the beginning of the vault we will have to account for that in the yield calculations.

Now that we have the yield in the underlying token we can then calculate the APY values given these returns as per the formula.

#### Keep up with Ondo

We have a lot of exciting announcements coming up for Ondo, including the second subscription period and the raising of caps on TVL.

Follow us on [Twitter](https://twitter.com/OndoFinance) and [Telegram](https://t.me/ondofinance) to stay up to date with announcements.

#### Legal Disclaimers

*This announcement has been written and published by Ondo Finance Inc. and provides no guarantee, commitment, or undertaking to utilize any of its assets, funds, properties or personnel, Ondo Protocol users or other protocol participants. Ondo Finance does not owe, and does not intend to assume, any duties or obligations to Ondo Protocol users or participants, other than duties or obligations arising under laws of general application, such as non-waivable torts.*

*To the maximum extent permitted by applicable law, all software relating to Ondo Protocol is being provided on an as-is, where-is basis, with no representations or warranties being made to Ondo Protocol participants and with no liability to Ondo Finance or any other person involved in the development of Ondo Protocol. The statements set forth in this announcement also are not intended to be representations, warranties, guarantees or assumptions of duty or liability of any kind, and Ondo Finance hereby disclaims the foregoing and will not be liable for any damages arising from use of Ondo Protocol. In the event of any conflict or inconsistency between this announcement or any other communication and the terms of any software license involved in Ondo Protocol, the terms of the software license shall govern to the exclusion of this announcement and such other communications.*

*The forward-looking statements in this announcement are subject to numerous assumptions, risks and uncertainties which are subject to change over time. Such assumptions, risks and uncertainties could cause actual results or developments to differ materially from the results and developments anticipated by us. Even if our anticipated results and developments are realized, such results and developments may nevertheless fail to achieve any or all of the expected benefits anticipated by this announcement. We reserve the right to change the plans, expectations and intentions stated and implied herein at any time and for any reason or no reason, in our sole and absolute discretion, and we undertake no obligation to update publicly or revise any forward-looking statement, whether as a result of new information, future developments or otherwise.*

*This announcement is not intended to provide legal, financial or investment or other advice and we recommend that you do not rely on, and do not make any financial or other decision based on this announcement.*

Next

[[그림: Ondo Raises $4M to Balance Risk and Reward for the DeFi Ecosystem]

Announcement•Aug 17, 2021

### Ondo Raises $4M to Balance Risk and Reward for the DeFi Ecosystem](https://ondo.finance/blog/ondo-raises-4m-to-balance-risk-and-reward-for-the-defi-ecosystem)

[[그림: Analyzing Return Scenarios]

Case Study•Aug 13, 2021

### Analyzing Return Scenarios](https://ondo.finance/blog/analyzing-return-scenarios)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://ondo.finance/#organization","name":"Ondo Finance","url":"https://ondo.finance","logo":"https://ondo.finance/images/ondo-icon.svg","foundingDate":"2021","sameAs":["https://x.com/Ondo","https://www.linkedin.com/company/ondo-finance/","https://github.com/ondoprotocol","https://www.youtube.com/@OndoFinance"],"contactPoint":{"@type":"ContactPoint","contactType":"customer support","email":"support@ondo.finance","url":"https://ondo.finance/contact"},"description":"Institutional Grade Finance. Onchain. For Everyone. Ondo Finance bridges traditional finance with blockchain through tokenized real-world assets."},{"@type":"WebSite","@id":"https://ondo.finance/#website","name":"Ondo Finance","url":"https://ondo.finance","publisher":{"@id":"https://ondo.finance/#organization"}}]}
{"@context":"https://schema.org","@type":"BlogPosting","headline":"APY Calculations Methodology","description":"There are so many ways to calculate projected APY, after all estimating the future is hard! In this post we will briefly go over our methodology for calcula…","articleBody":"There are so many ways to calculate projected APY, after all estimating the future is hard! In this post we will briefly go over our methodology for calculating APYs.\nUpcoming Vaults\n\nTo calculate the APY for upcoming vaults we take the previous 7 day yield and extrapolate that for the duration of the vault.\n\nWe calculate the daily yield from fees. In the case below it would be 0.0025 given the 0.25% trading fee earned by SUSHI LPs.\n\n\n\nWe calculate the daily rewards yield\n\n\n\nWe take the yield daily from the fees and rewards and then calculate the 7 day compounded todal.\n\n\n\nWhy use 7 days? We know that these fees and rewards can vary quite a bit day to day, so we would not want to use something like 1 days since that would cause large changes in displayed APY. We also don’t want to use too long a period such as a month since that could incorporate yields that are significantly different than current rates.\n\nThis yield over the last 7 days is then extrapolated for the duration of the vault to determine the combined returns of the vault.\n\n\n\nWe then split the returns into the Fixed and Variable Yield Components.\n\n\n\nFinally in order to calculate the APY from the yield we apply the following formula\n\n\n\nThis same methodology would be used for Uniswap, except that the rewards there would be zero. Also the trading fee would be 0.30% instead of the 0.25%.\nActive Vaults\n\nFor active vaults the calculation is a bit more complicated. We want to take the existing returns for the vault so far, and then also project out the future fee and reward yields.\n\nReward returns are calculated using the rewards for the vault so far, and then extrapolated for the duration of the vault.\n\n\n\nRemaining fees are calculated assuming the fee yield since vault start are constant for the remaining duration.\n\n\n\nCalculate LP returns since the vault started.\n\n\n\nFinally, we compound these three return components together to get the total returns for the vault.\n\n\n\nWe then split them into the fixed and variable components in terms of the underlying token. Since the token prices for the fixed and variable assets have likely changed since the beginning of the vault we will have to account for that in the yield calculations.\n\n\n\nNow that we have the yield in the underlying token we can then calculate the APY values given these returns as per the formula.\nKeep up with Ondo\n\nWe have a lot of exciting announcements coming up for Ondo, including the second subscription period and the raising of caps on TVL.\n\nFollow us on Twitter and Telegram to stay up to date with announcements.\nLegal Disclaimers\n\nThis announcement has been written and published by Ondo Finance Inc. and provides no guarantee, commitment, or undertaking to utilize any of its assets, funds, properties or personnel, Ondo Protocol users or other protocol participants. Ondo Finance does not owe, and does not intend to assume, any duties or obligations to Ondo Protocol users or participants, other than duties or obligations arising under laws of general application, such as non-waivable torts.\n\nTo the maximum extent permitted by applicable law, all software relating to Ondo Protocol is being provided on an as-is, where-is basis, with no representations or warranties being made to Ondo Protocol participants and with no liability to Ondo Finance or any other person involved in the development of Ondo Protocol. The statements set forth in this announcement also are not intended to be representations, warranties, guarantees or assumptions of duty or liability of any kind, and Ondo Finance hereby disclaims the foregoing and will not be liable for any damages arising from use of Ondo Protocol. In the event of any conflict or inconsistency between this announcement or any other communication and the terms of any software license involved in Ondo Protocol, the terms of the software license shall govern to the exclusion of this announcement and such other communications.\n\nThe forward-looking statements in this announcement are subject to numerous assumptions, risks and uncertainties which are subject to change over time. Such assumptions, risks and uncertainties could cause actual results or developments to differ materially from the results and developments anticipated by us. Even if our anticipated results and developments are realized, such results and developments may nevertheless fail to achieve any or all of the expected benefits anticipated by this announcement. We reserve the right to change the plans, expectations and intentions stated and implied herein at any time and for any reason or no reason, in our sole and absolute discretion, and we undertake no obligation to update publicly or revise any forward-looking statement, whether as a result of new information, future developments or otherwise.\n\nThis announcement is not intended to provide legal, financial or investment or other advice and we recommend that you do not rely on, and do not make any financial or other decision based on this announcement.","datePublished":"2021-08-20T19:44:00.000Z","dateModified":"2025-09-30T17:07:45Z","mainEntityOfPage":{"@type":"WebPage","@id":"https://ondo.finance/blog/apy-calculations-methodology"},"image":"https://cdn.sanity.io/images/8k2tqa6n/production/7e3d7a4aeeda52ff33059a75144d65f0f09ea791-744x567.png","publisher":{"@id":"https://ondo.finance/#organization"},"url":"https://ondo.finance/blog/apy-calculations-methodology"}
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://ondo.finance"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://ondo.finance/blog"},{"@type":"ListItem","position":3,"name":"APY Calculations Methodology","item":"https://ondo.finance/blog/apy-calculations-methodology"}]}
```