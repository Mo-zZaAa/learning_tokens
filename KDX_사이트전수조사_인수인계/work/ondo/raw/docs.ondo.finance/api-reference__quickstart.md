---
url: https://docs.ondo.finance/api-reference/quickstart
title: Quickstart - Ondo Finance
description: Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Step 1: Onboard to Ondo Stocks & Intelligent Portfolios](https://docs.ondo.finance/api-reference/quickstart)
* [Step 2: Get Your First Price Quote](https://docs.ondo.finance/api-reference/quickstart)
* [Step 3: Request a Soft Quote](https://docs.ondo.finance/api-reference/quickstart)
* [Step 4: Request a Mint Attestation](https://docs.ondo.finance/api-reference/quickstart)
* [Step 5: Submit On-Chain](https://docs.ondo.finance/api-reference/quickstart)
* [Next Steps](https://docs.ondo.finance/api-reference/quickstart)

Home

# Quickstart

Copy pageCopy page

Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.

Copy pageCopy page

## Step 1: Onboard to Ondo Stocks & Intelligent Portfolios

To get started, reach out to [onboarding@ondo.finance](mailto:onboarding@ondo.finance) and let the team know you’re interested in API access. Then head to [app.ondo.finance](https://app.ondo.finance/) to begin the onboarding process. The Ondo team will follow up with instructions to get your API keys.

## Step 2: Get Your First Price Quote

Once you have your API key, try fetching the current price for TSLAon:

```
curl -X GET "https://api.gm.ondo.finance/v1/assets/prices/TSLAon" \
  -H "x-api-key: YOUR_API_KEY"
```

All requests are authenticated via the `x-api-key` header.

## Step 3: Request a Soft Quote

A soft quote provides a non-binding price estimate without impacting your trading limits — useful for displaying pricing in a UI or validating quotes before committing:

```
curl -X POST "https://api.gm.ondo.finance/v1/attestations/soft" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "TSLAon",
    "side": "buy",
    "notionalValue": "1000",
    "duration": "short"
  }'
```

## Step 4: Request a Mint Attestation

When you’re ready to execute, request a binding mint attestation. This creates a signed payload that authorizes an on-chain mint:

```
curl -X POST "https://api.gm.ondo.finance/v1/attestations" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "TSLAon",
    "side": "buy",
    "notionalValue": "1000",
    "duration": "short"
  }'
```

The response includes key fields such as `attestationId`, `signature`, and `expiration` that you’ll need for the on-chain transaction.

## Step 5: Submit On-Chain

Take the attestation `signature` from the response and submit it to the smart contract manager for the asset type, along with USDC or another supported stablecoin, to atomically mint your tokens. See the [smart contract reference](https://docs.ondo.finance/api-reference/smart-contracts) for Ondo Stocks & Intelligent Portfolios contract instructions and addresses.

## Next Steps

* [Error Codes](https://docs.ondo.finance/api-reference/error-codes) — Reference for all API error codes
* [API Caching Strategy](https://docs.ondo.finance/api-reference/endpoint-caching) — Caching durations for each endpoint
* [Smart contract reference](https://docs.ondo.finance/api-reference/smart-contracts) — Contract interface for minting and redeeming
* [Smart contract addresses](https://docs.ondo.finance/addresses) — Contract addresses across supported chains

[Overview](https://docs.ondo.finance/api-reference/overview)[Request a Mint or Redeem Attestation](https://docs.ondo.finance/api-reference/attestations/request-a-mint-or-redeem-attestation)

[x](https://x.com/ondofinance)[github](https://github.com/ondoprotocol)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.ondo.finance/#organization","name":"Ondo Finance","url":"https://docs.ondo.finance","logo":{"@type":"ImageObject","url":"https://mintcdn.com/ondofinance-8a00cd96/KRJ38X1ymyGq9hDd/logo/Ondo-Logo-Black.png?fit=max&auto=format&n=KRJ38X1ymyGq9hDd&q=85&s=8858176a6886b62337d48bad288c4e83"}},{"@type":"WebSite","@id":"https://docs.ondo.finance#website","name":"Ondo Finance","url":"https://docs.ondo.finance","publisher":{"@id":"https://docs.ondo.finance/#organization"}},{"@type":"WebPage","@id":"https://docs.ondo.finance/api-reference/quickstart#webpage","url":"https://docs.ondo.finance/api-reference/quickstart","name":"Quickstart","description":"Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.","dateModified":"2026-09-24T00:59:51.991Z","isPartOf":{"@id":"https://docs.ondo.finance#website"},"breadcrumb":{"@id":"https://docs.ondo.finance/api-reference/quickstart#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.ondo.finance/api-reference/quickstart#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://docs.ondo.finance/api-reference/overview"},{"@type":"ListItem","position":2,"name":"Quickstart","item":"https://docs.ondo.finance/api-reference/quickstart"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.ondo.finance/api-reference/quickstart#article","headline":"Quickstart","name":"Quickstart","description":"Get started with the Ondo Stocks & Intelligent Portfolios API in minutes.","url":"https://docs.ondo.finance/api-reference/quickstart","mainEntityOfPage":{"@id":"https://docs.ondo.finance/api-reference/quickstart#webpage"},"dateModified":"2026-09-24T00:59:51.991Z","publisher":{"@id":"https://docs.ondo.finance/#organization"},"isPartOf":{"@id":"https://docs.ondo.finance#website"}}]}
{"@context":"https://schema.org","@type":"WebSite","name":"Ondo Finance","publisher":{"@type":"Organization","name":"Ondo Finance"},"provider":{"@type":"Organization","name":"Mintlify","url":"https://mintlify.com"}}
```