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
- 전체 그림(ov-) 줄은 다른 파일이 링크하지 않으면(`grep -rn "{ov-" companies kb` 0건) 과감하게 합칠 수 있다. 회사별 연표는 회사마다 ★ 한 줄 "시점 항목(방법) → ..."에 그 회사 범위 장 주장 줄 링크 하나. 같은 문장 틀을 반복하는 묶음은 한 줄에 회사별 괄호로.
- 뜻 줄을 지우기 전에 db/terms.csv의 용어 칸을 검색한다(화면 용어 풀이에 있으면 지움). check_body는 전체 그림의 근거 없는 ● 줄도 잡으니 정의 ● 줄에는 관련 본문 링크를 붙인다.

## 11. 스토리라인 리서치(회사별 막힌 곳, 통한 경로, 함정, 2026-11-17)
공통: 회사 "왜"는 회사 블로그, 실적 서한 전수(sitemap)에서, 인가 순서의 이유는 회사가 말하지 않으면 제도의 처리 기간(eCFR, FINRA 규칙)으로, 막힌 매체는 같은 기사를 실은 전재 사이트로. 축과 어긋나는 사실(자체 앱, 자체 거래 플랫폼)은 최근 6개월 글에 있으니 축을 쓰기 전에 훑는다.

### Binance
## 통한 경로
- binance.com 블로그와 공지는 curl에 202(봇 확인)로 막힘. Binance 보도자료는 prnewswire.com/news/binance/ 목록 페이지에 최근 20건 주소가 모두 있고, 각 보도자료 본문이 curl로 열림(옵션 출시, TradFi 무기한선물, 9주년, 첫 주 주식 데이터, Binance Pay, Capital Connect). AAP(aap.com.au, aapnews.aap.com.au) 사본도 열림.
- Binance 보도자료의 회사 숫자(주식 연계 무기한선물 월 거래대금, 기관 이용자 증가율, 슈퍼앱 목표)는 같은 날 매체 기사가 그대로 옮기므로 보도자료 원문을 1차로 쓴다.
- ESMA MiCA 등록부 CASPS.csv(Last-Modified로 기준일)를 grep하면 "MiCA 인가 없음"을 1차로 확인할 수 있다(Binance 0행).
- cointelegraph.com, decrypt.co, kitco.com, financemagnates.com, news.bizwatch.co.kr, thenationalnews.com은 curl로 열림. theblock.co는 경로에 따라 403(www 없는 news 경로와 post 경로).
- 아부다비 정부 미디어오피스(mediaoffice.abudhabi) 보도문에 UAE 직원 수(5,000명 중 1,000명)가 있어 Khaleej Times 단일 출처를 1차로 올릴 수 있었음.

#### 함정
- 기존 DB와 본문은 Binance 주식 무기한선물 시작을 2026-10-29로 적었으나, 2026-09-01 옵션 보도자료에 2026-01 주식 연계 무기한선물 거래대금(4.109억 달러)이 있고 TradFi 무기한선물 상품군은 2026-01-08(금, 은)부터임. 10-29와 11-12는 종목 추가 공지. 2층 문구 정정 필요(이번 범위 밖이라 고치지 않음).
- Finance Magnates 기사 날짜(2026-07-15)와 내용(6월 출시)이 어긋남. 매체 날짜보다 보도자료 날짜를 기준으로 쓴다.
- 회사 9주년 보도자료의 "가상자산 보유자의 43%"는 회사 추산(분모 7.41억 명은 업계 추정)이라 회사 주장으로만.

### Coinbase
## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| coinbase.com/blog(403) | Markets Media가 "By Coinbase"로 전문 전재(INTX 출범, Coinbase Clearing 승인, tGBP 상장). curl로 열림 | 회사 발표 문장 그대로라 1차 확인으로 씀 |
| investor.circle.com(403) | circle.com/blog 같은 글(2023-08-21 USDC 다음 장, 두 CEO 공동 서명) | Circle과 Coinbase 수익 배분 원문 |
| theblock.co(curl 403, WebFetch DNS 실패) | 같은 사건의 cointelegraph, decrypt, financemagnates 기사 | 셋 다 curl 200 |
| cftc.gov DCO 등록 명령 PDF(403) | 회사 발표 전재(Markets Media)와 매체 기사 | 등록일은 기존 F-1123 |
| sec.gov 10-K(403) | FairX 인수 금액(검색 요약 2.75억 달러)은 원문 미확인이라 쓰지 않음 | |

