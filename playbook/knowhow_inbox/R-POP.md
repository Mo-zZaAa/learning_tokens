# R-POP 노하우 (모집단 수, 야간 ATS 목적, 한국 자산 두 경로, 2026-11-16)

## 막힌 곳과 통한 공식 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| cftc.gov, sirt.cftc.gov(403, Cloudflare 봇 확인) | FCM 수는 NFA "Membership and Directories" 페이지의 Membership Totals(기준일 표기, FCM 79) | DCM, DCO 수는 대체 경로 없음. 사용자 로컬 브라우저 과제 |
| investor.gov(403 Access Denied) | eCFR 17 CFR 230.405 "Depositary share" 정의(ecfr.gov renderer API) | 법령 정의라 1차 |
| api.binance.com exchangeInfo(451, 지역 제한) | 없음. 사용자 로컬 브라우저 | 우회하지 않음 |
| api.gm.ondo.finance(403, API 키 필요) | app.ondo.finance/assets/<티커>on 개별 페이지 제목(404면 없음) | 전체 목록은 아님. 확인한 티커만 적는다 |
| dfs.ny.gov .../regulated_entities(404) | dfs.ny.gov/apps_and_licensing/virtual_currency_businesses 안의 Regulated Entities 표(39행) | 표에 기준일 없음, 열람일을 기준일로 |

## 쓸모 있었던 1차 출처 위치
- FINRA Industry Snapshot 2026(finra.org/sites/default/files/2026-05/2026-Industry-Snapshot.pdf, 표지 September 2026): p.21 Table 2.1.3 규모별 회사 수, p.23 Table 2.1.5 BD/IA 겸업, p.49~52 Table 2.6.1~2.6.3 사업 모델과 세그먼트(ATS와 ECN, Fintech, Clearing and Carrying). 세그먼트별 회사 명단은 없다. 4.5절 야간 ATS 그림은 숫자 표가 없다.
- ESMA 임시 MiCA 등록부: esma.europa.eu MiCA 페이지에 CASPS.csv 링크(경로는 2024-12 폴더지만 파일은 계속 갱신, Last-Modified로 기준일). 열 ac_legal_basis(60조 통지와 63조 인가 구분), ac_serviceCode(거래 플랫폼 운영 여부), ac_authorisationEndDate.
- BMA: bma.bm/regulated-entities 한 페이지(약 6MB)에 전 업종 표가 숨김 행으로 다 들어 있다. Digital Assets Business 행의 License/Registration Type(Class F, M, T)과 Allowed Business Activities 전문. 활동 문구는 200자 넘게 길어 자르면 거래소 여부를 놓친다.
- ADGM FSRA 등록부: 화면이 쓰는 POST /api/fsrac/firms/listing/filter(JSON). companyType 165368(금융회사), 167132(인정기관), assetClass 165388(가상자산), firmStatus 165369(활성). 인정기관은 recognitionType, 취소일, 옛 이름(previousNames)까지 나온다.
- FINRA ATS 주간 자료 저장본(sources/ATS-1/finra_ats_firm_2026.json)은 야간 3사만이 아니라 전체 ATS가 들어 있다. Tier T1, T2만 더하면 NMS 주식 ATS 전체 순위와 비중을 낼 수 있다. Bruce의 MPID는 BOSS.
- xStocks 상품 목록(xstocks.fi/us/products) HTML 안에 slug, name, symbol이 전부 들어 있다(1,436종).
- Robinhood RHJ 공시 라이브러리(robinhood.com/eu/en/legal/rhj/) HTML에 종목별 Final Terms PDF 주소가 전부 있다(212건). 파일명에 기초자산 이름이 들어가 grep으로 찾는다.
- 금융위원회 보도자료 검색: fsc.go.kr/no010101?srchKey=all&srchText=<검색어>. 외국인 통합계좌 가이드라인은 2025-11-27(no010101/85748).

## 함정
- merge_db.py는 출처 번호를 담당 폴더 이름순으로 다시 매긴다. R-POP처럼 중간 이름의 새 폴더가 출처를 더하면 그 뒤 담당의 출처 번호(S-0365부터)가 밀린다. 사실 번호는 그대로. kb/ 문서가 S 번호를 직접 적으면 어긋날 수 있다.
- 같은 링크의 출처는 기존 S 번호로 합쳐진다(이번에 6건). 기존 원문을 재열람해 사실을 더할 때 링크를 기존과 똑같이 적으면 출처가 늘지 않는다.
- FINRA 세그먼트 수는 "그 유형의 모집단"으로는 쓸 수 있지만, 특정 회사가 그 세그먼트라고 쓰면 안 된다(FINRA가 회사별 분류를 공개하지 않음).
- 전체 ATS 대비 야간 3사 비중(2.43%)은 야간 시장 크기가 아니다. 낮 시간 기관 거래가 분모에 섞인다.
