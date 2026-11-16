# notes: dinari.com/us, /us/disclosures, /bd/* (브로커딜러 공시) (SITE-dinari-1)
경로 기준: raw/는 H/work/dinari/raw/. /bd/terms는 전체 열독하지 않고 절 단위로 grep해 읽음.
## 페이지별 사실
### https://dinari.com/us/disclosures
- Dinari Securities, LLC: SEC 등록 브로커딜러, FINRA와 SIPC 회원, CRD 329672. 자기주도 웹 브로커리지 플랫폼. 적격 미국 고객만 주식 매매. USDC로 입금, 포지션을 dShares로 기록, 자기수탁 지갑으로 이전 가능. 소재지 260 Madison Avenue, Suite 8051, New York
  - 원문: "Dinari Securities provides a self-directed, web-based brokerage platform ... through which eligible U.S. customers may place orders to buy and sell equity stocks."
  - 위치: raw/dinari.com/us__disclosures.md / 1. About Dinari Securities, LLC
  - 틀: 기업 개요 > 취득 라이선스 및 근거 법령 > 미국
- 모자 관계: Dinari Securities는 Dinari, Inc.의 100% 자회사. Dinari, Inc.는 SEC 등록 명의개서대행(transfer agent)이며 dShares 기술을 개발해 Dinari Securities에 라이선스. Dinari, Inc.는 브로커딜러가 아님, 고객 계좌 미보유, 주문 미집행
  - 원문: "Dinari Securities is a wholly owned subsidiary of Dinari, Inc. Dinari, Inc. is registered with the SEC as a transfer agent"
  - 위치: raw/dinari.com/us__disclosures.md / 2. Our relationship with Dinari, Inc.
  - 틀: 기업 개요 > 지배구조 > 모회사, 기업 개요 > 취득 라이선스
- 이해상충 고지: 브로커리지 제공 상품은 계열사 기술을 쓰는 자체 상품(dShares)에 한정, 같은 주식은 다른 브로커에서 토큰 없이 살 수 있음
  - 위치: raw/dinari.com/us__disclosures.md / 2
  - 틀: 성과 및 경쟁력 > 제약 및 리스크
- 비미국 상품: 비미국 유통 파트너를 통해 제공되는 dShares 중 "Dinari, Inc.가 자기 명의로 주식을 보유하고 투자자에게 토큰을 발행하는 상품"은 Dinari, Inc.의 상품이고 Dinari Securities가 제공하지 않으며 미국인은 플랫폼으로 이용 불가
  - 원문: "any product in which Dinari, Inc. holds shares in its own name and issues tokens to investors, describes products of Dinari, Inc. ... not available to U.S. persons through the Platform."
  - 위치: raw/dinari.com/us__disclosures.md / 2
  - 틀: 핵심 사업 상세 > 발행 구조 > 발행 주체, 최종 투자자 > 국적 및 지역 제한 (핵심)
- 법적 성격(미국): 주식은 Alpaca가 보유하는 고객 브로커리지 계좌의 주식. dShare는 "2차 기록 토큰", 별도 투자도 아니고 타인 명의 주식에 대한 청구권도 아님. 블록체인 기록과 계좌 기록이 다르면 계좌 기록이 우선. 배당은 USDC. 분할, 합병, 공개매수, 스핀오프, 상장폐지, 소수주 참여
  - 원문: "A dShare is a secondary recordkeeping token: it reflects the stock position in your account. It is not a separate investment"
  - 위치: raw/dinari.com/us__disclosures.md / 3. What dShares are
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격, 투자자 권리
- 청산과 수탁: Alpaca Securities LLC(CRD 288202, SEC 8-69928)와 완전공개(fully disclosed) 청산 계약. 역할분담: Dinari Securities는 계좌 개설, 신원 확인, 주문 접수, 감독, 플랫폼과 dShares 기록 운영, 민원. Alpaca는 주문 라우팅과 집행, 청산과 결제, 증권과 현금 보관, 배당과 기업행위, 세무서식, 공식 장부. Alpaca는 dShares, 블록체인, USDC 변환에 책임 없음, 마진 미제공
  - 위치: raw/dinari.com/us__disclosures.md / 4. Our Clearing Firm
  - 틀: 사업 구조 > 서비스 범위 > 청산, 결제, 수탁 및 권리 기록
