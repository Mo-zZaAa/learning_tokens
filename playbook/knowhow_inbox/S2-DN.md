# S2-DN 리서치 노하우 (Dinari 개요, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| sec.gov(403), efts.sec.gov 전문 검색(403) | FINRA BrokerCheck 상세 보고서 PDF(files.brokercheck.finra.org/firm/firm_<CRD>.pdf, curl로 열림) | API 요약(api.brokercheck.finra.org)에는 직접 소유주만 있고, PDF에는 간접 소유주, 사업 종류, 청산 소개 계약과 효력일, 주별 승인일이 다 있음. Dinari Holdings 대 Dinari, Inc. 충돌이 여기서 풀림 |
| broadridge.com 일부 주소(404), sec.gov 10-K | broadridge.com/capability/governance-and-regulatory-compliance/proxy-services/ 와 /about/ (curl로 열림) | 회사 역할 한 줄과 규모(매출 60억 달러) |
| usd.dinari.com/transparency(자바스크립트 화면) | 없음. 준비금 크기는 쓰지 않음 | |

## 쓸모 있었던 1차 출처 위치
- Dinari 미국 밖판 약관 PDF(dinari.com/terms에서 링크, 2025-12-26 개정): 발행 주체(Dinari, Inc.), 보유자 권리 4.5(a)(b), 되사기 6장과 6.8(계약상 되팔 권리, 소유권 없음), 버뮤다 분리계정회사 3.7과 Annex 5, 의결권 없음 4.5(d), 배당 공제 4.5(c), 현지 승인 책임 7.1(o)와 Annex 4, 판매 제외 지역 Annex 1, USD+ 관리 보수 3.8(c)
- 판매사 쪽 고지문: Gemini 블로그 끝 고지에 EU 판매 법인의 인가(몰타 MFSA, MiFID 서비스)와 상품 성격("디지털 파생상품")이 나옴. 발행사 화면에 없는 현지 인가는 판매사 고지에서 찾는다
- Hyperliquid 공식 API(api.hyperliquid.xyz/info): spotMeta의 deployerTradingFeeShare, tokenDetails의 deployer와 deployTime, spotMetaAndAssetCtxs의 coin "@<번호>"별 24시간 거래 금액. 컨텍스트 목록 순서는 universe 순서와 다르므로 coin 칸으로 맞춘다
- DefiLlama(api.llama.fi/summary/dexs/<이름>, summary/fees/<이름>): methodology 칸에 무엇을 셌는지(주문 금액인지 2차 거래인지)가 적혀 있음. Dinari는 "dShare 주문 금액"이라 발행과 되사기 규모이고 2차 거래가 아님. chains 칸으로 빠진 체인을 확인
- dinari.com/sitemap.xml: 블로그 전체 목록으로 투자 유치 글이 몇 건인지 셀 수 있음(공개 범위 근거)

## 함정
- "파트너 앱에서 사고팖"은 2차 거래가 아님. Dinari는 주문마다 기초 주식을 사고팔며 토큰을 찍고 태움. 보유자끼리의 2차 거래는 HyperCore, Camelot처럼 남의 시설에서만 일어남
- 회사 요금 문서(파트너, 거래 수수료 없음)와 FAQ(발행 주문 0.25%에서 0.50%)가 같은 주에 갱신됐는데 서로 다름. 하나로 고르지 않고 둘 다 씀
- Gemini 고지문의 "offered for purchase and sale directly from Dinari"는 Gemini가 사서 되파는 것이 아니라 고객이 Gemini 플랫폼에서 Dinari로부터 직접 사는 구조임
- dShares 종목 목록은 자바스크립트로 그려져 curl 저장본에는 없음. 렌더링 저장본(사이트 전수조사 raw)에서 찾음(SK hynix 예탁증서 SKHY)
