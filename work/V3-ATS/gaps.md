# V3-ATS 빈칸 (Blue Ocean, Bruce, MOON 본문 v3)

## 공통
- 1년 전 대비 거래 규모: FINRA 주간 요약(ATS_W_FIRM)의 2025 Q3 값이 facts.csv에 없음. 같은 출처, 같은 산정 기준(13주 거래대금, 야간 3사 대비)으로 2025 Q2, Q3 값을 뽑아야 함.
- 2026-10 최근 3주 값: Bruce(F-0031)만 있음. 같은 3주의 Blue Ocean, MOON 거래대금과 점유율이 없어 나란히 못 씀.
- 호가 방식: Blue Ocean, MOON 모두 검증된 사실 없음(Blue Ocean 가격시간 우선은 F-0019 단일 출처). Form ATS-N 공개본(주문 유형, 우선순위)에서 확인 필요. Bruce는 Nasdaq 기술, FIX 접속만 씀.
- 수수료와 경제성: 3사 모두 구독료, 체결 수수료 사실 없음. KDX 시사점의 해외 확장 세 질문 중 "경제성"을 못 채우고 역할만 씀.
- 모회사 설립 연도와 창업자: Blue Ocean Technologies, Bruce Markets Holdings, OTC Markets Group 모두 facts.csv에 없음.
- 한국 시장과의 차이: 국내 대체거래소(넥스트레이드)의 거래시간, 대상 투자자 사실이 facts.csv에 없어 한국 쪽은 법령 ID와 F-1005, F-1010만 씀.

## 경영진 발언 (단일 출처 문제)
- QUOTES-C 발언 fact F-1072~F-1079(Blue Ocean 5건, Bruce 3건)는 검증 상태가 "단일 출처"라 본문 규칙상 못 씀.
- Blue Ocean: 대신 1차 출처 확인 사실이 붙은 보도자료 발언 3건을 씀(F-0004 삼성증권 제휴, F-0003 도쿄증권거래소, F-0017 토큰화 발표). 이 셋의 캡처는 이번에 새로 찍음: captures/quotes/BlueOcean_6.png, _7.png, _8.png. 기존 BlueOcean_1~5.png(F-1072~F-1076)는 검증 승격 후 교체 후보. 특히 F-1073(한국 서울 사무소), F-1074(한국 거점)는 한국 관련이라 승격 가치 큼.
- Bruce: 발언 3건(F-1077~F-1079)의 원문이 같은 기사에서 나온 1차 출처 확인 또는 교차 확인 사실(F-0025, F-0033, F-0023)과 링크가 같고, 원문 문장이 sources/ATS-1/bruce_wknd.txt, toss_bruce.txt, bruce_mm.txt에 있음을 확인. 그래서 본문 근거는 F-0025, F-0033, F-0023으로 붙임. F-1077~F-1079 자체를 검증 승격하면 그 ID로 바꾸면 됨.
- MOON: F-1080~F-1082가 1차 출처 확인이라 그대로 씀.

## 캡처
- captures/BlueOcean/, captures/Bruce/, captures/quotes/BlueOcean_1~5, Bruce_1~3, MOON_1~3는 커밋 fb48116에서 지워져 있었음. 직전 커밋(fb48116^)에서 작업 트리로 되살림(커밋은 안 함).
- MOON 로고와 화면: index.csv의 기존 주소(otcmarkets.com/market-activity/moon)는 시간 초과와 404. https://www.otcmarkets.com/otc-link/moon-overnight 에서 새로 찍어 captures/MOON/home.png, logo.png(헤더와 제목 부분 잘라냄)로 두고 index.csv에 두 줄 추가.
- ATS는 가입, 종목 목록, 주문 화면이 없는 B2B 시장이라 홈(과 Bruce 회사 소개)만 씀. Blue Ocean info1, info2와 Bruce info1은 404 페이지라 안 씀.

## 사고 이력
- Blue Ocean 2024-08-05 체결 취소 시각과 원인(F-0006, F-0007), 국내 피해 6,300억원, 약 9만 계좌(F-0008), 한국 비중 65%(F-0010), 서울 사무소와 보상 정책(F-0010), 2026-09 공정접근 기준 18종목 거래 중단(F-0012) 모두 단일 출처라 본문에서 뺌. 금융당국 발표나 회사 공지로 교차 확인 필요.
- Bruce, MOON 자체 사고 이력: 사실 없음. 2026-09 Blue Ocean 종목 중단 때 삼성, 토스가 MOON, Bruce로 안내한 사실(F-0045)도 단일 출처.

## 회사별
- Bruce: 최대주주 PEAK6(F-0022), 자사 집계 Q2 490.3억 달러(F-0026, FINRA 집계 393.5억과 충돌), 9월 점유율 20.77%(F-0030)는 단일 출처 또는 충돌이라 뺌. 한국 증권사 중 Bruce와 주문 계약을 맺은 회사 이름이 없음(F-0035는 회사명 미확인).
- MOON: OTC Link LLC가 MOON 운영 법인이라는 등록부 확인이 없음(F-0249 메모). 2025 Q4 일평균 거래대금 200% 증가(F-0039)는 단일 출처. MOON 별도 매출 미공개. 한국 증권사 개별 계약사 이름 없음.
- Blue Ocean: 서울 사무소 개설(2025-01)은 F-0010 단일 출처라 못 씀.
