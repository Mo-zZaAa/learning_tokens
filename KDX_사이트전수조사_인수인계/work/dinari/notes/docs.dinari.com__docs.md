# notes: docs.dinari.com/docs 안내 글 13건 (SITE-dinari-1)
경로 기준: raw/는 H/work/dinari/raw/docs.dinari.com/. 코드 예제는 요약만.
## 페이지별 사실
### https://docs.dinari.com/docs/what-is-dshare
- dShare는 증권(보통 미국 주식)에 1:1로 담보된 토큰. 발행(mint)과 소각(burn)은 중개계좌에서 해당 주문이 완료된 뒤에만 발생. 흐름: 고객이 블록체인에 자금 에스크로와 주문, Dinari가 Alpaca에 주문 전달, Alpaca 체결, Dinari가 체결 통지, 토큰 발행. 환매는 반대 순서로 소각 후 자금 이체
  - 원문: "a mint (aka issuance) or a burn (aka redemption) only occurs when a corresponding order is complete on a brokerage account"
  - 위치: raw/docs.dinari.com/docs__what-is-dshare.md / How is it backed?
  - 틀: 핵심 사업 상세 > 발행 구조 > 발행 주체, 기초자산 보관
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/what-is-usd
- USD+는 Dinari가 발행하는 수익형 스테이블코인. 1:1 달러, 단기 미국 국채와 USD로 100% 담보, 일일 리베이스로 보유 지갑 잔고 증가(스테이킹, 클레임, 락업 불필요). dShares 플랫폼의 기본 정산과 환매 토큰이며 배당도 USD+로 지급. 발행은 USDC 또는 USDT 입금, 환매는 1USD+당 1달러를 USDC로, 정산 0~3일(규모에 따라)
  - 원문: "USD+ is a yield-bearing stablecoin issued by Dinari. It is pegged 1:1 to the US dollar"
  - 위치: raw/docs.dinari.com/docs__what-is-usd.md / 첫 단락, Minting and redeeming
  - 틀: 사업 구조 > 상품 기초자산 > 가상자산, 수익원
- 배포 체인: Ethereum, Avalanche C-Chain, Base, Arbitrum, Plume
  - 위치: raw/docs.dinari.com/docs__what-is-usd.md / Where USD+ is available
  - 틀: 핵심 사업 상세 > 거래 구조 > 사용 블록체인
- 조사 질문 관련도: 중간
### https://docs.dinari.com/docs/regional-requirements
- 본문 없음(제목과 하위 링크 US Customers만)
- 조사 질문 관련도: 낮음(쓸 내용 없음, 사유: 빈 안내 페이지)
### https://docs.dinari.com/docs/restrictions
- 미지원 국가: 캐나다(라이선스 취득 진행 중이라고 밝힘). 그 밖에 OFAC, FATF 등과 협력해 지원하지 않는 국가 31개 나열(아프가니스탄, 벨라루스, 보스니아헤르체고비나, 중앙아프리카공화국, 크로아티아, 쿠바, 콩고민주공화국, 에티오피아, 기니비사우, 이란, 이라크, 코소보, 레바논, 리비아, 북마케도니아, 말리, 몬테네그로, 미얀마, 니카라과, 북한, 러시아, 세르비아, 슬로베니아, 소말리아, 남수단, 수단, 시리아, 우크라이나, 베네수엘라, 예멘, 짐바브웨). 한국은 목록에 없음
  - 원문: "For some regions, we are in the process of securing proper licensing to operate: Canada"
  - 위치: raw/docs.dinari.com/docs__restrictions.md / Unsupported Countries
  - 틀: 핵심 사업 상세 > 최종 투자자 > 국적 및 지역 제한
