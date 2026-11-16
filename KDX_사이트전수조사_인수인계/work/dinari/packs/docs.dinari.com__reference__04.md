# 읽기 묶음: docs.dinari.com / reference (4/5)


<<<PAGE https://docs.dinari.com/reference/getstocksplitsbyid>>>
---
url: https://docs.dinari.com/reference/getstocksplitsbyid
title: Get Stock Splits for Stock
description: Get a list of stock splits for a specific `Stock`.
The splits are ordered by the date they were created, with the most recent split first.

In an example 10-for-1 stock split, trading will be halted for the stock at the end of the `payable_date`, as
the split transitions from `PENDING` to `IN_PROGRESS`. This usually occurs over a weekend to minimize trading
disruptions. Each share of stock owned by a shareholder will then be converted into 10 shares, and the split
becomes `COMPLETE` as trading resumes on the `ex_date` with new split-adjusted prices.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Stock Splits for Stock

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/splits

Get a list of stock splits for a specific `Stock`.  
The splits are ordered by the date they were created, with the most recent split first.

In an example 10-for-1 stock split, trading will be halted for the stock at the end of the `payable_date`, as  
the split transitions from `PENDING` to `IN_PROGRESS`. This usually occurs over a weekend to minimize trading  
disruptions. Each share of stock owned by a shareholder will then be converted into 10 shares, and the split  
becomes `COMPLETE` as trading resumes on the `ex_date` with new split-adjusted prices.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

stock\_id

uuid

required

Query Params

page

integer

≥ 1

Defaults to 1

page\_size

integer

1 to 100

Defaults to 25

limit

integer

20 to 100

Defaults to 20

Number of results to return

order

string

enum

Defaults to asc

Sort order

ascdesc

Allowed:

`asc``desc`

next

string | null

Cursor for next page

previous

string | null

