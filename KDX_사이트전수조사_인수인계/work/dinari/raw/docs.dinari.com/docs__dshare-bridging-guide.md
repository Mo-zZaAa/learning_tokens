---
url: https://docs.dinari.com/docs/dshare-bridging-guide
title: dShare Bridging Guide
description: dShare Token Bridging Guide This guide explains how to bridge DShare tokens between supported blockchain networks using LayerZero V2 and the Omnichain Fungible Token (OFT) standard. Overview DShare tokens are cross-chain compatible using LayerZero V2. When you bridge tokens: Tokens are burned on the…
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

# dShare Bridging Guide

# dShare Token Bridging Guide

This guide explains how to bridge **DShare** tokens between supported blockchain networks using **LayerZero V2** and the **Omnichain Fungible Token (OFT)** standard.

# Overview

DShare tokens are cross-chain compatible using LayerZero V2. When you bridge tokens:

* Tokens are **burned** on the source chain
* Equivalent tokens are **minted** on the destination chain
* Typical transfer time is **~1 minutes**, depending on a variety of factors on the source and target chain.

---

## Prerequisites

Before bridging, ensure you have:

1. **DShare tokens** in your wallet on the **source chain**
2. **Native gas tokens** for fees:
   * **ETH** on Ethereum / Arbitrum / Base / Blast

---

## Supported Networks

### Mainnet

| Chain | LayerZero Endpoint ID (`dstEid`) |
| --- | --- |
| Ethereum | 30101 (as of 02/23 Ethereum is not supported as a destination, for most dShare) |
| Arbitrum | 30110 |
| Base | 30184 |
| Blast | 30243 |
| Plume | 30161 |

### Testnet

| Chain | LayerZero Endpoint ID (`dstEid`) |
| --- | --- |
| Sepolia | 40161 |
| Arbitrum Sepolia | 40231 |
| Base Sepolia | 40245 |
| Blast Sepolia | 40243 |
| DFN Paper | 40412 |

---

## Step-by-Step Bridging Process

The core interaction that starts a bridge, is interacting with the `send()` function on the dShare token contract. This involves populating a `sendParam` as an input, that is used to quote the bridge fee and then reused to call the send function.

sol

```
   function send(
        SendParam calldata _sendParam,
        MessagingFee calldata _fee,
        address _refundAddress
    ) external payable virtual returns (MessagingReceipt memory msgReceipt, OFTReceipt memory oftReceipt)
```

### Step 1: Estimate Bridging Fees (`quoteSend`)

Before sending, get a quote for the LayerZero messaging fees by calling `quoteSend()` on the dShare contract.

Solidity

```
// Parameters for quoteSend
SendParam memory sendParam = SendParam({
    dstEid: 30110,                                    // Destination chain EID (e.g., Arbitrum)
    to: bytes32(uint256(uint160(recipientAddress))),  // Recipient address as bytes32
    amountLD: 100 * 10**18,                           // Amount to send (18 decimals)
    minAmountLD: 99 * 10**18,                         // Minimum amount (slippage protection)
    extraOptions: "0x00030100110100000000000000000000000000030d40",  //Dinari internal default values (200k gas)
    composeMsg: "",                                   // Composed message (can be empty)
    oftCmd: ""                                        // OFT command (can be empty)
});

// Get the fee quote
MessagingFee memory fee = dshare.quoteSend(sendParam, false);
// fee.nativeFee = amount of native gas needed
// fee.lzTokenFee = amount of LZ token needed (usually 0)
```

---

### Step 2: Prepare the Bridge Transaction (`SendParam` + `MessagingFee`)

Construct the send parameters and the fee struct (using the values from `quoteSend`):

Solidity

```
SendParam memory sendParam = SendParam({
    dstEid: 30110,                                    // Destination LayerZero Endpoint ID
    to: bytes32(uint256(uint160(recipientAddress))),  // Recipient on destination chain
    amountLD: 100 * 10**18,                           // Amount to bridge (18 decimals)
    minAmountLD: 99 * 10**18,                         // Min amount after rounding/slippage
    extraOptions: "0x00030100110100000000000000000000000000030d40",  //Dinari internal default values (200k gas)
    composeMsg: "",                                   // Leave empty
    oftCmd: ""                                        // Leave empty
});

MessagingFee memory fee = MessagingFee({
    nativeFee: quotedNativeFee,                       // From quoteSend()
    lzTokenFee: 0                                     // Usually 0
});
```

---

### Step 3: Execute the Bridge (`send`)

Call the `send()` function on the DShare contract. **You must include `fee.nativeFee` as `msg.value`.**

Solidity

```
// Send tokens cross-chain
(MessagingReceipt memory receipt, OFTReceipt memory oftReceipt) = dshare.send{value: fee.nativeFee}(
    sendParam,
    fee,
    msg.sender  // Refund address for excess fees
);
```

**Important:** The LayerZero native fee must be sent as `msg.value` or your transaction will revert.

---

### Step 4: Wait for Confirmation

After submitting:

1. Wait for the **source chain** transaction to confirm
2. LayerZero relayers will process the cross-chain message
3. Tokens will be minted on the destination chain (usually **1–5 minutes**)

