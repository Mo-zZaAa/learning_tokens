---
url: https://docs.dinari.com/docs/stock-split-handling
title: Stock Splits
description: How Dinari applies forward and reverse stock splits to dShares
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Stock Splits

How Dinari applies forward and reverse stock splits to dShares

Dinari processes both forward and reverse stock splits through a single, unified pipeline. The only differences are the ratio's direction and how leftover fractions are handled.

```
graph LR
    A[Trading Halts] --> B[Token Rebased] --> C[Balances Verified] --> D[Trading Resumes]
```

---

## Reading a split

A split is described by two fields:

| Field | Meaning |
| --- | --- |
| `split_from` | Shares you hold before |
| `split_to` | Shares you hold after |

A **10-for-1 forward split** has `split_from = 1`, `split_to = 10`. A **1-for-40 reverse split** has `split_from = 40`, `split_to = 1`.

The direction is simply which value is larger:

TypeScriptPythonGoJava

```
// `split` is a StockSplit from the stock-splits list calls in the SDK examples below
const isReverse = Number(split.splitFrom) > Number(split.splitTo);
const multiplier = Number(split.splitTo) / Number(split.splitFrom); // 10 forward, 0.025 reverse
```

```
# `split` is a StockSplit from the stock-splits list calls in the SDK examples below
is_reverse = float(split.split_from) > float(split.split_to)
multiplier = float(split.split_to) / float(split.split_from)  # 10.0 forward, 0.025 reverse
```

```
// `split` is a StockSplit from the stock-splits list calls in the SDK examples below
splitFrom, _ := strconv.ParseFloat(split.SplitFrom, 64)
splitTo, _ := strconv.ParseFloat(split.SplitTo, 64)
isReverse := splitFrom > splitTo
multiplier := splitTo / splitFrom // 10 forward, 0.025 reverse
```

```
// `split` is a StockSplit from the stock-splits list calls in the SDK examples below
BigDecimal splitFrom = new BigDecimal(split.getSplitFrom());
BigDecimal splitTo = new BigDecimal(split.getSplitTo());
boolean isReverse = splitFrom.compareTo(splitTo) > 0;
BigDecimal multiplier = splitTo.divide(splitFrom, MathContext.DECIMAL64); // 10 forward, 0.025 reverse
```

### Dates and status

| Field | Meaning |
| --- | --- |
| `record_date` | Date a holder must hold to be entitled |
| `payable_date` | Trading halts at the **end** of this day |
| `ex_date` | Trading resumes at split-adjusted prices |
| `status` | `PENDING` → `IN_PROGRESS` → `COMPLETE` |

Splits are usually scheduled over a weekend to minimize disruption. While a split is `IN_PROGRESS`, the stock is not available for trading.

---

## Forward splits

### What happens

1. **Trading halts.** New orders are rejected, active orders are cancelled, and the dShare™ token is paused.
2. **The token is rebased** to match the split ratio.
3. **Dinari verifies balances** across all systems and confirms the underlying stock changes are reflected.
4. **Trading resumes.** New orders are accepted and the token is unpaused.  
   Balances scale automatically. Dinari adjusts the token's balance-per-share once rather than minting to each holder individually, so there is no per-wallet transaction to watch for — read the new balance from the portfolio endpoint after `COMPLETE`.

```
sequenceDiagram
    autonumber
    participant D as Dinari
    participant P as Partner
    participant U as End user
 
    Note over D: 10-for-1 split announced — status = PENDING
    P->>D: Poll for splits
    D-->>P: split_from 1, split_to 10,<br/>payable_date, ex_date
    P->>U: Notify: split scheduled
 
    Note over D: End of payable_date — status = IN_PROGRESS
    D->>D: Halt trading, cancel open orders,<br/>rebase the token
    P->>P: Pause trading in your UI
 
    Note over D: ex_date — status = COMPLETE, trading resumes
    P->>D: Read portfolio
    D-->>P: Balance x10, value unchanged
    P->>U: Update ledger, show new share count
```

---

## Reverse splits

A reverse split does the opposite: the share count falls and the price rises proportionally. A 1-for-40 reverse split turns 40 dShares into 1.

Reverse splits use the same pipeline as forward splits — halt, rebase, verify, resume. The ratio is simply inverted. The one difference that matters to your integration is fractional handling.

### Fractional handling

Because dShares are fractionable, most reverse splits produce no rounding problem: the holder ends up with fewer dShares at a higher price and the position value is unchanged.

The exception is when the post-split stock becomes **non-fractionable**. The leftover fraction cannot be represented, so it is liquidated and the holder receives the proceeds in **USD+** instead of dShares. A small enough position can end at zero shares plus a cash credit.

