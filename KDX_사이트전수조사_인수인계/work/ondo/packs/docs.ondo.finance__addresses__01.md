# 읽기 묶음: docs.ondo.finance / addresses (1/1)


<<<PAGE https://docs.ondo.finance/addresses>>>
---
url: https://docs.ondo.finance/addresses
title: Smart Contract Addresses - Ondo Finance
description: 
fetched: 2026-11-16
method: render
plan: read
---

## On this page

Back to top

* [OUSG](https://docs.ondo.finance/addresses)
  + [Ethereum](https://docs.ondo.finance/addresses)
  + [Polygon](https://docs.ondo.finance/addresses)
  + [Solana](https://docs.ondo.finance/addresses)
  + [XRP Ledger](https://docs.ondo.finance/addresses)
* [USDY](https://docs.ondo.finance/addresses)
  + [Ethereum](https://docs.ondo.finance/addresses)
  + [BNB Chain](https://docs.ondo.finance/addresses)
  + [Mantle](https://docs.ondo.finance/addresses)
  + [Solana](https://docs.ondo.finance/addresses)
  + [Sui](https://docs.ondo.finance/addresses)
  + [Aptos](https://docs.ondo.finance/addresses)
  + [Noble](https://docs.ondo.finance/addresses)
  + [Arbitrum](https://docs.ondo.finance/addresses)
  + [Stellar](https://docs.ondo.finance/addresses)
  + [Plume](https://docs.ondo.finance/addresses)
  + [Sei](https://docs.ondo.finance/addresses)
  + [Tempo](https://docs.ondo.finance/addresses)
* [Ondo Stocks](https://docs.ondo.finance/addresses)
  + [Ethereum](https://docs.ondo.finance/addresses)
  + [BNB Chain](https://docs.ondo.finance/addresses)
  + [HyperEVM](https://docs.ondo.finance/addresses)
  + [Robinhood Chain](https://docs.ondo.finance/addresses)
  + [Solana](https://docs.ondo.finance/addresses)
* [Ondo Intelligent Portfolios](https://docs.ondo.finance/addresses)
  + [Ethereum](https://docs.ondo.finance/addresses)
  + [BNB Chain](https://docs.ondo.finance/addresses)
  + [Solana](https://docs.ondo.finance/addresses)
* [Ondo Private Markets](https://docs.ondo.finance/addresses)
  + [Ethereum](https://docs.ondo.finance/addresses)
* [Ondo Bridge](https://docs.ondo.finance/addresses)
* [Legacy](https://docs.ondo.finance/addresses)
  + [OUSG - Ethereum](https://docs.ondo.finance/addresses)
  + [USDY - Ethereum](https://docs.ondo.finance/addresses)

Smart Contracts

# Smart Contract Addresses

Copy pageCopy page

Copy pageCopy page

Source code for the contracts below is published at [github.com/ondoprotocol/rwa-contracts](https://github.com/ondoprotocol/rwa-contracts).

## OUSG

### Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| OUSG | [`0x1B19C19393e2d034D8Ff31ff34c81252FcBbee92`](https://etherscan.io/token/0x1B19C19393e2d034D8Ff31ff34c81252FcBbee92) | [Github](https://github.com/ondoprotocol/tokenized-funds/blob/main/contracts/token/CashKYCSenderReceiver.sol) | The OUSG token |
| OUSG\_InstantManager | [`0x93358db73B6cd4b98D89c8F5f230E81a95c2643a`](https://etherscan.io/address/0x93358db73B6cd4b98D89c8F5f230E81a95c2643a) | [Etherscan](https://etherscan.io/address/0x93358db73B6cd4b98D89c8F5f230E81a95c2643a) | The Ondo smart contract investors use on the ondo.finance webapp to instantly buy or redeem OUSG |
| Coinbase Prime address (ousg.eth) | [`0xF67416a2C49f6A46FEe1c47681C5a3832cf8856c`](https://etherscan.io/address/0xF67416a2C49f6A46FEe1c47681C5a3832cf8856c) | N/A | Coinbase Prime custodian account. Investors can buy OUSG by transferring USDC to this address or by using the web app hosted on ondo.finance, where the CashManager will transfer USDC to this address on their behalf. |
| OndoIDRegistry | [`0xcf6958D69d535FD03BD6Df3F4fe6CDcd127D97df`](https://etherscan.io/address/0xcf6958D69d535FD03BD6Df3F4fe6CDcd127D97df) | [Etherscan](https://etherscan.io/address/0xcf6958D69d535FD03BD6Df3F4fe6CDcd127D97df) | Addresses that can hold OUSG are stored via this contract |
| OndoOracle | [`0x9Cad45a8BF0Ed41Ff33074449B357C7a1fAb4094`](https://etherscan.io/address/0x9Cad45a8BF0Ed41Ff33074449B357C7a1fAb4094) | [Etherscan](https://etherscan.io/address/0x9Cad45a8BF0Ed41Ff33074449B357C7a1fAb4094) | Unified interface for retrieving token price data required by Ondo contracts. |
| OUSG Recipient | [`0x72Be8C14B7564f7a61ba2f6B7E50D18DC1D4B63D`](https://etherscan.io/address/0x72Be8C14B7564f7a61ba2f6B7E50D18DC1D4B63D) | [Etherscan](https://etherscan.io/address/0x72Be8C14B7564f7a61ba2f6B7E50D18DC1D4B63D) | Recipient address for OUSG, for manual redemptions. |
| PYUSD Recipient | [`0x0317a350b093F8010837d1b844292555d73ebC2c`](https://etherscan.io/address/0x0317a350b093F8010837d1b844292555d73ebC2c) | [Etherscan](https://etherscan.io/address/0x0317a350b093F8010837d1b844292555d73ebC2c) | Recipient address for PYUSD, for manual subscriptions. |

### Polygon

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| OUSG | [`0xbA11C5effA33c4D6F8f593CFA394241CfE925811`](https://polygonscan.com/token/0xbA11C5effA33c4D6F8f593CFA394241CfE925811) | [PolygonScan](https://polygonscan.com/address/0xbA11C5effA33c4D6F8f593CFA394241CfE925811) | The OUSG token |
| CashManager | [`0x6B7443808ACFCD48f1DE212C2557462fA86Ee945`](https://polygonscan.com/address/0x6B7443808ACFCD48f1DE212C2557462fA86Ee945) | [PolygonScan](https://polygonscan.com/address/0x6B7443808ACFCD48f1DE212C2557462fA86Ee945) | The Ondo smart contract investors use on the ondo.finance webapp to buy or redeem OUSG |
| Registry | [`0x7cD852c0D7613aA869e632929560f310D4059AC1`](https://polygonscan.com/address/0x7cD852c0D7613aA869e632929560f310D4059AC1) | [PolygonScan](https://polygonscan.com/address/0x7cD852c0D7613aA869e632929560f310D4059AC1) | Addresses that can hold OUSG are stored via this contract |

### Solana

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| OUSG | [`i7u4r16TcsJTgq1kAG8opmVZyVnAKBwLKu6ZPMwzxNc`](https://solscan.io/token/i7u4r16TcsJTgq1kAG8opmVZyVnAKBwLKu6ZPMwzxNc) | N/A | The OUSG token on Solana |
| OUSG Circle address | [`EgFDCr2UmsoUvoJ5DcNZqVnkFZsDE9KyCYBhGcnrAd5G`](https://solscan.io/account/EgFDCr2UmsoUvoJ5DcNZqVnkFZsDE9KyCYBhGcnrAd5G) | N/A | Circle custodian account. Investors can buy OUSG by transferring USDC to this address. |

### XRP Ledger

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| OUSG | [`4F55534700000000000000000000000000000000.rHuiXXjHLpMP8ZE9sSQU5aADQVWDwv6h5p`](https://livenet.xrpl.org/token/4F55534700000000000000000000000000000000.rHuiXXjHLpMP8ZE9sSQU5aADQVWDwv6h5p) | N/A | The OUSG token on XRP Ledger |
| OUSG Recipient | [`rHprwRkvDexV5LF5tzKQmx7U7Ku2836DA1`](https://livenet.xrpl.org/accounts/rHprwRkvDexV5LF5tzKQmx7U7Ku2836DA1) | N/A | Recipient address for OUSG, for manual OUSG redemptions. |
| RLUSD Recipient | [`rEZiJUJskputkS6VjPAwdRLESNpdyRC6ba Destination Tag: 1`](https://livenet.xrpl.org/accounts/rEZiJUJskputkS6VjPAwdRLESNpdyRC6ba) | N/A | Recipient address for RLUSD, for manual OUSG subscriptions. |

## USDY

### Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x96F6eF951840721AdBF46Ac996b59E0235CB985C`](https://etherscan.io/token/0x96F6eF951840721AdBF46Ac996b59E0235CB985C) | [Etherscan](https://etherscan.io/address/0x96F6eF951840721AdBF46Ac996b59E0235CB985C) | The USDY token on Ethereum |
| rUSDY | [`0xaf37c1167910ebC994e266949387d2c7C326b879`](https://etherscan.io/token/0xaf37c1167910ebC994e266949387d2c7C326b879) | [Etherscan](https://etherscan.io/address/0xaf37c1167910ebC994e266949387d2c7C326b879) | The rUSDY token on Ethereum (rebasing USDY) |
| USDY\_InstantManager | [`0xa42613C243b67BF6194Ac327795b926B4b491f15`](https://etherscan.io/address/0xa42613C243b67BF6194Ac327795b926B4b491f15) | [Etherscan](https://etherscan.io/address/0xa42613C243b67BF6194Ac327795b926B4b491f15) | The Ondo smart contract used to instantly buy or redeem USDY |
| USDYc | [`0xe86845788d6e3e5c2393ade1a051ae617d974c09`](https://etherscan.io/token/0xe86845788d6e3e5c2393ade1a051ae617d974c09) | [Etherscan](https://etherscan.io/address/0xe86845788d6e3e5c2393ade1a051ae617d974c09) | The USDYc token, or “Cooking USDY,” on Ethereum. An onchain bookkeeping representation of the *Temporary Global Certificate* representing a lender’s rights to payment during the period before their USDY tokens are issued. When this period ends, USDY tokens are minted and the associated USDYc tokens are burned |
| USDY Coinbase Prime address (USDC Deposits) | [`0xbDa73A0F13958ee444e0782E1768aB4B76EdaE28`](https://etherscan.io/address/0xbDa73A0F13958ee444e0782E1768aB4B76EdaE28) | N/A | Coinbase Prime custodian account. Onboarded investors can buy USDY by transferring USDC to this address or by using the web app hosted on ondo.finance, where the USDYManager will transfer USDC to this address on their behalf. |
| USDYOracleWrapper | [`0x87b126e5518b6a1Bb8465779b4607C45C643DF90`](https://etherscan.io/address/0x87b126e5518b6a1Bb8465779b4607C45C643DF90) | [Etherscan](https://etherscan.io/address/0x87b126e5518b6a1Bb8465779b4607C45C643DF90) | A stable entry point for reading the USDY price. The wrapper always references the current canonical USDY oracle implementation, so integrators reading from this address stay aligned with the latest oracle without any action on their part. |
| ContinuousPriceOracle | [`0xbAEC2b9fE27cD054e1c0C2B720aF117d9D7eC871`](https://etherscan.io/address/0xbAEC2b9fE27cD054e1c0C2B720aF117d9D7eC871) | [Etherscan](https://etherscan.io/address/0xbAEC2b9fE27cD054e1c0C2B720aF117d9D7eC871) | The USDY price oracle from November 1, 2026. It calculates the price continuously from a stored price and a yearly rate. Listed for reference: integrators should read the USDY price from the USDYOracleWrapper. |
| Blocklist | [`0xd8c8174691d936E2C80114EC449037b13421B0a8`](https://etherscan.io/address/0xd8c8174691d936E2C80114EC449037b13421B0a8) | [Etherscan](https://etherscan.io/address/0xd8c8174691d936E2C80114EC449037b13421B0a8) | Smart contract which holds all blocked addresses |

### BNB Chain

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x608593d17A2decBbc4399e4185bE4922F97eD32E`](https://bscscan.com/token/0x608593d17A2decBbc4399e4185bE4922F97eD32E) | [BscScan](https://bscscan.com/address/0x608593d17A2decBbc4399e4185bE4922F97eD32E) | The USDY token on BNB Chain |
| USDY\_InstantManager | [`0x9bA360087075A4Cef548eeD71Eed197bf4cFA4E2`](https://bscscan.com/address/0x9bA360087075A4Cef548eeD71Eed197bf4cFA4E2) | [BscScan](https://bscscan.com/address/0x9bA360087075A4Cef548eeD71Eed197bf4cFA4E2) | The Ondo smart contract used to instantly buy or redeem USDY |
| USDYOracleWrapper | [`0x1B508f3eF4a0c26fE9659eB1011BFb8E5e0c7782`](https://bscscan.com/address/0x1B508f3eF4a0c26fE9659eB1011BFb8E5e0c7782) | [BscScan](https://bscscan.com/address/0x1B508f3eF4a0c26fE9659eB1011BFb8E5e0c7782) | A stable entry point for reading the USDY price. The wrapper always references the current canonical USDY oracle implementation, so integrators reading from this address stay aligned with the latest oracle without any action on their part. |
| ContinuousPriceOracle | [`0x2762E65716B93dE5e4d736be1062bC02f4c05d06`](https://bscscan.com/address/0x2762E65716B93dE5e4d736be1062bC02f4c05d06) | [BscScan](https://bscscan.com/address/0x2762E65716B93dE5e4d736be1062bC02f4c05d06) | The USDY price oracle from November 1, 2026. It calculates the price continuously from a stored price and a yearly rate. Listed for reference: integrators should read the USDY price from the USDYOracleWrapper. |
| Blocklist | [`0xA8a823584Ac88cb48e7F8F467d1be9c0601E43F8`](https://bscscan.com/address/0xA8a823584Ac88cb48e7F8F467d1be9c0601E43F8) | [BscScan](https://bscscan.com/address/0xA8a823584Ac88cb48e7F8F467d1be9c0601E43F8) | Smart contract which holds all blocked addresses |

### Mantle

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x5bE26527e817998A7206475496fDE1E68957c5A6`](https://explorer.mantle.xyz/token/0x5bE26527e817998A7206475496fDE1E68957c5A6) | [Mantle Explorer](https://explorer.mantle.xyz/token/0x5bE26527e817998A7206475496fDE1E68957c5A6?tab=contract) | The USDY token on Mantle |
| Mantle USD (mUSD) | [`0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3`](https://explorer.mantle.xyz/token/0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3) | [Mantle Explorer](https://explorer.mantle.xyz/token/0xab575258d37EaA5C8956EfABe71F4eE8F6397cF3?tab=contract) | The rebasing counterpart of USDY on Mantle |
| USDYOracleWrapper | [`0x1c45594c192EeB10aa54a385B9A5b03efdb402D2`](https://explorer.mantle.xyz/address/0x1c45594c192EeB10aa54a385B9A5b03efdb402D2) | [Mantle Explorer](https://explorer.mantle.xyz/address/0x1c45594c192EeB10aa54a385B9A5b03efdb402D2?tab=contract) | A stable entry point for reading the USDY price. The wrapper always references the current canonical USDY oracle implementation, so integrators reading from this address stay aligned with the latest oracle without any action on their part. |
| ContinuousPriceOracle | [`0x45713B83beF5D1B7AB74aA8A2487F5E7E0EB2FA2`](https://explorer.mantle.xyz/address/0x45713B83beF5D1B7AB74aA8A2487F5E7E0EB2FA2) | [Mantle Explorer](https://explorer.mantle.xyz/address/0x45713B83beF5D1B7AB74aA8A2487F5E7E0EB2FA2?tab=contract) | The USDY price oracle from November 1, 2026. It calculates the price continuously from a stored price and a yearly rate. Listed for reference: integrators should read the USDY price from the USDYOracleWrapper. |
| Redemption Price Oracle (Previous) | [`0xA96abbe61AfEdEB0D14a20440Ae7100D9aB4882f`](https://explorer.mantle.xyz/address/0xA96abbe61AfEdEB0D14a20440Ae7100D9aB4882f) | [Mantle Explorer](https://explorer.mantle.xyz/address/0xA96abbe61AfEdEB0D14a20440Ae7100D9aB4882f?tab=contract) | The previous USDY price oracle (Dynamic Rate Oracle). Replaced by the ContinuousPriceOracle on November 1, 2026, and is expected to be deprecated on December 31, 2026. |
| Blocklist | [`0xdBd7a7d8807f0C98c9A58f7732f2799c8587e5c6`](https://explorer.mantle.xyz/address/0xdBd7a7d8807f0C98c9A58f7732f2799c8587e5c6) | [Mantle Explorer](https://explorer.mantle.xyz/address/0xdBd7a7d8807f0C98c9A58f7732f2799c8587e5c6?tab=contract) | Smart contract which holds all blocked addresses |

### Solana

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`A1KLoBrKBde8Ty9qtNQUtq3C2ortoC3u7twggz7sEto6`](https://solscan.io/token/A1KLoBrKBde8Ty9qtNQUtq3C2ortoC3u7twggz7sEto6) | N/A | The USDY token on Solana |

### Sui

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x960b531667636f39e85867775f52f6b1f220a058c4de786905bdf761e06a56bb::usdy::USDY`](https://suiscan.xyz/mainnet/coin/0x960b531667636f39e85867775f52f6b1f220a058c4de786905bdf761e06a56bb::usdy::USDY) | [Suiscan](https://suiscan.xyz/mainnet/object/0x960b531667636f39e85867775f52f6b1f220a058c4de786905bdf761e06a56bb/contracts) | The USDY token on Sui |
| USDY Redemptions Account | [`0xabebc1a41aa460eb560469e6b3c22d610b44b877979989e5e9227cca5b271fd2`](https://suiscan.xyz/mainnet/account/0xabebc1a41aa460eb560469e6b3c22d610b44b877979989e5e9227cca5b271fd2) | N/A | Address for USDY Redemptions on Sui |

### Aptos

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc::usdy::USDY`](https://explorer.aptoslabs.com/account/0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc) | [Aptos Explorer](https://explorer.aptoslabs.com/account/0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc/modules/code/usdy?network=mainnet) | The USDY token on Aptos |
| USDY Redemptions Account | [`0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc`](https://explorer.aptoslabs.com/account/0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc) | N/A | Address for USDY Redemptions on Aptos |

### Noble

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`ausdy`](https://www.mintscan.io/noble/assets/native/YXVzZHk=) | [Github](https://github.com/ondoprotocol/usdy-noble) | The USDY token on Noble (Cosmos ecosystem) |
| USDY Redemptions Account | [`noble1c940mn5xm4vykfpts75ul6zx3ngy8ezf8qyvgu`](https://www.mintscan.io/noble/address/noble1c940mn5xm4vykfpts75ul6zx3ngy8ezf8qyvgu) | N/A | Address for USDY Redemptions on Noble |

### Arbitrum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x35e050d3C0eC2d29D269a8EcEa763a183bDF9A9D`](https://arbiscan.io/address/0x35e050d3C0eC2d29D269a8EcEa763a183bDF9A9D) | [Arbiscan Explorer](https://arbiscan.io/address/0x35e050d3C0eC2d29D269a8EcEa763a183bDF9A9D) | The USDY token on Arbitrum |
| USDY Redemptions Account | [`0xFDE36D55112f5AAaFa5087832AA557CaB7Be1888`](https://arbiscan.io/address/0xFDE36D55112f5AAaFa5087832AA557CaB7Be1888) | N/A | Address for USDY Redemptions on Arbitrum |

### Stellar

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`USDY-GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6`](https://stellar.expert/explorer/public/asset/USDY-GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6) | N/A | The USDY token on Stellar |
| USDY (Stellar Asset Contract) | [`CB3YA656OYIHU57657I5KGSBRHE5I3OZU4VFC22PYAOANFZHEWNYGAGP`](https://stellar.expert/explorer/public/contract/CB3YA656OYIHU57657I5KGSBRHE5I3OZU4VFC22PYAOANFZHEWNYGAGP) | N/A | The Soroban contract for the USDY token on Stellar, used by the Stellar OFT |
| USDY Redemptions Account | [`GC5T3RH2VK3G44FIHMOZY5UGN56L52UYFGHKFUX6X2HNIGEZ2PFXMI23`](https://stellar.expert/explorer/public/account/GC5T3RH2VK3G44FIHMOZY5UGN56L52UYFGHKFUX6X2HNIGEZ2PFXMI23) | N/A | Address for USDY Redemptions on Stellar |
| USDC (Stellar) Recipient | [`GAD3O7FODAFLAOXVVKGFBKQFFJFXSJ3LHWSPLEDEI5WQTCXQOE27JGNY?memoId=0`](https://stellar.expert/explorer/public/account/GAD3O7FODAFLAOXVVKGFBKQFFJFXSJ3LHWSPLEDEI5WQTCXQOE27JGNY) | N/A | Recipient address for USDC on Stellar, for USDY subscriptions. |

### Plume

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0xD2B65e851Be3d80D3c2ce795eB2E78f16cB088b2`](https://explorer.plume.org/address/0xD2B65e851Be3d80D3c2ce795eB2E78f16cB088b2) | [Plume Explorer](https://explorer.plume.org/address/0xD2B65e851Be3d80D3c2ce795eB2E78f16cB088b2?tab=contract) | The USDY token on Plume |

### Sei

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x54cD901491AeF397084453F4372B93c33260e2A6`](https://seiscan.io/address/0x54cD901491AeF397084453F4372B93c33260e2A6) | [Seiscan Explorer](https://seiscan.io/address/0x54cD901491AeF397084453F4372B93c33260e2A6) | The USDY token on Sei |

### Tempo

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDY | [`0x20c000000000000000000000D479B9f6eC0ceFf9`](https://explore.tempo.xyz/token/0x20c000000000000000000000D479B9f6eC0ceFf9) | N/A | The USDY token on Tempo, issued as a TIP-20 token with 6 decimals |
| USDY\_InstantManager | [`0x7E2A9d8B3B97EDa5922cdb320fC96e0ff4C8B4C5`](https://explore.tempo.xyz/address/0x7E2A9d8B3B97EDa5922cdb320fC96e0ff4C8B4C5) | [Tempo Explorer](https://explore.tempo.xyz/address/0x7E2A9d8B3B97EDa5922cdb320fC96e0ff4C8B4C5?tab=contract) | The Ondo smart contract used to instantly buy or redeem USDY |
| USDYOracleWrapper | [`0xb25b3266467a755328cfb8F1b349319C2B94419C`](https://explore.tempo.xyz/address/0xb25b3266467a755328cfb8F1b349319C2B94419C) | [Tempo Explorer](https://explore.tempo.xyz/address/0xb25b3266467a755328cfb8F1b349319C2B94419C?tab=contract) | A stable entry point for reading the USDY price. The wrapper always references the current canonical USDY oracle implementation, so integrators reading from this address stay aligned with the latest oracle without any action on their part. |
| ContinuousPriceOracle | [`0xeF4E3d039b9E6bcb601d1964a44ad6f556B6310c`](https://explore.tempo.xyz/address/0xeF4E3d039b9E6bcb601d1964a44ad6f556B6310c) | [Tempo Explorer](https://explore.tempo.xyz/address/0xeF4E3d039b9E6bcb601d1964a44ad6f556B6310c?tab=contract) | The USDY price oracle from November 1, 2026. It calculates the price continuously from a stored price and a yearly rate. Listed for reference: integrators should read the USDY price from the USDYOracleWrapper. |

## Ondo Stocks

### Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| GMTokenManager | [`0x2c158BC456e027b2AfFCCadF1BDBD9f5fC4c5C8c`](https://etherscan.io/address/0x2c158BC456e027b2AfFCCadF1BDBD9f5fC4c5C8c) | [Etherscan](https://etherscan.io/address/0x2c158BC456e027b2AfFCCadF1BDBD9f5fC4c5C8c) | The Ondo smart contract used to perform mints and redemptions of Ondo Stocks (via USDC or USDon). |
| GMIssuerManager | [`0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E`](https://etherscan.io/address/0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E) | [Etherscan](https://etherscan.io/address/0xec8bBB0c90c0B5F4D8240D0F7b49DA3b0aA41f4E) | The Ondo smart contract used to redeem Ondo Stocks for the underlying securities through Alpaca’s Instant Tokenization Network (ITN). |
| USDon | [`0xAcE8E719899F6E91831B18AE746C9A965c2119F1`](https://etherscan.io/address/0xace8e719899f6e91831b18ae746c9a965c2119f1) | [Etherscan](https://etherscan.io/address/0xace8e719899f6e91831b18ae746c9a965c2119f1) | The USDon token, which acts as the proximate token for swapping to/from Ondo Stocks. |
| USDonManager | [`0x05CCbB4b74854f8A067b83475E8c34f5a413D7e1`](https://etherscan.io/address/0x05CCbB4b74854f8A067b83475E8c34f5a413D7e1) | [Etherscan](https://etherscan.io/address/0x05CCbB4b74854f8A067b83475E8c34f5a413D7e1) | The Ondo PSM (Peg Stability Module) smart contract for USDon, facilitating swaps between USDon and USDC. |
| Ondo Stocks | [`See here for Ondo Stocks details`](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | [See Etherscan Contract links here](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | Ondo Stocks |
| SyntheticSharesOracle | [`0x9BC39DB6fbB44B91a48b8D5A6C208B82B1741bE6`](https://etherscan.io/address/0x9BC39DB6fbB44B91a48b8D5A6C208B82B1741bE6) | [Etherscan](https://etherscan.io/address/0x9BC39DB6fbB44B91a48b8D5A6C208B82B1741bE6) | Oracle contract reflecting the “synthetic shares” (stock-to-token multiplier) for Ondo Stocks. |
| GMTokenLimitOrder | [`0xf0Bc39Fc911F6437C84d16188dD8294F7110f451`](https://etherscan.io/address/0xf0Bc39Fc911F6437C84d16188dD8294F7110f451) | [Etherscan](https://etherscan.io/address/0xf0Bc39Fc911F6437C84d16188dD8294F7110f451) | The Ondo smart contract enabling users to place limit orders for minting and redeeming Ondo Stocks, using the GMTokenManager for order execution. |

### BNB Chain

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| GMTokenManager | [`0x91f8Aff3738825e8eB16FC6f6b1A7A4647bDB299`](https://bscscan.com/address/0x91f8Aff3738825e8eB16FC6f6b1A7A4647bDB299) | [BscScan](https://bscscan.com/address/0x91f8Aff3738825e8eB16FC6f6b1A7A4647bDB299) | The Ondo smart contract used to perform mints and redemptions of Ondo Stocks (via USDC or USDon). |
| GMIssuerManager | [`0x341f9e6463161F0C90037Cbc0150DC54e6d1e06e`](https://bscscan.com/address/0x341f9e6463161F0C90037Cbc0150DC54e6d1e06e) | [BscScan](https://bscscan.com/address/0x341f9e6463161F0C90037Cbc0150DC54e6d1e06e) | The Ondo smart contract used to redeem Ondo Stocks for the underlying securities through Alpaca’s Instant Tokenization Network (ITN). |
| USDon | [`0x1f8955E640Cbd9abc3C3Bb408c9E2E1f5F20DfE6`](https://bscscan.com/address/0x1f8955E640Cbd9abc3C3Bb408c9E2E1f5F20DfE6) | [BscScan](https://bscscan.com/address/0x1f8955E640Cbd9abc3C3Bb408c9E2E1f5F20DfE6) | The USDon token, which acts as the proximate token for swapping to/from Ondo Stocks. |
| Ondo Stocks | [`See here for Ondo Stocks details`](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | [See BscScan Contract links here](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | Ondo Stocks |
| SyntheticSharesOracle | [`0xF4Fd8a1B412633e10527454137A29Db7Aa35F15e`](https://bscscan.com/address/0xF4Fd8a1B412633e10527454137A29Db7Aa35F15e) | [BscScan](https://bscscan.com/address/0xF4Fd8a1B412633e10527454137A29Db7Aa35F15e) | Oracle contract reflecting the “synthetic shares” (stock-to-token multiplier) for Ondo Stocks. |
| GMTokenLimitOrder | [`0x96b525B1a93f31E65F4aAf18C53842eD28525D48`](https://bscscan.com/address/0x96b525B1a93f31E65F4aAf18C53842eD28525D48) | [BscScan](https://bscscan.com/address/0x96b525B1a93f31E65F4aAf18C53842eD28525D48) | The Ondo smart contract enabling users to place limit orders for minting and redeeming Ondo Stocks, using the GMTokenManager for order execution. |

### HyperEVM

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Ondo Stocks | [`See here for Ondo Stocks details`](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | [See HyperEVM Explorer Contract links here](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | Ondo Stocks |

### Robinhood Chain

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Ondo Stocks | [`See here for Ondo Stocks details`](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | [See Robin Etherscan Contract links here](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | Ondo Stocks |

### Solana

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Program ID | [`XzTT4XB8m7sLD2xi6snefSasaswsKCxx5Tifjondogm`](https://solscan.io/account/XzTT4XB8m7sLD2xi6snefSasaswsKCxx5Tifjondogm) | [GitHub](https://github.com/ondoprotocol/global-markets-solana) | The unique on-chain address used to identify and interact with the Ondo Stocks smart contract (called a “program” on Solana). |
| USDon | [`ZPFtoCe7WWqG4N3ZFRccS8T9SMBeHsd1Vmgv2i7ondo`](https://solscan.io/token/ZPFtoCe7WWqG4N3ZFRccS8T9SMBeHsd1Vmgv2i7ondo) | N/A | The USDon token, which acts as the proximate token for swapping to/from Ondo Stocks. |
| Ondo Stocks | [`See here for Ondo Stocks details`](https://www.dropbox.com/scl/fi/qjfxyg748mx0dwi6up86d/EXTERNAL-Ondo-GM-Tokens-Ondo-GM-Tokens.csv?rlkey=n3no1w78wrah3umsl0nr9s77i&e=2&st=spdit2q1&dl=0) | N/A | Ondo Stocks |

## Ondo Intelligent Portfolios

### Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| PortfolioTokenManager | [`0x54aC0E5f60EC257385f134D5Fa490A00e5ddD17c`](https://etherscan.io/address/0x54aC0E5f60EC257385f134D5Fa490A00e5ddD17c) | [Etherscan](https://etherscan.io/address/0x54aC0E5f60EC257385f134D5Fa490A00e5ddD17c) | The Ondo smart contract used to mint and redeem Ondo Intelligent Portfolios using USDC. |
| PortfolioTokenLimitOrder | [`0x6658F677902e1Df805AdF42fac015E1124AEbFDB`](https://etherscan.io/address/0x6658F677902e1Df805AdF42fac015E1124AEbFDB) | [Etherscan](https://etherscan.io/address/0x6658F677902e1Df805AdF42fac015E1124AEbFDB) | The Ondo smart contract enabling users to place limit orders for minting and redeeming Ondo Intelligent Portfolios, using the PortfolioTokenManager for order execution. |
| Ondo Intelligent Portfolios | [`See here for Ondo Intelligent Portfolios details`](https://docs.ondo.finance/partner-docs/tokens) | [See Etherscan Contract links here](https://docs.ondo.finance/partner-docs/tokens) | Ondo Intelligent Portfolios |

### BNB Chain

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| PortfolioTokenManager | [`0x28B2C711156EfB3238A19eFa6E0bF85F3523Bac4`](https://bscscan.com/address/0x28B2C711156EfB3238A19eFa6E0bF85F3523Bac4) | [BscScan](https://bscscan.com/address/0x28B2C711156EfB3238A19eFa6E0bF85F3523Bac4) | The Ondo smart contract used to mint and redeem Ondo Intelligent Portfolios using USDT. |
| PortfolioTokenLimitOrder | [`0xA2aA93cbB069B4BF246258E4D9cD093B914DcDFE`](https://bscscan.com/address/0xA2aA93cbB069B4BF246258E4D9cD093B914DcDFE) | [BscScan](https://bscscan.com/address/0xA2aA93cbB069B4BF246258E4D9cD093B914DcDFE) | The Ondo smart contract enabling users to place limit orders for minting and redeeming Ondo Intelligent Portfolios, using the PortfolioTokenManager for order execution. |
| Ondo Intelligent Portfolios | [`See here for Ondo Intelligent Portfolios details`](https://docs.ondo.finance/partner-docs/tokens) | [See BscScan Contract links here](https://docs.ondo.finance/partner-docs/tokens) | Ondo Intelligent Portfolios |

### Solana

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Program ID | [`XzTT4XB8m7sLD2xi6snefSasaswsKCxx5Tifjondogm`](https://solscan.io/account/XzTT4XB8m7sLD2xi6snefSasaswsKCxx5Tifjondogm) | [GitHub](https://github.com/ondoprotocol/global-markets-solana) | The unique on-chain address used to identify and interact with the Ondo smart contract (called a “program” on Solana). Shared with Ondo Stocks. |
| PortfolioTokenManager | [`GRXoCbbJdKpGLgcVvwkeypog1cEjKLXnyjKqzRjvbLPS`](https://solscan.io/account/GRXoCbbJdKpGLgcVvwkeypog1cEjKLXnyjKqzRjvbLPS) | N/A | The Ondo account used to mint and redeem Ondo Intelligent Portfolios using USDC. |
| Ondo Intelligent Portfolios | [`See here for Ondo Intelligent Portfolios details`](https://docs.ondo.finance/partner-docs/tokens) | N/A | Ondo Intelligent Portfolios |

## Ondo Private Markets

### Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| OPAIPon | [`0x1201dCFc7c0b2cE46C7604Bf104234AB42A56Bbd`](https://etherscan.io/token/0x1201dCFc7c0b2cE46C7604Bf104234AB42A56Bbd) | [Etherscan](https://etherscan.io/address/0x1201dCFc7c0b2cE46C7604Bf104234AB42A56Bbd) | The OPAIPon token on Ethereum. This is an Ondo Private Markets tokenized note with payout tied to the per-share value realized on OpenAI’s common shares and tradable on secondary spot markets. |

## Ondo Bridge

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Ethereum OFT Adapter | [`0xa6275720b3fB1Efe3E6EF2b5BF2293148852307D`](https://etherscan.io/address/0xa6275720b3fB1Efe3E6EF2b5BF2293148852307D) | [Etherscan](https://etherscan.io/address/0xa6275720b3fB1Efe3E6EF2b5BF2293148852307D) | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Ethereum |
| Mantle OFT Adapter | [`0x0bE393DC46248E4285dc5CAcA3084bc7e9bfbB41`](https://explorer.mantle.xyz/address/0x0bE393DC46248E4285dc5CAcA3084bc7e9bfbB41) | [Mantle Explorer](https://explorer.mantle.xyz/address/0x0bE393DC46248E4285dc5CAcA3084bc7e9bfbB41?tab=contract) | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Mantle |
| Arbitrum OFT Adapter | [`0x0bE393DC46248E4285dc5CAcA3084bc7e9bfbB41`](https://arbiscan.io/address/0x0be393dc46248e4285dc5caca3084bc7e9bfbb41) | [Arbiscan](https://arbiscan.io/address/0x0be393dc46248e4285dc5caca3084bc7e9bfbb41) | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Arbitrum |
| Solana OFT Adatper | [`7YNReenG6AXgVUfmSizt6hoVXrznS4zDdgCj1UTLJ2S3`](https://solscan.io/account/7YNReenG6AXgVUfmSizt6hoVXrznS4zDdgCj1UTLJ2S3) | N/A | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Solana |
| BNB Chain OFT Adapter | [`0xAE6a049cDda7536Af3875B3dAAF34f24Be5cF00c`](https://bscscan.com/address/0xAE6a049cDda7536Af3875B3dAAF34f24Be5cF00c) | [BscScan](https://bscscan.com/address/0xAE6a049cDda7536Af3875B3dAAF34f24Be5cF00c) | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on BNB Chain |
| Sei OFT Adapter | [`0x6f04B655d5209E85E47D3920A2EF407A66e83f6c`](https://seiscan.io/address/0x6f04B655d5209E85E47D3920A2EF407A66e83f6c) | [Seiscan Explorer](https://seiscan.io/address/0x6f04B655d5209E85E47D3920A2EF407A66e83f6c) | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Sei |
| Stellar OFT | [`CAJ4WISNJNHNL6EMO75K7L4EBMUUNFTAQ3MFAQAFNLYRTB72B2NYJIIX`](https://stellar.expert/explorer/public/contract/CAJ4WISNJNHNL6EMO75K7L4EBMUUNFTAQ3MFAQAFNLYRTB72B2NYJIIX) | N/A | LayerZero Omnichain Fungible Token, used for handling burn and mint bridge transfers on Stellar |
| Tempo OFT Adapter | [`0xd45c2377241F1dA765570e0D57920F1cf4855bCB`](https://explore.tempo.xyz/address/0xd45c2377241F1dA765570e0D57920F1cf4855bCB) | N/A | LayerZero Omnichain Fungible Token Adapter, used for handling burn and mint bridge transfers on Tempo |

## Legacy

The legacy contract addresses below have been deprecated and should no longer be used.

### OUSG - Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| Oracle (Legacy) | [`0x0502c5ae08E7CD64fe1AEDA7D6e229413eCC6abe`](https://etherscan.io/address/0x0502c5ae08E7CD64fe1AEDA7D6e229413eCC6abe) | [Etherscan](https://etherscan.io/address/0x0502c5ae08E7CD64fe1AEDA7D6e229413eCC6abe) | RateCheck Oracle for OUSG which holds the price for OUSG. The price can only be set +/- 74 bps relative to the price movement of the BlackRock Short-term US Treasuries (SHV) ETF. |
| OUSGInstantManager (Legacy) | [`0x2826989983e3a66F0622132D019c2Ae173eb6A43`](https://etherscan.io/address/0x2826989983e3a66F0622132D019c2Ae173eb6A43) | [Etherscan](https://etherscan.io/address/0x2826989983e3a66F0622132D019c2Ae173eb6A43) | Deprecated Ondo smart contract investors used on the ondo.finance webapp to instantly buy or redeem OUSG. Deprecated on April 7, 2025. |
| KYCRegistry (Legacy) | [`0x7cE91291846502D50D635163135B2d40a602dc70`](https://etherscan.io/address/0x7cE91291846502D50D635163135B2d40a602dc70) | [Github](https://github.com/ondoprotocol/tokenized-funds/blob/main/contracts/kyc/KYCRegistry.sol) | Deprecated Ondo smart contract that stored addresses that could hold OUSG. Deprecated on April 7, 2025. |
| OUSGManager (Legacy) | [`0xF16c188c2D411627d39655A60409eC6707D3d5e8`](https://etherscan.io/address/0xF16c188c2D411627d39655A60409eC6707D3d5e8) | [Etherscan](https://etherscan.io/address/0xF16c188c2D411627d39655A60409eC6707D3d5e8) | Deprecated Ondo smart contract investors used on the ondo.finance webapp to buy or redeem OUSG. Deprecated on April 15, 2024. |
| CashManager (Legacy) | [`0x3501883a646f1F8417BcB62162372550954D618f`](https://etherscan.io/address/0x3501883a646f1F8417BcB62162372550954D618f) | [Github](https://github.com/ondoprotocol/tokenized-funds/blob/main/contracts/CashManager.sol) | Deprecated Ondo smart contract investors used on the ondo.finance webapp to buy or redeem OUSG. Deprecated on December 13, 2023. |

### USDY - Ethereum

| Contract/address name | Address | Source code | Description |
| --- | --- | --- | --- |
| USDYManager | [`0x25A103A1D6AeC5967c1A4fe2039cdc514886b97e`](https://etherscan.io/address/0x25A103A1D6AeC5967c1A4fe2039cdc514886b97e) | [Etherscan](https://etherscan.io/address/0x25A103A1D6AeC5967c1A4fe2039cdc514886b97e) | Deprecated Ondo smart contract used on the ondo.finance webapp to buy or redeem USDY. |

[USDY and mUSD Conversion](https://docs.ondo.finance/tools/converter/usdy-musd-conversion)[Smart Contract Audits](https://docs.ondo.finance/audits)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/addresses#webpage","url":"https://docs.ondo.finance/addresses","name":"Smart Contract Addresses","dateModified":"2026-11-11T23:20:18.837Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/addresses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/addresses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Ondo Finance","item":"https://docs.ondo.finance"},{"@type":"ListItem","position":2,"name":"Smart Contract Addresses","item":"https://docs.ondo.finance/addresses"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/addresses#article","headline":"Smart Contract Addresses","name":"Smart Contract Addresses","url":"https://docs.ondo.finance/addresses","mainEntityOfPage":{"@id":"https://docs.ondo.finance/addresses#webpage"},"dateModified":"2026-11-11T23:20:18.837Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```