# REV-RH 노하우(Robinhood 매출 리서치, 2026-11-18)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| sec.gov, data.sec.gov(지정 User-Agent로도 403) | annualreports.com 연차보고서 PDF: /HostedData/AnnualReportArchive/r/NASDAQ_HOOD_<연도>.pdf(2021~2024), 최신은 /HostedData/AnnualReports/PDF/NASDAQ_HOOD_2025.pdf. 회사 페이지 /Company/robinhood-markets-inc 의 /Click/<번호> 링크가 최신 PDF로 감 | 10-K 원문 PDF 그대로. pdftotext -layout으로 표가 살아남. 연결이 끊기면 --retry 2 |
| investingnews.com 2021~2025 분기 대부분(404) | 2025 Q3, 2026 Q1만 열림. 연간 상품별 숫자는 10-K 3년 표로 해결 | 분기 사본을 찾기 전에 10-K MD&A 표를 먼저 봄 |
| capedge.com 문서 직접 주소(404, 서명 링크), techstory, benzinga, cnbc, axios(403), coindesk(429), yahoo(WebFetch 허용 밖) | 같은 사건을 실은 Nairametrics, amNY(로이터 전재), InvestmentNews, Kiplinger가 curl로 열림 | |

## 쓸모 있었던 1차 출처 위치
- Robinhood 10-K MD&A: 상품별 매출 표(옵션, 가상자산, 주식, 기타)와 이유 설명(거래 손님 수, 1인당 거래대금, 리베이트 요율, 매칭 장려금), 순이자 세부 표, 이자 받는 자산 표(잔액 평균과 연 수익률). 3년 표라 2021 10-K 한 권으로 2019~2021이 나옴
- Note 1 Concentrations of Revenue: 시장조성자별 순매출 비중(Citadel 2019 29%에서 2026 Q3 17%)
- 2021 10-K 위험요인: Dogecoin 매출 비중(분기별), 정규직 2018 말 289명
- Human Capital 절: 연말 정규직 수

## 함정
- 2021 10-K는 Dogecoin 2분기 몫을 "순매출의 32%"라고 적었으나 매체 숫자로 계산하면 거래 기반 매출의 32%와 맞음. 하나로 고르지 않음
- 예측시장 매출은 2025 10-K까지 "기타 거래"에 묶이고 2026 10-Q부터 따로 나옴. 2025 연간 값은 공개 안 됨
- kb/structs/robinhood/money.csv RH-M01의 "시장조성자와 거래소 몫 합계는 거래 기반 매출의 46%"는 10-Q 표상 "순매출의 46%"임(표 제목 Total as percentage of total net revenues)
- 공용 scratchpad의 h2t.py 같은 흔한 이름은 다른 세션이 덮어씀. 담당별 하위 폴더를 씀
