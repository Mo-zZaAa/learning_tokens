# S2-RH 리서치 노하우 (Robinhood 개요, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| investors.robinhood.com 보도자료, 10-Q(403) | 사이트 전수조사 사본 KDX_사이트전수조사_인수인계/work/robinhood/raw/investors.robinhood.com/ (Q3 2026 보도자료, Q4 2023 보도자료, 10-Q node__16931, 월간 지표, 전환사채 보도자료) | 2026-11-16 수집본. 열람일과 수집일을 함께 적음 |
| 옛 실적 보도자료(2021 Q4) | mondovisione.com 전재본(보도자료 전문과 손익계산서 표). 회사 뉴스룸 같은 날 글은 링크만 있음 | 2025 Q4는 investingnews.com 전재본이 curl로 열림 |
| sec.gov S-1(403), The Block S-1 해설(Cloudflare 확인 화면) | 테크크런치(2019 매출, 순손실), Malay Mail에 실린 로이터 기사(2020 매출, 상장 전 누적 55억 달러, 긴급 조달 이유) | 2018 손익과 2019 영역별은 못 찾음 |
| ciro.ca 공지(Cloudflare 확인 화면) | wonder.fi 보도자료(CIRO 승인일), osc.ca 등록 가상자산 거래 플랫폼 목록 | 우회하지 않음 |

## 쓸모 있었던 1차 출처 위치
- robinhood.com/us/en/newsroom/<slug>/ 와 robinhood.com/newsroom/<slug>/ 둘 다 curl로 열림. 투자 라운드 글이 시리즈 D(2018)부터 있음(robinhood-raises-363-million..., -323m..., -280-million..., -3-4-billion...). 인수 글은 완료일 갱신 문단이 붙어 있어 발표일과 완료일을 한 글에서 가림
- 10-Q(node__16931) Note 6 매출 표: 옵션, 이벤트 계약, 암호화폐, 주식, 신용 매수 이자, Cash Sweep, 신용카드, Gold 구독까지 줄별 금액. Note 3에 Rothera의 MIAXdx 대금(7,900만 달러, SIG 4,100만), 위험요인에 "Bitstamp 말고는 외부 거래소에 기댐" 문장
- Q4 2023 보도자료 Key Performance Metrics 머리 문단: Funded Customers가 옛 Net Cumulative Funded Accounts와 같은 계산이라는 문장. 연도별 고객 수를 이어 붙일 근거
- 이벤트 계약 수수료 공식과 거래소 수수료 상한: robinhood.com/us/en/support/articles/event-contracts-overview/
- 캐나다 등록 분류(투자딜러, 제한딜러, 딜러와 거래장 구분): osc.ca registered-crypto-asset-trading-platforms 표 한 장

## 함정
- 테크크런치 S-1 기사의 2020 매출 9.858억 달러는 회사 발표 9.59억 달러와 다름(오타로 보임). 회사 값을 씀
- 녹취 정리의 "2021 Q1 주문 흐름 대가 81%"는 원문을 열지 못함. 2020 비중(주식과 옵션 72%)은 2021 Q4 보도자료로 계산 가능
- 이벤트 계약 매출은 중개 수수료와 거래소 몫으로 나뉘어 공시되지 않음. 계약당 매출(약 1.05센트)로 판단만 가능
- Stock Tokens의 청약, 상환 수수료는 1차 청약 창구가 내는 것이라 이용자가 내는 돈으로 쓰지 않음
- 다른 세션이 `git add -A`로 커밋하면서 작업 중인 개요 초안이 먼저 커밋됨. 담당 파일은 마지막 저장본이 기준
