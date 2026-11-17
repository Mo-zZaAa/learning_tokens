# Dinari 공식 전략 틀

조사일 2026-11-17. 원문은 dinari.com(sitemap.xml 99건 전수 내려받아 검색)과 회사 블로그. F 번호는 db/facts.csv(이번 병합 F-1670~F-1678, 기존 번호는 그대로 인용).

## 1. 틀 이름과 요약
"pillars" 같은 이름 붙은 틀은 없다. 회사가 항목을 나눠 반복해 쓰는 구조는 둘이다.

| 틀 | 원문 이름 | 처음 나온 곳, 날짜 | 지금도 쓰나 |
|---|---|---|---|
| A. 발행, 유통, 거래(고객 세 갈래) | 홈 "Issue, distribute, and trade tokenized assets." 아래 Asset Issuers & Transfer Agents, Distribution Partners, Trading Firms & Market Makers | 블로그 기준 처음 확인 2026-09-30("infrastructure spanning issuance, distribution and trading"). 홈 문구 자체의 첫 게시일은 확인 못 함 | 씀. 홈(2026-11-17), Broadridge 발표(2026-11-05) |
| B. Dinari Financial Network(DFN) 다섯 범주 | "Network Capabilities": Market Access, Trading & Execution, Post-Trade Infrastructure, Distribution, Commercial Participation | 2026-07-06 The Dinari Financial Network | 씀(현재와 계획 기능을 함께 적은 로드맵 성격) |

- 미션 문장은 발표마다 다르다(아래 4절). 하나로 고정된 공식 문장은 확인 못 함.

## 2. 틀 A: 발행, 유통, 거래
| 원문 | 우리말 | 처음 나온 시점 | 실행과 숫자 | 근거 |
|---|---|---|---|---|
| Asset Issuers & Transfer Agents (ETF providers, Index publishers, Transfer agents) | 발행 쪽 고객: ETF 운용사, 지수 회사, 명의개서대리인 | 2026-09-30(블로그 표현) | 2025-10-07 S&P Dow Jones Indices와 S&P Digital Markets 50 지수(주식 35, 가상자산 15) 토큰화(F-1489). 2026-09-30 카카오페이증권과 한국 상장주식 토큰화 검토(F-0297) | F-1670, F-1671, F-1489 |
| Distribution Partners (Neobanks, Fintechs, Brokerages, Exchanges, Wallets) | 유통 쪽 고객: 네오뱅크, 핀테크, 증권사, 거래소, 지갑 | 2026-09-30(블로그 표현). B2B API는 2024년부터(Partner API, Managed Accounts) | 홈 표시 92개 관할, 700종 이상(F-0307, F-0310). 2026-08-04 미국 출시 724종, 증권사에 API 라이선스(F-1131). 2025-05 기준 60개국 이상(F-1673) | F-1670, F-0307, F-1131 |
| Trading Firms & Market Makers (Prop firms, Market makers, Institutional traders) | 거래 쪽 고객: 자기매매사, 시장조성사, 기관 트레이더 | 2026-09-30(블로그 표현) | 2026-05-20 Flow Traders와 dShares 24/7 거래(F-1676). 기존 24/5는 거래소, ATS, 다크풀 유동성 | F-1670, F-1676 |

