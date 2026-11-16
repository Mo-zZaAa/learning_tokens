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