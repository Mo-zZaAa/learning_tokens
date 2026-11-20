# 바깥 요인 연표 재료 (분기 단위, 2012~2026)

기준일 2026-11-20. 네 회사(Coinbase, Kraken, Robinhood, Binance)가 인가를 받거나 인가 회사를 산 때의 바깥 사정을 모은 재료. 해석과 결론은 쓰지 않음. 매체는 (보도, 매체명), 셈은 (계산), 회사가 스스로 한 말은 (회사 주장).

- 전체 연표: kb/licdeep/external_timeline.csv (141행. 분류별 돈의 국면 50, 미국 규제 45, 해외 규제 30, 업계 사건 16)
- 사실 DB: work/LICDEEP-EXT/facts.csv (LDEX-001부터 LDEX-167), 출처: work/LICDEEP-EXT/sources.csv (S-LDEX-001부터 S-LDEX-183)
- 원문 저장본: sources/LICDEEP-EXT/ (연준 표, Coin Metrics 가격, CoinDesk Data 요약, 금융위원회 보도자료, ESMA 경과 기간 목록, CSA 공고 21-332, GENIUS Act 20조)
- 날짜 기준: 감독기관 발표일, 법 시행일, 판결일, 거래 완료일. 기준금리는 FOMC 결정 발표일(적용일은 다음 날, 표에 따로)
- 이미 DB에 있는 사실은 다시 넣지 않고 번호만 씀: CASE-001부터 CASE-004, CASE-007, F-1188, F-1380, F-1440, F-1869, F-2125, F-2175, F-2201, F-2202, EXT-Coinbase-032, LOC-012

## 1. 분기별 가상자산 거래대금 (집계기관 한 곳: CoinDesk Data)

- 집계기관: CoinDesk Data(옛 CCData, 그 전 이름 CryptoCompare)의 월간 Exchange Review 요약 화면(data.coindesk.com/reports/). 요약 화면에 적힌 값만 씀. 전체 보고서 PDF는 이메일 입력 양식 뒤에 있어 받지 않음
- 정의: 중앙화 거래소(회사가 운영하는 거래소, CEX)의 현물 거래대금, 파생(선물, 무기한 선물, 옵션) 거래대금, 그 합계. 탈중앙 거래소(DEX) 거래는 들어가지 않음. 단위는 조 달러, 한 달 합
- 2018-12부터 2019-12까지 CryptoCompare 보도자료는 집계 범위가 달라(하위 등급 거래소 포함, 선물은 BitMEX와 bitFlyer 두 곳만 셈 등) 이 표에 섞지 않음. 2020-01부터 2022-10까지는 이 집계기관의 공개 요약 화면이 없음(옛 주소는 목록 화면으로 돌려보냄)
- 칸 읽는 법: 달마다 "합계 / 현물 / 파생", "-"는 그 달 요약에 값이 없음. 분기 합계는 세 달 합계가 모두 있을 때만 더함(계산). 합계가 없고 현물과 파생이 둘 다 있는 달은 현물+파생으로 셈하고 칸에 표시함
- 주의
  - 다음 달 보고서가 앞 달 값을 고친 경우가 있음. 2024-03 합계 9.12조를 2024-06 보고서는 9.05조로 적음. 2026-01 파생 4.40조와 2026-02 보고서의 감소율(2.41%)로 거꾸로 셈한 2026-01 파생 약 4.21조(계산)가 다름. 표는 각 달 보고서의 원문 값
  - 2025-04 보고서의 합계 6.79조와 현물 1.76조+파생 5.14조=6.90조(계산)가 맞지 않음(원문 그대로)
  - 이 표는 시장 전체 값. 회사별 거래량과 섞지 않음