```
sequenceDiagram
    autonumber
    participant D as Dinari
    participant P as Partner
    participant U as End user
 
    Note over D: 1-for-40 reverse split announced — status = PENDING
    P->>D: Poll for splits
    D-->>P: split_from 40, split_to 1,<br/>payable_date, ex_date
    P->>U: Notify: reverse split scheduled
 
    Note over D: End of payable_date — status = IN_PROGRESS
    D->>D: Halt trading, cancel open orders,<br/>rebase the token
    P->>P: Pause trading in your UI
 
    alt Post-split balance remains fractionable
        D->>D: Holder keeps a smaller<br/>dShare balance
    else Post-split balance is non-fractionable
        D->>D: Burn the leftover fraction,<br/>credit USD+ of equivalent value
        D->>P: Direct notification of<br/>affected holders
    end
 
    Note over D: ex_date — status = COMPLETE, trading resumes
    P->>D: Read portfolio and cash balances
    D-->>P: New balances, any USD+ credit
    P->>U: Update ledger, show new share count<br/>and any cash in lieu
```

### Duplicate asset records

A reverse split is sometimes accompanied by a CUSIP change, which can cause the market data provider to emit a duplicate stock record under the same symbol. Dinari refreshes the asset list and merges the duplicate into the existing record, so **the stock ID your integration references stays stable**. No action is required from you.

---

## Recommended Flow

Both directions call for the same integration work.

1. **Poll for splits** daily on the stocks your users hold. Splits are scheduled well in advance.
2. **Pause trading** in your interface while `status` is `IN_PROGRESS`, and expect open orders to be cancelled.
3. **Re-read balances** once `status` is `COMPLETE` and update your ledger. For reverse splits, check cash balances too — a USD+ credit may have replaced a fraction.
4. **Show the ratio, not just the new number.** "Your 5 shares became 50 in a 10-for-1 split, value unchanged" prevents most support tickets.

---

## SDK examples

### Detect upcoming and in-progress splits

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here";
  const response = await client.corporateActions.getStockSplitsById({
    stockId,
    limit: 20, // cursor pagination: the next page's cursor is in response.paginationMetadata.next
  });
  const splits = Array.isArray(response) ? response : response.data;

  for (const s of splits) {
    const isReverse = Number(s.splitFrom) > Number(s.splitTo);
    console.log(
      `${s.splitFrom}-for-${s.splitTo} ` +
      `${isReverse ? "reverse" : "forward"} — ` +
      `${s.status}, ex-date ${s.exDate}`
    );
  }
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

response = client.corporate_actions.get_stock_splits_by_id(
    stock_id="stock-id-here",
    limit=20,  # cursor pagination: the next page's cursor is in response.pagination_metadata.next
)
splits = response if isinstance(response, list) else response.data

for s in splits:
    is_reverse = float(s.split_from) > float(s.split_to)
    direction = "reverse" if is_reverse else "forward"
    print(f"{s.split_from}-for-{s.split_to} {direction} — "
          f"{s.status}, ex-date {s.ex_date}")
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"strconv"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	response, err := c.CorporateActions.GetStockSplitsByID(context.Background(), &dinari.GetStockSplitsByIDRequest{
		StockID: "stock-id-here",
		Limit:   dinari.Int(20), // cursor pagination: the next page's cursor is in PaginationMetadata.Next
	})
	if err != nil {
		log.Fatalf("Failed to list splits: %v", err)
	}

	for _, s := range response.GetPaginatedStockSplitResponse().Data {
		splitFrom, _ := strconv.ParseFloat(s.SplitFrom, 64)
		splitTo, _ := strconv.ParseFloat(s.SplitTo, 64)
		direction := "forward"
		if splitFrom > splitTo {
			direction = "reverse"
		}
		fmt.Printf("%s-for-%s %s — %s, ex-date %s\n", s.SplitFrom, s.SplitTo, direction, s.Status, s.ExDate)
	}
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.corporateactions.requests.GetStockSplitsByIdRequest;
import com.dinari.api.types.PaginatedStockSplitResponse;
import com.dinari.api.types.StockSplit;
import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        // With `limit`, the response is cursor-paginated: the next page's cursor is in getPaginationMetadata().getNext()
        var response = client.corporateActions().getStockSplitsById(
                "stock-id-here",
                GetStockSplitsByIdRequest.builder().limit(20).build());
        var page = (PaginatedStockSplitResponse) response.get();

        for (StockSplit s : page.getData()) {
            boolean isReverse = new BigDecimal(s.getSplitFrom()).compareTo(new BigDecimal(s.getSplitTo())) > 0;
            System.out.println(s.getSplitFrom() + "-for-" + s.getSplitTo() + " "
                    + (isReverse ? "reverse" : "forward") + " — "
                    + s.getStatus() + ", ex-date " + s.getExDate());
        }
    }
}
```

> **Info:** Each `StockSplit` contains `id`, `stock_id`, `split_from`, `split_to`, `record_date`, `payable_date`, `ex_date`, and `status`.

---

### Gate trading on split status

TypeScriptPythonGoJava

```
async function canTrade(stockId: string): Promise<[boolean, string | null]> {
  const response = await client.corporateActions.getStockSplitsById({ stockId, limit: 20 });
  const splits = Array.isArray(response) ? response : response.data;

  for (const s of splits) {
    if (s.status === "IN_PROGRESS") {
      const direction = Number(s.splitFrom) > Number(s.splitTo) ? "reverse split" : "stock split";
      return [
        false,
        `Trading is paused for a ${s.splitFrom}-for-${s.splitTo} ` +
        `${direction}. It resumes on ${s.exDate}.`,
      ];
    }
  }
  return [true, null];
}

