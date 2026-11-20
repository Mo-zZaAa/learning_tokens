# Binance 인가 획득 딥다이브: 인수, 직접 인가, 실패와 철수 (사실 모음)

- 작성: 2026-11-20. 범위: Binance 그룹(글로벌 플랫폼 Binance.com과 나라별 법인). Binance.US는 인가와 관련된 건만.
- 번호 표기
  - F-xxxx: db/facts.csv에 이미 있는 사실(다시 찾지 않음)
  - LDBN-xxx: 이번에 새로 확인한 사실(work/LICDEEP-BN/facts.csv, 출처는 work/LICDEEP-BN/sources.csv)
  - BN-Exx: kb/events/binance_events_src.py 사건 카드. CB-Exx, KR-Exx, RH-Exx: Coinbase, Kraken, Robinhood 사건 카드
- 표시: (보도, 매체명) 매체 기사, (회사 주장) 회사 숫자, (계산) 우리가 셈, (판단) 해석과 그 근거 사실. 결론 문장은 쓰지 않음.
- 용어
  - 인가(license): 감독기관이 영업을 허가한 것. 등록(registration): 자금세탁방지 목적의 신고와 등록. Binance가 발표에서 센 "인가와 등록" 수에는 둘이 섞여 있음
  - VASP: 가상자산사업자. CASP: EU와 키프로스의 가상자산서비스사업자. MiCA: EU 가상자산시장법(한 나라 인가로 EU 전체 영업)
  - 원칙 승인(in-principle approval): 정식 인가 전 단계. 조건을 채우면 정식 인가를 받음

## 0. 회사가 센 인가와 등록 수 (회사 주장, 시점순)

