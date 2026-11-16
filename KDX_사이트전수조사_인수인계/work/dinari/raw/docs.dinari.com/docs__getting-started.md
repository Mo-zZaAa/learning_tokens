---
url: https://docs.dinari.com/docs/getting-started
title: Quickstart
description: Dinari is infrastructure for tokenized real-world assets. Our API lets you offer your users U.S. equities and a yield-bearing dollar, on-chain, without becoming a broker-dealer yourself. We handle the brokerage relationships, settlement, custody, and compliance layer underneath. Partners can sign up…
fetched: 2026-11-16
method: static
plan: skim
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Quickstart

Dinari is infrastructure for tokenized real-world assets. Our API lets you offer your users U.S. equities and a yield-bearing dollar, on-chain, without becoming a broker-dealer yourself. We handle the brokerage relationships, settlement, custody, and compliance layer underneath. Partners can sign up for our account by going to [https://partners.dinari.com.](https://partners.dinari.com/)

# Dinari d**Shares**

Dinari offers our tokenize assets, called [dShares](https://docs.dinari.com/docs/what-is-dshare), as blockchain tokens backed 1:1 by real securities, mostly U.S. equities. Tokens are minted or burned only after the corresponding trade settles in a real brokerage account, so backing is always in sync with supply. The full list of dShares available can be seen on our [Transparency Page](https://app.dinari.com/transparency).

  

## The integration at a glance

Most integrations follow the same seven steps:

```
graph LR
  A[1. Create Entity] --> B[2. Verify identity]
  B --> C[3. Open Account<br/>+ connect Wallet]
  C --> D[4. Fund account]
  D --> E[5. Place orders]
  E --> F[6. Market data +<br/>corporate actions]
  F --> G[7. Deploy to<br/>production]
```

**1. Create an Entity** - An Entity represents your organization or one of your individual customers. It's the root object everything else attaches to.

**2. Perform KYC** - Every entity needs KYC before it can trade. Bring your own provider (Persona, Onfido, and others are supported) or use Dinari's white-label Managed KYC flow.

**3. Open an Account and connect a Wallet** - An Account is the financial account attached to an Entity. Wallets can be Dinari-managed or a self-custody wallet, linked by signed message.

**4. Fund the account** - Production accounts fund with USD+, USDC, or USDT through a connected wallet. In sandbox, call the faucet instead. Note, availability varies by chain.

**5. Place orders** - Dinari supports market and limit orders through our platform.

**6. Pull market data and handle asset lifecycle** - Supported stocks, live quotes, historical prices, and news. Dividends, splits, ticker changes, and mergers are processed for you, but your app needs to reflect them.

**7. Deploy to production** - Complete KYB, swap in production credentials, and point at mainnet contracts.

## Two ways to integrate

#### **API + SDK**

Build your own experience on top of our REST API using the TypeScript, Python, Java, or Go SDKs. Partners have full control over UX and flow.

#### **Hosted Trading**

A white-label, theme-able trading UI, fully hosted by us or self-hosted by you, wired to the same Enterprise API. The fastest route to launch if you don't want to build order entry and portfolio screens from scratch.

## Get started

### 1. Create a partner account

Log in or [sign up](https://partners.dinari.com/auth/register) at [partners.dinari.com](https://partners.dinari.com/).

### 2. Generate a sandbox API key

In the dashboard, select the **Sandbox** environment, then create a new API key. You'll get an **API Key ID** and an **API Secret Key**.

Bash

```
export DINARI_API_KEY_ID="your_key_id"
export DINARI_API_SECRET_KEY="your_secret_key"
```

### 3. Install an SDK

| Language | Library |
| --- | --- |
| Javascript / Typescript | [@dinari/api-sdk](https://www.npmjs.com/package/@dinari/api-sdk) |
| Java | [com.dinari.api:dinari-java](https://github.com/dinaricrypto/dinari-api-sdk-java) |
| Python | [dinari-api-sdk](https://pypi.org/project/dinari-api-sdk) |
| Go | [dinari-api-sdk-go](https://pkg.go.dev/github.com/dinaricrypto/dinari-api-sdk-go) |

### 4. Make your first call

Listing supported stocks needs no Entity, no KYC, and no funding it's the fastest way to confirm your credentials work.

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!,
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!,
  environment: DinariEnvironment.Sandbox,
});

async function main() {
  const stocks = await client.marketData.getStocks({ limit: 20 });
  console.log(stocks);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],
    environment=DinariClientEnvironment.SANDBOX,
)

stocks = client.market_data.get_stocks(limit=20)
print(stocks)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox),
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stocks, err := c.MarketData.GetStocks(context.Background(), &dinari.GetStocksRequest{
		Limit: dinari.Int(20),
	})
	if err != nil {
		log.Fatalf("Failed to list stocks: %v", err)
	}

	fmt.Printf("Stocks: %+v\n", stocks)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStocksRequest;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX)
                .apiKeyId(System.getenv("DINARI_API_KEY_ID"))
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY"))
                .build();

        var stocks = client.marketData().getStocks(GetStocksRequest.builder().limit(20).build());
        System.out.println(stocks);
    }
}
```

## Where to go next

**Onboard your first customer**  
[Entity Management](https://docs.dinari.com/docs/entity-management) → [Identity Verification](https://docs.dinari.com/docs/managing-kyc) → [Regional Requirements](https://docs.dinari.com/docs/regional-requirements) (see [US Customers](https://docs.dinari.com/docs/us) for additional requirements)

**Set up money movement**  
[Managing Accounts](https://docs.dinari.com/docs/managing-accounts) → [Managing Wallets](https://docs.dinari.com/docs/managing-wallets) → [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)

**Start trading**  
[Placing Orders](https://docs.dinari.com/docs/placing-orders) · [Order Types & Behaviors](https://docs.dinari.com/docs/order-type) · [Trading Hours](https://docs.dinari.com/docs/trading-hours) · [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)

**Keep your app in sync**  
[Stock Data](https://docs.dinari.com/docs/stock-data) · [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes) · [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing) — [dividends](https://docs.dinari.com/docs/dividend-payments), [splits](https://docs.dinari.com/docs/stock-split-handling), [ticker changes](https://docs.dinari.com/docs/ticker-changes), [mergers](https://docs.dinari.com/docs/mergers)

**Go deeper on the asset layer**  
[What are dShares™?](https://docs.dinari.com/docs/what-is-dshare) · [Blockchain](https://docs.dinari.com/docs/blockchain) · [Wrapping dShares™](https://docs.dinari.com/docs/wrapping) · [What is USD+?](https://docs.dinari.com/docs/what-is-usd) · [USD+ Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)

**Ship it**  
[Deploy to Production](https://docs.dinari.com/docs/deploy-to-production) · [Partner Fees](https://docs.dinari.com/docs/fees) · [Restrictions](https://docs.dinari.com/docs/restrictions) · [Security](https://docs.dinari.com/docs/security)

---

Full endpoint documentation lives in the [API Reference](https://docs.dinari.com/reference). Recent changes are in the [Changelog](https://docs.dinari.com/changelog). Happy Trading!

Updated 6 days ago

---

[Deploy to production](https://docs.dinari.com/docs/deploy-to-production)

Did this page help you?

Yes

No

Copy Page

* + [Dinari dShares](https://docs.dinari.com/docs/quickstart)
  + - [The integration at a glance](https://docs.dinari.com/docs/quickstart)
    - [Two ways to integrate](https://docs.dinari.com/docs/quickstart)
    - [Get started](https://docs.dinari.com/docs/quickstart)
    - * [1. Create a partner account](https://docs.dinari.com/docs/quickstart)
      * [2. Generate a sandbox API key](https://docs.dinari.com/docs/quickstart)
      * [3. Install an SDK](https://docs.dinari.com/docs/quickstart)
      * [4. Make your first call](https://docs.dinari.com/docs/quickstart)
    - [Where to go next](https://docs.dinari.com/docs/quickstart)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Quickstart","dateModified":"2026-11-10T17:53:39.000Z"}
```