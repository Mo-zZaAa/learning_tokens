# Coinbase 브리핑
- 축 : 직접 인가가 중심이고 빈 곳만 인수로 메워 현물 거래소에 선물과 옵션을 붙여, 거래대금 대부분이 파생
- 가설 : 다 한다, 회사가 2026 우선순위 1로 암호자산, 주식, 예측시장, 원자재, 외환을 한 곳에서 거래(Everything Exchange)를 명시

## Coinbase의 전략

### 1. 출발: 미국 개인용 비트코인 거래 앱이 뉴욕주 신탁 인가로 기관 보관에 들어섬
- Coinbase는 2012년 누구나 비트코인을 쉽게 주고받게 하자는 생각으로 시작한 미국 가상자산 거래소이며, 본업은 미국 개인에게 가상자산을 사고팔게 하고 받는 거래 수수료임 [F-1223](https://www.coinbase.com/about)[F-1115](https://en.wikipedia.org/wiki/Coinbase)
- 제도권에 들어선 계기는 뉴욕주 인가 두 가지이며, 모두 직접 받음 [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)
  - 2017-01 BitLicense(뉴욕주 금융감독청 NYDFS의 가상자산 사업 면허)와 송금 면허 [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)
  - 2018-10 Coinbase Custody Trust Company의 제한목적 신탁 인가(고객 자산 보관만 하는 신탁회사 인가). 보관 사업 자체는 2018-07에 시작함(Bitcoin Magazine 보도) [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)[F-1377](https://bitcoinmagazine.com/markets/coinbases-new-custody-service-opens-its-doors)
- 같은 해 본업 옆에 처음 붙인 것은 스테이블코인임. 2018-09 Circle(미국 결제 회사, 지금의 USDC 단독 발행사)과 함께 USDC(미국 달러와 1:1로 바꿀 수 있는 스테이블코인)를 출시했고, 두 회사가 Centre 컨소시엄(USDC 공동 운영 기구)을 세워 함께 운영함 [F-0790](https://www.base.org/blog/tokenized-stocks)[F-1609](https://www.circle.com/blog/ushering-in-the-next-chapter-for-usdc)
- 2020 Tagomi(기관용 가상자산 주문 중개 회사) 인수로 지금의 기관 거래 상품 Prime의 기반을 들임(Coinbase 설명을 Bitcoin Magazine 보도 항목에서 확인) [F-1377](https://bitcoinmagazine.com/markets/coinbases-new-custody-service-opens-its-doors)
- 이렇게 갖춘 보관과 기관 거래가 상장 해에 숫자로 드러남. 2021-04 Nasdaq 직상장(신주 공모 없이 기존 주식을 바로 상장) 뒤 2021년 한 해 기관 고객 50% 이상 증가, 보관 고객 수 2배, Prime 출시, 2021 Q4 거래대금의 68%가 기관 [F-1226](https://investor.coinbase.com/news/news-details/2021/Coinbase-Announces-Effectiveness-of-Registration-Statement-and-Anticipated-Listing-Date-of-its-Class-A-Common-Stock-on-the-Nasdaq-Global-Select-Market/default.aspx)[F-1608](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)
- 그러나 수익은 여전히 개인 거래 수수료 중심이었음. 2021 순매출 73.5억 달러 중 거래수익이 93%, 구독과 서비스 수익(보관 수수료, 스테이킹 보상, 이자처럼 거래 건수와 무관한 수익)이 7%였음 [F-1606](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)
  - 회사는 구독과 서비스 수익이 가격 영향은 받지만 대부분 반복 수익이라 매출을 안정시킨다고 설명함 [F-1607](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)
  - 해석 : 이후 확장은 거래 수수료 의존을 줄이는 방향(파생으로 거래 종류를 넓히고, USDC와 보관으로 반복 수익을 키움)으로 이어짐. 상장 첫 서한부터 반복 수익의 안정성을 강조했고, 2026년에도 CFO가 가상자산 시장 주기 의존을 줄이는 것을 목표로 말하기 때문 [F-1607](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)[F-1621](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)

### 2. 자산: 인가는 직접 신청하고, 기다리는 시간이나 유동성을 사야 하는 곳만 인수함
- 파생을 붙인 이유 : 지난 2년 세계 가상자산 거래대금의 75%가 파생인데 미국 시장은 그 일부에 그쳐 큰 성장 기회라고 회사가 설명함 [F-1601](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
- 미국에서 선물을 하려면 중개, 거래소, 청산의 세 인가가 필요함. Coinbase는 이 중 거래소만 사고 나머지 둘은 직접 받음
  - 선물 중개(FCM, 선물중개업자: 고객 주문과 증거금을 받는 회사) : 2021-09 NFA(미국 선물협회)에 직접 신청해 2023-08 등록까지 약 2년 걸림 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717)
  - 선물 거래소(DCM, CFTC가 지정한 선물거래소) : 중개 인가를 기다리던 2022-01 FairX(2020-11 지정을 받은 선물거래소) 인수를 발표함. FairX의 핵심 장점은 이미 CFTC 규제를 받는다는 점이었고, 회사는 FairX 인프라로 미국 모든 고객에게 가상자산 파생을 제공하겠다고 밝힘(디크립트 보도) [F-1622](https://decrypt.co/90341/coinbase-acquiring-derivatives-exchange-bitcoin-futures-trading)[F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)
  - 청산소(DCO, 거래 상대방 사이에서 결제를 보증하는 기관) : Coinbase Clearing LLC가 2025-11 직접 신청해 2026-09 등록됨. 인가 범위는 완전 담보 계약뿐이어서, 증거금 파생과 예정된 개별주식 무기한선물은 계속 외부 청산 파트너를 씀(파이낸스 매그닛 보도) [F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)[F-1624](https://www.financemagnates.com/cryptocurrency/exchange/coinbase-completes-us-derivatives-infrastructure-with-cftc-clearing-registration/)
  - 청산소를 직접 받은 이유 : CFO는 자체 예측시장 계약을 상장하고 수익성을 높이기 위해서라고 설명함. 회사 발표도 "처음으로 완전 담보 계약을 직접 만들고 결제할 수 있게 됨"이라고 함 [F-1614](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1623](https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/)
  - 같은 시기인 2025-12 예측시장 청산 인프라를 만들던 스타트업 The Clearing Company(2025-11 CFTC에 별도로 청산소 신청)를 인수해 팀을 들임(코인텔레그래프 보도) [F-1625](https://cointelegraph.com/news/coinbase-acquires-clearing-company-prediction-markets)[F-1626](https://www.marketsmedia.com/the-clearing-company-files-to-become-dco/)
- 옵션은 인수함 : 2025-05 Deribit(세계 최대 가상자산 옵션 거래소) 약 29억 달러 인수를 발표하고 2025-08 완료. 이유는 옵션 1위 거래소를 더해 현물, 선물, 무기한, 옵션을 한 플랫폼에 모으는 것, 경기를 덜 타는 옵션 수익, 해외 확장 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)[F-1601](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
  - 대가 중 1,100만 주는 Coinbase 주식으로 지급함 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
  - 그 결과 세계 옵션 미결제약정 선두가 됐고, 2026-10 국제 거래소 INTX(Coinbase International Exchange, 버뮤다 인가 파생 거래소)와 통합해 미국과 미국 밖 고객을 잇는 단일 규제 거래소가 됨. 옵션은 기관에 제공 중이고 개인용은 준비 중 [F-1618](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-0903(주주서한 PDF) F-0905(실적 발표 통화 녹취 PDF)
- 해석 : 직접과 인수를 가른 기준은 "인가 심사만 통과하면 되는가, 이미 쌓인 거래 상대와 유동성이 필요한가"로 보임. 근거는 아래 세 가지임 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717)[F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)[F-1622](https://decrypt.co/90341/coinbase-acquiring-derivatives-exchange-bitcoin-futures-trading)[F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
  - 중개와 청산소는 고객 계좌와 자기 상품 구조를 정하는 인가여서 시간이 걸려도 직접 받음(중개 약 2년, 청산소 약 10개월)
  - 거래소는 중개 인가를 기다리는 동안 먼저 열 수 있는 이미 지정된 거래소를 샀고, 옵션은 1위 거래소의 유동성 자체를 샀음
  - CFO도 주식 토큰을 두고 "토큰화 자산을 만드는 것은 쉽고, 유동성 깊이와 네트워크를 키우는 것이 어렵다"고 말함 F-1059(실적 발표 통화 녹취 PDF)
- 결과 : 2026 Q3 총 거래대금 1조 2,138억 달러 중 파생이 9,859억 달러(우리 계산 약 81%)이고, 파생 거래대금은 지난 2년 연복리 179% 성장함 F-1263(주주서한 PDF) [F-1618](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 다만 수익 구성은 다름. 예측시장과 파생을 합쳐도 거래수익의 25%이며, 거래수익 5.9억 달러 중 4.5억 달러가 소비자(개인) 거래수익임 [F-1621](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-1261(실적 발표 자료 PDF)
- 예측시장 : 파트너로 먼저 열고 직접 운영으로 옮기는 중
  - 2025-12 미국 출시 때는 주문을 모두 Kalshi(CFTC 지정 예측시장 거래소)로 넘김 [F-1376](https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase)
  - 2026 Q3 연환산 순수익 2억 달러 초과, 출시 이후 분기 복리 82% 성장. 자체 청산소 등록으로 자체 계약 상장이 가능해짐 F-0907(주주서한 PDF) [F-1614](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 다른 회사와 차이 : Robinhood도 2025-03 Kalshi 경유로 먼저 열었지만, 2026-01 거래소와 청산소를 가진 MIAXdx 지분 90%를 합작법인으로 인수함. Coinbase는 청산소를 직접 받고 스타트업 팀만 인수함 [F-1156](https://robinhood.com/us/en/newsroom/robinhood-prediction-markets-hub/)[F-0610](https://investors.robinhood.com/node/16931/html)[F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)[F-1625](https://cointelegraph.com/news/coinbase-acquires-clearing-company-prediction-markets)
- 주식 : 미국 안은 실물 주식, 미국 밖은 직접 발행한 주식 토큰과 주식 무기한선물
  - 미국 안 : 2025년 안에 앱 안 주식과 ETF 거래(초기 3,000종목)를 내놓고, 2026-02 미국 전체 이용자에게 8,000종목 이상으로 넓히며 USDC로 결제(Fnnews 보도) [F-0100](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-0101](https://en.fnnews.com/news/202602261546337944)
  - 미국 밖 : 2026-08 아부다비 ADGM(아부다비 국제금융센터, 자체 금융감독청 FSRA 보유)에 발행 법인을 세워 주식 토큰을 직접 발행하고, 기초주식은 Alpaca(미국 증권 중개 회사)가 분리 보관함. 토큰은 거래소 상장 없이 Base 위 DeFi(탈중앙 거래소와 대출 서비스)에서만 유통됨 [F-0082](https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf)[F-0081](https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf)[F-0088](https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf)
  - 미국 밖 고객에게는 주식 무기한선물도 냄. 회사는 이를 "전통 자산을 가상자산 결제망 위에" 올리는 전략이라고 설명함(키트코 보도) [F-1627](https://www.kitco.com/news/article/2026-05-07/coinbase-launches-gold-perp-and-silver-perp-futures-offering-247365-metals)
  - 해석 : 주식 토큰을 남의 발행사에 맡기지 않고 직접 발행한 바탕은 보관 사업임. CEO가 "크립토 최대 수탁기관이자 가장 신뢰받는 브랜드라 이길 권리가 있다"고 말했고, 실제로 가상자산 ETF 자산의 80% 이상을 보관하는 회사이기 때문 [F-1604](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf) F-1061(AMA 녹취 PDF)
- 원자재 : Coinbase Derivatives(인수한 FairX의 지금 이름)에 이미 금, 은 선물이 있었고 2026 Q1 상품선물 명목 거래대금이 520억 달러를 넘음. 2026-05 미국 밖 금, 은 무기한선물, 2026-06 미국 금, 은 선물 24시간 거래로 넓힘(비트코인닷컴, 키트코 보도) [F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)[F-1628](https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/)[F-1627](https://www.kitco.com/news/article/2026-05-07/coinbase-launches-gold-perp-and-silver-perp-futures-offering-247365-metals)

### 3. 비전: Everything Exchange, 스테이블코인과 결제, 온체인 세 우선순위
- 공식 틀은 두 가지임. 연간 우선순위 2026 Priorities(1 Everything Exchange, 2 Stablecoins & Payments, 3 Onchain)와 자산 축적 플라이휠(asset accumulation flywheel, 앞 단계의 결과가 다음 단계를 키우는 순환 구조)이며, 둘 다 2026-02-12 2025 Q4 주주서한에 실림. 2번과 3번의 서한 원문 정의는 Scale stablecoins and payments(USDC 쓰임과 결제 스택을 키워 거래 밖 실사용을 잡음), Bring the world onchain(Coinbase 앱의 DeFi 연동, Base App(Base 위 거래 중심 앱), Base 활동 확대)임 [F-1642](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-1643](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)
  - 우선순위의 변천 : 2024 우선순위는 매출 확대(핵심 거래와 USDC 개선), 쓰임 확대(USDC와 Base로 결제 실험), 업계 규제 명확성 추진 셋이었음(2023 Q4 주주서한, Markets Media 전재). 2025 목표는 drive revenue(매출 확대), drive utility(결제, 스테이블코인, Base로 쓰임 확대), scale our foundations(미국 가상자산 입법 달성과 가장 신뢰받는 플랫폼이라는 기반 확충)였음. 이렇게 회사 운영 목표 순서였던 틀이 2026에 상품 영역 이름으로 바뀌었고, 규제 항목은 목록에서 빠짐 [F-1645](https://www.marketsmedia.com/coinbase-increases-institutional-transaction-revenue/)[F-1644](https://s27.q4cdn.com/397450999/files/doc_financials/2024/q4/Q4-24-Shareholder-Letter.pdf)[F-1642](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)
  - 2026 Q3 주주서한(2026-10-29)은 같은 세 항목을 다시 내면서 정의를 넓힘. Everything Exchange 대상에 원자재와 외환을 더하고(연초는 암호자산, 파생, 주식, 예측시장), Onchain 정의에 에이전트를 더해 "거래, 결제, 에이전트를 온체인으로"로 바꿈. 같은 서한은 다음 개척지를 에이전트로 제시함 [F-1615](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-1646(주주서한 PDF)
  - 플라이휠 네 단계 : Most trusted(가장 신뢰받는 이름) → Grow assets on platform(고객이 플랫폼에 자산을 더 맡김) → Drive product adoption(자산이 있는 곳에서 상품을 더 씀) → Monetize & reinvest(수익을 플랫폼에 재투자). 서한은 2025년에 이 플라이휠을 처음 내놨다고(debuted) 적고, 2025년 성과로 전 세계 가상자산의 약 12% 보관과 플랫폼 자산 3년에 3배를 제시함 [F-1643](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)
- Everything Exchange의 첫 표현은 2025-07-31 2025 Q2 주주서한의 "온체인에서 거래할 수 있는 모든 것을 위한 하나의 플랫폼"(one platform for everything you can trade onchain)임 [F-1600](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
  - 2025년 말 예측시장(2025-12)과 앱 안 주식 거래를 내놓으며 실제 상품이 됐고, 2026-02 2026 우선순위 1로 올라감 [F-1376](https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase)[F-0100](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-1271](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)
  - 지금의 원문 정의는 "암호자산, 주식, 예측시장, 원자재, 외환을 깊은 유동성과 자본 효율로 한 곳에서 거래"(Trade every asset class in one place) [F-1615](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
- 자산별 실제 행동
  - 암호자산 파생 : 거래소 인수, 중개와 청산소 직접 등록, Deribit 인수로 갖춤. 거래대금 대부분을 만듦 F-1263(주주서한 PDF) [F-1623](https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/)
  - 예측시장 : Kalshi 연결 뒤 자체 청산소와 The Clearing Company 인수, 연환산 순수익 2억 달러 초과 F-0907(주주서한 PDF) [F-1625](https://cointelegraph.com/news/coinbase-acquires-clearing-company-prediction-markets)
  - 주식 : 미국 실물 8,000종목 이상, 미국 밖 주식 토큰과 주식 무기한선물 [F-0101](https://en.fnnews.com/news/202602261546337944)[F-0777](https://www.base.org/blog/tokenized-stocks)[F-1627](https://www.kitco.com/news/article/2026-05-07/coinbase-launches-gold-perp-and-silver-perp-futures-offering-247365-metals)
  - 원자재 : 금, 은 선물과 무기한선물 [F-1628](https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/)[F-1627](https://www.kitco.com/news/article/2026-05-07/coinbase-launches-gold-perp-and-silver-perp-futures-offering-247365-metals)
  - 외환 : 영국 파운드 스테이블코인 tGBP 상장(2026-04)과 CEO의 "기업이 결제를 받으며 외환을 거래할 수 있어야 한다"는 발언 단계임 [F-1629](https://www.marketsmedia.com/coinbase-lists-fiat-backed-sterling-stablecoin/)[F-1620](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 해석 : 의미 있는 기둥은 파생과 예측시장이고, 외환은 이름이 먼저 나온 기둥임. 파생은 거래대금의 약 81%, 예측시장은 연환산 2억 달러를 넘었지만, 외환은 스테이블코인 상장과 CEO 발언 단계이기 때문 F-1263(주주서한 PDF) F-0907(주주서한 PDF) [F-1629](https://www.marketsmedia.com/coinbase-lists-fiat-backed-sterling-stablecoin/)
  - CEO도 지난 1년 Everything Exchange 투자 중 예측시장과 파생이 성과를 내기 시작했고, 과거에는 현물 거래 비중이 지나치게 컸다고 말함 [F-1620](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 여러 자산을 한 계정에 묶는 장치는 Coinbase One(월 구독 회원제, 거래 수수료 면제와 USDC 보상 우대)임. 유료 구독자는 2025-12 약 100만 명이며 2026 Q3 전년 대비 24% 늘어남 F-1264(실적 발표 통화 녹취 PDF)
- 스테이블코인과 결제 : 스테이블코인 수익은 USDC 준비금 이자를 Circle과 나눈 몫임
  - 계약 원문 : 2023-08 Centre를 해산하고 Circle이 단독 발행사가 되면서 Coinbase는 Circle 지분을 받음. 이자 수익은 "각 플랫폼에 있는 USDC 양에 따라" 나누고, 그 밖의 USDC 유통에서 나온 이자는 반씩 나누기로 함(Circle과 Coinbase CEO 공동 서명 글) [F-1609](https://www.circle.com/blog/ushering-in-the-next-chapter-for-usdc)
  - 그래서 Coinbase 앱 안 USDC가 많을수록, 또 세상의 USDC 전체가 많을수록 수익이 늘어남. 2025 Q2 스테이블코인 수익 3.32억 달러 중 1.44억은 앱 안 USDC(평균 138억 달러), 1.88억은 플랫폼 밖 USDC(평균 474억 달러)에서 나옴 [F-1603](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
  - 2026 Q3 : 앱 안 평균 USDC 220억 달러(USDC 시가총액의 약 30%), 스테이블코인 수익 3.07억 달러. CEO는 USDC 경제적 수익의 약 50%를 가져간다고 말함 [F-1610](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-1262(실적 발표 자료 PDF) F-0914(주주서한 PDF)
  - 키우는 행동 : USDC 보상 프로그램, Hyperliquid(탈중앙 무기한선물 거래소) 같은 큰 플랫폼과의 USDC 제휴, 파생 거래소 담보로 USDC 사용, 청산소를 USDC 기반으로 설계 [F-1612](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1611](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1623](https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/)
  - Circle과는 협력과 경쟁이 섞여 있음. 둘 다 USDC 시가총액을 키우려 하지만 스테이블코인 결제 인프라는 각자 만들어 경쟁한다고 CFO가 말함 [F-1611](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 결제 : Base, USDC, x402(Coinbase가 만든 AI 에이전트용 결제 규약)로 Citibank, Shopify, Cloudflare, Checkout.com과 계약함. 개발자 플랫폼 결제 처리액은 분기 복리 160% 성장했으나 CFO는 아직 재무에 의미 있는 규모가 아니라고 함 [F-1613](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1616](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
- 구독과 서비스 수익이 중요한 이유 : 거래 건수가 아니라 보유 자산에서 나오는 반복 수익이어서 시장이 식어도 덜 줄기 때문(회사 설명). 비중이 2021 7%에서 2025 39%, 2026 Q3 49%로 커짐 [F-1607](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)[F-1606](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)[F-0112](https://sec-api.io/insights/coinbase-coin-q3-2026-earnings-sec-filing-analysis)[F-1621](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 2026 Q3 구성 : 스테이블코인 3.07억, 블록체인 보상(스테이킹) 0.86억, 이자와 금융 수수료 0.69억, 기타 1.09억 달러. 스테이블코인이 절반 이상임 F-1262(실적 발표 자료 PDF)
- 온체인 : Base가 중심임
  - Base는 Coinbase가 2023-02 발표하고 2023-07 개발자에게 연 뒤 2023-08 일반 공개를 예고한 이더리움 L2(이더리움 위에서 거래를 모아 처리하는 블록체인)이며, Optimism의 공개 소프트웨어 OP Stack으로 만듦(코인텔레그래프 보도) [F-1630](https://cointelegraph.com/news/coinbase-base-launches-mainnet-for-builders-will-onboard-users-august)
  - Coinbase는 시퀀서(Base 거래를 받아 순서를 정하고 기록하는 노드)를 운영하며 수수료를 받음. 이 수익은 기타 거래수익에 들어가고, CFO는 주식 토큰도 주로 시퀀서 수수료로 번다고 설명함 [F-0768](https://docs.base.org/terms-of-service)[F-0770](https://docs.base.org/terms-of-service)[F-1605](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf) F-1266(실적 발표 통화 녹취 PDF)
  - 결과 : 2026 Q3 현물 가상자산 거래와 DeFi 예치액 모두 1위 L2. 2025 Q2 Base 개인 간 거래대금의 90% 이상이 USDC여서 USDC 유통 경로 역할도 함 [F-1617](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1605](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
  - 주식 토큰 거래대금은 출시 이후 10억 달러 이상(주주서한) 또는 약 30억 달러(CFO)로 서로 다르며 하나로 고르지 않음. 같은 분기 현물 거래대금 1,345억 달러에 비하면 작은 사업임 F-0892(주주서한 PDF) F-0894(실적 발표 통화 녹취 PDF) F-0915(주주서한 PDF)
- 다른 회사와 차이
  - Robinhood Chain : Robinhood도 2026-07 자체 L2를 열었으나 Arbitrum(다른 회사의 L2 기술)을 빌렸고, 자기 앱에서 EU 고객에게 판 Stock Tokens(채무증권 형태)를 그 위로 옮기는 방식임. Coinbase는 3년 앞선 2023년에 Base를 열었고, 주식 토큰은 실물 주식 수익권 증서로 발행해 앱이 아닌 Base DeFi에서 누구나 거래하게 함 [F-0225](https://cryptobriefing.com/robinhood-crypto-mainnet-eu-perps/)[F-0221](https://www.marketsmedia.com/?p=144033)[F-0662](https://robinhood.com/eu/en/legal/rhj)[F-0079](https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf)[F-0757](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
  - Kraken : xStocks를 여러 체인에 배포하는 체인 중립 방식이고, Coinbase는 자기 체인 Base에 주식 토큰과 USDC를 모음 [F-1041](https://blog.kraken.com/product/xstocks/launch-on-ethereum)[F-0777](https://www.base.org/blog/tokenized-stocks)
  - 같은 비교로 Architect Partners(가상자산 인수합병 자문사)는 Coinbase를 단일 브랜드 Everything Exchange, Kraken을 여러 브랜드와 외부 회사가 쓰는 인프라로 평가함(코인데스크 보도) [F-1351](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
  - CEO 설명 : 다른 회사가 사람들을 월가로 데려가려 한다면 Coinbase는 월가가 필요 없는 탈중앙 금융 시스템을 만들려 하며, 강점은 Base, USDC 공동 창업, x402 [F-1619](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)

### 4. 시장: 규칙이 분명한 큰 시장은 직접 인가, 미국에서 못 하는 파생은 버뮤다, 주식 토큰은 아부다비
- 진출 원칙 : Go Broad, Go Deep(상품은 넓게, 시장은 일부에 깊게) 전략의 후속 계획(2023-09)에서 규칙이 분명한 EU, 영국, 캐나다, 브라질, 싱가포르, 호주를 가까운 우선 시장으로 정하고 인가 취득과 현지 운영에 집중하기로 함. 같은 글에서 미국은 집행 위주라고 비판함(코인텔레그래프 보도) [F-1632](https://cointelegraph.com/news/coinbase-near-term-priorities-eu-canada-brazil-singapore-australia)
  - 해석 : 무인가 판매로 수요를 먼저 확인하는 방식이 아니라, 규칙이 생긴 곳에 인가를 받고 들어가는 순서임. 실제 진출이 각 나라 규칙 시점을 따랐기 때문(영국 등록 2025-02, EU MiCA 인가 2025-06) [F-1633](https://cointelegraph.com/news/coinbase-fca-uk-crypto-registration)[F-1602](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)
- 미국에서 못 하는 파생은 버뮤다에서 먼저 함
  - 2023-05 버뮤다 금융청(BMA) 인가로 Coinbase International Exchange를 열어 미국 밖 기관에게 무기한선물(만기 없는 선물)을 USDC 결제로 제공함. 이유는 2022년 세계 가상자산 거래대금의 75% 가까이가 무기한선물이었기 때문(회사 설명) [F-1631](https://www.marketsmedia.com/introducing-coinbase-international-exchange/)[F-1416](https://www.bma.bm/regulated-entities)
  - 같은 무렵 미국에서는 SEC(미국 증권거래위원회)가 Coinbase를 제소함(2023-06) [F-1227](https://www.sec.gov/newsroom/press-releases/2025-47)
  - 그 뒤 2025-08 Deribit 인수로 미국 밖 기관 옵션 고객을 더함. 회사 부사장은 이를 국제 성장을 위한 가장 큰 행보라고 말함(코인텔레그래프 보도) [F-1217](https://cointelegraph.com/news/coinbase-acquire-deribit-2-9-billion)[F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
  - 미국에는 2025-07 CFTC 규제 무기한형 선물을 냈고, 2026-06 미국 고객에게 세계 무기한선물을 직접 제공하는 첫 FCM이 됨(비트코인닷컴 보도) [F-1601](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)[F-1628](https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/)
  - 해석 : 미국 밖에서 먼저 연 상품을 미국 규제가 정비된 뒤 미국으로 들여오는 순서임. 무기한선물이 버뮤다(2023)에서 미국(2025, 2026)으로, Deribit 옵션이 미국 밖 기관에서 미국 고객으로 넓어지는 중이기 때문 [F-1631](https://www.marketsmedia.com/introducing-coinbase-international-exchange/)[F-1628](https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/) F-1062(AMA 녹취 PDF)
- 큰 시장인 영국과 EU는 이미 하던 영업을 새 규칙에 맞춤
  - 영국 : 미국 밖 최대 시장임. 2025-02 FCA(영국 금융감독청) 가상자산사업자 등록(CB Payments Ltd)을 받았고, 회사는 영국 최대 등록 거래소라고 밝힘(코인텔레그래프 보도) [F-1633](https://cointelegraph.com/news/coinbase-fca-uk-crypto-registration)
  - EU : 2025-06 룩셈부르크에서 MiCA(EU 가상자산시장 규정) 인가를 받아 EEA 30개국에서 핵심 개인, 기관 서비스를 허용받고 기존 EEA 영업을 MiCA로 옮김. ESMA 등록부상 인가 서비스는 보관, 교환, 주문 집행과 전달 같은 중개형 7가지임 [F-1602](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)[F-0102](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)[F-0254](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)
  - 현지 통화 스테이블코인 지원(영국 파운드 tGBP)을 해외 확장 전략의 핵심 요소로 둠 [F-1629](https://www.marketsmedia.com/coinbase-lists-fiat-backed-sterling-stablecoin/)
- 주식 토큰은 판매국 인가 대신 발행지 인가로 넓게 유통함
  - 2026-08 아부다비 FSRA 허가를 받아 발행 법인을 세우고, Regulation S(미국 밖 판매에 미국 증권 등록을 면제하는 규정)로 미국 밖 적격 관할 개인에게 제공함. 모든 시장에서 제공되지는 않음 [F-0095](https://www.macaubusiness.com/coinbase-establishes-its-tokenization-hub-in-abu-dhabi-with-financial-services-permission-from-the-financial-services-regulatory-authority-fsra-2/)[F-0739](https://base.org/stocks)
  - 1차 발행과 상환만 신원확인을 거친 기관 참가자가 하고, 2차 거래는 Base DeFi에서 신원확인 없이 가능함 [F-0757](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
  - UAE 안에서는 아부다비를 토큰증권 허브로, 두바이를 파생상품 허브로 나눔(Macau Business 보도) [F-0097](https://www.macaubusiness.com/coinbase-establishes-its-tokenization-hub-in-abu-dhabi-with-financial-services-permission-from-the-financial-services-regulatory-authority-fsra-2/)
  - 미국 출시는 SEC의 혁신 면제(신기술 상품에 대한 예외 제도) 뒤 검토한다고 CFO가 말함 F-0898(실적 발표 통화 녹취 PDF)
- 자산 순서 : 가상자산 현물(2012) → 기관 보관과 USDC(2018) → 미국 선물(2022 거래소 인수, 2023 중개 등록) → 미국 밖 무기한선물(2023) → 옵션(2025 인수) → 예측시장(2025-12)과 미국 주식(2025 출시, 2026-02 전체 개방) → 미국 밖 주식 토큰(2026-08) → 청산소(2026-09) [F-1223](https://www.coinbase.com/about)[F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)[F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)[F-1228](https://www.nfa.futures.org/BasicNet/#0542717)[F-1631](https://www.marketsmedia.com/introducing-coinbase-international-exchange/)[F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)[F-1376](https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase)[F-0777](https://www.base.org/blog/tokenized-stocks)[F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)

### 5. 개인 거래 수수료 회사에서 파생 거래와 USDC 수익의 금융 플랫폼으로 바뀌는 중
- 전후 비교
  - 2021 : 순매출 73.5억 달러의 93%가 거래수익. 보관과 USDC는 작은 부수 사업 [F-1606](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)
  - 2026 Q3 : 순매출 12.2억 달러 F-1260(주주서한 PDF) 중 49%가 구독과 서비스(그중 절반 이상이 스테이블코인), 거래대금의 약 81%가 파생 [F-1621](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-1262(실적 발표 자료 PDF) F-1263(주주서한 PDF)
  - 2025년 연환산 매출 1억 달러 이상 상품이 12개라고 회사가 밝힘 [F-1272](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q4/coin-20260212.pdf)
- 당국과의 관계
  - 2023 : SEC가 Coinbase를 제소(2023-06). 회사는 같은 해 미국을 집행 위주라고 비판하며 해외 우선 시장을 정함 [F-1227](https://www.sec.gov/newsroom/press-releases/2025-47)[F-1632](https://cointelegraph.com/news/coinbase-near-term-priorities-eu-canada-brazil-singapore-australia)
  - 같은 2023-08에 CFTC 쪽 선물 중개 인가(FCM)는 받음 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717)
  - 2025 이후 : SEC 소송 취하(2025-02, SEC는 본안 판단이 아니라고 밝힘), 미국 첫 세계 무기한선물 FCM(2026-06), 청산소 등록(2026-09) [F-1227](https://www.sec.gov/newsroom/press-releases/2025-47)[F-1628](https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/)[F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)
  - 해석 : 증권 당국(SEC)과는 충돌했지만 선물 당국(CFTC)의 인가는 꾸준히 직접 받아 옴. 그래서 2025년 미국 규제 환경이 바뀐 뒤에는 이미 가진 중개와 거래소에 청산소만 더해 미국 파생 전 과정을 그룹 안에 갖출 수 있었음 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717)[F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)[F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)

### 6. KSF: 먼저 받은 인가와 USDC를 같은 계정의 고객에게 계속 얹음
- 보관 : 2018-10 뉴욕주 신탁 인가로, Robinhood Crypto의 뉴욕주 면허(2019-01)와 Kraken의 와이오밍 은행 인가(2020-09)보다 먼저 규제 보관기관이 됨 [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)[F-1337](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
  - 그 결과 가상자산 ETF 자산 보관 점유율 80% 이상, 비트코인 보유 상장사 상위 10곳 중 8곳의 보관기관, 플랫폼 보관자산은 전체 가상자산 시가총액의 12.5% [F-1604](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)[F-1222](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
- USDC : 2018 공동 출시와 2023 계약으로 USDC 이자 수익의 몫을 가짐. 2021 수익표에 별도 항목이 없던 스테이블코인 수익이 2026 Q3 분기 3.07억 달러로 구독과 서비스의 최대 항목이 됨 [F-1609](https://www.circle.com/blog/ushering-in-the-next-chapter-for-usdc)[F-1606](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf) F-1262(실적 발표 자료 PDF)
- 미국 선물 : 2023-08 FCM 등록으로, Kraken(2025-07 NinjaTrader 인수 뒤 미국 선물 제공)보다 약 2년 먼저 미국 개인에게 규제 선물을 팔 수 있는 중개 인가를 갖춤. 가상자산 거래대금 점유율은 10.7%(전년 5.6%)로 4분기 연속 올랐고 현물과 파생이 모두 기여함 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717)[F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)[F-1618](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/) F-0902(주주서한 PDF)
  - 한계 : 예측시장은 Robinhood(2025-03)보다 9개월 늦은 후발임 [F-1156](https://robinhood.com/us/en/newsroom/robinhood-prediction-markets-hub/)[F-1376](https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase)
- Base : 2023 출범으로 Robinhood Chain(2026-07)보다 3년 앞섰고, 2026 Q3 현물 거래와 DeFi 예치액 모두 1위 L2 [F-1630](https://cointelegraph.com/news/coinbase-base-launches-mainnet-for-builders-will-onboard-users-august)[F-0225](https://cryptobriefing.com/robinhood-crypto-mainnet-eu-perps/)[F-1617](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
- 운영 방식 : 같은 계정(앱, Coinbase One)에 상품을 얹고, USDC를 결제, 담보, 보상에 두루 써서 상품끼리 잇는 것임. CEO는 개인, 기관, 기업, 개발자를 한 플랫폼에서 상대하는 것을 강점으로 듦 [F-1619](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)[F-1611](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)

### 7. 가설: 미국 상장사이자 창업자 지배 회사였기에 생긴 방향
- 2021-04 Nasdaq 직상장 회사이며, 창업자 Brian Armstrong 중심의 B주가 주식의 15.5%로 의결권 78.6%를 가짐(B주 1주 20표). 2025-12 델라웨어에서 텍사스 법인으로 전환함 [F-1226](https://investor.coinbase.com/news/news-details/2021/Coinbase-Announces-Effectiveness-of-Registration-Statement-and-Anticipated-Listing-Date-of-its-Class-A-Common-Stock-on-the-Nasdaq-Global-Select-Market/default.aspx)[F-0104](https://sec-api.io/insights/coinbase-coin-q3-2026-earnings-sec-filing-analysis)[F-0103](https://sec-api.io/insights/coinbase-coin-q3-2026-earnings-sec-filing-analysis)
- 해석
  - 상장 주식이 인수 대금이 됨. Deribit 대가 중 1,100만 주가 Coinbase 주식이었기 때문 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
  - 분기 실적을 보는 공개시장 주주가 있어, 가격에 따라 출렁이는 거래수익보다 반복 수익(구독과 서비스)을 키우는 쪽으로 방향이 잡힌 것으로 보임. 상장 첫 서한부터 반복 수익의 안정성을 강조했고 2026에도 시장 주기 의존 축소를 목표로 말하기 때문 [F-1607](https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf)[F-1621](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
  - 미국 상장사여서 SEC 소송을 정면으로 맞았고, 그 시기를 인수가 아니라 인가 신청과 해외 직접 인가로 넘김. 비상장인 Kraken이 소송 종료 뒤 인수로 빠르게 인가를 모은 것과 다른 점임 [F-1227](https://www.sec.gov/newsroom/press-releases/2025-47)[F-1632](https://cointelegraph.com/news/coinbase-near-term-priorities-eu-canada-brazil-singapore-australia)[F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)[F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
  - 창업자가 의결권 대부분을 쥐고 있어 Base, 주식 토큰처럼 당장 수익이 작은 사업에도 오래 투자할 수 있었던 것으로 보임 [F-0104](https://sec-api.io/insights/coinbase-coin-q3-2026-earnings-sec-filing-analysis)[F-1605](https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf)

## 1층 (키워드)
- 시작 : 가상자산 현물 거래(2012), 미국 개인
- 붙인 것
  - 파생 : 선물 거래소 FairX(인수), 선물 중개(직접), 옵션 Deribit(인수), 청산소(직접)
  - 기관 : 보관 신탁 인가(직접), Prime(인수)
  - 스테이블코인 : USDC(파트너 Circle)
  - 주식, 예측시장 : 미국 주식(직접), 예측시장 Kalshi(파트너), 주식 토큰 아부다비 발행(직접)
  - 인가 : 뉴욕주 BitLicense, 버뮤다, EU MiCA(모두 직접)
- 지금 하는 것 : 현물, 선물, 옵션, 예측시장, 주식, 스테이블코인, 보관(2026 Q3 거래대금 1조 2,138억 달러 중 파생 약 81%, 총매출 12.2억 달러)
- 해외 진출
  - EU(룩셈부르크), 영국, 버뮤다, 아부다비 : 직접 인가
  - 미국 밖 기관 파생 : 인수(Deribit)
  - 미국 밖 개인 주식 토큰 : 인가 없이 판매(Base DeFi 유통)

## 2층 (받치는 사실)
- 시작 : 2012년 시작(회사 소개) [F-1223](https://www.coinbase.com/about)
- 보관 : Coinbase Custody Trust Company 뉴욕주 제한목적 신탁 인가 2018-10 [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses), 플랫폼 보관자산이 전체 암호자산 시가총액의 12.5%(2026 Q3) [F-1222](https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/)
- USDC : 2018-09 Circle과 공동 출시 [F-0790](https://www.base.org/blog/tokenized-stocks), Coinbase 상품 안 평균 USDC 220억 달러(USDC 시가총액의 약 30%, 2026 Q3) F-0914(주주서한 PDF)
- 선물 거래소 인수 : 2022 FairX 인수로 CFTC 지정 선물 거래소(DCM, 지정 2020-11-23) 확보 [F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)
- 중개와 청산 직접 등록 : 선물 중개(FCM) 2023-08-15 [F-1228](https://www.nfa.futures.org/BasicNet/#0542717), 청산소(DCO) 2026-09-28, 인수 아님 [F-1123](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations)
- 옵션 인수 : Deribit 약 29억 달러, 2025-08 완료, 현물, 선물, 무기한, 옵션을 한 플랫폼에 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
- 예측시장 : 2025-12-17 출시, 주문을 모두 Kalshi로 연결 [F-1376](https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase), CFTC 승인 뒤 자체 계약 상장, 연환산 순수익 2억 달러 초과 F-0907(주주서한 PDF)
- 지금 규모 : 2026 Q3 총 거래대금 1조 2,138억 달러 = 현물 1,345억 + 파생 9,859억 + 스테이블코인 935억 F-1263(주주서한 PDF), 총매출 12.2억 달러 F-1260(주주서한 PDF)
  - 파생 비중 계산(우리 계산) : 파생 9,859억 ÷ 총 1조 2,138억 = 0.812, 약 81%
- 해외 직접 인가 : 버뮤다 Coinbase Bermuda Limited Class F 2023-04-19 [F-1416](https://www.bma.bm/regulated-entities), 룩셈부르크 MiCA 가상자산서비스 인가 [F-0254](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv), 아부다비 FSRA 금융서비스 허가 2026-08(Macau Business 보도) [F-0095](https://www.macaubusiness.com/coinbase-establishes-its-tokenization-hub-in-abu-dhabi-with-financial-services-permission-from-the-financial-services-regulatory-authority-fsra-2/)
- 미국 밖 개인 주식 토큰 : 미국 밖 적격 관할 개인만 [F-0749](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base), Regulation S로 제공, 모든 시장에서 이용 가능하지는 않음 [F-0739](https://base.org/stocks)

## 3층 (꼬리질문 대비)
- Q : 거래대금 81%가 파생이면 수익도 파생이 대부분인가? / A : 아님, 예측시장과 파생을 합쳐 거래수익의 25% F-1261(투자자 발표 자료 PDF)
- Q : 파생 거래대금이 9,859억과 9,630억 두 개인 이유는? / A : 9,630억은 암호자산 파생만, 9,859억은 암호자산 외 파생까지 더한 값 F-0901(주주서한 PDF), F-1263(주주서한 PDF)
- Q : Deribit 인수 조건은? / A : 현금 7억 달러와 Coinbase 주식 1,100만 주, 약 29억 달러, 이유는 옵션 1위 거래소 확보, 경기를 덜 타는 옵션 수익, 해외 확장 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
- Q : FairX는 언제 인수했나? / A : 인수 발표는 2022-01이고, 거래소 지정은 그 전인 2020-11-23에 FairX가 받음 [F-1622](https://decrypt.co/90341/coinbase-acquiring-derivatives-exchange-bitcoin-futures-trading)[F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)
- Q : 증권 중개는 어떻게 얻었나? / A : 1982년 등록 증권사 Keystone Capital을 인수해 Coinbase Capital Markets로 상호 변경 [F-1120](https://api.brokercheck.finra.org/search/firm/10722)
- Q : SEC 소송은? / A : 2023-06-06 제기, 2025-02-27 양측 합의서로 취하, SEC는 본안 판단이 아니라고 밝힘 [F-1227](https://www.sec.gov/newsroom/press-releases/2025-47)
- Q : Coinbase 주식 토큰을 사면 주식을 갖나? / A : 아님, SPV가 Alpaca 분리 계좌에 보관한 기초주의 비례 수익권(ADGM 증서), 직접 투자 아님, FSRA는 증권으로 봄 [F-0079](https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf)
- Q : 주식 토큰 거래대금은? / A : 주주서한은 10억 달러 이상 F-0892(주주서한 PDF), CFO 발언은 약 30억 달러 F-0894(실적 발표 통화 녹취 PDF), 둘 다 회사 쪽 숫자이며 서로 다르고 하나로 고르지 않음
- Q : 점유율 10.7%는 누가 잰 것? / A : 회사 주주서한 값, 제3자 데이터와 회사가 고른 경쟁사 집합 기준(전년 5.6%) F-0902(주주서한 PDF)
- Q : Kraken과 차이는? / A : Kraken은 미국 파생 인가 셋(중개, 거래소, 청산소)을 모두 인수 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us), Coinbase는 거래소만 인수하고 중개와 청산소는 직접 등록, 주식 토큰도 발행사 인수가 아니라 직접 발행 [F-0777](https://www.base.org/blog/tokenized-stocks)
