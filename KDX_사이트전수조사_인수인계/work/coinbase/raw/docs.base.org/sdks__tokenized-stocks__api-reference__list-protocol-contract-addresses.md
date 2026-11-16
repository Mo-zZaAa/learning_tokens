---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses
title: List Protocol Contract Addresses - Base Documentation
description: Return the tokenized-stocks protocol contracts deployed on each supported chain.
fetched: 2026-11-16
method: render
plan: read
---

List protocol contract addresses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/chains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

default

```
{
  "chains": [
    {
      "chain_id": "<string>",
      "chain": "<string>",
      "policy_registry_address": "<string>",
      "token_supply_manager_address": "<string>",
      "token_factory_address": "<string>"
    }
  ]
}
```

```
{
  "code": 123,
  "message": "<string>",
  "details": [
    {
      "@type": "<string>"
    }
  ]
}
```

Tokenized Stocks API

# List Protocol Contract Addresses

Copy pageCopy page

Return the tokenized-stocks protocol contracts deployed on each supported chain.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

chains

List protocol contract addresses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/chains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

default

```
{
  "chains": [
    {
      "chain_id": "<string>",
      "chain": "<string>",
      "policy_registry_address": "<string>",
      "token_supply_manager_address": "<string>",
      "token_factory_address": "<string>"
    }
  ]
}
```

```
{
  "code": 123,
  "message": "<string>",
  "details": [
    {
      "@type": "<string>"
    }
  ]
}
```

## Example

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/chains
```

#### Response

200

application/json

A successful response.

Response message for `TokenizedEquitiesPublicApiService.ListChainContractAddresses`.

chains

object[]

The tokenized-equities protocol contract addresses for each supported chain.

Show child attributes

Was this page helpful?

YesNo

[List Tokenized Stocks

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks)[Get Token Total Supply

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- The tokenized-equities protocol contract addresses for each supported chain.
- Hide child attributes
- chains.chain_id
- string<uint64>
- The chain's numeric EVM chain ID.
- chains.chain
- string
- The chain's human-readable name.
- chains.policy_registry_address
- string
- The address of the PolicyRegistry contract or precompile.
- chains.token_supply_manager_address
- string
- The address of the TokenSupplyManager contract.
- chains.token_factory_address
- string
- The address of the TokenFactory contract.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "code": 123, "message": ...

### GET 누른 뒤

- chains
- Copied

### Report incorrect code 누른 뒤

- default
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "code": 123, "message": ...
- curl https://api.coinbase.com/...

### Yes 누른 뒤

- No
- Great! What worked best for you?
- The guide worked as expected
- It was easy to find the information I needed
- It was easy to understand the product and features
- The documentation is up to date
- Something else
- Cancel
- Submit feedback

### No 누른 뒤

- No
- How can we improve our product?
- Help me get started faster
- Make it easier to find what I'm looking for
- Make it easy to understand the product and features
- Update this documentation

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses","name":"List Protocol Contract Addresses","description":"Return the tokenized-stocks protocol contracts deployed on each supported chain.","dateModified":"2026-09-24T23:40:18.709Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"List Protocol Contract Addresses","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses#apireference","headline":"List Protocol Contract Addresses","name":"List Protocol Contract Addresses","description":"Return the tokenized-stocks protocol contracts deployed on each supported chain.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses#webpage"},"dateModified":"2026-09-24T23:40:18.709Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```