# 로컬 브라우저 확인 작업 (클라우드에서 막힌 페이지)

너는 사용자 컴퓨터에서 도는 Claude 세션이다. 클라우드 세션은 아래 사이트가 클라우드 IP 차단(403, 405, 지역 제한)으로 열리지 않았다. 사용자 브라우저로 공개 페이지를 열어 문장을 확인하고 캡처한다.

## 규칙
- 공개 페이지만 본다. 로그인하지 않는다. 계정, 결제, 개인정보 입력이 필요한 화면은 건너뛴다.
- 사이트가 사람 확인(캡차)을 요구하면 사용자에게 한 번 풀어 달라고 하고, 자동으로 우회하지 않는다.
- 페이지를 대량으로 긁지 않는다. 아래 항목에 필요한 페이지만 연다.
- 사실 행은 AGENT_GUIDE.md 형식으로 work/LOCAL/facts.csv, work/LOCAL/sources.csv에 쓴다(fact_id는 LOC-001부터, source_id는 LOC-S01부터). 검증 상태는 회사 공식 발표, 공시, 감독기관, 등록부면 "1차 출처 확인". 원문 근거 문장은 페이지의 영어 원문 그대로 한두 문장.
- 캡처는 captures/local/<회사>_<짧은이름>.png(폭 1200px 이하, 해당 문장이 보이게). 경로를 sources.csv의 캡처 파일 칸에.
- 항목별 결과(찾음/못 찾음, 링크, 원문 문장)는 kb/local_findings.md 표로.
- 이 세 곳(work/LOCAL, captures/local, kb/local_findings.md) 밖의 파일은 고치지 않는다. 다 하면 커밋하고 같은 브랜치에 푸시(`git pull --rebase` 후 `git push`).

## 확인할 것
### Coinbase
1. 설립 연도와 창업자, 공식 미션 문장: coinbase.com/about 또는 최신 10-K(investor.coinbase.com 또는 SEC EDGAR).
2. 2021-04 Nasdaq 직상장 공식 발표(investor.coinbase.com 보도자료).
3. SEC 소송 취하(2025-02): SEC 공식 발표나 Coinbase 블로그.
4. 예측시장 출시 시점(Coinbase 블로그 또는 보도자료).
5. Coinbase Prime, Coinbase Custody 출시 시점.
6. Coinbase Financial Markets의 NFA 등록(NFA BASIC, basic.nfa.futures.org에서 이름 검색): FCM 등록일.
### Binance (binance.com 공지)
7. 2026-06-01 미국 주식, ETF 7,000종 거래 개시 공지 본문.
8. bStocks 5종 담보 추가 공지(2026-10-28) 본문: 어떤 종목, 무슨 상품의 담보.
9. TradFi USDⓈ-M 무기한 계약 상장 공지(2026-10-29, 2026-11-11) 본문: 주식 종목이 들어 있나, 종목 이름.
10. 기관용 사업(Binance Institutional, VIP, 수탁) 출시 시점, 스테이블코인(BUSD 2019, FDUSD) 공지, 국채 토큰 담보(BUIDL, USYC 등) 수용 공지.
11. 창업자 창펑 자오 사면(2025-10 보도): 백악관이나 법무부 공식 문서(whitehouse.gov, justice.gov).
### Robinhood (investors.robinhood.com, newsroom)
12. 2026 Q3 실적 보도자료에서 Vlad Tenev 발언 "Our vision is to make everyone an owner..." 문단 캡처(captures/local/Robinhood_q3_quote.png).
13. 24 Hour Market이 Blue Ocean을 쓰는지 회사 발표나 공시.
14. Robinhood Derivatives, LLC의 NFA BASIC 등록일(NFA ID 0424278).
### SEC EDGAR (efts가 아니라 브라우저로)
15. Dinari, Inc.(CIK 0001898281)의 Form TA-1(명의개서대리인 등록) 접수일과 효력.
### Kraken
16. 예측시장 출시 발표(blog.kraken.com).
### 리히텐슈타인 FMA
17. Ondo Global Markets (BVI) Limited 기본 투자설명서 갱신(2026-11-11 이후 새 승인본 또는 보충서). fma-li.li의 승인 투자설명서 목록.
### 주식 무기한선물(선택)
18. Binance 선물 화면의 주식 무기한선물 목록과 24시간 거래대금, Bybit의 같은 정보(공개 화면만).

## 끝나면
kb/local_findings.md 맨 위에 찾은 것 개수, 못 찾은 것과 이유를 세 줄로 쓰고 푸시한다.