Cursor for previous page

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Stock Splits](https://docs.dinari.com/reference/getstocksplits)[Get News Articles for Stock](https://docs.dinari.com/reference/getstocknewsbystockid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/splits

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Stock Splits](https://docs.dinari.com/reference/getstocksplits)[Get News Articles for Stock](https://docs.dinari.com/reference/getstocknewsbystockid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stock Splits for Stock","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createeip155orderrequestpermit>>>
---
url: https://docs.dinari.com/reference/createeip155orderrequestpermit
title: Create EIP155 Order Request Permit
description: Generates a permit that can be signed and used to create an `OrderRequest` using Dinari's EVM smart contracts.

This is a convenience method to prepare the transactions needed to create an `OrderRequest` using Dinari's EVM smart contracts.
Once signed, the transactions can be sent to the EVM network to create the order.
Note that the fee quote is already included in the transactions, so no additional fee quote lookup is needed.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Create EIP155 Order Request Permit

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155/permit

Generates a permit that can be signed and used to create an `OrderRequest` using Dinari's EVM smart contracts.

This is a convenience method to prepare the transactions needed to create an `OrderRequest` using Dinari's EVM smart contracts.  
Once signed, the transactions can be sent to the EVM network to create the order.  
Note that the fee quote is already included in the transactions, so no additional fee quote lookup is needed.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for building a token permit involved in creating an `OrderRequest` using Dinari's EVM smart contracts.

chain\_id

string

enum

required

CAIP-2 chain ID of the blockchain where the `Order` will be placed.

eip155:1eip155:42161eip155:8453eip155:98866eip155:999eip155:43114eip155:56eip155:5042eip155:1329eip155:202110

Show 10 enum values

order\_tif

string

enum

required

Time in force. Indicates how long `Order` is valid for.

DAYGTCIOCFOK

Allowed:

`DAY``GTC``IOC``FOK`

order\_side

string

enum

required

Indicates whether `Order` is a buy or sell.

BUYSELL

Allowed:

`BUY``SELL`

order\_type

string

enum

required

Type of `Order`.

MARKETLIMIT

Allowed:

`MARKET``LIMIT`

payment\_token

string

required

Address of payment token. Required for Accounts outside of US jurisdiction. Accounts with US jurisdiction must use: USDC for live, MockUSD for sandbox.

payment\_token\_quantity

number | null

≥ 0

Amount of payment tokens involved. Required for market buy `Orders`.

asset\_token\_quantity

number | null

≥ 0

Amount of dShare asset tokens involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places for limit `Order Requests` or up to 6 decimal places for market sell `Order Requests`.

limit\_price

number | null

≥ 0

Price per asset in the asset's native currency. USD for US equities and ETFs. Required for limit `Orders`.

stock\_id

uuid | null

The ID of the `Stock` for which the `Order` is being placed.

token\_id

uuid | null

The ID of the `Token` for which the `Order` is being placed.

alloy\_id

uuid | null

The ID of the `Alloy` for which the `Order` is being placed.

client\_order\_id

string | null

Customer-supplied unique identifier to map this `Order` to an order in the customer's systems.

fee

number | null

≥ 0

Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Withdrawal by ID](https://docs.dinari.com/reference/getaccountwithdrawal)[Submit EIP155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155/permit

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Withdrawal by ID](https://docs.dinari.com/reference/getaccountwithdrawal)[Submit EIP155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create EIP155 Order Request Permit","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createeip155orderrequestpermittransaction>>>
---
url: https://docs.dinari.com/reference/createeip155orderrequestpermittransaction
title: Submit EIP155 Order Request
description: Submits a transaction for an EIP155 Order Request given the EIP155OrderRequest ID and Permit Signature.

An `EIP155OrderRequest` representing the proxied order is returned.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Submit EIP155 Order Request

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155

Submits a transaction for an EIP155 Order Request given the EIP155OrderRequest ID and Permit Signature.

An `EIP155OrderRequest` representing the proxied order is returned.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for creating a proxied `EIP155OrderRequestPermitTransaction`.

order\_request\_id

uuid

required

ID of the prepared proxied order to be submitted as a proxied order.

permit\_signature

string

required

`^0x([a-fA-F0-9]{2})*$`

Signature of the permit typed data, allowing Dinari to spend the payment token or dShare asset token on behalf of the owner. Safe wallets can send `0x` to `permit_transaction`.

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Create EIP155 Order Request Permit](https://docs.dinari.com/reference/createeip155orderrequestpermit)[Create EIP155 Order Request Permit Transaction](https://docs.dinari.com/reference/createeip155permittransaction)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Create EIP155 Order Request Permit](https://docs.dinari.com/reference/createeip155orderrequestpermit)[Create EIP155 Order Request Permit Transaction](https://docs.dinari.com/reference/createeip155permittransaction)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Submit EIP155 Order Request","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createeip155permittransaction>>>
---
url: https://docs.dinari.com/reference/createeip155permittransaction
title: Create EIP155 Order Request Permit Transaction
description: Prepare a transaction to be placed on EVM. The returned structure contains the necessary
data to create an `EIP155Transaction` object.

Safe wallets can send `0x` as `permit_signature`. Those orders aren't simulated before they're returned.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Create EIP155 Order Request Permit Transaction

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155/permit\_transaction

Prepare a transaction to be placed on EVM. The returned structure contains the necessary  
data to create an `EIP155Transaction` object.

Safe wallets can send `0x` as `permit_signature`. Those orders aren't simulated before they're returned.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for creating a proxied `EIP155OrderRequestPermitTransaction`.

order\_request\_id

uuid

required

ID of the prepared proxied order to be submitted as a proxied order.

permit\_signature

string

required

`^0x([a-fA-F0-9]{2})*$`

Signature of the permit typed data, allowing Dinari to spend the payment token or dShare asset token on behalf of the owner. Safe wallets can send `0x` to `permit_transaction`.

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Submit EIP155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/eip155/permit\_transaction

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Submit EIP155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create EIP155 Order Request Permit Transaction","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createbatchordercancellation>>>
---
url: https://docs.dinari.com/reference/createbatchordercancellation
title: Cancel Orders
description: Cancel multiple `Orders` by their IDs in a single request. Note that this requires the `Order` IDs, not the `OrderRequest` IDs.
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a
status of PENDING_FILL, PENDING_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Orders` may still be executed
if the cancellation request is not received in time.

The response will indicate which orders were successfully queued to cancel and which failed to queue.
Check the status using the "Get Order by ID" endpoint to confirm whether individual `Orders` have been cancelled.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Cancel Orders

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/cancel

Cancel multiple `Orders` by their IDs in a single request. Note that this requires the `Order` IDs, not the `OrderRequest` IDs.  
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a  
status of PENDING\_FILL, PENDING\_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Orders` may still be executed  
if the cancellation request is not received in time.

The response will indicate which orders were successfully queued to cancel and which failed to queue.  
Check the status using the "Get Order by ID" endpoint to confirm whether individual `Orders` have been cancelled.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for requesting `Order` cancellations from a list of `Order` IDs.

order\_ids

array of uuids

required

List of `Order` IDs to cancel

order\_ids\*

ADD  uuid

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Orders for Entity](https://docs.dinari.com/reference/getentityorders)[Managed Orders](https://docs.dinari.com/reference/managed-orders)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/cancel

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Orders for Entity](https://docs.dinari.com/reference/getentityorders)[Managed Orders](https://docs.dinari.com/reference/managed-orders)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Cancel Orders","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getaccountallorderfulfillments>>>
---
url: https://docs.dinari.com/reference/getaccountallorderfulfillments
title: Query Order Fulfillments
description: Query `OrderFulfillments` under the `Account`.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Query Order Fulfillments

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_fulfillments

Query `OrderFulfillments` under the `Account`.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Query Params

order\_ids

array of uuids

length ≤ 100

List of `Order` IDs to query `AccountOrderFulfillment` for.

order\_ids

ADD  uuid

page

integer

≥ 1

Defaults to 1

page\_size

integer

1 to 100

Defaults to 10

limit

integer

20 to 100

Defaults to 20

Number of results to return

order

string

enum

Defaults to asc

Sort order

ascdesc

Allowed:

`asc``desc`

next

string | null

Cursor for next page

previous

string | null

Cursor for previous page

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Order by ID](https://docs.dinari.com/reference/getorderbyid)[Get Order Fulfillments](https://docs.dinari.com/reference/getaccountorderfulfillments)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_fulfillments

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Order by ID](https://docs.dinari.com/reference/getorderbyid)[Get Order Fulfillments](https://docs.dinari.com/reference/getaccountorderfulfillments)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Query Order Fulfillments","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getaccountorderfulfillmentbyid>>>
---
url: https://docs.dinari.com/reference/getaccountorderfulfillmentbyid
title: Get Order Fulfillment by ID
description: Get a specific `OrderFulfillment` by its ID.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Order Fulfillment by ID

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_fulfillments/{order\_fulfillment\_id}

Get a specific `OrderFulfillment` by its ID.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

order\_fulfillment\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Order Fulfillments](https://docs.dinari.com/reference/getaccountorderfulfillments)[Get Orders for Entity](https://docs.dinari.com/reference/getentityorders)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_fulfillments/{order\_fulfillment\_id}

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Order Fulfillments](https://docs.dinari.com/reference/getaccountorderfulfillments)[Get Orders for Entity](https://docs.dinari.com/reference/getentityorders)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Order Fulfillment by ID","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getaccountorderfulfillments>>>
---
url: https://docs.dinari.com/reference/getaccountorderfulfillments
title: Get Order Fulfillments
description: Get `OrderFulfillments` for a specific `Order`.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Order Fulfillments

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}/fulfillments

