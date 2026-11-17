# PILLARS-A 노하우(전략 틀 원문 찾기, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| binance.com 블로그, About, Mission(curl 405, 봇 확인) | Playwright 기본 Chromium(UA 그대로)으로 열림. 응답 202 뒤 본문 렌더 | 위장 없이 열린 것. 블로그 From our CEO 목록 /en/blog/from-our-ceo |
| investors.robinhood.com 보도자료와 static-files(403) | investingnews.com/robinhood-reports-<분기>-results/ (GlobeNewswire 전재, Playwright 캡처 가능). 2025 Q1, Q2는 404 | finviz, globenewswire.com은 Playwright에서도 403 |
| Robinhood 실적 통화 녹취(IR 403, marketbeat, roic.ai 403) | bullfincher.io/companies/robinhood-markets/earnings-call/fy2023-q4 형식(제3자 녹취, 단일 출처) | insidermonkey는 유료 벽에 잘림 |
| Coinbase 과거 주주서한(sec.gov 403) | IR CDN 이름 규칙이 해마다 다름: 2024/q4/Q4-24-Shareholder-Letter.pdf, 2025/q2/Q2-2025-Shareholder-Letter.pdf, 2025/q4/coin-20260212.pdf. 2023 Q4는 못 찾아 Markets Media 전재로 | 실적 통화 녹취는 2022/q4/Coinbase-Q422-Earnings-Call-Transcript.pdf 형식 |
| web.archive.org(연결 끊김) | 없음 | 문장이 처음 걸린 날짜는 로컬 브라우저 과제 후보 |

## 찾는 순서
- 비상장사(Payward)는 분기 실적 글(payward.com/press-release/q<n>-<연>-financial-highlights)이 사실상 주주서한이다. sitemap.xml에 보도자료 전부가 있다.
- "처음 나온 시점"은 다음 분기 서한이 알려 줄 때가 많다(Payward Q3: "Last quarter we introduced four pillars", Coinbase Q4: "In 2025, we debuted our flywheel"). curl 텍스트 변환은 굵은 글씨 단락을 빠뜨릴 수 있어 Playwright innerText로 다시 확인한다.
- 실적 보도자료 표제가 우선순위 이름으로 바뀌는 시점과 CEO 통화에서 말한 시점이 다르다(Robinhood: 통화 2025-02, 보도자료 표제 2026-02). 둘을 나눠 적는다.

## 함정
- 번역 전재(htx.com 등)에만 있는 숫자는 회사 영문 원문에 없을 수 있다(Binance 준법 인력 1,280명).
- 같은 회사 사이트 안에서도 미션 문장이 페이지마다 다르다(Binance About과 Mission).
- 다른 담당(STORY-*)이 같은 서한에서 사실을 먼저 넣었을 수 있다. 쓰기 전에 db/facts.csv를 링크와 키워드로 검색해 겹치지 않게 한다.
