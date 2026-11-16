# US-2 제안: 미국 증권 인프라 사업자 등록과 토큰화 주식 거래 (기준일 2026-11-16)

## 1. 브로커딜러 등록
- 현행 제도: 남의 계산으로 증권 거래를 처리하거나(브로커) 자기 계산으로 업으로 사고팔면(딜러) SEC에 등록해야 한다. 등록 신청은 Form BD를 FINRA의 CRD로 낸다.
- 근거 조문: US-SEA-3a4, US-SEA-3a5, US-SEA-15a1, US-17CFR-240.15b1-1
- 링크: https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap2B-sec78o.htm , https://www.ecfr.gov/current/title-17/section-240.15b1-1

## 2. 명의개서대리인과 청산기관
- 현행 제도: 등록 증권의 발행과 이전을 기록하는 명의개서대리인, 대금과 증권 인도를 중개하는 청산기관(예탁기관 포함)은 각각 SEC 등록이 필요하다.
- 명의개서대리인은 한 달 일상 이전 건의 90% 이상을 3영업일 안에 처리해야 한다.
- 근거 조문: US-SEA-3a23, US-SEA-3a25, US-SEA-17A-b1, US-SEA-17A-c1, US-17CFR-240.17Ad-2
- 링크: https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap2B-sec78q-1.htm , https://www.ecfr.gov/current/title-17/section-240.17Ad-2

## 3. 거래소 등록과 거래소의 정의
- 현행 제도: 여러 매수자와 매도자의 주문을 모아 정해진 방식으로 체결하면 거래소로 본다(Rule 3b-16). 거래소는 전국증권거래소로 등록하거나 면제를 받아야 한다.
- 근거 조문: US-SEA-3a1, US-17CFR-240.3b-16, US-SEA-5, US-SEA-6a
- 링크: https://www.ecfr.gov/current/title-17/section-240.3b-16

## 4. ATS 규율 (Regulation ATS)
- 현행 제도: 거래소 기능을 하지만 회원 규칙 제정권과 징계권이 없는 시스템은 브로커딜러로 등록하고 Regulation ATS를 지키면 거래소 등록이 면제된다.
- 운영 20일 전 Form ATS 제출. NMS 주식을 다루면 Form ATS-N이 효력을 가져야 하고(SEC 120일 검토, 최대 90일 연장), ATS-N은 공개된다.
- 거래량 기준: 직전 6개월 중 4개월 이상 한 종목 거래량 5% 이상이면 호가 공표 의무와 공정접근 의무(서면 접근 기준, 부당한 거부 금지). 지방채와 회사채 20% 이상이면 시스템 안정성 의무.
- 근거 조문: US-17CFR-242.300, US-17CFR-240.3a1-1, US-17CFR-242.301-b1, US-17CFR-242.301-b2, US-17CFR-242.301-b3, US-17CFR-242.301-b5, US-17CFR-242.301-b6, US-17CFR-242.304
- 링크: https://www.ecfr.gov/current/title-17/section-242.301 , https://www.ecfr.gov/current/title-17/section-242.304

## 5. 특별목적 브로커딜러의 디지털자산 증권 수탁
- 현행 제도: SEC는 2020년 12월 성명(Release 34-90788)으로 디지털자산 증권만 다루는 등 조건을 지키는 브로커딜러를 5년 동안 집행조치하지 않겠다고 했다(2021-04-27 효력).
- 2019 FINRA 공동 직원 성명은 2025-05-15 철회, 2025-12-17 거래시장국 직원 성명이 브로커딜러의 암호자산 증권 수탁 고려 사항을 다룬다(2026-10 SEC 제안서 인용으로 확인).
- 5년 기한 이후 SPBD 성명의 갱신 또는 철회 여부는 아직 확인 못함(sec.gov 열람 필요).
- 근거: cases.csv US-2-C02, C03, C04
- 링크: https://www.govinfo.gov/content/pkg/FR-2021-02-26/html/2020-28847.htm , https://www.govinfo.gov/content/pkg/FR-2026-10-06/html/2026-20466.htm

## 6. 2026년 토큰화 NMS 주식 면제 명령 (Release 34-106402)
- 무엇: SEC가 2026-09-17 Exchange Act 36(a)(1)에 근거해 두 가지 한시 면제를 줬다. 기간 2026-09-17부터 2031-09-17까지 5년.
- 누가: (1) TSV(허가된 참가자에게 AMM 유동성풀을 제공하고 접근 기준을 정하는 자)는 거래소 정의에서 빠진다. 그래서 거래소 등록, ATS, Reg NMS가 적용되지 않는다. (2) 자기자본으로 유동성을 공급하는 Covered Firm은 딜러 등록을 면제받는다(고객 자산 보관 금지, 미등록 사실 공시).
- 대상: 발행회사 또는 제3자가 토큰화한 NMS 주식으로, 기초 주식과 같은 권리를 주는 것만. 상대 자산은 토큰화 주식, 비증권 가상자산(스테이블코인 등), 토큰화 MMF.
- 조건: 공개 퍼미션리스 원장의 감사 가능한 스마트컨트랙트, 운영자는 미국인, 운영 30일 전 공개 고지, 제3자 토큰화는 발행회사 고지 후 30일 대기와 이의 시 불가, 1차 발행 금지, 10분 내 거래자료 공개, 기초 주식 거래정지 시 동시 정지, 사고 통지.
- 상한: Tier 1(S&P 500, Russell 1000 등) 75종목, 종목별 전월 일평균 거래량의 0.25%. Tier 2는 250종목, 2.5%. 계열 TSV는 합산.
- 그대로 남는 것: 증권법 등록(공모), 사기 금지 조항(10(b), 10b-5), OFAC 제재. 의견 수렴 File No. 4-927.
- 근거 조문: US-SEA-36a1, US-SEA-3a1, US-SEA-3a5; cases.csv US-2-C01
- 링크: https://www.govinfo.gov/content/pkg/FR-2026-09-22/html/2026-19388.htm
