# 브라우저 확인이 필요한 빈칸 (kb/gap_audit.md의 "없음"과 "일부 있음")

방법은 LOCAL_GOOGLE_TASK.md와 같다.
1. 사용자 컴퓨터 Chrome에서 google.com으로 검색한다. 한국어도 된다. 구글 AI 요약이 나오면 요약 문장은 근거로 쓰지 않고 요약 옆 출처 링크를 눌러 원문 페이지로 들어가 근거 문장을 찾는다.
2. 출처 우선순위는 법령, 감독기관, 회사 공식, 공시 > 주요 매체(어느 매체인지 표기) > 위키백과(각주를 타고 원문으로). 로그인, 결제, 개인정보 화면은 건너뛰고 캡차는 사용자에게 맡긴다.
3. 결과는 채팅 표(번호, 항목, 찾은 내용, 출처 종류, 링크, 원문 근거 문장, 날짜, 캡처 파일)와 캡처 zip으로 준다. 못 찾으면 "못 찾음"과 검색어, 열어 본 곳을 적는다.
4. 아래 G 번호가 번호 기준이다. LOCAL_GOOGLE_TASK.md에 같은 질문이 있으면 그 번호를 적었고 한 번만 확인한다.

## A. 한국 제도

### G1. 해외 주식 토큰의 한국 법상 분류에 대한 당국 해석
- 질문: 금융위, 금감원이 해외에서 발행된 주식 토큰(채무증서형, 수익권 증서형, 파생계약형)을 자본시장법상 어떤 증권이나 파생상품으로 봤는가?
- 이미 본 출처: 법령 문언만(KR-자본시장법-3, 4, 4-⑤, 4-⑨). 당국 해석 없음. F-1020은 MMF 토큰 회신 보도 1건
- 찾을 곳: https://www.fsc.go.kr/no010101 (금융위 보도자료 목록, 검색어 "토큰증권", "해외", "주식 토큰"), https://better.fsc.go.kr (금융규제 민원포털 법령해석 회신 검색), https://www.law.go.kr 법령해석례 검색 "증권 해당 여부 토큰", https://www.fss.or.kr 보도자료. 구글: "해외 주식 토큰 자본시장법 증권 해당 금융위"
- 채울 곳: regulation_compare.md "해외 주식 토큰의 한국 법상 성격" 표 해석 자료 열, Ondo, Kraken, Robinhood, Dinari 본문 "한국 시장과의 차이"
- 브라우저가 필요한 이유: 민원포털과 법령해석례는 검색 화면(동적 페이지)이고 클라우드 IP에서 fss.or.kr, 일부 fsc.go.kr이 열리지 않았음

### G2. 조문 원문 열람과 laws.csv 등록
- 질문: 제4조제3항, 제4항, 제7항, 제8항, 제5조, 시행령 제7조제4항제6호, 제11조, 제120조, 제184조 원문이 아래 주소에서 열리는가, 시행일은 언제인가(시행령 제120조는 2026-07-28 개정 표시)?
- 이미 본 출처: 국가법령정보센터 전문 저장본 work/KR-1/raw/law.txt, decree.txt(시행 2026-11-13)
- 찾을 곳: https://www.law.go.kr/법령/자본시장과금융투자업에관한법률/제5조, https://www.law.go.kr/법령/자본시장과금융투자업에관한법률시행령/제120조, 같은 형식의 제11조, 제184조, 제7조
- 채울 곳: db/laws.csv 신규 행, regulation_compare.md 새 절의 링크 확인 표시 제거
- 브라우저가 필요한 이유: 조문 화면이 동적 렌더링이라 클라우드 수집은 전문 덩어리만 받음. 조문별 주소 작동 확인 필요

