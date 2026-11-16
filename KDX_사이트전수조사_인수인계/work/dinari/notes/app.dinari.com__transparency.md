# notes: app.dinari.com/transparency (첫머리와 표 구조만 확인)
열람 기준: raw 머리 fetched 2026-11-16, method render. 경로 H=KDX_사이트전수조사_인수인계/work/dinari. 같은 내용이 www.dinari.com/transparency(raw/www.dinari.com/transparency.md)에도 있음(50,540자).

## 페이지별 사실

### https://app.dinari.com/transparency
- 페이지 성격: 이름은 Transparency이나 실제 내용은 "Dinari Financial Network" 제목의 종목별 시세표(준비금, 보유 현황 표 아님). 컬럼: Ticker, Last Price, Volume (24 hr)(shares / USD), Bid / Ask, High / Low (24 hr). 행 약 769개(raw에서 센 행 수). 기준일 또는 갱신 시각 표기 없음(렌더 시점 값, fetched 2026-11-16).
  - 원문: "Welcome to Dinari ... Trade real-world stocks as blockchain tokens on Base. Own fractionalized, 1:1 asset-backed dShares, 24/7, globally."
  - 위치: raw/app.dinari.com/transparency.md / 상단 Welcome, 표 머리
  - 틀: 성과 및 경쟁력 > 사업 성과(거래 현황), 핵심 사업 상세 > 거래 구조
  - 숫자면: 24시간 거래량 예 AAPL 0.48주 / $170.45 등 대부분 "빈 값 표시". 거래가 거의 없음. 이 수치를 규모 지표로 쓰지 말 것(렌더 시점 24시간 값).
- 상단 고지: "Total purchases for U.S. customers cannot exceed $5,000 per day", 계정별, 미국 동부 자정 초기화. "Limits may change at any time."
  - 위치: raw/app.dinari.com/transparency.md / 첫 줄
  - 틀: 핵심 사업 상세 > 최종 투자자 > 국적 및 지역 제한 ; 성과 및 경쟁력 > 제약 및 리스크
- 준비금 또는 보유 현황 수치는 이 페이지에 없음.
- 조사 질문 관련도: 중간(미국 일일 매수 한도 $5,000)

### https://usd.dinari.com/transparency (참고, 범위 밖이나 준비금 표라 확인)
- USD+ 담보 표: "USD+ is 100%-backed by short-term US Treasuries." 행: WisdomTree Floating Rate Treasury Fund(USFR) 보유 3행(56.815, 71,318.444, 0.027 USFR; 가치 $2,868.61, $3,600,868.24, $1.38), USDC 3행($3,603.20, $23,385.02, $60.19), USD+ 2행($0.00, $4.98). 표 가치 합계 약 $3.63M(내가 더한 값). 체인 열은 비어 있고 기준일 표기 없음(fetched 2026-11-16).
  - 원문: "USD+ is 100%-backed by short-term US Treasuries."
  - 위치: raw/usd.dinari.com/transparency.md / 표
  - 틀: 성과 및 경쟁력 > 사업 성과(USD+ 규모), 사업 구조 > 상품 기초자산
  - 숫자면: 무엇을 잰 것=USD+ 담보 자산 잔고의 달러 가치, 기준일 미명시
- 조사 질문 관련도: 낮음(USD+는 별도 묶음)

## 새로 나온 용어
- 없음

## 서로 어긋나는 서술
- "100%-backed"라 하나 표의 담보 합계($3.63M)와 USD+ 발행 총량은 이 페이지에 없어 대조 불가.

## 더 봐야 할 것
- dShares 준비금과 보유 현황(vault holdings)은 2023-08-14 글이 "total vault holdings per asset" 공개를 언급. 해당 공개 페이지 위치 확인 필요.
