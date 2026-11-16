# 읽기 묶음: docs.base.org / sdks (1/1)


<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action>>>
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

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon
title: Get Token Icon - Base Documentation
description: Redirect to a tokenized stock's icon using its ticker symbol.
fetched: 2026-11-16
method: render
plan: read
---

Get token icon

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/images/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

404

503

```
404 page not found
```

```
<string>
```

Tokenized Stocks API

# Get Token Icon

Copy pageCopy page

Redirect to a tokenized stock’s icon using its ticker symbol.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

images

/

{symbol}

Get token icon

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/images/{symbol}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

404

503

```
404 page not found
```

```
<string>
```

## Example

Use the token symbol, including its token suffix. Symbols are case-insensitive; the `.png` suffix is optional.

cURL

```
curl -L https://api.coinbase.com/v1/tokenized-stocks/images/TSLAc.png --output TSLAc.png
```

The endpoint returns HTTP `302` with the image URL in the `Location` header. The `-L` flag follows the redirect to download the image. This endpoint does not return a JSON metadata document.
An unknown symbol returns HTTP `404`. Token data that is temporarily unavailable returns HTTP `503`. These errors have plain-text bodies.

#### Path Parameters

symbol

string

required

The token ticker symbol, optionally followed by .png.

#### Response

302

Redirect to the current asset URL. Follow the Location header; the response is not a JSON document.

Was this page helpful?

YesNo

