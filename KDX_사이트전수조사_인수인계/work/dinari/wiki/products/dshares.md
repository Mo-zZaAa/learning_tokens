# dShares
확인일 2026-11-16. 회사가 밝힌 내용.

## 무엇인가
- 기초 증권(주로 미국 주식, ETF)에 1:1로 담보된 토큰. 발행과 소각은 중개계좌에서 해당 주문이 완료된 뒤에만 일어난다고 설명한다. [출처](https://docs.dinari.com/docs/what-is-dshare)
- 상품군 탭: Stocks, Sector/Asset Class ETF, Strategy ETFs, BDCs, REITs. [출처](https://dinari.com/dshares)
- S&P Digital Markets 50 Index($SPDM)는 주식 35종과 디지털자산 15종을 묶은 지수 상품. [출처](https://dinari.com/)
- 자산 발행사용 Direct Indexing Portfolios(DIPs)는 주식, ETF, RWA, 암호자산을 묶고 자동 리밸런싱과 환매를 지원한다고 소개한다. [출처](https://dinari.com/business)

## 발행과 수탁 구조
- 생애주기: 파트너 플랫폼에서 주문, Dinari Securities가 수탁 브로커리지 계좌에서 NMS 증권 취득, 검증된 지갑에 1:1 토큰 발행, 배당과 분할 자동 반영, 거래 또는 소각을 통한 직접 환매. [출처](https://dinari.com/dshares)
- 수탁은 Alpaca Securities LLC(CRD 288202, SEC 8-69928). [출처](https://dinari.com/dshares)
- 준비금은 Big 4 회계법인이, 스마트컨트랙트는 Hacken 등이 감사한다고 주장하나 법인명은 적혀 있지 않다. [출처](https://dinari.com/dshares)

## 법적 성격(서술이 갈린다)
- 미국 공시: dShare는 계좌의 주식 포지션을 반영하는 2차 기록 토큰이며 별도 투자가 아니다. 온체인 잔고와 계좌 기록이 다르면 계좌 기록이 우선한다. [출처](https://dinari.com/us/disclosures)
- docs 미국 편: 기초 증권 실소유의 2차 원장이며 1933년 증권법, 1934년 증권거래소법, Reg NMS 보호를 받는다고 서술. [출처](https://docs.dinari.com/docs/us)
- docs FAQ: 직접 주주는 아니고 dShare 구매 시 별도 증권을 받는다. [출처](https://docs.dinari.com/docs/faqs)
- business 페이지: 기초 증권에 대한 직접 청구권이 있고 합성 노출과 SPV가 없다. [출처](https://dinari.com/business)
- 비미국 유통 상품 중 Dinari, Inc.가 자기 명의로 주식을 보유하고 토큰을 발행하는 상품은 Dinari, Inc.의 상품이며 미국인은 플랫폼으로 이용할 수 없다. [출처](https://dinari.com/us/disclosures)
- Dinari는 컴플라이언스, 기업행위, 오류 시정을 위해 dShares를 동결, 차단, 되돌림, 소각, 재발행할 권리를 보유한다. [출처](https://dinari.com/bd/dshares-risk)
- 허가 없는 환경(Hyperliquid)으로 이동하면 restricted state가 되어 일부 소유권 권리가 복귀 시까지 정지된다. [출처](https://dinari.com/case-studies/hyperliquid)

## 투자자 권리
- 현금배당: 글로벌 홈과 FAQ는 USD+, 미국판과 미국 공시는 USDC. [출처](https://dinari.com/) [출처](https://dinari.com/us/disclosures)
- 분할 등 기업행위 자동 반영. [출처](https://docs.dinari.com/docs/corporate-action-processing)
- 의결권: Broadridge 위임장 인프라 연동 발표(2026-11-05). [출처](https://dinari.com/blog/broadridge-and-dinari-partner-to-bring-proxy-voting-to-dshares)
- 비미국 고객 배당에는 30% 미국 원천징수를 Dinari가 자동 징수한다(2026-03-26 이후 지급분). [출처](https://docs.dinari.com/docs/taxes-reporting)
- SIPC: Alpaca 계좌의 주식은 보호 대상, 자기수탁 지갑 등으로 옮긴 dShares와 USDC는 보호 밖. [출처](https://dinari.com/us/disclosures)

## 대상 고객과 제한
- 미국: 만 18세 이상 미국 거주자, 개인 비사업용 단독 계좌. [출처](https://dinari.com/bd/terms) 1일 매수 한도 합계 5,000달러. [출처](https://dinari.com/us/disclosures)
- 미국 고객이 받은 토큰은 현재 비양도이며 DeFi 사용 제한이라고 docs가 밝힌다(미국 공시는 자기수탁 지갑 이전 가능으로 서술, 어긋남). [출처](https://docs.dinari.com/docs/us)
- 미지원 국가: 캐나다(라이선스 취득 진행 중)와 31개국. 한국은 목록에 없으나 이는 한국 제공 인가를 뜻하지 않는다. [출처](https://docs.dinari.com/docs/restrictions)
- 지역 표기: 유럽 MiFID II 하 유통, 홍콩 일반 증권 취급, 중남미 디지털 결제 라이선스 하 유통(근거 인가 미제시). [출처](https://dinari.com/dshares)

## 거래 구조
- 거래시간(미국 고객 BD 경로): 정규 9:30-16:00 ET, 프리 4:00-9:30, 애프터 16:00-20:00, 주말과 휴장일 불가. [출처](https://dinari.com/bd/extended-hours)
- docs 4개 세션: 정규, 확장, 야간, Open(24/7, 블록체인 전용, 지정가, 일부 종목). 24/7 종목은 9개(SPY, QQQ, AAPL, AMZN, META, MSTR, NVDA, SPCX, TSLA). [출처](https://docs.dinari.com/docs/trading-hours) [출처](https://docs.dinari.com/docs/24-7-trading)
- 유동성: 정규장에는 거래소와 대체거래소 유동성을 모아 최선 체결, 장외 시간에는 Flow Traders가 시장조성. [출처](https://dinari.com/case-studies/flow-traders)
- 주문은 Alpaca로 보내 라우팅하며 FINRA Rule 5310 최선집행을 진다. [출처](https://dinari.com/us/disclosures)
- 지원 체인: Ethereum, Arbitrum One, Avalanche C-Chain, Base, HyperEVM, HyperCore, Plume(FAQ는 5개). [출처](https://docs.dinari.com/docs/blockchain) [출처](https://docs.dinari.com/docs/faqs)

## 해석
- 미국 고객 구조(브로커리지 계좌가 원본, 토큰은 기록)와 비미국 구조(Dinari, Inc. 보유 기반 토큰)는 법적으로 다른 상품일 가능성이 있다. 사이트만으로는 단정할 수 없다.
