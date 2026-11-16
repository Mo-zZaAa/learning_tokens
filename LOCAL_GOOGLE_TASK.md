# Chrome 탐방 지시: 구글 검색으로 남은 빈칸 채우기

너는 사용자 컴퓨터의 Chrome에서 도는 Claude다. 클라우드 쪽 리서치는 사이트 차단과 엄격한 출처 규칙 때문에 아래 빈칸을 채우지 못했다. 사람이 구글로 찾는 방식대로 탐방해서 채운다.

## 방법
1. google.com에서 검색한다(아래 각 항목의 "검색어" 그대로 시작, 필요하면 바꿔도 됨). 한국어로 물어도 된다.
2. 구글 AI 요약(AI 개요)이 나오면 읽고, 요약 옆이나 아래의 출처 링크를 눌러 원문으로 들어간다. AI 요약 문장 자체는 근거로 쓰지 않는다. 원문 페이지에서 그 내용이 실제로 있는 문장을 찾는다.
3. 출처 우선순위: 회사 공식(블로그, 보도자료, IR, 약관) > 감독기관, 공시 > 주요 매체(로이터, 블룸버그, 코인데스크, The Block, 국내 경제지 등) > 위키백과(각주를 타고 원문으로). 공식 원문을 못 찾으면 주요 매체 1곳이면 된다(어느 매체인지 표에 적는다).
4. 원문에서 근거 문장이 보이게 캡처한다(파일 이름: <회사>_<짧은이름>.png, 폭 1200px 이하).
5. 미시적인 정확성(정확한 일자, 쪽 번호)보다 "왜, 무엇을 위해, 그래서 어떻게 됐나"를 찾는 데 시간을 쓴다.
6. 로그인, 결제, 개인정보 화면은 건너뛴다. 캡차가 나오면 사용자에게 한 번 풀어 달라고 한다. 대량으로 긁지 않는다.

## 결과 형식(채팅으로)
항목마다 한 줄씩 표로:
| # | 항목 | 찾은 내용(쉬운 한국어 2~3문장) | 출처 종류(회사 공식, 감독기관, 매체명, 위키백과) | 링크 | 원문 근거 문장(원문 언어 그대로 1~2문장) | 날짜 | 캡처 파일 |
못 찾은 항목은 "못 찾음"과 검색어, 열어 본 곳 한 줄. 끝나면 캡처를 한 zip으로 묶어 사용자에게 준다.

## 찾을 것 (우선순위 순)

### A. 큰 그림: 전략, 비전, 인수 이유 (가장 중요)
1. Kraken(Payward): Payward가 Kraken의 지주회사가 된 시점과 이유, 2021년 이후 법인 구조 개편. 검색어: "Payward Kraken holding company restructure"
2. Kraken: 왜 선물부터 샀나(Crypto Facilities 2019, NinjaTrader 2025)에 대한 CEO, 회사 설명. 검색어: "Kraken why acquire NinjaTrader futures strategy Sethi"
3. Kraken: 버뮤다, 아일랜드, 키프로스 법인을 고른 이유, 각 법인이 하는 일. 검색어: "Kraken Bermuda license xStocks why Bermuda", "Kraken Cyprus MiFID license derivatives Europe"
4. Kraken: Backed를 원래 누가 세웠고 누가 투자했나(Backed Finance AG, 스위스), 인수 전 주식 토큰 시장 위치. 검색어: "Backed Finance founders investors seed round"
5. Kraken: Embed, Payward Services 이용 기업 목록과 수. 검색어: "Kraken Embed partners bunq banks list", "Payward Services clients"
6. Coinbase: 2021-04-14 Nasdaq 직상장 첫날(시초가, 시가총액). 검색어: "Coinbase direct listing April 14 2021 opening price market cap"
7. Coinbase: 예측시장 출시(Kalshi 제휴) 공식 발표, Coinbase Prime과 Custody 출시 시점. 검색어: "Coinbase prediction markets Kalshi launch announcement", "Coinbase Prime launch 2018"
8. Coinbase: Deribit 인수 금액(29억 달러)과 이유. 검색어: "Coinbase Deribit acquisition $2.9 billion why"
9. Coinbase: 월간 거래 이용자(MTU) 최근 값(10-K, 실적 발표). 검색어: "Coinbase monthly transacting users 2025 10-K"
10. Robinhood: 2021-07-29 Nasdaq IPO(공모가, 조달액, 첫날 주가). 검색어: "Robinhood IPO July 29 2021 price raised"
11. Robinhood: TradePMR, WonderFi, MIAXdx 인수 이유(회사 발표). 검색어: "Robinhood acquire TradePMR why", "Robinhood WonderFi acquisition Canada reason", "Robinhood Susquehanna MIAXdx joint venture why"
12. Robinhood: EU 비상장 회사 토큰(OpenAI, SpaceX) 이후 변화(중단, 확대, 리투아니아 중앙은행 결론). 검색어: "Robinhood OpenAI token Bank of Lithuania outcome"
13. Robinhood: Robinhood Ventures Fund I 규모, 수수료, 보유 종목. 검색어: "Robinhood Ventures Fund I RVI fees holdings size"
14. Binance: 연간 이용자, 거래대금, 매출(회사 연례 보고, 매체 추정). 검색어: "Binance 2025 annual report users trading volume revenue"
15. Binance: MGX 20억 달러 투자(2025-03)와 아부다비 거점을 고른 이유. 검색어: "MGX Binance $2 billion investment Abu Dhabi why"
16. Binance: 고팍스 인수 지분율과 금액. 검색어: "바이낸스 고팍스 지분율 인수 금액"
17. Ondo: 고객 수(보유자 수), 매출, 전체 TVL 최근 값. 검색어: "Ondo Finance holders number TVL 2026"
18. Ondo: 국채 토큰 시장 과거 규모(2025, 2026-01)와 Ondo 점유율 변화. 검색어: "tokenized treasuries market size 2025 Ondo share rwa.xyz"
19. Ondo: Oasis Pro 인수 금액과 이유. 검색어: "Ondo Oasis Pro acquisition price why"
20. Dinari: 매출, 고객 수, 파트너 수, 투자 라운드(시드, 시리즈 A 투자자). 검색어: "Dinari dShares partners number revenue Series A investors"

### B. 거래 시설(야간 ATS)
21. Blue Ocean ATS: 요금표(구독 브로커 대상 수수료), 구독 브로커 수, 한국 주문 비중. 검색어: "Blue Ocean ATS fee schedule subscribers number Korea share"
22. Bruce ATS: 요금, 구독자 수, 2025-06 투자 라운드 금액과 투자자. 검색어: "Bruce Markets funding round investors amount"
23. MOON ATS(OTC Markets): 수수료, 참가자, OTC Markets Group 주요 주주. 검색어: "OTC Markets MOON ATS fees subscribers", "OTC Markets Group major shareholders"
24. 세 ATS의 Form ATS-N 요약(수수료, 공정접근 대응). 검색어: "Form ATS-N Blue Ocean ATS fees fair access"

### C. 주황(조사 대상 밖이지만 비교용)
25. Securitize: 상장(SPAC, 2026), 기업가치, 주요 투자자, 한국 제휴(KB 등). 검색어: "Securitize public listing 2026 valuation", "Securitize KB 국민은행 MOU"
26. tZERO: 소유 구조(ICE 투자, Overstock), 기업가치, 최근 사업. 검색어: "tZERO ownership ICE investment 2026"

## 끝나면
채팅에 표를 주고, 캡처 zip을 사용자에게 준다. 사용자가 이 결과를 클라우드 세션에 붙여 넣으면 사실 DB와 본문에 반영된다.
