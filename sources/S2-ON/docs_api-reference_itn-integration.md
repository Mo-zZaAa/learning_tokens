> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ondo.finance/llms.txt
> Use this file to discover all available pages before exploring further.

# ITN Integration

> Integrate Alpaca's Instant Tokenization Network with Ondo Stocks on Ethereum and BNB Chain.

Alpaca's Instant Tokenization Network (ITN) allows authorized participants to convert supported underlying securities into Ondo Stocks and redeem Ondo Stocks for the underlying securities.

For the complete ITN workflow and API details, see Alpaca's [Tokenization Guide for Authorized Participants](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant).

## Choose an environment

> [tab] Production
>
> Production connects Ondo's production environment with Alpaca's live environment.
>
> | Service | Base URL |
> | :- | :- |
> | Ondo Global Markets | `https://api.gm.ondo.finance` |
> | Alpaca Broker API | `https://broker-api.alpaca.markets` |
>
> > [!WARNING]
> >
> > Production ITN transactions involve assets with real value. On-chain transactions are irreversible and require ETH or BNB for gas.

> [tab] Staging
>
> Staging connects Ondo's staging environment with Alpaca's sandbox.
>
> | Service | Base URL |
> | :- | :- |
> | Ondo Global Markets | `https://api.gm-staging.ondo.finance` |
> | Alpaca Broker API | `https://broker-api.sandbox.alpaca.markets` |
>
> > [!WARNING]
> >
> > Staging contracts are deployed on Ethereum and BNB Chain mainnet. Tokens minted through the sandbox flow have no monetary value, but on-chain transactions require real ETH or BNB for gas.

## Prerequisites

Complete these steps before submitting an ITN request:

> [!WARNING]
>
> When signing up for an Alpaca account and an Ondo account, you must use the **same email address**. The handshake process will fail to complete if there is a mismatch.

