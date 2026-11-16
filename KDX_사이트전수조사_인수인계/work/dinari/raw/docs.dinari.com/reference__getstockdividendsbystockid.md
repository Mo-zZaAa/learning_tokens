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