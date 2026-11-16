---
url: https://docs.dinari.com/docs/stock-data
title: Stock Data
description: This section provides examples on retrieving the list of stocks supported on Dinari and supporting metadata for those stocks. SDK References Language URL Javascript / Typescript https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#market-data Python https://github.com/din…
fetched: 2026-11-16
method: static
plan: read
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

# Stock Data

This section provides examples on retrieving the list of stocks supported on Dinari and supporting metadata for those stocks.

# SDK References

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

# SDK Examples

## Get list of Stocks

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
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
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
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
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	// Example: Get a list of all stocks
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
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var stocks = client.marketData().getStocks(GetStocksRequest.builder().limit(20).build());
        System.out.println(stocks);
    }
}
```

## Get historical prices for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  const prices = await client.marketData.getStockPriceChart({
    stockId,
    timespan: "DAY",
  });

  console.log(prices);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

prices = client.market_data.get_stock_price_chart(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
    timespan="DAY",
)
print(prices)
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
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	prices, err := c.MarketData.GetStockPriceChart(context.Background(), &dinari.GetStockPriceChartRequest{
		StockID:  stockID,
		Timespan: dinari.StockTickTimespan1Day,
	})
	if err != nil {
		log.Fatalf("Error getting historical prices: %v", err)
	}

	fmt.Printf("Response: %+v\n", prices)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStockPriceChartRequest;
import com.dinari.api.types.StockTickTimespan1;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        var prices = client.marketData().getStockPriceChart(
                stockId,
                GetStockPriceChartRequest.builder().timespan(StockTickTimespan1.DAY).build());
        System.out.println(prices);
    }
}
```

## Get news for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  // Optionally specify a limit on the number of news articles returned
  const news = await client.marketData.getStockNewsByStockId({ stockId, limit: 5 });

  console.log(news);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

news = client.market_data.get_stock_news_by_stock_id(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
    limit=5,
)
print(news)
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
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	news, err := c.MarketData.GetStockNewsByStockID(context.Background(), &dinari.GetStockNewsByStockIDRequest{
		StockID: stockID,
		Limit:   dinari.Int(5),
	})
	if err != nil {
		log.Fatalf("Failed to get stock news: %v", err)
	}

	fmt.Printf("News: %+v\n", news)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStockNewsByStockIdRequest;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        // Optionally specify a limit on the number of news articles returned
        var news = client.marketData().getStockNewsByStockId(
                stockId,
                GetStockNewsByStockIdRequest.builder().limit(5).build());
        System.out.println(news);
    }
}
```

## Get live market quote for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  const quote = await client.marketData.getStockCurrentQuotesRouteV2({ stockId });

  console.log(quote);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

quote = client.market_data.get_stock_current_quotes_route_v2(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
)
print(quote)
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
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	quote, err := c.MarketData.GetStockCurrentQuotesRouteV2(context.Background(), &dinari.GetStockCurrentQuotesRouteV2Request{
		StockID: stockID,
	})
	if err != nil {
		log.Fatalf("Failed to get stock quote: %v", err)
	}

	fmt.Printf("Quote: %+v\n", quote)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        var quote = client.marketData().getStockCurrentQuotesRouteV2(stockId);
        System.out.println(quote);
    }
}
```

Updated 6 days ago

---

[Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)[Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)

Did this page help you?

Yes

No

Copy Page

* + [SDK References](https://docs.dinari.com/docs/stock-data)
  + [SDK Examples](https://docs.dinari.com/docs/stock-data)
  + - [Get list of Stocks](https://docs.dinari.com/docs/stock-data)
    - [Get historical prices for a Stock](https://docs.dinari.com/docs/stock-data)
    - [Get news for a Stock](https://docs.dinari.com/docs/stock-data)
    - [Get live market quote for a Stock](https://docs.dinari.com/docs/stock-data)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Stock Data","dateModified":"2026-11-10T17:53:39.000Z"}
```