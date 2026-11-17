> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Moving money and exchanging assets

> Choose an operation by its source, destination, and exchange behavior.

Moving funds and exchanging assets are separate actions. Choose the operation that matches both your source and your intended destination.

| Operation | What it does |
| - | - |
| Deposit or withdrawal | Moves funds into or out of a Payward account |
| Transfer | Moves the same asset between Payward accounts in your integration's program |
| Swap | Exchanges assets through a quote that you request and execute |
| Conversion | Combines asset exchange with movement between supported balance, bank, or wallet sources and destinations |
| Hosted purchase | Collects payment and delivers crypto through the hosted checkout documented under Ramp |

The [Create transfer](https://docs.services.payward.com/api-reference/funds/create-transfer.md) API operation moves funds between Payward accounts. Both accounts must be in your integration's account group, called a **program**. They can belong to different users, such as a business and its supplier. A Payward account in another program isn't an eligible destination.

An external bank account or wallet isn't a destination for this operation, even if its owner has a Payward account in your program.

## Conversion rule vs. conversion transaction

A **conversion rule** defines how incoming deposits are converted. While active, it automatically starts a separate **conversion transaction** for each matching deposit. An **on-demand conversion** executes once without creating a rule.

For a conversion rule, the destination bank account must match the account's verified identity. Third-party bank payouts aren't supported.

See [Conversions](https://docs.services.payward.com/tabs/developer-documentation/payments/conversion-rules.md) for the supported source and destination combinations.

## Market price vs. executable quote

A market price supports display and valuation. An executable quote offers terms for a particular trade and expires. Creating the quote doesn't execute the trade.

For a swap, fix either the source amount you spend or the destination amount you receive. The API calculates the other side. Check the returned amounts, fees, and expiration before execution. See [Swaps](https://docs.services.payward.com/tabs/developer-documentation/trade/swap.md).

## Account-funded vs. wallet-funded

An account-funded trade uses the Payward account balance. The documented on-chain swap uses an approved external wallet and requires a blockchain transaction. Its [`account_id`](https://docs.services.payward.com/tabs/concepts/users-and-accounts#user-vs-account) identifies the Payward account associated with the trade. The wallet's owner must match that account's verified identity.

See [On-chain swaps](https://docs.services.payward.com/tabs/developer-documentation/trade/onchain-quotes.md) for supported assets, networks, and execution requirements.
