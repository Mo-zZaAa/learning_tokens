# R-K 리서치: Kraken 본문 메모 79개 답변용 사실 (2026-11-16)

표기: 찾음 = F 번호와 원문 한 문장. 새 사실은 F-1245~F-1259(work/R-K, RK-001~015). 본문은 고치지 않음. 기존 DB 사실은 이번에 다시 열지 않고 db/facts.csv에서 가져옴.

## 1. Payward와 Kraken의 관계, 계열사, 상장, 25% 공시
- 찾음(관계): F-0176 "Payward, the developer of the xStocks tokenized equities framework and parent company of Kraken". F-0359~F-0362 공식 사이트 구조화 데이터에 법인명 Payward, Inc., 모회사 Payward 별도 표기.
- 찾음(계열사 지분): F-0372 Kraken Securities LLC "a wholly owned subsidiary of Payward, Inc."(미국 브로커딜러, F-0242). F-0375 Payward Interactive, Inc.(미국 암호화폐 서비스). F-0938 Backed Finance AG는 Payward Europe Limited(아일랜드)가 100%, 그 위에 Payward, Inc.가 100%. F-0177 NinjaTrader 완료 2025-05-01. F-1116 Small Exchange 2025-10. F-1118 Bitnomial 2026-05-01 완료. F-1195 Reap 2026-07-01 완료(Reap 브랜드 독립 유지, F-1256). F-1194 Saldo Bank 계약, 종결 2027 예상. Breakout은 F-1252.
- 찾음(25%): F-0938 원문 "no individual shareholder holds more than 25% of the shares in Payward, Inc., US." 출처는 Backed Assets (JE) Limited 기본투자설명서 2026-05-08 p.61(inputs/manual/B01...txt). 의미: 단일 개인 지배주주 없음을 투자설명서가 밝힌 것이고 주주 명단은 아님. 법적 해석은 하지 않음.
- 찾음(상장): 모두 비상장. F-1188 Payward가 SEC에 Form S-1 초안 비공개 제출(2025-11-19), 제출 주체는 Payward. F-0183, F-0184(2026-03 중단, 2027 Q2 이후 보도, 언론). F-1187 2025-11 기업가치 200억 달러.
- 못 찾음: Payward가 지주회사가 된 시점(법인 개편일). 찾아본 곳: payward.com/about(연혁에 없음), 구조화 데이터, 투자설명서 구조도(2026년 기준 구조만). 버뮤다, 아일랜드, 키프로스 법인 각각의 지분율 표(투자설명서에 법인명만). NinjaTrader, Small Exchange, Bitnomial 인수 후 지분 구조 공시는 못 찾음.

## 2. Backed
- 찾음(원래 회사): F-1250 Adam Levi(공동창업자) "Founded in 2021, the team built a compliant and scalable solution that seamlessly bridges crypto and traditional finance." 법무법인 Walkers 공지(sources/EXT-Kraken/walkers.txt, F-0145)에서 공동창업자 Roberto Klein, Backed Assets (JE) Limited는 "Jersey's first tokenised assets issuer". F-0937 스위스 Backed Assets GmbH(2021-04-20 설립)가 2024-02-23 저지 발행사에 합병. F-0935 저지 법인 2024-01-19 설립.
- 찾음(인수 이유와 이후): F-0139, F-0140, F-1251. F-1251 "Kraken plans to integrate xStocks more deeply into its broader product suite — including Krak". F-0923 2026-01-06 "the Parent sold, assigned and transferred to Payward all of its right, title and interest in certain technology and intellectual property assets related to the tokenized equities business."(최초 대가 USDC 16.823백만, 2차 보충서 p.6). F-0970 "The Issuer does not independently maintain the employees or technical capabilities necessary to perform the tokenization services." F-0924 "Neither Payward nor PEL has guaranteed the Issuer's obligations under the Products". F-0922 모회사가 대여채권 약 6,075,435달러를 출자로 소멸.
- 찾음(저지인 이유, 부분): 회사가 저지를 고른 이유 문장은 없음. 사실로 F-0940(저지 JFSC는 차입통제령 동의만, 감독 인가 없음, "will operate without supervision by any authority in any jurisdiction"), F-0990(JFSC가 승인 참가자와 브로커를 규제 받는 금융회사로 한정하라 요구), F-0974(저지 전문투자자 면제령). 즉 발행사는 SPV(F-0935 계열, 투자설명서 2.3.2.1)이고 규제 인가는 판매 법인과 보관 기관이 맡음. 이유 해석은 하지 않음.
- 찾음(보관): F-0964 InCore Bank AG는 FINMA 인가 스위스 은행으로 스위스 담보 보관, 대금 계좌 제공(F-0967)과 브로커(F-0966), Alpaca Crypto LLC는 미국 보관기관 기재, Alpaca Securities LLC는 SEC 등록 브로커딜러로 계좌와 Prime Borrower 역할(F-0959). F-0960 InCore는 증권 대여를 금지당함. 두 곳인 이유는 스위스 담보와 미국 담보로 나뉜 법구조(F-0962).
- 못 찾음: Backed 투자자 명단, 창업 시 초기 자본, 주식 토큰 발행 순위(2025-06 이전). 인수 금액 공개 없음. 찾아본 곳: Kraken 블로그, Walkers, payward.com 보도자료, 투자설명서. Alpaca 소재지 불일치(뉴욕 vs 노스캐롤라이나)는 work/BACKED/notes.md.