- 미지원 업종(Enterprise 파트너 프로그램): 도박, 대마, 총기와 탄약, 귀금속 서비스, 성인물, 현금 거래, FX 서비스
  - 위치: raw/docs.dinari.com/docs__restrictions.md / Unsupported Sectors
  - 틀: 핵심 사업 상세 > 최종 투자자 > 대상
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/us (US Customers, 2026-06-22 갱신, 페이지 업데이트 10일 전)
- 미국 법적 성격: 미국에서 dShares는 기초 증권에 대한 실제 소유의 "2차 원장"이며 1933년 증권법, 1934년 증권거래소법, Reg NMS 등의 보호 대상이라고 밝힘. Dinari Securities LLC가 SEC와 FINRA 감독 하의 브로커딜러, 통합 파트너(디지털자산 또는 핀테크 플랫폼)는 온보딩과 접점 제공자일 뿐 매매 체결, 추천, 감독 불가(FINRA 3110)
  - 원문: "Dinari dShares are a secondary ledger for real ownership in the underlying securities"
  - 위치: raw/docs.dinari.com/docs__us.md / Overview
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격, 기업 개요 > 취득 라이선스 > 미국
- 미국 고객 계좌는 모두 Dinari Securities LLC가 Alpaca 청산 관계 하에서 개설과 유지. 온보딩, KYC/AML, 기록보존(17a-3, 17a-4), CAT 보고, 거래감시는 Dinari Securities 책임
  - 위치: raw/docs.dinari.com/docs__us.md / Serving US Customers
  - 틀: 사업 구조 > 서비스 범위 > 고객 접점
- 미국 고객 자격: 미국 시민, 영주권자와 임시 거주자, 미국 세법상 납세자(US tax persons). 파트너 요건: KYB와 보충 계약, 실명 공개(omnibus 풀링 금지), 검증된 이메일, API v2 사용, Dinari 승인 UI, 라이브 계정 감사, OFAC 스크리닝, 30일마다 제재와 PEP 스크리닝
  - 원문: "Partners may not intermediate or pool orders (\"omnibus accounts\") for US customers."
  - 위치: raw/docs.dinari.com/docs__us.md / US Customer Qualifications, Requirements
  - 틀: 핵심 사업 상세 > 최종 투자자 > 대상, 국적 및 지역 제한
- 미국 특수 조건: 발행 토큰은 현재 비양도이며 DeFi 프로토콜 사용 제한, 미국 고객은 래핑 dShares 불가, 전용 지갑에만 발행(옴니버스 지갑 불가), ACH 선입금 또는 JIT 입금, 고객 UI에 "블록체인 네이티브 토큰이 아님" 고지 필수, NBBO 데이터 매 15초 갱신, 마케팅은 FINRA 2210 사전 검토
  - 원문: "Issued tokens are currently non-transferrable and are restricted from use in DeFi protocols."
  - 위치: raw/docs.dinari.com/docs__us.md / Special Considerations
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리, 거래 구조 > 거래 방식
- 입금: 스테이블코인 입금은 주 머니트랜스미터 법과 연방 MSB 규정 관할이라고 밝히고, Circle Internet Financial과 제휴해 실시간 결제. 미국 관할 계좌는 USDC만 지원. 흐름: 고객 지갑 → Dinari 관리 지갑 → BitGo → USD → 브로커리지 계좌. 머니트랜스미터 면허 보유 파트너는 Funding Facilitation Account로 JIT 입금 가능
  - 위치: raw/docs.dinari.com/docs__us.md / Funding Flows
  - 틀: 사업 구조 > 서비스 범위 > 결제 (BitGo는 flowchart 코드에서만 확인, 의미 확인 필요)
- 적격투자자: 사모와 미등록 증권(사모신용 펀드, 지수 토큰 등)은 적격투자자만. 자격 구분은 Get Stocks 엔드포인트에 표시. 자격 기준 소득 20만 달러(공동 30만) 또는 순자산 100만 달러(주거 제외)
  - 위치: raw/docs.dinari.com/docs__us.md / Accredited Investors
  - 틀: 핵심 사업 상세 > 최종 투자자 > 대상
- 수익원(파트너 부문): 실시간 NBBO 시세 조회 유료(요청당 0.0075달러, 미국 고객이 정규장에서 sip 피드 조회할 때만). UTP와 CTA 데이터 요금은 Dinari가 부담하고 파트너에 월별 청구
  - 위치: raw/docs.dinari.com/docs__us.md / Realtime Market Data (NBBO), Fee Schedule
  - 틀: 사업 구조 > 수익원