### G3. 국내 투자자가 해외 토큰을 합법적으로 사는 경로와 금융위 회신 원문
- 질문: 한국 거주자가 해외 발행 토큰증권, 주식 토큰을 살 수 있다고 본 당국 판단이 있는가? F-1020 회신(2026-08 말)의 원문과 대상은 무엇인가?
- 이미 본 출처: 블록미디어 2026-09-01(https://www.blockmedia.co.kr/archives/1134616, 금융위 원문 미열람), F-1019(MTN 2026-07-16)
- 찾을 곳: 위 블록미디어 기사의 출처 링크, https://www.fsc.go.kr/no010101 에서 2026-08~09 보도자료, 구글 "해외 토큰증권 국내 거주자 재판매 금융위 회신"
- 채울 곳: regulation_compare.md 새 절 경로 표 마지막 줄, Ondo와 Dinari 본문 한국 시장과의 차이
- 브라우저가 필요한 이유: 검색 화면과 매체 원문 링크 타기가 필요하고 금융위 일부 페이지가 클라우드 IP에서 302로 본문이 안 받아짐

### G4. 하위법규 개정 확정 여부와 제4조제1항 개정 전 원문
- 질문: 2026-10-02~11-11 입법예고된 시행령 둘과 규정 셋은 확정 공포됐는가, 조문 번호와 시행일은? 2026-02-03 삭제된 자본시장법 제4조제1항 단서 제1호, 제2호의 삭제 전 내용은?
- 이미 본 출처: https://www.fsc.go.kr/no010101/87838, https://www.fsc.go.kr/po010101/87650, https://www.fsc.go.kr/no010101/86064
- 찾을 곳: https://www.law.go.kr 자본시장법 시행령 연혁(공포 예정 포함)과 신구조문 대비표, https://www.fsc.go.kr/no010101 최신 보도자료
- 채울 곳: regulation_compare.md 새 절 시행일 표, kb/regulation_kr.md 3
- 브라우저가 필요한 이유: 연혁과 신구조문 대비는 동적 화면이고 PDF 별첨은 브라우저로 내려받아야 함

## B. 미국 안 판매

### G5. Ondo 미국용 보관형의 매수 대상과 판매 경로
- 질문: 2026-07 출시된 IVV, MU 토큰을 미국 개인과 기관 중 누가 어디서 살 수 있는가?
- 이미 본 출처: https://ondo.finance/blog/ondo-launches-tokenized-securities-in-usa (대상 없음) [F-1128][F-1129]
- 찾을 곳: https://docs.ondo.finance/ondo-stocks/eligibility, https://ondo.finance (미국 페이지, 메뉴), https://ondo.finance/blog 이후 글, 구글 "Ondo tokenized securities US eligibility Oasis Pro"
- 채울 곳: Ondo, B 상품 구조 "미국용 보관형"과 C 최종 투자자
- 브라우저가 필요한 이유: 앱과 문서 페이지가 동적 로딩이라 셸 수집에서 빈 화면

### G6. SEC 상장주식 토큰 혁신 면제를 실제로 이용하는 회사
- 질문: 2026-09-17 명령 이후 TSV나 Covered Firm으로 공개 고지(Notice)를 낸 회사가 있는가, 누구인가? Dinari 서술(F-0294)과 맞는가?
- 이미 본 출처: https://www.govinfo.gov/content/pkg/FR-2026-09-22/html/2026-19388.htm, F-0294, F-0642, F-0898, F-1362
- 찾을 곳: https://www.sec.gov/comments/4-927/4-927.htm (File No. 4-927 의견서 목록, 주소 형식은 SEC 관례), https://www.sec.gov/newsroom 보도자료, 구글 "Tokenized NMS stock exemption TSV notice launches" 후 회사 블로그. 이 주소는 sec.gov라 클라우드에서 열리지 않음
- 채울 곳: regulation_compare.md 토큰화 주식 거래 시장 줄, Dinari, Coinbase, Kraken 본문 한국 시장과의 차이 또는 제약
- 브라우저가 필요한 이유: sec.gov 클라우드 IP 403, 의견서 목록은 검색 화면

## C. 실물 없는 노출

### G7. 주식 무기한선물 규모와 주요 거래 장소
- 질문: 거래소별(Binance, Bybit, OKX, Hyperliquid 등) 주식 무기한선물 24시간 거래대금과 미결제약정 합계는? 업계 전체 규모를 낸 공식 통계나 보고서가 있는가?
- 이미 본 출처: Hyperliquid API F-1134~F-1137, Binance 화면 F-1238, F-1239, TP-501(CoinDesk Research, Bullish 의뢰), kb/perp_vs_spot.md
- 찾을 곳: https://www.binance.com/en/markets/futures, https://www.bybit.com/en/trade/futures/, https://www.okx.com/markets/futures, https://app.hyperliquid.xyz/ , 구글 "equity perpetual futures open interest volume exchanges 2026"
- 채울 곳: kb/perp_vs_spot.md(화면 탭), Binance 본문 사업 범위(자산 2)
- 브라우저가 필요한 이유: Binance와 Bybit가 클라우드 IP를 차단(451, 403)하고 시세 화면은 동적. 본 화면 값은 한 시점 값이라 시각을 적을 것. LOCAL_GOOGLE_TASK #14와 별개

### G8. 과거 합성 주식 사례 Mirror Protocol, Synthetix와 결말
- 질문: Mirror Protocol과 Synthetix의 합성 주식은 언제 어떻게 운영됐고 어떻게 끝났는가(종료, 규제 조치, 소송)?
- 이미 본 출처: 없음(IOSCO 보고서 주석 118이 Terra/Luna 붕괴 한 줄)
- 찾을 곳: https://www.sec.gov/enforcement-litigation/litigation-releases 에서 Terraform Labs 사건, https://docs.mirror.finance 와 종료 공지, https://blog.synthetix.io 와 https://governance.synthetix.io 의 합성 주식 종료 제안, 구글 "Mirror Protocol mAssets SEC Terraform complaint security-based swaps", "Synthetix sTSLA sunset"
- 채울 곳: Robinhood, Kraken 본문 B 상품 구조의 합성형 설명 또는 kb/overview.md 선례
- 브라우저가 필요한 이유: sec.gov 403, 프로젝트 사이트는 동적 문서 화면. 매체 1곳 이상으로 확인하고 회사 발표는 따로 표기

## D. 깊이

### G9. Ondo 국채 토큰 과거 잔액 추이
- 질문: OUSG, USDY 발행 잔액과 국채 토큰 시장 규모의 2025년, 2026-01 시점 값은?
- 이미 본 출처: 2026-11-13, 11-16 값 F-1315, F-1318, F-1320~F-1322
- 찾을 곳: https://app.rwa.xyz/treasuries (기간 선택 차트), https://defillama.com/protocol/ondo-finance (제3자 TVL 차트), https://ondo.finance 홈 TVL, 구글 "tokenized treasuries market size 2025 Ondo share". LOCAL_GOOGLE_TASK #18과 합침
- 채울 곳: Ondo, 국채 토큰 사업 "발행 잔액과 시장 내 위치"
- 브라우저가 필요한 이유: 차트는 동적 렌더링이고 과거 시점은 로그인이나 별도 경로 필요. 캡처에 날짜가 보이게

### G10. Robinhood 비상장 토큰의 개별 약관, 규모, 감독기관 후속
- 질문: OpenAI, SpaceX 토큰의 약관상 권리, 발행 규모, 리투아니아 중앙은행 조회의 결과, 지금도 제공되는가?
- 이미 본 출처: F-0222, F-1327~F-1329(2025-07-07까지)
- 찾을 곳: https://robinhood.com/eu/en/support 와 https://docs.robinhood.com/rhj/ 의 Final Terms 목록, https://www.lb.lt (리투아니아 중앙은행 보도자료), 구글 "Robinhood OpenAI token Bank of Lithuania outcome". LOCAL_GOOGLE_TASK #12와 합침
- 채울 곳: Robinhood, B 상품 구조 비상장 토큰, 제약과 리스크
- 브라우저가 필요한 이유: Final Terms 목록이 동적 로딩이고 investors.robinhood.com은 클라우드 403

## E. 자료

### G11. Binance 연간 이용자와 거래대금, 매출
- 질문: 활성 이용자 수, 연간 거래대금(현물과 선물 구분, 산정 방식), 매출 공개 값은?
- 이미 본 출처: F-1201(등록 3.2억), F-0675, F-0674(about 페이지 표기, 단일 출처)
- 찾을 곳: https://www.binance.com/en/about, 구글 "Binance 2025 annual report users trading volume revenue". LOCAL_GOOGLE_TASK #14와 합침
- 채울 곳: Binance, 회사 개요 본업과 규모
- 브라우저가 필요한 이유: binance.com 클라우드 405(봇 확인), 동적 페이지

### G12. Ondo 고객 수와 매출
- 질문: Ondo 보유자 수, 매출, 전체 TVL의 회사 공개 값이나 신뢰할 수 있는 매체 값은?
- 이미 본 출처: 시장 전체 보유자 86,310(F-1320), DefiLlama fees F-1326(제3자). 블로그 209건에서 공개 수치 없음
- 찾을 곳: https://ondo.finance 홈, https://defillama.com/protocol/ondo-finance, https://app.rwa.xyz/platforms/ondo, 구글 "Ondo Finance holders number TVL 2026". LOCAL_GOOGLE_TASK #17과 합침
- 채울 곳: Ondo, 회사 개요 본업과 규모
- 브라우저가 필요한 이유: rwa.xyz 세부 열은 로그인과 동적 화면

### G13. Dinari 매출, 고객 수, 거래 규모
- 질문: 회사 또는 매체가 낸 매출, 고객 수, 파트너 수, 거래액은?
- 이미 본 출처: F-0128, F-1027, F-1031, F-1333(제3자), F-0350. 매출과 고객 수는 회사 비공개 표시
- 찾을 곳: https://dinari.com/blog, https://www.rwa.xyz/ 토큰화 주식 플랫폼 표, 구글 "Dinari dShares partners number revenue Series A investors". LOCAL_GOOGLE_TASK #20과 합침
- 채울 곳: Dinari, 회사 개요 본업과 규모
- 브라우저가 필요한 이유: 동적 페이지와 검색 화면

### G14. 야간 ATS 3곳의 수수료와 수익 구조
- 질문: Blue Ocean, Bruce, MOON의 구독 브로커 대상 수수료, 구독자 수, 시세 판매 수익은? Form ATS-N Part III 수수료와 공정접근 항목은?
- 이미 본 출처: F-1294(Interactive Brokers 요율표, 단일 출처), F-1302, F-1183, F-1298. Form ATS-N 원문은 못 열음
- 찾을 곳: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=ATS-N (EDGAR 회사 검색), https://www.interactivebrokers.com/en/accounts/fees/blueocean-ats.php, https://www.blueocean-tech.io, https://www.brucemarkets.com, https://www.otcmarkets.com (MOON ATS). LOCAL_GOOGLE_TASK #21~24와 합침
- 채울 곳: Blue Ocean, Bruce, MOON, 거래 시설 운영 "수수료와 수익원"
- 브라우저가 필요한 이유: sec.gov 클라우드 403, otcmarkets.com이 셸에서 열리지 않음, 원문이 PDF

### G15. Dinari 미국판 대상 서술의 불일치
- 질문: 미국판 이용 자격은 "적격 미국 투자자와 사업자"인가 "만 18세 이상 미국 거주 개인"인가, 둘 다인가?
- 이미 본 출처: https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-in [F-1131], https://dinari.com/bd/terms [F-0319]
- 찾을 곳: https://dinari.com/us/disclosures, https://dinari.com/bd/terms, https://dinari.com/get-started
- 채울 곳: Dinari, C 최종 투자자와 한국 시장과의 차이
- 브라우저가 필요한 이유: 약관 페이지가 동적이고 가입 화면 문구는 열람해야 보임(로그인은 하지 않음)