const [allowed, message] = await canTrade("stock-id-here");
if (!allowed) {
  showBanner(message);
}
```

```
def can_trade(stock_id: str) -> tuple[bool, str | None]:
    response = client.corporate_actions.get_stock_splits_by_id(stock_id=stock_id, limit=20)
    splits = response if isinstance(response, list) else response.data

    for s in splits:
        if s.status == "IN_PROGRESS":
            direction = "reverse split" if float(s.split_from) > float(s.split_to) else "stock split"
            return False, (
                f"Trading is paused for a {s.split_from}-for-{s.split_to} "
                f"{direction}. It resumes on {s.ex_date}."
            )
    return True, None

allowed, message = can_trade("stock-id-here")
if not allowed:
    show_banner(message)
```

```
canTrade := func(stockID string) (bool, string, error) {
	response, err := c.CorporateActions.GetStockSplitsByID(ctx, &dinari.GetStockSplitsByIDRequest{
		StockID: stockID,
		Limit:   dinari.Int(20),
	})
	if err != nil {
		return false, "", err
	}

	for _, s := range response.GetPaginatedStockSplitResponse().Data {
		if s.Status == dinari.StockSplitStatus1InProgress {
			splitFrom, _ := strconv.ParseFloat(s.SplitFrom, 64)
			splitTo, _ := strconv.ParseFloat(s.SplitTo, 64)
			direction := "stock split"
			if splitFrom > splitTo {
				direction = "reverse split"
			}
			return false, fmt.Sprintf("Trading is paused for a %s-for-%s %s. It resumes on %s.",
				s.SplitFrom, s.SplitTo, direction, s.ExDate), nil
		}
	}
	return true, "", nil
}

allowed, message, err := canTrade("stock-id-here")
if err != nil {
	log.Fatalf("Failed to check splits: %v", err)
}
if !allowed {
	showBanner(message)
}
```

```
static Optional<String> tradingPausedReason(DinariClient client, String stockId) {
    var response = client.corporateActions().getStockSplitsById(
            stockId,
            GetStockSplitsByIdRequest.builder().limit(20).build());
    var page = (PaginatedStockSplitResponse) response.get();

    for (StockSplit s : page.getData()) {
        if (StockSplitStatus1.IN_PROGRESS.equals(s.getStatus())) {
            boolean isReverse = new BigDecimal(s.getSplitFrom()).compareTo(new BigDecimal(s.getSplitTo())) > 0;
            String direction = isReverse ? "reverse split" : "stock split";
            return Optional.of("Trading is paused for a " + s.getSplitFrom() + "-for-" + s.getSplitTo()
                    + " " + direction + ". It resumes on " + s.getExDate() + ".");
        }
    }
    return Optional.empty();
}

Optional<String> reason = tradingPausedReason(client, "stock-id-here");
reason.ifPresent(message -> showBanner(message));
```

---

### Reconcile balances after a split completes

TypeScriptPythonGoJava

```
const accountId = "your-account-id";

// Snapshot before the split
const beforePortfolio = await client.accounts.getAccountPortfolio({ accountId });
const before = new Map(beforePortfolio.assets.map((b) => [b.stockId, b.amount]));

// ... after status flips to COMPLETE ...

const portfolio = await client.accounts.getAccountPortfolio({ accountId });

for (const b of portfolio.assets) {
  const old = before.get(b.stockId);
  if (old !== undefined && old !== b.amount) {
    console.log(`${b.symbol} on chain ${b.chainId}: ${old} -> ${b.amount}`);
    ledger.setBalance(accountId, b.stockId, b.amount, "stock_split");
  }
}