#### 쓸모 있었던 1차 출처 위치
- Coinbase 과거 주주서한: s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf, .../2021/q4/Coinbase-Q421-Shareholder-Letter.pdf. 파일 이름 규칙이 분기마다 달라 추측 주소는 404(Q1-2025, Q3-2025, Q4-2024). 검색으로 정확한 이름을 먼저 찾는다.
- Q2 2025 서한: Everything Exchange 첫 표현(p.7), 파생을 키우는 이유(75%, p.8), 스테이블코인 수익을 플랫폼 안과 밖 USDC로 나눈 표(p.4~6), ETF 보관 점유율 80% 이상(p.6).
- Q4 2021 서한 p.10 표: 상장 첫해 수익 구성(거래 93%, 구독과 서비스 7%)과 2020 비교. "반복 수익이라 안정" 문장(p.11).
- Q3 2026 AMA, 분석가 콜 녹취(inputs/manual/B03_*): Circle 관계(협력과 경쟁, 50%, 30%), 청산소를 받은 이유(예측시장 자체 계약), 결제 계약사, Everything Exchange 외환 발언.

#### 함정
- The Clearing Company(2025-11 DCO 신청 발표)와 Coinbase Clearing LLC(CFTC 신청일 2025-11-14)가 같은 신청인지 공개 자료로 확인되지 않는다. 검색 요약 둘이 서로 반대로 말했다. 별개 사실로 쓰고 잇지 않는다.
- link_story.py는 링크 칸이 로컬 경로인 사실(주주서한 PDF 등)을 대괄호 없는 번호로 바꾼다. 한 줄에 그런 번호만 있으면 check_story가 "근거 없음"으로 잡으므로 링크가 있는 사실을 같이 붙이고, 남은 번호 뒤에 "(주주서한 PDF)"처럼 출처 종류를 붙였다.
- 새 사실의 링크를 IR 폴더 주소(.../2026/q3/)로 두면 기존 F-1221, F-1222와 같은 방식으로 링크가 걸린다(원문 위치 칸에 로컬 파일 이름).
- 외환(FX)은 2026 우선순위 정의에만 있고 출시 상품은 없다(tGBP 상장, CEO 발언 수준). 기둥별 실현 여부를 볼 때 "이름뿐인 기둥" 후보로 먼저 표시한다.

### Dinari
## 통한 경로
- Reuters 기사 원문(reuters.com)은 막히나, 같은 기사를 실은 지역 방송 사이트(whbl.com 등 Reuters 전재)가 curl로 열림. 본문은 HTML 안 기사 블록에서 "By <기자> (Reuters)" 이후를 잘라 읽음.
- 인가 "순서의 이유"는 회사가 말하지 않으면 제도의 처리 기간으로 근거를 세움: 명의개서대리인 등록 효력(17 CFR 240.17Ac2-1, 제출 30일째, eCFR renderer API로 열림)과 FINRA 신규 회원 심사(FINRA Rule 1014, finra.org 규칙 페이지 curl로 열림). 회사 사실(법인 설립일, 승인일)과 나란히 두면 해석 근거가 됨.
- Alpaca 비교: docs.alpaca.markets/docs/about-broker-api(이용 형태 증권사, RIA), alpaca.markets/tokenization(토큰 발행자 아님 고지) 둘 다 curl로 열림.
- Dinari 사이트 전수조사 저장본(KDX_사이트전수조사_인수인계/work/dinari/raw/)에 블로그, 사례 연구, docs가 다 있어 "왜" 문장(B2B 이유, 목표 문장, 파트너 KYC 방식)을 grep으로 찾는 것이 가장 빠름. 자체 앱 존재는 sbt.dinari.com, app.dinari.com 저장본 제목("Dinari Trading App")과 2023 추천 프로그램 글로 확인.

#### 막힌 곳
- theblock.co, thedefiant.io, blockworks.co, fortune.com, cryptonews.com, sec.gov(SEC Crypto Task Force의 WilmerHale Dinari 메모 2025-05) 모두 403 또는 허용 밖. WebFetch는 blockworks.co DNS 실패(세션 허용 밖).
- 창업자가 명의개서대리인을 먼저 받은 이유를 직접 말한 원문은 찾지 못함(Fortune 2026-08-04 기사에 관련 발언이 있다는 검색 요약만 있음, 403). 사용자 로컬 브라우저 과제 후보.

