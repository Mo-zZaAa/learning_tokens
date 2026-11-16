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