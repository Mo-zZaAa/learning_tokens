# Kraken 브리핑
- 축 : 인수로 미국 파생 인가 한 벌과 주식 토큰 발행사까지 사서, 선물과 주식 토큰을 발행부터 청산까지 한 그룹 안에서 처리
- 가설 : 다 한다, 거래, 은행, 자산관리, 기업용 인프라 네 기둥을 동시에 넓히고 현물 점유율 6.5%로 1등 아님

## 스토리라인 (PM 초안 반영)

### 1. 출발: 오래된 가상자산 거래소가 은행 인가로 제도권 문을 엶
- Kraken은 2011년에 시작한 가상자산 거래소이고, 모회사 Payward 아래에서 거래소 하나로 10년 가까이 자람 [F-0176](https://www.payward.com/press-release/gtn-xstocks)
  - 이 시기 확장은 작은 거래소 인수로 고객과 통화를 넓히는 정도(2016 뉴욕 Coinsetter, 캐나다 Cavirtex, 네덜란드 CleverCoin) [F-1335](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
- 2019-02 영국 Crypto Facilities를 1억 달러 넘게 주고 사면서 처음으로 "현물 옆에 파생"을 붙임. 이유는 고객이 현물과 선물을 한 곳에서 거래하게 하려는 것, 당시 최대 인수 [F-1367](https://www.theblock.co/news/markets/2019-02-04-kraken-acquires-crypto-trading-platform-crypto-facilities-in-a-nine-figure-deal-10195)
  - 다만 영국 회사라 이 선물은 미국 밖 고객용. 미국 고객에게는 열 수 없는 상태로 출발 [F-1336](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
- 2020-09 와이오밍 특수목적 은행(SPDI) 인가: 가상자산 거래소 중 처음 받은 미국 은행 인가 [F-1337](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
  - 미국 회사였지만 이때부터 "거래소"가 아니라 "은행 인가를 가진 금융회사"로 제도권에 들어서는 첫 발판이 됨. 이 은행 법인이 지금의 수탁을 맡음 [F-0377](https://www.kraken.com/institutions/custody)
  - 그 연장선에서 지금은 연준 제한목적 마스터 계정까지 갖고(회사 발표), 미국 달러 송금을 남의 은행 대신 자기 계정으로 옮기는 중 [F-1254](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1259](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)

### 2. 자산: 선물로 재미를 보고, 미국 안에서 하려고 인가를 통째로 삼
- 미국 밖에서는 선물이 이미 돈이 되는 사업이었는데, 미국 안에서는 6년 가까이 못 함
  - 이유 1 : 2021-09 미국 고객에게 등록 없이 마진 거래를 제공했다가 CFTC 제재(125만 달러). 미국에서 레버리지 상품을 팔려면 선물중개업자(FCM) 등록이 반드시 필요하다는 것이 확인됨 [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
  - 이유 2 : 직접 등록하면 기술과 인가에 돈과 시간이 너무 든다는 것이 CEO 설명. 그래서 "만들지 말고 산다"로 정함 [F-1346](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 이유 3(해석) : 당국과 소송 중이던 시기에는 인수도 쉽지 않았음. 실제 인수 발표는 SEC가 Kraken 소송을 취하한 2025-03과 같은 달 [CASE-004](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26278)[F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)
- 그래서 1년 사이 미국 파생 인가를 한 벌로 모음
  - 2025-05 NinjaTrader(선물중개업자, 15억 달러): 인수 두 달 뒤인 2025-07 미국 고객에게 CME 가상자산 선물을 처음 엶 [F-0177](https://www.financemagnates.com/cryptocurrency/kraken-completes-15b-ninjatrader-acquisition-as-funded-accounts-jump-26-in-q1/)[F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)
  - 2025-10 Small Exchange(선물거래소, 1억 달러): 남의 거래소에 주문을 넘기던 데서 자기 거래소를 갖게 됨 [F-1116](https://blog.kraken.com/news/acquires-small-exchange)
  - 2026-05 Bitnomial(중개, 거래소, 청산소 셋 다, 5.5억 달러): 미국 파생의 마지막 칸인 청산까지 그룹 안으로 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)[F-1345](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 이 인가 한 벌 위에 미국 주식 무기한선물을 CFTC와 SEC에 함께 신청(2026-09), 미국 고객용 온체인 무기한선물도 예고. 산 인가들이 다음 상품의 바탕이 됨 [F-1189](https://www.payward.com/press-release/payward-single-stock-perpetual-futures-filing)[F-1190](https://www.payward.com/press-release/payward-hyperliquid-onchain-perpetual-futures)
- 같은 시기에 주식으로도 넓힘. 미국 안은 직접, 미국 밖은 주식 토큰
  - 미국 안 : 2025-04 실물 주식 거래 시작(중개는 Alpaca), 지금 11,000종 이상, 일부 주만 [F-1338](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[F-0420](https://www.kraken.com/stocks)[F-0422](https://www.kraken.com/stocks)
  - 미국 밖 : 2025-06 xStocks 출시. 처음엔 직접 만들지 않고 저지의 발행사 Backed가 만든 토큰을 Kraken이 팔았음. 저지는 발행사 자체에 금융 인가를 요구하지 않아 발행 부담이 가벼운 곳 [F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)F-0940
  - 팔아 보니 커짐(운용자산 2026-02 2.25억 달러 → 10억 달러 초과) → 2025-12 Backed를 통째로 사서 발행까지 그룹 안으로. CEO 설명은 "발행부터 결제까지 수직 통합" [F-0165](https://www.payward.com/press-release/xstocks-surpasses-1-billion-aum)[F-0139](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion)[F-1043](https://blog.kraken.com/news/backed-acquisition)
  - 그 결과 xStocks 누적 거래 450억 달러 초과, 보유자 55만 초과, 해외 개인의 미국 IPO 참여(IPO Access)까지 붙임 [F-0166](https://www.payward.com/press-release/xstocks-surpasses-1-billion-aum)[F-1046](https://blog.kraken.com/product/xstocks/spacex-ipo-access)
- Nasdaq과는 짝을 맞춰 역할을 나눔(2026-09)
  - Nasdaq이 Payward에 1억 달러를 넣고, Payward는 Nasdaq 시장감시 기술을 자기 모든 거래장에 깜 [F-1119](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)[F-1255](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)
  - Nasdaq은 허가형 시장의 토큰 주식(2027 예정)을 내고, Payward는 그 보유자의 신원확인 온보딩과 초기 정산을 맡으며, xStocks가 도는 무허가 시장과 Nasdaq 토큰 시장을 잇는 연결 통로를 같이 만듦 [F-0160](https://www.payward.com/press-release/payward-partners-with-nasdaq)[F-1044](https://blog.kraken.com/news/payward-partners-with-nasdaq)[F-0159](https://www.payward.com/press-release/payward-partners-with-nasdaq)
  - 해석 : 규칙이 아직 없는 주식 토큰 시장에서 Nasdaq의 신뢰와 감시 기술을 먼저 들여와 "믿을 만한 쪽"이 되고, 두 시장 사이 길목을 선점하는 구조. 회사도 인수 기준에서 "살 수 없는 신뢰와 입지는 Nasdaq, LSE 같은 기존 기관과 제휴"라고 밝힘 [F-1349](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)

### 3. 비전: 개인 거래소에서 기업이 빌려 쓰는 금융 인프라로
- 예전 기관 사업은 따로 전략이 있었다기보다, 거래소가 가진 것 중 기관이 좋아할 기능을 묶어 파는 정도
  - 2024-03 기관 전담 부문, 2025-06 Prime(펀드, 은행, 기업 재무부서를 위한 거래, 수탁, 금융 한 계정) [F-1339](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[F-1159](https://blog.kraken.com/product/kraken-prime/introducing-kraken-prime)[F-0439](https://www.kraken.com/prime)
- 지금은 CEO가 회사를 "지주회사가 아니라 플랫폼 하나, 대차대조표 하나, 규제 체계 하나"로 부르고, 사업 네 기둥 중 하나로 기업용 인프라 Payward Services를 명시 [F-1347](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 무엇을 파나 : Kraken 자신이 쓰려고 만든 수탁, 유동성, 규제 준수, 위험관리, 결제와 정산을 은행, 핀테크, 증권사, 다른 가상자산 거래소에 API로 [F-1350](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - 누가 쓰나 : 최소 25개 기업. 네덜란드 은행 bunq는 수 주 만에 자기 앱에 가상자산 거래를 넣었고, 경쟁 거래소 OKX는 xStocks를 받아 자기 주식 토큰을 냄 [F-1366](https://www.coindesk.com/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)[F-0452](https://www.kraken.com/institutions/banks)[F-1257](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
  - 돈도 이쪽으로 옮겨 가는 중 : 2026 Q3 총플랫폼마진 4.87억 달러 중 52%가 거래 수수료가 아닌 자산 기반과 접근 기반 [F-1245](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 이미 있는 다른 트랙도 기업용으로 다시 꽂는 중
  - 인수로 모은 미국 파생 인가 한 벌(FCM, DCM, DCO)을 파트너에게 그대로 빌려줌, 파트너 앱 안 지갑, 파트너 자체 브랜드 xStocks, 비상장사가 자기 주식을 토큰으로 공모하는 xPO [F-1258](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 결제까지 넘봄
  - 2026-07 Reap 인수(최대 6억 달러): 스테이블코인 카드 발급, 국경 간 송금, 기업 재무관리. 개인 결제가 아니라 기업 결제를 먼저 잡는 형태 [F-1195](https://www.payward.com/press-release/payward-reap-close)[F-1355](https://www.tokenpost.kr)
  - 어디부터 어떻게 : Reap 브랜드와 경영진은 그대로 두고, Reap이 이미 가진 인가로 아시아태평양과 미주부터, 반대로 Payward의 EU, 미국 인가를 Reap에 빌려 유럽, 미국으로. Visa와 함께 100개 이상 시장에 스테이블코인 카드 [F-1256](https://www.payward.com/press-release/payward-reap-close)
  - 결제의 바닥인 은행 계좌도 직접 갖추는 중 : 미국은 연준 계정, EU는 리투아니아 인가 디지털 은행 Saldo 인수(2027 종결 예정)로 예금과 대출을 자기 대차대조표에. 회사 표현은 "빌려 쓰는 레일을 소유한 레일로 교체" [F-1259](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)[F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)
  - 결제를 노리는 다른 곳 : Coinbase는 2026 우선순위에 스테이블코인과 결제(USDC), Robinhood는 Robinhood Banking, Binance는 Binance Pay와 카드. 차이는 Kraken이 인수한 결제 회사를 기업용 인프라에 붙여 "기업에게 파는" 쪽이라는 점 [F-0113](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-1158](https://www.robinhood.com/us/en/newsroom/introducing-strategies-banking-and-cortex)[F-0723](https://www.binance.com/en/about-legal/binance-card-global)

### 4. 시장: 거점 한 곳에서 넓게 팔아 보고, 큰 시장은 직접 인가, 빡센 곳은 인가 가진 파트너
- 거점 버뮤다 : 2024-08 디지털자산 인가(Class F) 한 장으로 거래소, 파생 거래소, 수탁을 모두 할 수 있음. 2024-10 이 법인으로 파생 거래장(200개 이상 계약)을 먼저 열었고, 같은 법인이 2025-06 xStocks의 판매 창구가 됨 [F-1416](https://www.bma.bm/regulated-entities)[F-1368](https://www.businesswire.com/news/home/20241003985524/en/Kraken-Launches-Regulated-Derivatives-Venue-in-Bermuda)[F-1369](https://support.kraken.com/articles/where-is-kraken-licensed-or-regulated)
  - 이 한 장으로 거의 다 되는 이유 : 버뮤다 법인이 미국 밖 여러 나라 고객을 직접 받고, xStocks는 판매국 증권 감독기관에 따로 등록하지 않음. 그래서 출시 며칠 만에 140개국 이상 [F-0391](https://www.kraken.com/xstocks)[F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)
  - 해석 : 수요 검증은 여기서 함. 인가 한 장으로 넓게 팔아 보고, 돈이 되는 것이 확인되면 큰 시장에 제대로 들어감
- 큰 시장 EU : 인가 없이는 못 파는 시장이라 직접 확보. 가상자산과 증권을 따로 풂
  - 가상자산 : 사실 2013년 첫 BTC/EUR부터 7개국 국가별 등록으로 이미 영업 중이었음. MiCA가 2026-07부터 인가를 의무로 바꾸자 2025-06 아일랜드에서 MiCA를 받아 EU 단일 인가(30개국)로 옮김. 새로 연 것이 아니라 하던 영업을 지킨 것 [F-1438](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)[F-1440](https://www.fsma.be/en/news/crypto-assets-service-providers-end-transitional-period)[F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
  - 증권과 파생 : 영국 Crypto Facilities로는 EU 고객에게 규제 파생을 줄 수 없어(해석: 브렉시트 뒤 영국 인가로는 EU 영업이 막힘), 2025-02 키프로스 투자회사를 사서 EU 증권 인가(MiFID)를 얻음 → 2025-05 EU 규제 파생, 2026-05 xStocks EU 판매 [F-1370](https://blog.kraken.com/news/eu-mifid-license)[F-1342](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))F-0920
  - 미국에서 이미 연 것을 EU로 옮기는 중 : 은행(Saldo Bank로 예금과 대출), 결제(Reap의 유럽 진출) [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1256](https://www.payward.com/press-release/payward-reap-close)
- 규제가 더 빡센 상장주 시장 : 직접 인가 대신 그 나라 인가를 가진 파트너가 맡음
  - GTN이 기초주식 집행, 수탁, 기관 판매를 맡고, 독일은 Deutsche Boerse의 360X에서 거래 [F-1084](https://www.payward.com/press-release/gtn-xstocks)[F-0175](https://www.payward.com/press-release/xstocks-dax-40)
- 자산 순서와 목표 : 가상자산 → 미국 주식 토큰 → 영국, EU 상장주 200종 이상(DAX 40 전부, 2026-11) → 홍콩 수백 종(수 주 안) → 영국, 유럽, 한국 상장자산(계획), LSE의 xStocks 상장 2027 예정. "각국 상장주를 토큰으로"를 공개 목표로 걸고 그 선두를 노림 [F-1360](https://www.hosu-news.com/news/articleView.html?idxno=187188)[F-1361](https://www.theblock.co/news/defi/2026-07-22-kraken-parent-payward-partners-gtn-scale-xstocks-internationally-beyond-us-equities-409448)[F-0170](https://www.payward.com/press-release/gtn-xstocks)[F-0174](https://www.payward.com/press-release/xstocks-uk-eu-equities)

### 5. 청산소까지 사며 가상자산 거래소라는 정체성을 벗는 중
- Bitnomial로 청산소까지 들어오면서 미국 파생에서 중개, 거래소, 청산을 한 그룹이 다 가짐. 거래소가 아니라 시장 인프라 회사에 가까워짐 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
- 당국과 사이가 좋아 보이는 이유
  - 2025 이후 : SEC 소송 취하(2025-03), 연준 계정(회사 발표), CFTC와 SEC에 주식 무기한선물 공동 신청, Nasdaq 감시 기술 도입 [CASE-004](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26278)[F-1254](https://www.payward.com/press-release/payward-acquires-saldo-bank)[F-1189](https://www.payward.com/press-release/payward-single-stock-perpetual-futures-filing)[F-1255](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)
  - 그 전 : 2015 뉴욕 철수, 2021 CFTC 제재, 2022 OFAC 제재, 2023 SEC 스테이킹 합의로 당국과 계속 부딪힘 [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[CASE-003](https://www.sec.gov/newsroom/press-releases/2023-25)
  - 해석 : 처음부터 사이가 좋았던 것이 아니라, 2025년 미국 규제 환경이 바뀐 뒤 "등록 없이 팔다 제재받던 거래소"에서 "인가를 다 가진 금융회사"로 스스로 자리를 옮기는 중. 인수 연쇄, 연준 계정, 청산소, Nasdaq 감시 기술이 모두 같은 방향

### 6. KSF: 인수를 야무지게 함. 하나 살 때마다 바로 다음 상품이 나옴
- 무엇을 사나 : 이미 인가를 가진 회사만. 미국 안에서는 막힌 규제를 뚫는 인가(선물중개 NinjaTrader, 선물거래소 Small Exchange, 중개, 거래소, 청산 한 벌 Bitnomial), 미국 밖에서는 현지 인가(EU 증권 키프로스 투자회사, 아시아태평양 결제 Reap, EU 은행 Saldo) [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)[F-1116](https://blog.kraken.com/news/acquires-small-exchange)[F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)[F-1370](https://blog.kraken.com/news/eu-mifid-license)[F-1195](https://www.payward.com/press-release/payward-reap-close)[F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)
- 어떻게 굴리나 : 산 회사의 인가, 브랜드, 경영진을 그대로 둔 채 그룹에서 운영(Bitnomial, Reap). 인가를 새로 받는 시간 없이 바로 상품을 얹음 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)[F-1256](https://www.payward.com/press-release/payward-reap-close)
- 그래서 효과가 빠름 : NinjaTrader 두 달 뒤 미국 선물, 키프로스 석 달 뒤 EU 파생, Backed 인수 뒤 xStocks 운용자산 4배 [F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)[F-1342](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))[F-0165](https://www.payward.com/press-release/xstocks-surpasses-1-billion-aum)
- 고르는 기준 : 쇼핑 목록 없이 "인프라 공백을 메우나, 고객이 원하는 역량인가"를 정량으로 따짐. 사지 못하는 신뢰는 제휴로 [F-1349](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)

### 7. 가설: 비상장 모회사라서 가능한 속도
- Payward는 비상장(2025-11 상장 서류 비공개 제출, 2027 Q2 전에는 상장 안 함), 외부 자금 없이 굴러가고 2026 Q3 조정 EBITDA 6천만 달러 [F-1352](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)[F-0180](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
- 최근 투자자는 Citadel Securities, Nasdaq 같은 전통 금융의 전략적 투자자 [F-1352](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
- 해석
  - 분기 실적을 묻는 주주가 없어 1년 반 동안 공개된 것만 27.5억 달러 넘는 인수를 연달아 할 수 있었음 [F-1355](https://www.tokenpost.kr)
  - Nasdaq, Citadel 같은 주주가 들어오면서 인가 심사와 제휴에서 "전통 금융이 믿는 회사"라는 신호를 줌
  - 상장을 미루는 것도 인가를 다 모은 뒤 "금융 인프라 회사"로 상장하려는 순서로 볼 수 있음

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
