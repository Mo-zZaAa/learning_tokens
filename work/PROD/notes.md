# 분류 정의 원문 확인 (2026-11-16 추가)
- SEC 직원 성명 원문(Statement on Tokenized Securities, 2026-01-28, Corporation Finance, Investment Management, Trading and Markets 공동)을 사용자가 준 PDF로 확인함: inputs/manual/B17_sec_staff_statement_tokenized_securities_20260128.pdf(OCR 텍스트 .txt).
- 정의: 발행사 직접(issuer-sponsored), 제3자 보관형(custodial: 기초 증권을 보관하고 토큰이 보관 증권에 대한 소유 지분을 나타냄), 제3자 합성형(synthetic: 제3자 자신의 증권으로 합성 노출. 연계증권 또는 증권기반 스와프).
- 이 정의로 8개 상품 분류를 다시 대조한 결과 바꿀 것 없음. 아래 로펌 해설 기반 정의는 길잡이로만 남김.

# PROD 메모 (기준일 2026-11-16, 열람 2026-11-16T12:30Z)

## 1. 토큰 법적 성격 분류 정의와 출처 (맨 위)
SEC 직원 성명(2026-01-28, Statement on Tokenized Securities) 원문은 sec.gov라 셸에서 403이어서 열지 못했다. 성명을 인용한 아래 두 출처의 문장으로 정의를 잡았다.

