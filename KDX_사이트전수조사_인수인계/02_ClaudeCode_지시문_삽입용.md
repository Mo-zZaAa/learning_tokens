# Claude Code 지시문에 넣을 부분: 공식 사이트 수집

아래 내용을 Claude Code 지시문의 "원자료 수집" 단계에 넣는다. 기업별 정리 틀과 산출물 형식은 기존 지시문을 그대로 따른다.

---

## 공식 사이트 수집은 인수인계 묶음을 사용

### 준비 (한 번만)

1. `KDX_사이트전수조사_인수인계.zip`을 작업 폴더에 푼다.
2. `KDX_사이트전수조사_인수인계/skill/company-site-wiki` 폴더를 `.claude/skills/company-site-wiki`로 복사한다.
3. 필요한 도구 설치: `pip install requests beautifulsoup4 lxml markdownify playwright "markitdown[pdf]"`. Chrome이 없는 컴퓨터면 `playwright install chromium`도 실행.
4. `python .claude/skills/company-site-wiki/scripts/sitewiki.py --help`가 도는지 확인.
5. `00_먼저읽기.md`와 `.claude/skills/company-site-wiki/SKILL.md`를 읽는다.

### 작업 방식

- 공식 사이트 조사는 SKILL.md의 절차(map > plan > fetch > digest > 읽기와 메모 > 위키 > audit)를 따른다. 검색과 낱장 열람으로 공식 사이트를 훑지 않는다.
- 회사별 작업 폴더는 `KDX_사이트전수조사_인수인계/work/<회사>`를 그대로 이어 쓴다. 새 회사는 같은 위치에 `work/<회사>`를 만든다.
- 공식 사이트 밖의 자료(감독기관 등록부, 공시, 보도)는 기존 지시문 방식대로 따로 찾는다. 위키의 open-questions.md에 모인 "외부 확인이 필요한 것"이 그 출발점이다.
- 회사별 위키(`work/<회사>/wiki`)는 원자료 정리본이다. 기업별틀 엑셀은 위키와 notes를 근거로 채우고, 칸마다 출처 URL을 남긴다.

### 다시 하지 않을 것

- Kraken 목록화(map): 끝났다. `work/kraken/inventory.csv`에 URL 약 21.7만 개와 계획이 들어 있다. map을 다시 돌리지 않는다.
- Kraken 읽기 계획: `work/kraken/overrides.json`에 제외와 우선순위가 들어 있다. `fetch`를 실행하면 그 계획대로 이어서 수집된다. 계획을 바꿀 때는 패턴을 추가하는 방식으로만 바꾼다.
- Dinari 수집(map, fetch, digest): 끝났다. `work/dinari/packs`의 묶음을 바로 읽으면 된다.
- Ondo 목록화(map): 끝났다. 수집 상태는 `00_먼저읽기.md` 표를 본다. 남은 것은 `fetch`만 이어서 실행.
- `00_먼저읽기.md`의 "더 볼 필요 없는 곳"에 적힌 구역은 열지 않는다. 기업별틀을 채우다가 꼭 필요해지면 해당 URL만 패턴으로 올린다.

### 토큰을 아끼는 규칙

- 수집(map, fetch, digest, audit)은 스크립트가 하므로 토큰이 거의 들지 않는다. 토큰은 묶음을 읽을 때 든다.
- `inventory.csv`, raw 폴더, packs 폴더를 통째로 열지 않는다. Kraken의 inventory.csv는 44MB다. 필요한 줄만 `grep`이나 짧은 파이썬으로 뽑아 본다. 현황은 `plan_summary.md`, `packs/_index.md`, `packs/_groups.md`, `coverage.md`로 본다.
- 읽기 전에 예상량을 먼저 계산한다. `packs/_index.md`의 글자수를 더해 4로 나누면 대략의 토큰 수다. 회사 하나를 읽기 전에 "읽을 묶음, 글자수 합계, 예상 토큰"을 한 번 보고한다.
- 주간 사용량의 50%를 넘길 것으로 보이면 읽기를 시작하지 말고 멈춘 뒤 사용자에게 보고한다. 보고 내용: 지금까지 읽은 양, 남은 묶음과 예상량, 줄일 수 있는 안(묶음 우선순위).
- 묶음은 조사 질문과 관련이 큰 것부터 읽고, 읽을 때마다 notes를 남긴다. 같은 원문을 두 번 읽지 않는다.
- 글 묶음(블로그, 고객센터, 약관)은 먼저 URL과 제목을 핵심어로 걸러 관련 글만 읽는다.
- 서브에이전트로 나눌 때는 회사나 호스트 단위로 나누고, 각 서브에이전트는 notes 파일만 돌려준다. 원문을 대화로 돌려보내지 않는다.

### 끝낼 때

- 회사마다 `audit`을 실행해 `coverage.md`를 남긴다. 안 읽은 범위(구역, 쪽수, 사유)를 그대로 적는다. 읽지 않은 것을 읽은 것처럼 쓰지 않는다.
- 회사별로 수집 쪽수, 정독 쪽수, 미열람 범위, 외부 확인이 필요한 항목 수를 한 표로 보고한다.
