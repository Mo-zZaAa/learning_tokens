# 읽기 묶음: docs.kraken.com / home (1/1)


<<<PAGE https://docs.kraken.com/home/cli>>>
---
url: https://docs.kraken.com/home/cli
title: kraken-cli - Kraken Developers
description: One-install CLI for Spot and Derivatives trading — scripting, automation, paper trading, and AI agent workflows!
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Install](#install)
* [What it covers](#what-it-covers)
  + [Command groups](#command-groups)
* [Paper trading](#paper-trading)
* [Sessions and recipes](#sessions-and-recipes)
* [Scripting and automation](#scripting-and-automation)
* [Account management](#account-management)
* [Dead man’s switch](#dead-man%E2%80%99s-switch)
* [Authentication](#authentication)
* [Interactive shell](#interactive-shell)
* [AI agent integration](#ai-agent-integration)

Tools

# kraken-cli

Copy pageCopy page

One-install CLI for Spot and Derivatives trading — scripting, automation, paper trading, and AI agent workflows!

Copy pageCopy page

kraken-cli is a compiled CLI for trading and account management across the Kraken exchange. No runtime dependencies. One install covers Spot, Derivatives, xStocks, Forex, Earn, and Subaccounts, and puts three binaries on your PATH:

* `kraken` — the CLI
* `kraken-mcp` — the [MCP server](/home/mcp) for AI agents
* `kraken-shell` — an interactive shell

## GitHub

Source, releases, and changelog

## MCP server

Give AI agents 152 MCP tools from the CLI

## Install

```
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/krakenfx/kraken-cli/releases/latest/download/kraken-cli-installer.sh | sh
```

Supported on macOS (Apple Silicon and Intel) and Linux (x86\_64 and ARM64). On Windows, use WSL. Every release artifact is signed with minisign; see [Verifying binaries](https://github.com/krakenfx/kraken-cli#verifying-binaries).
The installer puts the binaries in `~/.cargo/bin` (or `$CARGO_HOME/bin` if you set it) and adds that folder to your PATH for new terminals only. Open a new terminal window, or run `source "$HOME/.cargo/env"`. If an AI agent or editor was already running, quit it and start it again from a new terminal.
Verify the install:

```
kraken status && kraken ticker BTC/USD
```

## What it covers

188 commands across 15 groups. Six asset classes in one install:

| Asset class | Examples | Notes |
| --- | --- | --- |
| Crypto spot | BTC, ETH, SOL (1,400+ pairs) | Default engine |
| xStocks (tokenized equities) | AAPL, TSLA, SPY (79 assets) | `--asset-class tokenized_asset` |
| Forex | EUR/USD, GBP/USD (11 pairs) | `--asset-class forex` |
| Perpetual futures | 317 contracts | Futures engine |
| Inverse and fixed-date futures | BTC, ETH, SOL (20 contracts) | Futures engine |
| Earn / staking | Flexible and bonded strategies | `kraken earn` |

Spot is the default: `kraken order buy`, `kraken balance`. Futures commands are explicit: `kraken futures order buy`.

### Command groups

| Group | Commands | Auth required |
| --- | --- | --- |
| market | 11 | No |
| account | 18 | Yes |
| trade | 9 | Yes |
| funding | 10 | Yes |
| earn | 6 | Yes |
| subaccount | 2 | Yes |
| futures | 39 | Mixed |
| futures-paper | 17 | No |
| futures-ws | 9 | Mixed |
| websocket | 17 | Mixed |
| paper | 17 | No |
| workspace | 25 | No |
| feedback | 1 | No |
| auth | 6 | Mixed |
| utility | 1 | No |

The [command catalog](https://github.com/krakenfx/kraken-cli/blob/main/agents/tool-catalog.json) lists every command with its arguments. It is generated from the code, so it always matches the release.

## Paper trading

The CLI’s built-in paper trading engine runs against live prices with no authentication required. It is the recommended way to test strategies and integrations.

```
# Spot paper trading in an isolated workspace
kraken workspace create sandbox --capital 10000 --mode paper
export KRAKEN_WORKSPACE=sandbox
kraken paper buy BTC/USD 0.001 --type limit --price 50000
kraken paper status

# Futures paper trading is not workspace-scoped yet: run it without KRAKEN_WORKSPACE
unset KRAKEN_WORKSPACE
kraken futures paper init --balance 10000
kraken futures paper buy PF_XBTUSD 1 --leverage 10 --type limit --price 50000
kraken futures paper positions
```

To trade live, replace `kraken paper buy` with `kraken order buy` and provide credentials. Pass `--type` when you switch: `paper buy` defaults to a market order and `order buy` to a limit order.
When a paper workspace has the evidence, `kraken workspace promote` checks the promotion checklist and switches the workspace to live execution on the real account. It is a dangerous command: it needs credentials and asks for confirmation.

## Sessions and recipes

Record a session in a paper workspace, explain its P&L, then package it so it can run again:

```
export KRAKEN_WORKSPACE=sandbox
kraken session start --symbols BTC/USD --channels trades --for 15m
kraken explain pnl --session latest
kraken recipe create btc-levels --from-session latest
kraken recipe run btc-levels --for 15m
```

## Scripting and automation

Every command supports `-o json`. Exit code 0 means success, 1 a runtime failure (with a JSON error envelope on stdout), and 2 a usage error. This makes the CLI composable in shell scripts and CI pipelines:

```
# Cancel all open orders (--yes answers the confirmation a script cannot)
kraken order cancel-all --yes

# Stream the live order book to a file
kraken ws book BTC/USD -o json >> book.jsonl

# Fetch balances as JSON, filter with jq
kraken balance -o json | jq 'keys'
```

Stdout always produces valid JSON on success or an error envelope on failure. Stderr carries diagnostics only. Never parse stderr for data.

## Account management

```
kraken balance
kraken open-orders -o json
kraken trades-history
```

## Dead man’s switch

Cancel all open orders if your process stops sending heartbeats:

```
kraken order cancel-after 60
```

## Authentication

Sign in once in the browser:

```
kraken auth login
```

It saves a restricted Spot API key with no withdrawal rights and an expiry date: 90 days, or less with `--valid-for`. `--read-only` creates a key that cannot trade. It needs a terminal, so run it yourself; a script or an AI agent cannot create a key.
To use a key you created yourself, generate it at [Settings → API](https://www.kraken.com/u/security/api) for Spot, or in the Futures interface for Derivatives, and store it with the setup wizard. Run it in a normal terminal, because it reads your input:

```
kraken setup
```

Credentials are resolved in this order:

1. Command-line flags (`--api-key`, `--api-secret`)
2. Environment variables (`KRAKEN_API_KEY`, `KRAKEN_API_SECRET`, and `KRAKEN_FUTURES_API_KEY`, `KRAKEN_FUTURES_API_SECRET` for futures)
3. The active stored key in `config.toml` (`~/.config/kraken/` on Linux, `~/Library/Application Support/kraken/` on macOS): the API key from `kraken setup` or `kraken auth set`, or the sign-in key from `kraken auth login`

`kraken auth show` tells you which stored key is active, and `kraken auth switch api-key` or `kraken auth switch sign-in` changes it. Grant only the permissions your workflow needs. Never paste API keys into an AI chat.

## Interactive shell

For exploratory sessions:

```
kraken-shell
```

## AI agent integration

The CLI is designed for machine consumption: structured JSON output, stable error categories, and predictable exit codes. See the [MCP server](/home/mcp) page to give LLM agents the CLI’s request/response commands as tools.
Agent resources shipped with the CLI:

| Resource | Purpose |
| --- | --- |
| [AGENTS.md](https://github.com/krakenfx/kraken-cli/blob/main/AGENTS.md) | Full agent integration guide |
| [CONTEXT.md](https://github.com/krakenfx/kraken-cli/blob/main/CONTEXT.md) | Runtime context for tool-using agents |
| [agents/tool-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/tool-catalog.json) | 188 commands with parameter schemas |
| [agents/error-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/error-catalog.json) | 10 error categories with retry guidance |
| [skills/](https://github.com/krakenfx/kraken-cli/tree/main/skills) | 59 goal-oriented workflow packages |
| [CLAUDE.md](https://github.com/krakenfx/kraken-cli/blob/main/CLAUDE.md) | Claude-specific guidance |

Was this page helpful?

YesNo

[Support](/home/support)[MCP Server](/home/mcp)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/cli#webpage","url":"https://docs.kraken.com/home/cli","name":"kraken-cli","description":"One-install CLI for Spot and Derivatives trading — scripting, automation, paper trading, and AI agent workflows!","dateModified":"2026-11-13T08:49:41.235Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/cli#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/cli#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken Developers","item":"https://docs.kraken.com"},{"@type":"ListItem","position":2,"name":"kraken-cli","item":"https://docs.kraken.com/home/cli"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/cli#article","headline":"kraken-cli","name":"kraken-cli","description":"One-install CLI for Spot and Derivatives trading — scripting, automation, paper trading, and AI agent workflows!","url":"https://docs.kraken.com/home/cli","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/cli#webpage"},"dateModified":"2026-11-13T08:49:41.235Z","keywords":"CLI, command line, kraken-cli, paper trading, scripting, automation, Rust","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```

<<<PAGE https://docs.kraken.com/home/guides/quickstart>>>
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

<<<PAGE https://docs.kraken.com/home/mcp>>>
---
url: https://docs.kraken.com/home/mcp
title: MCP server - Kraken Developers
description: Give AI agents Kraken CLI commands as tools through the kraken-mcp Model Context Protocol server
fetched: 2026-11-16
method: render
plan: read
---

## On this page

Back to top

* [Quickstart](#quickstart)
* [Client setup](#client-setup)
* [Services](#services)
  + [Dangerous tools](#dangerous-tools)
* [Authentication](#authentication)
* [What agents can do](#what-agents-can-do)
* [Safety notes](#safety-notes)
* [Agent resources](#agent-resources)

Tools

# MCP server

Copy pageCopy page

Give AI agents Kraken CLI commands as tools through the kraken-mcp Model Context Protocol server

Copy pageCopy page

kraken-cli ships a [Model Context Protocol](https://modelcontextprotocol.io) server, `kraken-mcp`, over stdio. It serves 152 of the CLI’s commands as MCP tools that any MCP-compatible AI agent can call — Claude, Cursor, GitHub Copilot, Windsurf, and others.
Streams (WebSocket feeds, recording, replay, session start), interactive commands, and the local credential commands `auth switch` and `auth reset` stay CLI-only. A tool call is one request and one response; a stream never returns. Run streams with the CLI, for example `kraken record`, and read the results back with tools such as `kraken_tape_list` and `kraken_explain_pnl`, or `kraken_session_show` with the `workspace` service.
`kraken-mcp` comes with the CLI install. [Install the CLI](/home/cli) first.

## Quickstart

```
kraken-mcp -s market,paper,feedback
```

This starts the server with market data, paper trading, and the feedback tool, which uploads the text you give it to Kraken. No credentials are required, and no tool can trade live or move funds.

## Client setup

* Claude Code
* Claude Desktop
* Cursor
* VS Code (Copilot)
* Windsurf

Install the plugin, which adds the MCP server and the CLI’s agent skills:

```
/plugin marketplace add krakenfx/kraken-cli
/plugin install kraken-cli@kraken
```

Or register only the MCP server for your user:

```
claude mcp add --scope user kraken -- kraken-mcp -s market,paper,feedback
```

The plugin asks for no API key. To add live trading, use `-s market,paper,trade` with a least-privilege API key (see [Authentication](#authentication)).Verify it is registered:

```
claude mcp list
```

If it shows “Failed to connect”, Claude Code cannot find `kraken-mcp` on its PATH. Quit Claude Code and start it again from a new terminal window, or register the full path, which works before `kraken-mcp` is on your PATH:

```
claude mcp add --scope user kraken -- "$HOME/.cargo/bin/kraken-mcp" -s market,paper,feedback
```

If you set `CARGO_HOME`, use `$CARGO_HOME/bin/kraken-mcp` instead.

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```
{
  "mcpServers": {
    "kraken": {
      "command": "kraken-mcp",
      "args": ["-s", "market,paper,feedback"]
    }
  }
}
```

Restart Claude Desktop to pick up the change.

Create or edit `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` in your project:

```
{
  "mcpServers": {
    "kraken": {
      "command": "kraken-mcp",
      "args": ["-s", "market,paper,feedback"]
    }
  }
}
```

Reload the Cursor window after saving.

Create or edit `.vscode/mcp.json` in your workspace:

```
{
  "servers": {
    "kraken": {
      "type": "stdio",
      "command": "kraken-mcp",
      "args": ["-s", "market,paper,feedback"]
    }
  }
}
```

Edit `~/.codeium/windsurf/mcp_config.json`:

```
{
  "mcpServers": {
    "kraken": {
      "command": "kraken-mcp",
      "args": ["-s", "market,paper,feedback"]
    }
  }
}
```

Restart Windsurf to apply.

Other MCP clients take the same command and arguments: `kraken-mcp -s market,paper,feedback`. Gemini CLI users can install the extension instead: `gemini extensions install https://github.com/krakenfx/kraken-cli`.
If a client reports “Failed to connect” or cannot start the server, set `command` to the full path that `command -v kraken-mcp` prints. Desktop apps often do not see the PATH your terminal uses.

## Services

Pass `-s <services>` to control which command groups are exposed. Multiple services are comma-separated.

| Service | Tools | Auth | Risk level | What it exposes |
| --- | --- | --- | --- | --- |
| `market` | 11 | No | None | Ticker, orderbook, trades, OHLC, spreads, asset info, tape library |
| `account` | 18 | Yes | Read-only, except `export-retrieve` and `export-delete` (dangerous) | Balances, orders, trade history, ledgers, positions, exports |
| `paper` | 17 | No | Simulation; `reset` is dangerous | Spot paper trading with live prices, P&L explanation, research lab |
| `workspace` | 20 | No | `reset` and `promote` are dangerous; live workspaces reach the real account | Paper and live workspaces, sessions, recipes, reports, extensions |
| `futures-paper` | 17 | No | None (simulation) | Futures paper trading |
| `feedback` | 1 | No | Uploads text to Kraken | Product feedback upload to Kraken |
| `trade` | 9 | Yes | Dangerous | Place, amend, and cancel live Spot orders |
| `futures` | 39 | Mixed | Dangerous | Futures market data and order entry |
| `earn` | 6 | Yes | Dangerous | Staking allocations and deallocations |
| `funding` | 10 | Yes | Dangerous | Deposits, withdrawals, and transfers |
| `subaccount` | 2 | Yes | Dangerous | Subaccount creation and transfers |
| `auth` | 2 | Mixed | Read-only | Credential status and validation |
| `all` | 152 | Mixed | Mixed | All of the above |

**Default** (no `-s` flag): `market`, `account`, `paper`, `workspace`, `feedback`.

### Dangerous tools

Tools marked dangerous (order placement, withdrawals, transfers, workspace promotion) need your approval for every call. The server asks you through MCP elicitation and runs the call only if you approve. A client that cannot show an elicitation gets no prompt from the server: the call runs when the model sets `acknowledged: true` in its arguments, so on such a client rely on the client’s own tool-approval prompt. Start the server with `--allow-dangerous` to turn the gate off.

```
# Ask for approval on every dangerous call
kraken-mcp -s all

# Turn the approval gate off (use in trusted, controlled environments only)
kraken-mcp -s all --allow-dangerous
```

## Authentication

Set credentials as environment variables in the client’s MCP configuration, or in the shell that starts the server:

```
export KRAKEN_API_KEY="your-key"
export KRAKEN_API_SECRET="your-secret"
kraken-mcp -s market,account,trade
```

Or store a key once in a terminal, with `kraken auth login` (browser sign-in, a restricted key with no withdrawal rights) or `kraken setup` (a key you created). The server reads the same active stored key as the CLI. `kraken-mcp` takes no `--api-key` or `--api-secret` flags.

## What agents can do

With `market`, `paper`, and `feedback`, an agent can:

* Query live prices, orderbooks, and recent trades for any pair
* Place and cancel paper trades against live prices
* List recorded tapes and explain a stopped session’s P&L

With `account`, it can read balances and open orders. With `trade` added, it can place, amend, and cancel live orders. With `funding`, it can initiate withdrawals. Scope services to the minimum your workflow requires.

## Safety notes

* The MCP server runs locally over stdio and is not exposed as a network service
* Use minimum-permission API keys scoped to what the agent actually needs
* The default service set places no live orders and moves no funds; its few dangerous tools (workspace promotion and reset, paper reset, export retrieval and deletion) still need approval, and so does creating a live workspace
* Treat agent sessions with live trading scope the same as a logged-in user session
* Set position size limits and pair allowlists at the API key level on Kraken’s settings page

## Agent resources

The CLI ships supplementary resources for agent integration:

| Resource | Purpose |
| --- | --- |
| [AGENTS.md](https://github.com/krakenfx/kraken-cli/blob/main/AGENTS.md) | Full integration guide with patterns and constraints |
| [CONTEXT.md](https://github.com/krakenfx/kraken-cli/blob/main/CONTEXT.md) | Runtime context injected at session start |
| [agents/tool-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/tool-catalog.json) | All 188 commands with parameter schemas; the `reach` field marks the 152 MCP tools |
| [agents/error-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/error-catalog.json) | 10 error categories with retry guidance |
| [skills/](https://github.com/krakenfx/kraken-cli/tree/main/skills) | 59 pre-built workflow packages for common trading tasks |
| [CLAUDE.md](https://github.com/krakenfx/kraken-cli/blob/main/CLAUDE.md) | Claude-specific guidance for the CLI |

Was this page helpful?

YesNo

[CLI](/home/cli)[Overview](/home/sdks)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 펼치거나 눌러야 보이던 내용

- Edit ~/Library/Application Support/Claude/claude_desktop_config.json:
- Create or edit ~/.cursor/mcp.json (global) or .cursor/mcp.json in your project:
- Create or edit .vscode/mcp.json in your workspace:
- Edit ~/.codeium/windsurf/mcp_config.json:

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/mcp#webpage","url":"https://docs.kraken.com/home/mcp","name":"MCP server","description":"Give AI agents Kraken CLI commands as tools through the kraken-mcp Model Context Protocol server","dateModified":"2026-11-12T15:11:30.314Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/mcp#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/mcp#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"MCP server","item":"https://docs.kraken.com/home/mcp"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/mcp#article","headline":"MCP server","name":"MCP server","description":"Give AI agents Kraken CLI commands as tools through the kraken-mcp Model Context Protocol server","url":"https://docs.kraken.com/home/mcp","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/mcp#webpage"},"dateModified":"2026-11-12T15:11:30.314Z","keywords":"MCP, Model Context Protocol, AI agent, Claude, Cursor, Copilot, Windsurf, tool use, kraken-mcp","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```

<<<PAGE https://docs.kraken.com/home/sdks/go>>>
---
url: https://docs.kraken.com/home/sdks/go
title: Go - Kraken Developers
description: api-go — the official Go module for the Spot and Derivatives APIs
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Install](#install)
* [What it covers](#what-it-covers)
* [Example](#example)

SDKs

# Go

Copy pageCopy page

api-go — the official Go module for the Spot and Derivatives APIs

Copy pageCopy page

[api-go](https://github.com/krakenfx/api-go) is the official Go module for building integrations against the Spot and Derivatives APIs.

## Install

```
go get github.com/krakenfx/api-go/v2/...
```

## What it covers

* Spot and Derivatives REST (public and authenticated endpoints)
* Spot and Derivatives WebSocket (public data streams and private channels)
* Order operations: add, amend, cancel
* Real-time order book construction with CRC32 checksum validation
* Instrument and asset lookups, account data retrieval

## Example

```
client := krakenapi.New(apiKey, apiSecret)
resp, err := client.AddOrder(krakenapi.AddOrderOptions{
    Pair:      "XBTUSD",
    Type:      "buy",
    OrderType: "limit",
    Price:     "60000",
    Volume:    "0.01",
})
```

Was this page helpful?

YesNo

[Overview](/home/sdks)[Rust](/home/sdks/rust)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/sdks/go#webpage","url":"https://docs.kraken.com/home/sdks/go","name":"Go","description":"api-go — the official Go module for the Spot and Derivatives APIs","dateModified":"2026-09-08T06:34:18.012Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/sdks/go#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/sdks/go#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"SDKs","item":"https://docs.kraken.com/home/sdks"},{"@type":"ListItem","position":3,"name":"Go","item":"https://docs.kraken.com/home/sdks/go"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/sdks/go#article","headline":"Go","name":"Go","description":"api-go — the official Go module for the Spot and Derivatives APIs","url":"https://docs.kraken.com/home/sdks/go","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/sdks/go#webpage"},"dateModified":"2026-09-08T06:34:18.012Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```

<<<PAGE https://docs.kraken.com/home/sdks>>>
---
url: https://docs.kraken.com/home/sdks
title: SDKs - Kraken Developers
description: Official Kraken SDKs for Spot and Derivatives, plus community libraries
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Which one to use](#which-one-to-use)
* [Other tools](#other-tools)
* [Community libraries](#community-libraries)

SDKs

# SDKs

Copy pageCopy page

Official Kraken SDKs for Spot and Derivatives, plus community libraries

Copy pageCopy page

## Go

api-go. Spot and Derivatives, REST and WebSocket. The most complete coverage.

## Rust

kraken-sdk. Spot REST and WebSocket v2, plus Derivatives streams and order entry over the Unified WebSocket. Async-native.

## Which one to use

|  | Go | Rust |
| --- | --- | --- |
| Spot | Yes | Yes |
| Derivatives | Yes | Yes |
| Status | Stable | Stable |

## Other tools

## kraken-cli

One install, three binaries: `kraken`, `kraken-mcp` and `kraken-shell`. 188 commands for Spot and Derivatives trading, paper trading, scripting, and AI agent support.

## MCP server

`kraken-mcp` serves 152 of the CLI’s commands as MCP tools for LLM agents.

## Community libraries

These libraries are not officially maintained by Kraken. Review before using in production.

| Library | Language | Scope | Repository |
| --- | --- | --- | --- |
| kraken-wsclient-py | Python | WebSocket only (Spot) | [github.com/krakenfx/kraken-wsclient-py](https://github.com/krakenfx/kraken-wsclient-py) |
| kraken-api-client | PHP | REST (example only) | [github.com/krakenfx/kraken-api-client](https://github.com/krakenfx/kraken-api-client) |

Was this page helpful?

YesNo

[MCP Server](/home/mcp)[Go](/home/sdks/go)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/sdks#webpage","url":"https://docs.kraken.com/home/sdks","name":"SDKs","description":"Official Kraken SDKs for Spot and Derivatives, plus community libraries","dateModified":"2026-11-12T15:11:30.326Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/sdks#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/sdks#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"SDKs","item":"https://docs.kraken.com/home/sdks"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/sdks#article","headline":"SDKs","name":"SDKs","description":"Official Kraken SDKs for Spot and Derivatives, plus community libraries","url":"https://docs.kraken.com/home/sdks","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/sdks#webpage"},"dateModified":"2026-11-12T15:11:30.326Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```

<<<PAGE https://docs.kraken.com/home/sdks/rust>>>
---
url: https://docs.kraken.com/home/sdks/rust
title: Rust - Kraken Developers
description: kraken-sdk — the official Rust SDK for the Spot API, plus Derivatives streams and order entry over the Unified WebSocket
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [Requirements](#requirements)
* [Install](#install)
* [What it covers](#what-it-covers)
  + [Spot](#spot)
  + [Derivatives (Futures)](#derivatives-futures)
  + [Both](#both)
* [Example](#example)
  + [Derivatives example](#derivatives-example)
* [Notes for developers coming from other Kraken SDKs](#notes-for-developers-coming-from-other-kraken-sdks)

SDKs

# Rust

Copy pageCopy page

kraken-sdk — the official Rust SDK for the Spot API, plus Derivatives streams and order entry over the Unified WebSocket

Copy pageCopy page

[kraken-sdk](https://github.com/krakenfx/kraken-api-sdk) is the official Rust SDK for building integrations against the Spot API and, over the Unified WebSocket, the Derivatives (Futures) API. It is async-native, built on tokio, and presents REST and WebSocket behind a single client.

Spot is covered over REST and WebSocket v2. Derivatives is covered over the Unified WebSocket only: public and private streams, and order entry. There are no Derivatives REST methods.

## Requirements

Requires Rust 1.88 or later and the tokio async runtime.

## Install

```
[dependencies]
kraken-sdk = { git = "https://github.com/krakenfx/kraken-api-sdk", tag = "v0.1.0" }
tokio = { version = "1", features = ["full"] }
rust_decimal = "1"
```

## What it covers

### Spot

* Spot REST — complete public market data, plus authenticated account and trading endpoints
* Spot WebSocket v2 — public data streams and the authenticated `executions` and `balances` channels
* Order operations: add, amend, cancel, batch add, batch cancel, cancel-all, and a dead man’s switch
* Order routing over REST or authenticated WebSocket, selectable per call
* Real-time order book construction with CRC32 checksum validation and automatic reseeding on mismatch

### Derivatives (Futures)

* Public Unified WebSocket streams — system status, instrument, ticker, trade, OHLC and order book (maintained with CRC32 validation, or raw deltas)
* Private Unified WebSocket streams — `executions`, `positions`, `balances`, `margin` and `preferences`
* Order operations over the authenticated Unified WebSocket: place, amend, cancel by client order id or venue order id, batch place (2–15 orders on one symbol), batch cancel (2–50 orders), cancel-all, and a dead man’s switch that is independent of Spot’s
* Uses the same API key as Spot

### Both

* Automatic reconnect with subscription replay
* Typed errors carrying a stable code, category, retryable flag and request id
* An event bus for connection state, rate-limit warnings, order book gaps and order lifecycle

## Example

```
use kraken_sdk::{ApiKey, Client, Symbol};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder()
        .with_api_key(
            ApiKey::new(std::env::var("KRAKEN_API_KEY")?),
            std::env::var("KRAKEN_API_SECRET")?,
        )?
        .build()?;

    let resp = client.trade()
        .limit_buy(Symbol::new("BTC/USD")?, "0.01".parse()?, "60000".parse()?)
        .await?;

    println!("placed {:?}", resp.txid);
    Ok(())
}
```

Public market data needs no credentials:

```
use kraken_sdk::{Client, Symbol};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder().build()?;
    let pair = Symbol::new("BTC/USD")?;

    let tickers = client.market().ticker(Some(&[pair.clone()])).await?;
    if let Some(t) = tickers.get(&pair) {
        println!("last={} bid={} ask={}", t.last_price, t.bid_price, t.ask_price);
    }
    Ok(())
}
```

### Derivatives example

Stream a Futures order book, then place a limit order. Futures orders always travel on the authenticated Unified WebSocket, so call `client.ready()` before the first WebSocket operation.

```
use kraken_sdk::{
    ApiKey, BookDepth, Client, FuturesOrder, FuturesOrderRequest, OrderType, Side,
};
use rust_decimal::Decimal;
use std::str::FromStr;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::builder()
        .with_api_key(
            ApiKey::new(std::env::var("KRAKEN_API_KEY")?),
            std::env::var("KRAKEN_API_SECRET")?,
        )
        .build()?;
    client.ready().await?;

    // Dropping the guard unsubscribes and deregisters the handler
    let _book = client.market().futures().on_book_for(
        vec!["PF_XBTUSD".to_owned()],
        BookDepth::D10,
        |book| println!("{} bids={} asks={}", book.symbol, book.bids.len(), book.asks.len()),
    )?;

    let order = FuturesOrder::new(Side::Buy, Decimal::from_str("0.01")?)
        .order_type(OrderType::Limit)
        .price(Decimal::from_str("1500")?);
    let resp = client
        .trade()
        .futures()
        .order(FuturesOrderRequest::new("PF_ETHUSD", order))
        .await?;

    println!("placed {:?}", resp.txid);
    client.close().await?;
    Ok(())
}
```

Public Futures streams need no credentials. The private channels and order entry do.

## Notes for developers coming from other Kraken SDKs

* **Spot symbols use the modern format only.** `BTC/USD`, not `XBTUSD` or `XXBTZUSD`. Legacy codes return a typed error rather than being silently translated. Asset codes in responses are normalised the same way, so balances are keyed `BTC` and `USD`.
* **Derivatives symbols are the native venue strings.** `PF_XBTUSD`, `PF_ETHUSD` and dated contracts such as `FI_XBTUSD_251226`. A Spot pair sent to a Futures method is rejected before anything is sent.
* **Prices and quantities are decimals, not floats.** Parse them from strings (`"0.01".parse()?`). The API does not accept `f64`.
* **A WebSocket subscription is two steps:** register a handler, then subscribe. The `on_*_for` helpers do both in one call and unsubscribe when dropped.
* **Rate limits are reported, not enforced.** For Spot, the SDK emits a warning event as you approach your tier limit and never sleeps on your behalf, so pacing stays under your control. It does not track Derivatives orders. A venue throttle comes back as a retryable `RateLimited` error.
* **Derivatives has no REST path.** `.via(Transport::Rest)` on a Futures order returns a typed `UnsupportedTransport` error.
* **Dead man’s switches are per product.** The Spot and Derivatives timers are independent, and `cancel_all` on one does not touch the other’s orders.

See the [kraken-sdk repository](https://github.com/krakenfx/kraken-api-sdk) for the full method reference, guides and event catalogue.

Was this page helpful?

YesNo

[Go](/home/sdks/go)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/sdks/rust#webpage","url":"https://docs.kraken.com/home/sdks/rust","name":"Rust","description":"kraken-sdk — the official Rust SDK for the Spot API, plus Derivatives streams and order entry over the Unified WebSocket","dateModified":"2026-11-12T15:11:30.308Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/sdks/rust#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/sdks/rust#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Tools","item":"https://docs.kraken.com/home/cli"},{"@type":"ListItem","position":2,"name":"SDKs","item":"https://docs.kraken.com/home/sdks"},{"@type":"ListItem","position":3,"name":"Rust","item":"https://docs.kraken.com/home/sdks/rust"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/sdks/rust#article","headline":"Rust","name":"Rust","description":"kraken-sdk — the official Rust SDK for the Spot API, plus Derivatives streams and order entry over the Unified WebSocket","url":"https://docs.kraken.com/home/sdks/rust","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/sdks/rust#webpage"},"dateModified":"2026-11-12T15:11:30.308Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```

<<<PAGE https://docs.kraken.com/home/support>>>
---
url: https://docs.kraken.com/home/support
title: Support - Kraken Developers
description: Get help with Kraken API integrations — support channels, status monitoring, and contact options
fetched: 2026-11-16
method: static
plan: read
---

## On this page

Back to top

* [API status](#api-status)
* [Help center](#help-center)
* [Contact](#contact)

Getting started

# Support

Copy pageCopy page

Get help with Kraken API integrations — support channels, status monitoring, and contact options

Copy pageCopy page

## API status

Check real-time health and incident history for all Kraken APIs at [status.kraken.com](https://status.kraken.com).

## Help center

Browse troubleshooting guides, FAQs, and account-related support at [support.kraken.com](https://support.kraken.com).

## Contact

For API-specific issues, send a full copy of your request including your IP address and all headers to [api@kraken.com](mailto:api@kraken.com).

| Topic | Contact |
| --- | --- |
| General API support | [api@kraken.com](mailto:api@kraken.com) |
| Institutional onboarding | [institutional@kraken.com](mailto:institutional@kraken.com) |
| Embed / B2B partnerships | [embed@kraken.com](mailto:embed@kraken.com) |
| Market data licensing | [marketdata@kraken.com](mailto:marketdata@kraken.com) |

Was this page helpful?

YesNo

[Quickstart](/home/guides/quickstart)[CLI](/home/cli)

[x](https://x.com/krakenfx)[github](https://github.com/krakenfx)[linkedin](https://linkedin.com/company/kraken-exchange)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://docs.kraken.com/#organization","name":"Kraken Developers","url":"https://docs.kraken.com","logo":{"@type":"ImageObject","url":"https://mintcdn.com/kraken/opwCJHYUnRFWd1O3/logo/light.svg?fit=max&auto=format&n=opwCJHYUnRFWd1O3&q=85&s=6be2f97a23f9a7aa6ef071ae334cc89c"}},{"@type":"WebSite","@id":"https://docs.kraken.com#website","name":"Kraken Developers","url":"https://docs.kraken.com","publisher":{"@id":"https://docs.kraken.com/#organization"}},{"@type":"WebPage","@id":"https://docs.kraken.com/home/support#webpage","url":"https://docs.kraken.com/home/support","name":"Support","description":"Get help with Kraken API integrations — support channels, status monitoring, and contact options","dateModified":"2026-11-12T15:11:30.307Z","isPartOf":{"@id":"https://docs.kraken.com#website"},"breadcrumb":{"@id":"https://docs.kraken.com/home/support#breadcrumb"}},{"@type":"BreadcrumbList","@id":"https://docs.kraken.com/home/support#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Getting started","item":"https://docs.kraken.com"},{"@type":"ListItem","position":2,"name":"Support","item":"https://docs.kraken.com/home/support"}]},{"@type":["Article","TechArticle"],"@id":"https://docs.kraken.com/home/support#article","headline":"Support","name":"Support","description":"Get help with Kraken API integrations — support channels, status monitoring, and contact options","url":"https://docs.kraken.com/home/support","mainEntityOfPage":{"@id":"https://docs.kraken.com/home/support#webpage"},"dateModified":"2026-11-12T15:11:30.307Z","publisher":{"@id":"https://docs.kraken.com/#organization"},"isPartOf":{"@id":"https://docs.kraken.com#website"}}]}
```