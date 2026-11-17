> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Portfolio

> Use the Portfolio API to show account value, asset positions, transaction history, and historical portfolio performance.

## Overview

The Portfolio API gives you the account-level view after users deposit, withdraw, trade, transfer funds, or earn rewards. Use it to show current portfolio value, per-asset balances, an activity feed, and historical performance. Subscribe to Portfolio transaction webhooks when you want change notifications without continuous polling.

All Portfolio endpoints are scoped to a specific `account_id`. Pass the same `quote_symbol` and `quote_type` across the current portfolio, history, and transaction calls when you want their monetary values to use the same quote asset.

## Prerequisites

* Payward Services API credentials (see the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md))
* A verified user with at least one account
* Base URL: `https://api.services.payward.com`

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

Every Portfolio endpoint is a `GET` with query parameters. Sign the query string along with the path by passing the parameters as the helper's `params` argument.

## Portfolio workflow

Use this flow when you build a portfolio dashboard or reconcile user activity after payments and trades.

**1. Show the current portfolio**

Fetch account-level values and the per-asset balance breakdown in one snapshot.

`GET /v1/accounts/{account_id}/portfolio`

**2. Build the activity feed**

Fetch transaction history for deposits, withdrawals, transfers, swaps, price trigger swaps, and earn rewards.

`GET /v1/accounts/{account_id}/portfolio/transactions`

**3. Subscribe to transaction changes**

Register for `transaction.*` webhook events. Retrieve the complete transaction from Portfolio after each notification.

`POST /v1/webhooks`

**4. Chart portfolio performance**

Fetch historical balances and valuations for a selected time window.

`GET /v1/accounts/{account_id}/portfolio/history`

## Step 1: get the current portfolio

Call `GET /v1/accounts/{account_id}/portfolio` to get the account totals and per-asset balances in one consistent snapshot. Set `with_zero_balances=true` when you also need assets with zero balances, such as when you display every supported asset.

```python Python theme={null}
def get_portfolio(
    account_id, quote_symbol="USD", quote_type="fiat", with_zero_balances=False
):
    params = {
        "quote_symbol": quote_symbol,
        "quote_type": quote_type,
        "with_zero_balances": str(with_zero_balances).lower(),
    }
    path = f"/v1/accounts/{account_id}/portfolio?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


portfolio = get_portfolio("ABCD1234EFGH5678")
print(portfolio["data"]["total_in_quote"])
for asset in portfolio["data"]["assets"]:
    print(
        asset["symbol"],
        asset["balances"]["total"],
        asset["balances"].get("total_in_quote"),
    )
```

```javascript JavaScript theme={null}
async function getPortfolio(accountId, quoteSymbol = 'USD', quoteType = 'fiat', withZeroBalances = false) {
  const params = new URLSearchParams({
    quote_symbol: quoteSymbol,
    quote_type: quoteType,
    with_zero_balances: String(withZeroBalances),
  });
  const path = `/v1/accounts/${accountId}/portfolio?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const portfolio = await getPortfolio('ABCD1234EFGH5678');
