# S2-ON 리서치 노하우 (Ondo 개요, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| The Block 기사(403), CoinDesk 2021 기사(429) | 회사 블로그 원문(ondo.finance/blog/<슬러그>, curl로 열림) | 시드, 시리즈 A 참여사, 토큰 판매 금액은 회사 글에 다 있음. 시리즈 A 기업가치는 언론에만 있어 못 씀 |
| api.adviserinfo.sec.gov(열림, 소유자 정보 없음) | 없음. 투자자문사 지분 관계는 단정하지 않음 | FINRA BrokerCheck API의 content 안 directOwners는 증권사 소유자를 바로 보여 줌(Oasis Pro Markets 소유자 Ondo Finance Inc.) |
| docs.ondo.foundation/llms.txt(404) | docs.ondo.foundation/ 첫 화면과 /ondo-token | 재단 성격(케이맨 제도, 실질 소유자 없음), CoinList 판매분 비중 |

## 쓸모 있었던 1차 출처 위치
- ondo.finance/usdy 화면의 Portfolio Overview: 담보 구성(국채, SHVon, 은행 예금), 만기수익률, 표시 APY. 지급 수익률 정책 문장은 USDY 출시 글(2023-08-03, "minus a small spread")
- docs.ondo.finance/api-reference/overview.md: 1차 매수자(Primary Purchaser) 발행과 상환 흐름. 거래소, 지갑이 어떻게 토큰을 받는지 묻는 질문의 출발점
- docs.ondo.finance/ondo-stocks/token-and-quote-pricing.md: 견적가와 발행 법인 매매가 차이(회사 수익원)
- app.rwa.xyz/treasuries HTML: 플랫폼 표(상품 수, 합계)와 상품 표(상품별 가치)가 같은 화면에 서버 렌더됨. tbody 안 tr를 모두 읽어야 짝수 줄이 빠지지 않음

## 함정
- rwa.xyz 플랫폼 합계는 펀드가 펀드를 담는 겹침을 그대로 더함. USDY 담보 SHVon(회사 화면 4.17억 달러)이 rwa.xyz 상품 표 SHVon(4.19억 달러)으로 다시 잡혀 Ondo 합계가 부풂. 순위를 쓸 때 상품 표와 담보 구성을 같이 본다
- rwa.xyz Franklin 합계는 하루 사이 33억에서 35억 달러로 바뀜(BENJI 12.80억이 15.47억으로). 날짜를 붙여 쓴다
- DefiLlama는 Ondo 수입을 0으로 잡음(보유자 수익만 체인에서 보임). "외부 추정 매출"로 쓰지 않는다
- 상품 발행 법인(BVI)의 다수 지분은 재단 쪽(Flux Finance 90.01%)이라 "Ondo가 남기는 돈"과 "Ondo Finance Inc. 손익"이 다를 수 있음. 수익원 서술에 주어를 발행 법인으로 쓴다
- 회사 블로그 sitemap의 lastmod는 게시일이 아님(2026-07에 일괄 갱신). 게시일은 본문의 "분류 • Mon D, YYYY" 첫 줄로 본다
