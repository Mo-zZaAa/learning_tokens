# STORY-Dinari 노하우 (2026-11-17)

## 통한 경로
- Reuters 기사 원문(reuters.com)은 막히나, 같은 기사를 실은 지역 방송 사이트(whbl.com 등 Reuters 전재)가 curl로 열림. 본문은 HTML 안 기사 블록에서 "By <기자> (Reuters)" 이후를 잘라 읽음.
- 인가 "순서의 이유"는 회사가 말하지 않으면 제도의 처리 기간으로 근거를 세움: 명의개서대리인 등록 효력(17 CFR 240.17Ac2-1, 제출 30일째, eCFR renderer API로 열림)과 FINRA 신규 회원 심사(FINRA Rule 1014, finra.org 규칙 페이지 curl로 열림). 회사 사실(법인 설립일, 승인일)과 나란히 두면 해석 근거가 됨.
- Alpaca 비교: docs.alpaca.markets/docs/about-broker-api(이용 형태 증권사, RIA), alpaca.markets/tokenization(토큰 발행자 아님 고지) 둘 다 curl로 열림.
- Dinari 사이트 전수조사 저장본(KDX_사이트전수조사_인수인계/work/dinari/raw/)에 블로그, 사례 연구, docs가 다 있어 "왜" 문장(B2B 이유, 목표 문장, 파트너 KYC 방식)을 grep으로 찾는 것이 가장 빠름. 자체 앱 존재는 sbt.dinari.com, app.dinari.com 저장본 제목("Dinari Trading App")과 2023 추천 프로그램 글로 확인.

## 막힌 곳
- theblock.co, thedefiant.io, blockworks.co, fortune.com, cryptonews.com, sec.gov(SEC Crypto Task Force의 WilmerHale Dinari 메모 2025-05) 모두 403 또는 허용 밖. WebFetch는 blockworks.co DNS 실패(세션 허용 밖).
- 창업자가 명의개서대리인을 먼저 받은 이유를 직접 말한 원문은 찾지 못함(Fortune 2026-08-04 기사에 관련 발언이 있다는 검색 요약만 있음, 403). 사용자 로컬 브라우저 과제 후보.

## 함정
- 회사가 "자기 고객 화면 없음"처럼 보여도 자체 앱이 있음(2023 자체 웹 앱, 2026 미국판 Dinari Trading App). 축 문장과 어긋나는 사실은 스토리라인에서 "자체 앱과 파트너 판매 비중은 공개 없음"으로 정직하게 적음.
- 사례 연구 거래대금은 파트너마다 집계 기간이 다름(Cadana 2026-01-01~06-15, Meru 2026-01-01~07-15, Hyperliquid 첫 달 기준일 미표시). 합산하지 않음.
- 판매 국가 수는 글마다 다름(60+, 70+, 85+, 91, 92). 시점과 기준을 붙여 나열하고 하나로 고르지 않음.
