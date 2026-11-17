# Dinari 브리핑
- 축 : 증권사 역할을 대신하는 API로 핀테크 앱을 판매 창구로 붙여 미국 주식 토큰을 대는 B2B 공급사(자체 앱 Dinari Trading App은 보조 창구)
- 가설 : 둘 다 아님, 주식 토큰 B2B 공급 하나에 집중하나 그 영역 1등 아님(발행 잔액 1,520만 달러)

## 스토리라인

### 1. 출발: 미국 밖 지갑 이용자에게 직접 팔다가, 다른 회사 앱에 붙는 공급사로 방향을 정함
- 미국 안 판매 자격은 두 단계로 갖춤. 2022-05 Dinari, Inc.(본사, 토큰 기술 회사)가 SEC(미국 증권거래위원회)에 명의개서대리인(발행 회사를 대신해 주주 명부와 증권 이전을 기록하는 등록 자격)으로 등록했고, 2025-06 자회사 Dinari Securities가 증권사(broker-dealer, 고객 주문을 받는 등록 증권회사)로 승인받아 미국 53개 주와 영토에서 영업할 수 있게 됨 [F-1237](https://www.sec.gov/Archives/edgar/data/1915430/000191543022000003/0001915430-22-000003-index.html)[F-0116](https://api.brokercheck.finra.org/search/firm/329672)[F-0120](https://api.brokercheck.finra.org/search/firm/329672)
- Dinari는 2021년 설립된 미국 주식 토큰 회사이며, 2023-08 미국 밖 개인용 dShares(미국 주식과 ETF(상장지수펀드)에 1:1로 대응하는 Dinari의 토큰 상품)를 출시함 [F-1053](https://dinari.com/blog/chainlink-ccip-arbitrum-ethereum-usdplus)[F-0273](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)
  - 설립 이유 : 멕시코, 태국 같은 나라는 증권계좌 보유율이 1% 미만이지만 블록체인 지갑 보유율은 5%에서 10%에 이를 수 있어, 증권계좌 대신 지갑으로 미국 주식에 투자하게 하려는 것이라고 회사가 밝힘 [F-0274](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)
  - 처음에는 자체 웹 앱으로 직접 팔았음. 2023-09 지갑을 연결해 가입하는 이용자에게 가입 보너스와 추천 보상(Apple 주식 토큰)을 주는 프로그램을 운영함 [F-1480](https://dinari.com/blog/dinari-sign-up-bonus-referral-program)
- 6개월 뒤인 2024-02 기업용 API(다른 회사 앱이 Dinari 기능을 불러 쓰는 연결 규격)를 공개하며 판매 방식을 바꿈. 2024-07부터는 핀테크 앱이 자기 화면 안에 dShares를 끼워 넣는 방식이 중심이 됨 [F-0277](https://dinari.com/blog/b2b-api-and-managed-account)[F-1204](https://dinari.com/blog/ecosystem-api-partners)
  - 회사가 밝힌 이유 : 핀테크와 네오뱅크(지점 없는 모바일 은행)가 미국 주식을 넣으려면 여러 업체와 여러 나라 법, 규제를 거쳐 수개월이 걸리는데, Dinari API 하나로 미국 증권업 규정을 직접 다루지 않고 빠르게 출시할 수 있다는 것 [F-1483](https://dinari.com/blog/12m-series-a-equities-onchain)
  - 파트너는 증권사 등록 없이 판매하고, 증권 계좌 관계, 결제, 보관, 규정 준수는 Dinari가 맡는 구조임 [F-0332](https://dinari.com/business)[F-0335](https://dinari.com/get-started)
  - 외부 시각도 같음. Reuters(국제 통신사)는 Dinari가 Charles Schwab, Robinhood 같은 개인 증권사와 달리 고객에게 직접 서비스하지 않고 다른 회사 플랫폼에 자기 화면을 넣는 회사라고 보도함 [F-1475](https://whbl.com/2025/06/26/dinari-granted-first-broker-dealer-registration-to-offer-tokenized-stocks/)
  - 회사도 2026-09 목표를 "토큰 주식의 단일 목적지를 만드는 것이 아니라, 투자자가 이미 돈을 관리하는 금융 플랫폼 곳곳에서 미국 주식을 쓸 수 있게 하는 것"으로 정리함 [F-1484](https://dinari.com/blog/dinari-powers-bitcoin-coms-u-s-launch-of-tokenized-equities)
  - 자체 앱은 보조 창구로 남음. 미국판 출시 때도 Dinari Trading App(자체 앱)을 파트너 8곳과 함께 판매 창구로 둠 [F-1487](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)[F-0293](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
  - 해석 : 지갑 보유율이 증권계좌보다 높다는 설립 논리에 따르면 고객은 이미 지갑과 송금 앱 안에 있음. 시드 투자 1,000만 달러(2023 말) 규모의 신생 회사가 그 고객을 직접 모으기보다 고객을 가진 앱에 붙는 쪽을 택한 것으로 보임. 자체 앱 출시(2023-08) 6개월 만에 기업용 API로 옮겼기 때문 [F-0274](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)[F-0275](https://dinari.com/blog/weve-closed-10-million-in-seed-funding-and-added-new-dshares)[F-0273](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)[F-0277](https://dinari.com/blog/b2b-api-and-managed-account)

### 2. 자산: 명의개서대리인과 증권사 자격을 직접 갖추고, 그 위에 급여, 송금, 투자 앱, 지갑, 거래소, 증권사를 판매 창구로 붙임
- 인가는 명의개서대리인을 먼저(2022), 증권사를 나중(2025)에 받음
  - 명의개서대리인은 신청서(Form TA-1)를 내면 SEC가 막지 않는 한 30일째 효력이 생기는 등록임. Dinari는 2022-04-05 신청, 2022-05-05 SEC 수리로 한 달 만에 갖춤 [F-1478](https://www.ecfr.gov/current/title-17/section-240.17Ac2-1)[F-1237](https://www.sec.gov/Archives/edgar/data/1915430/000191543022000003/0001915430-22-000003-index.html)
  - 증권사는 FINRA(미국 증권사 자율규제기구)가 신청서, 면담, 법규 준수 능력을 심사해야 회원이 됨. Dinari Securities는 2023-12-05 법인 설립에서 2025-06-20 승인까지 약 1년 6개월이 걸림 [F-1479](https://www.finra.org/rules-guidance/rulebooks/finra-rules/1014)[F-0117](https://api.brokercheck.finra.org/search/firm/329672)[F-0116](https://api.brokercheck.finra.org/search/firm/329672)
  - 명의개서대리인이 연 것 : 미국 밖 판매는 Regulation S(미국 밖에서 미국인 아닌 사람에게 파는 증권은 미국 공모 등록이 필요 없다는 규정)로 미국 인가 없이 가능했고, 회사는 명의개서대리인 등록을 "실물자산 담보 토큰의 신뢰받는 표준"이 되기 위한 신뢰 근거로 내세움(2023-08, 2024-01). 지금은 파트너에게 주는 기능 목록에 명의개서 서비스가 들어 있음 [F-0338](https://docs.dinari.com/docs/faqs)[F-1481](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)[F-1482](https://dinari.com/blog/future-finance-tokenized-real-world-assets)[F-1485](https://dinari.com/blog/dinari-powers-bitcoin-coms-u-s-launch-of-tokenized-equities)
  - 증권사가 연 것 : 그 전에는 미국인이 이용할 수 없었음. 증권사 등록으로 처음 미국 투자자 대상 판매가 가능해졌다고 Reuters가 보도했고, 2026-08-04 미국 적격 투자자와 미국 사업자용 724종(미국 대형주 지수 S&P 500 전 종목 포함)을 출시함. 미국 투자자는 증권사 계좌 속 주식 자체를 소유하고 토큰은 그 2차 기록임 [F-0313](https://dinari.com/us/disclosures)[F-1476](https://whbl.com/2025/06/26/dinari-granted-first-broker-dealer-registration-to-offer-tokenized-stocks/)[F-1131](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)[F-0996](https://dinari.com/us/disclosures)
  - 같은 등록으로 미국 증권사, 은행, 핀테크가 Dinari 인프라를 라이선스해 자기 고객에게 파는 길도 열림 [F-1487](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
  - 해석 : 순서는 걸리는 시간과 필요한 시점에 맞춘 것으로 보임. 미국 밖 판매는 미국 인가가 필요 없어 한 달이면 되는 명의개서 등록으로 신뢰 근거만 먼저 갖추고 출시했고, 심사가 긴 증권사는 미국인 판매를 위해 나중에 받음. CEO도 출발점을 "미국에서 합법인 토큰 주식 표준"이라고 말함 [F-1478](https://www.ecfr.gov/current/title-17/section-240.17Ac2-1)[F-1479](https://www.finra.org/rules-guidance/rulebooks/finra-rules/1014)[F-1477](https://whbl.com/2025/06/26/dinari-granted-first-broker-dealer-registration-to-offer-tokenized-stocks/)
- 판매 창구는 파트너 유형별로 넓힘. 아래 거래대금은 모두 회사 사례 연구의 자체 집계이고 기간이 달라 합산하지 않음
  - 급여 : Cadana(100개국 이상 급여, 해외 지급 회사)가 급여를 받은 직원이 같은 앱에서 바로 투자하게 하려고 붙임. 거래대금 127만 달러 이상, 주문 1,426건(2026-01-01~2026-06-15) [F-1497](https://dinari.com/case-studies/cadana)[F-0347](https://dinari.com/case-studies/cadana)
  - 송금, 국경 간 금융 : Meru(중남미 프리랜서, 원격 근무자용 해외 수취와 달러 보관 앱)는 증권 인프라를 직접 만들지 않고 붙임. 거래대금 440만 달러 이상, 고객 4,814명, 44개국(2026-01-01~2026-07-15)으로 사례 중 가장 큼 [F-1496](https://dinari.com/case-studies/meru)[F-0350](https://dinari.com/case-studies/meru). Kem(달러 송금, 가상자산, 카드 지출을 묶은 앱)도 걸프 지역 이용자에게 724종을 연동함 [F-1491](https://dinari.com/blog/kem-brings-tokenized-u-s-equities-to-its-global-money-platform-with-dinari)
  - 투자 앱 : Fasset(신흥국 대상 디지털 자산 앱) 거래대금 144만 달러 이상. Eldora는 표의 52만 달러와 본문의 10.1만 달러 이상이 서로 다름 [F-0349](https://dinari.com/case-studies/fasset)[F-0348](https://dinari.com/case-studies/eldora)
  - 지갑 : Bitcoin.com 지갑(가상자산 지갑 앱, 회사 발표문 기준 누적 지갑 8,400만 개 이상)이 2026-05 미국 밖, 2026-09 미국 이용자에게 개시함. Dinari가 만든 완성형 거래 화면(Embedded Trading App)을 처음 쓴 파트너임 [F-1486](https://dinari.com/blog/bitcoincom-and-dinari-bring-tokenized-equities-and-etfs-to-global-investors)[F-0286](https://dinari.com/blog/bitcoincom-and-dinari-bring-tokenized-equities-and-etfs-to-global-investors)[F-1485](https://dinari.com/blog/dinari-powers-bitcoin-coms-u-s-launch-of-tokenized-equities)
  - 거래소 : Hyperliquid(블록체인 위 거래소)에 SpaceX 토큰을 첫 미국 주식 현물로(회사 주장) 상장해 첫 달 거래대금 1,180만 달러 이상(회사 집계). 신원확인 없는 환경으로 나가면 일부 주주 권리가 멈추는 방식으로 규제 밖 시장에도 공급함 [F-0354](https://dinari.com/case-studies/hyperliquid)[F-0353](https://dinari.com/case-studies/hyperliquid)
  - 증권사 채널 : 2026-07 tZERO(미국 토큰증권 증권사, NYSE 운영사 ICE가 소수 지분 보유)와 제휴. tZERO가 중개, 보관, 청산, 결제를 맡고 Dinari는 토큰 기술을 맡아 다른 증권사가 한 번의 연동으로 토큰 주식을 팔게 하는 틀임 [F-0288](https://dinari.com/blog/dinari-and-tzero-partner)[F-1402](https://www.financemagnates.com/institutional-forex/ice-taps-tzero-to-help-build-nyse-tokenized-securities-infrastructure/)
  - 거래 지원 : Flow Traders(시장조성 회사, 호가를 계속 내는 회사)가 정규장 밖 호가를 맡아 24시간 거래 9종목 [F-1036](https://dinari.com/blog/flow-traders-and-dinari-partner-to-unlock-24-7-tokenized-equity-markets)[F-0343](https://docs.dinari.com/docs/24-7-trading)
- 판매 창구를 늘리는 방법도 파트너가 쉽게 붙도록 만듦. 2024-09 미국 밖 핀테크에 1년 무료 거래 크레딧 1만 달러를 주는 유인 프로그램을 열었고, 파트너에게 거래 수수료 대신 월 2,000달러부터의 API 이용료와 주문당 0.20달러 네트워크 수수료를 받음 [F-1493](https://dinari.com/blog/fintech-developer-incentive-program)[F-0336](https://docs.dinari.com/docs/fees)

### 3. 비전: 핀테크 공급사에서 증권사와 기관이 쓰는 토큰 증권 인프라로
- 회사가 내건 방향은 시점마다 넓어짐
  - 2023-08 : "실물자산 담보 토큰의 신뢰받는 표준" [F-1481](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)
  - 2025-05 : 미션 "누구나 어디서든 미국 주식시장에 즉시, 규정을 지켜 접근" 그리고 이를 API 하나로 핀테크에 공급 [F-1114](https://dinari.com/blog/12m-series-a-equities-onchain)[F-1483](https://dinari.com/blog/12m-series-a-equities-onchain)
  - 2025-06 : CEO "최종 목표는 온체인 증권사만이 아니라 온체인 거래소" [F-1477](https://whbl.com/2025/06/26/dinari-granted-first-broker-dealer-registration-to-offer-tokenized-stocks/)
  - 2026-07 : 자체 체인 DFN(Dinari Financial Network, 2025-08 출시한 자체 블록체인, Avalanche 기술 기반)을 증권사, 거래소, 발행사, 수탁사, 명의개서대리인을 잇는 기관 참여 틀로 다시 정의함. 참여 증권사는 자기 고객과 화면을 그대로 두고 거래부터 주주 서비스까지 받음 [F-0282](https://dinari.com/blog/dinari-launches-the-dinari-financial-network-an-omni-chain-orderbook-powered-by-avalanche)[F-0287](https://dinari.com/blog/the-dinari-financial-network)[F-1488](https://dinari.com/blog/the-dinari-financial-network)
  - 2026-09 : 기관 사업 세 기둥을 명시 "기존 금융기관에 통합, 토큰 증권 기반 신상품, 탈중앙 시장으로 확장" [F-0296](https://dinari.com/blog/dinari-expands-business-development-team)
- 기둥별 실제 행동
  - 기존 금융기관 통합(실행 중) : 증권사 등록(2025-06), tZERO 제휴(2026-07), 미국 증권사용 API(2026-08), 증권사와 기관 담당 부사장 영입(2026-09) [F-0116](https://api.brokercheck.finra.org/search/firm/329672)[F-0288](https://dinari.com/blog/dinari-and-tzero-partner)[F-1487](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)[F-0296](https://dinari.com/blog/dinari-expands-business-development-team)
  - 토큰 증권 기반 신상품(초기) : 2025-10 S&P Dow Jones Indices(미국 지수 회사)와 미국 상장사 35종, 가상자산 15종을 묶은 지수를 만들고 Dinari가 토큰화함 [F-1489](https://dinari.com/blog/s-p-dow-jones-indices-and-dinari-launch-s-p-digital-markets-50-as-official-index-for-top-crypto-tokens-and-u-s-equities)
  - 탈중앙 시장 확장(실행 중) : Hyperliquid 상장, Flow Traders 24시간 호가 [F-0354](https://dinari.com/case-studies/hyperliquid)[F-0343](https://docs.dinari.com/docs/24-7-trading)
  - 온체인 거래소(말하고 진행 중) : 자체 체인 출시와 검증자(가상자산 거래소 Gemini, 수탁 회사 BitGo, 자산운용사 VanEck) 확보까지 진행함 [F-0283](https://dinari.com/blog/dinari-launches-the-dinari-financial-network-an-omni-chain-orderbook-powered-by-avalanche)[F-1035](https://dinari.com/blog/dinari-launches-the-dinari-financial-network-an-omni-chain-orderbook-powered-by-avalanche)
- 비슷한 API를 파는 다른 회사와의 차이
  - Alpaca(미국 청산 증권사) : Broker API로 최종 고객의 증권 계좌 개설, 입금, 매매를 만들게 하며, 문서상 이용자는 증권사와 투자자문사임. 토큰은 직접 발행하지 않고 토큰 발행사에 원주 보관과 발행, 소각 API를 줌 [F-1494](https://docs.alpaca.markets/docs/about-broker-api)[F-1495](https://alpaca.markets/tokenization)
    - Dinari는 Alpaca 위층에 있음. Dinari의 주문 집행, 청산, 보관도 Alpaca가 맡고, Dinari는 토큰 발행과 증권사 역할을 맡아 파트너가 증권사 등록 없이 지갑 고객에게 팔게 함 [F-0315](https://dinari.com/us/disclosures)[F-0332](https://dinari.com/business)
  - Ondo(미국 토큰 발행 회사) : 대형 가상자산 거래소와 지갑(Bitget 등)에 공급하고, 미국 증권사 자격은 인수(Oasis Pro, 미국 토큰증권 증권사, 2025-10)로 얻음 [F-0202](https://cfotech.news/story/bitget-widens-ondo-tokenised-stocks-etfs-metals)[F-1216](https://ondo.finance/blog/ondo-acquires-oasis-pro)
  - Backed/xStocks(Kraken 그룹의 주식 토큰) : 모회사 Kraken(미국 가상자산 거래소)을 첫 판매처로 두고 100곳 이상 파트너에 연동함 [F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)[F-0162](https://www.payward.com/press-release/xstocks-one-year)
  - Dinari만의 차이 : 고객 신원확인, 주문, 기업행위, 배당, 명의개서까지 증권사 기능을 묶어 소형 핀테크에 주고, 필요하면 거래 화면까지 줌. 미국판은 투자자가 주식 자체를 소유하는 구조이며, Ondo 토큰은 발행사에 대한 담보부 채권임 [F-1485](https://dinari.com/blog/dinari-powers-bitcoin-coms-u-s-launch-of-tokenized-equities)[F-0996](https://dinari.com/us/disclosures)[F-0998](https://www.mfsa.mt/wp-content/uploads/2026/01/Ondo-Global-Markets-BVI-Limited-Final-Terms-Document-dated-11-November-2025.pdf)
- 1등이 아닌 이유
  - 발행 잔액(rwa.xyz, 토큰화 자산 집계 사이트의 제3자 집계) 1,520만 달러로 11위, 점유율 0.41%. 1위 Binance(세계 최대 가상자산 거래소) 13.6억 달러, 2위 Ondo 8.99억 달러, 3위 xStocks 6.77억 달러 [F-1027](https://app.rwa.xyz/stocks)[F-1021](https://app.rwa.xyz/stocks)[F-1022](https://app.rwa.xyz/stocks)[F-1023](https://app.rwa.xyz/stocks)
  - 2026-01-16 310만 달러(0.4%)에서 다섯 배로 늘었으나 점유율은 그대로임 [F-1031](https://cryptoslate.com/tokenized-equities-approach-1b-as-institutional-rails-emerge/)[F-1027](https://app.rwa.xyz/stocks)
  - 해석 : 파트너가 데려오는 고객만큼만 커지는 구조이며 파트너가 작기 때문으로 보임. 가장 큰 사례인 Meru가 6개월 반 동안 거래대금 440만 달러인 반면, 상위 3곳은 자기 거래소 고객(Binance, Kraken)이나 대형 거래소 유통(Ondo의 Bitget)을 가짐 [F-0350](https://dinari.com/case-studies/meru)[F-1021](https://app.rwa.xyz/stocks)[F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)[F-0202](https://cfotech.news/story/bitget-widens-ondo-tokenised-stocks-etfs-metals)
  - 해석 : 미국판은 개인당 하루 매수 합계 5,000달러 한도와 파트너의 주문 합산 금지가 있어 미국에서도 빠르게 커지기 어려운 조건임 [F-0314](https://dinari.com/us/disclosures)[F-0325](https://docs.dinari.com/docs/us)

### 4. 시장: 미국 밖은 Regulation S로 팔고, 현지 파트너 앱이 고객을 맡음
- 미국 밖은 Regulation S로 판매하고, 미국인은 쓸 수 없음. 기초 주식은 Dinari 명의 계좌(버뮤다 분리계정회사)에 둠 [F-0338](https://docs.dinari.com/docs/faqs)[F-0313](https://dinari.com/us/disclosures)[F-0997](https://cdn.prod.website-files.com/656fd13bce08f2dc3bc50573/695ee673aa80e179e884fafc_Dinari-dShares-Terms-and-Conditions-Revised-12-26-25-CLEAN-with-links.pdf)
- 판매 국가는 파트너가 늘 때마다 늘어남. 회사 서술 기준 60개국 이상(2025-05), 70개국 이상(2025-10), 85개 이상 관할(2026-11 FAQ), 홈페이지는 미국 포함 92개 관할(2026-11). 서술마다 기준이 달라 하나로 고르지 않음 [F-0281](https://dinari.com/blog/12m-series-a-equities-onchain)[F-1489](https://dinari.com/blog/s-p-dow-jones-indices-and-dinari-launch-s-p-digital-markets-50-as-official-index-for-top-crypto-tokens-and-u-s-equities)[F-0338](https://docs.dinari.com/docs/faqs)[F-0307](https://dinari.com/)
  - 신규 이용자 다수는 중남미(아르헨티나, 브라질)라는 투자사 500 Global(미국 벤처투자사)의 게시글이 있음 [F-0130](https://500.co/content/dinari-raises-us12-7m-series-a-to-make-it-easy-for-anyone-anywhere-to-access-and-invest-in-the-u-s-stock-market-markup-1177)
- 고객은 현지 파트너가 맡음
  - 파트너가 이미 고객 신원확인을 하면 그 정보를 Dinari API로 넘기고(AML(자금세탁방지) 프로그램 제출, Dinari 감사 가능), 하지 않으면 Dinari 화이트라벨 신원확인 화면을 씀 [F-1490](https://docs.dinari.com/docs/managing-kyc)
  - 예 : 중남미는 Meru(44개국 고객), 걸프 지역은 Kem, 싱가포르는 1exchange(사모시장 토큰 거래소) [F-0350](https://dinari.com/case-studies/meru)[F-1491](https://dinari.com/blog/kem-brings-tokenized-u-s-equities-to-its-global-money-platform-with-dinari)[F-0137](https://www.finanzen.net/nachricht/aktien/1exchange-and-dinari-partner-to-empower-cross-border-access-to-tokenized-us-securities-15263890)
- 현지 규제는 회사 서술로 유럽은 MiFID II(EU 투자회사 규정) 아래 유통, 중남미는 디지털 결제 라이선스 아래 유통임. 캐나다는 인가 추진 중이라 미지원임 [F-0271](https://dinari.com/dshares)[F-0272](https://docs.dinari.com/docs/restrictions)
- 자산 순서 : 미국 주식 20종(2023-12) → 약 100종(2024 말) → 724종(2026-08, 미국 안과 밖 공통) → 한국 상장주 해외 유통 검토(2026-09) [F-0275](https://dinari.com/blog/weve-closed-10-million-in-seed-funding-and-added-new-dshares)[F-0278](https://dinari.com/blog/dinaris-2024-year-in-review-assets-apis-and-more)[F-0339](https://docs.dinari.com/docs/faqs)
  - 한국 : 2026-09-29 카카오페이증권과 한국 상장주를 토큰으로 해외 투자자에게 유통하는 시험(PoC) 업무협약을 맺었고, 상용화 여부와 시점은 미정임. 카카오페이증권은 전날 Ondo와도 협약함 [F-0131](https://www.etoday.co.kr/news/view/2630410)[F-0133](https://www.etoday.co.kr/news/view/2630410)[F-0136](https://www.mt.co.kr/stock/2026/09/29/2026092916273597892)

### 5. 정체성 변화와 당국 관계: 핀테크 공급사에서 미국 증권사와 기관용 인프라로
- 직접 판매(2023 자체 웹 앱) → 핀테크 API 공급(2024~2025) → 미국 증권사와 기관이 쓰는 토큰 증권 인프라(2026, tZERO, DFN 재정의, 미국 증권사 API, 기관 영업 조직)로 옮겨 가는 중임 [F-1480](https://dinari.com/blog/dinari-sign-up-bonus-referral-program)[F-0277](https://dinari.com/blog/b2b-api-and-managed-account)[F-0288](https://dinari.com/blog/dinari-and-tzero-partner)[F-0287](https://dinari.com/blog/the-dinari-financial-network)[F-0296](https://dinari.com/blog/dinari-expands-business-development-team)
- 당국 관계 : 증권사의 징계, 고객 분쟁 공시 0건. 2026-07 업계 단체 Blockchain Association(미국 가상자산 업계 단체)에 가입해 미국 정책 논의에 참여하고, SEC가 2026-01 성명에서 설명한 보관형 토큰 모델의 개척자라고 스스로 말함(회사 주장) [F-0119](https://api.brokercheck.finra.org/search/firm/329672)[F-1039](https://dinari.com/blog/dinari-joins-blockchain-association)[F-0290](https://dinari.com/blog/dinari-joins-blockchain-association)

### 6. KSF 후보: 미국 자격을 먼저 갖추고 증권사 기능을 묶어 파트너에게 넘김(점유율은 0.4% 안팎)
- 대상 : 증권사 등록이 없는 급여, 송금, 투자 앱, 지갑과 이미 고객이 있는 증권사 [F-0332](https://dinari.com/business)[F-0288](https://dinari.com/blog/dinari-and-tzero-partner)
- 운영 방식 : 파트너는 고객과 화면을 갖고, Dinari는 신원확인 대행, 주문, 보관 위탁, 기업행위, 명의개서를 맡음 [F-1490](https://docs.dinari.com/docs/managing-kyc)[F-1485](https://dinari.com/blog/dinari-powers-bitcoin-coms-u-s-launch-of-tokenized-equities)
- 선점 : 증권사 등록(2025-06)은 Ondo의 증권사 인수(2025-10)보다 4개월 빨랐고, 미국판 724종(2026-08)은 Ondo 미국 보관형 2종(2026-07)보다 넓음. 회사는 각각을 업계 처음이라고 주장함 [F-0116](https://api.brokercheck.finra.org/search/firm/329672)[F-1216](https://ondo.finance/blog/ondo-acquires-oasis-pro)[F-1131](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)[F-1128](https://ondo.finance/blog/ondo-launches-tokenized-securities-in-usa)[F-1205](https://500.co/content/dinari-makes-history-with-first-u-s-broker-dealer-license-for-tokenized-stocks-unlocking-lower-trading-costs-24-7-trading-and-more-markup-1186)[F-1206](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
- 효과 : 잔액은 2026-01-16 310만 달러에서 2026-11-16 1,520만 달러로 다섯 배가 됐으나 점유율은 0.4%에서 0.41%로 제자리임 [F-1031](https://cryptoslate.com/tokenized-equities-approach-1b-as-institutional-rails-emerge/)[F-1027](https://app.rwa.xyz/stocks)

### 7. 가설: 투자금이 작은 신생 회사라는 점이 파트너 판매와 직접 등록을 택하게 함
- Dinari는 2021년 설립된 비상장 신생 회사이며 누적 투자금은 2,265만 달러임. 공동 창업자는 CEO Gabriel Otte와 최고법무책임자(CLO) Chas Rampenthal 등임 [F-1053](https://dinari.com/blog/chainlink-ccip-arbitrum-ethereum-usdplus)[F-0279](https://dinari.com/blog/12m-series-a-equities-onchain)[F-1054](https://dinari.com/blog/dinari-at-token2049-exploring-securities-backed-tokens)
- 해석
  - 고객을 직접 모을 자금이 적어 고객을 가진 앱에 붙는 길을 택한 것으로 보임. 자체 앱 출시 6개월 만에 기업용 API로 옮겼기 때문 [F-0273](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)[F-0277](https://dinari.com/blog/b2b-api-and-managed-account)
  - 같은 이유로 인가도 인수보다 직접 등록을 택한 것으로 보임. Ondo는 증권사를 인수로 얻었으나 Dinari는 1년 6개월을 들여 직접 등록함 [F-1216](https://ondo.finance/blog/ondo-acquires-oasis-pro)[F-0117](https://api.brokercheck.finra.org/search/firm/329672)[F-0116](https://api.brokercheck.finra.org/search/firm/329672)
  - 법무 책임자가 공동 창업자인 구성은 제품 출시(2023-08)보다 명의개서 등록(2022-05)을 먼저 한 순서와 맞음 [F-1054](https://dinari.com/blog/dinari-at-token2049-exploring-securities-backed-tokens)[F-1237](https://www.sec.gov/Archives/edgar/data/1915430/000191543022000003/0001915430-22-000003-index.html)[F-0273](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform)
  - 그 결과 규제 자격은 먼저 갖췄으나 고객 규모는 파트너 규모를 넘지 못함. 2026년 들어 증권사와 기관으로 판매 대상을 옮기는 것도 큰 고객을 가진 곳에 붙으려는 같은 논리로 보임 [F-1027](https://app.rwa.xyz/stocks)[F-0288](https://dinari.com/blog/dinari-and-tzero-partner)[F-0296](https://dinari.com/blog/dinari-expands-business-development-team)

## 1층 (키워드)
- 미국 안 판매 자격 : 명의개서대리인 Dinari, Inc. SEC 등록(2022-05), 증권사 Dinari Securities 등록(2025-06, 53개 주와 영토)
- 시작 : 미국 밖 개인용 미국 주식 토큰 dShares(2023-08), 종목 20종
- 붙인 것
  - 판매 창구 : 핀테크 앱 Meru, Cadana, Fasset(2024-07), 1exchange, Bitcoin.com 지갑, Hyperliquid, 증권사 채널 tZERO(모두 파트너)
  - 공급 기능 : 기업용 API(직접, 2024-02), 미국판 724종과 미국 증권사 API(직접, 2026-08)
  - 거래 지원 : 입금 Ramp, Transak, 24시간 호가 Flow Traders, 의결권 Broadridge(모두 파트너)
  - 자체 인프라 : 달러 토큰 USD+, 자체 체인 DFN(직접)
- 지금 하는 것 : 핀테크 앱, 지갑, 증권사에 API로 미국 주식 토큰 공급(724종 이상, 발행 잔액 1,520만 달러), 자체 앱 Dinari Trading App은 보조 창구
- 해외 진출
  - 미국 밖 판매 : Regulation S(미국 공모 등록 불요)
  - 현지 파트너 앱이 고객 담당(60개국 이상)

## 2층 (받치는 사실)
- 명의개서대리인 : Dinari, Inc/TA 등록 신청서(TA-1) 2022-04-05 접수, 2022-05-05 SEC 수리 [F-1237](https://www.sec.gov/Archives/edgar/data/1915430/000191543022000003/0001915430-22-000003-index.html)
- 증권사 : Dinari Securities 2025-06-20 FINRA 승인, SEC 등록 증권사, 주 등록 53곳(주, DC, 영토 포함) [F-0116](https://api.brokercheck.finra.org/search/firm/329672) [F-0120](https://api.brokercheck.finra.org/search/firm/329672)
- 시작 : 2023-08-14 미국 밖 dShare 플랫폼 출시, 시드 750만 달러 [F-0273](https://dinari.com/blog/7-5m-in-seed-investments-and-ex-us-launch-of-dshare-platform), 2023-12 종목 20종 [F-0275](https://dinari.com/blog/weve-closed-10-million-in-seed-funding-and-added-new-dshares)
- 기업용 API : 2024-02-29 B2B REST API 공개 [F-0277](https://dinari.com/blog/b2b-api-and-managed-account), 파트너는 증권사 등록 없이 단일 API로 판매 [F-0332](https://dinari.com/business)
- 앱 끼워 넣기 파트너 : Meru 고객 거래대금 440만 달러 이상, 고객 4,814명, 44개국(2026-07-15) [F-0350](https://dinari.com/case-studies/meru), Cadana 127만 달러 이상(2026-06-15) [F-0347](https://dinari.com/case-studies/cadana), 둘 다 회사 사례 연구 집계
- 24시간 호가와 온체인 거래소 : Flow Traders 제휴(2025-12-09) [F-1036](https://dinari.com/blog/flow-traders-and-dinari-partner-to-unlock-24-7-tokenized-equity-markets), 24시간 세션 9종목(2026-11-16) [F-0343](https://docs.dinari.com/docs/24-7-trading), Hyperliquid SpaceX dShare 첫 달 거래대금 1,180만 달러 이상(회사 집계) [F-0354](https://dinari.com/case-studies/hyperliquid)
- 지갑과 증권사 채널 : Bitcoin.com 지갑 300종 이상(2026-05-14) [F-0286](https://dinari.com/blog/bitcoincom-and-dinari-bring-tokenized-equities-and-etfs-to-global-investors), tZERO 증권사용 제휴(2026-07-08) [F-0288](https://dinari.com/blog/dinari-and-tzero-partner)
- 미국판 : 2026-08-04 자격 있는 미국 투자자와 사업자에 724종, 미국 증권사에 API(Circle 제휴) [F-1131](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses), 출시 파트너 8곳 [F-0293](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
- 지금 규모 : 지원 종목 724개 이상(회사 문서, 2026-11-12) [F-0339](https://docs.dinari.com/docs/faqs), 발행 잔액 1,520만 달러, 점유율 0.41%(rwa.xyz 제3자 집계, 2026-11-16) [F-1027](https://app.rwa.xyz/stocks)
- 해외 : 60개국 이상 이용(회사 주장, 2025-05) [F-0281](https://dinari.com/blog/12m-series-a-equities-onchain), 미국 밖판은 미국인 이용 불가 [F-0313](https://dinari.com/us/disclosures)

## 3층 (꼬리질문 대비)
- Q : SEC 조사나 제재가 있나 / A : FINRA 증권사 조회에서 징계, 고객 분쟁 공시 0건 [F-0119](https://api.brokercheck.finra.org/search/firm/329672)
- Q : 토큰을 사면 법적으로 무엇을 갖나 / A : 미국판은 증권사 계좌 속 주식 자체를 소유하고 토큰은 2차 기록 [F-0996](https://dinari.com/us/disclosures). 미국 밖판은 Dinari에 대한 기초자산 가치 청구권뿐, 주식 소유권 없음 [F-0997](https://cdn.prod.website-files.com/656fd13bce08f2dc3bc50573/695ee673aa80e179e884fafc_Dinari-dShares-Terms-and-Conditions-Revised-12-26-25-CLEAN-with-links.pdf)
- Q : 증권사가 망하면 보호되나 / A : dShares는 Dinari Securities가 보유하지 않아 SIPC(미국 증권사 파산 때 고객 계좌 보호 제도) 대상 아님 [F-0292](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
- Q : 인수한 회사가 있나 / A : 인수 0건. 증권사와 명의개서는 직접 등록, 주문 집행, 청산, 보관은 Alpaca(미국 청산 증권사)에 위탁 [F-0315](https://dinari.com/us/disclosures)
- Q : 숫자의 출처 등급은 / A : 파트너별 거래대금은 회사 사례 연구 집계이고 기간이 달라 합산하지 않음. Eldora는 표 52만 달러와 본문 10.1만 달러 이상이 어긋남 [F-0348](https://dinari.com/case-studies/eldora). 60개국은 회사 주장 [F-0281](https://dinari.com/blog/12m-series-a-equities-onchain). 발행 잔액은 rwa.xyz 제3자 집계 [F-1027](https://app.rwa.xyz/stocks)
- Q : 미국 밖 판매는 어떤 규정으로 하나 / A : 미국 공모 등록이 필요 없는 Regulation S [F-0338](https://docs.dinari.com/docs/faqs). 현지는 회사 서술로 유럽 MiFID II 하 유통, 중남미 디지털 결제 라이선스 하 유통 [F-0271](https://dinari.com/dshares)
- Q : 한국 관련은 / A : 2026-09-29 카카오페이증권과 한국 주식 해외 유통 MOU, PoC 단계 [F-0131](https://www.etoday.co.kr/news/view/2630410), 상용화 여부와 시점 미정 [F-0133](https://www.etoday.co.kr/news/view/2630410). 카카오페이증권은 전날 Ondo와도 MOU [F-0136](https://www.mt.co.kr/stock/2026/09/29/2026092916273597892)
- Q : 한국 개인이 쓸 수 있나 / A : 미국판은 만 18세 이상 미국 거주자만 [F-0319](https://dinari.com/bd/terms). 미국 밖판의 미지원 국가 목록(캐나다 외 31개국)에 한국은 들어 있지 않음 [F-0341](https://docs.dinari.com/docs/restrictions)
- Q : Ondo와 차이는 / A : 미국 자격을 Dinari는 직접 등록(2025-06), Ondo는 Oasis Pro 인수(2025-10) [F-1216](https://ondo.finance/blog/ondo-acquires-oasis-pro). 판매 창구는 Dinari가 소형 핀테크 앱, Ondo는 대형 가상자산 거래소 Bitget 등 [F-0202](https://cfotech.news/story/bitget-widens-ondo-tokenised-stocks-etfs-metals)
- Q : 가장 먼저 시작했는데 왜 작나 / A : 2023-08 시작, Kraken은 2025-06 [F-1040](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available). 지금 1위 Binance 13.6억 달러의 약 1/90 [F-1021](https://app.rwa.xyz/stocks). 해석 : 파트너 API는 파트너가 고객을 데려와야 커지는 구조
