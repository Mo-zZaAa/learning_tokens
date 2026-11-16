# 읽기 묶음: docs.dinari.com / docs (4/5)


<<<PAGE https://docs.dinari.com/docs/placing-orders>>>
---
url: https://docs.dinari.com/docs/placing-orders
title: Placing Orders
description: Dinari allows users to place orders utilzing the Dinari API and via EVM Direct Interactions
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

# Placing Orders

Dinari allows users to place orders utilzing the Dinari API and via EVM Direct Interactions

# Order Lifecycle

Every dShare order, whether it's a buy or sell, moves through the same four stages. Only the direction of value changes: a buy converts payment tokens into dShares, and a sell converts dShares back into payment tokens.

1. **Validation**: An order is placed against an account that has completed KYC and holds sufficient funds in payment tokens for a buy, or sufficient dShares for a sell. Dinari returns an order record immediately so the order can be tracked from this point forward.
2. **Validation:** Dinari confirms the account's eligibility and balance, then prepares the order for execution. Orders that fail these checks never reach the market.
3. **Execution:** The order is routed to be filled against the underlying security. Market orders fill at the prevailing price; limit orders wait until the limit price is reached, and may expire unfilled.
4. **Settlement:** Once filled, the result is settled on-chain in a single step: a buy mints dShares to the user's wallet, and a sell burns the dShares and releases the proceeds. Tokens and balances only ever move together with the fill a partially settled order is not possible.

An order is complete once it reaches a terminal state. Fulfilled means the fill and the on-chain settlement both succeeded. Cancelled or expired means nothing was minted or burned, and the committed funds are returned: the payment for a buy, or the dShares for a sell.

The diagrams below trace this flow end to end for each side of the trade.

## Buying a dShare

```
sequenceDiagram
    autonumber
    participant U as End user
    participant P as Partner
    participant D as Dinari
    participant B as Dinari Securities
    participant C as Chain

    U->>P: Requests a buy<br/>(payment amount in stablecoin)
    P->>D: POST /accounts/{id}/order_requests/market_buy
    D-->>P: OrderRequest:<br/>order_request_id, status
    D->>D: Verifies KYC, account,<br/>and available funds

    D->>B: Routes order for execution
    B-->>D: Fill confirmation:<br/>filled_qty, filled_avg_price
    D->>C: Mints dShares<br/>to the user's wallet
    C-->>D: Fulfillment confirmed

    P->>D: GET /accounts/{id}/orders/{order_id}
    D-->>P: Order status: FULFILLED
    P->>U: Confirm dShares received
```

## Selling a dShare

```
sequenceDiagram
    autonumber
    participant U as End user
    participant P as Partner
    participant D as Dinari
    participant B as Dinari Securities
    participant C as Chain

    U->>P: Requests a sell<br/>(quantity of dShares)
    P->>D: POST /accounts/{id}/order_requests/market_sell
    D-->>P: OrderRequest:<br/>order_request_id, status
    D->>D: Verifies KYC, account,<br/>and dShare balance

    D->>B: Routes order for execution
    B-->>D: Fill confirmation:<br/>filled_qty, filled_avg_price
    D->>C: Burns dShares and releases<br/>stablecoin proceeds to the user's wallet
    C-->>D: Fulfillment confirmed

    P->>D: GET /accounts/{id}/orders/{order_id}
    D-->>P: Order status: FULFILLED
    P->>U: Credit proceeds and notify
```

> ℹ️
>
> If an order cannot be completed then no tokens are minted or burned. A buy returns the payment to the user, and a sell returns the dShares.

# Requirements for dShare Orders

Before an `Entity` can place a dShare order, make sure it fulfills the following pre-requisites:

