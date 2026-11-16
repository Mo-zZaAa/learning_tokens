# 열린 질문

확인일: 2026-11-16. 상태 표기: 해소(외부 자료로 풀림), 부분 해소, 미해결, 충돌. 외부 확인은 work/EXT-Coinbase(facts.csv의 EXT-Coinbase-번호)를 따른다. 이 위키의 사실 줄에는 사이트 근거만 쓰고 외부 확인 내용은 이 문서의 상태 표기에만 적는다. 외부 투자설명서는 NVDAc 하나만 읽었다(EXT-Coinbase 메모).

## A. 충돌
1. 발행 주체. 사이트는 토큰화 주식이 "issued by Coinbase"라고 표기하고(법인명 없음) 같은 사이트가 Base는 발행하지 않는다고 쓴다. [출처](https://base.org/stocks) [출처](https://www.base.org/blog/tokenized-stocks) 상태: 충돌. NVDAc 투자설명서(FSRA 승인, 2026-08-04)의 발행인은 ADGM의 Coinbase Onchain SPV Ltd이고, 이 SPV는 Onchain Marketplace Ltd(OMHL) 100% 자회사, OMHL은 Coinbase Global 100% 자회사라고 한다(EXT-Coinbase-001, 003). 사이트 문구는 그룹 전체를 Coinbase로 줄여 쓴 것으로 보이나 사이트가 그렇게 설명하지는 않는다. 다른 종목의 발행인은 미확인.
2. 투자자 권리. 사이트는 "실제 주식에 대한 수익적 청구권"과 "기초 주식에 대한 직접적이고 선순위인 청구권"을 함께 쓴다. [출처](https://base.org/stocks) 상태: 충돌 후보. 투자설명서는 기초주식 지분에 대한 비례적 수익권을 나타내는 ADGM 증서이고 기초주식 직접 투자가 아니며, 토큰은 운영상 증표, 법적 소유 기록은 Legal Register라고 한다(EXT-Coinbase-004, 005). KYC 등 베스팅 조건을 못 넘은 보유자는 상환할 수 없다(EXT-Coinbase-010). 사이트가 이 조건을 적지 않은 점이 차이다.
3. 배당 처리. 사이트는 배당이 배수 상승으로 반영되고 원천징수세와 수수료를 뺀 뒤 재투자된다고 쓴다. [출처](https://base.org/stocks) 상태: 부분 해소. 투자설명서는 직접 지급 없이 재투자, 매각, Deposit Ratio 조정 등으로 처리한다고 한다(EXT-Coinbase-011). 사이트의 "배수"와 투자설명서의 "Deposit Ratio"가 같은 개념인지는 확인하지 못했다.

## B. 회사가 밝힌 인가, 규모, 순위 (제3자 확인 필요)
4. ADGM FSRA 인가. Coinbase가 ADGM FSRA의 라이선스를 받고 인가되어 있다는 표기. [출처](https://base.org/stocks) 상태: 부분 해소. ADGM 보도자료가 FSRA FSP 취득(투자 거래 주선과 수탁)을 전한다(EXT-Coinbase-020, 단일 출처 성격의 보도자료). FSRA 공개 등록부와 보유 법인(SPV, Tokenisation Entity, 모회사 중 어디)은 미확인.
5. Alpaca 보관과 ADGM 감독. 블로그는 Alpaca의 파산 격리 구조가 ADGM 규제기관 감독을 받는다고 쓴다. [출처](https://www.base.org/blog/tokenized-stocks) 상태: 부분 해소. 투자설명서는 기초주식을 SPV 명의 분리 계좌에 신탁 보관하고 수탁과 중개를 Alpaca가 맡는다고 한다(EXT-Coinbase-006). Alpaca 쪽 인가와 ADGM 감독이 미치는 범위는 미확인.
6. 규모 수치. 24시간 거래량 $131.68M, 전체 공급액 $6.94B, 전체 차입액 $2.54B(2026-11-15 UTC). [출처](https://www.base.org/markets/stocks) 상태: 미해결. 제3자 확인 없음. 전체 공급액과 차입액이 토큰화 주식만의 값인지 Base 렌딩 전체인지 페이지에 정의가 없다. 종목별 온체인 시가총액($7.75M 등)과 규모가 크게 달라 같은 범위의 값으로 보기 어렵다.
7. 종목 수. 사이트 표는 45개 종목(개별 주식 아닌 MAG7 포함), 문서의 Chainlink 피드 목록은 10개이고, 검색 요약은 출시 시 13종목이라고 전한다(EXT-Coinbase-018, 019). [출처](https://www.base.org/markets/stocks) 상태: 부분 해소. 시점 차이로 보이나 현재 종목 수의 1차 목록은 미확인. 문서의 나열과 EXT의 열람일 티커 10개(NVDAc 등)는 일치한다.
8. "다른 상품과 다르다"는 주장(합성, 채권 청구권, 파생 래퍼). [출처](https://base.org/stocks) 상태: 미해결. 홍보 문구이고 대조 대상이 특정되지 않았다.

## C. 사이트 안의 확인 필요 사항
9. 미국 외 "적격 관할"이 어디인지 목록이 읽은 페이지에 없다. 상태: 미해결. 투자설명서는 미국인 제외(Reg S)와 ADGM 밖 배포 불가를 적는다(EXT-Coinbase-009).
10. 1차 발행과 상환은 AP만 가능하다는 표기. [출처](https://base.org/stocks) 상태: 해소. 투자설명서도 신규 창설은 SPV가 승인한 Authorised Participant만 가능하다고 한다(EXT-Coinbase-008). NVDAc만 확인.
11. 24시간 거래와 가격 피드 시간. 사이트는 주말과 공휴일에도 거래된다고 쓰고, 문서는 Chainlink 피드가 24/5이며 주말에는 마지막 종가를 유지한다고 쓴다. [출처](https://base.org/stocks) [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base) 상태: 미해결. 주말 거래가는 어떤 기준으로 정해지는지 설명이 없다.
12. 수수료. 사이트에는 "Coinbase 수수료"라는 말만 있고 율이 없다. 상태: 부분 해소. 투자설명서에 창설 0.01%, 상환 0.05%, 분배금 5.0%가 있다(EXT-Coinbase-012). 사이트 수수료와 같은 항목인지는 미확인.
13. Base 약관 상대방 Coinbase Technologies, Inc.의 설립지와 지분 관계. [출처](https://docs.base.org/terms-of-service) 상태: 미해결. 약관은 준거법 캘리포니아, 불만 접수 주소 뉴욕만 적는다. 이 법인이 토큰화 주식 발행과 무슨 관계인지 사이트에 없다.
14. Base 운영 주체. 약관은 Coinbase가 시퀀서를 운영한다고 하고 홍보 문구는 Base를 "중립적이고 허가 없는 인프라"라고 한다. [출처](https://docs.base.org/terms-of-service) [출처](https://base.org/stocks) 상태: 미해결. 중립성 주장과 단일 운영자 구조의 관계는 설명이 없다.
15. Aave, Morpho와 Base의 "상업적 관계" 내용. [출처](https://www.base.org/markets/stocks/mstrc) 상태: 미해결. 관계의 성격과 금액은 사이트에 없다.
16. 투자설명서 링크는 종목별로 제공되나 이 조사에서는 열지 않았다. 상태: 부분 해소. EXT가 NVDAc만 읽었고 다른 종목이 같은 구조인지 미확인(EXT-Coinbase 메모).

## D. 읽지 않은 범위
- 수집 완료 98쪽 중 메모에 반영된 것은 24쪽(verify 기준 빠진 쪽 0). 나머지 74쪽 중 일부는 Base Markets 개별 종목 페이지, docs SDK의 tokenized-stocks API 참조 10쪽(투자설명서 조회, 컨트랙트 주소, 기업행위 API 등)이다. 이 위키에 반영되지 않았다.
- 인벤토리 648쪽 중 485쪽은 목록만 만들고 읽지 않았다(docs specifications 62, upgrades 44, base-chain 43 등과 brand, chain, status 하위 사이트).
- www.base.org/stocks, /stocksmaxxing, /stocksmaxxing/rules, www.base.org/terms-of-service는 읽기 대상이었으나 수집 파일이 없다. base.org/stocks는 www로 이동하는 주소로 열렸다.
- coinbase.com은 봇 차단으로 범위 밖이다. Coinbase 본사의 인가(미국 주 송금업, BitLicense, FINRA 등)는 이 위키에서 다루지 않았고 EXT 쪽 미확인 목록을 따른다(FINRA BrokerCheck, 뉴욕 BitLicense, NFA 등록부, SEC 원문).