- 출처 A (Federal Register, 91 FR 60168, SEC 명령, govinfo 전재, https://www.govinfo.gov/content/pkg/FR-2026-09-22/html/2026-19388.htm, 로컬 사본 sources/US-1/tokenNMS.txt 25~67행): 토큰화 주식은 "(1) a security tokenized by, or on behalf of, the issuer of the underlying NMS stock; or (2) a security tokenized by a third party that is unaffiliated with the issuer of the underlying NMS stock." 그리고 "does not include securities where a third party issues a crypto asset representing its own security that provides synthetic exposure to an underlying security, such as a tokenized linked security or a tokenized security-based swap." 각주 3과 4가 성명의 각주 5, 11, 13-16을 가리킨다.
- 출처 B (Cleary Gottlieb 해설, https://www.clearygottlieb.com/news-and-insights/publication-listing/sec-staff-issues-guidance-on-tokenized-security-taxonomies): "The Divisions identified two types of models for third party securities tokenization: (1) Custodial Tokenized Securities; and (2) Synthetic Tokenized Securities." / "A 'linked security' is a security issued by the third party itself that provides synthetic exposure to a referenced security, but it is not an obligation of the issuer of the referenced security and confers no rights or benefits from the issuer of the referenced security." / 연계증권은 "a debt security (such as a structured note) or an equity security ... or a security that is a security based swap". 보관형: "a crypto asset issued by a third party representing the underlying security of a third party, such as a tokenized security entitlement."
- 출처 C (Dechert 해설, https://www.dechert.com/knowledge/onpoint/2026/2/sec-staff-maps-tokenization-models--tokenized-securities-are-sti.html): "In the custodial model, a third-party creates a crypto asset that operates as a 'tokenized security entitlement' by conveying an indirect interest in an underlying security legally owned by the third party." / "In the synthetic model, a third-party may issue a tokenized 'linked security' that provides synthetic exposure to an underlying security issued by an unaffiliated entity."

이 과제의 4분류 적용 기준
- 발행사 직접: 기초 주식의 발행사가 또는 발행사를 대신해 토큰화. 이번 대상 8개 상품 중 해당 없음(모두 기초 발행사와 무관한 제3자).
- 제3자 보관형: 제3자가 기초증권을 보관하고, 토큰이 그 증권에 대한 수익적 이익 또는 증권 권리(entitlement)를 나타냄.
- 제3자 합성형(연계증권): 제3자 자기 채무 또는 증권(부채증권, 트래커 증서)이고 보유자는 기초증권에 권리가 없음. 담보가 있어도 보유자 권리는 발행사에 대한 채권.
- 제3자 합성형(스와프): 제3자와의 파생계약(스와프성 계약)을 토큰으로 표시.
주의: 성명 원문의 정의 문장은 직접 못 봤고 출처 A, B, C가 요약한 것이다. 직원 성명은 법적 효력이 없다(출처 A 각주 2).

## 2. 상품별 분류 판단 메모
- Kraken xStocks: Backed Assets (JE) Limited가 내는 만기 없는 Tracker Certificates, 스위스법상 부채증서(debt instruments). 보유자는 채권자 권리만 있고 기초자산, 담보에 대한 권리 없음. 담보는 기초주식(Standard Collateral is the Underlying)이지만 보유자 청구권은 발행사에 대한 것이라 연계증권으로 분류.
- Ondo Global Markets: Final Terms "Product Security Type: Debt instrument", 기초자산 인도 청구권 없음, 담보부 제한소구 채무. 연계증권.
- Robinhood Stock Tokens(RHJ): Base Prospectus가 "debt securities that provide exposure to the relevant Underlying", 기초 소유권과 권리 없음. 연계증권.
- Robinhood Classic Stock Tokens: 약관 Schedule E가 "financial derivative contracts between you and Robinhood", MiFID II 파생상품. 스와프로 분류했으나 미국법상 security-based swap 해당 여부 분석은 안 했다(판단, 낮은 확신). 계약 상대방은 약관상 Robinhood Europe, UAB, 10-Q 공시는 주어를 Robinhood로 적어 불일치로 남김.
- Binance bStocks와 Coinbase 토큰: ADGM FSMR 별표1 92항 증서로 "1:1 또는 pro rata beneficial interest in the Underlying held in custody"이고 기초주식이 발행사 명의 분리계좌에 보관, 보관형. 단 ADGM 증서가 미국법상 증권 권리(entitlement)와 같은지는 별개 문제.
- Dinari 미국판: 고객이 Alpaca가 청산 보관하는 자기 중개계좌의 주식을 소유하고 토큰은 2차 기록. 보관형. 이 구조에선 토큰 자체가 증권이 아니라는 서술이어서 SEC의 보관형 정의(권리 이전 기록)에 가장 가깝다.
- Dinari 미국 밖판: 약관(Terms and Conditions for the Dinari Tokens)은 "you will not have any claim of right or title to the actual Underlying Asset, you do have a claim to the value", 기초자산은 Dinari 명의 계좌에 별도 보관. 보유자는 기초자산 권리가 없고 Dinari에 가치 청구권만 있으므로 연계증권으로 분류. 그러나 Dinari 사이트는 "custodial model", 비즈니스 페이지는 "Tokenholders hold a direct claim on the backing security", 사이트 FAQ는 "you receive a separate security"라고 해 서술이 갈린다. 판단 보류성 분류이므로 검토 필요.

## 3. 원주 1대1 보유와 기타 칸 단서
- Robinhood Stock Tokens: 칸은 예로 두었으나 근거는 Form 10-Q 문장이다. Base Prospectus는 담보(Collateral)가 기초증권, 현금, 대여 시 적격 금융상품, 이동 중 자금의 어느 것일 수 있다고 적고(2쪽 요약 Collateral 항목) 엄격한 1대1 보유 의무는 보이지 않는다. 약관, 투자설명서만으로는 확인 안 됨에 가깝다. Final Terms(종목별)는 열지 않았다.
- Ondo: 담보에는 기초주식과 현금이 함께 포함될 수 있고 발행 직후 결제 대기 구간은 USD로 일부 담보된다고 Final Terms가 적는다. 예로 두되 단서.
- Dinari 미국 밖판: 약관 3.7이 기초자산을 Dinari 명의 계좌에 취득한다고 적어 예. 단 보유자는 기초자산 청구권이 없음.

## 4. 칸별 근거 문장 중 CSV 머리줄에 칸이 없어 여기 둔 것
머리줄에 미국 판매 근거 문장, 고객 화면 근거 문장 칸이 없어 아래에 적는다.
- Kraken xStocks
  - 미국 판매 근거 문장: The Products offered on primary and secondary markets and other platforms under this Base Prospectus are not for distribution to any U.S. person or any person or address in the U.S.
  - 고객 화면 근거 문장: Access and trade xStocks directly in the Kraken app.
- Robinhood Stock Tokens(2026-07)
  - 미국 판매 근거 문장: may not be offered, sold or delivered within the United States to, or for the account or benefit of U.S. Persons
  - 고객 화면 근거 문장: we updated the Robinhood Wallet in July 2026 to allow eligible users in selected jurisdictions to access Stock Tokens and decentralized perpetual futures via a third-party decentralized exchange (거래 자체는 제3자 탈중앙 거래소)
- Robinhood Classic Stock Tokens(EU, 2025-06)
  - 미국 판매 근거 문장: Classic Stock Tokens, launched in June 2025, are bilateral contracts with eligible customers in certain EEA jurisdictions.
  - 고객 화면 근거 문장: Classic Stock Tokens are derivative contracts between you and Robinhood.
  - 원주 보관처 근거 문장: The underlying assets of Classic Stock Tokens are owned by Robinhood and held with a US-licensed institution.
- Binance bStocks
  - 미국 판매 근거 문장: may not be offered, sold or otherwise transferred (i) within the United States or (ii) to, or for the account or benefit of, any U.S. Person
  - 고객 화면 근거 문장: subscribing for the Certificates ... on the Binance Platform (Redemption Order: Investor on the Binance Platform to the Redemption Agent)
- Coinbase Base 주식 토큰(예: NVDAc)
  - 미국 판매 근거 문장: may be offered, sold, or otherwise delivered at any time only to transferees that are Non-U.S. Persons
  - 고객 화면 근거 문장: 신규 증권 창설은 Authorised Participant만 가능(F-0083). Coinbase 앱 직접 판매 문장은 못 찾음
- Dinari dShares 미국판
  - 미국 판매 근거 문장: Dinari Securities provides a self-directed, web-based brokerage platform through which eligible U.S. customers may place orders to buy and sell equity stocks.
  - 고객 화면 근거 문장: Dinari Securities provides a self-directed, web-based brokerage platform
- Dinari dShares 미국 밖판
  - 미국 판매 근거 문장: You certify that you, and any other holder of Tokens due to a Distribution by you, are not a U.S. Person
  - 고객 화면 근거 문장: dShares products offered outside the United States through non-U.S. distribution partners, including any product in which Dinari, Inc. holds shares in its own name and issues tokens to investors, describes products of Dinari, Inc.
- Ondo Global Markets(Ondo Stocks)
  - 미국 판매 근거 문장: b. (i) who are not in the United States, who do not originate any buy orders in the United States, who are not U.S. persons
  - 고객 화면 근거 문장: Onboarding to the Ondo Stocks platform is open to institutional participants and retail users/individuals in supported jurisdictions.

## 5. 못 채운 것과 찾아본 곳
- Binance bStocks 발행 주체 BTech Holdings Limited의 소재지: 투자설명서에서 ADGM 등록 법인으로 읽히나 소재지를 직접 적은 문장은 이번에 확정하지 않았다(Moderna 투자설명서 1~110행 훑음). 칸은 ADGM으로 적고 단서를 붙였다.
- Dinari Securities, Dinari, Inc. 소재지: 미국으로만 적었다. 이번에 연 문서(us/disclosures, 약관)에 도시, 주 표기를 확인하지 못함.
- Coinbase 앱에서의 직접 판매: Coinbase 투자설명서와 base.org 자료에서 소매 앱 판매 문장을 못 찾아 아니오로 두었다(근거는 신규 창설이 Authorised Participant로 제한). 2차 시장은 허가 없이 거래 가능.
- Coinbase 투자설명서는 로컬 사본 sources/EXT-Coinbase/NVDAc.txt로 문장을 확인했다(링크 api.coinbase.com은 셸 재열람 안 함).
- Robinhood 10-Q(investors.robinhood.com/node/16931/html)는 셸 curl이 403이라 재열람 못 하고 KDX 수집본 raw(KDX_사이트전수조사_인수인계/work/robinhood/raw/investors.robinhood.com/node__16931__html.md)와 db/facts.csv F-0630 이하의 문장을 썼다. blocked_links.csv에 기록.
- 성명 원문(sec.gov)은 못 열었다. blocked_links.csv에 기록.
- Robinhood 종목별 Final Terms, Classic Stock Tokens의 KID(PRIIPs)는 열지 않았다.
- 대표 종목 하나의 투자설명서로 상품 전체를 대표시켰다(Binance는 Moderna bStocks 2026-09-01판, Coinbase는 NVDAc, Ondo는 QQQon 제품 1호 Final Terms, Kraken은 2026-05-08 Base Prospectus 최종조건 사본). 종목마다 문구가 다를 수 있다.
- 범위 밖 발견: Robinhood Stock Tokens 투자설명서는 스위스법상 원장증권(Registerwertrechte)이고 Base Prospectus 표지일이 2026-06-25(공시 라이브러리는 2026-09-02, 2026-11-09 보충서 표시)로 판이 여러 개다.
- 추가 상품 후보(이번에는 근거 확인 안 해 넣지 않음): Kraken의 미국 주식 거래(Kraken Securities LLC, 토큰 아님), Binance가 Ondo 토큰을 제공하는 건(PYMNTS 2026-02-24).