| 분기 | 달별 원문 값(합계 / 현물 / 파생, 조 달러) | 분기 합계(계산, 세 달 합계가 모두 있을 때만) | 분기 현물 합(계산) | 분기 파생 합(계산) |
|---|---|---|---|---|
| 2012-Q1부터 2022-Q3 | 빈칸(이 집계기관의 공개 요약 화면 없음, 빈칸 1) |  |  |  |
| 2022-Q4 | 10월 빈칸; [11월](https://data.coindesk.com/reports/exchange-review-november-2022) - / 1.06 / 1.44; [12월](https://data.coindesk.com/reports/exchange-review-december-2022) - / 0.544 / - |  |  |  |
| 2023-Q1 | [01월](https://data.coindesk.com/reports/exchange-review-january-2023) - / 0.86 / -; [02월](https://data.coindesk.com/reports/exchange-review-february-2023) - / 0.946 / -; [03월](https://data.coindesk.com/reports/exchange-review-march-2023) - / 1.04 / 2.77 |  | 2.85 |  |
| 2023-Q2 | [04월](https://data.coindesk.com/reports/exchange-review-april-2023) 2.77 / - / -; [05월](https://data.coindesk.com/reports/exchange-review-may-2023) 2.41 / 0.495 / 1.95; [06월](https://data.coindesk.com/reports/exchange-review-june-2023) 2.71 / 0.575 / 2.13 | 7.89 |  |  |
| 2023-Q3 | [07월](https://data.coindesk.com/reports/exchange-review-july-2023) 2.36 / - / -; [08월](https://data.coindesk.com/reports/exchange-review-august-2023) 2.09 / 0.475 / -; [09월](https://data.coindesk.com/reports/exchange-review-september) 1.67 / 0.336 / 1.33 | 6.12 |  |  |
| 2023-Q4 | [10월](https://data.coindesk.com/reports/exchange-review-october-2023) 2.57 / - / -; [11월](https://data.coindesk.com/reports/exchange-review-november) 3.61 / 0.9658 / -; [12월](https://data.coindesk.com/reports/exchange-review-december-2023) 4.68 / - / - | 10.86 |  |  |
| 2024-Q1 | [01월](https://data.coindesk.com/reports/exchange-review-january-2024) 4.65 / 1.4 / 3.25; [02월](https://data.coindesk.com/reports/exchange-review-february-2024) 4.73 / 1.41 / 3.32; [03월](https://data.coindesk.com/reports/exchange-review-march-2024) 9.12 / - / - | 18.50 |  |  |
| 2024-Q2 | [04월](https://data.coindesk.com/reports/exchange-review-april-2024) 6.58 / 2.01 / 4.57; [05월](https://data.coindesk.com/reports/exchange-review-may-2024) 5.27 / 1.57 / -; [06월](https://data.coindesk.com/reports/exchange-review-june-2024) 4.22 / - / - | 16.07 |  |  |
| 2024-Q3 | [07월](https://data.coindesk.com/reports/exchange-review-july-2024) 4.94 / - / -; [08월](https://data.coindesk.com/reports/exchange-review-august-2024) 5.22 / - / -; [09월](https://data.coindesk.com/reports/exchange-review-september-2024) 4.34 / - / - | 14.50 |  |  |
| 2024-Q4 | [10월](https://data.coindesk.com/reports/exchange-review-october-2024) 5.19 / - / -; [11월](https://data.coindesk.com/reports/exchange-review-november-2024) 10.4 / - / -; [12월](https://data.coindesk.com/reports/exchange-review-december-2024) 11.3 / - / - | 26.89 |  |  |
| 2025-Q1 | [01월](https://data.coindesk.com/reports/exchange-review) 9.03 / - / -; [02월](https://data.coindesk.com/reports/exchange-review-february) 7.2 / - / -; [03월](https://data.coindesk.com/reports/exchange-review-march) 6.79 / 1.98 / 4.81 | 23.02 |  |  |
| 2025-Q2 | [04월](https://data.coindesk.com/reports/exchange-review-april-2025) 6.79 / 1.76 / 5.14; [05월](https://data.coindesk.com/reports/exchange-review-may) 8.46 / 2.07 / 6.39; [06월](https://data.coindesk.com/reports/exchange-review-june-2025) - / - / - |  |  |  |
| 2025-Q3 | [07월](https://data.coindesk.com/reports/exchange-review-july-2025) - / - / 6.5; [08월](https://data.coindesk.com/reports/exchange-review-august-2025) - / 2.36 / 7.36; [09월](https://data.coindesk.com/reports/exchange-review-september-2025) - / 2.14 / 5.98 |  |  | 19.84 |
| 2025-Q4 | [10월](https://data.coindesk.com/reports/exchange-review-october-2025) - / 2.7 / 7.56; [11월](https://data.coindesk.com/reports/exchange-review-november-2025) 7.74 / 2.13 / 5.61; [12월](https://data.coindesk.com/reports/exchange-review-december-2025) 5.79 / - / - | 23.79 (한 달 이상은 현물+파생 합으로 셈) |  |  |
| 2026-Q1 | [01월](https://data.coindesk.com/reports/exchange-review-january-2026) - / - / 4.4; [02월](https://data.coindesk.com/reports/exchange-review-february-2026) - / 1.5 / 4.11; [03월](https://data.coindesk.com/reports/exchange-review-march-2026) 5.26 / - / 3.99 |  |  | 12.50 |
| 2026-Q2 | [04월](https://data.coindesk.com/reports/exchange-review-april-2026) 4.61 / - / -; [05월](https://data.coindesk.com/reports/exchange-review-may-2026) - / - / -; [06월](https://data.coindesk.com/reports/exchange-review-june-2026) 4.99 / - / - |  |  |  |
| 2026-Q3 | [07월](https://data.coindesk.com/reports/exchange-review-july-2026) 3.76 / - / -; 08월 빈칸; 09월 빈칸 |  |  |  |
| 2026-Q4 | 10월에서 12월 보고서 없음(빈칸 3) |  |  |  |

- 표에서 보이는 국면(계산, 분기 합계가 있는 분기만): 2023-Q3 6.12조로 가장 낮고, 2024-Q4 26.89조로 가장 높음. 2024-Q4는 2023-Q3의 약 4.4배
- 월 단위 사건(연표 행): 2024-03 9.12조 당시 최고, 2024-12 11.3조 새 최고, 2025-10-10 대량 강제 청산(미결제약정 21.4% 감소, 1위가 Binance에서 CME로), 2026-07 3.76조로 2023-11 뒤 최저

## 2. 미국 기준금리(연방기금금리 목표 범위) 변경일

- 출처: 연준 공개시장 운영 표([openmarket.htm](https://www.federalreserve.gov/monetarypolicy/openmarket.htm), 적용일 기준, 2026-09-16 갱신)와 각 FOMC 성명(결정 발표일). 32회 변경을 성명 원문 문장으로 하나씩 대조함
- 2012-01부터 2015-12-16 결정 전까지 연 0%에서 0.25%(2008-12-16 결정 뒤 그대로)

| 결정 발표일 | 적용일 | 변경 | 새 목표 범위(연) | 원문 |
|---|---|---|---|---|
| 2008-12-16 | 2008-12-16 | 인하 | 0%에서 0.25%(2012-01부터 2015-12까지 이 범위 유지) | [표](https://www.federalreserve.gov/monetarypolicy/openmarket.htm) |
| 2015-12-16 | 2015-12-17 | 인상 25bp | 0.25%에서 0.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20151216a.htm) |
| 2016-12-14 | 2016-12-15 | 인상 25bp | 0.50%에서 0.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20161214a.htm) |
| 2017-03-15 | 2017-03-16 | 인상 25bp | 0.75%에서 1.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20170315a.htm) |
| 2017-06-14 | 2017-06-15 | 인상 25bp | 1.00%에서 1.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20170614a.htm) |
| 2017-12-13 | 2017-12-14 | 인상 25bp | 1.25%에서 1.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20171213a.htm) |
| 2018-03-21 | 2018-03-22 | 인상 25bp | 1.50%에서 1.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20180321a.htm) |
| 2018-06-13 | 2018-06-14 | 인상 25bp | 1.75%에서 2.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20180613a.htm) |
| 2018-09-26 | 2018-09-27 | 인상 25bp | 2.00%에서 2.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20180926a.htm) |
| 2018-12-19 | 2018-12-20 | 인상 25bp | 2.25%에서 2.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20181219a.htm) |
| 2019-07-31 | 2019-08-01 | 인하 25bp | 2.00%에서 2.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20190731a.htm) |
| 2019-09-18 | 2019-09-19 | 인하 25bp | 1.75%에서 2.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20190918a.htm) |
| 2019-10-30 | 2019-10-31 | 인하 25bp | 1.50%에서 1.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20191030a.htm) |
| 2020-03-03 | 2020-03-04 | 인하 50bp | 1.00%에서 1.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200303a.htm) |
| 2020-03-15 | 2020-03-16 | 인하 100bp | 0%에서 0.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm) |
| 2022-03-16 | 2022-03-17 | 인상 25bp | 0.25%에서 0.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm) |
| 2022-05-04 | 2022-05-05 | 인상 50bp | 0.75%에서 1.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220504a.htm) |
| 2022-06-15 | 2022-06-16 | 인상 75bp | 1.50%에서 1.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220615a.htm) |
| 2022-07-27 | 2022-07-28 | 인상 75bp | 2.25%에서 2.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220727a.htm) |
| 2022-09-21 | 2022-09-22 | 인상 75bp | 3.00%에서 3.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220921a.htm) |
| 2022-11-02 | 2022-11-03 | 인상 75bp | 3.75%에서 4.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm) |
| 2022-12-14 | 2022-12-15 | 인상 50bp | 4.25%에서 4.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm) |
| 2023-02-01 | 2023-02-02 | 인상 25bp | 4.50%에서 4.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230201a.htm) |
| 2023-03-22 | 2023-03-23 | 인상 25bp | 4.75%에서 5.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230322a.htm) |
| 2023-05-03 | 2023-05-04 | 인상 25bp | 5.00%에서 5.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230503a.htm) |
| 2023-07-26 | 2023-07-27 | 인상 25bp | 5.25%에서 5.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230726a.htm) |
| 2024-09-18 | 2024-09-19 | 인하 50bp | 4.75%에서 5.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a.htm) |
| 2024-11-07 | 2024-11-08 | 인하 25bp | 4.50%에서 4.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20241107a.htm) |
| 2024-12-18 | 2024-12-19 | 인하 25bp | 4.25%에서 4.50% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20241218a.htm) |
| 2025-09-17 | 2025-09-18 | 인하 25bp | 4.00%에서 4.25% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20250917a.htm) |
| 2025-10-29 | 2025-10-30 | 인하 25bp | 3.75%에서 4.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20251029a.htm) |
| 2025-12-10 | 2025-12-11 | 인하 25bp | 3.50%에서 3.75% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20251210a.htm) |
| 2026-09-16 | 2026-09-17 | 인상 25bp | 3.75%에서 4.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) |
| 2026-10-28 | | 동결 | 3.75%에서 4.00% | [성명](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm) |