* [Entity has a valid KYC](https://docs.dinari.com/v2.0/docs/managing-kyc)
* [Entity has a valid account](https://docs.dinari.com/v2.0/docs/managing-accounts)
* Entity has enough funds

# How Orders are Placed

The Dinari SDKs wrap the Dinari REST API, mapping each SDK function directly to an API endpoint. They handle authentication, request construction, and response parsing, while SDK parameters and return objects match the underlying endpoint's request body and response.

The [API Reference](https://docs.dinari.com/reference) is the source of truth for both integration styles. Use the endpoint reference pages below to see input fields, validation rules, and response schemas.

There are two ways to place an order:

* **Managed Orders** — for `Accounts` with a Dinari-managed wallet. Dinari handles custody and settlement.
* **Unmanaged Orders (self-custody)** — for `Accounts` using their own wallet. Orders are placed via smart contract interactions on an EVM chain, using a permit-based flow.

## Managed Orders

> ❗️
>
> ### This is only usable by Accounts with a Dinari-managed wallet.

Each managed order SDK function wraps one of the following API endpoints:

| Order type | SDK function (TS shown) | API endpoint |
| --- | --- | --- |
| Market Buy | `client.managedOrders.createMarketBuyManagedOrderRequest()` | [Create Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest) — `POST /api/v2/accounts/{account_id}/order_requests/market_buy` |
| Market Sell | `client.managedOrders.createMarketSellManagedOrderRequest()` | [Create Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest) — `POST /api/v2/accounts/{account_id}/order_requests/market_sell` |
| Limit Buy | `client.managedOrders.createLimitBuyManagedOrderRequest()` | [Create Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest) — `POST /api/v2/accounts/{account_id}/order_requests/limit_buy` |
| Limit Sell | `client.managedOrders.createLimitSellManagedOrderRequest()` | [Create Limit Sell Managed Order Request](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest) — `POST /api/v2/accounts/{account_id}/order_requests/limit_sell` |

### Parameters

The parameters below apply to both the API and the SDKs — they are the same. In the API, `account_id` is a path parameter and the rest are body fields; in the SDKs, `account_id` is passed together with the rest of the parameters (in Java, it is the first positional argument).

For the authoritative, per-endpoint list of input values and validation rules, see the corresponding API references: [Market Buy](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest), [Market Sell](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest), [Limit Buy](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest), [Limit Sell](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest).

### Response

All four endpoints — and therefore all four SDK functions — return the same object: an `OrderRequest`. The response is identical whether you call the API directly or through an SDK.

The full response schemas, including error responses (`422`, `423`), are documented on each endpoint's API reference page linked above.

### Example (SDK)

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

  const limitBuy = await client.managedOrders.createLimitBuyManagedOrderRequest({
    accountId,
    assetQuantity: 1,
    limitPrice: 1.5,
    stockId,
  });
  console.log("Limit Buy Response:", limitBuy);

  const limitSell = await client.managedOrders.createLimitSellManagedOrderRequest({
    accountId,
    assetQuantity: 1,
    limitPrice: 1.5,
    stockId,
  });
  console.log("Limit Sell Response:", limitSell);

  const marketBuy = await client.managedOrders.createMarketBuyManagedOrderRequest({
    accountId,
    stockId,
    paymentAmount: 150.0,
  });
  console.log("Market Buy Response:", marketBuy);

  const marketSell = await client.managedOrders.createMarketSellManagedOrderRequest({
    accountId,
    stockId,
    assetQuantity: 1,
  });
  console.log("Market Sell Response:", marketSell);
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

limit_buy = client.managed_orders.create_limit_buy_managed_order_request(
    account_id=account_id,
    asset_quantity=1,
    limit_price=1.5,
    stock_id=stock_id,
)

limit_sell = client.managed_orders.create_limit_sell_managed_order_request(
    account_id=account_id,
    asset_quantity=1,
    limit_price=1.5,
    stock_id=stock_id,
)

market_buy = client.managed_orders.create_market_buy_managed_order_request(
    account_id=account_id,
    stock_id=stock_id,
    payment_amount=150.0,
)

market_sell = client.managed_orders.create_market_sell_managed_order_request(
    account_id=account_id,
    stock_id=stock_id,
    asset_quantity=1,
)
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

	limitBuyResp, err := c.ManagedOrders.CreateLimitBuyManagedOrderRequest(context.Background(), &dinari.CreateLimitOrderBuyRequestInput{
		AccountID:     accountID,
		AssetQuantity: 1,
		LimitPrice:    1.5,
		StockID:       dinari.String(stockID),
	})
	if err != nil {
		log.Fatalf("Failed to create limit buy order: %v", err)
	}
	fmt.Printf("Limit Buy Response: %+v\n", limitBuyResp)

	limitSellResp, err := c.ManagedOrders.CreateLimitSellManagedOrderRequest(context.Background(), &dinari.CreateLimitOrderSellRequestInput{
		AccountID:     accountID,
		AssetQuantity: 1,
		LimitPrice:    1.5,
		StockID:       dinari.String(stockID),
	})
	if err != nil {
		log.Fatalf("Failed to create limit sell order: %v", err)
	}
	fmt.Printf("Limit Sell Response: %+v\n", limitSellResp)

	marketBuyResp, err := c.ManagedOrders.CreateMarketBuyManagedOrderRequest(context.Background(), &dinari.CreateMarketBuyOrderRequestInput{
		AccountID:     accountID,
		PaymentAmount: 150.0,
		StockID:       dinari.String(stockID),
	})
	if err != nil {
		log.Fatalf("Failed to create market buy order: %v", err)
	}
	fmt.Printf("Market Buy Response: %+v\n", marketBuyResp)

	marketSellResp, err := c.ManagedOrders.CreateMarketSellManagedOrderRequest(context.Background(), &dinari.CreateMarketSellOrderRequestInput{
		AccountID:     accountID,
		AssetQuantity: 1,
		StockID:       dinari.String(stockID),
	})
	if err != nil {
		log.Fatalf("Failed to create market sell order: %v", err)
	}
	fmt.Printf("Market Sell Response: %+v\n", marketSellResp)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.managedorders.requests.CreateLimitOrderBuyRequestInput;
import com.dinari.api.resources.managedorders.requests.CreateLimitOrderSellRequestInput;
import com.dinari.api.resources.managedorders.requests.CreateMarketBuyOrderRequestInput;
import com.dinari.api.resources.managedorders.requests.CreateMarketSellOrderRequestInput;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String stockId = "your-stock-id";

        var limitBuy = client.managedOrders().createLimitBuyManagedOrderRequest(
                accountId,
                CreateLimitOrderBuyRequestInput.builder().assetQuantity(1).limitPrice(1.5).stockId(stockId).build());
        System.out.println("Limit Buy Response: " + limitBuy);

        var limitSell = client.managedOrders().createLimitSellManagedOrderRequest(
                accountId,
                CreateLimitOrderSellRequestInput.builder().assetQuantity(1).limitPrice(1.5).stockId(stockId).build());
        System.out.println("Limit Sell Response: " + limitSell);

        var marketBuy = client.managedOrders().createMarketBuyManagedOrderRequest(
                accountId,
                CreateMarketBuyOrderRequestInput.builder().paymentAmount(150.0).stockId(stockId).build());
        System.out.println("Market Buy Response: " + marketBuy);

        var marketSell = client.managedOrders().createMarketSellManagedOrderRequest(
                accountId,
                CreateMarketSellOrderRequestInput.builder().assetQuantity(1).stockId(stockId).build());
        System.out.println("Market Sell Response: " + marketSell);
    }
}
```

## Unmanaged Orders

For `Accounts` using their own wallet, orders are placed on-chain via a permit-based flow on EVM (EIP-155) chains. As with managed orders, the SDK functions for this flow are wrappers around API endpoints — the parameters and responses are the same in both. The two endpoints involved are:

* [Create EIP-155 Order Request Permit Transaction](https://docs.dinari.com/reference/createeip155permittransaction) — given the `EIP155OrderRequest` ID and the signed permit, prepares a transaction to be placed on EVM. The returned structure contains the necessary data to create an `EIP155Transaction` object (used in the **User Sponsored** flow).
* [Submit EIP-155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction) — submits a transaction for an EIP-155 Order Request given the `EIP155OrderRequest` ID and permit signature; Dinari creates and submits the transaction on your behalf and returns the `EIP155OrderRequest` representing the proxied order (used in the **Dinari Sponsored** flow).

See each reference page for the exact input values and response schemas. Below the examples below on how to places these orders using the Dinari SDK.

## EVM

### User Sponsored Orders

You create and send the transaction yourself, keeping full control of the blockchain interaction:

1. **Create permit** — call the API to generate a permit for the order.
2. **Sign permit** — use your wallet's private key to sign the permit message.
3. **Create permit transaction** — submit the signed permit to receive transaction details.
4. **Sign and send transaction** — sign the resulting transaction and broadcast it to the blockchain.

TypeScriptPythonGoJava

```
import { createWalletClient, http } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { arbitrumSepolia } from "viem/chains";
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const accountId = "your-account-id";
  const stockId = "your-stock-id";

  // Step 1. Create the permit
  const permitResponse = await client.orderRequests.createEip155OrderRequestPermit({
    accountId,
    chainId: "eip155:421614", // Arbitrum Sepolia
    orderSide: "BUY",
    orderTif: "DAY",
    orderType: "MARKET",
    stockId,
    paymentToken: process.env.PAYMENT_TOKEN!, // Replace with your payment token address
    paymentTokenQuantity: 1.5,
  });

  // Step 2. Sign the permit (EIP-712 typed data) with your wallet; viem is shown here
  const account = privateKeyToAccount(`0x${process.env.PRIVATE_KEY}`);
  const walletClient = createWalletClient({
    account,
    chain: arbitrumSepolia,
    transport: http("https://sepolia-rollup.arbitrum.io/rpc"),
  });

  const permit = permitResponse.permit as any;
  const permitSignature = await walletClient.signTypedData({
    account,
    domain: permit.domain,
    types: permit.types,
    primaryType: permit.primaryType,
    message: permit.message,
  });

  // Step 3. Create the permit transaction
  const transaction = await client.orderRequests.createEip155PermitTransaction({
    accountId,
    body: {
      orderRequestId: permitResponse.orderRequestId,
      permitSignature,
    },
  });

  // Step 4. Sign and send the transaction
  const txHash = await walletClient.sendTransaction({
    account,
    to: transaction.contractAddress as `0x${string}`,
    data: transaction.data as `0x${string}`,
    value: BigInt(transaction.value),
  });
  console.log("Transaction hash:", txHash);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment
from eth_account import Account
from eth_account.messages import encode_typed_data
from web3 import HTTPProvider, Web3
from web3.types import HexStr, Wei

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

account_id = "your-account-id"
stock_id = "your-stock-id"

# Step 1. Create the permit
resp = client.order_requests.create_eip155order_request_permit(
    account_id=account_id,
    chain_id="eip155:421614",  # Arbitrum Sepolia
    order_side="BUY",
    order_tif="DAY",
    order_type="MARKET",
    payment_token="0xC6E13d97d73721ecA623F6d6c77ceBAFD2fF6431",  # Replace with your payment token address
    payment_token_quantity=1.5,
    stock_id=stock_id,
)

# Step 2. Sign the permit
private_key = "your-wallet-private-key"
acct = Account.from_key(private_key)
message = encode_typed_data(full_message=resp.permit)
signature = acct.sign_message(message).signature
permit_signature = "0x" + signature.hex()

# Step 3. Create the permit transaction
tx_resp = client.order_requests.create_eip155permit_transaction(
    account_id=account_id,
    order_request_id=resp.order_request_id,
    permit_signature=permit_signature,
)

# Step 4. Sign and send the transaction
w3 = Web3(HTTPProvider("https://sepolia-rollup.arbitrum.io/rpc"))

tx = {
    "to": tx_resp.contract_address,
    "data": tx_resp.data,
    "value": int(tx_resp.value),
    "gas": w3.eth.estimate_gas(
        {
            "from": acct.address,
            "to": tx_resp.contract_address,
            "data": HexStr(tx_resp.data),
            "value": Wei(int(tx_resp.value)),
        }
    ),
    "gasPrice": w3.eth.gas_price,
    "nonce": w3.eth.get_transaction_count(acct.address),
    "chainId": 421614,  # Arbitrum Sepolia
}

signed = acct.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
print("Transaction hash:", tx_hash.hex())
```

```
package main

import (
	"context"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"os"

	"github.com/chenzhijie/go-web3"
	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
	"github.com/ethereum/go-ethereum/signer/core/apitypes"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx := context.Background()

	accountID := "your-account-id"
	stockID := "your-stock-id"

	// Step 1. Create the permit
	permitResp, err := c.OrderRequests.CreateEip155OrderRequestPermit(ctx, &dinari.Eip155OrderRequestPermitInput{
		AccountID:            accountID,
		ChainID:              dinari.ChainIDEip155421614,
		OrderSide:            dinari.OrderSideBuy,
		OrderTif:             dinari.OrderTifDay,
		OrderType:            dinari.OrderTypeMarket,
		StockID:              dinari.String(stockID),
		PaymentToken:         "0x6a34FDFE60D1758dF5b577d413E37397D21c3E78", // Replace with your payment token address
		PaymentTokenQuantity: dinari.Float64(1.5),
	})
	if err != nil {
		log.Fatalf("Failed to create permit: %v", err)
	}

	// Step 2. Sign the permit
	w3, err := web3.NewWeb3("https://sepolia-rollup.arbitrum.io/rpc")
	if err != nil {
		log.Fatalf("Failed to connect to the RPC provider: %v", err)
	}
	w3.Eth.SetChainId(421614)
	if err := w3.Eth.SetAccount("your-wallet-private-key"); err != nil {
		log.Fatalf("Failed to set account: %v", err)
	}

	permitSignature, err := signPermit(w3, permitResp.Permit)
	if err != nil {
		log.Fatalf("Failed to sign permit: %v", err)
	}

	// Step 3. Create the permit transaction
	transaction, err := c.OrderRequests.CreateEip155PermitTransaction(ctx, &dinari.CreateEip155PermitTransactionRequest{
		AccountID: accountID,
		Body: &dinari.Eip155OrderRequestPermitTransaction{
			OrderRequestID:  permitResp.OrderRequestID,
			PermitSignature: permitSignature,
		},
	})
	if err != nil {
		log.Fatalf("Failed to create permit transaction: %v", err)
	}
	fmt.Printf("Transaction: %+v\n", transaction)

	// Step 4. Sign and send the transaction with your wallet library
}

// signPermit signs the EIP-712 typed data returned by Dinari with the wallet's private key.
func signPermit(w3 *web3.Web3, permit map[string]any) (string, error) {
	var types apitypes.Types
	var domain apitypes.TypedDataDomain
	var message apitypes.TypedDataMessage

	for key, target := range map[string]any{"types": &types, "domain": &domain, "message": &message} {
		raw, err := json.Marshal(permit[key])
		if err != nil {
			return "", fmt.Errorf("failed to marshal %s: %w", key, err)
		}
		if err := json.Unmarshal(raw, target); err != nil {
			return "", fmt.Errorf("failed to unmarshal %s: %w", key, err)
		}
	}

	signed, err := w3.Eth.SignTypedData(apitypes.TypedData{
		Types:       types,
		PrimaryType: permit["primaryType"].(string),
		Domain:      domain,
		Message:     message,
	})
	if err != nil {
		return "", err
	}
	return "0x" + hex.EncodeToString(signed), nil
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.orderrequests.requests.CreateEip155OrderRequestPermitTransactionRequest;
import com.dinari.api.resources.orderrequests.requests.CreateEip155PermitTransactionRequest;
import com.dinari.api.resources.orderrequests.requests.Eip155OrderRequestPermitInput;
import com.dinari.api.types.ChainId;
import com.dinari.api.types.Eip155OrderRequestPermitTransaction;
import com.dinari.api.types.OrderSide;
import com.dinari.api.types.OrderTif;
import com.dinari.api.types.OrderType;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String stockId = "your-stock-id";

        // Step 1. Create the permit
        var permitResp = client.orderRequests().createEip155OrderRequestPermit(
                accountId,
                Eip155OrderRequestPermitInput.builder()
                        .chainId(ChainId.EIP155421614) // Arbitrum Sepolia
                        .orderTif(OrderTif.DAY)
                        .orderSide(OrderSide.BUY)
                        .orderType(OrderType.MARKET)
                        .paymentToken("0x6a34FDFE60D1758dF5b577d413E37397D21c3E78") // Replace with your payment token address
                        .stockId(stockId)
                        .paymentTokenQuantity(1.5)
                        .build());

        // Step 2. Sign the permit (EIP-712 typed data) with your wallet library
        String permitSignature = signPermit(permitResp.getPermit());

        // Step 3. Create the permit transaction
        var transaction = client.orderRequests().createEip155PermitTransaction(
                accountId,
                CreateEip155PermitTransactionRequest.builder()
                        .body(Eip155OrderRequestPermitTransaction.builder()
                                .orderRequestId(permitResp.getOrderRequestId())
                                .permitSignature(permitSignature)
                                .build())
                        .build());
        System.out.println(transaction);

        // Step 4. Sign and send the transaction with your wallet library
    }

    // Replace with your wallet library of choice (for example web3j) to sign the typed data
    // and return the hex-encoded signature.
    private static String signPermit(Map<String, Object> permit) {
        throw new UnsupportedOperationException("Sign the permit with your wallet library");
    }
}
```

### Dinari Sponsored

After signing the permit, you submit the signature to Dinari, which creates and submits the transaction on your behalf:

1. **Create permit** - generate an order permit via the API.
2. **Sign the permit** - sign the permit using your wallet credentials.
3. **Submit order through Dinari** - send the signed permit to Dinari for processing rather than manually constructing a transaction.

TypeScriptPythonGoJava

```
import { createWalletClient, http } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { arbitrumSepolia } from "viem/chains";
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const accountId = "your-account-id";
  const stockId = "your-stock-id";

  // Step 1. Create the permit
  const permitResponse = await client.orderRequests.createEip155OrderRequestPermit({
    accountId,
    chainId: "eip155:421614", // Arbitrum Sepolia
    orderSide: "BUY",
    orderTif: "DAY",
    orderType: "MARKET",
    stockId,
    paymentToken: process.env.PAYMENT_TOKEN!, // Replace with your payment token address
    paymentTokenQuantity: 1.5,
  });

  // Step 2. Sign the permit (EIP-712 typed data) with your wallet; viem is shown here
  const account = privateKeyToAccount(`0x${process.env.PRIVATE_KEY}`);
  const walletClient = createWalletClient({
    account,
    chain: arbitrumSepolia,
    transport: http("https://sepolia-rollup.arbitrum.io/rpc"),
  });

  const permit = permitResponse.permit as any;
  const permitSignature = await walletClient.signTypedData({
    account,
    domain: permit.domain,
    types: permit.types,
    primaryType: permit.primaryType,
    message: permit.message,
  });

  // Step 3. Submit the order through Dinari
  const orderRequest = await client.orderRequests.createEip155OrderRequestPermitTransaction({
    accountId,
    body: {
      orderRequestId: permitResponse.orderRequestId,
      permitSignature,
    },
  });
  console.log(orderRequest);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment
