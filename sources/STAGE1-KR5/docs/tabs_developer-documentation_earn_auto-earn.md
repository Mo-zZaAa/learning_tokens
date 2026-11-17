> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto Earn

> The Earn API exposes Auto Earn: enable or disable yield generation across eligible assets, read the user's allocations and historical rewards, and discover which assets are Auto Earn eligible by user or by country.

## Overview

This page covers **Auto Earn**. To allocate into a specific strategy yourself, see [Bonded Earn](https://docs.services.payward.com/tabs/developer-documentation/earn/bonded-earn.md).

Auto Earn is a single product. You don't allocate balances per asset: you flip a per-yield-source switch for the user and Payward picks assets and routes eligible balances. Payward absorbs any on-chain bonding or unbonding periods, so allocated assets stay liquid and remain at the user's disposal at all times. The supported yield sources are `staking`, `base_rewards`, and `opt_in_rewards`; more may be added without breaking the response shape.

The integration shape is eight endpoints, listed with their API key permissions in the [API reference](#api-reference) at the end of this page.

> [!NOTE]
>
> If you have used Kraken's [Spot REST Earn](https://docs.kraken.com/api/docs/guides/spot-rest-earn/) endpoints
> (`Strategies`, `Allocations`, `Allocate`, `Deallocate`), the PWS Earn API is a higher-level abstraction of the same
> product. PWS picks assets, routes eligible balances, and hides any on-chain bonding or unbonding so allocated assets
> remain liquid for the user. You see the result through the eight endpoints in the [API reference](#api-reference) and
> through the Portfolio API, which surfaces each settled reward as an `earn_reward` transaction.

## Prerequisites

* Payward Services API credentials (see the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md)). The API key needs the `earn-auto-read` permission, plus `earn-auto-write` to change preferences (see [API key permissions](#api-key-permissions)).
* A verified user with at least one account.
* Examples read the API base URL from the `PWS_BASE_URL` environment variable (see [Environments](https://docs.services.payward.com/tabs/developer-documentation/testing/overview.md#environments)) and credentials from `PWS_API_KEY` and `PWS_API_SECRET`.

## Workflow

**1. Discover Auto Earn assets (optional, pre-account)**

Show what's available in a country before you have an account. User-agnostic.

`GET /v1/earn/auto/assets?country=US`

**2. Discover Auto Earn assets for an account**

Show APY and per-user allocation cap for the account's eligible assets.

`GET /v1/accounts/{account_id}/earn/auto/assets`

**3. Set Auto Earn preferences**

Enable or disable a yield source. Async.

`PATCH /v1/accounts/{account_id}/earn/auto`

**4. Poll until preferences settle**

Read current preferences and watch `pending_enabled` / `pending_disabled` resolve.

`GET /v1/accounts/{account_id}/earn/auto`

**5. Read allocations and rewards**

Show how much is currently earning, and historical / upcoming rewards.

* `GET /v1/accounts/{account_id}/earn/auto/allocations`
* `GET /v1/accounts/{account_id}/earn/auto/rewards/summary`
* `GET /v1/accounts/{account_id}/earn/auto/rewards`
* `GET /v1/accounts/{account_id}/earn/auto/rewards/upcoming`

## Auto Earn preference lifecycle

Each yield source has one of four states. A yield source appears in `GET /v1/accounts/{account_id}/earn/auto` if the account is eligible for it, is enrolled in it, or has an enable in flight. A missing yield source means none of these apply. Enabling a yield source the account isn't eligible for fails with `not_eligible`. Disabling always works. There is no separate eligibility endpoint.

| State | Meaning | What to show |
| - | - | - |
| `enabled` | Yield source is active. Eligible balances are earning. | "On". |
| `disabled` | Yield source is off. No new allocations. | "Off". |
| `pending_enabled` | `PATCH` accepted; provisioning in progress. | "Enabling…" with a spinner. Don't allow re-toggling. |
| `pending_disabled` | `PATCH` accepted; unallocation in progress. | "Disabling…" with a spinner. Don't allow re-toggling. |

`PATCH /v1/accounts/{account_id}/earn/auto` returns immediately with an empty `data` object. Poll `GET /v1/accounts/{account_id}/earn/auto` until the pending state resolves.

> [!WARNING]
>
> Only one Auto Earn preference change can be in progress per account at a time. Submitting a `PATCH` while any yield
> source is in `pending_enabled` or `pending_disabled` returns `409 Conflict` with the code `allocation_in_progress`.
> Wait for the pending state to resolve in `GET /v1/accounts/{account_id}/earn/auto` before issuing the next change.

## Asset, amount, and quote-currency conventions

Allocation and reward entries describe an **asset** at the top level using three fields:

| Field | Description |
| - | - |
| `symbol` | Ticker symbol (e.g., `ETH`, `EUR`). |
| `type` | `fiat`, `crypto`, `stablecoin`, `xstock`, or `tokenized_money_market_fund`. |
| `name` | Human-readable name (e.g., `"Ethereum"`). |

All **monetary fields inside an entry** are plain decimal strings:

| Suffix | Denominated in |
| - | - |
| (none) | The entry's own asset. `allocated: "100.1234"` means 100.1234 ETH on an `ETH` entry. |
| `_in_quote` | The request's quote currency. `allocated_in_quote: "12345.12"` is 12,345.12 EUR when `quote_symbol=EUR`. |

The allocations and rewards endpoints accept `quote_symbol` and `quote_type` to choose the quote asset, and **echo both at the top level of the response** so you can format `*_in_quote` values without re-stating the choice. Today only `quote_type=fiat` is supported; `quote_symbol` defaults to `USD`. Pass the same values across Earn and the Portfolio API so totals reconcile.

The list endpoints page with `page_token` / `page_size`. `page_size` defaults to 20 and must be between 1 and 25. Other values return `400 Bad Request`. A valid `page_size` is ignored when you pass `page_token`. Pass `next_page_token` back as `page_token` to get the next page; it is absent on the last page.

## Authentication setup

Authenticated endpoints require an HMAC-SHA512 request signature in the `API-Sign` header and the signing time in the `API-Timestamp` header. The helpers below compute both. The examples call `signed_headers` (`signedHeaders` in JavaScript) with the request's method, its path including any query string, and the exact body string they send. See the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md) for the full algorithm.

The examples read the API base URL from the `PWS_BASE_URL` environment variable, and your credentials from `PWS_API_KEY` and `PWS_API_SECRET`. Set `PWS_BASE_URL` to the sandbox or production base URL, listed in [Environments](https://docs.services.payward.com/tabs/developer-documentation/testing/overview.md#environments).

```python Python theme={null}
import base64
import hashlib
import hmac
import json
import os
import time
import uuid
from urllib.parse import urlencode

import requests

API_KEY = os.environ["PWS_API_KEY"]
API_SECRET = os.environ["PWS_API_SECRET"]
BASE_URL = os.environ["PWS_BASE_URL"]


def payward_signature(secret, timestamp, method, path_with_query, body=""):
    """Return the API-Sign value for one request.

    body is the exact string sent on the wire, or "" for a request without a body.
    """
    body_hash = hashlib.sha256(body.encode("utf-8")).hexdigest().upper()
    message = f"{timestamp}\n{method.upper()}\n{path_with_query}\n{body_hash}"
    mac = hmac.new(base64.b64decode(secret), message.encode("utf-8"), hashlib.sha512)
    return base64.b64encode(mac.digest()).decode()


def signed_headers(method, path_with_query, body="", idempotent=False):
    """Return the headers for one request, signed now."""
    timestamp = str(time.time_ns() // 1_000_000)
    headers = {
        "API-Key": API_KEY,
        "API-Timestamp": timestamp,
        "API-Sign": payward_signature(
            API_SECRET, timestamp, method, path_with_query, body
        ),
    }
    if body:
        headers["Content-Type"] = "application/json"
    if idempotent:
        headers["Idempotency-Key"] = str(uuid.uuid4())
    return headers
```

```javascript JavaScript theme={null}
import crypto from 'node:crypto';

const API_KEY = process.env.PWS_API_KEY;
const API_SECRET = process.env.PWS_API_SECRET;
const BASE_URL = process.env.PWS_BASE_URL;

/**
 * Returns the API-Sign value for one request.
 * `body` is the exact string sent on the wire, or '' for a request without a body.
 */
function paywardSignature(secret, timestamp, method, pathWithQuery, body = '') {
  const bodyHash = crypto.createHash('sha256').update(body, 'utf8').digest('hex').toUpperCase();
  const message = `${timestamp}\n${method.toUpperCase()}\n${pathWithQuery}\n${bodyHash}`;
  return crypto.createHmac('sha512', Buffer.from(secret, 'base64')).update(message, 'utf8').digest('base64');
}

/** Returns the headers for one request, signed now. */
function signedHeaders(method, pathWithQuery, body = '', { idempotent = false } = {}) {
  const timestamp = String(Date.now());
  const headers = {
    'API-Key': API_KEY,
    'API-Timestamp': timestamp,
    'API-Sign': paywardSignature(API_SECRET, timestamp, method, pathWithQuery, body),
  };
  if (body) {
    headers['Content-Type'] = 'application/json';
  }
  if (idempotent) {
    headers['Idempotency-Key'] = crypto.randomUUID();
  }
  return headers;
}
```

> [!NOTE]
>
> Idempotency is per operation, not global. A write endpoint that supports safe retries documents an `Idempotency-Key`
> header in its API reference entry, together with how replays and key reuse behave for that operation. Where it is
> supported, generate a fresh UUIDv4 per logical attempt and reuse that same key for every retry of that attempt. Treat
> an endpoint that does not document the header as non-idempotent: after a timeout or another unknown outcome, reconcile
> the current state before issuing another request rather than retrying automatically.

The Earn endpoints either accept query parameters or a JSON body. Build the path with its query string once, then pass it to `signed_headers` and use it in the request URL.

### API key permissions

Create the API key in the Payward Console with the permissions your integration needs:

| Permission | Grants |
| - | - |
| `earn-auto-read` | Read Auto Earn eligibility, preferences, allocations, and rewards. |
| `earn-auto-write` | Change Auto Earn preferences with `PATCH /v1/accounts/{account_id}/earn/auto`. |

Grant both to an integration that sets preferences and then polls them.

## Step 1: discover Auto Earn assets by country

`GET /v1/earn/auto/assets` is **user-agnostic**. `country` is required and must be a two-letter ISO 3166-1 alpha-2 code. Use it to surface the value proposition before sign-up, for example on a landing page filtered by the visitor's country. Pagination is via `page_token` / `page_size`. To list only assets backed by specific yield sources, repeat the optional `yield_source` query parameter (for example, `yield_source=staking&yield_source=base_rewards`).

```python Python theme={null}
def list_auto_earn_assets_by_country(country, page_size=20, page_token=None):
    params = {"country": country, "page_size": str(page_size)}
    if page_token:
        params["page_token"] = page_token
    path = f"/v1/earn/auto/assets?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


catalog = list_auto_earn_assets_by_country("US")
for asset in catalog["data"]:
    label = (
        f"{asset['symbol']} ({asset['name']})" if asset.get("name") else asset["symbol"]
    )
    cap = (
        f"cap {asset['user_cap']} {asset['symbol']}"
        if "user_cap" in asset
        else "no cap"
    )
    print(f"{label}: {asset['apy']}% APY, {cap}")
```

```javascript JavaScript theme={null}
async function listAutoEarnAssetsByCountry(country, pageSize = 20, pageToken = null) {
  const params = new URLSearchParams({ country, page_size: String(pageSize) });
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/earn/auto/assets?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const catalog = await listAutoEarnAssetsByCountry('US');
for (const asset of catalog.data) {
  const label = asset.name ? `${asset.symbol} (${asset.name})` : asset.symbol;
  const cap = asset.user_cap !== undefined ? `cap ${asset.user_cap} ${asset.symbol}` : 'no cap';
  console.log(`${label}: ${asset.apy}% APY, ${cap}`);
}
```

### Response example

```json theme={null}
{
  "data": [
    {
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "yield_source": "staking",
      "apy": "3.41",
      "user_cap": "1000"
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `name` | Human-readable asset name. It can be empty: fall back to `symbol`. |
| `yield_source` | Yield source that backs this asset (`staking`, `base_rewards`, or `opt_in_rewards`). |
| `apy` | Estimated annual percentage yield as a decimal string (e.g., `"3.41"` for 3.41%). Gross, before any reward fee. |
| `user_cap` | Maximum amount the user can have allocated to Auto Earn for this asset, in the asset's native units. Show as a "max" hint. Absent when there is no cap. |
| `next_page_token` | Opaque cursor; pass back as `page_token` to fetch the next page. |

> [!TIP]
>
> APY is an estimate, not a guarantee. Display the value with a `%` suffix and label it "estimated", since realized
> yield depends on network conditions and fees.

## Step 2: discover Auto Earn assets for an account

`GET /v1/accounts/{account_id}/earn/auto/assets` returns the same shape as Step 1 but scoped to a specific account and accepting the same `page_token`, `page_size`, and `yield_source` parameters. Use it after sign-up to confirm exactly which assets are eligible for Auto Earn in that account.

```python Python theme={null}
def list_account_auto_earn_assets(account_id, page_size=20, page_token=None):
    params = {"page_size": str(page_size)}
    if page_token:
        params["page_token"] = page_token
    path = f"/v1/accounts/{account_id}/earn/auto/assets?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


account_id = "WFFGB6Z8AK5WF9JL"
account_assets = list_account_auto_earn_assets(account_id)
for asset in account_assets["data"]:
    cap = (
        f"cap {asset['user_cap']} {asset['symbol']}"
        if "user_cap" in asset
        else "no cap"
    )
    print(f"{asset['symbol']}: {asset['apy']}% APY ({cap})")
```

```javascript JavaScript theme={null}
async function listAccountAutoEarnAssets(accountId, pageSize = 20, pageToken = null) {
  const params = new URLSearchParams({ page_size: String(pageSize) });
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/accounts/${accountId}/earn/auto/assets?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const accountId = 'WFFGB6Z8AK5WF9JL';
const accountAssets = await listAccountAutoEarnAssets(accountId);
for (const asset of accountAssets.data) {
  const cap = asset.user_cap !== undefined ? `cap ${asset.user_cap} ${asset.symbol}` : 'no cap';
  console.log(`${asset.symbol}: ${asset.apy}% APY (${cap})`);
}
```

### Response example

```json theme={null}
{
  "data": [
    {
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "yield_source": "staking",
      "apy": "3.41",
      "user_cap": "1000"
    }
  ]
}
```

## Step 3: set Auto Earn preferences

Send a `PATCH` to `/v1/accounts/{account_id}/earn/auto` with the desired state of each yield source you want to change. **All body fields are optional**: yield sources you omit keep their current preference, so you can flip a single source without touching the others. Unknown fields are ignored: a misspelled yield source returns `200 OK` and changes nothing.

Supported yield sources: `staking`, `base_rewards`, `opt_in_rewards`. Allowed values: `"enabled"`, `"disabled"`. Enabling a yield source the account isn't eligible for fails with `not_eligible`. Disabling always works.

```python Python theme={null}
def set_auto_earn_preferences(account_id, preferences):
    path = f"/v1/accounts/{account_id}/earn/auto"
    body = json.dumps(preferences)

    response = requests.patch(
        BASE_URL + path,
        headers=signed_headers("PATCH", path, body, idempotent=True),
        data=body,
        timeout=10,
    )
    return response.status_code, response.json()


status, body = set_auto_earn_preferences(account_id, {"staking": "enabled"})
if status != 200:
    raise RuntimeError(f"Toggle rejected: {status} {body['error']['code']}")
print(f"Toggle accepted: HTTP {status}")
```

```javascript JavaScript theme={null}
async function setAutoEarnPreferences(accountId, preferences) {
  const path = `/v1/accounts/${accountId}/earn/auto`;
  const body = JSON.stringify(preferences);

  const response = await fetch(BASE_URL + path, {
    method: 'PATCH',
    headers: signedHeaders('PATCH', path, body, { idempotent: true }),
    body,
  });

  return { status: response.status, body: await response.json() };
}

const { status, body } = await setAutoEarnPreferences(accountId, { staking: 'enabled' });
if (status !== 200) throw new Error(`Toggle rejected: ${status} ${body.error.code}`);
console.log(`Toggle accepted: HTTP ${status}`);
```

### Response example

```json theme={null}
{
  "data": {}
}
```

> [!NOTE]
>
> The `200 OK` confirms the preference change was accepted, not that every eligible balance is already earning.
> Provisioning runs asynchronously; observe `pending_enabled` / `pending_disabled` on `GET /v1/accounts/{account_id}
>     /earn/auto` to know when the change has settled. A second `PATCH` issued before the pending state resolves returns
> `409 Conflict` with the code `allocation_in_progress`: see the [preference lifecycle](#auto-earn-preference-lifecycle)
> above.

## Step 4: poll until preferences settle

`GET /v1/accounts/{account_id}/earn/auto` returns the current preference for every yield source the account is eligible for, is enrolled in, or has an enable in flight. Eligibility is country-aware: if a user who isn't enrolled moves to a region where staking isn't supported, the `staking` field disappears from this response. Enabling it then fails with `not_eligible`.

```python Python theme={null}
def get_auto_earn_preferences(account_id):
    path = f"/v1/accounts/{account_id}/earn/auto"
    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


def wait_for_settled(account_id, source, max_attempts=60):
    pending = {"pending_enabled", "pending_disabled"}
    for _ in range(max_attempts):
        prefs = get_auto_earn_preferences(account_id)
        state = prefs["data"].get(source)
        print(f"{source}: {state}")
        if state is None or state not in pending:
            return prefs
        time.sleep(2)
    raise RuntimeError(f"{source} did not settle in time")


prefs = wait_for_settled(account_id, "staking")
```

```javascript JavaScript theme={null}
async function getAutoEarnPreferences(accountId) {
  const path = `/v1/accounts/${accountId}/earn/auto`;
  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

async function waitForSettled(accountId, source, maxAttempts = 60) {
  const pending = new Set(['pending_enabled', 'pending_disabled']);
  for (let i = 0; i < maxAttempts; i++) {
    const prefs = await getAutoEarnPreferences(accountId);
    const state = prefs.data[source];
    console.log(`${source}: ${state}`);
    if (state === undefined || !pending.has(state)) return prefs;
    await new Promise(resolve => setTimeout(resolve, 2000));
  }
  throw new Error(`${source} did not settle in time`);
}

const prefs = await waitForSettled(accountId, 'staking');
```

### Response example

```json theme={null}
{
  "data": {
    "staking": "enabled"
  }
}
```

## Step 5a: list current allocations

`GET /v1/accounts/{account_id}/earn/auto/allocations` returns the user's current per-asset allocation, plus the all-asset total in the requested quote currency. Assets with a zero balance aren't listed. The endpoint is cursor-paginated; `next_page_token` is absent on the last page. All amounts inside entries are plain decimal strings; the response echoes `quote_symbol` / `quote_type` at the top level so you know how to format `*_in_quote` values.

```python Python theme={null}
def list_auto_earn_allocations(
    account_id, quote_symbol="USD", page_token=None, page_size=20
):
    params = {
        "quote_symbol": quote_symbol,
        "quote_type": "fiat",
        "page_size": str(page_size),
    }
    if page_token:
        params["page_token"] = page_token
    path = f"/v1/accounts/{account_id}/earn/auto/allocations?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


allocations = list_auto_earn_allocations(account_id, quote_symbol="EUR")
quote = allocations["quote_symbol"]
print(f"Total allocated: {allocations['total_allocated_in_quote']} {quote}")
for entry in allocations["data"]:
    print(
        f"  {entry['allocated']} {entry['symbol']} "
        f"(~{entry['allocated_in_quote']} {quote})"
    )
```

```javascript JavaScript theme={null}
async function listAutoEarnAllocations(accountId, quoteSymbol = 'USD', pageToken = null, pageSize = 20) {
  const params = new URLSearchParams({
    quote_symbol: quoteSymbol,
    quote_type: 'fiat',
    page_size: String(pageSize),
  });
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/accounts/${accountId}/earn/auto/allocations?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const allocations = await listAutoEarnAllocations(accountId, 'EUR');
const quote = allocations.quote_symbol;
console.log(`Total allocated: ${allocations.total_allocated_in_quote} ${quote}`);
for (const entry of allocations.data) {
  console.log(`  ${entry.allocated} ${entry.symbol} (~${entry.allocated_in_quote} ${quote})`);
}
```

### Response example

```json theme={null}
{
  "quote_symbol": "EUR",
  "quote_type": "fiat",
  "total_allocated_in_quote": "12345.12",
  "data": [
    {
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "allocated": "100.1234",
      "allocated_in_quote": "12345.12"
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `quote_symbol` / `quote_type` | Echo of the requested quote asset. Use to format `*_in_quote` values. |
| `total_allocated_in_quote` | Cross-asset allocation total in the quote currency. Use it for a dashboard hero value. |
| `data[].allocated` | Per-asset amount currently earning, in the entry's asset. |
| `data[].allocated_in_quote` | Same per-asset amount in the quote currency. |
| `next_page_token` | Opaque cursor; pass back as `page_token` for the next page. |

> [!NOTE]
>
> Auto Earn allocations are liquid. The `allocated` amount is the user's current earning balance and is always at the
> user's disposal: PWS absorbs any on-chain bonding or unbonding so there are no "in-transit" amounts for you to track
> on the Earn side.

## Step 5b: read rewards

Rewards are split across three endpoints, so you fetch only what a screen needs:

| Need | Endpoint |
| - | - |
| Headline total across all assets | `GET /v1/accounts/{account_id}/earn/auto/rewards/summary` |
| Lifetime rewards per asset | `GET /v1/accounts/{account_id}/earn/auto/rewards` |
| Next payout: expected amounts and date | `GET /v1/accounts/{account_id}/earn/auto/rewards/upcoming` |

All three accept `quote_symbol` and `quote_type` with the same semantics as allocations, and echo both at the top level of the response. The per-asset and upcoming endpoints also accept `page_token` / `page_size`. All reward amounts are net of any reward fee.

### Total rewards

`GET /v1/accounts/{account_id}/earn/auto/rewards/summary` returns the lifetime total across every Auto Earn asset, converted to the quote currency. Use it for the headline figure of a rewards card.

```json theme={null}
{
  "data": {
    "total_rewarded_in_quote": "325.62",
    "quote_symbol": "USD",
    "quote_type": "fiat"
  }
}
```

Each payout is valued when it is paid, so the total doesn't move with asset prices. For a non-USD quote, the USD total is converted at today's USD rate, so it still moves with that rate.

### Rewards per asset

`GET /v1/accounts/{account_id}/earn/auto/rewards` returns the lifetime rewards of each asset, sorted by symbol, A-Z. Assets that have never paid a reward are omitted.

```python Python theme={null}
def list_auto_earn_rewards(
    account_id, quote_symbol="USD", page_token=None, page_size=20
):
    params = {
        "quote_symbol": quote_symbol,
        "quote_type": "fiat",
        "page_size": str(page_size),
    }
    if page_token:
        params["page_token"] = page_token
    path = f"/v1/accounts/{account_id}/earn/auto/rewards?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


rewards = list_auto_earn_rewards(account_id, quote_symbol="EUR")
for entry in rewards["data"]:
    print(
        f"  {entry['symbol']}: rewarded {entry['rewarded']} {entry['symbol']}"
        f" ({entry['rewarded_in_quote']} {rewards['quote_symbol']})"
    )
```

```javascript JavaScript theme={null}
async function listAutoEarnRewards(accountId, quoteSymbol = 'USD', pageToken = null, pageSize = 20) {
  const params = new URLSearchParams({
    quote_symbol: quoteSymbol,
    quote_type: 'fiat',
    page_size: String(pageSize),
  });
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/accounts/${accountId}/earn/auto/rewards?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const rewards = await listAutoEarnRewards(accountId, 'EUR');
for (const entry of rewards.data) {
  console.log(
    `  ${entry.symbol}: rewarded ${entry.rewarded} ${entry.symbol} (${entry.rewarded_in_quote} ${rewards.quote_symbol})`,
  );
}
```

#### Response example

```json theme={null}
{
  "quote_symbol": "EUR",
  "quote_type": "fiat",
  "data": [
    {
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "rewarded": "13.5",
      "rewarded_in_quote": "2451.12"
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `quote_symbol` / `quote_type` | Echo of the requested quote asset. Use to format `*_in_quote` values. |
| `data[].rewarded` | Lifetime rewards for the asset, in the asset itself. Includes rewards paid in other assets, converted to this asset at the time of the payout. |
| `data[].rewarded_in_quote` | Same lifetime total in the quote currency. Each payout is valued when it is paid, so it doesn't move with the asset price. For a non-USD quote, the USD total is converted at today's USD rate. Includes rewards paid in other assets. |
| `next_page_token` | Opaque cursor; pass back as `page_token` for the next page. |

### Upcoming rewards

`GET /v1/accounts/{account_id}/earn/auto/rewards/upcoming` returns the expected reward of each asset at its next payout, together with the date of that payout. The amount is what has accrued so far plus an estimate up to the payout date. It leaves out rewards that belong to a later payout period.

The amounts are estimates and the date is a target, so payouts can be delayed. `next_reward_date` is one date for the whole account: the earliest payout among the assets. Each amount is for its asset's own next payout, which can be later than that date. The date covers every asset, not just the current page, so it reads the same on every page.

Assets with nothing pending are omitted, and `next_reward_date` is then absent. `other_assets` is usually an empty array. When a reward is paid in other assets (e.g., EIGEN paid on the ETH entry), it lists that part separately.

```json theme={null}
{
  "quote_symbol": "EUR",
  "quote_type": "fiat",
  "next_reward_date": "2026-05-07T16:57:51Z",
  "data": [
    {
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "upcoming_reward": "0.56",
      "upcoming_reward_in_quote": "101.23",
      "other_assets": [
        {
          "symbol": "EIGEN",
          "type": "crypto",
          "name": "EigenLayer",
          "upcoming_reward": "0.1",
          "upcoming_reward_in_quote": "2.34"
        }
      ]
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `next_reward_date` | Earliest payout date among the assets with a pending reward. Absent when nothing is pending. |
| `data[].upcoming_reward` / `_in_quote` | Accrued plus projected reward for the asset, in the asset itself and in the quote currency. Net of any reward fee. Zero when the asset only has `other_assets`. |
| `data[].other_assets` | Part of the reward paid in assets other than the entry's own. Same amount fields as the entry, without a nested `other_assets`. Don't add them to the entry's amounts. |
| `next_page_token` | Opaque cursor; pass back as `page_token` for the next page. |

> [!NOTE]
>
> Reward amounts can be very small for low-APY assets: a value like `"0.00000001"` is common. Decide up front how to
> render near-zero values (for example, "\<0.00000001 ETH" or "\~0").

## Reconciling rewards in Portfolio

The `curl` examples read these environment variables:

* `PWS_BASE_URL`: the API base URL. Set it to the sandbox or production base URL, listed in
  [Environments](https://docs.services.payward.com/tabs/developer-documentation/testing/overview.md#environments).
* `PWS_API_KEY`: your API key.
* `PWS_API_TIMESTAMP` and `PWS_API_SIGN`: the timestamp and signature of each request. To compute them, see
  [Authentication](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md).
* Compute `PWS_API_SIGN` over the exact `-d` string, including its line breaks and indentation, and over the exact path
  and query in the URL. Each request needs a new `PWS_API_TIMESTAMP` and `PWS_API_SIGN`.

When a payout settles, it appears in the Portfolio activity feed as an `earn_reward` transaction:

```bash theme={null}
curl -X GET "$PWS_BASE_URL/v1/accounts/WFFGB6Z8AK5WF9JL/portfolio/transactions?types=earn_reward&start_timestamp=2026-04-01T00%3A00%3A00Z&end_timestamp=2026-04-30T23%3A59%3A59Z&quote_symbol=USD" \
  -H "API-Key: $PWS_API_KEY" \
  -H "API-Timestamp: $PWS_API_TIMESTAMP" \
  -H "API-Sign: $PWS_API_SIGN"
```

The signature covers the query string exactly as you send it, including the colons in the timestamps encoded as `%3A`. Compute `PWS_API_SIGN` over this exact path and query string. If the encoding changes after you sign, for example to a raw `:`, the request returns `401 Unauthorized`.

Use the [Portfolio guide](https://docs.services.payward.com/tabs/developer-documentation/accounts/portfolio.md) for the activity feed and pagination, and the Reports endpoints for downloadable settlement statements.

## Error handling

All error responses share a standard envelope:

```json theme={null}
{
  "error": {
    "type": "earn_error",
    "status": 400,
    "code": "bad_request",
    "instance": "req-abc123",
    "causes": [
      {
        "field": "country",
        "message": "must match pattern \"^[A-Z]{2}$\""
      }
    ]
  }
}
```

| Field | Description |
| - | - |
| `type` | Error class (e.g., `earn_error`). |
| `status` | HTTP status code. |
| `code` | Machine-readable error code in snake\_case (e.g., `bad_request`, `not_eligible`). |
| `instance` | Request ID for this occurrence: include it in support tickets. |
| `doc_url` | Optional link to documentation for this error. |
| `causes` | Optional array of per-field validation failures. Each entry has a `field` (dot-notation path) and a human-readable `message`. |

`causes[]` isn't always present. Some invalid input returns `400 Bad Request` without it: an unknown `yield_source` filter, a bad enum value in the `PATCH` body, or an out-of-range `page_size`. Validate input before you send it, and don't depend on `causes[]` to find the problem.

| HTTP status | Cause | Remediation |
| - | - | - |
| `400 Bad Request` | Invalid `country` (not ISO 3166-1 alpha-2), unsupported `quote_type`, unknown `yield_source` filter value, bad enum value in the `PATCH` body, or bad pagination tokens | Validate query parameters and body before sending. Inspect `causes[]` for per-field details when present. |
| `401 Unauthorized` | Missing or invalid signature, key, or timestamp | Verify `API-Key`, `API-Timestamp`, and `API-Sign`. See [Troubleshooting](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md#troubleshooting). |
| `403 Forbidden` | Account is not authorized to use Earn, or you enabled a yield source the account isn't eligible for (`not_eligible`) | Confirm the account's product entitlements. For `not_eligible`, don't enable that yield source. |
| `403 Forbidden` | The API key lacks a required permission: `earn-auto-read` for reads, `earn-auto-write` for the `PATCH` | Add the required [API key permissions](#api-key-permissions) in Console. |
| `404 Not Found` | Unknown `account_id` | Verify the `account_id` belongs to your partner. |
| `409 Conflict` | An Auto Earn preference change is already in progress for this account (`allocation_in_progress`): only one may be in flight | Poll `GET /v1/accounts/{account_id}/earn/auto` until no yield source is in `pending_enabled` / `pending_disabled`, then retry. |
| `429 Too Many Requests` | Rate limit hit | Honor `Retry-After` and back off exponentially. |

### Best practices

1. **Treat the `PATCH` as eventually consistent.** A `200 OK` confirms the change was accepted, not that balances are already earning.
2. **Only one preference change in flight per account.** Wait for the pending state to resolve before submitting another change; otherwise the second `PATCH` returns `409 Conflict`.
3. **Only send the yield sources you actually want to change.** Omit the others to keep their preferences untouched.
4. **Pass `quote_symbol` consistently** across allocations, rewards, and Portfolio so converted totals line up across views.
5. **Don't assume APY is fixed.** Refetch the asset list whenever you display APY; it drifts with network conditions and country availability.
6. **Capture `X-Trace-Id` from response headers.** It speeds up support investigations.

## API reference

| Method | API key permission | Endpoint | Description |
| - | - | - | - |
| GET | `earn-auto-read` | [`/v1/earn/auto/assets`](https://docs.services.payward.com/api-reference/production-live/auto-earn/get-auto-earn-assets) | List Auto Earn assets eligible in a country (user-agnostic). Required `country`, optional `yield_source` filter. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto/assets`](https://docs.services.payward.com/api-reference/production-live/auto-earn/get-account-auto-earn-assets) | List Auto Earn assets available to the given account, with APY and per-user cap. Optional `yield_source` filter. |
| PATCH | `earn-auto-write` | [`/v1/accounts/{account_id}/earn/auto`](https://docs.services.payward.com/api-reference/production-live/auto-earn/set-auto-earn-preferences) | Set Auto Earn preferences per yield source. Async; empty `data: {}` on success. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto`](https://docs.services.payward.com/api-reference/production-live/auto-earn/get-auto-earn-preferences) | Get current Auto Earn preferences. Includes `pending_enabled` / `pending_disabled` while a `PATCH` is being applied. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto/allocations`](https://docs.services.payward.com/api-reference/production-live/auto-earn/get-auto-earn-allocations) | List the user's current per-asset allocations and the cross-asset total in the requested quote currency. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto/rewards/summary`](https://docs.services.payward.com/api-reference/production-live/auto-earn/get-auto-earn-reward-summary) | Get the lifetime total rewards across all assets in the quote currency. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto/rewards`](https://docs.services.payward.com/api-reference/production-live/auto-earn/list-auto-earn-rewards) | List lifetime rewards per asset, in the asset and in the quote currency. |
| GET | `earn-auto-read` | [`/v1/accounts/{account_id}/earn/auto/rewards/upcoming`](https://docs.services.payward.com/api-reference/production-live/auto-earn/list-upcoming-auto-earn-rewards) | List the expected reward of each asset at the next payout, with the next payout date. |
