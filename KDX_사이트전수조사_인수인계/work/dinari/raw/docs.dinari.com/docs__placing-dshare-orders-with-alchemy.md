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