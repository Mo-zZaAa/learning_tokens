# 리서치 노하우 (실제로 통한 방법, 계속 갱신)

새 리서치를 시작할 때 먼저 읽는다. 리서치 담당은 끝날 때 playbook/knowhow_inbox/<담당>.md에 새 노하우를 적고, 메인 세션이 여기에 합친다(README.md 순서). 봇 차단이나 지역 제한을 우회하는 방법은 노하우가 아니다.

## 1. 클라우드 세션에서 막히는 곳과 실제로 통한 공식 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| www.sec.gov(403, 자동도구) | federalregister.gov, govinfo.gov 관보 사본. 사용자 로컬 브라우저 | SEC 릴리스, 승인 명령은 관보에 같은 문서 |
| coinbase.com, investor.coinbase.com(403) | 사용자 로컬 브라우저(About, IR). 주주서한 PDF는 사용자 업로드 | 미션, 설립, 상장 예정 발표 확인됨 |
| investors.robinhood.com(403) | GlobeNewswire 배포본의 MENAFN 사본, 사용자 로컬 브라우저 | 실적 보도자료 인용 캡처 |
| binance.com 공지(405, 봇 확인) | PR Newswire 배포본 사본(aap.com.au), 공지 목록 공개 API(제목만), 사용자 로컬 브라우저 | 공지 본문은 로컬로만 |
| justice.gov(봇 확인) | 사용자 로컬 브라우저(사면 목록 페이지) | 재무부 FinCEN, OFAC 문서는 열림 |
| NFA BASIC(403) | 사용자 로컬 브라우저 | "Formerly Known As"로 인수 경로가 드러남 |
| Business Wire(403) | 같은 문장을 실은 매체 3곳 교차(Bernama, Markets Media, Pulse2) | 원문 배포처가 PR Newswire가 아닐 수 있음 |
| WebFetch 도구(DNS 실패 다수) | curl로 직접 | |

- 막힌 항목이 여럿 쌓이면 LOCAL_BROWSER_TASK.md 형식으로 사용자 로컬 세션에 넘긴다. 18개 중 11개를 1차로 찾음(2026-11-17). 결과는 채팅 표와 캡처 zip으로 받아 work/LOCAL/에 넣는다.

## 2. 쓸모 있었던 1차 출처 위치
- FINRA BrokerCheck: 증권사 등록일(firmStatusDate), 옛 상호(otherNames). 지도 시점과 "등록 시점" 의미가 다를 수 있음.
- CFTC DCM, DCO 목록: 지정일. 인수 시점과 등록 시점을 구분.
- SEC EDGAR: 명의개서대리인 TA-1은 본사 CIK가 아니라 별도 주체 "<회사>/TA" CIK로 접수될 수 있음(Dinari, Inc/TA).
- 리히텐슈타인 FMA 승인 투자설명서 목록 PDF: 승인일, 유효기간, 보충서 날짜. 목록 작성일 이후 건은 없음.
- 투자설명서(Backed, RHJ, BTech, Coinbase SPV): 법적 성격, 담보, 보관처, 발행사 존속 의존, 채무자 교체, 해지 조항.
- rwa.xyz: 토큰화 주식 플랫폼 표(같은 날 순위와 잔액). 과거 값은 제3자 글에 실린 표(Sentora 2026-01)로.
- Hyperliquid 공식 API(api.hyperliquid.xyz/info): 주식 무기한선물 미결제약정, 24시간 거래대금.
- 회사 약관 PDF: 법인 옛 이름과 인가 범위(Binance ADGM 약관). 파일 정보에 Draft 표시가 있으면 적는다.

## 3. 도구
- tools/pdf_quote.py: PDF 한 쪽에서 인용 문장만 잘라 캡처(두 단 편집은 실패할 수 있음).
- tools/find_line.py: 본문 줄 ID 찾기(링크 {xx-0000}용).
- tools/merge_db.py: 여러 담당이 동시에 쓰면 반드시 `flock /tmp/kdx_merge.lock`으로. 판정 파일은 work/MANUAL/verdicts.csv가 마지막에 이김(그 앞은 VER-* 이름순).
- tools/check_body.py: 근거 규칙 점검.
- tools/compile_axis.py: 확장 축 표.

## 4. 함정
- CSV 머리에 BOM이 있으면 열 이름이 깨짐(utf-8-sig로 읽기). 따옴표 머리는 csv.reader로.
- 검색 요약, AI 요약에 있는 날짜와 숫자는 원문에서 다시 확인(예: "2026-05 승인"은 실제로는 제출 즉시 효력).
- 언론이 쓴 숫자와 1차 숫자가 엇갈리면(예: 18개 종목 대 4종) 둘 다 출처와 함께 적고 섞지 않는다.
- 회사가 "첫"이라고 말한 것은 회사 주장으로. 투자사 게시글의 문구는 회사 문구가 아님.
- 제3자 보고서 수치는 집계 기준(중앙화 거래소만 등)과 의뢰처를 붙인다.