Track the message using LayerZero Scan (use your transaction hash):

* [https://layerzeroscan.com](https://layerzeroscan.com/)

---

## End-to-End Example (Using Ethers.js)

JSX

```
const { ethers } = require("ethers");

// Connect to provider and wallet
const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// DShare contract interface
const dshareAbi = [
  "function quoteSend((uint32,bytes32,uint256,uint256,bytes,bytes,bytes), bool) view returns ((uint256,uint256))",
  "function send((uint32,bytes32,uint256,uint256,bytes,bytes,bytes), (uint256,uint256), address) payable returns ((bytes32,uint64,(uint256,uint256)), (uint256,uint256))"
];

const dshare = new ethers.Contract(DSHARE_ADDRESS, dshareAbi, wallet);

async function bridgeTokens(destinationEid, recipientAddress, amount) {
  // Convert recipient address to bytes32
  const recipientBytes32 = ethers.utils.hexZeroPad(recipientAddress, 32);

  // Prepare send parameters
  const sendParam = {
    dstEid: destinationEid,
    to: recipientBytes32,
    amountLD: ethers.utils.parseEther(amount.toString()),
    minAmountLD: ethers.utils.parseEther((amount).toString()), 
    extraOptions: "0x00030100110100000000000000000000000000030d40",  //At dinari we use a 200k gas value on the recipient chain, a rough approximation of what is required.
    composeMsg: "0x", //You can use this to include extra data, like correlation ids - if desired.
    oftCmd: "0x"
  };

  // Get fee quote
  const [nativeFee, lzTokenFee] = await dshare.quoteSend(sendParam, false);
  console.log("Estimated native fee:", ethers.utils.formatEther(nativeFee));

  // Execute bridge
  const tx = await dshare.send(
    sendParam,
    { nativeFee, lzTokenFee },
    wallet.address,
    { value: nativeFee }
  );

  console.log("Transaction submitted:", tx.hash);
  await tx.wait();
  console.log("Bridge initiated! Track at: https://layerzeroscan.com/tx/" + tx.hash);
}

// Example: Bridge 100 tokens to Arbitrum
bridgeTokens(30110, "0xYourAddressHere", 100);
```

---

## Important Notes

### Fees

* **Native gas fee** is required for LayerZero messaging (paid in ETH or the chain’s native token)
* **No protocol fee**: DShare does not charge extra bridging fees
* Excess fees are refunded to the refund address provided in `send()`

### Token Decimals

* DShare uses **18 local decimals**
* Cross-chain transfers use 6 **shared decimals**
* Minor rounding differences (“dust”) can occur, leaving a small amount on the original wallet and chain.

  ```
  **Example:** You want to bridge `1.123456789012345678` tokens (18 decimals, 1.123456789012345678 * 10^18 in wei):
    - Only `1.123456` (6 decimals) can be represented cross-chain
    - `0.000000078912345678` remains in your source wallet as dust
  ```

### Paused State

* Bridging is disabled when the token is paused
* Check `paused()` before bridging
* Tokens may be paused during events like stock splits

### Address Format (`bytes32`)

* Destination address must be passed as `bytes32`
* Solidity conversion pattern:
  + `bytes32(uint256(uint160(address)))`

---

## Troubleshooting

### `NoPeer`

*Revert Code:* **`0xf6ff4fb7`**

Destination chain is not configured. Contact the Dinari team or verify the peer is set for the destination EID.

### `EnforcedPause`

*Revert Code:* **`0xd93c0665`**

Token is paused (often for operational events like stock splits). Try again at a later time after bridging is unpaused.

### Tokens not arriving

1. Confirm the source transaction succeeded
2. Search your transaction hash on LayerZero Scan for message status.
3. During heavy congestion, delivery can take **up to ~15 minutes**
4. If stuck, LayerZero supports retry mechanisms (see LayerZero Scan / docs)

   1. You can retry the delivery of a bridge by calling the `lzReceive` function on the destination dShare.

   sol

   ```
   function lzReceive(
               Origin calldata _origin,      // Source chain info
               address _receiver,            // Destination DShare contract address
               bytes32 _guid,                // Unique message identifier (from LayerZero Scan)
               bytes calldata _message,      // Encoded message (from LayerZero Scan)
               bytes calldata _extraData     // Additional data (usually empty)
      ) external payable;
   ```

     

   sol

   ```
   **Origin Struct:**

   struct Origin {
       uint32 srcEid;    // Source chain LayerZero Endpoint ID
       bytes32 sender;   // Source DShare contract address (as bytes32)
       uint64 nonce;     // Message nonce (from LayerZero Scan)
   }
   ```

   **Manual Recovery Script (ethers.js):**

   JavaScript

   ```
   const { ethers } = require("ethers");

   /**
    * Manually retry a stuck cross-chain transfer
    * Get the required values from LayerZero Scan for your stuck transaction
    */
   async function retryStuckTransfer(
       destinationRpcUrl,
       privateKey,
       // Values from LayerZero Scan
       lzEndpointAddress,      // LayerZero endpoint on destination chain
       dshareAddress,          // DShare contract on destination chain
       srcEid,                 // Source chain endpoint ID (e.g., 30101 for Ethereum)
       senderAddress,          // Source DShare contract address
       nonce,                  // Message nonce from LayerZero Scan
       guid,                   // Message GUID from LayerZero Scan
       message                 // Message payload from LayerZero Scan
   ) {
       const provider = new ethers.providers.JsonRpcProvider(destinationRpcUrl);
       const wallet = new ethers.Wallet(privateKey, provider);

       // LayerZero Endpoint V2 ABI
       const endpointAbi = [
           "function lzReceive((uint32 srcEid, bytes32 sender, uint64 nonce) origin, address receiver, bytes32 guid, bytes message, bytes extraData) external payable"
       ];

       const endpoint = new ethers.Contract(lzEndpointAddress, endpointAbi, wallet);

       // Construct origin from LayerZero Scan data
       const origin = {
           srcEid: srcEid,
           sender: ethers.utils.hexZeroPad(senderAddress, 32),
           nonce: nonce
       };

       console.log("Retrying stuck transfer...");
       console.log("  GUID:", guid);
       console.log("  Source EID:", srcEid);
       console.log("  Nonce:", nonce);

       // Call lzReceive on the endpoint to deliver the message
       const tx = await endpoint.lzReceive(
           origin,
           dshareAddress,
           guid,
           message,
           "0x",  // extraData - usually empty
           { gasLimit: 500000 }  // Set appropriate gas limit
       );

       console.log("Transaction submitted:", tx.hash);
       const receipt = await tx.wait();
       console.log("Transaction confirmed! Tokens should now be in your wallet.");
       return receipt;
   }

   // Example usage with values from LayerZero Scan:
   /*
   retryStuckTransfer(
       "https://arb-mainnet.g.alchemy.com/v2/YOUR_KEY",  // Destination RPC
       "0xYOUR_PRIVATE_KEY",
       "0x1a44076050125825900e736c501f859c50fE728c",     // Arbitrum LZ Endpoint
       "0xDShareContractOnArbitrum",                      // Destination DShare
       30101,                                             // Source: Ethereum
       "0xDShareContractOnEthereum",                      // Source DShare
       42,                                                // Nonce from LZ Scan
       "0xabcd1234...",                                   // GUID from LZ Scan
       "0x..."                                            // Message from LZ Scan
   );
   */
   ```

   How to get these variables from layerZero (manually)

   1. Go to [https://layerzeroscan.com](https://layerzeroscan.com/)
   2. Search for your source transaction hash
   3. Click on the message to see details
   4. Find these values:
      * **GUID**: The unique message identifier
      * **Source EID**: The source chain's LayerZero endpoint ID
      * **Nonce**: The message sequence number
      * **Payload/Message**: The encoded message data (may need to decode from the "Message" field)

   **Important Notes:**

   * You need native gas tokens on the destination chain to pay for the retry transaction
   * The message must already be verified (check status on LayerZero Scan)
   * If the message hasn't been verified yet, wait for confirmations
   * Contact Dinari support if manual recovery failss

## Security Considerations

1. **Verify contract addresses** (only interact with official dShare tokens)
2. **Test with a small amount first**
3. **Double-check the destination address**

---

## Getting Help

* **Dinari Support:** Contact Dinari for bridging issues
* **LayerZero Scan:** [https://layerzeroscan.com](https://layerzeroscan.com/)
* **LayerZero V2 Documentation:** [LayerZero V2 OFT Quickstart | LayerZero](https://docs.layerzero.network/v2/developers/evm/oft/quickstart)

---

*Last updated: January 2026*

Updated about 1 month ago

---

[Hyperliquid](https://docs.dinari.com/docs/hyperliquid)[Deprecation Notices](https://docs.dinari.com/docs/deprecations)

Did this page help you?

Yes

No

Copy Page

* + [dShare Token Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
  + [Overview](https://docs.dinari.com/docs/dshare-bridging-guide)
  + - [Prerequisites](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Supported Networks](https://docs.dinari.com/docs/dshare-bridging-guide)
    - * [Mainnet](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Testnet](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Step-by-Step Bridging Process](https://docs.dinari.com/docs/dshare-bridging-guide)
    - * [Step 1: Estimate Bridging Fees (quoteSend)](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Step 2: Prepare the Bridge Transaction (SendParam + MessagingFee)](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Step 3: Execute the Bridge (send)](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Step 4: Wait for Confirmation](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [End-to-End Example (Using Ethers.js)](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Important Notes](https://docs.dinari.com/docs/dshare-bridging-guide)
    - * [Fees](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Token Decimals](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Paused State](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Address Format (bytes32)](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Troubleshooting](https://docs.dinari.com/docs/dshare-bridging-guide)
    - * [NoPeer](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [EnforcedPause](https://docs.dinari.com/docs/dshare-bridging-guide)
      * [Tokens not arriving](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Security Considerations](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Getting Help](https://docs.dinari.com/docs/dshare-bridging-guide)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"dShare Bridging Guide","dateModified":"2026-10-14T11:27:27.000Z"}
```