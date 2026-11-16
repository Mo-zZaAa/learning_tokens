# LICMAP 대조 노트 (열람 2026-11-16, 14:37Z 전후)

입력 inputs/license_map/ 를 다시 조사하지 않고 db/licenses.csv, db/relations.csv, 감독기관 등록부와 대조함. db 파일은 수정하지 않음.

## 집계
- licenses.csv 51행: 등록부 일치 19, 다름 5, 등록부 미확인 20, 맡김 7(공시 확인 1, 공시 아님 6)
- relations.csv 28행 + acquisitions.csv 12행: DB 일치 19, DB에 없음 13, 다름 8 (relations_check.csv의 열1~6은 원본 파일마다 뜻이 다름. relations.csv는 유형, 주는 쪽, 받는 쪽, 내용, 시점, 링크. acquisitions.csv는 회사, 시점, 대상, 얻은 것, 이유, 링크)
- 우리 DB(db/licenses.csv 30줄) 중 맵과 직접 겹친 등록: Dinari Securities, Kraken Securities, Robinhood Financial, Robinhood Securities, Coinbase Capital Markets, Oasis Pro, Bitstamp Europe(MiCA). 나머지 일치는 이번에 직접 연 등록부(FINRA BrokerCheck, CFTC, CySEC, ESMA CSV)로 확인.

## 열어본 등록부
- FINRA BrokerCheck API: Alpaca, tZERO(2곳), Securitize Markets, Kraken, Robinhood, Coinbase, Dinari, Oasis 검색과 상세. NinjaTrader, Bitnomial, Nest, Bitstamp, Siebert 계열 BD는 검색 0건
- CFTC DCO 목록과 DCM 목록(cftc.gov, 셸 curl)
- CySEC 키프로스 투자회사 목록
- ESMA CASP CSV(407줄)
- 못 연 곳: NFA BASIC(API 403, 화면은 스크립트), ADGM FSRA 검색 앱(페이지는 열리나 검색 불가, 일부 호스트 502), CNMV(검색 403), SEC 명의개서대리인 서류(www.sec.gov 접근 불가, 우회 안 함), JFSC 저지와 BVI는 미시도(시간 상한)

## 회사별 요약
- Payward (Kraken): Kraken Securities BD 일치(등록 2024-06-10, 맵 2025.4와 시점 의미 다름). Form CRS(회사 공시)에서 Alpaca가 청산을 맡는 것 확인. 키프로스 법인은 Payward Europe Digital Solutions (CY) Limited, 라이선스 342/17, 2017-11-13(전신 법인 기준) 확인. Small Exchange와 Bitnomial의 DCM, DCO 등록 확인. NinjaTrader는 NFA 미확인. Backed Assets (JE)는 JFSC 미확인.
- Coinbase: Coinbase Capital Markets Corp 일치(이전 명칭에 KEYSTONE CAPITAL CORPORATION, 2018 Keystone 인수 추진과 부합). Coinbase Derivatives DCM(FairX 상호, 지정 2020-11-23), Coinbase Clearing DCO(2026-09-28) 일치. 아부다비 법인 두 곳과 Coinbase Financial Markets는 미확인. 맡김 두 행의 출처는 집계, 리서치라 공시 아님.
- Binance: Nest Exchange, Clearing and Custody, Trading, BTech 모두 ADGM 등록부를 못 열어 미확인. BrokerCheck에 Nest 법인 없음.
- Robinhood: Robinhood Financial 일치(2013-10-14). Robinhood Securities 시점 다름(2018.11 vs 2017-10-13). MIAXdx는 법인명이 다름(CFTC 현재 법인명 Rothera Exchange and Clearing LLC, 2026-01-20 개명). Bitstamp은 DB 등록(MiCA, NY DFS)과 부합. Jersey 발행 법인과 Robinhood Derivatives는 미확인.
- Dinari: 아래 별도 절.
- Ondo: Oasis Pro Markets LLC 일치(CRD 149420, 소유주 ONDO FINANCE INC.). BVI 발행 법인은 공개 등록부 없어 미확인. 명의개서대리인은 sec.gov 막혀 미확인. 맡김(Alpaca) 출처는 Alpaca 블로그로 회사 발표이나 공시는 아님.
- Securitize: Securitize Markets, LLC(CRD 283256) 확인, 옛 이름 Distributed Technology Markets LLC가 DTM 인수와 부합. EU 거래결제 시스템, 스페인 투자회사, 명의개서대리인은 미확인.
- tZERO: tZERO Securities, LLC(CRD 123421), tZERO Digital Asset Securities, LLC(CRD 316189) 일치. CFTC에서 tZERO DCM(2026-11-10), tZERO DCO(2026-10-16) 일치. Transfer Services는 미확인.
- Alpaca: Alpaca Securities LLC(CRD 288202, 지정 2018-03-26) 일치. 2024 자기 청산 전환은 등록부에 없어 미대조.