#### 함정
- 회사가 "자기 고객 화면 없음"처럼 보여도 자체 앱이 있음(2023 자체 웹 앱, 2026 미국판 Dinari Trading App). 축 문장과 어긋나는 사실은 스토리라인에서 "자체 앱과 파트너 판매 비중은 공개 없음"으로 정직하게 적음.
- 사례 연구 거래대금은 파트너마다 집계 기간이 다름(Cadana 2026-01-01~06-15, Meru 2026-01-01~07-15, Hyperliquid 첫 달 기준일 미표시). 합산하지 않음.
- 판매 국가 수는 글마다 다름(60+, 70+, 85+, 91, 92). 시점과 기준을 붙여 나열하고 하나로 고르지 않음.

### KR
- payward.com 전수 목록: www.payward.com/sitemap.xml은 301로 /sitemaps/sitemap.xml에 감(curl -L). 보도자료 약 80건 주소가 다 나옴. 분기 실적은 press-release/q1-2026-financial-highlights, q2-2026-financial-highlights, payward-q3-2026-financial-highlights, 2025-financial-highlights.
- 사업 기둥의 첫 시점: Q2 2026 서한(2026-08-14)이 네 기둥을 처음 정의, Q1 2026(2026-05-18)은 Direct to Consumer와 B2B 두 묶음. Q3(2026-11-13)에 AI가 다섯째. 코인데스크 인터뷰(2026-09-26)는 재설명.
- 수익 지표가 Q3에 바뀜: Q2까지 조정매출 기준 "Asset-Based and Other Revenue" 비중(55%에서 60%), Q3부터 TPM 기준 거래, 자산, 접근 세 갈래(46%, 50%, 52%). 두 계열은 이어 붙이지 않는다. 각 정의 원문은 Q3 본문과 각주 [3], [6], [8].
- payward.com/asset-management, /banking 페이지에 "Coming soon" 표기가 있어 이름뿐인 기둥 판단의 1차 근거가 됨.
- 함정: xStocks EU 판매 시작은 2025-09-10(blog.kraken.com/product/xstocks/now-available-to-eu-clients, PEDSL CySEC). Backed 투자설명서의 2026-05-04 계약은 지정참가자(AP) 계약이지 판매 시작이 아님.
- EU 파생 출시 1차: blog.kraken.com/news/euro-reg-futures(2025-05-20). Business Wire 원문은 403.
- 경쟁 B2B 인프라 공식 홈페이지는 curl로 열림: zerohash.com, paxos.com, anchorage.com, bitgo.com, fireblocks.com, alpaca.markets/broker. coinbase.com은 403이라 docs.cdp.coinbase.com(및 /llms.txt)과 Markets Media 기사(CaaS, 2025-08-04)로 대신함.
- Gemini 블로그(gemini.com/blog/...)는 curl로 열림. 2025-06-27 EU MSTR 1종목, Dinari 발행.
- 공유 scratchpad 루트에 둔 스크립트를 다른 담당이 덮어씀(h2t.py). 담당별 하위 폴더에 스크립트까지 두어야 함.
- B2B 이용사 수는 발언마다 다름: Reap 인수 발표(2026-05-07) Sethi "1,900 B2B partners", 코인데스크(2026-09) "최소 25곳". 하나로 고르지 않음.

