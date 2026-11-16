# KDX 해외 사례 리서치 실행 지시

너는 이 리서치의 메인 세션이다. 직접 조사하지 말고, 서브에이전트를 병렬로 띄워 수집과 검증을 시키고, 너는 기초 지식 관리, 배분, 병합, 품질 판정을 맡는다. 총 시간은 90분이다.

공식 사이트 원자료는 다른 대화에서 만든 스킬(company-site-wiki)과 일부 회사의 수집 결과(인수인계 묶음)를 이어 쓴다(5-1절). 사용량은 5-2절을 지킨다.

## 1. 배경

- 의뢰 맥락: KDX(국내 장외 조각투자 유통 플랫폼, 출발점은 신탁수익증권과 국내 개인, 일반법인)의 중장기 확장 전략 수립. 확장 축은 자산, 고객, 시장(해외) 세 가지.
- 이 리서치가 답할 질문
  1. 해외 주식 토큰 사업자는 무엇을, 누구에게, 어떤 구조로 제공해 성장했는가. 해외 상품의 국내 공급과 국내 자산의 해외 공급을 검토하는 근거로 쓰인다.
  2. 다른 시간대 고객을 상대하는 대체거래소(ATS)는 사업성이 있는가. 해외 투자자 시간대에 국내 주식 토큰을 체결하는 시장 구상의 근거로 쓰인다.
  3. 미국과 한국의 제도 차이가 이 사업들을 어떻게 가능하게 했고, 국내에서는 무엇이 제약인가.
- 보고받는 사람(PM)의 요구: 회사별로 설립 목적, 성장 경로, 현재 사업(무엇을, 누구에게, 어떤 방식으로), 타깃 수요, 성공요인, KDX 시사점, 한국과의 차이. 사례는 이름만 적지 말고 구조가 설명되어야 한다.
- 읽는 사람은 금융 기초 용어부터 확인하는 수준이다. 본문의 모든 용어는 용어 DB에 풀이가 있어야 하고, 회사, 상품, 기관 이름 뒤에는 한눈에 이해되는 설명을 괄호로 붙인다.
- 토큰증권만 찾지 않는다. 회사의 전체 사업을 다 찾고, 그 안에서 토큰증권 관련 내용은 있는 대로 다 찾는다.

## 2. 대상과 우선순위

| 순위 | 대상 | 깊이 |
|---|---|---|
| 1 | 한미 제도 기초(법령 원문, 판례, 제재) | 다른 모든 조사의 기준. 가장 먼저 수행 |
| 2 | Kraken(모회사 Payward), Robinhood, Binance, Coinbase, Dinari, Ondo | 상세 조사 |
| 3 | 미국 ATS 후보 추림 | 후보를 추리는 것이 먼저. 전수 상세 조사는 하지 않음 |
| 4 | 추린 ATS 후보 2~4곳 | 상세 조사. 시간 부족 시 야간 거래 3곳(Blue Ocean ATS, Bruce ATS, MOON ATS)만 |

- 제외: PPEX.
- Securitize, tZERO는 다른 담당자가 조사한다. 직접 조사하지 않는다. 다만 위 대상을 조사하다가 이 두 회사에 대해 확인이 필요한 점이 나오면 `db/handover_questions.csv`에 적는다.
- ATS 후보 추림 기준: (1) 사업 성과(거래 규모, 성장), (2) 다른 ATS와 구별되는 시장, 고객, 거래 방식, (3) 토큰증권 취급 현황과 계획. SEC ATS 목록은 이름과 취급 자산만 훑고, 기준에 걸리는 곳만 후보로 올린다. 중요하지 않은 곳은 파지 않는다.
- 공식 사이트 원자료의 진행 상태는 회사마다 다르다. 5-1절의 "회사별 시작점" 표를 따른다.

## 3. 절대 규칙

1. 기억으로 쓰지 않는다. 네가 이미 아는 내용이라도 이번 실행에서 연 링크로 확인된 것만 DB에 넣는다. 인수인계 묶음의 raw 파일(스크립트가 받은 공식 사이트 원문 변환본)은 연 링크로 본다. 이때 열람 일시는 raw 파일 머리의 `fetched` 값이다.
2. 모든 사실 줄에는 출처 링크, 원문 근거 문장(짧게), 열람 일시가 있어야 한다. 없으면 넣지 않는다.
3. 출처 우선순위: 법령 원문, 규제기관 문서, 회사 공시와 보도자료, 약관과 투자설명서가 1차 출처. 숫자, 날짜, 인가, 지분율은 1차 출처를 먼저 찾는다. 언론만 있으면 서로 다른 2곳 이상이 일치할 때만 확인으로 본다. 회사 사이트에 적힌 인가와 등록 사실은 감독기관 등록부나 공시로 확인해야 `1차 출처 확인`으로 본다.
4. 검증 상태는 넷 중 하나로 표기: `1차 출처 확인`, `교차 확인`, `단일 출처`, `충돌`.
5. 회사별 본문에는 `1차 출처 확인`과 `교차 확인`만 쓴다. `단일 출처`와 `충돌`은 DB에만 남긴다.
6. "왜"는 회사가 직접 밝힌 이유만 쓴다. 추측한 동기는 쓰지 않는다.
7. 숫자는 무엇을 잰 것인지와 기준일을 함께 적는다.
8. 찾았으나 공개 자료가 없는 항목은 지어내지 말고 `db/absent.csv`에 찾아본 곳과 함께 적는다. 확인할 필요가 없다고 판단해 넘긴 항목도 사유와 함께 같은 파일에 적는다.
9. 사용자는 자리에 없다. 질문하려고 멈추지 않는다. 사용자 확인이 필요한 일(새 MCP나 외부 도구 사용 허가, 접근하지 못한 링크)은 파일에 적어 두고 계속 진행한다. 그 밖의 판단은 스스로 내리고 `handoff.md`에 적는다. SKILL.md가 "사용자에게 보여 주고 진행"하라는 곳(정독 대상 300쪽 초과 등)도 묻지 않고 5-2절 상한 안에서 스스로 정한다. 멈추는 예외는 하나뿐이다: 5-2절의 사용량 상한에 걸릴 때.
10. 단계가 끝날 때마다 결과를 커밋하고 브랜치로 푸시한다. 중간에 끊겨도 그때까지의 결과가 남아야 한다.
11. 5-2절 사용량 규칙을 지킨다. 주간 사용 한도의 50%를 넘기지 않는다.

## 4. 도구 허가와 접근 불가 링크

