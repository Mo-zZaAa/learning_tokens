# 리서치 노하우 (실제로 통한 방법, 계속 갱신)

새 리서치를 시작할 때 먼저 읽는다. 리서치 담당은 끝날 때 playbook/knowhow_inbox/<담당>.md에 새 노하우를 적고, 메인 세션이 여기에 합친다(README.md 순서). 봇 차단이나 지역 제한을 우회하는 방법은 노하우가 아니다.

## 1. 클라우드 세션에서 막히는 곳과 실제로 통한 공식 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| www.sec.gov(403, 자동도구) | federalregister.gov, govinfo.gov 관보 사본. 사용자 로컬 브라우저 | SEC 릴리스, 승인 명령은 관보에 같은 문서 |
| coinbase.com, investor.coinbase.com(403) | 사용자 로컬 브라우저(About, IR). 주주서한 PDF는 사용자 업로드 | 미션, 설립, 상장 예정 발표 확인됨 |
| investors.robinhood.com(403) | GlobeNewswire 배포본의 MENAFN 사본, 사용자 로컬 브라우저 | 실적 보도자료 인용 캡처 |
| binance.com 공지(405, 봇 확인) | PR Newswire 배포본 사본(aap.com.au), 공지 목록 공개 API(제목만), 사용자 로컬 브라우저 | 공지 본문은 로컬로만 |
| justice.gov(봇 확인) | 사용자 로컬 브라우저(사면 목록 페이지) | 재무부 FinCEN, OFAC 문서는 열림 |
| NFA BASIC(403) | 사용자 로컬 브라우저 | "Formerly Known As"로 인수 경로가 드러남 |
| Business Wire(403) | 같은 문장을 실은 매체 3곳 교차(Bernama, Markets Media, Pulse2) | 원문 배포처가 PR Newswire가 아닐 수 있음 |
| WebFetch 도구(DNS 실패 다수) | curl로 직접 | |

- 막힌 항목이 여럿 쌓이면 LOCAL_BROWSER_TASK.md 형식으로 사용자 로컬 세션에 넘긴다. 18개 중 11개를 1차로 찾음(2026-11-17). 결과는 채팅 표와 캡처 zip으로 받아 work/LOCAL/에 넣는다.
- 큰 그림(인수 이유, 국가를 고른 이유, 투자자, 요금표)은 LOCAL_GOOGLE_TASK.md 형식으로 사용자 Chrome의 구글 탐방에 넘긴다. 26개 항목 중 22개를 채움(2026-11-17, 캡처 42장). 결과는 work/CHROME/(chrome_result.md, facts.csv, sources.csv, apply_map.md)에 넣는다. 회사 공식, 공시, 감독기관은 1차 출처 확인, 매체는 단일 출처(본문에 매체 이름), (추정) 표시 값과 원문 미확인 값은 넣지 않는다.
- Chrome 탐방에서도 막힌 것: rwa.xyz 과거 점유율(로그인), 비상장사 매출과 고객 수(비공개), 감독기관의 최종 결론(발표 없음), 구독사 수(공시에 "다수"만). 다음에는 이런 항목을 처음부터 "공개 없음 후보"로 표시한다.

## 2. 쓸모 있었던 1차 출처 위치
- FINRA BrokerCheck: 증권사 등록일(firmStatusDate), 옛 상호(otherNames). 지도 시점과 "등록 시점" 의미가 다를 수 있음.
- CFTC DCM, DCO 목록: 지정일. 인수 시점과 등록 시점을 구분.
- SEC EDGAR: 명의개서대리인 TA-1은 본사 CIK가 아니라 별도 주체 "<회사>/TA" CIK로 접수될 수 있음(Dinari, Inc/TA).
- 리히텐슈타인 FMA 승인 투자설명서 목록 PDF: 승인일, 유효기간, 보충서 날짜. 목록 작성일 이후 건은 없음.
- 투자설명서(Backed, RHJ, BTech, Coinbase SPV): 법적 성격, 담보, 보관처, 발행사 존속 의존, 채무자 교체, 해지 조항.
- rwa.xyz: 토큰화 주식 플랫폼 표(같은 날 순위와 잔액). 과거 값은 제3자 글에 실린 표(Sentora 2026-01)로.
- Hyperliquid 공식 API(api.hyperliquid.xyz/info): 주식 무기한선물 미결제약정, 24시간 거래대금.
- 회사 약관 PDF: 법인 옛 이름과 인가 범위(Binance ADGM 약관). 파일 정보에 Draft 표시가 있으면 적는다.

