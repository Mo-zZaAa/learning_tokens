# Kraken(Payward) 공식 전략 틀

열람일 2026-11-17. 담당 PILLARS-A. 원문은 payward.com 실적 서한(curl과 Playwright로 열림).

## 1. 틀 이름과 원문 항목

- 틀 이름: **pillars**(사업 기둥). 2026 Q2 실적 서한(2026-08-14, 공동 CEO Arjun Sethi 명의)에서 "On top of that foundation we operate four pillars"로 처음 내걸었고, 2026 Q3 서한(2026-11-13)에서 "Last quarter we introduced four pillars: Trading, Banking, Asset Management, and Payward Services. This quarter we made AI the fifth."로 다섯 개가 됨.
- 기둥 아래 바탕(foundation): 매칭 엔진 하나, 위험 엔진 하나, 담보와 결제 핵심 하나, 100개 넘는 인가와 등록(2026 Q2 서한).
- 기둥 위 시장 해석: 세 힘(three forces) convergence, onshoring, automation(2026 Q2, Q3 서한 공통).

| 원문 | 우리말 | 처음 나온 시점 | 실행과 숫자(회사 제시) | 근거 |
|---|---|---|---|---|
| Payward Trading | 거래(가상자산, 주식, 전통 시장의 현물과 파생) | 2026-08-14(Q2 서한) | 미국 개인 대상 첫 CFTC 규제 현물 신용거래, 미국 첫 CFTC 규제 무기한선물(Bitnomial 인프라, 인수 2026-05-01 종결), Kraken Prop. 선물 일평균 수익거래 전년 대비 8% 증가(Q2). 파생 계약 건수 6,600만 건, 전년 대비 84% 증가(Q3) | F-1638, F-1503, F-1498 |
| Payward Banking | 은행(예금, 결제, 카드, 수탁, 대출) | 2026-08-14 | 가상자산 담보 신용한도 Flexline(2026-04), Krak 11개 EU 시장 확대(Q2). Kraken Financial 연준 마스터 계정(2026-03-04 발표), 다음 단계는 달러 송금을 자체 마스터 계정으로 옮기고 유럽 예금을 자기 대차대조표에 둠(Q3) | F-1597, F-1532, F-1259, F-1596 |
| Payward Asset Management | 자산운용(구조화 수익, 토큰화 자산, 비상장 시장 접근) | 2026-08-14 | IPO Access(SpaceX, Bending Spoons), xStocks 묶음, xStocks 보유 리워드 최대 1%(Q2). 다음 단계 xPO(규제 승인 필요), xStocks 기반 펀드. 홈페이지는 이 부문 브랜드를 Coming soon으로 표시 | F-1506, F-1509, F-1640 |
| Payward Services | 기업용 인프라(같은 인프라를 상품으로 판매) | 2026-08-14(기둥). 사업 출시는 2026-03-11 | 통합 API 첫 외부 파트너, DeFi Earn 비트코인 금고 예치 약 4억 달러, Bitget 등 xStocks 유통(Q2). Reap 인수 종결 2026-07-01(최대 6억 달러, Q1 서한). 접근 기반 TPM 전년 대비 59% 증가, 전체의 약 4분의 1(Q3) | F-1511, F-1507, F-1195, F-1502 |
| AI | AI(에이전트와 사람이 결제, 거래, 금융에서 행동하게 하는 인프라) | 2026-11-13(Q3 서한, 다섯째 기둥) | 모든 앱에 에이전트 하네스, 첫 하네스는 내년 초 예정. 다음 출시는 개인 금융 에이전트(고객 한도 안, 거래 전 승인, 행동 기록). Kraken CLI에 MCP 서버 탑재(Q2 서한) | F-1639, F-1640 |