- 시작하자마자 쓸 수 있는 도구를 점검한다. 추가로 쓰고 싶은 MCP나 외부 도구(예: 영상 자막 수집 도구, 화면 캡처 도구)가 있으면 설치나 연결을 하지 말고 `mcp_requests.md`에 도구 이름, 쓰려는 곳, 필요한 권한, 없을 때의 대안을 적는다.
- 사전 허가된 도구: 인수인계 묶음의 company-site-wiki 스킬, 그 스크립트 `sitewiki.py`, 스크립트가 쓰는 파이썬 패키지(requests, beautifulsoup4, lxml, markdownify, playwright, markitdown). 사이트 전체 수집은 이 스크립트로 한다. 브라우저는 이미 설치된 Chromium이나 Chrome을 쓰고, `python3 -c "import playwright"`가 되고 브라우저가 있으면 `playwright install`을 하지 않는다. 없을 때만 설치한다.
- 허가받지 않은 도구는 쓰지 않는다. 기본 도구(웹 검색, 웹 열람, 셸)와 위 스크립트로 끝까지 진행하고, 다른 도구가 있었다면 더 얻을 수 있었던 것을 `handoff.md`에 적는다. 사용자가 돌아와 허가하면 그때 보강한다.
- 셸에서 외부 사이트 접속이 막히면(네트워크 제한) 웹 검색과 웹 열람 도구로 대신하고, 막힌 도메인을 `handoff.md`에 모아 적는다. 공식 사이트 수집이 막히면 SKILL.md의 "막혔을 때" 절을 따른다.
- 열지 못한 링크(로그인, 유료 구독, 접속 차단, 읽기 어려운 형식)는 `db/blocked_links.csv`에 모은다. 열: 링크, 무엇이 있는 곳인지, 필요한 이유, 막힌 종류, 시도한 방법, 필요한 조치. 스크립트 수집에서 상태가 blocked인 페이지도 웹 열람 도구로 그 URL만 한 번 더 시도한 뒤 안 되면 여기에 넣는다. 종료 보고의 맨 위에 이 목록과 `mcp_requests.md`를 보여 준다. 사용자가 파일로 넘겨주면 `inputs/`에서 읽어 반영한다.

## 5. 기초 지식 공유 방식

- `kb/` 폴더가 기초 지식이다. 메인 세션만 고친다.
  - `kb/regulation_us.md`, `kb/regulation_kr.md`: 쟁점별 현행 제도, 근거 조문, 링크
  - `kb/regulation_compare.md`: 쟁점별 한미 비교와 차이에 따른 결과. 마크다운 표 하나로 쓰고 열은 쟁점, 미국 제도, 미국 근거 조문(law_id와 링크), 국내 제도, 국내 근거 조문(law_id와 링크), 차이에 따른 결과로 고정한다. 리서치 뒤 웹 화면 작업이 이 표를 그대로 CSV로 바꿔 쓴다.
  - `kb/glossary.md`: 용어 풀이
  - `kb/canon.md`: 출처끼리 충돌했을 때 내린 판정과 근거
- 모든 서브에이전트는 시작할 때 `kb/`를 읽는다.
- 서브에이전트가 기초 지식에 더하거나 고칠 것을 찾으면 `kb/proposals/<에이전트 이름>.md`에 링크와 함께 적는다. 메인 세션이 단계가 끝날 때마다 모아 `kb/`에 반영하고, 이후 띄우는 서브에이전트는 반영된 내용을 읽는다.
- 회사 조사 중 제도와 관련된 발견(예: 특정 인가의 근거 조문, 면제 조건)은 반드시 proposals로 올린다. 공식 사이트 묶음을 읽다가 나온 것도 같다.

## 5-1. 공식 사이트 원자료: 인수인계 묶음과 company-site-wiki 스킬

### 위치와 설치 (0단계에서 한 번)

1. `inputs/KDX_사이트전수조사_인수인계.zip`을 저장소 맨 위에서 푼다. 결과 폴더는 `KDX_사이트전수조사_인수인계/`이고, 이하 H라고 쓴다.
2. 회사별 원자료 작업 폴더는 `H/work/<회사>`(소문자 회사명: kraken, dinari, ondo, robinhood, coinbase, binance, 그리고 ATS별 폴더)다. 서브에이전트 산출 폴더 `work/<회사>_<주제>/`와는 다른 곳이다. 섞지 않는다.
3. `H/skill/company-site-wiki` 폴더를 `.claude/skills/company-site-wiki`로 복사한다. 이하 S는 `.claude/skills/company-site-wiki/scripts/sitewiki.py`.
4. 설치: `pip install requests beautifulsoup4 lxml markdownify playwright "markitdown[pdf]"`. 브라우저는 4절대로.
5. `python3 S --help`가 도는지, `curl -sI https://dinari.com`으로 셸에서 외부 접속이 되는지 확인한다.
6. `H/00_먼저읽기.md`와 `.claude/skills/company-site-wiki/SKILL.md`를 읽는다. 둘이 이 지시문과 어긋나면 이 지시문을 따른다. `H/01_*.md`, `H/02_*.md`는 이 지시문에 이미 반영했으므로 읽지 않는다.

### 원자료의 층과 순서

raw(원문 변환본, 스크립트가 만듦) > notes(묶음별 사실 메모) > wiki(회사별 원자료 정리본) > DB 줄(`work/<회사>_site/`를 거쳐 `db/`) > `companies/<회사>.md`(기업별틀)

- 공식 사이트는 SKILL.md 절차(map > plan > fetch > digest > 읽기와 notes > wiki > audit)로만 조사한다. 웹 검색과 낱장 열람으로 공식 사이트를 훑지 않는다.
- 회사별 위키(`H/work/<회사>/wiki/`)는 원자료 정리본이다. 기업별틀(`companies/<회사>.md`, 원본은 `inputs/`의 기업별 틀 엑셀)은 위키와 DB의 사실을 근거로 그다음에 채운다. 기업별 틀 엑셀과 스토리라인 파일은 고치지 않는다.
- 위키 줄은 SKILL.md대로 출처 URL을 붙인다. DB로 옮길 때 원문 근거 문장, 원문 위치(raw 파일 경로와 절 제목), 열람 일시(raw의 `fetched`)를 채운다.
- 공식 사이트 원문은 `sources/`에 다시 복사하지 않는다. `db/sources.csv`의 `저장 파일 경로`에 raw 파일 경로를 적는다. `sources/`는 공식 사이트 밖 자료(공시, 규제기관 문서, 언론)용이다.

### 회사별 시작점

| 회사 | 끝난 것(다시 하지 않음) | 이어서 할 것 |
|---|---|---|
| Kraken | map(URL 218,200개, `H/work/kraken/inventory.csv`), 읽기 계획(`overrides.json`), 70쪽 수집 | fetch 반복(대기 966쪽, 아래 "먼저 읽을 묶음" 구역부터 `--only`로) > digest > 읽기. 회사 소유 도메인 추가(아래) |
| Dinari | map, fetch(308쪽, PDF 12건 포함, 대기 0), digest | `H/work/dinari/packs` 읽기부터 |
| Ondo | map | fetch 반복(대기 183쪽) > digest > 읽기 |
| Robinhood, Coinbase, Binance | 없음 | map부터 |
| 미국 ATS(Blue Ocean, Bruce, MOON, 2단계에서 추린 후보) | 없음 | map부터. 운영사 도메인은 12절 보도자료와 SEC Form ATS-N에서 확인 |

