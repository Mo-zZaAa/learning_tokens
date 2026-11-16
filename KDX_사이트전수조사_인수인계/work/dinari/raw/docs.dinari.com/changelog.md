---
url: https://docs.dinari.com/changelog
title: Changelog
description: 
fetched: 2026-11-16
method: render
plan: read
---

4 months ago

[# v20260709-097f56a](https://docs.dinari.com/changelog/v20260709-097f56a)

### Changed

* `jurisdiction` (`US`) can now be specified as a parameter for **post** /api/v2/entities/{entity\_id}/kyc/url to enable partners to leverage managed US KYC workflows

5 months ago

[# v20260617-68ffb6a](https://docs.dinari.com/changelog/v20260617-68ffb6a)

### Changed

* `payment_token_address` can now be specified for Market Buy and Limit Buy on Managed Orders to opt out of default USD+ as payment token
* Cancel API now returns more meaningful status codes and error messages
* Latest SDK versions now serve API responses using cursor-based pagination

### Added

* Latest SDK versions now support HyperEVM and Avalanche C-Chain for orders

7 months ago

[# v20260417-cdbbd85](https://docs.dinari.com/changelog/v20260417-cdbbd85)

### Changed

This release introduces cursor-based pagination and an object return for paginated endpoints for the following endpoints:

* **get** /api/v2/market\_data/stocks/
* **get** /api/v2/market\_data/stocks/splits
* **get** /api/v2/market\_data/stocks/{stock\_id}/splits
* **get** /api/v2/entities/
* **get** /api/v2/entities/{entity\_id}/accounts
* **get** /api/v2/accounts/{account\_id}/interest\_payments
* **get** /api/v2/accounts/{account\_id}]/dividend\_payments
* **get** /api/v2/accounts/{account\_id}/token\_transfers
* **get** /api/v2/orders/
* **get** /api/v2/accounts/{account\_id}/orders
* **get** /api/v2/accounts/{account\_id}/order\_fulfillments
* **get** /api/v2/accounts/{account\_id}/order\_requests
* **get** /api/v2/accounts/{account\_id}/withdrawal\_requests
* **get** /api/v2/accounts/{account\_id}/withdrawals

Page-based pagination will be deprecated on May 29, 2026. To ease transition for current users, the page-based behavior is preserved unless `limit` is set on the query parameters, which will explicitly trigger the cursor-based pagination.

Refer to the table below for the difference between both:

  

|  | Page (Previous) | Cursor (Next) |
| --- | --- | --- |
| Query Parameters | `page`, `page_size` | `limit`, `order`, `next`, `previous` |
| Endpoint Return | list | object |
| Pagination Methodology | Increment `page` | Set `next` or `previous` |

8 months ago

[# v20250323-9ce7614](https://docs.dinari.com/changelog/v20250323-9ce7614)

#### Added

* **Multi-Asset Support (Alloys)**: Updated Order and Order Request endpoints to support `alloy_id` alongside the existing `stock_id`. This is a preparatory update to support future Alloy Index Token listings, such as the S&P Digital Markets 50.

#### Changed

* **Flexible Schema Validation**: Updated response models to treat `stock_id` and `alloy_id` as optional fields. This ensures backward compatibility for current stock workflows while clearing the way for future asset types.

10 months ago

[# v20260114-9a86c2e](https://docs.dinari.com/changelog/v20260114-9a86c2e)

### Fixed

* Fixed issue with Order Processing and USD+ Redemptions

10 months ago

[# v20260113-22d5943](https://docs.dinari.com/changelog/v20260113-22d5943)

### Changed

* Internal process improvements

10 months ago

[# v20260108-e96def6](https://docs.dinari.com/changelog/v20260108-e96def6)

### Added

* Add `REJECTED` status to OrderRequestStatus to indicate if the request has been rejected
* Add `reject_message` to OrderRequest that indicates why the order request was rejected

### Fixed

* Fix issues refunding cancelled orders

10 months ago

[# v20260106-fdcfb81](https://docs.dinari.com/changelog/v20260106-fdcfb81)

### Fixed

* Bug fix to enable account creation on sandbox after Managed KYC completion

11 months ago

[# v20251229-5853698](https://docs.dinari.com/changelog/v20251229-5853698)

### Changed

* Improve support for smart contract wallets

11 months ago

[# v20251229-502a74e](https://docs.dinari.com/changelog/v20251229-502a74e)

### Changed

* Bug fixes

1 of 2