from eth_account import Account
from eth_account.messages import encode_typed_data

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

account_id = "your-account-id"
stock_id = "your-stock-id"

# Step 1. Create the permit
resp = client.order_requests.create_eip155order_request_permit(
    account_id=account_id,
    chain_id="eip155:421614",  # Arbitrum Sepolia
    order_side="BUY",
    order_tif="DAY",
    order_type="MARKET",
    payment_token="0xC6E13d97d73721ecA623F6d6c77ceBAFD2fF6431",  # Replace with your payment token address
    payment_token_quantity=1.5,
    stock_id=stock_id,
)

# Step 2. Sign the permit
private_key = "your-wallet-private-key"
acct = Account.from_key(private_key)
message = encode_typed_data(full_message=resp.permit)
signature = acct.sign_message(message).signature
permit_signature = "0x" + signature.hex()

# Step 3. Submit the order through Dinari
order_request = client.order_requests.create_eip155order_request_permit_transaction(
    account_id=account_id,
    order_request_id=resp.order_request_id,
    permit_signature=permit_signature,
)
print(order_request)
```

```
package main

import (
	"context"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"os"

	"github.com/chenzhijie/go-web3"
	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
	"github.com/ethereum/go-ethereum/signer/core/apitypes"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx := context.Background()

	accountID := "your-account-id"
	stockID := "your-stock-id"

	// Step 1. Create the permit
	permitResp, err := c.OrderRequests.CreateEip155OrderRequestPermit(ctx, &dinari.Eip155OrderRequestPermitInput{
		AccountID:            accountID,
		ChainID:              dinari.ChainIDEip155421614,
		OrderSide:            dinari.OrderSideBuy,
		OrderTif:             dinari.OrderTifDay,
		OrderType:            dinari.OrderTypeMarket,
		StockID:              dinari.String(stockID),
		PaymentToken:         "0x6a34FDFE60D1758dF5b577d413E37397D21c3E78", // Replace with your payment token address
		PaymentTokenQuantity: dinari.Float64(1.5),
	})
	if err != nil {
		log.Fatalf("Failed to create permit: %v", err)
	}

	// Step 2. Sign the permit
	w3, err := web3.NewWeb3("https://sepolia-rollup.arbitrum.io/rpc")
	if err != nil {
		log.Fatalf("Failed to connect to the RPC provider: %v", err)
	}
	w3.Eth.SetChainId(421614)
	if err := w3.Eth.SetAccount("your-wallet-private-key"); err != nil {
		log.Fatalf("Failed to set account: %v", err)
	}

	permitSignature, err := signPermit(w3, permitResp.Permit)
	if err != nil {
		log.Fatalf("Failed to sign permit: %v", err)
	}

	// Step 3. Submit the order through Dinari
	orderRequest, err := c.OrderRequests.CreateEip155OrderRequestPermitTransaction(ctx, &dinari.CreateEip155OrderRequestPermitTransactionRequest{
		AccountID: accountID,
		Body: &dinari.Eip155OrderRequestPermitTransaction{
			OrderRequestID:  permitResp.OrderRequestID,
			PermitSignature: permitSignature,
		},
	})
	if err != nil {
		log.Fatalf("Failed to submit order request: %v", err)
	}
	fmt.Printf("Order request: %+v\n", orderRequest)
}

