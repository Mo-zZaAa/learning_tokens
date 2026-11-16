---
url: https://docs.dinari.com/docs/dividend-payments
title: Dividends
description: How Dinari calculates and distributes dividends to dShare holders, and how to reconcile them in your integration.
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

# Dividends

How Dinari calculates and distributes dividends to dShare holders, and how to reconcile them in your integration.

# Dividends

Holders of any dShare token backed by a dividend-issuing security receive dividends. Cash dividends are the supported, fully automated dividend type at Dinari. They are detected, calculated, and distributed end-to-end without manual intervention.

---

## How it works at Dinari

```
sequenceDiagram
    autonumber
    participant I as Issuer
    participant D as Dinari
    participant C as Chain
    participant P as Partner
    participant U as End user
 
    I->>D: Declares dividend<br/>(record, ex, pay dates)
    D->>D: Ingests and classifies<br/>as cash_dividend
    P->>D: GET /market_data/stocks/{id}/dividends
    D-->>P: Announcement:<br/>cash_amount, ex_dividend_date, pay_date
    P->>U: Surface upcoming dividend
 
    I->>D: Fiat payment settles<br/>from the underlying
    D->>D: Calculate per-holder amount<br/>(minimum $0.10)
    D->>C: Distribute USD+ to dShare holders<br/>(or dShare into wrapped dShares)
 
    P->>D: GET /accounts/{id}/dividend_payments
    D-->>P: DividendPayment records
    P->>U: Credit user and notify
```

### Qualification

To be eligible for a dividend, **all** of the following must be true:

* The wallet is registered with an account
* The account is registered with an entity
* The entity is qualified with a valid KYC

### Distribution

Once the fiat payment from the underlying is confirmed, distribution runs shortly after. The amount per holder is calculated, and the form it arrives in depends on how the dShares are held:

| Held type | Receive dividend as |
| --- | --- |
| dShare | USD+ |
| Wrapped dShare | Underlying dShare, deposited into the wrapped dShare |

### Supported chains

| Chain name | Chain ID |
| --- | --- |
| Mainnet | 1 |
| Base | 8453 |
| Arbitrum | 42161 |
| Avalanche C-Chain | 43114 |
| Plume | 98866 |

### Dividend types

Announcement data distinguishes two types:

| Type | Meaning |
| --- | --- |
| `CD` | Dividends that have been paid and/or are expected to be paid on consistent schedules |
| `SC` | Special Cash dividends that have been paid that are infrequent or unusual, and/or can not be expected to occur in the future |

Both are cash distributions and follow the same path.

---

## Integration guide to dividends

Dividends require no on-chain action from you. Dinari takes the snapshot, calculates entitlements, and distributes them. Your integration is read-only so you are only responsible for confirming a user qualifies before the snapshot, then reconcile what was paid.

To integrate dividends, complete three steps:

1. **Find the dividend** -fetch announcements and identify the ex-dividend and pay dates.
2. **Reconcile the payment** - after the pay date, list what was paid and confirm the cash balance moved.

### Step 1: Find the dividend

#### Initialize the client

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

const accountId = "your-account-id";
const entityId = "your-entity-id";
const stockId = "stock-id-here";
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

ACCOUNT_ID = "your-account-id"  # Replace with the actual Account ID
ENTITY_ID = "your-entity-id"    # Replace with the actual Entity ID
STOCK_ID = "stock-id-here"      # Replace with the actual Stock ID
```

```
package main

import (
	"context"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

var (
	c = client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx = context.Background()
)

const (
	accountID = "your-account-id"
	entityID  = "your-entity-id"
	stockID   = "stock-id-here"
)
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    static final DinariClient client = DinariClient.builder()
            .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
            .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
            .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
            .build();

    static final String accountId = "your-account-id";
    static final String entityId = "your-entity-id";
    static final String stockId = "stock-id-here";
}
```

#### Fetch announced dividends and select the next one

Announcements describe what the underlying issuer declared — use them for dates and estimates, not as a record of payment. Sort by ex-dividend date and take the next one that has not yet passed.

TypeScriptPythonGoJava

```
const dividends = await client.corporateActions.getStockDividendsByStockId({ stockId });
const today = new Date().toISOString().slice(0, 10);

const next = dividends
  .filter((d) => d.exDividendDate != null && d.exDividendDate >= today)
  .sort((a, b) => a.exDividendDate!.localeCompare(b.exDividendDate!))[0];

