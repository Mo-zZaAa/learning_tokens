---
url: https://support.kraken.com/articles/xstocks-faq
title: xStocks Frequently Asked Questions | Kraken Support
description: Find answers to common questions about xStocks, including how they work, trading hours, fees, and availability on Kraken.
fetched: 2026-11-16
method: render
plan: read
---

Ask AI

All

Filter by:

All Products

How do I deposit cash into my account?

I need help with account verification

Why can't I access my account?

Are there any crypto withdrawal fees?

I need help signing into my account

1. [Support](https://support.kraken.com/)
2. [xStocks](https://support.kraken.com/categories/xstocks)
3. [xStocks on Kraken](https://support.kraken.com/sections/xstocks-on-kraken)

# xStocks frequently asked questions

Last updated: November 11, 2026

### Overview

What are xStocks?

xStocks are tokenized representations of real U.S. stocks and ETFs. Each xStock is backed 1:1 by the underlying equity, held in regulated custody, and issued as an onchain token on Solana, Ethereum, TON, and Ink.

How are xStocks different from traditional stocks?

xStocks do not confer shareholder rights like voting or dividends paid as cash. They offer price exposure to the underlying asset and pass on the economic benefit of dividends via a rebasing mechanism — not direct shareholder rights.

Unlike traditional brokerage models, xStocks remove friction, costly fees, limited market hours, and complex onboarding, offering instant settlement, fractional investments, 24/7 market access (for select assets), and self-custody. xStocks are built on blockchain technology and use smart contracts for transparency, automation, and cost-efficiency.

| Feature | Traditional Stocks | xStocks |
| --- | --- | --- |
| Trading Hours | Limited to market hours | 24/7\* for select assets on Kraken Pro; 24/7 onchain  UK-listed and EU-listed xStocks trade during their exchange’s hours on Kraken at launch. |
| Settlement Time | 1 business day | Instant or near-instant via smart contracts |
| Accessibility | Limited by geography and intermediaries | Available in 110+ countries (excl. US, UK, Canada, Australia, sanctioned jurisdictions) |
| Transparency | Relies on third parties | Immutable records on blockchain |
| DeFi utility | None | Usable as collateral, lendable, transferable between wallets |

Who can buy xStocks?

xStocks are available to eligible non-U.S. clients in 110+ countries. They are not accessible in the US (or to US persons), Canada, UK, or Australia.

What xStocks are available?

131 assets in total: 100 stocks, 27 ETFs, and 4 specialist assets.   
  
Full listing at [xstocks.fi](https://xstocks.fi/) or via the Kraken app.

### Buying and trading

When can I trade xStocks?

The following 10 US-listed xStocks trade 24/7 on Kraken Pro: $TSLAx, $QQQx, $SPYx, $NVDAx, $CRCLx, $AAPLx, $HOODx, $MSTRx, $GLDx, $GOOGLx.

All other US-listed xStocks trade 24/5 and are not available on weekends. UK-listed and EU-listed xStocks trade during the regular hours of the exchange where the company is listed, and are not available on weekends or exchange market holidays. When withdrawn to a self-hosted wallet, xStocks can be traded 24/7 onchain via DEX integrations.

How do I fund my account to buy xStocks?

You can buy xStocks using fiat, crypto, or stablecoins (including USDC and USDG). Kraken handles the conversion during the trade. Note: USDT is not directly supported, convert to USDC or USD first.

What’s the minimum investment for xStocks?

xStocks allow fractional purchases with as little as $1 USD.

Are there any trading fees?

**On Kraken:**

* No trading fees when purchasing xStocks with USDG or USD.
* Standard Instant Buy trading fees apply when purchasing with other assets.
* A spread may be included in the asset price to lock in a price for each transaction.

**On Kraken Pro:**

* Spot orderbook: -2 bps rebate for makers, 10 bps for takers.
* [Full fee schedule](https://www.kraken.com/features/fee-schedule).

**Conversions:**

* A fixed 1% trading fee applies when converting xStocks.

What is a multiplier?

The multiplier determines the ratio between an xStock and its underlying onchain token. Token issuers (Backed Assets (JE) Limited) update the multiplier when corporate actions like dividends or stock splits occur.   
  
**Dividend example:** When a company pays a dividend, the token issuer reinvests it by acquiring more of the underlying asset, then updates the multiplier so your xStock holdings reflect the increased equity. Your xStock balance increases while the onchain token quantity stays the same.

1. You buy 1 $AAPLx with a multiplier of 1.0 → equals 1 onchain token.
2. A dividend equivalent to 0.1 shares is paid — multiplier is updated to 1.1.
3. Your $AAPLx balance now shows 1.1 shares. If you withdraw, you receive 1 onchain token, now worth 1.1 $AAPLx.   
     
   **Stock split example:** In a 4:1 split, the multiplier is multiplied by 4. All holder balances update automatically. No user action required.

Why has my order quantity changed?

Your executed xStock order quantity may differ from the quantity you ordered for two reasons:

**The multiplier changed while your order was open**

To maintain the same onchain quantity, the xStock amount is updated if the multiplier changes.  
  
Example:

1. 1

   You place an order to buy 1 AAPLx at $200 with a multiplier of 1.0 → equals 1 onchain token.
2. 2

   A dividend equivalent to 0.1 shares is paid while your order is open, so the multiplier is updated to 1.1.
3. 3

   Your order now shows 1.1 AAPLx, but still represents 1 onchain token.

**Quantity is calculated from onchain tokens**

When you place an xStock order, the order quantity is divided by the multiplier, then rounded to 8 decimal places to arrive at the onchain token quantity. This can lead to slight changes in the final displayed amount.  
  
Example:

1. 1

   You place an order to buy 1 TSLAx with a multiplier of 1.3 → equals 0.76923076 onchain tokens.
2. 2

   That maps back to 0.99999999 TSLAx, not exactly 1.

### Price and dividends

How do xStocks track the price of the real stock?

During regular market hours, xStock prices are anchored to the official exchange price of the underlying equity. Market makers quote around the real-time reference price, ensuring tight alignment.   
  
Outside market hours (extended hours and weekends), market makers use alternative data sources including ATS platforms, index futures, and internal models to approximate fair value. Spreads are wider outside market hours. When markets reopen, any price divergence is rapidly corrected via arbitrage — historically under 1% mismatch at Monday open.

Do I receive dividends from xStocks?

Yes, but not as cash. Dividend payouts are automatically reinvested into more of the underlying asset, and your xStocks balance increases to reflect the dividend via the rebasing/multiplier mechanism. There is no separate cash credit or line item, the increase appears as a higher effective token balance in your portfolio.   
  
The rebasing calculation: Net Dividend (after applicable withholding tax, which is 30% for US-listed and regional-listed xStocks) divided by the closing price of the underlying share on the prior day. The multiplier is updated at approximately 8:00 PM EST on the day prior to the Ex-Date.

### Withdrawals and other platforms

Can I withdraw xStocks to a crypto wallet?

Yes, self-custody is supported. You can withdraw your xStocks to a compatible wallet on Solana, Ethereum, TON, or Ink. xStocks tokens are permissionless and freely transferable onchain.

Can I withdraw my xStocks and trade them on tradfi like IBKR?

No. xStocks are onchain tokens — they cannot be transferred to a traditional brokerage account. Holding xStocks is not the same as buying a share of the underlying company. xStocks provide exposure to the value of the stock but do not carry shareholder rights, voting rights, or any legal claim to the underlying company shares or residual assets in the event of the underlying company's liquidation.

Can I use xStocks in DeFi?

Yes. xStocks are permissionless onchain tokens and can be used across DeFi protocols:

* **As collateral:** Deposit $TSLAx or $SPYx into Kamino (Solana) or Morpho (Ethereum) and borrow against them without selling your position.
* **Liquidity provision:** Add xStocks to liquidity pools on Raydium, Orca, or Byreal to earn fees.
* **Lending markets:** Lend xStocks to earn yield via Kamino, Loopscale, JupLend (Solana) or Euler (Ethereum).
* **Earn xPoints:** Hold, provide liquidity, or use lending markets to earn xPoints — Kraken's onchain incentive program (live March 17, 2026).

### Safety

Are xStocks safe to use?

Kraken and Backed Assets (JE) Limited utilize secure custody, audited reserves, and blockchain infrastructure to ensure the safety and transparency of xStock holdings.   
  
Key safeguards:

* **Custody:** Underlying shares are held by Alpaca Securities LLC (FINRA-regulated, SIPC member), with supplemental coverage by Lloyd's of London up to $175M aggregate. InCore Bank is a secondary custodian.
* **Proof of Reserves:** Published weekly onchain, verified by third-party auditors.
* **Audits:** Quarterly ISAE 3000 assurance audits.
* **Bankruptcy remoteness:** The SPV structure is designed so that if Kraken or Backed goes bankrupt, users can still claim the underlying value of their assets directly with Alpaca.

Still, investing in xStocks involves an element of risk. Read Kraken's [xStocks Risk Disclosure](https://www.kraken.com/legal/xstocks) and the Base Prospectus and related [Final Terms](https://assets.backed.fi/legal-documentation).

For the latest information see [xStocks Risk Disclosure](https://www.kraken.com/legal/xstocks) and <https://assets.backed.fi/legal-documentation>

[Overview](https://support.kraken.com/articles/xstocks-faq)[Buying and trading](https://support.kraken.com/articles/xstocks-faq)[Price and dividends](https://support.kraken.com/articles/xstocks-faq)[Withdrawals and other platforms](https://support.kraken.com/articles/xstocks-faq)[Safety](https://support.kraken.com/articles/xstocks-faq)

## Contact us

[Sign in to contact us](https://id.kraken.com/sign-in)

## 펼치거나 눌러야 보이던 내용

### How are xStocks different from traditional stocks? 누른 뒤

- How are xStocks different from traditional stocks?
- xStocks do not confer shareholder rights like voting or dividends paid as cash. They offer price exposure to the underlying asset and pass on the economic benefit of dividends via a rebasing mechanism — not direct shareholder rights.
- Unlike traditional brokerage models, xStocks remove friction, costly fees, limited market hours, and complex onboarding, offering instant settlement, fractional investments, 24/7 market access (for select assets), and self-custody. xStocks are built on blockchain technology and use smart contracts for transparency, automation, and cost-efficiency.
- Feature	Traditional Stocks	xStocks
- Trading Hours	Limited to market hours
- 24/7* for select assets on Kraken Pro; 24/7 onchain
- UK-listed and EU-listed xStocks trade during their exchange’s hours on Kraken at launch.
- Settlement Time	1 business day	Instant or near-instant via smart contracts
- Accessibility	Limited by geography and intermediaries
- Available in 110+ countries (excl. US, UK, Canada, Australia, sanctioned jurisdictions)
- Transparency	Relies on third parties	Immutable records on blockchain
- DeFi utility
- None
- Usable as collateral, lendable, transferable between wallets

### What xStocks are available? 누른 뒤

- What xStocks are available?
- 131 assets in total: 100 stocks, 27 ETFs, and 4 specialist assets.
- Full listing at xstocks.fi or via the Kraken app.

### Are there any trading fees? 누른 뒤

- Are there any trading fees?
- On Kraken:
- No trading fees when purchasing xStocks with USDG or USD.
- Standard Instant Buy trading fees apply when purchasing with other assets.
- A spread may be included in the asset price to lock in a price for each transaction.
- On Kraken Pro:
- Spot orderbook: -2 bps rebate for makers, 10 bps for takers.
- Full fee schedule.
- Conversions:
- A fixed 1% trading fee applies when converting xStocks.

### What is a multiplier? 누른 뒤

- What is a multiplier?
- The multiplier determines the ratio between an xStock and its underlying onchain token. Token issuers (Backed Assets (JE) Limited) update the multiplier when corporate actions like dividends or stock splits occur.
- Dividend example: When a company pays a dividend, the token issuer reinvests it by acquiring more of the underlying asset, then updates the multiplier so your xStock holdings reflect the increased equity. Your xStock balance increases while the onchain token quantity stays the same.
- You buy 1 $AAPLx with a multiplier of 1.0 → equals 1 onchain token.
- A dividend equivalent to 0.1 shares is paid — multiplier is updated to 1.1.
- Your $AAPLx balance now shows 1.1 shares. If you withdraw, you receive 1 onchain token, now worth 1.1 $AAPLx.
- Stock split example: In a 4:1 split, the multiplier is multiplied by 4. All holder balances update automatically. No user action required.

### Can I use xStocks in DeFi? 누른 뒤

- Can I use xStocks in DeFi?
- Yes. xStocks are permissionless onchain tokens and can be used across DeFi protocols:
- As collateral: Deposit $TSLAx or $SPYx into Kamino (Solana) or Morpho (Ethereum) and borrow against them without selling your position.
- Liquidity provision: Add xStocks to liquidity pools on Raydium, Orca, or Byreal to earn fees.
- Lending markets: Lend xStocks to earn yield via Kamino, Loopscale, JupLend (Solana) or Euler (Ethereum).
- Earn xPoints: Hold, provide liquidity, or use lending markets to earn xPoints — Kraken's onchain incentive program (live March 17, 2026).

### Are xStocks safe to use? 누른 뒤

- Are xStocks safe to use?
- Kraken and Backed Assets (JE) Limited utilize secure custody, audited reserves, and blockchain infrastructure to ensure the safety and transparency of xStock holdings.
- Key safeguards:
- Custody: Underlying shares are held by Alpaca Securities LLC (FINRA-regulated, SIPC member), with supplemental coverage by Lloyd's of London up to $175M aggregate. InCore Bank is a secondary custodian.
- Proof of Reserves: Published weekly onchain, verified by third-party auditors.
- Audits: Quarterly ISAE 3000 assurance audits.
- Bankruptcy remoteness: The SPV structure is designed so that if Kraken or Backed goes bankrupt, users can still claim the underlying value of their assets directly with Alpaca.
- Still, investing in xStocks involves an element of risk. Read Kraken's xStocks Risk Disclosure and the Base Prospectus and related Final Terms.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"WebSite","url":"https://kraken.com","description":"Buy, sell, trade and learn about crypto on Kraken — the simple, powerful crypto platform that grows with you.","potentialAction":{"@type":"RegisterAction","target":"https://www.kraken.com/sign-up"},"publisher":{"@context":"https://schema.org","@type":"Organization","name":"Kraken","alternateName":"Kraken Exchange","url":"https://www.kraken.com/","logo":{"@type":"ImageObject","@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","url":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","contentUrl":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","width":900,"height":900,"caption":"Kraken"},"image":{"@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg"},"sameAs":["https://www.facebook.com/KrakenFX","https://twitter.com/krakenfx","https://www.youtube.com/@KrakenCryptoExchange","https://en.wikipedia.org/wiki/Kraken_(company)","https://www.linkedin.com/company/krakenfx","https://www.instagram.com/krakenfx/","https://www.reddit.com/r/Kraken","https://apps.apple.com/us/app/kraken-buy-crypto-bitcoin/id1481947260","https://play.google.com/store/apps/details?id=com.kraken.invest.app&hl=en_US"],"contactPoint":{"@type":"ContactPoint","url":"https://support.kraken.com/hc/en-us/forms","contactType":"Customer Service"},"address":{"@type":"PostalAddress","streetAddress":"237 Kearny St #102","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94108","addressCountry":"US"}}},{"@type":"BreadcrumbList","@id":"https://support.kraken.com/articles/xstocks-faq#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://support.kraken.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://support.kraken.com/articles"},{"@type":"ListItem","position":3,"name":"Xstocks Faq","item":"https://support.kraken.com/articles/xstocks-faq"}]},{"@type":"WebPage","@id":"https://support.kraken.com/articles/xstocks-faq#webpage","url":"https://support.kraken.com/articles/xstocks-faq","name":"xStocks Frequently Asked Questions | Kraken Support","description":"Find answers to common questions about xStocks, including how they work, trading hours, fees, and availability on Kraken.","isPartOf":{"@id":"https://support.kraken.com/#website"},"publisher":{"@id":"https://support.kraken.com/#organization"},"breadcrumb":{"@id":"https://support.kraken.com/articles/xstocks-faq#breadcrumb"}}]}
{"@context":"https://schema.org","@graph":[{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are xStocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>xStocks are tokenized representations of real U.S. stocks and ETFs. Each xStock is backed 1:1 by the underlying equity, held in regulated custody, and issued as an onchain token on Solana, Ethereum, TON, and Ink.\u003c/p>\u003c/div>"}},{"@type":"Question","name":"How are xStocks different from traditional stocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>xStocks do not confer shareholder rights like voting or dividends paid as cash. They offer price exposure to the underlying asset and pass on the economic benefit of dividends via a rebasing mechanism — not direct shareholder rights. \u003c/p>\u003cp>Unlike traditional brokerage models, xStocks remove friction, costly fees, limited market hours, and complex onboarding, offering instant settlement, fractional investments, 24/7 market access (for select assets), and self-custody. xStocks are built on blockchain technology and use smart contracts for transparency, automation, and cost-efficiency.\u003c/p>\u003c/div>\n\u003ctable>\n\u003ctr>\u003ctd>Feature\u003c/td>\u003ctd>Traditional Stocks\u003c/td>\u003ctd>xStocks\u003c/td>\u003c/tr>\n\u003ctr>\u003ctd>Trading Hours\u003c/td>\u003ctd>Limited to market hours\u003c/td>\u003ctd>\u003cp>24/7* for select assets on Kraken Pro; 24/7 onchain\u003c/p>\u003cp>UK-listed and EU-listed xStocks trade during their exchange’s hours on Kraken at launch.\u003c/p>\u003c/td>\u003c/tr>\n\u003ctr>\u003ctd>Settlement Time\u003c/td>\u003ctd>1 business day\u003c/td>\u003ctd>Instant or near-instant via smart contracts\u003c/td>\u003c/tr>\n\u003ctr>\u003ctd>Accessibility\u003c/td>\u003ctd>Limited by geography and intermediaries\u003c/td>\u003ctd>\u003cp>Available in 110+ countries (excl. US, UK, Canada, Australia, sanctioned jurisdictions)\u003c/p>\u003c/td>\u003c/tr>\n\u003ctr>\u003ctd>Transparency\u003c/td>\u003ctd>Relies on third parties\u003c/td>\u003ctd>Immutable records on blockchain\u003c/td>\u003c/tr>\n\u003ctr>\u003ctd>\u003cp>DeFi utility\u003c/p>\u003c/td>\u003ctd>\u003cp>None\u003c/p>\u003c/td>\u003ctd>\u003cp>Usable as collateral, lendable, transferable between wallets\u003c/p>\u003c/td>\u003c/tr>\n\u003c/table>"}},{"@type":"Question","name":"Who can buy xStocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>xStocks are available to eligible non-U.S. clients in 110+ countries. They are not accessible in the US (or to US persons), Canada, UK, or Australia.\u003c/p>\u003c/div>"}},{"@type":"Question","name":"What xStocks are available?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>131 assets in total: 100 stocks, 27 ETFs, and 4 specialist assets. \u003cbr>\u003cbr>Full listing at \u003ca target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"http://xstocks.fi\">xstocks.fi\u003c/a> or via the Kraken app.\u003c/p>\u003c/div>"}}]}]}
{"@context":"https://schema.org","@graph":[{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"When can I trade xStocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>The following 10 US-listed xStocks trade 24/7 on Kraken Pro: $TSLAx, $QQQx, $SPYx, $NVDAx, $CRCLx, $AAPLx, $HOODx, $MSTRx, $GLDx, $GOOGLx. \u003c/p>\u003cp>All other US-listed xStocks trade 24/5 and are not available on weekends. UK-listed and EU-listed xStocks trade during the regular hours of the exchange where the company is listed, and are not available on weekends or exchange market holidays. When withdrawn to a self-hosted wallet, xStocks can be traded 24/7 onchain via DEX integrations.\u003c/p>\u003c/div>"}},{"@type":"Question","name":"How do I fund my account to buy xStocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>You can buy xStocks using fiat, crypto, or stablecoins (including USDC and USDG). Kraken handles the conversion during the trade. Note: USDT is not directly supported, convert to USDC or USD first.\u003c/p>\u003c/div>"}},{"@type":"Question","name":"What’s the minimum investment for xStocks?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>xStocks allow fractional purchases with as little as $1 USD.\u003c/p>\u003c/div>"}},{"@type":"Question","name":"Are there any trading fees?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>\u003cstrong>On Kraken:\u003c/strong>\u003c/p>\u003cul>\u003cli>\u003cp>No trading fees when purchasing xStocks with USDG or USD.\u003c/p>\u003c/li>\u003cli>\u003cp>Standard Instant Buy trading fees apply when purchasing with other assets. \u003c/p>\u003c/li>\u003cli>\u003cp>A spread may be included in the asset price to lock in a price for each transaction.\u003c/p>\u003c/li>\u003c/ul>\u003cp>\u003c/p>\u003cp>\u003cstrong>On Kraken Pro:\u003c/strong>\u003c/p>\u003cul>\u003cli>\u003cp>Spot orderbook: -2 bps rebate for makers, 10 bps for takers. \u003c/p>\u003c/li>\u003cli>\u003cp>\u003ca target=\"_self\" rel=\"noopener noreferrer nofollow\" href=\"https://www.kraken.com/features/fee-schedule\">Full fee schedule\u003c/a>.\u003cbr>\u003c/p>\u003c/li>\u003c/ul>\u003cp>\u003cstrong>Conversions:\u003c/strong>\u003c/p>\u003cul>\u003cli>\u003cp>A fixed 1% trading fee applies when converting xStocks.\u003c/p>\u003c/li>\u003c/ul>\u003c/div>"}},{"@type":"Question","name":"What is a multiplier?","acceptedAnswer":{"@type":"Answer","text":"\u003cdiv>\u003cp>The multiplier determines 
```