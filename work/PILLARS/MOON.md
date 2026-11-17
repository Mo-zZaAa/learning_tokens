# MOON ATS(OTC Markets Group) 공식 전략 틀

조사일 2026-11-17. OTC Markets Group(OTCQX: OTCM)은 SEC 등록 공시 회사가 아니어서 10-K가 없고, 연차보고서는 회사 사이트(otcmarkets.com)에만 있다. 이 세션에서 otcmarkets.com은 열리지 않았다(아래 5절). 그래서 GlobeNewswire와 PR Newswire 배포 실적 발표 사본, blog.otcmarkets.com을 썼다. F 번호는 db/facts.csv(이번 병합 F-1694~F-1700, 기존 번호는 그대로 인용).

## 1. 틀 이름과 요약
| 틀 | 원문 | 처음 나온 곳, 날짜 | 지금도 쓰나 |
|---|---|---|---|
| A. 세 사업 부문(business lines) | OTC Link, Market Data Licensing, Corporate Services | 이번에 확인한 가장 이른 원문: 2016-05-04 1분기 실적 발표 표(당시 이름 "OTC Link ATS", "Market data licensing", "Corporate services"). 그 전은 거슬러 확인 못 함 | 씀(2026-03-04 2025 실적, 2026-05-06 2026 1분기) |
| B. 미션 문장 | 2016 "our mission to create better informed and more efficient markets" / 2026 회사 소개 끝 "how we create better informed and more efficient markets" | 2016-05-04 | 씀 |
| C. 2025 두 핵심 과제 | "two key initiatives: the launch of the OTCID Basic Market on July 1, 2025 and the ramp up of our overnight trading offering in NMS securities" | 2026-03-04 2025 실적 발표(CEO R. Cromwell Coulson) | 2026 방향: OTCQX, OTCQB, OTCID 시장 활용 교육과 "data-driven platforms" 규모 확대 |

- MOON ATS는 사업 부문 A의 OTC Link 안에 있다. OTC Link LLC(FINRA, SEC 등록 브로커딜러)가 OTC Link ATS, OTC Link ECN, OTC Link NQB, MOON ATS(2026-05 발표부터 OTC Overnight 추가)를 운영(F-1696).
- 회사 소개 문단의 구조: "data-driven disclosure standards form the foundation of our public markets"(공개시장 OTCQX, OTCQB, OTCID, Pink Limited) + "OTC Link ATSs provide critical market infrastructure that broker-dealers rely on"(F-1696).

## 2. 틀 A: 세 사업 부문
| 원문 | 우리말 | 처음 나온 시점 | 실행과 숫자(2025년, 총수익) | 근거 |
|---|---|---|---|---|
| OTC Link | 거래 시설(ATS) 사업: 증권사 간 호가, 체결. MOON ATS 포함 | 2016-05-04 이전 | 26.26백만 달러(+17%). 2025 OTC Link 고유 구독사 145곳, 하루 평균 체결 약 6.2만 건(2024년 3.8만, F-1700). MOON ATS 2024-12 출시(F-1699, F-0036), 2026 1분기 MOON 세션당 평균 약 7.1만 건, 720만 주(F-1698) | F-1694, F-1700, F-1698 |
| Market Data Licensing | 시세 데이터 판매 | 2016-05-04 이전 | 50.364백만 달러(+15%), 가장 큰 부문. 2026-03 MOON ATS와 OTC Overnight 데이터를 증권사 라이선스에 포함(barchart 배포본, https://www.barchart.com/story/news/1059334/otc-markets-group-includes-overnight-market-data-in-per-user-broker-dealer-enterprise-licensing) | F-1694 |
| Corporate Services | 상장 회사 서비스(OTCQX, OTCQB, OTCID 등급 수수료, 공시 서비스) | 2016-05-04 이전 | 48.664백만 달러(+8%). 2025-07-01 OTCID 개설(1,035사로 시작, 연말 1,052사) | F-1694, F-1695 |

- 총수익 125.288백만 달러(2025, +13%). 부문 표의 비중: 데이터 40%, 상장 서비스 39%, OTC Link 21%(F-1694 표에서 계산).
- 해석 : MOON ATS(야간 NMS 주식 거래)는 그룹 매출에서 가장 작은 부문의 일부다. 회사가 MOON 단독 매출을 따로 공개하지 않아 크기는 "OTC Link 거래 기반 수익에 기여"까지만 쓸 수 있다(F-1694).

## 3. 변천
1. 2016-05-04 세 부문 표와 미션 문장 확인(F-1697). 당시 회사 소개는 OTCQX, OTCQB, Pink 시장과 OTC Link ATS 하나.
2. 2024-12 MOON ATS 출시, 일요일~목요일 오후 8시~오전 4시(ET). 기존 OTC Overnight(장외, 해외 교차거래 종목 야간 거래)을 보완(F-1699).
3. 2025-07-01 OTCID Basic Market 개설.
4. 2026-03-04 CEO가 2025 두 핵심 과제로 OTCID와 야간 NMS 거래를 꼽음(F-1695).
5. 2026-05-06 회사 소개 문단의 ATS 목록에 OTC Overnight 추가(F-1698 출처와 같은 발표).
- 바뀐 것: 사업 부문 이름 "OTC Link ATS"가 "OTC Link"로 바뀌고 그 아래 ATS가 1개에서 5개로 늘었다. 세 부문 구분은 그대로다.

## 4. 캡처(captures/pillars/)
- MOON_fy2025_business_lines.png: 2025 사업 부문별 수익 표(Public.com 사본, 폭 559px 표 요소 캡처)
- MOON_fy2025_ceo_initiatives.png: 2025 두 핵심 과제 CEO 발언
- MOON_fy2025_about_lines.png: 회사 소개 문단(공개시장, OTC Link ATS들, MOON ATS)
- MOON_2016_business_lines.png: 2016-05-04 세 부문 표
- MOON_2016_mission_lines.png: 2016-05-04 미션 문장
- MOON_launch_blog_2025.png: MOON ATS 출시 블로그

## 5. 못 찾은 것과 열어 본 곳
- 연차보고서(2025, https://www.otcmarkets.com/file/company/financial-report/530624/content)의 전략 절과 사업 설명: otcmarkets.com이 이 세션 네트워크 밖(curl 응답 없음, WebFetch DNS 실패). 사용자 로컬 Chrome에서 열린 적 있음(work/CHROME, 캡처 실패). 연차보고서 안의 "Our Strategy" 같은 절의 존재와 항목은 확인 못 함. 다음은 사용자 로컬 브라우저 과제 후보.
- GlobeNewswire 원문(globenewswire.com 403), researchpool 사본(403), kbew98country 사본(연결 불가). Public.com(pubt.io), Stockwatch, PR Newswire 사본이 열림.
- MOON ATS 단독 매출, 구독사 수: 공개 없음(실적 발표는 "growing base of dedicated subscribers"만).
- 2016년보다 이른 세 부문 사용 시점: 거슬러 확인 못 함.