// signPermit signs the EIP-712 typed data returned by Dinari with the wallet's private key.
func signPermit(w3 *web3.Web3, permit map[string]any) (string, error) {
	var types apitypes.Types
	var domain apitypes.TypedDataDomain
	var message apitypes.TypedDataMessage

	for key, target := range map[string]any{"types": &types, "domain": &domain, "message": &message} {
		raw, err := json.Marshal(permit[key])
		if err != nil {
			return "", fmt.Errorf("failed to marshal %s: %w", key, err)
		}
		if err := json.Unmarshal(raw, target); err != nil {
			return "", fmt.Errorf("failed to unmarshal %s: %w", key, err)
		}
	}

	signed, err := w3.Eth.SignTypedData(apitypes.TypedData{
		Types:       types,
		PrimaryType: permit["primaryType"].(string),
		Domain:      domain,
		Message:     message,
	})
	if err != nil {
		return "", err
	}
	return "0x" + hex.EncodeToString(signed), nil
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.orderrequests.requests.CreateEip155OrderRequestPermitTransactionRequest;
import com.dinari.api.resources.orderrequests.requests.CreateEip155PermitTransactionRequest;
import com.dinari.api.resources.orderrequests.requests.Eip155OrderRequestPermitInput;
import com.dinari.api.types.ChainId;
import com.dinari.api.types.Eip155OrderRequestPermitTransaction;
import com.dinari.api.types.OrderSide;
import com.dinari.api.types.OrderTif;
import com.dinari.api.types.OrderType;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String stockId = "your-stock-id";

        // Step 1. Create the permit
        var permitResp = client.orderRequests().createEip155OrderRequestPermit(
                accountId,
                Eip155OrderRequestPermitInput.builder()
                        .chainId(ChainId.EIP155421614) // Arbitrum Sepolia
                        .orderTif(OrderTif.DAY)
                        .orderSide(OrderSide.BUY)
                        .orderType(OrderType.MARKET)
                        .paymentToken("0x6a34FDFE60D1758dF5b577d413E37397D21c3E78") // Replace with your payment token address
                        .stockId(stockId)
                        .paymentTokenQuantity(1.5)
                        .build());

        // Step 2. Sign the permit (EIP-712 typed data) with your wallet library
        String permitSignature = signPermit(permitResp.getPermit());

        // Step 3. Submit the order through Dinari
        var orderRequest = client.orderRequests().createEip155OrderRequestPermitTransaction(
                accountId,
                CreateEip155OrderRequestPermitTransactionRequest.builder()
                        .body(Eip155OrderRequestPermitTransaction.builder()
                                .orderRequestId(permitResp.getOrderRequestId())
                                .permitSignature(permitSignature)
                                .build())
                        .build());
        System.out.println(orderRequest);
    }

    // Replace with your wallet library of choice (for example web3j) to sign the typed data
    // and return the hex-encoded signature.
    private static String signPermit(Map<String, Object> permit) {
        throw new UnsupportedOperationException("Sign the permit with your wallet library");
    }
}
```

Updated 6 days ago

---

[Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)[Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)

Did this page help you?

Yes

No

Copy Page

* + [Order Lifecycle](https://docs.dinari.com/docs/placing-orders)
  + - [Buying a dShare](https://docs.dinari.com/docs/placing-orders)
    - [Selling a dShare](https://docs.dinari.com/docs/placing-orders)
  + [Requirements for dShare Orders](https://docs.dinari.com/docs/placing-orders)
  + [How Orders are Placed](https://docs.dinari.com/docs/placing-orders)
  + - [Managed Orders](https://docs.dinari.com/docs/placing-orders)
    - * [Parameters](https://docs.dinari.com/docs/placing-orders)
      * [Response](https://docs.dinari.com/docs/placing-orders)
      * [Example (SDK)](https://docs.dinari.com/docs/placing-orders)
    - [Unmanaged Orders](https://docs.dinari.com/docs/placing-orders)
    - [EVM](https://docs.dinari.com/docs/placing-orders)
    - * [User Sponsored Orders](https://docs.dinari.com/docs/placing-orders)
      * [Dinari Sponsored](https://docs.dinari.com/docs/placing-orders)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Placing Orders","dateModified":"2026-11-10T01:00:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy>>>
---
url: https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy
title: Placing dShare Orders with Alchemy
description: This page details how orders can be placed using the Alchemy Account kit & Dinari SDK
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

# Placing dShare Orders with Alchemy

This page details how orders can be placed using the Alchemy Account kit & Dinari SDK

# Ordering with Alchemy Account Kit Smart Wallet

This guide shows how to place a dShare order using the Dinari Partner SDK (`@dinari/api-sdk`) where an **Alchemy Account Kit smart contract wallet** signs the order intent.

## How it works

When the funder is an Account Kit smart wallet, you must use the externally-signed path. The flow is:

1. Create an order request and get back the EIP-712 permit to sign.
2. Sign the permit with the smart wallet (produces an **ERC-1271** contract-account signature).
3. Submit the signed permit — Dinari-sponsored or self-sponsored.
4. Poll the order request until it reaches a terminal state.

> 🚧
>
> ### NOTE: Smart-wallet signatures are not EOA signatures
>
> A standard ERC-2612 `permit()` recovers the signer with `ecrecover`, which only accepts EOA signatures and will reject a smart-contract wallet. A contract-wallet (ERC-1271) signature is only honored if the verifying contract supports ERC-1271 as Uniswap **Permit2** does. Confirm your payment path validates ERC-1271/Permit2 (not raw ERC-2612) before going to mainnet.

### Prerequisites

To place an order, an Entity needs:

* A valid **KYC** on the Entity.
* A valid **Account** under the Entity.
* Enough **payment-token balance** in the smart wallet to cover the order plus fees.

For this integration you also need:

* Create a **Dinari partner account** and generate an API Key ID and API Secret Key in `partners.dinari.com`. Start in **sandbox**.
* Create an **Alchemy API key** in `dashboard.alchemy.com`, and optionally create a **Gas Manager policy ID** for gas sponsorship.
* Store the smart wallet's **owner private key** in a server-side secret store. This is the signer/owner of the account — not the account address.
* Load secrets from your secret manager at runtime, but do not paste secret values into examples, logs, or client-side code.

### Step 1: Initialize the Dinari client

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const dinariCredentials = await loadDinariCredentialsFromSecretManager();

const dinari = new DinariClient({
  apiKeyId: dinariCredentials.apiKeyID,
  apiSecretKey: dinariCredentials.apiSecretKey,
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)
```

```
package main

import (
	"context"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

var (
	c = client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx = context.Background()
)
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    static final DinariClient client = DinariClient.builder()
            .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
            .apiKeyId(System.getenv("DINARI_API_KEY_ID"))
            .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY"))
            .build();
}
```

> The smart wallet interactions in this guide use Alchemy Account Kit (TypeScript). The Python, Go and Java tabs show the Dinari API calls that stand on their own (client setup, stock lookup, permit creation, Dinari-sponsored submission and order status), with the same variable names.

### Step 2: Create the headless smart wallet client

This is the server-side signer client (not the React hooks path). The smart account is a **Modular Account V2** whose owner is a `LocalAccountSigner` built from a private key.

TypeScript

```
import { createModularAccountV2Client } from "@account-kit/smart-contracts";
import { LocalAccountSigner } from "@aa-sdk/core";
import { alchemy, arbitrumSepolia } from "@account-kit/infra";

const walletSecrets = await loadWalletSecretsFromSecretManager();
const alchemyConfig = await loadAlchemyConfigFromSecretManager();

const owner = LocalAccountSigner.privateKeyToAccountSigner(
  walletSecrets.ownerPrivateKey as `0x${string}`,
);

const smartAccountClient = await createModularAccountV2Client({
  mode: "default",
  chain: arbitrumSepolia,
  transport: alchemy({ apiKey: alchemyConfig.apiKey }),
  signer: owner,
});

// The smart contract account address (not the owner EOA):
const smartWalletAddress = smartAccountClient.account.address;
```

`signTypedData` on this client produces a signature validatable via **ERC-1271**. If the account is not yet deployed, the signature is wrapped per ERC-6492.

### Step 3: Deploy the smart account

A Modular Account V2 deploys on its first user operation. On-chain ERC-1271 validation requires the account to be deployed (unless the verifier supports ERC-6492), so deploy it before signing permits.

TypeScript

```
const isDeployed = await smartAccountClient.account.isAccountDeployed();

if (!isDeployed) {
  const deployOp = await smartAccountClient.sendUserOperation({
    uo: { target: smartAccountClient.account.address, data: "0x", value: 0n },
  });
  await smartAccountClient.waitForUserOperationTransaction({ hash: deployOp.hash });
}
```

> 🚧
>
> ### Deployment needs gas
>
> The deploy user operation costs gas. Fund the account with native gas or attach an Alchemy Gas Manager policy to the client.

### Step 4: Complete KYC and link your wallet (one-time)

These steps run once per user. KYC requires the user to complete a hosted flow, so it cannot be fully automated server-side.

TypeScript

```
// Entity + KYC
const entity = await dinari.entities.createEntities({ name: "Jane Doe" });
const kyc = await dinari.kyc.createManagedEntityKycEmbed({ entityId: entity.id });
console.log("Send the user to:", kyc.embedUrl);

// Account
const account = await dinari.accounts.createEntityAccounts({ entityId: entity.id });
const accountId = account.id;

// Link the smart wallet (signed with the wallet, ERC-1271)
const nonceResp = await dinari.wallets.getAccountWalletConnectionNonce({
  accountId,
  walletAddress: smartWalletAddress,
  chainId: "eip155:421614",
});

const linkSignature = await smartAccountClient.signMessage({
  message: nonceResp.message,
});

await dinari.wallets.createAccountWalletConnection({
  accountId,
  chainId: "eip155:421614",
  nonce: nonceResp.nonce,
  signature: linkSignature,
  walletAddress: smartWalletAddress,
});
```

> 📘
>
> ### Linking also uses an ERC-1271 signature
>
> The wallet-linking nonce is signed by the smart wallet, so the account must be deployed (Step 3) for the signature to validate.

### Step 5: Select the stock and order parameters

TypeScriptPythonGoJava

```
const stocks = await dinari.marketData.getStocks({ symbols: "AAPL", limit: 20 });
const stock = (Array.isArray(stocks) ? stocks : stocks.data).find((s) => s.symbol === "AAPL");
if (!stock) throw new Error("Stock not found");
const stockId = stock.id;
```

```
stocks = client.market_data.get_stocks(symbols="AAPL", limit=20)
stock = next((s for s in (stocks if isinstance(stocks, list) else stocks.data) if s.symbol == "AAPL"), None)
if stock is None:
    raise RuntimeError("Stock not found")
stock_id = stock.id
```