if (!next) {
  console.log("No upcoming dividend announced for this stock.");
} else {
  const kind = next.dividendType === "SC" ? "special" : "regular";
  console.log(
    `${next.ticker}: ${next.cashAmount} ${next.currency} (${kind}) — ` +
    `record ${next.recordDate}, ex-date ${next.exDividendDate}, pays ${next.payDate}`
  );
}
```

```
from datetime import date

dividends = client.corporate_actions.get_stock_dividends_by_stock_id(
    stock_id=STOCK_ID
)
today = date.today()

upcoming = sorted(
    (d for d in dividends if d.ex_dividend_date is not None and d.ex_dividend_date >= today),
    key=lambda d: d.ex_dividend_date,
)
next_dividend = upcoming[0] if upcoming else None

if next_dividend is None:
    print("No upcoming dividend announced for this stock.")
else:
    kind = "special" if next_dividend.dividend_type == "SC" else "regular"
    print(f"{next_dividend.ticker}: {next_dividend.cash_amount} "
          f"{next_dividend.currency} ({kind}) — "
          f"record {next_dividend.record_date}, "
          f"ex-date {next_dividend.ex_dividend_date}, "
          f"pays {next_dividend.pay_date}")
```

```
dividends, err := c.CorporateActions.GetStockDividendsByStockID(ctx, &dinari.GetStockDividendsByStockIDRequest{
	StockID: stockID,
})
if err != nil {
	log.Fatalf("Failed to get dividends: %v", err)
}
today := time.Now().UTC().Truncate(24 * time.Hour)

var next *dinari.StockDividendAnnouncementDetail
for _, d := range dividends {
	if d.ExDividendDate == nil || d.ExDividendDate.Before(today) {
		continue
	}
	if next == nil || d.ExDividendDate.Before(*next.ExDividendDate) {
		next = d
	}
}

if next == nil {
	fmt.Println("No upcoming dividend announced for this stock.")
} else {
	kind := "regular"
	if str(next.DividendType) == "SC" {
		kind = "special"
	}
	fmt.Printf("%s: %s %s (%s) — record %s, ex-date %s, pays %s\n",
		str(next.Ticker), str(next.CashAmount), str(next.Currency), kind,
		next.RecordDate.Format("2006-01-02"), next.ExDividendDate.Format("2006-01-02"), next.PayDate.Format("2006-01-02"))
}
```

```
var dividends = client.corporateActions().getStockDividendsByStockId(stockId);
String today = LocalDate.now().toString();

StockDividendAnnouncementDetail next = dividends.stream()
        .filter(d -> d.getExDividendDate().isPresent() && d.getExDividendDate().get().compareTo(today) >= 0)
        .min(Comparator.comparing(d -> d.getExDividendDate().get()))
        .orElse(null);

if (next == null) {
    System.out.println("No upcoming dividend announced for this stock.");
} else {
    String kind = "SC".equals(next.getDividendType().orElse("")) ? "special" : "regular";
    System.out.println(next.getTicker().orElse("") + ": " + next.getCashAmount().orElse("") + " "
            + next.getCurrency().orElse("") + " (" + kind + ") — record " + next.getRecordDate().orElse("")
            + ", ex-date " + next.getExDividendDate().orElse("") + ", pays " + next.getPayDate().orElse(""));
}
```

### Step 2: Check eligibility

#### Confirm the holding and estimate the entitlement

Balances are returned per chain, so sum across them rather than reading the first match. Distributions below $0.10 are not paid, so check that threshold too.

TypeScriptPythonGoJava

```
const portfolio = await client.accounts.getAccountPortfolio({ accountId });

const totalHeld = portfolio.assets
  .filter((b) => b.stockId === stockId)
  .reduce((sum, b) => sum + Number(b.amount), 0);

if (totalHeld === 0) {
  console.log("Not eligible: no dShares held for this stock.");
}

const estimated = totalHeld * Number(next.cashAmount);

if (estimated > 0 && estimated < 0.1) {
  console.log(
    `Estimated entitlement is ${estimated.toFixed(4)} ${next.currency}, ` +
    `below the $0.10 minimum. No payment will be made.`
  );
}
```

```
portfolio = client.accounts.get_account_portfolio(account_id=ACCOUNT_ID)

total_held = sum(
    float(b.amount) for b in portfolio.assets if b.stock_id == STOCK_ID
)

if total_held == 0:
    print("Not eligible: no dShares held for this stock.")

estimated = total_held * float(next_dividend.cash_amount)

if 0 < estimated < 0.10:
    print(f"Estimated entitlement is {estimated:.4f} "
          f"{next_dividend.currency}, below the $0.10 minimum. "
          f"No payment will be made.")