## 3. xStocks
- 찾음: F-1249 출시일 2025-06-30, 60종, Solana, 미국 밖 적격 고객, 140개국 이상 계획. "We're not launching a novelty. We're unlocking something foundational"(F-1040).
- 찾음(거래량과 보유자 시계열): F-0141 6개월 100억 달러 초과(2025-12-02), F-0158 250억 달러와 8.5만 명(2026-03-09), F-0162 350억 달러, 약 20만(2026-07-02), F-0164 400억(2026-09-01), F-0166 450억 달러, 55만 명 초과(2026-10-28). AUM F-0165 10억 달러(2026-10-27). 체인 F-0142, F-0397(10개 이상). 순위 F-1023 rwa.xyz 3위 6.77억 달러, F-1030 2026-01-16 1.937억(22.6%)에서 이어짐. F-0161 CoinGecko 시총 상위 15개 중 8개.
- 찾음(경쟁 날짜): Robinhood EU 주식 토큰 2025-06(F-0221, F-0640, 일자는 확인 못함), Ondo Global Markets는 "under eight months" 전 총예치 10억 돌파(2026-05, F-0199)로 2025-09 전후 추정이고 출시일 직접 문장은 못 찾음, Binance bStocks 2026-06-12(F-0053), Dinari 미국 2026-08-04(F-1206), Binance 2021-04 구 주식 토큰은 2021-07 중단(F-1124).
- 못 찾음: 처음 공급 거래소 목록(Bybit 등) 1차 공지(F-1083은 Bybit 추천사만, 사용자 메모의 Bybit 누적 5.5억 달러는 포필러스 보고서 인용으로 재확인 안 함). 유명해진 이유는 숫자(F-0141, F-0162, F-0166)로만 보이고 회사의 인과 설명은 F-1045.
- 주의: 메모 57번처럼 제3자 보고서 수치는 본문에서 빼자는 사용자 지시가 있어 회사 발표 수치를 우선함.