- 국면 묶음(계산, 위 표에서 셈)
  - 0% 대: 2008-12부터 2015-12까지, 2020-03부터 2022-03까지
  - 첫 인상기: 2015-12부터 2018-12까지 9회 인상, 정점 연 2.25%에서 2.50%
  - 2019 인하 3회, 2020-03 두 차례 긴급 인하로 0%대
  - 둘째 인상기: 2022-03부터 2023-07까지 11회, 합 525bp, 정점 연 5.25%에서 5.50%(2024-09 첫 인하 전까지 유지)
  - 인하기: 2024-09부터 2025-12까지 6회, 합 175bp
  - 2026-09-16 25bp 인상(2023-07 뒤 첫 인상), 2026-10-28 동결. 다음 회의(2026-12)는 오늘 뒤라 없음

## 3. 비트코인 고점과 저점 (집계기관 한 곳: Coin Metrics)

- 출처: Coin Metrics Community API의 PriceUSD(일별 기준가). Coin Metrics 정의: "The fixed closing price of the asset as of 00:00 UTC the following day (i.e., midnight UTC of the current day)". 하루 한 값이라 흔히 보도되는 장중 최고가보다 낮을 수 있음
- 고점과 저점 고르는 법(계산): 고점에서 50% 넘게 빠지면 그 고점을, 저점에서 두 배 넘게 오르면 그 저점을 순환점으로 잡음. 2019-06, 2020-03, 2021-04, 2021-07은 이 기준에 걸린 중간 순환점. 2026-06-30 값은 아직 두 배 반등이 없어 저점 확정 아님
- 2012-01-01 5.29달러, 2012-12-31 13.55달러