// Reverse splits may also produce a USD+ credit in lieu of a fraction
const cash = await client.accounts.getAccountCash({ accountId });
```

```
ACCOUNT_ID = "your-account-id"

# Snapshot before the split
before = {
    b.stock_id: b.amount
    for b in client.accounts.get_account_portfolio(account_id=ACCOUNT_ID).assets
}

# ... after status flips to COMPLETE ...

portfolio = client.accounts.get_account_portfolio(account_id=ACCOUNT_ID)

for b in portfolio.assets:
    old = before.get(b.stock_id)
    if old is not None and old != b.amount:
        print(f"{b.symbol} on chain {b.chain_id}: {old} -> {b.amount}")
        ledger.set_balance(ACCOUNT_ID, b.stock_id, b.amount, reason="stock_split")

# Reverse splits may also produce a USD+ credit in lieu of a fraction
cash = client.accounts.get_account_cash(account_id=ACCOUNT_ID)
```

```
accountID := "your-account-id"

// Snapshot before the split
beforePortfolio, err := c.Accounts.GetAccountPortfolio(ctx, &dinari.GetAccountPortfolioRequest{AccountID: accountID})
if err != nil {
	log.Fatalf("Failed to get portfolio: %v", err)
}
before := map[string]string{}
for _, b := range beforePortfolio.Assets {
	before[b.StockID] = b.Amount
}

// ... after status flips to COMPLETE ...

portfolio, err := c.Accounts.GetAccountPortfolio(ctx, &dinari.GetAccountPortfolioRequest{AccountID: accountID})
if err != nil {
	log.Fatalf("Failed to get portfolio: %v", err)
}

for _, b := range portfolio.Assets {
	if old, ok := before[b.StockID]; ok && old != b.Amount {
		fmt.Printf("%s on chain %s: %s -> %s\n", b.Symbol, b.ChainID, old, b.Amount)
		ledger.SetBalance(accountID, b.StockID, b.Amount, "stock_split")
	}
}

// Reverse splits may also produce a USD+ credit in lieu of a fraction
cash, err := c.Accounts.GetAccountCash(ctx, &dinari.GetAccountCashRequest{AccountID: accountID})
```

```
String accountId = "your-account-id";

// Snapshot before the split
Map<String, String> before = new HashMap<>();
for (DshareBalance b : client.accounts().getAccountPortfolio(accountId).getAssets()) {
    before.put(b.getStockId(), b.getAmount());
}

// ... after status flips to COMPLETE ...

var portfolio = client.accounts().getAccountPortfolio(accountId);

for (DshareBalance b : portfolio.getAssets()) {
    String old = before.get(b.getStockId());
    if (old != null && !old.equals(b.getAmount())) {
        System.out.println(b.getSymbol() + " on chain " + b.getChainId() + ": " + old + " -> " + b.getAmount());
        ledger.setBalance(accountId, b.getStockId(), b.getAmount(), "stock_split");
    }
}

// Reverse splits may also produce a USD+ credit in lieu of a fraction
var cash = client.accounts().getAccountCash(accountId);
```

> Each `DshareBalance` in the portfolio contains `stock_id`, `symbol`, `amount`, `chain_id`, and `token_address`.

---

Updated 6 days ago

---

[Dividends](https://docs.dinari.com/docs/dividend-payments)[Ticker Changes](https://docs.dinari.com/docs/ticker-changes)

Did this page help you?

Yes

No

Copy Page

* + [Reading a split](https://docs.dinari.com/docs/stock-split-handling)
  + - [Dates and status](https://docs.dinari.com/docs/stock-split-handling)
  + [Forward splits](https://docs.dinari.com/docs/stock-split-handling)
  + - [What happens](https://docs.dinari.com/docs/stock-split-handling)
  + [Reverse splits](https://docs.dinari.com/docs/stock-split-handling)
  + - [Fractional handling](https://docs.dinari.com/docs/stock-split-handling)
    - [Duplicate asset records](https://docs.dinari.com/docs/stock-split-handling)
  + [Recommended Flow](https://docs.dinari.com/docs/stock-split-handling)
  + [SDK examples](https://docs.dinari.com/docs/stock-split-handling)
  + - [Detect upcoming and in-progress splits](https://docs.dinari.com/docs/stock-split-handling)
    - [Gate trading on split status](https://docs.dinari.com/docs/stock-split-handling)
    - [Reconcile balances after a split completes](https://docs.dinari.com/docs/stock-split-handling)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Stock Splits","dateModified":"2026-11-10T03:21:35.000Z"}
```