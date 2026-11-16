---
url: https://docs.dinari.com/docs/us
title: US Customers
description: Guide to offering dShares™ to US customers.
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

# US Customers

Guide to offering dShares™ to US customers.

Last Updated: 2026-06-22  
 Compliance Contact: [✉️ [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection)  
 Technical Contact: [✉️ [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection)  
 Service Status: [https://status.dinari.com](https://status.dinari.com/)

## Overview

In the United States, Dinari dShares™ are a secondary ledger for real ownership in the underlying securities and come with all the protections, rights and responsibilities defined by the comprehensive framework set forth by the Securities Act of 1933, Securities Exchange act of 1934, Regulation NMS and many others. The Securities Exchange Commission (SEC) and Financial Industry Regulatory Authority (FINRA) set and enforce compliance and investor protections.

Dinari Securities, LLC operates under SEC and FINRA oversight as a fully registered broker-dealer, while integration partners (such as digital asset or fintech platforms) act solely as introducing or referral platforms for purposes of onboarding and customer access. Partners are not authorized to perform or represent any broker-dealer activities, including but not limited to trade execution, recommendations, or supervisory reviews under FINRA Rule 3110.

Please reach out to us at [✉️ [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection) to get started!

### Serving US Customers

To offer securities to US customers, Dinari Inc. partners with Dinari Securities, LLC, registered broker-dealer CRD #329672, member SEC/FINRA ([🔗 BrokerCheck](https://brokercheck.finra.org/firm/summary/329672)). All US customer accounts are established and maintained by Dinari Securities, LLC under its clearing relationship with Alpaca Securities, LLC.

All regulated activities including customer onboarding, KYC/AML, recordkeeping (Rule 17a-3/17a-4), CAT reporting, and trade surveillance remain the responsibility of Dinari Securities, LLC. Partners must transmit accurate data promptly and ensure all communications or marketing materials do not misrepresent their regulatory status.

### US Customer Qualifications

This guide covers the requirements for customers who are:

* US citizens
* US permanent and temporary residents
* People or are otherwise considered a [🔗 US tax persons](https://www.irs.gov/individuals/international-taxpayers/classification-of-taxpayers-for-us-tax-purposes)

### Requirements

There are some high-level requirements that must be met to have US customer support enabled:

* Additional **Business Verification (KYB) requirements** for your company and a signed supplemental partner agreement.
* Customer identity must be **fully-disclosed** with additional information requirements as specified below.
* Partners may not intermediate or pool orders ("omnibus accounts") for US customers.
* A **verified email** must accompany the entity KYC for voting and other corporate action notifications.
* **Additional onboarding requirements** including agreement and disclosure screens.
* Integration must use **Dinari's API v2** (SDK highly recommended).
* Your product and UI must **strictly adhere** to the guidance in this document and is subject to approval by Dinari.
* A live US customer account must be provided to Dinari Securities for **periodic random auditing** of the onboarding and trading flows.
* Establish and maintain a Compliance Contact and Technical Contact for ongoing communication and testing coordination with Dinari’s Regulatory Technology team.
* Implementation of OFAC and sanctions screening on all inbound wallet funding sources, supplementing Dinari’s own AML systems.

#### Data Security & Recordkeeping Requriments

Partners must comply with Dinari’s Data Security and Recordkeeping Requirements, including:

* Use of encrypted transmission (TLS 1.2+).
* Real-time data push of all customer onboarding and transactional events.
* Support for Dinari’s periodic security validation, integration audit, and penetration testing (at least annually).
* Partners agree to maintain an independent information security certification (e.g., SOC 2 Type II, ISO 27001, or equivalent) or attest annually to Dinari’s information security questionnaire.

### Special Considerations

In addition to the requirements, there are a few special considerations for US customers.

* Issued tokens are currently **non-transferrable** and are restricted from use in DeFi protocols.
* Currently, wrapped dShares™ are not available for US customers.
* Tokens will only be issued to **dedicated wallets**. Omnibus wallets are not currently supported for US users. All US customer wallets must be uniquely associated with verified brokerage accounts; partners may not re-use or pool wallet addresses across multiple users.
* Accounts must be pre-funded (via ACH) or just-in-time funded (more detail below)
* Partners must ensure customer interfaces clearly disclose that digital representations of securities are not blockchain-native tokens for trading or DeFi use.
* Required pre-trade confirmation screen enhancements including metered [National Best Bid & Offer (NBBO) data](https://www.investopedia.com/terms/n/nbbo.asp) provided by Dinari Securities at an additional fee (detailed below).
* Any communications to U.S. persons referencing dShares™ or Dinari Securities must be pre-reviewed and approved by Dinari’s compliance team to ensure adherence to FINRA Rule 2210 (Communications with the Public).
* Partner support teams must redirect all inquiries regarding account disputes, trade errors, or regulatory complaints to Dinari Securities, LLC per FINRA Rule 4513.
* Corporate-action events (dividends, splits, proxy voting) must flow through Dinari’s broker-dealer systems. Partners must not attempt to independently record, issue, or manage any such entitlements.

## Funding Flows

### Wallets

Requirements:

* Dinari supports EOA and standard smart contract wallets for end-users on any supported blockchain.
* End-users must have *dedicated* wallets (not shared or omnibus).
* Wallets *must not* contain any existing dShares™ to avoid jurisdictional conflicts.

Notes:

* Prior to the delivery of dShares™ to the customer's wallet, an on-chain transfer will be deployed to

#### Wallet Service

White-labeled non-custodial wallet services are *coming soon*.

### Stablecoin Funding

The use of stablecoins to fund US customer trades falls under the jurisdiction of state money transmitter laws and federal money services business (MSB) regulations. Dinari partners with **Circle Internet Financial, LLC** to facilitate real-time settlement of trades.

> 📘
>
> Currently, USDC is the only supported settlement stablecoin for US jurisdiction accounts.

Flow Diagram

```
flowchart LR
  CustomerWallet -- stablecoin --> ManagedWallet[Managed Wallet - Dinari]
  ManagedWallet --> 
  Bitgo -- USD --> BrokerageAccount[Brokerage Account Dinari]
```

### Bring-Your-Own-Funding

> 📘
>
> ### Qualified Money Transmitter License Holders
>
> If you are a Money Services Business with the requisite money transmitter licenses, you may qualify to operate your own funding facilitation account to enable just-in-time funding for your customers.

To achieve just-in-time funding for your US customers, partners may open and operate a Funding Facilitation Account (FFA) on Dinari. This account would contain operational a

Flow Diagram

```
flowchart LR
  subgraph Dinari-Side
    PartnerBank
    Partner --> TransferAPI[Transfer API] -- transfer --> PartnerFFA[Partner FFA]
    TransferAPI -- withdraw --> PartnerFFA
    PartnerFFA -- USD (wire withdraw) --> PartnerBank
    PartnerBank -- USD (wire deposit) --> PartnerFFA
    PartnerFFA <-- USD (transfer) --> Customer[Customer Account]
  end

  subgraph Partner-Side
    CustomerWallet -- stablecoin --> PartnerWallet
  end
```

## Onboarding Flow

To ensure compliance with current US securities laws, the following guidance is provided. Required language, links and UI elements will be noted in each step.

> 📘
>
> ### Approval Required
>
> * Any integration, data schema, or workflow changes affecting regulated processes (e.g., KYC flow, funding logic, disclosures) must be submitted to Dinari Compliance for review prior to deployment.
> * Partners must submit final UI screenshots, text, and data-collection steps for compliance approval under FINRA Rule 2210 before public release.

Requirements:

* All onboarding data (PII + KYC fields) must be encrypted in transit and at rest using AES-256 or stronger encryption.

### Offering disclosure

️⚠️ Required screen.

* It must be **clearly** disclosed to US customers that they are becoming customers of Dinari Securities, LLC as their facing broker-dealer.
* Buttons or links out as escape hatches for unqualified users are allowed but must be clearly noted.
* Usage of the Dinari Inc. or Dinari Securities, LLC logos is not required.
* Partners must not modify or abbreviate Dinari-provided disclosure language. Any stylistic change requires pre-approval.
* Partners must surface disclosure content before any account creation or funding event to satisfy SEC electronic-delivery standards.

The following text must be shown **verbatim**.

> Access brokerage services in the US with Dinari Securities LLC
>
> Discover the world of securities trading, offered by Dinari Securities LLC, an SEC registered broker-dealer (member SIPC).

The following subtext must appear **verbatim** at the bottom with live links as shown below.

> Securities offered through Dinari Securities, LLC, registered broker-dealer, member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/). Clearing services are offered through Alpaca Securities LLC, a third-party registered broker-dealer, member FINRA/SIPC. Dinari Securities, LLC and Alpaca Securities, LLC are not affiliated entities.
>
> You can review the background of our broker-dealer on [FINRA’s BrokerCheck](https://brokercheck.finra.org/firm/summary/329672).
>
> This content is provided for informational purposes only and is not intended as and may not be relied on in any manner as investment advice, a recommendation of any interest in any security offered. All investing involves risk, including the loss of principal and may not be suitable for all investors. Investors should consider their own investment goals, risk tolerance, and financial situation before investing. Past performance does not guarantee future results and there is no guarantee any trend will continue.

### Terms & Conditions

️⚠️ Required screen.

The user must be required to check every box to continue with the text and live links **verbatim**.

* I am a US citizen, permanent resident, or other US person for tax purposes.
* Investment Risk - Investing in securities involves risk. The value of your investments can fluctuate, and you could lose money. We will provide you with information about the risks associated with different investments before you make any investment decisions.
* I have read and agree to the Dinari Inc. [Terms of Service](https://dinari.com/terms) and [Privacy Policy](https://dinari.com/privacy).
* I have read and agree to the Dinari Securities, LLC [Terms of Service](https://dinari.com/bd/terms), [Privacy Policy](https://dinari.com/bd/privacy) and [Market Data Terms & Conditions](https://dinari.com/bd/market-data-terms)
* I have read the [Brokerage Agreement](https://dinari.com/bd/brokerage-agreement), [Client Relationship Summary](https://dinari.com/bd/crs) and [Business Continuity Disclosure](https://dinari.com/bd/business-continuity).
* I have read, understood, and agree to be bound by Alpaca Securities LLC and Dinari Securities, LLC account terms, and all other terms, disclosures and disclaimers applicable to me, as referenced in the [Alpaca Customer Agreement](https://files.alpaca.markets/disclosures/library/AcctAppMarginAndCustAgmt.pdf). I also acknowledge that the Alpaca Customer Agreement contains a pre-dispute arbitration clause in Section 44.
* By clicking 'I agree', I understand I am signing this agreement electronically, and that my electronic signature will have the same effect as physically signing and returning the Application.

The button to continue **must** be labeled "I agree".

Other disclosures or agreements may be included on this screen but must be clearly demarcated and separate from the broker-dealer agreements.

### Identity Verification

The following table outlines the required and optional KYC fields for each US user. This can either be all collected when onboarding the user to Dinari Securities, LLC, or an existing onboarding KYC process can be supplemented with the missing fields.

Please refer to the [Identity Verification](https://docs.dinari.com/docs/managing-kyc) documentation for more information on how to submit this information and field names.

* Accounts will only be activated upon full data collection.
* Partners must run sanctions and PEP screening on all new and existing customers at least every 30 days and retain audit evidence.
* Each field must match CIP (Customer Identification Program) standards under the USA PATRIOT Act 31 CFR § 1023.220.
* Partners must immediately report any KYC mismatch or OFAC hit to Dinari Compliance via email to [✉️ [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection)

> ⚠️
>
> ### Verification
>
> Note that all US customer identity information will be verified independently by Dinari Securities, LLC.

| Field | Note |
| --- | --- |
| Legal First Name |  |
| Legal Last Name |  |
| Date of Birth |  |
| Social Security Number |  |
| Residential Address |  |
| Country of Residence |  |
| US citizen | Non-citizens must enter their immigration status or visa information |
| Country of tax residence |  |
| Country of birth | Only required for non-US citizens |
| Country of citizenship | Only required for non-US citizens |
| Visa Type | Only required for visa holders |
| Visa Expiration | Only required for visa holders |
| Date of depature from US | Only required for B1 visa holders |
| Investible / Liquid Assets | **Must show the following segments:** $0 - $19,999  $20,000 - $49,999 $50,000-$99,999 $100,000-$499,999 $500,000+ |
| Employment Status |  |
| Account Funding Source |  |
| Employer |  |
| Employer Address |  |
| Occupation / Job Title |  |
| Special Considerations | **The following checkboxes must be shown verbatim:**   [ ] **Affliated or work with a US registered broker-dealer or FINRA.** - Are you or an immediate family member affiliated with or employed by a stock exchange, regulatory body, member firm of an exchange, FINRA or a municipal securities broker-dealer? [ ] **Senior executive at or a 10% or greater shareholder of a publicly traded company.** - Are you or an immediate family member an officer or 10% or greater shareholder of a publicly traded company, subject to the US Securities Exchange Act 1934? [ ] **I am a family member or relative of a senior political figure.** - Are you or an immediate family member currently or formerly a Politically Exposed Person or Public Official? [ ] I am a senior political figure. [ ] None of the above apply to me or my family. |
| Image of ID | Must be a government issued ID. (Driver's License, Passport, Permanent Resident Card, etc) |

  

### Nonprofessional Status Attestation

⚠️ Required screen.

Users must attest to their non-professional status as this affects the fees assessed by the Market Data providers (see below for fee schedule).

The following text should be shown verbatim and with live links:

> **Nonprofessional Status**
>
> To comply with market data regulations, please confirm your status as a non-professional or professional user.
>
> **A non-professional is generally an individual who:**
>
> * Receives market data solely for personal, non-business use
> * Is not registered or qualified with a securities agency, exchange, or association
> * Does not operate a securities business or act on behalf of an institution
>
> For more information, see the [Market Data Agreement](https://dinari.com/bd/market-data-agreement).
>
> Select one:
>
> ( ) I attest that I am a non-professional user  
>  ( ) I am a professional user

> ⚠️
>
> ### Penalties may apply
>
> Note that back-fees may apply for metered queries of incorrectly categorized people. Please see [Realtime Market Data](https://docs.dinari.com/docs/us) for more information.

### Disclosures

⚠️ Required screen.

A dedicated disclosures screen must be shown to the user following the onboarding process.

* Partners must display Dinari and Alpaca regulatory disclosures verbatim with live links. Removal or rearrangement of legal text is prohibited.
* Partners agree to quarterly compliance audits of displayed disclosures and electronic consent capture.

#### Dinari Inc.

| Document | Link |
| --- | --- |
| Terms of Service | <https://dinari.com/terms> |
| Privacy Policy | <https://dinari.com/privacy> |

#### Dinari Securities, LLC

| Document | Link |
| --- | --- |
| Brokerage Agreement | <https://dinari.com/bd/brokerage-agreement> |
| Client Relationship Summary | <https://dinari.com/bd/crs> |
| Business Continuity Disclosure | <https://dinari.com/bd/business-continuity> |
| Terms of Service | <https://dinari.com/bd/terms> |
| Privacy Policy | <https://dinari.com/bd/privacy> |
| Market Data Terms & Conditions | <https://dinari.com/bd/market-data-terms> |

#### Alpaca Securities, LLC

| Document | Link |
| --- | --- |
| Use and Risk | <https://files.alpaca.markets/disclosures/library/UseAndRisk.pdf> |
| Terms and Conditions | <https://files.alpaca.markets/disclosures/library/TermsAndConditions.pdf> |
| Privacy Notice | <https://files.alpaca.markets/disclosures/library/PrivacyNotice.pdf> |
| Payment for Order Flow Disclosure | <https://files.alpaca.markets/disclosures/library/PFOF.pdf> |
| Margin Disclosure Statement | <https://files.alpaca.markets/disclosures/library/MarginDiscStmt.pdf> |
| Extended Hours Trading Risk Disclosure | <https://files.alpaca.markets/disclosures/library/ExtHrsRisk.pdf> |
| Business Continuity Disclosure | <https://files.alpaca.markets/disclosures/library/BCPSummary.pdf> |
| Customer Relationship Summary | <https://files.alpaca.markets/disclosures/library/FormCRS.pdf> |

### Trusted Contact

⚠️ Optional during onboarding. Required in application.

A trusted contact for all US customers must be supplied. This can either be collected during onboarding or within the application at a later time. A possible design for a modal is shown below

### Accredited Investors

While most assets offered on the Dinari platform are registered US public equities, there are an increasing number of private and unregistered securities that are being offered from private credit funds and index tokens. These types of instruments are only available to [accredited investors](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/accredited-investors).

Assets with accredited investor restrictions will be noted in the [🔗 Get Stocks](https://docs.dinari.com/reference/getstocks) endpoint.

Submission of accreditation attestation for entities is *optional* but they will not be Please refer to the **TBD** API endpoint for submission details.

#### Sample Accredited Investor Attestation (US)

I certify that I am an accredited investor because (check one):

* My individual income has exceeded $200,000 in each of the last two years, and I expect to earn at least that much this year.
* My joint income with my spouse or partner has exceeded $300,000 in each of the last two years, and we expect to earn at least that much this year.
* My individual or joint net worth with my spouse or partner is over $1,000,000, not including my primary residence.

OR

* I am not an accredited investor.

I understand that this information is being relied upon by the issuer to confirm my eligibility as an accredited investor.

## Special Elements

### Asset Listing Page

The listing of tokenized securities cannot be mixed with other types of assets (crypto, non-securities RWAs). They must be presented with the following minimum set of data obtained from the Dinari API:

* Stock Symbol
* Company Name
* Price (Last) in USD
* Change (% or $ or both)

> ⚠️
>
> Listing of non-dShares™ assets is prohibited on this page to avoid confusion.

> ⚠️
>
> ### Text and Links Policy
>
> Text and links outside of the Dinari API News endpoint is generally prohibited on this page.

At the bottom of the listing page must be the following disclaimer verbatim.

> Securities offered through Dinari Securities, LLC, registered broker-dealer, member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/). Clearing services are offered through Alpaca Securities LLC, a third-party registered broker-dealer, member FINRA/SIPC. Dinari Securities, LLC and Alpaca Securities, LLC are not affiliated entities.

### Asset Page

The asset page must contain the following minimum set of data obtained from the Dinari API:

* Price (Last)
* Change (% or $ or both)
* Timestamp (in the local timezone or ET)
* Open Price
* Volume
* Dividend Yield
* 52-week Range
* Market Cap

> ⚠️
>
> Market data must be obtained in its entirety from the Dinari API and cannot be mixed with other data sources.

> ⚠️
>
> Listing of non-dShares™ assets is prohibited on this page to avoid confusion.

> ⚠️
>
> ### Text and Links Policy
>
> Text and links outside of the Dinari API News endpoint is generally prohibited on this page.

At the bottom of the listing page must be the following disclaimer verbatim.

> Securities offered through Dinari Securities, LLC, registered broker-dealer, member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/). Clearing services are offered through Alpaca Securities LLC, a third-party registered broker-dealer, member FINRA/SIPC. Dinari Securities, LLC and Alpaca Securities, LLC are not affiliated entities.

### Pre-trade Confirmation

As required by SEC regulation, US users must be shown National Best Bid & Offer (NBBO) data at the pre-trade confirmation screen.

* Partners must refresh NBBO data every 15 seconds (or more frequently if streaming).

> ⚠️
>
> ### Fees apply.
>
> See the [Realtime Market Data](https://docs.dinari.com/docs/us) section for more information.

In addition to the order confirmation details, the following fields must be shown to the user to satisfy SEC display and trade-through rules. The data is available in the `GetStockQuote` endpoint.

| Field | Note |
| --- | --- |
| Symbol | Stock symbol |
| Bid | The highest available bid (buy-side) price |
| Bid Size | The number of shares available at the best bid price (x100) |
| Bid Exchange | The exchange posting the highest bid price |
| Offer | The lowest available offer (sell-side) price |
| Offer Size | The number of shares available at the best offer price (x100) |
| Offer Exchange | The exchange posting the highest bid price |
| Quote Timestamp | The time the NBBO quote was generated (ET) |

### Realtime Market Data (NBBO)

In addition to the standard market data provided by the API, Real-time (NBBO) Market Data is provided by Dinari Securities, LLC under license by the UTP (NASDAQ) and CTA (NYSE) data services for a fee.

In order to receive real-time NBBO market data, you must pass a `feed` and `entity_id` arguments to the `Get Stock Quote` endpoint.

> ⚠️
>
> Fees apply for usage of real-time market data. See the [Fee Schedule](https://docs.dinari.com/docs/us) for more details.

> ⚠️
>
> ### Required
>
> Usage of real-time market data can be used anywhere but is required on the pre-trade confirmation screen. See the [Pre-trade Confirmation Screen](https://docs.dinari.com/docs/us) section above for more detail.

> 📘
>
> ### Self-sourced NBBO data
>
> Partners with their own sources of NBBO data are not required to use the Dinari data APIs. If you would like to use your own NBBO data sources, please provide copies of your UTP/CTA licenses and the latest audit to [✉️ [email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection).

> ⚠️
>
> ### No-Cache Policy
>
> The `Get Stock Quote` endpoint must not be cached for US customers and can only be used for the sole purpose of displaying quotation data to the end-user. Use of this data for any other reason including non-display analytics is prohibited. Proper usage of this endpoint will be verified prior to going live and upon random auditing.

#### Fee Schedule

Usage of real-time market data is provided for a fee when the following criteria are all met:

* The requesting customer is a US customer.
* When the `Get Stock Quote` endpoint is called with the `feed=sip` and `entity_id=ENTITY_ID`.
* Request is during **Regular Trading Hours**. See [Trading Hours](https://docs.dinari.com/docs/trading-hours) for more details.

If a query does not meet all these conditions then it is provided free of charge.

The current fee per-query is: **$0.0075**.

> 📘
>
> ### Monthly Billed
>
> Partners will receive monthly usage reports and invoices from Dinari for pass-through UTP/CTA fees. Dinari pays all access and redistribution fees for all partners.

Requirements:

* Disputes must be submitted within 30 days of invoice receipt.
* Partners must maintain billing contact information and notify Dinari of changes within five business days.
* Audit records will be provided upon request.

> ✅
>
> ### Capped billing
>
> *Coming soon.* Capped billing is available for your customers with a non-professional attestation on file.

## Compliance Oversight and Audit

* Dinari Securities retains all supervisory authority over U.S. customer activity and may conduct random integration audits to validate compliance with this guide.
* Partners must cooperate with Dinari’s requests for data extracts, logs, or customer records within two business days.
* Significant security incidents or compliance breaches must be reported to Dinari within 24 hours of discovery.

## Marketing and Representation Guidelines

* Partners must not represent themselves as registered broker-dealers or use the Dinari or Alpaca logos without written permission.
* All marketing and promotional materials referencing dShares™ must receive pre-approval from Dinari Compliance.
* Partners must disclose their role accurately as “technology integration partner” or “introducing platform.”

Updated 10 days ago

---

[Regional Requirements](https://docs.dinari.com/docs/regional-requirements)[Restrictions](https://docs.dinari.com/docs/restrictions)

Did this page help you?

Yes

No

Copy Page

* + [Overview](https://docs.dinari.com/docs/us)
  + - [Serving US Customers](https://docs.dinari.com/docs/us)
    - [US Customer Qualifications](https://docs.dinari.com/docs/us)
    - [Requirements](https://docs.dinari.com/docs/us)
    - * [Data Security & Recordkeeping Requriments](https://docs.dinari.com/docs/us)
    - [Special Considerations](https://docs.dinari.com/docs/us)
  + [Funding Flows](https://docs.dinari.com/docs/us)
  + - [Wallets](https://docs.dinari.com/docs/us)
    - * [Wallet Service](https://docs.dinari.com/docs/us)
    - [Stablecoin Funding](https://docs.dinari.com/docs/us)
    - [Bring-Your-Own-Funding](https://docs.dinari.com/docs/us)
  + [Onboarding Flow](https://docs.dinari.com/docs/us)
  + - [Offering disclosure](https://docs.dinari.com/docs/us)
    - [Terms & Conditions](https://docs.dinari.com/docs/us)
    - [Identity Verification](https://docs.dinari.com/docs/us)
    - [Nonprofessional Status Attestation](https://docs.dinari.com/docs/us)
    - [Disclosures](https://docs.dinari.com/docs/us)
    - * [Dinari Inc.](https://docs.dinari.com/docs/us)
      * [Dinari Securities, LLC](https://docs.dinari.com/docs/us)
      * [Alpaca Securities, LLC](https://docs.dinari.com/docs/us)
    - [Trusted Contact](https://docs.dinari.com/docs/us)
    - [Accredited Investors](https://docs.dinari.com/docs/us)
    - * [Sample Accredited Investor Attestation (US)](https://docs.dinari.com/docs/us)
  + [Special Elements](https://docs.dinari.com/docs/us)
  + - [Asset Listing Page](https://docs.dinari.com/docs/us)
    - [Asset Page](https://docs.dinari.com/docs/us)
    - [Pre-trade Confirmation](https://docs.dinari.com/docs/us)
    - [Realtime Market Data (NBBO)](https://docs.dinari.com/docs/us)
    - * [Fee Schedule](https://docs.dinari.com/docs/us)
  + [Compliance Oversight and Audit](https://docs.dinari.com/docs/us)
  + [Marketing and Representation Guidelines](https://docs.dinari.com/docs/us)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"US Customers","dateModified":"2026-11-06T16:24:03.000Z"}
```