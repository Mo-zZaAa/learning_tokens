# STORY-Robinhood 리서치 노하우 (2026-11-17)

- robinhood.com/newsroom/<slug>/ 는 curl로 열림(investors.robinhood.com, globenewswire.com은 403). 글 목록은 사이트 전수조사 inventory.csv의 sitemap-newsroom.xml 행(473건)에서 slug로 찾는다. 2016 Gold, 2017 옵션, 2018 가상자산, 2018 자체 청산, 2019 영국 발표, 2022 Ziglu, 2023 X1 같은 옛 글도 남아 있다. 날짜는 HTML 안 "datePublished".
- 과거 실적 발표: 전수조사 사본에 2023 Q1에서 Q4, 2026 Q2, Q3 보도자료가 있다. 2024 Q4 보도자료는 GlobeNewswire 배포본을 실은 manilatimes.net(tmt-newswire/globenewswire 경로)가 curl로 열림.
- 10-Q(node__16931__html.md) MD&A에 매출 항목별 비중 표(옵션, 이벤트 계약, 암호화폐, 주식, 순이자 세부, 기타 안 Gold 구독료)가 있다. 수익 구성 변화는 이 표와 2023 보도자료를 이어 쓰면 된다. 위험요인에 창업자 의결권(12% 지분, 50% 초과 의결권), 규제 절에 Bitstamp 법인별 인가가 있다.
- 사업 기둥 원문은 2026 Q2, Q3 보도자료 Highlights 표제(#1 Platform for Active Traders, #1 in Wallet Share for the Next Generation, #1 Global Financial Ecosystem). 처음 쓴 시점을 보도자료로 확정하지 못함(2024 Q4 보도자료는 Active Traders 표제만). 통화 녹취 사이트(roic.ai, marketbeat)와 investing.com은 403.
- 막힌 매체: theblock.co, crowdfundinsider, blockworks(403), yahoo(429). 같은 사건은 financemagnates.com, bankingdive.com, amp.cnn.com이 열림.
- 함정: Robinhood 예측시장은 Kalshi를 대체한 것이 아니라 Kalshi, ForecastEx, Rothera, Crypto.com으로 나눠 보냄(2026-09 뉴스룸). "파트너 뒤 인수"를 "교체"로 쓰지 않는다.
