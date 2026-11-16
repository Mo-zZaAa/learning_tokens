# 읽기 묶음: docs.dinari.com / changelog (1/1)


<<<PAGE https://docs.dinari.com/changelog>>>
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

<<<PAGE https://docs.dinari.com/changelog/v20250323-9ce7614>>>
---
url: https://docs.dinari.com/changelog/v20250323-9ce7614
title: v20250323-9ce7614
description: Added Multi-Asset Support (Alloys) : Updated Order and Order Request endpoints to support alloy_id alongside the existing stock_id . This is a preparatory update to support future Alloy Index Token listings, such as the S&P Digital Markets 50. Changed Flexible Schema Validation : Updated response mo…
fetched: 2026-11-16
method: static
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20250323-9ce7614

8 months ago

#### Added

* **Multi-Asset Support (Alloys)**: Updated Order and Order Request endpoints to support `alloy_id` alongside the existing `stock_id`. This is a preparatory update to support future Alloy Index Token listings, such as the S&P Digital Markets 50.

#### Changed

* **Flexible Schema Validation**: Updated response models to treat `stock_id` and `alloy_id` as optional fields. This ensures backward compatibility for current stock workflows while clearing the way for future asset types.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20250323-9ce7614","dateModified":"2026-09-02T16:51:14.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251218-161c362>>>
---
url: https://docs.dinari.com/changelog/v20251218-161c362
title: v20251218-161c362
description: Changed
Update internal infrastructure and processes to address operational reliability
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251218-161c362

11 months ago

### Changed

* Update internal infrastructure and processes to address operational reliability

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251218-161c362","dateModified":"2026-09-02T16:51:08.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251222-82d808b>>>
---
url: https://docs.dinari.com/changelog/v20251222-82d808b
title: v20251222-82d808b
description: Changed Update status field description on OrderRequest and EIP155OrderRequest API schemas to provide more information about the meaning of each status Update internal error logging Update internal configurations for speed optimizations Added Add optional cancel_message field to OrderRequest and EIP…
fetched: 2026-11-16
method: static
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251222-82d808b

11 months ago

### Changed

* Update `status` field description on `OrderRequest` and `EIP155OrderRequest` API schemas to provide more information about the meaning of each status
* Update internal error logging
* Update internal configurations for speed optimizations

### Added

* Add optional `cancel_message` field to `OrderRequest` and `EIP155OrderRequest` API schemas to provide more context to reverted orders
* Add internal tests to increase test coverage
* Add automation for publishing API docs to docs.dinari.com

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251222-82d808b","dateModified":"2026-09-02T16:51:08.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251223-9385ea7>>>
---
url: https://docs.dinari.com/changelog/v20251223-9385ea7
title: v20251223-9385ea7
description: Changed
General performance and maintenance updates to improve long-term reliability and scalability.
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251223-9385ea7

11 months ago

### Changed

* General performance and maintenance updates to improve long-term reliability and scalability.

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251223-9385ea7","dateModified":"2026-09-02T16:51:09.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251223-d86787c>>>
---
url: https://docs.dinari.com/changelog/v20251223-d86787c
title: v20251223-d86787c
description: Changed
Improve order submission speed
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251223-d86787c

11 months ago

### Changed

* Improve order submission speed

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251223-d86787c","dateModified":"2026-09-02T16:51:09.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251226-63ffcf2>>>
---
url: https://docs.dinari.com/changelog/v20251226-63ffcf2
title: v20251226-63ffcf2
description: Changed
Migrate data with our third-party vendor
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251226-63ffcf2

11 months ago

### Changed

* Migrate data with our third-party vendor

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251226-63ffcf2","dateModified":"2026-09-02T16:51:10.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251229-502a74e>>>
---
url: https://docs.dinari.com/changelog/v20251229-502a74e
title: v20251229-502a74e
description: Changed
Bug fixes
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251229-502a74e

11 months ago

### Changed

* Bug fixes

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251229-502a74e","dateModified":"2026-09-02T16:51:10.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20251229-5853698>>>
---
url: https://docs.dinari.com/changelog/v20251229-5853698
title: v20251229-5853698
description: Changed
Improve support for smart contract wallets
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20251229-5853698

11 months ago

### Changed

* Improve support for smart contract wallets

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20251229-5853698","dateModified":"2026-09-02T16:51:11.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260106-fdcfb81>>>
---
url: https://docs.dinari.com/changelog/v20260106-fdcfb81
title: v20260106-fdcfb81
description: Fixed
Bug fix to enable account creation on sandbox after Managed KYC completion
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260106-fdcfb81

10 months ago

### Fixed

* Bug fix to enable account creation on sandbox after Managed KYC completion

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260106-fdcfb81","dateModified":"2026-09-02T16:51:12.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260108-e96def6>>>
---
url: https://docs.dinari.com/changelog/v20260108-e96def6
title: v20260108-e96def6
description: Added
Add REJECTED status to OrderRequestStatus to indicate if the request has been rejected Add reject_message to OrderRequest that indicates why the order request was rejected
Fixed
Fix issues refunding cancelled orders
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260108-e96def6

