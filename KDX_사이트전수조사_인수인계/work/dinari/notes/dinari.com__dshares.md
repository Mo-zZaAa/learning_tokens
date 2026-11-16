# notes: dinari.com/dshares 첫 쪽 (SITE-dinari-1)
경로 기준: raw/는 H/work/dinari/raw/. 종목 표(약 2,900줄)와 변형 쪽(page=1~10)은 읽지 않음(plan 지침).
## 페이지별 사실
### https://dinari.com/dshares
- 구조: dShares는 기초 증권에 1:1로 담보된 토큰. 기초 주식과 ETF는 미국 등록 브로커딜러가 수탁. 회사는 이를 "Dinari가 개척한 수탁 모델이며 SEC가 토큰화 증권 분류에서 같은 모델을 설명한다"고 주장(제3자 확인 필요)
  - 원문: "Dinari pioneered this custodial model, the same model the SEC now describes in its taxonomy of tokenized securities."
  - 위치: raw/dinari.com/dshares.md / The mechanics behind dShares
  - 틀: 핵심 사업 상세 > 발행 구조 > 법적 성격
- 생애주기 5단계: 파트너 플랫폼에서 주문(스테이블코인 또는 피아트 결제는 파트너별), Dinari Securities LLC(SEC 등록, FINRA 회원 브로커딜러)가 수탁 브로커리지 계좌에서 NMS 증권 취득, 검증된 지갑에 1:1 토큰 발행, 배당과 분할 자동 반영, 24/5 통합 마켓플레이스에서 거래 또는 소각으로 직접 환매(기초주식 매도 후 스테이블코인 수령)
  - 원문: "Dinari Securities, LLC, an SEC-registered FINRA-member broker-dealer, acquires the underlying NMS security in a custodial brokerage account."
  - 위치: raw/dinari.com/dshares.md / The lifecycle of a dShare
  - 틀: 핵심 사업 상세 > 발행 구조 > 발행 주체, 거래 구조 > 거래 방식
- 기초자산 보관: Dinari 명의의 수탁 증권계좌에 보유자를 위해 보관, "street name"과 같은 구조라고 설명. 수탁은 Alpaca Securities LLC(CRD 288202, SEC 8-69928). 운영 계좌와 분리된 독립 수탁. 준비금은 Big 4 회계법인이 감사, 스마트컨트랙트는 Hacken 등이 감사
  - 원문: "Custody lives at Alpaca Securities LLC, a FINRA-member broker-dealer (CRD# 288202 / SEC# 8-69928)."
  - 위치: raw/dinari.com/dshares.md / Where the assets sit
  - 틀: 핵심 사업 상세 > 발행 구조 > 기초자산 보관
- 투자자 권리: 현금배당(스테이블코인, 지갑으로 직접), 분할 자동 반영, 직접 환매(기초주식 시장가), 검증된 담보. "경제적 권리는 보유자에게 있다"
  - 위치: raw/dinari.com/dshares.md / What you own
  - 틀: 핵심 사업 상세 > 발행 구조 > 투자자 권리
- 내장 컴플라이언스: 지갑 KYC/KYB 통과 후에만 상호작용, 제한 지역으로의 이전은 코드가 차단, 법이 요구하는 경우 적격투자자 확인을 컨트랙트 수준에서 강제, AML 모니터링
  - 원문: "Hard-coded jurisdictional logic blocks transfers to restricted regions."
  - 위치: raw/dinari.com/dshares.md / Built-in Compliance
  - 틀: 핵심 사업 상세 > 최종 투자자 > 국적 및 지역 제한
- 지역: 미국은 Dinari Securities LLC, 미국 53개 주와 영토에서 영업, CRD 329672 / SEC 8-71215. 국제는 91개 관할에서 현지 규제에 맞춤. 유럽은 MiFID II 하의 유통, 홍콩은 일반 증권으로 취급, 중남미는 디지털 결제 라이선스 하의 유통
  - 원문: "Europe: distributed under MiFID II / Hong Kong: treated as a standard security / Latin America: distributed under digital payments licenses"
  - 위치: raw/dinari.com/dshares.md / Where dShares work
  - 틀: 기업 개요 > 취득 라이선스 및 근거 법령 > 미국, 미국 외 (회사 주장, open-questions 대상)
- 상품군 탭: Stocks, Sector/Asset Class ETF, Strategy ETFs, BDCs, REITs. 종목 표에 일부 종목은 "24/7 trading" 표시(예: AAPL, AMZN)
  - 위치: raw/dinari.com/dshares.md / Explore
  - 틀: 사업 구조 > 상품 기초자산 > 토큰증권
- 구입 경로는 "파트너 플랫폼"(Find a partner) 또는 파트너로서 제공(/business)
  - 위치: raw/dinari.com/dshares.md / Two ways to use dShares
- 조사 질문 관련도: 높음
## 새로 나온 용어
- NMS security, street name, 직접 환매(direct redemption)
## 서로 어긋나는 서술
- Dinari Securities의 SEC 번호: 이 페이지는 SEC# 8-71215, (Alpaca는 8-69928). FINRA CRD 329672는 모든 페이지에서 일치. BrokerCheck 대조 필요
- 거래시간: 이 페이지는 "24/5 통합 마켓플레이스", docs는 4개 세션(24/7 Open 세션 포함)
## 더 봐야 할 것
- /transparency(app.dinari.com/transparency) 준비금 표, 감사 보고서(assets.dinari.com/audits)
- "Big 4" 감사 법인 이름 불명
