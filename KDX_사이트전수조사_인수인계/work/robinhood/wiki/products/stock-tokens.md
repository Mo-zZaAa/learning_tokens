# Stock Tokens (Robinhood Chain판)와 Classic Stock Tokens (EU판)

확인일 2026-11-16. 회사가 밝힌 내용(공식 사이트와 회사 공시). 제3자 확인이 필요한 주장은 open-questions.md에 올렸다.

## 한눈에
- 두 세대가 있다. Stock Tokens(2026-07 출시, 발행사 RHJ, 부채증권)와 Classic Stock Tokens(2025-06 출시, EEA 고객과의 파생계약). [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 2026-10 실적 문서는 옛 "Robinhood Stock Tokens"를 Classic Stock Tokens로 부른다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)

## 발행 구조 (Stock Tokens)
- 발행 주체: Robinhood Assets (Jersey) Limited(RHJ), 저지에 설립된 비공개 유한회사. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 법적 성격: 토큰화 부채증권. 기초증권에 대한 법적 또는 수익적 권리를 주지 않고 경제적 노출만 준다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 상환 시 기초증권 시장가에서 수수료와 세금을 뺀 현금을 지급할 의무가 있다고 회계 주석에 적었다(주어는 "us"). [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 기초자산 보관: 기초증권을 매수해 담보로 보유해야 한다. 보관기관 이름은 읽은 범위에 없다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 감독: RHJ는 저지에서 일정한 동의(consents)를 받았으나 건전성 감독이나 보증이 아니라고 스스로 밝혔다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 투자설명서: 리히텐슈타인 금융시장감독청(FMA)이 EU 투자설명서 규정에 따라 RHJ의 Tokenised Products Programme 기본투자설명서를 승인했다. 승인은 RHJ나 상품 품질에 대한 보증이 아니라고 함. 승인일은 사이트 원문에 없다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 공시 라이브러리: RHJ Base Prospectus(표시일 2026-09-02), 2026-11-09 보충서, 종목별 Final Terms(약 212줄, 가장 이른 표시일 2026-06-30). [RHJ Disclosure Library](https://robinhood.com/eu/en/legal/rhj)
- 같은 라이브러리에 Robinhood Assets (Jersey) Limited 개인정보 처리방침(2026-06-30)이 있다. [RHJ Disclosure Library](https://robinhood.com/eu/en/legal/rhj)

## 최종 투자자와 지역 제한
- 미국 증권법상 미등록이며 미국, 캐나다, 영국, 스위스 등 여러 관할에서 제한된다("including, without limitation"이라 목록이 전부가 아님). [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 2026 2분기 실적 보도자료: Robinhood Wallet을 통해 120개국 이상의 적격 이용자에게 제공. [2026 2분기 보도자료](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results)
- 2026-07 Wallet 갱신으로 선택된 관할 이용자가 제3자 탈중앙 거래소를 통해 접근한다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- Wallet은 150개국 이상에서 이용 가능하며 케이맨 자회사 Robinhood Non-Custodial Ltd.가 제공한다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 한국 거주자 가능 여부는 사이트에서 확인되지 않는다(open-questions 참고).

## 거래 구조
- 거래 방식: Robinhood Wallet에서 제3자 탈중앙 거래소 경유. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 사용 블록체인: Robinhood Chain(아래 절과 products/robinhood-chain.md). 이 연결을 명시한 문장은 읽은 사이트 원문에서 직접 못 찾았다. 외부 자료(EXT-Robinhood)는 이전 체인을 Arbitrum으로 적는다.
- 거래시간과 유동성 확보 방안: Stock Tokens판은 사이트 원문에서 못 찾음.
- 규모: 2026-09-30 공개 stock token 의무 공정가치 1억 8,500만 달러(Stock Tokens와 Classic 합산 여부 불명). [Form 10-Q](https://investors.robinhood.com/node/16931/html)

## Classic Stock Tokens (EU)
- 투자자와 Robinhood 사이의 파생계약이며 기초증권 가격으로 책정되고 기초증권 권리는 없다. [EU invest](https://robinhood.com/eu/en/invest)
- MiFID II 하에서 파생상품으로 제공된다고 표시(인가 기관 미기재). [EU invest](https://robinhood.com/eu/en/invest)
- 기초자산은 Robinhood가 소유하며 미국 면허 기관에 보관. [EU invest](https://robinhood.com/eu/en/invest)
- 공시상 EEA 일부 관할 적격 고객과의 양자 계약이며 기초증권 보유 의무는 없고 헤지 목적으로 매수. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 거래시간: 월요일 02시부터 토요일 02시(CET/CEST), 장외 주문은 대기. 다른 지갑이나 플랫폼으로 전송 불가. [EU invest](https://robinhood.com/eu/en/invest)
- 배당: 기초증권 배당에 상응하는 금액을 적격 보유자에게 현금 지급(통상 배당 아님). [EU invest](https://robinhood.com/eu/en/invest)
- 수수료: 주문마다 0.1% FX 수수료 외 Robinhood 수수료 없음. 최소 1유로. [EU invest](https://robinhood.com/eu/en/invest)
- 종목 수 2,000개 이상은 회사 홍보 문구. [EU 홈](https://robinhood.com/eu/en)
- 위험: 시장 상황이나 Robinhood 파산으로 원금 전액 손실 가능. [EU invest](https://robinhood.com/eu/en/invest)
- EU 공시 목록: Stock and ETP Tokens KID, 고객 자산 보호 조치 요약, 투자자 보험 제도 정보. [EU 공시 목록](https://robinhood.com/eu/en/about/legal)

## 규제 환경
- 2026-09 SEC 임시 조건부 혁신 면제는 Stock Tokens와 Classic Stock Tokens에 적용되지 않는다. [Form 10-Q](https://investors.robinhood.com/node/16931/html)
- 토큰화 실물자산의 규제 방식은 불확실하다고 위험요인에 공시. [Form 10-Q](https://investors.robinhood.com/node/16931/html)

## 해석
- 같은 이름의 두 상품이 발행 주체(RHJ 대 Robinhood), 성격(부채증권 대 파생계약), 대상 지역(미국 외 다수 대 EEA)이 다르다. 비교할 때 세대를 구분해야 한다.
