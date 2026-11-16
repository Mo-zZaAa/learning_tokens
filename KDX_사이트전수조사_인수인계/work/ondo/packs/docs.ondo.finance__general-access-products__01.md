# 읽기 묶음: docs.ondo.finance / general-access-products (1/1)


<<<PAGE https://docs.ondo.finance/general-access-products/usdy/basics>>>
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

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins
title: Comparison to Stablecoins - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

USDY

# Comparison to Stablecoins

Copy pageCopy page

Copy pageCopy page

USDY is not classified as a traditional stablecoin; instead, it is a tokenized secured note. Like stablecoins, USDY operates as a bearer asset that can be transferred to investors without their needing to be onboarded with the issuer, although onboarding is necessary for minting or redeeming. However, unlike with stablecoins, USDY holders earn almost all of the yield from the assets that back USDY.Below is a table that compares stablecoins and USDY:

|  | Stablecoins | USDY |
| --- | --- | --- |
| Bankruptcy-remoteness | Stablecoins are generally issued out of operating companies. If a stablecoin issuer went bankrupt, including for reasons unrelated to operating their respective stablecoins, holders may be unable to redeem | USDY is issued by Ondo Global Markets (BVI) Limited, a company that is designed to be bankruptcy-remote from any other entities, including Ondo operating companies |
| Yield | Stablecoin holders receive no direct interest | USDY holders receive yield generated from the underlying assets (less amounts to satisfy fees, obligations, and expenses) in the form of increasing redemption value |
| Secured by high-quality assets | Stablecoins are generally unsecured liabilities of their issuers with no security interest in the assets that back them and are at risk of being subordinated to the claims of other creditors | USDY holders have a security interest in the assets that back it |
| Regulatory status | Stablecoins exist in a regulatory gray area and are not structured in a way to be able to pay holders a yield | USDY is issued in compliance with US federal and state securities and financial crime compliance laws |
| Third-party oversight | Stablecoin issuers can, in many cases, unilaterally change the type of assets that back them | Ankura Trust Company protects USDY holders as Verification Agent and Collateral Agent, enforcing narrow eligibility criteria and is able to force a wind-down in an event of non-compliance |
| Timely redemptions | If stablecoin issuers fail to meet redemption requests within a timely manner, there would be no Event of Default nor automatic wind-down process. Rather, stablecoin holders would likely need to litigate in court to recover their assets | If either Ondo USDY LLC (the previous issuer of USDY) or Ondo Global Markets (BVI) Limited fails to meet a redemption request in a timely manner, an Event of Default will occur, mandating Ankura Trust to liquidate the investment portfolio and repay token holders, subject to USDY holder approval |

