# EXT(공식 사이트 밖 자료) 에이전트 공통 지시

- 먼저 AGENT_GUIDE.md(공통 머리말, CSV 형식)를 읽고 kb/를 훑는다(regulation_us.md, regulation_kr.md, cases.md).
- 맡은 회사의 7절 틀(INSTRUCTIONS.md 7절) 주제 A~E(INSTRUCTIONS.md 6절 2b 표) 가운데 공식 사이트 밖 자료로 채울 수 있는 것을 찾는다. 공식 사이트(회사 도메인)는 다른 담당이 스크립트로 읽으니 열지 않는다. 단, 회사 보도자료가 뉴스와이어(prnewswire, businesswire, globenewswire)에 실린 것은 열어도 된다.
- 우선순위: 1) 인가와 등록(감독기관 등록부: FINRA BrokerCheck, 주 감독기관, 각국 감독기관 등록부: FCA, CySEC, BaFin, DFSA, VARA, FSA 등) 2) 지배구조, 주요 주주, 인수와 제휴(금액, 지분율, 시점) 3) 성과 지표(무엇을 잰 것, 기준일) 4) 제재와 사고 5) 경영진이 밝힌 진출 사유와 향후 방향(실적 발표, 주주서한, 인터뷰 원문) 6) 한국 관련(국내 제휴, 한국 주식 취급, 한국 투자자 이용 경로).
- 열기: 셸 curl(-sL, 기본 UA)로 받아 sources/<에이전트 이름>/에 텍스트로 저장하고 근거로 쓴다. WebFetch는 대부분 DNS로 막혀 있다. www.sec.gov는 막혀 있다(UA 바꾸기 금지). SEC 문서는 federalregister.gov, govinfo.gov로 찾는다. 봇 차단(403, 확인 화면) 사이트는 우회하지 않고 blocked_links.csv에 남긴다.
- 언론만 있는 사실은 서로 다른 2곳 이상을 열어 일치할 때 교차 확인. 1곳이면 단일 출처.
- 쓰는 곳: work/<에이전트 이름>/ 의 facts.csv, sources.csv, terms.csv, relations.csv, notes.md, blocked_links.csv, absent.csv(찾았으나 공개 자료 없음). Securitize, tZERO 관련 확인 거리는 handover_questions.csv. 제도 발견은 kb/proposals/<에이전트 이름>.md.
- 시간 상한 20분. 사실 40~80줄이면 충분하다. 끝나면 10줄 보고(채운 틀 항목, 못 채운 것과 이유, 막힌 출처).
