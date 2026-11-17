# S2-CB 리서치 노하우 (Coinbase 개요, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| sec.gov 10-K, 10-Q(403) | IR CDN의 연례 주총 게시본: s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf(2025 10-K), doc_events/2024/Jun/14/coinbase-global-inc-2023-10k_filed.pdf(2023 10-K), doc_financials/2021/q4/8e5e0508-...pdf(2021 10-K), doc_financials/2026/q2/Coinbase-Global-Inc-Q2-2026-10Q.pdf | 10-K 본문 전체라 금리 민감도(Item 7A), 지역별 매출, 거래 상대 집중, 인수 대가가 다 있음. 파일 이름은 검색으로 먼저 찾고 추측은 몇 개만 |
| 2022 4분기 주주서한(IR CDN에 없음, docoh는 죽은 주소, capedge 404) | last10k.com/sec-filings/coin/<접수번호>.htm 페이지에 8-K 첨부 주주서한 본문이 실림 | 10-K 본문 섹션(Item 7A)은 동적으로 불러와 curl로는 안 나옴 |
| coinbase.com 블로그(Deribit 발표, System Update) 403 | Deribit 발표 문장은 Pulse 2.0이 그대로 인용 | 매체 이름을 본문에 밝힘 |
| cftc.gov 자기인증 PDF(403) | 같은 내용을 담은 Nodal Clear 보도자료(Silicon UK의 Business Wire 전재), FairX 2021 보도자료(PR Newswire) | 청산 주체 확인 |
| OCC 결정문 cd1370.pdf(curl에 차단 화면) | OCC 신청서 공개본(comptrollerofthecurrency.gov .../coinbase-national-trust-company.pdf)은 열림 | 승인 결과는 빈칸 |
| NFA 용어집, investor.gov(이동 화면, 403) | eCFR 17 CFR 1.3(FCM, DCO, 소개 중개사 정의), 17 CFR 33.3(옵션은 DCM 상장, FCM 판매), FINRA 옵션 설명 페이지 | 용어 뜻 줄의 1차 근거 |

## 쓸모 있었던 1차 출처 위치
- 2025 10-K: Item 1의 거래소 4곳 표, Base 시퀀서 수수료 문장, 주 송금업과 BitLicense, CCTC 신탁, 증권사(2025-12 주식, 소개 중개사), FCM(2025-12 사건 계약), Deribit VARA 인가. Item 7A 금리 1.5%p 민감도. 주석의 지역별 매출과 "한 거래 상대 19%"(스테이블코인 수익 비중과 세 해 모두 같음)
- 2023 10-K: FairX 완료일(2022-02-01)과 대가 2.75억 달러 구성, 금리 5%p 민감도
- 2021 10-K: 2019~2021 손익과 매출 분해, 우선주 A부터 E 시리즈 표, 2021 차입
- 뉴욕주 신탁의 뜻: NYDFS 2018-10-23 보도자료(좁은 보관 업무, 회사가 적격 수탁기관이 됐다고 말함), 뉴욕 은행법 102-a(nysenate.gov), iShares ETF 설명서(ishares.com/us/prospectus/bita, 수탁인이자 적격 수탁기관)
- 예측시장 자체 계약: docs.cdp.coinbase.com/derivatives-predictions/welcome(curl로 열림, 시험 환경 공개 문장)

## 함정
- 발표 대가(Deribit 29억 달러)와 회계 대가(42.9억)는 주식을 완료일 종가로 다시 평가했기 때문. 10-K 주석 각주에 그 문장이 있음
- 2026부터 회사 보유 스테이블코인 수익을 순매출 밖으로 옮겨 적음(2026 2분기 10-Q 주석 2). 2025 이전 분기 값과 2026 값이 서한마다 다르게 보일 수 있음
- "직접 자기 걸로 만들었다"(예측시장)는 반쯤만 맞음. 2026-11-17 기준 자체 계약은 시험 환경뿐
