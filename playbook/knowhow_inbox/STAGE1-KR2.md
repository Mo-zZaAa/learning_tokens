# STAGE1-KR2 리서치 노하우 (Kraken 2011~2018 연표)

- blog.kraken.com 옛 글(2011~2018)은 sitemap_index.xml에 일부만 있다. 전체 목록은 워드프레스 공개 REST API로 받는다: `https://blog.kraken.com/wp-json/wp/v2/posts?before=2019-03-01T00:00:00&per_page=100&page=1&orderby=date&order=asc&_fields=date,link,title` (응답 헤더 X-WP-Total 122건, 2쪽). 글 본문은 curl로 열림. `?slug=<슬러그>`로 개별 글 날짜 확인.
- 옛 글 안의 링크는 blog.kraken.com/post/<숫자>/... 형식인데 지금 주소는 /news/<슬러그> 또는 /product/<슬러그>다. 슬러그로 찾는다.
- 회사 회고 글(10주년 2021-07-28, 11주년, 13주년)은 연도별 한 줄 요약이 있어 빈 해 채우기에 쓸모 있다. 다만 연도가 당시 글과 다를 수 있다(마진 2014 대 당시 글 2015-05-25, Crypto Facilities 2018 대 발표 2019-02-04). 당시 글을 우선한다.
- payward.com/about의 "2015 현물과 선물 첫 제공"은 2019-02-04 Kraken 글("Today, Kraken becomes the first and only crypto exchange to offer both spot and futures")과 어긋난다. Crypto Facilities 설립 연도(2015)를 가져다 쓴 것으로 보이나 근거는 없다.
- 2015-08 뉴욕 철수 원문 블로그 글은 현재 블로그 목록에 없다. Finance Magnates(성명 인용), SiliconANGLE(이유 목록), Bitcoin Magazine(복귀 조건)로 교차 확인. coindesk.com 옛 기사는 429, dev.coindesk.com은 로그인 화면.
- 뉴욕주 검찰총장실 가상시장 건전성 보고서 PDF(ag.ny.gov/sites/default/files/vmii_report.pdf)는 curl로 열림.
- 2018 일본 철수는 Bloomberg 원문 대신 Japan Times(Bloomberg 기사 전재)와 Cointelegraph가 curl로 열림. cnbc.com은 403.
- 2011~2018 매출은 회사, 매체 어디에도 공개 숫자가 없다(비상장). 대신 블로그의 거래량 기록 글, 2016 투자 발표의 누적 거래액, 2019-02 보도자료의 2018 연간 거래대금을 쓴다.