- SIPC: 증권 최대 50만 달러(현금 25만). Alpaca 계좌의 주식은 보호 대상. USDC는 비대상. 자기수탁 지갑이나 제3 플랫폼으로 이전한 dShares는 보호 밖. 블록체인 장애, 컨트랙트 결함, 키 분실은 비보호
  - 위치: raw/dinari.com/us__disclosures.md / 5. SIPC protection and its limits
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리, 성과 및 경쟁력 > 제약 및 리스크
- USDC(Circle 발행, 제휴 아님)로 입금과 매각대금 수령. 제3자 결제 파트너가 환전 스프레드, 발행과 환매 수수료, 네트워크 비용을 부과할 수 있음
  - 위치: raw/dinari.com/us__disclosures.md / 6. Circle and USDC
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래 방식
- 수익원: 거래별 수수료(commission, 거래 명목금액에 따라 변동), 규제, 거래소, 청산 수수료는 Dinari Securities가 부담. 거래가 많을수록 수익이 느는 이해상충을 스스로 고지. 시장데이터는 Massive.com 제공
  - 원문: "Dinari Securities charges a commission on each transaction that varies based on the notional value of the transaction."
  - 위치: raw/dinari.com/us__disclosures.md / 11. Fees and commissions
  - 틀: 사업 구조 > 수익원
- 주문 집행: Alpaca로 보내 라우팅. FINRA Rule 5310 최선집행. SEC Rule 606 보고는 Alpaca 사이트
  - 위치: raw/dinari.com/us__disclosures.md / 12. Order execution and routing
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래 방식
- 이용 한도와 자격: 미국 고객 1일 매수 한도 합계 5,000달러(회사가 변경 가능). 신원 확인과 관할 요건 충족자만 접근
  - 원문: "Purchases by U.S. customers are currently limited to $5,000 per day in total."
  - 위치: raw/dinari.com/us__disclosures.md / 13. Daily limits and eligibility
  - 틀: 핵심 사업 상세 > 최종 투자자 > 대상, 국적 및 지역 제한
- 조사 질문 관련도: 높음
### https://dinari.com/bd/terms (Terms of Service and Customer Agreement, 마지막 갱신 2026-07-21; 전체 1,425줄 중 해당 절만 읽음)
- 이 문서는 Dinari Securities LLC의 일반 브로커리지 약관으로, "dShare", 토큰, 블록체인, 지갑, 수탁 위치에 대한 규정이 없음(grep 결과 해당어 없음). dShares의 법적 성격은 /us/disclosures와 /bd/dshares-risk에 있음
  - 위치: raw/dinari.com/bd__terms.md / 전체 (grep dshare, token, blockchain, wallet 무결과)
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격 (공백 표시)
- 이용 자격: 만 18세 이상, 관련 법 준수. 고객은 "미국 거주자"임을 진술하고 보증, 단독 계좌 소유자, 업무용 아님(개인 비사업용), 증권 전문가 아님, 상장사 임원 또는 10% 주주 아님. KYC로 이름, 미국 주소, 생년월일, SSN 또는 납세자번호, 시민권 수집
  - 원문: "You are a resident of the United States, at least 18 years old when you initially create your Account"
  - 위치: raw/dinari.com/bd__terms.md / 4.2 About You, USA PATRIOT Act 절
  - 틀: 핵심 사업 상세 > 최종 투자자 > 대상, 국적 및 지역 제한
- 제재 지역: OFAC 포괄 제재 관할 또는 Dinari Securities가 위험 기준으로 제한한 관할에서 접속하면 계좌 제한과 주문 취소 가능
  - 위치: raw/dinari.com/bd__terms.md / 제재 관련 절(약 430행)
  - 틀: 핵심 사업 상세 > 최종 투자자 > 국적 및 지역 제한
- 청산 구조: Alpaca 등 청산기관에 계좌를 소개하고 완전공개 방식으로 청산. 규칙 14b-1(c)에 따라 발행사 요청 시 명의 보유 증권의 실소유자 이름과 주소 공개 가능(반대 의사 표시 가능)
  - 위치: raw/dinari.com/bd__terms.md / 1, 2.6, 30. RULE 14B-1(C)
  - 틀: 핵심 사업 상세 > 발행 구조 > 기초자산 보관, 투자자 권리
- 수수료: 수수료표에 있는 수수료, 인상 시 30일 전 통지, 프로모션에 따라 차등 가능
  - 위치: raw/dinari.com/bd__terms.md / 18. FEES AND CHARGES
  - 틀: 사업 구조 > 수익원
- 조사 질문 관련도: 중간
### https://dinari.com/bd/crs (Form CRS, 2026-07-20 발효)
- 주 사업은 소매 고객에게 웹 기반 주식 매매 플랫폼 제공, 사모 발행(private placement)도 소매 고객에게 제공. 투자 조언 없음, 계좌 모니터링 없음, 국내 계좌 최소금액 없음. 거래 수수료 부과, 규제와 청산 비용은 회사 부담. 징계 이력 없음이라고 밝힘. 마진 이자의 일부를 받는 이해상충을 예로 듦
  - 원문: "Dinari also offers private placements to retail customers."
  - 위치: raw/dinari.com/bd__crs.md / 2. What investment services, 3. What fees
  - 틀: 사업 구조 > 수익원, 기업 개요 > 취득 라이선스 및 근거 법령 > 미국