## 3. 도구
- tools/pdf_quote.py: PDF 한 쪽에서 인용 문장만 잘라 캡처(두 단 편집은 실패할 수 있음).
- tools/find_line.py: 본문 줄 ID 찾기(링크 {xx-0000}용).
- tools/merge_db.py: 여러 담당이 동시에 쓰면 반드시 `flock /tmp/kdx_merge.lock`으로. 판정 파일은 work/MANUAL/verdicts.csv가 마지막에 이김(그 앞은 VER-* 이름순).
- tools/check_body.py: 근거 규칙 점검.
- tools/compile_axis.py: 확장 축 표.

## 4. 함정
- CSV 머리에 BOM이 있으면 열 이름이 깨짐(utf-8-sig로 읽기). 따옴표 머리는 csv.reader로.
- 검색 요약, AI 요약에 있는 날짜와 숫자는 원문에서 다시 확인(예: "2026-05 승인"은 실제로는 제출 즉시 효력).
- 언론이 쓴 숫자와 1차 숫자가 엇갈리면(예: 18개 종목 대 4종) 둘 다 출처와 함께 적고 섞지 않는다.
- 회사가 "첫"이라고 말한 것은 회사 주장으로. 투자사 게시글의 문구는 회사 문구가 아님.
- 제3자 보고서 수치는 집계 기준(중앙화 거래소만 등)과 의뢰처를 붙인다.

## 5. 사용자 제공 자료
- 사용자가 직접 찾아 준 자료(위키백과, 언론 인터뷰, 국내 매체 요약)는 사용자가 인용을 허락하면 검증 상태 "사용자 제공"으로 넣고, 본문에 출처 종류를 괄호로 밝힌다. 같은 내용이 두 곳 이상이면 "교차 확인".
- 위키백과 각주는 1차 자료(회사 블로그, 등록부, 소송 번호)로 가는 지도다. 회사 연혁의 빈 칸(설립일, 초기 인수, 제재 이력)을 빠르게 채운다.
- 코인데스크 한국어판(coindesk.com/ko)은 CEO 인터뷰 원문이 한국어로 있어 비전 문장을 찾기 좋다. 토큰포스트, 디지털투데이는 인수 금액 합계 같은 요약이 빠르다(단일이면 사용자 제공 또는 교차 확인 필요).

