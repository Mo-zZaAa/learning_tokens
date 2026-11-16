# LIC 메모 (열람 2026-11-16)
조회 방법: FINRA BrokerCheck API(원문 sources/LIC/brokercheck_<CRD>.json), ESMA CASPS.csv(sources/LIC/ESMA_CASPS_2024-12.csv, 파일명은 2024-12지만 ac_lastupdate 최신 2026-11-11), NY DFS 면허 목록(sources/LIC/dfs_vc.html).
한계: BrokerCheck JSON은 사업 유형 상세(ATS, 청산 여부)를 주지 않아 하는 일은 법인 역할 기준(해당 행 근거 문장에 명시). NFA BASIC은 JS와 CSRF 기반 RPC라 직접 조회하지 않음. FCA 등록부는 SPA라 내용 없음. www.sec.gov, cftc.gov 열지 않음.
## 인수 또는 제휴 근거 (웹 검색 결과 수준, 원문 페이지는 직접 열지 못함. 교차 확인 필요)
- Robinhood가 Bitstamp 인수 완료 2025-06-02: https://robinhood.com/newsroom/robinhood-completes-acquisition-of-bitstamp (검색 결과 요약만). 등록부 쪽 근거: ESMA 목록의 Bitstamp Europe S.A.(CSSF), DFS 목록의 Bitstamp USA, Inc.
- Ondo가 Oasis Pro 인수 완료 2025-10: https://www.theblock.co/news/deals/2025-10-06-ondo-completes-acquisition-of-us-regulated-broker-oasis-pro-373547 (7월 발표, 10월 완료. 시점은 work/EXT-Ondo와 충돌 표기). 등록부 근거: BrokerCheck 149420 owner ONDO FINANCE INC., 기존 명칭 LAVECCHIA CAPITAL LLC.
- Kraken이 NinjaTrader 인수 완료 2025-05-01: https://www.businesswire.com/news/home/20250501627804/en/Kraken-Completes-Acquisition-of-NinjaTrader (검색 결과 요약만). 등록부 확인 못 해 licenses.csv에 없음.
- Coinbase Capital Markets Corp(CRD 10722)는 1982년 CRD, 이전 명칭 다수(Auour Advisory 등). 기존 BD를 취득해 개명한 것으로 보이나 인수 사실 출처 미확보. 확보 방식은 직접 등록으로 두되 미확인.
- 제휴로 빌림(청산 외부 위탁 등)은 이번에 등록부로 확인한 건 없음. BrokerCheck의 referOtherBd 값(Dinari Y, Kraken Securities Y, Robinhood Financial Y, Oasis Pro Y, Bruce Markets Y)은 다른 BD와의 관계 표시일 수 있으나 의미 미확인, 후속 확인 필요.
## 범위 밖
- 송금업 주별 면허는 DFS(뉴욕)만. Bakkt 등 다른 DFS 면허자는 제외.
- 열려 있던 BrokerCheck 부가 검색: tZERO Securities(CRD 123421) 등록부 JSON 저장만(licenses.csv 미포함).
