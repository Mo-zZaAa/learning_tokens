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