```

```
portfolio, err := c.Accounts.GetAccountPortfolio(ctx, &dinari.GetAccountPortfolioRequest{AccountID: accountID})
if err != nil {
	log.Fatalf("Failed to get portfolio: %v", err)
}

totalHeld := 0.0
for _, b := range portfolio.Assets {
	if b.StockID == stockID {
		amount, _ := strconv.ParseFloat(b.Amount, 64)
		totalHeld += amount
	}
}

if totalHeld == 0 {
	fmt.Println("Not eligible: no dShares held for this stock.")
}

cashAmount, _ := strconv.ParseFloat(str(next.CashAmount), 64)
estimated := totalHeld * cashAmount

if estimated > 0 && estimated < 0.10 {
	fmt.Printf("Estimated entitlement is %.4f %s, below the $0.10 minimum. No payment will be made.\n",
		estimated, str(next.Currency))
}
```

```
var portfolio = client.accounts().getAccountPortfolio(accountId);

double totalHeld = portfolio.getAssets().stream()
        .filter(b -> b.getStockId().equals(stockId))
        .mapToDouble(b -> Double.parseDouble(b.getAmount()))
        .sum();

if (totalHeld == 0) {
    System.out.println("Not eligible: no dShares held for this stock.");
}

double estimated = totalHeld * Double.parseDouble(next.getCashAmount().orElse("0"));

if (estimated > 0 && estimated < 0.10) {
    System.out.printf("Estimated entitlement is %.4f %s, below the $0.10 minimum. No payment will be made.%n",
            estimated, next.getCurrency().orElse(""));
}
```

#### Confirm the account is qualified to receive

A holding alone is not enough: the wallet must be connected and the entity must hold a valid KYC. This catches accounts that lapsed after onboarding.

TypeScriptPythonGoJava

```
let hasWallet = true;
try {
  await client.wallets.getWallet({ accountId });
} catch (e) {
  if (e instanceof DinariError && e.statusCode === 404) {
    hasWallet = false;
    console.log("Not eligible: no wallet connected to this account.");
  } else {
    throw e;
  }
}

// The entity behind the account must be KYC-qualified.
const kyc = await client.kyc.getEntityKyc({ entityId });
if (kyc.status !== "PASS") {
  console.log(`Not eligible: entity KYC status is ${kyc.status}.`);
}
```

```
try:
    client.wallets.get_wallet(account_id=ACCOUNT_ID)
except ApiError as e:
    if e.status_code != 404:
        raise
    print("Not eligible: no wallet connected to this account.")

# The entity behind the account must be KYC-qualified.
kyc = client.kyc.get_entity_kyc(entity_id=ENTITY_ID)
if kyc.status != "PASS":
    print(f"Not eligible: entity KYC status is {kyc.status}.")
```

```
if _, err := c.Wallets.GetWallet(ctx, &dinari.GetWalletRequest{AccountID: accountID}); err != nil {
	var apiErr *core.APIError
	if !errors.As(err, &apiErr) || apiErr.StatusCode != 404 {
		log.Fatalf("Failed to get wallet: %v", err)
	}
	fmt.Println("Not eligible: no wallet connected to this account.")
}

// The entity behind the account must be KYC-qualified.
kyc, err := c.Kyc.GetEntityKyc(ctx, &dinari.GetEntityKycRequest{EntityID: entityID})
if err != nil {
	log.Fatalf("Failed to get KYC: %v", err)
}
var kycStatus dinari.KycStatus
if k := kyc.GetBaseline(); k != nil {
	kycStatus = k.Status
} else if k := kyc.GetUs(); k != nil {
	kycStatus = k.Status
}
if kycStatus != dinari.KycStatusPass {
	fmt.Printf("Not eligible: entity KYC status is %s.\n", kycStatus)
}
```

```
try {
    client.wallets().getWallet(accountId);
} catch (DinariClientApiException e) {
    if (e.statusCode() != 404) {
        throw e;
    }
    System.out.println("Not eligible: no wallet connected to this account.");
}

// The entity behind the account must be KYC-qualified.
var kyc = client.kyc().getEntityKyc(entityId);
KycStatus kycStatus = kyc.getBaseline().map(BaselineKyc::getStatus)
        .or(() -> kyc.getUs().map(UsKyc::getStatus))
        .orElseThrow();
