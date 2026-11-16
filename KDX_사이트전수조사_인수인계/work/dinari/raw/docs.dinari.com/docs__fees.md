---
url: https://docs.dinari.com/docs/fees
title: Partner Fees
description: Dinari offers competitive pricing for our enterprise API service, see the section below for an overview of our fee structure. For more specific information regarding our fees, contact support@dinari.com
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

# Partner Fees

Dinari offers competitive pricing for our enterprise API service, see the section below for an overview of our fee structure. For more specific information regarding our fees, contact [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection)

# Standard Partner Fees

Dinari does not collect transaction fees from our partners or their end users. We do, however, collect other types of fees. These fees are:

1. [API Access Fees](https://docs.dinari.com/docs/fees)
2. [Network Fees](https://docs.dinari.com/docs/fees)
3. [USDT Conversion Fees](https://docs.dinari.com/docs/fees)
4. [OTC Order Fees](https://docs.dinari.com/docs/fees)

# API Access Fees

API access is billed monthly and starts at **$2,000 per month**. Both basic and enterprise plans are available. Dinari also provides free sandbox access while you evaluate and build. See [Quickstart](https://docs.dinari.com/docs/getting-started) to generate a sandbox key.

Please [Contact us](https://dinari.com/contact-us) us or send an email to [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection) to discuss which plan fits your volume and use case.

# Network Fees

Dinari has two mechanisms for managing network fees:

* Flat Rate Network Charges
* Billing in Arrears

Partners can choose which approach best suits their business model and customer base. See the breakdown of both types below

### Flat Rate Network Charges

For flat rate fees, Dinari uses the following schedule:

| Network | Order Fee |
| --- | --- |
| Standard Network Fee | $0.20 |
| Ethereum Mainnet | Based on ETH Gas Fees |

Because the order fee covers the cost of settling the order on-chain, it is materially higher on ethereum mainnet than on the L2s and other networks Dinari supports. The exact fee for any given order is returned with the order request and permit responses, which is the authoritative figure to display to your users. The final network fee will be added to the total cost of the order being placed.

### Billing in Arrears

Partners also have the ability to aggregate and pay network fees at cost in arrears. This approach is best when partners charge their end users a transaction fee or are willing to batch bill network fees on a monthly basis.

When this option is chosen, partners are required to provide the fee they are charging as part of their market buy. See “How to Set Customer Transaction Fees” at the bottom of this page for more details.

# USDT Conversion Fees

Orders paid or settled in USDT are converted at the prevailing market rate. Dinari charges this rate (determined by oracle pricing) + 3bps markup. These fees are aggregated and charged in a lump sum at the end of each month so that trades can execute at their full value (i.e., the fee is not taken from the transaction itself, but rather billed across all such transactions at month-end).

# OTC Trading Fees

Dinari offers OTC execution to partners seeking trading support for large orders, or who prefer to transact as an institutional partner without API integration.

| Requirement | Detail |
| --- | --- |
| Availability | Partners only |
| Minimum order size | $25,000 |
| Pricing | Spread quoted per trade, typically up to 10 bps |
| Settlement | USDC or USDT |

Larger orders are generally quoted tighter. Small orders and those in thinly traded and low-liquidity names may be quoted wider, and large USDT-settled orders will incorporate conversion fees.

[Contact us](https://dinari.com/contact-us) for a quote on a specific name and size.

# How to Set Customer Transaction Fees

## Setting your own fee

Partners can specify the exact fee to collect on an order by passing the optional `fee` parameter. The scenarios where this would be incorporated is when Dinari is collecting fees on your behalf, or you as a partner have chosen to be billed in arrears.

| Field | Value |
| --- | --- |
| Type | String-encoded decimal |
| Unit | USD |
| Precision | Up to 6 decimal places |
| Constraint | Non-negative |
| Default | $0.20 |

The value provided for payment\_amount is the total amount for the transaction, fees inclusive. Therefore if you are looking to purchase an exact amount of any stock, then you would need to add the fee cost to the total payment amount.

In your manage order request to purchase ***$150.00*** worth of ***Stock X,*** you would set the corresponding parameters to:

* `payment_amount: 150.25`
* `fee: "0.25"`

The ability to set these fees are included for all managed orders placed through the Dinari API or managed orders place using our SDK. The full list of endpoints where this is accepted can be seen below, followed by an example of how to implement these fees using our SDK.

* [Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
* [Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
* [Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
* [Limit Sell Managed Order Request](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [EIP155 Order Request Permit](https://docs.dinari.com/reference/createeip155orderrequestpermit)
* [EIP155 Order Request Permit Transaction](https://docs.dinari.com/reference/createeip155permittransaction)

An example of doing this using our SDK for a ***Market Buy*** through a ***Managed Wallet*** would be:

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const accountId = "your-account-id";
  const stockId = "your-stock-id";

  // Market Buy Order
  const marketBuy = await client.managedOrders.createMarketBuyManagedOrderRequest({
    accountId,
    stockId,
    // Total amount for a $150.00 asset purchase, fee inclusive
    paymentAmount: 150.25,
    // The fee for the purchase
    fee: 0.25,
  });
  console.log(marketBuy);
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

account_id = "your-account-id"
stock_id = "your-stock-id"

# Market Buy Order
market_buy = client.managed_orders.create_market_buy_managed_order_request(
    account_id=account_id,
    stock_id=stock_id,
    # Total amount for a $150.00 asset purchase, fee inclusive
    payment_amount=150.25,
    # The fee for the purchase
    fee=0.25,
)
print(market_buy)
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

	accountID := "your-account-id"
	stockID := "your-stock-id"

	// Market Buy Order
	marketBuy, err := c.ManagedOrders.CreateMarketBuyManagedOrderRequest(context.Background(), &dinari.CreateMarketBuyOrderRequestInput{
		AccountID: accountID,
		StockID:   dinari.String(stockID),
		// Total amount for a $150.00 asset purchase, fee inclusive
		PaymentAmount: 150.25,
		// The fee for the purchase
		Fee: dinari.Float64(0.25),
	})
	if err != nil {
		log.Fatalf("Failed to create market buy order: %v", err)
	}

	fmt.Printf("Market Buy Response: %+v\n", marketBuy)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.managedorders.requests.CreateMarketBuyOrderRequestInput;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String stockId = "your-stock-id";

        // Market Buy Order
        var marketBuy = client.managedOrders().createMarketBuyManagedOrderRequest(
                accountId,
                CreateMarketBuyOrderRequestInput.builder()
                        // Total amount for a $150.00 asset purchase, fee inclusive
                        .paymentAmount(150.25)
                        .stockId(stockId)
                        // The fee for the purchase
                        .fee(0.25)
                        .build());
        System.out.println(marketBuy);
    }
}
```

Updated 6 days ago

---

[Trading Hours](https://docs.dinari.com/docs/trading-hours)[Entity Management](https://docs.dinari.com/docs/entity-management)

Did this page help you?

Yes

No

Copy Page

* + [Standard Partner Fees](https://docs.dinari.com/docs/fees)
  + [API Access Fees](https://docs.dinari.com/docs/fees)
  + [Network Fees](https://docs.dinari.com/docs/fees)
  + - * [Flat Rate Network Charges](https://docs.dinari.com/docs/fees)
      * [Billing in Arrears](https://docs.dinari.com/docs/fees)
  + [USDT Conversion Fees](https://docs.dinari.com/docs/fees)
  + [OTC Trading Fees](https://docs.dinari.com/docs/fees)
  + [How to Set Customer Transaction Fees](https://docs.dinari.com/docs/fees)
  + - [Setting your own fee](https://docs.dinari.com/docs/fees)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Partner Fees","dateModified":"2026-11-10T01:00:11.000Z"}
```