10 months ago

### Added

* Add `REJECTED` status to OrderRequestStatus to indicate if the request has been rejected
* Add `reject_message` to OrderRequest that indicates why the order request was rejected

### Fixed

* Fix issues refunding cancelled orders

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260108-e96def6","dateModified":"2026-09-02T16:51:12.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260113-22d5943>>>
---
url: https://docs.dinari.com/changelog/v20260113-22d5943
title: v20260113-22d5943
description: Changed
Internal process improvements
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260113-22d5943

10 months ago

### Changed

* Internal process improvements

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260113-22d5943","dateModified":"2026-09-02T16:51:13.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260114-9a86c2e>>>
---
url: https://docs.dinari.com/changelog/v20260114-9a86c2e
title: v20260114-9a86c2e
description: Fixed
Fixed issue with Order Processing and USD+ Redemptions
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260114-9a86c2e

10 months ago

### Fixed

* Fixed issue with Order Processing and USD+ Redemptions

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260114-9a86c2e","dateModified":"2026-09-02T16:51:13.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260417-cdbbd85>>>
---
url: https://docs.dinari.com/changelog/v20260417-cdbbd85
title: v20260417-cdbbd85
description: Changed This release introduces cursor-based pagination and an object return for paginated endpoints for the following endpoints: get /api/v2/market_data/stocks/ get /api/v2/market_data/stocks/splits get /api/v2/market_data/stocks/{stock_id}/splits get /api/v2/entities/ get /api/v2/entities/{entity_…
fetched: 2026-11-16
method: static
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260417-cdbbd85

7 months ago

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

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260417-cdbbd85","dateModified":"2026-09-02T16:51:14.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260617-68ffb6a>>>
---
url: https://docs.dinari.com/changelog/v20260617-68ffb6a
title: v20260617-68ffb6a
description: Changed payment_token_address can now be specified for Market Buy and Limit Buy on Managed Orders to opt out of default USD+ as payment token Cancel API now returns more meaningful status codes and error messages Latest SDK versions now serve API responses using cursor-based pagination Added Latest…
fetched: 2026-11-16
method: static
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260617-68ffb6a

5 months ago

### Changed

* `payment_token_address` can now be specified for Market Buy and Limit Buy on Managed Orders to opt out of default USD+ as payment token
* Cancel API now returns more meaningful status codes and error messages
* Latest SDK versions now serve API responses using cursor-based pagination

### Added

* Latest SDK versions now support HyperEVM and Avalanche C-Chain for orders

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260617-68ffb6a","dateModified":"2026-09-02T16:51:15.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog/v20260709-097f56a>>>
---
url: https://docs.dinari.com/changelog/v20260709-097f56a
title: v20260709-097f56a
description: Changed
jurisdiction ( US ) can now be specified as a parameter for post /api/v2/entities/ entity_id /kyc/url to enable partners to leverage managed US KYC workflows
fetched: 2026-11-16
method: render
plan: read
---

[Back to All](https://docs.dinari.com/changelog)

# v20260709-097f56a

4 months ago

### Changed

* `jurisdiction` (`US`) can now be specified as a parameter for **post** /api/v2/entities/{entity\_id}/kyc/url to enable partners to leverage managed US KYC workflows

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"v20260709-097f56a","dateModified":"2026-09-02T16:51:15.000Z"}
```

<<<PAGE https://docs.dinari.com/changelog?page=2>>>
---
url: https://docs.dinari.com/changelog?page=2
title: Changelog
description: 
fetched: 2026-11-16
method: render
plan: read
---

11 months ago

[# v20251226-63ffcf2](https://docs.dinari.com/changelog/v20251226-63ffcf2)

### Changed

* Migrate data with our third-party vendor

11 months ago

[# v20251223-d86787c](https://docs.dinari.com/changelog/v20251223-d86787c)

### Changed

* Improve order submission speed

11 months ago

[# v20251223-9385ea7](https://docs.dinari.com/changelog/v20251223-9385ea7)

### Changed

* General performance and maintenance updates to improve long-term reliability and scalability.

11 months ago

[# v20251222-82d808b](https://docs.dinari.com/changelog/v20251222-82d808b)

### Changed

* Update `status` field description on `OrderRequest` and `EIP155OrderRequest` API schemas to provide more information about the meaning of each status
* Update internal error logging
* Update internal configurations for speed optimizations

### Added

* Add optional `cancel_message` field to `OrderRequest` and `EIP155OrderRequest` API schemas to provide more context to reverted orders
* Add internal tests to increase test coverage
* Add automation for publishing API docs to docs.dinari.com

11 months ago

[# v20251218-161c362](https://docs.dinari.com/changelog/v20251218-161c362)

### Changed

* Update internal infrastructure and processes to address operational reliability

2 of 2

<<<PAGE https://docs.dinari.com/changelog?page=1>>>
(본문이 https://docs.dinari.com/changelog 과 같아 생략)