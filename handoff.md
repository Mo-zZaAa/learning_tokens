# KDX 해외 사례 리서치 인계 (백데이터 입구, 2026-11-20)

이 파일 하나로 "무엇이 어디 있고, 무엇을 믿고, 어떻게 꺼내 쓰고, 어떻게 이어서 고치나"를 알 수 있게 씀. 예전 인계(2026-11-16)는 handoff_261116.md.

---

## 0. 30초 요약

- **무엇을 조사했나**
  - 해외 6개사: Robinhood, Kraken(모회사 Payward), Binance, Coinbase, Dinari, Ondo
  - 미국 야간 ATS 3곳: Blue Ocean, Bruce, MOON
  - 제도: 미국, 한국, EU, 걸프 등
  - 주제: 사업 구조, 상품, 매출, 인가 획득(직접 대 인수), 주식 토큰
- **언제:** 2026-11-16 ~ 2026-11-20
- **어디에:**
  - GitHub: Mo-zZaAa/learning_tokens, 브랜치 `research/kdx-overseas-20261116`(커밋 300개 넘음)
  - 크기: 약 1.3GB, 대부분 원문 저장본
- **처음 열 것**

| 누가 | 순서 |
|---|---|
| 사람 | 1) `deliverables/KDX_백데이터_261120.xlsx`(DB 전부와 자료 목록을 한 엑셀로) 2) 화면 https://claude.ai/artifact/QnuzMo25ig3Qw9K7ACgFuJ 3) `deliverables/`의 A4 docx와 정리 md |
| 다른 Claude 세션 | 1) 이 파일 2) `CLAUDE.md` 3) `playbook/writing_rules.md`, `playbook/research_knowhow.md` 4) `catalog.csv` 5) `tools/fsearch.py`로 사실 찾기 |

---

## 1. 층 구조: 원문 → 사실 DB → 정리본 → 화면과 납품

| 층 | 어디 | 규모(2026-11-20) | 믿는 정도 |
|---|---|---|---|
| 1. 원문 | `sources/`(작업별 원문 2,500여 파일), `KDX_사이트전수조사_인수인계/`(공식 사이트 전수 수집), `work/*/raw`, `captures/`(캡처), `inputs/`(사용자 제공) | 원문 사본 약 1GB | 원문 그대로 |
| 2. 사실 DB | `db/`(사실 2,773, 출처 1,474, 인가 30, 관계 116, 법령 88, 사건 18, 용어 179 등). 원천은 `work/<작업 ID>/` | 사실마다 날짜, 원문 문장, 링크, 검증 상태 | 검증 상태 칸을 봄(`db/README.md`) |
| 3. 정리본 | `companies/*_v4.md`(회사 본문), `kb/`(카드, 해설, 매출, 사건, 구조 표, 인가 딥다이브, 제도) | 회사별, 주제별 | 숫자는 DB 번호로 거슬러 갈 수 있음 |
| 4. 화면과 납품 | `web/v5/`(화면 원본), Artifact(아래 3절), `deliverables/`(docx, md, xlsx, zip) | | 3층을 보기 좋게 묶은 것 |

자료 덩어리마다 종류, 내용, 언제 쓰나, 크기, 마지막 커밋일은 `catalog.csv`(엑셀 "자료 목록" 시트와 같음).

---

## 2. 백데이터로 꺼내 쓰는 법(상황별)

