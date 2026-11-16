# V3-Robinhood 빈칸 목록 (companies/Robinhood_v3.md)

## 화면과 로고 (줄을 쓰지 않음)
- 로고, 가입, 종목 목록, 주문 캡처 없음. captures/Robinhood/ 폴더가 비어 있고 captures/index.csv의 Robinhood 4건(logo, signup, list, order)이 모두 HTTP 404(Page not found). 맨 위 로고 줄과 회사 개요의 "● 화면" 줄을 뺐음.
- 다시 뜰 곳: robinhood.com/eu/en/stock-tokens/ 대신 현재 EU 주식 토큰 페이지 주소, Robinhood Wallet 앱 화면(지갑판 주문), EU 앱 가입 화면. 브라우저 수집 필요.

## 경영진 발언
- 발언 4(Tenev, 2026-10-27 3분기 실적 보도자료, F-1067) 캡처 파일 없음. captures/quotes/에 Robinhood_01~03만 있음. 이미지 줄을 뺐음.
- 발언 2 원문은 첫 두 문장만 인용(원문 뒤 문장에 긴 줄표가 있어 잘라냄). 전문은 work/QUOTES-B/quotes.csv QUOTES-B-009.

## B 규모(시장 내 위치)
- 1년 전 대비 발행 잔액, 점유율, 순위: 같은 출처(rwa.xyz) 2025-11 기준 값이 db에 없음. 쓰지 않음.
- EU판(Classic Stock Tokens) 발행 잔액: rwa.xyz 표(F-1025)는 지갑판(RHJ)만 잡힘. EU판은 양자 파생계약이라 온체인 잔액 값이 없음. 회사 공시(10-Q)에서 EU판 잔액 수치 필요.
- F-1025(1.49억 달러, 2026-11-16)와 F-0639(공정가치 1.85억 달러, 2026-09-30)는 출처와 기준일이 달라 성과에만 따로 둠.

## D 공급 방식
- 지갑판 DEX 거래처와 출범 파트너 목록(Uniswap, Rialto, Lighter, 1inch, Arcus, Chainlink, BitGo 등) F-0226은 단일 출처라 Uniswap만 F-0227로 씀. 공식 출처 대조 필요.
- 파트너(DEX)를 거쳐 사는 고객의 구성(국가, 개인 여부)은 미공개(work/QUOTES-C/partners.csv).
- 지역 제한에 UAE 포함 여부 F-0229 단일 출처.

## E 인가
- 싱가포르 MAS 자본시장서비스 면허(F-0617), 두바이 DFSA 인가(F-0618, F-0619, F-0238) 단일 출처라 뺐음. 1차 출처(10-Q 또는 감독기관 등록부) 대조 필요.
- 지갑판 판매 주체 Robinhood Non-Custodial Ltd.(케이맨)의 인가나 등록 여부 자료 없음.

## 기본정보와 지배구조
- RHJ 단독 주주 Robinhood International, Inc.와 Robinhood Markets의 지분 관계 원문 미확인(db/relations.csv에도 "지분 관계는 미확인").
- 주요 주주와 비율 자료 없음(F-0600 비고).

## G 한국 접점 (대분류를 뺌)
- 한국 진출 계획 없음 발언, 의결권과 현물 상환 로드맵(F-0240) 단일 출처, 요약문 잘림.
- 한국이 제한 관할과 판매 제한 문구에 없다는 것(F-0883) 단일 출처. 본문에는 교차 가능한 F-0880만 C에 씀.
- 한국 회사와의 협약, 한국 주식 취급 자료 없음(RHJ Series 54 iShares MSCI South Korea ETF 연계 토큰은 work/RHJ/notes.md 메모, facts.csv 미등재).

## 성과
- Robinhood Chain 첫 분기 상위 5위, DEX 거래액 800억 달러, 수수료 5,000만 달러(F-0236, F-0669) 단일 출처라 뺐음.
- Bitstamp 매출, 고객 수(F-0218) 단일 출처.
- Alpaca 토큰화 주식 수탁 점유율(F-1033, F-1034) 단일 출처라 Coopetition 근거에서 뺐음.
