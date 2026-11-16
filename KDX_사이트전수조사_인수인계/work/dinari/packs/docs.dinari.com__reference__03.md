# 읽기 묶음: docs.dinari.com / reference (3/5)


<<<PAGE https://docs.dinari.com/reference/createordercancellation>>>
---
url: https://docs.dinari.com/reference/createordercancellation
title: Cancel Order
description: Cancel an `Order` by its ID. Note that this requires the `Order` ID, not the `OrderRequest` ID.
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a
status of PENDING_FILL, PENDING_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Order` may still be executed
if the cancellation request is not received in time.

Check the status using the "Get Order by ID" endpoint to confirm whether the `Order` has been cancelled.
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

# Cancel Order

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}/cancel

Cancel an `Order` by its ID. Note that this requires the `Order` ID, not the `OrderRequest` ID.  
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a  
status of PENDING\_FILL, PENDING\_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Order` may still be executed  
if the cancellation request is not received in time.

Check the status using the "Get Order by ID" endpoint to confirm whether the `Order` has been cancelled.

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

# 400 Bad Request

# 404 Not Found

# 409 Conflict

# default Default error response

Updated 7 months ago

---

[Get Order Request by ID](https://docs.dinari.com/reference/getorderrequestbyid)[Create Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/orders/{order\_id}/cancel

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200400404409default

Updated 7 months ago

---

[Get Order Request by ID](https://docs.dinari.com/reference/getorderrequestbyid)[Create Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Cancel Order","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getlistorderrequests>>>
---
url: https://docs.dinari.com/reference/getlistorderrequests
title: List Order Requests
description: Lists `OrderRequests`.<br>Optionally `OrderRequests` can be filtered by certain parameters.
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

# List Order Requests

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests

Lists `OrderRequests`.  
Optionally `OrderRequests` can be filtered by certain parameters.

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

order\_request\_id

uuid | null

Order Request ID for the `OrderRequest`

order\_id

uuid | null

Order ID for the `OrderRequest`

client\_order\_id

string | null

Customer-supplied ID to map this `OrderRequest` to an order in their own systems.

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

[Cancel Orders](https://docs.dinari.com/reference/createbatchordercancellation)[Get Order Request by ID](https://docs.dinari.com/reference/getorderrequestbyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Cancel Orders](https://docs.dinari.com/reference/createbatchordercancellation)[Get Order Request by ID](https://docs.dinari.com/reference/getorderrequestbyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"List Order Requests","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getorderrequestbyid>>>
---
url: https://docs.dinari.com/reference/getorderrequestbyid
title: Get Order Request by ID
description: Get a specific `OrderRequest` by its ID.
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

# Get Order Request by ID

get

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/{order\_request\_id}

Get a specific `OrderRequest` by its ID.

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

order\_request\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[List Order Requests](https://docs.dinari.com/reference/getlistorderrequests)[Cancel Order](https://docs.dinari.com/reference/createordercancellation)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/{order\_request\_id}

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[List Order Requests](https://docs.dinari.com/reference/getlistorderrequests)[Cancel Order](https://docs.dinari.com/reference/createordercancellation)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Order Request by ID","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getalloycurrentprice>>>
---
url: https://docs.dinari.com/reference/getalloycurrentprice
title: Get Alloy current price
description: Get the current price for a specified `Alloy`.
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

# Get Alloy current price

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/{alloy\_id}/current\_price

Get the current price for a specified `Alloy`.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

alloy\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Alloys](https://docs.dinari.com/reference/getalloys)[Get Historical Alloy Prices](https://docs.dinari.com/reference/getalloypricechart)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/{alloy\_id}/current\_price

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Alloys](https://docs.dinari.com/reference/getalloys)[Get Historical Alloy Prices](https://docs.dinari.com/reference/getalloypricechart)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Alloy current price","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getalloypricechart>>>
---
url: https://docs.dinari.com/reference/getalloypricechart
title: Get Historical Alloy Prices
description: Get historical price data for a specified `Alloy`. Each index in the array represents a single tick in a price chart.
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

# Get Historical Alloy Prices

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/{alloy\_id}/historical\_prices/

Get historical price data for a specified `Alloy`. Each index in the array represents a single tick in a price chart.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

alloy\_id

uuid

required

Query Params

timespan

string

enum

required

The timespan of the historical prices to query.

DAYWEEK

Allowed:

`DAY``WEEK`

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Alloy current price](https://docs.dinari.com/reference/getalloycurrentprice)[Get Stock Quote](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/{alloy\_id}/historical\_prices/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Alloy current price](https://docs.dinari.com/reference/getalloycurrentprice)[Get Stock Quote](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Historical Alloy Prices","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getalloys>>>
---
url: https://docs.dinari.com/reference/getalloys
title: Get Alloys
description: Returns available `Alloys` with cursor-based pagination.
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

# Get Alloys

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/

Returns available `Alloys` with cursor-based pagination.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Query Params

symbols

array of strings

If set, this endpoint will return Alloys that match the symbols specified

symbols

ADD  string

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

[Get Stock current price](https://docs.dinari.com/reference/getstockcurrentprice)[Get Alloy current price](https://docs.dinari.com/reference/getalloycurrentprice)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/alloys/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Stock current price](https://docs.dinari.com/reference/getstockcurrentprice)[Get Alloy current price](https://docs.dinari.com/reference/getalloycurrentprice)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Alloys","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getmarkethours>>>
---
url: https://docs.dinari.com/reference/getmarkethours
title: Get Market Hours
description: Get the market hours for the current trading session and next open trading session.
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

# Get Market Hours

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/market\_hours/

Get the market hours for the current trading session and next open trading session.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Stock Dividend Announcements](https://docs.dinari.com/reference/getstockdividendsbystockid)[Get Stock current price](https://docs.dinari.com/reference/getstockcurrentprice)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/market\_hours/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Stock Dividend Announcements](https://docs.dinari.com/reference/getstockdividendsbystockid)[Get Stock current price](https://docs.dinari.com/reference/getstockcurrentprice)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Market Hours","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstockcurrentprice>>>
---
url: https://docs.dinari.com/reference/getstockcurrentprice
title: Get Stock current price
description: Get current price for a specified `Stock`.
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

# Get Stock current price

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/current\_price

Get current price for a specified `Stock`.

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

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Market Hours](https://docs.dinari.com/reference/getmarkethours)[Get Alloys](https://docs.dinari.com/reference/getalloys)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/current\_price

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Market Hours](https://docs.dinari.com/reference/getmarkethours)[Get Alloys](https://docs.dinari.com/reference/getalloys)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stock current price","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstockcurrentquotesroutev2>>>
---
url: https://docs.dinari.com/reference/getstockcurrentquotesroutev2
title: Get Stock Quote
description: Get quote for a specified `Stock`.
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

# Get Stock Quote

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/current\_quote

Get quote for a specified `Stock`.

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

feed

string

enum

Requested data source for the quote. Only applies when using x-api-version: 2.  
Allowed values:

* `null`: (default) Selects the highest quality available free data source.
* `sip`: Consolidated quote from all U.S. exchanges (NBBO). This is a paid data source and incurs usage-based billing.

sipnull

Allowed:

`sip``null`

entity\_id

string | null

Entity id of customer requesting quote. Required to use sip feed. If this is an internal query, supply your organization entity\_id

Headers

X-API-Version

string

Version for this method

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 6 months ago

---

[Get Historical Alloy Prices](https://docs.dinari.com/reference/getalloypricechart)[Entities](https://docs.dinari.com/reference/entities)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/current\_quote

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 6 months ago

---

[Get Historical Alloy Prices](https://docs.dinari.com/reference/getalloypricechart)[Entities](https://docs.dinari.com/reference/entities)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stock Quote","dateModified":"2026-06-03T20:55:09.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstockdividendsbystockid>>>
---
url: https://docs.dinari.com/reference/getstockdividendsbystockid
title: Get Stock Dividend Announcements
description: Get a list of announced stock dividend details for a specified `Stock`.

Note that this data applies only to actual stocks. Yield received for holding tokenized shares may differ from this.
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

# Get Stock Dividend Announcements

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/dividends

Get a list of announced stock dividend details for a specified `Stock`.

Note that this data applies only to actual stocks. Yield received for holding tokenized shares may differ from this.

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

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get News Articles for Stock](https://docs.dinari.com/reference/getstocknewsbystockid)[Get Market Hours](https://docs.dinari.com/reference/getmarkethours)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/dividends

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get News Articles for Stock](https://docs.dinari.com/reference/getstocknewsbystockid)[Get Market Hours](https://docs.dinari.com/reference/getmarkethours)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stock Dividend Announcements","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstocknewsbystockid>>>
---
url: https://docs.dinari.com/reference/getstocknewsbystockid
title: Get News Articles for Stock
description: Get the most recent news articles relating to a `Stock`, including a summary of the article 
        and a link to the original source.
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

# Get News Articles for Stock

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/news

Get the most recent news articles relating to a `Stock`, including a summary of the article  
and a link to the original source.

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

limit

integer

1 to 25

Defaults to 10

The number of articles to return.

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Stock Splits for Stock](https://docs.dinari.com/reference/getstocksplitsbyid)[Get Stock Dividend Announcements](https://docs.dinari.com/reference/getstockdividendsbystockid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/news

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Stock Splits for Stock](https://docs.dinari.com/reference/getstocksplitsbyid)[Get Stock Dividend Announcements](https://docs.dinari.com/reference/getstockdividendsbystockid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get News Articles for Stock","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstockpricechart>>>
---
url: https://docs.dinari.com/reference/getstockpricechart
title: Get Historical Stock Prices
description: Get historical price data for a specified `Stock`. Each index in the array represents a single tick in a price chart.
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

# Get Historical Stock Prices

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/historical\_prices/

Get historical price data for a specified `Stock`. Each index in the array represents a single tick in a price chart.

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

timespan

string

enum

required

The timespan of the historical prices to query.

DAYWEEKMONTHYEAR

Allowed:

`DAY``WEEK``MONTH``YEAR`

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Stocks](https://docs.dinari.com/reference/getstocks)[Get Stock Splits](https://docs.dinari.com/reference/getstocksplits)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/{stock\_id}/historical\_prices/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Stocks](https://docs.dinari.com/reference/getstocks)[Get Stock Splits](https://docs.dinari.com/reference/getstocksplits)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Historical Stock Prices","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstocks>>>
---
url: https://docs.dinari.com/reference/getstocks
title: Get Stocks
description: Get a list of `Stocks`.
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

# Get Stocks

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/

Get a list of `Stocks`.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Query Params

symbols

array of strings

length ≤ 100

List of `Stock` symbols to query. If not provided, all `Stocks` are returned.

symbols

ADD  string

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

[⚠️ Environment](https://docs.dinari.com/reference/environments)[Get Historical Stock Prices](https://docs.dinari.com/reference/getstockpricechart)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[⚠️ Environment](https://docs.dinari.com/reference/environments)[Get Historical Stock Prices](https://docs.dinari.com/reference/getstockpricechart)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stocks","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getstocksplits>>>
---
url: https://docs.dinari.com/reference/getstocksplits
title: Get Stock Splits
description: Get a list of stock splits for `Stocks` available for trade via Dinari.
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

# Get Stock Splits

get

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/splits

Get a list of stock splits for `Stocks` available for trade via Dinari.  
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

[Get Historical Stock Prices](https://docs.dinari.com/reference/getstockpricechart)[Get Stock Splits for Stock](https://docs.dinari.com/reference/getstocksplitsbyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/market\_data/stocks/splits

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Historical Stock Prices](https://docs.dinari.com/reference/getstockpricechart)[Get Stock Splits for Stock](https://docs.dinari.com/reference/getstocksplitsbyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Stock Splits","dateModified":"2026-04-20T21:43:36.000Z"}
```