if (!KycStatus.PASS.equals(kycStatus)) {
    System.out.println("Not eligible: entity KYC status is " + kycStatus + ".");
}
```

### Step 3: Reconcile the payment

#### List payments for the window

`start_date` is inclusive, `end_date` is exclusive, both required and in **US Eastern time**. Filter by `stock_id` for a single dividend.

TypeScriptPythonGoJava

```
const payments = await client.accounts.getAccountDividendPayments({
  accountId,
  startDate: "2026-01-01", // Inclusive, US Eastern time
  endDate: "2026-02-01", // Exclusive, US Eastern time
  stockId, // optional
  limit: 20,
});

for (const p of Array.isArray(payments) ? payments : payments.data) {
  console.log(`${p.paymentDate}: ${p.amount} ${p.currency} from ${p.stockId}`);
}
```

```
import datetime

payments = client.accounts.get_account_dividend_payments(
    account_id=ACCOUNT_ID,
    start_date=datetime.date(2026, 1, 1),  # Inclusive, US Eastern time
    end_date=datetime.date(2026, 2, 1),    # Exclusive, US Eastern time
    stock_id=STOCK_ID,                     # Optional
    limit=20,
)

for p in payments if isinstance(payments, list) else payments.data:
    print(f"{p.payment_date}: {p.amount} {p.currency} from {p.stock_id}")
```

```
payments, err := c.Accounts.GetAccountDividendPayments(ctx, &dinari.GetAccountDividendPaymentsRequest{
	AccountID: accountID,
	StartDate: dinari.MustParseDate("2026-01-01"), // Inclusive, US Eastern time
	EndDate:   dinari.MustParseDate("2026-02-01"), // Exclusive, US Eastern time
	StockID:   dinari.String(stockID),             // Optional
	Limit:     dinari.Int(20),
})
if err != nil {
	log.Fatalf("Failed to get dividend payments: %v", err)
}

for _, p := range payments.GetPaginatedDividendPaymentResponse().Data {
	fmt.Printf("%s: %s %s from %s\n", p.PaymentDate.Format("2006-01-02"), p.Amount, p.Currency, p.StockID)
}
```

```
var payments = client.accounts().getAccountDividendPayments(
        accountId,
        GetAccountDividendPaymentsRequest.builder()
                .startDate("2026-01-01") // Inclusive, US Eastern time
                .endDate("2026-02-01") // Exclusive, US Eastern time
                .stockId(stockId) // Optional
                .limit(20)
                .build());

for (DividendPayment p : ((PaginatedDividendPaymentResponse) payments.get()).getData()) {
    System.out.println(p.getPaymentDate() + ": " + p.getAmount() + " " + p.getCurrency() + " from " + p.getStockId());
}
```

#### Page through larger windows

Results are cursor-paginated (`limit` between 20 and 100), so a wide date range spans several pages. Follow the cursor — skipping this is the most common cause of a reconciliation that silently misses payments.

TypeScriptPythonGoJava

```
async function allDividendPayments(accountId: string, startDate: string, endDate: string) {
  const results = [];
  let cursor: string | undefined = undefined;

  do {
    const page = await client.accounts.getAccountDividendPayments({
      accountId,
      startDate,
      endDate,
      limit: 20,
      order: "asc",
      next: cursor,
    });

    if (Array.isArray(page)) {
      results.push(...page);
      break;
    }
    results.push(...page.data);
    cursor = page.paginationMetadata.next;
  } while (cursor);

  return results;
}
```

```
def all_dividend_payments(account_id, start_date, end_date):
    results = []
    cursor = None

    while True:
        page = client.accounts.get_account_dividend_payments(
            account_id=account_id,
            start_date=start_date,
            end_date=end_date,
            limit=20,
            order="asc",
            next=cursor,
        )

        results.extend(page.data)
        cursor = page.pagination_metadata.next
        if not cursor:
            break

    return results
```

```
allDividendPayments := func(accountID string, startDate, endDate time.Time) ([]*dinari.DividendPayment, error) {
	var results []*dinari.DividendPayment
	var cursor *string

	for {
		page, err := c.Accounts.GetAccountDividendPayments(ctx, &dinari.GetAccountDividendPaymentsRequest{
			AccountID: accountID,
			StartDate: startDate,
			EndDate:   endDate,
			Limit:     dinari.Int(20),
			Order:     dinari.GetAccountDividendPaymentsRequestOrderAsc.Ptr(),
			Next:      cursor,
		})
		if err != nil {
			return nil, err
		}

		paginated := page.GetPaginatedDividendPaymentResponse()
		results = append(results, paginated.Data...)
		cursor = paginated.PaginationMetadata.Next
		if cursor == nil {
			return results, nil
		}
	}
}
```

```
static List<DividendPayment> allDividendPayments(DinariClient client, String accountId, String startDate, String endDate) {
    List<DividendPayment> results = new ArrayList<>();
    Optional<String> cursor = Optional.empty();

    do {
        var page = (PaginatedDividendPaymentResponse) client.accounts().getAccountDividendPayments(
                accountId,
                GetAccountDividendPaymentsRequest.builder()
                        .startDate(startDate)
                        .endDate(endDate)
                        .limit(20)
                        .order(GetAccountDividendPaymentsRequestOrder.ASC)
                        .next(cursor)
                        .build()).get();

        results.addAll(page.getData());
        cursor = page.getPaginationMetadata().getNext();
    } while (cursor.isPresent());

    return results;
}
```

#### Confirm the cash balance moved

dShare holders are paid in USD+. Reading the cash balance closes the loop and catches a payment record with no matching on-chain credit.

TypeScriptPythonGoJava

```
const cash = await client.accounts.getAccountCash({ accountId });

