# 로컬 브라우저 확인 결과 반영 (2026-11-17 KST 확인, 2026-11-16 기준 작업)

출처: work/LOCAL/local_result.md, 캡처 captures/local/ 17장. 사실 행 work/LOCAL/facts.csv(LOC-001~017), 병합 후 F-1223~F-1239.

## 항목, 새 F 번호, 반영한 곳
| # | 항목 | 새 F | 반영한 곳 |
|---|---|---|---|
| 1 | Coinbase 설립 2012, 공동 창업자, 미션 | F-1223, F-1224, F-1225 | Coinbase 정체 카드 "설립과 미션", checklist(대표 상품 비고) |
| 2 | Coinbase 2021-04-14 Nasdaq 직상장 예정 발표(첫 거래 확인 아님) | F-1226 | 정체 카드 상장, checklist 상장 칸(못 찾음에서 1차 확인) |
| 3 | SEC 소송 2025-02-27 취하 | F-1227 | 정체 카드 큰 사고와 제재, checklist(단일 출처에서 1차 확인) |
| 6 | Coinbase Financial Markets FCM 2023-08-15 직접 등록 | F-1228 | Coinbase E, 사업 범위 자산 2, 해석 중분류 |
| 7 | Binance 미국 주식과 ETF 7,000종 이상(2026-06-01) | F-1229 | Binance 정체 카드, checklist 종목 수 |
| 8 | bStocks 5종 증거금 담보(2026-10-28, 차입 불가) | F-1230 | Binance 사업 범위 자산 2 |
| 9 | TradFi 무기한 계약 2026-10-29(주식 5, ETF 1), 2026-11-12(NU, FRHC) | F-1231, F-1232 | Binance 사업 범위 자산 2 |
| 10 | BUIDL 기관 장외결제 담보(2025-11-14) | F-1233 | Binance 자산 2와 고객 축 |
| 11 | CZ 사면 2025-10-21(법무부 목록) | F-1234 | Binance 정체 카드 사면 줄 근거 추가, checklist |
| 12 | Robinhood Q3 Tenev 발언 | F-1235 | 발언 4 캡처를 captures/local/Robinhood_q3_quote.png로 교체(링크는 IR 원문 그대로). 기존 F-1067과 같은 문장 |
| 14 | Robinhood Derivatives(이전 Marex North America) FCM 2010-11-23 | F-1236 | Robinhood E 미국 선물 중개 줄. 인수 시점은 자료에 없음 |
| 15 | Dinari, Inc/TA(CIK 0001915430) TA-1 접수 2022-04-05, 수리 2022-05-05, 효력일 미확인 | F-1237 | Dinari E 명의개서대리인 줄 |
| 18 | Binance 주식 무기한선물 24시간 거래대금 | F-1238(개별 주식), F-1239(ETF, 금, 분류 미확인) | kb/perp_vs_spot.md 2절 |

## 승격(work/MANUAL/verdicts.csv, 단일 출처에서 1차 출처 확인)
F-0107(SEC 취하), F-1121(Coinbase FCM). F-1067, F-1198은 이미 1차라 생략.

## 반영하지 않은 것과 이유
- F-1115(Coinbase 설립 2012-06, 위키백과 기준): 승격 안 함. 회사 페이지는 연도 2012만 말하고 6월은 확인 못 했다. 본문은 새 F-1223 사용.
- 4, 5(Coinbase 예측시장, Prime과 Custody 출시일), 13(24 Hour Market과 Blue Ocean), 16(Kraken 예측시장): 보도만 또는 못 찾음이라 사실 행 없음.
- 17(Ondo 기본 투자설명서 갱신): 확인 못 함. FMA 승인 목록은 PDF 다운로드라 열지 않음.
- 10의 일부(Binance 기관 사업 출시 시점, BUSD, FDUSD, USYC): 못 찾음.
- 9의 "최대 20배, 24시간"은 캡처에 보이는 화면 밖 표 행을 로컬 세션이 읽은 값이다. 사실 행 원문 위치에 그렇게 적었다.
- 18의 SPCX는 개별 주식인지 화면에 표시가 없어 F-1239에 분류 미확인으로 넣었다. Bybit은 안 함.
- 15의 "30일 뒤 효력"은 로컬 세션 추정이라 쓰지 않았다.