```
stocks, err := c.MarketData.GetStocks(ctx, &dinari.GetStocksRequest{
	Symbols: []*string{dinari.String("AAPL")},
	Limit:   dinari.Int(20),
})
if err != nil {
	log.Fatalf("Failed to list stocks: %v", err)
}

var stockID string
for _, s := range stocks.GetPaginatedStockResponse().Data {
	if s.Symbol == "AAPL" {
		stockID = s.ID
	}
}
if stockID == "" {
	log.Fatal("Stock not found")
}
```

```
var stocks = client.marketData().getStocks(
        GetStocksRequest.builder().symbols("AAPL").limit(20).build());
String stockId = ((PaginatedStockResponse) stocks.get()).getData().stream()
        .filter(s -> s.getSymbol().equals("AAPL"))
        .findFirst()
        .orElseThrow(() -> new RuntimeException("Stock not found"))
        .getId();
```

| Field | Meaning |
| --- | --- |
| `stock_id` | Dinari UUID of the dShare (from `marketData.getStocks()`). |
| `order_side` | `"BUY"` or `"SELL"`. |
| `order_type` | `"MARKET"` or `"LIMIT"`. |
| `order_tif` | Time-in-force, e.g. `"DAY"`. |
| `payment_token` | Payment-token ERC-20 address (e.g. USDC on the target chain). |
| `payment_token_quantity` | For a market **buy**, the notional amount of payment token to spend. |
| `chain_id` | CAIP-2 chain id, e.g. `"eip155:421614"`. |

> 📘
>
> ### Amount fields by order type
>
> Market **buys** use `payment_token_quantity` (notional). Market **sells** and **limit** orders use `asset_quantity` (number of dShares); limit orders also take `limit_price`. Fees are added on top of the notional.

### Step 6: Create the order permit

TypeScriptPythonGoJava

```
const orderConfig = await loadOrderConfig();

const permitResponse = await dinari.orderRequests.createEip155OrderRequestPermit({
  accountId,
  chainId: "eip155:421614",
  orderSide: "BUY",
  orderType: "MARKET",
  orderTif: "DAY",
  stockId,
  paymentToken: orderConfig.paymentTokenAddress,
  paymentTokenQuantity: 10.0, // notional to spend
});

const orderRequestId = permitResponse.orderRequestId;
const permit = permitResponse.permit; // { domain, types, primaryType, message }
```

```
permit_response = client.order_requests.create_eip155order_request_permit(
    account_id=account_id,
    chain_id="eip155:421614",
    order_side="BUY",
    order_type="MARKET",
    order_tif="DAY",
    stock_id=stock_id,
    payment_token=payment_token_address,
    payment_token_quantity=10.0,  # notional to spend
)

order_request_id = permit_response.order_request_id
permit = permit_response.permit  # { domain, types, primaryType, message }
```

```
permitResponse, err := c.OrderRequests.CreateEip155OrderRequestPermit(ctx, &dinari.Eip155OrderRequestPermitInput{
	AccountID:            accountID,
	ChainID:              dinari.ChainIDEip155421614,
	OrderSide:            dinari.OrderSideBuy,
	OrderType:            dinari.OrderTypeMarket,
	OrderTif:             dinari.OrderTifDay,
	StockID:              dinari.String(stockID),
	PaymentToken:         paymentTokenAddress,
	PaymentTokenQuantity: dinari.Float64(10.0), // notional to spend
})
if err != nil {
	log.Fatalf("Failed to create permit: %v", err)
}

orderRequestID := permitResponse.OrderRequestID
permit := permitResponse.Permit // { domain, types, primaryType, message }
```

```
var permitResponse = client.orderRequests().createEip155OrderRequestPermit(
        accountId,
        Eip155OrderRequestPermitInput.builder()
                .chainId(ChainId.EIP155421614)
                .orderTif(OrderTif.DAY)
                .orderSide(OrderSide.BUY)
                .orderType(OrderType.MARKET)
                .paymentToken(paymentTokenAddress)
                .stockId(stockId)
                .paymentTokenQuantity(10.0) // notional to spend
                .build());

String orderRequestId = permitResponse.getOrderRequestId();
Map<String, Object> permit = permitResponse.getPermit(); // { domain, types, primaryType, message }
```

The response carries an `order_request_id` and a `permit` object shaped exactly like an EIP-712 `TypedDataDefinition`.

### Step 7: Sign the permit with the smart wallet

TypeScript

```
const permitSignature = await smartAccountClient.signTypedData({
  typedData: {
    domain: permit.domain,
    types: permit.types,
    primaryType: permit.primaryType,
    message: permit.message,
  },
});
```

### Step 8: Submit the signed order

Choose one of two submission modes.

**Dinari-sponsored** — Dinari pays gas and submits on-chain:

TypeScriptPythonGoJava

```
const result = await dinari.orderRequests.createEip155OrderRequestPermitTransaction({
  accountId,
  body: { orderRequestId, permitSignature },
});
```

```
permit_signature = "your-permit-signature"  # The signature from Step 7

result = client.order_requests.create_eip155order_request_permit_transaction(
    account_id=account_id,
    order_request_id=order_request_id,
    permit_signature=permit_signature,
)
```

```
permitSignature := "your-permit-signature" // The signature from Step 7

result, err := c.OrderRequests.CreateEip155OrderRequestPermitTransaction(ctx, &dinari.CreateEip155OrderRequestPermitTransactionRequest{
	AccountID: accountID,
	Body: &dinari.Eip155OrderRequestPermitTransaction{
		OrderRequestID:  orderRequestID,
		PermitSignature: permitSignature,
	},
})
if err != nil {
	log.Fatalf("Failed to submit order request: %v", err)
}
fmt.Printf("%+v\n", result)
```

```
String permitSignature = "your-permit-signature"; // The signature from Step 7

var result = client.orderRequests().createEip155OrderRequestPermitTransaction(
        accountId,
        CreateEip155OrderRequestPermitTransactionRequest.builder()
                .body(Eip155OrderRequestPermitTransaction.builder()
                        .orderRequestId(orderRequestId)
                        .permitSignature(permitSignature)
                        .build())
                .build());
System.out.println(result);
```

**Self-sponsored** — you send the transaction from the smart wallet:

TypeScript

```
const tx = await dinari.orderRequests.createEip155PermitTransaction({
  accountId,
  body: { orderRequestId, permitSignature },
});

const op = await smartAccountClient.sendUserOperation({
  uo: {
    target: tx.contractAddress as `0x${string}`,
    data: tx.data as `0x${string}`,
    value: BigInt(tx.value ?? 0),
  },
});

const txHash = await smartAccountClient.waitForUserOperationTransaction({
  hash: op.hash,
});
```

### Step 9: Poll order status

TypeScriptPythonGoJava

```
const orderRequest = await dinari.orderRequests.getOrderRequestById({
  accountId,
  orderRequestId,
});
console.log("Status:", orderRequest.status);
```

```
order_request = client.order_requests.get_order_request_by_id(
    account_id=account_id,
    order_request_id=order_request_id,
)
print("Status:", order_request.status)
```

```
orderRequest, err := c.OrderRequests.GetOrderRequestByID(ctx, &dinari.GetOrderRequestByIDRequest{
	AccountID:      accountID,
	OrderRequestID: orderRequestID,
})
if err != nil {
	log.Fatalf("Failed to get order request: %v", err)
}
fmt.Println("Status:", orderRequest.Status)
```

```
var orderRequest = client.orderRequests().getOrderRequestById(accountId, orderRequestId);
System.out.println("Status: " + orderRequest.getStatus());
```

Two status concepts exist:

* `OrderRequestStatus` — the request status (pre-brokerage), on the `OrderRequest`.
* `BrokerageOrderStatus` — the resulting on-chain/brokerage `Order`, via `dinari.orders.getOrderById({ accountId, orderId })`.

Poll the order request to a terminal state, then track the resulting order and fulfillments.

## Common errors

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Permit signature rejected on submit | Payment path uses raw ERC-2612 (`ecrecover`), which rejects contract-wallet signatures | Confirm Dinari's verifier supports ERC-1271 / Permit2 for your token and chain |
| `isValidSignature` reverts | Smart account not deployed | Deploy the account first (Step 3) |
| Wallet-linking fails | Account not deployed when linking signature was produced | Deploy, then link |
| Insufficient funds | Payment-token balance below notional + fees | Fund the smart wallet; budget for fees on top of the notional |
| User operation fails in self-sponsored mode | No native gas and no paymaster | Fund the wallet or attach a Gas Manager policy |

Updated 6 days ago

---

