> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bonded Earn

> Allocate into Bonded Earn strategies, track each request until it settles, follow allocations through bonding and unbonding, and read historical and upcoming rewards.

## Overview

Bonded Earn lets you allocate a user's balance into a specific earn strategy and deallocate it again. Unlike [Auto Earn](https://docs.services.payward.com/tabs/developer-documentation/earn/auto-earn.md), you choose the strategy and the amount, and you see the lock-up periods.

Proof-of-stake networks pay rewards for using tokens to help secure the network. Some strategies require funds to stay allocated during bonding or unbonding periods. An exit queue is the network's waiting list before unbonding begins.

Depending on the strategy, funds can pass through a bonding period before they earn and, for ETH, an exit queue, then an unbonding period, before they return to the user (see [Allocation lifecycle](#allocation-lifecycle)).

Allocate and deallocate are **asynchronous**. A request is accepted first and settles later. You get a `request_id` back and poll for the outcome.

The integration shape is eleven endpoints, listed in the [API reference](#api-reference) at the end of this page.

## Prerequisites

* Payward Services API credentials (see the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md)). The API key needs the `earn-bonded-read` permission, plus `earn-bonded-write` to allocate and deallocate (see [API key permissions](#api-key-permissions)).
* A verified user with at least one account and sufficient balance in the strategy's asset. If the user holds a different asset, follow the [Swaps guide](https://docs.services.payward.com/tabs/developer-documentation/trade/swap.md) to acquire it first.
* Examples read the API base URL from the `PWS_BASE_URL` environment variable (see [Environments](https://docs.services.payward.com/tabs/developer-documentation/testing/overview.md#environments)) and credentials from `PWS_API_KEY` and `PWS_API_SECRET`.

## Workflow

**1. Discover strategies (optional, pre-account)**

Show which Bonded Earn strategies are offered in a country before the user has an account.

`GET /v1/earn/bonded/strategies?country=US`

**2. Discover strategies for an account**

Show the account's strategies, with whether it can allocate or deallocate right now.

`GET /v1/accounts/{account_id}/earn/bonded/strategies`

**3. Allocate**

Submit an allocation with an `Idempotency-Key`. Async.

`POST /v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/allocate`

**4. Poll the request until it settles**

Watch `status` move from `pending` to `succeeded` or `failed`.

`GET /v1/accounts/{account_id}/earn/bonded/requests/{request_id}`

**5. Read allocations and rewards**

Show what is bonding, earning or on its way out, and the rewards.

* `GET /v1/accounts/{account_id}/earn/bonded/allocations`
* `GET /v1/accounts/{account_id}/earn/bonded/rewards/upcoming`

**6. Deallocate**

Submit a deallocation, then poll it the same way.

`POST /v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/deallocate`

## Allocation lifecycle

An allocation moves through up to four states.

| State | Meaning | Earns rewards |
| - | - | - |
| `bonding` | Allocated, waiting for the bonding period to end. | As set by the strategy's `bonding_period` |
| `earning` | Allocated and earning. | Yes |
| `exit_queue` | Deallocated, waiting in the network's exit queue before unbonding starts (ETH only). | Yes |
| `unbonding` | Deallocated, waiting for the unbonding period to end before funds come back. | As set by the strategy's `unbonding_period` |

Each strategy has three period objects, `bonding_period`, `exit_queue_period`, and `unbonding_period`, with the same fields:

| Field | Description |
| - | - |
| `seconds` | Length of the period. Zero when the strategy has no such period. |
| `type` | `fixed` when `seconds` is a guarantee, `variable` when it is an estimate. |
| `rewards` | `accruing` when the funds earn during the period, `not_accruing` when they don't. |

## Asset, amount, and quote-currency conventions

Entries describe their **asset** with `symbol` (e.g., `ETH`), `type` (`fiat`, `crypto`, `stablecoin`, [`xstock`](https://docs.services.payward.com/tabs/developer-documentation/tokenized-assets/xstocks), or `tokenized_money_market_fund`) and `name` (e.g., `"Ethereum"`).

All **monetary fields** are plain decimal strings:

| Suffix | Denominated in |
| - | - |
| (none) | The strategy's own asset. `total: "2.0"` means 2 ETH on an `ETH` entry. |
| `_in_quote` | The request's quote currency. `total_in_quote: "4000.0"` is 4,000 USD when `quote_symbol=USD`. |

The allocation and reward endpoints accept `quote_symbol` and `quote_type`, and **echo both in the response**. Today only `quote_type=fiat` is supported; `quote_symbol` defaults to `USD`. An unsupported quote returns `400 Bad Request` with a cause on `quote_symbol` or `quote_type`.

The list endpoints page with `page_token` / `page_size`. `page_size` defaults to 20 and must be between 1 and 25. Other values return `400 Bad Request`. A valid `page_size` is ignored when you pass `page_token`. Pass `next_page_token` back as `page_token` to get the next page; it is absent on the last page.

Strategy lists, allocations, rewards per strategy and upcoming rewards are sorted by asset symbol (A-Z), then unbonding period (shortest first, variable last). Allocation states are sorted by the soonest scheduled change. Pending requests are sorted oldest first.

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

Bonded Earn endpoints take query parameters or a JSON body. Include the query string in the path you sign: the helper supports this through its `params` argument.

### API key permissions

Create the API key in the Payward Console with the permissions your integration needs:

| Permission | Grants |
| - | - |
| `earn-bonded-read` | Read Bonded Earn strategies, requests, allocations, and rewards. |
| `earn-bonded-write` | Allocate and deallocate with the `allocate` and `deallocate` endpoints. |

Grant both to an integration that allocates and then polls the request.

## Idempotency keys

`Idempotency-Key` is **required** on allocate and deallocate. It must be a UUIDv4 in the canonical hyphenated form, for example `550e8400-e29b-41d4-a716-446655440000`. Generate one key per logical request and keep it until the request has settled:

* **Retrying the same request** with the same key, strategy and `amount` returns the original `request_id` and moves no funds again. This is how you retry safely after a timeout or a dropped connection.
* **Reusing a key for a different request** (another strategy, another `amount`, or a deallocation request instead of an allocation request) returns `409 Conflict` with `error.code` `idempotency_key_reused`.
* Keys are scoped to the account.
* A request and its key are kept for at least 24 hours after the request completes. After that, the same key starts a new request, and the old `request_id` returns `404 Not Found`. A pending request is never removed.

> [!WARNING]
>
> With `idempotent=True`, the Python `signed_headers` helper generates a new key on every call. The JavaScript helper
> does the same with `idempotent: true`. For allocation and deallocation requests, leave that option unset. Create the
> key yourself and pass the same value on every retry, as the examples below do.

## One request per strategy at a time

Only one allocation or deallocation request can be in progress on a strategy at a time. A second request on the same strategy returns `409 Conflict` with `error.code` `allocation_in_progress` until the first one settles. Requests on different strategies run independently.

## Step 1: discover strategies by country

`GET /v1/earn/bonded/strategies` is **user-agnostic**. `country` is required and must be a two-letter ISO 3166-1 alpha-2 code. Strategy terms can vary by `country`. For a signed-in user, use the account strategy list in step 2 for their terms.

Some strategies have no lock-up: all three periods are 0 seconds, so the funds return as soon as a deallocation settles. Their `strategy_type` is `instant`, and strategies with lock-up periods are `bonded`. The same asset can have both, usually with a higher APY for `bonded`.

Filter with `type`, `yield_source`, and `symbol`:

| Parameter | Meaning | Allowed values |
| - | - | - |
| `type` | Asset classification, not the strategy's bonding type. | `fiat`, `crypto`, `stablecoin`, `xstock`, `tokenized_money_market_fund` |
| `yield_source` | Source of the strategy's yield. | `staking`, `base_rewards`, `opt_in_rewards` |
| `symbol` | Asset ticker symbol. | A symbol returned by the strategy list, such as `ETH` or `SOL`. |

```python Python theme={null}
def list_bonded_strategies_by_country(country, page_size=20, page_token=None):
    params = {"country": country, "page_size": str(page_size)}
    if page_token:
        params["page_token"] = page_token
    path = f"/v1/earn/bonded/strategies?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


country_page_token = None
while True:
    catalog = list_bonded_strategies_by_country("US", page_token=country_page_token)
    for strategy in catalog["data"]:
        print(
            f"{strategy['id']}: {strategy['symbol']} {strategy['strategy_type']}, {strategy['apy']}% APY"
        )
    country_page_token = catalog.get("next_page_token")
    if not country_page_token:
        break
```

```javascript JavaScript theme={null}
async function listBondedStrategiesByCountry(country, pageSize = 20, pageToken = null) {
  const params = new URLSearchParams({ country, page_size: String(pageSize) });
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/earn/bonded/strategies?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

let countryPageToken = null;
do {
  const catalog = await listBondedStrategiesByCountry('US', 20, countryPageToken);
  for (const strategy of catalog.data) {
    console.log(`${strategy.id}: ${strategy.symbol} ${strategy.strategy_type}, ${strategy.apy}% APY`);
  }
  countryPageToken = catalog.next_page_token;
} while (countryPageToken);
```

### Response example

```json theme={null}
{
  "data": [
    {
      "id": "ESDQCOL-WTZEU-NU55QF",
      "strategy_type": "bonded",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "yield_source": "staking",
      "apy": "3.10",
      "other_assets": [],
      "bonding_period": { "type": "fixed", "seconds": 0, "rewards": "not_accruing" },
      "unbonding_period": { "type": "variable", "seconds": 1209600, "rewards": "not_accruing" },
      "exit_queue_period": { "type": "fixed", "seconds": 5340, "rewards": "accruing" },
      "reward_frequency_seconds": 604800,
      "auto_compound": "enabled",
      "user_min_allocation": "0.01",
      "user_cap": "100",
      "fee_schedule": {
        "volume_basis": "shared_usd",
        "tiers": [
          { "min_volume": "0", "fee_percentage": "25" },
          { "min_volume": "1000000", "fee_percentage": "20" }
        ]
      }
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `id` | Strategy identifier. Pass it as `strategy_id` to allocate and deallocate. |
| `apy` | Estimated annual percentage yield, combined across all reward assets. Gross, before any reward fee. |
| `other_assets` | Reward assets other than the strategy's own, each with its share of `apy`. Usually empty. |
| `bonding_period` | Wait after an allocation before the funds start earning. |
| `exit_queue_period` | Wait after a deallocation before unbonding starts. |
| `unbonding_period` | Wait after the exit queue (or after the deallocation, when there is no exit queue) before the funds return to the account. |
| `reward_frequency_seconds` | Time between reward payouts. Usually one week. |
| `auto_compound` | `enabled` when rewards are added back to the allocation. |
| `user_min_allocation` | Minimum amount per allocation request, in the strategy's asset. Calculated from a USD minimum at the current exchange rate, so it can change. Fetch it again just before submitting the request. |
| `user_cap` | Most the account may allocate, in the strategy's asset. Absent when unlimited. |
| `fee_schedule` | Fee taken from the strategy's rewards, by allocated volume. Absent when the fee cannot be shown as one schedule. See [Reward fee schedule](#reward-fee-schedule). |

> [!TIP]
>
> APY is an estimate, not a guarantee. Label it "estimated". When `other_assets` is not empty, `apy` already includes
> their share: show it as the total, for example "3.10% (includes 0.50% EIGEN)".

### Reward fee schedule

`fee_schedule` shows the fee taken from the strategy's rewards. `apy` is gross, and `rewarded` amounts are net of this fee.

| Field | How to use it |
| - | - |
| `volume_basis` | What the volume in each tier counts. `strategy` is the account's allocation in this strategy, in the strategy's asset. `shared_usd` is the account's allocation in USD across every strategy on the same fee schedule. Funds in the exit queue or unbonding do not count. |
| `tiers[].min_volume` | Allocation this tier applies from, in the unit `volume_basis` names, as a decimal string. The first tier starts at `"0"`. |
| `tiers[].fee_percentage` | Total fee for the tier, as a share of each reward in percentage points. `"15"` means 15 percent. |

Tiers are sorted by ascending `min_volume`. In the example above, an account with less than 1,000,000 USD allocated pays 25 percent. From 1,000,000 USD it pays 20 percent.

## Step 2: discover strategies for an account

`GET /v1/accounts/{account_id}/earn/bonded/strategies` returns the same fields, with `fee_schedule` for the account, plus whether the account can act right now. It also lists strategies the account still holds an allocation in after it stopped being eligible, so the user can still deallocate.

This list is also paged. Follow `next_page_token` until it is absent, using the same loop as in step 1.

Use [Get portfolio](https://docs.services.payward.com/api-reference/portfolio/get-portfolio.md) to match strategies to assets the user already holds.

The total waiting time after deallocation is `exit_queue_period.seconds` plus `unbonding_period.seconds`. If either period's `type` is `variable`, the total is an estimate.

### Response example

```json theme={null}
{
  "data": [
    {
      "id": "ESDQCOL-WTZEU-NU55QF",
      "strategy_type": "bonded",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "yield_source": "staking",
      "apy": "3.10",
      "other_assets": [],
      "bonding_period": { "type": "fixed", "seconds": 0, "rewards": "not_accruing" },
      "unbonding_period": { "type": "variable", "seconds": 1209600, "rewards": "not_accruing" },
      "exit_queue_period": { "type": "fixed", "seconds": 5340, "rewards": "accruing" },
      "reward_frequency_seconds": 604800,
      "auto_compound": "enabled",
      "user_min_allocation": "0.01",
      "user_cap": "100",
      "can_allocate": true,
      "can_deallocate": true,
      "fee_schedule": {
        "volume_basis": "shared_usd",
        "tiers": [
          { "min_volume": "0", "fee_percentage": "25" },
          { "min_volume": "1000000", "fee_percentage": "20" }
        ]
      }
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `can_allocate` | Whether the account can allocate into this strategy now. Hide or disable the action when `false`. |
| `can_deallocate` | Whether the account can deallocate from this strategy now. |

## Step 3: allocate

Send a `POST` with the `amount` in the strategy's asset. The response is `202 Accepted` with a `request_id`.

```python Python theme={null}
def allocate_bonded(account_id, strategy_id, amount, idempotency_key):
    path = f"/v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/allocate"
    body = json.dumps({"amount": amount})

    headers = {**signed_headers("POST", path, body), "Idempotency-Key": idempotency_key}
    response = requests.post(
        BASE_URL + path,
        headers=headers,
        data=body,
        timeout=10,
    )
    return response.status_code, response.json()


account_id = "WFFGB6Z8AK5WF9JL"

# Keep this key until the request settles; reuse it on every retry.
key = str(uuid.uuid4())
status, body = allocate_bonded(account_id, "ESDQCOL-WTZEU-NU55QF", "2.0", key)
if status != 202:
    raise RuntimeError(f"Allocate rejected: {status} {body['error']['code']}")
request_id = body["data"]["request_id"]
```

```javascript JavaScript theme={null}
async function allocateBonded(accountId, strategyId, amount, idempotencyKey) {
  const path = `/v1/accounts/${accountId}/earn/bonded/strategies/${strategyId}/allocate`;
  const body = JSON.stringify({ amount });

  const headers = { ...signedHeaders('POST', path, body), 'Idempotency-Key': idempotencyKey };
  const response = await fetch(BASE_URL + path, {
    method: 'POST',
    headers,
    body,
  });

  return { status: response.status, body: await response.json() };
}

const accountId = 'WFFGB6Z8AK5WF9JL';

// Keep this key until the request settles; reuse it on every retry.
const key = crypto.randomUUID();
const { status, body } = await allocateBonded(accountId, 'ESDQCOL-WTZEU-NU55QF', '2.0', key);
if (status !== 202) throw new Error(`Allocate rejected: ${status} ${body.error.code}`);
const requestId = body.data.request_id;
```

### Response example

```json theme={null}
{
  "data": {
    "request_id": "EBARERNY-PXH3CV-XQJL2O"
  }
}
```

> [!NOTE]
>
> `202 Accepted` confirms the request was recorded, not that the funds moved. A request that is accepted can still fail
> when it is processed: always poll its status in step 4.

A request can be rejected up front, before it is recorded. Except for `idempotency_key_reused`, where another request already owns the key, no request is recorded and the key stays free: fix the input and retry with the same key. Branch on `error.code`:

| HTTP status | `error.code` | Meaning |
| - | - | - |
| `400 Bad Request` | `insufficient_balance` | Deallocate only: the amount is more than the funds that are earning. Bonding, exit queue and unbonding funds don't count. |
| `400 Bad Request` | `amount_too_high` | The amount is larger than the system can represent. |
| `400 Bad Request` | `bad_request` | Allocate only: the amount is below the strategy's `user_min_allocation`. |
| `400 Bad Request` | `bad_request` | An invalid `strategy_id`, including a failed checksum. Inspect the `strategy_id` entry in `causes[]`. |
| `403 Forbidden` | `forbidden` | The account isn't eligible for the strategy. |
| `403 Forbidden` | `gateway` | The API gateway rejected the key (`error.type: service_error`), for example because it lacks an `earn-bonded-read` or `earn-bonded-write` permission. Add the required [API key permissions](#api-key-permissions) in Console. |
| `404 Not Found` | `strategy_not_found` | The ID decodes correctly, but the strategy doesn't exist or isn't served by this API. |
| `409 Conflict` | `idempotency_key_reused` | The key was already used for a different request. |
| `409 Conflict` | `allocation_in_progress` | Another request on this strategy is still running. Wait and retry. |

An allocation request is not rejected up front when the account balance is insufficient. It is accepted and fails later, so check `error.reason` in step 4. Strategy caps work the same way and fail with `above_user_cap`.

New codes may be added. Treat an unknown code as a generic `bad_request`, `not_found` or `request_conflict` error for its status.

## Step 4: poll the request until it settles

`GET /v1/accounts/{account_id}/earn/bonded/requests/{request_id}` returns the request. `status` is `pending` until it is processed, then `succeeded` or `failed`; both are final.

```python Python theme={null}
def get_bonded_request(account_id, request_id):
    path = f"/v1/accounts/{account_id}/earn/bonded/requests/{request_id}"
    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()["data"]


def wait_for_bonded_request(account_id, request_id, interval=3, timeout=300):
    deadline = time.monotonic() + timeout
    while True:
        request = get_bonded_request(account_id, request_id)
        if request["status"] != "pending" or time.monotonic() > deadline:
            return request
        time.sleep(interval)


request = wait_for_bonded_request(account_id, request_id)
if request["status"] == "failed":
    print(f"Failed: {request['error']['reason']}")
```

```javascript JavaScript theme={null}
async function getBondedRequest(accountId, requestId) {
  const path = `/v1/accounts/${accountId}/earn/bonded/requests/${requestId}`;
  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  const body = await response.json();
  return body.data;
}

async function waitForBondedRequest(accountId, requestId, intervalMs = 3000, timeoutMs = 300000) {
  const deadline = Date.now() + timeoutMs;
  for (;;) {
    const request = await getBondedRequest(accountId, requestId);
    if (request.status !== 'pending' || Date.now() > deadline) return request;
    await new Promise(resolve => setTimeout(resolve, intervalMs));
  }
}

const request = await waitForBondedRequest(accountId, requestId);
if (request.status === 'failed') console.log(`Failed: ${request.error.reason}`);
```

### Response example

```json theme={null}
{
  "data": {
    "id": "EBARERNY-PXH3CV-XQJL2O",
    "idempotency_key": "11111111-1111-4111-8111-111111111111",
    "request_type": "allocate",
    "strategy_id": "ESDQCOL-WTZEU-NU55QF",
    "symbol": "ETH",
    "type": "crypto",
    "name": "Ethereum",
    "strategy_type": "bonded",
    "amount": "2.0",
    "status": "failed",
    "created_at": "2026-06-01T12:00:00Z",
    "completed_at": "2026-06-01T12:00:05Z",
    "error": {
      "reason": "insufficient_balance",
      "message": "The account balance is insufficient for this allocation."
    }
  }
}
```

| Field | How to use it |
| - | - |
| `status` | `pending`, `succeeded` or `failed`. Keep polling while `pending`. |
| `idempotency_key` | The key you sent. Use it to match the request to your own log. |
| `amount` | The amount as you submitted it. The settled amount can differ once it is rounded to the asset's precision. |
| `completed_at` | When the request reached a final status. Absent while `pending`. |
| `error.reason` | Present only when `status` is `failed`. Branch on it, not on `error.message`. |

A failed request is still a `200 OK`: the outcome is in `status` and `error`, not in the HTTP status. A strategy cap is checked here, after the request is accepted: an allocation above `user_cap` fails with `above_user_cap`. Known `error.reason` values are `above_user_cap`, `insufficient_balance`, `not_eligible`, `canceled` and `internal`. New values may be added: treat an unknown one as a generic failure.

> [!NOTE]
>
> A failed request owns its key. Retrying the same key returns the same failed request. To try again, for example after
> the user tops up, send a new request with a new key.

To list every request of the account that is still pending, use `GET /v1/accounts/{account_id}/earn/bonded/requests`. A request drops off that list once it reaches a final status.

## Step 5a: list allocations

`GET /v1/accounts/{account_id}/earn/bonded/allocations` returns one entry per strategy, with the amount in each lifecycle state and the soonest upcoming change.

### Response example

```json theme={null}
{
  "quote_symbol": "USD",
  "quote_type": "fiat",
  "data": [
    {
      "strategy_id": "ESDQCOL-WTZEU-NU55QF",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "strategy_type": "bonded",
      "total": "2.0",
      "total_in_quote": "4000.0",
      "bonding": "2.0",
      "bonding_in_quote": "4000.0",
      "earning": "0",
      "earning_in_quote": "0",
      "exit_queue": "0",
      "exit_queue_in_quote": "0",
      "unbonding": "0",
      "unbonding_in_quote": "0",
      "next_transition": {
        "amount": "2.0",
        "amount_in_quote": "4000.0",
        "state": "bonding",
        "next_state": "earning",
        "transitions_at": "2026-06-01T12:00:00Z"
      }
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `total` / `_in_quote` | Everything allocated to the strategy, across all states. |
| `bonding`, `earning`, `exit_queue`, `unbonding` | The part in each state. They add up to `total`. |
| `next_transition` | The soonest scheduled change. Absent when nothing is bonding, in the exit queue or unbonding. |
| `next_transition.next_state` | The state entered next. Absent when the funds leave the strategy after this change. |
| `next_transition.available_at` | When the funds become available. For `exit_queue` it is an estimate that includes the unbonding period. Absent while bonding. |

## Step 5b: list allocation state changes

`GET /v1/accounts/{account_id}/earn/bonded/allocation-states` lists every upcoming change, ordered by when each allocation leaves its current state. Use it for a timeline: "1 ETH unbonds on June 8". Filter with `strategy_id`, and with `state` (`bonding`, `exit_queue` or `unbonding`) more than once to get several states.

### Response example

```json theme={null}
{
  "quote_symbol": "USD",
  "quote_type": "fiat",
  "data": [
    {
      "strategy_id": "ESDQCOL-WTZEU-NU55QF",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "amount": "1.0",
      "amount_in_quote": "2000.0",
      "state": "exit_queue",
      "next_state": "unbonding",
      "transitions_at": "2026-06-01T12:00:00Z",
      "available_at": "2026-06-15T12:00:00Z"
    }
  ]
}
```

## Step 6: read rewards

Rewards are paid once a week, at about the same time for every strategy. Each user's account has its own weekly payout time, derived from its account ID. It is fixed for the lifetime of the account and cannot be changed.

For each strategy returned by [upcoming rewards](#upcoming-rewards), `next_reward_date` gives the expected payout date and time in UTC.

Three endpoints cover rewards. All take `quote_symbol` / `quote_type`; the two lists also page.

| Endpoint | Returns |
| - | - |
| `GET /v1/accounts/{account_id}/earn/bonded/rewards/summary` | The total paid across every strategy, in the quote currency, net of any reward fee, calculated like `rewarded_in_quote`. The headline figure. |
| `GET /v1/accounts/{account_id}/earn/bonded/rewards` | Lifetime rewards per strategy. Strategies that never paid a reward are left out. |
| `GET /v1/accounts/{account_id}/earn/bonded/rewards/upcoming` | The expected reward of each strategy at its next reward date. Strategies with nothing pending are left out. |

### Rewards per strategy

```json theme={null}
{
  "quote_symbol": "USD",
  "quote_type": "fiat",
  "data": [
    {
      "strategy_id": "ESDQCOL-WTZEU-NU55QF",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "strategy_type": "bonded",
      "rewarded": "0.0175",
      "rewarded_in_quote": "43.75"
    }
  ]
}
```

`rewarded` is one lifetime figure in the strategy's asset, net of any reward fee. Rewards paid in another asset are converted into the strategy's asset when they are paid and included. `rewarded_in_quote` is calculated from the USD value of each reward at the time it was paid, so it does not move with the asset price. With `quote_symbol=USD` it is that USD figure. For any other `quote_symbol`, the USD figure is calculated into that currency at today's USD rate, so it can change with fiat exchange rates.

### Upcoming rewards

```json theme={null}
{
  "quote_symbol": "USD",
  "quote_type": "fiat",
  "data": [
    {
      "strategy_id": "ESDQCOL-WTZEU-NU55QF",
      "symbol": "ETH",
      "type": "crypto",
      "name": "Ethereum",
      "upcoming_reward": "0.0056",
      "upcoming_reward_in_quote": "14.00",
      "next_reward_date": "2026-06-01T00:00:00Z",
      "other_assets": [
        {
          "symbol": "EIGEN",
          "type": "crypto",
          "name": "Eigenlayer",
          "upcoming_reward": "0.1",
          "upcoming_reward_in_quote": "0.25"
        }
      ]
    }
  ]
}
```

| Field | How to use it |
| - | - |
| `upcoming_reward` / `_in_quote` | The reward accrued so far plus the estimate up to `next_reward_date`, net of any reward fee. Leaves out rewards that belong to a later payout period. An estimate, not a guarantee. |
| `next_reward_date` | When the reward is expected to be paid. A target, not a guarantee: payouts can be delayed. Shared by every entry in `other_assets`. |
| `other_assets` | The part paid in other assets than the strategy's own. Usually empty. |

## Step 7: deallocate

Deallocation requests work like allocation requests: same body, same required `Idempotency-Key` header and rules, same `202 Accepted` with a `request_id` to poll. Partial deallocation is allowed. To leave a strategy completely, send the full `earning` amount. Funds that are bonding, in the exit queue or unbonding can't be deallocated. There is no "deallocate all" shortcut.

```python Python theme={null}
def deallocate_bonded(account_id, strategy_id, amount, idempotency_key):
    path = f"/v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/deallocate"
    body = json.dumps({"amount": amount})

    headers = {**signed_headers("POST", path, body), "Idempotency-Key": idempotency_key}
    response = requests.post(
        BASE_URL + path,
        headers=headers,
        data=body,
        timeout=10,
    )
    return response.status_code, response.json()


# Keep this key until the request settles; reuse it on every retry.
key = str(uuid.uuid4())
status, body = deallocate_bonded(account_id, "ESDQCOL-WTZEU-NU55QF", "2.0", key)
if status != 202:
    raise RuntimeError(f"Deallocate rejected: {status} {body['error']['code']}")
request_id = body["data"]["request_id"]
```

```javascript JavaScript theme={null}
async function deallocateBonded(accountId, strategyId, amount, idempotencyKey) {
  const path = `/v1/accounts/${accountId}/earn/bonded/strategies/${strategyId}/deallocate`;
  const body = JSON.stringify({ amount });

  const headers = { ...signedHeaders('POST', path, body), 'Idempotency-Key': idempotencyKey };
  const response = await fetch(BASE_URL + path, {
    method: 'POST',
    headers,
    body,
  });

  return { status: response.status, body: await response.json() };
}

// Keep this key until the request settles; reuse it on every retry.
const deallocationKey = crypto.randomUUID();
const { status: deallocationStatus, body: deallocationBody } = await deallocateBonded(
  accountId,
  'ESDQCOL-WTZEU-NU55QF',
  '2.0',
  deallocationKey,
);
if (deallocationStatus !== 202) {
  throw new Error(`Deallocate rejected: ${deallocationStatus} ${deallocationBody.error.code}`);
}
const deallocationRequestId = deallocationBody.data.request_id;
```

### Response example

```json theme={null}
{
  "data": {
    "request_id": "EBARERNY-PXH3CV-XQJL2O"
  }
}
```

A rejected deallocation request returns the same codes as an allocation request: see the table in step 3. Poll the `request_id` as in step 4. The funds then pass through any nonzero exit queue and unbonding periods. Even when both periods are zero, deallocated funds can show as `unbonding` for a brief period. Follow them with `allocation-states` until they are available.

## Error handling

All error responses use the standard envelope:

```json theme={null}
{
  "error": {
    "type": "earn_error",
    "status": 400,
    "code": "insufficient_balance",
    "instance": "req_01H00000000000000000000000",
    "causes": [
      {
        "field": "amount",
        "message": "Not enough funds to deallocate"
      }
    ]
  }
}
```

`causes[]` isn't always present. Some invalid input returns `400 Bad Request` without it: an unknown `yield_source` or `type` filter value, or an out-of-range `page_size`. Validate input before you send it, and don't depend on `causes[]` to find the problem.

| HTTP status | `error.code` | Cause | Remediation |
| - | - | - | - |
| `400 Bad Request` | `bad_request`, `insufficient_balance`, `amount_too_high` | Invalid input, an unsupported quote, a bad page token, or a rejected allocation or deallocation request (see step 3) | Inspect `error.code` and `causes[]`. Fix the input; the same key can be reused. |
| `401 Unauthorized` | Not applicable | Missing or invalid signature, key, or timestamp | Verify `API-Key`, `API-Timestamp`, and `API-Sign`. See [Troubleshooting](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md#troubleshooting). |
| `403 Forbidden` | `forbidden` | The account is not authorized to use Bonded Earn | Confirm the account's product entitlements. |
| `403 Forbidden` | `gateway` | The API gateway rejected the key (`error.type: service_error`), for example because it lacks the required earn permission. | Add the required [API key permissions](#api-key-permissions) in Console. |
| `404 Not Found` | `strategy_not_found`, `not_found` | Bonded Earn is not enabled, the strategy or request doesn't exist, or the request has expired | Check the identifiers. A request id can expire 24 hours or more after the request completes. |
| `409 Conflict` | `idempotency_key_reused`, `allocation_in_progress` | The key was used for a different request, or another request on the strategy is still running | Use a new key for a new request; for `allocation_in_progress`, wait for the running request. |
| `429 Too Many Requests` | Not applicable | Rate limit hit | Honor `Retry-After` and back off exponentially. |
| `500` / `503` / `504` | Not applicable | Server error or timeout | Retry with the **same** `Idempotency-Key`: a request that was recorded is not run twice. |

### Best practices

1. **One key per request, reused on every retry.** That makes retries after a timeout safe.
2. **Always poll the status.** `202 Accepted` means recorded, not done. A failed request comes back as `200 OK` with `status: failed`.
3. **Branch on codes, not messages.** Use `error.code` for rejections and `error.reason` for failed requests, and handle unknown values generically.
4. **Use `can_allocate` / `can_deallocate`** from the account strategy list to decide which actions to offer.
5. **Pass `quote_symbol` consistently** across allocations and rewards so converted totals line up.

## API reference

| Method | Endpoint | Description | API key permission |
| - | - | - | - |
| GET | [`/v1/earn/bonded/strategies`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-bonded-earn-strategies) | List Bonded Earn strategies available in a country (user-agnostic). Required `country` query parameter. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/strategies`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-account-bonded-earn-strategies) | List the account's strategies, with whether it can allocate or deallocate now. | `earn-bonded-read` |
| POST | [`/v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/allocate`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/allocate-to-a-bonded-earn-strategy) | Allocate into a strategy. Async; requires `Idempotency-Key`. Returns a `request_id`. | `earn-bonded-write` |
| POST | [`/v1/accounts/{account_id}/earn/bonded/strategies/{strategy_id}/deallocate`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/deallocate-from-a-bonded-earn-strategy) | Deallocate from a strategy. Async; requires `Idempotency-Key`. Returns a `request_id`. | `earn-bonded-write` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/requests/{request_id}`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/get-bonded-earn-request-status) | Get the status of one allocation or deallocation request. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/requests`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-pending-bonded-earn-requests) | List requests that are still pending. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/allocations`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-bonded-earn-allocations) | List allocation totals per strategy, with the amount in each lifecycle state. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/allocation-states`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-bonded-earn-allocation-states) | List upcoming allocation state changes. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/rewards/summary`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/get-bonded-earn-reward-summary) | Get the total historical rewards across every strategy in the quote currency. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/rewards`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-bonded-earn-rewards-by-strategy) | List historical rewards per strategy. | `earn-bonded-read` |
| GET | [`/v1/accounts/{account_id}/earn/bonded/rewards/upcoming`](https://docs.services.payward.com/api-reference/production-live/bonded-earn/list-upcoming-bonded-earn-rewards) | List the next reward per strategy. | `earn-bonded-read` |
