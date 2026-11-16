---
url: https://docs.ondo.finance/ondo-stocks/troubleshooting
title: Troubleshooting - Ondo Finance
description: 
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [I’m trying to buy or sell a tokenized stock and it keeps failing. What should I do?](https://docs.ondo.finance/ondo-stocks/troubleshooting)
* [The price of my token doesn’t match the price of the underlying asset. Why not?](https://docs.ondo.finance/ondo-stocks/troubleshooting)
* [When I am actually buying or selling an Ondo tokenized stock, the price seems to be slightly different from the main price listed? Why?](https://docs.ondo.finance/ondo-stocks/troubleshooting)
* [Why does my wallet show a simulation warning or failure when I try to buy Ondo Stocks?](https://docs.ondo.finance/ondo-stocks/troubleshooting)
* [I’m still having trouble. Who should I contact?](https://docs.ondo.finance/ondo-stocks/troubleshooting)

Ondo Stocks

# Troubleshooting

Copy pageCopy page

Copy pageCopy page

### I’m trying to buy or sell a tokenized stock and it keeps failing. What should I do?

If you’re having trouble buying or selling Ondo Stocks, please first check [status.ondo.finance](https://status.ondo.finance/) to ensure that the platform is operating correctly, the platform and the specific token you are trying to buy or sell are currently available for trading (including, for weekends and holidays, whether the token is enabled for Off-Hours trading). If you are still having issues, you can contact us at [support@ondo.finance](mailto:support@ondo.finance)Our system also has certain risk parameters or rate limits. You may want to wait a few minutes and try again or try a smaller order size.**Please note that we may only be able to support users trying to mint or redeem tokens via our API or web app directly.** If you are trying to buy or sell Ondo tokenized stocks on the secondary market, please contact the market directly.

### The price of my token doesn’t match the price of the underlying asset. Why not?

This is to be expected over time. Ondo Stocks are ‘total return’ trackers, so token prices will often not match the underlying asset. [Read more about this here](https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing).On Solana and BNB Chain, supported wallets and explorers use a display multiplier to adjust the token balances and prices shown to you. This allows changes in shares per token, including those resulting from dividend reinvestment, to be reflected in your displayed balance, with a corresponding adjustment to the price per displayed unit. Wallets and explorers that do not support these adjustments use a presentation similar to Ethereum, where changes in shares per token are reflected in the per-token price. These adjustments affect only how your holdings are displayed; they do not change your onchain token balance or economic exposure.

### When I am actually buying or selling an Ondo tokenized stock, the price seems to be slightly different from the main price listed? Why?

See [this](https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing).

### Why does my wallet show a simulation warning or failure when I try to buy Ondo Stocks?

When purchasing Ondo Stocks through certain Solana applications, your wallet may display a simulation warning such as “Simulation failed” or “This transaction reverted during simulation.”
This is expected behavior and does not indicate a problem with the transaction.

* **Why does this happen?**
  Ondo Stocks use a just-in-time (JIT) minting model. When you buy an Ondo Stocks token, the tokens are minted at the exact moment your swap executes—they don’t exist beforehand. Because your wallet simulates transactions before execution, it cannot predict the balance changes for tokens that haven’t been minted yet. This causes the simulation to fail even though the actual transaction will succeed.
* **Is it safe to proceed?**
  Yes, provided you verify the transaction details before approving:
  + Confirm you are swapping the intended USDC amount
  + Confirm you are sending or receiving the correct Ondo Stocks token (e.g., AAPLon, TSLAon)
  + Confirm the transaction originates from the application you are using

### I’m still having trouble. Who should I contact?

If you are interacting directly via our API or web app, please contact us at [support@ondo.finance](mailto:support@ondo.finance). If you are transacting on the secondary market, please contact that party directly.

[Partners & Media](https://docs.ondo.finance/ondo-stocks/partners-and-media)[Important Notes](https://docs.ondo.finance/ondo-stocks/important-notes)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/ondo-stocks/troubleshooting#webpage","url":"https://docs.ondo.finance/ondo-stocks/troubleshooting","name":"Troubleshooting","dateModified":"2026-11-07T00:41:58.094Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/ondo-stocks/troubleshooting#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/ondo-stocks/troubleshooting#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Stocks","item":"https://docs.ondo.finance/ondo-stocks/overview"},{"@type":"ListItem","position":2,"name":"Troubleshooting","item":"https://docs.ondo.finance/ondo-stocks/troubleshooting"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/ondo-stocks/troubleshooting#article","headline":"Troubleshooting","name":"Troubleshooting","url":"https://docs.ondo.finance/ondo-stocks/troubleshooting","mainEntityOfPage":{"@id":"https://docs.ondo.finance/ondo-stocks/troubleshooting#webpage"},"dateModified":"2026-11-07T00:41:58.094Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```