| 하고 싶은 것 | 어디서 | 방법 |
|---|---|---|
| 숫자나 날짜 하나를 인용 | `db/facts.csv` | `python3 -I tools/fsearch.py "Bitstamp&인가"` → fact_id, 기준일, 검증 상태, 링크를 같이 적음 |
| 원문을 다시 확인 | `db/sources.csv` → `sources/` | `python3 -I tools/fsearch.py --src "Deribit"` → 저장 파일 경로가 있으면 저장소 안 사본, 없으면 링크 |
| 회사 한 곳을 처음부터 이해 | `kb/easy/<회사>.md`(쉬운 해설), `kb/<회사>_overview/`(카드), `companies/<회사>_v4.md`(본문) | 해설 → 카드 → 본문 순 |
| 매출과 사업 모델 | `kb/revenue/<회사>.md`, `deliverables/매출로본성공원인_4개사_261118.md` | 해마다 구성, 등락 이유, 왜 이 회사에서 됐나 |
| 인가: 직접 대 인수, 시점, 목적 | `kb/licdeep/01_틀에맞춘답.md`, 회사별 카드, `00_평행연표.md`, `00_발언모음.md` | 사용자 틀에 맞춘 답과 근거 |
| 인가: 회사별로 무엇을 하려고, 어떻게 얻어, 어디에 썼나 | `kb/licdeep/04_회사별_인가표.md`, `deliverables/회사별_인가표_261122.xlsx`, 30초 인가 스토리 `kb/licdeep/05_30초_인가스토리.md` | 인가를 나란히 놓지 않고 회사별로 줄 세움. 다시 만들기: `python3 -I kb/licdeep/build_04.py` |
| 회사 연혁과 사건 | `kb/events/<회사>_events_src.py`(사건 카드 원본), `kb/structs/<회사>/timeline.csv` | |
| 한 장 요약 | `deliverables/KDX_A4_*.docx`, `deliverables/4개사_불렛과근거_261119.md` | 불렛과 줄별 근거 |
| 제도 | `kb/regulation_us.md`, `regulation_kr.md`, `regulation_compare.md`, `kb/licdeep/external.md`(나라별 제도 표) | |
| 사람에게 넘김 | `deliverables/KDX_백데이터_261120.xlsx`, docx, 화면 링크 | 엑셀 "읽는 법" 시트부터 |
| 다른 Claude 채팅에서 백데이터로 | Claude 프로젝트 지식에 엑셀, `handoff.md`, `kb/licdeep/01_틀에맞춘답.md`, 필요한 회사 md를 올림 | 사실은 fact_id로 인용하라고 지시 |
| 다른 Claude Code 세션에 맡김 | 이 저장소와 브랜치를 붙여 시작 | 아래 시작 문구 |

다른 Claude Code 세션 시작 문구(붙여 넣기용)

> 저장소 learning_tokens, 브랜치 research/kdx-overseas-20261116. handoff.md, CLAUDE.md, playbook/writing_rules.md, playbook/research_knowhow.md를 먼저 읽어. 사실은 db/facts.csv에서 tools/fsearch.py로 찾고 fact_id와 링크로 인용해. 새 사실은 work/<작업 ID>/facts.csv에 넣고 tools/merge_db.py로 병합해. 할 일: (여기에 적기)

---

## 3. 화면(Artifact)

| 화면 | 링크 | 마지막 갱신 | 원본 |
|---|---|---|---|
| KDX 해외 사례(본 화면, 회사별 4층: 카드, 매출로 본 원인, 쉬운 해설, 개요 문서) | https://claude.ai/artifact/QnuzMo25ig3Qw9K7ACgFuJ | 2026-11-18(57판) | `web/v5/build.py` → `web/v5/index.html`, 덧붙인 파일 `web/v5/ondo_deep.html` |
| 해외 사례 9곳 전체 그림 | https://claude.ai/artifact/YQd7eFkjTPSBbWa1QZC6oD | 2026-11-16 | |
| KDX 미국 6개사 개요 | https://claude.ai/artifact/AxJGYFzxm3cKFrFkCGbpGX | 2026-11-17 | |
| Kraken PM 질의 전량과 리서치 답(261118) | https://claude.ai/artifact/LGbbj6AgKBvoJcAs24qY9o | 2026-11-18 | `inputs/pm_261118/` |
| 주식 토큰 인가 지도 | https://claude.ai/artifact/BUnC7V4PNMEodsPef3vQAo | 2026-11-16 | `inputs/license_map/` |
| 미국 주식 토큰 조사 틀과 관계도 | https://claude.ai/artifact/74wczjJKoCALNHbJpA6hra | 2026-11-16 | |

- 본 화면의 메모(사용자 피드백 149건)는 화면 DB에 있음
  - 2026-11-20 저장소로 내보냄: `discussion/site_db_export_261120/memos/*.json`, 표는 `memos.csv`
  - 화면 안 "고치기"로 바꾼 칸(edits 모음)은 0건이었음
- 화면 다시 게시: `python3 web/v5/build.py` 뒤 Artifact 게시
  - 원본: `web/v5/index.html`
  - 파일: `{"ondo_deep.html": "web/v5/ondo_deep.html"}`
  - 권한: sample, db, downloads를 유지

---

## 4. 납품물(`deliverables/`)