## 6. 회차 L6에서 합친 노하우(리서치 담당 R-K, R-D, R-ATS, R-BIZ)
- SEC 명령과 거래소 규칙: federalregister.gov API(documents.json?conditions[term]=SR 번호나 "23 Hours per Day")로 찾고 govinfo.gov/content/pkg/FR-날짜/html/문서번호.htm 으로 원문. 제목의 "Order Granting Approval"과 "Immediate Effectiveness"를 구분(MEMX는 즉시 효력, 승인 아님).
- Form ATS-N: Part III Item 19가 수수료, 공정접근은 Reg ATS 301(b)(5) 관련 항목. sec.gov가 막히면 원문은 로컬 브라우저로. Blue Ocean 소유자 공시는 Form BD Schedule A/B(FAQ 페이지 링크).
- 배포처 재게재: Business Wire와 GlobeNewswire가 막히면 같은 보도문을 실은 사이트(silicon.co.uk, MENAFN 등). CNBC 기사는 NBC 지역국 전재본(nbcsandiego.com 등).
- 회사 문서 색인: Ondo는 docs.ondo.finance/llms.txt(문서 .md 주소 목록)와 ondo.finance/sitemap.xml(블로그 전수). 추측 URL은 404가 많다.
- 상품 구성 비중: FAQ 문장보다 상품 페이지의 표(기준일 표시)를 쓴다(OUSG Portfolio Overview).
- RWA.xyz: app.rwa.xyz/treasuries 같은 서버 렌더 HTML에서 리그 표와 자산 표를 읽는다. 세부 열은 로그인 필요, 과거 시점은 별도 경로가 필요해 처음부터 못 찾음 후보.
- Coinbase: 사용자 제공 주주서한 텍스트(inputs/manual/B03_*)가 최우선(부록 Financial Summary, 슬라이드 15, 21, 22쪽, 콜 6쪽 시퀀서 수수료). 과거 서한은 IR CDN(s27.q4cdn.com) PDF가 열림.
- Robinhood: 사이트 전수조사 사본(KDX_사이트전수조사_인수인계/work/robinhood/raw/investors.robinhood.com/)의 Q3 보도자료와 10-Q(node__16931__html.md)를 grep. 주식 토큰 잔액은 파생상품 주석, PFOF는 위험요인.
- Kraken: payward.com 보도자료와 blog.kraken.com은 curl로 열림. 지분, 위험, 보관 질문은 Backed 투자설명서(inputs/manual/B01_*) 쪽수부터(p.61 주주 구조, p.66 직원 없음, 2차 보충서 p.4 Payward 의존, p.5~6 지식재산 양도). Payward 분기 실적 본문 각주에 자금 계정, 총플랫폼마진 정의.
- 비상장사 매출, 거래량: DefiLlama API(api.llama.fi/summary/fees, dexs)는 제3자 값이고 회사 매출이 아님. 쓰면 반드시 주석.
- 회사가 사업 단위(예: xStocks) 매출을 공개하지 않으면 추정하지 않고 "공개 없음".

## 7. 다듬기와 동시 작업 노하우(P1, P2)
- 큰 그림 빈칸 찾기: db/facts.csv에서 검증 상태가 단일 출처, 사용자 제공, 교차 확인, 회사 주장이면서 본문에 번호가 안 쓰인 사실을 회사별로 뽑는다(본문 F 번호 집합을 빼는 짧은 파이썬, 회사 칸은 startswith). 창업 배경, 사고 원인, 한국 비중, 파트너 거래대금이 여기서 나왔다.
- 줄 ID: 대분류 첫머리 "주장 :" 줄은 전체 그림이 링크한다. 길게 고치면 유사도 0.55 아래로 떨어져 ID가 끊긴다. 설명은 세부 불렛으로 내린다. build의 "찾지 못한 줄 링크" 경고로 확인.
- 여러 담당이 동시에 고칠 때: 파일을 담당별로 나누고, build는 `flock /tmp/kdx_build.lock python3 web/build.py`로만 돌린다. 이전 상태가 필요한 일(줄 ID 복구)은 시작 전에 본문과 web/line_ids.json 사본을 떠 둔다.
- ● 라벨을 길게 바꾸면 줄 ID가 끊긴다. 빌드 전에 web/build.py의 parse와 assign_ids를 web/line_ids.json 사본에 돌려 사라지는 ID가 없는지 미리 본다(scratchpad 미리보기 스크립트 방식).
- 회사 문서 원문 저장본(sources/R-*/)에만 있고 사실 행이 없는 문장이 있다(Ondo OUSG 한국 거주자 제외). 감사 때 원문 저장본을 grep해 사실 행으로 올린다(work/MANUAL/facts.csv).

## 8. 공식 모집단 수와 등록부(R-POP, 2026-11-17)