for (const c of cash) {
  console.log(`${c.symbol}: ${c.amount}`);
}
```

```
cash = client.accounts.get_account_cash(account_id=ACCOUNT_ID)

for c in cash:
    print(f"{c.symbol}: {c.amount}")
```

```
cash, err := c.Accounts.GetAccountCash(ctx, &dinari.GetAccountCashRequest{AccountID: accountID})
if err != nil {
	log.Fatalf("Failed to get cash: %v", err)
}

for _, b := range cash {
	fmt.Printf("%s: %s\n", b.Symbol, b.Amount)
}
```

```
var cash = client.accounts().getAccountCash(accountId);

for (PaymentTokenBalance c : cash) {
    System.out.println(c.getSymbol() + ": " + c.getAmount());
}
```

> ⚠️
>
> ### Wrapped dShare holders will see no cash movement
>
> Wrapped holders receive the underlying dShare deposited into the wrapped position rather than a USD+ credit. Check the portfolio, not the cash balance, for those accounts.

## Complete reference script

This is the complete, uninterrupted script for checking eligibility and reconciling a dividend:

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment, DinariError } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

const accountId = "your-account-id";
const entityId = "your-entity-id";
const stockId = "stock-id-here";

function addDays(isoDate: string, days: number): string {
  const d = new Date(isoDate);
  d.setDate(d.getDate() + days);
  return d.toISOString().slice(0, 10);
}

async function main() {
  // --- Step 1: Find the dividend ---
  const dividends = await client.corporateActions.getStockDividendsByStockId({ stockId });
  const today = new Date().toISOString().slice(0, 10);

  const next = dividends
    .filter((d) => d.exDividendDate != null && d.exDividendDate >= today)
    .sort((a, b) => a.exDividendDate!.localeCompare(b.exDividendDate!))[0];

  if (!next) {
    console.log("No upcoming dividend announced for this stock.");
    return;
  }

  console.log(
    `Next dividend: ${next.cashAmount} ${next.currency} per share, ` +
    `ex-date ${next.exDividendDate}, pays ${next.payDate}`
  );

  // --- Step 2: Check eligibility, before 4:00 AM ET on the ex-date ---
  const portfolio = await client.accounts.getAccountPortfolio({ accountId });
  const totalHeld = portfolio.assets
    .filter((b) => b.stockId === stockId)
    .reduce((sum, b) => sum + Number(b.amount), 0);

  const reasons: string[] = [];

  if (totalHeld === 0) {
    reasons.push("no dShares held for this stock");
  }

  const estimated = totalHeld * Number(next.cashAmount);
  if (estimated > 0 && estimated < 0.1) {
    reasons.push(`estimated entitlement ${estimated.toFixed(4)} is below the $0.10 minimum`);
  }

  try {
    await client.wallets.getWallet({ accountId });
  } catch (e) {
    if (e instanceof DinariError && e.statusCode === 404) {
      reasons.push("no wallet connected to the account");
    } else {
      throw e;
    }
  }

  const kyc = await client.kyc.getEntityKyc({ entityId });
  if (kyc.status !== "PASS") {
    reasons.push(`entity KYC status is ${kyc.status}`);
  }

  if (reasons.length) {
    console.log(`Not eligible: ${reasons.join("; ")}`);
  } else {
    console.log(`Eligible. Estimated entitlement: ${estimated.toFixed(4)} ${next.currency}`);
  }

  // --- Step 3: Reconcile, after the pay date ---
  const payDate = next.payDate!;
  const payments = [];
  let cursor: string | undefined = undefined;

  do {
    const page = await client.accounts.getAccountDividendPayments({
      accountId,
      startDate: payDate,
      endDate: addDays(payDate, 7),
      stockId,
      limit: 20,
      order: "asc",
      next: cursor,
    });

    if (Array.isArray(page)) {
      payments.push(...page);
      break;
    }
    payments.push(...page.data);
    cursor = page.paginationMetadata.next;
  } while (cursor);

  for (const p of payments) {
    console.log(`Paid ${p.amount} ${p.currency} on ${p.paymentDate}`);
  }

  // Close the loop against the on-chain cash balance.
  const cash = await client.accounts.getAccountCash({ accountId });
  console.log("Cash balances:", cash);
}

main();
```

