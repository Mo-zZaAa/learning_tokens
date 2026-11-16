---
url: https://docs.dinari.com/reference/order-requests
title: Create EIP155 Order Request Permit
description: Generates a permit that can be signed and used to create an OrderRequest using Dinari's EVM smart contracts.
This is a convenience method to prepare the transactions needed to create an OrderRequest using Dinari's EVM smart contracts. Once signed, the transactions can be sent to the EVM network to c…
fetched: 2026-11-16
method: render
plan: skim
---

`CTRL-/`

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
| Make a request to see history. | | | |

0 Requests This Month

#### URL Expired

The URL for this request expired after 30 days.

Close

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

Response body

object

status

integer

required

HTTP status code

message

string

required

Human-readable message

error\_id

string

required

Reference Id for Dinari support

error

string

Additional context and information

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

cURL Request

Examples

```
```
xxxxxxxxxx
```

12

1

```
curl --request POST \
```

2

```
     --url https://api-enterprise.sbt.dinari.com/api/v2/accounts/account_id/order_requests/eip155/permit \
```

3

```
     --header 'accept: application/json' \
```

4

```
     --header 'content-type: application/json' \
```

5

```
     --data '
```

6

```
{
```

7

```
  "chain_id": "eip155:1",
```

8

```
  "order_tif": "DAY",
```

9

```
  "order_side": "BUY",
```

10

```
  "order_type": "MARKET"
```

11

```
}
```

12

```
'
```
```

Try It!

default

```
```
xxxxxxxxxx
```

12

5

1

```
{
```

2

```
  "status": 0,
```

3

```
  "message": "string",
```

4

```
  "error_id": "string"
```

5

```
}
```
```

Updated 7 months ago

---

[Get Withdrawal by ID](https://docs.dinari.com/reference/getaccountwithdrawal)[Submit EIP155 Order Request](https://docs.dinari.com/reference/createeip155orderrequestpermittransaction)

Did this page help you?

Yes

No

## 펼치거나 눌러야 보이던 내용

- Defaults to 422
- Defaults to Unprocessable Entity
- field_errors
- array of objects
- Contains list of field-specific errors
- field_name
- Name of field with error
- field_error
- Description of error
- body_error
- Description of body-specific error (ex. JSON issues)
- "error_id": "string",
- "error": {
- "field_errors": [
- "field_name": "string",
- "field_error": "string"
- "body_error": "string"

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create EIP155 Order Request Permit","dateModified":"2026-04-20T21:43:36.000Z"}
```