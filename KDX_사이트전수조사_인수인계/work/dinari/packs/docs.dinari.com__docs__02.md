# 읽기 묶음: docs.dinari.com / docs (2/5)


<<<PAGE https://docs.dinari.com/docs/blockchain>>>
---
url: https://docs.dinari.com/docs/blockchain
title: Blockchain
description: Supported blockchains dShares™ are currently available on the following blockchains with many more coming soon. Blockchain chain_id Ethereum Mainnet eip155:1 Arbitrum One eip155:42161 Avalanche C-Chain eip155:43114 Base eip155:8453 HyperEVM eip155:999 HyperCore N/A Plume eip155:98866 HyperCore is Hy…
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

# Blockchain

# Supported blockchains

dShares™ are currently available on the following blockchains with many more coming soon.

| Blockchain | chain\_id |
| --- | --- |
| [Ethereum Mainnet](https://ethereum.org/) | `eip155:1` |
| [Arbitrum One](https://arbitrum.io/) | `eip155:42161` |
| [Avalanche C-Chain](https://www.avax.network/) | `eip155:43114` |
| [Base](https://www.base.org/) | `eip155:8453` |
| [HyperEVM](https://hyperliquid.xyz/) | `eip155:999` |
| [HyperCore](https://hyperliquid.xyz/) | N/A |
| [Plume](https://plume.org/) | `eip155:98866` |

*HyperCore is Hyperliquid's non-EVM order-book layer, so it has no EVM chain ID — dShares™ there are identified by a HyperCore token index.*

> 📘
>
> If you'd like to bring dShares™ to your blockchain, please reach out to us via email to [📧 [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection).

> 🚧
>
> Support for the [Kinto blockchain](https://www.kinto.xyz/) has been deprecated as part of the scheduled orderly shutdown of the blockchain. For more information, please see the [Kinto deprecation](https://docs.dinari.com/docs/kinto-deprecation) information page.

> 🚧
>
> Support for the [Blast blockchain](https://blast.io/) has been deprecated. For more information, please see the [Blast deprecation](https://docs.dinari.com/docs/deprecations) information page.

Updated about 1 month ago

---

[What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)[Wrapping dShares™](https://docs.dinari.com/docs/wrapping)

Did this page help you?

Yes

No

Copy Page

* + [Supported blockchains](https://docs.dinari.com/docs/blockchain)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Blockchain","dateModified":"2026-10-14T11:27:27.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/wrapping>>>
---
url: https://docs.dinari.com/docs/wrapping
title: Wrapping dShares™
description: Learn how to wrap dShares into ERC-20 tokens on HyperEVM and transfer them to HyperCore.
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

# Wrapping dShares™

Learn how to wrap dShares into ERC-20 tokens on HyperEVM and transfer them to HyperCore.

## What is wrapping?

Wrapping is the process of converting a native asset into a standardized token format (ERC-20), enabling native assets to interact with smart contracts across multiple chains. Understanding this concept is fundamental to cross-chain asset management.

In the Hyperliquid ecosystem, wrapping allows dShares™ to transition from the native HyperCore trading ledger into standard ERC-20 tokens on HyperEVM. This process works by locking the native dShares asset and minting a wrapped equivalent in return, making the shares compatible with EVM smart contracts and enabling interaction with the broader DeFi ecosystem.

dShares™ cannot be bridged directly to other chains. To move them, you must first wrap them into wrapped dShares and then send the wrapped tokens to a HyperCore bridge.

```
sequenceDiagram
    actor P as Partner
    participant API as Dinari API
    participant HE as HyperEVM
    participant L1 as Dinari L1
    participant HC as HyperCore
    Note over P,HC: Phase 1 — Purchase the dShare
    P->>API: 1. Request order permit
    API-->>P: Return permit to sign
    P->>API: 2. Submit signed permit
    API->>HE: 3. Submit order on HyperEVM
    HE->>L1: Bridge order to Dinari L1
    L1->>L1: 4. Process order
    L1->>HE: Bridge dShare back to HyperEVM
    Note over P,HC: Phase 2 — Move to HyperCore
    P->>HE: 5. deposit() on wrapped dShare
    HE-->>P: 6. Receive wrapped dShare
    P->>HE: 7. transfer() to bridge address
    HE->>HC: Tokens arrive on HyperCore
```

## Integration guide to wrapping dShares™

To bridge your dShares™, complete three on-chain interactions:

1. **Approval**: Grant the wrapped dShare contract permission to move your dShares. This security step explicitly authorizes how many tokens the contract can spend on your behalf.
2. **Deposit (wrap)**: Call the deposit function to exchange your native dShares for their wrapped equivalent. This locks your original assets and mints the corresponding wrapped tokens to your account.
3. **Bridge**: Transfer your newly created wrapped dShares to the HyperCore bridge address, which initiates the cross-chain transfer to your destination.

## Addresses for SPCX dShare and wrapped dShare

| Address | Value |
| --- | --- |
| Native dShare contract | `0x9b4Db2271EB1fa0aEe1abA7ed55E51C38cE514a3` |
| Wrapped dShare contract | `0x95687557C66BC799a850bA7037673528238ae763` |
| HyperEVM to HyperCore bridge address | `0x2000000000000000000000000000000000000262` |
| HyperCore token index | `610` |

  

### Step 1: Approval

#### Initialize the chain manager and account

Start by initializing the EVM manager for your chain.

TypeScript

```
import { DinariClient } from "@dinari/api-sdk";
import { ethers } from 'ethers'; // v6

// Dinari API SDK is used to link your wallet to your account
const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!,
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!,
});

// HyperEVM mainnet is chain ID 999. Use the testnet RPC only if testing on 998.
const provider = new ethers.JsonRpcProvider('https://rpc.hyperliquid.xyz/evm');
const wallet = new ethers.Wallet(process.env['WALLET_PRIVATE_KEY']!, provider);

// Set these to the dShare being wrapped and its wrapped dShare on the target chain.
const dshareAddress = 'dShare-Address';
const wrappedDshareAddress = 'your-wrapped-dShare-address';
```

#### Load the native and wrapped dShare contracts

* See the ERC-20 spec: <https://eips.ethereum.org/EIPS/eip-20>
* See the ERC-4626 spec: <https://eips.ethereum.org/EIPS/eip-4626>

TypeScript

```
// Generic ERC20 Interfaces
const ERC20_ABI = [
  'function allowance(address owner, address spender) view returns (uint256)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function balanceOf(address owner) view returns (uint256)',
  'function decimals() view returns (uint8)',
  'function transfer(address to, uint256 amount) returns (bool)',
];

// Create the Wrapped ABI for the Existing Contract
const WRAPPED_ABI = [...ERC20_ABI, 'function deposit(uint256 assets, address receiver) returns (uint256 shares)'];

const dshare = new ethers.Contract(dshareAddress, ERC20_ABI, wallet);
const wrappedDshare = new ethers.Contract(wrappedDshareAddress, WRAPPED_ABI, wallet);
```

  

#### Link your wallet to your Account

TypeScriptPythonGoJava

```
// Link your wallet to your Dinari account -this is required to use the API.
async function main() {
  const accountId = 'your-account-id';
  const nonceResp = await client.wallets.getAccountWalletConnectionNonce({
    accountId,
    walletAddress: wallet.address,
    chainId: 'eip155:999',
  });

  // Sign the nonce message to prove ownership
  const signature = await wallet.signMessage(nonceResp.message);

  // Connect you wallet to your Dinari Account using the signed nonce
  await client.wallets.createAccountWalletConnection({
    accountId,
    chainId: 'eip155:999',
    nonce: nonceResp.nonce,
    signature,
    walletAddress: wallet.address,
  });
```

```
import os

from dinari_api_sdk import DinariClient

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],
)

account_id = "your-account-id"
wallet_address = "your-wallet-address"

# Link your wallet to your Dinari account - this is required to use the API.
nonce_resp = client.wallets.get_account_wallet_connection_nonce(
    account_id=account_id,
    wallet_address=wallet_address,
    chain_id="eip155:999",
)

# Sign nonce_resp.message with your wallet to prove ownership
signature = "your-wallet-signature"

# Connect your wallet to your Dinari Account using the signed nonce
client.wallets.create_account_wallet_connection(
    account_id=account_id,
    chain_id="eip155:999",
    nonce=nonce_resp.nonce,
    signature=signature,
    wallet_address=wallet_address,
)
```

```
package main

import (
	"context"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx := context.Background()

	accountID := "your-account-id"
	walletAddress := "your-wallet-address"

	// Link your wallet to your Dinari account - this is required to use the API.
	nonceResp, err := c.Wallets.GetAccountWalletConnectionNonce(ctx, &dinari.GetAccountWalletConnectionNonceRequest{
		AccountID:     accountID,
		WalletAddress: walletAddress,
		ChainID:       dinari.WalletChainIDEip155999,
	})
	if err != nil {
		log.Fatalf("Failed to get wallet nonce: %v", err)
	}

	// Sign nonceResp.Message with your wallet to prove ownership
	signature := "your-wallet-signature"

	// Connect your wallet to your Dinari Account using the signed nonce
	_, err = c.Wallets.CreateAccountWalletConnection(ctx, &dinari.CreateAccountWalletConnectionInput{
		AccountID:     accountID,
		ChainID:       dinari.WalletChainIDEip155999,
		Nonce:         nonceResp.Nonce,
		Signature:     signature,
		WalletAddress: walletAddress,
	})
	if err != nil {
		log.Fatalf("Failed to connect wallet: %v", err)
	}
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.resources.wallets.requests.CreateAccountWalletConnectionInput;
import com.dinari.api.resources.wallets.requests.GetAccountWalletConnectionNonceRequest;
import com.dinari.api.types.WalletChainId;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .apiKeyId(System.getenv("DINARI_API_KEY_ID"))
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY"))
                .build();

        String accountId = "your-account-id";
        String walletAddress = "your-wallet-address";

        // Link your wallet to your Dinari account - this is required to use the API.
        var nonceResp = client.wallets().getAccountWalletConnectionNonce(
                accountId,
                GetAccountWalletConnectionNonceRequest.builder()
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP155999)
                        .build());

        // Sign nonceResp.getMessage() with your wallet to prove ownership
        String signature = "your-wallet-signature";

        // Connect your wallet to your Dinari Account using the signed nonce
        client.wallets().createAccountWalletConnection(
                accountId,
                CreateAccountWalletConnectionInput.builder()
                        .signature(signature)
                        .nonce(nonceResp.getNonce())
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP155999)
                        .build());
    }
}
```

  

#### Set the total amount of shares to wrap and contract decimals

TypeScript

```
  // Set the total amount of shares to wrap and contract decimals
  const decimals = await dshare.decimals();
  const totalAmount = ethers.parseUnits('10', decimals);
```

  

#### Now you can sign your approval

TypeScript

```
  const currentAllowance = await dshare.allowance(wallet.address, wrappedDshareAddress);
  if (currentAllowance < totalAmount) {
    const approveTx = await dshare.approve(wrappedDshareAddress, totalAmount);
    await approveTx.wait();
  }
```

  

### Step 2: Deposit (wrap)

Specify the amount of native dShares you intend to wrap and deposit them into the wrapped dShare contract. The contract mints wrapped dShares to your account in return.

TypeScript

```
// Wrapping spends native dShares, so validate the native dShare balance.
const balance = await dshare.balanceOf(wallet.address);
	if (balance < totalAmount) {
  	throw new Error(`Insufficient dShare balance: have ${balance}, need ${totalAmount}`);
}
  
// Your deposit needs the total amount of shares to wrap and the receiver address on the target chain.
const wrappedBefore = await wrappedDshare.balanceOf(wallet.address);
const depositTx = await wrappedDshare.deposit(totalAmount, wallet.address);
await depositTx.wait();
const wrappedAfter = await wrappedDshare.balanceOf(wallet.address);
const mintedAmount = wrappedAfter - wrappedBefore;
```

### Step 3: Transfer to the HyperCore bridge

Transfer the wrapped tokens to the HyperCore bridge address. This initiates the cross-chain transfer. Bridge the amount that was actually minted in Step 2 (`minted_amount`), send it to the correct bridge address, and verify the transaction on-chain so the bridge can process and finalize the transfer.

TypeScript

```
const bridgeAddress = 'target-bridge-address';
const transferTx = await wrappedDshare.transfer(bridgeAddress, mintedAmount);
await transferTx.wait();
```

## Complete reference script

This is the complete, uninterrupted script for bridging a dShare to HyperCore:

TypeScript

```
import { DinariClient } from "@dinari/api-sdk";
import { ethers } from 'ethers'; // v6

// Dinari API SDK (REST): used here to link the wallet to your account.
const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!,
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!,
});

// HyperEVM mainnet is chain ID 999. Use the testnet RPC only if testing on 998.
const provider = new ethers.JsonRpcProvider('https://rpc.hyperliquid.xyz/evm');
const wallet = new ethers.Wallet(process.env['WALLET_PRIVATE_KEY']!, provider);

// Set these to the dShare being wrapped and its wrapped dShare on the target chain.
const dshareAddress = 'dShare-Address';
const wrappedDshareAddress = 'your-wrapped-dShare-address';

// Minimal ERC-20 (dShare) and ERC-4626 (wrapped dShare) interfaces.
// See the ERC-20 spec: https://eips.ethereum.org/EIPS/eip-20
// See the ERC-4626 spec: https://eips.ethereum.org/EIPS/eip-4626
const ERC20_ABI = [
  'function allowance(address owner, address spender) view returns (uint256)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function balanceOf(address owner) view returns (uint256)',
  'function decimals() view returns (uint8)',
  'function transfer(address to, uint256 amount) returns (bool)',
];
const WRAPPED_ABI = [...ERC20_ABI, 'function deposit(uint256 assets, address receiver) returns (uint256 shares)'];

const dshare = new ethers.Contract(dshareAddress, ERC20_ABI, wallet);
const wrappedDshare = new ethers.Contract(wrappedDshareAddress, WRAPPED_ABI, wallet);

// Link your wallet to your Dinari account -this is required to use the API.
async function main() {
  const accountId = 'your-account-id';
  const nonceResp = await client.wallets.getAccountWalletConnectionNonce({
    accountId,
    walletAddress: wallet.address,
    chainId: 'eip155:999',
  });

  // Sign the nonce message to prove ownership
  const signature = await wallet.signMessage(nonceResp.message);

  // Connect you wallet to your Dinari Account using the signed nonce
  await client.wallets.createAccountWalletConnection({
    accountId,
    chainId: 'eip155:999',
    nonce: nonceResp.nonce,
    signature,
    walletAddress: wallet.address,
  });

  // Set the total amount of shares to wrap and contract decimals
  const decimals = await dshare.decimals();
  const totalAmount = ethers.parseUnits('10', decimals);

  // --- Step 1: Approval ---
  const currentAllowance = await dshare.allowance(wallet.address, wrappedDshareAddress);
  if (currentAllowance < totalAmount) {
    const approveTx = await dshare.approve(wrappedDshareAddress, totalAmount);
    await approveTx.wait();
  }

  // --- Step 2: Deposit (wrap) ---
  // Wrapping spends native dShares, so validate the native dShare balance.
  const balance = await dshare.balanceOf(wallet.address);
  if (balance < totalAmount) {
    throw new Error(`Insufficient dShare balance: have ${balance}, need ${totalAmount}`);
  }

  // Your deposit needs the total amount of shares to wrap and the receiver address on the target chain.
  const wrappedBefore = await wrappedDshare.balanceOf(wallet.address);
  const depositTx = await wrappedDshare.deposit(totalAmount, wallet.address);
  await depositTx.wait();
  const wrappedAfter = await wrappedDshare.balanceOf(wallet.address);
  const mintedAmount = wrappedAfter - wrappedBefore;

  // --- Step 3: Transfer to the HyperCore bridge ---
  const bridgeAddress = 'target-bridge-address';
  const transferTx = await wrappedDshare.transfer(bridgeAddress, mintedAmount);
  await transferTx.wait();
}

main();
```

  

## Wrapping Using Hyper Explorer

One alternative to programmatic wrapping, is using Hyper Explorer to wrap a dShare by utilizing Proxy Contract Interactions on HyperEVM with the token you intend like to wrap. The same high level steps are performed, however they are performed as contract interactions on the hyperevm scan page. In this example, we're using SpaceX (SPCX)

### Step 1: Provide Approval to your Connected Wallet

Navigate to the contract page on HyperEVM Scan for the SPCX Token and utilize the approve() function call.

For example SPCX (SpaceX Wrapped Token). Navigate to its token listing on HyperEVM Scan, navigate to the Contract Page, and select [Write As Proxy](https://hyperevmscan.io/token/0x9b4db2271eb1fa0aee1aba7ed55e51c38ce514a3). Go to the Approve Function and set the spender to the wrapped token contract address and the amount you want to wrap.

For SpaceX the wrapped token contract address is: `0x95687557C66BC799a850bA7037673528238ae763`

 [그림: HyperEVM Scan approval form for approving the SPCX wrapped token contract as spender] 

### Step 2: Perform the Deposit

Call the deposit function on the same page with the assets set to the number of dShares you want to wrap and the to address. [Direct Link for SpaceX Deposit Function](https://hyperevmscan.io/address/0x95687557C66BC799a850bA7037673528238ae763)

 [그림: HyperEVM Scan deposit function for wrapping SPCX dShares] 

### Step 3: Transfer the Tokens

Call the transfer function for the token with the transfer address set to the assets HyperEVM Bridge Address, for SPCX this is `0x2000000000000000000000000000000000000262`, and amount set to the amount of wrapped dShares retrieved from previous call. [Direct Link for SpaceX Transfer Function](https://hyperevmscan.io/address/0x95687557C66BC799a850bA7037673528238ae763)

*Note: This address changes depending on the token. Be sure you provide the specific address for the dShare you're wrapping.*

 [그림: HyperEVM Scan transfer function for sending wrapped SPCX dShares to the HyperEVM bridge address]

Updated 6 days ago

---

[Blockchain](https://docs.dinari.com/docs/blockchain)[Hyperliquid](https://docs.dinari.com/docs/hyperliquid)

Did this page help you?

Yes

No

Copy Page

* + [What is wrapping?](https://docs.dinari.com/docs/wrapping)
  + [Integration guide to wrapping dShares™](https://docs.dinari.com/docs/wrapping)
  + [Addresses for SPCX dShare and wrapped dShare](https://docs.dinari.com/docs/wrapping)
  + - [Step 1: Approval](https://docs.dinari.com/docs/wrapping)
    - * [Initialize the chain manager and account](https://docs.dinari.com/docs/wrapping)
      * [Load the native and wrapped dShare contracts](https://docs.dinari.com/docs/wrapping)
      * [Link your wallet to your Account](https://docs.dinari.com/docs/wrapping)
      * [Set the total amount of shares to wrap and contract decimals](https://docs.dinari.com/docs/wrapping)
      * [Now you can sign your approval](https://docs.dinari.com/docs/wrapping)
    - [Step 2: Deposit (wrap)](https://docs.dinari.com/docs/wrapping)
    - [Step 3: Transfer to the HyperCore bridge](https://docs.dinari.com/docs/wrapping)
  + [Complete reference script](https://docs.dinari.com/docs/wrapping)
  + [Wrapping Using Hyper Explorer](https://docs.dinari.com/docs/wrapping)
  + - [Step 1: Provide Approval to your Connected Wallet](https://docs.dinari.com/docs/wrapping)
    - [Step 2: Perform the Deposit](https://docs.dinari.com/docs/wrapping)
    - [Step 3: Transfer the Tokens](https://docs.dinari.com/docs/wrapping)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Wrapping dShares™","dateModified":"2026-11-10T01:00:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/what-is-dshare>>>
---
url: https://docs.dinari.com/docs/what-is-dshare
title: What are dShares™?
description: A dShare™ is a token 1:1 backed by a security , commonly a U.S. equity. How is it backed? To ensure a true 1:1 backing, a mint (aka issuance) or a burn (aka redemption) only occurs when a corresponding order is complete on a brokerage account: sequenceDiagram actor A as Customer participant B as Blo…
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

# What are dShares™?

A dShare™ is a token 1:1 backed by a [security](https://www.investopedia.com/terms/s/security.asp), commonly a U.S. equity.

# How is it backed?

To ensure a true 1:1 backing, a mint (aka issuance) or a burn (aka redemption) only occurs when a corresponding order is complete on a brokerage account:

```
sequenceDiagram
	actor A as Customer
	participant B as Blockchain
	participant C as Dinari
	participant D as Alpaca
	Note over A,D: Issuance
	A ->> B: Escrow funds and submit order
	B ->> C: Forward order
	C ->> D: Submit order
	D ->> D: Fill order
	D ->> C: Notify completion
	C ->> B: Fill order
	B ->> A: Mint dShares
	Note over A,D: Redemption
	A ->> B: Escrow dShares and submit order
	B ->> C: Forward order
	C ->> D: Submit order
	D ->> D: Fill order
	D ->> C: Notify completion
	C ->> B: Fill order
	B ->> B: Burn dShares
	B ->> A: Transfer funds
```

Updated about 1 month ago

---

[Hosted Trading](https://docs.dinari.com/docs/hosted-trading)[Blockchain](https://docs.dinari.com/docs/blockchain)

Did this page help you?

Yes

No

Copy Page

* + [How is it backed?](https://docs.dinari.com/docs/what-is-dshare)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"What are dShares™?","dateModified":"2026-10-14T11:27:27.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/usdplus-evm>>>
---
url: https://docs.dinari.com/docs/usdplus-evm
title: EVM
description: USD+ Token Address Mainnet Chain Chain ID Address Mainnet 1 0xC9E3df3D230980B45adC623C81C3DF4A73a5350f Base 8453 0xC9E3df3D230980B45adC623C81C3DF4A73a5350f Arbitrum 42161 0xC9E3df3D230980B45adC623C81C3DF4A73a5350f Plume 98866 0xC9E3df3D230980B45adC623C81C3DF4A73a5350f Testnet Chain Chain ID Address…
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

# EVM

# USD+ Token Address

## Mainnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Mainnet | 1 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Base | 8453 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Arbitrum | 42161 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Plume | 98866 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |

## Testnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Base Sepolia | 84532 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Plume Testnet | 98867 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Arbitrum Sepolia | 421614 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |
| Sepolia | 11155111 | `0xC9E3df3D230980B45adC623C81C3DF4A73a5350f` |

  

# USD+ Minter Contract

## Mainnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Mainnet | 1 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Base | 8453 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Arbitrum | 42161 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Plume | 98866 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |

## Testnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Base Sepolia | 84532 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Plume Testnet | 98867 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Arbitrum Sepolia | 421614 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |
| Sepolia | 11155111 | `0x500c1B2F2ce1Cb64c53cc7759d8110EFf5dE93cE` |

  

# USD+ Redeemer Contract

## Mainnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Mainnet | 1 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Base | 8453 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Arbitrum | 42161 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Plume | 98866 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |

## Testnet

| Chain | Chain ID | Address |
| --- | --- | --- |
| Base Sepolia | 84532 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Plume Testnet | 98867 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Arbitrum Sepolia | 421614 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |
| Sepolia | 11155111 | `0xC22E4A78B8aD3fa027c3be66387a4067947a7C45` |

Updated about 1 month ago

---

[What is USD+?](https://docs.dinari.com/docs/what-is-usd)[Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)

Did this page help you?

Yes

No

Copy Page

* + [USD+ Token Address](https://docs.dinari.com/docs/usdplus-evm)
  + - [Mainnet](https://docs.dinari.com/docs/usdplus-evm)
    - [Testnet](https://docs.dinari.com/docs/usdplus-evm)
  + [USD+ Minter Contract](https://docs.dinari.com/docs/usdplus-evm)
  + - [Mainnet](https://docs.dinari.com/docs/usdplus-evm)
    - [Testnet](https://docs.dinari.com/docs/usdplus-evm)
  + [USD+ Redeemer Contract](https://docs.dinari.com/docs/usdplus-evm)
  + - [Mainnet](https://docs.dinari.com/docs/usdplus-evm)
    - [Testnet](https://docs.dinari.com/docs/usdplus-evm)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"EVM","dateModified":"2026-10-14T11:27:32.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/usdplus-evm-integration-guide>>>
---
url: https://docs.dinari.com/docs/usdplus-evm-integration-guide
title: Integration Guide
description: Minting USD+ To mint USD+, a deposit or mint can be performed on the USD+ Minter Contract as seen below: /// @notice calculate USD+ amount to mint for payment /// @param paymentToken payment token /// @param paymentTokenAmount amount of payment token function previewDeposit(IERC20 paymentToken, uint…
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

# Integration Guide

# Minting USD+

To mint USD+, a `deposit` or `mint` can be performed on the [USD+ Minter Contract](https://docs.dinari.com/docs/usdplus-evm) as seen below:

depositmint

```
/// @notice calculate USD+ amount to mint for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
function previewDeposit(IERC20 paymentToken, uint256 paymentTokenAmount)
  external
  view
  returns (uint256 usdPlusAmount);

/// @notice mint USD+ for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token to spend
/// @param receiver recipient
/// @return usdPlusAmount amount of USD+ minted
function deposit(IERC20 paymentToken, uint256 paymentTokenAmount, address receiver)
	external
	returns (uint256 usdPlusAmount);
```

```
/// @notice calculate the payment token amount to spend to mint USD+
/// @param paymentToken payment token
/// @param usdPlusAmount amount of USD+ to mint
function previewMint(IERC20 paymentToken, uint256 usdPlusAmount) 
	external view 
	returns (uint256 paymentTokenAmount);

/// @notice mint USD+ for payment
/// @param paymentToken payment token
/// @param usdPlusAmount amount of USD+ to mint
/// @param receiver recipient
/// @return paymentTokenAmount amount of payment token spent
function mint(IERC20 paymentToken, uint256 usdPlusAmount, address receiver)
	external
	returns (uint256 paymentTokenAmount);
```

# Redeeming USD+

To redeem USD+, a `requestRedeem` or `requestWithdraw`can be performed on the [USD+ Redeem Contract](https://docs.dinari.com/docs/usdplus-evm) as seen below:

requestRedeemrequestWithdraw

```
/// @notice calculate payment token amount received for burning USD+
/// @param paymentToken payment token
/// @param usdplusAmount amount of USD+ to burn
function previewRedeem(IERC20 paymentToken, uint256 usdplusAmount)
	external
	view
	returns (uint256 paymentTokenAmount);

/// @notice create a request to burn USD+ for payment
/// @param paymentToken payment token
/// @param usdplusAmount amount of USD+ to burn
/// @param receiver recipient
/// @param owner USD+ owner
/// @return ticket request ticket number
/// @dev exchange rate fixed at time of request creation
function requestRedeem(IERC20 paymentToken, uint256 usdplusAmount, address receiver, address owner)
	external
	returns (uint256 ticket);
```

```
/// @notice calculate payment token amount received for burning USD+
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
function previewWithdraw(IERC20 paymentToken, uint256 paymentTokenAmount)
	external
	view
	returns (uint256 usdplusAmount);

/// @notice create a request to burn USD+ for payment
/// @param paymentToken payment token
/// @param paymentTokenAmount amount of payment token
/// @param receiver recipient
/// @param owner USD+ owner
/// @return ticket request ticket number
/// @dev exchange rate fixed at time of request creation
function requestWithdraw(IERC20 paymentToken, uint256 paymentTokenAmount, address receiver, address owner)
	external
	returns (uint256 ticket);
```

Either of the two methods above will create a redemption request that may take 0-3 days depending on the size of the redemption made.

Updated about 1 month ago

---

[EVM](https://docs.dinari.com/docs/usdplus-evm)[Trading Hours](https://docs.dinari.com/docs/trading-hours)

Did this page help you?

Yes

No

Copy Page

* + [Minting USD+](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
  + [Redeeming USD+](https://docs.dinari.com/docs/usdplus-evm-integration-guide)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Integration Guide","dateModified":"2026-10-14T11:27:32.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/what-is-usd>>>
---
url: https://docs.dinari.com/docs/what-is-usd
title: What is USD+?
description: USD+ is a yield-bearing stablecoin issued by Dinari. It is pegged 1:1 to the US dollar, 100% backed by short-term US treasuries and USD , and it automatically pays yield to anyone holding it — no staking, claiming, or lockups required. Think of USD+ like a brokerage cash sweep . When cash sits idle…
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

# What is USD+?

USD+ is a yield-bearing stablecoin issued by Dinari. It is pegged 1:1 to the US dollar, [100% backed by short-term US treasuries and USD](https://usd.dinari.com/transparency), and it automatically pays yield to anyone holding it — no staking, claiming, or lockups required.

Think of USD+ like a **brokerage cash sweep**. When cash sits idle in a brokerage account, it is automatically swept into short-term US treasuries so it earns yield instead of doing nothing. USD+ works the same way for onchain dollars: it is the default redemption and settlement token across Dinari, and simply holding it earns yield on short-term US treasuries.

# How yield works

USD+ is a **daily rebasing** token. Yield is distributed by increasing every holder's balance directly in their wallet — the number of USD+ you hold grows over time while each USD+ remains redeemable for $1.

* **Automatic** — yield accrues to your wallet without staking, claiming, or any onchain action.
* **Rebasing** — your balance increases on a daily basis; you do not receive a separate reward token.
* **Backed by treasuries** — the dollars backing USD+ are invested in short-term US treasuries, and the interest those treasuries earn is what funds the rebase.

# Minting and redeeming

* **Mint** USD+ by depositing a supported stablecoin (USDC or USDT) of equivalent value.
* **Redeem** USD+ at any time for $1 each, paid in USDC. Redemptions settle in 0–3 days depending on size.

There are two ways to access USD+:

1. **App** — mint, hold, and redeem directly at [usd.dinari.com](https://usd.dinari.com/).
2. **Smart contract** — integrate USD+ programmatically using the Minter and Redeemer contracts. See the [USD+ token & contract addresses](https://docs.dinari.com/docs/usdplus-evm) and the [EVM integration guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide).

# Where USD+ is available

USD+ is deployed on multiple EVM chains, including Ethereum, Avalanche C-Chain, Base, Arbitrum, and Plume (with testnet deployments available for development). The token and contract addresses for each chain are listed in [Blockchain → EVM](https://docs.dinari.com/docs/usdplus-evm).

USD+ is also the default stablecoin across the Dinari [dShares™](https://docs.dinari.com/docs/what-is-dshare) platform — for example, dividends on tokenized equities are paid in USD+, so distributions begin earning yield the moment they land.

Updated about 1 month ago

---

[Deprecation Notices](https://docs.dinari.com/docs/deprecations)[Blockchain](https://docs.dinari.com/docs/blockchain-1)

Did this page help you?

Yes

No

Copy Page

* + [How yield works](https://docs.dinari.com/docs/what-is-usd)
  + [Minting and redeeming](https://docs.dinari.com/docs/what-is-usd)
  + [Where USD+ is available](https://docs.dinari.com/docs/what-is-usd)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"What is USD+?","dateModified":"2026-10-14T11:27:32.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/deploy-to-production>>>
---
url: https://docs.dinari.com/docs/deploy-to-production
title: Deploy to production
description: Once you've integrated with Dinari, follow this checklist to deploy to production: Complete KYB with Dinari Generate an API key in the production environment Update usages of API SDK to use above key and production endpoint Update usages of smart contracts to point to mainnet addresses
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

# Deploy to production

Once you've integrated with Dinari, follow this checklist to deploy to production:

* Complete KYB with Dinari
* Generate an API key in the production environment
* Update usages of API SDK to use above key and production endpoint
* Update usages of smart contracts to point to mainnet addresses

Updated about 1 month ago

---

[Quickstart](https://docs.dinari.com/docs/quickstart)[Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

Did this page help you?

Yes

No

Copy Page

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Deploy to production","dateModified":"2026-10-14T11:25:12.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/hosted-trading>>>
---
url: https://docs.dinari.com/docs/hosted-trading
title: Hosted Trading
description: Dinari offers a hosted trading interface for compatible web and mobile interfaces.
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

# Hosted Trading

Dinari offers a hosted trading interface for compatible web and mobile interfaces.

As an alternative to a standard API integration, Dinari offers a white-label and theme-able fully-hosted or self-hosted trading web UI that can be used in your mobile or web application.

  
  
  

# Features

* Fully-managed or self-hosted options available.
* Compatible with all major web-based wallet interfaces.
* Supports mobile webview-based wallet integrations including [Base](https://join.base.app/), [Coinbase Wallet](https://wallet.coinbase.com/), [Metamask](https://metamask.io/download) etc.
* Supports multiple blockchains
* Integrates directly with the Dinari Enterprise API for trading and market data functionality.
* Includes both the front-end and back-end services.
* [*optional*] Hosted KYC flows by our identity verification provider [Persona](https://withpersona.com/).

# Hosting Options

## Dinari Hosting

Trading interfaces may be fully-hosted by Dinari which offers whitelabel turnkey integration with existing web trading interfaces or mobile applications.

* Fully-managed and dedicated hosting infrastructure with 99.99% SLA uptime.
* Automated container-based updates, testing and green/blue deployment.
* Deployable in any major AWS region.
* Completely independent AWS account and runtime environment including private networking, database and capacity isolation.
* Utilizes industry best practices for secure deployment.
* Logs and readonly-access to AWS account is available.
* Additional restricted staging environments are available.

### Integration Instructions

1. Partner submits logo and color scheme.
2. Dinari builds and deploys an isolated instance of the trading interface to `[PARTNER_ID].dinari-hosted.com`.
3. Integrate a webview in your mobile app or redirect users to this site.

*Initial integration support for the hosted option is included.*

> ✅
>
> All Dinari-hosted trading interfaces are available as separate subdomains on the `dinari-hosted.com` domain ensuring isolation of cookies and other domain-specific data.

## Self-hosting

* Fully customizable with source-code and containerized versions available.
* Host on your own infrastructure with unlimited use and perpetual licensing without royalties.
* Can be hosted on a root domain or any subdomain.
* `Makefile`-based development, build and run scripts.
* Multi-arch containers available for both x86\_64 and ARMv8 architectures.
* Fully-automated DB migrations.
* Terraform provisioning code available upon request.

### Requirements

* Node.JS 24 runtime or general container runtime.
* PostgreSQL 16 database

Updated about 1 month ago

---

[Deploy to production](https://docs.dinari.com/docs/deploy-to-production)[What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)

Did this page help you?

Yes

No

Copy Page

* + [Features](https://docs.dinari.com/docs/hosted-trading)
  + [Hosting Options](https://docs.dinari.com/docs/hosted-trading)
  + - [Dinari Hosting](https://docs.dinari.com/docs/hosted-trading)
    - * [Integration Instructions](https://docs.dinari.com/docs/hosted-trading)
    - [Self-hosting](https://docs.dinari.com/docs/hosted-trading)
    - * [Requirements](https://docs.dinari.com/docs/hosted-trading)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Hosted Trading","dateModified":"2026-10-14T11:25:12.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/quickstart>>>
---
url: https://docs.dinari.com/docs/quickstart
title: Quickstart
description: Dinari is infrastructure for tokenized real-world assets. Our API lets you offer your users U.S. equities and a yield-bearing dollar, on-chain, without becoming a broker-dealer yourself. We handle the brokerage relationships, settlement, custody, and compliance layer underneath. Partners can sign up…
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

<<<PAGE https://docs.dinari.com/docs/faqs>>>
---
url: https://docs.dinari.com/docs/faqs
title: FAQs
description: Overview What is Dinari? Dinari provides infrastructure for trading traditional securities, like stocks and exchange-traded funds (ETFs), on the blockchain. It uses smart contracts (programs that run on a blockchain) to represent these securities as tokens, called dShares, and automates buying and s…
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

# FAQs

## Overview

**What is Dinari?**

Dinari provides infrastructure for trading traditional securities, like stocks and exchange-traded funds (ETFs), on the blockchain. It uses smart contracts (programs that run on a blockchain) to represent these securities as tokens, called dShares, and automates buying and selling them.

**What are dShares?**

dShares are tokenized representations of traditional equities that are backed 1:1 by the underlying securities. When you hold a dShare, you hold the same economic rights you would get by holding the underlying stock through a traditional broker, such as dividends and stock splits.

**Do I own the actual shares?**

No, Dinari holds the underlying stocks in custody through a third-party custodial broker. When you purchase a dShare, you receive a separate security. The corresponding shares back that security, but you are not a direct shareholder in the company.

**Are dShares physically backed?**

Yes, one real share in a custodial brokerage account backs each dShare in circulation. A third-party custodial broker holds the underlying assets. An independent Big Four accounting firm audits the reserves to confirm this 1:1 backing.

---

## **Getting Started: KYC & Wallets**

**How can I purchase dShares?**

Before you purchase dShares:

1. Set up a wallet compatible with the Ethereum Virtual Machine (EVM), the environment that runs Ethereum smart contracts.
2. Fund your wallet with enough supported stablecoin (a token designed to maintain a stable value) for your purchase.
3. Complete Know Your Customer (KYC), the identity verification process.

**What do I need for the KYC verification process?**

Prepare a government-issued identity document (like a driver's license or passport) and proof of residency (such as a current utility bill or bank statement).

**Can I purchase dShares without performing a KYC check?**

No, Dinari requires you to complete KYC verification before purchasing dShares.

**Which countries does Dinari support?**

Dinari offers dShares in over 85 jurisdictions outside the United States under Regulation S. Check Dinari's documentation for the list of unsupported countries.

**Can I connect an existing smart contract wallet?**

Yes, Dinari supports self-custody smart contract wallets (wallets you control through on-chain code) for proxied orders. Dinari identifies these as EIP-155 orders; EIP-155 uses chain IDs to protect transaction signatures from reuse on another chain.

Connect the wallet using its contract address and chain ID (the network identifier, such as `eip155:8453` for Base). Use ERC-1271, the standard for validating smart contract wallet signatures, when signing messages.

---

## **Trading & Orders**

**What order types are supported?**

Dinari supports two order types: **MARKET** and **LIMIT**. Dinari does not support stop, stop-limit, or trailing orders.

**Can I trade outside of U.S. market hours?**

Yes, Dinari operates across four distinct trading sessions, including extended, overnight, and weekend sessions. During extended, overnight, and weekend sessions, Dinari accepts only **limit orders** directly. It automatically converts market orders to marketable limit orders (limit orders priced to execute against available offers).

**How does settlement work?**

Settlement occurs on-chain in a single step once an order is filled. A buy mints dShares to your wallet, and a sell burns dShares and releases the proceeds. Partially settled orders are not possible.

**Does Dinari support short selling?**

No, native short selling of dShares is not supported. The only way to get short exposure is through tokenized inverse ETFs that Dinari supports.

**What is the maximum order size?**

There is no single fixed maximum order size. Precision limits and partner-configurable caps constrain order sizes. For example, the payment amount for a market buy supports 2 decimal places. Orders above $5,000 USD may take 1–2 days to execute.

---

## **Dividends & Corporate Actions**

**How are dividends paid?**

Dinari supports fully automated cash dividends. Dinari pays them in stablecoins (like USD+) directly to your wallet on the same schedule as the underlying stock.

**What corporate actions are supported?**

Dinari processes dividends, stock splits (forward and reverse), ticker changes, and mergers. Dinari automatically reflects these changes on the dShare token and your ledger.

**Do I need to do anything for a stock split?**

No, a stock split mirrors automatically on your dShare balance. For example, a 10-for-1 split means your 5 shares become 50, with the total value remaining unchanged.

---

## **Fees & Costs**

**How much does it cost to use Dinari?**

Fees vary by network. Issuance orders bear a fee of $1 plus 0.25% to 0.50% on Ethereum, or $0.20 plus 0.25% to 0.50% on Layer 2 (L2) networks, plus network fees. Layer 2 networks process transactions on top of a base blockchain.

**Can transaction fees be paid in stablecoins?**

Yes, Dinari allows transaction fees to be paid in stablecoins rather than ETH, improving the user experience.

---

## **Supported Assets & Networks**

**Which stocks are supported?**

Dinari supports over 724 tokenized U.S. stocks and ETFs, including all S&P 500 companies. A full list is available on the Dinari platform.

**Which blockchains are supported?**

Dinari supports Ethereum, Base, Arbitrum, Avalanche C-Chain, and Plume.

**Can dShares be bridged between chains?**

Yes, you can transfer dShares between supported blockchain networks using LayerZero V2, a protocol for sending messages between blockchains. The transfers use the Omnichain Fungible Token (OFT) standard, which maintains a unified token supply across networks.

---

## **Technical Integration (For Developers)**

**What is the order lifecycle?**

Every order moves through four stages: **Validation**, **Preparation**, **Execution**, and **Settlement**. A buy converts payment tokens into dShares, and a sell converts dShares back into payment tokens.

**How do I place an order via the API?**

You can place orders through three methods:

* **Managed Orders:** For Dinari-managed wallets.
* **Proxied Orders (EIP-155):** For self-custody wallets.
* **Direct smart contract calls:** Interact with the contracts directly.

**What is the difference between** `/permit` **and** `/permit_transaction`**?**

The `/permit` endpoint generates an EIP-2612 permit (a signed token-spending approval) for an **externally owned account (EOA)**, which you control with a private key.

The `/permit_transaction` endpoint prepares a transaction for **smart contract wallets** using ERC-1271 and Permit2. ERC-1271 validates smart contract wallet signatures. Permit2 is a contract system for signature-based token-spending permissions.

**What should I do if an order fails with a 423 error?**

A 423 error ("Account is currently in use") means a concurrent request is already being processed for that account. You should serialize your requests per account and implement a request queue.

**How should I handle a 404 "Account not found" error?**

This typically means you are using an account ID from a different environment (sandbox vs. production). Verify your client's `environment` setting matches where the account was created.

**Can I reuse a** `client_order_id` **after a failed order?**

No, a 409 conflict indicates that an existing order already uses the `client_order_id`. Generate a new, unique ID for each retry attempt.

Updated 4 days ago

---

[Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)[Status Pages](https://docs.dinari.com/docs/status-pages)

Did this page help you?

Yes

No

Copy Page

* + [Overview](https://docs.dinari.com/docs/faqs)
  + [Getting Started: KYC & Wallets](https://docs.dinari.com/docs/faqs)
  + [Trading & Orders](https://docs.dinari.com/docs/faqs)
  + [Dividends & Corporate Actions](https://docs.dinari.com/docs/faqs)
  + [Fees & Costs](https://docs.dinari.com/docs/faqs)
  + [Supported Assets & Networks](https://docs.dinari.com/docs/faqs)
  + [Technical Integration (For Developers)](https://docs.dinari.com/docs/faqs)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"FAQs","dateModified":"2026-11-12T18:23:06.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/status-pages>>>
---
url: https://docs.dinari.com/docs/status-pages
title: Status Pages
description: Dinari Status Page Managed by Dinari. Provides updates on platform availability, API incidents, and maintenance notices. Dinari Status When to check Before Placing Large or Time-Sensitive Orders If you are about to submit a high-value order or a batch of orders during market hours, check the status…
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

# Status Pages

## Dinari Status Page

Managed by Dinari. Provides updates on platform availability, API incidents, and maintenance notices.

[Dinari Status](https://status.dinari.com/)

---

## When to check

* **Before Placing Large or Time-Sensitive Orders**  
  If you are about to submit a high-value order or a batch of orders during market hours, check the status page first to confirm that ordering, market data, and settlement services are fully operational.

* **During Regular U.S. Market Hours (9:30 AM – 4:00 PM ET)**  
  Market data feeds (current\_price, current\_quote, WebSocket) are most active during regular trading hours. If you observe stale prices, missing OHLC candles, or delayed quotes, check here first to see whether a known data feed issue is already being tracked.
* **During Overnight and Weekend Sessions**  
  Dinari supports 24/7 trading through Flow Traders. Liquidity is lower outside regular hours, and only limit orders are accepted. If you see wide spreads, zero bid/ask values, or delayed fills, this may be expected session behavior rather than an incident. The status page will confirm whether any infrastructure issues are affecting overnight or weekend sessions.
* **When API Requests Return Unexpected Errors**  
  If you receive 5xx errors (500, 502, 503) or the 423 "Account in use" error on multiple requests, check the status page to see if a broader API incident is in progress before troubleshooting your own integration.
* **Before Scheduled Maintenance Windows**  
  Planned maintenance will be announced in advance. Check this page before maintenance windows to confirm the scope, affected components, and expected duration.
* **After Deploying to Production**  
  If you have recently deployed an integration change and observe degraded performance, check the status page to rule out a platform-side issue before rolling back your change.

Updated 10 days ago

---

[FAQs](https://docs.dinari.com/docs/faqs)

Did this page help you?

Yes

No

Copy Page

* + [Dinari Status Page](https://docs.dinari.com/docs/status-pages)
  + [When to check](https://docs.dinari.com/docs/status-pages)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Status Pages","dateModified":"2026-11-06T16:53:06.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/staying-safe-on-dinari>>>
---
url: https://docs.dinari.com/docs/staying-safe-on-dinari
title: Staying Safe on Dinari
description: At Dinari, the security of our users and the integrity of our platform are our highest priorities. As tokenized assets become more popular, malicious actors are increasingly attempting to impersonate legitimate financial platforms to defraud consumers. We have recently identified fake websites and a…
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

# Staying Safe on Dinari

At Dinari, the security of our users and the integrity of our platform are our highest priorities. As tokenized assets become more popular, malicious actors are increasingly attempting to impersonate legitimate financial platforms to defraud consumers.

We have recently identified fake websites and apps operating under names like "Dinari Pro" to trick users into sending funds. This guide will help you verify our official channels, understand how Dinari actually operates, and recognize the red flags of a scam so you can protect yourself.

---

### The Official Dinari Channels

To ensure you are interacting with the real Dinari, always verify the URL. Scammers often buy look-alike domains or use our brand name on social media to deceive you.

* Our Official Web App: [https://app.dinari.com](https://app.dinari.com/)
* Our Official Corporate Website: [https://dinari.com](https://dinari.com/)
* Official Support Email: [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection)

⚠️**Warning:** We do not have a product called "Dinari Pro." Any website, app, or social media account using the name "Dinari Pro" is a malicious fake.

---

### **What Dinari Actually Offers (And What We Don't)**

Understanding our core business model is the easiest way to spot a fake platform.

**What we DO offer:**

* **Tokenized Stocks (dShares):** We allow users to buy tokenized representations of traditional U.S. stocks and ETFs (like Apple, Tesla, or the S&P 500).
* **1:1 Backing:** Every dShare is fully backed by a real share held in a regulated U.S. brokerage account.
* **Stablecoin Payments:** To purchase dShares, you must use supported stablecoins (like USDC) on specific blockchain networks (like Arbitrum or Base).

**What we DO NOT offer:**

* **We do NOT accept ETH, BTC, or other coins for direct deposits.** If a platform claiming to be Dinari asks you to send Ethereum (ETH) or other coins to a wallet address to fund your account, it is a scam.
* **We do NOT solicit users via dating apps, WhatsApp, Telegram, or text message.** We will never initiate a romantic relationship or unsolicited investment advice.
* **We do NOT require you to pay "taxes" or "unlock fees" to withdraw your funds.** Taxes are your personal responsibility to your local government; Dinari does not collect taxes on their behalf as a condition for withdrawal.

---

### Common Scam Tactics (The "Pig Butchering" Playbook)

Scammers use sophisticated psychological tactics to build trust before stealing your money. Watch out for these common patterns:

* **The "Romance" Hook:** The scam often begins on a dating app or social media. The scammer builds a fake relationship with you over weeks before introducing a "can't-miss" investment opportunity.
* **The Fake Routing App:** Scammers may tell you to use a legitimate third-party app (like the "Ult" app or a specific crypto exchange) to route your funds. They claim this provides "added security," but it is simply a way to bypass your bank's fraud warnings and get your money into a self-custodial wallet they control.
* **Fake Trading Dashboards:** Once you deposit funds into their fake platform, they will show you a dashboard with fake balances and huge "profits."
* **The Withdrawal Lock:** When you try to withdraw your money, the platform will suddenly freeze your account. They will demand you pay "taxes," "gas fees," or "penalty fees" to unlock your funds. Once you pay, they will disappear.

---

### 🚨**Red Flags: How to Spot a Scam**

If you encounter any of the following, you are likely dealing with a scam:

* **Unsolicited contact:** Someone you don't know messages you about an investment opportunity.
* **Guaranteed returns:** Promises of high profits with zero risk.
* **Pressure to act fast:** Scammers will tell you the "opportunity is closing" to prevent you from doing research.
* **Depositing to arbitrary wallets:** You are asked to send crypto directly to a random string of characters, rather than interacting with a verified smart contract or KYC-verified platform.
* **Requests for "Tax" payments:** They tell you that you must pay a tax or fee before you can withdraw your own money.

---

### What to Do If You Are a Victim

If you believe you have been targeted by a scam impersonating Dinari, act immediately:

* **Stop All Contact:** Cut off all communication with the scammer and the fake platform.
* **Contact Your Bank and Exchanges:** Immediately contact the bank or crypto exchange (e.g., Coinbase, Crypto.com) you used to transfer funds. Report the transactions as fraudulent and provide the receiving wallet addresses.
* **Report to Authorities:** File a report with your local law enforcement and the relevant cybercrime authority in your country.
  + **United States:** File a report with the FBI's Internet Crime Complaint Center (IC3) at ic3.gov.
* **Secure Your Devices:** If you downloaded an app or software at the direction of the scammer, delete it immediately and run an antivirus scan on your device.

---

### How to Report a Fake Site to Us

If you find a fake website, social media profile, or app impersonating Dinari, please report it to us so we can take legal and technical action (such as issuing takedown requests).

* **Report to Dinari:** Email [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection) with the subject line "Security Report: Impersonation". Include the URL, screenshots, your wallet address, your transaction hash, and any relevant details.
* **Report to Google:** Use Google Safe Browsing to report phishing sites (safebrowsing.google.com/safebrowsing/report\_phish/).
* **Report to the Host:** Use a WHOIS lookup to find the hosting provider of the fake site and send an abuse report to them.

**When in doubt, verify before you send.** Always ensure you are on **dinari.com** or **app.dinari.com,** and never send funds based on a link sent to you via a messaging app.

Updated 20 days ago

---

[Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)[FAQs](https://docs.dinari.com/docs/faqs)

Did this page help you?

Yes

No

Copy Page

* + [The Official Dinari Channels](https://docs.dinari.com/docs/staying-safe-on-dinari)
  + [What Dinari Actually Offers (And What We Don't)](https://docs.dinari.com/docs/staying-safe-on-dinari)
  + [Common Scam Tactics (The "Pig Butchering" Playbook)](https://docs.dinari.com/docs/staying-safe-on-dinari)
  + [🚨Red Flags: How to Spot a Scam](https://docs.dinari.com/docs/staying-safe-on-dinari)
  + [What to Do If You Are a Victim](https://docs.dinari.com/docs/staying-safe-on-dinari)
  + [How to Report a Fake Site to Us](https://docs.dinari.com/docs/staying-safe-on-dinari)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Staying Safe on Dinari","dateModified":"2026-10-27T02:58:35.000Z"}
```