console.log(portfolio.data.total_in_quote);
for (const asset of portfolio.data.assets) {
  console.log(asset.symbol, asset.balances.total, asset.balances.total_in_quote);
}
```

Use these account-level fields for the dashboard header:

| Field | How to use it |
| - | - |
| `as_of` | Show when the latest index price in the snapshot was updated. |
| `quote` | Identify the quote asset used by monetary values throughout the snapshot. |
| `total_in_quote` | Show total account value in the quote asset. |
| `availability.available_in_quote` | Show funds available for trading or withdrawal after holds. |
| `availability.withheld.*_in_quote` | Explain amounts held for open orders, earn products, or other temporary holds. |
| `pnl.*_in_quote` | Show account-level average-cost-basis PnL when available. |
| `assets` | Render the per-asset balance breakdown from the same snapshot. |

For each item in `assets`, use these fields:

| Field | How to use it |
| - | - |
| `symbol` and `type` | Identify the asset unambiguously. |
| `index_price_in_quote` | Show the price of one native asset unit in the top-level quote asset. |
| `balances.total` | Show the balance in the asset's native display units. |
| `balances.total_in_quote` | Show the value of that same total in the top-level quote asset. |
| `balances.main` | Show balances held in the main source, including balances used by spot trading and received from swaps. |
| `held_for_orders` | Show native asset amounts held for open orders. |
| `earn` | Break earn balances down by liquidity state and yield source. |
| `availability` | Show native amounts available for trading or internal transfer. |
| `credit_line`, `spot_margin`, and `pnl` | Add credit and explicitly quoted spot-margin and average-cost-basis details when they apply. |

Quote-denominated monetary amounts end in `_in_quote`. Native asset amounts omit that suffix. For example, `balances.total` is an amount in the asset itself; it is not a price. Use `balances.total_in_quote` when you need its value in `data.quote`. The nested balance sources use the same `total` and `total_in_quote` naming.

Account-level `availability` is an aggregate in `data.quote`; it does not belong inside `balances.main`. Per-asset `availability.trade` and `availability.transfer` are native amounts for those actions.

The `pnl` objects are optional. A PnL status can be `in_progress` while its corresponding value is absent or not final. Numeric PnL fields ending in `_in_quote` use `data.quote`. `pnl.reference_currency` identifies Portfolio's calculation basis; it does not change the display currency.

See the [Get portfolio API reference](https://docs.services.payward.com/api-reference/portfolio/get-portfolio.md) for every query parameter and response field.

## Step 2: build the activity feed

Call `GET /v1/accounts/{account_id}/portfolio/transactions` to list user-visible portfolio activity. Use it after a deposit, withdrawal, swap, price trigger swap, or earn reward to show what changed and support reconciliation.

```python Python theme={null}
def list_portfolio_transactions(account_id, page_token=None):
    params = [
        ("types", "deposit"),
        ("types", "withdrawal"),
        ("types", "swap"),
        ("statuses", "successful"),
        ("start_timestamp", "2026-04-01T00:00:00Z"),
        ("end_timestamp", "2026-04-30T23:59:59Z"),
        ("sort_direction", "desc"),
        ("quote_symbol", "USD"),
        ("quote_type", "fiat"),
        ("page_size", "20"),
    ]
    if page_token:
        params.append(("page_token", page_token))
    path = f"/v1/accounts/{account_id}/portfolio/transactions?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


transactions = list_portfolio_transactions("ABCD1234EFGH5678")
for transaction in transactions["data"]:
    print(transaction["timestamp"], transaction["type"], transaction["status"])
