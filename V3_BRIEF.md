# v3 본문용 근거 수집 공통 지시

- 먼저 AGENT_GUIDE.md를 읽는다. 기억으로 쓰지 않는다. 연 링크로 확인한 것만.
- 이미 DB에 있는 사실(db/facts.csv)은 다시 찾지 않는다. grep으로 먼저 확인한다.
- 셸 curl 기본 UA. www.sec.gov는 클라우드 접속이 막혀 있다(우회 금지). 봇 차단 사이트는 우회하지 않고 blocked_links.csv에 적는다.
- 화면 캡처는 Playwright(python3, 환경변수 PLAYWRIGHT_BROWSERS_PATH=/root/.pwb, chromium.launch()), 뷰포트 1440x900, deviceScaleFactor 2, PNG로 captures/에 저장. 로그인이 필요한 화면은 로그인하지 않고 공개된 화면만 찍는다(가입 화면은 첫 단계까지만, 개인정보 입력 안 함).
- 결과는 자기 폴더 work/<이름>/에 facts.csv(AGENT_GUIDE 형식, 틀 항목에 v3 대분류: 회사 개요와 확장 경로, A~G, 성과와 판단, 또는 ATS 틀 항목)와 지정된 표 파일로.
- 임시 파일은 /tmp/claude-0/-home-user-learning-tokens/278e97de-614f-5353-9c24-5d14e3110c37/scratchpad/<이름>/ 안에만.
- 끝나면 5줄 보고.

## 경영진 발언 표(quotes.csv) 머리줄
회사,발언자,직함,장소(행사나 매체),일시,링크,원문(영어 그대로),번역,해석(무엇이 클 것이고 그래서 무엇을 한다),캡처 파일,출처 종류,fact_id
- 발언은 "어디가 클 것이고 그래서 우리는 무엇을 한다"가 드러나는 것으로 고른다. 회사당 3건 이상.
- 캡처: 발언이 보이는 화면을 Playwright로 찍어 captures/quotes/<회사>_<번호>.png. 영상만 있으면 영상 페이지 화면과 시각.
- 출처가 회사 채널(블로그, 보도자료, 실적 발표 녹취, 공식 영상)이면 facts.csv 검증 상태 1차 출처 확인, 언론 인터뷰는 서로 다른 2곳이 일치할 때 교차 확인, 아니면 단일 출처.
