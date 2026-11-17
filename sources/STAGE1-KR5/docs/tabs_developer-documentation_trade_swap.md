> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Swaps

> The Swaps API offers institutional FX-style trading. Lock a price for ~2 minutes, execute against the locked quote, then poll until the trade reaches a terminal state.

## Prerequisites

* Payward Services API credentials (see the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md)).
* A verified user with at least one account and sufficient balance in the source asset.
* Examples read the API base URL from the `PWS_BASE_URL` environment variable, and credentials from `PWS_API_KEY` and `PWS_API_SECRET`.

## Workflow

**1. Check quote limits (optional)**

Confirm the amount you plan to fix falls within current min/max bounds.

`GET /v1/accounts/{account_id}/quotes/limits`

**2. Request a quote**

Lock a price for \~2 minutes.

`POST /v1/accounts/{account_id}/quotes`

**3. Execute the quote**

Commit the locked price before it expires.

`POST /v1/accounts/{account_id}/quotes/{quote_id}/execute`

**4. Poll for terminal status**

Wait for the quote to settle, or subscribe to webhooks.

`GET /v1/accounts/{account_id}/quotes/{quote_id}`

## Quote lifecycle

| Status | Description |
| - | - |
| `offered` | Quote created and locked. May still expire if the market moves too far before you execute. |
| `executing` | Execution accepted. The trade is being processed asynchronously. |
| `executed` | Terminal. The trade settled. |
| `expired` | Terminal. The TTL elapsed, or the market moved too far for the locked price to remain valid. |
| `failed` | Terminal. The trade failed to execute. |

A quote is valid for approximately 120 seconds (2 minutes) after creation. Calling execute on a quote whose `expires_at` has passed returns `410 Gone`.

## Specifying the trade

A quote needs `from`, `to`, and `fee` fields. Set the `amount` on **exactly one** of `from` or `to` to indicate which side of the trade is fixed. The server calculates the other side. Setting both or neither returns `400 Bad Request`.

| Scenario | `from.amount` | `to.amount` |
| - | - | - |
| "Sell 0.5 BTC for whatever USD that yields" | `"0.5"` | omit |
| "Buy whatever BTC \$5,000 yields" | omit | `"5000"` |

Each side carries a `type` that classifies the asset:

| `type` | Examples |
| - | - |
| `fiat` | `USD`, `EUR`, `GBP` |
| `crypto` | `BTC`, `ETH`, `SOL` |
| `stablecoin` | `USDC`, `USDT`, `DAI` |
| `xstock` | `TSLAx`, `AAPLx` |

The `fee` object sets the partner's fee applied on top of the execution price. Provide it as basis points, a flat amount, or both:

* `fee.bps`: fee in basis points (1 bps = 0.01%, so 50 bps is 0.5%). Defaults to `0` when omitted.
* `fee.absolute`: a flat fee amount denominated in the quote currency, sent as a decimal string (e.g., `"10.00"`).

When both are set they combine. Omit `fee` entirely to charge no partner fee. An `absolute` value that is too small to apply or too large for the trade size is rejected with `400 Bad Request` on `fee.absolute`.

## Check quote limits

Before creating a quote, you can fetch the effective amount limits for a pair on the selected account:

```
GET /v1/accounts/{account_id}/quotes/limits
```

Required query parameters:

| Parameter | Description |
| - | - |
| `from_symbol` | Source asset ticker (e.g., `USD`) |
| `from_type` | Source asset classification (`fiat`, `crypto`, `stablecoin`, or `xstock`) |
| `to_symbol` | Destination asset ticker (e.g., `ETH`) |
| `to_type` | Destination asset classification |
| `amount_side` | Side whose amount you will fix when creating the quote (`from` or `to`). Limits are in that asset. |

Limits are a point-in-time estimate and can change before you create a quote. Clamp create-quote amounts to `[minimum_swap, maximum]`. When present, `limit_reasons` explains which constraints contributed to `maximum`. Dust-only floors are not exposed on this endpoint; a dust-sweep-specific minimum may be added later.

### Response example

```json theme={null}
{
  "data": {
    "asset": { "symbol": "USD", "type": "fiat" },
    "minimum_swap": "1",
    "maximum": "150000",
    "precision": 2,
    "limit_reasons": ["liquidity"]
  }
}
```