### 막힌 곳과 통한 공식 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| cftc.gov, sirt.cftc.gov(403, Cloudflare 봇 확인) | FCM 수는 NFA "Membership and Directories" 페이지의 Membership Totals(기준일 표기, FCM 79) | DCM, DCO 수는 대체 경로 없음. 사용자 로컬 브라우저 과제 |
| investor.gov(403 Access Denied) | eCFR 17 CFR 230.405 "Depositary share" 정의(ecfr.gov renderer API) | 법령 정의라 1차 |
| api.binance.com exchangeInfo(451, 지역 제한) | 없음. 사용자 로컬 브라우저 | 우회하지 않음 |
| api.gm.ondo.finance(403, API 키 필요) | app.ondo.finance/assets/<티커>on 개별 페이지 제목(404면 없음) | 전체 목록은 아님. 확인한 티커만 적는다 |
| dfs.ny.gov .../regulated_entities(404) | dfs.ny.gov/apps_and_licensing/virtual_currency_businesses 안의 Regulated Entities 표(39행) | 표에 기준일 없음, 열람일을 기준일로 |

### 쓸모 있었던 1차 출처 위치(모집단 수)
- FINRA Industry Snapshot 2026(finra.org/sites/default/files/2026-05/2026-Industry-Snapshot.pdf, 표지 September 2026): p.21 Table 2.1.3 규모별 회사 수, p.23 Table 2.1.5 BD/IA 겸업, p.49~52 Table 2.6.1~2.6.3 사업 모델과 세그먼트(ATS와 ECN, Fintech, Clearing and Carrying). 세그먼트별 회사 명단은 없다. 4.5절 야간 ATS 그림은 숫자 표가 없다.
- ESMA 임시 MiCA 등록부: esma.europa.eu MiCA 페이지에 CASPS.csv 링크(경로는 2024-12 폴더지만 파일은 계속 갱신, Last-Modified로 기준일). 열 ac_legal_basis(60조 통지와 63조 인가 구분), ac_serviceCode(거래 플랫폼 운영 여부), ac_authorisationEndDate.
- BMA: bma.bm/regulated-entities 한 페이지(약 6MB)에 전 업종 표가 숨김 행으로 다 들어 있다. Digital Assets Business 행의 License/Registration Type(Class F, M, T)과 Allowed Business Activities 전문. 활동 문구는 200자 넘게 길어 자르면 거래소 여부를 놓친다.
- ADGM FSRA 등록부: 화면이 쓰는 POST /api/fsrac/firms/listing/filter(JSON). companyType 165368(금융회사), 167132(인정기관), assetClass 165388(가상자산), firmStatus 165369(활성). 인정기관은 recognitionType, 취소일, 옛 이름(previousNames)까지 나온다.
- FINRA ATS 주간 자료 저장본(sources/ATS-1/finra_ats_firm_2026.json)은 야간 3사만이 아니라 전체 ATS가 들어 있다. Tier T1, T2만 더하면 NMS 주식 ATS 전체 순위와 비중을 낼 수 있다. Bruce의 MPID는 BOSS.
- xStocks 상품 목록(xstocks.fi/us/products) HTML 안에 slug, name, symbol이 전부 들어 있다(1,436종).
- Robinhood RHJ 공시 라이브러리(robinhood.com/eu/en/legal/rhj/) HTML에 종목별 Final Terms PDF 주소가 전부 있다(212건). 파일명에 기초자산 이름이 들어가 grep으로 찾는다.
- 금융위원회 보도자료 검색: fsc.go.kr/no010101?srchKey=all&srchText=<검색어>. 외국인 통합계좌 가이드라인은 2025-11-27(no010101/85748).

### 함정
- merge_db.py는 출처 번호를 담당 폴더 이름순으로 다시 매긴다. R-POP처럼 중간 이름의 새 폴더가 출처를 더하면 그 뒤 담당의 출처 번호(S-0365부터)가 밀린다. 사실 번호는 그대로. kb/ 문서가 S 번호를 직접 적으면 어긋날 수 있다.
- 같은 링크의 출처는 기존 S 번호로 합쳐진다(이번에 6건). 기존 원문을 재열람해 사실을 더할 때 링크를 기존과 똑같이 적으면 출처가 늘지 않는다.
- FINRA 세그먼트 수는 "그 유형의 모집단"으로는 쓸 수 있지만, 특정 회사가 그 세그먼트라고 쓰면 안 된다(FINRA가 회사별 분류를 공개하지 않음).
- 전체 ATS 대비 야간 3사 비중(2.43%)은 야간 시장 크기가 아니다. 낮 시간 기관 거래가 분모에 섞인다.

