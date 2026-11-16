# 웹 검토 화면

- 만들기: `python3 web/build.py` → `web/index.html`(한 파일, 서버나 외부 주소 없이 열림). 게시 주소: https://claude.ai/artifact/QnuzMo25ig3Qw9K7ACgFuJ (같은 파일로 다시 게시하면 주소 유지)
- 읽는 것: `companies/<회사>_vN.md` 중 가장 높은 N, `captures/`, `db/`(facts, sources, laws, cases, terms, cross, cross_ats, ats_events, relations), `work/LICMAP/licenses_check.csv`(인가 지도와 등록부 대조), `inputs/license_map/`(relations, acquisitions), `kb/regulation_compare.md`, `discussion/log.jsonl`
- 줄 ID: `web/line_ids.json`에 고정. 다시 만들어도 같은 줄(같은 대분류, 같거나 비슷한 문구)은 같은 ID. 화면 번호(예: Kraken B-3)는 표시용으로 매번 다시 매김.
- 화면 탭: 본문(1배치, 메모와 챌린지), 가로 비교(2배치), 인가와 관계(3배치), 제도와 용어(4배치), 메모.
- 사용자 메모: 브라우저 저장. "메모 보내기"로 글 복사 또는 json 저장. 받은 json은 `discussion/inbox/<시각>.json`에 둔다.

## 메모를 받았을 때(메인 세션이 할 일)
1. 메모마다 쉬운 말로 답(새 사실은 링크와 근거 문장 규칙).
2. 본문, DB, 용어를 고친다. 사용자가 직접 고친 문구, 확정한 줄은 `web/locks.json`에 `{줄 ID: {"text": 문구, "confirmed": true}}`로 넣어 덮어쓰지 않는다.
3. `discussion/log.jsonl`에 한 줄: `{"time","company","company_slug","line_id","disp","memo_id","type","question","answer","changes":[{"where","before","after"}],"status":"답함|합의|보류"}`
4. `python3 web/build.py` 후 같은 파일로 다시 게시. 화면에서 그 줄 아래에 질문, 답, 고친 내용(이전 → 새)이 보이고 사용자는 "합의" 또는 "다시 챌린지"를 누른다.

## 내보내기(5배치)
`python3 web/export.py` → `export/handoff_to_chat.zip`. `discussion/inbox/*.json`의 고침, 추가, 삭제, 순서, 확정, 주황을 시간 순서로 반영한 최종 줄 기준. 줄 순서 = 엑셀 행 순서.