```

```javascript JavaScript theme={null}
async function listPortfolioTransactions(accountId, pageToken = null) {
  const params = new URLSearchParams({
    start_timestamp: '2026-04-01T00:00:00Z',
    end_timestamp: '2026-04-30T23:59:59Z',
    sort_direction: 'desc',
    quote_symbol: 'USD',
    quote_type: 'fiat',
    page_size: '20',
  });
  // `types` and `statuses` are arrays: repeat a key to filter on several values at once.
  params.append('types', 'deposit');
  params.append('types', 'withdrawal');
  params.append('types', 'swap');
  params.append('statuses', 'successful');
  if (pageToken) params.set('page_token', pageToken);
  const path = `/v1/accounts/${accountId}/portfolio/transactions?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const transactions = await listPortfolioTransactions('ABCD1234EFGH5678');
for (const transaction of transactions.data) {
  console.log(transaction.timestamp, transaction.type, transaction.status);
}
```

Common filters:

| Filter | How to use it |
| - | - |
| `types` | Filter by `swap`, `price_trigger_swap`, `recurring_swap`, `earn_reward`, `deposit`, `withdrawal`, or `transfer`. |
| `statuses` | Filter by `in_progress`, `successful`, or `failed`. |
| `start_timestamp` and `end_timestamp` | Restrict results to a time window. |
| `assets` | Filter by asset references using indexed deep-object syntax. |
| `ids` | Look up specific portfolio transaction IDs. |
| `references` | Look up originating Funding references using indexed `kind` and `id` fields. |
| `sort_direction` | Return newest-first with `desc` or oldest-first with `asc`. |
| `quote_symbol` | Add best-effort `amount_in_quote` values to spend, receive, and fee amounts. Defaults to `USD`. |
| `quote_type` | Use `fiat` or `stablecoin`. `stablecoin` requires `quote_symbol`. |

Each returned transaction includes the required fields `id`, `timestamp`, `type`, and `status`. It can include `spend`, `receive`, or both. Failed transactions can omit movement details.

Transactions without a defined lifecycle status are not returned.

Deposits and withdrawals can also carry `details` with `type: "funding"` and a `crypto_transaction_id` you can use to link to a block explorer. For withdrawals, the hash can remain absent after broadcast or block inclusion until completion is reported. Fiat funding omits this field.

Successful `swap`, `price_trigger_swap`, and `recurring_swap` transactions include `details.quote_id`. Use it to correlate the transaction with the quote that executed it. Failed swap attempts appear with `status: "failed"`. Their details use `type: "failed_swap"`, `type: "failed_price_trigger_swap"`, or `type: "failed_recurring_swap"` and include `failure_reason`. The reason is one of `insufficient_funds`, `card_issue`, `user_account_issue`, or `other`.

### Reconcile a fiat withdrawal

Use the `withdrawal_id` returned by [Create withdrawal](https://docs.services.payward.com/api-reference/funds/create-withdrawal.md) to find the corresponding Portfolio transaction in the same account:

```http theme={null}
GET /v1/accounts/{account_id}/portfolio/transactions?types[0]=withdrawal&references[0][kind]=funding&references[0][id]={withdrawal_id}
```

This works for withdrawals to registered funding addresses and supported linked bank accounts. The result has
`type: "withdrawal"` and `reference.kind: "funding"`. Its `reference.id` matches the Funding withdrawal ID; the
Portfolio transaction's own `id` is a separate identifier.

Transactions can appear asynchronously. An empty response immediately after submission does not establish that the
withdrawal failed. Poll with `statuses` omitted so you can observe both `in_progress` and a terminal status,
`successful` or `failed`. Filtering only for `in_progress` hides the transaction once it reaches a terminal status.

Fiat withdrawal amounts appear under `spend` with the public asset symbol and `type: "fiat"`. For a same-asset fee,
`spend.total` is the gross debit, `spend.sub_total` is the amount excluding the fee, and `spend.fee` is the fee.
Blockchain fields are absent for fiat withdrawals.

Use `next_page_token` as `page_token` to fetch more transactions. Continue until the token is absent, even when a page
is empty.

See the [List Portfolio Transactions API reference](https://docs.services.payward.com/api-reference/portfolio/list-portfolio-transactions.md) for all filters and response fields.

## Step 3: subscribe to transaction changes

Register a webhook to receive change notifications for the Portfolio transaction categories you use. One webhook can subscribe to any combination of these events:

| Event type | Portfolio transaction category | Correlation fields when available |
| - | - | - |
| `transaction.swap` | `swap` | `quote_id` |
| `transaction.price_trigger_swap` | `price_trigger_swap` | `quote_id` |
| `transaction.earn_reward` | `earn_reward` | `strategy_id`, `reward_id` |
| `transaction.deposit` | `deposit` | `funding_reference`, `crypto_transaction_id` |
| `transaction.withdrawal` | `withdrawal` | `funding_reference`, `crypto_transaction_id` |
| `transaction.transfer` | `transfer` | `transfer_id` |

Every payload contains `type`, `transaction_id`, `user_id`, `account_id`, and `timestamp`. It can also contain `status`.

Treat the webhook as a change notification. Use `transaction_id` as the `ids` filter on `GET /v1/accounts/{account_id}/portfolio/transactions` to retrieve the complete ledger entry.

The same transaction can emit more than one event as its status changes. Deduplicate delivery retries with the `svix-id` header.

> [!NOTE]
>
> Failed swap and price trigger swap execution attempts do not emit `transaction.*` events because they do not contain
> ledger movements. Use the relevant quote or price trigger swap failure event instead.

See the [Register webhook API reference](https://docs.services.payward.com/api-reference/webhooks/register-webhook.md) to create a subscription and review the event payload schemas.

## Step 4: chart portfolio performance

Call `GET /v1/accounts/{account_id}/portfolio/history` to draw a portfolio value chart or show how balances changed over time.

```python Python theme={null}
def list_portfolio_history(account_id):
    params = [
        ("start_timestamp", "2026-04-01T00:00:00Z"),
        ("end_timestamp", "2026-04-30T23:59:59Z"),
        ("quote_symbol", "USD"),
        ("quote_type", "fiat"),
        ("assets[0][symbol]", "BTC"),
        ("assets[0][type]", "crypto"),
        ("assets[1][symbol]", "ETH"),
        ("assets[1][type]", "crypto"),
    ]
    path = f"/v1/accounts/{account_id}/portfolio/history?{urlencode(params)}"

    response = requests.get(
        BASE_URL + path, headers=signed_headers("GET", path), timeout=10
    )
    response.raise_for_status()
    return response.json()


history = list_portfolio_history("ABCD1234EFGH5678")
for point in history["data"]:
    print(point["timestamp"], point.get("value"))
```

```javascript JavaScript theme={null}
async function listPortfolioHistory(accountId) {
  const params = new URLSearchParams({
    start_timestamp: '2026-04-01T00:00:00Z',
    end_timestamp: '2026-04-30T23:59:59Z',
    quote_symbol: 'USD',
    quote_type: 'fiat',
    'assets[0][symbol]': 'BTC',
    'assets[0][type]': 'crypto',
    'assets[1][symbol]': 'ETH',
    'assets[1][type]': 'crypto',
  });
  const path = `/v1/accounts/${accountId}/portfolio/history?${params}`;

  const response = await fetch(BASE_URL + path, {
    method: 'GET',
    headers: signedHeaders('GET', path),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  return response.json();
}

const history = await listPortfolioHistory('ABCD1234EFGH5678');
for (const point of history.data) {
  console.log(point.timestamp, point.value);
}
```

Use the history endpoint for:

* Portfolio value charts with `timestamp` and `value`.
* Historical PnL views with `total_pnl`, when available.
* Historical asset-balance charts when you request `assets` filters with both `symbol` and `type`.
* Quote-aware charts with top-level `quote_symbol`, `quote_type`, `start_timestamp`, and `end_timestamp`.

The history endpoint returns a maximum of 365 data points per request. Use a narrower time window when you need fewer points.

> [!NOTE]
>
> A missing asset balance at the start of the range means the user did not hold that asset at that time. A zero balance
> means the user may have held the asset previously, but did not hold it at that snapshot. The latest daily balance can
> be delayed by up to about five hours after UTC midnight while data is processed.

See the [List Portfolio History API reference](https://docs.services.payward.com/api-reference/portfolio/list-portfolio-history.md) for all query parameters and response fields.

## API reference

| Method | Endpoint | Description |
| - | - | - |
| GET | [`/v1/accounts/{account_id}/portfolio`](https://docs.services.payward.com/api-reference/portfolio/get-portfolio) | Get account-level values and per-asset balances in one snapshot |
| GET | [`/v1/accounts/{account_id}/portfolio/transactions`](https://docs.services.payward.com/api-reference/portfolio/list-portfolio-transactions) | List portfolio transactions for deposits, withdrawals, transfers, swaps, and earn rewards |
| GET | [`/v1/accounts/{account_id}/portfolio/history`](https://docs.services.payward.com/api-reference/portfolio/list-portfolio-history) | List historical balances and valuations for a portfolio |
| POST | [`/v1/webhooks`](https://docs.services.payward.com/api-reference/webhooks/register-webhook) | Subscribe to Portfolio transaction change notifications |
