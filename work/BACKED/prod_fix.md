# work/PROD/companies.csv "Kraken xStocks" 줄 수정 제안 (직접 수정 안 함)
근거는 Backed Assets (JE) Limited 기본 투자설명서 2026-05-08(사용자 제공 PDF, inputs/manual/B01_backed_base_prospectus_20260727_*.pdf, 합본 txt)이고 사실은 work/BACKED/facts.csv의 BACKED-001부터 056에 있다. 쪽은 인쇄 쪽 번호. 2차 보충서 기준 제안은 work/MANUAL/prod_fix.md에 따로 있으니 둘을 함께 반영할 것.

## 한 줄 결론
- 분류 "제3자 합성형(연계증권)" 유지. 근거 링크를 hanfa.hr에서 투자설명서로 교체하거나 병기하고 근거 문장을 아래로 보강.
- 원주 1대1 보유는 "예"를 유지하되 조건 표기 필요(표준 담보 기준, 현금 등 기타 담보와 대여 허용, 상품별 Final Terms).
- 원주 보관처 칸의 Maerki Baumann은 이 투자설명서로 확인되지 않음. 투자설명서가 이름을 대는 곳은 InCore, Alpaca, GTN Europe.
- 투자설명서에는 Kraken이라는 단어가 없음. "자체 고객 화면 여부" 칸은 이 문서로 근거를 못 댐(기존 kraken.com 근거 유지).

## 1. 토큰의 법적 성격 (SEC 직원 성명 분류)
판단: 제3자 합성형(연계증권). 발행사 직접형 아님(발행사 Backed는 기초 주식 발행사와 무관한 제3자), 제3자 보관형 아님, 제3자 합성형(스와프) 아님.

근거 문장(BACKED-010, 011, 012, 016):
- 구조화상품, 채무증서: "The securities issued are structured products (and debt instruments) according to Swiss Law." (p.8). 상품 종류는 "designed as Tracker Certificates"(p.81).
- 보유자 권리는 발행사에 대한 상환금 청구권: "The holder of the Products has a claim against the Issuer for the Redemption Amount in accordance with the formula as set out in the relevant Final Terms" (p.83).
- 기초와 담보에 대한 권리 없음: "The Investors in a Product are not entitled to any rights or claims to the Underlying or the Underlying Components or the Collateral aside from those described in the Terms and Conditions. Physical delivery of the Underlyings and/or Collateral is excluded" (p.83). 주주권 없음: "the Investors' respective creditors' rights do not consist of any shareholders' rights" (p.83).
- 토큰 형식은 스위스 원장기반증권(CO 제973d조 이하)이고 이는 발행사 자신의 증권(채무)을 토큰으로 만든 것: "Ledger-Based Securities according to Art. 973d et seqq. Swiss Code of Obligations" (p.82). 기초 주식의 권리(entitlement)를 옮기는 토큰이 아님.

왜 보관형이 아닌가: 이 팀 정의(work/PROD/notes.md 1절)상 보관형은 토큰이 기초증권에 대한 수익적 이익 또는 권리(entitlement)를 나타내는 경우. 이 상품은 기초 주식이 발행사 명의 계좌에 있고(p.57 "hold in its own name and its own account securities", p.101 담보는 발행사 제공), 투자자에게 있는 것은 상환금 청구권과 그 청구권을 담보하는 질권(담보 대리인 경유)뿐이며 기초와 담보에 대한 별도 권리가 배제됨. 담보가 있어도 보유자 권리는 발행사 채권이라는 연계증권 정의와 맞음.

왜 스와프가 아닌가: 투자설명서에 파생계약이나 스와프 상대방이 없다. 상품은 스위스법상 구조화상품(채무증서)이고 기초주식을 발행사가 실제로 매수해 보유함(p.77-78 발행 과정). 다만 "트래커 증서가 미국법상 security-based swap인지"는 분석하지 않았고 직원 성명 정의도 PROD notes처럼 해설 출처 기준이라 판단의 한계가 있음(확신: 연계증권 쪽이 보관형, 스와프보다 높음).

주의: 토큰 형식(원장기반증권)을 "증권 토큰 자체가 기초 주식의 권리"로 읽으면 보관형 오분류 위험. p.82의 'securities'는 발행사 채무증서를 가리킴.

