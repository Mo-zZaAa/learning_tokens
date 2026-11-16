---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action
title: Get Corporate Action - Base Documentation
description: Return a tokenized stock's announced or applied corporate action.
fetched: 2026-11-16
method: render
plan: read
---

Get corporate action

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/corporate-actions/{id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

503

```
{
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "uri": "<string>",
  "contract_address": "<string>",
  "symbol": "<string>",
  "description": "<string>",
  "status": "CORPORATE_ACTION_STATUS_UNSPECIFIED",
  "announced_at": "2023-11-07T05:31:56Z",
  "applied_at": "2023-11-07T05:31:56Z",
  "multiplier_before": 123,
  "multiplier_after": 123,
  "announcements": [
    {
      "announcement_id": "<string>",
      "description": "<string>",
      "tx_hash": "<string>",
      "block_number": "<string>",
      "block_time": "2023-11-07T05:31:56Z"
    }
  ]
}
```

```
{
  "code": 3,
  "message": "field 'id' must be a corporate action UUID"
}
```

```
{
  "code": 5,
  "message": "corporate action \"00000000-0000-4000-8000-000000000001\" was not found"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

Tokenized Stocks API

# Get Corporate Action

Copy pageCopy page

Return a tokenized stock’s announced or applied corporate action.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

corporate-actions

/

{id}

Get corporate action

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/corporate-actions/{id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

503

```
{
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "uri": "<string>",
  "contract_address": "<string>",
  "symbol": "<string>",
  "description": "<string>",
  "status": "CORPORATE_ACTION_STATUS_UNSPECIFIED",
  "announced_at": "2023-11-07T05:31:56Z",
  "applied_at": "2023-11-07T05:31:56Z",
  "multiplier_before": 123,
  "multiplier_after": 123,
  "announcements": [
    {
      "announcement_id": "<string>",
      "description": "<string>",
      "tx_hash": "<string>",
      "block_number": "<string>",
      "block_time": "2023-11-07T05:31:56Z"
    }
  ]
}
```

```
{
  "code": 3,
  "message": "field 'id' must be a corporate action UUID"
}
```

```
{
  "code": 5,
  "message": "corporate action \"00000000-0000-4000-8000-000000000001\" was not found"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

## Find the Action ID

Use the UUID at the end of the `uri` emitted in the token contract’s onchain `Announcement` event. Do not use the event’s `id` argument: it can be numeric or include a suffix such as `:pre` or `-1`. Announcements without an addressable URI cannot be looked up through this endpoint.

## Example

This example retrieves a GOOGLc cash dividend.

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/corporate-actions/e82812a6-0b24-41c4-8ed1-322d1b466d33
```

The response is the corporate action object itself, without a `corporate_action` wrapper. It includes the token, description, status, first announcement time, and onchain announcement history in chronological order.

* `CORPORATE_ACTION_STATUS_ANNOUNCED`: the action is announced but has not changed the token’s multiplier.
* `CORPORATE_ACTION_STATUS_APPLIED`: the multiplier update has been applied. Only then are `applied_at`, `multiplier_before`, and `multiplier_after` populated.

Multiplier values are already normalized from their 18-decimal fixed-point scale. Announcement `block_number` values are decimal strings in JSON.
A malformed UUID returns HTTP `400`; an unknown action or an action on a test/non-live token returns HTTP `404`. Temporarily unavailable or stale action data returns HTTP `503`. These errors use the JSON error format described in the [API overview](https://docs.base.org/sdks/tokenized-stocks/overview).

#### Path Parameters

id

string<uuid>

required

The corporate action UUID from the onchain announcement URI.

#### Response

200

application/json

The corporate action object, not a corporate\_action wrapper.

A corporate action announced on a live tokenized equity token. Applied-only fields are omitted until the multiplier update is applied.

id

string<uuid>

The UUID in the final segment of the onchain announcement URI.

uri

string<uri>

The canonical public URI of this corporate action.

contract\_address

string

The token contract address on Base.

symbol

string

The token ticker symbol.

description

string

The action description, such as Cash Dividend or Stock Split.

status

enum<string>

Whether the action is announced or applied.

Available options:

`CORPORATE_ACTION_STATUS_UNSPECIFIED`,

`CORPORATE_ACTION_STATUS_ANNOUNCED`,

`CORPORATE_ACTION_STATUS_APPLIED`

announced\_at

string<date-time>

The time of the first onchain announcement.

applied\_at

string<date-time>

The time of the multiplier-changing announcement. Omitted until applied.

multiplier\_before

number<double>

The multiplier before application, normalized from its 18-decimal fixed-point value. Omitted until applied.

multiplier\_after

number<double>

The multiplier after application, normalized from its 18-decimal fixed-point value. Omitted until applied.

announcements

object[]

Onchain announcements, oldest first.

Show child attributes

Was this page helpful?

YesNo

[List Cached Prospectuses

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses)[Base Earn API

Next](https://docs.base.org/sdks/base-earn/overview)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- Onchain announcements, oldest first.
- Hide child attributes
- announcements.announcement_id
- string
- The onchain Announcement event id. It may differ from the corporate action UUID, for example by a :pre or -1 suffix.
- announcements.description
- string
- The announcement description.
- announcements.tx_hash
- string
- The transaction hash of the announcement.
- announcements.block_number
- string<uint64>
- The block number, serialized as a decimal string.
- announcements.block_time
- string<date-time>
- The UTC block timestamp of the announcement.

### Close assistant panel 누른 뒤

- Skip to main content
- Assistant
- Responses are generated using AI and may contain mistakes.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "code": 3, "message": "f...

### GET 누른 뒤

- {id}
- Copied

### Report incorrect code 누른 뒤

- 503
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "code": 3, "message": "f...
- curl https://api.coinbase.com/...

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action","name":"Get Corporate Action","description":"Return a tokenized stock's announced or applied corporate action.","dateModified":"2026-10-16T16:44:12.421Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Corporate Action","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action#apireference","headline":"Get Corporate Action","name":"Get Corporate Action","description":"Return a tokenized stock's announced or applied corporate action.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action#webpage"},"dateModified":"2026-10-16T16:44:12.421Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```