## 9. 줄 ID와 동시 작업 보강(L9)
- 대분류 제목을 바꾸면 줄 ID의 대분류 코드가 바뀌어 같은 문구도 새 ID를 받는다. 옮긴 줄의 옛 ID를 지키려면 빌드 직전 같은 flock 안에서 web/line_ids.json의 그 항목 sec 값만 새 코드로 바꾼다.
- 강조 표기(==, !!, **)는 줄 가운데에 넣으면 유사도 매칭으로 ID가 유지된다. 빌드 전에 사본으로 parse, assign_ids를 돌려 사라진 ID가 없는지 본다.
- 공유 scratchpad에는 담당별 하위 폴더를 쓴다.
- 등록부 중 회사 이름이 실제로 나오는 곳(ESMA, NYDFS, BMA, ADGM)만 "N곳의 하나"로 단정한다. FINRA 규모, 세그먼트와 SEC 집계는 명단이 없어 회사 공시에 기댄 해석으로만.

## 10. 덜어내기 절차(L10, CUT-K, CUT-2, CUT-3)
- 손으로 다시 쓰지 말고 git HEAD 원본에서 "지울 줄 번호 목록 + 바꿀 줄 사전 + 뒤에 붙일 줄 사전"으로 새 파일을 만든다. 남는 줄이 글자 그대로라 줄 ID가 유지되고 다시 돌려도 결과가 같다.
- 시작 전에 web/build.py의 parse와 assign_ids로 "ID, 대분류, 문구, 링크한 파일"을 뽑는다(line_ids.json은 복사본). 다른 파일이 링크한 줄은 남기고, 같은 본문 안에서만 링크된 줄은 지운 뒤 링크를 남은 줄로 바꾼다. 끝나면 사라진 ID와 `{xx-0000}` 링크를 대조한다.
- 줄 수는 Python 정규식 `^\s*[●★-] `로 센다(grep -E는 다바이트 묶음을 잘못 읽음).
- 짧은 줄의 가운데를 크게 지우면 유사도가 0.55 아래로 떨어져 새 ID가 붙고 답이 화면에서 사라진다. 빌드 전 옛 ID와 새 문구의 비율이 0.7 미만인 것을 확인한다.
- "쉽게 말하면"을 지우면 대분류 맨 위에 머리 ● 없는 ★가 남는다. 주장 ●을 앞으로 옮긴다. 그림 해설을 지우면 그림 줄도, 인용 머리를 지우면 ①②③도 같이 지운다.
- 정체 카드와 성과 장의 같은 숫자는 전체 그림이 링크한 쪽을 남긴다.
- "인가와 인수로 열린 것" 묶음이 흩어진 등록일, 개장일, 인가 목록 줄을 대신해 줄이 오히려 준다. 근거 찾기: 인가 이름(MiCA, FCM, DCM, DCO, ADGM, CNV)으로 db/facts.csv 검색, EU 인가 범위는 ESMA 등록부 서비스 코드 b(거래 플랫폼)로 거래소형과 중개형을 가름. "규제에 맞춘 것"은 하던 영업을 옮겼다는 1차 문장이나 등록부의 이전 지위(IAPD 면제보고자문사 철회일)로만. 인가가 계기가 아닌 것(Regulation S, 백업 계약)도 같은 묶음에 적는다. 약관이 "라이선스 아님"이라 밝힌 등록은 "등록만".
- 병렬 담당은 scratchpad/<담당>/ 하위 폴더를 처음부터 쓴다.