[Placing Orders](https://docs.dinari.com/docs/placing-orders)[Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)

Did this page help you?

Yes

No

Copy Page

* + [Ordering with Alchemy Account Kit Smart Wallet](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
  + - [How it works](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - * [Prerequisites](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 1: Initialize the Dinari client](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 2: Create the headless smart wallet client](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 3: Deploy the smart account](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 4: Complete KYC and link your wallet (one-time)](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 5: Select the stock and order parameters](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 6: Create the order permit](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 7: Sign the permit with the smart wallet](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 8: Submit the signed order](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
      * [Step 9: Poll order status](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Common errors](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Placing dShare Orders with Alchemy","dateModified":"2026-11-10T01:00:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults>>>
---
url: https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults
title: Placing dShare Orders with Safe Vaults
description: This guide shows how to place a dShare order where a safe vault funds the order, signs the permit, and submits the transaction.
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

# Placing dShare Orders with Safe Vaults

This guide shows how to place a dShare order where a safe vault funds the order, signs the permit, and submits the transaction.

## How it works

1. Approve Permit2 from the Safe (once per payment token, per chain).
2. Create an order request with `createPermit` and receive the EIP-712 permit.
3. Sign the permit with the Safe (**ERC-1271** signature).
4. Build the transaction with `createPermitTransaction`.
5. Execute the transaction from the Safe.
6. Poll the order request until it reaches a terminal state.

> 🚧
>
> ### Permit2 approval is required
>
> Dinari issues an ERC-2612 permit to any wallet without a Permit2 allowance, and a Safe cannot sign ERC-2612. See [Step 3](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults).

```
sequenceDiagram
    autonumber
    participant S as Safe
    participant P as Partner
    participant D as Dinari
    participant C as Chain

    S->>C: approve(Permit2) on payment token (one-time)
    P->>D: createPermit
    D-->>P: order_request_id, permit
    P->>S: Sign permit (owners)
    S-->>P: ERC-1271 signature
    P->>D: createPermitTransaction
    D-->>P: contract_address, data, value
    P->>S: execTransaction
    S->>C: Submit order
    P->>D: orderRequests.retrieve
    D-->>P: Status
```

## Prerequisites

To place an order, an Entity needs:

* A valid **KYC** on the Entity.
* A valid **Account** under the Entity.
* Enough **payment-token balance** in the Safe to cover the order plus fees.

For this integration you also need:

* #### A **Dinari API Key ID and API Secret Key** from `partners.dinari.com`. Start in **sandbox**.
* A **deployed Safe** (v1.3.0+) using the default `CompatibilityFallbackHandler`.
* Private keys for at least `threshold` Safe owners, stored server-side.
* Native gas in the owner EOA that executes Safe transactions.

### Step 1: Initialize the clients

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";
import Safe from "@safe-global/protocol-kit";

const dinariCredentials = await loadDinariCredentialsFromSecretManager();
const walletSecrets = await loadWalletSecretsFromSecretManager();
const config = await loadChainConfig();

const dinari = new DinariClient({
  apiKeyId: dinariCredentials.apiKeyID,
  apiSecretKey: dinariCredentials.apiSecretKey,
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

const safe = await Safe.init({
  provider: config.rpcUrl,
  signer: walletSecrets.ownerPrivateKey, // a Safe owner
  safeAddress: config.safeAddress,
});

if (!(await safe.isSafeDeployed())) {
  throw new Error("Deploy the Safe before signing permits");
}

const safeAddress = await safe.getAddress();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)
```

```
package main

import (
	"context"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

var (
	c = client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx = context.Background()
)
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    static final DinariClient client = DinariClient.builder()
            .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
            .apiKeyId(System.getenv("DINARI_API_KEY_ID"))
            .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY"))
            .build();
}
```

> The Safe interactions in this guide use the Safe TypeScript SDK. The Python, Go and Java tabs show the Dinari API calls that stand on their own (client setup, stock lookup, permit creation and order status), with the same variable names.

### Step 2: Complete KYC and link the Safe (one-time)

KYC requires the user to complete a hosted flow, so it cannot be fully automated server-side.

TypeScript

```
const entity = await dinari.entities.createEntities({ name: "Jane Doe" });
const kyc = await dinari.kyc.createManagedEntityKycEmbed({ entityId: entity.id });
console.log("Send the user to:", kyc.embedUrl);

const account = await dinari.accounts.createEntityAccounts({ entityId: entity.id });
const accountId = account.id;

const nonceResp = await dinari.wallets.getAccountWalletConnectionNonce({
  accountId,
  walletAddress: safeAddress,
  chainId: "eip155:421614",
});

const linkMessage = await safe.signMessage(safe.createMessage(nonceResp.message));

await dinari.wallets.createAccountWalletConnection({
  accountId,
  chainId: "eip155:421614",
  nonce: nonceResp.nonce,
  signature: linkMessage.encodedSignatures(),
  walletAddress: safeAddress,
});
```

> 📘
>
> ### Link the Safe, not an owner
>
> `walletAddress` must be the Safe address. Linking an owner EOA attributes orders to a wallet with no funds.

### Step 3: Approve Permit2 (one-time, per token)

`createpermit` picks the permit type from the wallet's on-chain ERC-20 allowance to Permit2, not from the wallet type:

| Safe's allowance to Permit2 | Permit returned | Safe can sign? |
| --- | --- | --- |
| None | ERC-2612 `Permit` | No |
| Present | Permit2 `PermitTransferFrom` | Yes |

Send the approval as a Safe transaction so the allowance belongs to the Safe:

TypeScript

```
import { encodeFunctionData, erc20Abi, maxUint256 } from "viem";

const PERMIT2 = "0x000000000022D473030F116dDEE9F6B43aC78BA3";

const approveTx = await safe.createTransaction({
  transactions: [
    {
      to: config.paymentTokenAddress,
      value: "0",
      data: encodeFunctionData({
        abi: erc20Abi,
        functionName: "approve",
        args: [PERMIT2, maxUint256],
      }),
    },
  ],
});

await safe.executeTransaction(await safe.signTransaction(approveTx));
```

> 🚧
>
> ### Per token, per chain
>
> Each payment token on each chain needs its own approval. If the allowance is revoked or used up, `createPermit` goes back to returning ERC-2612 permits.

### Step 4: Select the stock and order parameters

TypeScriptPythonGoJava

```
const stocks = await dinari.marketData.getStocks({ symbols: "AAPL", limit: 20 });
const stock = (Array.isArray(stocks) ? stocks : stocks.data).find((s) => s.symbol === "AAPL");
if (!stock) throw new Error("Stock not found");
const stockId = stock.id;
```

```
stocks = client.market_data.get_stocks(symbols="AAPL", limit=20)
stock = next((s for s in (stocks if isinstance(stocks, list) else stocks.data) if s.symbol == "AAPL"), None)
if stock is None:
    raise RuntimeError("Stock not found")
stock_id = stock.id
```

```
stocks, err := c.MarketData.GetStocks(ctx, &dinari.GetStocksRequest{
	Symbols: []*string{dinari.String("AAPL")},
	Limit:   dinari.Int(20),
})
if err != nil {
	log.Fatalf("Failed to list stocks: %v", err)
}

var stockID string
for _, s := range stocks.GetPaginatedStockResponse().Data {
	if s.Symbol == "AAPL" {
		stockID = s.ID
	}
}
if stockID == "" {
	log.Fatal("Stock not found")
}
```

```
var stocks = client.marketData().getStocks(
        GetStocksRequest.builder().symbols("AAPL").limit(20).build());
String stockId = ((PaginatedStockResponse) stocks.get()).getData().stream()
        .filter(s -> s.getSymbol().equals("AAPL"))
        .findFirst()
        .orElseThrow(() -> new RuntimeException("Stock not found"))
        .getId();
```

| Field | Meaning |
| --- | --- |
| `stock_id` | Dinari UUID of the dShare (from `marketData.getStocks()`). |
| `order_side` | `"BUY"` or `"SELL"`. |
| `order_type` | `"MARKET"` or `"LIMIT"`. |
| `order_tif` | Time-in-force, e.g. `"DAY"`. |
| `payment_token` | Payment-token address. Must be the token approved in Step 3. |
| `payment_token_quantity` | For a market **buy**, the notional amount of payment token to spend. |
| `chain_id` | CAIP-2 chain id, e.g. `"eip155:421614"`. |

Market sells and limit orders use `asset_quantity` instead; limit orders also take `limit_price`. Fees are added on top of the notional.

### Step 5: Create the order permit

TypeScriptPythonGoJava

```
const permitResponse = await dinari.orderRequests.createEip155OrderRequestPermit({
  accountId,
  chainId: "eip155:421614",
  orderSide: "BUY",
  orderType: "MARKET",
  orderTif: "DAY",
  stockId,
  paymentToken: config.paymentTokenAddress,
  paymentTokenQuantity: 10.0,
});

const orderRequestId = permitResponse.orderRequestId;
const permit = permitResponse.permit as Record<string, any>; // { domain, types, primaryType, message }

if (permit.primaryType === "Permit") {
  throw new Error("Got an ERC-2612 permit. Approve Permit2 from the Safe (Step 3).");
}
```

```
permit_response = client.order_requests.create_eip155order_request_permit(
    account_id=account_id,
    chain_id="eip155:421614",
    order_side="BUY",
    order_type="MARKET",
    order_tif="DAY",
    stock_id=stock_id,
    payment_token=payment_token_address,
    payment_token_quantity=10.0,
)

order_request_id = permit_response.order_request_id
permit = permit_response.permit  # { domain, types, primaryType, message }

if permit["primaryType"] == "Permit":
    raise RuntimeError("Got an ERC-2612 permit. Approve Permit2 from the Safe (Step 3).")
```

```
permitResponse, err := c.OrderRequests.CreateEip155OrderRequestPermit(ctx, &dinari.Eip155OrderRequestPermitInput{
	AccountID:            accountID,
	ChainID:              dinari.ChainIDEip155421614,
	OrderSide:            dinari.OrderSideBuy,
	OrderType:            dinari.OrderTypeMarket,
	OrderTif:             dinari.OrderTifDay,
	StockID:              dinari.String(stockID),
	PaymentToken:         paymentTokenAddress,
	PaymentTokenQuantity: dinari.Float64(10.0),
})
if err != nil {
	log.Fatalf("Failed to create permit: %v", err)
}

orderRequestID := permitResponse.OrderRequestID
permit := permitResponse.Permit // { domain, types, primaryType, message }

if permit["primaryType"] == "Permit" {
	log.Fatal("Got an ERC-2612 permit. Approve Permit2 from the Safe (Step 3).")
}
```

```
var permitResponse = client.orderRequests().createEip155OrderRequestPermit(
        accountId,
        Eip155OrderRequestPermitInput.builder()
                .chainId(ChainId.EIP155421614)
                .orderTif(OrderTif.DAY)
                .orderSide(OrderSide.BUY)
                .orderType(OrderType.MARKET)
                .paymentToken(paymentTokenAddress)
                .stockId(stockId)
                .paymentTokenQuantity(10.0)
                .build());

String orderRequestId = permitResponse.getOrderRequestId();
Map<String, Object> permit = permitResponse.getPermit(); // { domain, types, primaryType, message }

if ("Permit".equals(permit.get("primaryType"))) {
    throw new IllegalStateException("Got an ERC-2612 permit. Approve Permit2 from the Safe (Step 3).");
}
```

Check `primaryType` before signing. `Permit` means ERC-2612 and will fail; `PermitTransferFrom` or `PermitWitnessTransferFrom` means Permit2.

### Step 6: Sign the permit with the Safe

TypeScript

```
let signedPermit = await safe.signMessage(
  safe.createMessage({
    domain: permit.domain,
    types: permit.types,
    primaryType: permit.primaryType,
    message: permit.message,
  }),
);

// For threshold > 1, add each remaining owner's signature:
for (const ownerKey of walletSecrets.additionalOwnerKeys) {
  const ownerSafe = await safe.connect({ signer: ownerKey });
  signedPermit = await ownerSafe.signMessage(signedPermit);
}

const permitSignature = signedPermit.encodedSignatures();
```

> 🚧
>
> ### Use `encodedSignatures()`
>
> Pass the Safe's encoded signature, not an owner's raw 65-byte signature. The Safe's `isValidSignature` rejects raw owner signatures.

Permits have a short deadline. If owner approvals take time, create a new permit (Step 5) once signers are ready.

### Step 7: Build and send the transaction

TypeScript

```
const tx = await dinari.orderRequests.createEip155PermitTransaction({
  accountId,
  body: { orderRequestId, permitSignature },
});

const orderTx = await safe.createTransaction({
  transactions: [
    { to: tx.contractAddress, data: tx.data, value: tx.value ?? "0" },
  ],
});

const result = await safe.executeTransaction(await safe.signTransaction(orderTx));
console.log("Tx hash:", result.hash);
```

The owner EOA pays gas; the Safe is `msg.sender`. Do not send `tx.data` directly from an owner EOA.

### Step 8: Poll order status

TypeScriptPythonGoJava

```
const orderRequest = await dinari.orderRequests.getOrderRequestById({
  accountId,
  orderRequestId,
});
console.log("Status:", orderRequest.status);
```

```
order_request = client.order_requests.get_order_request_by_id(
    account_id=account_id,
    order_request_id=order_request_id,
)
print("Status:", order_request.status)
```

```
orderRequest, err := c.OrderRequests.GetOrderRequestByID(ctx, &dinari.GetOrderRequestByIDRequest{
	AccountID:      accountID,
	OrderRequestID: orderRequestID,
})
if err != nil {
	log.Fatalf("Failed to get order request: %v", err)
}
fmt.Println("Status:", orderRequest.Status)
```

```
var orderRequest = client.orderRequests().getOrderRequestById(accountId, orderRequestId);
System.out.println("Status: " + orderRequest.getStatus());
```

Two status concepts exist:

* `OrderRequestStatus` — the request status (pre-brokerage), on the `OrderRequest`.
* `BrokerageOrderStatus` — the resulting `Order`, via `dinari.orders.getOrderById({ accountId, orderId })`.

### Permit2 and smart contract wallets

ERC-2612 `permit()` verifies signatures with `ecrecover`, which only works for EOAs. Permit2 checks whether the signer has code and, if so, calls `isValidSignature` on it (ERC-1271). A Safe can only pass the second check.

`createPermit` returns an ERC-2612 permit whenever the wallet has no Permit2 allowance for the payment token. A new Safe has none, so its first order fails. The API accepts the signature either way, because verification happens on-chain:

| Flow | What you see |
| --- | --- |
| User Sponsored | Safe transaction reverts, usually `GS013` |
| Dinari Sponsored | No error returned; the order request expires |

  

> 🔨
>
> **Fix:** approve Permit2 from the Safe ([Step 3](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)) and check `primaryType` before signing ([Step 5](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)).

## Common errors

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| `primaryType` is `Permit` | No Permit2 allowance for this token/chain | Approve Permit2 from the Safe (Step 3) |
| `GS013` on order submission | ERC-2612 permit was signed | Approve Permit2, create and sign a new permit |
| Order request expires (Dinari Sponsored) | ERC-2612 permit was signed | Approve Permit2, create and sign a new permit |
| `isValidSignature` reverts | Safe not deployed, or non-default fallback handler | Deploy the Safe; use `CompatibilityFallbackHandler` |
| Signature rejected with a Permit2 permit | Raw owner signature sent | Send `encodedSignatures()` |
| Transaction reverts as expired | Permit deadline passed during signing | Create a new permit |
| Wallet linking fails | Safe not deployed, or owner EOA linked | Deploy, then link the Safe address |
| Order reverts or attributed to the wrong wallet | `tx.data` sent from an owner EOA | Execute through the Safe (Step 7) |
| Insufficient funds | Safe balance below notional + fees | Fund the Safe; see [Partner Fees](https://docs.dinari.com/docs/fees) |

Updated 6 days ago

---

[Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)[Order Types & Behaviors](https://docs.dinari.com/docs/order-type)

Did this page help you?

Yes

No

Copy Page

* + [How it works](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Prerequisites](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + - * [A Dinari API Key ID and API Secret Key from partners.dinari.com. Start in sandbox.](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 1: Initialize the clients](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 2: Complete KYC and link the Safe (one-time)](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 3: Approve Permit2 (one-time, per token)](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 4: Select the stock and order parameters](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 5: Create the order permit](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 6: Sign the permit with the Safe](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 7: Build and send the transaction](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Step 8: Poll order status](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
    - [Permit2 and smart contract wallets](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Common errors](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Placing dShare Orders with Safe Vaults","dateModified":"2026-11-10T01:00:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/funding-accounts-through-wallets>>>
---
url: https://docs.dinari.com/docs/funding-accounts-through-wallets
title: Funding Accounts through Wallets
description: This section covers how an Account can be funded through its connected Wallet . Funding on Sandbox EVM In testnet, EVM wallets can be funded by calling the faucet: import { DinariClient, DinariEnvironment } from "@dinari/api-sdk"; const client = new DinariClient({ apiKeyId: process.env.DINARI_API_KE…
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

# Funding Accounts through Wallets

This section covers how an `Account` can be funded through its connected `Wallet`.

# Funding on Sandbox

## EVM

In testnet, EVM wallets can be funded by calling the faucet:

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

  await client.accounts.createAccountFaucet({
    accountId,
    chainId: "eip155:84532",
  });

  console.log("Sandbox tokens minted");
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

client.accounts.create_account_faucet(
    account_id=account_id,
    chain_id="eip155:84532",
)
print("Sandbox tokens minted")
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

	err := c.Accounts.CreateAccountFaucet(context.Background(), &dinari.FaucetInput{
		AccountID: accountID,
		ChainID:   dinari.ChainIDEip15584532.Ptr(),
	})
	if err != nil {
		log.Fatalf("Failed to mint sandbox tokens: %v", err)
	}

	fmt.Println("Sandbox tokens minted")
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.accounts.requests.FaucetInput;
import com.dinari.api.types.ChainId;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";

        client.accounts().createAccountFaucet(
                accountId,
                FaucetInput.builder().chainId(ChainId.EIP15584532).build());
        System.out.println("Sandbox tokens minted");
    }
}
```

# Funding on Production

## External Wallets

### EVM

External wallets can be funded via USD+, USDC, or USDT

## Managed Wallets

### EVM

Similar to external wallets, managed wallets can be funded via USD+, USDC, or USDT.

Updated 6 days ago

---

[Managing Wallets](https://docs.dinari.com/docs/managing-wallets)[Ordering](https://docs.dinari.com/docs/dshare-ordering)

Did this page help you?

Yes

No

Copy Page

* + [Funding on Sandbox](https://docs.dinari.com/docs/funding-accounts-through-wallets)
  + - [EVM](https://docs.dinari.com/docs/funding-accounts-through-wallets)
  + [Funding on Production](https://docs.dinari.com/docs/funding-accounts-through-wallets)
  + - [External Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
    - * [EVM](https://docs.dinari.com/docs/funding-accounts-through-wallets)
    - [Managed Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
    - * [EVM](https://docs.dinari.com/docs/funding-accounts-through-wallets)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Funding Accounts through Wallets","dateModified":"2026-11-10T01:00:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/entity-management>>>
---
url: https://docs.dinari.com/docs/entity-management
title: Entity Management
description: An Entity represents either your organization, or your individual customers. The following sections provide an example on how to manage entities. Please note that to manage your organization, use the entity id provided in your dashboard. SDK References Language URL Javascript / Typescript https://gi…
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

# Entity Management

An `Entity` represents either your organization, or your individual customers. The following sections provide an example on how to manage entities. Please note that to manage your organization, use the entity id provided in your dashboard.

# SDK References

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#entities](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#entities](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#entities](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#entities](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

# SDK Examples

## Creating Entity

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const entity = await client.entities.createEntities({
    name: "John Doe LLC",
  });

  console.log(entity);
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

entity = client.entities.create_entities(
    name="John Doe LLC",
)
print(entity)
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

	entity, err := c.Entities.CreateEntities(context.Background(), &dinari.CreateEntityInput{
		Name: "John Doe LLC",
	})
	if err != nil {
		log.Fatalf("Failed to create entity: %v", err)
	}

	fmt.Printf("New Entity ID: %+v\n", entity.ID)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.entities.requests.CreateEntityInput;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var entity = client.entities().createEntities(
                CreateEntityInput.builder().name("John Doe LLC").build());
        System.out.println("New Entity ID: " + entity.getId());
    }
}
```

Updated 6 days ago

---

[Partner Fees](https://docs.dinari.com/docs/fees)[Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)

Did this page help you?

Yes

No

Copy Page

* + [SDK References](https://docs.dinari.com/docs/entity-management)
  + [SDK Examples](https://docs.dinari.com/docs/entity-management)
  + - [Creating Entity](https://docs.dinari.com/docs/entity-management)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Entity Management","dateModified":"2026-11-10T17:53:39.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/managing-accounts>>>
---
url: https://docs.dinari.com/docs/managing-accounts
title: Managing Accounts
description: An Account represents a financial account linked to an Entity , such as a brokerage account, a blockchain wallet for stocks, etc. The following sections provide an example on how to manage accounts on an entity. Please note that to manage your organization, use the entity id provided in your dashboa…
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

# Managing Accounts

An `Account` represents a financial account linked to an `Entity`, such as a brokerage account, a blockchain wallet for stocks, etc. The following sections provide an example on how to manage accounts on an entity. Please note that to manage your organization, use the entity id provided in your dashboard.

# SDK Reference

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#accounts](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#accounts](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#accounts](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#accounts](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

# SDK Examples

## Creating an Account

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const entity = await client.entities.createEntities({
    name: "Jane Doe",
  });

  const account = await client.accounts.createEntityAccounts({ entityId: entity.id });

  console.log(account);
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

entity = client.entities.create_entities(
    name="Jane Doe",
)

account = client.accounts.create_entity_accounts(
    entity_id=entity.id,
)
print(account)
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

	entity, err := c.Entities.CreateEntities(context.Background(), &dinari.CreateEntityInput{
		Name: "Jane Doe",
	})
	if err != nil {
		log.Fatalf("Failed to create entity: %v", err)
	}

	account, err := c.Accounts.CreateEntityAccounts(context.Background(), &dinari.CreateAccountInput{
		EntityID: entity.ID,
	})
	if err != nil {
		log.Fatalf("Failed to create account: %v", err)
	}

	fmt.Printf("Account ID: %+v\n", account.ID)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.entities.requests.CreateEntityInput;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var entity = client.entities().createEntities(
                CreateEntityInput.builder().name("Jane Doe").build());

        var account = client.accounts().createEntityAccounts(entity.getId());
        System.out.println("Account ID: " + account.getId());
    }
}
```

## Adding Wallet to an Account

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
  const walletAddress = "your-wallet-address";

  // Step 1: Get the nonce message to sign
  const nonceResp = await client.wallets.getAccountWalletConnectionNonce({
    accountId,
    walletAddress,
    chainId: "eip155:1",
  });

  // Step 2: Sign the message (replace this with actual off-chain signing)
  const signature = "your-wallet-signature"; // Sign nonceResp.message with the wallet

  // Step 3: Connect the wallet using the signed message
  const linkedWallet = await client.wallets.createAccountWalletConnection({
    accountId,
    chainId: "eip155:1",
    nonce: nonceResp.nonce,
    signature,
    walletAddress,
  });

  console.log(linkedWallet);
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
wallet_address = "your-wallet-address"

# Step 1: Get the nonce message to sign
nonce_resp = client.wallets.get_account_wallet_connection_nonce(
    account_id=account_id,
    wallet_address=wallet_address,
    chain_id="eip155:1",
)

# Step 2: Sign the message (replace this with actual off-chain signing)
signature = "your-wallet-signature"  # Sign nonce_resp.message with the wallet

# Step 3: Connect the wallet using the signed message
linked_wallet = client.wallets.create_account_wallet_connection(
    account_id=account_id,
    chain_id="eip155:1",
    nonce=nonce_resp.nonce,
    signature=signature,
    wallet_address=wallet_address,
)
print(linked_wallet)
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
	walletAddress := "your-wallet-address"

	// Step 1: Get the nonce message to sign
	nonceResp, err := c.Wallets.GetAccountWalletConnectionNonce(context.Background(), &dinari.GetAccountWalletConnectionNonceRequest{
		AccountID:     accountID,
		WalletAddress: walletAddress,
		ChainID:       dinari.WalletChainIDEip1551,
	})
	if err != nil {
		log.Fatalf("Failed to get wallet nonce: %v", err)
	}

	// Step 2: Sign the message (replace this with actual off-chain signing)
	signature := "your-wallet-signature" // Sign nonceResp.Message with the wallet

	// Step 3: Connect the wallet using the signed message
	linkedWallet, err := c.Wallets.CreateAccountWalletConnection(context.Background(), &dinari.CreateAccountWalletConnectionInput{
		AccountID:     accountID,
		ChainID:       dinari.WalletChainIDEip1551,
		Nonce:         nonceResp.Nonce,
		Signature:     signature,
		WalletAddress: walletAddress,
	})
	if err != nil {
		log.Fatalf("Failed to connect external wallet: %v", err)
	}

	fmt.Printf("Linked Wallet: %+v\n", linkedWallet)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.wallets.requests.CreateAccountWalletConnectionInput;
import com.dinari.api.resources.wallets.requests.GetAccountWalletConnectionNonceRequest;
import com.dinari.api.types.WalletChainId;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String walletAddress = "your-wallet-address";

        // Step 1: Get the nonce message to sign
        var nonceResp = client.wallets().getAccountWalletConnectionNonce(
                accountId,
                GetAccountWalletConnectionNonceRequest.builder()
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP1551)
                        .build());

        // Step 2: Sign the message (replace this with actual off-chain signing)
        String signature = "your-wallet-signature"; // Sign nonceResp.getMessage() with the wallet

        // Step 3: Connect the wallet using the signed message
        var linkedWallet = client.wallets().createAccountWalletConnection(
                accountId,
                CreateAccountWalletConnectionInput.builder()
                        .signature(signature)
                        .nonce(nonceResp.getNonce())
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP1551)
                        .build());
        System.out.println(linkedWallet);
    }
}
```

### Customer Wallets

Customer wallets are connected with the external wallet flow shown above.

### Managed Wallets

> ❗️
>
> ### This will only work on your organization's accounts

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

  const wallet = await client.wallets.createAccountWalletInternalConnection({
    accountId,
    walletAddress: "your-wallet-address",
    chainId: "eip155:1",
  });

  console.log(wallet);
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

wallet = client.wallets.create_account_wallet_internal_connection(
    account_id="your-account-id",
    wallet_address="your-wallet-address",
    chain_id="eip155:1",
)
print(wallet)
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

	wallet, err := c.Wallets.CreateAccountWalletInternalConnection(context.Background(), &dinari.CreateAccountWalletInternalConnectionInput{
		AccountID:     "your-account-id",
		WalletAddress: "your-wallet-address",
		ChainID:       dinari.WalletChainIDEip1551,
	})
	if err != nil {
		log.Fatalf("Failed to connect managed wallet: %v", err)
	}

	fmt.Printf("Wallet: %+v\n", wallet)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.wallets.requests.CreateAccountWalletInternalConnectionInput;
import com.dinari.api.types.WalletChainId;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var wallet = client.wallets().createAccountWalletInternalConnection(
                "your-account-id",
                CreateAccountWalletInternalConnectionInput.builder()
                        .walletAddress("your-wallet-address")
                        .chainId(WalletChainId.EIP1551)
                        .build());
        System.out.println(wallet);
    }
}
```

Updated 6 days ago

---

[Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)[Managing Wallets](https://docs.dinari.com/docs/managing-wallets)

Did this page help you?

Yes

No

Copy Page

* + [SDK Reference](https://docs.dinari.com/docs/managing-accounts)
  + [SDK Examples](https://docs.dinari.com/docs/managing-accounts)
  + - [Creating an Account](https://docs.dinari.com/docs/managing-accounts)
    - [Adding Wallet to an Account](https://docs.dinari.com/docs/managing-accounts)
    - * [Customer Wallets](https://docs.dinari.com/docs/managing-accounts)
      * [Managed Wallets](https://docs.dinari.com/docs/managing-accounts)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Managing Accounts","dateModified":"2026-11-10T17:53:39.000Z"}
```