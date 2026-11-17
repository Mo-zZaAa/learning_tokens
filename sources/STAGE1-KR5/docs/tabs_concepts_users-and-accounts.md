> ## Documentation Index
> Fetch the complete documentation index at: https://docs.services.payward.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users, accounts, and ownership

> Identify the user and account involved in an operation.

When building the integration that connects your organization to Payward Services, **user** and **account** name resources in the API.

## User vs. account

A **user** is the API resource associated with one or more Payward accounts. In a client-facing integration, it represents a client. An **account** holds that user's balances and activity. A new user starts with one account; you can create additional accounts for the same user.

| Identifier | What it identifies |
| - | - |
| `external_reference` | Your reference for the user in your own system |
| `user_id` | The Payward user |
| `account_id` | A specific account associated with that user |

Within the [Get user](https://docs.services.payward.com/api-reference/users/get-user.md) response's `data` object, `id` is the user ID and `accounts[].id` contains the account IDs. Use an *account* ID for account-scoped calls; a user ID isn't interchangeable with it.

## Payward account vs. bank account or wallet

A Payward account is separate from an external bank account or blockchain wallet. An API request can identify a Payward account while using funds from an external wallet, as [on-chain swaps](https://docs.services.payward.com/tabs/developer-documentation/trade/onchain-quotes.md) do.

With [Bank links](https://docs.services.payward.com/tabs/developer-documentation/payments/bank-links.md), a `bank_link_id` identifies a connection to a bank. An `account_link_id` identifies one bank account shared through that connection. Neither is a Payward `account_id`.

## Account scope vs. ownership checks

Your credentials authenticate your integration. The user or account ID selects the resource the request acts on. The operation still has its own ownership and permission requirements; knowing an ID doesn't grant access.

See [Verification, permissions, and eligibility](https://docs.services.payward.com/tabs/concepts/verification-and-eligibility.md).