## 4. 인수별 왜, 어떻게, 그 뒤, 계획
- NinjaTrader: F-1117(2025-03-20 발표, 약 15억 달러는 언론, F-1042 Sethi 발언), F-0177(완료). 뒤: F-1190, F-1189에서 NinjaTrader Clearing이 계좌 보유. 쓴 곳 정리는 kb/scope_rationale/Kraken.md.
- Small Exchange: F-1116(1억 달러, IG Group, "paves the way for a fully U.S.-native derivatives venue" 블로그 부제). 뒤 사용처 못 찾음.
- Bitnomial: F-1118 "Payward now owns the complete US derivatives stack – a Futures Commission Merchant (FCM), a Designated Contract Market (DCM), and a Derivatives Clearing Organization (DCO)". F-1189 주식 무기한선물 10종 서류, F-1190 Hyperliquid 온체인 무기한선물. 금액은 회사 발표에 없음(관계표에 The Block 최대 5.5억).
- 순서 이유(선물, 파생 거래소, 청산소): 회사 문장 있음. F-0178 "Our CFTC-regulated exchange, clearinghouse, and futures broker are how we bring activity onshore" 와 Q3 보고 "one set of licenses serves many products and partners"(F-0180 출처 문서). 순서 자체의 이유 문장(왜 FCM 먼저)은 못 찾음.
- Backed: 위 2번과 F-1043. Nasdaq Ventures: F-1119, F-1255 "The investment in Payward reflects the strategic nature of the work the two organizations are advancing together." Nasdaq 쪽 이유는 Nasdaq Equity Tokens와 발행사 중심 접근 유지, 시장감시 계약. NET 2027 Q2 출시 예상(2026-03에는 2027 Q1이었음, F-0159). 
- Reap: F-1256, F-1195 "With Reap, partners can issue cards, originate cross-border payments, and manage treasury against on-chain liquidity". Saldo Bank: F-1254 "We're not acquiring a bank to be a bank."(F-1194). Breakout: F-1252(2025-09-04 안내, 금액 못 찾음).
- 못 찾음: Small Exchange 이후 상품, Breakout 인수 금액과 이유 문장(블로그는 상품 안내문).

## 5. 지역 인가
- 찾음: 버뮤다 Payward Digital Solutions Ltd. BMA 디지털자산 사업 라이선스(F-0154, F-0387, F-0919 AP 계약 2025-04-28). 아일랜드 MiCA CASP 2025-06(F-0250, F-0251, 중앙은행 F-0382). 키프로스 Payward Europe Digital Solutions (CY) Ltd. MiFID II 투자회사(F-0156, F-0920 AP 계약 2026-05-04).
- 부분: 주식 토큰은 가상자산 서비스가 아니라 EU 투자설명서 규정의 증권(F-0148, F-0942 FMA 승인)이라 판매 법인에 MiFID II(키프로스)가 붙는 것으로 보임. 이는 해석이며 회사나 감독기관의 "왜 그곳" 문장은 못 찾음. 가상자산은 MiCA(F-0250). 미국 밖 대부분 지역 판매는 EEA 밖이라 버뮤다 법인(F-0401).
- 못 찾음: 버뮤다, 아일랜드, 키프로스를 고른 이유 문장. 찾아본 곳: Kraken 블로그, payward.com/about, 투자설명서, 법적 고지 페이지.

## 6. 판매 제외 범위
- 찾음: F-0393 "Tokenized stocks are not accessible in the US, Canada, UK, or Australia at this time" 는 토큰화 주식에 대한 문장(F-0157 영국 인가 없는 관할 불가). 암호화폐는 별도: 영국에서 FCA 등록 암호자산 기업이나 규제 대상 서비스 아님(F-0384, F-0385), 미국은 Payward Interactive 등으로 제공(F-0375). 즉 이 제외는 주식 토큰 한정이고 가상자산은 지역별 별도 제공. 한국은 투자설명서에 언급 없음(work/BACKED/absent.csv).

## 7. SEC 사건
- 찾음: CASE-003 2023-02-09 스테이킹 합의, 광고 수익률 최대 연 21%, 총 3천만 달러, 인정도 부인도 안 함, 스테이킹 서비스 중단과 미등록 스테이킹 영구 금지. CASE-004 2023-11-20 제기 후 2025-03-27 with prejudice 취하. sec.gov는 셸 403이라 이번에 다시 열지 않고 기존 행 사용.

## 8. 자금 계정과 Q3 실적
- 찾음(정의, F-1248): 원문 "Funded Accounts refers to the number of client accounts that maintained a balance greater than zero ... not a count of unique clients."
- 찾음(구성): F-1245 TPM 4.87억 달러 = 거래 기반 2.34억 + 자산 기반 1.28억 + 접근 기반 1.25억. 접근 기반은 전체의 약 4분의 1. F-0180 조정 EBITDA 6천만, 거래량 3,530억, 자금 계정 710만. F-1191 청구 가능 계정 150만. 
- 못 찾음: xStocks가 TPM에서 차지하는 몫(F-1246). 회사가 별도 공개하지 않음. 이 숫자는 추정 금지.