- CRS는 "독점 상품(proprietary products)을 판매하지 않는다"고 쓰나, 공시와 위험고지는 dShares를 독점 상품으로 인정(서로 어긋나는 서술)
  - 원문: "We do not offer for sale or purchase proprietary products."
  - 위치: raw/dinari.com/bd__crs.md / 2
- 조사 질문 관련도: 중간
### https://dinari.com/bd/dshares-risk
- 두 겹의 위험: 일반 투자 위험과 블록체인 기록 위험이 더해짐. 공식 기록은 계좌 명세와 거래확인서, 온체인 잔고가 다르면 계좌 기록이 우선, 정합이 지연될 수 있음
  - 위치: raw/dinari.com/bd__dshares-risk.md / 2. What you own, and the two records of it
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격
- 이전 통제: Dinari는 컴플라이언스, 기업행위, 오류 시정을 위해 dShares를 동결, 차단, 되돌림, 소각, 재발행할 수 있는 권리와 능력을 보유. 여러 블록체인 발행 가능. 자기수탁 지갑 이전은 신원 확인된 비제한 지역 지갑만 가능
  - 원문: "Dinari reserves the right and ability to freeze, block, reverse, burn or reissues dShares"
  - 위치: raw/dinari.com/bd__dshares-risk.md / 3. Risks of the blockchain record, 4. Transferring dShares
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리, 성과 및 경쟁력 > 제약 및 리스크
- 권리: 배당은 지급일로부터 영업일 2일 내 USDC로 지갑에 입금. 기업행위(분할, 병합, 합병, 공개매수, 교환, 스핀오프, 유상증자, 주식배당, 상장폐지) 반영, 의결권 서류는 등록 이메일로 전달. 소수주는 선택 종목만(Alpaca 소수주 상품에 의존), 중단 시 공정가치로 청산해 스테이블코인으로 지급
  - 위치: raw/dinari.com/bd__dshares-risk.md / 5. Rights associated with your position
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리
- 기술 의존: 기술은 모회사 Dinari, Inc.가 개발, 라이선스. 규제 불확실성(토큰화 증권과 스테이블코인 규제는 변할 수 있음). 플랫폼 장애 시 대체 주문 수단 없음, 매수 일 한도 5,000달러
  - 위치: raw/dinari.com/bd__dshares-risk.md / 6, 9, 11
  - 틀: 성과 및 경쟁력 > 제약 및 리스크
- 조사 질문 관련도: 높음
### https://dinari.com/bd/extended-hours
- 거래 세션: 정규 9:30-16:00 ET, 프리마켓 4:00-9:30, 애프터아워 16:00-20:00. 그 밖 시간 주문은 대기 또는 거부(원문 "queued ... / will be rejected" 두 표현이 병기됨), 주말과 휴장일은 불가. 거래 정지 종목은 주문 불수리. FINRA Rule 2265 공시
  - 원문: "Trading is not available on weekends and market holidays."
  - 위치: raw/dinari.com/bd__extended-hours.md / When you can trade
  - 틀: 핵심 사업 상세 > 거래 구조 > 거래시간 (미국 고객 BD 경로 기준, docs의 24/7 세션과 다름)
- 조사 질문 관련도: 높음
### https://dinari.com/bd/etp
- ETP(ETF, ETN) 일반 위험 고지: 시장가와 NAV 괴리, 연말 분배, ETN 발행사 신용위험, 레버리지와 인버스 상품 위험
- 조사 질문 관련도: 낮음 (표준 고지)
### https://dinari.com/us
- (home 묶음 notes 참조: dinari.com__home-business-usdplus-getstarted.md)
## 새로 나온 용어
- 완전공개 청산(fully disclosed clearing), 2차 기록 토큰(secondary recordkeeping token), Rule 14b-1(c), 소수주(fractional position), Form CRS
## 서로 어긋나는 서술
- CRS "독점 상품 미제공" vs 공시 "dShares는 독점 상품"
- /bd/extended-hours는 주말 거래 불가, docs의 Open(24/7) 세션은 금요일 20시부터 일요일 20시 블록체인 전용 거래. 미국 고객은 BD 경로이므로 24/7 세션이 적용되는지 불명(미국 고객 토큰은 현재 비양도 및 DeFi 제한)
- 미국 고객 이전 가능 여부: US 공시와 위험고지는 자기수탁 지갑 이전 가능, docs/us는 "발행 토큰은 현재 비양도, DeFi 사용 제한"
## 더 봐야 할 것
- FINRA BrokerCheck의 Dinari Securities LLC(CRD 329672) 등록일과 SEC 파일번호(8-71215로 dshares 페이지 표기), Dinari, Inc.의 SEC 명의개서대행 등록(Form TA)
- /bd/brokerage-agreement, /bd/business-continuity, /bd/privacy, /bd/market-data-terms (정독 범위 밖)
- Alpaca Securities LLC 수탁 모델, Alpaca 소수주 한계
- handover 후보: Securitize, tZERO 언급 없음