```
import os
from datetime import date, timedelta

from dinari_api_sdk import DinariClient
from dinari_api_sdk.core.api_error import ApiError
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

ACCOUNT_ID = "your-account-id"  # Replace with the actual Account ID
ENTITY_ID = "your-entity-id"    # Replace with the actual Entity ID
STOCK_ID = "stock-id-here"      # Replace with the actual Stock ID

# --- Step 1: Find the dividend ---
dividends = client.corporate_actions.get_stock_dividends_by_stock_id(stock_id=STOCK_ID)
today = date.today()

upcoming = sorted(
    (d for d in dividends if d.ex_dividend_date is not None and d.ex_dividend_date >= today),
    key=lambda d: d.ex_dividend_date,
)

if not upcoming:
    print("No upcoming dividend announced for this stock.")
    raise SystemExit

next_dividend = upcoming[0]
print(f"Next dividend: {next_dividend.cash_amount} {next_dividend.currency} "
      f"per share, ex-date {next_dividend.ex_dividend_date}, "
      f"pays {next_dividend.pay_date}")

# --- Step 2: Check eligibility, before 4:00 AM ET on the ex-date ---
portfolio = client.accounts.get_account_portfolio(account_id=ACCOUNT_ID)
total_held = sum(
    float(b.amount) for b in portfolio.assets if b.stock_id == STOCK_ID
)

reasons = []

if total_held == 0:
    reasons.append("no dShares held for this stock")

estimated = total_held * float(next_dividend.cash_amount)
if 0 < estimated < 0.10:
    reasons.append(f"estimated entitlement {estimated:.4f} is below the $0.10 minimum")

try:
    client.wallets.get_wallet(account_id=ACCOUNT_ID)
except ApiError as e:
    if e.status_code != 404:
        raise
    reasons.append("no wallet connected to the account")

kyc = client.kyc.get_entity_kyc(entity_id=ENTITY_ID)
if kyc.status != "PASS":
    reasons.append(f"entity KYC status is {kyc.status}")

if reasons:
    print("Not eligible: " + "; ".join(reasons))
else:
    print(f"Eligible. Estimated entitlement: {estimated:.4f} {next_dividend.currency}")

# --- Step 3: Reconcile, after the pay date ---
pay_date = next_dividend.pay_date
payments = []
cursor = None

while True:
    page = client.accounts.get_account_dividend_payments(
        account_id=ACCOUNT_ID,
        start_date=pay_date,
        end_date=pay_date + timedelta(days=7),
        stock_id=STOCK_ID,
        limit=20,
        order="asc",
        next=cursor,
    )

    payments.extend(page.data)
    cursor = page.pagination_metadata.next
    if not cursor:
        break

for p in payments:
    print(f"Paid {p.amount} {p.currency} on {p.payment_date}")

# Close the loop against the on-chain cash balance.
cash = client.accounts.get_account_cash(account_id=ACCOUNT_ID)
print("Cash balances:", cash)
```