Get `OrderFulfillments` for a specific `Order`.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

order\_id

uuid

required

Query Params

page

integer

≥ 1

Defaults to 1

page\_size

integer

1 to 100

Defaults to 10

limit

integer

20 to 100

Defaults to 20

Number of results to return

order

string

enum

Defaults to asc

Sort order

ascdesc

Allowed:

`asc``desc`

next

string | null

Cursor for next page

previous

string | null

Cursor for previous page

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Query Order Fulfillments](https://docs.dinari.com/reference/getaccountallorderfulfillments)[Get Order Fulfillment by ID](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}/fulfillments

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Query Order Fulfillments](https://docs.dinari.com/reference/getaccountallorderfulfillments)[Get Order Fulfillment by ID](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Order Fulfillments","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getentityorders>>>
---
url: https://docs.dinari.com/reference/getentityorders
title: Get Orders for Entity
description: Get a list of all `Orders` under the `Entity`.<br>Optionally `Orders` can be transaction hash or fulfillment transaction hash.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Orders for Entity

get

https://api-enterprise.sbt.dinari.com/api/v2/orders/

Get a list of all `Orders` under the `Entity`.  
Optionally `Orders` can be transaction hash or fulfillment transaction hash.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Query Params

chain\_id

string | null

CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

order\_transaction\_hash

string | null

Transaction hash of the `Order`.

order\_fulfillment\_transaction\_hash

string | null

Fulfillment transaction hash of the `Order`.

order\_request\_id

uuid | null

Order Request ID for the `Order`

page

integer

≥ 1

Defaults to 1

page\_size

integer

1 to 25

Defaults to 10

limit

integer

20 to 100

Defaults to 20

Number of results to return

order

string

enum

Defaults to asc

Sort order

ascdesc

Allowed:

`asc``desc`

next

string | null

Cursor for next page

previous

string | null

Cursor for previous page

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Order Fulfillment by ID](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)[Cancel Orders](https://docs.dinari.com/reference/createbatchordercancellation)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/orders/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Order Fulfillment by ID](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)[Cancel Orders](https://docs.dinari.com/reference/createbatchordercancellation)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Orders for Entity","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getorderbyid>>>
---
url: https://docs.dinari.com/reference/getorderbyid
title: Get Order by ID
description: Get a specific `Order` by its ID.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Order by ID

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}

