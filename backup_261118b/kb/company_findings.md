
# 회사 조사에서 올라온 제도 발견 (proposals 원문 병합, 메인 검토 전)

## EXT-Binance

- ADGM FSMR 별표1 92항: bStocks를 증서(Certificate)로 분류. 한국의 예탁증권(DR)이나 신탁수익증권과 비교할 근거. 출처 https://www.prnewswire.com/apac/news-releases/binance-exchange-launches-bstocks-tokenized-securities-11-backing-and-247-trading-302798969.html
- 미국인 제외 구조: Securities Act of 1933 미등록, ADGM 외 공모 없음, 2차 시장 한정. regulation_us.md의 Reg S 논의와 연결 가능.
- 한국 FIU의 대주주 변경 승인(특금법상 임원 변경 신고) 사례: 고팍스. https://decrypt.co/344719/binance-cleared-acquire-korean-crypto-exchange-gopax

## EXT-Coinbase
- regulation_us.md에 ADGM 사례 보강 제안: Coinbase 토큰화 주식은 ADGM FSRA 승인 투자설명서로 발행한 Certificate over Shares이며 Reg S로 비미국인 한정. 출처 https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf
- cases.md CASE-001(Coinbase 소송 취하)은 이번에도 SEC 원문 미열람. 검색 요약상 "본안 판단 아님, 정책 재정비 이유"로 일치.
- 용어 제안: Vesting Conditions(토큰 이전과 법적 권리의 분리)는 한국 전자등록 계좌부 비교에 유용.

## EXT-Dinari
1. 미국 BD 등록 확인(1차): FINRA BrokerCheck, Dinari Securities LLC, CRD 329672, SEC 8-71215, FINRA 승인 2025-06-20, 공시 0건. https://api.brokercheck.finra.org/search/firm/329672 . kb/regulation_us.md의 "토큰은 기록 수단, 법적 권리는 브로커 계좌" 모델(SITE-dinari-1 제안 1)의 근거로 쓸 수 있음.
2. 법인명 불일치: BrokerCheck 직접 소유주는 Dinari Holdings, LLC, 회사 공지는 Dinari, Inc.(완전 모회사). 지배구조 도식 전에 SEC/EDGAR 확인 필요.
3. 명의개서대리인 등록은 아직 외부 1차 확인 못 함(SEC 차단). 한국 언론도 회사 서술을 따름. 확인 전까지 "회사 주장"으로 표기 권고.
4. 카카오페이증권 제휴는 2026-09-29 MOU, 탐색 단계(상용화 미정, 감독 정책 검토 전제). SITE-dinari-2 제안 6의 날짜 09-30은 09-29로 정정 후보. https://www.etoday.co.kr/news/view/2630410 . 국내 쟁점: 해외투자자 통합계좌(옴니버스)로 원주를 조달해 해외 토큰 발행을 하는 구조가 regulation_kr.md의 해외 유통 쟁점에 해당.
5. 투자 유치: 시드 7.5백만(2023-08) 총 10백만, 시리즈 A 12.7백만(2025-05), 누적 22.65백만. 주도 Hack VC, Blockchange.

## EXT-Kraken
- 용어 xStocks, Tracker, Tokenizer, xPO, TPM을 work/EXT-Kraken/terms.csv에 정리. 근거: https://hanfa.hr/notifikacije/FTWS_971932.pdf , https://www.payward.com/press-release/payward-q3-2026-financial-highlights
- 사례: xStocks는 발행사(Jersey)가 EU 투자설명서 규정에 따라 만기 없는 추적 증권으로 발행하고, 미국과 영국 등은 제외, 기초주식은 스위스 은행과 미국 브로커가 수탁(S10). 한국 비교 때 "발행 법인, 투자설명서, 판매 법인"이 3곳으로 나뉜 구조로 설명 가능.

## EXT-Ondo

- cases.md CASE-008: Decrypt 보도(2025-12-08)는 Ondo 블로그 발표일을 월요일(12-08)로 전함. 기존 "2025-11 말 통지"와 발표일을 구분해 적을 것. https://decrypt.co/351509/ondo-says-biden-era-sec-investigation-closed-no-charges
- 용어 추가 후보: 트래커 인증서, 제한소구, Regulation S (work/EXT-Ondo/terms.csv). 근거 https://www.mfsa.mt/wp-content/uploads/2026/01/Ondo-Global-Markets-BVI-Limited-Final-Terms-Document-dated-11-November-2025.pdf
- 구조 발견: 미국 밖 토큰화 주식은 BVI SPV가 스위스법 채무증권으로 발행하고 미국 브로커(Alpaca)와 수탁(BitGo)이 기초주를 보유. 한국 STO 비교 때 "기초자산 소유권 없는 채권" 쟁점으로 쓸 것.

## EXT-Robinhood

