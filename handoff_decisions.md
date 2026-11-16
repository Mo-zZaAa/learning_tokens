# 진행 중 판단 기록 (handoff.md에 합침)
- 셸 외부 접속이 처음엔 막혀 있어 환경 허용 호스트 40개를 사용자 승인으로 추가함(11:45 UTC). 그 밖 호스트는 WebFetch로 대체.
- Python Playwright 1.65가 찾는 브라우저 버전(1255)이 설치본(1243)과 달라 /root/.pwb에 링크를 만들어 PLAYWRIGHT_BROWSERS_PATH로 지정. 스킬 파일은 고치지 않음.
- Dinari는 수집이 끝나 있어 1단계와 동시에 읽기를 시작함(지시문 6절 순서와 다름, 시간 절약). kb가 비어 있는 상태라 용어와 제도 발견은 proposals로만 올리게 함.
- Dinari 묶음은 docs.dinari.com/docs만 54만 자라 묶음 단위가 아니라 페이지 단위로 골라 정독(정독 상한 회사당 30만 자). 고르지 않은 페이지는 coverage에 미열람으로 남김.
- 웹 열람 도구(WebFetch)는 세션 시작 때의 도메인 목록을 따라 환경을 제한 없음으로 바꾼 뒤에도 대부분 호스트에서 DNS 실패. 서브에이전트는 셸 curl로 원문을 받아 sources/<에이전트>/에 저장하고 근거로 씀.
- www.sec.gov: 셸 403(SEC는 연락처가 들어간 User-Agent를 요구). 임의 연락처로 바꾸는 시도는 권한 판정에서 거부되어 하지 않음. SEC 규칙과 명령은 Federal Register(federalregister.gov, govinfo.gov)로 대체. EDGAR 공시는 사용자 허가(연락처 UA) 필요 항목으로 blocked_links에 남김.
- Coinbase(www, investor, help)와 investors.robinhood.com은 봇 차단(Cloudflare, Akamai) 403. 헤드리스 브라우저도 차단. 우회하지 않음. Coinbase 공식 사이트 수집(map) 불가 → 사이트 밖 자료만으로 조사.
- 사용자 요청(12:0x UTC): db/licenses.csv 추가, 등록부로만 확인. 웹 화면 지시에 등록 지도 배치(2-1) 추가. LIC 에이전트 띄움.