| Field | Description |
| - | - |
| `minimum_swap` | Smallest amount valid for create quote in the `amount_side` asset |
| `maximum` | Largest amount currently available in the `amount_side` asset |
| `precision` | Max decimal places for ordinary tradable amounts |
| `limit_reasons` | Optional constraints that shaped `maximum` (`user_balance`, `liquidity`, `other`) |

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

## Step 1: request a quote

Send a `POST` to `/v1/accounts/{account_id}/quotes` with the trade body.

```python Python theme={null}
def create_swap_quote(account_id):
    path = f"/v1/accounts/{account_id}/quotes"
    body = json.dumps(
        {
            "from": {"symbol": "BTC", "type": "crypto", "amount": "0.5"},
            "to": {"symbol": "USD", "type": "fiat"},
            "fee": {"bps": 50},
        }
    )

    response = requests.post(
        BASE_URL + path,
        headers=signed_headers("POST", path, body),
        data=body,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


account_id = "NL00KRAK0123456789"
quote = create_swap_quote(account_id)
print(f"Quote ID:    {quote['data']['id']}")
print(f"Status:      {quote['data']['status']}")
print(f"Expires at:  {quote['data']['expires_at']}")
print(
    f"You send:    {quote['data']['from']['amount']} {quote['data']['from']['symbol']}"
)
print(f"You receive: {quote['data']['to']['amount']} {quote['data']['to']['symbol']}")
```

```javascript JavaScript theme={null}
async function createSwapQuote(accountId) {
  const path = `/v1/accounts/${accountId}/quotes`;
  const body = JSON.stringify({
    from: { symbol: 'BTC', type: 'crypto', amount: '0.5' },
    to: { symbol: 'USD', type: 'fiat' },
    fee: { bps: 50 },
  });

  const response = await fetch(BASE_URL + path, {
    method: 'POST',
    headers: signedHeaders('POST', path, body),
    body,
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const accountId = 'NL00KRAK0123456789';
const quote = await createSwapQuote(accountId);
console.log('Quote ID:   ', quote.data.id);
console.log('Status:     ', quote.data.status);
console.log('Expires at: ', quote.data.expires_at);
```

### Response example

```json theme={null}
{
  "data": {
    "id": "Q-BTC2USD-1",
    "status": "offered",
    "created_at": "2026-04-23T16:00:00Z",
    "expires_at": "2026-04-23T16:00:30Z",
    "from": {
      "symbol": "BTC",
      "type": "crypto",
      "amount": "0.5"
    },
    "to": {
      "symbol": "USD",
      "type": "fiat",
      "amount": "31495.50"
    },
    "fees": {
      "trade": {
        "symbol": "USD",
        "type": "fiat",
        "amount": "150.00"
      }
    },
    "rate": {
      "base": { "symbol": "BTC", "type": "crypto" },
      "quote": { "symbol": "USD", "type": "fiat" },
      "price": "63291.00"
    }
  }
}
```

> [!WARNING]
>
> Quotes expire after **120 seconds** (2 minutes). Execute the quote promptly or request a new one if it expires. The
> exact expiration time is returned in the `expires_at` field of the quote response.

## Step 2: execute the quote

Send a `POST` to `/v1/accounts/{account_id}/quotes/{quote_id}/execute` with an empty JSON object, `{}`, as the body. The response confirms the quote moved to `executing`; settlement happens asynchronously.

```python Python theme={null}
def execute_swap_quote(account_id, quote_id):
    path = f"/v1/accounts/{account_id}/quotes/{quote_id}/execute"
    body = "{}"

    response = requests.post(
        BASE_URL + path,
        headers=signed_headers("POST", path, body),
        data=body,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


execution = execute_swap_quote(account_id, quote["data"]["id"])
print(f"Status: {execution['data']['status']}")
```

```javascript JavaScript theme={null}
async function executeSwapQuote(accountId, quoteId) {
  const path = `/v1/accounts/${accountId}/quotes/${quoteId}/execute`;
  const body = '{}';

  const response = await fetch(BASE_URL + path, {
    method: 'POST',
    headers: signedHeaders('POST', path, body),
    body,
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const execution = await executeSwapQuote(accountId, quote.data.id);
console.log('Status:', execution.data.status);
```

