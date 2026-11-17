> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use cases

Payward Services supports two primary categories of use cases: Trade and Payments Orchestration. Each category serves different partner types and end-user needs, though many partners combine both.

Both categories can use Payward-managed verification when end users need KYC. Use [Hosted KYC](https://docs.services.payward.com/tabs/developer-documentation/verifications/hosted-kyc.md) when Payward should collect evidence in a hosted UI. [Check whether initial onboarding is complete](https://docs.services.payward.com/tabs/developer-documentation/verifications/onboarding-status.md) before requesting a quote or conversion for a new user.

## Trade

Trade use cases involve enabling end users to buy, sell, and hold digital assets. This includes spot crypto trading, stablecoin conversion, tokenized asset trading, and earn/staking products.

The trade use case is most commonly adopted by banks, brokerages, and fintechs that want to offer crypto trading within their existing product experience. Typical implementations include:

* **In-app crypto trading:** End users buy and sell crypto assets directly within the partner's mobile or web application. PWS provides onchain quote execution, CLOB execution, custody, and settlement. The partner controls the UI and branding.

* **Portfolio management:** Crypto holdings appear alongside traditional assets in the user's portfolio view. PWS provides portfolio APIs for balance, history, and performance data.

* **Recurring purchases:** Users set up automated, scheduled crypto purchases (e.g., \$100 of BTC every Monday). PWS handles scheduling and execution via the Price Trigger Swaps API.

* **Earn and staking:** Users earn yield on idle crypto holdings. PWS provides staking infrastructure and Auto Earn toggles.

* **Tokenized equities:** Users trade tokenized versions of traditional stocks (xStocks) alongside crypto. PWS provides atomic onchain quote execution for xStock trades.

## Payments orchestration

Payments use cases involve moving value across borders using crypto and stablecoin rails. This includes remittance, vendor payouts, merchant settlement, and treasury operations.

The payments use case is designed for companies that move money at scale and want faster, cheaper alternatives to traditional correspondent banking. Typical implementations include:

* **Cross-border remittance:** Enable P2P money transfers between individuals in different countries using stablecoin rails. Fiat on-ramp in the sender's country, stablecoin transfer, fiat off-ramp in the recipient's country.

* **Vendor/supplier payouts:** Pay international vendors and suppliers in their local currency via stablecoin-to-fiat conversion. Attach invoice references for reconciliation.

* **Merchant settlement:** Settle e-commerce transactions in stablecoins, then convert to the merchant's preferred fiat currency for bank withdrawal.

* **Contractor/gig worker payroll:** Pay international contractors in stablecoins or their local fiat currency. Faster and cheaper than SWIFT wires.

* **Treasury operations:** Corporate treasury teams use PWS to hold, convert, and transfer stablecoin balances across subsidiaries and geographies.