- 다시 실행하지 않는 것: Kraken map, Kraken 읽기 계획 새로 짜기, Dinari map, fetch, digest, Ondo map, 스크립트 동작 시험. Kraken 계획을 바꿀 때는 `plan`에 패턴을 더하는 방식으로만 바꾼다.
- Kraken map은 초기판으로 돌려 stocks 종목별 목록이 일부(448쪽)만 있다. map을 다시 돌리지 않는다. 전체 종목 수는 사이트 본문이나 다른 출처로 확인한다.
- Ondo의 `map_log.md` 하위 사이트 후보 중 공개용으로 보이는 것(community, summit, ai, usdy 등)만 `--seed`로 추가한다. 시험용, 내부용(dvn, grpc, api, cdn, betterstack, entity-tax-cert 등)은 열지 않는다.
- Kraken 회사 소유 도메인: `H/00_먼저읽기.md` 7번의 후보(payward.com, services.payward.com, xstocks.fi, krak.app, ninjatrader.com, breakoutprop.com, cfbenchmarks.com, reap.global)와 assets.backed.fi(xStocks 법적 문서 위치). 소유 근거(12절 Payward 보도자료, 자동 이동, 약관의 운영 주체)를 확인한 곳만 `python3 S map --work H/work/kraken --domain 새도메인 --seed https://새도메인`으로 같은 폴더에 추가한다. payward.com, xstocks.fi, backed.fi를 먼저 하고, 나머지는 5-2절 "미룰 일"이다. 근거를 못 찾으면 handoff.md에 적고 넘긴다.
- Coinbase는 인수인계 묶음에 없다. 다른 새 회사와 같이 map부터 한다.
- 새 회사(Robinhood, Coinbase, Binance)의 plan 조정은 Kraken 기준을 따른다: 국가판과 언어판 중복, 앱 화면, 로그인, 가입, 문의 양식, 자산별로 같은 틀이 반복되는 가격과 판촉 페이지는 skip이나 list. 블로그, 고객센터, 약관 글은 `inventory.csv`의 URL을 핵심어로 걸러(`grep -iE`) 걸린 것만 skim이나 read로 올린다. 핵심어는 `H/00_먼저읽기.md` 5번 Kraken 핵심어에 그 회사의 상품명을 더한 것. 메인 세션은 `map_log.md`와 `plan_summary.md`만 보고 패턴을 정한다.
- 새 회사의 IR, 뉴스룸처럼 다른 도메인에 있는 회사 운영 사이트는 `map_log.md`의 "사이트가 링크한 외부 호스트"에서 근거(푸터 법인명, 자동 이동, 운영 주체)를 보고 가려 `--domain`으로 추가한다.
- Binance 사이트는 접속 지역에 따라 셸에서 막힐 수 있다. 막히면 SKILL.md "막혔을 때"를 따르고 `db/blocked_links.csv`와 `handoff.md`에 적는다.
- ATS 운영사 사이트가 대형 사이트의 일부(예: MOON ATS가 운영사 사이트의 한 구역)이면 map 뒤 plan에서 ATS 관련 구역과 투자자 정보 구역만 read로 두고 나머지는 list로 둔다.

### 제외 범위 (열지 않는다)

`H/00_먼저읽기.md` 5번 "더 볼 필요 없는 곳"을 그대로 제외 범위로 쓴다. 기업별틀을 채우다가 꼭 필요해지면 해당 URL만 `plan --read` 패턴으로 올리고 사유를 handoff.md에 적는다.

Kraken