- 감독: Dinari Securities가 모든 미국 고객 활동 감독권 보유, 무작위 통합 감사, 데이터 요청 2영업일 내 협조, 보안 사고 24시간 내 보고
  - 위치: raw/docs.dinari.com/docs__us.md / Compliance Oversight and Audit
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/trading-hours
- 4개 세션(ET): 정규 9:30-16:00(시장가와 지정가), 확장(프리 4:00-9:30, 애프터 16:00-20:00, 지정가만), 야간(전날 20:00-04:00 평일, 일요일 20:00 시작, 지정가만, 다음 영업일이 개장일일 때만 열림), Open 24/7(금 20:00-일 20:00 및 타 세션 폐장 시, 블록체인 전용, 지정가만, 일부 종목, 낮은 유동성). 시장가 주문은 비정규 세션에서 시장성 지정가로 자동 전환(매수는 최근 ASK, 매도는 최근 BID)
  - 원문: "Open (24/7) ... Limit only, blockchain only ... Limited tickers; lower liquidity"
  - 위치: raw/docs.dinari.com/docs__trading-hours.md / Sessions Overview, Session Details
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래시간, 유동성 확보 방안
- 정규장 시장가 주문 후 dShares는 30분 이내 지갑 도착. 미국 은행 휴일에 큰 거래는 T+2 결제 가능. 시장 휴장일에는 정규, 확장, Open(24/7) 세션 폐장(야간 세션 휴장 명시 없음)
  - 위치: raw/docs.dinari.com/docs__trading-hours.md / Common Scenarios, Holidays
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래시간
- 2026, 2027 NYSE 휴장표 수록(조사 관련도 낮음)
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/24-7-trading
- 24/7 세션 거래 가능 종목 9개: SPY, QQQ, AAPL, AMZN, META, MSTR, NVDA, SPCX(Space Exploration Technologies Corp., SpaceX), TSLA. 목록은 늘어날 예정
  - 위치: raw/docs.dinari.com/docs__24-7-trading.md / 표
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래시간, 유동성 확보 방안
  - 숫자: 종목 9개, 기준 2026-11-16 raw
- 조사 질문 관련도: 중간
### https://docs.dinari.com/docs/245-tradable-assets
- 본문 표가 수집되지 않음(제목과 부제만). 다른 전수 조사 대상 아님, 24/5 종목 목록은 미확인
- 조사 질문 관련도: 낮음(쓸 내용 없음, 사유: 표 미수집)
### https://docs.dinari.com/docs/blockchain
- dShares 지원 체인: Ethereum Mainnet, Arbitrum One, Avalanche C-Chain, Base, HyperEVM, HyperCore(Hyperliquid의 비EVM 호가창 계층), Plume. Kinto(질서 있는 종료)와 Blast는 지원 중단
  - 원문: "dShares are currently available on the following blockchains with many more coming soon."
  - 위치: raw/docs.dinari.com/docs__blockchain.md / Supported blockchains
  - 틀: 핵심 사업 상세 > 거래 구조 > 사용 블록체인
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/corporate-action-processing
- 지원 자산 전체에 대해 배당, 분할, 티커 변경, 합병을 처리하고 Dinari 플랫폼에 자동 반영. 파트너는 시장데이터 API로 확인해야 함. 소수주 포함 역분할과 합병 같은 예외는 Dinari 팀이 직접 연락
  - 위치: raw/docs.dinari.com/docs__corporate-action-processing.md / Supported Corporate Actions, Monitoring
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리
- 조사 질문 관련도: 중간
### https://docs.dinari.com/docs/fees
- 파트너 수수료: Dinari는 파트너와 최종 사용자에게 거래 수수료를 받지 않는다고 밝힘. 부과 항목은 API 접근료(월 2,000달러부터, 샌드박스 무료), 네트워크 수수료(표준 주문당 0.20달러, 이더리움 메인넷은 가스 연동), USDT 환전 수수료(오라클 가격 + 3bp, 월말 합산 청구), OTC 주문 수수료(최소 25,000달러, 스프레드 통상 10bp까지, USDC 또는 USDT 결제)
  - 원문: "Dinari does not collect transaction fees from our partners or their end users."
  - 위치: raw/docs.dinari.com/docs__fees.md / Standard Partner Fees, API Access Fees, Network Fees, USDT Conversion Fees, OTC Trading Fees
  - 틀: 사업 구조 > 수익원
  - 숫자: API 월 2,000달러부터, 네트워크 주문당 0.20달러, USDT 3bp, OTC 10bp까지(회사 가격표, 2026-11-10 갱신)
