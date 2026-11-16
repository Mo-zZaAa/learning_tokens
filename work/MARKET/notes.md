# MARKET 노트 (열람 2026-11-16)

## 방법과 한계
- rwa.xyz 주식 페이지(app.rwa.xyz/stocks)는 셸 curl로 열리고 페이지 내장 데이터(__NEXT_DATA__)에 플랫폼별 표가 들어 있어 최신값(기준일 2026-11-16 03:55Z 갱신), 7일 전 값, 30일 전 점유율을 뽑았다. 같은 화면을 Playwright로 captures/market/에 저장.
- 일별 시계열 API(tokenTimeseries)는 curl에서 403(Request origin not allowed). 브라우저 안에서 호출하면 열릴 수 있으나 접근 제한을 피하는 것이라 하지 않았다. 따라서 rwa.xyz 안에서 약 1년 전(2025-11) 값은 얻지 못했다. 플랫폼 페이지에서는 90일 전(2026-08-18)까지만 나온다.
- market.csv의 "1년 전" 칸은 같은 출처가 아니다. Sentora 보고서 표(rwa.xyz 인용, 2026-01-16)이며 이것이 확인한 가장 이른 값이다. 2025-11 무렵 값은 없음. 시장 전체의 2025-11 무렵 값은 Alpaca 2025-12-04(수탁 4.8억 달러)와 한 기사의 2025-11-12 약 6.66억 달러(검색 요약, 열지 못함)뿐.
- Token Terminal, Dune 화면에서는 수치를 직접 얻지 못했다(Token Terminal은 소개 문구만, Dune은 403).
- Sentora 기준일 1월 16일은 검색 결과 요약에서 확인했고 CryptoSlate 표에는 날짜가 없다.

## 출처끼리 수치가 다른 곳
1. Ondo 점유율: Cointelegraph(RWA.xyz, 2026-03) 약 58%, Ondo 자사 주장(2026-05) 70% 이상, 이번 rwa.xyz 24.2%. 1월 Sentora 53.8%. 하락 원인은 bStocks(Binance)가 90일 전 5.55억에서 13.6억으로 늘어 1위가 된 영향으로 보이나, 분모 정의(분산형만 vs 전체)와 상품 분류 변경(rwa.xyz가 2025년 distributed와 represented로 나눔)도 영향. 확인 못함.
2. Ondo 잔액: 주식 표 8.99억, 플랫폼 페이지 42.24억(국채 등 전 자산군 포함), 회사 주장 TVL 10억(2026-05).
3. xStocks: 주식 표 6.77억, 플랫폼 페이지 7.01억(전 자산군).
4. 시장 전체 2026-01: rwa.xyz 대시보드 스크린샷(rwa.xyz 블로그, Robinhood 글) 9.13억, Sentora 6행 합계 8.47억, 보도 헤드라인 약 9.63억. 
5. Alpaca 수탁 점유율: 자사 94%(2025-12, 2026-07), Token Terminal 83.5%(2026-10), X 유통 85.8%(2026-10-29). 발행사 점유율과는 다른 지표.
6. Securitize: rwa.xyz 현재 49개 자산 2.65억, Sentora 1월 1개 자산 1.466억. 구성 정의가 달라 증감 비교 부적합.
7. Robinhood: 주식 표 1.49억(분산형). rwa.xyz 블로그(2026-01-27)에는 Robinhood 발행사 페이지가 represented 1,082만 달러로 표기. 같은 상품을 분산형과 represented 어느 쪽에 넣느냐에 따라 달라짐. 1월 Sentora 표에는 Robinhood 행 없음.
8. Coinbase: rwa.xyz 플랫폼 라벨 Coinbase Global 4,690만(343개 자산). Coinbase 자체 토큰화 주식 상품 전체인지 미확인.
9. 이름 매핑: rwa.xyz "xStocks"=Kraken 유통(발행 Backed), "Ondo"=Ondo Global Markets, "bStocks"=Binance(BTech Holdings Limited), "Robinhood"=Robinhood Stock Tokens, "Dinari"=dShares. Backed Finance는 별도 행(210만).

## 범위 밖 발견
- rwa.xyz 블로그 "Robinhood's Tokenized Stocks: The Good, The Bad, and The Fix"(2026-01-27)가 Robinhood 공급량 불일치를 다룸. 별도 조사 가치.
- Alpaca가 Ondo, xStocks, Binance, Robinhood, Coinbase의 수탁을 맡는다는 보도(Crypto Briefing 2026-10-29).