### Ondo
- Ondo 블로그 전수: ondo.finance/sitemap.xml 안 blog 주소 약 190건, curl로 본문이 서버 렌더되어 열림. 날짜는 본문의 "분류 • Mon D, YYYY" 줄로 확인. 비전, 계획 변경, 유통처 발표가 거의 다 여기에 있음.
- 옛 글 제목이 새 이름으로 바뀌어 있음(2024-02 "Introducing Ondo Global Markets" 주소는 그대로인데 화면 제목은 "Introducing Ondo Stocks"). 주소 슬러그로 옛 이름과 첫 발표 시점을 가린다.
- 비전, 미션 원문: 2024-01-11 ondos-journey-vision...(발행 플랫폼 수렴 전망, 상장 증권 100조 달러), 2025-02-03 towards-the-open-economy(미션 문장), 2025-02-04 global-markets(설계 변경 이유), 2026-06-01 onward-...(위층 이동). "왜 오래 걸렸나"는 계획 발표 글과 출시 글을 나란히 보면 나온다(허가형 → 자유 이전 토큰).
- 유통처가 밝힌 수치는 유통처 공식 글로 1차 승격: Bitget 안 Ondo 비중 73%에서 89%는 bitget.com/blog/articles/bitget-tokenized-stocks-etfs-ondo-expansion(2026-03-17)에 원문이 있음(기존 CFOtech 보도 대체 가능).
- 회사 발표 보유자 수는 시점마다 정의가 다름(2026-08 "holders" 186,636, 2026-10 "cumulative holders" 45만 이상). 이어 쓸 때 정의를 같이 적는다.
- 회사 TVL(Ondo 발표 13억 달러)과 rwa.xyz 분산 가치(8.99억 달러)는 기준이 달라 같은 줄에서 순위 비교에 쓰지 않는다.
- 함정: "자기 거래소 없음" 축과 어긋나는 사실(2026-07 Ondo Perps 직접 운영, Oasis Pro ATS 보유)이 블로그 뒤쪽 글에 있음. 축 서술 전에 최근 6개월 글을 훑는다.

