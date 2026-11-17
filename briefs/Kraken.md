# Kraken 브리핑
- 축 : 인수로 미국 파생 인가 한 벌과 주식 토큰 발행사까지 사서, 선물과 주식 토큰을 발행부터 청산까지 한 그룹 안에서 처리
- 가설 : 다 한다, 거래, 은행, 자산관리, 기업용 인프라 네 기둥을 동시에 넓히고 현물 점유율 6.5%로 1등 아님

## 스토리라인 (PM 초안 반영)

### 1. 출발과 미국 안 기반
- 2011 미국 가상자산 거래소로 시작, 모회사 Payward [F-0176](https://www.payward.com/press-release/gtn-xstocks)
- 2020-09 와이오밍 특수목적 은행(SPDI) 인가: 가상자산 거래소 중 첫 미국 은행 인가, 제도권 금융 진입의 첫 발판 [F-1337](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[F-0378](https://www.kraken.com/prime)
- 지금은 연준 제한목적 마스터 계정까지 보유(회사 발표), 미국 달러 송금을 자체 계정으로 옮기는 중 [F-1254](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1259](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)

### 2. 자산: 선물은 인수로, 주식 토큰은 발행사째로
- 가상자산 선물은 2019 영국 Crypto Facilities 인수로 시작, 미국 밖 고객용 [F-1367](https://www.theblock.co/news/markets/2019-02-04-kraken-acquires-crypto-trading-platform-crypto-facilities-in-a-nine-figure-deal-10195)
- 미국 안 선물까지 약 6년이 걸린 이유
  - 2021-09 미국 고객에게 등록 없이 마진 거래를 제공해 CFTC 제재(125만 달러): 미국에서 하려면 선물중개업자(FCM) 등록이 필요 [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
  - 직접 등록은 기술과 인가에 돈과 시간이 너무 든다는 것이 CEO 설명 → 인가를 가진 회사를 사는 쪽을 택함 [F-1346](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 해석 : 실제 인수는 SEC가 Kraken 소송을 취하한 2025-03과 같은 달. 미국 규제 환경이 바뀐 시점에 몰아서 산 것으로 보임 [CASE-004](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26278)[F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)
- 미국 파생 인가 한 벌을 1년 안에 인수로 모음
  - 2025-05 NinjaTrader: 선물중개업자(FCM), 2025-07 미국 고객 CME 가상자산 선물 개시 [F-0177](https://www.financemagnates.com/cryptocurrency/kraken-completes-15b-ninjatrader-acquisition-as-funded-accounts-jump-26-in-q1/)[F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)
  - 2025-10 Small Exchange: 선물거래소(DCM) [F-1116](https://blog.kraken.com/news/acquires-small-exchange)
  - 2026-05 Bitnomial: 중개, 거래소, 청산소(FCM, DCM, DCO) 모두 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
  - 그 위에 미국 주식 무기한선물을 CFTC와 SEC에 함께 신청(2026-09) [F-1189](https://www.payward.com/press-release/payward-single-stock-perpetual-futures-filing)
- 주식 토큰: 2025-06 xStocks 출시는 발행사 Backed(저지 법인, 저지는 발행사 자체에 금융 인가를 요구하지 않음)가 만들고 Kraken이 판매 → 2025-12 Backed를 인수해 발행까지 그룹 안으로 [F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)F-0940[F-0139](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion)
  - CEO 설명 : 발행부터 결제까지 수직 통합 [F-1043](https://blog.kraken.com/news/backed-acquisition)
- Nasdaq과의 역할 분담(2026-09)
  - Nasdaq이 Payward에 1억 달러 투자, Payward는 Nasdaq 시장감시 기술을 모든 거래장에 도입 [F-1119](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)[F-1255](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)
  - Nasdaq은 허가형 시장의 토큰 주식(Nasdaq Equity Tokens, 2027 예정), Payward는 그 보유자의 신원확인 온보딩과 초기 정산 계층, 그리고 xStocks 쪽 무허가 시장과 잇는 게이트웨이 [F-0160](https://www.payward.com/press-release/payward-partners-with-nasdaq)[F-1044](https://blog.kraken.com/news/payward-partners-with-nasdaq)
  - 해석 : 거래소가 못 하는 신뢰는 Nasdaq에게서 빌리고, 두 토큰 시장 사이 연결이라는 빈자리를 Kraken이 먼저 차지하는 구조. 회사도 "살 수 없는 신뢰와 입지는 기존 기관과 제휴"를 인수 기준으로 밝힘 [F-1349](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)

### 3. 비전: 개인 거래소에서 기업용 금융 인프라로
- 그 전: 기관은 별도 전략보다 기존 기능을 기관이 쓰는 수준 → 2024-03 Kraken Institutional, 2025-06 Prime(거래, 수탁, 금융 한 계정) [F-1339](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[F-1159](https://blog.kraken.com/product/kraken-prime/introducing-kraken-prime)
- 지금: CEO가 사업 네 기둥 중 하나로 기업용 인프라 Payward Services를 명시 [F-1347](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 무엇 : Kraken용으로 만든 수탁, 유동성, 규제 준수, 결제와 정산을 은행, 핀테크, 증권사, 가상자산 플랫폼에 API로 [F-1350](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 누구 : 최소 25개 기업, 예 bunq(Embed), OKX(xStocks 기반 토큰 주식), WOO X EU(수탁), Hyperliquid [F-1366](https://www.coindesk.com/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)[F-1374](https://www.businesswire.com/news/home/20250429878133/en/Kraken-Launches-Embed-a-Crypto-as-a-Service-Enabling-Banks-and-Fintechs-to-Provide-Clients-Seamless-Access-to-Crypto)[F-1257](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 다른 트랙도 기업용으로 다시 붙이는 중(로드맵) : 파생 인가 한 벌(FCM, DCM, DCO), 파트너 앱 안 지갑, 파트너 자체 브랜드 xStocks, 비상장사 온체인 공모 xPO [F-1258](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 결제
  - 2026-07 Reap 인수(최대 6억 달러): 스테이블코인 카드 발급, 국경 간 송금, 기업 재무관리를 Payward Services에 추가 [F-1195](https://www.payward.com/press-release/payward-reap-close)[F-1355](https://www.tokenpost.kr)
  - 어디부터 : Reap이 가진 인가로 아시아태평양과 미주, Payward의 EU, 미국 인가로 Reap의 유럽, 미국 진출, Visa와 100개 이상 시장에 스테이블코인 카드 [F-1256](https://www.payward.com/press-release/payward-reap-close)
  - 은행 쪽 : 미국은 연준 계정, EU는 Saldo Bank 인수(2027 종결 예정)로 예금과 대출을 자기 대차대조표에 [F-1259](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)[F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)
  - 결제를 노리는 다른 곳 : Coinbase(2026 우선순위에 스테이블코인과 결제, USDC), Robinhood(Robinhood Banking), Binance(Binance Pay, 카드) [F-0113](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-1158](https://www.robinhood.com/us/en/newsroom/introducing-strategies-banking-and-cortex)[F-0723](https://www.binance.com/en/about-legal/binance-card-global)

### 4. 시장: 거점 하나로 먼저 팔고, 큰 시장은 직접 인가, 빡센 곳은 현지 인가 가진 파트너
- 거점 버뮤다 한 곳 : 2024-08 디지털자산 Class F 인가 한 장(거래소, 파생 거래소, 수탁)으로 버뮤다 법인이 미국 밖 고객의 현물, 파생, xStocks 중개 [F-1416](https://www.bma.bm/regulated-entities)[F-1369](https://support.kraken.com/articles/where-is-kraken-licensed-or-regulated)
  - 이 한 장으로 되는 이유 : xStocks는 판매국 증권 감독기관에 등록하지 않고, 버뮤다 법인이 여러 나라 고객을 직접 받음 → xStocks 출시 직후 140개국 이상 [F-0391](https://www.kraken.com/xstocks)[F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)
- 큰 시장 EU : 인가 없이는 못 파는 큰 시장이라 직접 확보
  - 가상자산 : 이미 7개국 국가별 등록으로 영업 중 → MiCA가 2026-07부터 인가를 의무화 → 2025-06 아일랜드 MiCA 인가로 EU 단일 인가 [F-1438](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)[F-1440](https://www.fsma.be/en/news/crypto-assets-service-providers-end-transitional-period)[F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
  - 파생, 주식 토큰(증권) : 2025-02 키프로스 투자회사 인수(MiFID) → 2025-05 EU 규제 파생, 2026-05 xStocks EU 판매 계약 [F-1370](https://blog.kraken.com/news/eu-mifid-license)[F-1342](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))F-0920
  - 미국에서 연 것을 EU로 옮기는 중 : 은행(Saldo Bank), 결제(Reap 유럽 진출) [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1256](https://www.payward.com/press-release/payward-reap-close)
- 규제가 더 엄격한 상장주 시장 : 현지 인가를 가진 파트너 GTN이 집행, 수탁, 기관 판매를 맡음, 독일은 Deutsche Boerse 360X [F-1084](https://www.payward.com/press-release/gtn-xstocks)[F-0175](https://www.payward.com/press-release/xstocks-dax-40)
- 자산 순서 : 가상자산 → 미국 주식 토큰 → 영국, EU 상장주 200종 이상(DAX 40 전부, 2026-11) → 홍콩 → 영국, 유럽, 한국 상장자산(계획), LSE 상장 2027 예정 [F-1360](https://www.hosu-news.com/news/articleView.html?idxno=187188)[F-0170](https://www.payward.com/press-release/gtn-xstocks)[F-0174](https://www.payward.com/press-release/xstocks-uk-eu-equities)
- 해석 : 수요 확인은 인가 한 장으로 넓게 파는 버뮤다에서, 돈이 큰 시장(EU)은 직접 인가, 직접 못 들어가는 상장주 시장은 현지 인가를 가진 파트너

### 5. 청산소까지: 가상자산 거래소라는 정체성을 벗는 중
- Bitnomial 인수로 미국 파생에서 중개, 거래소, 청산을 모두 그룹 안에 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
- 당국과의 관계
  - 2025 이후 : SEC 소송 취하(2025-03), 연준 계정 보유(회사 발표), CFTC와 SEC에 공동 신청 [CASE-004](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26278)[F-1254](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1189](https://www.payward.com/press-release/payward-single-stock-perpetual-futures-filing)
  - 그 전 : 2015 뉴욕 철수, 2021 CFTC 제재, 2022 OFAC 제재, 2023 SEC 스테이킹 합의 [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[CASE-003](https://www.sec.gov/newsroom/press-releases/2023-25)
  - 해석 : 처음부터 사이가 좋았던 것이 아니라 2025 이후 규제 환경이 바뀌면서 인가를 직접 갖추는 쪽으로 돌아선 것. 제재를 받던 "등록 없이 팔던 거래소"에서 "인가를 다 가진 금융회사"로 바꾸는 것이 인수 연쇄의 목적으로 읽힘

### 6. KSF: 인가를 가진 회사만 골라 사고, 산 회사를 그대로 굴림
- 사는 대상의 공통점 : 이미 인가를 가진 곳(FCM NinjaTrader, DCM Small Exchange, FCM+DCM+DCO Bitnomial, EU 증권 키프로스 투자회사, 결제 Reap, EU 은행 Saldo) [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)[F-1116](https://blog.kraken.com/news/acquires-small-exchange)[F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)[F-1370](https://blog.kraken.com/news/eu-mifid-license)[F-1195](https://www.payward.com/press-release/payward-reap-close)[F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)
- 산 뒤 방식 : 기존 인가와 브랜드, 경영진을 유지한 채 그룹에서 운영(Bitnomial, Reap) → 인가를 새로 받는 시간 없이 바로 상품 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)[F-1256](https://www.payward.com/press-release/payward-reap-close)
- 효과 : NinjaTrader 인수 두 달 뒤 미국 선물 개시, Backed 인수 뒤 xStocks 누적 거래 450억 달러 초과 [F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)[F-0166](https://www.payward.com/press-release/xstocks-surpasses-1-billion-aum)
- 기준 : 쇼핑 목록 없이 인프라 공백인지, 고객이 원하는 역량인지로 판단 [F-1349](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)

### 7. 가설: 비상장 모회사라서 가능한 속도
- Payward는 비상장(2025-11 상장 서류 비공개 제출, 2027 Q2 전 상장 계획 없음), 외부 자금 없이 운영 가능, 2026 Q3 조정 EBITDA 6천만 달러 [F-1352](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)[F-0180](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 투자자는 Citadel Securities, Nasdaq 같은 전략적 투자자 [F-1352](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
- 해석 : 분기 실적 압박이 없는 비상장 회사라 1년 반 동안 27.5억 달러 이상(공개분)의 인수를 연달아 할 수 있었고, Nasdaq, Citadel 같은 전통 금융 주주가 인가와 제휴에서 신뢰를 보태는 것으로 보임. 상장을 미루는 것도 인가 모으기를 먼저 끝내려는 순서로 볼 수 있음 [F-1355](https://www.tokenpost.kr)

## 1층 (키워드)
- 시작 : 가상자산 현물 거래소(2011, 모회사 Payward)
- 붙인 것
  - 파생 : Crypto Facilities(2019), NinjaTrader, Small Exchange, Bitnomial(모두 인수)
  - 주식, 주식 토큰 : 미국 주식(직접) → xStocks 판매(파트너) → 발행사 Backed(인수) → 해외 상장주 GTN(파트너)
  - 은행, 결제 : 와이오밍 은행 인가(직접), Reap(인수), EU 은행 Saldo(인수)
  - 기업, 기관용 : Embed, Prime(직접), 시장감시 Nasdaq(파트너)
  - 해외 인가 : 버뮤다 파생 거래장(직접), 키프로스 투자회사(인수)
- 지금 하는 것 : 거래, 은행, 자산관리, 기업용 인프라(2026 Q3 플랫폼 거래량 3,530억 달러, 총플랫폼마진 4.87억 달러)
- 해외 진출
  - 미국 밖 여러 나라 : 버뮤다 법인으로 판매(판매국 인가 없음)
  - EU : 직접 인가(아일랜드) + 인수(키프로스)
  - 홍콩, 영국, EU 상장주 : 파트너(GTN), 독일 파트너(360X)
  - 아시아태평양 결제 : 인수(Reap)

## 2층 (받치는 사실)
- 시작 : 2011-07 설립, 거래소 이름은 Kraken, 숫자와 인수 주체는 모회사 Payward [F-1109](https://www.payward.com/about)
- 파생 시작 : 2019-02 영국 FCA 규제 파생 거래소 Crypto Facilities 인수, 1억 달러 이상(The Block 보도) [F-1367](https://www.theblock.co/news/markets/2019-02-04-kraken-acquires-crypto-trading-platform-crypto-facilities-in-a-nine-figure-deal-10195)
- 미국 파생 인가 셋 인수 : NinjaTrader(선물 중개 FCM) 약 15억 달러 2025-03 발표 [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader), Small Exchange(선물 거래소 DCM) 1억 달러 2025-10 [F-1116](https://blog.kraken.com/news/acquires-small-exchange), Bitnomial 2026-05-01 완료로 FCM, DCM, DCO(청산소) 모두 보유 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
- 발행사 인수 : xStocks 발행사 Backed 2025-12-02 인수 합의, 2026-01 지분 100% [F-0139](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion)
- 지금 규모 : 2026 Q3 플랫폼 거래량 3,530억 달러, 총플랫폼마진 4.87억 달러, 조정 EBITDA 6천만 달러, 자금 계정 710만 개 [F-0180](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 현물 점유율 : 업계 현물 거래량 대비 6.5%(2026-09), 1년 전 3.3% [F-1247](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 주식 토큰 : xStocks 누적 거래량 450억 달러 초과, 보유자 55만 초과(2026-10 발표) [F-0166](https://www.payward.com/press-release/xstocks-surpasses-1-billion-aum)
- EU : 2025-02 키프로스 투자회사 인수로 MiFID 인가 [F-1370](https://blog.kraken.com/news/eu-mifid-license), 2025-06 아일랜드 MiCA 인가로 EEA 30개국 영업권 [F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
- 미국 밖 판매 : 버뮤다 Payward Digital Solutions Class F 인가 2024-08-01 [F-1416](https://www.bma.bm/regulated-entities), xStocks 제공 법인이며 판매국 증권 규제기관에는 등록하지 않음(Payward 발표) [F-0154](https://www.payward.com/press-release/xstocks-one-year)
- 파트너와 결제 : GTN 제휴 1단계로 영국, EU 상장주 200종 이상 xStocks 배포 [F-0174](https://www.payward.com/press-release/xstocks-uk-eu-equities), Reap 기존 인가로 아시아태평양과 미주 확장(2026-07 인수 완료) [F-1256](https://www.payward.com/press-release/payward-reap-close)

## 3층 (꼬리질문 대비)
- Q : Bitnomial 인수 금액은? / A : 5.5억 달러, 현금과 주식(코인데스크 보도), 회사 완료 발표에는 금액 없음 [F-1345](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
- Q : 왜 직접 만들지 않고 샀나? / A : 미국 선물 중개업체를 처음부터 세우면 기술과 규제 승인에 비용과 시간이 많이 든다는 Sethi 공동 CEO 설명(코인데스크 보도) [F-1346](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
- Q : 인수에 쓴 돈은 모두 얼마? / A : 공개 금액만 최소 27.5억 달러(NinjaTrader 15억, Small Exchange 1억, Bitnomial 최대 5.5억, Reap 최대 6억), Backed는 비공개(토큰포스트 보도) [F-1355](https://www.tokenpost.kr)
- Q : Backed 인수 조건은? / A : 금액 비공개, 2026-01-05경 Payward Europe Limited가 Backed Finance AG 주식 100% 매입 F-0939(Backed 기본 투자설명서 PDF)
- Q : xStocks를 사면 주식을 갖나? / A : 아님, 저지 발행사에 대한 상환금 채권, 기초주는 발행사가 1:1 담보로 보유 F-0991(Backed 기본 투자설명서 텍스트), Payward는 발행사 채무를 보증하지 않음 F-0924(Backed 투자설명서 2차 보충서 PDF)
- Q : SEC와의 문제는? / A : 2023-02 스테이킹 미등록 공모 쟁점으로 합의, 서비스 중단과 3천만 달러 납부 [CASE-003](https://www.sec.gov/newsroom/press-releases/2023-25), 2023-11 별건 소송은 2025-03 취하 [CASE-004](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26278)
- Q : 그 밖의 제재 이력은? / A : 2021-09 CFTC 미등록 마진거래 125만 달러, 2022-11 OFAC 이란 제재 위반 36.2만 달러, 2024 호주 ASIC 벌금 800만 호주달러(위키백과 정리) [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
- Q : 어느 나라에 xStocks를 못 파나? / A : 미국, 캐나다, 영국, 호주에서 접근 불가 [F-0393](https://www.kraken.com/xstocks)
- Q : 주식 토큰 1등인가? / A : 발행 잔액 기준 3위 6.8억 달러, 1위 Binance 13.6억 달러(rwa.xyz 제3자 집계, 2026-11-16) [F-1023](https://app.rwa.xyz/stocks), 누적 거래량 450억 달러는 회사 발표라 다른 지표
- Q : Coinbase와 차이는? / A : Kraken은 미국 파생 인가 셋을 모두 인수, Coinbase는 선물 거래소만 인수하고 중개(FCM)는 2023-08 직접 등록 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717), 청산소(DCO)는 2026-09 직접 등록 [F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)