## Dinari 관련
- Dinari Securities, LLC: BrokerCheck 일치(CRD 329672, SEC 8-71215). 시점 다름: 맵 서술 2025.6.26 FINRA 등록, 등록부 firmStatusDate 2025-06-20. 우리 DB 값(06-20)과 등록부가 같고 맵이 다름.
- Dinari Inc.(발행, 명의개서대리인): 등록 증권사가 아니라 모회사. SEC 서류 확인 불가로 미확인. BrokerCheck는 Dinari Securities의 직접 소유주를 Dinari Holdings, LLC로 표기하는데 회사 공지는 Dinari Inc.(db/relations.csv에 이미 기록). 이 불일치는 해소하지 못함.
- Alpaca 위탁: 맵 출처는 coinmarketcap(집계)이라 공시 아님. DB는 dinari.com/us/disclosures(회사 공시)에 근거한 Alpaca-Dinari Securities 관계를 가짐.
- tZERO 제휴: 맵 출처는 언론. DB는 dinari.com 블로그 근거로 2026-07-08 가짐(일치).
- 관계 대조: Dinari-Circle, Dinari-Gemini, 카카오페이증권-Dinari, Dinari-tZERO 모두 DB 일치. 맵에 없는 Dinari 관계는 DB에 다수(Broadridge, Flow Traders, Series A 투자자 등).

## 다른 점 목록
1. Dinari Securities 시점 2025.6.26(맵) vs 2025-06-20(등록부, DB)
2. Kraken Securities 시점 2025.4(맵) vs 2024-06-10
3. Robinhood Securities 시점 2018.11 vs 2017-10-13
4. MIAXdx 법인명: 맵 MIAXdx vs CFTC 현재 Rothera Exchange and Clearing LLC(옛 LedgerX). DB의 Rothera -> MIAXdx 인수 관계와 구조 충돌 가능
5. Deribit 금액 29억(맵) vs 42.9억 회계 대가(DB)
6. Bitstamp 금액 2억(맵) vs 2.24억 공정가치(DB)
7. Backed 인수: 맵은 확보, DB는 종결 여부 확인 못함
8. Ondo-Binance, Trust Wallet, Coinbase-Alpaca, BlackRock: 방향이나 시점이 DB와 다름(relations_check.csv)
9. 맵에서 DB에 없는 관계 13건: ICE-OKX, Coinbase-Ondo 투자, Securitize-ICE, 카카오페이증권-Siebert, Alpaca-Binance, Apex-Coinbase, Coinbase Prime-Ondo, 경쟁 2건, Small Exchange, FairX, Securitize-DTM, Pacific Stock Transfer
10. 맵 시점 다수가 인수나 서비스 시작일이고 등록부는 등록일이라 의미가 다름. 일치로 두고 차이 칸에 적음.
11. 맵 출처 중 회사 공시는 Kraken Form CRS 1건뿐. 위탁 행 대부분은 언론이나 집계 출처로 공시 근거가 필요함.

## 범위 밖 발견
- CFTC 목록에 Nasdaq MRX Futures 등 신규 지정, 등록 건이 다수(2026-10~11). 별도 조사 대상일 수 있음.
