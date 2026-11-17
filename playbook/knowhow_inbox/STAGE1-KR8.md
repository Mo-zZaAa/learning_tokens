# STAGE1-KR8 리서치 노하우 (Kraken PM 질문 9건: 영국 파생 규제, CFTC 승인 기간, 시장감시, IPO Access, LSE 24, Prime, xStocks 구조와 통화, SPDI)

- FCA 성명과 보도자료(fca.org.uk/news/statements/..., /news/press-releases/...)는 curl로 열림. FCA 등록부(register.fca.org.uk)는 화면이 자바스크립트이고 API(services/V0.1/Firm/번호)는 헤더 없으면 403. 법인의 과거 인가 범위(예: Crypto Facilities의 2019년 MTF 이전 허가)는 사용자 로컬 브라우저 과제. FCA Handbook 페이지도 자바스크립트라 본문이 비어 옴.
- Crypto Facilities 원 사이트(cryptofacilities.com)의 뉴스와 회원 약관이 curl로 열림. MTF 인가일(2020-07-06), "MTF 운영 인가" 문장은 여기서 1차로 잡힘. 회사 보도자료끼리 MTF 연도가 다름(2019 대 2020).
- CFTC 문서(cftc.gov)는 403이지만, 회사가 자기 사이트에 CFTC 명령 PDF를 올려 둠(bitnomial.com/exchange/regulatory 페이지의 orders 링크). DCM 명령문에 "신청서 제출과 보완 기간(2016-09-30부터 2020-02-20)"이 적혀 있어 승인 기간을 1차로 계산할 수 있음. CFTC 위원장, 위원 발언은 Mondo Visione 전재본이 열림(신청 시점 "In April 2022"가 여기 있음).
- 신청일을 공개하지 않은 DCM은 신청 직후 회사 공동 보도자료의 "recently filed" 문장으로 하한을 잡음(Small Exchange: Eventus 2019-03-11, CQG 2019-03-13, 둘 다 curl 열림). Business Wire, MarketScreener 사본은 403.
- DCM, DCO 심사 기준 기간과 시장감시 의무는 eCFR renderer API(api/renderer/v1/content/enhanced/current/title-17?part=38&section=38.156)로 바로 원문. 미국 법전은 uscode.house.gov 주소가 404라 law.cornell.edu/uscode/text/7/6 사용.
- Nasdaq 보도자료(ir.nasdaq.com 403, nasdaq.com 연결 끊김)는 Markets Media 전재본(끝에 "Source: Nasdaq")으로 대신함.
- LSEG 보도자료(lseg.com/en/media-centre/press-releases/2026/...)와 LSE 24 안내서 PDF가 curl로 열림. 회사 발표의 "LSE 24"가 무엇인지는 LSE 원문으로 확인해야 함(토큰 전용 시장이 아니라 시간 외 별도 거래장).
- xStocks 상품별 Final Terms: assets.backed.fi/legal-documentation은 이 환경에서 "Access Restricted"(지역 제한, 우회하지 않음). 크로아티아 HANFA 통지 PDF(hanfa.hr/notifikacije/FTWS_번호.pdf)는 개별 파일이 열리지만 목록 페이지는 403이라 종목별로 찾을 수 없음. 영국, EU 주식 xStocks의 상품 통화는 사용자 로컬 과제.
- Kraken 공개 API(api.kraken.com/0/public/AssetPairs?aclass_base=tokenized_asset)로 Kraken Pro에 올라간 xStocks 거래쌍과 호가 통화를 1차로 셀 수 있음(2026-11-17 기준 354쌍 전부 USD).
- 와이오밍 법은 wyoleg.gov/<연도>/Enroll/<법안>.pdf(제정 법률 원문)가 curl로 열림. 요약본(Summaries)보다 조문이 자세함(예금자 법인 요건, 2020 부수 업무 목록).
- 함정: 은행 인가가 스테이킹을 열려던 것이라는 가설은 순서로 먼저 확인. Kraken 거래소 스테이킹은 2019-12-13 시작으로 은행 인가(2020-09-16)보다 앞섬.
- web.archive.org는 이 세션에서 DNS 실패(archive.org 가용성 API만 열림).
