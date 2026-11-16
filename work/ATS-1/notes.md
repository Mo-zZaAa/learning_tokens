운영사 도메인: blueocean-tech.io (Blue Ocean, blueoceanats.com이 여기로 리다이렉트), brucemarkets.com (Bruce), otcmarkets.com (MOON, OTC Markets Group)

# ATS-1 notes (기준일 2026-11-16)

## 채운 것
- 3사 운영사, 모회사, 출범, 거래시간, 한국 증권사 연결, 사고, 토큰증권, FINRA 거래 통계를 facts.csv 45줄로 정리.
- FINRA 통계는 otctransparency 화면 대신 FINRA 공개 API(api.finra.org, weeklySummary, summaryTypeCode ATS_W_FIRM)를 셸로 받음. MPID: BLUE BOATS, BOSS(Bruce), MOON. 응답 원본은 sources/ATS-1/finra_ats_firm_2026.json. 주 시작일 기준 13주 합산(Q2는 03-30~06-22, Q3는 07-06~09-28)이며 분기 경계를 정확히 자른 값이 아니다.
- 점유율은 야간 3사 합계 대비 거래대금 비중으로 직접 계산(공개 자료의 계산값 아님).

## 충돌과 주의
- Bruce 자사 발표 Q2 체결 $49.03B(1.16B주), 3사 합계 $391.2B(11.14B주)는 FINRA 합산 $39.4B, $319.1B(9.5B주)와 다르다. 집계 범위가 다를 수 있으나 이유 미확인. 둘 다 적고 FINRA는 1차, Bruce는 회사 발표로 구분.
- Bruce 자사 9월 점유율 20.77%(거래대금)는 FINRA 2026-09-07~10-19 6주 계산 21.9%와 비슷하다.
- 거래시간: Bruce는 2025-06 일~목, 홈페이지는 8pm~4am ET만 적음(2026-09-29 주말 확대 계획). 요일은 현재 확인 필요.
- 한국 증권사 연결: Bruce는 메리츠(2026-09-14), 토스(2026-10-01)가 시세 피드 연결이며 주문 연결이 아님. 한국 증권사가 백업으로 Bruce, MOON과 복수 계약했다는 보도(2025-08~11)는 있으나 증권사별 계약은 못 찾음. NH투자증권은 Bruce 투자자(2025-06 라운드).
- MOON 운영 법인: OTC Link LLC는 보도자료가 OTC Link ATS, ECN, NQB를 운영한다고 적은 법인이다. MOON이 이 법인 소속이라고 명시한 문장은 못 찾음(FINRA BrokerCheck 미열람).
- 2026-10-21 Blue Ocean 전산장애(시세 중단, 주문 정상)는 검색 요약에만 나오고 원문을 열지 못해 facts에 넣지 않음.

## 범위 밖 한 줄
- Blue Ocean의 MEMX 기술 이전 계획(2024)과 2026-09 Fair Access 종목 중단은 Nasdaq 기반 Bruce와의 경쟁 구도 설명에 쓸 수 있음.
- Robinhood는 2024-08 Blue Ocean 이용 중 야간 거래를 중단했고 2025-06, 2026-09 Bruce에 투자함(S02, S05, S06).