[USDY Basics](https://docs.ondo.finance/general-access-products/usdy/basics)[USDY vs Rebasing USDY (rUSDY)](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins","name":"Comparison to Stablecoins","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"Comparison to Stablecoins","item":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins#article","headline":"Comparison to Stablecoins","name":"Comparison to Stablecoins","url":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/eligibility>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/eligibility
title: Eligibility - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Jurisdiction-Based Prohibitions:](https://docs.ondo.finance/general-access-products/usdy/eligibility)
* [Jurisdiction-Based Restrictions:](https://docs.ondo.finance/general-access-products/usdy/eligibility)

USDY

# Eligibility

Copy pageCopy page

Copy pageCopy page

This page provides information on the types of persons that are prohibited or restricted from subscribing for, acquiring or redeeming USDY tokens.

### Jurisdiction-Based Prohibitions:

Ondo prohibits business activities from certain jurisdictions in accordance with its Compliance policies. By agreeing to a business relationship with Ondo, any partners agree to not offer Ondo related products or services in connection with any of the outlined prohibited jurisdictions. Individuals located or residing in and entities organized under the laws of or with a principal place of business in, any jurisdiction listed below (**“Prohibited Persons”**) are prohibited from subscribing for, acquiring or redeeming USDY tokens:

* Afghanistan
* Belarus
* Canada
* Crimea, Donetsk People’s Republic (DNR), Luhansk People’s Republic (LNR), Kherson and Zaporizhzhia regions (Ukraine), the city of Sevastopol
* Cuba
* Democratic Republic of Korea
* Iran
* Libya
* Myanmar
* Russia
* Somalia
* South Sudan
* Sudan
* Syria
* United States, or any of its states, possessions, territories or federal districts\*

\* Persons who place buy orders from within the United States, or any of its states, possessions, territories or federal districts, and persons who are “US persons” or acting for the account or benefit of any “US persons” within the meaning of Rule 902 of Regulation S promulgated under the United States Securities Act of 1933, as amended, are also prohibited from subscribing for, acquiring or redeeming USDY tokens.
Ondo Global Markets (BVI) Limited, the issuer of USDY tokens, also prohibits persons from subscribing for, acquiring or redeeming its tokens if it determines, in its sole discretion, that such activity may constitute a violation of (i) applicable laws, rules or regulations, including but not limited to sanctions restrictions, (ii) the terms of the USDY tokens’ governing documents; or (iii) the issuer’s governing documents and policies. In addition, if Prohibited Persons, directly or indirectly, hold in the aggregate 50% or more beneficial ownership or control of any entity, such entity may also be (or will be, if Prohibited Persons are prohibited as a result of applicable sanctions regulations) prohibited from subscribing for, acquiring or redeeming USDY tokens.

### Jurisdiction-Based Restrictions:

Individuals residing in or, in certain cases, citizens of, and entities organized under the laws of or with a principal place of business in, any jurisdiction in the table set forth below must satisfy one or more of the eligibility requirements set forth opposite the name of such jurisdiction in order to be issued USDY tokens. For convenience purposes only, the below table also lists the key financial thresholds that are generally sufficient for an individual or entity to satisfy the applicable requirements; however, such information is provided only as a guide and does not amend, replace or supersede the requirements set forth under applicable laws, rules or regulations. Please refer to the applicable jurisdiction’s law, rules and regulations for definitions of the defined terms used in the table below. To onboard with the token issuer, Restricted Persons generally will be required to produce evidence that they satisfy the applicable eligibility requirements and to certify or declare their eligible status.

| Jurisdiction | Eligibility Requirements | Summary of Key Financial Thresholds (Individuals) | Summary of Key Financial Thresholds (Entities) |
| --- | --- | --- | --- |
| **Brazil** | ”Qualified Investor” under CVM Resolution No. 30, of May 11th, 2021 (Article 12) | R$1 million in financial investments; or approved technical qualification/certification | Professional investors; investment funds; or investment clubs (managed by Qualified Investors) |
|  | “Professional Investor” under CVM Resolution No. 30, of May 11th, 2021 (Article 11) | R$10 million in financial investments; non-resident investor; or professionals who hold certain financial services accreditation by the Brazilian Securities Commission (Comissão de Valores Mobiliários - CVM) | Financial institutions; insurance/capitalization companies; pension entities; investment funds; or investment clubs (managed by CVM-authorized managers) |
| **Any Member State of the European Economic Area** | ”Professional Client” under MiFID II, Annex II, Section I; or “Qualified Investor” under article 2(1)(e) of Prospectus Regulation (EU) 2017/1129 | Applicable for entities or individuals:  Fulfill 2 of the 3 below criteria: EUR 500,000 financial portfolio; 10 significant transactions/quarter over the previous 4 quarters; or 1 year of financial sector experience | Certain regulated financial institutions, or large undertakings that meet two of the following three size requirements: balance sheet total of at least EUR 20 million; net turnover of at least EUR 40 million; or own funds of at least EUR 2 million |
| **Hong Kong** | ”Professional Investor” (Individual) under the Securities and Futures (Professional Investor) Rules (PI Rules) | HK$8 million portfolio value (alone or with associates) | Not applicable |
|  | ”Professional Investor” (Corporate/Trust) under the Securities and Futures (Professional Investor) Rules (PI Rules) | Not applicable | Trust corporations with HK$40 million total assets; corporations or partnerships with HK$8 million portfolio or HK$40 million total assets; or investment holding corporations wholly owned by Professional Investors |
|  | ”Professional Investor” (Institutional) under the Securities and Futures Ordinance (SFO) Schedule 1 Part 1 | Not applicable | Recognized exchange companies; intermediaries; financial institutions; insurers; collective investment schemes; governments; or central banks |
| **Malaysia** | ”Sophisticated Investor” (“High Net Worth Individual”) under the Capital Markets and Services Act 2007 | RM 3 million net personal/joint assets (excluding primary residence); or RM 300,000 annual income (individual) / RM 400,000 annual income (joint) | Not applicable |
|  | ”Sophisticated Investor” (“High Net Worth Entity”) under the Capital Markets and Services Act 2007 | Not applicable | Trust companies or public company trustees with RM 10 million assets under management; corporations or partnerships with RM 10 million total net assets; statutory bodies; or pension funds |
|  | ”Sophisticated Investor” (Accredited Investor) under the Capital Markets and Services Act 2007 | Not applicable | Unit trust schemes; Capital Markets Services Licence (CMSL) holders; licensed banks; closed-end funds; or similar regulated entities |
| **Singapore** | ”Accredited Investor” under Securities and Futures Act (SFA) (Section 4A(1)) | S$2 million net personal assets (max S$1 million from primary residence); S$1 million financial assets (net of liabilities); or S$300,000 annual income | S$10 million net assets |
|  | ”Institutional Investor” under the Securities and Futures Act (SFA) (Section 4A(1)(c)) | Not applicable | Governments; central banks; regulated financial institutions; pension funds; collective investment schemes; or other similarly regulated financial institutions |
| **Switzerland** | FinSA “Professional Client” or “Institutional Client” in accordance with Article 4, paragraphs 3 and 4 of the Swiss Financial Services Act. | Not applicable. | Regulated financial intermediary; insurance company; foreign client subject to prudential supervision; central bank; certain public entities; pension fund; company with professional treasury operations; or a large company meeting two of the following three criteria: CHF 20 million balance, CHF 40 million turnover, CHF 2 million equity; private investment structures with professional treasury operations that have been established for High Net Worth Individuals (HNWI) |
| **United Kingdom** | ”Professional Client” under MiFID II, Annex II, Section I; or “Qualified Investor” under article 2(1)(e) of Prospectus Regulation (EU) 2017/1129 | Fulfill 2 of the 3 below criteria: EUR 500,000 financial portfolio; 10 significant transactions/quarter over the previous 4 quarters; or 1 year of financial sector experience | Certain regulated financial institutions, or large undertakings meeting two of the following three: balance sheet total of at least EUR 20 million; net turnover of at least EUR 40 million; or own funds of at least EUR 2 million |

Please note that Ondo Global Markets (BVI) Limited also imposes non-jurisdiction-related eligibility criteria in accordance with its know-your-customer policies, procedures and practices and contractual agreements.
For certain important notes related to USDY tokens, please see [Important Notes](https://docs.ondo.finance/general-access-products/usdy/important-notes).

[USDY Price Oracle](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)[Important Notes](https://docs.ondo.finance/general-access-products/usdy/important-notes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/eligibility#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/eligibility","name":"Eligibility","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/eligibility#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/eligibility#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"Eligibility","item":"https://docs.ondo.finance/general-access-products/usdy/eligibility"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/eligibility#article","headline":"Eligibility","name":"Eligibility","url":"https://docs.ondo.finance/general-access-products/usdy/eligibility","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/eligibility#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/important-notes>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/important-notes
title: Important Notes - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

USDY

# Important Notes

Copy pageCopy page

Copy pageCopy page

[\*] USDY tokens have not been registered under the US Securities Act of 1933, as amended (the “Act”) or the securities or financial instrument laws of any other jurisdiction, and may not be offered or sold in the US or to US persons unless registered under the Act or an exemption from the registration requirements thereof is available. In certain jurisdictions, including the United Kingdom, Switzerland and Singapore, the tokens are offered and sold only to qualified investors or professional clients, as the case may be (or that jurisdiction’s analogue thereof). [Other jurisdiction-based prohibitions and restrictions apply](https://docs.ondo.finance/general-access-products/usdy/eligibility). The issuer of USDY is not registered as an investment company under the US Investment Company Act of 1940, as amended, or as an Alternative Investment Fund or Undertaking for Collective Investment in Transferable Securities in the European Economic Area, or under the securities or financial instrument laws of any other jurisdiction.
USDY tokens provide their holders with economic exposure to short-term US treasuries, but USDY tokens are not themselves US treasuries and do not provide their holders with rights to hold or receive any US treasuries.
In the United Kingdom, the communications herein may be deemed a financial promotion pursuant to Section 21 of the Financial Services and Markets Act 2000. To the extent that any such finding is made, the communications herein are only intended for, and directed at, investment professionals as defined in article 19 of the Financial Services and Markets Act 2000 (Financial Promotions) Order 2005 (the “FPO”) who have experience of interacting with the USDY tokens; high net worth companies as defined in article 49 of the FPO, and/or any other persons to whom lawful communication is permitted. Any person not falling within these categories is not permitted to act upon anything within the communications herein, and shall not be entitled to rely upon their contents. Ondo Global Markets (BVI) Limited will not enter into arrangements with such persons concerning USDY tokens as a result of this or any other communication.
USDY tokens are issued by Ondo Global Markets (BVI) Limited, a British Virgin Islands business company. Ondo Finance Inc., a Delaware (USA) corporation, provides tokenization services to, and is an equity holder of, Ondo Global Markets (BVI) Limited.
The USDY token issuer, its affiliates, their respective shareholders and members, and their respective directors, officers, employees, consultants, agents and representatives (the “Ondo Persons”) do not endorse, the Ondo Persons do not make any representation or warranty whatsoever (express or implied, including but not limited to any warranty of merchantability, fitness for a particular purpose, or non-infringement) regarding, and THE ONDO PERSONS SHALL NOT HAVE ANY LIABILITY WHATSOEVER WITH RESPECT TO ANYONE’S USE OF, any third-party products, services or technologies referenced herein.
Nothing herein constitutes any offer to sell, or any solicitation of an offer to buy, any assets. Nothing herein constitutes investment, legal, tax or financial advice. Acquiring tokens involves risks. A holder of tokens may incur losses, including total loss of their purchase price. Past performance may not be (and for the tokens will not be) an indication of future results. Investors are responsible for conducting their own research, investigation, verification, checks or consultation for professional or investment advice.
The communications herein may contain forward-looking statements, including, but not limited to, statements regarding future financial performance, business strategies, or expectations for the growth or development of Ondo Finance, Ondo Global Markets (BVI) Limited, or any of their respective affiliates (each, an “Applicable Entity”). These statements are based on management’s current expectations, estimates, projections, and beliefs, and are subject to a number of risks, uncertainties, and assumptions that could cause actual results to differ materially from those anticipated. Forward-looking statements can be identified by the use of terminology such as “may,” “will,” “should,” “expect,” “intend,” “plan,” “anticipate,” “believe,” “estimate,” “predict,” “potential,” “continue,” or the negative of these terms or other similar expressions. Factors that could cause actual results to differ materially from those contemplated by the forward-looking statements include, but are not limited to, the following: economic, competitive, legal, governmental, and technological factors affecting the operations, markets, products, services, or prices of any Applicable Entity. No Applicable Entity undertakes any obligation to update or revise any forward-looking statements, whether as a result of new information, future events, or otherwise, except as required by law.
Additional terms and restrictions apply. See [docs.ondo.finance/legal/terms-of-service](https://docs.ondo.finance/legal/terms-of-service), [docs.ondo.finance/general-access-products/usdy](https://docs.ondo.finance/general-access-products/usdy/basics), [ondo.finance/usdy](https://ondo.finance/usdy), [app.ondo.finance](https://app.ondo.finance/) and (as applicable) the token offering documents for details.

[Eligibility](https://docs.ondo.finance/general-access-products/usdy/eligibility)[Cash Management 101](https://docs.ondo.finance/qualified-access-products/cash-management-101)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/important-notes#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/important-notes","name":"Important Notes","dateModified":"2026-11-07T00:41:58.301Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/important-notes#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/important-notes#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"Important Notes","item":"https://docs.ondo.finance/general-access-products/usdy/important-notes"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/important-notes#article","headline":"Important Notes","name":"Important Notes","url":"https://docs.ondo.finance/general-access-products/usdy/important-notes","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/important-notes#webpage"},"dateModified":"2026-11-07T00:41:58.301Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/rebasing>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/rebasing
title: Rebasing - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What is rebasing and how does it work? How is it different than airdropping?](https://docs.ondo.finance/general-access-products/usdy/rebasing)
* [How often do you rebase rUSDY?](https://docs.ondo.finance/general-access-products/usdy/rebasing)
* [What is the difference between rebasing rUSDY and updating the USDY token price onchain?](https://docs.ondo.finance/general-access-products/usdy/rebasing)
* [How do I convert between USDY and rUSDY?](https://docs.ondo.finance/general-access-products/usdy/rebasing)

USDY

# Rebasing

Copy pageCopy page

Copy pageCopy page

### **What is rebasing and how does it work? How is it different than airdropping?**

Rebasing is a mechanism through which the total supply of tokens is adjusted. Rebasing works by taking the “base” number of tokens, T, and multiplying it by some “rebasing factor”, RF, to get a new number of tokens. For example, let’s say there were a total of 100 tokens: 10 were held by Holder A (10% of the total) and 90 by Holder B (90% of the total). In a rebasing, we might want to double the total number of tokens (i.e. a rebasing factor of 2). We multiply each holder’s balance by the Rebasing Factor — 2 in this case — so after rebasing a total of 200 tokens are outstanding in which Holder A has 20 tokens (still 10% of the total) and Holder B has 180 tokens (still 90% of the total). Economically, Holder A and Holder B are in the same position both before and after rebasing.
How can we do this? One way would be to mint and airdrop new tokens to each token holder. This would cost a lot of gas, however, because it requires updating each token contract storage location that represents a user’s balance. Rebasing allows us to adjust all token holder balances in a gas-efficient manner by introducing the concept of user “shares”. A “share” is similar to a share of a company’s stock - it can be thought of as a claim on a percentage of the total supply of rUSDY tokens (and, in fact, the concept of rebasing is similar to the concept of a share split – except rebasing is automatic). A user’s balance is then equal to the percentage of total shares they hold, multiplied by the total number of tokens:`NumTokens_User = NumTokens_Total * (NumShares_User / NumShares_Total)`When we rebase, therefore, we only have to update ***one*** contract storage location: `NumTokens_Total`. As you can see from the formula above, that will increase the balance in your wallet while keeping your ***percentage*** of the total tokens the same. Here’s an example where we increase `NumTokens_Total` from 100 to 200:

|  | Holder A Shares | Holder B Shares | Total Number of Shares | Total Supply of rUSDY Tokens | Holder A rUSDY Balance | Holder B rUSDY Balance |
| --- | --- | --- | --- | --- | --- | --- |
| Before Rebasing | 1 | 9 | 10 | 100 | (1/10) \* 100 = 10 rUSDY Tokens | 9/10\* 100 = 90 rUSDY Tokens |
| After Rebasing | 1 | 9 | 10 | 200 (increase) | (1/10) \* 200 = 20 rUSDY Tokens | 9/10 \* 200 = 180 rUSDY Tokens |

And what number do we set the `NumTokens_Total` to be? We set it equal to the Total Value Locked (TVL) of rUSDY at the current USDY price. In other words, we set `NumTokens_Total = TVL`, thereby making `TVL / NumTokens_Total equal` to $1.00.The rebasing factor RF, then, is calculated as `RF = NumTokens_Total_New / NumTokens_Total_Old`.We can use a simple example to check this. Let’s say that at one point the total number of tokens (NumTokens\_Total\_Old) was 2 (implying an rUSDY TVL of $2.00). Let’s also say that, some time later, the price of USDY had increased to $2, so the TVL of rUSDY (TVL) was now $4. This implies that the Reference Token Price - the ‘face value’ of the rUSDY token price - is 4 dollars / 2 tokens = $2 per token. To keep the Reference Token price per rUSDY token equal to $1.00, we need to double the number of tokens. In this case, the RF would be 2 ($4/$2 = 2). As a result, because the number of rUSDY tokens doubled for everyone, the Reference Token Price per rUSDY token would be reduced to $1.00 per token.Finally, please note that when your rUSDY balance increases due to rebasing, you will see the balance increase in your wallet, but you will not see an accompanying transaction in your wallet’s activity or on a block explorer. This is because the tokens are simply being rebased rather than tokens being sent to the holder’s wallet.

### **How often do you rebase rUSDY?**

rUSDY rebases continuously. rUSDY balances are calculated from the current USDY price whenever they are read, so they grow continuously as the USDY price grows, instead of in one step each day.Yield accrues to tokens continuously. Instant redemptions use the USDY price at the moment the redemption is submitted, so they include all yield accrued up to that moment. Please note that rUSDY and USDY holders are not ‘paid out’ yield, but rather that yield is reflected by the increased value of their existing USDY tokens or increased number of rUSDY tokens.

### **What is the difference between rebasing rUSDY and updating the USDY token price onchain?**

The USDY token price (aka the Reference Token Price) is calculated continuously, and rUSDY balances are calculated from that same price, so a “price update” and a “rebase” are effectively the same event and happen together, continuously.

### **How do I convert between USDY and rUSDY?**

Use the [Ondo Converter](https://ondo.finance/convert) on our website to easily convert between USDY and rUSDY

[USDY vs Rebasing USDY (rUSDY)](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy)[USDY Price Oracle](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/rebasing#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/rebasing","name":"Rebasing","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/rebasing#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/rebasing#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"Rebasing","item":"https://docs.ondo.finance/general-access-products/usdy/rebasing"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/rebasing#article","headline":"Rebasing","name":"Rebasing","url":"https://docs.ondo.finance/general-access-products/usdy/rebasing","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/rebasing#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle
title: USDY Price Oracle - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [How the price is calculated](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [Rate changes](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [What changed](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)
* [For integrators](https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle)

USDY

# USDY Price Oracle

Copy pageCopy page

Copy pageCopy page

Starting November 1, 2026 at 00:00 UTC, the USDY price on Ethereum, BNB Chain, Mantle and Tempo comes from the `ContinuousPriceOracle` contract and rises continuously instead of once a day.

**Important for integrators:** The new oracle does not support `getPriceHistorical`. The `USDYOracleWrapper` has never supported it, so nothing changes if you read the wrapper. If your integration calls `getPriceHistorical` on the previous oracle directly, you will need another way to get USDY prices from November 1, 2026 onward.

## How the price is calculated

The oracle stores a price and a yearly rate (APY). Each time the price is read, the oracle calculates it: the stored price, grown continuously at that rate since it was stored. USDY therefore earns yield throughout the day, and rUSDY and mUSD balances grow at the same pace.

## Rate changes

The rate stays in force until Ondo changes it, so the price continues to accrue at that rate without a daily update. Ondo can schedule a new rate to start at a future time. A routine change is limited on-chain to 10% of the current rate (for example, at 3.75% APY, about 0.375 percentage points) and to once every 8 hours. Changes larger than this, or sooner than 8 hours after the last one, can only be made through a timelock.The `ContinuousPriceOracle` contract was audited by Spearbit (March 2025) and Cyfrin (October 2026). See [Smart Contract Audits](https://docs.ondo.finance/audits).

## What changed

Before November 1, 2026, the USDY price came from the Dynamic Rate Oracle, which added a full day of yield at 00:00 UTC and needed a new rate range every month.

|  | Previous oracle (Dynamic Rate Oracle) | New oracle (ContinuousPriceOracle) |
| --- | --- | --- |
| How the price moves | Once a day, at 00:00 UTC | Continuously |
| How the rate is set | Daily rate for a fixed date range | Yearly rate that stays until changed |
| If no update is made | Price stops growing at the end of the range | Price continues to accrue at the current rate |

## For integrators

Read the USDY price from the `USDYOracleWrapper` for your chain, listed on [Smart Contract Addresses](https://docs.ondo.finance/addresses). The wrapper always points to the current USDY oracle, so integrators reading it don’t need to do anything at the switchover or at any future oracle change. The `ContinuousPriceOracle` addresses are listed there for reference. If you calculate the USDY price off-chain, switch to the continuous calculation.The new oracle supports `getPrice()` and `getPriceData()`, which never revert. It does not support `getPriceHistorical`.The previous oracle is expected to be deprecated on December 31, 2026. After that it receives no new rate and is paused, so `getPrice()` and `getPriceData()` on it will fail instead of returning an outdated price. Integrators that read it directly should move to the `USDYOracleWrapper` before then.

[Rebasing](https://docs.ondo.finance/general-access-products/usdy/rebasing)[Eligibility](https://docs.ondo.finance/general-access-products/usdy/eligibility)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle","name":"USDY Price Oracle","dateModified":"2026-11-12T23:39:39.167Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"USDY Price Oracle","item":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#article","headline":"USDY Price Oracle","name":"USDY Price Oracle","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-price-oracle#webpage"},"dateModified":"2026-11-12T23:39:39.167Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```

<<<PAGE https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy>>>
---
url: https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy
title: USDY vs Rebasing USDY (rUSDY) - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [What’s the difference between USDY and rUSDY?](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy)
* [How do I decide between USDY and rUSDY?](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy)
* [How do I convert between USDY and rUSDY?](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy)

USDY

# USDY vs Rebasing USDY (rUSDY)

Copy pageCopy page

Copy pageCopy page

### **What’s the difference between USDY and rUSDY?**

The ‘r’ in rUSDY stands for ‘rebasing’. rUSDY is intended to maintain a price of $1.00 per token (with the accruing yield being represented by the division of rUSDY tokens into more tokens via [rebasing](https://docs.ondo.finance/general-access-products/usdy/rebasing)). By contrast, the accruing yield of USDY tokens gets ‘accumulated’ into the price, such that the price of USDY is intended to appreciate over time. For example, let’s say you held 100 rUSDY tokens and 100 USDY tokens that were each worth a dollar. The next day the USDY price per token increased to $1.01 per token. After the price update and rebasing, your holdings of both rUSDY and USDY would each be worth $101.00. You would still have a balance of 100 USDY tokens worth $1.01 apiece. However, due to the rebasing nature of rUSDY tokens, you would now hold 101 rUSDY tokens worth $1.00 per token.

### **How do I decide between USDY and rUSDY?**

While we believe many tokenholders will want to hold rUSDY because of its intended price stability, certain protocols, exchanges, or custodians may not support rebasing tokens. Regardless, converting between USDY and rUSDY is [easy](https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy).

### **How do I convert between USDY and rUSDY?**

Use the [Ondo Converter](https://ondo.finance/convert) on our website to easily convert between USDY and rUSDY.

[Comparison to Stablecoins](https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins)[Rebasing](https://docs.ondo.finance/general-access-products/usdy/rebasing)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy#webpage","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy","name":"USDY vs Rebasing USDY (rUSDY)","dateModified":"2026-11-07T00:41:58.287Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"USDY","item":"https://docs.ondo.finance/general-access-products/usdy/basics"},{"@type":"ListItem","position":2,"name":"USDY vs Rebasing USDY (rUSDY)","item":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy#article","headline":"USDY vs Rebasing USDY (rUSDY)","name":"USDY vs Rebasing USDY (rUSDY)","url":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy","mainEntityOfPage":{"@id":"https://docs.ondo.finance/general-access-products/usdy/usdy-vs-rebasing-usdy#webpage"},"dateModified":"2026-11-07T00:41:58.287Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```