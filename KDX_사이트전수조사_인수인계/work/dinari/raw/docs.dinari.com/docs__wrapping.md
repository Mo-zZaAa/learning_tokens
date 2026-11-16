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