### Robinhood
- robinhood.com/newsroom/<slug>/ 는 curl로 열림(investors.robinhood.com, globenewswire.com은 403). 글 목록은 사이트 전수조사 inventory.csv의 sitemap-newsroom.xml 행(473건)에서 slug로 찾는다. 2016 Gold, 2017 옵션, 2018 가상자산, 2018 자체 청산, 2019 영국 발표, 2022 Ziglu, 2023 X1 같은 옛 글도 남아 있다. 날짜는 HTML 안 "datePublished".
- 과거 실적 발표: 전수조사 사본에 2023 Q1에서 Q4, 2026 Q2, Q3 보도자료가 있다. 2024 Q4 보도자료는 GlobeNewswire 배포본을 실은 manilatimes.net(tmt-newswire/globenewswire 경로)가 curl로 열림.
- 10-Q(node__16931__html.md) MD&A에 매출 항목별 비중 표(옵션, 이벤트 계약, 암호화폐, 주식, 순이자 세부, 기타 안 Gold 구독료)가 있다. 수익 구성 변화는 이 표와 2023 보도자료를 이어 쓰면 된다. 위험요인에 창업자 의결권(12% 지분, 50% 초과 의결권), 규제 절에 Bitstamp 법인별 인가가 있다.
- 사업 기둥 원문은 2026 Q2, Q3 보도자료 Highlights 표제(#1 Platform for Active Traders, #1 in Wallet Share for the Next Generation, #1 Global Financial Ecosystem). 처음 쓴 시점을 보도자료로 확정하지 못함(2024 Q4 보도자료는 Active Traders 표제만). 통화 녹취 사이트(roic.ai, marketbeat)와 investing.com은 403.
- 막힌 매체: theblock.co, crowdfundinsider, blockworks(403), yahoo(429). 같은 사건은 financemagnates.com, bankingdive.com, amp.cnn.com이 열림.
- 함정: Robinhood 예측시장은 Kalshi를 대체한 것이 아니라 Kalshi, ForecastEx, Rothera, Crypto.com으로 나눠 보냄(2026-09 뉴스룸). "파트너 뒤 인수"를 "교체"로 쓰지 않는다.

## 12. 공식 전략 틀(기둥, 우선순위) 찾기와 캡처(2026-11-17)
공통: 틀은 분기 서한과 실적 보도자료 머리, 연말 CEO 서한, 홈 화면에 있다. 처음 나온 시점은 직전 분기 서한부터 거슬러 올라가며 같은 낱말을 찾는다. 캡처는 Playwright 기본 Chromium(위장 없음)으로 원문 화면을 찍고 captures/pillars/<회사>_<짧은이름>.png로 둔다. 결과물에는 공백 표시를 옮기지 않는다.

### PILLARS-A
## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| binance.com 블로그, About, Mission(curl 405, 봇 확인) | Playwright 기본 Chromium(UA 그대로)으로 열림. 응답 202 뒤 본문 렌더 | 위장 없이 열린 것. 블로그 From our CEO 목록 /en/blog/from-our-ceo |
| investors.robinhood.com 보도자료와 static-files(403) | investingnews.com/robinhood-reports-<분기>-results/ (GlobeNewswire 전재, Playwright 캡처 가능). 2025 Q1, Q2는 404 | finviz, globenewswire.com은 Playwright에서도 403 |
| Robinhood 실적 통화 녹취(IR 403, marketbeat, roic.ai 403) | bullfincher.io/companies/robinhood-markets/earnings-call/fy2023-q4 형식(제3자 녹취, 단일 출처) | insidermonkey는 유료 벽에 잘림 |
| Coinbase 과거 주주서한(sec.gov 403) | IR CDN 이름 규칙이 해마다 다름: 2024/q4/Q4-24-Shareholder-Letter.pdf, 2025/q2/Q2-2025-Shareholder-Letter.pdf, 2025/q4/coin-20260212.pdf. 2023 Q4는 못 찾아 Markets Media 전재로 | 실적 통화 녹취는 2022/q4/Coinbase-Q422-Earnings-Call-Transcript.pdf 형식 |
| web.archive.org(연결 끊김) | 없음 | 문장이 처음 걸린 날짜는 로컬 브라우저 과제 후보 |

#### 찾는 순서
- 비상장사(Payward)는 분기 실적 글(payward.com/press-release/q<n>-<연>-financial-highlights)이 사실상 주주서한이다. sitemap.xml에 보도자료 전부가 있다.
- "처음 나온 시점"은 다음 분기 서한이 알려 줄 때가 많다(Payward Q3: "Last quarter we introduced four pillars", Coinbase Q4: "In 2025, we debuted our flywheel"). curl 텍스트 변환은 굵은 글씨 단락을 빠뜨릴 수 있어 Playwright innerText로 다시 확인한다.
- 실적 보도자료 표제가 우선순위 이름으로 바뀌는 시점과 CEO 통화에서 말한 시점이 다르다(Robinhood: 통화 2025-02, 보도자료 표제 2026-02). 둘을 나눠 적는다.

#### 함정
- 번역 전재(htx.com 등)에만 있는 숫자는 회사 영문 원문에 없을 수 있다(Binance 준법 인력 1,280명).
- 같은 회사 사이트 안에서도 미션 문장이 페이지마다 다르다(Binance About과 Mission).
- 다른 담당(STORY-*)이 같은 서한에서 사실을 먼저 넣었을 수 있다. 쓰기 전에 db/facts.csv를 링크와 키워드로 검색해 겹치지 않게 한다.

### PILLARS-B
## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| www.otcmarkets.com(curl 응답 없음, WebFetch DNS 실패: 세션 네트워크 밖) | 실적 발표 배포 사본: pubt.io(Public.com), stockwatch.com, prnewswire.com(2016 등 옛 발표) | 연차보고서 본문은 사용자 로컬 브라우저 과제 |
| globenewswire.com, app.researchpool.com(403) | 위 사본 | |
| web.archive.org(프록시 터널 끊김). archive.org/wayback/available API는 응답하지만 스냅샷 본문은 못 받음 | 회사 블로그 날짜로 거슬러 올라감 | 홈 문구의 첫 게시일은 못 찾음 후보 |
| Ondo 블로그 일부(Ondo Stocks 분류 글, 예: towards-the-open-economy): 브라우저에서 "Access Restricted, not accessible in your jurisdiction" | 같은 문장이 있는 다른 분류 글(Announcement)을 찾아 캡처 | 지역 제한 우회 안 함 |
| ondo.finance 홈 첫 화면 미션 문장(스크롤 애니메이션, Playwright 스크롤로 안 나타남) | 같은 문장을 쓴 블로그 글로 캡처 | |

#### 쓸모 있었던 방법
- 워드프레스 사이트(blueocean-tech.io)는 /wp-json/wp/v2/posts?per_page=100&page=N 과 /pages 로 전 글과 페이지를 날짜, 수정일과 함께 받는다. "처음 나온 시점"을 문구 grep으로 찾기 좋다.
- 회사 블로그 전수 내려받기(ondo sitemap 190건, dinari 99건, bruce 95건) 후 문구별 첫 등장 날짜를 뽑으면 틀의 시작 시점이 나온다. 보도자료 끝 회사 소개 문단(About)이 미션 문장 변천을 가장 잘 보여 준다.
- 그림 안의 틀(Ondo 2026-06-01 네 층 스택)은 텍스트 검색에 안 걸린다. 캡처를 눈으로 확인하다가 발견했다. 이미지 주소(cdn.sanity.io)를 전 글에서 대조하면 그 그림이 처음 쓰인 글을 찾을 수 있다.
- 표 캡처는 Playwright locator('table').filter({hasText}).screenshot()이 좌표 계산보다 안정적(지연 로딩으로 좌표가 바뀜).

#### 함정
- 회사가 "pillars"라 부르지 않는 홈 화면 블록을 틀로 적을 때는 "회사가 틀이라 부르지 않음"을 명시한다(Bruce 홈 네 블록, Blue Ocean 방향 셋).
- 같은 날 같은 회사가 세 요소를 다르게 적기도 한다(Ondo 2025-02-03: 플랫폼, 자산, 인프라 대 자산, 인프라, 생태계). 하나로 고르지 않고 둘 다 적는다.
- 인프라 항목의 실체가 바뀐다(Ondo Chain L1 → Ondo Network 실행 계층). 항목 이름만 보고 연속이라 쓰지 않는다.

## 13. 엑셀 내보내기(tools/export_briefs_xlsx.py, 2026-11-17)
- python3 tools/export_briefs_xlsx.py → export/KDX_해외사례_브리핑.xlsx. 시트: 목차, 축과 가설, 전략 틀 비교, 회사 6곳, 야간 ATS.
- 사진 배치: 전략 틀 캡처는 스토리라인 3절 아래, 근거 캡처(work/*/sources.csv의 캡처 칸 → 사실 번호)는 그 사실을 인용한 줄 아래, 나머지는 시트 끝 참고 캡처. 사진 옆 칸에 무엇, 해석(tools/capture_notes.py), 파일 경로.
- 함정: 위키백과 주소처럼 괄호가 든 URL은 괄호 짝을 허용하는 정규식으로 뽑는다. 표 구분선 "|---|"를 문서 끝 표시("---")로 잘못 자르지 않는다. 사진은 표시 크기 1.5배 JPEG로 줄여 넣는다(31MB → 8MB). 행 높이는 한글 기준 C열 한 줄 약 44자. 결과물에서 공백 표시(비공개, 미확인 등)는 사진 설명까지 거른다.
- 확인: soffice --headless --convert-to pdf 후 pdftoppm으로 한 쪽 렌더(쪽 맞춤 가로 1장).
- 웹 브리핑 탭(web/brief_data.py): 엑셀과 같은 배치를 데이터로 만들어 build.py가 D.briefs로 넣는다. 사진은 web/brief_img/*.jpg(폭 900px, 품질 78)로 따로 두고 상대 경로로 참조, Artifact 게시 때 files 지도로 함께 올린다(페이지 안 data URI로 넣으면 16MB 한도를 넘음).

## 14. 미국 증권사 비교 숫자(2026-11-17 추가)
- Interactive Brokers 월간 지표: interactivebrokers.com/mkt/getFileNew.php?file=latestMetricPR 가 curl로 열리나 Java 직렬화 덩어리 안에 PDF가 들어 있음. %PDF부터 %%EOF까지 잘라 pdftotext로 읽음.
- Charles Schwab 실적: sec.gov(403), pressroom.aboutschwab.com(Cloudflare 확인 화면), aboutschwab.com IR(403), finance.yahoo.com(curl 429, WebFetch 허용 밖) 모두 막힘. 우회하지 않고 검색 결과 3건 일치로 DB에 넣되 검증 상태에 "사용자 로컬 브라우저 확인 대기"를 적음.

- (2026-11-19) WebFetch 허용 밖: sensortower.com, esg.robinhood.com, aboutschwab.com, theblock.co. curl로는 investors.robinhood.com과 sec.gov가 403. Robinhood 2026 3분기 실적 발표와 10-Q는 sources/S2-RH/ir_q3-2026-results.md, ir_10q_q3-2026_node16931.md에 이미 저장돼 있으니 먼저 grep한다.

## 15. 화면 메모 읽기(2026-11-17 추가)
- 화면(Artifact)의 메모는 브라우저 저장과 함께 화면 DB의 memos 모음에 저장됨. 다음 회차는 "메모 보내기" 파일을 기다리지 말고 ArtifactData list(url=화면 링크, collection=memos)로 바로 읽는다. 화면 메모는 view, brief, quote(고른 글) 칸이 있고, 본문 줄 메모는 lid(줄 ID)가 있다.