### Response example

```json theme={null}
{
  "data": {
    "id": "Q-BTC2USD-1",
    "status": "executing"
  }
}
```

## Step 3: poll for terminal status

After executing, poll `GET /v1/accounts/{account_id}/quotes/{quote_id}` until `status` reaches a terminal value (`executed`, `expired`, or `failed`).

```python Python theme={null}
def get_swap_quote(account_id, quote_id):
    path = f"/v1/accounts/{account_id}/quotes/{quote_id}"
    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


def wait_for_terminal_status(account_id, quote_id, max_attempts=60):
    terminal = {"executed", "expired", "failed"}

    for _ in range(max_attempts):
        quote = get_swap_quote(account_id, quote_id)
        status = quote["data"]["status"]
        print(f"Status: {status}")

        if status in terminal:
            return quote

        time.sleep(1)

    raise RuntimeError("Quote did not reach a terminal state in time")


final = wait_for_terminal_status(account_id, quote["data"]["id"])
```

```javascript JavaScript theme={null}
async function getSwapQuote(accountId, quoteId) {
  const path = `/v1/accounts/${accountId}/quotes/${quoteId}`;
  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

async function waitForTerminalStatus(accountId, quoteId, maxAttempts = 60) {
  const terminal = new Set(['executed', 'expired', 'failed']);

  for (let i = 0; i < maxAttempts; i++) {
    const quote = await getSwapQuote(accountId, quoteId);
    const { status } = quote.data;
    console.log('Status:', status);

    if (terminal.has(status)) {
      return quote;
    }

    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  throw new Error('Quote did not reach a terminal state in time');
}

const final = await waitForTerminalStatus(accountId, quote.data.id);
```

### Response example

```json theme={null}
{
  "data": {
    "id": "Q-BTC2USD-1",
    "status": "executed",
    "created_at": "2026-04-23T16:00:00Z",
    "expires_at": "2026-04-23T16:00:30Z",
    "from": {
      "symbol": "BTC",
      "type": "crypto",
      "amount": "0.5"
    },
    "to": {
      "symbol": "USD",
      "type": "fiat",
      "amount": "31495.50"
    },
    "fees": {
      "trade": {
        "symbol": "USD",
        "type": "fiat",
        "amount": "150.00"
      }
    },
    "rate": {
      "base": { "symbol": "BTC", "type": "crypto" },
      "quote": { "symbol": "USD", "type": "fiat" },
      "price": "63291.00"
    }
  }
}
```

> [!TIP]
>
> Instead of polling, subscribe to the `quote.executed` and `quote.execution_failed` webhooks and use `GET` only for
> reconciliation.

## Error handling

| HTTP status | Code | Cause | Remediation |
| - | - | - | - |
| `400 Bad Request` | validation error | Both or neither of `from.amount` / `to.amount` were set | Set exactly one side of the trade |
| `409 Conflict` | `insufficient_funds` | The account balance cannot cover the quote | Fund the account or request a smaller quote |
| `410 Gone` | `quote_expired` | The quote was executed after its `expires_at` | Request a new quote, review its `rate` and `fees`, then execute it before `expires_at` |

### Best practices

* **Capture `Request-Id` from response headers.** It speeds up support investigations.

## API reference

| Method | Endpoint | Description |
| - | - | - |
| GET | [`/v1/accounts/{account_id}/quotes/limits`](https://docs.services.payward.com/api-reference/swaps/get-quote-limits) | Get effective quote amount limits |
| POST | [`/v1/accounts/{account_id}/quotes`](https://docs.services.payward.com/api-reference/swaps/create-quote) | Create a swap quote (locks price \~2m) |
| POST | [`/v1/accounts/{account_id}/quotes/{quote_id}/execute`](https://docs.services.payward.com/api-reference/swaps/execute-quote) | Execute a locked quote |
| GET | [`/v1/accounts/{account_id}/quotes/{quote_id}`](https://docs.services.payward.com/api-reference/swaps/get-quote) | Read the current state of a quote |