| 파일 | 내용 |
|---|---|
| KDX_백데이터_261120.xlsx | 읽는 법, 자료 목록, DB 표 전부, 인가 딥다이브 연표, 화면 메모 |
| KDX_회사별A4_4개사_261118.docx, KDX_A4_<회사>_261118.docx | A4 긴 판(지침 v2.1 양식) |
| KDX_A4_간결_<회사>_261118.docx | A4 간결 판(사용자 Robinhood A4 모양) |
| 매출로본성공원인_4개사_261118.md | 4개사 매출 구성과 원인(출처 뺀 판) |
| <회사>_내글다듬기_261119.md, 4개사_불렛과근거_261119.md | 사용자 글에 사실 채움, 짧은 불렛과 줄별 근거 |
| 인가획득딥다이브_261120.zip | `kb/licdeep/` 전체 묶음 |

예전 납품(2026-11-17 전후)은 `export/`(브리핑 엑셀, 최종본 묶음).

---

## 5. 지킬 규칙(요약, 전체는 playbook)

- 확인된 것만, 링크 필수. 핵심(법적 구조, 인가, 핵심 수치)은 1차 자료. 매체는 이름을 밝힘
- (판단) 해석, (계산) 공개 숫자로 셈, (회사 주장), (보도, 매체명)을 붙임
- 가운뎃점과 긴 줄표를 쓰지 않음. 금지어(제공, 지원, 확대, 강화, 통합, 연결 등)
- 화면과 글에 PM 언급, 사람 이름, "배울 점" 절을 두지 않음
- 판매자 원칙: 남이 파는 것을 그 회사가 파는 것처럼 쓰지 않음(누가 누구에게 파나)
- 사용자 글을 다듬을 때: 말투는 두고 짧은 불렛과 줄별 근거를 짝으로(lessons_log L37, L38)

---

## 6. 갱신하는 법

1. **새 사실:** `work/<작업 ID>/facts.csv`, `sources.csv`를 만들고 `flock /tmp/kdx_merge.lock python3 -I tools/merge_db.py .`로 병합
2. **DB 줄 고치기:** `db/_fact_id_map.csv`로 원천 줄을 찾아 원천도 같이 고침. 병합하면 DB를 원천에서 다시 만들기 때문
3. **백데이터 다시 만들기:** `python3 -I tools/build_backdata.py <YYMMDD>`. catalog.csv, 엑셀, 메모 표를 다시 만듦
4. **인가 딥다이브 합치기:** `python3 -I kb/licdeep/merge.py`. 평행 연표, 발언 모음, 가설 표, 빈칸 목록을 다시 만듦
5. **원문 저장:** 세션 임시 폴더(/tmp 아래 scratchpad)는 세션이 끝나면 사라짐. 받은 원문은 `sources/<작업 ID>/`에 넣고 sources.csv의 저장 파일 경로를 채움
6. **커밋:** 단계마다 커밋하고 `git push -u origin research/kdx-overseas-20261116`

---

## 7. 알려진 한계와 열린 판단

- **막힌 출처:** `db/blocked_links.csv` 123건. 자주 막히는 곳은 sec.gov, cftc.gov, investors.robinhood.com, coinbase.com 블로그, theblock.co, coindesk.com. 통한 우회 경로(공식 사본, 등록부 API)는 `playbook/research_knowhow.md` 1절, 14절, 16절
- **DB 결함:** `db/README.md` 끝 "알려진 결함"
- **사용자 결정을 기다리는 사실 충돌**
  - Coinbase 날짜 4건(FCM 2023-08-15 대 16, 미국 무기한선물 시작 시기 등)
  - Kraken 장외 데스크 시작(2018-09 대 2016), EU xStocks 시작일
  - xStocks 수수료 상한(5% 대 0.5%)
  - Robinhood 예측시장 시작(2024-10 선거 계약 대 2025-03 허브)
  - 환율 1,380 대 1,430
- **빈칸:** 인가 딥다이브 빈칸 142개(`kb/licdeep/00_빈칸목록.md`), 회사별 빈칸은 `kb/gaps.csv`, `db/absent.csv`
- **시장 거래대금:** 한 집계기관(CoinDesk Data) 분기 값은 2023-Q2부터만 있음

---

## 8. 다음 할 일 후보(사용자 확인 전, 시작하지 않음)

- Robinhood와 Coinbase 분기 IR과 실적 통화 녹취 전량 읽기
- 간결 A4를 한 장으로 줄이기
- 인가 딥다이브 빈칸 중 답을 바꿀 수 있는 것 보강(01_틀에맞춘답.md 3절)
- 브랜치를 main에 합치거나 태그를 달아 보존(사용자 결정)
