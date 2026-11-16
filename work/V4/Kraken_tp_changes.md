# Kraken v4 제3자 보고서 반영 바뀐 줄 (2026-11-16, 담당 A)

'+'는 넣은 줄. 지운 줄 없음(Kraken 아래 참고). db/facts.csv 변경 없음. db/third_party.csv에 TP-1xx 행 추가(work/TP-A/third_party.csv).

```diff
+● 규모 과거 대비
+  ★ 2026-01 초 1.95억 달러 2위(24.37%) → 11-16 6.77억 3위(18.26%) [TP-002][F-1023]
+  ★ 3.5배, 점유율 6.1%p 하락 [TP-002][F-1023]
+  ![rwa.xyz 순위표(Sentora 주간 글, 2026-01-09)](../captures/reports/W1_sentora_rwa_league_table_2026-01.png)
+● 제3자 시각
+  ★ 스위스 본사와 저지 SPV, 무기명 채무증권(포필러스, Securitize 후원, 2026-02 기준) [TP-114]
+  ★ 발행, 상환 수수료 0.5%, 보수 연 0.25% 도입 가능(포필러스, Securitize 후원, 문서 기재) [TP-114]
+  ![합성형 흐름(CoinDesk Research, Bullish 의뢰, 2026-09)](../captures/reports/R2_p08_synthetic.png)
+  ![간접 방식 흐름(포필러스, Securitize 후원, 2026-02)](../captures/reports/R1_p26_indirect_tokenization.png)
+● 제3자 시각
+  ★ 발행, 상환만 KYC, 이후 자유 유통(포필러스, Securitize 후원, 2026-02 기준) [TP-114]
+  ★ 거래 78%가 100달러 미만, 2025-07~10(포필러스, Securitize 후원) [TP-113]
+  ★ 위 78%는 Backed와 Ondo 합산, Kraken 단독 아님(포필러스, Securitize 후원) [TP-113]
+● 제3자 시각
+  ★ 100만 달러 교환 시 TSLAx 약 5%, NVDAx 최대 80% 밀림(Jupiter 탈중앙 거래소 기준, 포필러스, Securitize 후원, 2026-02 발간, 시점 미표기) [TP-111]
+  ★ 미국장 휴장 때 가격이 벌어질 수 있다고 xStocks 문서가 밝힘(CoinDesk Research, Bullish 의뢰, 2026-08 기준) [TP-112]
+  ★ Bybit xStocks 누적 거래대금 약 5.5억 달러(포필러스, Securitize 후원, 2026-02 이전) [TP-116]
+  ![간접 방식 4사 비교표(포필러스, Securitize 후원, 2026-02, Backed 열)](../captures/reports/R1_p36_indirect_platforms_table.png)
+● 제3자 시각
+  ★ 스위스법 준거, 리히텐슈타인 승인으로 EU 유통(포필러스, Securitize 후원) [TP-115]
+  ★ 유럽 판매는 키프로스 법인 인가, 그 법인이 직접 상대방(포필러스, Securitize 후원) [TP-115]
+● 제3자 시각
+  ★ 가능했던 이유 : 여러 관할 결합으로 EU 전역 유통(포필러스, Securitize 후원) [TP-115]
+  ★ 큰 금액 교환은 가격 밀림, 100만 달러 TSLAx 약 5%(포필러스, Securitize 후원) [TP-111]
+● 제3자 평가
+  ★ 평가 1 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 70쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-111]
+    ① 원문 : "For example, swapping $1M of TSLAx on Jupiter results in roughly 5% slippage, while NVDAx experiences slippage as high as 80%, rendering it effectively untradeable."
+    ② 번역 : 예를 들어 Jupiter에서 TSLAx 100만 달러를 교환하면 가격이 약 5% 밀리고, NVDAx는 최대 80%까지 밀려 사실상 거래할 수 없다.
+    ③ 해석 : 100만 달러 기준, 탈중앙 거래소 Jupiter 사례이며 Kraken 앱 체결과는 다름. 2026-02 발간 보고서라 현재 유동성과 다를 수 있음
+  ![평가 1 원문](../captures/reports/quotes/TP-111.png)
+  ★ 평가 2 : CoinDesk Research(Bullish 의뢰), 발행사 안내서, 2026-09-29, 15쪽, https://www.coindesk.com/research/the-future-of-equity-ownership-an-issuer-s-guide-to-tokenized-equities [TP-112]
+    ① 원문 : "xStocks’ documentation, for instance, notes that token prices may diverge from the underlying shares when U.S. markets are closed, liquidity is thin, or reference pricing is stale."
+    ② 번역 : 예컨대 xStocks 문서는 미국 시장 휴장, 유동성 부족, 기준 가격 지연 때 토큰 가격이 원주와 벌어질 수 있다고 밝힌다.
+    ③ 해석 : 발행사 직접 방식을 미는 의뢰사 글이라 래퍼 방식에 불리하게 쓴 면이 있으나 출처는 xStocks 자체 문서. 한국에서 가격 괴리 고지 기준에 참고
+  ![평가 2 원문](../captures/reports/quotes/TP-112.png)
+  ★ 평가 3 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 77쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-113]
+    ① 원문 : "In addition, an analysis of trading data from Backed Finance and Ondo between July and October 2025 shows that 78% of all trades were under $100."
+    ② 번역 : Backed와 Ondo의 2025년 7월~10월 거래 데이터를 보면 전체 거래의 78%가 100달러 미만이었다.
+    ③ 해석 : 두 발행사 합산 수치로 Kraken만의 값이 아님. 소액 개인 수요라는 방향만 참고
+  ![평가 3 원문](../captures/reports/quotes/TP-113.png)
```

## 비고
- 과거 대비 줄은 점검기의 40자 한도 때문에 두 줄(잔액 순위, 배수와 점유율 변화)로 나눔. 수치는 메인 지정값 그대로.
- R1 70쪽 가격 밀림: 100만 달러 교환, Jupiter(탈중앙 거래소) 기준, 보고서 2026-02 발간이며 측정 시점은 표기 없음.
- R1 77쪽 78%: Backed와 Ondo 합산 거래(2025-07~10). Kraken 단독 수치 아님을 줄에 밝힘.
- R1 37~38쪽 수수료 0.5%, 보수 0.25%는 문서 기재 2026-02 기준. 본문 F-0977(상한 5%, 연 5% 이내)과 다른 값이라 대조 필요(실제 부과 수준과 상한의 차이일 수 있음). db에는 넣지 않음.
- R2 15쪽(xStocks 휴장 때 가격 괴리)은 Bullish 의뢰 글이나 출처는 xStocks 자체 문서.
- 쓰지 않음: R1 37쪽 Backed 보관처 "스위스 규제 금융기관"(DB 은행, 중개사 세 곳 유지, 8절), R1 69~72 오라클, 담보 항목(Kraken 거래 장소 줄과 중복), R2 10 표 xStocks 열(가로 비교 몫).
