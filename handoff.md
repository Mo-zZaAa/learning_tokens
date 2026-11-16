# KDX 해외 사례 리서치 인계 (2026-11-16)

브랜치 `research/kdx-overseas-20261116`. 지시문은 `INSTRUCTIONS.md`(v3, 이후 사용자 요청 반영분 포함). 판단 기록 원문은 `handoff_decisions.md`.

## 0. 먼저 볼 것: 접근 불가 링크와 도구 요청

- `db/blocked_links.csv` 88건. 많이 막힌 곳:
  - www.sec.gov(21건): SEC는 연락처를 담은 요청 식별 문자열(User-Agent)을 요구함. 임의 값 넣기는 권한 판정에서 거부되어 하지 않음. **사용자 허가가 필요함**: 연락처를 넣어도 되면 EDGAR 공시(10-K, 10-Q), SEC 성명(2026-01-28 토큰화 증권 성명), 면제 명령 보도자료, Form ATS-N, 명의개서대리인 등록부를 바로 열 수 있음.
  - 봇 차단 사이트(우회하지 않음): coinbase.com 전체, investors.robinhood.com 일부, theblock.co(8), businesswire.com(7), thedefiant.io, justice.gov, defillama.com, crowdfundinsider.com, cftc.gov, otcmarkets.com, assets.backed.fi(지역 제한).
  - 열지 못한 등록부: CFTC/NFA(JS 방식), FCA, ADGM, BVI 등기부, VARA.
- `mcp_requests.md`: 영상 자막 수집 도구, 화면 캡처 도구. 둘 다 쓰지 않았고 영상 조사(VID-1, VID-2)는 미룸.

## 1. 한 일

| 단계 | 내용 |
|---|---|
| 0 | 인수인계 zip 두 개 적용, 스킬과 에이전트 정의 설치, 환경 네트워크 허용(사용자 승인), 브라우저 경로 맞춤 |
| 1 | 제도 6개 에이전트(US-1~3, KR-1~2, CASE). `kb/regulation_us.md`, `regulation_kr.md`, `cases.md`, `regulation_compare.md` 작성. 법령 88조, 사건 18건 |
| 2 | 공식 사이트: Kraken, Ondo, Robinhood, Binance, Coinbase(base.org) 수집과 Haiku 묶음 읽기, verify. Dinari는 기존 수집분 정독. 회사별 위키 6개. 사이트 밖 자료 EXT 6개, ATS-1(야간 3곳), ATS-2(후보 추림), LIC(등록부) |
| 3 | 독립 검증 9개(회사 6, 사이트 Binance와 Coinbase, ATS, 제도). 원문 근거 문장 재대조, 숫자, 날짜, 인가, 법적 성격 전수 |
| 4 | DB 병합(`tools/merge_db.py`), 회사 본문 9개(`companies/`), 규칙 점검(`tools/check_body.py`), 사용자 추가 요청(licenses, relations 열 추가, 상품 DB) |

## 2. 회사별 채움 상태

사실 수(검증 상태별, `db/facts.csv`)

| 회사 | 1차 출처 확인 | 교차 확인 | 단일 출처 | 충돌 | 합계 |
|---|---|---|---|---|---|
| Kraken(Payward) | 86 | 7 | 54 | 4 | 151 |
| Robinhood | 99 | 12 | 15 | 3 | 129 |
| Binance | 63 | 7 | 20 | 0 | 90 |
| Coinbase | 96 | 6 | 58 | 3 | 163 |
| Dinari | 59 | 17 | 38 | 10 | 124 |
| Ondo | 110 | 10 | 24 | 2 | 146 |
| Blue Ocean ATS | 10 | 4 | 6 | 0 | 20 |
| Bruce ATS | 9 | 4 | 2 | 2 | 17 |
| MOON ATS | 6 | 3 | 2 | 0 | 11 |

공식 사이트(인수인계 스킬)

| 회사 | 장부 URL | 정독, 훑기 계획 | 수집 쪽 | 메모한 쪽 | 근거 대조(verify) | 미열람 범위 |
|---|---|---|---|---|---|---|
| Kraken | 218,550 | 1,142 | 204 | 47 | 428줄 중 불일치 2 | 우선 구역 외 대기 912쪽(blog, support 대부분), assets-cms PDF 다수 |
| Dinari | 464 | 339 | 308 | 58 | 별도 형식(메모 선행), 3단계에서 원문 대조 | blog 54건 제목만, docs 일부, audits |
| Ondo | 1,391 | 863 | 557 | 84 | 381줄 불일치 0 | usdy, ousg, learn, blog, api-reference 등 473쪽 |
| Robinhood | 51,060 | 413 | 152 | 60 | 329줄 중 불일치 15(미사용) | robinhood.com 본 사이트 대기 233쪽(수집 정체), cdn 법적 문서 일부 |
| Binance | 1,938,316 | 1,658 | 97 | 85 | 120줄 불일치 0 | 종목 상세 2,039쪽 목록만, 약관 본문, 투자설명서 PDF |
| Coinbase(base.org) | 647 | 139 | 98 | 24 | 251줄 불일치 0 | markets 02, 03(같은 틀), docs SDK |