- 경영진 설명(매체): Sethi는 CoinDesk 인터뷰(2026-09-26)에서 지주회사가 아니라 "하나의 플랫폼, 하나의 대차대조표, 하나의 규제 체계"이고 사업은 네 축이라고 설명(F-1347, F-1364, 단일 출처).
- 수익 구분(기둥과 별개): Q3부터 총플랫폼마진(TPM)을 거래 기반, 자산 기반, 접근 기반 셋으로 보고. 자산과 접근 기반 합계 52%(F-1501, F-1502).

## 2. 변천(처음 내건 시점 거슬러 찾기)

| 시점 | 문서 | 틀 | 근거 |
|---|---|---|---|
| 2026-02-03 | 2025 Financial Highlights | 슈퍼인프라(superinfrastructure): 유동성 풀, 위험과 증거금 엔진, 담보와 결제, 준법과 인가가 각각 하나. 고객 구분은 소비자, 전문, 기관, 지역 상품. 기둥 표현 없음 | F-1641 |
| 2026-03-11 | Introducing Payward Services | B2B 인프라 사업 출시(뒤에 넷째 기둥이 됨) | F-1511 |
| 2026-05-18 | Q1 2026 서한 | Direct to Consumer, Business to Business(Institutional, B2B) 두 묶음. 기둥 표현 없음 | F-1499 |
| 2026-08-14 | Q2 2026 서한 | 세 힘 + 네 기둥(Trading, Banking, Asset Management, Services) 처음 | F-1637, F-1498 |
| 2026-09-26 | CoinDesk 인터뷰(매체) | 네 축 그대로 설명 | F-1347, F-1364 |
| 2026-11-13 | Q3 2026 서한 | AI를 다섯째 기둥으로 추가. 앞 네 기둥은 "원장 하나를 보는 네 화면" | F-1500, F-1639 |
| 2026-11-17 열람 | payward.com 홈페이지 | 카드 다섯(Trading, Banking, AI, Asset Management, Services)과 하위 항목, 브랜드 배치 | F-1640 |

## 3. 캡처(captures/pillars/)
- Kraken_q2_2026_header.png: Q2 서한 제목, 날짜, 작성자, 세 힘 첫머리
- Kraken_q2_2026_four_pillars.png: 네 기둥 원문 정의
- Kraken_q3_2026_header.png: Q3 서한 제목과 날짜
- Kraken_q3_2026_first_four_pillars.png: "Last quarter we introduced four pillars... AI the fifth" 단락
- Kraken_q3_2026_five_pillars_next.png: 다섯 기둥별 다음 단계(Trading, Banking, Asset Management, Payward Services, AI)
- Kraken_payward_home_pillars.png: 홈페이지 다섯 카드
- Kraken_q1_2026_d2c_b2b.png: Q1 서한의 Direct to Consumer, Business to Business 묶음
- Kraken_2025_one_infrastructure.png: 2025 연간의 공유 요소 넷

## 4. 새 사실 번호
F-1637(세 힘), F-1638(Trading Q2 실행), F-1639(AI 기둥 계획), F-1640(홈페이지 다섯 카드), F-1641(슈퍼인프라 이전 틀). 기존 F-1498~F-1509, F-1511, F-1532, F-1596, F-1597은 다른 담당(STORY-KR)이 먼저 넣어 다시 넣지 않음.

## 5. 못 찾은 것과 열어 본 곳
- 기둥별 매출이나 이익: 공개 없음. 회사는 TPM을 기둥이 아니라 거래, 자산, 접근 기반으로만 나눔(Q3 서한 각주까지 확인).
- 기둥 체계를 정한 내부 문서, 투자자의 날 자료: 비상장사라 없음. S-1은 비공개 제출(F-1188)이라 원문 없음.
- 2025 이전 Kraken 시절 공식 전략 틀: kraken.com 채용 페이지 미션 문장(F-1110) 외 못 찾음.
- 열어 본 곳: payward.com 홈, about, newsroom 사이트맵의 보도자료 전부 목록, Q1, Q2, Q3, 2025 실적 글, Introducing Payward Services, Our AI doctrine(내부 AI 사용 원칙이라 전략 틀 아님), /ai 페이지.