- 파트너가 `fee` 파라미터로 고객 수수료를 설정(기본값 0.20달러)해 Dinari가 대신 징수하거나 파트너가 후불 청구
  - 위치: raw/docs.dinari.com/docs__fees.md / How to Set Customer Transaction Fees
  - 틀: 사업 구조 > 수익원
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/faqs
- Dinari는 블록체인 상 전통 증권 거래 인프라. 질문 "실제 주식을 소유하나": "아니오. 제3자 수탁 브로커에서 보관하고, dShare를 사면 별도의 증권을 받는다. 기초 주식이 이를 담보하지만 회사의 직접 주주는 아니다"
  - 원문: "No, Dinari holds the underlying stocks in custody through a third-party custodial broker. When you purchase a dShare, you receive a separate security."
  - 위치: raw/docs.dinari.com/docs__faqs.md / Overview
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격, 투자자 권리
- 지역: "미국 외 85개 이상 관할에서 Regulation S 하에 제공". KYC 필수(신분증, 거주 증빙). 주문: MARKET과 LIMIT만, 정지와 트레일링 불가. 단일 결제로 매수 시 발행, 매도 시 소각. 공매도 미지원(인버스 ETF만). 5,000달러 초과 주문은 1~2일 소요 가능. 지원 종목 724개 이상(S&P 500 전체 포함). 지원 체인: Ethereum, Base, Arbitrum, Avalanche C-Chain, Plume(blockchain 페이지에 HyperEVM, HyperCore 추가로 불일치). 체인 간 이동은 LayerZero V2 OFT
  - 원문: "Dinari offers dShares in over 85 jurisdictions outside the United States under Regulation S."
  - 위치: raw/docs.dinari.com/docs__faqs.md / Getting Started, Trading & Orders, Supported Assets & Networks
  - 틀: 핵심 사업 상세 > 최종 투자자 > 국적 및 지역 제한, 거래 구조
  - 숫자: 724개 이상(지원 종목, FAQ 기준 2026-11-12 갱신)
- 발행 수수료(FAQ): 이더리움 1달러 + 0.25~0.50%, L2는 0.20달러 + 0.25~0.50%, 네트워크 수수료 별도. fees 페이지의 "거래 수수료 없음"과 불일치
  - 위치: raw/docs.dinari.com/docs__faqs.md / Fees & Costs
  - 틀: 사업 구조 > 수익원
- 배당은 USD+ 등 스테이블코인으로 기초 주식과 같은 일정에 지급
  - 위치: raw/docs.dinari.com/docs__faqs.md / Dividends & Corporate Actions
- 조사 질문 관련도: 높음
### https://docs.dinari.com/docs/taxes-reporting
- 비미국 고객 배당에 대해 미국 세법 1441조에 따른 30% 원천징수를 Dinari가 브로커 수준에서 자동 징수하고 IRS에 납부(2026-03-26 이후 지급분). 조약 감면은 W-8BEN 서류 제출, 초과 징수는 1040-NR로 환급 신청. 미국 고객은 Dinari Securities가 1099-DIV 발행
  - 원문: "Dinari will automatically withhold and remit 30% of all applicable U.S. stock dividends to the U.S. Internal Revenue Service"
  - 위치: raw/docs.dinari.com/docs__taxes-reporting.md / Taxes > Dividends
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리, 국내 시장과의 차이 > 제도 비교
- 보고: 온체인 조회, 옴니버스 지갑 파트너에게 월말 잔고 CSV, 거래 보고서 CSV 요청 가능
  - 위치: raw/docs.dinari.com/docs__taxes-reporting.md / Reporting
- 조사 질문 관련도: 중간
## 새로 나온 용어
- Managed Orders, Proxied Orders(EIP-155), Funding Facilitation Account(FFA), OFT(Omnichain Fungible Token), HyperCore, rebasing, Hosted Trading
## 서로 어긋나는 서술
- 수수료: fees 페이지 "거래 수수료 없음" vs FAQ "발행 주문 1달러(또는 0.20달러) + 0.25~0.50%"
- 지원 체인: FAQ 5개, blockchain 페이지 7개(HyperEVM, HyperCore 추가)
- 지원 관할: FAQ 미국 외 85개 이상(Reg S) vs 홈 91 + 미국
- 권리: FAQ "직접 주주 아님, 별도 증권" vs docs/us "실제 소유의 2차 원장"
## 더 봐야 할 것
- /docs/security, /docs/managing-kyc, /docs/hosted-trading, /docs/wrapping, /docs/hyperliquid, /docs/dividend-payments 등 정독 범위 밖
- 245-tradable-assets 표(수집 누락)
- BitGo의 역할(US 입금 흐름도에서만 등장)
