# 읽기 묶음: docs.dinari.com / docs (3/5)


<<<PAGE https://docs.dinari.com/docs/dividend-payments>>>
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

<<<PAGE https://docs.dinari.com/docs/corporate-action-processing>>>
---
url: https://docs.dinari.com/docs/corporate-action-processing
title: Corporate Actions
description: This page documents what corporate actions Dinari supports, and how they are handled.
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

# Corporate Actions

This page documents what corporate actions Dinari supports, and how they are handled.

When an underlying security undergoes a change like a split, dividend, ticker update, or merger (known as a corporate action), those updates must be reflected on the dShare token and your ledger. This section outlines the corporate actions Dinari supports, how we process them, and how to handle them in your API integration.

## Supported Corporate Actions

We process corporate actions for all supported assets and automatically reflect these events on the Dinari platform. For specific details, refer to the dedicated page for each corporate action type. There you will find our handling procedures, partner integration diagrams, SDK examples, and a readiness checklist.

* [Dividends](https://docs.dinari.com/docs/dividend-payments) - Cash distributions paid to holders
* [Stock Splits](https://docs.dinari.com/docs/stock-split-handling) - Both forward and reverse splits
* [Ticker Changes](https://docs.dinari.com/docs/ticker-changes) - Symbol, Name, and CUSIP changes
* [Mergers](https://docs.dinari.com/docs/mergers) - Cash, Stock, and Mixed-consideration deals

## Monitoring for Corporate Actions

Dinari maintains numerous Market Data endpoints which provide users with news regarding corporate actions for all assets we issue. We advise all partners to regularly check these endpoints to be aware of any upcoming major events to prevent unnecessary downtime.

| What you want to know | Where to look |
| --- | --- |
| Upcoming and in-progress splits | `GET /api/v2/market_data/stocks/splits` |
| Splits for one stock | `GET /api/v2/market_data/stocks/{stock_id}/splits` |
| Announced dividends for a stock | `GET /api/v2/market_data/stocks/{stock_id}/dividends` |
| Dividends actually paid to an account | `GET /api/v2/accounts/{account_id}/dividend_payments` |
| Current positions, per chain | `GET /api/v2/accounts/{account_id}/portfolio` |

> ℹ️
>
> #### The Dinari Team will contact you directly regarding any edge cases for upcoming corporate actions. Examples include **reverse splits with fractional entitlements** or **mergers** that affect your held assets.

Updated about 1 month ago

---

[24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)[Dividends](https://docs.dinari.com/docs/dividend-payments)

Did this page help you?

Yes

No

Copy Page

* + [Supported Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Monitoring for Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Corporate Actions","dateModified":"2026-10-14T11:29:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/mergers>>>
---
url: https://docs.dinari.com/docs/mergers
title: Mergers
description: How Dinari handles cash, stock, and mixed-consideration mergers affecting dShares
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

# Mergers

How Dinari handles cash, stock, and mixed-consideration mergers affecting dShares

# Mergers

A merger combines multiple companies. For target holders, the key question is what asset they receive at closing. This payout (cash, stock, or a mix) maps directly to Dinari's event classifications.

---

## The three consideration types

The consideration, cash, acquirer stock, or a mix, is fixed by the deal terms, and it maps directly onto Dinari's classification:

| Consideration | What a holder receives |
| --- | --- |
| Cash only | A fixed cash amount per share. The target's shares are extinguished and delisted. |
| Stock only | Acquirer shares at a fixed exchange ratio, preserving market exposure. |
| Cash and stock | A combination of partial liquidity plus continued equity participation. |

---

## Which structure applies

```
flowchart TD
    A["Merger announced"] --> B{"Consideration?"}
 
    B -->|"Cash only"| C["cash_merger"]
    B -->|"Acquirer stock only"| D["stock_merger"]
    B -->|"Cash and stock"| E["stock_and_cash_merger"]
 
    C --> F{"Does Dinari<br/>hold this asset?"}
    D --> F
    E --> F
 
    F -->|"No"| G["No action.<br/>No partner impact."]
    F -->|"Yes"| H["Manual triage.<br/>Dinari contacts you directly."]
```

---

## What that means in practice

Rely on direct communication from Dinari, not the API, to confirm event outcomes, timing, and settlement assets.

***What you can rely on:***

* Dinari detects merger announcements and checks whether it holds the affected asset.
* When a held asset is affected, Dinari will coordinates the resolution and notify you.
* Position and cash changes are observable once resolved.

***What you should not assume:***

* That a merger produces an event object you can poll for.
* That a stock-for-stock merger automatically produces an acquirer dShare.
* That timing matches the deal's closing date to the hour.

---

## Recommendations for Managing Mergers Programmatically

1. **Watch for unexplained position removals.** There is no merger event endpoint, so a position disappearing from the portfolio is your programmatic signal — and your partner channel is the primary notification path.
2. **Snapshot positions before a known effective date.** A before/after diff is the only reliable reconciliation method available.
3. **Reconcile both positions and cash.** A cash merger settles as a cash entitlement; the portfolio alone shows a position vanishing with nothing in its place.

> ℹ️
>
> #### Note: There is no dedicated merger endpoint or SDK method. You detect a merger's effects by reconciling holdings and cash across the effective date.

Updated about 1 month ago

---

[Ticker Changes](https://docs.dinari.com/docs/ticker-changes)[Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)

Did this page help you?

Yes

No

Copy Page

* + [Mergers](https://docs.dinari.com/docs/mergers)
  + - [The three consideration types](https://docs.dinari.com/docs/mergers)
    - [Which structure applies](https://docs.dinari.com/docs/mergers)
    - [What that means in practice](https://docs.dinari.com/docs/mergers)
    - [Recommendations for Managing Mergers Programmatically](https://docs.dinari.com/docs/mergers)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Mergers","dateModified":"2026-10-14T11:29:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/stock-split-handling>>>
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

<<<PAGE https://docs.dinari.com/docs/ticker-changes>>>
---
url: https://docs.dinari.com/docs/ticker-changes
title: Ticker Changes
description: How Dinari handles issuer symbol, name, and CUSIP changes.
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

# Ticker Changes

How Dinari handles issuer symbol, name, and CUSIP changes.

# Ticker Changes

A ticker change, or more precisely a name change, is a rebranding event. The company changes its name, ticker symbol, and/or CUSIP, in any combination. No balances move and no cash is paid; only the identity changes.

Two things to know:

* A name change sometimes arrives alongside a reverse stock split, so both events can hit the same security in the same week.
* A CUSIP change matters even when the ticker looks identical, because the CUSIP is what follows the security through settlement.

---

## What changes at Dinari

When the symbol or CUSIP changes, Dinari swaps in new internal records for the security and updates the dShare™ token name.

| Property | Changes? |
| --- | --- |
| Share quantity held | ❌ No |
| Position value | ❌ No |
| Displayed symbol | ✅ Possibly |
| Displayed company name | ✅ Possibly |
| Underlying CUSIP | ✅ Possibly |
| Dinari `stock_id` you reference | ❌ No — Dinari maintains continuity |

### The asset goes quiet for a while

When the identifier changes, the old asset dShare is disabled and a new one is issued. Until Dinari re-points its records at the new identifier, the asset is disabled on the platform and all orders for it will be rejected.

---

## How it works, from your side

```
sequenceDiagram
    autonumber
    participant D as Dinari
    participant P as Partner
    participant U as End user
 
    Note over D: Name / symbol / CUSIP change — asset disabled
    D->>D: Verify the new asset,<br/>check for affected orders
 
    Note over D,P: Asset unavailable — orders rejected
    P->>D: Order submission
    D-->>P: Rejected — asset disabled
    P->>U: Show "temporarily unavailable"
 
    D->>D: Re-point records to the new asset,<br/>update token name, re-enable
 
    Note over D: Asset re-enabled — trading resumes
    D->>P: Confirmation of new symbol
    P->>D: Read portfolio
    D-->>P: Same amount, updated symbol<br/>and token metadata
    P->>U: Refresh mapping, display new symbol
```

Before re-enabling, Dinari validates that the asset is active again, all records reference the current asset, no orders or positions were affected, and share quantities are unchanged.

---

## Recommendations

1. **Key off** `stock_id`**, never the ticker symbol.** Treat `symbol` as a display field you refresh from the API. This is critical to ensuring that you are not impacted by ticker changes.
2. **Automatically handle rejections gracefully during the window.** Show "temporarily unavailable" rather than a raw error, and back off on retries.
3. **Refresh metadata afterwards.** Re-read the portfolio and update your cached `stock_id` → `symbol` and `token_address` mapping.
4. **Don't adjust balances.** Quantities don't move in a name change. If one did, check for a reverse split in the same window and contact your Dinari representative.

Updated about 1 month ago

---

[Stock Splits](https://docs.dinari.com/docs/stock-split-handling)[Mergers](https://docs.dinari.com/docs/mergers)

Did this page help you?

Yes

No

Copy Page

* + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + - [What changes at Dinari](https://docs.dinari.com/docs/ticker-changes)
    - * [The asset goes quiet for a while](https://docs.dinari.com/docs/ticker-changes)
    - [How it works, from your side](https://docs.dinari.com/docs/ticker-changes)
    - [Recommendations](https://docs.dinari.com/docs/ticker-changes)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Ticker Changes","dateModified":"2026-10-14T11:29:11.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api>>>
---
url: https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api
title: Order Fulfillment Amounts in the Orders API
description: Overview When querying order details via the Orders API endpoints, the returned asset_token_quantity and payment_token_quantity fields represent the placed order quantities , not the actual fulfilled amounts. This is a common point of confusion for integrators. 💡Reference: Get Order Fulfillments Th…
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

# Order Fulfillment Amounts in the Orders API

## Overview

When querying order details via the Orders API endpoints, the returned asset\_token\_quantity and payment\_token\_quantity fields represent the **placed order quantities**, not the actual fulfilled amounts. This is a common point of confusion for integrators.

**💡Reference:** [**Get Order Fulfillments**](https://docs.dinari.com/reference/getaccountorderfulfillments)

---

## The Issue

The asset\_token\_quantity and payment\_token\_quantity fields in the **Orders API** responses reflect the amount the user initially requested at order placement. They do **not** reflect:

* Partial fills
* Final settled amounts
* Adjustments due to market price changes or slippage

Relying on these fields for reconciliation, settlement tracking, or balance updates will lead to inaccuracies.

---

## The Correct Approach

To obtain the **actual fulfillment amounts** for an order, we must query the **Order Fulfillments API** endpoints.

### ⚠️ Important Notes:

* Each order can have **multiple fulfillments** (e.g., partial fills over time).
* The sum of all fulfillments for a given order equals the total settled amount.
* Fulfillment records contain precise, finalized quantities for both the asset and the payment token.

---

## Best Practices

1. **Do not** use `asset_token_quantity` or `payment_token_quantity` from the Orders API for:

* Updating user balances
* Calculating fees
* Confirming order completion

2. **Always** fetch fulfillment records for an order to:

* Determine the net settled quantity
* Handle partial fills correctly
* Reconcile transactions with external systems

3. **Iterate** over all fulfillments associated with an order ID, as a single order may have one or more entries.

---

## Additional Context

| **API** | **Purpose** | **Fields to Use** |
| --- | --- | --- |
| **Orders API** | Order placement and high-level status | For order creation confirmation only |
| **Order Fulfillments API** | Settlement and execution details | For actual transferred amounts |

---

## Related Questions

* Q: Why would an order have multiple fulfillments?  
  A: Due to liquidity fragmentation, market depth, or execution over time, a single limit or market order may be filled across several distinct trades.
* Q: Should I sum all fulfillments to get the total?  
  A: Yes. The sum of all fulfillment amounts equals the final settled quantity for that order.

Updated about 1 month ago

---

[Order Types & Behaviors](https://docs.dinari.com/docs/order-type)[Stock Data](https://docs.dinari.com/docs/stock-data)

Did this page help you?

Yes

No

Copy Page

* + [Overview](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [The Issue](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [The Correct Approach](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + - [⚠️ Important Notes:](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Best Practices](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Additional Context](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
  + [Related Questions](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Order Fulfillment Amounts in the Orders API","dateModified":"2026-10-14T11:28:42.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/order-type>>>
---
url: https://docs.dinari.com/docs/order-type
title: Order Types & Behaviors
description: Market and limit order types across Dinari's order-placement APIs, including required fields, pricing logic, and order controls.
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

# Order Types & Behaviors

Market and limit order types across Dinari's order-placement APIs, including required fields, pricing logic, and order controls.

Dinari abstracts most market-structure complexity behind a single set of order-placement APIs. This page explains the order types Dinari supports, the fields each requires, and how order type affects pricing and order controls.

## Order Types

| `order_type` | Behavior |
| --- | --- |
| `MARKET` | Executes at the prevailing market price.1 |
| `LIMIT` | Executes only at the specified `limit_price` or better. |

* 1 Market order behavior may change depending on the available trading sessions. See [Marketable Limit](https://docs.dinari.com/docs/order-type) documentation for additional information.

> ℹ️
>
> ### Stop, stop-limit, trailing order types are not supported at this time.

`order_side` is either `BUY` or `SELL`.

## Order Placement

The method of placing an order depends primarily on the wallet type.

| Method | Wallet type | Description | Endpoint(s) |
| --- | --- | --- | --- |
| **Managed Orders** | Dinari-managed wallet | Dinari places the order on your behalf. | `POST /api/v2/accounts/{account_id}/order_requests/{market_buy | market_sell | limit_buy | limit_sell}` |
| **Order Request (EIP-155)** | Self-custodied wallet | Generate a permit, sign it, then either submit it on-chain yourself or have Dinari submit it for you. | `POST /api/v2/accounts/{account_id}/order_requests/eip155/permit` `POST /api/v2/accounts/{account_id}/order_requests/eip155/submit` |

Every order flows through the same v2 `OrderRequest` → `Order` model. An `OrderRequest` must be created first, which is submitted on-chain to create an `Order`.

```
flowchart LR
  ManagedWallet --> OrderRequest
  SelfWallet[Self-custodied wallet] --> OrderRequestEIP155
  OrderRequest -- auto submitted--> Blockchain
  OrderRequestEIP155 -- Dinari sponsored<br/>eip155/submit --> Blockchain
  OrderRequestEIP155 -- self-sponsored submission --> Blockchain
  Blockchain --> Order
```

Go to [Placing Orders](https://docs.dinari.com/docs/placing-dshare-orders) for more detail on placing orders.

### Required fields by order type

| **Order Type** | **Required Fields** | **Precision** |
| --- | --- | --- |
| Market buy | `payment_amount` (USD notional) | ≤ 2 decimals |
| Market sell | `asset_quantity` | ≤ 6 decimals |
| Limit buy / sell | `asset_quantity` + `limit_price` | quantity ≤ 4 decimals, price ≤ 2 decimals |

## Order Behavior

While the order interface is simple, it's important to understand the behavior of each `order_type` which is dependent primarily on the available trading sessions when the order was submitted.

| Trading Session1 *(times in ET)* | Hours | Availability | `order_type` | Behavior |
| --- | --- | --- | --- | --- |
| **Regular** | Weekdays *9:30a-4:00pm* | All tickers, high liquidity. | `market` | Market |
| `limit` | Limit |
| **Extended** | Weekdays *4:00am-9:30am* *4:00pm-8:00pm* | Most tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |
| **Overnight** | Weekdays2 *8:00pm(T-1)-4:00am* | Most tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |
| **Open (24/7)** | *All other times.3* | Limited tickers, low liquidity. | `market` | Marketable limit |
| `limit` | Limit |

* 1 See [Trading Hours](https://docs.dinari.com/docs/trading-hours) for more detailed information.
* 2 From 8:00pm the previous day to 4:00am of days with a regular trading session. See [Trading Hours](https://docs.dinari.com/docs/trading-hours) for more detailed information.
* 3 The Open (24/7) trading session is open when other trading sessions are closed for limited tickers. This includes weekends and holidays.

### Marketable Limit Orders

When a market order cannot be routed as a plain market instruction — primarily outside regular U.S. market hours — Dinari converts it into a **marketable limit** order to attempt to fill the order at the best available price similar to true market orders.

* **Buys** are priced at the latest **ASK**.
* **Sells** are priced at the latest **BID**.

Because the result is a limit order, it may fill fully, partially, or not at all. Any unfilled remainder is refunded.

### Non-fractionable Assets

Market buy orders placed for non-fractional assets in all trading sessions are treated similarly and converted to marketable limit orders. In the background, Dinari calculates the maximum number of shares that can be bought before placing a quantity order.

After the order is filled or cancelled, the remainder is refunded.

## Time in Force

The order Time in Force determines how long an order remains eligible for execution.

### Supported values

| `order_tif` | Meaning |
| --- | --- |
| `DAY` (default) | Active until the next end of extended trading hours.1 |
| `GTC` | Good 'til cancelled (up to 90 days). |
| `IOC` | Immediate or cancel. Fills what it can immediately, then cancels any remainder; partial fills allowed. |
| `FOK` | Fill or kill. Must fill in full immediately or the entire order is cancelled; no partial fills. |

* 1 Note: `DAY` orders placed on the weekend will be valid until the next end of extended trading hours (i.e. 8:00pm ET on Monday)

## Guidance For Partners

* **Outside regular hours, submit limit orders with an explicit** `limit_price`**.** This is the most predictable path.
* **Expect partial fills and refunds** when placing market orders outside of the Regular Trading Session. Reconcile against `Order` status and the associated `OrderFulfillment` records rather than assuming a single terminal fill.
* **A weekend order shown as** `PENDING``SUBMITTED` **is usually correct, not stuck.** It may be resting on the Dinari order book or waiting to re-route to the broker when the weekend session ends.

Updated about 1 month ago

---

[Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)[Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)

Did this page help you?

Yes

No

Copy Page

* + [Order Types](https://docs.dinari.com/docs/order-type)
  + [Order Placement](https://docs.dinari.com/docs/order-type)
  + - [Required fields by order type](https://docs.dinari.com/docs/order-type)
  + [Order Behavior](https://docs.dinari.com/docs/order-type)
  + - [Marketable Limit Orders](https://docs.dinari.com/docs/order-type)
    - [Non-fractionable Assets](https://docs.dinari.com/docs/order-type)
  + [Time in Force](https://docs.dinari.com/docs/order-type)
  + - [Supported values](https://docs.dinari.com/docs/order-type)
  + [Guidance For Partners](https://docs.dinari.com/docs/order-type)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Order Types & Behaviors","dateModified":"2026-10-14T11:28:42.000Z"}
```