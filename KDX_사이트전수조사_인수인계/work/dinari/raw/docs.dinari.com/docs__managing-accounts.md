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