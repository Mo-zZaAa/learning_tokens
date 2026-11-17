> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# On-chain swaps

> The on-chain swaps API lets you create a wallet-funded xStocks quote, submit the returned payload on-chain, and poll until the quote reaches a terminal state.

## Prerequisites

* Payward Services API credentials (see the [Authentication guide](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md)).
* A verified user with at least one account and on-chain quote trading enabled.
* A source wallet registered on the user's withdrawal-address list as a same-owner address. The address must be approved before you create a quote.
* Enough source-asset balance in the wallet to settle the on-chain quote.

## Workflow

**1. Create an on-chain quote**

Create a wallet-funded xStocks on-chain quote and receive the on-chain payload.

`POST /v1/accounts/{account_id}/onchain-quotes`

**2. Submit the on-chain transaction**

Call the Payward on-chain proxy contract with the returned payload before `expires_at`.

`executeSwap(...)`

**3. Poll for terminal status**

Wait for Payward Services to observe settlement, or subscribe to webhooks.

`GET /v1/accounts/{account_id}/onchain-quotes/{quote_id}`

## Quote lifecycle

| Status | Description |
| - | - |
| `pending` | Quote is being prepared. Transitions to `offered` once the signed payload is ready, or to `failed` if preparation fails. |
| `offered` | Quote created and locked. Valid until `expires_at`. |
| `executing` | The on-chain transaction was observed and is awaiting confirmation. |
| `executed` | Terminal. The on-chain quote completed. |
| `expired` | Terminal. `expires_at` elapsed before settlement. |
| `failed` | Terminal. The on-chain transaction reverted, or the offer could not be completed. |

## Specifying the trade

Onchain quotes are restricted to xStock and USDC pairs. Set the `wallet` block on `from`: the quote is funded from the user's wallet, not from the user's Payward Services account balance.

| Field | Required | Description |
| - | - | - |
| `from.wallet` | yes | `{ address, network }`. Must be an approved same-owner withdrawal address. |
| `from.symbol` | yes | Source asset symbol. Use `USDC` when buying xStocks, or the xStock when selling. |
| `from.type` | yes | `stablecoin` or `xstock`. |
| `to.symbol` | yes | Destination asset symbol. |
| `to.type` | yes | `stablecoin` or `xstock`. |
| `from.amount` or `to.amount` | one of | Set exactly one. The server calculates the other side. |

The only supported `network` value is `ethereum`.

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

## Step 1: create an on-chain quote

Send a `POST` to `/v1/accounts/{account_id}/onchain-quotes` with `from.wallet` populated. The create response returns the full quote including `execution_details`, which carries the proxy contract address and the signed on-chain payload.

> [!WARNING]
>
> Store `execution_details` from the create response. `GET /v1/accounts/{account_id}/onchain-quotes/{quote_id}` returns
> quote status and amounts, but it does not return a fresh on-chain execution payload.

## Step 2: submit the on-chain transaction

Call `executeSwap` on `execution_details.proxy_address`. Pass the returned `proxy_swap_message` before the quote expires.

The proxy call uses this argument shape:

```typescript Typescript theme={null}
const proxyAbi = [
  {
    type: 'function',
    name: 'executeSwap',
    stateMutability: 'nonpayable',
    outputs: [],
    inputs: [
      {
        name: 'proxySwapMessage',
        type: 'tuple',
        components: [
          {
            name: 'atomicMessage',
            type: 'tuple',
            components: [
              { name: 'quoteId', type: 'bytes32' },
              { name: 'expiration', type: 'uint256' },
              {
                name: 'incomingTransfer',
                type: 'tuple',
                components: [
                  { name: 'from', type: 'address' },
                  { name: 'to', type: 'address' },
                  { name: 'token', type: 'address' },
                  { name: 'amount', type: 'uint256' },
                ],
              },
              {
                name: 'outgoingTransfer',
                type: 'tuple',
                components: [
                  { name: 'from', type: 'address' },
                  { name: 'to', type: 'address' },
                  { name: 'token', type: 'address' },
                  { name: 'amount', type: 'uint256' },
                ],
              },
            ],
          },
          { name: 'atomicSignature', type: 'bytes' },
          {
            name: 'inputTokenPermit',
            type: 'tuple',
            components: [
              { name: 'token', type: 'address' },
              { name: 'value', type: 'uint256' },
              { name: 'v', type: 'uint8' },
              { name: 'r', type: 'bytes32' },
              { name: 's', type: 'bytes32' },
            ],
          },
          { name: 'signature', type: 'bytes' },
        ],
      },
    ],
  },
] as const;

const zeroPermit = {
  token: '0x0000000000000000000000000000000000000000',
  value: 0n,
  v: 0,
  r: '0x0000000000000000000000000000000000000000000000000000000000000000',
  s: '0x0000000000000000000000000000000000000000000000000000000000000000',
};

function tokenTransfer(transfer) {
  return {
    from: transfer.from,
    to: transfer.to,
    token: transfer.token,
    amount: BigInt(transfer.amount),
  };
}

const execution = quote.data.execution_details;
const message = execution.proxy_swap_message;
const atomic = message.atomic_message;

const proxyMessage = {
  atomicMessage: {
    quoteId: atomic.quote_id,
    expiration: BigInt(atomic.expiration),
    incomingTransfer: tokenTransfer(atomic.incoming_transfer),
    outgoingTransfer: tokenTransfer(atomic.outgoing_transfer),
  },
  atomicSignature: message.atomic_signature,
  inputTokenPermit: message.input_token_permit ?? zeroPermit,
  signature: message.signature,
};

await walletClient.writeContract({
  address: execution.proxy_address,
  abi: proxyAbi,
  functionName: 'executeSwap',
  args: [proxyMessage],
});
```

