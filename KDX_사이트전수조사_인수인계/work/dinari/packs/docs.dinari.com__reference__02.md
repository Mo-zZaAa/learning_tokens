# 읽기 묶음: docs.dinari.com / reference (2/5)


<<<PAGE https://docs.dinari.com/reference/getcurrententity>>>
---
url: https://docs.dinari.com/reference/getcurrententity
title: Get Current Entity
description: Get the current authenticated `Entity`, which represents your organization.
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

# Get Current Entity

get

https://api-enterprise.sbt.dinari.com/api/v2/entities/me

Get the current authenticated `Entity`, which represents your organization.

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

[Create Entity](https://docs.dinari.com/reference/createentities)[Get Entity by ID](https://docs.dinari.com/reference/getentitybyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/me

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Create Entity](https://docs.dinari.com/reference/createentities)[Get Entity by ID](https://docs.dinari.com/reference/getentitybyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Current Entity","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getentities>>>
---
url: https://docs.dinari.com/reference/getentities
title: Get Entities
description: Get a list of direct `Entities` your organization manages. These `Entities` represent individual customers of your organization.
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

# Get Entities

get

https://api-enterprise.sbt.dinari.com/api/v2/entities/

Get a list of direct `Entities` your organization manages. These `Entities` represent individual customers of your organization.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Query Params

reference\_id

string | null

Case sensitive unique reference ID for the `Entity`.

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

[Get Stock Quote](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)[Create Entity](https://docs.dinari.com/reference/createentities)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Stock Quote](https://docs.dinari.com/reference/getstockcurrentquotesroutev2)[Create Entity](https://docs.dinari.com/reference/createentities)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Entities","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getentitybyid>>>
---
url: https://docs.dinari.com/reference/getentitybyid
title: Get Entity by ID
description: Get a specific customer `Entity` of your organization by their ID.
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

# Get Entity by ID

get

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}

Get a specific customer `Entity` of your organization by their ID.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Get Current Entity](https://docs.dinari.com/reference/getcurrententity)[Update Entity](https://docs.dinari.com/reference/updateentitybyid)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Get Current Entity](https://docs.dinari.com/reference/getcurrententity)[Update Entity](https://docs.dinari.com/reference/updateentitybyid)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get Entity by ID","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/updateentitybyid>>>
---
url: https://docs.dinari.com/reference/updateentitybyid
title: Update Entity
description: Update a specific customer `Entity` of your organization.
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

# Update Entity

patch

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}

Update a specific customer `Entity` of your organization.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

Body Params

Input parameters for updating an `Entity`.

reference\_id

string | null

