# work/PROD/companies.csv "Robinhood Stock Tokens(2026-07)" 줄 수정 제안

기준일 2026-11-16. 근거는 모두 RHJ 투자설명서와 공시 사이트(원문 PDF는 sources/RHJ/, 근거 문장은 work/RHJ/facts.csv). 파일은 직접 고치지 않았다.

## 1. 원주 1대1 보유 여부 (현재 줄: "예" 후 괄호로 엄격한 1대1은 아님)
- 판정: "예"로 두지 말고 "조건부(담보는 기초주 중심이나 현금 등 허용)"로 바꾸는 것을 제안.
- 근거 1(투자설명서): 담보는 (a) 기초자산 (b) 현금 (c) 대여 시 적격 금융상품 (d) 매매 중 이동 자금과 자산 중 하나 이상으로 구성될 수 있다. 같은 문서가 각 시리즈는 "fully collateralised"라고 쓴다. 최소 담보 수준은 상환금액 총액(수량이 아닌 가치 기준)이다. RHJ-012, RHJ-013.
  링크: https://cdn.robinhood.com/assets/robinhood/legal/rhj_base_prospectus.pdf (8쪽 표, 정의 Collateral, 위험요소 Minimum Collateral Level)
- 근거 2(대여): Final Terms에 따라 기초주를 Prime Borrower에게 빌려줄 수 있고, 차입자는 100% 이상 가치의 현금 또는 적격 금융상품을 담보로 제공한다. Apple Final Terms(Series 14)는 대여가 적용된다. RHJ-014, RHJ-015.
  링크: https://cdn.robinhood.com/assets/robinhood/legal/rhj_final_terms_for_tokenised_debt_securities_linked_to_apple.pdf
- 근거 3(회사 FAQ는 더 강한 표현): "Every single Stock Token in circulation is backed 1:1 by the corresponding underlying equity." RHJ-011. FAQ는 마케팅 성격이므로 투자설명서 문구를 우선하고, 두 문구가 다르다는 점을 함께 적는 것을 권한다.
  링크: https://docs.robinhood.com/rhj/faq
- 10-Q 문장(기초증권을 매수해 담보로 보유할 의무)은 현재 줄에 이미 있고, 위 투자설명서 담보 범위와 병기하면 된다.
- 주의: 1:1은 토큰 1개가 기초주 1주 시장가에 연동된다는 뜻(Final Terms "on a 1:1 basis")이기도 하다. 담보 보유의 1:1과 가격 연동의 1:1을 구분해 쓴다. 배당은 승수로 반영되어 토큰당 주식 수가 늘어난다(RHJ-026, RHJ-027).

## 2. 원주 보관처 (현재 줄: "Alpaca Securities LLC(별도 지정이 없는 한)")
- 유지 가능. 보강: Alpaca Securities LLC는 보관기관(Custodian)과 브로커(Broker)를 겸한다(공시 사이트 Service Provider Details). 투자설명서는 "unless otherwise specified in the applicable Final Terms and/or on the Issuer Website"라 적어 변경 가능성을 남긴다. 대여 시 기초주는 Prime Borrower 쪽에 나가 있을 수 있다. RHJ-018, RHJ-019, RHJ-014.
- 링크: https://docs.robinhood.com/rhj/service-providers , 투자설명서 8쪽.
- 추가로 적을 만한 것: 결제 계좌 JPMorgan Chase Bank, N.A. 런던 지점, 담보 대리인 겸 검증 대리인 Security Agent Services AG(스위스), Authorised Participant Bitstamp Global Ltd(RHJ-020, RHJ-022).

## 3. 법적 성격 근거 (현재 줄: 연계증권, 기초 노출 문구)
- 현재 인용문 "The Products are debt securities that provide exposure to the relevant Underlying. ... The Products do not provide ownership over the Underlying or convey any of its attached rights"는 투자설명서 71쪽 부근 FAQ 절에 있는 문장으로 확인됨(RHJ 기본투자설명서 기준). 유지 가능.
- 보강 문구: 스위스 채무법 제973d조 이하의 원장기반증권(Registerwertrechte), 스위스법 적용, 담보부 한정상환청구(secured, limited recourse) 채무, 만기 없음, 무이자, USD 현금 상환(실물 인도 없음). RHJ-008 ~ RHJ-010. 링크: 투자설명서 9쪽, 12쪽, 50쪽, 105쪽.
- 투자자 권리: 기초주 의결권, 참석권, 신주인수권, 이익 분배권 없음. 발행사 자체에 대한 주주 권리도 없음. RHJ-024, RHJ-025.
- 규제 상태: 발행사는 비규제(not regulated). 저지 COBO Consent(JFSC 산하 Companies Registry)만 받음. EU 투자설명서는 리히텐슈타인 FMA 승인. RHJ-003 ~ RHJ-005. 규제 지위를 "저지 인가"로 쓰지 말 것.

## 4. 그 밖에 줄에서 고칠 것
- "판매 안 함" 칸: 공시 사이트 제한 관할은 미국과 미국인, 캐나다, 영국, 스위스(포괄 표현 "including, without limitation")이며 한국은 목록에 없다. 한국 판매 가능으로 읽으면 안 되고 "한국 명시 없음"으로 적는다. RHJ-029 ~ RHJ-032. 웹사이트 이용 조건은 전문투자자 또는 인가 금융기관 제안을 받은 사람.
- 기본투자설명서 날짜: 문서는 2026-06-25자(공시 라이브러리 게시 시각은 2026-09-02). 최신 보충서는 2026-11-09. 현재 줄의 링크 자체는 최신본으로 유효.
- 발행사 식별: 등록번호 162428, LEI 984500ADFHQZ9D6B9A29(RHJ-002). 유럽 Classic Stock Tokens(Robinhood Europe, UAB 파생계약)와는 다른 상품이므로 줄을 섞지 말 것(현재 4번째 줄 구분은 적절).