If you do not pass an input-token permit, approve the proxy to spend the source token from the user's wallet before you broadcast the transaction.

> [!WARNING]
>
> Onchain quote settlement happens on-chain. There is no server-side execute endpoint: the proxy contract call is the
> only way to fulfill an on-chain quote offer.

## Step 3: poll for terminal status

After broadcasting on-chain, poll `GET /v1/accounts/{account_id}/onchain-quotes/{quote_id}` until `status` reaches a terminal value (`executed`, `expired`, or `failed`).

> [!TIP]
>
> Subscribe to the `quote.executed` and `quote.execution_failed` webhooks if you do not want to poll.

## Reviewing on-chain quotes

List previously created on-chain quotes with `GET /v1/accounts/{account_id}/onchain-quotes`. Results are returned newest-first. Use `page_token` and `page_size` (defaults to 50, max 200) for pagination: `next_page_token` is omitted on the final page.

> [!NOTE]
>
> History entries omit `execution_details`. The signed on-chain payload is only returned by the create response.

## Error handling

| HTTP status | Code | Cause | Remediation |
| - | - | - | - |
| `400 Bad Request` | validation error | `from.wallet.address` is not an approved same-owner address. | Have the user add the wallet in the Payward UI and wait for approval. |
| `400 Bad Request` | validation error | Both or neither of `from.amount` / `to.amount` were set. | Set exactly one side of the trade. |
| `400 Bad Request` | validation error | `from`/`to` pair is not an xStock/USDC trade. | Restrict trades to xStock ↔ stablecoin pairs. |
| `403 Forbidden` | forbidden | The user is not eligible for on-chain quote trading. | Confirm the user's eligibility with your account manager. |
| `410 Gone` | `quote_expired` | `expires_at` elapsed before settlement. | Request a new quote, review its amounts, then submit the new `execution_details.proxy_swap_message` before `expires_at`. |
| `503 Service Unavailable` | `insufficient_liquidity` | No liquidity is available at the requested size. | Retry with a smaller size. If it persists, contact support. |

## Best practices

1. Register wallets ahead of time. Screening can take time and will block quote creation until the address is approved.
2. Store the on-chain quote create response. It is the only response that includes the signed on-chain execution payload.
3. Treat `executed`, `expired`, and `failed` as terminal. Request a new quote for another attempt.
4. Submit on-chain well before `expires_at`. Gas spikes and confirmation time reduce the usable window.
5. Capture `Request-Id` from response headers. It speeds up support investigations.

## API reference

| Method | Endpoint | Description |
| - | - | - |
| POST | [`/v1/accounts/{account_id}/onchain-quotes`](https://docs.services.payward.com/api-reference/on-chain-swaps/create-on-chain-quote) | Create a wallet-funded on-chain quote. Returns the quote with `execution_details`. |
| GET | [`/v1/accounts/{account_id}/onchain-quotes`](https://docs.services.payward.com/api-reference/on-chain-swaps/list-on-chain-quotes) | List on-chain quotes for the authenticated user (paginated, newest first). |
| GET | [`/v1/accounts/{account_id}/onchain-quotes/{quote_id}`](https://docs.services.payward.com/api-reference/on-chain-swaps/get-on-chain-quote) | Read on-chain quote status and amounts. Does not return a new execution payload. |