Case sensitive unique reference ID for the `Entity`. We recommend setting this to the unique ID of the `Entity` in your system.

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get Entity by ID](https://docs.dinari.com/reference/getentitybyid)[KYC](https://docs.dinari.com/reference/kyc)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Get Entity by ID](https://docs.dinari.com/reference/getentitybyid)[KYC](https://docs.dinari.com/reference/kyc)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Update Entity","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/environments>>>
---
url: https://docs.dinari.com/reference/environments
title: ⚠️ Environment
description: The contents of this API points to the live environment. To use a different environment, replace the base URL with the intended environment's as shown below: Environment Base Url Sandbox https://api-enterprise.sandbox.dinari.com/api/v2 Live https://api-enterprise.sbt.dinari.com/api/v2
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

# ⚠️ Environment

The contents of this API points to the live environment. To use a different environment, replace the base URL with the intended environment's as shown below:

| Environment | Base Url |
| --- | --- |
| Sandbox | <https://api-enterprise.sandbox.dinari.com/api/v2> |
| Live | <https://api-enterprise.sbt.dinari.com/api/v2> |

Updated about 1 year ago

---

[Market Data](https://docs.dinari.com/reference/market-data)

Did this page help you?

Yes

No

Updated about 1 year ago

---

[Market Data](https://docs.dinari.com/reference/market-data)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"⚠️ Environment","dateModified":"2025-09-29T16:51:47.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createentitykyc>>>
---
url: https://docs.dinari.com/reference/createentitykyc
title: Submit KYC Data
description: Submit KYC data directly, for partners that are provisioned to provide their own KYC data.

This feature is available for everyone in sandbox mode, and for specifically provisioned partners in production.
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

# Submit KYC Data

post

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc

Submit KYC data directly, for partners that are provisioned to provide their own KYC data.

This feature is available for everyone in sandbox mode, and for specifically provisioned partners in production.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

Body Params

BASELINEUS

Input parameters for providing KYC information for an `Entity` in the baseline jurisdiction.

data

object

required

KYC data of the `Entity`.

data object

provider\_name

string

required

length ≥ 1

Name of the KYC provider that provided the KYC information.

jurisdiction

string

enum

Defaults to BASELINE

Jurisdiction of the KYC check.

BASELINE

Allowed:

`BASELINE`

Responses

# 201 Created

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get KYC Data](https://docs.dinari.com/reference/getentitykyc)[Get KYC Documents](https://docs.dinari.com/reference/getentitykycdocument)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422default

Updated 7 months ago

---

[Get KYC Data](https://docs.dinari.com/reference/getentitykyc)[Get KYC Documents](https://docs.dinari.com/reference/getentitykycdocument)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Submit KYC Data","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createentitykycdocument>>>
---
url: https://docs.dinari.com/reference/createentitykycdocument
title: Upload KYC Documents
description: Upload KYC-related documentation for partners that are provisioned to provide their own KYC data.
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

# Upload KYC Documents

post

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/{kyc\_id}/document

Upload KYC-related documentation for partners that are provisioned to provide their own KYC data.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

kyc\_id

uuid

required

Query Params

document\_type

string

enum

required

Type of `KYCDocument` to be uploaded.

GOVERNMENT\_IDSELFIERESIDENCYUNKNOWN

Allowed:

`GOVERNMENT_ID``SELFIE``RESIDENCY``UNKNOWN`

Body Params

File input for uploading a `KYCDocument`.

file

file

required

File to be uploaded. Must be a valid image or PDF file (jpg, jpeg, png, pdf) less than 10MB in size.

Responses

# 201 Created

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Get KYC Documents](https://docs.dinari.com/reference/getentitykycdocument)[Create Managed KYC Check](https://docs.dinari.com/reference/createmanagedentitykycembed)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/{kyc\_id}/document

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422default

Updated 7 months ago

---

[Get KYC Documents](https://docs.dinari.com/reference/getentitykycdocument)[Create Managed KYC Check](https://docs.dinari.com/reference/createmanagedentitykycembed)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Upload KYC Documents","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createmanagedentitykycembed>>>
---
url: https://docs.dinari.com/reference/createmanagedentitykycembed
title: Create Managed KYC Check
description: Create a Dinari-managed KYC Check and get a URL for your end customer to interact with.

The URL points to a web-based KYC interface that can be presented to the end customer for KYC verification.
Once the customer completes this KYC flow, the KYC check will be created and available in the KYC API.
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

# Create Managed KYC Check

post

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/url

Create a Dinari-managed KYC Check and get a URL for your end customer to interact with.

The URL points to a web-based KYC interface that can be presented to the end customer for KYC verification.  
Once the customer completes this KYC flow, the KYC check will be created and available in the KYC API.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

Body Params

Input for creating a managed KYC check.

jurisdiction

string

enum

Defaults to BASELINE

Jurisdiction for the KYC check. Defaults to BASELINE.

BASELINEUS

Allowed:

`BASELINE``US`

Responses

# 200 OK

# 422 Unprocessable Entity

# default Default error response

Updated 7 months ago

---

[Upload KYC Documents](https://docs.dinari.com/reference/createentitykycdocument)[Accounts](https://docs.dinari.com/reference/accounts)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/url

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200422default

Updated 7 months ago

---

[Upload KYC Documents](https://docs.dinari.com/reference/createentitykycdocument)[Accounts](https://docs.dinari.com/reference/accounts)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Managed KYC Check","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getentitykyc>>>
---
url: https://docs.dinari.com/reference/getentitykyc
title: Get KYC Data
description: Get most recent KYC data of the `Entity`.

If there are any completed KYC checks, data from the most recent one will be returned.
If there are no completed KYC checks, the most recent KYC check information, regardless of status, will be returned.
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

# Get KYC Data

get

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc

Get most recent KYC data of the `Entity`.

If there are any completed KYC checks, data from the most recent one will be returned.  
If there are no completed KYC checks, the most recent KYC check information, regardless of status, will be returned.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Update Entity](https://docs.dinari.com/reference/updateentitybyid)[Submit KYC Data](https://docs.dinari.com/reference/createentitykyc)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Update Entity](https://docs.dinari.com/reference/updateentitybyid)[Submit KYC Data](https://docs.dinari.com/reference/createentitykyc)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get KYC Data","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/getentitykycdocument>>>
---
url: https://docs.dinari.com/reference/getentitykycdocument
title: Get KYC Documents
description: Get uploaded documents for a KYC check
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

# Get KYC Documents

get

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/{kyc\_id}/document

Get uploaded documents for a KYC check

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

Loading…

Path Params

entity\_id

uuid

required

kyc\_id

uuid

required

Responses

# 200 OK

# default Default error response

Updated 7 months ago

---

[Submit KYC Data](https://docs.dinari.com/reference/createentitykyc)[Upload KYC Documents](https://docs.dinari.com/reference/createentitykycdocument)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/entities/{entity\_id}/kyc/{kyc\_id}/document

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200default

Updated 7 months ago

---

[Submit KYC Data](https://docs.dinari.com/reference/createentitykyc)[Upload KYC Documents](https://docs.dinari.com/reference/createentitykycdocument)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Get KYC Documents","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createlimitbuymanagedorderrequest>>>
---
url: https://docs.dinari.com/reference/createlimitbuymanagedorderrequest
title: Create Limit Buy Managed Order Request
description: Create a managed `OrderRequest` to place a limit buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.
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

# Create Limit Buy Managed Order Request

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/limit\_buy

Create a managed `OrderRequest` to place a limit buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

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

Input parameters for creating a limit buy `OrderRequest`.

asset\_quantity

number

required

≥ 0

Amount of dShare asset involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places.

limit\_price

number

required

≥ 0

Price at which to execute the order. Must be a positive number with a precision of up to 2 decimal places.

stock\_id

uuid | null

ID of `Stock`.

alloy\_id

uuid | null

ID of `Alloy`.

recipient\_account\_id

uuid | null

ID of `Account` to receive the `Order`.

client\_order\_id

string | null

Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

payment\_token\_address

string | null

Address of the payment token to be used for the payment of the order. If not provided, the default payment token (USD+) will be used.

fee

number | null

≥ 0

Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

Responses

# 201 Created

# 422 Unprocessable Entity

# 423 Locked

# default Default error response

Updated 7 months ago

---

[Create Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)[Create Limit Sell Managed Order Request](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/limit\_buy

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422423default

Updated 7 months ago

---

[Create Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)[Create Limit Sell Managed Order Request](https://docs.dinari.com/reference/createlimitsellmanagedorderrequest)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Limit Buy Managed Order Request","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createlimitsellmanagedorderrequest>>>
---
url: https://docs.dinari.com/reference/createlimitsellmanagedorderrequest
title: Create Limit Sell Managed Order Request
description: Create a managed `OrderRequest` to place a limit sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.
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

# Create Limit Sell Managed Order Request

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/limit\_sell

Create a managed `OrderRequest` to place a limit sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

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

Input parameters for creating a limit sell `OrderRequest`.

asset\_quantity

number

required

≥ 0

Amount of dShare asset involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places.

limit\_price

number

required

≥ 0

Price at which to execute the order. Must be a positive number with a precision of up to 2 decimal places.

stock\_id

uuid | null

ID of `Stock`.

alloy\_id

uuid | null

ID of `Alloy`.

recipient\_account\_id

uuid | null

ID of `Account` to receive the `Order`.

payment\_token\_address

string | null

Address of the payment token to be used for the sell order. If not provided, the default payment token (USD+) will be used. Should only be specified if `recipient_account_id` for a non-managed wallet account is also provided.

client\_order\_id

string | null

Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

fee

number | null

≥ 0

Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

Responses

# 201 Created

# 422 Unprocessable Entity

# 423 Locked

# default Default error response

Updated 7 months ago

---

[Create Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)[Proxied Orders](https://docs.dinari.com/reference/proxied-orders)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/limit\_sell

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422423default

Updated 7 months ago

---

[Create Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)[Proxied Orders](https://docs.dinari.com/reference/proxied-orders)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Limit Sell Managed Order Request","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createmarketbuymanagedorderrequest>>>
---
url: https://docs.dinari.com/reference/createmarketbuymanagedorderrequest
title: Create Market Buy Managed Order Request
description: Create a managed `OrderRequest` to place a market buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.
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

# Create Market Buy Managed Order Request

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/market\_buy

Create a managed `OrderRequest` to place a market buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

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

Input parameters for creating a market buy `OrderRequest`.

payment\_amount

number

required

≥ 0

Amount of currency (USD for US equities and ETFs) to pay for the order.  
Must be a positive number with a precision of up to 2 decimal places.

payment\_token\_address

string | null

Address of the payment token to be used for the payment of the order. If not provided, the default payment token (USD+) will be used.

stock\_id

uuid | null

ID of `Stock`.

alloy\_id

uuid | null

ID of `Alloy`.

recipient\_account\_id

uuid | null

ID of `Account` to receive the `Order`.

client\_order\_id

string | null

Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

fee

number | null

≥ 0

Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

Responses

# 201 Created

# 422 Unprocessable Entity

# 423 Locked

# default Default error response

Updated 7 months ago

---

[Cancel Order](https://docs.dinari.com/reference/createordercancellation)[Create Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/market\_buy

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422423default

Updated 7 months ago

---

[Cancel Order](https://docs.dinari.com/reference/createordercancellation)[Create Market Sell Managed Order Request](https://docs.dinari.com/reference/createmarketsellmanagedorderrequest)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Market Buy Managed Order Request","dateModified":"2026-04-20T21:43:36.000Z"}
```

<<<PAGE https://docs.dinari.com/reference/createmarketsellmanagedorderrequest>>>
---
url: https://docs.dinari.com/reference/createmarketsellmanagedorderrequest
title: Create Market Sell Managed Order Request
description: Create a managed `OrderRequest` to place a market sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.
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

# Create Market Sell Managed Order Request

post

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/market\_sell

Create a managed `OrderRequest` to place a market sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

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

Input parameters for creating a market sell `OrderRequest`.

asset\_quantity

number

required

≥ 0

Quantity of shares to trade. Must be a positive number with a precision of up to 6 decimal places.

stock\_id

uuid | null

ID of `Stock`.

alloy\_id

uuid | null

ID of `Alloy`.

recipient\_account\_id

uuid | null

ID of `Account` to receive the `Order`.

payment\_token\_address

string | null

Address of the payment token to be used for the sell order. If not provided, the default payment token (USD+) will be used. Should only be specified if `recipient_account_id` for a non-managed wallet account is also provided.

client\_order\_id

string | null

Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

fee

number | null

≥ 0

Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

Responses

# 201 Created

# 422 Unprocessable Entity

# 423 Locked

# default Default error response

Updated 7 months ago

---

[Create Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)[Create Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)

Did this page help you?

Yes

No

Language

ShellNodeRubyPHPPython

Credentials

Header +1

URL

Base URL

https://api-enterprise.sbt.dinari.com/api/v2/accounts/{account\_id}/order\_requests/market\_sell

```
Loading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

201422423default

Updated 7 months ago

---

[Create Market Buy Managed Order Request](https://docs.dinari.com/reference/createmarketbuymanagedorderrequest)[Create Limit Buy Managed Order Request](https://docs.dinari.com/reference/createlimitbuymanagedorderrequest)

Did this page help you?

Yes

No

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Market Sell Managed Order Request","dateModified":"2026-04-20T21:43:36.000Z"}
```