[Get Token Metadata

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata)[Get Token Prospectus

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {symbol}
- Copied

### Report incorrect code 누른 뒤

- 503
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- <string>
- curl -L https://api.coinbase.c...

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon","name":"Get Token Icon","description":"Redirect to a tokenized stock's icon using its ticker symbol.","dateModified":"2026-10-16T16:44:12.420Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Icon","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#apireference","headline":"Get Token Icon","name":"Get Token Icon","description":"Redirect to a tokenized stock's icon using its ticker symbol.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon#webpage"},"dateModified":"2026-10-16T16:44:12.420Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata
title: Get Token Metadata - Base Documentation
description: Return a tokenized stock's contractURI-compatible metadata document.
fetched: 2026-11-16
method: render
plan: read
---

Get token metadata

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/metadata/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

404

503

```
{
  "contract_address": "<string>",
  "name": "<string>",
  "symbol": "<string>",
  "image": "<string>",
  "prospectus_url": "<string>",
  "description": "<string>",
  "adgm_isin": "<string>"
}
```

```
{
  "code": 5,
  "message": "ticker \"UNKNOWNC\" is not a listed tokenized equity token"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

Tokenized Stocks API

# Get Token Metadata

Copy pageCopy page

Return a tokenized stock’s contractURI-compatible metadata document.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

metadata

/

{ticker}

Get token metadata

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/metadata/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

404

503

```
{
  "contract_address": "<string>",
  "name": "<string>",
  "symbol": "<string>",
  "image": "<string>",
  "prospectus_url": "<string>",
  "description": "<string>",
  "adgm_isin": "<string>"
}
```

```
{
  "code": 5,
  "message": "ticker \"UNKNOWNC\" is not a listed tokenized equity token"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
}
```

## Example

Use the token symbol, including its token suffix, such as `TSLAc`. Ticker lookup is case-insensitive.

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/metadata/TSLAc
```

The response contains `contract_address`, `name`, `symbol`, `description`, `image`, and `prospectus_url`. It also includes `adgm_isin`, the ADGM ISIN of the tokenized security, when available. The image and prospectus URLs are stable API links that redirect to the current assets. A `prospectus_url` does not guarantee that a PDF is currently cached; check [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) for available tickers.

#### Path Parameters

ticker

string

required

The token ticker symbol, including its token suffix. Lookup is case-insensitive.

#### Response

200

application/json

Token metadata.

A contractURI-compatible metadata document for a listed tokenized stock.

contract\_address

string

The ERC-20 token contract address on Base.

name

string

The name of the underlying equity.

symbol

string

The token ticker symbol.

image

string<uri>

Stable API URL that redirects to the current token icon.

prospectus\_url

string<uri>

Stable API URL that redirects to the approved prospectus when available. Use GET /v1/tokenized-stocks/prospectuses to discover cached prospectuses.

description

string

The same human-readable tokenized-stock description returned in the token list.

adgm\_isin

string

The ADGM ISIN of the tokenized security, taken from its approved primary prospectus. Distinct from the underlying stock's ISIN. Omitted when unavailable.

Was this page helpful?

YesNo

[Get Token Total Supply

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply)[Get Token Icon

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "contract_address": "<stri...

### GET 누른 뒤

- {ticker}
- Copied

### Report incorrect code 누른 뒤

- 503
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "contract_address": "<stri...
- curl https://api.coinbase.com/...

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata","name":"Get Token Metadata","description":"Return a tokenized stock's contractURI-compatible metadata document.","dateModified":"2026-11-09T12:27:23.982Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Metadata","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#apireference","headline":"Get Token Metadata","name":"Get Token Metadata","description":"Return a tokenized stock's contractURI-compatible metadata document.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata#webpage"},"dateModified":"2026-11-09T12:27:23.982Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus
title: Get Token Prospectus - Base Documentation
description: Redirect to a tokenized stock's approved prospectus PDF.
fetched: 2026-11-16
method: render
plan: read
---

Get token prospectus

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectus/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

400

404

```
invalid ticker
```

```
404 page not found
```

Tokenized Stocks API

# Get Token Prospectus

Copy pageCopy page

Redirect to a tokenized stock’s approved prospectus PDF.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

prospectus

/

{ticker}

Get token prospectus

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectus/{ticker}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

400

404

```
invalid ticker
```

```
404 page not found
```

## Example

Use the token ticker, including its token suffix. Tickers are case-insensitive; the `.pdf` suffix is optional. Dotted share-class tickers such as `BRK.Bc` are supported.

cURL

```
curl -L https://api.coinbase.com/v1/tokenized-stocks/prospectus/TSLAc.pdf --output TSLAc.pdf
```

The endpoint returns HTTP `302` with the approved prospectus PDF URL in the `Location` header. When a ticker has several documents, it redirects to the first one in the order that [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) returns: primary first, then newest approval date, then URL. The `-L` flag follows the redirect to download the PDF. This endpoint does not return JSON.
A malformed ticker returns HTTP `400`. A ticker with no available prospectus returns HTTP `404`. These errors have plain-text bodies. Use [List Cached Prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses) to discover available tickers.

#### Path Parameters

ticker

string

required

The token ticker symbol, optionally followed by .pdf.

#### Response

302

Redirect to the current asset URL. Follow the Location header; the response is not a JSON document.

Was this page helpful?

YesNo

[Get Token Icon

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon)[List Cached Prospectuses

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {ticker}
- Copied

### Report incorrect code 누른 뒤

- 404
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- 404 page not found
- curl -L https://api.coinbase.c...

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus","name":"Get Token Prospectus","description":"Redirect to a tokenized stock's approved prospectus PDF.","dateModified":"2026-10-29T15:40:34.969Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Prospectus","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#apireference","headline":"Get Token Prospectus","name":"Get Token Prospectus","description":"Redirect to a tokenized stock's approved prospectus PDF.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus#webpage"},"dateModified":"2026-10-29T15:40:34.969Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply
title: Get Token Total Supply - Base Documentation
description: Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.
fetched: 2026-11-16
method: render
plan: read
---

Get token total supply

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/total-supply/{contract_address}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

default

```
123
```

```
{
  "code": 3,
  "message": "field 'contract_address' must be a 20-byte hex address"
}
```

```
{
  "code": 5,
  "message": "contract_address \"0x0000000000000000000000000000000000000001\" is not a supported tokenized equity token"
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

# Get Token Total Supply

Copy pageCopy page

Return a tokenized stock’s ERC-20 total supply, normalized by the token’s decimals.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

total-supply

/

{contract\_address}

Get token total supply

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/total-supply/{contract_address}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

404

default

```
123
```

```
{
  "code": 3,
  "message": "field 'contract_address' must be a 20-byte hex address"
}
```

```
{
  "code": 5,
  "message": "contract_address \"0x0000000000000000000000000000000000000001\" is not a supported tokenized equity token"
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

This example uses AMDc. For other tokens, use an address returned by [List Tokenized Stocks](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks).

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/total-supply/0xB2000000000000000000000d8Ce462E99ee7A47B
```

The response is a JSON number, not an object with a `total_supply` property. It is normalized by the token’s decimals, so do not divide it again.
A malformed contract address returns HTTP `400` with service code `3`. A correctly formatted address that is not a supported tokenized equity token returns HTTP `404` with service code `5`.

#### Path Parameters

contract\_address

string

required

The address of the ERC-20 token contract on Base. Find token addresses on the [Base assets page](https://www.base.org/assets) or from `GET /v1/tokenized-stocks`.

Pattern: `^0x[a-fA-F0-9]{40}$`

#### Response

200

application/json

The token's total supply, normalized by the token's decimals. This is a token-unit amount, not the number of underlying shares; multiply by `multiplier` to convert to shares.

The response is of type `number<double>`.

Was this page helpful?

YesNo

[List Protocol Contract Addresses

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses)[Get Token Metadata

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata)

## 펼치거나 눌러야 보이던 내용

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### GET 누른 뒤

- {contract_address}
- Copied

### Report incorrect code 누른 뒤

- default
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- 123
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

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply","name":"Get Token Total Supply","description":"Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.","dateModified":"2026-10-16T16:44:12.419Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"Get Token Total Supply","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#apireference","headline":"Get Token Total Supply","name":"Get Token Total Supply","description":"Return a tokenized stock's ERC-20 total supply, normalized by the token's decimals.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply#webpage"},"dateModified":"2026-10-16T16:44:12.419Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses
title: List Cached Prospectuses - Base Documentation
description: List cached approved prospectus documents by ticker, with ISINs when known.
fetched: 2026-11-16
method: render
plan: read
---

List cached prospectuses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectuses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

```
{
  "prospectuses": [
    {
      "ticker": "SKYDC",
      "isin": "US69932A2042",
      "documents": [
        {
          "type": "primary",
          "approval_date": "2026-10-12",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---prospectus-pskyc---12oct2026_10_12_2026_16-24-26.pdf"
        },
        {
          "type": "supplementary",
          "approval_date": "2026-10-19",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---supplementary-prospectus-pskyc---19oct2026_10_19_2026_13-29-29.pdf"
        }
      ]
    }
  ]
}
```

Tokenized Stocks API

# List Cached Prospectuses

Copy pageCopy page

List cached approved prospectus documents by ticker, with ISINs when known.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

/

prospectuses

List cached prospectuses

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks/prospectuses', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

```
{
  "prospectuses": [
    {
      "ticker": "SKYDC",
      "isin": "US69932A2042",
      "documents": [
        {
          "type": "primary",
          "approval_date": "2026-10-12",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---prospectus-pskyc---12oct2026_10_12_2026_16-24-26.pdf"
        },
        {
          "type": "supplementary",
          "approval_date": "2026-10-19",
          "url": "https://www.adgm.com/globalassets/market-disclosure/content/prospectus/coinbase-onchain-spv-ltd---supplementary-prospectus-pskyc---19oct2026_10_19_2026_13-29-29.pdf"
        }
      ]
    }
  ]
}
```

## Example

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks/prospectuses
```

The response contains a `prospectuses` array, sorted alphabetically by uppercase ticker. Each entry includes `ticker`, the underlying equity’s `isin` when known, and a `documents` array. A ticker can have several documents, such as a primary prospectus and a later supplement.
Each document has these fields:

| Field | Description |
| --- | --- |
| `type` | `primary` or `supplementary` |
| `approval_date` | Approval date in `YYYY-MM-DD` format |
| `url` | Direct URL to the approved PDF |

Documents are ordered primary first, then newest approval date, then URL.
To get a single PDF for a ticker, use [Get Token Prospectus](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus), which redirects to the first document in this order.
The prospectus cache refreshes in the background. Before a successful refresh, the cache can be empty and the `prospectuses` field can be omitted. This is a prospectus-availability list, not a list of tokens available for trading.

#### Response

200 - application/json

Cached prospectuses.

The currently cached prospectuses, one entry per uppercase ticker, sorted alphabetically by ticker. The prospectuses field can be omitted when the cache is empty.

prospectuses

object[]

Show child attributes

Was this page helpful?

YesNo

[Get Token Prospectus

Previous](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus)[Get Corporate Action

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- object[]
- Hide child attributes
- prospectuses.ticker
- string
- The uppercase token ticker, including its token suffix, such as TSLAC.
- prospectuses.isin
- string
- The underlying equity ISIN. Omitted when not yet known from cached metadata.
- prospectuses.documents
- object[]
- Every cached primary and supplementary document for this ticker, ordered primary first, then newest approval date, then URL.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "prospectuses": [ { ...

### GET 누른 뒤

- prospectuses
- Copied

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
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses","name":"List Cached Prospectuses","description":"List cached approved prospectus documents by ticker, with ISINs when known.","dateModified":"2026-11-13T14:02:19.652Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"List Cached Prospectuses","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#apireference","headline":"List Cached Prospectuses","name":"List Cached Prospectuses","description":"List cached approved prospectus documents by ticker, with ISINs when known.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses#webpage"},"dateModified":"2026-11-13T14:02:19.652Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses>>>
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

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks
title: List Tokenized Stocks - Base Documentation
description: Return the Coinbase-issued tokenized-stock records currently exposed through the API.
fetched: 2026-11-16
method: render
plan: read
---

List tokenized stocks

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks?page_size=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

503

default

```
{
  "tokens": [
    {
      "contract_address": "<string>",
      "symbol": "<string>",
      "name": "<string>",
      "decimals": 123,
      "icon_url": "<string>",
      "total_supply": 123,
      "isin": "<string>",
      "adgm_isin": "<string>",
      "multiplier": 123,
      "paused_features": [
        123
      ],
      "nav_price": 123,
      "nav_price_updated_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "first_mint_date": "2023-11-07T05:31:56Z"
    }
  ],
  "next_page_token": "<string>"
}
```

```
{
  "code": 3,
  "message": "page_size must not be negative"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
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

# List Tokenized Stocks

Copy pageCopy page

Return the Coinbase-issued tokenized-stock records currently exposed through the API.

Copy pageCopy page

GET

/

v1

/

tokenized-stocks

List tokenized stocks

JavaScript

```
const options = {method: 'GET'};

fetch('https://api.coinbase.com/v1/tokenized-stocks?page_size=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

200

400

503

default

```
{
  "tokens": [
    {
      "contract_address": "<string>",
      "symbol": "<string>",
      "name": "<string>",
      "decimals": 123,
      "icon_url": "<string>",
      "total_supply": 123,
      "isin": "<string>",
      "adgm_isin": "<string>",
      "multiplier": 123,
      "paused_features": [
        123
      ],
      "nav_price": 123,
      "nav_price_updated_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "first_mint_date": "2023-11-07T05:31:56Z"
    }
  ],
  "next_page_token": "<string>"
}
```

```
{
  "code": 3,
  "message": "page_size must not be negative"
}
```

```
{
  "code": 14,
  "message": "data is temporarily unavailable"
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
curl https://api.coinbase.com/v1/tokenized-stocks
```

## Pagination

The default page size is `100` when `page_size` is omitted or `0`. Values above `500` are capped at `500`. Negative page sizes and malformed page sizes or cursors return HTTP `400`.
Pass the response’s `next_page_token` as `page_token` to retrieve the next page, keeping other parameters unchanged. Continue until `next_page_token` is omitted. Tokens are ordered by contract address.

## Response Fields

The token schema includes `description` and `first_mint_date`. The first-mint date is the UTC block timestamp of the token’s first positive mint, not its deployment time. It can be absent if never minted or not yet resolved.
Default-valued scalar fields, empty arrays, and unset timestamps can be omitted. For example, a zero supply may be absent from the list. Check the [response field guidance](https://docs.base.org/sdks/tokenized-stocks/overview) before interpreting missing supply or NAV data.

#### Query Parameters

page\_size

integer<int32>

default:100

The maximum number of records to return in one page. Defaults to 100 when omitted or zero. Values above 500 are capped at 500; negative values return HTTP 400.

Required range: `x >= 0`

page\_token

string

The `next_page_token` value from a previous response. Pass it to fetch the next page of records. Keep other request parameters unchanged between pages. A malformed cursor returns HTTP 400.

#### Response

200

application/json

A successful response.

Response message for `TokenizedEquitiesPublicApiService.ListTokenizedEquityTokens`.

tokens

object[]

The tokenized-stock records in this page.

Show child attributes

next\_page\_token

string

A token for fetching the next page. Pass it as `page_token` in the next request. Omitted on the last page.

Was this page helpful?

YesNo

[Tokenized Stocks API

Previous](https://docs.base.org/sdks/tokenized-stocks/overview)[List Protocol Contract Addresses

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses)

## 펼치거나 눌러야 보이던 내용

### Show child attributes 누른 뒤

- The tokenized-stock records in this page.
- Hide child attributes
- tokens.contract_address
- string
- The address of the ERC-20 token contract on Base.
- tokens.symbol
- string
- The token's ticker symbol.
- tokens.name
- string
- The name of the underlying equity.
- tokens.decimals
- integer<int64>
- The number of decimals used by the token.
- tokens.icon_url
- string
- URL of an icon representing the underlying equity.
- tokens.total_supply
- number<double>
- The token's total supply, normalized by the token's decimals. This is a token-unit amount, not the number of underlying shares; multiply by multiplier to convert to shares.
- tokens.isin
- string
- The ISIN of the underlying equity.
- tokens.adgm_isin
- string
- The ADGM ISIN of the tokenized security, taken from its approved primary prospectus. Distinct from the underlying stock's ISIN. Omitted when unavailable.
- tokens.multiplier
- number<double>
- The token's current scaling factor between token units and underlying shares, adjusted for its 18-decimal fixed-point scale (1.0 means no adjustment). It can change for corporate actions such as dividends or stock splits.
- tokens.paused_features
- integer<int64>[]
- Feature flags currently paused on the token contract.
- tokens.nav_price
- number<double>
- The most recently published Chainlink-based NAV/reference value for the token, read from its Chainlink price feed on Base and adjusted for the feed's decimals. This is a total-return reference value, not a live bid/ask or execution price. Check nav_price_updated_at and apply staleness bounds before relying on it.
- tokens.nav_price_updated_at
- string<date-time>
- The time at which nav_price was last updated onchain, per the Chainlink feed's latestRoundData() updatedAt. Chainlink only publishes a new round when the price moves past a deviation threshold or the heartbeat elapses, and feeds stop updating outside market hours, so this can lag wall-clock time by minutes to many hours. Apply staleness bounds before relying on nav_price.
- tokens.description
- string
- A human-readable description of the tokenized stock, based on its name and symbol.
- tokens.first_mint_date
- string<date-time>
- The UTC block timestamp of the first positive ERC-20 mint (Transfer from the zero address), not the contract deployment time. Omitted if never minted or not yet resolved. Later mints or burns do not change this date.

### Ask Assistant 누른 뒤

- Responses are generated using AI and may contain mistakes.
- const options = {method: 'GET'...

### Ask Assistant 누른 뒤

- const options = {method: 'GET'...
- { "tokens": [ { "c...

### GET 누른 뒤

- tokenized-stocks
- Copied

### Report incorrect code 누른 뒤

- default
- Report incorrect code
- Please provide a detailed description of the incorrect code.
- Cancel
- Submit

### Ask Assistant 누른 뒤

- { "tokens": [ { "c...
- curl https://api.coinbase.com/...

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks","name":"List Tokenized Stocks","description":"Return the Coinbase-issued tokenized-stock records currently exposed through the API.","dateModified":"2026-10-16T16:44:12.418Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"},{"@type":"ListItem","position":2,"name":"List Tokenized Stocks","item":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks"}]},{"@type":["TechArticle","APIReference"],"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#apireference","headline":"List Tokenized Stocks","name":"List Tokenized Stocks","description":"Return the Coinbase-issued tokenized-stock records currently exposed through the API.","url":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks#webpage"},"dateModified":"2026-10-16T16:44:12.418Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

<<<PAGE https://docs.base.org/sdks/tokenized-stocks/overview>>>
---
url: https://docs.base.org/sdks/tokenized-stocks/overview
title: Tokenized Stocks API - Base Documentation
description: Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Endpoints](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Wallet Positions and Profit and Loss](https://docs.base.org/sdks/tokenized-stocks/overview)
* [List Tokenized Stocks](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Interpreting Response Fields](https://docs.base.org/sdks/tokenized-stocks/overview)
* [Errors](https://docs.base.org/sdks/tokenized-stocks/overview)

Tokenized Stocks API

# Tokenized Stocks API

Copy pageCopy page

Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.

Copy pageCopy page

Use the public Tokenized Stocks API to retrieve reference data for [Coinbase-issued tokenized stocks on Base](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks). The API is read-only and does not require an API key.

Coinbase tokenized stocks are available only to persons in eligible jurisdictions outside of the United States. This API provides read-only reference data only; it does not provide trading, execution, issuance, minting, redemption, or custody functionality. The availability of any token or related product may be subject to jurisdictional, eligibility, and compliance requirements. Integrators are responsible for applying applicable restrictions.

Base URL

```
https://api.coinbase.com/v1/tokenized-stocks
```

[Browse the API reference](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks) for complete request and response schemas and an interactive request builder.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | [List tokenized-stock records](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks). |
| `GET` | `/chains` | [List protocol contract addresses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-protocol-contract-addresses). |
| `GET` | `/total-supply/{contract_address}` | [Get normalized token supply](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-total-supply). |
| `GET` | `/metadata/{ticker}` | [Get token metadata](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-metadata). |
| `GET` | `/images/{symbol}` | [Redirect to a token icon](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-icon). |
| `GET` | `/prospectus/{ticker}` | [Redirect to a prospectus PDF](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-token-prospectus). |
| `GET` | `/prospectuses` | [List cached prospectuses](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-cached-prospectuses). |
| `GET` | `/corporate-actions/{id}` | [Get a corporate action](https://docs.base.org/sdks/tokenized-stocks/api-reference/get-corporate-action). |

## Wallet Positions and Profit and Loss

The API provides reference data, not wallet-specific data. No endpoint accepts a wallet address, and the API does not return a wallet’s positions, cost basis, trade history, or profit and loss.
To show a holder’s current position in share-equivalent units, read the balance onchain with [`balanceOfUI`](https://docs.base.org/specifications/b20/reference/interfaces/ib20-asset/balance-of-ui), which applies the current `multiplier` (see [Multipliers](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks)). A balance does not give you cost basis or profit and loss. To calculate those, you need trade history from every route you want to include. Your app’s own records cover only the trades made through your app.

## List Tokenized Stocks

cURL

```
curl https://api.coinbase.com/v1/tokenized-stocks
```

The response includes token contract addresses, symbols, names, descriptions, decimals, ISINs, and multipliers. Depending on the token, it can also include an ADGM ISIN, an icon URL, total supply, first-mint date, paused features, and NAV/reference value data. Presence in the response does not imply trading availability or eligibility.
Results are paginated, so a single request may not return every record. When the response includes `next_page_token`, pass it as the `page_token` query parameter to fetch the next page, and repeat until `next_page_token` is omitted. Keep other request parameters unchanged between pages.
Use `page_size` to set the page size. The default is `100` when omitted or set to `0`. Values above `500` are capped at `500`; negative values return HTTP `400`. Tokens are ordered by contract address.

cURL

```
curl "https://api.coinbase.com/v1/tokenized-stocks?page_token=<next_page_token>"
```

## Interpreting Response Fields

JSON responses omit default-valued scalar fields, empty arrays, and unset timestamps. For example, a zero `total_supply` or empty `paused_features` array can be omitted. Do not assume every field is present, and do not treat missing NAV data as a usable price.

* **`total_supply`** is the token supply normalized by the token’s decimals. It is a token-unit amount, not the number of underlying shares.
* **`multiplier`** is the current scaling factor between token units and underlying shares. It can change for corporate actions such as dividends or stock splits, so always apply the current value when converting token units to shares.
* **`nav_price`** is the most recently published Chainlink-based NAV/reference value for the token. It is not a live bid/ask or execution price.
* **`nav_price_updated_at`** is when `nav_price` was last updated onchain. Feeds update only on price deviation or heartbeat and hold their last value outside market hours, so check this timestamp and apply staleness bounds before relying on `nav_price`.
* **`isin`** is the underlying stock’s ISIN.
* **`adgm_isin`** is the ADGM ISIN of the tokenized security, taken from its approved prospectus. It is distinct from the stock ISIN and can be absent when unavailable.
* **`description`** is a human-readable description of the tokenized stock.
* **`first_mint_date`** is the UTC block timestamp of the first positive ERC-20 mint, not the contract deployment time. It can be absent if the token has never been minted or its first mint has not yet been resolved. Later mints and burns do not change it.

## Errors

JSON endpoints return an error object with `code` and `message`. The code is a service error code, not the HTTP status. For example:

Invalid Page Token

```
{"code": 3, "message": "page_token is invalid"}
```

| HTTP Status | Code | Meaning |
| --- | --- | --- |
| `400` | `3` | Invalid input, such as a malformed page token, negative page size, invalid contract address, or malformed corporate action UUID. |
| `404` | `5` | The requested token, ticker, or corporate action is not supported or not found. |
| `503` | `14` | Required data is temporarily unavailable. |

The icon and prospectus redirect endpoints return HTTP `302` with a `Location` header on success, not JSON. Their lookup and validation errors use plain-text bodies. See each endpoint’s reference for its specific responses.
For integration guidance, price-feed details, and current token contract addresses, see [List Tokenized Stocks](https://docs.base.org/build-on-base/integrate-defi/list-tokenized-stocks).

Was this page helpful?

YesNo

[debug\_traceBlockByNumber

Previous](https://docs.base.org/base-chain/api-reference/debug-api/debug_traceBlockByNumber)[List Tokenized Stocks

Next](https://docs.base.org/sdks/tokenized-stocks/api-reference/list-tokenized-stocks)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.base.org/#organization","name":"Base Documentation","url":"https://docs.base.org","logo":{"@type":"ImageObject","url":"https://mintcdn.com/base-a060aa97/9LdNiQhE-qTXRlrp/logo/logo_light.svg?fit=max&auto=format&n=9LdNiQhE-qTXRlrp&q=85&s=346ebfbc4cbad6fa96a3466bb7f5aa3a"}},{"@type":"WebSite","@id":"https://docs.base.org#website","name":"Base Documentation","url":"https://docs.base.org","publisher":{"@id":"https://docs.base.org/#organization"}},{"@type":"WebPage","@id":"https://docs.base.org/sdks/tokenized-stocks/overview#webpage","url":"https://docs.base.org/sdks/tokenized-stocks/overview","name":"Tokenized Stocks API","description":"Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.","dateModified":"2026-11-13T14:02:19.652Z","isPartOf":{"@id":"https://docs.base.org#website"},"breadcrumb":{"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.base.org/sdks/tokenized-stocks/overview#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Base Documentation","item":"https://docs.base.org"},{"@type":"ListItem","position":2,"name":"Tokenized Stocks API","item":"https://docs.base.org/sdks/tokenized-stocks/overview"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#article","headline":"Tokenized Stocks API","name":"Tokenized Stocks API","description":"Read tokenized-stock records, supplies, metadata, prospectuses, and corporate actions on Base.","url":"https://docs.base.org/sdks/tokenized-stocks/overview","mainEntityOfPage":{"@id":"https://docs.base.org/sdks/tokenized-stocks/overview#webpage"},"dateModified":"2026-11-13T14:02:19.652Z","publisher":{"@id":"https://docs.base.org/#organization"},"isPartOf":{"@id":"https://docs.base.org#website"}}]}
```

## 목록만 둔 URL 22건 (inventory.csv에서 plan=list)
- https://docs.base.org/sdks/base-anvil
- https://docs.base.org/sdks/base-earn/api-reference/borrow
- https://docs.base.org/sdks/base-earn/api-reference/claim
- https://docs.base.org/sdks/base-earn/api-reference/deposit
- https://docs.base.org/sdks/base-earn/api-reference/get-redemption
- https://docs.base.org/sdks/base-earn/api-reference/list-positions
- https://docs.base.org/sdks/base-earn/api-reference/list-vaults
- https://docs.base.org/sdks/base-earn/api-reference/request-withdraw
- https://docs.base.org/sdks/base-earn/api-reference/withdraw
- https://docs.base.org/sdks/base-earn/call-the-api
- https://docs.base.org/sdks/base-earn/concepts
- https://docs.base.org/sdks/base-earn/errors
- https://docs.base.org/sdks/base-earn/execute-calls
- https://docs.base.org/sdks/base-earn/faq
- https://docs.base.org/sdks/base-earn/lend-example
- ...
