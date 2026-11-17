> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transaction lifecycles and settlement

> Understand what a response or status proves about an operation.

API requests, saved resources such as [conversion rules](https://docs.services.payward.com/tabs/concepts/money-movement.md#conversion-rule-vs-conversion-transaction), and transactions each have their own lifecycle. Their statuses describe different parts of the process.

## Request accepted vs. operation completed

Payward can accept an API request before finishing the work it starts. For example, when you request execution of a swap quote, the quote's `status` field changes to `executing`, meaning the trade is in progress. It changes to `executed` after the trade settles.

Read the operation's documented status before showing success. An HTTP success response alone may only confirm acceptance.

## Active rule vs. completed transaction

A conversion rule with a `status` of `active` is ready to process matching deposits. It doesn't mean a deposit arrived or a conversion completed. Each resulting transaction has its own progress and outcome.

See [rule lifecycle](https://docs.services.payward.com/tabs/developer-documentation/payments/conversion-rules.md#rule-lifecycle) and [conversion transactions](https://docs.services.payward.com/tabs/developer-documentation/payments/conversion-rules.md#monitoring-conversions).

## Execution vs. settlement

**Execution** performs the trade. **Settlement** completes the associated movement of assets. For a conversion transaction, the `settling` status means the conversion has occurred but delivery to the destination is still in progress.

Status names and completion conditions vary by operation. Swaps can exchange crypto for crypto or trade between crypto and fiat. A completed swap means the trade has settled. Any later withdrawal or transfer is a separate operation with its own status. See [Swaps](https://docs.services.payward.com/tabs/developer-documentation/trade/swap.md#quote-lifecycle).

## Operation status vs. account history

An operation can complete before its transaction appears in [Portfolio](https://docs.services.payward.com/tabs/developer-documentation/accounts/portfolio.md). For transfers, a `status` value of `complete` in the create response doesn't guarantee immediate visibility in account history. The transfer ID and Portfolio transaction ID are different identifiers.

Use the documented status and matching fields to determine the outcome. See [Transfer reconciliation](https://docs.services.payward.com/tabs/developer-documentation/payments/transfers.md#reconcile-through-portfolio).
