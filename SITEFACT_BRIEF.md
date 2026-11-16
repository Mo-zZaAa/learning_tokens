# SITEFACT(공식 사이트 notes를 위키와 DB 줄로 옮기는 담당) 지시

- 먼저 AGENT_GUIDE.md(CSV 형식)와 INSTRUCTIONS.md 7절(틀)을 읽는다. kb/는 훑기만.
- 입력: H/work/<회사>/notes/*.md 전부와, 있으면 H/work/<회사>/verify.md. H=/home/user/learning_tokens/KDX_사이트전수조사_인수인계. packs는 열지 않는다. raw는 근거 확인이 꼭 필요할 때 grep으로 해당 줄만.
- verify.md에서 "원문에서 못 찾은 근거"로 표시된 사실은 옮기지 않는다.
- 할 일 1: H/work/<회사>/wiki/ 에 SKILL.md 6단계 구조로 위키를 쓴다. 최소한 index.md, overview.md, products/<핵심 상품>.md, licenses.md, timeline.md, open-questions.md. 줄마다 `[출처](URL)`. 회사가 밝힌 인가, 규모, 순위는 open-questions.md에도 올린다.
- 할 일 2: 위키 사실을 work/SITE-<회사>/facts.csv, sources.csv, terms.csv, relations.csv로 옮긴다. 한 줄에 사실 하나.
  - 링크: 그 페이지 URL. 원문 근거 문장: notes의 근거 구절 그대로. 원문 위치: raw 파일 경로(H/work/<회사>/inventory.csv에서 grep -F "URL," 로 file 열). 열람 일시: raw 머리의 fetched(없으면 2026-11-16). 검증 상태: 회사 약관, 공시, 보도자료면 1차 출처 확인, 회사 홍보 문구이고 인가, 규모, 순위 주장이면 단일 출처.
  - 틀 항목과 시작(연월), 자산 유형, 밸류체인 위치를 가능한 한 채운다.
- 시간 상한 15분. 사실 60~120줄. 끝나면 5줄 보고(facts 수, 위키 파일, open-questions 수).