```
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	core "github.com/dinaricrypto/dinari-api-sdk-go/core"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

// str dereferences an optional string field.
func str(s *string) string {
	if s == nil {
		return ""
	}
	return *s
}

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)
	ctx := context.Background()

	accountID := "your-account-id"
	entityID := "your-entity-id"
	stockID := "stock-id-here"

	// --- Step 1: Find the dividend ---
	dividends, err := c.CorporateActions.GetStockDividendsByStockID(ctx, &dinari.GetStockDividendsByStockIDRequest{
		StockID: stockID,
	})
	if err != nil {
		log.Fatalf("Failed to get dividends: %v", err)
	}
	today := time.Now().UTC().Truncate(24 * time.Hour)

	var next *dinari.StockDividendAnnouncementDetail
	for _, d := range dividends {
		if d.ExDividendDate == nil || d.ExDividendDate.Before(today) {
			continue
		}
		if next == nil || d.ExDividendDate.Before(*next.ExDividendDate) {
			next = d
		}
	}

	if next == nil {
		fmt.Println("No upcoming dividend announced for this stock.")
		return
	}

	fmt.Printf("Next dividend: %s %s per share, ex-date %s, pays %s\n",
		str(next.CashAmount), str(next.Currency),
		next.ExDividendDate.Format("2006-01-02"), next.PayDate.Format("2006-01-02"))

	// --- Step 2: Check eligibility, before 4:00 AM ET on the ex-date ---
	portfolio, err := c.Accounts.GetAccountPortfolio(ctx, &dinari.GetAccountPortfolioRequest{AccountID: accountID})
	if err != nil {
		log.Fatalf("Failed to get portfolio: %v", err)
	}

	totalHeld := 0.0
	for _, b := range portfolio.Assets {
		if b.StockID == stockID {
			amount, _ := strconv.ParseFloat(b.Amount, 64)
			totalHeld += amount
		}
	}

	var reasons []string

	if totalHeld == 0 {
		reasons = append(reasons, "no dShares held for this stock")
	}

	cashAmount, _ := strconv.ParseFloat(str(next.CashAmount), 64)
	estimated := totalHeld * cashAmount
	if estimated > 0 && estimated < 0.10 {
		reasons = append(reasons, fmt.Sprintf("estimated entitlement %.4f is below the $0.10 minimum", estimated))
	}

	if _, err := c.Wallets.GetWallet(ctx, &dinari.GetWalletRequest{AccountID: accountID}); err != nil {
		var apiErr *core.APIError
		if !errors.As(err, &apiErr) || apiErr.StatusCode != 404 {
			log.Fatalf("Failed to get wallet: %v", err)
		}
		reasons = append(reasons, "no wallet connected to the account")
	}

	kyc, err := c.Kyc.GetEntityKyc(ctx, &dinari.GetEntityKycRequest{EntityID: entityID})
	if err != nil {
		log.Fatalf("Failed to get KYC: %v", err)
	}
	var kycStatus dinari.KycStatus
	if k := kyc.GetBaseline(); k != nil {
		kycStatus = k.Status
	} else if k := kyc.GetUs(); k != nil {
		kycStatus = k.Status
	}
	if kycStatus != dinari.KycStatusPass {
		reasons = append(reasons, fmt.Sprintf("entity KYC status is %s", kycStatus))
	}

	if len(reasons) > 0 {
		fmt.Printf("Not eligible: %v\n", reasons)
	} else {
		fmt.Printf("Eligible. Estimated entitlement: %.4f %s\n", estimated, str(next.Currency))
	}

	// --- Step 3: Reconcile, after the pay date ---
	var payments []*dinari.DividendPayment
	var cursor *string

	for {
		page, err := c.Accounts.GetAccountDividendPayments(ctx, &dinari.GetAccountDividendPaymentsRequest{
			AccountID: accountID,
			StartDate: *next.PayDate,
			EndDate:   next.PayDate.AddDate(0, 0, 7),
			StockID:   dinari.String(stockID),
			Limit:     dinari.Int(20),
			Order:     dinari.GetAccountDividendPaymentsRequestOrderAsc.Ptr(),
			Next:      cursor,
		})
		if err != nil {
			log.Fatalf("Failed to get dividend payments: %v", err)
		}

		paginated := page.GetPaginatedDividendPaymentResponse()
		payments = append(payments, paginated.Data...)
		cursor = paginated.PaginationMetadata.Next
		if cursor == nil {
			break
		}
	}

	for _, p := range payments {
		fmt.Printf("Paid %s %s on %s\n", p.Amount, p.Currency, p.PaymentDate.Format("2006-01-02"))
	}

	// Close the loop against the on-chain cash balance.
	cash, err := c.Accounts.GetAccountCash(ctx, &dinari.GetAccountCashRequest{AccountID: accountID})
	if err != nil {
		log.Fatalf("Failed to get cash: %v", err)
	}
	fmt.Printf("Cash balances: %+v\n", cash)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.DinariClientApiException;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.accounts.requests.GetAccountDividendPaymentsRequest;
import com.dinari.api.resources.accounts.types.GetAccountDividendPaymentsRequestOrder;
import com.dinari.api.types.BaselineKyc;
import com.dinari.api.types.DividendPayment;
import com.dinari.api.types.KycStatus;
import com.dinari.api.types.PaginatedDividendPaymentResponse;
import com.dinari.api.types.StockDividendAnnouncementDetail;
import com.dinari.api.types.UsKyc;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String entityId = "your-entity-id";
        String stockId = "stock-id-here";

        // --- Step 1: Find the dividend ---
        var dividends = client.corporateActions().getStockDividendsByStockId(stockId);
        String today = LocalDate.now().toString();

        StockDividendAnnouncementDetail next = dividends.stream()
                .filter(d -> d.getExDividendDate().isPresent() && d.getExDividendDate().get().compareTo(today) >= 0)
                .min(Comparator.comparing(d -> d.getExDividendDate().get()))
                .orElse(null);

        if (next == null) {
            System.out.println("No upcoming dividend announced for this stock.");
            return;
        }

        System.out.println("Next dividend: " + next.getCashAmount().orElse("") + " " + next.getCurrency().orElse("")
                + " per share, ex-date " + next.getExDividendDate().orElse("") + ", pays " + next.getPayDate().orElse(""));

        // --- Step 2: Check eligibility, before 4:00 AM ET on the ex-date ---
        var portfolio = client.accounts().getAccountPortfolio(accountId);
        double totalHeld = portfolio.getAssets().stream()
                .filter(b -> b.getStockId().equals(stockId))
                .mapToDouble(b -> Double.parseDouble(b.getAmount()))
                .sum();

        List<String> reasons = new ArrayList<>();

        if (totalHeld == 0) {
            reasons.add("no dShares held for this stock");
        }

        double estimated = totalHeld * Double.parseDouble(next.getCashAmount().orElse("0"));
        if (estimated > 0 && estimated < 0.10) {
            reasons.add(String.format("estimated entitlement %.4f is below the $0.10 minimum", estimated));
        }

        try {
            client.wallets().getWallet(accountId);
        } catch (DinariClientApiException e) {
            if (e.statusCode() != 404) {
                throw e;
            }
            reasons.add("no wallet connected to the account");
        }

        var kyc = client.kyc().getEntityKyc(entityId);
        KycStatus kycStatus = kyc.getBaseline().map(BaselineKyc::getStatus)
                .or(() -> kyc.getUs().map(UsKyc::getStatus))
                .orElseThrow();
        if (!KycStatus.PASS.equals(kycStatus)) {
            reasons.add("entity KYC status is " + kycStatus);
        }

        if (!reasons.isEmpty()) {
            System.out.println("Not eligible: " + String.join("; ", reasons));
        } else {
            System.out.printf("Eligible. Estimated entitlement: %.4f %s%n", estimated, next.getCurrency().orElse(""));
        }

        // --- Step 3: Reconcile, after the pay date ---
        LocalDate payDate = LocalDate.parse(next.getPayDate().orElseThrow());
        List<DividendPayment> payments = new ArrayList<>();
        Optional<String> cursor = Optional.empty();

        do {
            var page = (PaginatedDividendPaymentResponse) client.accounts().getAccountDividendPayments(
                    accountId,
                    GetAccountDividendPaymentsRequest.builder()
                            .startDate(payDate.toString())
                            .endDate(payDate.plusDays(7).toString())
                            .stockId(stockId)
                            .limit(20)
                            .order(GetAccountDividendPaymentsRequestOrder.ASC)
                            .next(cursor)
                            .build()).get();

            payments.addAll(page.getData());
            cursor = page.getPaginationMetadata().getNext();
        } while (cursor.isPresent());

        for (DividendPayment p : payments) {
            System.out.println("Paid " + p.getAmount() + " " + p.getCurrency() + " on " + p.getPaymentDate());
        }

        // Close the loop against the on-chain cash balance.
        var cash = client.accounts().getAccountCash(accountId);
        System.out.println("Cash balances: " + cash);
    }
}
```

Updated 6 days ago

---

[Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)[Stock Splits](https://docs.dinari.com/docs/stock-split-handling)

Did this page help you?

Yes

No

Copy Page

* + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + - [How it works at Dinari](https://docs.dinari.com/docs/dividend-payments)
    - * [Qualification](https://docs.dinari.com/docs/dividend-payments)
      * [Distribution](https://docs.dinari.com/docs/dividend-payments)
      * [Supported chains](https://docs.dinari.com/docs/dividend-payments)
      * [Dividend types](https://docs.dinari.com/docs/dividend-payments)
    - [Integration guide to dividends](https://docs.dinari.com/docs/dividend-payments)
    - * [Step 1: Find the dividend](https://docs.dinari.com/docs/dividend-payments)
      * [Step 2: Check eligibility](https://docs.dinari.com/docs/dividend-payments)
      * [Step 3: Reconcile the payment](https://docs.dinari.com/docs/dividend-payments)
    - [Complete reference script](https://docs.dinari.com/docs/dividend-payments)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Dividends","dateModified":"2026-11-10T03:21:35.000Z"}
```