Get a specific `Order` by its ID.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

order\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Orders](https://docs.dinari.com/reference/getorders)[Query Order Fulfillments](https://docs.dinari.com/reference/getaccountallorderfulfillments)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Orders](https://docs.dinari.com/reference/getorders)[Query Order Fulfillments](https://docs.dinari.com/reference/getaccountallorderfulfillments)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Order by ID","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getorders>>>
---
url: https://docs.dinari.com/reference/getorders
title: Get Orders
description: Get a list of all `Orders` under the `Account`.<br>Optionally `Orders` can be filtered by chain ID, transaction hash, or client order ID.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Get Orders

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders

Get a list of all `Orders` under the `Account`.  
Optionally `Orders` can be filtered by chain ID, transaction hash, or client order ID.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Query Params

chain\_id

string | null

CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

order\_transaction\_hash

string | null

Transaction hash of the `Order`.

client\_order\_id

string | null

Customer-supplied identifier to search for `Order`s.

page

integer

≥ 1

Defaults to 1

page\_size

integer

1 to 25

Defaults to 10

limit

integer

20 to 100

Defaults to 20

Number of results to return

order

string

enum

Defaults to asc

Sort order

ascdesc

Allowed:

`asc``desc`

next

string | null

Cursor for next page

previous

string | null

Cursor for previous page

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Connect an internal Wallet to Account](https://docs.dinari.com/reference/createaccountwalletinternalconnection)[Get Order by ID](https://docs.dinari.com/reference/getorderbyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Connect an internal Wallet to Account](https://docs.dinari.com/reference/createaccountwalletinternalconnection)[Get Order by ID](https://docs.dinari.com/reference/getorderbyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Orders","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createaccountwalletconnection>>>
---
url: https://docs.dinari.com/reference/createaccountwalletconnection
title: Connect Wallet to Account
description: Connect a `Wallet` to the `Account` after verifying the signature.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Connect Wallet to Account

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/wallet/external

Connect a `Wallet` to the `Account` after verifying the signature.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for connecting an `Account` to a `Wallet` owned by the `Entity`.

signature

string

required

`0x[a-fA-F0-9]+`

Signature payload from signing the connection message with the `Wallet`.

nonce

uuid

required

Nonce contained within the connection message.

wallet\_address

string

required

Address of the `Wallet`.

chain\_id

string

enum

required

CAIP-2 formatted chain ID of the blockchain the `Wallet` to link is on. eip155:0 is used for EOA wallets

eip155:1eip155:42161eip155:8453eip155:98866eip155:999eip155:43114eip155:56eip155:5042eip155:1329eip155:202110eip155:0

Show 11 enum values

Responses

# 201 Created

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Wallet Connection Nonce](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)[Connect an internal Wallet to Account](https://docs.dinari.com/reference/createaccountwalletinternalconnection)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/wallet/external

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422default

Updated 7 months ago

---

[Get Wallet Connection Nonce](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)[Connect an internal Wallet to Account](https://docs.dinari.com/reference/createaccountwalletinternalconnection)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Connect Wallet to Account","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createaccountwalletinternalconnection>>>
---
url: https://docs.dinari.com/reference/createaccountwalletinternalconnection
title: Connect an internal Wallet to Account
description: Connect an internal `Wallet` to the `Account`.
fetched: 2026-11-16
method: static
plan: read
---

## Dinari Enterprise API

* [⚠️ Environment](https://docs.dinari.com/reference/environments)
* [Market Data](https://docs.dinari.com/reference/getstocks)
  + [Get Stocksget](https://docs.dinari.com/reference/getstocks)
  + [Get Historical Stock Pricesget](https://docs.dinari.com/reference/getstockpricechart)
  + [Get Stock Splitsget](https://docs.dinari.com/reference/getstocksplits)
  + [Get Stock Splits for Stockget](https://docs.dinari.com/reference/getstocksplitsbyid)
  + [Get News Articles for Stockget](https://docs.dinari.com/reference/getstocknewsbystockid)
  + [Get Stock Dividend Announcementsget](https://docs.dinari.com/reference/getstockdividendsbystockid)
  + [Get Market Hoursget](https://docs.dinari.com/reference/getmarkethours)
  + [Get Stock current priceget](https://docs.dinari.com/reference/getstockcurrentprice)
  + [Get Alloysget](https://docs.dinari.com/reference/getalloys)
  + [Get Alloy current priceget](https://docs.dinari.com/reference/getalloycurrentprice)
  + [Get Historical Alloy Pricesget](https://docs.dinari.com/reference/getalloypricechart)
  + [Get Stock Quoteget](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)
* [Entities](https://docs.dinari.com/reference/getentities)
  + [Get Entitiesget](https://docs.dinari.com/reference/getentities)
  + [Create Entitypost](https://docs.dinari.com/reference/createentities)
  + [Get Current Entityget](https://docs.dinari.com/reference/getcurrententity)
  + [Get Entity by IDget](https://docs.dinari.com/reference/getentitybyid)
  + [Update Entitypatch](https://docs.dinari.com/reference/updateentitybyid)
* [KYC](https://docs.dinari.com/reference/getentitykyc)
  + [Get KYC Dataget](https://docs.dinari.com/reference/getentitykyc)
  + [Submit KYC Datapost](https://docs.dinari.com/reference/createentitykyc)
  + [Get KYC Documentsget](https://docs.dinari.com/reference/getentitykycdocument)
  + [Upload KYC Documentspost](https://docs.dinari.com/reference/createentitykycdocument)
  + [Create Managed KYC Checkpost](https://docs.dinari.com/reference/createmanagedentitykycembed)
* [Accounts](https://docs.dinari.com/reference/getentityaccounts)
  + [Get Accounts for Entityget](https://docs.dinari.com/reference/getentityaccounts)
  + [Create Account for Entitypost](https://docs.dinari.com/reference/createentityaccounts)
  + [Get Account by IDget](https://docs.dinari.com/reference/getaccount)
  + [Deactivate Accountpost](https://docs.dinari.com/reference/createaccountdeactivation)
  + [Get Portfolioget](https://docs.dinari.com/reference/getaccountportfolio)
  + [Get Cash Balancesget](https://docs.dinari.com/reference/getaccountcash)
  + [Get Interest Paymentsget](https://docs.dinari.com/reference/getaccountinterestpayments)
  + [Get Dividend Paymentsget](https://docs.dinari.com/reference/getaccountdividendpayments)
  + [Sandbox Faucetpost](https://docs.dinari.com/reference/createaccountfaucet)
  + [Get TokenTransfersget](https://docs.dinari.com/reference/gettokentransfers)
  + [Create TokenTransferpost](https://docs.dinari.com/reference/createtokentransfers)
  + [Get TokenTransfer by IDget](https://docs.dinari.com/reference/gettokentransfer)
  + [Get Brokerage Account Activitiesget](https://docs.dinari.com/reference/getbrokerageaccountactivities)
* [Wallets](https://docs.dinari.com/reference/getwallet)
  + [Get Walletget](https://docs.dinari.com/reference/getwallet)
  + [Get Wallet Connection Nonceget](https://docs.dinari.com/reference/getaccountwalletconnectionnonce)
  + [Connect Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletconnection)
  + [Connect an internal Wallet to Accountpost](https://docs.dinari.com/reference/createaccountwalletinternalconnection)
* [Orders](https://docs.dinari.com/reference/getorders)
  + [Get Ordersget](https://docs.dinari.com/reference/getorders)
  + [Get Order by IDget](https://docs.dinari.com/reference/getorderbyid)
  + [Query Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountallorderfulfillments)
  + [Get Order Fulfillmentsget](https://docs.dinari.com/reference/getaccountorderfulfillments)
  + [Get Order Fulfillment by IDget](https://docs.dinari.com/reference/getaccountorderfulfillmentbyid)
  + [Get Orders for Entityget](https://docs.dinari.com/reference/getentityorders)
  + [Cancel Orderspost](https://docs.dinari.com/reference/createbatchordercancellation)
* [Managed Orders](https://docs.dinari.com/reference/getlistorderrequests)
  + [List Order Requestsget](https://docs.dinari.com/reference/getlistorderrequests)
  + [Get Order Request by IDget](https://docs.dinari.com/reference/getorderrequestbyid)
  + [Cancel Orderpost](https://docs.dinari.com/reference/createordercancellation)
  + [Create Market Buy Managed Order Requestpost](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)
  + [Create Market Sell Managed Order Requestpost](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)
  + [Create Limit Buy Managed Order Requestpost](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)
  + [Create Limit Sell Managed Order Requestpost](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)
* [Proxied Orders](https://docs.dinari.com/reference/proxied-orders)
* [Withdrawals](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Get Withdrawal Requestsget](https://docs.dinari.com/reference/getaccountwithdrawalrequests)
  + [Create Withdrawal Requestpost](https://docs.dinari.com/reference/createaccountwithdrawalrequests)
  + [Get Withdrawal Request by IDget](https://docs.dinari.com/reference/getaccountwithdrawalrequest)
  + [Get Withdrawalsget](https://docs.dinari.com/reference/getaccountwithdrawals)
  + [Get Withdrawal by IDget](https://docs.dinari.com/reference/getaccountwithdrawal)
* [Order Requests](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Create EIP155 Order Request Permitpost](https://docs.dinari.com/reference/createeip155orderrequestpermit)
  + [Submit EIP155 Order Requestpost](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)
  + [Create EIP155 Order Request Permit Transactionpost](https://docs.dinari.com/reference/createeip155permittransaction)

Powered by

Copy Page

# Connect an internal Wallet to Account

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/wallet/internal

Connect an internal `Wallet` to the `Account`.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

account\_id

uuid

required

Body Params

Input parameters for connecting an `Account` to a `Wallet` owned by the `Entity`.

wallet\_address

string

required

Address of the `Wallet`.

chain\_id

string

enum

required

CAIP-2 formatted chain ID of the blockchain the `Wallet` to link is on. eip155:0 is used for EOA wallets

eip155:1eip155:42161eip155:8453eip155:98866eip155:999eip155:43114eip155:56eip155:5042eip155:1329eip155:202110eip155:0

Show 11 enum values

is\_shared

boolean | null

Is the linked Wallet shared or not

truefalse

Responses

# 201 Created

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Connect Wallet to Account](https://docs.dinari.com/reference/createaccountwalletconnection)[Orders](https://docs.dinari.com/reference/orders)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/wallet/internal

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422default

Updated 7 months ago

---

[Connect Wallet to Account](https://docs.dinari.com/reference/createaccountwalletconnection)[Orders](https://docs.dinari.com/reference/orders)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Connect an internal Wallet to Account","dateModified":"2026-04-20T21:43:36.000Z"}
```