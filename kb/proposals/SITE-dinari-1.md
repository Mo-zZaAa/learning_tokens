# SITE-dinari-1 제도 관련 발견 (Dinari 공식 사이트 원문 기준, 회사가 밝힌 내용이며 제3자 확인 전)
기준: H=KDX_사이트전수조사_인수인계, raw 열람 2026-11-16. 상세 notes는 H/work/dinari/notes/.

1. 미국 고객 구조: Dinari Securities, LLC(SEC 등록 브로커딜러, FINRA와 SIPC 회원, CRD 329672)가 고객 계좌를 개설하고, Alpaca Securities LLC(CRD 288202)가 완전공개 방식으로 청산, 증권 수탁을 맡는다. dShare는 계좌 주식의 "2차 기록 토큰"이며 공식 장부는 계좌 기록이 우선한다고 밝힘. 즉 미국에서는 토큰이 아니라 브로커리지 계좌의 주식이 법적 소유. 제안: kb/regulation_us.md에 "토큰은 기록 수단, 법적 권리는 브로커 계좌" 모델을 별도 유형으로 기재. 링크: https://dinari.com/us/disclosures , https://docs.dinari.com/docs/us
2. 비미국 구조: Dinari, Inc.(SEC 등록 명의개서대행, 브로커딜러 아님)가 기초 주식을 자기 명의로 보유하고 투자자에게 토큰을 발행하는 상품이 있으며, Dinari Securities의 상품이 아니고 미국인에게 제공되지 않는다고 밝힘. 85개 이상 관할에서 Regulation S 하에 제공(FAQ). 제안: Reg S 이슈(US-3 쟁점)의 사례로 연결. 링크: https://dinari.com/us/disclosures , https://docs.dinari.com/docs/faqs
3. 사이트가 주장하는 현지 규제: 유럽 MiFID II 하 유통, 홍콩 일반 증권 취급, 중남미 디지털 결제 라이선스 하 유통. 회사 주장이며 근거 인가 불명. 링크: https://dinari.com/dshares
4. 파트너가 BD 라이선스 없이 제공 가능하다는 구조: 파트너는 "소개 플랫폼"에 한정(체결, 추천, 감독 불가, FINRA 3110, 2210 적용), 옴니버스 풀링 금지, 실명 공개, 전용 지갑. 제안: 한국에서 중개와 소개 구분 논의에 참고. 링크: https://docs.dinari.com/docs/us
5. 미국 토큰 이전 제한: docs/us는 미국 고객 토큰이 현재 비양도, DeFi 제한. US 공시는 자기수탁 지갑 이전 가능(등록 지갑)이라고 하여 서로 어긋남. 이전 시 SIPC 보호 상실. 링크: https://docs.dinari.com/docs/us , https://dinari.com/us/disclosures
6. 발행사의 동결, 소각, 재발행 권한과 토큰 단위 컴플라이언스(KYC 게이팅, 지역 제한, 적격투자자 검증)를 계약에 내장: https://dinari.com/bd/dshares-risk , https://dinari.com/dshares
7. 비미국 고객 배당에 30% 원천징수를 Dinari가 브로커 수준에서 징수(2026-03-26 이후 지급분): https://docs.dinari.com/docs/taxes-reporting
8. 스테이블코인 입금은 주 머니트랜스미터법과 연방 MSB 규정 관할이라고 회사가 밝힘, 미국은 USDC만(Circle). 링크: https://docs.dinari.com/docs/us
9. 미국 고객 일 매수 한도 5,000달러, 사모 발행 소매 제공(Form CRS), 비등록 증권은 적격투자자 한정: https://dinari.com/us/disclosures , https://dinari.com/bd/crs

확인 필요(외부): FINRA BrokerCheck의 Dinari Securities LLC, SEC 파일번호(8-71215로 표기)와 등록 이력, Dinari, Inc. Form TA, Alpaca 등록, 회사가 말한 "SEC 분류에 해당 수탁 모델이 기술됨"의 실제 문서.