## 9. CEO 발언 시점 순
- 찾음(Sethi, 말하고 이룬 것): 2025-03-20 NinjaTrader 인수 발표(F-1042) -> 2025-05-01 완료(F-0177). 2025-06-30 "xStocks ... unlocking something foundational"(F-1040) -> 출시 60종(F-1249), 1년 뒤 8/15(F-0161). 2025-12-02 "Unifying issuance, trading and settlement under one framework"(F-1043) -> 2026-01 Backed 100%(F-0939). 2026-03-09 Nasdaq 상호운용(F-1044) -> 2026-09 Nasdaq Ventures 투자(F-1119). 2026-05-07 Reap 발표 -> 2026-07-01 완료(F-1256). 2026-10-14 Saldo Bank "the ambition is global"(F-1254) -> 진행 중(종결 2027 예상).
- 진행 중: xPO, 개별주식 무기한선물 10종, Hyperliquid 온체인 무기한선물, 에이전트(F-1258, F-1259, F-1189, F-1190).
- 못 찾음: Jesse Powell과 Dave Ripley 발언. payward.com/about은 Powell을 창업 서술에서만 언급(F-1109), governance 페이지에는 발언 없음. 외부 언론과 2025 이전 블로그는 이번 시간 안에 열지 못함.

## 10. 기업용 서비스
- 찾음: F-1257 Payward Services 이용 사례(OKX, WOO X EU, GTN), F-0452 bunq가 Embed로 "in weeks" 앱 내 거래 출시, F-0453 프랑스 대형 은행 제휴(이름 없음), F-1193 xStocks 100개 이상 파트너, F-1159 Prime 2025-06-03, F-0443 Prime 기관 고객 1,000곳 이상(기준일 없음). F-1256 Reap으로 카드 추가. 로드맵 F-1258.
- 못 찾음: 이용 기업 총수(F-1193이 "공개 없음"), Payward Services 시작 시점.

## 11. xPO와 GTN 홍콩
- 찾음: xPO F-0182, F-1258. GTN F-0170, F-1084: "beginning by tokenizing equities listed in Hong Kong, before expanding to tokenize UK-listed assets, European assets, South Korean assets, and more"(2026-07-22 발표). 홍콩 시작 시점 날짜는 못 찾음(발표문에 없음, 각 시장 인가 조건). 한국은 계획 단계(F-0171).

## 12. KSF 근거
- 찾음(선행 주장, 회사 서술): 연혁 최초 주장 F-1253(2014 준비금 증명, 2015 현물과 선물 한 플랫폼, 2019 SPDI, 2020 영국 MTF). 성과 숫자: 점유율 3.3%에서 6.5%(F-1247), xStocks 출시 6개월 100억 달러(F-0141), 1년 뒤 8/15(F-0161), 2026-01 1.94억에서 2026-11 6.77억 달러(F-1030, 18.3% 점유로 3위, 비율은 하락), Ondo는 2026-03 약 58%(F-1032). 
- 주의: xStocks 점유율은 2026-01 22.6%에서 18.3%로 줄어 선점이 점유 유지로 이어졌다고 말할 수 없음. 거래량 전후(인수 전후 비교)는 Backed 인수 전후 거래량 시계열만 있음(F-0141, F-0158, F-0164).
- 못 찾음: NinjaTrader, Bitnomial 인수 전후 파생 거래량 비교.

## F 번호표(이번 신규)
RK-001=F-1245 TPM 구성 / RK-002=F-1246 xStocks 몫 공개 없음 / RK-003=F-1247 점유율 3.3->6.5% / RK-004=F-1248 자금 계정 정의 / RK-005=F-1249 xStocks 출시 2025-06-30 / RK-006=F-1250 Backed 2021 설립 / RK-007=F-1251 Backed 인수와 Krak / RK-008=F-1252 Breakout 2025-09-04 / RK-009=F-1253 회사 연혁 최초 주장 / RK-010=F-1254 Saldo 뱅킹 축 / RK-011=F-1255 Nasdaq 투자 이유 / RK-012=F-1256 Reap 인수 후 / RK-013=F-1257 Payward Services 사례 / RK-014=F-1258 xPO와 서비스 로드맵 / RK-015=F-1259 뱅킹 레일 계획.