- 각 회사 `KDX_사이트전수조사_인수인계/work/<회사>/coverage.md`, `verify.md`, `wiki/coverage.md`에 상세.
- 회사 본문: 9개 모두 규칙 점검 통과(모든 줄 근거 ID, 근거는 1차 출처 확인 또는 교차 확인만, 중분류 4줄 이내, 줄 40자 이내). 지운 칸 214건은 `db/absent.csv`.

## 3. 남은 공백

- 성과 수치: Kraken xStocks 거래량, AUM, 보유자 수와 Binance bStocks AUM은 회사 자체 주장이라 단일 출처. 독립 측정치(온체인 대시보드는 403) 확인 필요.
- 인가: BMA(버뮤다), CFTC/NFA, FCA, ADGM 개별 등록부 확인 못함. Dinari, Inc.의 명의개서대리인 등록, MOON ATS의 운영 법인(OTC Link LLC 추정)도 미확인.
- 경영진 발언 원문(향후 방향): Binance, Robinhood, MOON, Bruce는 확인된 발언이 없어 칸 삭제.
- 한국 관련: Robinhood 한국 진출 계획 기사(단일 출처), 각 사 한국 투자자 이용 가능 여부.
- 영상(VID-1, VID-2): 수행 안 함.
- 상품 DB(`db/companies.csv`)는 PROD 에이전트 결과 반영 여부를 아래 7절에 적음.

## 4. 충돌과 판정

`kb/canon.md`. 주요 판정:
- Bruce ATS 2026 Q2 거래대금: 회사 490.3억 달러 대 FINRA 합산 393.5억 달러. FINRA 기준, 둘 다 DB에 충돌로 남김.
- Coinbase 토큰 투자자 권리: 보도자료(주주 권리 포함) 대 투자설명서(배당 직접 지급 없음, 의결권 제한). 투자설명서 기준.
- Robinhood Bitstamp 인수가: 언론 2억 달러 대 10-Q 공정가치 2.24억 달러. 10-Q 기준.
- Ondo Oasis Pro 인수: 2025-07 발표, 2025-10-07 완료(회사 블로그).
- Dinari 증권사 모회사: BrokerCheck 직접 소유주 Dinari Holdings, LLC 대 회사 표기 Dinari, Inc. 등록부 사실만 본문 사용.
- Kraken xStocks 종목 수(700, 1,000, 1,300, 1,500 초과)는 보도자료마다 다름. 본문에 쓰지 않음.

## 5. 지시문과 다르게 한 것(요약)

- 시간: 11:43 UTC 시작, 12:31 본문 9개 완료로 90분 안. 다만 공식 사이트 수집은 읽기와 파일 충돌을 막으려고 12:16에 멈춰 대기 쪽이 남음.
- 네트워크: 처음엔 허용 호스트 추가, 이후 사용자 승인으로 제한 없음 전환. 웹 열람 도구는 세션 시작 때 목록을 따라 계속 막혀 셸 curl로 대체.
- 회사 위키 작성과 DB 옮기기는 메인 대신 sonnet 에이전트(SITEFACT)가 함. 메인은 위키의 open-questions, verify, DB로 본문 작성.
- Dinari는 추가분 zip 전에 sonnet이 정독해 메모 형식이 다름(verify 대상 아님, 3단계 원문 대조로 대신).
- 판정 기준: 회사 자체 문서(약관, 투자설명서, docs, 보도자료)는 자기 상품 내용에 대해 1차 출처. 인가 보유, 규모, 순위 주장은 등록부나 독립 출처가 있어야 확인.
- 제도 비교 줄은 사실 ID 대신 law_id(예: [KR-자본시장법-119])를 근거로 붙임.
- Binance 장부(458MB)는 GitHub 한도 때문에 압축본만 커밋.

## 6. 다음에 팔 가치가 있는 주제

1. SEC 공시(EDGAR) 허용 후: Coinbase, Robinhood 10-K, 10-Q의 토큰 사업 서술, SEC 2026-01-28 성명 원문으로 상품 분류 확정.
2. 등록부 보강: BMA, CFTC/NFA, FCA, ADGM, VARA. `db/licenses.csv`의 빈칸 채우기.
3. 독립 성과 지표: 온체인 대시보드(DefiLlama, Dune) 접근이 되면 주식 토큰별 발행 잔액, 거래량을 같은 기준으로 비교.
4. 한국 연결: 카카오페이증권의 Dinari, Ondo 협약 진행, 국내 증권사의 야간 ATS 주문 연결 현황.
5. ATS 후보 STEN(개인 대상 비상장주식), CGXS(체결 방식 차별) 상세 조사.
6. 영상: 경영진 발표 영상 자막과 캡처(도구 허가 필요).

## 7. 사용량

- `usage_log.md`: 서브에이전트 누적 약 840만 토큰(12:31 UTC). 사용자 확인값(약 114만 토큰에 1%p)으로 보면 주간 사용률 약 28~29% 추정. 상한 50% 안.