| 날짜 | 구분 | 값(달러) | 직전 고점 대비(계산) | 설명 |
|---|---|---|---|---|
| 2013-12-04 | 고점 | 1,135 |  | 2013 순환 고점 |
| 2015-01-14 | 저점 | 176 | -84.5% | 2013 고점 뒤 저점 |
| 2017-12-16 | 고점 | 19,641 | +1,631% | 2017 순환 고점 |
| 2018-12-15 | 저점 | 3,185 | -83.8% | 2017 고점 뒤 저점 |
| 2019-06-26 | 고점 | 12,863 | -35% | 2019 중간 반등 고점 |
| 2020-03-12 | 저점 | 4,959 | -61.4% | 2020-03 급락 저점 |
| 2021-04-13 | 고점 | 63,446 | +393% | 2021 첫 고점 |
| 2021-07-20 | 저점 | 29,767 | -53.1% | 2021 중간 저점 |
| 2021-11-08 | 고점 | 67,542 | +6% | 2021 순환 고점 |
| 2022-11-09 | 저점 | 15,758 | -76.7% | 2021 고점 뒤 저점(FTX 붕괴 주간) |
| 2025-10-06 | 고점 | 124,824 | +85% | 2025 순환 고점, 이 자료의 역대 최고 |
| 2026-06-30 | 저점 | 58,525 | -53.1% | 2025 고점 뒤 지금까지 최저(저점 확정 아님) |
| 2026-11-19 | 마지막 값 | 61,881 | -50.4% | 2025-10-06 고점 대비 |

- 분기별 값(분기말 값, 분기 안 최고와 최저, 모두 Coin Metrics 일별 기준가)

| 분기 | 분기말 값 | 분기 최고(날짜) | 분기 최저(날짜) |
|---|---|---|---|
| 2012-Q1 | 4.89 | 7.10 (2012-01-08) | 4.26 (2012-02-16) |
| 2012-Q2 | 6.68 | 6.69 (2012-06-20) | 4.71 (2012-04-07) |
| 2012-Q3 | 12.39 | 13.45 (2012-08-16) | 6.45 (2012-07-03) |
| 2012-Q4 | 13.55 | 13.76 (2012-12-13) | 10.13 (2012-10-26) |
| 2013-Q1 | 93.90 | 93.90 (2013-03-31) | 13.28 (2013-01-02) |
| 2013-Q2 | 89.48 | 231 (2013-04-09) | 68.28 (2013-04-16) |
| 2013-Q3 | 126 | 131 (2013-09-01) | 66.34 (2013-07-06) |
| 2013-Q4 | 730 | 1,135 (2013-12-04) | 104 (2013-10-02) |
| 2014-Q1 | 455 | 914 (2014-01-06) | 455 (2014-03-31) |
| 2014-Q2 | 639 | 672 (2014-06-03) | 367 (2014-04-10) |
| 2014-Q3 | 389 | 651 (2014-07-02) | 373 (2014-09-29) |
| 2014-Q4 | 321 | 423 (2014-11-12) | 310 (2014-12-30) |
| 2015-Q1 | 245 | 316 (2015-01-02) | 176 (2015-01-14) |
| 2015-Q2 | 264 | 264 (2015-06-30) | 220 (2015-04-14) |
| 2015-Q3 | 237 | 311 (2015-07-12) | 212 (2015-08-24) |
| 2015-Q4 | 430 | 465 (2015-12-15) | 238 (2015-10-02) |
| 2016-Q1 | 416 | 459 (2016-01-07) | 366 (2016-01-31) |
| 2016-Q2 | 674 | 767 (2016-06-16) | 417 (2016-04-01) |
| 2016-Q3 | 609 | 703 (2016-07-02) | 527 (2016-08-02) |
| 2016-Q4 | 969 | 980 (2016-12-28) | 610 (2016-10-04) |
| 2017-Q1 | 1,082 | 1,289 (2017-03-03) | 788 (2017-01-11) |
| 2017-Q2 | 2,453 | 2,974 (2017-06-11) | 1,090 (2017-04-01) |
| 2017-Q3 | 4,335 | 4,918 (2017-09-01) | 1,911 (2017-07-16) |
| 2017-Q4 | 13,921 | 19,641 (2017-12-16) | 4,217 (2017-10-04) |
| 2018-Q1 | 6,922 | 17,104 (2018-01-06) | 6,832 (2018-03-30) |
| 2018-Q2 | 6,376 | 9,796 (2018-05-05) | 5,859 (2018-06-28) |
| 2018-Q3 | 6,604 | 8,398 (2018-07-24) | 6,136 (2018-08-10) |
| 2018-Q4 | 3,687 | 6,605 (2018-10-08) | 3,185 (2018-12-15) |
| 2019-Q1 | 4,094 | 4,110 (2019-02-23) | 3,359 (2019-02-07) |
| 2019-Q2 | 10,843 | 12,863 (2019-06-26) | 4,138 (2019-04-01) |
| 2019-Q3 | 8,282 | 12,579 (2019-07-09) | 8,065 (2019-09-29) |
| 2019-Q4 | 7,167 | 9,558 (2019-10-27) | 6,609 (2019-12-17) |
| 2020-Q1 | 6,432 | 10,362 (2020-02-14) | 4,959 (2020-03-12) |
| 2020-Q2 | 9,144 | 10,199 (2020-06-01) | 6,625 (2020-04-15) |
| 2020-Q3 | 10,772 | 12,316 (2020-08-17) | 9,067 (2020-07-03) |
| 2020-Q4 | 29,023 | 29,023 (2020-12-31) | 10,556 (2020-10-03) |
| 2021-Q1 | 58,792 | 61,289 (2021-03-13) | 29,381 (2021-01-01) |
| 2021-Q2 | 35,065 | 63,446 (2021-04-13) | 31,684 (2021-06-25) |
| 2021-Q3 | 43,782 | 52,641 (2021-09-06) | 29,767 (2021-07-20) |
| 2021-Q4 | 46,355 | 67,542 (2021-11-08) | 46,334 (2021-12-17) |
| 2022-Q1 | 45,562 | 47,560 (2022-01-01) | 34,996 (2022-01-22) |
| 2022-Q2 | 19,333 | 46,663 (2022-04-04) | 19,014 (2022-06-18) |
| 2022-Q3 | 19,435 | 24,426 (2022-08-13) | 18,507 (2022-09-21) |
| 2022-Q4 | 16,524 | 21,283 (2022-11-05) | 15,758 (2022-11-09) |
| 2023-Q1 | 28,515 | 28,515 (2023-03-31) | 16,607 (2023-01-01) |
| 2023-Q2 | 30,485 | 30,667 (2023-06-27) | 25,098 (2023-06-14) |
| 2023-Q3 | 26,978 | 31,435 (2023-07-13) | 25,135 (2023-09-11) |
| 2023-Q4 | 42,217 | 44,205 (2023-12-08) | 26,741 (2023-10-12) |
| 2024-Q1 | 71,227 | 73,082 (2024-03-13) | 39,577 (2024-01-22) |
| 2024-Q2 | 62,763 | 71,713 (2024-04-08) | 58,142 (2024-05-01) |
| 2024-Q3 | 63,260 | 68,171 (2024-07-28) | 53,839 (2024-09-06) |
| 2024-Q4 | 93,390 | 106,116 (2024-12-17) | 60,221 (2024-10-10) |
| 2025-Q1 | 82,461 | 105,988 (2025-01-21) | 79,006 (2025-03-10) |
| 2025-Q2 | 107,153 | 111,477 (2025-05-22) | 76,351 (2025-04-08) |
| 2025-Q3 | 113,972 | 123,443 (2025-08-13) | 105,566 (2025-07-01) |
| 2025-Q4 | 87,517 | 124,824 (2025-10-06) | 84,775 (2025-11-22) |
| 2026-Q1 | 68,215 | 97,044 (2026-01-14) | 63,495 (2026-02-05) |
| 2026-Q2 | 58,525 | 82,257 (2026-05-10) | 58,525 (2026-06-30) |
| 2026-Q3 | 83,580 | 86,505 (2026-09-21) | 60,066 (2026-07-01) |
| 2026-Q4 | 61,881 (2026-11-19 값) | 86,521 (2026-10-04) | 61,881 (2026-11-19) |

