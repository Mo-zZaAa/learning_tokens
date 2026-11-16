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