## 2. 원주 1대1 보유 여부
현재 칸 "예". 유지하되 아래로 보강하고 조건을 비고로 붙일 것.
- 의무 문장(BACKED-021): "The Standard Collateral consists of such number of Underlyings (or Underlying Components in the case of Baskets) corresponding to the number of outstanding Ledger-Based Securities in the Product." (p.101). 담보 가치는 "must correspond to the then current value of the outstanding Products" (p.101).
- 조건 1(BACKED-023, 024): 현금, 상장 장부증권, 가상자산 등 "Other Collateral"이 허용되고 이 경우 초과담보 요구(p.101-102). 어떤 상품이 표준 담보만 쓰는지는 상품별 Final Terms.
- 조건 2(BACKED-022): 발행 옵션2에서 결제 기간(T+2) 중에는 이동 중 현금(법정화폐 또는 스테이블코인)과 인도 청구권도 표준 담보에 포함(p.101-102).
- 조건 3(BACKED-025): Final Terms가 허용하면 기초주식을 Prime Borrower(Alpaca Securities LLC)에 대여할 수 있고, 대여분은 담보에서 빠지고 같은 가치의 현금이 대신 들어감(p.76). 보관기관 InCore는 대여 금지(p.68-69).
- 조건 4(BACKED-020): 고정 액면 상품은 토큰 수를 재계산해 가치를 1:1로 맞춤(p.79-80). 토큰 1개가 주식 1주라는 뜻이 아님.
- 소유 구조: 담보 주식은 발행사 명의 계좌에 있고 투자자를 위한 질권만 설정됨(p.73, 95-96). 투자자 직접 소유 아님.
기존 근거 문장 "The Standard Collateral is the Underlying."은 hanfa.hr 문서 것이므로 유지해도 되나 p.101 문장으로 교체가 더 정확.

## 3. 원주 보관처
현재 칸: Maerki Baumann & Co. AG(취리히), InCore Bank AG(슐리렌), Alpaca Securities LLC(뉴욕).
투자설명서 기준(BACKED-030, 031, 032, 033):
- InCore Bank AG, Schlieren, Zurich: 스위스 보관기관, 브로커, 대금 계좌 제공자(FINMA 인가 은행). p.68, 70, 71.
- Alpaca Crypto LLC, San Mateo, California: 미국 보관기관(FinCEN 등록 MSB). p.68. 2025-03-28 약정 p.69.
- Alpaca Securities LLC, Wilmington, North Carolina: 미국 브로커(SEC 등록 브로커딜러, FINRA 회원)와 증권대여 Prime Borrower. p.70, 76. 현재 칸의 "뉴욕"과 투자설명서의 "노스캐롤라이나 Wilmington"이 다름. 어느 쪽이 맞는지는 판정하지 않음.
- GTN Europe Financial Services Limited, 잉글랜드와 웨일스: 영국 보관기관 겸 브로커(FCA 인가 1003343), 2026-06-30 계약. p.68-70.
- Maerki Baumann: 이 투자설명서 전체에 없음(absent.csv). 현재 칸 근거인 hanfa.hr 문서에서만 확인되므로, 제거하지 말고 "투자설명서 2026-05-08 목록에는 없음" 비고를 붙이길 권장.
- 담보 대리인(보관기관과 별개): Security Agent Services AG, Zug(p.72).
- 상품별 보관기관은 Final Terms가 정하므로 이 목록이 모든 xStock에 적용되는지는 미확인(p.68, 69).

## 4. 판매 제한
미국 투자자 판매 "판매 안 함" 유지. 근거 문장 추가(BACKED-037): "THE PRODUCTS OFFERED UNDER THIS BASE PROSPECTUS ON PRIMARY MARKETS, SECONDARY MARKETS AND OTHER PLATFORMS ARE NOT FOR DISTRIBUTION TO ANY U.S. PERSON OR TO ANY PERSON OR ADDRESS IN THE U.S." (p.6, 128). 링크는 투자설명서 사본 병기.
한국: 투자설명서에 대한민국 언급 없음(absent.csv). 한국 투자자 판매 가능 여부는 이 문서로 판단하지 말 것.

## 5. 발행 주체 칸 보강 정보 (열이 있다면)
- 소재지 저지 유지(BACKED-001, p.55-56). 등록번호 152608, LEI 984500001AB7C6C7F577.
- 지배: Backed Assets (JE) Limited, 주주 Backed Finance AG(Zug), 그 위에 Payward Europe Limited(아일랜드), 그 위에 Payward, Inc.(미국). 2026-01-05경 Payward 계열이 Backed Finance AG를 100% 인수(BACKED-004, 005, p.56-58, 61). "뿌리"가 Kraken(Payward)인 점과 일치. 단 인수 이전(2022년부터) xStocks는 Backed 자체 상품이었음(p.3, 64 공모 이력). 시점 구분 필요.
- 규제 상태(BACKED-006, 007, 008): 금융감독 인가 대상 아님. 저지 JFSC 동의와 AML 등록, 리히텐슈타인 FMA의 투자설명서 승인뿐이고 승인은 증권 품질 보증이 아님. 단일 출처 표기(등록부 미확인).
- 위험 한 줄(BACKED-051, 052, 054): 투자자는 담보에도 불구하고 발행사 신용위험을 부담. Payward는 발행사 채무를 보증하지 않으며 지원 의무도 없음(p.30). 발행사는 Payward 그룹의 기술과 운영 자원에 의존(p.33, 66).

## 6. 관련 fact_id, 검증 상태, 열람 일시
- 관련 fact_id 칸에 BACKED-010, 011, 012, 016, 021, 023, 025, 030, 037 추가(병합 때 F- 번호로 바뀜).
- 검증 상태 1차 출처 확인 유지(투자설명서는 상품 내용의 1차 출처). 인가 보유 주장(FMA 승인, JFSC 동의)을 칸에 쓸 경우에만 단일 출처.
- 열람 일시는 facts.csv의 값을 사용.
