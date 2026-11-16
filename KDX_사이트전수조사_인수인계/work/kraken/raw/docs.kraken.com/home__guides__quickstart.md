---
url: https://docs.kraken.com/home/guides/quickstart
title: Quickstart - Kraken Developers
description: From Kraken account to your first programmatic trade in minutes
fetched: 2026-11-16
method: render
plan: read
---

## On this page

Back to top

* [Next steps](#next-steps)

Getting started

# Quickstart

Copy pageCopy page

From Kraken account to your first programmatic trade in minutes

Copy pageCopy page

This guide walks you through the complete setup from creating your API key to placing your first order programmatically.

1

Create a Kraken account

If you don’t have one, sign up at [kraken.com](https://www.kraken.com). You’ll need to complete identity verification before accessing trading APIs.

Spot trading requires a verified account. Futures trading requires additional activation — see your account settings.

2

Generate an API key

Go to [Settings → API](https://www.kraken.com/u/security/api) and click **Add key**.For this quickstart, enable these permissions:

* **Query Funds** — read balances
* **Query Open Orders & Trades** — read order status
* **Create & Modify Orders** — place orders

Copy your API key and private key. The private key is only shown once.

Store your private key securely. Never commit it to version control or share it. For production use, restrict the key to specific IP addresses.

3

Verify connectivity

Check that the API is reachable and your system clock is correct. The `Time` endpoint requires no authentication:

```
curl https://api.kraken.com/0/public/Time
```

Expected response:

```
{
  "error": [],
  "result": {
    "unixtime": 1700000000,
    "rfc1123": "Thu,  1 Jan 2026 00:00:00 +0000"
  }
}
```

Your system clock must be within a few seconds of real time. An incorrect clock is the most common cause of `EAPI:Invalid nonce` errors.

4

Check your balances

Your first authenticated request. The nonce must be a strictly increasing integer — using the current timestamp in milliseconds works well.

cURL

Python

```
API_KEY="your_api_key"
API_SECRET="your_private_key"
NONCE=$(date +%s%3N)
DATA="nonce=$NONCE"
API_PATH="/0/private/Balance"

SIGNATURE=$(echo -n "${NONCE}${DATA}" | \
  openssl dgst -sha256 -binary | \
  cat <(echo -n "$API_PATH") - | \
  openssl dgst -sha512 -binary -hmac "$(echo "$API_SECRET" | base64 -d)" | \
  base64)

curl -X POST "https://api.kraken.com${API_PATH}" \
  -H "API-Key: $API_KEY" \
  -H "API-Sign: $SIGNATURE" \
  -d "$DATA"
```

```
import time, base64, hashlib, hmac, urllib.parse, requests

api_key = "your_api_key"
api_secret = "your_private_key"

def kraken_request(url_path, data):
    nonce = str(int(time.time() * 1000))
    data["nonce"] = nonce
    postdata = urllib.parse.urlencode(data)
    encoded = (nonce + postdata).encode()
    message = url_path.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(api_secret), message, hashlib.sha512)
    sig = base64.b64encode(mac.digest()).decode()
    return requests.post(
        "https://api.kraken.com" + url_path,
        headers={"API-Key": api_key, "API-Sign": sig},
        data=data
    ).json()

print(kraken_request("/0/private/Balance", {}))
```

5

Test in a UAT environment

Both Spot and Futures provide UAT environments for validating your integration before going live.**Spot UAT** is available on request — contact your Account Manager. Once provisioned, it uses a separate base URL and isolated API keys but mirrors the full production trading stack.**Futures sandbox** is self-service at `https://demo-futures.kraken.com`. Generate a separate API key on the demo platform to get started immediately.

```
# Futures sandbox — get available instruments
curl https://demo-futures.kraken.com/derivatives/api/v3/instruments

# Place a limit order (buy 1 BTC perpetual at $90,000)
curl -X POST https://demo-futures.kraken.com/derivatives/api/v3/sendorder \
  -H "APIKey: your_sandbox_api_key" \
  -H "Authent: your_signature" \
  -d "orderType=lmt&symbol=PF_XBTUSD&side=buy&size=1&limitPrice=90000"
```

The Futures demo environment resets periodically. It is intended for integration validation, not persistent backtesting.

## Next steps

[## API key permissions

Understand which permissions to enable for each use case](/exchange/guides/rest/api-keys)

[## Authentication

Deep dive into nonce management and signature generation](/exchange/guides/rest/authentication)

[## Rate limits

Understand trading rate limits and how to stay within them](/exchange/guides/rest/ratelimits)

[## WebSocket

Switch to WebSocket for real-time order updates and market data](/exchange/guides/websockets/introduction)

[## Error reference

Common errors and how to fix them](/exchange/guides/general/errors)

[## API comparison

Choose between REST, WebSocket, and FIX for your use case](/exchange/guides/general/api-comparison)

Was this page helpful?

YesNo

[Welcome](/)[Support](/home/support)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/guides/quickstart#webpage","url":"https://docs.kraken.com/home/guides/quickstart","name":"Quickstart","description":"From Kraken account to your first programmatic trade in minutes","dateModified":"2026-06-11T06:04:03.240Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/guides/quickstart#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/guides/quickstart#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Getting started","item":"https://docs.kraken.com"},{"@type":"ListItem","position":2,"name":"Quickstart","item":"https://docs.kraken.com/home/guides/quickstart"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/guides/quickstart#article","headline":"Quickstart","name":"Quickstart","description":"From Kraken account to your first programmatic trade in minutes","url":"https://docs.kraken.com/home/guides/quickstart","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/guides/quickstart#webpage"},"dateModified":"2026-06-11T06:04:03.240Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```