| 구역 | 처리 |
|---|---|
| 국가판 접두어 27개(ar, at, au, be, br, ca, ch, cn, cz, de, dk, es, fi, fr, gb, gr, in, it, mx, nl, no, pl, pt, ro, se, tw, ua) 아래 페이지(180,878쪽). 단, 특정 국가판에만 있는 71쪽(장부 note 칸 표시)은 남아 있음 | 제외 |
| pro.kraken.com/app/*(거래 앱 화면 23,797쪽) | 제외 |
| id.kraken.com, app.kraken.com, proapp.kraken.com, 가입 화면, 고객센터 문의 양식과 검색 | 제외 |
| www의 buy, sell, price-prediction, convert, prices, categories, compare, competitions(약 4,000쪽) | 목록만 |
| www의 features 아래 dollar-cost-averaging, futures, margin-trading, auto-earn, staking의 자산별 페이지(약 1,500쪽). 각 기능 첫 화면은 정독 | 목록만 |
| www의 xstocks 종목별 1,216쪽, stocks 종목별 448쪽 | 표본만(xstocks 5종목, stocks aapl과 tsla). 종목 목록은 inventory.csv에서 뽑음 |
| www의 learn(676쪽) | 목록만 |
| blog의 market-reports, tag, category, kraken-japan, go(약 2,000쪽) | 목록만 |
| docs.kraken.com API 참조, status.kraken.com 장애 이력(약 500쪽) | 목록만 |
| 그 밖의 blog와 support 글(약 4,400쪽) | 핵심어에 걸린 281건만 훑기. 그중 xstock, equit, tokeniz가 들어간 글만 정독 |

Dinari

- docs.dinari.com/reference(API 참조 72쪽): 표본 2~3쪽만.
- dinari.com/dshares 묶음 4개: 첫 쪽만 정독. 나머지는 종목 표만 다른 쪽 번호 변형.
- assets.dinari.com/audits(스마트컨트랙트 감사 보고서 PDF 4건): 보안 감사 내용이 필요할 때만.
- www.dinari.com(dinari.com과 같은 내용), money2020, careers, contact-us, privacy, status, app.dinari.com의 trade, orders, portfolio: 읽지 않음.
- docs.dinari.com/login 이동 주소 124건: robots.txt 제외 대상. 수집하지 않음.

Ondo

- app.ondo.finance/assets/* 477쪽: 표본만.
- 인증서 기록에서 나온 시험용, 내부용 하위 호스트 449개: 열지 않음.

공통(SKILL.md "지킬 것"): robots.txt 제외 경로, 로그인 화면, 캡차, 차단은 우회하지 않는다. 요청 속도 옵션을 올리지 않는다. staging, dev, test, internal, admin 같은 호스트는 열지 않는다.

### 먼저 읽을 묶음

| 회사 | 먼저 읽을 묶음 |
|---|---|
| Kraken | www의 xstocks, stocks, institutions, legal(equities, xstocks, digital-assets-brokerage-services), prime, krak, compliance, features 첫 화면들, press. blog의 product/xstocks. support의 xstocks 관련 글. assets-cms의 PDF 37건(제목부터 확인). 최상위 바로 아래 215쪽은 행사와 경품 페이지가 섞여 있으니 `packs/_index.md`의 묶음 이름을 보고 고름 |
| Dinari | dshares 첫 쪽, usdplus, business, get-started, us, bd(브로커딜러 공시 PDF 7건), terms-conditions-usdplus-stusdplus-tokens, case-studies, transparency, assets.dinari.com/forms(USD+ 백서), docs.dinari.com/docs의 안내 글 |
| Ondo | docs의 ondo-stocks, general-access-products, legal. app의 표본 자산 페이지. ondo.finance 본 사이트 |
| 새 회사, ATS | 주식 토큰 상품 페이지, 법적 고지와 약관, 투자자 정보, 보도자료 목록, 회사 소개. 핵심어에 걸린 글 |

- 이 표에 없는 묶음은 기본적으로 읽지 않는다. 5-2절 상한이 남을 때만 관련도 순으로 더 읽는다.
- 같은 틀 묶음(`packs/_groups.md`의 닮은 정도 0.5 이상)은 표본만 읽는다.

### notes 형식

SKILL.md 5단계 형식을 쓰되, DB로 옮길 사실 줄에는 아래를 붙인다.

```markdown
### <URL>
- 사실 한 줄
  - 원문: "짧은 원문 근거 문장"
  - 위치: <raw 파일 경로> / <절 제목>
  - 틀: <7절 틀의 항목, 예: 핵심 사업 상세 > 발행 구조 > 법적 성격>
  - 숫자면: 무엇을 잰 것, 기준일
- 조사 질문 관련도: 높음, 중간, 낮음
```

- 정독한 페이지는 쓸 내용이 없어도 한 줄(쓸 내용 없음, 사유)을 남긴다.
- "서로 어긋나는 서술"과 "더 봐야 할 것"은 SKILL.md 형식 그대로 둔다. 위키의 `open-questions.md`로 모인다.

### 공식 사이트 밖 자료

- 감독기관 등록부(FINRA BrokerCheck, SEC EDGAR, 각국 감독기관), 공시, 실적 발표, 주주서한, 언론, 인터뷰는 2단계 외부 수집 에이전트가 웹 검색과 열람으로 찾는다. 출발점은 위키의 `open-questions.md`와 7절 틀의 빈칸이다.
- 외부 수집 에이전트는 공식 사이트(H/work/<회사>의 범위)를 다시 열지 않는다. 사이트 내용이 필요하면 그 회사의 notes나 위키를 읽는다.

## 5-2. 사용량

- 원칙: 이 실행은 주간 사용 한도의 50%를 넘기지 않는다. 나머지는 사용자가 이 실행 뒤 질의응답 등에 쓸 몫이다.
- 토큰이 드는 곳: 수집(map, plan, fetch, digest, audit)은 스크립트라 토큰이 거의 들지 않는다. 토큰은 묶음 읽기, 웹 열람, 서브에이전트 지시와 보고에서 든다. 그래서 수집은 넓게, 읽기는 좁게 한다.

### 상한 정하기

메인 세션은 주간 사용률을 직접 보지 못한다. 그래서 아래 순서로 상한을 정한다.

1. 0단계에서 `inputs/usage.md`를 읽는다. 사용자가 시작 전에 적어 둔 주간 사용률(%)과 이번 실행에 쓸 상한이 있으면 그것을 쓴다. %는 메인 세션이 직접 잴 수 없으므로, 파일에 적힌 대리 상한(정독 글자수, 서브에이전트 토큰 누적)을 지킨다.
2. 파일이 없으면 기본 상한을 쓴다: 공식 사이트 원문 정독 합계 회사당 30만 자, ATS 1곳당 10만 자, 전체 200만 자(약 50만 토큰). 상한은 5-1절 "먼저 읽을 묶음" 안에서 관련도 높은 순으로 채운다.
3. 서브에이전트가 끝날 때 표시되는 토큰 수를 `usage_log.md`에 누적한다.

### 읽기 전 보고

- 회사마다 읽기 시작 전에 `usage_log.md`에 한 줄을 쓰고 대화에도 남긴다: 읽을 묶음 목록, 글자수 합계(`packs/_index.md`의 글자수), 예상 토큰(글자수 ÷ 4), 지금까지 누적, 상한 대비 비율.

### 멈춤

- 다음 회사를 읽으면 상한을 넘길 것으로 보이면 그 읽기를 시작하지 않는다.
- 멈출 때 할 일: 읽기와 새 서브에이전트 띄우기를 멈춘다. 이미 모인 결과의 병합, 커밋, 푸시만 한다. `usage_report.md`를 쓰고 종료 보고 맨 위에 둔 뒤 끝낸다.
- `usage_report.md` 내용: 지금까지 읽은 양(묶음, 글자수, 토큰), 남은 묶음과 예상량, 줄일 수 있는 안(묶음 우선순위, 낮은 모델로 돌릴 수 있는 일).

### 모델 배분

서브에이전트를 띄울 때 `model`을 지정한다.

| 일 | 모델 |
|---|---|
| map, plan, fetch, digest, audit 실행, CSV 합치기, 중복 제거, ID 부여, 원문 근거 문장 대조 | 모델 쓰지 않음(셸, 짧은 파이썬) |
| ATS-2 목록 훑기, VID-1과 VID-2(영상 찾기와 자막 정리), skim 표 확인, 관련도 낮은 묶음 읽기, 용어 후보 뽑기 | haiku |
| 먼저 읽을 묶음 정독과 notes, 위키 작성과 DB 옮기기, 외부 수집, 검증, 1단계 US-1, US-3, KR-1, CASE | sonnet |
| 1단계 US-2, KR-2(이 과제의 핵심 쟁점) | opus |
| kb 반영, 충돌 판정(canon.md), companies 본문, 핵심 성공요인과 KDX 시사점 | 메인 세션 |

### 미룰 일 (시간과 상한이 남을 때만)

- VID-1, VID-2.
- ATS 후보 중 야간 거래 3곳 밖의 상세 조사.
- Kraken의 부수 도메인(krak.app, ninjatrader.com, breakoutprop.com, cfbenchmarks.com, reap.global).
- 5-1절 "먼저 읽을 묶음"에 없는 묶음(예: Ondo api-reference 5묶음 약 52만 자, intelligent-portfolios, Dinari blog와 audits, Kraken blog의 훑기 대상).

### 아끼는 규칙

- `inventory.csv`, `raw/`, `packs/`를 통째로 열지 않는다. Kraken의 inventory.csv는 44MB다. 필요한 줄만 `grep`이나 짧은 파이썬으로 뽑는다. 현황은 `plan_summary.md`, `packs/_index.md`, `packs/_groups.md`, `coverage.md`로 본다.
- 같은 원문을 두 번 읽지 않는다. 묶음 하나를 읽을 때마다 notes를 남긴다. 읽기로 한 묶음은 끝까지 읽되, 읽을 묶음 수로 양을 줄인다.
- 서브에이전트는 결과를 자기 파일에 쓰고 대화로는 10줄 보고만 돌려준다. 원문을 대화로 돌려보내지 않는다.
- 검증 3단계에서 공식 사이트 사실의 원문 근거 문장이 raw 파일에 그대로 있는지는 메인 세션이 스크립트(`grep -F`)로 먼저 대조한다. 검증 에이전트는 뜻이 맞는지와 외부 출처만 본다.

## 6. 진행 순서와 시간

시각은 셸의 `date`로 확인하고, 단계별 상한을 넘기면 다음 단계로 넘어간다.

### 0단계 (10분) 준비

- 도구 점검, 허가가 필요한 도구 기록, 폴더 생성, `inputs/` 읽기(`usage.md` 포함).
- 5-1절 "위치와 설치".
- 공식 사이트 수집을 셸 백그라운드로 시작한다. 토큰이 들지 않고, 이후 단계와 동시에 돈다. `fetch --minutes 8`을 대기 0이 될 때까지 반복하는 셸 반복문으로 돌리고, 끝나면 `digest`를 실행한다. 회사별로 따로 돌린다.
  ① Ondo: fetch 반복 > digest. 공개용 하위 사이트 추가는 map 후 이어서.
  ② Kraken: 먼저 읽을 구역을 `--only`로 먼저 받고 나머지 > digest. 소유가 확인된 도메인은 map 추가 후 fetch.
  ③ Robinhood, Coinbase, Binance: map. 끝나는 대로 메인 세션이 plan 패턴을 정하고 fetch > digest.
  ④ ATS 3곳 운영사 사이트: map > plan > fetch > digest.
- Dinari는 수집이 끝나 있으므로 2단계에서 바로 읽는다.
- 0단계가 끝날 때 커밋한다(H 폴더 포함).

### 1단계 (20분) 한미 제도 기초

서브에이전트 6개를 한 번에 띄운다. 모델은 5-2절 표대로.

| 에이전트 | 범위 |
|---|---|
| US-1 | 증권의 정의와 판단 기준, 가상자산과 증권의 경계, 감독기관 역할 분담 |
| US-2 | 사업자 등록 체계(브로커딜러, 명의개서대리인, 청산기관, 거래소), ATS 규율, 2026년 9월 SEC의 주식 토큰 관련 조건부 면제 |
| US-3 | 발행 규제와 면제(공모, 사모, 역외 발행), 자국민 판매 제외 구조, 예탁증권 제도 |
| KR-1 | 자본시장법의 증권 정의와 종류, 금융투자업 인가 단위와 최저 자기자본, 장외거래중개업, 다자간매매체결회사 |
| KR-2 | 토큰증권 제도(전자증권법과 자본시장법 개정, 2026년 10월 하위법규 입법예고, 금융위 정책 방향), 발행과 유통 분리, 금융업과 가상자산업의 겸영 제한, 해외 발행 증권의 국내 판매, 외국인 투자 경로 |
| CASE | 미국과 한국의 관련 판결, 제재, 합의, 면제 명령, 비조치 의견. 대상 6개사가 당사자인 사건 우선 |

- 각 에이전트는 법령 원문과 규제기관 문서를 직접 연다. 로펌 해설은 길잡이로만 쓰고, 조문은 원문에서 확인한다.
- 결과로 `kb/`를 채운 뒤 2단계로 넘어간다.
- 이 단계 동안 백그라운드 수집 상태를 `coverage.md`와 `plan_summary.md`로 한 번 확인하고, 새 회사의 plan 패턴을 정한다.

### 2단계 (35분) 수집

한 번의 메시지에서 환경이 허용하는 최대 수를 동시에 띄우고, 남은 것은 끝나는 대로 이어 띄운다. 하나씩 차례로 돌리지 않는다. 다만 5-2절 상한 안에서 띄운다.

2a 공식 사이트 읽기(회사마다)

- 읽기 전에 5-2절 "읽기 전 보고"를 한다.
- SITE-<회사>-<번호> 에이전트: 그 회사의 먼저 읽을 묶음을 호스트나 구역 단위로 나눠 맡는다. 에이전트 하나에 묶음 글자수 합계 15만 자 안팎. 맡은 묶음을 끝까지 읽고 `H/work/<회사>/notes/<묶음이름>.md`만 쓴다(5-1절 notes 형식).
- 수집이 아직 안 끝난 회사는 준비된 묶음부터 읽는다. 2단계 시작 20분 뒤에도 준비되지 않은 묶음은 coverage에 "미열람(수집 미완료)"으로 남긴다.
- WIKI-<회사> 에이전트(회사마다 하나): 그 회사의 읽기가 끝나면 notes로 `H/work/<회사>/wiki/`를 SKILL.md 6단계대로 쓰고, `python3 S audit --work H/work/<회사> --wiki H/work/<회사>/wiki`를 실행한다. 이어 위키 사실을 10절 열에 맞춰 `work/<회사>_site/`의 facts.csv, sources.csv, terms.csv, relations.csv, notes.md로 옮긴다. 줄마다 `틀 항목`을 단다. 위키 `glossary.md`의 용어는 terms.csv로, 제도 관련 발견은 proposals로 올린다.

2b 공식 사이트 밖 자료(회사마다, 2a와 동시에)

아래 주제 표는 채울 항목의 점검표다. 공식 사이트에서 나오는 부분은 2a가 채우고, 2b는 사이트 밖 자료만 찾는다.

| 주제 | 채울 항목 |
|---|---|
| A 기업 개요 | 기본정보, 지배구조(모회사, 주요 주주), 취득 라이선스와 근거 법령(미국, 미국 외), 받은 제재 |
| B 연혁과 방향 | 설립 목적, 단계별 확장 경로(인수, 제휴, 인가 취득, 출시를 시점과 함께), 토큰증권 사업 진출 배경(출발 사업과의 관계, 회사가 밝힌 진출 사유), 향후 방향(경영진 발표, 실적 발표, 주주서한, 인터뷰 원문) |
| C 사업 구조 | 자산군별 상품(전통증권, 토큰증권, 가상자산, 파생상품 및 기타)의 제공 내용, 대상 고객, 제공 방식. 서비스 범위(발행, 매매 체결, 청산, 결제, 수탁 및 권리 기록, 고객 접점)별 개시 시기와 수행 법인. 수익원 |
| D 핵심 사업 상세 | KDX가 참고할 사업 하나(대개 주식 토큰 사업)의 최종 투자자(대상, 국적 및 지역 제한), 발행 구조(발행 주체, 법적 성격, 기초자산 보관, 투자자 권리), 거래 구조(거래 방식, 유동성 확보 방안, 거래시간, 사용 블록체인), 주요 사례 |
| E 성과와 국내 관련 | 사업 성과 지표, 타깃 수요, 성공요인으로 회사나 제3자가 꼽은 것, 제약과 리스크(사고, 제재), 국내 관련 사업 동향(국내 제휴, 한국 주식 취급, 한국 투자자 이용 경로) |

- EXT-<회사>-AE: 주제 A와 E의 사이트 밖 자료(감독기관 등록부, 공시, 제재, 성과 지표, 국내 제휴 보도). 쓰는 곳 `work/<회사>_AE/`.
- EXT-<회사>-BCD: 주제 B, C, D의 사이트 밖 자료(공시, 실적 발표, 주주서한, 투자설명서, 언론, 인터뷰). 쓰는 곳 `work/<회사>_BCD/`.
- 위키의 `open-questions.md`가 나오면 그 항목을 해당 EXT 에이전트에 이어서 보낸다.
- 상장사(Robinhood, Coinbase, MOON ATS의 모회사)는 SEC 공시와 실적 발표 자료를 먼저 본다. 비상장사는 보도자료, 규제기관 제출 문서, 투자설명서, 약관, 경영진 인터뷰가 대신한다.

그 밖의 에이전트

| 에이전트 | 범위 |
|---|---|
| ATS-1 | 야간 거래 ATS 3곳의 운영사, 모회사, 거래시간, 대상 고객, 거래 규모, 점유율, 사고 이력, 국내 증권사 연결 현황. 운영사 사이트 부분은 `H/work/<ATS>`의 묶음을 읽어 notes로 남기고, 사이트 밖 자료(FINRA 통계, Form ATS-N, 보도)는 직접 찾음 |
| ATS-2 | SEC ATS 목록과 FINRA 거래 통계를 훑어 후보 추림 기준에 걸리는 곳을 올리고 선정 사유를 적음 |
| VID-1, VID-2 | 대상 회사 경영진과 규제 당국자의 발표, 인터뷰 영상. 9절 참조. 5-2절 "미룰 일" |

- 2a 밖의 각 에이전트는 자기 파일에만 쓴다: `work/<회사>_<주제>/facts.csv`, `sources.csv`, `terms.csv`, `relations.csv`, `notes.md`. 공용 파일을 직접 고치지 않는다.

### 3단계 (15분) 독립 검증

- 회사별 검증 에이전트 6개, 제도 1개, ATS 1개를 한 번에 띄운다.
- 검증 에이전트는 수집 에이전트의 메모를 보지 않는다. `facts.csv`의 각 줄을 받아 링크를 다시 열고, 근거 문장이 실제로 그 내용을 말하는지 대조해 검증 상태를 매긴다.
- 공식 사이트 사실은 메인 세션이 먼저 원문 근거 문장이 raw 파일에 있는지 스크립트로 대조해 넘긴다. 검증 에이전트는 raw 파일의 해당 절을 열어 뜻을 대조하고, raw에 없거나 바뀌었을 수 있는 값(종목 수, 수수료, 규모)만 링크를 다시 연다.
- 회사 사이트에만 근거가 있는 인가와 등록 사실은 감독기관 등록부를 열어 대조한다.
- 같은 사실에 출처가 다르게 말하면 `충돌`로 표기하고, 메인 세션이 1차 출처 기준으로 판정해 `kb/canon.md`에 적는다.
- 숫자, 날짜, 인가, 지분율, 법적 성격은 전수 대조한다. 나머지는 시간 안에서 가능한 만큼 대조하고, 대조하지 못한 줄은 `단일 출처`로 둔다.

### 4단계 (10분) 병합과 인계

- `work/`의 파일을 `db/`로 합친다(중복 제거, ID 부여). `work/<회사>_site/`도 포함한다.
- 회사별 본문 `companies/<회사>.md`를 7절의 틀과 8절 규칙대로 쓴다. 근거는 `db/`의 사실이고, 위키는 빠진 사실을 찾는 데만 쓴다.
- `handoff.md`를 쓴다: 한 일, 회사별 채움 상태, 남은 공백, 충돌과 판정, 접근 불가 링크, 다음에 팔 가치가 있는 주제, 사용량(`usage_log.md` 누적과 상한 대비).
- `handoff.md`의 회사별 채움 상태에 공식 사이트 표를 넣는다: 수집 쪽수, 정독 쪽수, 미열람 범위(구역, 쪽수, 사유), 외부 확인이 필요한 항목 수. 값은 각 회사의 audit 결과 `coverage.md`에서 가져온다. 읽지 않은 것을 읽은 것처럼 쓰지 않는다.
- 결과 폴더 전체를 `result.zip`으로 묶어 저장소에 함께 커밋하고 브랜치로 푸시한 뒤, 브랜치 이름과 zip 경로를 알린다. `result.zip`에서 `H/work/*/raw`, `H/work/*/files`, `H/work/*/packs`, `H/work/*/inventory.csv`는 뺀다(내부 작업용 원문, 용량). 이 파일들은 저장소에는 커밋해 둔다. 100MB를 넘는 파일은 gzip으로 묶어 커밋한다.

## 7. 회사별 본문의 틀

`companies/<회사>.md`는 아래 순서와 기호를 그대로 쓴다. 대분류는 `##`, 중분류는 `●`, 소분류는 `★`, 세부는 `①②③`. 칸 이름은 점검표다(8절). 해당이 없는 줄은 지운다. 하지 않는다는 사실 자체가 의미 있으면 사실로 적는다. 각 줄 끝에 근거 사실 ID를 `[F-...]`로 붙인다.

```
## 기업 개요
● 기본정보
  ★ 법인명 :
  ★ 소재지 :
  ★ 설립 시기 :
  ★ 상장 현황 :
● 지배구조
  ★ 모회사 :
  ★ 주요 주주 :
● 취득 라이선스 및 근거 법령
  ★ 미국 :
  ★ 미국 외 :

## 연혁 및 확장 경로
● 설립 목적
● 단계별 확장 경로
  ★ 1단계(기간) : 단계 성격
    ① 사건(시점, 내용)
● 토큰증권 사업 진출 배경
  ★ 출발 사업과의 관계 :
  ★ 진출 사유 :
● 향후 방향
  ★ 경영진 발표 원문 : (캡처 파일 경로, 문서명, 쪽)
  ★ 해석 :

## 사업 구조
● 상품 기초자산(상품별 제공 내용, 대상 고객, 제공 방식)
  ★ 전통증권 :
  ★ 토큰증권 :
  ★ 가상자산 :
  ★ 파생상품 및 기타 :
● 서비스 범위(개시 시기, 수행 법인)
  ★ 발행 :
  ★ 매매 체결 :
  ★ 청산 :
  ★ 결제 :
  ★ 수탁 및 권리 기록 :
  ★ 고객 접점 :
● 수익원

## 핵심 사업 상세
● 대상 사업 :
● 최종 투자자
  ★ 대상 :
  ★ 국적 및 지역 제한 :
● 발행 구조
  ★ 발행 주체 :
  ★ 법적 성격 :
  ★ 기초자산 보관 :
  ★ 투자자 권리 :
● 거래 구조
  ★ 거래 방식 :
  ★ 유동성 확보 방안 :
  ★ 거래시간 :
  ★ 사용 블록체인 :
● 주요 사례(해당 시) :
  ★ 제공 내용 :
  ★ 대상 고객 :
  ★ 제공 방식 :

## 성과 및 경쟁력
● 사업 성과
  ★ 지표(수치, 산정 기준, 기준일) :
● 타깃 수요
● 핵심 성공요인(KSF)
● 제약 및 리스크

## 국내 시장과의 차이
● 국내 관련 사업 동향
● 제도 비교
  ★ 쟁점 :
    ① 현지 제도 :
    ② 국내 제도 :
    ③ 국내 적용 시 결과 :
● 수요 비교
  ★ 비교 항목 :
    ① 현지 :
    ② 국내 :
    ③ 차이의 의미 :

## KDX 시사점
● 벤치마킹 요소
● 한계 및 유의사항
```

- 맨 위 요약(기업 정의, 조사 목적, 조사 내용, Summary)은 쓰지 않는다. 사용자가 직접 쓴다.
- "KDX 시사점"과 "핵심 성공요인"은 사실이 아니라 판단이다. 근거가 된 사실 ID를 반드시 붙이고, 근거 없이 쓰지 않는다.
- 제도 비교에는 그 회사 사업에 실제로 걸리는 쟁점만 쓴다. 모든 회사에 공통인 쟁점은 `kb/regulation_compare.md`에 둔다.
- ATS 회사는 "핵심 사업 상세"의 대상 사업을 그 ATS의 거래 사업으로 잡고, 발행 구조는 지운다.
- 이 틀의 원본은 `inputs/`의 기업별 틀 엑셀이다. 엑셀은 고치지 않는다.

## 8. 본문 작성 규칙

- 문어체 개조식, 명사형 종결. 구어체, 홍보성 표현, 슬로건 금지.
- 분량: 중분류(●)마다 3~4줄 이내. 한 줄은 40자 이내, 한 줄에 메시지 하나. 40자에는 줄 끝의 `[F-...]`와 이름 뒤 괄호 설명을 세지 않는다.
- 줄마다 연도, 이름, 숫자 중 하나를 넣는다. 위에서 아래로 읽으면 시간순이나 원인과 결과 순서가 되게 쓴다.
- 법인 전체 이름, 인가 기관명, 발표일 같은 세부는 본문에서 빼고 `db/facts.csv`에만 둔다. 본문에는 약칭과 연도(필요하면 연월)만 쓴다. 예외: 기본정보의 법인명 칸에는 정식 법인명을 한 번 적는다. 라이선스 칸에는 인가 종류와 근거 법령만 쓴다.
- 칸 이름은 점검표다. 칸 여러 개를 한 줄로 합쳐도 되고, 전할 말이 없는 칸은 지운다. 합친 칸은 `db/absent.csv`에 적지 않는다. 자료가 없어서 지운 칸과 필요 없어서 지운 칸은 3절 8번대로 적는다.
- 회사, 상품, 기관 이름이 파일에서 처음 나올 때 바로 이해되는 설명을 괄호로 붙인다. 예: Robinhood(미국 주식 거래 앱 운영사). 두 번째부터는 붙이지 않는다.
- 사례는 이름만 적지 않는다. 무엇을, 누구에게, 어떤 방식으로 제공하는지가 그 칸의 줄들 안에서 설명되어야 한다. 한 줄에 다 넣지 말고 줄을 나누고(3~4줄 안에서), 나머지 세부는 facts.csv에 둔다.
- 제목을 "A와 B"로 묶지 않는다. 소분류로 나눈다.
- "최초", "유일", "핵심" 같은 말은 근거가 받칠 때만 쓴다.
- 긴 줄표와 가운뎃점 기호를 쓰지 않는다.
- 경영진 발표 원문 칸의 근거 표기(캡처 파일 경로, 문서명, 쪽)는 40자 제한에서 뺀다.
- Securitize, tZERO에 대해 추가 확인이 필요한 줄은 줄 앞에 `[추가 확인]`을 붙인다.

## 9. 영상

- 대상 회사 경영진과 규제 당국자의 발표, 인터뷰 영상 링크를 찾는다. 회사 공식 채널과 주요 행사, 방송을 우선한다.
- 자막이나 스크립트를 긁어 `videos/<영상 ID>.txt`로 저장한다.
- 스크립트에서 위 틀의 항목을 받치는 발언 지점을 찾아 시각(분:초)을 적고, 그 시점의 화면을 `captures/`에 저장한다.
- `db/videos.csv` 열: 영상 ID, 제목, 채널, 출연자와 직함, 게시일, 링크, 시각, 캡처 파일, 발언 요지, 받치는 사실 ID.
- 영상 발언은 `경영진 발언` 출처로 취급한다. 숫자와 날짜는 문서 출처로 다시 확인한다.
- 영상 작업은 5-2절 "미룰 일"이다. 상한과 시간이 남을 때 haiku로 돌린다.

## 10. DB 구조

모두 UTF-8 CSV. 본문과 메모는 마크다운.

| 파일 | 열 |
|---|---|
| `db/facts.csv` | fact_id, 회사, 사업 법인, 법인 소재지, 시작(연월), 끝 또는 현재, 상태(운영 중, 발표, 계획, 중단), 자산 유형(전통증권, 토큰증권, 가상자산, 파생상품 및 기타), 밸류체인 위치(상품 공급, 체결, 청산, 결제, 기록, 고객 접점, 투자자), 세부 기능, 무엇을, 누구에게, 어떤 방식으로, 근거 인가, 관련 조문 ID, 값, 단위, 무엇을 잰 것, 기준일, 회사가 밝힌 이유, 앞선 fact_id, 틀 항목(7절의 어느 줄인지), source_id, 링크, 원문 근거 문장, 원문 위치, 검증 상태, 열람 일시 |
| `db/sources.csv` | source_id, 제목, 발행 주체, 발행일, 출처 종류, 언어, 링크, 저장 파일 경로, 캡처 파일, 접근 결과, 열람 일시 |
| `db/terms.csv` | 용어, 원어, 쉬운 뜻, 이 과제에서 중요한 이유, 헷갈리는 짝, 차이 한 줄, 한국의 대응 용어와 제도, source_id |
| `db/laws.csv` | law_id, 국가, 법령명, 조항, 시행일 또는 기준일, 원문 발췌, 쉬운 풀이, 관련 쟁점, 링크, 검증 상태 |
| `db/cases.csv` | case_id, 국가, 기관 또는 법원, 사건명, 시점, 종류, 당사자, 쟁점, 결론, 그 뒤 달라진 것, 관련 회사, 링크, 검증 상태 |
| `db/relations.csv` | 주체, 주체 유형, 대상, 대상 유형, 관계 종류(모회사와 자회사, 지분 투자, 인수와 합병, 사업 제휴, 발행과 유통 위탁, 상장과 자금 조달), 지분율, 금액, 시점, 상태, 회사가 밝힌 목적, source_id, 링크, 검증 상태 |
| `db/ats_screen.csv` | ATS명, 운영사, 모회사, 취급 자산, 대상 고객, 거래시간, 거래 방식, 거래 규모(기준 기간), 차별화 요소, 토큰증권 취급 현황, 선정 결과, 선정 사유, 링크 |
| `db/videos.csv` | 9절 참조 |
| `db/blocked_links.csv` | 4절 참조 |
| `db/absent.csv` | 회사, 항목, 구분(필요 없어 제외, 찾았으나 공개 자료 없음), 사유, 찾아본 곳 |
| `db/handover_questions.csv` | 대상(Securitize, tZERO), 추가로 볼 것, 질문이 나온 배경, 관련 fact_id |

- 밸류체인 위치와 자산 유형은 위 값만 쓴다. 웹 화면에서 연도별로 칸이 채워지는 지도를 그리는 데 쓰이므로 `시작(연월)`을 빠뜨리지 않는다.
- 공식 사이트 밖 원문은 `sources/`에 저장한다(HTML은 텍스트로, PDF는 원본). 공식 사이트 원문은 raw 파일이 대신하고, `저장 파일 경로`에 raw 경로를 적는다(5-1절). 공식 사이트 사실의 `원문 위치`는 raw 파일 경로와 절 제목, `열람 일시`는 raw의 `fetched`.
- 경영진 발표 자료의 해당 쪽은 `captures/`에 이미지로 저장한다.
- 8절에서 본문에서 뺀 세부는 리서치 뒤의 웹 화면이 줄을 눌렀을 때 보여 준다. 그래서 facts.csv에 빠짐없이 둔다: `사업 법인`에는 정식 법인명, `근거 인가`에는 인가 종류와 인가 기관을 함께 적고, 발표일은 그 사실의 source_id가 가리키는 sources.csv `발행일`에 둔다.

## 11. 서브에이전트에게 줄 지시의 공통 머리말

각 서브에이전트 지시문에 아래를 그대로 넣는다.

```
- 먼저 kb/ 폴더를 읽는다.
- 맡은 범위만 조사한다. 범위 밖 발견은 notes.md에 한 줄로 남긴다.
- 기억으로 쓰지 않는다. 이번에 연 링크로 확인한 것만 facts.csv에 넣는다.
- 한 줄에 사실 하나. 링크, 원문 근거 문장, 원문 위치, 열람 일시가 없으면 넣지 않는다.
- 1차 출처를 먼저 찾는다. 언론 기사를 봤으면 그 기사가 가리키는 원문을 찾아간다.
- 열지 못한 링크는 blocked_links.csv 형식으로 남긴다.
- 기초 지식에 더하거나 고칠 것은 kb/proposals/<이름>.md에 링크와 함께 적는다.
- 자기 폴더 work/<이름>/ 에만 쓴다.
- 끝나면 채운 항목, 못 채운 항목과 이유, 새로 나온 용어를 10줄 이내로 보고한다.
- 원문을 대화로 돌려보내지 않는다. 결과는 파일에 쓰고 보고는 10줄로 한다.
```

공식 사이트 읽기 에이전트(SITE, WIKI, ATS-1의 사이트 부분)에는 아래를 더한다.

```
- .claude/skills/company-site-wiki/SKILL.md의 5단계(읽기와 메모)와 6단계(위키)를 따른다.
- 맡은 묶음만 끝까지 읽는다. inventory.csv, raw/, packs/를 통째로 열지 않는다.
- 지시문 5-1절의 제외 범위(H/00_먼저읽기.md 5번)는 열지 않는다.
- 이 에이전트의 "자기 폴더"는 H/work/<회사>/notes/의 맡은 묶음 파일이다. WIKI 에이전트는 H/work/<회사>/wiki/와 work/<회사>_site/다.
- 사실 줄마다 원문 근거 문장, raw 위치, 틀 항목을 단다(5-1절 notes 형식).
- 회사 사이트가 밝힌 인가, 규모, 순위는 사실로 확정하지 않고 open-questions.md에 확인할 곳과 함께 올린다.
```

공식 사이트 밖 자료 에이전트(EXT)에는 아래를 더한다.

```
- 그 회사의 공식 사이트(H/work/<회사>의 범위)는 다시 열지 않는다. 사이트 내용이 필요하면 H/work/<회사>/notes/나 wiki/를 읽는다.
```

## 12. 이 대화 이전에 열람된 링크

아래는 출발점이다. 내용을 그대로 믿지 말고 다시 열어 확인한다. Payward 보도자료는 Kraken 소유 도메인 추가의 근거로도 쓴다(5-1절).

- SEC 주식 토큰 조건부 면제(2026-09-17): https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment
- SEC ATS 목록: https://www.sec.gov/foia/frequently-requested-documents/alternative-trading-system-ats-list
- SEC Form ATS-N 제출 현황: https://www.sec.gov/files/divisions/marketreg/form-ats-n-filings.htm
- Payward의 Backed 인수 발표: https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion
- Payward xStocks 1주년: https://www.payward.com/press-release/xstocks-one-year
- Payward와 GTN 제휴: https://www.payward.com/press-release/gtn-xstocks
- Payward와 런던증권거래소 제휴: https://payward.com/press-release/payward-lseg-tokenization-partnership
- Payward와 Nasdaq 제휴: https://www.payward.com/press-release/payward-partners-with-nasdaq
- Dinari 미국 투자자 대상 출시: https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses
- 카카오페이증권과 Dinari 협약: https://www.etoday.co.kr/news/view/2630410
- Ondo 예치 자산 10억달러 발표: https://www.tmcnet.com/usubmit/2026/05/11/10380498.htm
- Binance bStocks 출시: https://www.prnewswire.com/apac/news-releases/binance-exchange-launches-bstocks-tokenized-securities-11-backing-and-247-trading-302798969.html
- Binance bStocks 운용자산 10억달러: https://www.prnewswire.com/news-releases/binances-bstocks-become-the-fastest-tokenized-equity-product-to-surpass-1-billion-in-assets-under-management-302909927.html
- Robinhood Chain 가동 보도: https://theblock.co/news/business/2026-07-01-robinhood-chain-goes-live-mainnet-alongside-24-7-tokenized-stocks-lighter-perps-planned-crypto-agentic-trading-406918
- Bruce Markets와 메리츠증권 연결: https://www.prnewswire.com/apac/news-releases/meritz-securities-connects-to-bruce-markets-data-feed-for-us-equities-improving-market-data-for-korean-traders-302876583.html
- OTC Markets의 MOON ATS 출범: https://www.nasdaq.com/press-release/otc-markets-group-announces-launch-moon-ats-new-overnight-trading-platform-national
- Blue Ocean ATS 체결 취소(2024-08): https://www.marketsmedia.com/blue-ocean-ats-resumes-after-cancelling-trades
- 금융위 토큰증권 하위법규 입법예고(2026-10): https://www.fsc.go.kr/no010101/87838
- 금융위 토큰증권 정책 방향: https://www.fsc.go.kr/po010101/87650

Coinbase는 이전에 열람한 링크도, 수집해 둔 사이트 원자료도 없다. 공식 사이트는 5-1절대로 map부터 하고, 사이트 밖은 회사 투자자 정보 페이지와 SEC 공시에서 시작한다.

## 13. 입력 파일

`inputs/` 폴더에 사용자가 넣어 둔 파일을 먼저 읽는다.

- KDX 중장기전략 스토리라인: 사례가 어느 주장에 쓰이는지 확인하는 기준
- 기업별 틀 엑셀: 7절 틀의 원본
- 과거 해외 거래소 현황표, tZERO 정리본: 서술 깊이와 문체의 참고
- `KDX_사이트전수조사_인수인계.zip`: 공식 사이트 수집 스킬과 회사별 수집 결과(5-1절)
- `usage.md`(있으면): 시작 시점 주간 사용률과 이번 실행 상한(5-2절)

## 14. 완료 기준

- 회사 6곳과 ATS 후보의 본문에서 모든 줄에 사실 ID가 붙어 있고, 그 사실의 검증 상태가 `1차 출처 확인` 또는 `교차 확인`이다.
- 7절 틀의 각 줄이 채워졌거나, 다른 칸과 합쳐졌거나, 지운 이유가 `db/absent.csv`에 있다.
- 본문이 8절 분량 규칙(중분류 3~4줄, 한 줄 40자, 한 줄 메시지 하나)을 지킨다.
- 본문에 쓴 용어가 모두 `db/terms.csv`에 있다.
- `kb/regulation_compare.md`의 쟁점마다 한미 양쪽 근거 조문 링크가 있다.
- ATS 후보 선정 결과와 사유가 `db/ats_screen.csv`에 있다.
- 공식 사이트를 다룬 회사마다 audit을 돌린 `coverage.md`가 있고, "정독했으나 위키에 안 쓰인 페이지"는 위키에 반영되었거나 사유가 적혀 있다. 미열람 범위가 handoff.md 표에 있다.
- 사용량이 5-2절 상한 안이고, `usage_log.md`에 회사별 예상량과 누적이 있다. 상한에 걸려 멈췄으면 `usage_report.md`가 있다.
- 결과가 브랜치에 푸시되어 있고, `handoff.md`, 브랜치 이름, zip 경로를 보고했다.
