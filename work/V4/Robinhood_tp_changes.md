# Robinhood v4 제3자 보고서 반영 바뀐 줄 (2026-11-16, 담당 A)

'+'는 넣은 줄. 지운 줄 없음(Kraken 아래 참고). db/facts.csv 변경 없음. db/third_party.csv에 TP-1xx 행 추가(work/TP-A/third_party.csv).

```diff
+● 출발 사업 수익 구조
+  ★ 고객 주문을 Citadel로 보내고 PFOF를 받음(포필러스, Securitize 후원, 2026-02) [TP-110]
+  ★ 필자는 무수수료를 착시로 서술(포필러스) [TP-110]
+● 규모 과거 대비
+  ★ 2026-01 초 rwa.xyz 표에는 없음(집계 전) [TP-005]
+● 제3자 시각
+  ★ EU 법인이 원주 사고 파생계약 토큰 지급(포필러스, Securitize 후원, 2026-02 기준이라 지갑판 이전) [TP-104]
+  ★ 투자자는 EU 법인 상대 계약상 청구권 보유(포필러스, Securitize 후원) [TP-104]
+  ![합성형 흐름(CoinDesk Research, Bullish 의뢰, 2026-09)](../captures/reports/R2_p08_synthetic.png)
+  ![간접 방식 흐름(포필러스, Securitize 후원, 2026-02)](../captures/reports/R1_p26_indirect_tokenization.png)
+● 제3자 시각
+  ★ 담보 서비스 없음, 원주 상환 불가(포필러스, Securitize 후원, 2026-02 기준) [TP-106]
+  ★ 앱 안에서만 거래, 회사가 상대방 겸 유동성 공급자(포필러스, Securitize 후원) [TP-102]
+  ★ 출금 제한으로 자산이 자체 플랫폼에 머문다는 보도, 지갑판 출시 전 상태(Finance Magnates, 2026-03) [TP-107]
+  ![간접 방식 4사 비교표(포필러스, Securitize 후원, 2026-02, 지갑판 이전)](../captures/reports/R1_p36_indirect_platforms_table.png)
+● 제3자 시각
+  ★ 리투아니아 인가로 EEA 30여 개국 판매(포필러스, Securitize 후원, 2026-02 기준) [TP-105]
+  ★ MiFID II 장외 파생이라 회사가 직접 상대방(포필러스, Securitize 후원) [TP-105]
+  ★ 장부 기록 의무가 없어 분산원장 사용 가능(포필러스, Securitize 후원 설명) [TP-105]
+  ![리투아니아 역할 분담(포필러스, Securitize 후원, 2026-02, 표 출처 Dan Kim LawVax)](../captures/reports/R1_p56_robinhood_lithuania_table.png)
+● 제3자 시각
+  ★ 가능했던 이유 : 장외 파생이라 시범제도 면제 불필요(포필러스, Securitize 후원) [TP-105]
+● 제약과 리스크 대조(제3자)
+  ★ 비상장 토큰은 소유권과 상환 없음, OpenAI 승인 부인(포필러스, Securitize 후원) [TP-108]
+  ★ IOSCO 각주가 Robinhood 비상장 토큰 보도를 사례로 듦(IOSCO, 감독기구) [TP-109]
+● 제3자 평가
+  ★ 평가 1 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 29쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-101]
+    ① 원문 : "From a personal perspective, I also view indirect tokenization as a transitional approach."
+    ② 번역 : 개인적으로 나는 간접 토큰화를 과도기 방식으로 본다.
+    ③ 해석 : 직접 방식을 쓰는 후원사 쪽 보고서의 견해. 인가 없이 낸 간접 방식이 규제 명확화 뒤에도 남을지가 KDX가 볼 점
+  ![평가 1 원문](../captures/reports/quotes/TP-101.png)
+  ★ 평가 2 : 포필러스(Securitize 후원), 주식 토큰화 보고서, 2026-02-23, 69쪽, https://4pillars.io/en/reports/2026-the-year-of-tokenized-stocks [TP-102]
+    ① 원문 : "Robinhood acts as both counterparty and liquidity provider, internalizing user order flow within its platform."
+    ② 번역 : Robinhood은 상대방이자 유동성 공급자로서 이용자 주문을 자기 플랫폼 안에서 내부 처리한다.
+    ③ 해석 : 2026-02 기준이라 자체 체인과 지갑판 이전 설명. 회사가 상대방을 겸하는 구조의 이해상충 고지가 KDX가 볼 점
+  ![평가 2 원문](../captures/reports/quotes/TP-102.png)
+  ★ 평가 3 : CoinDesk Research(Bullish 의뢰), 발행사 안내서 비교표, 2026-09-29(2026-08 기준), 10쪽, https://www.coindesk.com/research/the-future-of-equity-ownership-an-issuer-s-guide-to-tokenized-equities [TP-103]
+    ① 원문 : 표 칸 "Synthetic tokenized equities", "Derivative", "Debt / no rights", "Shadow / no consent"(Robinhood 열)
+    ② 번역 : 합성형 토큰 주식, 파생, 채무이고 주주권 없음, 발행사 동의 없는 구조.
+    ③ 해석 : 발행사 직접 방식에 유리한 의뢰사 표라 낮게 매긴 면이 있음. 지갑판 반영 표라 EU판과 구분해 읽어야 함. 표 원문은 이미지 아닌 칸 글자라 캡처 없음
```

## 비고
- R1은 2026-02 기준(지갑판, 자체 체인 이전). 줄마다 기준 시점을 적음. W2 출금 제한은 2026-03 보도, 지갑판 2026-07 출시 전 상태로 표시.
- R1 85 대조: 기존 F-0222(OpenAI 반박, 리투아니아 중앙은행 설명 요구)와 내용이 같음. R1이 더하는 것은 "상환 불가, 소유권 없음"뿐이라 한 줄만 넣음.
- R2 10 표 칸은 이미지가 아니라 표 글자라 인용 캡처 없음(TP-103). 원문 칸의 가운뎃점은 "/"로 바꿔 적음.
- R1 56 표(Robinhood이 SPV로 원주 매수)는 본문 F-0641(헤지용 매수, 보유 의무 없음)과 같은 방향. 그림만 붙임.
- 쓰지 않음: R1 36~37 중 Arbitrum, 자체 L2 예정(기존 줄과 중복, 시점 이전).