- Robinhood는 같은 이름의 Stock Tokens가 두 세대다. EU판(2025-06, Robinhood Europe UAB 인가 하) 과 Robinhood Chain판(2026-07, 미국 밖 120여 개국, 부채증권). 2026-10-27 실적 발표는 앞의 것을 Classic Stock Tokens로 부른다. 용어집에 구분 필요. 근거: https://finviz.com/news/409270/robinhood-reports-third-quarter-2026-results , https://www.blockmedia.co.kr/archives/1124371
- SEC 3개 부서 직원의 2026-01-28 토큰화 증권 합동 성명(발행사 주도형과 제3자 주도형, 연방 증권법 동일 적용)이 regulation_us.md에 없으면 추가 후보. 근거는 블록미디어 인용이며 SEC 원문은 미열람: https://www.blockmedia.co.kr/archives/1124371

## SITE-dinari-1
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

## SITE-dinari-2
모두 회사 블로그의 서술이다. 원문 확인(SEC 문서, 등록부)은 외부 수집 담당 몫이며 아직 하지 않았다. 근거 파일: KDX_사이트전수조사_인수인계/work/dinari/notes/dinari.com__blog.md, dinari.com__case-studies.md.

1. 미국 토큰화 증권의 "custodial model" 정의
- 회사 서술: SEC가 2026년 1월 토큰화 증권 성명에서 "제3자가 발행사 증권을 보유하고 그 권리를 나타내는 크립토 자산을 발행하는" custodial model을 기술했다고 함. [출처](https://dinari.com/blog/dinari-joins-blockchain-association)
- 제안: kb/regulation_us.md에 "토큰화 증권 3분류(발행사 직접 토큰, 제3자 수탁 토큰, 합성)" 항목을 두고 SEC 성명 원문(2026-01)을 링크와 함께 채운다. 원문 미확인.

2. SEC Innovation Exemption(2026-09, 회사 서술)
- 토큰화 NMS 주식을 다루는 거래장소와 유동성 공급자에 대한 조건부, 한시 완화. 핵심 요건은 기초증권과 "same rights and privileges", SEC 위원장이 "No Synthetics"로 요약했다고 회사가 인용. 거래량, 대상 증권, 참여자 제한과 공개 의견 수렴 중. [출처](https://dinari.com/blog/the-secs-innovation-exemption-advances-the-market-for-tokenized-equities)
- 제안: SEC 원문(발표일, 조건, 의견 수렴 기한)을 laws.csv 후보로 올리고, 한국 비교에서 "합성 금지와 동일 권리 요건"을 쟁점으로 둔다.

3. 미국 사업 법인 구조(회사 서술)
- Dinari Inc.: SEC 등록 명의개서대리인(Exchange Act Section 17A(c), 2022 등록이라 서술), 자기를 "technology company, not a broker-dealer"라 고지. Dinari Securities, LLC: 등록 브로커딜러, FINRA/SIPC 회원, Dinari Inc. 완전 자회사. 청산과 계좌 carry는 Alpaca Securities LLC(비제휴). [출처](https://dinari.com/blog/broadridge-and-dinari-partner-to-bring-proxy-voting-to-dshares) [출처](https://dinari.com/blog/the-secs-innovation-exemption-advances-the-market-for-tokenized-equities)
- 제안: 외부 수집이 EDGAR(명의개서대리인 등록, Form TA-1)와 BrokerCheck(Dinari Securities LLC)로 확인. 틀의 "취득 라이선스 및 근거 법령 > 미국"에 연결.

4. SIPC 비보호 고지
- "dShares are not held by Dinari Securities LLC and are not protected by SIPC." 토큰화 증권도 연방증권법상 증권이라 서술. [출처](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
- 제안: 국내 투자자 보호(예탁, 투자자예탁금 분리) 비교의 쟁점으로 추가. 제도 비교의 "국내 적용 시 결과"는 자본시장법 쪽 확인 후.

5. 허가 없는 환경 이동 시 권리 정지("restricted state")
- 미국 밖 적격 시장에서 dShare가 DeFi로 이동하면 일부 소유권 권리가 정지되고 검증 환경 복귀 시 복원. [출처](https://dinari.com/case-studies/hyperliquid)
- 제안: 권리와 이전 가능성 분리 설계가 규제상 어떤 근거인지(약관, 투자설명서) 확인 필요. 국내 토큰증권 유통 요건과 비교 쟁점 후보.

6. 한국 관련
- 2026-09-30 카카오페이증권과 한국 상장주식 토큰화 해외 유통 탐색 제휴(소싱 틀, PoC, 공동 태스크포스, 단계는 탐색). 한국 내 인가나 한국 투자자 대상 서비스 언급 없음. [출처](https://dinari.com/blog/kakaopay-securities-and-dinari-partner-to-expand-global-access-to-korean-equities)
- 제안: 이 제휴는 "미국 규제 안에서 운영된 토큰화 인프라를 한국 주식에 적용"하는 역방향 사례. 국내 쪽 근거(카카오페이증권 공시 또는 보도, 금융당국 입장)는 외부 수집 필요. kb/regulation_kr.md의 해외 유통 쟁점(해외 투자자 대상 국내 증권 토큰 발행)과 연결.
