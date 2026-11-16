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