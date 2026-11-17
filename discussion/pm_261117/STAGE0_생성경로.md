# 사이트 내장 데이터가 만들어지는 경로 (0단계, 2026-11-17)

한 줄 요약: 원본 파일(사실 DB, 본문, 브리핑, 문서 화면, 표, 메모 답) → `web/build.py` → `web/index.html` 안의 `<script id="data">`(D) → 같은 파일의 화면 코드(`web/template.html`)가 그림.

## 1. 원본과 스크립트

| 화면 또는 데이터(D의 키) | 원본 | 만드는 스크립트 | 비고 |
|---|---|---|---|
| 사실 DB | `work/*/facts.csv`, `work/*/sources.csv` | `tools/merge_db.py` → `db/facts.csv`, `db/sources.csv`, `db/_fact_id_map.csv` | F 번호는 병합 때 부여. 작업 폴더 번호(예: M3KR-001)와 F 번호의 대응은 `_fact_id_map.csv` |
| 회사 본문(D.companies): 정체 카드, 개요, 범위, 발언, A~G, 차이, 판단 | `companies/<회사>_v4.md`(번호가 가장 큰 판), 전체 그림은 `kb/overview.md` | `web/build.py`의 `parse()`, `assign_ids()` | 줄 번호(kr-0390 등)는 `web/line_ids.json`에 고정. 같은 섹션 안에서 문장이 55% 이상 비슷하면 같은 번호를 유지 |
| 브리핑(D.briefs) | `briefs/<회사>.md`, `captures/` | `web/brief_data.py`(엑셀 내보내기 `tools/export_briefs_xlsx.py`의 정리 함수를 같이 씀) | 사진은 `web/brief_img/`로 줄여 게시 때 함께 올림 |
| 핵심(D.core) | `briefs/00_브리핑_핵심_261117.md` | `web/build.py`가 문자열 그대로 넣음 | 화면에서 세 줄과 번호 서사로 나눠 그림 |
| 회사별 전략(D.strat) | `briefs/00_전략_한눈에.md` | 같음 | |
| 거래소 3곳 비교(D.cmp3) | `briefs/KDX_가상자산거래소3곳_비교브리핑_261117.md` | 같음 | |
| 파트별 해외 사례(D.parts) | `briefs/KDX_스토리라인_파트별_해외사례_261117.md` | 같음 | |
| 질문과 답(D.qa) | `briefs/PM_질문과_짚을점_261117.md` | 같음 | |
| 표: 순위, 교차, 체크, 축, 인가, 관계, 제도, 사건 등(D.rank, cls, check, axis, perp, cross, ats, events, lic, rel, reg, tp_reg, common) | `db/*.csv`, `kb/*.csv`, `kb/*.md` | `web/build.py`의 `extra_data()` | 표 안의 근거 번호는 `evidence()`로 출처 링크를 붙임 |
| 메모 답(D.log) | `discussion/log.jsonl` | `web/build.py` | 화면에서 해당 줄 아래에 답을 보임 |
| 검색과 질문 창용 사실 목록(D.facts) | `db/facts.csv` | `web/build.py` | 번호, 회사, 무엇을(400자), 기준일, 링크 |
| 화면 코드 | `web/template.html` | `web/build.py`가 D를 끼워 `web/index.html`을 씀 | 게시: Artifact에 `web/index.html` |
| 엑셀 | 브리핑: `tools/export_briefs_xlsx.py` → `export/KDX_해외사례_브리핑.xlsx` / 본문: 화면의 "엑셀 받기" / 확정본 묶음: `web/export.py` → `export/handoff_to_chat.zip` | | |

## 2. 실행 순서
1. 새 사실: `flock /tmp/kdx_merge.lock python3 -I tools/merge_db.py .`
2. 본문 점검: `python3 tools/check_body.py companies/<회사>_v4.md`, 브리핑 점검: `python3 tools/check_story.py briefs/<회사>.md`
3. 화면 만들기: `flock /tmp/kdx_build.lock python3 web/build.py`
4. 현황표: `python3 tools/stage0_audit.py` → `work/STAGE0/`

## 3. 되돌리는 법
- 0단계 보존 시점은 커밋 `7201cd1`(브랜치 research/kdx-overseas-20261116, 원격에 올라가 있음). 로컬 태그 `stage0-261117`도 같은 커밋을 가리킴(원격으로 태그를 올리는 것은 연결이 끊겨 실패).
- 되돌리기: `git checkout 7201cd1 -- web db companies briefs kb tools discussion axes.md` 뒤 `python3 web/build.py`