| 시점 | 회사가 밝힌 수와 목록 | 근거 |
|---|---|---|
| 2022-11-30 | 승인이나 인가를 받은 곳: 프랑스, 이탈리아, 스페인, 바레인, 아부다비, 두바이, 뉴질랜드, 카자흐스탄, 폴란드, 리투아니아, 키프로스. 일본(SEBC 인수)이 동아시아 첫 인가 | LDBN-015 ([Mondo Visione 전재](https://mondovisione.com/media-and-resources/news/binance-acquires-jfsa-registered-sakura-exchange-bitcoin-committed-to-enter-jap-20221130/)) |
| 2023-01-11 | EU 7개국(프랑스, 이탈리아, 리투아니아, 스페인, 키프로스, 폴란드, 스웨덴), 세계 15개 관할 | LDBN-044 ([PR Newswire 전재](https://www.aap.com.au/aapreleases/cision20230111ae83777/)) |
| 2023-09-27 | 18개국 인가와 등록, 2023-01 뒤 5곳 더 발표 | LDBN-032 ([PR Newswire 전재](https://aap.com.au/aapreleases/cision20230927ae21598/)) |
| 2024-08-15 | 인도 등록이 19번째 세계 규제 이정표 | LDBN-054 ([Finance Magnates](https://www.financemagnates.com/cryptocurrency/binance-secures-19th-global-approval-with-indian-aml-registration/)) |
| 2024-11-21 | 나라별 인가와 등록 20개 넘음(CEO 1년 서한) | BN-E29 |
| 2025-01-02 | 브라질 증권사 인수 승인이 21번째 | LDBN-027 ([iProfesional](https://www.iprofesional.com/tecnologia/420043-brasil-otorga-a-binance-su-21-autorizacion-regulatoria-global)) |
| 2025-12-08 | 글로벌 플랫폼 Binance.com 전체를 ADGM이 승인(글로벌 플랫폼의 첫 감독 당국) | F-0064, F-1554, LDBN-062 |

- 주의: 2022-11-30 목록에 폴란드가 있으나 폴란드 발표는 2023-01-18(LDBN-045). 폴란드 등록일 자체는 빈칸 5.
- 주의: 세는 단위가 "나라", "관할", "이정표"로 발표마다 다름. 이어 붙여 증가 폭을 계산하지 않음.

## 1. 모든 인수 목록

| 발표일 | 완료일 | 대상 | 대상이 하는 일 | 얻은 인가나 손님 | 대금 | 깊게 봄 | 출처 |
|---|---|---|---|---|---|---|---|
| 2018-07-31 | 2018-07-31 | Trust Wallet(미국) | 이용자가 자기 열쇠로 보관하는 지갑 앱 | 기술 팀(인가 없음) | 비공개, 현금과 Binance 주식과 BNB | 목록만(BN-E07) | F-1872 ([TechCrunch](https://techcrunch.com/2018/07/31/crypto-exchange-binance-buys-trust-wallet-in-first-acquisition-deal/)) |
| 2019-09-02 | 2019-09-02(발표) | JEX | 가상자산 현물과 파생(무기한선물, 옵션) 거래 플랫폼 | 파생 상품과 개발 팀(인가 없음) | 비공개 | 카드 1-1 | LDBN-001, F-1713 |
| 2019-11-21 | 미완료라고 CZ가 2022-08 주장 | WazirX(운영사 Zanmai Labs, 인도) | 인도 가상자산 거래소 | 인도 손님(분쟁) | 최대 1,000만 달러(보도) | 카드 3-2 | LDBN-008 |
| 2020-04-02 | 비공개 | CoinMarketCap | 가상자산 시세와 거래소 순위 사이트 | 유입 경로(인가 없음) | 약 4억 달러(보도) | 목록만(BN-E13) | F-1878, LDBN-025 |
| 2020-05-12 | 2020-05-12 투자, 2022-12-19 지분 늘림 | Tokocrypto(인도네시아) | 인도네시아 가상자산 거래소 | Bappebti 승인(2019-11) | 비공개 | 카드 1-2 | LDBN-009, LDBN-011 |
| 2020-06 | 2020-06 | EddieUK(영국, 이름을 Binance Markets Limited로 바꿈) | 영국 법인 | binance.uk 출범용 법인(출범 못 함) | 비공개 | 카드 3-3 | LDBN-063 |
| 2020-07-06 | 2020-07(과반 지분) | Swipe(필리핀 본사) | 가상자산 직불카드(발행은 영국 FCA 인가 Contis) | 카드 사업(인가는 발행사 쪽) | 비공개 | 목록만 | LDBN-006, LDBN-007 |
| 2021-12 | 비공개 | Hg Exchange 지분 18%(싱가포르) | 싱가포르 사설 증권거래소 | 지분(인가 회사) | 비공개 | 카드 3-4 | LDBN-014 |
| 2022-03-01 | 비공개 | MX Global 지분(말레이시아, Cuscapi와 함께) | 말레이시아 SC 인가 디지털자산거래소 4곳 중 하나 | 지분(인가 회사) | 비공개 | 카드 1-7 | LDBN-013 |
| 2022-03 | 2025-01-02(BC 승인 발표) | Sim;paul(브라질, 지금 Binance Brasil Corretora) | 증권사 | 전자화폐 발행(EMI), 증권 유통 인가 | 비공개 | 카드 1-5 | LDBN-026 |
| 2022-04-18(Gulf Energy 공시) | 2023-05-26(합작사 인가) | Gulf Binance(태국 합작) | 새 합작 거래소(상대 Gulf Innova) | 합작사가 새로 받은 인가 | 비공개 | 카드 1-6 | LDBN-029, LDBN-031 |
| 2022-11-08(구속력 없는 의향서) | 2022-11-09 철회 | FTX.com(미국 FTX.US 제외) | 가상자산 거래소 | 없음 | 없음 | 카드 3-1 | LDBN-023 |
| 2022-11-30 | 2022-11-30 | Sakura Exchange BitCoin(일본, 지금 Binance Japan) | 일본 금융청 등록 가상자산교환업자 | 일본 등록 | 비공개(100%) | 카드 1-3 | LDBN-015, LDBN-016 |
| 2022-12-19(Binance.US 최고 입찰 보도) | 2023-04-25 해지 | Voyager Digital 자산(미국 파산 중개사) | 가상자산 중개 | 손님 | 약 10억 달러 | 카드 3-7 | LDBN-064, LDBN-028 |
| 2023-02-03 | 2025-10-15(최대주주 변경 수리) | 스트리미(한국 고팍스 운영사) | 원화 가상자산 거래소 | 금융정보분석원(FIU) 신고 | 약 1,200억 원, 고파이 부채 560억 원 상환 약속(보도) | 카드 1-4 | LDBN-021, F-1389, F-0073 |

- 반대 방향(Binance가 판 것): 2023-09-27 러시아 사업 전부를 CommEX에 매각(LDBN-032, 카드 3-12). 2025-10-09 Binance Japan 지분 40%를 PayPay에 넘김(LDBN-020, 카드 1-3의 9칸)
- 카자흐스탄은 인수가 아니라 직접 인가(카드 2-11). 태국은 인수가 아니라 합작(카드 1-6)
- 외부 투자 유치: 2025-03-12 MGX 20억 달러, 소수 지분, 스테이블코인 납입(F-0069). 인수가 아니므로 카드 2-3(ADGM)에서 다룸

## 2. 직접 인가 목록

| 인가 | 나라 | 법인 | 신청일 | 승인일 | 걸린 기간 | 출처 |
|---|---|---|---|---|---|---|
| 가상자산서비스사업자 인가 | 바레인(중앙은행 CBB) | 바레인 법인(이름 빈칸 4) | 원칙 승인 약 2021-12(보도: 3개월 전) | 2022-03-14 | 원칙 승인부터 약 3개월(보도) | LDBN-046 |
| 잠정 인가 → MVP → 운영 MVP → VASP | 두바이(VARA) | Binance FZE | 빈칸 | 잠정 2022-03, MVP 2022-09-19, 운영 MVP 2023-07-31, VASP 2024-04-18 | 잠정부터 VASP까지 약 25개월(계산) | F-0068, LDBN-048, LDBN-049, LDBN-050 |
| 중개 딜러 원칙 승인 → 거래소, 청산소, 브로커 인가 3종 | 아부다비(ADGM FSRA) | Binance (AD) Ltd(지금 Nest Clearing and Custody), Nest Services(지금 Nest Exchange), BCI(지금 Nest Trading) | 빈칸 | 원칙 승인 2022-04(보도 2022-04-10), 인가 발표 2025-12-08, 등록부 효력 2025-12-08과 2026-01-05 | 원칙 승인 보도부터 인가 발표까지 1,338일(계산) | LDBN-047, LDBN-062, F-1418 |
| 디지털자산서비스사업자 등록(PSAN) | 프랑스(AMF) | Binance France SAS | 빈칸 | 2022-05-04 | 빈칸 | LDBN-041 |
| 가상자산 서비스사업자 등록 | 이탈리아(OAM) | Binance Italy | 빈칸 | 2022-05-27 | 빈칸 | LDBN-042 |
| 가상자산사업자 등록 | 스페인(중앙은행) | Moon Tech Spain | 2022-01-28 | 2022-07-07 | 160일(계산) | LDBN-043 |
| VASP 등록 | 리투아니아(법인등록센터, FIU) | Bifinity UAB | 빈칸 | 빈칸(2020부터 영업) | 빈칸 | LDBN-055 |
| 원칙 인가 → 정식 인가 → 정식 DATF 인가 | 카자흐스탄(AIFC AFSA) | Binance Kazakhstan | 빈칸 | 원칙 2022-08, 정식 2022-10, 틀 재편 2023-01, 정식 DATF 2024-09 | 원칙부터 정식 DATF까지 약 25개월(계산) | LDBN-051, LDBN-052 |
| 등록(종류 빈칸) | 뉴질랜드 | 빈칸 | 빈칸 | 2022-11-30 이전(회사 목록) | 빈칸 | LDBN-015 |
| 3등급 CASP 등록 | 키프로스(CySEC) | Binance Cyprus Limited | 빈칸 | 2022-10-20(2023-09-11 말소) | 빈칸 | LDBN-037, LDBN-038 |
| VASP 등록 | 폴란드 | Binance Poland sp. z o.o. | 빈칸 | 2022-11-30 이전(회사 목록), 2023-01-18 발표 | 빈칸 | LDBN-015, LDBN-045 |
| 가상화폐 관리와 거래 금융기관 등록 | 스웨덴(FI) | Binance Nordics AB(등록번호 66822) | 빈칸 | 2023-01-10 | 빈칸("수개월 협의", 회사) | LDBN-044 |
| 비트코인 서비스사업자(BSP), 디지털자산서비스사업자(DASP) | 엘살바도르(중앙은행, 국가디지털자산위원회) | 빈칸 | 빈칸 | 2023-08-08 | 빈칸 | LDBN-053 |
| 보고 의무 기관 등록 | 인도(FIU-IND) | 빈칸 | 빈칸 | 2024-08-15 발표 | 빈칸 | LDBN-054 |
| 가상자산서비스사업자(PSAV) 등록 No. 76 | 아르헨티나(CNV) | Binance Services Latinoamérica S.A. de C.V. | 빈칸 | 2024-09-11 | 빈칸 | F-0712, F-0713 |
| MiCA 인가 신청 | 그리스(HCMC) | 빈칸 | 2026-01 | 2026-06-24 철회 | 약 5개월 뒤 철회 | LDBN-056, F-1548 |

- 일본, 한국, 인도네시아, 브라질은 인수로, 태국은 합작으로 들어감(카드 1). 독일, 네덜란드, 싱가포르, 그리스는 신청 뒤 철회나 실패(카드 3)

## 3. 카드 1. 인수 건

### 1-1 JEX (2019-09, 파생 기능)
1. 한 줄 사건: 2019-09-02 Binance가 가상자산 현물과 파생 거래 플랫폼 JEX를 샀다고 Finance Magnates에 밝힘. 무기한선물과 옵션 상품이 있던 회사이고 이름을 Binance JEX로 바꿈. 금액 비공개(LDBN-001, [Finance Magnates 2019-09-02](https://www.financemagnates.com/cryptocurrency/news/binance-acquires-derivatives-specialist-jex/); F-1713 The Block)
2. 그 전 상태: Binance에 파생 상품이 없었음. 직전 주 9월 파생 상품 출시를 예고했고, 인수 발표일에 시험용 플랫폼 둘을 공개(LDBN-001). 이미 하던 제휴는 빈칸 1
3. 직접 받는 길: 자체 개발판 선물 플랫폼을 함께 만들어 JEX판과 나란히 5일 시험한 뒤 2019-09-13 Binance Futures 출시(F-1714, Bitcoinist 보도). (계산) 인수 발표부터 출시까지 11일. 이 상품에 받은 인가는 빈칸 2
4. 대상 회사: Finance Magnates는 JEX가 중국계로 보인다고 적음(LDBN-001). 설립 연도, 인가, 손님, 거래량은 빈칸 1
5. 판 쪽: 빈칸 1
6. 승인: 빈칸 2
7. 대금: 비공개(LDBN-001)
8. 같은 시기 바깥
   - 시장(한 집계기관 CryptoCompare로 통일): 2019-09 파생 월 거래대금 1위 OKEx 903.4억 달러, 2위 Huobi 845.2억 달러. Binance 값은 발표문에 없음(LDBN-002, [CryptoCompare 2019-10-21](https://data.coindesk.com/press-releases/cryptocompare-releases-exchange-review-for-september-2019))
   - 미국: Binance Futures 출시가 미국 Bakkt 비트코인 선물 출시 직전(F-1714 매체 제목). 같은 시기 글로벌 플랫폼에서 미국 이용자를 막고 Binance.US를 엶(BN-E11)
   - 경쟁: Kraken 2019-02-04 영국 가상자산 파생 회사 Crypto Facilities 인수 발표(KR-E09). Coinbase 2019-08-15 Xapo 기관 보관 사업 인수(CB-E14). Robinhood 2019-11-19 영국 진출 발표(RH-E11)
9. 산 뒤(BitMEX와 비교, 모두 CryptoCompare)
   - 2019-11 상품별 월 거래대금: BitMEX BTC 무기한선물 379억 달러, Binance BTC 무기한선물 323억 달러(LDBN-003)
   - 2019-12: BitMEX BTC 무기한선물 531억 달러, Binance BTC 무기한선물 294억 달러(상품 3위). ETH 무기한선물 하루 평균 거래대금 점유율 BitMEX 44%, Binance 23%(LDBN-004)
   - 2020-09 거래소 합계: Binance 1,648억 달러로 파생 1위, BitMEX 564억 달러. 전체 6,349억 달러 대비 Binance 약 26.0%, BitMEX 약 8.9%(계산, LDBN-005)
   - 주의: 2019-09, 11, 12 발표문에는 BitMEX 거래소 합계가 없어 그 시기는 상품(BTC 무기한선물)끼리만 비교함. 거래소 합계 비교는 2020-09부터
   - JEX 브랜드와 팀을 그 뒤 어떻게 썼는지는 빈칸 1
10. 발언: Yi He(공동 창업자) 2019-09-02, quotes 파일 "JEX"

### 1-2 Tokocrypto (인도네시아, 2020-05 투자, 2022-12 지분 늘림)
1. 한 줄 사건: 2020-05-12 Binance가 인도네시아 규제 거래소 Tokocrypto에 금액 비공개로 투자(LDBN-009, [Finance Magnates](https://www.financemagnates.com/cryptocurrency/news/binance-invests-undisclosed-sum-in-indonesian-crypto-exchange/)). 2022-12-19 현금을 더 넣어 지분을 늘림(LDBN-011, [Cointelegraph](https://cointelegraph.com/news/binance-acquires-100-of-indonesian-tokocrypto-after-initial-investment-in-2020)). 지분율은 비공개
2. 그 전 상태: Binance는 2020-04 루피아 P2P 거래를 열었을 뿐 인도네시아 인가가 없었음(LDBN-010). CZ는 은행 관계가 있어 현지 법정화폐 거래를 받을 수 있는 국내 거래소와 일하기를 우선한다고 말했었음(LDBN-010, Cointelegraph 보도)
3. 직접 받는 길: Binance 자체의 인도네시아 신청 기록은 빈칸 6
4. 대상 회사: 2018 설립, 2019-11 상품선물거래감독청(Bappebti) 승인을 받은 인도네시아 첫 규제 거래소(LDBN-009). 그 뒤 Bappebti 승인은 의무가 됐고 2022-03까지 17곳이 승인받음(LDBN-011). 손님 450만 명 넘음(2024, 회사 발표, LDBN-012)
5. 판 쪽: 2020 이전 투자자는 싱가포르 QCP Capital(LDBN-009). 2021 상장을 검토했으나 하지 않음. 2022-09 직원 45명(20%) 감원, 커뮤니티 공간과 NFT 장터 분사. 2022-12 창업자 Pang Xue Kai가 CEO에서 물러남(LDBN-011)
6. 승인: 지분 취득에 필요한 승인과 기간은 빈칸 6. 인수 뒤 Tokocrypto가 2024-09-09 실물 가상자산 거래업자(PFAK) 정식 인가를 받음(인도네시아 셋째, 예비 등록 35곳, LDBN-012). (계산) 첫 투자부터 정식 인가까지 약 4년 4개월
7. 대금: 비공개(LDBN-009, LDBN-011)
8. 같은 시기 바깥
   - 2020-05: 같은 해 4월 CoinMarketCap 인수(F-1878), CZ가 이익의 약 4분의 1을 투자와 인수에 쓴다고 말함(F-1871, 2020-04)
   - 2022-12: 직전 달 FTX 사태(LDBN-023), 일본 SEBC 인수(2022-11-30, LDBN-015), 2022-12-19 Binance.US의 Voyager 자산 최고 입찰 보도(LDBN-064)
   - 경쟁: Kraken 2022-11-28 미국 재무부 제재 위반 합의와 30% 감원(KR-E12). 인도네시아에서 경쟁 세 회사의 움직임은 빈칸 6
9. 산 뒤: 2024 손님 450만 명, 월평균 거래대금 138% 증가(회사 발표, LDBN-012). 2025-01 Binance는 인도네시아를 최근 규제 진전의 하나로 듦(LDBN-027). 2026-07 Teng은 아시아 진출국에 인도네시아를 넣음(F-1548)
10. 발언: CZ 2020-05-12, CZ 2022-12-19, Teng 2024-09(quotes 파일 "Tokocrypto")

### 1-3 Sakura Exchange BitCoin (일본, 2022-11)
1. 한 줄 사건: 2022-11-30 Binance가 일본 금융청 등록 가상자산교환업자 Sakura Exchange BitCoin(SEBC) 지분 100% 인수를 발표. 조건 비공개(LDBN-015, [보도자료 전재](https://mondovisione.com/media-and-resources/news/binance-acquires-jfsa-registered-sakura-exchange-bitcoin-committed-to-enter-jap-20221130/); F-1551)
2. 그 전 상태: 일본 금융청이 2018과 2021-06 무등록 영업을 경고(F-1551). Binance는 2018 일본에서 몰타로 옮김(LDBN-019, BN-E05). 이미 하던 일본 제휴는 빈칸 7
3. 직접 받는 길: Binance는 2022-09 금융청에 운영 인가를 정식 신청해 재진입하겠다고 발표(LDBN-018, [Decrypt 2022-11-30](https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura)). 약 2개월 뒤 인수 발표. 실제 신청서 제출 여부와 결과는 빈칸 7
4. 대상 회사
   - 금융청 등록부(2026-09-30 기준 28곳): Binance Japan 주식회사, 관동재무국장 제00031호, 등록일 2022-10-14. 옛 등록번호 긴키재무국장 제00003호, 옛 등록일 2017-12-01(LDBN-016, [금융청 등록 일람 PDF](https://www.fsa.go.jp/menkyo/menkyoj/kasoutuka.pdf))
     - 뜻: 2017-12 긴키(오사카 쪽) 재무국에 처음 등록, 2022-10 관동(도쿄 쪽) 재무국으로 등록을 다시 받음
   - Kitco는 SEBC가 2017 설립이고 인수 발표 한 달 전에 금융청 등록을 받았다고 적음(LDBN-017). (계산) 관동 등록 47일 뒤 인수 발표
   - 엔화 거래쌍 11개(BTC/JPY 등)와 상담 서비스(LDBN-015). 손님 수와 거래량은 빈칸 7
5. 판 쪽: SEBC CEO Hitomi Yamamoto가 발표에 함께함(LDBN-015). 전 주인이 누구고 왜 팔았는지는 빈칸 7
6. 승인: 인수에 대한 금융청 승인 여부와 기간은 빈칸 7. (계산) 인수 발표부터 Binance Japan 출범(2023-08-01)까지 244일(LDBN-019)
7. 대금: 비공개(LDBN-015)
8. 같은 시기 바깥
   - 2022-11-02 CZ: 현지 인가를 가진 회사, 결제 사업자, 은행까지 살 대상으로 봄(LDBN-024)
   - 2022-11-08~09 FTX 인수 의향서와 철회(LDBN-023). 2022-11 Binance가 거래소 거래의 75%를 차지(CryptoCompare, Kitco 인용, LDBN-017)
   - 경쟁: Kraken은 2018-04 일본 거주자 서비스 중단을 발표했었음(F-1771). Kraken 2022-11-28 제재 위반 합의와 감원(KR-E12). Coinbase, Robinhood의 같은 시기 일본 움직임은 이 저장소 자료에 없음(빈칸 7)
9. 산 뒤
   - 2022-11-30 같은 날 Binance.com이 일본 거주자 신규 가입을 막음(LDBN-017)
   - 2023-08-01 SEBC가 Binance Japan K.K.로 출범, 34종 현물. 글로벌 Binance 일본 이용자 이전은 2023-08-14부터(LDBN-019). 일본 허용 밖 토큰은 BTC로 바꿔 옮기는 약관(F-0716)
   - 2025-10-09 SoftBank 계열 PayPay가 Binance Japan 지분 40%를 삼(2025-09부터 PayPay 지분법 회사, LDBN-020)
   - 2026-09-30 Binance Pay 이용자가 일본 PayPay 가맹점에서 결제(F-1539). 일본은 bStocks 판매 제한 지역(F-1864)
10. 발언: Chino(Binance Japan 총괄), Yamamoto(SEBC CEO), 대변인(quotes 파일 "Sakura")

### 1-4 고팍스 (한국, 2023-02)
1. 한 줄 사건: 2023-02-03 Binance가 원화 거래소 고팍스 운영사 스트리미의 지분 과반을 샀다고 발표(지분율, 금액은 발표에 없음, LDBN-021, [TechCrunch 2023-02-06](https://techcrunch.com/2023/02/06/binance-acquires-majority-stake-in-korean-crypto-exchange-gopax/)). 블록미디어는 72.26% 인수, 뒤에 67.45% 보유, 투자액 약 1,200억 원과 고파이 부채 560억 원 상환 약속이라고 보도(F-1389)
2. 그 전 상태: 2021 한국 철수(F-0074, BN-E16). 2021 특정금융정보법 시행으로 한국 손님을 받으려면 FIU 신고가 필요했음(BN-E16)
3. 직접 받는 길: Binance 법인의 한국 직접 신고 시도 기록은 빈칸 8
4. 대상 회사: FIU 신고를 마친 원화 거래소(BN-E23). 손님 60만 명 넘음(2021-03, 회사 웹사이트, LDBN-021). 2021 원화 거래대금 점유율은 업비트 76.6%, 빗썸 18.5%, 코인원 4.5%(Xangle, LDBN-021). 설립 연도와 매출은 빈칸 8
5. 판 쪽: 2022-11 고팍스 예치 상품 고파이가 미국 Genesis 사태로 출금을 멈춤. Genesis 모회사 DCG는 2021-04 투자한 고팍스 2대 주주이고 스트리미는 Genesis 10대 채권자 중 하나(LDBN-021). 2023-01 현지 보도는 최대주주 이준행 CEO 지분 41.2% 매입 협상이라고 전함(TechCrunch 인용, LDBN-021)
6. 승인: 2023-03 FIU에 임원 변경 신고, 2025-10-15 수리(F-0073). (계산) 인수 발표부터 수리까지 985일. 당국과 회사 모두 늦어진 이유를 밝히지 않음(BN-E23)
7. 대금: 자금은 Binance 주도 공동투자 기금 Industry Recovery Initiative(10억 달러 약정)에서 나옴(LDBN-021). 금액은 F-1389(보도)
8. 같은 시기 바깥
   - 2023 초 BUSD 신규 발행 중단(BN-E22). 2023-06 미국 SEC가 Binance를 제소(BN-E25)
   - 경쟁: Kraken 2023-02-09 SEC와 미국 스테이킹 중단 합의(KR-E13). Robinhood 2023-02-13 영국 Ziglu 인수 계약 해지(RH-E18). Coinbase 2023-02-23 Base 발표(CB-E25)
9. 산 뒤
   - 수리 뒤에도 Binance와 호가창을 함께 쓰기 어렵고 국내에서 마진과 파생을 팔 수 없음(F-1553)
   - 2025-10 기준 고팍스 국내 점유율 1% 미만. 2025-09 Binance 앱 월간 활성 이용자 약 33만 명, 고팍스 5만 명(아이지에이웍스 모바일인덱스, 비즈워치 보도). 스트리미의 가상자산사업자 갱신 신고는 미수리(LDBN-022)
10. 발언: CZ 2023-02(quotes 파일 "고팍스")

### 1-5 Sim;paul (브라질 증권사, 2022-03 협상, 2025-01 승인)
1. 한 줄 사건: 2022-03 Binance가 브라질 포르투알레그리 증권사 Sim;paul 인수 협상을 발표. 2025-01-02 브라질 중앙은행(BC)이 연말연초에 인수를 승인했다고 발표(LDBN-026, [InfoMoney](https://www.infomoney.com.br/?p=2718163)). 지금 이름 Binance Brasil Corretora de Câmbio e Valores Mobiliários
2. 그 전 상태: Binance는 이미 브라질에서 글로벌 거래소로 영업하고 있었다고 회사가 밝힘(LDBN-027)
3. 직접 받는 길: 같은 인가를 직접 신청한 기록은 빈칸 9
4. 대상 회사: 전자화폐 발행(EMI)과 증권 유통 인가를 가진 증권사(LDBN-026). 설립 연도, 손님, 매출은 빈칸 9
5. 판 쪽: 빈칸 9
6. 승인: BC. 2022-03 발표부터 2025-01 승인 발표까지 약 2년 10개월(계산, LDBN-026). Bitcoin.com은 "2년 넘게 걸림"이라고 적음(LDBN-028)
7. 대금: 비공개(빈칸 9)
8. 같은 시기 바깥
   - 2022-03: 바레인 인가(LDBN-046), MX Global 지분(LDBN-013), 두바이 잠정 인가(LDBN-048)
   - 2025-01: 브라질 법안이 거래소의 브라질 안 본사를 요구하는 방향으로 논의 중(LDBN-026)
   - 경쟁: Coinbase는 2023-09 브라질을 우선 시장 여섯 곳에 넣음(F-1632). Robinhood 2024-11-19 TradePMR 인수 발표(RH-E28)
9. 산 뒤: Binance는 브라질에서 증권사 인가를 가진 첫 가상자산 거래소가 됨(LDBN-026). 단기적으로 가상자산 밖 상품 계획은 없다고 함(LDBN-028). 회사가 센 21번째 규제 이정표(LDBN-027)
10. 발언: Teng, Nazar(중남미 총괄) 2025-01(quotes 파일 "Sim;paul")

### 1-6 Gulf Binance (태국 합작, 2022-04 공시, 2023-05 인가)
1. 한 줄 사건: 2022-04-18 태국 Gulf Energy가 공시로 Binance와 태국 거래소 합작을 추진하고 합작사가 인가를 신청한다고 밝힘(LDBN-029, [Cointelegraph](https://cointelegraph.com/news/gulf-energy-pursues-joint-venture-with-binance-invests-in-bnb)). 2023-05-26 합작사 Gulf Binance가 디지털자산 사업자 인가를 받음(LDBN-031, F-1552)
2. 그 전 상태: 2021-07-02 태국 SEC가 Binance를 무인가 영업으로 형사 고발(F-1552)
3. 직접 받는 길: 합작사가 새로 신청(LDBN-029). Binance 단독 신청 기록은 빈칸 10
4. 대상 회사: 새로 세운 합작사. 상대 Gulf Innova는 Gulf Energy 자회사(LDBN-031)
5. 판 쪽: 해당 없음. Gulf Energy는 같은 공시로 Binance.US 운영사 BAM Trading 우선주와 BNB에도 투자(LDBN-029)
6. 승인: 재무부 인가 2023-05-26, SEC 영업 승인 2023-11(LDBN-030). (계산) 합작 공시부터 인가까지 약 13개월
7. 대금: 지분 구조와 출자액은 빈칸 10
8. 같은 시기 바깥: 2023-05-12 캐나다 철수(LDBN-034), 2023-06 SEC 제소(BN-E25), 2023-06-16 네덜란드 철수(LDBN-033). 경쟁: Coinbase 2023-05 버뮤다 인가 거래소에서 미국 밖 기관에 무기한선물(CB-E26)
9. 산 뒤: 2024-01-16 Binance TH 개장(LDBN-030). 2023-01~10 태국 거래소 거래대금 1,160억 달러 중 Bitkub 77%(CoinGecko, Bangkok Post 인용, LDBN-030). 태국은 bStocks 판매 제한 지역(F-1864). Binance TH 점유율은 빈칸 10
10. 발언: Teng 2023-05-26(quotes 파일 "태국")

### 1-7 MX Global 지분 (말레이시아, 2022-03)
1. 한 줄 사건: 2022-03-01 Binance가 Cuscapi Berhad와 함께 말레이시아 증권위원회(SC) 인가 디지털자산거래소 4곳 중 하나인 MX Global 지분을 삼(LDBN-013, [Cointelegraph](https://cointelegraph.com/news/binance-back-in-malaysia-via-a-strategic-stake-in-regulated-digital-exchange))
2. 그 전 상태: 2021-07 SC 명령 뒤 말레이시아 영업을 줄였음(LDBN-013). 말레이시아 당국의 2021-07 형사 고발(F-1706)
3. 직접 받는 길: 빈칸 11
4. 대상, 5. 판 쪽, 6. 승인, 7. 대금: 지분율, 금액, 승인 모두 빈칸 11
8. 같은 시기 바깥: 같은 달 바레인 인가(2022-03-14, LDBN-046), 두바이 잠정 인가(LDBN-048), 브라질 Sim;paul 협상(LDBN-026)
9. 산 뒤: 빈칸 11
10. 발언: 대변인 2022-03(quotes 파일 "MX Global")

## 4. 카드 2. 직접 받은 인가

### 2-1 바레인 중앙은행 가상자산서비스사업자 인가 (2022-03)
- 인가와 법인: 가상자산서비스사업자 인가(거래, 수탁, 포트폴리오 관리). 법인 이름은 빈칸 4
- 신청과 승인: 원칙 승인 뒤 약 3개월 만에 2022-03-14 정식 인가(LDBN-046, [FinanceFeeds](https://financefeeds.com/binance-gets-first-regulatory-licence-middle-east/)). CZ는 걸프협력회의 지역 첫 글로벌 가상자산 사업자 인가라고 트윗
- 연 상품: 빈칸 4
- 왜 그 나라: CZ "fully licensed and regulated around the world" 여정의 이정표(quotes 파일). 제도 특징은 빈칸 4
- 다른 세 회사: 이 저장소 자료에 바레인 인가 기록 없음

### 2-2 두바이 VARA (2022-03 잠정 → 2024-04 VASP)
- 법인: Binance FZE
- 단계: 2022-03 잠정 인가(사무소 설치, 사전 자격 투자자 대상, LDBN-048) → 2022-09-19 MVP 인가(F-0068) → 2023-07-31 운영 MVP(기관과 자격 개인만, 자격 개인은 21세 이상 순유동자산 50만 디르함, LDBN-049) → 2024-04-18 VASP 인가로 일반 개인 대상(LDBN-050, [Gulf News](https://gulfnews.com/business/markets/binance-receives-vasp-licence-from-dubais-virtual-assets-regulatory-authority-1.1713430742124))
- 걸린 기간: 잠정부터 VASP까지 약 25개월(계산). 2023-04 VARA가 추가 정보를 요구했음(LDBN-049)
- 연 상품: VASP 인가로 개인에게 현물, 마진(자격 이용자), 스테이킹. 파생은 자격, 기관 투자자만(LDBN-050)
- 왜 그 나라: CZ는 두바이에서처럼 세계 공통 이행 기준을 만들 기회라고 말함(LDBN-048). 2022-03 CZ는 두바이를 당분간 근거지라고 함(LDBN-047 기사). UAE 직원 약 1,000명(F-1555)
- 다른 세 회사: Coinbase는 Deribit 인수로 VARA 조건부 VASP 인가를 가진 Deribit FZE를 얻음(F-2095, CB-E34). Robinhood는 두바이 DIFC의 DFSA 인가(2026-10, F-1284. VARA와 다른 감독기관). Kraken은 VARA 정식 승인 뒤 출시 계획(F-0179)

### 2-3 아부다비 ADGM (2022-04 원칙 승인 → 2025-12 인가 3종)
- 단계
  - 2022-04: Binance Holdings가 ADGM에서 가상자산 중개 딜러 원칙 승인. 정식 인가가 나면 자회사 Binance (AD) Ltd로 중동 북아프리카 고객을 받는다고 함(LDBN-047, [Gulf News 2022-04-10](https://gulfnews.com/business/crypto-exchange-binance-gets-in-principle-approval-in-abu-dhabi-1.87098732))
  - 2024-11-29: ADGM FSRA 협의 문서에 의견서 제출(F-0724)
  - 2025-03-12: 아부다비 투자사 MGX가 20억 달러 투자(첫 기관 투자, 소수 지분, 스테이블코인 납입, F-0069, F-1555)
  - 2025-12-03: 공동 창업자 Yi He를 Teng과 함께 공동 CEO로 임명(LDBN-061)
  - 2025-12-08: FSRA가 Binance.com 글로벌 플랫폼을 세 법인으로 승인. Nest Services(곧 Nest Exchange) 인정투자거래소, Nest Clearing and Custody 인정청산기관(수탁, 중앙예탁), BCI Limited(곧 Nest Trading) 브로커딜러. 규제 영업 개시 2026-01-05(LDBN-062, F-0064, [보도자료](https://tools.prnewswire.com/en-us/live/20813/release/20251207EN41035))
  - 등록부: Nest Clearing and Custody(옛 이름 Binance (AD)) 인정청산기관 2025-12-08, Nest Exchange 인정투자거래소 2026-01-05(F-1418)
- 걸린 기간(계산): 원칙 승인 보도부터 1,338일. MGX 투자 발표부터 271일. 공동 CEO 임명부터 5일
- 공동 CEO의 감독청 경력
  - Teng은 Binance 합류 전 ADGM FSRA CEO(F-0685). 그 재임 중 ADGM은 5년이 안 돼 인가 약 2,700건, 승인 금융기관 150곳 넘게 됨(LDBN-059, Fintech News Singapore 2021-08-23). 그 전 싱가포르거래소 최고규제책임자(LDBN-059)
  - 2021-08 Binance Singapore CEO 합류, 2022-04 중동 북아프리카 총괄(LDBN-047), 2023-01 유럽과 중동 북아프리카 총괄(LDBN-044), 2023-05 미국 밖 지역 시장 총괄, 2023-11-21 CEO(LDBN-058)
  - 아부다비 정부 미디어오피스는 MGX 발표에 Teng이 세계 첫 가상자산 규제 틀의 하나를 시작하는 데 핵심 역할을 했고 그 경력이 Binance 규제 전략에 결정적이라고 적음(LDBN-060, [Abu Dhabi Media Office 2025-03-12](https://www.mediaoffice.abudhabi/en/economy/mgx-invests-in-binance-cryptocurrency-exchange-in-landmark-us2bn-deal/))
  - Teng의 FSRA CEO 재임 시작일과 끝난 날은 빈칸 12
- MGX 투자와 인가의 관계: 회사나 당국이 둘을 잇는 문장은 찾지 못함(빈칸 13). (판단) 같은 관할의 정부 계열 투자사가 주주가 된 뒤 271일 만에 같은 관할 인가가 나옴. 근거: F-0069, LDBN-062. 인과는 확인하지 못해 잇지 않음
- 연 상품: 2026-01-08 TradFi 무기한선물(BN-E35), 2026-06-01 미국 주식(BN-E39), 2026-06-12 bStocks(BN-E40), 2026-09-01 주식 옵션(BN-E44)
- 왜 그 나라: 규제 명확성과 정당성(Teng, F-1071). 이 인가가 UAE 밖 여러 시장 접근에 신뢰를 준다(회사 주장, F-1554). 원문은 quotes 파일
- 다른 세 회사: Coinbase는 아부다비 SPV(Coinbase Onchain SPV Ltd)로 2026-08-24 미국 밖 개인용 주식 토큰 발행(CB-E50), UAE에 아부다비 토큰증권 허브와 두바이 파생 허브 계획(F-0097). Kraken, Robinhood의 ADGM 인가는 이 저장소 자료에 없음

### 2-4 프랑스 AMF 등록 PSAN (2022-05)
- 법인: Binance France SAS. 승인일 2022-05-04(CZ 트윗, LDBN-041, [Euronews](https://www.euronews.com/next/2022/05/05/crypto-exchange-binance-gets-french-regulatory-approval-eyes-paris-as-regional-hub-in-euro)). 신청일 빈칸 14
- 성격: 등록. Binance France는 지역 본부를 위해 정식 인가도 추진한다고 함(LDBN-041)
- 왜 그 나라: 파리를 유럽 거점으로 삼으려고. CZ는 앞서 프랑스에 1억 유로 투자를 약속(LDBN-041). 프랑스는 Binance를 등록한 첫 EU 회원국. 같은 때 스위스, 스웨덴, 스페인, 네덜란드, 포르투갈, 오스트리아 등록 추진 중이라고 함(LDBN-041)
- 다른 세 회사: Kraken은 MiCA 전부터 프랑스 등 나라별 VASP 등록을 가짐(F-1438)이고 2024-09-24 BCM 인수로 프랑스, 폴란드 등록을 더함(F-1808)

### 2-5 이탈리아 OAM 등록 (2022-05)
- 법인: Binance Italy. 2022-05-27 OAM 등록(LDBN-042, [Cointelegraph](https://cointelegraph.com/news/binance-gets-approval-to-operate-in-italy-will-open-office-in-milan)). 본사 밀라노. 신청일 빈칸 14
- 그 전: 2021 이탈리아 당국이 Binance 상품의 인가 대상 여부를 조사(F-1707), 2021 주식 토큰 관련 지적(F-1534)
- 왜 그 나라: "가능한 모든 곳에서 인가와 등록을 받으려 함"(대변인, quotes 파일)
- 다른 세 회사: Kraken 이탈리아 VASP 등록(F-1438)

### 2-6 스페인 중앙은행 등록 (2022-01 신청, 2022-07 등록)
- 법인 Moon Tech Spain. 2022-01-28 신청, 2022-07-07 등록, 160일(계산, LDBN-043, [Finance Magnates](https://www.financemagnates.com/cryptocurrency/news/binance-obtains-vasp-registration-in-spain/))
- 연 상품: 스페인에서 가상자산 교환과 수탁(같은 기사). 스페인어권 인력 채용 계획(Binance Spain 대표)
- 다른 세 회사: Kraken 스페인 VASP 등록(F-1438)

### 2-7 리투아니아 VASP 등록 (Bifinity UAB, 2020~2025)
- Bifinity는 2020부터 리투아니아에서 영업한 Binance 법인이고 리투아니아 큰 납세자 중 하나(LDBN-055, [LRT 2026-06-11](https://www.lrt.lt/naujienos/verslas/4/2957021/binance-traukiasi-is-lietuvos-padalinio-uzdarymui-vadovauja-elcinas-mamedovas)). 등록일은 빈칸 15
- 결과: 2025-12-31부터 Binance 이용자 서비스 중단, 2026-01부터 필요한 MiCA 인가를 받지 못함(카드 3-13)
- 다른 세 회사: Robinhood Europe UAB(리투아니아)는 2025-05-29 MiCA 인가(F-1414)

### 2-8 키프로스 CySEC 3등급 CASP 등록 (2022-10 → 2023-09 말소)
- 법인 Binance Cyprus Limited, 2022-10-20 등록(현물, 수탁, 스테이킹, 카드, LDBN-037, [Cyprus Mail](https://cyprus-mail.com/2022/10/21/cysec-issues-crypto-asset-license-to-binance)). 근거는 CySEC 자금세탁방지 규칙
- 결과: 카드 3-8
- 다른 세 회사: Kraken은 2025-02 키프로스 투자회사를 사서 EU 증권 인가를 얻음(KR-E18, 가상자산 등록과 다른 인가)

### 2-9 폴란드 VASP 등록
- 법인 Binance Poland sp. z o.o. 2022-11-30 회사 목록에 이미 있고 2023-01-18 폴란드 기준 충족을 발표, 폴란드 이용자는 새 약관 동의 필요(LDBN-045, [Cointelegraph](https://cointelegraph.com/news/binance-registers-as-virtual-assets-service-provider-in-poland)). 등록일은 빈칸 5
- 그 뒤 쓰임: 2023-06 벨기에 중지 명령 뒤 벨기에 이용자를 이 법인으로 옮김(LDBN-035)
- 다른 세 회사: Kraken은 BCM 인수로 폴란드 등록을 얻음(F-1808)

### 2-10 스웨덴 금융감독청 등록 (2023-01)
- 법인 Binance Nordics AB(등록번호 66822), 2023-01-10 등록(LDBN-044, [보도자료 전재](https://www.aap.com.au/aapreleases/cision20230111ae83777/)). 신청일 빈칸 14. 회사는 수개월 협의 결과라고 함
- 연 상품: 유로 입출금, 현물, 마진, 스테이킹, Binance Pay, 카드 등(같은 보도자료)
- 다른 세 회사: 이 저장소 자료에 없음

### 2-11 카자흐스탄 AIFC AFSA (2022-08 원칙 → 2024-09 정식 DATF)
- 2022-08 원칙 인가, 2022-10 정식 인가, 2023-01 AFSA가 디지털자산거래시설(DATF) 틀을 재편, 2024-09 정식 DATF 동의, 2024-09 말 정식 DATF 인가(거래시설, 중개 딜러, 수탁)(LDBN-051, LDBN-052)
- 걸린 기간: 원칙부터 정식 DATF까지 약 25개월(계산). 외부 재무 감사, ISO 인증, 내외부 감사를 거침(회사 성명, LDBN-051)
- 제도 특징: 2023-02 디지털자산법 통과 뒤 AFSA가 무인가 거래소 980곳 접속을 막음(Coinbase 포함, Cointelegraph, LDBN-051 기사)
- 다른 세 회사: Kraken AFSA 원칙 승인(F-0179)

### 2-12 엘살바도르 BSP, DASP (2023-08)
- 2023-08-08 중앙은행이 비트코인 서비스사업자, 국가디지털자산위원회가 디지털자산서비스사업자 인가(LDBN-053, [Decrypt](https://decrypt.co/151727/binance-secures-crypto-exchange-license-el-salvador)). 법인, 신청일 빈칸 16
- 다른 세 회사: 이 저장소 자료에 없음

### 2-13 인도 FIU-IND 등록 (2024-08)
- 2024-08-15 보고 의무 기관 등록을 발표하고 인도 이용자에게 웹사이트와 앱을 다시 엶. 회사가 센 19번째 규제 이정표(LDBN-054). 등록 전 FIU 과징금 1.882억 루피(약 225만 달러)(Decrypt 기사 제목). 신청일 빈칸 16
- 그 전: 2019 WazirX 거래(카드 3-2)

### 2-14 아르헨티나 CNV 등록 (2024-09)
- Binance Services Latinoamérica가 2024-09-11 PSAV 등록부 No. 76. 회사는 이 등록이 CNV 인가나 감독이 아니라고 명시(F-0712, F-0713, BN-E28)

## 5. 카드 3. 실패, 해지, 철회, 철수

### 3-1 FTX 인수 의향서와 다음 날 철회 (2022-11)
- 하려던 것: 2022-11-08 CZ가 FTX의 요청으로 FTX.com 전부를 인수하는 구속력 없는 의향서에 서명했다고 트윗. FTX.US는 제외. CZ는 Binance가 언제든 빠질 수 있다고 함(LDBN-023, [SiliconANGLE](https://siliconangle.com/2022/11/08/binance-nixes-deal-acquire-ftx-liquidity-crisis/))
- 앞뒤: 2022-11-06 Binance가 보유 FTT 매도를 발표. SBF는 CZ가 FTX의 첫 투자자였다고 트윗(LDBN-023)
- 멈춘 이유: 2022-11-09 Binance 트윗. 실사 결과와 고객 자금 유용, 미국 기관 조사 보도(원문은 quotes 파일)
- 그 뒤: 2022-11-17 CZ는 자신들이 "낙타 등을 부러뜨린 마지막 지푸라기"였다고 말함(LDBN-025 기사, F-2232). 2022-11-30 일본 SEBC 인수(카드 1-3), 2023-02 고팍스 인수에 산업 회복 기금 사용(카드 1-4)

### 3-2 WazirX (2019-11 발표, 2022-08 미완료 주장)
- 하려던 것: 2019-11-21 Binance 블로그가 인도 거래소 WazirX 인수를 발표(보도상 최대 1,000만 달러)(LDBN-008, [Decrypt](https://decrypt.co/106944/binance-never-completed-acquisition-troubled-crypto-exchange-wazirx-changpeng-zhao))
- 멈춘 이유(회사 발언): 2022-08-05 CZ가 거래가 완료되지 않았고 운영 법인 Zanmai Labs 지분을 가진 적 없다고 트윗. WazirX는 완료됐다고 주장. 같은 시기 인도 집행국이 WazirX 자산을 동결(LDBN-008)
- 그 뒤: 2024-08 Binance 자체 법인으로 FIU-IND 등록(카드 2-13)

### 3-3 영국 (2020-06 법인 인수, 2021-06 FCA 조치, 2023-10 신규 가입 중단)
- 하려던 것: 2020-06 EddieUK를 사서 Binance Markets Limited로 이름을 바꿈. binance.uk 출범용이었으나 출범하지 못함(LDBN-063, [Decrypt 2021-06-28](https://decrypt.co/74658/uk-fca-reveals-its-huge-issue-with-binance-no-hq-and-aml-approach))
- 멈춘 이유: 2021-06-26 FCA가 Binance Markets Limited의 영국 규제 영업을 막음. FCA는 본사가 없다는 점을 "큰 문제"라고 함(F-1706, F-1709, BN-E18)
- 그 뒤: 2023-10-16 신규 영국 이용자 가입 중단. FCA 광고 규칙(2023-10-08 시행)에서 광고 승인을 맡던 Rebuildingsociety.com이 FCA 제한을 받아서. 새 승인자를 찾는 중이라고 함(LDBN-040, [Decrypt](https://decrypt.co/201841/binance-says-no-to-brits-crypto-exchange-stops)). 영국은 bStocks 제한 지역(F-1864)
- EddieUK가 인수 전 FCA 인가를 가졌는지는 빈칸 17

### 3-4 싱가포르 MAS 신청 철회 (2021-12)
- 하려던 것: Binance Asia Services가 MAS 거래소 인가를 신청해 Binance.sg 영업
- 멈춘 것: 2021-12-13 신청 철회, Binance.sg 폐쇄 결정(LDBN-014, [Decrypt](https://decrypt.co/88111/binance-withdraws-application-license-singapore))
- 그 뒤 대신 한 것: 철회 1주일 전 싱가포르 사설 증권거래소 Hg Exchange 지분 18% 발표(Cointelegraph 2022-03-02 정리, LDBN-013 기사). 싱가포르를 연구개발 거점으로 둔다고 함(Teng)

### 3-5 캐나다 (2021 온타리오, 2023-05 전체)
- 2021 온타리오 등록을 하지 못해 온타리오에서 철수, 2022 앨버타에 법인을 세움(LDBN-034, [BetaKit](https://betakit.com/binance-exits-canada-as-crypto-trading-platforms-feel-broader-impact-of-stricter-regulations/))
- 2023-05-12 캐나다 전체 철수 트윗. 스테이블코인과 투자자 한도에 관한 새 지침 때문(LDBN-034, 원문은 quotes 파일). 그 전 달 Paxos, OKX가 캐나다 철수 발표, Binance 캐나다 총괄 사임(LDBN-034)
- 다른 세 회사: Robinhood는 2026-06-01 캐나다 등록 플랫폼 WonderFi를 인수해 진출(F-1999, F-2001)

### 3-6 호주 파생 법인 인가 취소 (2023-04)
- 2023-04-06 ASIC가 Binance Australia Derivatives(Oztures Trading)의 금융서비스 인가를 회사 요청으로 취소. ASIC는 2023-02부터 일부 개인을 도매 투자자로 잘못 분류한 문제를 점검했음. 파생 포지션은 2023-04-21까지 모두 청산(LDBN-057, [Gulf News](https://gulfnews.com/business/markets/australia-cancels-binances-financial-services-licence-amid-probe-1.1680798214549))
- 회사 발언: ASIC와 협의 뒤 호주에서 "더 집중된 방식". 2026-07 Teng은 아시아 진출국에 호주를 넣음(F-1548)
- 이 인가를 언제, 어떻게(직접 또는 인수) 얻었는지는 빈칸 18

### 3-7 Binance.US의 Voyager 자산 인수 해지 (2023-04)
- 하려던 것: 파산한 미국 중개사 Voyager Digital의 자산과 손님을 약 10억 달러에 인수. 2022-12-19 Binance.US가 최고 입찰자로 뽑혔다는 보도. FTX가 붕괴 전 낸 14억 달러 입찰보다 27% 낮은 값(LDBN-064, [Blockhead](https://www.blockhead.co/2022/12/20/binance-acquires-indonesias-tokocrypto-after-voyager-deal); LDBN-028)
- 멈춘 이유: 2023-04-25 Binance.US가 해지. "적대적이고 불확실한 미국 규제 환경"(Binance.US 트윗). 미국 연방 당국이 저지를 접은 지 1주일 안(LDBN-028, [Finance Magnates](https://www.financemagnates.com/cryptocurrency/binanceus-terminates-1b-voyager-asset-purchase-deal/))
- 그 뒤: 2023-06 SEC가 Binance, Binance.US를 제소(BN-E25), Binance.US 미국 점유율 하락(F-1702)

### 3-8 키프로스 등록 말소 (2023-06 신청, 2023-09 말소)
- 2023-06-14 CySEC이 Binance Cyprus를 등록 말소 신청 심사 대상으로 올림(LDBN-033 기사). 2023-09-11 말소 확인. 6개월 넘게 연속으로 이 등록으로 영업하지 않았기 때문(LDBN-038, [Finance Magnates](https://www.financemagnates.com/cryptocurrency/cyprus-regulator-officially-deregisters-local-binance-entity/))
- 회사 발언: 앞으로 18개월 MiCA 준수에 집중하고 더 큰 EU 시장에 힘을 모음(Cointelegraph 2023-06-16 인용, LDBN-033 기사)

### 3-9 네덜란드 (2022-04 과징금, 2023-06 철수)
- 2022-04 네덜란드 중앙은행(DNB)이 무등록 영업으로 300만 달러 넘는 과징금(Cointelegraph 정리, LDBN-033). 과징금 결정일과 정확한 금액의 1차 확인은 빈칸 19
- 2023-06-16 VASP 등록을 하지 못해 네덜란드 철수 발표. 다른 길을 찾았으나 등록 경로가 없었다고 함. 2023-07-17부터 출금만(LDBN-033, [Cointelegraph](https://cointelegraph.com/news/binance-crypto-exchange-exits-netherlands))
- 등록이 안 된 이유에 대한 DNB 발표는 빈칸 19

### 3-10 벨기에 (2023-06 중지 명령, 2023-09 재개)
- 2023-06-23 FSMA가 EEA 밖에서 벨기에 고객에게 영업했다며 즉시 중지 명령. FSMA는 EEA 다른 회원국 인가 법인을 통한 영업은 허용(LDBN-035, [The Next Web](https://thenextweb.com/news/crypto-binance-belgium-eu-poland))
- 대신 한 것: 벨기에 이용자를 Binance Poland로 옮기고 2023-09-25 신규 가입 재개(LDBN-036)

### 3-11 독일 BaFin 수탁 인가 신청 철회 (2023-07)
- 2023-06-29 BaFin 거절 보도, 2023-07-26 Binance가 스스로 철회했다고 확인. 다시 신청할 계획(LDBN-039, [Cointelegraph](https://cointelegraph.com/news/binance-withdraws-crypto-license-germany))
- 신청일은 빈칸 14

### 3-12 러시아 사업 매각 (2023-09)
- 2023-09-27 러시아 사업 전부를 CommEX에 매각. 이용자 정리 최대 1년. 수익 배분과 되사기 선택권 없음(LDBN-032, [보도자료 전재](https://aap.com.au/aapreleases/cision20230927ae21598/))
- 멈춘 이유: 러시아 영업이 준법 전략과 맞지 않음(최고준법책임자 Perlman, quotes 파일)
- 매각 금액과 CommEX 주주는 빈칸 20

### 3-13 리투아니아 Bifinity 철수 (2025-12)
- 2025-12 Binance는 리투아니아 규제 변화로 2025-12-31부터 Bifinity가 Binance 이용자 서비스를 끊는다고 발표. 법정화폐 업무는 프랑스 감독 Harmoniie와 리투아니아 중앙은행 인가 Zen.com으로 넘김. 2026-01부터 필요한 MiCA 인가를 받지 못했다고 리투아니아 중앙은행이 확인. 2026-04-14 이사회가 청산 책임자 선임(LDBN-055)

### 3-14 그리스 MiCA 인가 신청 철회 (2026-01 신청, 2026-06 철회)
- 하려던 것: 2026-01 그리스 자본시장위원회(HCMC)에 MiCA 인가 신청. 그리스를 고른 이유의 하나로 최근 경제 성장을 듦(대변인, LDBN-056, [Decrypt](https://decrypt.co/371990/binance-withdraws-mica-license-application-greece-eu-users-limbo))
- 멈춘 이유: 2026-06-24 철회. HCMC가 2026-07-01 기한 전에 답하지 않아 다른 EU 회원국에서 인가를 받겠다고 함. 철회 1주일 전 Reuters가 거절 예정이라고 보도(LDBN-056)
- 그 뒤: Teng은 EU에서 빠져나간 자금의 70%가 개인 지갑, 30%만 MiCA 인가 거래소로 갔다고 말함. 아시아(일본, 한국, 태국, 인도네시아, 호주, 필리핀) 진출을 듦(F-1548). ESMA 등록부에 Binance 법인 없음(F-1549, 2026-11-11)

### 3-15 기존 사건 카드에 있는 철수 (다시 찾지 않음)
- 2017-09 중국 금지 전 일본으로 이전, 2018 일본 경고 뒤 몰타(BN-E03, BN-E05)
- 2021 한국 철수(BN-E16), 2021-07 주식 토큰 신규 판매 중단(BN-E17), 2021 독일, 이탈리아, 네덜란드에서 선물과 파생 중단(F-1707)

## 6. 직접 인가와 인수가 갈린 나라 대조표 (사실만, 해석은 (판단))

| 나라 | 그 전 당국 조치 | 들어간 길 | 날짜 | 근거 |
|---|---|---|---|---|
| 일본 | 2018, 2021-06 무등록 경고 | 직접 신청 예고(2022-09) 뒤 등록 회사 인수 | 2022-11-30 | F-1551, LDBN-018, LDBN-015 |
| 한국 | 2021 철수(신고 의무 시행) | 신고 마친 거래소 인수 | 2023-02-03 | F-0074, LDBN-021 |
| 인도네시아 | Bappebti 승인 의무화 | 첫 승인 거래소에 투자 | 2020-05-12 | LDBN-009, LDBN-011 |
| 말레이시아 | 2021-07 SC 명령, 형사 고발 | 인가 거래소 지분 | 2022-03-01 | LDBN-013, F-1706 |
| 태국 | 2021-07-02 SEC 형사 고발 | 현지 대기업과 합작 뒤 새 인가 | 2023-05-26 | F-1552, LDBN-029 |
| 싱가포르 | 2021 MAS 신청 심사 중 | 신청 철회, 인가 거래소 지분 18% | 2021-12-13 | LDBN-014 |
| 브라질 | 거래소 현지 본사 요구 법안 논의 | 증권사 인수 | 2022-03 협상, 2025-01 승인 | LDBN-026 |
| 영국 | 2021-06 FCA 조치 | 2020 법인 인수 뒤 막힘 | 2020-06 | LDBN-063, F-1709 |
| EU 나라별(프랑스, 이탈리아, 스페인, 리투아니아, 키프로스, 폴란드, 스웨덴) | 2021 여러 나라 경고(F-1707) | 직접 등록 | 2022-05~2023-01 | LDBN-041~045, LDBN-037 |
| EU MiCA | 2026-07-01 경과기간 종료 | 그리스 직접 신청 뒤 철회 | 2026-06-24 | LDBN-056 |
| 바레인, 두바이, 아부다비, 카자흐스탄, 엘살바도르 | 이 저장소 자료에 당국 경고 기록 없음 | 직접 인가 | 2022-03~2025-12 | LDBN-046~053, LDBN-062 |

- (판단) 인수, 지분, 합작 쪽 나라(일본, 한국, 말레이시아, 태국)는 모두 그 전에 당국이 Binance 영업을 경고하거나 고발한 나라임. 근거: F-1551, F-0074, F-1706, F-1552. 직접 인가 쪽 걸프 나라와 카자흐스탄은 2022 원칙 승인부터 시작한 새 제도임(LDBN-046~052). 이 구분을 회사가 말한 문장은 찾지 못함(빈칸 21)
- (판단) 인수로 들어간 나라도 시간을 줄이지 못한 경우가 있음: 한국 신고 수리 985일(계산, F-0073), 브라질 승인 약 2년 10개월(LDBN-026). 일본은 인수 뒤 출범까지 244일(LDBN-019)

## 7. 빈칸 목록

1. JEX: 설립 연도, 판 쪽, 손님과 거래량, 인수 뒤 JEX 브랜드와 팀의 쓰임, 2019-08 이전 제휴. The Block 원문(theblock.co)은 403, CoinDesk는 429로 막힘
2. JEX와 Binance Futures에 받은 인가나 승인 여부. 회사가 밝힌 자료를 찾지 못함
3. 2019-09 파생 시장 점유율(거래소 합계 기준 BitMEX 대 Binance). CryptoCompare 발표문에 BitMEX 합계가 없음. 2019-09 Exchange Review PDF 원문은 찾지 못함(검색 요약의 "BitMEX 무기한선물 417억 달러"는 원문 미확인이라 넣지 않음)
4. 바레인 인가 법인 이름, 원칙 승인 정확한 날짜, 연 상품. CBB 등록부 미열람
5. 폴란드 등록 정확한 날짜(2022-11-30 이전). 폴란드 등록부 미열람
6. Tokocrypto: 2020 지분율(The Block은 지배 지분 보도, theblock.co 403), 지분 취득 승인 당국, Binance 자체 인도네시아 신청 여부, 인도네시아에서 경쟁 세 회사의 움직임
7. SEBC: 전 주인과 판 이유, 손님 수와 거래량, 인수에 대한 금융청 승인 여부(검색 요약에 Financial Times가 "승인 불필요"라고 썼다는 말이 있으나 원문 미확인), 2022-09 직접 신청서 실제 제출 여부, 같은 시기 Coinbase, Robinhood 일본 움직임
8. 고팍스: 설립 연도, 매출, Binance의 한국 직접 신고 시도 여부
9. Sim;paul: 설립 연도, 손님, 매출, 전 주인, 대금. 2022-03 MoU 원문(mergerlinks 검색 결과만, 미열람)
10. Gulf Binance: 지분 구조(51:49 보도는 검색 요약만), 출자액, Binance TH 점유율
11. MX Global: 지분율, 금액, 그 뒤 관계
12. Teng의 ADGM FSRA CEO 재임 시작일과 끝난 날(검색 요약에 2015 시작이라는 말이 있으나 newswire.ca 원문 403)
13. MGX 투자와 ADGM 인가를 잇는 회사나 당국 발언. 찾지 못함
14. 프랑스, 이탈리아, 스웨덴 등록과 독일 BaFin 신청의 신청일. AMF 목록 주소 404, 다른 등록부 미열람
15. 리투아니아 Bifinity 등록일. 리투아니아 법인등록센터 미열람
16. 엘살바도르, 인도 인가 법인 이름과 신청일
17. EddieUK가 인수 전 가진 FCA 지위. FCA 등록부 미열람
18. 호주 파생 법인(Oztures Trading) 인가를 얻은 시점과 방법
19. 네덜란드 DNB 과징금 결정 1차 문서(dnb.nl 추측 주소 404), 등록 실패 이유
20. 러시아 매각 금액과 CommEX 주주(회사 비공개)
21. 직접 인가와 인수를 고른 기준에 대한 회사 발언. CZ 2022-11-02 발언(LDBN-024)과 2020 발언(LDBN-010) 밖에 찾지 못함
22. Swipe 잔여 지분 인수(2020-12 보도 검색 요약만, 연도 미확인)

- 막힌 경로: theblock.co(403), coindesk.com(429), cryptoglobe.com(429), benzinga.com(403), investmentexecutive.com(403), cnbc.com(403), news.abs-cbn.com(403), arabianbusiness.com(403), newswire.ca(403), finextra.com(403), wam.ae(본문 비어 있음), binance.com 공지(202 봇 확인, 우회하지 않음), amf-france.org와 fca.org.uk와 dnb.nl와 fsma.be의 추측 주소(404). 우회, 브라우저 위장은 하지 않음