1. Complete onboarding with Alpaca for a [BrokerAPI account](https://docs.alpaca.markets/us/docs/getting-started-with-broker-api#1-create-an-account). Contact Ondo for an introduction to the Alpaca team, or coordinate directly with Alpaca if you already have a relationship. A TradingAPI account alone does not currently meet ITN onboarding requirements. Use an Alpaca sandbox account for staging and a live Alpaca account for production.
2. Complete the [Ondo Stocks onboarding and KYC process](https://docs.ondo.finance/ondo-stocks/onboarding-and-kyc.md) to establish your Ondo account. **Use the same email address as your Alpaca account**.
3. Request access to the Ondo API and obtain an API key for your selected environment.
4. Confirm that your Alpaca and Ondo accounts use the same email address before requesting the handshake. Provide the Alpaca team with this shared email address and your corresponding **Alpaca account number**. The account number is different from the Alpaca account ID used in API paths.
5. Wait for Alpaca to coordinate with Ondo regarding the linking of your accounts.
6. Provide the Ondo team with the wallet address that you plan to use for ITN requests.
7. Wait for Ondo to enable ITN access for the wallet(s) you provided.

> [!NOTE]
>
> Mint requests will fail if the Alpaca and Ondo accounts are not linked or if the destination wallet has not been enabled for ITN.

## Supported assets

ITN supports the assets below on Ethereum and BNB Chain. Use the stock ticker when submitting an Alpaca request.

> [tab] Production
>
> | Ondo token symbol | Stock ticker |
> | :- | :- |
> | `AAPLon` | `AAPL` |
> | `AMDon` | `AMD` |
> | `AMZNon` | `AMZN` |
> | `ARMon` | `ARM` |
> | `ASMLon` | `ASML` |
> | `AVGOon` | `AVGO` |
> | `COINon` | `COIN` |
> | `CRCLon` | `CRCL` |
> | `CRWVon` | `CRWV` |
> | `DRAMon` | `DRAM` |
> | `FUTUon` | `FUTU` |
> | `GLWon` | `GLW` |
> | `GMEon` | `GME` |
> | `GOOGLon` | `GOOGL` |
> | `HOODon` | `HOOD` |
> | `INTCon` | `INTC` |
> | `LLYon` | `LLY` |
> | `METAon` | `META` |
> | `MRVLon` | `MRVL` |
> | `MSFTon` | `MSFT` |
> | `MSTRon` | `MSTR` |
> | `MUon` | `MU` |
> | `NFLXon` | `NFLX` |
> | `NVDAon` | `NVDA` |
> | `ORCLon` | `ORCL` |
> | `OXYon` | `OXY` |
> | `PDDon` | `PDD` |
> | `PLTRon` | `PLTR` |
> | `PYPLon` | `PYPL` |
> | `QCOMon` | `QCOM` |
> | `QQQon` | `QQQ` |
> | `RDDTon` | `RDDT` |
> | `SKHYon` | `SKHY` |
> | `SLVon` | `SLV` |
> | `SNDKon` | `SNDK` |
> | `SOFIon` | `SOFI` |
> | `SPCXon` | `SPCX` |
> | `SPYon` | `SPY` |
> | `STRCon` | `STRC` |
> | `TQQQon` | `TQQQ` |
> | `TSLAon` | `TSLA` |
> | `TSMon` | `TSM` |

> [tab] Staging
>
> | Ondo token symbol | Stock ticker |
> | :- | :- |
> | `AAPLon` | `AAPL` |
> | `AMZNon` | `AMZN` |
> | `MSFTon` | `MSFT` |
> | `NVDAon` | `NVDA` |
> | `TSLAon` | `TSLA` |

## Rate limits

The following USD notional limits apply independently to mint and redemption requests during each [market session](https://docs.ondo.finance/ondo-stocks/market-hours-and-trading-availability.md). Each request must meet the minimum per request, and the combined value of your requests must not exceed the maximum total per account for that session.

> [tab] Production
>
> | Market session | Minimum per request | Maximum total per account |
> | :- | -: | -: |
> | Pre-market | \$1,000 | \$1,000,000 |
> | Regular | \$1,000 | \$5,000,000 |
> | Post-market | \$1,000 | \$1,000,000 |
> | Overnight | \$1,000 | \$1,000,000 |
> | Off-hours | \$1,000 | \$500,000 |

> [tab] Staging
>
> | Market session | Minimum per request | Maximum total per account |
> | :- | -: | -: |
> | Pre-market | \$1 | \$500,000 |
> | Regular | \$1 | \$1,000,000 |
> | Post-market | \$1 | \$500,000 |
> | Overnight | \$1 | \$250,000 |
> | Off-hours | \$1 | \$100,000 |

> [!NOTE]
>
> Additional system-wide and asset-level limits apply. During periods of high traffic, these limits may prevent a mint from being accepted or delay a redemption until capacity becomes available.

To see your current limits and remaining capacity for an asset on each network, use [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset.md).

## Fees

Ondo charges a fee for minting and redeeming assets. See the table below for each direction's fee in basis points.

> [tab] Production
>
> | Direction | Fee |
> | :- | -: |
> | Mint | 0 bps (0%) |
> | Redeem | 5 bps (0.05%) |

> [tab] Staging
>
> | Direction | Fee |
> | :- | -: |
> | Mint | 0 bps (0%) |
> | Redeem | 5 bps (0.05%) |

> [!NOTE]
>
> Alpaca may charge its own fees for mint and redemption requests. The response from Alpaca's [List Tokenization Requests endpoint](#check-request-status) includes any fees associated with each request. See Alpaca's [Tokenization Guide for Authorized Participants](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant) for its current fee schedule.

## Check asset availability

Before minting or redeeming, use the ITN endpoints to check availability and limits.

* [List ITN Assets](https://docs.ondo.finance/api-reference/itn/list-itn-assets.md) returns each ITN asset with its networks, token addresses, and fees.
* [Get ITN Status](https://docs.ondo.finance/api-reference/itn/get-itn-status.md) reports whether minting and redeeming are open, globally and for each asset on each network.
* [Get ITN Limits for an Asset](https://docs.ondo.finance/api-reference/itn/get-itn-limits-for-an-asset.md) returns your session limits and how much you can still mint and redeem on each network.

> [tab] Production
>
> ```bash theme={null}
> curl --request GET \
>   "https://api.gm.ondo.finance/v1/itn/status" \
>   --header "x-api-key: ${GM_API_KEY}"
>
> curl --request GET \
>   "https://api.gm.ondo.finance/v1/itn/assets/AAPLon/limits" \
>   --header "x-api-key: ${GM_API_KEY}"
> ```

> [tab] Staging
>
> ```bash theme={null}
> curl --request GET \
>   "https://api.gm-staging.ondo.finance/v1/itn/status" \
>   --header "x-api-key: ${GM_API_KEY}"
>
> curl --request GET \
>   "https://api.gm-staging.ondo.finance/v1/itn/assets/AAPLon/limits" \
>   --header "x-api-key: ${GM_API_KEY}"
> ```

Ondo does not continue redemption settlement while a relevant `MARKET_PAUSED`, `PAUSED_GM_CHAIN`, or `ASSET_PAUSED` status is active. `ASSET_LIMITED` does not pause ITN. If no pause is reported and a request remains pending, contact [support@ondo.finance](mailto:support@ondo.finance).

## Mint Ondo Stocks

To mint Ondo Stocks, submit a request through [Alpaca's Mint Request endpoint](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant#alpacas-mint-request). Set `issuer` to `ondo`. The only supported `network` values are `ethereum` for Ethereum and `binance` for BNB Chain.

> [tab] Production
>
> ```bash theme={null}
> curl --request POST \
>   "https://broker-api.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/mint" \
>   --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}" \
>   --header "Content-Type: application/json" \
>   --data '{
>     "underlying_symbol": "AAPL",
>     "qty": "1",
>     "issuer": "ondo",
>     "network": "ethereum",
>     "wallet_address": "0xYOUR_ENABLED_WALLET"
>   }'
> ```
>
> Use your live Alpaca credentials for production ITN requests.

> [tab] Staging
>
> ```bash theme={null}
> curl --request POST \
>   "https://broker-api.sandbox.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/mint" \
>   --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}" \
>   --header "Content-Type: application/json" \
>   --data '{
>     "underlying_symbol": "AAPL",
>     "qty": "1",
>     "issuer": "ondo",
>     "network": "ethereum",
>     "wallet_address": "0xYOUR_ENABLED_WALLET"
>   }'
> ```
>
> Use your Alpaca sandbox credentials for staging ITN requests.

The `qty` field is the number of underlying shares to tokenize and may contain up to nine decimal places. Ondo calculates the corresponding Ondo Stock token amount and delivers it to the enabled wallet after the underlying shares settle.

To mint on BNB Chain, change `network` to `binance`.

## Check request status

Use Alpaca's [List Tokenization Requests endpoint](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant#list-tokenization-requests) to monitor your mint and redemption requests:

> [tab] Production
>
> ```bash theme={null}
> curl \
>   "https://broker-api.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/requests" \
>   --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}"
> ```

> [tab] Staging
>
> ```bash theme={null}
> curl \
>   "https://broker-api.sandbox.alpaca.markets/v1/accounts/${ALPACA_ACCOUNT_ID}/tokenization/requests" \
>   --user "${ALPACA_BROKER_KEY}:${ALPACA_BROKER_SECRET}"
> ```

Each request has a `status` of `pending`, `completed`, or `rejected`. The response also includes identifiers, quantities, network information, transaction hashes, and any fees associated with the requests.

## Redeem Ondo Stocks

Redemptions begin on-chain. From the wallet enabled during onboarding, first approve the ITN issuer contract to spend the Ondo Stocks you want to redeem. Then call `redeem(address,uint256)` on the issuer contract. A successful redemption burns the tokens. Ondo detects the burn and works with Alpaca to transfer the corresponding underlying shares to your linked Alpaca account. See Alpaca's [Redeem Workflow](https://docs.alpaca.markets/us/docs/tokenization-guide-for-authorized-participant#redeem-workflow) for more information.

### Find the token contract address

Use [Get Contract Addresses for an Asset](https://docs.ondo.finance/api-reference/assets/get-contract-addresses-for-an-asset.md) with the Ondo Stock symbol:

> [tab] Production
>
> ```bash theme={null}
> curl --request GET \
>   "https://api.gm.ondo.finance/v1/assets/${TOKEN_SYMBOL}/addresses" \
>   --header "x-api-key: ${GM_API_KEY}"
> ```

> [tab] Staging
>
> ```bash theme={null}
> curl --request GET \
>   "https://api.gm-staging.ondo.finance/v1/assets/${TOKEN_SYMBOL}/addresses" \
>   --header "x-api-key: ${GM_API_KEY}"
> ```

Select the address whose `networkChainId` is `ethereum-1` or `bsc-56`. Use the returned `decimals` value when converting a human-readable token amount into the integer passed to the contract.

### Submit the redemption

The flow is the same on Ethereum and BNB Chain. Use an RPC endpoint for your selected network and the corresponding ITN issuer contract:

> [tab] Production
>
> | Network | ITN issuer contract |
> | :- | :- |
> | Ethereum | [`0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E`](https://etherscan.io/address/0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E) |
> | BNB Chain | [`0x341f9e6463161f0c90037cbc0150dc54e6d1e06e`](https://bscscan.com/address/0x341f9e6463161f0c90037cbc0150dc54e6d1e06e) |

> [tab] Staging
>
> | Network | ITN issuer contract |
> | :- | :- |
> | Ethereum | [`0x46c65333cea9a3c6357c4f075e9f67aaef0639df`](https://etherscan.io/address/0x46c65333cea9a3c6357c4f075e9f67aaef0639df) |
> | BNB Chain | [`0x194e4db0a165c4108db08534564196d915eadcf3`](https://bscscan.com/address/0x194e4db0a165c4108db08534564196d915eadcf3) |
>
> > [!WARNING]
> >
> > These contracts are deployed on mainnet even though staging uses Alpaca's sandbox. The tokens have no monetary value, but transactions require real ETH or BNB for gas.

The approval and redemption transactions must both be sent from the wallet that Ondo enabled for ITN.

The example below uses Foundry's [`cast`](https://getfoundry.sh/cast/overview) command. Ondo Stocks use 18 decimal places, so convert the human-readable token amount before submitting it. This amount represents the Ondo Stocks being redeemed, not the number of underlying shares.

```bash theme={null}
TOKEN_ADDRESS="0xTOKEN_ADDRESS"
ISSUER_ADDRESS="0xITN_ISSUER_ADDRESS"
TOKEN_AMOUNT="1.5"
AMOUNT_WEI="$(cast to-wei "${TOKEN_AMOUNT}")"
RPC_URL="https://YOUR_NETWORK_RPC_URL"

# Approve the ITN issuer contract to spend the tokens being redeemed.
cast send "${TOKEN_ADDRESS}" \
  "approve(address,uint256)" "${ISSUER_ADDRESS}" "${AMOUNT_WEI}" \
  --rpc-url "${RPC_URL}" \
  --private-key "${PRIVATE_KEY}"

# Transfer and burn the tokens to begin settlement through Alpaca.
cast send "${ISSUER_ADDRESS}" \
  "redeem(address,uint256)" "${TOKEN_ADDRESS}" "${AMOUNT_WEI}" \
  --rpc-url "${RPC_URL}" \
  --private-key "${PRIVATE_KEY}"
```

After the redemption transaction is confirmed, use the [request status endpoint](#check-request-status) to follow settlement. It may take time for a newly observed redemption to appear in Alpaca. Do not resubmit a successful on-chain redemption while it is being processed. The request remains `pending` until Alpaca transfers the underlying shares and the redemption completes.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.