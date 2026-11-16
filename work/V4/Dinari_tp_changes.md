# Dinari v4 제3자 보고서 반영 바뀐 줄 (2026-11-16, 담당 A)

'+'는 넣은 줄. 지운 줄 없음(Kraken 아래 참고). db/facts.csv 변경 없음. db/third_party.csv에 TP-1xx 행 추가(work/TP-A/third_party.csv).

```diff
+● 규모 과거 대비
+  ★ 2026-01 초 300만 달러 7위(0.37%) → 11-16 1,520만 11위(0.41%) [TP-004][F-1027]
+  ★ 잔액 5.1배 [TP-004][F-1027]
+  ![rwa.xyz 순위표(Sentora 주간 글, 2026-01-09)](../captures/reports/W1_sentora_rwa_league_table_2026-01.png)
+● 제3자 시각
+  ★ 운영 모델이 Robinhood EU판과 거의 같음(포필러스, Securitize 후원, 2026-02 기준, 미국판 이전) [TP-117]
+  ★ 개인 수수료 네트워크 0.2~50달러, 주문 0.25~0.50%(포필러스, Securitize 후원, 미국 밖판) [TP-118]
+  ★ 배당의 5% 수취(포필러스, Securitize 후원, 미국 밖판) [TP-118]
+  ![간접 방식 흐름, Dinari는 미국 밖판에만 해당(포필러스, Securitize 후원, 2026-02)](../captures/reports/R1_p26_indirect_tokenization.png)
+● 제3자 시각
+  ★ 토큰은 Dinari 등록 이용자끼리만 이전(포필러스, Securitize 후원, 2026-02 기준) [TP-120]
+  ★ 배당은 USD+ 스테이블코인으로 지급(포필러스, Securitize 후원) [TP-120]
+  ![간접 방식 4사 비교표(포필러스, Securitize 후원, 2026-02, 미국판 이전)](../captures/reports/R1_p36_indirect_platforms_table.png)
+● 제3자 시각
+  ★ 표에 SEC 명의개서대리인, FINRA 증권사로 적힘(CoinDesk Research, Bullish 의뢰, 2026-08 기준) [TP-119]
+  ★ 표는 Dinari를 보관형으로 묶어 우리 분류와 다름(CoinDesk Research) [TP-119]
+● 제3자 평가
+  ★ 평가 1 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 39쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-117]
+    ① 원문 : "The operating model is almost identical to Robinhood’s Stock Tokens."
+    ② 번역 : 운영 모델은 Robinhood의 Stock Tokens와 거의 같다.
+    ③ 해석 : 2026-02 기준 미국 밖 dShares 설명으로 미국판(2026-08) 이전. 미국판은 계좌 속 주식 구조라 이 평가를 미국판에 옮기면 안 됨
+  ![평가 1 원문](../captures/reports/quotes/TP-117.png)
+  ★ 평가 2 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 39쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-118]
+    ① 원문 : "dShares carry a relatively high number of fees."
+    ② 번역 : dShares는 수수료 항목이 비교적 많다.
+    ③ 해석 : 개인 직접 이용 기준 수수료. 우리 본문의 파트너 API 요금(F-0336)과 대상이 다르므로 섞어 읽지 않음
+  ![평가 2 원문](../captures/reports/quotes/TP-118.png)
+  ★ 평가 3 : CoinDesk Research(Bullish 의뢰), 발행사 안내서 비교표, 2026-09-29(2026-08 기준), 10쪽, https://www.coindesk.com/research/the-future-of-equity-ownership-an-issuer-s-guide-to-tokenized-equities [TP-119]
+    ① 원문 : 표 칸 "Custodial tokenized equities", "Econ only", "Dinari-held", "SEC TA + FINRA BD"(Dinari 열)
+    ② 번역 : 보관형, 경제적 권리만, 장부는 Dinari가 보유, SEC 명의개서대리인과 FINRA 증권사.
+    ③ 해석 : 발행사 직접 방식을 미는 의뢰사 표. 미국판과 미국 밖판을 한 열로 묶어 우리 분류(미국판 보관형, 밖판 연계증권)와 다름. 표 원문은 칸 글자라 캡처 없음
```

## 비고
- R1은 미국판(2026-08) 이전, 미국 밖 dShares 설명이다. 줄과 평가 해석에 명시.
- R1 39쪽 출시일 2024-08-27은 쓰지 않음(8절 확인 담당이 따로 확인).
- R1 39쪽 수수료(개인 직접 기준: 네트워크 0.2~50달러, 주문 0.25~0.50%, 배당 5%)는 본문 F-0336(파트너 API 월 2,000달러, 주문당 0.20달러)과 대상이 달라 병기만 하고 우열을 두지 않음.
- 과거 대비 줄의 5.1배는 40자 한도 때문에 별도 줄로 분리.
- R2 10 표는 Dinari를 보관형 하나로 묶음. 우리 분류(미국판 보관형, 미국 밖판 연계증권)와 다름을 E에 한 줄로 적음.
