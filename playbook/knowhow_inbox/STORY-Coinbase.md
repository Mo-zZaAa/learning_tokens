# STORY-Coinbase 리서치 노하우 (2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| coinbase.com/blog(403) | Markets Media가 "By Coinbase"로 전문 전재(INTX 출범, Coinbase Clearing 승인, tGBP 상장). curl로 열림 | 회사 발표 문장 그대로라 1차 확인으로 씀 |
| investor.circle.com(403) | circle.com/blog 같은 글(2023-08-21 USDC 다음 장, 두 CEO 공동 서명) | Circle과 Coinbase 수익 배분 원문 |
| theblock.co(curl 403, WebFetch DNS 실패) | 같은 사건의 cointelegraph, decrypt, financemagnates 기사 | 셋 다 curl 200 |
| cftc.gov DCO 등록 명령 PDF(403) | 회사 발표 전재(Markets Media)와 매체 기사 | 등록일은 기존 F-1123 |
| sec.gov 10-K(403) | FairX 인수 금액(검색 요약 2.75억 달러)은 원문 미확인이라 쓰지 않음 | |

## 쓸모 있었던 1차 출처 위치
- Coinbase 과거 주주서한: s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf, .../2021/q4/Coinbase-Q421-Shareholder-Letter.pdf. 파일 이름 규칙이 분기마다 달라 추측 주소는 404(Q1-2025, Q3-2025, Q4-2024). 검색으로 정확한 이름을 먼저 찾는다.
- Q2 2025 서한: Everything Exchange 첫 표현(p.7), 파생을 키우는 이유(75%, p.8), 스테이블코인 수익을 플랫폼 안과 밖 USDC로 나눈 표(p.4~6), ETF 보관 점유율 80% 이상(p.6).
- Q4 2021 서한 p.10 표: 상장 첫해 수익 구성(거래 93%, 구독과 서비스 7%)과 2020 비교. "반복 수익이라 안정" 문장(p.11).
- Q3 2026 AMA, 분석가 콜 녹취(inputs/manual/B03_*): Circle 관계(협력과 경쟁, 50%, 30%), 청산소를 받은 이유(예측시장 자체 계약), 결제 계약사, Everything Exchange 외환 발언.

## 함정
- The Clearing Company(2025-11 DCO 신청 발표)와 Coinbase Clearing LLC(CFTC 신청일 2025-11-14)가 같은 신청인지 공개 자료로 확인되지 않는다. 검색 요약 둘이 서로 반대로 말했다. 별개 사실로 쓰고 잇지 않는다.
- link_story.py는 링크 칸이 로컬 경로인 사실(주주서한 PDF 등)을 대괄호 없는 번호로 바꾼다. 한 줄에 그런 번호만 있으면 check_story가 "근거 없음"으로 잡으므로 링크가 있는 사실을 같이 붙이고, 남은 번호 뒤에 "(주주서한 PDF)"처럼 출처 종류를 붙였다.
- 새 사실의 링크를 IR 폴더 주소(.../2026/q3/)로 두면 기존 F-1221, F-1222와 같은 방식으로 링크가 걸린다(원문 위치 칸에 로컬 파일 이름).
- 외환(FX)은 2026 우선순위 정의에만 있고 출시 상품은 없다(tGBP 상장, CEO 발언 수준). 기둥별 실현 여부를 볼 때 "이름뿐인 기둥" 후보로 먼저 표시한다.