## 3. 틀 B: DFN 다섯 범주(2026-07-06)
| 원문 | 우리말 | 처음 나온 시점 | 실행과 숫자 | 근거 |
|---|---|---|---|---|
| Market Access | 시장 접근(dShares, 증권사와 거래소 연결, API와 FIX, 시세) | 2026-07-06 | DFN 자체는 2025-08-14 Avalanche 기반 L1으로 먼저 출시, 초기 검증자 Gemini, BitGo, VanEck(F-0282, F-1674) | F-1672, F-0282 |
| Trading & Execution | 거래와 체결(24/7, 소수 단위 호가창, 금액 기준 투자, 포트폴리오 자동 전환) | 2026-07-06 | 2026-05-20 24/7 거래 개시(F-1676) | F-1672, F-1676 |
| Post-Trade Infrastructure | 사후 처리(수탁, 청산, 결제, 스테이블코인 결제, 배당, 기업행위, 주주 서비스, 명의개서 연결) | 2026-07-06 | 2026-07-08 tZERO 제휴(F-0288), 2026-08 USDC 배당, 2026-11-05 Broadridge 의결권(F-1677) | F-1672, F-0288, F-1677 |
| Distribution | 유통(발행사 후원 dShares, 증권사 유통, 2차 유동성, 주주 소통) | 2026-07-06 | 2026-08-04 미국 브로커딜러에 API 라이선스(F-1131) | F-1672, F-1131 |
| Commercial Participation | 참여사 수익 프로그램(결제와 청산 인센티브, 유동성 프로그램 등) | 2026-07-06 | 실행 사례 확인 못 함(회사도 "expected"로 적음) | F-1672 |

- DFN의 뜻이 바뀌었다: 2025-08-14에는 "Avalanche 기반 L1, 옴니체인 호가창"(F-0282), 2026-07-06에는 "브로커딜러, 거래소, 발행사, 수탁사를 잇는 시장 틀(market framework)". 블록체인 이름보다 참여 기관 모델을 앞세운다.
- 다음 계획(2026-08-04 미국 출시 글): 24/7 거래, T+0 결제, 담보 대출과 증거금, 자동 포트폴리오 관리(F-1678).

## 4. 미션 문장 변천
| 날짜 | 원문 | 근거 |
|---|---|---|
| 2024-02-06 | USD+ 출시 글 "Dinari's Future Roadmap" 절. 구체 항목 없이 "big announcements planned" | https://dinari.com/blog/usd-stusd-yield-bearing-stablecoin |
| 2025-05-01 | "At Dinari, our mission is simple: make it easy for anyone, anywhere, to access the U.S. stock market" | F-1673 |
| 2025-08-14 | "with a mission to enable investing in anything from anywhere through its compliance-first, blockchain-based tokenization technology"(회사 소개 문단, 2025-12-09 Roxom 발표까지 같음) | F-1674 |
| 2025-08-27 | CEO "Our mission is to democratize access to U.S. dollars and equities globally."(Rain 발표) | https://dinari.com/blog/rain-adds-support-for-dinaris-usd-enabling-yield-bearing-stablecoin-spending-across-latam |
| 2025-10-08 | CEO "Our mission at Dinari is to help set a standard for how tokenized equities can safely and compliantly enhance traditional finance." | F-1675 |
| 2026-11-05 | 회사를 "a financial infrastructure company enabling the issuance, distribution and trading of tokenized equities"로 소개 | F-1677 |

- 해석 : 개인 접근(2025 상반기) → 기관 시장 틀(2026 하반기)로 무게가 옮겨 감. 2024년 Partner API(B2B) 출시, 2026-07 DFN 재정의, 2026-08 미국 증권사 API가 같은 방향의 실행이다(F-1672, F-1131).

## 5. 캡처(captures/pillars/)
- Dinari_home_issue_distribute_trade.png: 홈 "Issue, distribute, and trade tokenized assets."와 세 고객군
- Dinari_dfn_capabilities.png: DFN Network Capabilities 다섯 범주 전체
- Dinari_dfn_intro.png: DFN 글 첫머리(시장 틀 정의, 2026-07-06)
- Dinari_mission_seriesA_2025.png: 2025-05-01 미션 문장
- Dinari_mission_boilerplate_2025.png: 2025-08-14 회사 소개 문단 미션

## 6. 못 찾은 것과 열어 본 곳
- 홈 "Issue, distribute, and trade" 문구의 첫 게시일: web.archive.org 연결 끊김으로 확인 못 함. 블로그 99건 중 같은 표현의 첫 글이 2026-09-30.
- Commercial Participation 범주의 실제 프로그램, DFN 참여사 수: 공개 확인 못 함.
- 연차 보고서, 투자자 서한: 비상장사라 공개 없음. 공식 "pillars" 표현은 사이트 전수 검색에서 0건.
