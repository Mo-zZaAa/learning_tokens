> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ramp

> The Payward Ramp API lets you embed a fiat-to-crypto on-ramp into your application via a hosted checkout flow.

The Payward Ramp API lets you embed a fiat-to-crypto on-ramp into your application. Instead of building payment processing, KYC, and crypto delivery yourself, you call Ramp endpoints to discover what's available, preview pricing, and then generate a hosted checkout URL that handles the rest. Your user pays in fiat; Payward delivers crypto to the destination wallet.

> [!NOTE]
>
> **Not what you're looking for?** Ramp is designed for end-user fiat-to-crypto purchases via a hosted checkout flow. If
> you need to move funds between PWS accounts (Transfers), convert assets programmatically without a checkout UI
> (Conversions), or execute institutional FX-style trades (Swap), see the [PWS API reference](https://docs.services.payward.com/api-reference.md).

## How it works

A typical Ramp integration follows four steps:

**1. Discover**

Query supported countries, fiat currencies, payment methods, and cryptocurrency assets to know what options are
valid for your user's location.

**2. Preview**

Call the prospective quote endpoint to show the user an estimated pay/receive breakdown before they commit.

**3. Check limits**

Optionally verify that the user's intended amount falls within min/max bounds.

**4. Checkout**

Generate a hosted checkout URL and redirect the user to it. Payward handles payment processing and crypto delivery.

## Base URL

The `curl` examples read these environment variables:

* `PWS_BASE_URL`: the API base URL. Set it to the sandbox or production base URL, listed in
  [Environments](https://docs.services.payward.com/tabs/developer-documentation/testing/overview.md#environments).
* `PWS_API_KEY`: your API key.
* `PWS_API_TIMESTAMP` and `PWS_API_SIGN`: the timestamp and signature of each request. To compute them, see
  [Authentication](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md).
* Compute `PWS_API_SIGN` over the exact `-d` string, including its line breaks and indentation, and over the exact path
  and query in the URL. Each request needs a new `PWS_API_TIMESTAMP` and `PWS_API_SIGN`.

## Authentication

All requests require three headers:

| Header | Description |
| - | - |
| `API-Key` | Your public API key |
| `API-Timestamp` | Time you signed the request, in Unix milliseconds, included in the signature |
| `API-Sign` | HMAC signature computed with your API secret |

See [Authentication](https://docs.services.payward.com/tabs/developer-documentation/get-started/authentication.md) for how to generate the signature.

## Step 1: Discover supported options

Before building your UI, query the discovery endpoints to understand what's valid for your user's country. All four endpoints are read-only and can be called at startup or cached.

### List supported countries

```
GET /v1/ramp/countries
```

Returns countries where Ramp is available. Countries that require regional filtering include a `subdivisions` array. Use the returned `country` value and any relevant `subdivision` value as inputs to all other Ramp endpoints.

### List fiat currencies

```
GET /v1/ramp/fiat-currencies
```

Returns fiat currencies supported for funding Ramp transactions (e.g., `USD`, `EUR`). Pass the returned codes as `from_symbol` in later calls.

### List payment methods

```
GET /v1/ramp/payment-methods
```

Returns available payment methods (e.g., `credit_card`). Pass the returned identifiers as `from_method`.

### List cryptocurrency assets

```
GET /v1/ramp/buy/crypto
```

Returns cryptocurrency assets available for purchase, along with their supported networks and withdrawal methods. Both `to_symbol` and `to_method` values for later calls come from here.

All four discovery endpoints are cursor-paginated. Use `page_size` to set the first page size (default 50, maximum 200). If a response includes `next_page_token`, pass that value as `page_token` to fetch the next page. Page tokens are scoped to the original endpoint and country/subdivision where applicable, and the token's page size wins over a new `page_size` value.

Query parameters:

| Parameter | Required | Description |
| - | - | - |
| `country` | Yes | Required for fiat currencies, payment methods, and cryptocurrency assets |
| `subdivision` | No | ISO 3166-2 suffix from the countries response |
| `page_size` | No | First-page size, from 1 to 200. Defaults to 50 |
| `page_token` | No | Opaque token from `next_page_token` for the next page of the same result set |

```bash theme={null}
curl -X GET "$PWS_BASE_URL/v1/ramp/buy/crypto?country=US&subdivision=CA&page_size=200" \
  -H "API-Key: $PWS_API_KEY" \
  -H "API-Timestamp: $PWS_API_TIMESTAMP" \
  -H "API-Sign: $PWS_API_SIGN"
```

## Step 2: Preview pricing

Before sending your user to checkout, call the prospective quote endpoint to display an estimated cost breakdown. This call does **not** reserve liquidity: it's safe to call on every keystroke for a live price preview.

```
GET /v1/ramp/quotes/prospective
```

The `from_*` parameters describe the side the user pays with and the `to_*` parameters the side they receive: the same source/destination model the Conversions and Swap APIs use.

Required parameters:

| Parameter | Description |
| - | - |
| `from_symbol` | Fiat currency ticker (e.g., `USD`) |
| `from_method` | Payment method (e.g., `credit_card`) |
| `from_amount` | Amount the user intends to spend |
| `to_symbol` | Cryptocurrency asset ticker to receive (e.g., `BTC`) |
| `to_method` | Withdrawal method (e.g., `Bitcoin`) |
| `country` | User's country code |

Optional parameters:

| Parameter | Description |
| - | - |
| `from_type` | Asset classification (`fiat`, `crypto`, `stablecoin`, `xstock`) |
| `to_type` | Asset classification for the destination side |
| `subdivision` | US state / CA province code |
| `affiliate_fee_bps` | Your affiliate fee in basis points (e.g., `250` = 2.5%) |

The response includes a `from` object (the side the user pays, fiat) and a `to` object (the side they receive, crypto), each with a full fee breakdown. Asset references use the `{ symbol, type, name }` shape:

```json theme={null}
{
  "data": {
    "from": {
      "asset": { "symbol": "USD", "type": "fiat", "name": "US Dollar" },
      "total": "1015.00",
      "subtotal": "1000.00",
      "fee": "10.00",
      "deposit_fee": "5.00",
      "affiliate_fee": "2.50",
      "withdrawal_fee": null
    },
    "to": {
      "asset": { "symbol": "BTC", "type": "crypto", "name": "Bitcoin" },
      "total": "0.01587302",
      "subtotal": "0.01587302",
      "fee": null,
      "deposit_fee": null,
      "affiliate_fee": null,
      "withdrawal_fee": "0.00010000"
    },
    "unit_price": {
      "asset": { "symbol": "BTC", "type": "crypto", "name": "Bitcoin" },
      "denomination_asset": { "symbol": "USD", "type": "fiat", "name": "US Dollar" },
      "unit_price": "63000.00"
    }
  }
}
```

> [!NOTE]
>
> **Affiliate fee note:** `affiliate_fee_bps` increases the fee charged to the user. In responses, `affiliate_fee`
> represents your portion of the returned `fee` amount, so do not add it again in your UI.

## Step 3: Check transaction limits (optional)

```
GET /v1/ramp/limits
```

Returns the minimum and maximum transaction amounts for a given configuration. Call this to validate user input before generating a checkout URL or to display limit guidance in your UI. Uses the same required parameters as the prospective quote endpoint.

## Step 4: Generate a checkout URL

Once you have confirmed options and the user is ready to proceed, generate a hosted checkout URL. Redirect your user to this URL: Payward handles the payment form, KYC checks, and crypto delivery.

```
GET /v1/ramp/checkout
```

Required parameters:

| Parameter | Description |
| - | - |
| `from_symbol` | Fiat currency ticker (e.g., `USD`) |
| `from_method` | Payment method |
| `from_amount` | Amount to charge |
| `to_symbol` | Cryptocurrency asset ticker to deliver |
| `to_method` | Withdrawal method |
| `country` | User's country code |

Useful optional parameters:

| Parameter | Description |
| - | - |
| `from_type` | Asset classification for the funding side |
| `to_type` | Asset classification for the destination side |
| `to_address` | Pre-fill the destination wallet address |
| `to_network` | Specify the withdrawal network |
| `to_memo` | Memo/tag for assets that require it (e.g., XRP) |
| `redirect_url` | Where to send the user after a successful purchase |
| `failure_url` | Where to send the user after a failed purchase |
| `affiliate_fee_bps` | Your affiliate fee in basis points |
| `external_user_id` | Your internal user ID (stored for reconciliation) |
| `external_partner_id` | Your partner identifier for multi-tenant reconciliation |
| `external_transaction_id` | Your internal transaction ID |
| `external_metadata` | Arbitrary metadata (max 1000 chars) |

The response contains the checkout URL and an echo of the submitted parameters for client-side confirmation, grouped into `from` and `to` side objects:

```json theme={null}
{
  "data": {
    "checkout_url": "https://ramp.example.com/checkout/abc123def456",
    "request_data": {
      "from": {
        "symbol": "USD",
        "type": "fiat",
        "method": "credit_card",
        "amount": "1000.00"
      },
      "to": {
        "symbol": "BTC",
        "type": "crypto",
        "method": "Bitcoin",
        "network": "Bitcoin",
        "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
        "memo": null
      },
      "affiliate_fee_bps": "250",
      "country": "GB",
      "subdivision": null,
      "redirect_url": "https://example.com/checkout/success",
      "failure_url": "https://example.com/checkout/failure",
      "external_user_id": "user_01J0M7C0Z9F8YX3GQH8E",
      "external_partner_id": null,
      "external_transaction_id": "INV-2026-04-0042",
      "external_metadata": "{\"order_id\":\"order_12345\"}"
    }
  }
}
```

Redirect the user to `checkout_url`. The hosted page collects card details, performs any required identity verification, and delivers the crypto.

## Receiving transaction updates

Payward pushes real-time transaction status updates to a webhook endpoint **you implement**. Register your endpoint via the [Webhooks API](https://docs.services.payward.com/api-reference/webhooks/register-webhook.md), then handle POST callbacks at your URL.

Each callback payload includes the transaction status and, when complete, the delivered amount and destination address. The `external_transaction_id` and `external_user_id` you passed at checkout are echoed back, making reconciliation straightforward.

## API reference

### API calls

| Method | Endpoint | Description |
| - | - | - |
| GET | [`/v1/ramp/countries`](https://docs.services.payward.com/api-reference/ramp/list-ramp-countries) | List supported countries and subdivisions |
| GET | [`/v1/ramp/fiat-currencies`](https://docs.services.payward.com/api-reference/ramp/list-ramp-fiat-currencies) | List supported fiat currencies |
| GET | [`/v1/ramp/payment-methods`](https://docs.services.payward.com/api-reference/ramp/list-ramp-payment-methods) | List supported payment methods |
| GET | [`/v1/ramp/buy/crypto`](https://docs.services.payward.com/api-reference/ramp/list-ramp-buy-cryptocurrency-assets) | List cryptocurrency assets available for purchase |
| GET | [`/v1/ramp/limits`](https://docs.services.payward.com/api-reference/ramp/get-ramp-limits) | Get min/max transaction limits |
| GET | [`/v1/ramp/quotes/prospective`](https://docs.services.payward.com/api-reference/ramp/get-ramp-prospective-quote) | Preview from/to amounts without reserving liquidity |
| GET | [`/v1/ramp/checkout`](https://docs.services.payward.com/api-reference/ramp/get-ramp-checkout-url) | Generate a hosted checkout URL |

### Webhook callbacks

Payward sends these requests to the webhook endpoint you implement.

| Method | Endpoint | Description |
| - | - | - |
| POST | [`{your_webhook_url}`](#receiving-transaction-updates) | Receive real-time transaction status updates |