## 4. 나라별 제도 요약

- 칸 기준: "다른 나라 영업"은 그 인가 하나로 다른 나라 고객을 상대할 수 있는지, 또는 다른 나라 회사가 그 나라 고객을 상대할 때 무엇이 필요한지. "법정 심사 기간"은 법령에 적힌 기한만(실제 걸린 기간은 회사 카드에서). 빈칸은 이번에 1차 자료로 확인하지 못한 칸이고 끝의 빈칸 목록 번호를 붙임

| 나라, 지역 | 법과 인가 | 시행일 | 다른 나라 영업 | 법정 심사 기간 | 허용 업무 | 출처 |
|---|---|---|---|---|---|---|
| 미국 뉴욕주 | BitLicense(23 NYCRR Part 200, NYDFS 가상자산 영업 인가). 다른 길로 제한목적 신탁회사 인가. 2026-11-16 열람 목록에 BitLicense 26곳, 신탁 인가 13곳(F-1411) | 2015-06-24(기존 업체 신청 기한 2015-08-10, 첫 인가 2015-09-22 Circle) | 뉴욕 주민 대상 영업에 필요. 다른 주는 주별 송금업 인가를 따로 받음(Coinbase 10-K, F-2285) | 빈칸 4 | 가상자산 영업(정의 조문 원문 미열람, 빈칸 4) | [NYDFS 안내](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses), [첫 인가](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr1509221) |
| 미국 연방(스테이블코인) | GENIUS Act(Public Law 119-27). 지급 스테이블코인 발행 허가제(OCC, 연준, FDIC, NCUA, 주 감독기관) | 서명 2025-07-18. 시행은 서명 18개월 뒤(2027-01-18, 계산)와 주요 연방 감독기관 최종 규정 120일 뒤 중 빠른 날. OCC 최종 규정 효력 2027-01-18 | 빈칸 6 | 빈칸 6 | 지급 스테이블코인 발행 | [법률](https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm), [OCC 규정](https://www.federalregister.gov/documents/2026/10/23/2026-21706/implementing-the-guiding-and-establishing-national-innovation-for-us-stablecoins-act-for-the) |
| 미국 연방(CFTC 등록 거래소) | 지정계약시장(DCM)에서 가상자산 현물 상장 거래(2025-12-04 발표, 보도). 무기한 계약은 건별 심사(2026-05-29 정책 성명) | 2025-12-04 발표, 2020 개인 상품 거래 지침 철회 2025-12-10 | 빈칸 6 | 빈칸 6 | 선물, 옵션, 이벤트 계약, 레버리지 현물 상장(보도) | [CFTC 철회](https://www.federalregister.gov/documents/2025/12/16/2025-22872/withdrawal-of-interpretive-guidance-retail-commodity-transactions-involving-certain-digital-assets), [무기한 정책](https://www.federalregister.gov/documents/2026/06/03/2026-11020/policy-statement-concerning-the-listing-of-perpetual-contracts) |
| EU | MiCA(Regulation (EU) 2023/1114) 가상자산 서비스 사업자(CASP) 인가. 회원국 감독청이 인가 | 발효 2023-06-29, 스테이블코인 편 2024-06-30, CASP 2024-12-30. 기존 사업자 경과 기간 회원국별 6, 9, 12, 18개월, 최종 2026-07-01 | 한 회원국 인가로 EU 전역 영업(설립 또는 서비스 자유, 59조 7항). 다른 회원국 영업은 본국 감독청 통지가 상대국에 전달된 날 또는 늦어도 통지 15일째부터(65조 4항) | 접수 확인 5영업일, 완비 판단 25영업일, 완비 뒤 결정 40영업일, 보완 요청으로 멈춘 기간 최대 20영업일(63조) | 10종: 보관, 거래 플랫폼 운영, 법정화폐 교환, 가상자산 간 교환, 주문 집행, 모집 주선, 주문 접수 전달, 자문, 일임 운용, 이전(3조 1항 16호) | [59조](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-59-authorisation), [63조](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-63-assessment-application), [65조](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-65-cross-border-provision-crypto), [149조](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-149-entry-force-and-application), [경과 기간 목록](https://www.esma.europa.eu/sites/default/files/2024-12/List_of_MiCA_grandfathering_periods_art._143_3.pdf) |
| EU(증권 주문) | MiFIR 39a조: 증권사의 주문 대가(PFOF) 수령 금지 | 2024-03-28 발효. 이미 PFOF가 있던 회원국은 자국 고객 한정 2026-06-30까지 면제 가능(독일 2024-03-21 통지) | 해당 없음 | 해당 없음 | 금지 규정(거래 장소의 공개 요금표상 고객 몫 할인은 예외) | [39a조](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifir/article-39a-prohibition-receiving-payment), [면제 목록](https://www.esma.europa.eu/sites/default/files/2024-03/ESMA35-335435667-5923_List_of_EU_Member_States_using_temporary_exemption_from_PFOF_prohibition_under_the_MiFIR_review.pdf) |
| 영국 | (1) 자금세탁방지 등록(MLR 2017 개정, FCA) (2) 금융광고 규제 (3) 새 인가 제도(FSMA 2000 (Cryptoassets) Regulations 2026, 2026-02-04 의회 통과) | (1) 2020-01-10 (2) 2023-10-08 (3) 신청 창구 2026-09-30부터 2027-02-28, 전면 시행 2027-10-25 | 금융광고 규제는 해외 회사도 영국 소비자 대상이면 적용. 영국 인가로 다른 나라 영업은 빈칸 5 | FSMA 55V 일반 기한: 완비 신청 6개월, 미완비 12개월. 새 가상자산 인가에 같은 기한이 쓰이는지는 빈칸 5 | 등록은 자금세탁방지 감독만(FCA: 금융옴부즈만과 예금보험 보호 대상 아님). 2021-01-06부터 개인 대상 가상자산 파생상품, ETN 판매 금지 | [FCA 제도](https://www.fca.org.uk/publications/policy-statements/cryptoasset-regime), [MLR](https://www.legislation.gov.uk/uksi/2019/1511/made), [광고](https://www.fca.org.uk/firms/cryptoassets/marketing-uk-consumers), [55V](https://www.legislation.gov.uk/ukpga/2000/8/section/55V) |
| 캐나다 | 증권법상 가상자산 거래 플랫폼 등록. 등록 전 영업은 등록 전 약정(PRU) | PRU 요구 2022-08-15, 약정 범위 넓힘 발표 2022-12-12, 공고 21-332 2023-02-22(새 PRU 30일 안 제출) | 캐나다 고객 대상이면 외국 플랫폼도 PRU 대상. Binance 2023-05-12, OKX 2023-03, Bybit 2023-05 철수(보도) | 빈칸 6 | PRU 조건: 고객 자산 분리 보관, 담보 재사용 금지, 모든 고객 증거금과 레버리지 금지. 증권이나 파생에 해당하는 가상자산 매매 금지, 스테이블코인은 증권으로 봄(보도, Cointelegraph) | [21-332](https://www.bcsc.bc.ca/-/media/PWS/New-Resources/Securities-Law/Instruments-and-Policies/Policy-2/21332-CSA-Staff-Notice-February-22-2023.pdf?dt=20240417212452) |
| 일본 | 자금결제법 가상통화(지금 이름 암호자산) 교환업 등록(지방재무국) | 2017-04-01. 2017-09 말 등록 11곳, 심사 중 19곳 | 일본 거주자 대상 영업은 일본 등록 필요. 외국 사업자도 일본 안 사무소 기준으로 지방재무국과 사전 상담 | 빈칸 6 | 가상통화 교환 서비스(세부 범위 빈칸 6). 등록 요건 예: 최저 자본금 1,000만 엔, 순자산 마이너스 아님 | [FSA 2017](https://www.fsa.go.jp/en/news/2017/20170930-1/02.pdf), [FSA 2018](https://www.fsa.go.jp/en/newsletter/weekly2018/285.html) |
| 한국 | 특정금융정보법 가상자산사업자 신고(금융정보분석원, FIU), 가상자산이용자보호법 | 이용자보호법 2024-07-19. 특금법 신고 의무 시행일은 빈칸 8 | 국외 사업자도 내국인 대상 영업이면 신고 의무(특금법 6조 2항). 판단 기준: 한국어 홈페이지, 한국인 대상 마케팅, 원화 결제. 미신고 영업 5년 이하 징역 또는 5천만 원 이하 벌금. 2026-06-24 기준 신고 사업자 28곳. 2025-03-25 앱 17곳, 2026-10-13 사이트 27건 접속차단 | 빈칸 6 | 매도, 매수, 교환, 이전, 보관, 관리, 중개, 알선, 대행(이용자보호법 2조 1호 범위). 예치금 은행 보관, 가상자산 80% 이상 인터넷과 분리 보관 | [2025-03-26](https://www.fsc.go.kr/no010101/84237), [2026-06-24](https://www.fsc.go.kr/no010101/87177), [2026-10-13](https://www.fsc.go.kr/no010101/87916), [시행령](https://www.fsc.go.kr/no010101/82530) |
| 아부다비(ADGM) | ADGM 금융감독청(FSRA) 가상자산 규제 틀 | 2018-06-25 | 빈칸 6 | 빈칸 6 | 현물 가상자산 활동(거래소, 보관, 기타 중개) | [ADGM 2018](https://www.adgm.com/media/announcements/adgm-launches-crypto-asset-regulatory-framework) |
| 두바이 | Law No. 4 of 2022, 가상자산규제청(VARA) 인가(Permit). VARA 가상자산 및 관련 활동 규정 2023 | 법 2022-02-28(공포일 시행), 규정 첫 판 2023-02-07(지금 판 효력 2025-06-19) | 두바이 전역(특구, 자유구역 포함, DIFC 제외)에 적용. 두바이에서 영업하려면 인가 먼저. 다른 나라 영업은 빈칸 6 | 빈칸 6 | 7종: 플랫폼 운영과 관리, 법정화폐 교환, 가상자산 간 교환, 이전, 보관과 관리, 지갑, 가상 토큰 발행과 거래(법 16조) | [법](https://dlp.dubai.gov.ae/Legislation%20Reference/2022/Law%20No.%20(4)%20of%202022%20Regulating%20Virtual%20Assets.html), [규정](https://rulebooks.vara.ae/rulebook/virtual-assets-and-related-activities-regulations-2023) |
| 버뮤다 | Digital Asset Business Act 2018(DABA), 버뮤다 통화청(BMA) 인가. 처음 완전(F), 제한(M) 2종, 지금 시험(T) 더해 3종 | 2018-09-17 BMA 발표 때 법과 하위 규칙 시행 중(정확한 시행일 빈칸 7) | 빈칸 6 | 빈칸 6 | 거래소, ICO, 디지털자산 지급 서비스 등 디지털자산 사업 전반(BMA 2018 발표 문구) | [BMA 2018](https://www.bma.bm/documents-centre/documents-news-and-press-releases/general-all-sectors/bma-releases-licensing-requirements-for-digital-asset-businesses) |
| 싱가포르 | 지급서비스법(디지털 지급 토큰 서비스 인가, MAS). 금융서비스시장법(FSMA 2022) 디지털토큰서비스업(DTSP) | 지급서비스법 2020-01-28. DTSP 2025-06-30(경과 기간 없음) | DTSP: 싱가포르 거점에서 해외 고객만 상대해도 인가 필요, MAS는 인가를 극히 제한적으로만 줌(MAS 2025-05-30 답변서, 원문 열람 막힘. 보도, Cointelegraph) | 빈칸 6 | 빈칸 6 | [MAS 답변서](https://www.mas.gov.sg/-/media/response-to-feedback-received-from-dtsp-cp.pdf), [보도](https://cointelegraph.com/news/singapore-crypto-firms-deadline-overseas-digital-token-services) |

- MiCA 경과 기간(ESMA 목록, 파일 수정일 2026-05-20): 6개월 라트비아, 헝가리, 네덜란드, 폴란드, 슬로베니아, 핀란드. 9개월 스웨덴. 12개월 독일, 아일랜드, 리투아니아, 오스트리아, 슬로바키아, 노르웨이. 18개월 벨기에, 불가리아, 체코, 덴마크, 에스토니아, 그리스, 스페인, 프랑스, 크로아티아, 이탈리아, 키프로스, 룩셈부르크, 몰타, 포르투갈, 루마니아, 아이슬란드, 리히텐슈타인. 일부 나라는 신청 마감이 따로 있음(체코 2025-07-31, 덴마크 2024-12-30, 이탈리아 2025-12-30, 불가리아 2025-10-08)
- 2026-11-11 기준 ESMA 임시 MiCA 등록부 CASP 종료일 없는 404곳(F-1413). 이미 DB에 있는 숫자라 다시 세지 않음

## 5. 서로 다른 값과 주의

- SEC 대 Binance 제소일: 로펌 해설(Reed Smith)과 SEC 보도자료 번호 2023-101은 2023-06-05, 워싱턴 DC 연방지법 의견서(2024-06-28)는 "On June 6, 2023". 둘 다 적고 고르지 않음(연표는 2023-06-05 행에 둘 다 씀)
- BitLicense 시행일: NYDFS 안내 화면은 2015-06-24 시행, 2015-08-10 기존 업체 신청 기한. 기존 사실 S1KR2-024(work/STAGE1-KR2)의 "2015-07-24 시행"과 다름. 메인 세션 확인 필요
- Coinbase 소송 취하일: SEC 2025-47은 2025-02-27, Coinbase 10-K는 2025-02-28(CASE-001에 이미 충돌 표시)
- Kraken 소송 취하: 2025-03-03은 Kraken이 밝힌 실무진 원칙 합의일, 2025-03-27은 공동 합의서 제출일(S1KR3-010, S1KR3-011)
- CoinDesk Data 값 수정: 1절 주의 참고. 같은 달 값도 보고서마다 다를 수 있어 회사 카드에서 인용할 때 보고서 달을 같이 적어야 함
- 비트코인 가격은 Coin Metrics 하루 한 값. 장중 최고가(보도에 흔한 값)와 섞지 않음

## 6. 빈칸 목록

1. CoinDesk Data 거래대금 2012-Q1부터 2022-Q3(2022-10 포함): 공개 요약 화면 없음. 시도: data.coindesk.com/sitemap.xml 전수(331개 주소), 옛 ccdata.io 주소(목록 화면으로 돌려보냄), 전체 보고서 PDF(이메일 양식이라 받지 않음). 2018-12부터 2019-12 CryptoCompare 보도자료는 범위가 달라 뺌
2. CoinDesk Data 월 합계가 요약에 없는 달: 2022-11, 2022-12, 2023-01부터 2023-03, 2025-06(Binance 값만), 2025-07부터 2025-10(현물, 파생만), 2026-01, 2026-02, 2026-05(거래소별 값만). 분기 합계가 비는 원인
3. CoinDesk Data 2026-08, 2026-09, 2026-10 Exchange Review: 사이트맵과 연구 목록의 마지막이 2026-07, 짐작한 주소는 404
4. 뉴욕 BitLicense 법정 심사 기간과 "가상자산 영업" 정의 조문(23 NYCRR 200.2) 원문: 이번에 열람 못함
5. 영국 새 가상자산 인가의 심사 기간(FSMA 55V 일반 기한이 그대로 쓰이는지)과 영국 인가로 다른 나라 고객을 상대할 수 있는지: FCA 정책 성명 본문(PDF) 미열람
6. 법정 심사 기간과 다른 나라 영업 조건: 미국 GENIUS 발행 허가, CFTC DCM, 캐나다, 일본, 한국, ADGM, 두바이, 버뮤다, 싱가포르. 이번에 1차 조문으로 확인 못함
7. 버뮤다 DABA 2018 정확한 시행일: 법 81조(시행 조항) 원문 미열람. BMA 2018-09-17 발표는 "시행 중"까지만
8. 한국 특정금융정보법 가상자산사업자 신고 의무 시행일과 신고 기한(2021): 금융위원회 보도자료 검색에서 원문 못 찾음. 2026-08 개정 특금법의 정확한 시행일도 "26.8월 이후" 표현만 확인
9. Coincheck 해킹 정확한 날짜와 금액의 1차 자료: 저장 매체 기사는 "this year", 약 5.34억 달러(Cointelegraph)만
10. Kalshi 1심 판결 명령일(이유서 2024-09-12는 확인, "A separate order has issued")과 항소법원의 취하 결정일(보도: 신청 2025-05-05, 결정 이틀 뒤)
11. SEC Crypto Task Force 출범일 1차 원문(SEC 보도자료 2025-30, sec.gov 403). 지금은 로펌 해설(2025-01-21)과 SEC 관보 서술("In early 2025")
12. SEC 대 Binance 소장 접수일(사건 기록 표지): 2023-06-05와 06-06 충돌을 가를 원문 미열람
13. Coinbase 웰스 통지(2023-03-22) 1차 원문(Coinbase 2023 1분기 10-Q, sec.gov 403). 지금은 로펌 해설
14. FTX 자회사 Embed(주식 청산 증권사) 매각 결과와 사는 쪽
15. FTX Japan 매각 bitFlyer 원문 PDF(403)와 파산 법원 승인일
16. FTX EU 매각 금액, 거래 완료일, 키프로스 인가 재개일(보도는 2025-01-07 인수 발표와 인가 정지까지만)
17. Silvergate 청산 발표 원문(Business Wire 403, 보도로만)
18. CLARITY Act 상원 경과(congress.gov 403)
19. Kraken 2021에서 2022 상장 계획의 1차 자료(회사 발표 없음, Protos 정리 기사뿐)
20. 싱가포르 MAS 원문 2건(지급서비스법 시행 보도자료, DTSP 답변서): curl은 점검 화면, WebFetch는 세션 허용 밖. 지금은 검색 결과와 매체
21. GENIUS Act 다른 연방 감독기관(연준, FDIC, NCUA) 최종 규정 여부: 관보 검색에서 OCC 최종 규정(2026-10-23)과 재무부 임시 최종 규정(2026-09-30)만 나옴
22. 제3순회 항소법원 판결 뒤 연방대법원 신청(No. 25A1465) 결과
23. SEC와 CFTC의 2025-09 공동 성명(등록 거래소의 현물 가상자산 거래 허용) 원문: 보도로만 존재 확인, 날짜와 원문 미열람
24. CoinDesk Data 이전 연도(2012에서 2021) 비트코인 외 시장 국면 숫자(가상자산 전체 시가총액 등): 이번 범위에서 찾지 않음

## 7. 막힌 경로

- eur-lex.europa.eu: 202 빈 응답(봇 확인). 우회하지 않고 ESMA Interactive Single Rulebook(MiCA 3, 59, 63, 65, 143, 149조, MiFIR 39a조)과 프랑스 AMF 안내로 대신함
- www.mas.gov.sg: curl 점검 화면, WebFetch 허용 밖(ENOTFOUND)
- www.sec.gov(403): 소송 보도자료와 10-Q. govinfo.gov 법원 판결문, federalregister.gov, 기존 사용자 로컬 브라우저 열람분(LOCAL-S03)으로 대신함
- securities-administrators.ca, lautorite.qc.ca, sso.agc.gov.sg(403): CSA 공고는 BCSC 사본으로 대신함
- restructuring.ra.kroll.com(FTX 파산 기록, 403), courtlistener.com(403): FTX 자회사 매각은 MIAX 보도자료와 매체로
- cftc.gov(403, 기존 노하우): CFTC 결정은 federalregister.gov 관보로, 2025-12-04 발표는 매체로
- businesswire.com, finextra.com, bitflyer.com PDF(403): 같은 사건을 실은 매체로
- data.coindesk.com 전체 보고서: 이메일 입력 양식(HubSpot) 뒤. 이메일을 넣지 않음
- congress.gov(403): 법률은 govinfo.gov PLAW 사본
- hklaw.com 일부 주소(403): 제3순회 판결은 법원 원문 PDF(www2.ca3.uscourts.gov)로
