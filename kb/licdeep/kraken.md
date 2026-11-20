# Kraken(Payward) 인가 획득 딥다이브: 인수, 직접 인가, 철수 카드

- 범위: Payward, Inc.(Kraken 모회사, 비상장)와 자회사의 회사 인수, 직접 받은 인가, 실패와 철수. 2026-11-20 열람 기준
- 근거 번호: F- 는 db/facts.csv, LDKR- 는 이번에 새로 확인한 사실(work/LICDEEP-KR/facts.csv), KR-E 는 사건 카드(kb/events/kraken_events_src.py). 번호를 누르면 원문 링크
- 표기: (판단)은 해석이고 근거 번호를 같이 씀. (회사 주장), (보도, 매체명), (계산). 확인하지 못한 칸은 비우고 맨 끝 빈칸 목록의 번호(B01 꼴)만 적음
- 우리 분류
  - 인가 인수: 인가를 가진 회사를 사서 그 인가를 살려 쓴 건
  - 고객 인수: 고객, 인력, 기술을 흡수하고 법인 인가는 쓰지 않은 건

## 1. 모든 인수 목록 (회사째 산 것, 발표일 순)

| 발표일 | 완료일 | 대상 | 대상이 하는 일 | 얻은 인가나 손님 | 대금 | 깊게 봄 | 출처 |
|---|---|---|---|---|---|---|---|
| 2016-01-19 | 2016-01-26 계정 이전 | Coinsetter(뉴욕, 2012 설립)와 그 자회사 Cavirtex(캐나다, 2011 설립) | 비트코인 거래소 | 북미 고객과 직원(브랜드 흡수, 인가는 쓰지 않음) | 비공개 | 아니오(고객 인수) | [F-1752](https://blog.kraken.com/news/kraken-acquiring-coinsetter-and-cavirtex-to-expand) [F-1753](https://blog.kraken.com/news/krakens-story-in-canada) |
| 2016-06-28 | 2016-06-29 계정 이전 | CleverCoin(네덜란드, 2013 설립) | 비트코인 거래소 | 유럽 고객 수천 명 | 비공개 | 아니오(고객 인수) | [F-1761](https://blog.kraken.com/news/kraken-acquires-dutch-bitcoin-exchange-clevercoin) |
| 2016-12-13 | 발표일(완료형) | Glidera(시카고, 2015 출시) | 지갑 이용자의 미국 은행 자동이체 비트코인 매매 | 지갑 제휴처, 창업 인력(공동 창업자 Dave Ripley는 2022 CEO) | 비공개 | 아니오(고객 인수) | [F-1762](https://blog.kraken.com/news/kraken-acquires-glidera) [F-1793](https://blog.kraken.com/news/kraken-announces-leadership-succession-plan) |
| 2017-03-01 | 발표일(완료형) | Cryptowatch | 차트와 거래 화면 | 기술과 이용자 | 비공개 | 아니오 | [F-1763](https://blog.kraken.com/news/kraken-acquires-cryptowatch-and-launches-new-trade) |
| 2019-02-04 | 발표일(완료형) | Crypto Facilities Ltd(런던, 2015 설립) | 가상자산 선물 거래장, 비트코인 기준가 산출 | 영국 FCA 인가(FRN 757895), 선물 고객 | 9자리 금액(1억 달러 이상), 비율 비공개 | 예(1-1) | [F-1803](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release) [F-1778](https://blog.kraken.com/product/unlock-futures-trading-with-our-crypto-facilities-acquisition) [F-1779](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release) |
| 2019-07-31 | 발표일(완료형) | Interchange | 기관 트레이더 포트폴리오 대사 도구 | 팀 | 비공개 | 아니오 | [F-1804](https://blog.kraken.com/news/interchange-founders-on-kraken-acquisition) |
| 2019-12-17 | 진행형 발표 | Circle Trade(Circle의 장외 데스크) | 장외 대량 거래 | 장외 인력 20명 넘게, 아시아 거래 상대 | 비공개 | 아니오 | [F-1805](https://blog.kraken.com/news/kraken-otc-acquires-circle-trade) |
| 2020-01-14 | 발표일(완료형) | Bit Trade Pty Ltd(호주, 2013 설립) | 호주 가상자산 거래소 | 호주 고객, 현지 대표 | 비공개 | 예(1-2) | [F-1806](https://blog.kraken.com/news/kraken-acquires-australias-longest-running-crypto-service-provider-bit-trade) [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf) |
| 2021-12-21 | 발표일(완료형) | Staked | 비수탁 스테이킹 인프라 | 기술과 고객 | 비공개(업계 최대급이라고만 밝힘) | 아니오 | [F-1802](https://blog.kraken.com/news/kraken-to-allow-a-new-way-to-earn-crypto-rewards-with-staked-acquisition) |
| 2023-10-05 | 2024-09-24 | Coin Meester B.V.(BCM, 네덜란드, 2017 설립) | 가상자산 중개 | 네덜란드 고객, 프랑스와 폴란드 VASP 등록 | 비공개 | 예(1-3) | [F-1807](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business) [F-1808](https://blog.kraken.com/news/kraken-bcm) |
| 2025-02-28 이전(빈칸 B01) | 빈칸 | Beaufort Fiduciaries Pty Ltd(호주) | 호주 금융서비스 인가(AFSL 545124) 보유 회사 | 도매 고객용 파생 인가 | 비공개 | 예(1-2 안에서) | [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf) |
| 2025-02-03 | 비공개(법인 이름 변경 2025-01-24) | Greenfields Wealth(옛 Pacific Union Group, 키프로스) | CFD 투자회사 | CySEC 투자회사 인가 342/17(EU MiFID) | 비공개 | 예(1-4) | [F-1809](https://blog.kraken.com/news/eu-mifid-license) [F-1810](https://www.cysec.gov.cy/en-GB/entities/investment-firms/cypriot/45914/) [F-1811](https://api.gleif.org/api/v1/lei-records/2138006O8D7SV36PWU16) [F-1812](https://www.financemagnates.com/forex/exclusive-krakens-cyprus-move-pu-prime-linked-cfds-firm-revealed-as-acquisition-target/) |
| 2025-03-20 | 2025-05-01 | NinjaTrader Group(시카고, 2003 설립) | 개인 선물 거래 앱과 선물 중개사(FCM) | CFTC FCM, 트레이더 약 200만 명 | 15억 달러(가격 조정 조항), 비율 비공개 | 예(1-5) | [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader) [F-0177](https://www.financemagnates.com/cryptocurrency/kraken-completes-15b-ninjatrader-acquisition-as-funded-accounts-jump-26-in-q1/) [F-2031](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader) |
| 2025-08-20 | 자산 인수 | Capitalise.ai(이스라엘, 2015 설립)의 자산과 기술 | 말로 쓴 문장을 매매 전략으로 바꾸는 자동화 | 기술과 창업 인력 | 비공개 | 아니오 | [LDKR-020](https://www.payward.com/press-release/kraken-acquires-capitalise-ai-trading-automation) |
| 2025-09-04 | 효력 2025-09-01 | Breakout | 평가형 프롭 트레이딩 | 트레이더 고객(인가 없음) | 비공개 | 아니오 | [F-1252](https://blog.kraken.com/news/kraken-acquires-breakout) [LDKR-021](https://www.payward.com/press-release/kraken-acquires-breakout-for-global-prop-trading) |
| 2025-10-16 | 2025-10-16 | Small Exchange, Inc.(시카고, 2019 출범) | CFTC 지정 선물 거래소(DCM) | DCM 인가(손님 없음은 빈칸 B13) | 1억 달러 = 현금 3,250만 + Payward 주식 6,750만 | 예(1-6) | [F-1116](https://blog.kraken.com/news/acquires-small-exchange) [F-2028](https://financialreports.eu/filings/8026393/content) |
| 2025-12-02 | 2026-01-05경 지분 100% | Backed Finance AG(스위스, 2021 설립) | 주식 토큰 xStocks 발행 | 발행 체계(저지 발행 법인), 지식재산 | 비공개 | 예(1-7) | [F-0139](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion) F-0939(로컬 저장 문서) F-0923(로컬 저장 문서) |
| 2026-05-18 이전(빈칸 B02) | 발표일(완료형) | Magna | 가상자산 프로젝트의 토큰 지급 일정, 청구, 배분 대행 | 기술과 고객 | 비공개 | 아니오 | [F-2033](https://www.payward.com/press-release/payward-acquires-magna) |
| 2026-04-17 | 2026-05-01 | Bitnomial(시카고) | 가상자산 선물 거래소, 청산소, 선물 중개 | DCM, DCO, FCM 세 인가 | 최대 5.5억 달러(현금과 주식, Payward 주식가치 200억 달러 기준) | 예(1-8) | [F-2029](https://www.payward.com/press-release/payward-to-acquire-bitnomial) [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us) |
| 2026-05-07 | 2026-07-01 | Reap Technologies Holdings Limited | 스테이블코인 기반 카드 발급, 국경 간 송금 | 아시아태평양과 미주 인가, 기업 고객 | 최대 6억 달러(현금과 Payward 주식, 200억 달러 기준) | 예(1-9) | [F-2030](https://www.payward.com/press-release/payward-acquires-reap) [F-1195](https://www.payward.com/press-release/payward-reap-close) |
| 2026-07-27 | 합의 단계 | Magic Labs의 지갑 대행 사업 | 파트너 앱 안 비수탁 지갑 | 지갑 6,000만 개, 개발자 20만 | 비공개 | 아니오 | [F-1514](https://www.payward.com/press-release/payward-to-acquire-magic-labs-wallet-infrastructure) |
| 2026-10-14 | 2027 예상(규제 승인 필요) | Saldo Finance Oy와 자회사 Saldo Bank UAB(리투아니아 인가) | 디지털 은행 | EU 은행 인가, 예금과 대출 고객 | 비공개 | 예(1-10) | [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank) [F-1358](https://www.digitaltoday.co.kr) [LDKR-017](https://www.payward.com/press-release/payward-acquires-saldo-bank) |
| 2026-11-18 | 2027 Q1 예상 | Tribe Capital Management(2018 설립) | 벤처 투자와 자산운용(운용자산 27억 달러) | 운용 조직과 펀드(인가 종류는 빈칸 B03) | 비공개 | 아니오 | [LDKR-019](https://www.payward.com/press-release/payward-to-acquire-tribe-capital) |

- 회사째 산 것이 아니라 목록에서 뺀 것
  - AAVE 토큰 지분 매입(2026-11-05, 계열 펀드와 고객이 토큰을 삼) [LDKR-050](https://www.payward.com/sitemaps/sitemap.xml)
  - Onyx Odds 시리즈 A 주도 투자 [F-1507](https://www.payward.com/press-release/q2-2026-financial-highlights)
  - 독일거래소 그룹의 Payward 구주 매입(2026-04, 방향이 반대인 투자 유치) [F-2026](https://deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-Group-Acquires-a-Stake-in-Kraken-for-200-Million-5077740), Nasdaq Ventures 1억 달러 투자 유치(2026-09) [F-1255](https://www.payward.com/press-release/payward-nasdaq-tokenized-equities)
- 못 산 것: Deribit 다수 지분 협상(2025-02 보도, 2025-05 Coinbase가 인수) 카드 3-8

## 2. 직접 받은 인가 목록 (승인일 순)

| 인가 | 나라 | 법인 | 신청일 | 승인일 | 걸린 기간 | 출처 |
|---|---|---|---|---|---|---|
| 송금업자(MSB) 등록, 주별 송금업 인가 | 미국 연방, 주 | Payward Interactive, Inc.(NMLS 1843762) | 빈칸 B04 | 빈칸 B04 | 빈칸 | [F-0375](https://www.kraken.com/krak) [F-0376](https://www.kraken.com/krak) |
| 송금업자(MSB) 등록 | 캐나다(FINTRAC) | Kraken 캐나다 법인 | 빈칸 | 2019-07 | 빈칸 | [LDKR-033](https://www.financemagnates.com/cryptocurrency/kraken-files-pre-registration-with-canadas-ontario-regulator/) |
| 금융서비스 허가(FSP 190008) | UAE 아부다비(ADGM) | Payward MENA Holdings Limited | 빈칸 | 허가일 2019-12-12, 가상자산 MTF와 수탁 조건 충족 2022-04-25 | 허가일에서 조건 충족까지 약 2년 4개월(계산) | [LDKR-024](https://www.adgm.com/public-registers/fsra/firms/financial-firms/payward-mena-holdings-limited-190008) [LDKR-025](https://www.adgm.com/media/announcements/adgm-welcomes-kraken-global-virtual-asset-exchange-to-its-international-financial-centre) |
| 다자간거래시설(MTF) 운영 인가 | 영국 FCA | Crypto Facilities Ltd(2019 인수 법인) | 빈칸 B05 | 2020-07-06 | 인수에서 약 1년 5개월(계산) | [F-2036](https://www.cryptofacilities.com/cryptocurrency-news/crypto-facilities-becomes-first-licensed-crypto-futures-venue-in-europe) [F-2039](https://www.kraken.com/press/releases/Kraken-MTF-integrates-with-Coppers-growing-ClearLoop-network) |
| 특수목적 예금기관(SPDI) 은행 인가 | 미국 와이오밍주 | Payward Financial, Inc.(Kraken Financial) | 빈칸 B06 | 2020-09-16 | SPDI 법 시행(2019-10-01)에서 약 11개월 반(계산) | [F-1719](https://blog.kraken.com/post/6241/kraken-wyoming-first-digital-asset-bank) [F-1722](https://www.wyoleg.gov/2019/Summaries/HB0074.pdf) |
| 암호자산교환업 등록(関東財務局長 第00022号) | 일본 금융청 | Payward Asia株式会社 | 빈칸 | 2020-09-08 | 2018 철수에서 약 2년 5개월(계산) | [LDKR-031](https://blog.kraken.com/post/6363/launch-in-japan) |
| 가상자산 MLR 등록 | 영국 FCA | Crypto Facilities Ltd | 빈칸 | 2021-11-03 | 빈칸 | [LDKR-045](https://www.kraken.com/press/releases/crypto-facilities-receives-cryptoasset-registration-from-the-uks-fca) |
| 가상자산 MLR 등록 | 영국 FCA | Payward Ltd | 빈칸 | 빈칸 B07 | 빈칸 | [F-0384](https://www.kraken.com/legal/uk/investor-education) [LDKR-039](https://cryptoslate.com/kraken-strengthens-uk-crypto-regulatory-standing-with-fca-electronic-money-license/) |
| VASP 등록 | 아일랜드 중앙은행 | Payward Europe Solutions Limited | 빈칸 | 2023-09-27 이전(정확한 날 빈칸 B08) | 빈칸 | [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/) |
| VASP 등록(OAM) | 이탈리아 | 빈칸 | 빈칸 | 2023-09-27 이전(빈칸 B08) | 빈칸 | [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/) |
| 전자화폐기관(EMI) 인가 | 아일랜드 중앙은행 | Payward 아일랜드 법인 | 빈칸 | 2023-09-27 보도 | 빈칸 | [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/) |
| VASP 등록 | 스페인 중앙은행 | 빈칸 | 빈칸 | 2023-09-27 보도 | 빈칸 | [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/) |
| 사전 등록 약정(PRU) 뒤 제한 딜러 등록 | 캐나다 OSC | Payward Canada Inc.와 Payward, Inc. | PRU 2023-03-30 발표 | 2025-04-02 발표 | 약 2년(계산) | [LDKR-033](https://www.financemagnates.com/cryptocurrency/kraken-files-pre-registration-with-canadas-ontario-regulator/) [LDKR-034](https://blog.kraken.com/news/restricted-dealer-registration-canada) |
| SEC 브로커딜러 등록, FINRA 회원 | 미국 | Kraken Securities LLC(옛 Payward Equities LLC) | 법인 설립 2022-11-02(신청일 빈칸) | 2024-06-10 | 설립에서 약 19개월(계산) | [F-0242](https://api.brokercheck.finra.org/search/firm/324343) [LDKR-036](https://api.brokercheck.finra.org/search/firm/324343) |
| 디지털자산사업 Class F | 버뮤다 BMA | Payward Digital Solutions Ltd(PDSL) | 빈칸 | 2024-08-01 | 빈칸 | [F-1416](https://www.bma.bm/regulated-entities) |
| 디지털자산사업 Class F(수탁) | 버뮤다 BMA | Payward Commercial Treasury | 빈칸 | 2024-11-06 | 빈칸 | [F-1416](https://www.bma.bm/regulated-entities) |
| 전자화폐기관(EMI) 인가 | 영국 FCA | Payward 영국 법인(법인 이름 빈칸 B07) | 빈칸 | 2025-03-11 보도 | 빈칸 | [LDKR-039](https://cryptoslate.com/kraken-strengthens-uk-crypto-regulatory-standing-with-fca-electronic-money-license/) |
| MiCA 가상자산사업자(CASP) 인가 | 아일랜드 중앙은행(EU 30개국 패스포트) | Payward Europe Solutions Limited, Payward Global Solutions Limited(거래 플랫폼 운영) | 빈칸 B09 | 2025-06-25 | 빈칸 | [F-0250](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv) [F-0251](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv) [F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland) |
| 연준 제한목적 마스터 계정 | 미국 연준(캔자스시티) | Payward Financial, Inc. | 빈칸 B10(회사는 5년 넘는 당국 접촉이라고만 밝힘) | 2026-03-04 | 회사 표현 5년 넘게 | [F-1532](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account) [LDKR-016](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account) |
| 국법 신탁회사 인가 신청 | 미국 OCC | Payward National Trust Company(신청) | 2026-05-08 | 심사 중 | 진행 중 | [LDKR-018](https://www.payward.com/press-release/payward-files-application-for-occ-national-trust-company) |
| 가상자산사업자 예비 승인, 최종 시장 승인 | UAE 두바이 VARA | Payward FZCO | 빈칸 | 예비 2026-05-21, 최종 2026-10-12 | 예비에서 최종까지 약 5개월(계산) | [LDKR-027](https://www.payward.com/press-release/payward-vara-authorization-uae) [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch) |
| VASP 등록 | 영국령 버진아일랜드 FSC | Payward 계열(법인 이름 빈칸) | 빈칸 | 2026-06-23 발표 | 빈칸 | [LDKR-030](https://www.payward.com/press-release/payward-bvi-vasp-registrations) |
| 디지털자산 거래 시설, 투자 매매 중개, 수탁 원칙 승인 | 카자흐스탄 AFSA | Payward Kazakhstan | 빈칸 | 원칙 승인 2026-10-22 | 진행 중 | [LDKR-029](https://www.payward.com/press-release/kraken-afsa-in-principle-approval-kazakhstan) |

- 회사 발표 기준 인가와 등록 수: 세계 100건 넘게(2026-10-12) [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch)

## 3. 카드 1. 인수 건

### 1-1. Crypto Facilities(2019-02, 영국 선물 거래장)
1. 한 줄 사건: 2019-02-04 Kraken이 런던의 Crypto Facilities(가상자산 선물 거래장이자 CME 비트코인 기준가 산출 회사)를 샀다고 발표. 9자리 금액(1억 달러 이상), 당시 Kraken 최대 인수 [F-1803](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release) [F-1778](https://blog.kraken.com/product/unlock-futures-trading-with-our-crypto-facilities-acquisition). 발표문이 "acquisition"을 완료형으로 써서 별도 완료일 표기 없음
2. 그 전 상태
   - Kraken에는 선물이 없었고 2015-05부터 현물 거래소 안 신용거래(마진)만 있었음 [F-1778](https://blog.kraken.com/product/unlock-futures-trading-with-our-crypto-facilities-acquisition) (KR-E06)
   - 이미 하던 관계: 2016-05-04 CME 비트코인 기준가의 시세 공급 거래소로 선정, 지수 계산은 Crypto Facilities가 맡음 [F-1758](https://blog.kraken.com/news/kraken-to-provide-pricing-data-for-new-cme-group). 인수 협상은 약 10개월 [F-1778](https://blog.kraken.com/product/unlock-futures-trading-with-our-crypto-facilities-acquisition)
3. 직접 받는 길: Kraken이 영국 FCA 인가를 직접 신청한 기록은 빈칸 B11. 제도: FCA는 2018-04-06 가상자산 선물은 MiFID II 금융상품이 될 수 있어 매매와 주선에 FCA 인가가 필요하다고 밝힘 [F-2034](https://www.fca.org.uk/news/statements/cryptocurrency-derivatives)
4. 대상 회사: 2015 설립, 런던, FCA 인가(FRN 757895). 비트코인, 이더리움, XRP, 라이트코인, 비트코인캐시 선물을 처음 낸 규제 법인(회사 주장) [F-1779](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release). 매출 2018 100만 파운드 남짓, 2019 630만 파운드 [F-2317](https://find-and-update.company-information.service.gov.uk/company/09172128/filing-history). 손님 수는 빈칸
5. 판 쪽: 창업자 겸 CEO가 이끈 회사. 주주 구성과 판 이유는 빈칸 B12. 창업자 발언은 10번
6. 승인: FCA 지배주주 변경 승인일 빈칸 B12
7. 대금: 9자리 금액, 현금과 주식 비율 비공개 [F-1803](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release). 같은 해 2019-06 Kraken은 개인 2,263명에게서 1,350만 달러를 모았고 쓰임을 인수라고 밝힘 [F-2022](https://siliconangle.com/2019/06/25/cryptocurrency-exchange-kraken-raises-13-5m-bnktothefuture-campaign/)
8. 같은 시기 바깥
   - 2018 하락장. 2018-11 CEO는 투자를 받는다면 시장이 내려간 때 회사를 사는 데 쓰겠다고 말함 [F-1826](https://sia.hackernoon.com/jesse-powell-is-building-a-culture-of-crypto-values-at-kraken-9d4983227c9f)
   - 경쟁사: 2018-06 Coinbase가 증권사 Keystone 등 3곳 인수 발표 [F-2115](https://altswire.com/crypto-exchange-coinbase-buys-broker-dealers-move-offer-regulated-securities/), 2018-07 SEC와 FINRA 승인 [F-2116](https://www.wealthmanagement.com/financial-technology/coinbase-says-it-has-green-light-to-list-coins-deemed-securities)
9. 산 뒤
   - 2019-02 Kraken 적격 고객이 처음 선물 거래(최대 50배, 미국 거주자 제외) [F-1778](https://blog.kraken.com/product/unlock-futures-trading-with-our-crypto-facilities-acquisition)
   - 2020-07-06 FCA 다자간거래시설(MTF) 인가, 회사 자료끼리 2019와 2020이 엇갈림 [F-2036](https://www.cryptofacilities.com/cryptocurrency-news/crypto-facilities-becomes-first-licensed-crypto-futures-venue-in-europe) [F-2039](https://www.kraken.com/press/releases/Kraken-MTF-integrates-with-Coppers-growing-ClearLoop-network)
   - 2021-11-03 FCA 가상자산 MLR 등록 [LDKR-045](https://www.kraken.com/press/releases/crypto-facilities-receives-cryptoasset-registration-from-the-uks-fca)
   - 2021 매출 1,395만 파운드, 거래량 1,910억 달러. 2022 매출 362만 파운드 [F-2318](https://find-and-update.company-information.service.gov.uk/company/09172128/filing-history)
   - 2023~2025 자기 매출은 줄고 그룹 이전가격 수입이 2025년 2,588만 파운드로 늚. 고객 계약은 그룹 다른 회사가 맺음 [F-2319](https://find-and-update.company-information.service.gov.uk/company/09172128/filing-history)
   - 2026 Kraken MTF는 기관용 가상자산 선물 250종 넘게 [F-2038](https://mtf.kraken.com)
10. 발언: Kraken CEO, Crypto Facilities 창업자 [LDKR-044](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release). "왜 직접 만들지 않고 샀나"에 대한 회사 문장은 빈칸 B11 (kraken_quotes.md 1-1)

### 1-2. Bit Trade(2020-01, 호주)와 Beaufort Fiduciaries(호주 금융서비스 인가)
1. 한 줄 사건: 2020-01-14 호주에서 가장 오래된 가상자산 서비스 Bit Trade(2013 설립)를 샀다고 발표, 금액 비공개 [F-1806](https://blog.kraken.com/news/kraken-acquires-australias-longest-running-crypto-service-provider-bit-trade). 시점 미상(2025-02-28 이전) 호주 금융서비스 인가(AFSL 545124)를 가진 Beaufort Fiduciaries를 삼 [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf)
2. 그 전 상태: 호주 현지 영업 법인 여부 빈칸 B14. 한 달 전 2019-12-17 Circle의 장외 데스크를 사 아시아 거래 상대를 얻음 [F-1805](https://blog.kraken.com/news/kraken-otc-acquires-circle-trade)
3. 직접 받는 길: AUSTRAC 등록이나 AFSL을 Kraken 이름으로 직접 신청한 기록 빈칸 B14. Kraken은 2025-02 ASIC 의견서에서 가상자산 회사가 AFSL을 신청하거나 사는 흐름이 있다고 적음 [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf)
4. 대상 회사: Bit Trade 2013 설립, 대표가 Kraken 호주 대표가 됨 [F-1806](https://blog.kraken.com/news/kraken-acquires-australias-longest-running-crypto-service-provider-bit-trade). Beaufort는 도매 고객 대상 AFSL 보유 [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf). 손님 규모 빈칸
5. 판 쪽: Bit Trade와 Beaufort의 전 주인과 판 이유 빈칸 B14
6. 승인: 빈칸
7. 대금: 둘 다 비공개
8. 같은 시기 바깥: 2019-07 Interchange, 2019-12 Circle Trade 인수로 기관과 장외 쪽 인력이 늚 [F-1804](https://blog.kraken.com/news/interchange-founders-on-kraken-acquisition) [F-1805](https://blog.kraken.com/news/kraken-otc-acquires-circle-trade)
9. 산 뒤
   - 호주 고객은 BitTrade Pty Limited가 맡음 [F-0459](https://www.kraken.com/legal/price-predictor-terms). Kraken은 AUSTRAC에 디지털화폐 거래소로 등록 [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf)
   - 2024-07-18 기관 수탁을 호주 기관으로 넓힘 [F-2063](https://www.kraken.com/press/releases/Kraken-Institutional-Expands-Custody-Solution-to-UK-and-Australia)
   - Beaufort로 도매 고객에게 상품을 넓힘(Bit Trade는 그 인가의 대리인) [LDKR-040](https://download.asic.gov.au/media/h5mfmwo3/kraken.pdf)
   - 2024 호주 ASIC 소송, 벌금 800만 호주달러(위키백과 정리, 단일 출처) [F-1343](https://en.wikipedia.org/wiki/Kraken_(cryptocurrency_exchange))
10. 발언: 호주 달러 유동성과 거래 경험에서 가장 좋은 서비스를 목표로 함(회사 발표) [F-1806](https://blog.kraken.com/news/kraken-acquires-australias-longest-running-crypto-service-provider-bit-trade)

### 1-3. BCM(2023-10 발표, 2024-09 완료, 네덜란드 중개사)
1. 한 줄 사건: 2023-10-05 네덜란드 등록 가상자산 중개사 Coin Meester B.V.(BCM, 2017 설립) 인수 계획 발표, 2024-09-24 완료, 금액 비공개 [F-1807](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business) [F-1808](https://blog.kraken.com/news/kraken-bcm)
2. 그 전 상태
   - 2023-10 기준 VASP 등록은 아일랜드, 이탈리아, 스페인이고 다른 나라 등록을 추진 중 [LDKR-042](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business)
   - 2023-09-27 아일랜드 전자화폐기관(EMI) 인가와 스페인 VASP 등록 [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/)
3. 직접 받는 길: 네덜란드 중앙은행(DNB) 등록을 직접 신청한 기록 빈칸 B15
4. 대상 회사: 네덜란드의 오래된 등록 중개사(회사 주장), 프랑스와 폴란드 VASP 등록 보유 [F-1808](https://blog.kraken.com/news/kraken-bcm). 고객 수와 거래량 빈칸 B15
5. 판 쪽: 공동 창업자 겸 CEO가 Kraken을 사업을 맡을 곳으로 들며 넘김 [LDKR-042](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business). 다른 주주와 판 이유 빈칸
6. 승인: 규제 승인 조건, 발표에서 완료까지 355일(계산) [F-1807](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business) [F-1808](https://blog.kraken.com/news/kraken-bcm). 승인 당국 이름 빈칸
7. 대금: 비공개
8. 같은 시기 바깥
   - 회사는 EU가 MiCA 체계를 세운 것을 유럽 성장 계획을 앞당긴 이유로 듦 [F-1807](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business)
   - MiCA 가상자산사업자 조항 적용 2024-12-30, 경과기간 최대 2026-07-01 [F-1440](https://www.fsma.be/en/news/crypto-assets-service-providers-end-transitional-period). 회원국 경과기간: 네덜란드 6개월, 폴란드 6개월, 프랑스 18개월, 아일랜드 12개월 [LDKR-037](https://www.esma.europa.eu/sites/default/files/2024-12/List_of_MiCA_grandfathering_periods_art._143_3.pdf)
   - 경쟁사 MiCA: Robinhood 리투아니아 2025-05-29, Coinbase 룩셈부르크 2025-06-20 [F-1414](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)
9. 산 뒤
   - 완료 때 독일(제휴), 스페인, 이탈리아, 네덜란드, 벨기에, 아일랜드, 프랑스, 폴란드 8개국에서 VASP 영업 가능 [LDKR-043](https://blog.kraken.com/news/kraken-bcm)
   - 2025-06-25 아일랜드 MiCA 인가로 나라별 등록을 하나로 바꿈 [F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland) [F-1438](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
   - (판단) 네덜란드 경과기간 끝(2024-12-30에서 6개월, 계산상 2025-06-30) 닷새 전에 MiCA 인가를 받음. 근거 [LDKR-037](https://www.esma.europa.eu/sites/default/files/2024-12/List_of_MiCA_grandfathering_periods_art._143_3.pdf) [F-0250](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)
10. 발언: Kraken CEO, BCM CEO, Kraken 유럽 총괄 [LDKR-042](https://blog.kraken.com/news/kraken-to-acquire-dutch-crypto-broker-bcm-in-commitment-to-grow-european-business) [LDKR-043](https://blog.kraken.com/news/kraken-bcm)

### 1-4. 키프로스 투자회사(2025-02, EU MiFID 인가)
1. 한 줄 사건: 2025-02-03 CySEC 승인을 받은 키프로스 투자회사를 사서 EU MiFID 인가를 얻었다고 발표 [F-1809](https://blog.kraken.com/news/eu-mifid-license). 대상은 CFD 회사 Greenfields Wealth(옛 Pacific Union Group)라고 Finance Magnates가 보도 [F-1812](https://www.financemagnates.com/forex/exclusive-krakens-cyprus-move-pu-prime-linked-cfds-firm-revealed-as-acquisition-target/). 금액과 완료일 비공개
2. 그 전 상태: EU 고객 대상 규제 파생 판매 법인이 있었는지 빈칸 B16. 파생 거래장은 영국 법인(Crypto Facilities, 기관용 MTF)과 버뮤다 법인(2024-10, 미국과 EU 밖) [F-2036](https://www.cryptofacilities.com/cryptocurrency-news/crypto-facilities-becomes-first-licensed-crypto-futures-venue-in-europe) [F-1368](https://www.businesswire.com/news/home/20241003985524/en/Kraken-Launches-Regulated-Derivatives-Venue-in-Bermuda) [F-1369](https://support.kraken.com/articles/where-is-kraken-licensed-or-regulated)
3. 직접 받는 길: MiFID 인가를 직접 신청한 기록 빈칸 B16
4. 대상 회사: 인가번호 342/17, 인가일 2017-11-13, 옛 이름 Pacific Union Group Ltd와 BrightFX Capital Ltd. 투자 서비스는 주문 접수 전달, 주문 집행, 자기매매 [F-1810](https://www.cysec.gov.cy/en-GB/entities/investment-firms/cypriot/45914/). 법적 이름 변경 기록 2023-12-18, 2025-01-24 [F-1811](https://api.gleif.org/api/v1/lei-records/2138006O8D7SV36PWU16)
5. 판 쪽: 키프로스 밖에서 PU Prime 브랜드와 엮인 CFD 회사(보도, Finance Magnates) [F-1812](https://www.financemagnates.com/forex/exclusive-krakens-cyprus-move-pu-prime-linked-cfds-firm-revealed-as-acquisition-target/). 판 이유 빈칸 B16
6. 승인: CySEC 승인(승인일 미표기) [F-1809](https://blog.kraken.com/news/eu-mifid-license). (계산) LEI 이름 변경 2025-01-24가 발표 열흘 전 [F-1811](https://api.gleif.org/api/v1/lei-records/2138006O8D7SV36PWU16)
7. 대금: 비공개
8. 같은 시기 바깥
   - MiCA 조항 적용 2024-12-30 [F-1440](https://www.fsma.be/en/news/crypto-assets-service-providers-end-transitional-period), 키프로스 MiCA 경과기간 18개월 [LDKR-037](https://www.esma.europa.eu/sites/default/files/2024-12/List_of_MiCA_grandfathering_periods_art._143_3.pdf). MiFID는 MiCA와 다른 금융상품 인가(KR-E18)
   - 같은 달 2025-02 Deribit 인수 협상 보도 [LDKR-041](https://blockhead.co/2025/02/21/coinbase-kraken-in-talks-to-acquire-deribit-as-crypto-derivatives-market-heats-up-2), 다음 달 2025-03-20 NinjaTrader 발표 [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)
9. 산 뒤
   - 2025-05-20 EEA 적격 고객에게 무기한과 만기 가상자산 파생 [F-1813](https://blog.kraken.com/news/euro-reg-futures) [F-1529](https://blog.kraken.com/news/euro-reg-futures)
   - 2025-09-10 EU 고객 xStocks 판매, 판매 법인이 이 회사 [F-1528](https://blog.kraken.com/product/xstocks/now-available-to-eu-clients)
   - CySEC 승인 도메인에 eu.kraken.com, ninjatrader.com/eu [F-1810](https://www.cysec.gov.cy/en-GB/entities/investment-firms/cypriot/45914/)
10. 발언: Kraken 공동 총괄 [LDKR-046](https://blog.kraken.com/news/eu-mifid-license)

### 1-5. NinjaTrader(2025-03 발표, 2025-05 완료, 미국 선물 중개사)
1. 한 줄 사건: 2025-03-20 계약 발표, 2025-05-01 완료. 미국 개인 선물 거래 앱과 CFTC 등록 선물 중개사(FCM)를 가진 회사를 15억 달러(가격 조정 조항)에 삼 [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader) [F-0177](https://www.financemagnates.com/cryptocurrency/kraken-completes-15b-ninjatrader-acquisition-as-funded-accounts-jump-26-in-q1/) [F-2031](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader)
2. 그 전 상태
   - 미국 개인에게 레버리지를 팔 인가 없음: 2021-09-28 CFTC가 FCM 등록 없이 미국 개인 신용거래를 했다며 125만 달러 제재 [F-1781](https://mondovisione.com/media-and-resources/news/cftc-imposes-a-125-million-penalty-against-kraken-for-offering-illegal-off-exc-2021928/) [F-1782](https://mondovisione.com/media-and-resources/news/cftc-imposes-a-125-million-penalty-against-kraken-for-offering-illegal-off-exc-2021928/). 2021-06-23부터 ECP가 아닌 미국 고객 새 마진 차단 [F-1848](https://decrypt.co/73233/crypto-exchange-kraken-disables-margin-trading-some-u-s-residents)
   - 선물은 미국 밖에서만: 영국 법인과 2024-10 버뮤다 거래장 [F-1368](https://www.businesswire.com/news/home/20241003985524/en/Kraken-Launches-Regulated-Derivatives-Venue-in-Bermuda)
   - 인수 전 Kraken과 NinjaTrader의 제휴 기록 빈칸 B17. NinjaTrader는 2022-06 Coinbase 첫 선물의 외부 판매 중개사였음 [F-2112](https://www.financemagnates.com/cryptocurrency/trading/coinbase-to-target-retail-traders-with-first-bitcoin-derivatives/)
3. 직접 받는 길
   - Kraken이 FCM을 직접 신청한 기록 빈칸 B17
   - 공동 CEO: 미국 선물 중개를 처음부터 만들면 기술과 규제 승인에 비용과 시간이 많이 듦(코인데스크 한국어판 인터뷰) [F-1346](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange) [F-1365](https://www.coindesk.com/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)
   - 비교: Coinbase는 FCM을 2021-09-15 직접 신청해 2023-08-15 등록(약 23개월, 계산) [F-1228](https://www.nfa.futures.org/BasicNet/#0542717). Robinhood는 옛 Marex North America(FCM, 2010 등록)를 넘겨받음 [F-1236](https://www.nfa.futures.org/BasicNet/#0424278)
4. 대상 회사
   - 2003 설립, 시카고, 트레이더 약 200만 명 [F-1117](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader). 2020-01 기준 활성 트레이더 50만 명 넘음 [LDKR-002](https://ninjatrader.com/News/NinjaTrader-Announces-Majority-Growth-Investment-led-by-Long-Ridge-Equity-Partners)
   - FCM의 출처: 2021-01-13 비청산 FCM TransAct Futures와 소개 중개사 Infinity Futures를 사서 얻음 [LDKR-003](https://ninjatrader.com/News/NinjaTrader-Acquires-TransAct-Futures). 2022-01-12 Tradovate를 1.15억 달러에 삼 [LDKR-004](https://www.ninjatrader.com/news/ninjatrader-acquires-tradovate/)
   - FCM(NFA ID 0309379), 선물은 청산 회원 FCM 두 곳의 합산 계좌로 청산, 고객은 주로 개인 단타 트레이더 [LDKR-005](https://ninjatrader.com/getmedia/e75aec7b-7efc-488b-954a-b81c9dac7d9b/NinjaTrader-Clearing-LLC-Disclosure-Document-2026-05-06.pdf)
   - 매출과 이익 빈칸 B18
5. 판 쪽
   - 다수 지분은 사모펀드 Long Ridge Equity Partners. 2020-01-06 Long Ridge 주도, DRW Venture Capital 참여로 다수 지분 투자 [LDKR-001](https://ninjatrader.com/News/Kraken-to-Acquire-NinjaTrader-Introducing-the-Next-Era-of-Professional-Trading) [LDKR-002](https://ninjatrader.com/News/NinjaTrader-Announces-Majority-Growth-Investment-led-by-Long-Ridge-Equity-Partners). (계산) 보유 약 5년 2개월 뒤 매각
   - Long Ridge의 판 이유 문장 빈칸 B19. NinjaTrader CEO는 Kraken과 합쳐 세계 규모로 키운다고 말함 [LDKR-006](https://ninjatrader.com/News/Kraken-to-Acquire-NinjaTrader-Introducing-the-Next-Era-of-Professional-Trading)
   - 같은 DRW Venture Capital이 2025-11 Payward 8억 달러 유치 1차 회차 주도사 가운데 하나 [F-2025](https://blog.kraken.com/news/800-million-raise-to-advance-strategic-roadmap)
6. 승인: 발표에서 완료까지 42일(계산). FCM 지배권 변경 당국 절차 빈칸 B17
7. 대금: 15억 달러, 현금과 주식 비율 비공개(제3자 자문사도 비공개로 적음) [F-2031](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader). NinjaTrader 매출 대비 배수 빈칸 B18. 직전 Kraken 가치 108억 달러(2022-02, 제3자 기재) [F-2023](https://architectpartners.com/wp-content/uploads/2025/03/Kraken-_-NinjaTrader-MA-Alert.pdf)
8. 같은 시기 바깥
   - 2025-03-03 SEC 실무진이 Kraken 소송 재소 불가 취하에 원칙 합의 [F-1790](https://blog.kraken.com/news/sec-lawsuit-dismissal), 2025-03-27 공식 취하 [F-1791](https://decrypt.co/312072/sec-drops-cases-kraken-consensys-cumberland-drw)
   - Wall Street Journal 선보도 뒤 2025-03-20 발표, 원칙 합의에서 17일(계산). 회사는 두 일을 잇는 말을 하지 않음 [LDKR-007](https://cointelegraph.com/news/kraken-reportedly-nears-billion-dollar-deal-allowing-futures-trading-us-report)
   - 같은 달 Kraken이 상장 계획을 확인했다고 Decrypt가 보도 [LDKR-007](https://cointelegraph.com/news/kraken-reportedly-nears-billion-dollar-deal-allowing-futures-trading-us-report). 2025-02 Deribit 협상 보도 [LDKR-041](https://blockhead.co/2025/02/21/coinbase-kraken-in-talks-to-acquire-deribit-as-crypto-derivatives-market-heats-up-2)
   - 경쟁사: 2024-03 Robinhood Marex FCM 인수(위키 정리) [F-1567](https://en.wikipedia.org/wiki/Robinhood_Markets), 2025-05-08 Coinbase Deribit 인수 발표 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform)
9. 산 뒤
   - 2025-07 미국 고객에게 CME 상장 가상자산 선물(법인 이름 Kraken Derivatives US) [F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders)
   - 2025 선물 하루 평균 수익 거래 수 119% 증가(NinjaTrader 편입 포함) [F-2322](https://www.payward.com/press-release/2025-financial-highlights)
   - 2026-05-06 미국 개인 CFTC 규제 현물 마진, 고객은 NinjaTrader 계약에 서명 [F-1850](https://blog.kraken.com/product/margin/cftc-regulated-spot) [F-1851](https://support.kraken.com/articles/getting-started-us-margin)
   - NinjaTrader Clearing이 Kalshi Klear 직접 청산 회원(이벤트 계약), Bitnomial 규칙으로 신용 현물 처리 [LDKR-005](https://ninjatrader.com/getmedia/e75aec7b-7efc-488b-954a-b81c9dac7d9b/NinjaTrader-Clearing-LLC-Disclosure-Document-2026-05-06.pdf)
   - 외부 선물 소개 중개사가 Payward Services Derivatives(옛 NinjaTrader Connect)로 청산 [LDKR-008](https://www.financemagnates.com/forex/exclusive-metrotrade-rebuilds-with-kraken-owner-payward-adds-crypto-contracts/)
   - Kraken 인가로 NinjaTrader의 영국, 유럽, 호주 진출을 이익 항목으로 듦 [LDKR-049](https://ninjatrader.com/News/Kraken-to-Acquire-NinjaTrader-Introducing-the-Next-Era-of-Professional-Trading). CySEC 승인 도메인 ninjatrader.com/eu [F-1810](https://www.cysec.gov.cy/en-GB/entities/investment-firms/cypriot/45914/)
10. 발언: Kraken 공동 CEO(2025-03-20, 2026-09), NinjaTrader CEO [F-1042](https://blog.kraken.com/news/kraken-to-acquire-ninjatrader) [LDKR-006](https://ninjatrader.com/News/Kraken-to-Acquire-NinjaTrader-Introducing-the-Next-Era-of-Professional-Trading) [F-1346](https://www.coindesk.com/ko/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange)

### 1-6. Small Exchange(2025-10, 미국 선물 거래소 DCM)
1. 한 줄 사건: 2025-10-16 영국 IG Group에서 시카고의 CFTC 지정 선물 거래소 Small Exchange를 1억 달러에 샀다고 발표, 같은 날 완료 [F-1116](https://blog.kraken.com/news/acquires-small-exchange) [F-2028](https://financialreports.eu/filings/8026393/content)
2. 그 전 상태: 미국 고객 선물은 NinjaTrader FCM으로 CME 상장 계약을 파는 단계 [F-1439](https://blog.kraken.com/product/kraken-derivatives-us/first-cftc-regulated-perpetual-futures-for-us-traders). 자기 거래소는 없음
3. 직접 받는 길: Kraken이 DCM을 직접 신청한 기록 빈칸 B20. 제도상 심사 기준 180일이지만 서류 보완으로 멈출 수 있음 [F-2051](https://www.ecfr.gov/current/title-17/chapter-I/part-38/section-38.3). Small Exchange 자신은 2019-03 이전 신청, 2020-03-10 지정(최소 약 1년) [F-2049](https://www.eventus.com/cat-press-and-news/the-small-exchange-to-deploy-eventus-systems-technology-for-real-time-market-surveillance/) [F-2050](https://mondovisione.com/news/cftc-designates-small-exchange-inc-as-a-contract-market-2020310). Bitnomial 거래소는 첫 제출에서 약 3년 7개월 [F-2048](https://bitnomial.com/exchange/regulatory/cftc/orders/bitnomial-exchange-cftc-order.pdf)
4. 대상 회사: 2019 출범, 2020-03-10 DCM 지정 [F-2050](https://mondovisione.com/news/cftc-designates-small-exchange-inc-as-a-contract-market-2020310) [LDKR-009](https://fxnewsgroup.com/forex-news/retail-forex/ig-group-acquires-the-small-exchange-from-foris-dax-markets/). 손님 수와 거래량 빈칸 B13
5. 판 쪽
   - 전 주인 이력: IG가 지분 39%를 갖다가 2021-12 매각 합의, 2022-03 Crypto.com 모회사 Foris DAX Markets에 넘김 [LDKR-010](https://www.financemagnates.com/forex/ig-group-acquires-small-exchange-from-cryptocoms-parent/). 2023-04-03 IG가 Foris DAX에서 다시 삼(금액 비공개) [LDKR-009](https://fxnewsgroup.com/forex-news/retail-forex/ig-group-acquires-the-small-exchange-from-foris-dax-markets/)
   - IG가 판 이유: CEO가 Small Exchange 인수에 대한 상당한 수익이고 Kraken과 새 가상자산 상품 유통을 함께 하게 된다고 말함. 같은 공시에서 IG는 호주 거래소 Independent Reserve 인수, 영국 FCA 가상자산 등록, zerohash 지분을 다른 가상자산 행보로 듦 [LDKR-011](https://financialreports.eu/filings/8026393/content)
6. 승인: 발표와 완료 같은 날 [F-2028](https://financialreports.eu/filings/8026393/content). CFTC 쪽 절차 문서 빈칸 B20
7. 대금
   - 1억 달러 = 현금 3,250만 달러 + Payward 주식 6,750만 달러(67.5%) [F-2028](https://financialreports.eu/filings/8026393/content)
   - IG 세후 이익 7,330만 파운드, 주식 대가는 IG 규제 자본에서 뺌 [F-2028](https://financialreports.eu/filings/8026393/content)
   - 같은 시기 Payward 가치: 2025-09 150억 달러(보도) [F-2024](https://www.financemagnates.com/cryptocurrency/kraken-secures-500m-at-15b-valuation-is-an-ipo-imminent-now/), 2025-11 200억 달러 [F-1187](https://payward.com/press-release/kraken-raises-800m)
8. 같은 시기 바깥
   - 2025-11-18 8억 달러 유치, 2025-11-19 상장 서류 비공개 제출 [F-2025](https://blog.kraken.com/news/800-million-raise-to-advance-strategic-roadmap) [F-1188](https://blog.kraken.com/news/draft-registration-statement-initial-public-offering)
   - 경쟁사: Coinbase DCM은 FairX 인수로(지정 2020-11-23) [F-1122](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations). Robinhood는 2025-11-25 Susquehanna 합작 발표, 2026-01-20 MIAXdx(DCM, DCO) 인수 완료 [F-1157](https://robinhood.com/newsroom/robinhood-prediction-markets-joint-venture/)
9. 산 뒤
   - IG와 새 거래소 상품 유통 제휴 [F-2028](https://financialreports.eu/filings/8026393/content)
   - Small Exchange에 실제로 상장한 상품과 거래량 빈칸 B13. 7개월 뒤 2026-04 Bitnomial을 사고 첫 미국 무기한선물은 Bitnomial 시장으로 냄 [F-1638](https://www.payward.com/press-release/q2-2026-financial-highlights)
10. 발언: Kraken 공동 CEO, IG CEO [LDKR-012](https://blog.kraken.com/news/acquires-small-exchange) [LDKR-011](https://financialreports.eu/filings/8026393/content)

### 1-7. Backed(2025-12, 주식 토큰 발행사)
1. 한 줄 사건: 2025-12-02 xStocks를 발행하는 스위스 Backed Finance AG 인수 합의 발표, 2026-01-05경 Payward Europe Limited가 지분 100% 매입, 금액 비공개 [F-0139](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion) F-0939(로컬 저장 문서)
2. 그 전 상태
   - 2025-06-30부터 Backed 발행 xStocks를 Kraken 앱이 미국 밖 적격 고객에게 팜(제휴) [F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)
   - 버뮤다 법인 PDSL이 2025-04-28 발행사와 지정참가자(AP) 계약 F-0919(로컬 저장 문서)
3. 직접 받는 길: 발행사를 직접 세우는 길을 검토했는지 빈칸 B21. 발행사는 금융감독 인가 대상이 아님(투자설명서) F-0940(로컬 저장 문서)
4. 대상 회사: 2021 설립 [LDKR-022](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion). 2026-01-16 xStocks 발행 잔액 1.937억 달러(rwa.xyz 집계, 보도) [F-1030](https://cryptoslate.com/tokenized-equities-approach-1b-as-institutional-rails-emerge/). 매출 빈칸
5. 판 쪽: 발표문은 인수로 Backed가 더 빨리 크는 데 필요한 자본과 자원을 얻는다고 적고, 공동 창업자는 Kraken 규모로 계획을 앞당긴다고 말함 [LDKR-022](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion). 다른 주주와 지분 빈칸
6. 승인: 발표에서 지분 매입까지 약 34일(계산) F-0939(로컬 저장 문서). 2026-01-06 지식재산을 Payward에 양도 F-0923(로컬 저장 문서)
7. 대금: 비공개. 지식재산 최초 대가 USDC 1,682.3만 개(투자설명서) F-0923(로컬 저장 문서)
8. 같은 시기 바깥: 2025-12 독일거래소 그룹 제휴 [F-0175](https://www.payward.com/press-release/xstocks-dax-40), 2025-12-17 Alpaca가 기초 주식 우선 거래처 [F-1524](https://www.payward.com/press-release/xstocks-momentum-with-alpaca-and-kraken-partnership)
9. 산 뒤
   - 2026-11-16 발행 잔액 6.77억 달러(같은 집계 기준) [F-1030](https://cryptoslate.com/tokenized-equities-approach-1b-as-institutional-rails-emerge/)
   - 2026-11-11 회사 발표 xStocks 자산 11억 달러 넘음, 1,500종 넘음(집계 기준 다름) [F-0167](https://www.payward.com/press-release/xstocks-uk-eu-equities)
   - Payward가 발행사 지출을 부담하는 토큰화 서비스 계약(2026-01-05) F-0921(로컬 저장 문서)
10. 발언: Kraken 공동 CEO, Backed 공동 창업자 [F-1043](https://blog.kraken.com/news/backed-acquisition) [LDKR-022](https://www.payward.com/press-release/kraken-acquires-backed-xstocks-expansion)

### 1-8. Bitnomial(2026-04 발표, 2026-05 완료, 거래소, 청산소, 중개사 묶음)
1. 한 줄 사건: 2026-04-17 계약 발표, 2026-05-01 완료. 선물 거래소(DCM), 청산소(DCO), 선물 중개사(FCM)를 모두 가진 Bitnomial 지분 100%를 최대 5.5억 달러(현금과 주식)에 삼 [F-2029](https://www.payward.com/press-release/payward-to-acquire-bitnomial) [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
2. 그 전 상태: FCM(NinjaTrader, 2025-05)과 DCM(Small Exchange, 2025-10)은 있었으나 청산소는 없었음. 완료 발표가 이번에 미국 파생 세 인가를 다 갖게 됐다고 적음 [F-1118](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)
3. 직접 받는 길
   - Kraken이 DCO를 직접 신청한 기록 빈칸 B22
   - Bitnomial 청산소: 2022-04 신청, 2023-12-15 등록(약 20개월). 거래소, 청산소, 중개사를 한 그룹이 갖는 구조에 CFTC 의견 요청이 있었음 [F-2044](https://mondovisione.com/media-and-resources/news/opening-statement-of-cftc-chairman-rostin-behnam-for-the-december-13th-commissio-20231213/) [F-2045](https://bitnomial.com/exchange/regulatory/cftc/orders/bitnomial-clearinghouse-cftc-order.pdf)
   - 비교: Coinbase 쪽 The Clearing Company 2025-11 DCO 신청 [F-1626](https://www.marketsmedia.com/the-clearing-company-files-to-become-dco/), Coinbase Clearing 2026-09 승인 [F-1623](https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/)
4. 대상 회사: DCM 2020-04-17 지정(첫 제출 2016-09-30) [F-2048](https://bitnomial.com/exchange/regulatory/cftc/orders/bitnomial-exchange-cftc-order.pdf), DCO 2023-12-15 [F-2045](https://bitnomial.com/exchange/regulatory/cftc/orders/bitnomial-clearinghouse-cftc-order.pdf), 자체 청산 가동 2025-01-30, 그 전 청산은 MIAX Futures에 맡김(판단) [F-2047](https://www.marketsmedia.com/bitnomial-to-launch-cftc-regulated-digital-asset-derivatives-ccp/). 손님 수와 매출 빈칸 B23
5. 판 쪽: 창업자 겸 CEO는 Payward에 들어가면 그 미래를 맞는 규모로 만들 수 있다고 말함 [LDKR-013](https://www.payward.com/press-release/payward-to-acquire-bitnomial). 다른 주주와 판 이유 빈칸 B23
6. 승인: 발표에서 완료까지 14일(계산). 회사는 CFTC 통지를 낸다고 적음 [F-2029](https://www.payward.com/press-release/payward-to-acquire-bitnomial)
7. 대금: 최대 5.5억 달러, 현금과 주식 비율과 "최대" 조건 비공개, Payward 주식가치 200억 달러 기준 [F-2029](https://www.payward.com/press-release/payward-to-acquire-bitnomial)
8. 같은 시기 바깥
   - 2026-03 상장 준비 중단 보도 [F-0183](https://news.bitcoin.com/kraken-co-ceo-arjun-sethi-confirms-confidential-ipo-filing-at-semafor-world-economy-summit/), 2026-04-14 독일거래소 구주 매입(계산상 가치 약 133억 달러) [F-2026](https://deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-Group-Acquires-a-Stake-in-Kraken-for-200-Million-5077740)
   - 2026-05-07 Reap 발표 [F-2030](https://www.payward.com/press-release/payward-acquires-reap), 2026-05-08 OCC 신탁 신청 [LDKR-018](https://www.payward.com/press-release/payward-files-application-for-occ-national-trust-company)
   - 경쟁사: Robinhood 2026-01-20 MIAXdx 인수 완료 [F-1157](https://robinhood.com/newsroom/robinhood-prediction-markets-joint-venture/)
9. 산 뒤
   - 2026 Q2 미국 첫 CFTC 규제 무기한선물(Bitnomial 인프라, 회사 주장) [F-1638](https://www.payward.com/press-release/q2-2026-financial-highlights)
   - 2026-09-16 Hyperliquid 위 미국 고객용 무기한선물 신청, 2026-09-18 개별 주식 무기한선물 10종 신청 [F-1190](https://www.payward.com/press-release/payward-hyperliquid-onchain-perpetual-futures) [F-1189](https://www.payward.com/press-release/payward-single-stock-perpetual-futures-filing)
   - 2026 Q3 파생 계약 6,600만 건(전년 대비 84% 증가) [F-1503](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)
10. 발언: Kraken 공동 CEO(발표, 완료), Bitnomial 창업자 [LDKR-013](https://www.payward.com/press-release/payward-to-acquire-bitnomial) [LDKR-014](https://www.payward.com/press-release/payward-completes-acquisition-of-bitnomial-the-first-fully-cftc-licensed-crypto-native-derivatives-stack-in-the-us)

### 1-9. Reap(2026-05 발표, 2026-07 완료, 스테이블코인 카드와 결제)
1. 한 줄 사건: 2026-05-07 계약 발표, 2026-07-01 완료. 스테이블코인 기반 카드 발급, 국경 간 송금, 재무관리 회사 Reap을 최대 6억 달러(현금과 Payward 주식)에 삼 [F-2030](https://www.payward.com/press-release/payward-acquires-reap) [F-1195](https://www.payward.com/press-release/payward-reap-close)
2. 그 전 상태: 2026-03-11 기업용 사업 Payward Services 출시 [F-1511](https://www.payward.com/press-release/introducing-payward-services). 미국 Krak 카드는 Lead Bank가 Visa 라이선스로 발행 [F-0435](https://www.kraken.com/krak)
3. 직접 받는 길: 카드 발급과 송금 인가를 직접 받는 길 검토 여부 빈칸 B24
4. 대상 회사: 2025 매출과 거래량이 거의 세 배, 인가를 아시아에서 남미로 넓힘(회사 주장) [LDKR-023](https://www.payward.com/press-release/payward-acquires-reap). 매출 금액 빈칸 B24
5. 판 쪽: 공동 창업자 겸 CEO는 Payward 합류를 자연스러운 다음 걸음이라고 말함 [LDKR-023](https://www.payward.com/press-release/payward-acquires-reap). 주주 빈칸 B24
6. 승인: 발표에서 완료까지 55일(계산)
7. 대금: 최대 6억 달러, 비율 비공개, Payward 주식가치 200억 달러 기준 [F-2030](https://www.payward.com/press-release/payward-acquires-reap). 2026-05 매체는 Payward가 200억 달러 가치로 새 투자를 받는 중이라고 보도 [F-2032](https://unchainedcrypto.com/kraken-parent-payward-seeks-fresh-funding-at-20-billion-valuation-ahead-of-planned-ipo/)
8. 같은 시기 바깥: 2026-07-27 Magic Labs 지갑 사업 인수 합의 [F-1514](https://www.payward.com/press-release/payward-to-acquire-magic-labs-wallet-infrastructure)
9. 산 뒤: Reap 브랜드와 경영진 유지, Reap 인가로 아시아태평양과 미주, Payward 인가로 Reap이 유럽과 미국 [F-1256](https://www.payward.com/press-release/payward-reap-close). 2026-09-24 Visa 스테이블코인 카드 100개 넘는 시장 [F-1513](https://www.payward.com/press-release/reap-visa-stablecoin-card-programs-100-markets)
10. 발언: Kraken 공동 CEO, Reap CEO [F-1512](https://www.payward.com/press-release/payward-acquires-reap) [LDKR-023](https://www.payward.com/press-release/payward-acquires-reap)

### 1-10. Saldo Bank(2026-10 계약, EU 은행)
1. 한 줄 사건: 2026-10-14 핀란드 지주회사 Saldo Finance Oy(자회사 Saldo Bank UAB, 리투아니아 인가 디지털 은행) 인수 계약, 종결 2027 예상(규제 승인 필요), 금액 비공개 [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank) [F-1358](https://www.digitaltoday.co.kr)
2. 그 전 상태
   - 2013-10 독일 Fidor Bank 제휴로 유로 입출금 [F-1731](https://blog.kraken.com/news/kraken-forms-exclusive-partnership-with-fidor-bank)
   - 2020-09 와이오밍 SPDI는 대출 금지 [F-1719](https://blog.kraken.com/post/6241/kraken-wyoming-first-digital-asset-bank) [F-1722](https://www.wyoleg.gov/2019/Summaries/HB0074.pdf)
   - 2023-03 Silvergate 붕괴 뒤 Silvergate 경유 ACH 입출금을 2023-03-27부터 끝냄(2019부터 써 옴) [LDKR-015](https://www.financemagnates.com/cryptocurrency/news/kraken-to-suspend-ach-deposits-and-withdrawals/)
   - 2023-09 아일랜드 EMI [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/), 2026-03-04 연준 마스터 계정 [F-1532](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account), 누적 대출 20억 달러 넘게 [F-1254](https://www.payward.com/press-release/payward-acquires-saldo-bank)
3. 직접 받는 길: EU 은행 인가를 직접 신청한 기록 빈칸 B25
4. 대상 회사: 4개 영업 시장(리투아니아, 핀란드, 스웨덴, 독일)과 네덜란드 패스포트, 예금, 소비자 대출, 중소기업 대출, 신용카드 [LDKR-017](https://www.payward.com/press-release/payward-acquires-saldo-bank) [F-1358](https://www.digitaltoday.co.kr). 고객 수와 자산 규모 빈칸 B25
5. 판 쪽: Saldo 대표는 은행 인가는 그 위에 무엇을 짓느냐만큼 가치 있다고 말함 [LDKR-017](https://www.payward.com/press-release/payward-acquires-saldo-bank). 주주와 판 이유 빈칸 B25
6. 승인: 종결 전. 승인 당국 이름 빈칸
7. 대금: 비공개
8. 같은 시기 바깥: 2026-10-12 두바이 VARA 최종 승인 [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch), 2026-10-22 카자흐스탄 원칙 승인 [LDKR-029](https://www.payward.com/press-release/kraken-afsa-in-principle-approval-kazakhstan). 경쟁사: Coinbase 2025-10-03 OCC 신탁회사 신청 [F-2122](https://www.comptrollerofthecurrency.gov/topics/charters-and-licensing/digital-assets-licensing-applications/coinbase-national-trust-company.pdf)
9. 산 뒤: 종결 전. 계획은 유럽 고객 예금 이자, 대출, 다른 핀테크용 은행 기능(규제 승인 필요) [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)
10. 발언: Kraken 공동 CEO, Saldo 대표, 회사 글 [LDKR-017](https://www.payward.com/press-release/payward-acquires-saldo-bank) [F-1194](https://www.payward.com/press-release/payward-acquires-saldo-bank)

## 4. 카드 2. 직접 받은 인가

### 2-1. 미국 송금업(FinCEN MSB, 주별 송금업)
- 법인: Payward Interactive, Inc.(NMLS 1843762), FinCEN 등록 송금업자 [F-0375](https://www.kraken.com/krak) [F-0376](https://www.kraken.com/krak). 신청일, 승인일, 주별 인가 수 빈칸 B04
- 연 상품: Krak 송금(제3자 결제), 미국 고객 가상자산 서비스 [F-0376](https://www.kraken.com/krak)
- 다른 세 회사: 다른 회사 담당 파일 참조

### 2-2. 영국(FCA MTF, MLR 등록, EMI)
- 법인과 승인일: Crypto Facilities MTF 2020-07-06 [F-2036](https://www.cryptofacilities.com/cryptocurrency-news/crypto-facilities-becomes-first-licensed-crypto-futures-venue-in-europe), Crypto Facilities MLR 2021-11-03 [LDKR-045](https://www.kraken.com/press/releases/crypto-facilities-receives-cryptoasset-registration-from-the-uks-fca), Payward Ltd 가상자산 등록(날짜 빈칸 B07) [F-0384](https://www.kraken.com/legal/uk/investor-education), 영국 EMI 2025-03-11 보도 [LDKR-039](https://cryptoslate.com/kraken-strengthens-uk-crypto-regulatory-standing-with-fca-electronic-money-license/)
- 연 상품: 기관 MTF 선물 250종 넘게 [F-2038](https://mtf.kraken.com). 영국 가상자산 거래는 규제 밖 서비스라고 회사가 고지 [F-0385](https://www.kraken.com/legal/uk/investor-education)
- 왜 영국: 인수 법인을 런던에 두고 FCA 감독을 받겠다고 밝힘 [LDKR-044](https://blog.kraken.com/news/kraken-acquires-crypto-derivatives-trading-platform-and-index-provider-crypto-facilities-in-nine-figure-deal-official-press-release)
- 다른 세 회사: Robinhood는 Bitstamp UK(FCA 등록) 인수로 2026-08 영국 가상자산 출시 [F-1578](https://robinhood.com/newsroom/robinhood-launches-crypto-trading-for-uk-investors/)

### 2-3. 와이오밍 SPDI 은행(2020-09)
- 법인: Payward Financial, Inc.(Kraken Financial). 승인 2020-09-16, 신청일 빈칸 B06 [F-1719](https://blog.kraken.com/post/6241/kraken-wyoming-first-digital-asset-bank)
- 제도: 2019 와이오밍 법이 처음 만든 은행 형태, 예금 100% 유동자산, 대출 금지, 예금자는 법인만 [F-1722](https://www.wyoleg.gov/2019/Summaries/HB0074.pdf) [F-2076](https://www.wyoleg.gov/2019/Enroll/HB0074.pdf)
- 연 상품: 기관 적격 수탁(2024-03 미국, 2024-07 영국과 호주) [F-2063](https://www.kraken.com/press/releases/Kraken-Institutional-Expands-Custody-Solution-to-UK-and-Australia), 2026-03-04 연준 마스터 계정 [F-1532](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account)
- 왜 이 인가: 외부 금융기관 의존을 줄이려고(회사 발표) [F-1719](https://blog.kraken.com/post/6241/kraken-wyoming-first-digital-asset-bank). 뉴욕 경로는 2015 철수로 닫힘(KR-E10, 판단)
- 다른 세 회사: Coinbase는 뉴욕 제한목적 신탁(2018-10)과 OCC 신탁 신청(2025-10) [F-2119](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr1810231) [F-2122](https://www.comptrollerofthecurrency.gov/topics/charters-and-licensing/digital-assets-licensing-applications/coinbase-national-trust-company.pdf)

### 2-4. 일본 암호자산교환업 재등록(2020-09)
- 법인: Payward Asia株式会社, 등록 2020-09-08(関東財務局長 第00022号), 계좌 개설 2020-09-18 [LDKR-031](https://blog.kraken.com/post/6363/launch-in-japan)
- 그 전: 2018-04 일본 철수, 2018년까지 쓰던 Payward Japan 서비스는 폐지 [F-1771](https://japantimes.co.jp/news/2018/04/18/business/u-s-cryptocurrency-exchange-kraken-leave-japanese-market) [LDKR-031](https://blog.kraken.com/post/6363/launch-in-japan)
- 그 뒤: 2022-12-28 두 번째 철수 발표(카드 3-4)

### 2-5. 아부다비 ADGM(2019 허가, 2022 가상자산 조건 충족)
- 법인: Payward MENA Holdings Limited, FSP 190008, 허가일 2019-12-12 [LDKR-024](https://www.adgm.com/public-registers/fsra/firms/financial-firms/payward-mena-holdings-limited-190008)
- 2022-04-25 가상자산 MTF와 수탁 승인 조건 충족, 디르함 거래 계획 [LDKR-025](https://www.adgm.com/media/announcements/adgm-welcomes-kraken-global-virtual-asset-exchange-to-its-international-financial-centre)
- 왜: Kraken 유럽 중동 총괄은 UAE의 높은 가상자산 참여율과 ADGM 규제 선도를 이유로 듦 [LDKR-025](https://www.adgm.com/media/announcements/adgm-welcomes-kraken-global-virtual-asset-exchange-to-its-international-financial-centre)
- 그 뒤: 2023-02 사무소 정리, 2025-12-19 허가 철회(카드 3-5)
- 다른 세 회사: Binance는 2025-12 ADGM 인정투자거래소 등 3종 [F-0064](https://tools.prnewswire.com/en-us/live/20813/release/20251207EN41035) [F-0066](https://tools.prnewswire.com/en-us/live/20813/release/20251207EN41035)

### 2-6. EU 국가별 등록과 아일랜드 EMI(2023)
- 2023-09-27 보도: 아일랜드 EMI, 스페인 VASP, 그 전에 아일랜드와 이탈리아 VASP [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/)
- 왜: 유럽의 앞을 내다본 규제 덕에 확신을 갖고 키울 수 있다고 부사장이 말함 [LDKR-038](https://www.financemagnates.com/cryptocurrency/kraken-bolsters-eu-presence-gains-approvals-in-ireland-and-spain/)
- 그 뒤: BCM 인수로 프랑스, 폴란드, 네덜란드를 더함(카드 1-3)

### 2-7. 캐나다 제한 딜러(2023 약정, 2025 등록)
- 법인: Payward Canada Inc.와 Payward, Inc.
- 2019-07 FINTRAC 송금업자 등록, 2023-03-30 사전 등록 약정(PRU) 발표, 2025-04-02 제한 딜러 등록 발표(약 2년, 계산) [LDKR-033](https://www.financemagnates.com/cryptocurrency/kraken-files-pre-registration-with-canadas-ontario-regulator/) [LDKR-034](https://blog.kraken.com/news/restricted-dealer-registration-canada)
- 왜: 캐나다 증권감독자 협의체의 더 엄격해진 투자자 보호 지침을 지키려고(회사 성명, 매체 인용) [LDKR-033](https://www.financemagnates.com/cryptocurrency/kraken-files-pre-registration-with-canadas-ontario-regulator/)
- 제도 상황: OSC는 2022-06 KuCoin 영업 금지와 Bybit 제재, Binance는 2021 온타리오에서 나감(매체) [LDKR-033](https://www.financemagnates.com/cryptocurrency/kraken-files-pre-registration-with-canadas-ontario-regulator/)
- 다른 세 회사: Robinhood는 2026-06 WonderFi 인수로 캐나다 [F-0219](https://www.kucoin.com/news/flash/robinhood-completes-180m-acquisition-of-wonderfi-to-expand-in-canada)

### 2-8. 미국 브로커딜러(Kraken Securities, 2024-06)
- 법인: Kraken Securities LLC(옛 Payward Equities LLC, 2022-11-02 델라웨어 설립), FINRA 승인 2024-06-10, 53개 주와 지역 등록(뉴욕 포함) [LDKR-036](https://api.brokercheck.finra.org/search/firm/324343) [F-0242](https://api.brokercheck.finra.org/search/firm/324343)
- 연 상품: 2025-04-14 미국 주식과 ETF 1.1만 종 넘게, 청산은 Alpaca [F-1800](https://blog.kraken.com/product/equities/stock-and-etf-trading) [F-1801](https://www.financemagnates.com/cryptocurrency/kraken-adds-over-us-stocks-and-etfs-in-collaboration-with-broker-dealer-alpaca/)
- 다른 세 회사: Coinbase는 2018 Keystone 등 인수로 [F-2115](https://altswire.com/crypto-exchange-coinbase-buys-broker-dealers-move-offer-regulated-securities/), Robinhood는 2013 직접 등록 [F-0243](https://api.brokercheck.finra.org/search/firm/165998)

### 2-9. 버뮤다 BMA Class F(2024-08)
- 법인: PDSL 2024-08-01, Payward Commercial Treasury 2024-11-06 [F-1416](https://www.bma.bm/regulated-entities)
- 연 상품: 2024-10 파생 거래장 200개 넘는 계약 [F-1368](https://www.businesswire.com/news/home/20241003985524/en/Kraken-Launches-Regulated-Derivatives-Venue-in-Bermuda), 2025-06 xStocks 판매 법인 [F-1249](https://blog.kraken.com/product/xstocks/tokenized-equities-now-available)
- 왜 버뮤다: 국제적으로 인정받는 규제 관할(회사 발표) [F-1368](https://www.businesswire.com/news/home/20241003985524/en/Kraken-Launches-Regulated-Derivatives-Venue-in-Bermuda)
- 다른 세 회사: Coinbase Bermuda 2023-04-19 Class F [F-1416](https://www.bma.bm/regulated-entities), 2023-05 국제 거래소 출범 [F-1631](https://www.marketsmedia.com/introducing-coinbase-international-exchange/)

### 2-10. 아일랜드 MiCA(2025-06)
- 법인: Payward Europe Solutions Limited(수탁, 교환 등), Payward Global Solutions Limited(거래 플랫폼 운영 코드 b) [F-0250](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv) [F-0251](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)
- 승인 2025-06-25, 신청일 빈칸 B09
- 왜 아일랜드: 아일랜드 중앙은행의 오랜 엄격한 감독 경험(공동 CEO) [LDKR-047](https://blog.kraken.com/news/mica-license-central-bank-of-ireland) [F-1371](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
- 새로 연 것과 맞춘 것: 7개국 국가별 등록으로 하던 영업을 MiCA 하나로 옮김 [F-1438](https://blog.kraken.com/news/mica-license-central-bank-of-ireland). MiFID와 EMI를 더해 현물, 파생, 결제 [LDKR-047](https://blog.kraken.com/news/mica-license-central-bank-of-ireland)
- 그 뒤: 2026 Q2 EEA 계정 증가가 두드러졌다고 밝힘(회사 주장) [F-1530](https://www.payward.com/press-release/q2-2026-financial-highlights)
- 다른 세 회사: Coinbase 룩셈부르크 2025-06-20, Robinhood 리투아니아 2025-05-29(둘 다 거래 플랫폼 운영 코드 없음) [F-1414](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)

### 2-11. 연준 마스터 계정(2026-03)
- 법인: Kraken Financial, 승인 2026-03-04, 신청일 빈칸 B10 [F-1532](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account)
- 회사는 5년 넘는 당국 접촉과 검사를 거쳤다고 밝힘 [LDKR-016](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account)
- 왜: Fedwire 직접 결제, 중개 은행 의존 축소(공동 CEO) [LDKR-016](https://www.payward.com/press-release/kraken-first-digital-asset-bank-federal-reserve-master-account)
- 그 뒤: 미국 달러 송금을 자체 계정으로 옮기는 계획 [F-1259](https://www.payward.com/press-release/payward-q3-2026-financial-highlights)

### 2-12. OCC 국법 신탁회사 신청(2026-05)
- 2026-05-08 신청, Payward National Trust Company 설립 목적, 주로 가상자산 수탁과 신탁 [LDKR-018](https://www.payward.com/press-release/payward-files-application-for-occ-national-trust-company)
- 왜: 연방 감독 적격 수탁이 필요한 기관 고객, 와이오밍 SPDI와 보완(공동 CEO) [LDKR-018](https://www.payward.com/press-release/payward-files-application-for-occ-national-trust-company)
- 다른 세 회사: Coinbase 2025-10-03 신청 [F-2122](https://www.comptrollerofthecurrency.gov/topics/charters-and-licensing/digital-assets-licensing-applications/coinbase-national-trust-company.pdf)

### 2-13. 두바이 VARA(2026-05 예비, 2026-10 최종)
- 법인: Payward FZCO. 예비 승인 2026-05-21, 최종 시장 승인 2026-10-12(약 5개월, 계산) [LDKR-027](https://www.payward.com/press-release/payward-vara-authorization-uae) [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch)
- 왜: 역외가 아니라 현지 감독 법인으로 영업하려고(공동 CEO) [LDKR-027](https://www.payward.com/press-release/payward-vara-authorization-uae)
- 연 상품 계획: 디르함 현물과 신용거래, 스테이킹, xStocks, Krak, 기관 장외와 Prime [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch)
- 그 전: 2023-02 아부다비 철수(카드 3-5)
- 다른 세 회사: Binance VARA 2022 [F-0068](https://www.vara.ae/en/news/binance-secures-mvp-licence-from-dubais-virtual-assets-regulatory-authority/), Robinhood 두바이 DFSA 2026-10 [F-0238](https://finviz.com/news/409270/robinhood-reports-third-quarter-2026-results), Coinbase가 인수한 Deribit VARA 조건부 인가 [F-2095](https://s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf)

### 2-14. 영국령 버진아일랜드 VASP(2026-06)
- 2026-06-23 BVI FSC VASP 등록 발표(2022 VASP 법) [LDKR-030](https://www.payward.com/press-release/payward-bvi-vasp-registrations)

### 2-15. 카자흐스탄 AFSA 원칙 승인(2026-10)
- 2026-10-22 Payward Kazakhstan, 디지털자산 거래 시설, 투자 매매 중개, 수탁 원칙 승인 [LDKR-029](https://www.payward.com/press-release/kraken-afsa-in-principle-approval-kazakhstan)

## 5. 카드 3. 실패, 해지, 철회, 철수

### 3-1. 뉴욕(2015-08, BitLicense 미신청)
- 무엇을 멈췄나: 뉴욕주 BitLicense를 신청하지 않고 뉴욕 주민 서비스 중단(시행 2015-07-24, 유예 끝 2015-08-10) [F-1750](https://www.financemagnates.com/cryptocurrency/exchange/bitfinex-kraken-latest-to-pull-out-of-ny-as-bitlicense-grace-period-ends/)
- 왜: 뉴욕 은행 보장 없음, 무인가 경쟁자 단속 보장 없음, 뉴욕만 서비스를 나눠야 함, 작은 시장에 드는 비용(성명, 매체 인용) [F-1751](https://siliconangle.com/?p=242146)
- 그 뒤: 2018-04 뉴욕 검찰 질의 거부, 2018-09 뉴욕주 금융감독청 회부 [F-1772](https://coinjournal.net/news/kraken-ceo-blasts-attorney-general-schneiderman) [F-1773](https://ag.ny.gov/sites/default/files/vmii_report.pdf). Kraken Securities는 뉴욕주 증권사 등록이 있음 [LDKR-036](https://api.brokercheck.finra.org/search/firm/324343). Krak 카드는 뉴욕 제외 [F-0436](https://www.kraken.com/krak)
- 다른 회사: Coinbase BitLicense 2017-01 [F-1412](https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses)

### 3-2. 워싱턴주(2017-03)
- 무엇을 멈췄나: 워싱턴주 고객 서비스 중단. 2016-12 산 Glidera도 같은 달 중단(보도, Bitcoin.com) [LDKR-035](https://news.bitcoin.com/regulations-shapeshift-keepkey-washington-state/)
- 왜: 주가 요구하는 규제 준수 비용이 높음(회사 설명, 매체 인용) [LDKR-035](https://news.bitcoin.com/regulations-shapeshift-keepkey-washington-state/)
- 그 뒤: 복귀 시점 빈칸 B26

### 3-3. 일본 1차(2018-04)
- 무엇을 멈췄나: 2018-04-17 일본 거주자 서비스를 2018-06 말까지 끝낸다고 발표(2014-10부터 영업) [F-1771](https://japantimes.co.jp/news/2018/04/18/business/u-s-cryptocurrency-exchange-kraken-leave-japanese-market)
- 왜: 일본 사업 비용 상승, 다른 지역에 자원 집중(회사 성명, 매체 인용) [F-1771](https://japantimes.co.jp/news/2018/04/18/business/u-s-cryptocurrency-exchange-kraken-leave-japanese-market)
- 그 뒤: 2020-09-08 Payward Asia로 재등록 [LDKR-031](https://blog.kraken.com/post/6363/launch-in-japan)

### 3-4. 일본 2차(2022-12 발표, 2023-01 등록 반납)
- 무엇을 멈췄나: Payward Asia 서비스 종료와 2023-01-31 금융청 등록 반납 [LDKR-032](https://cointelegraph.com/news/kraken-quits-japan-for-second-time-blaming-a-weak-crypto-market)
- 왜: 일본 시장 상황과 세계 약세장으로 일본 사업을 더 키울 자원을 쓸 만하지 않음(회사 블로그, 매체 인용) [LDKR-032](https://cointelegraph.com/news/kraken-quits-japan-for-second-time-blaming-a-weak-crypto-market)
- 같은 시기: 2022-11-30 직원 약 30% 감원 (KR-E12)
- 그 뒤 대신 한 것: 빈칸 B27

### 3-5. 아부다비(2023-02 사무소 정리, 2025-12 허가 철회)
- 무엇을 멈췄나: 2023-02 디르함 거래 중단과 사무소 정리(보도, CoinGeek) [LDKR-026](https://coingeek.com/kraken-shuts-down-abu-dhabi-office-less-than-a-year-after-launch/). 등록부상 허가 철회일 2025-12-19 [LDKR-024](https://www.adgm.com/public-registers/fsra/firms/financial-firms/payward-mena-holdings-limited-190008)
- 왜: 자원을 사명에 맞게 배치하려고 사업을 정기적으로 다시 봄(대변인, 매체 인용) [LDKR-026](https://coingeek.com/kraken-shuts-down-abu-dhabi-office-less-than-a-year-after-launch/)
- 그 뒤 대신 한 것: 2026-05 두바이 VARA 예비 승인, 2026-10 최종 승인(카드 2-13) [LDKR-027](https://www.payward.com/press-release/payward-vara-authorization-uae) [LDKR-028](https://www.payward.com/press-release/kraken-plans-uae-launch)

### 3-6. 미국 개인 신용거래 중단(2021-06)과 CFTC 제재(2021-09)
- 무엇을 멈췄나: 2021-06-23부터 ECP가 아닌 미국 고객 새 마진 차단 [F-1848](https://decrypt.co/73233/crypto-exchange-kraken-disables-margin-trading-some-u-s-residents)
- 왜: CFTC는 지정 선물 거래소 밖 소매 상품거래이고 FCM 미등록이라고 봄, 125만 달러 [F-1781](https://mondovisione.com/media-and-resources/news/cftc-imposes-a-125-million-penalty-against-kraken-for-offering-illegal-off-exc-2021928/) [F-1782](https://mondovisione.com/media-and-resources/news/cftc-imposes-a-125-million-penalty-against-kraken-for-offering-illegal-off-exc-2021928/)
- 그 뒤 대신 한 것: NinjaTrader(FCM) 인수 뒤 2026-05-06 CFTC 규제 마진으로 다시 엶 [F-1850](https://blog.kraken.com/product/margin/cftc-regulated-spot)

### 3-7. 미국 수탁형 스테이킹 중단(2023-02)
- 무엇을 멈췄나: 2023-02-09 SEC 합의로 미국 고객 수탁형 스테이킹 종료, 3,000만 달러 [F-1786](https://blog.kraken.com/news/settlement) [F-1787](https://techcrunch.com/2023/02/09/kraken-ends-its-crypto-staking-services-for-us-clients-following-30m-sec-charge)
- 그 뒤: 2023-11-20 SEC 거래소 소송, 2025-03 취하 [F-1788](https://blog.kraken.com/news/kraken-continues-to-fight-for-its-mission-and-crypto-innovation-in-the-united-states) [F-1790](https://blog.kraken.com/news/sec-lawsuit-dismissal) [F-1791](https://decrypt.co/312072/sec-drops-cases-kraken-consensys-cumberland-drw)

### 3-8. Deribit 인수 협상(2025-02 보도, 못 산 것)
- 무엇을 하려 했나: 옵션 거래소 Deribit 다수 지분 인수 협상(보도, Blockhead가 CoinDesk 인용). Deribit 가치 40억에서 50억 달러로 Bloomberg가 봄 [LDKR-041](https://blockhead.co/2025/02/21/coinbase-kraken-in-talks-to-acquire-deribit-as-crypto-derivatives-market-heats-up-2)
- 왜 멈췄나: 회사 발언 빈칸 B28
- 그 뒤: 2025-05-08 Coinbase가 약 29억 달러(현금 7억 달러와 주식)에 인수 발표 [F-1378](https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform). Kraken은 같은 해 NinjaTrader(2025-03), Small Exchange(2025-10)를 삼

## 6. 빈칸 목록
- 막힌 경로(시도한 방법)
  - coindesk.com 영문 기사(2026-09-26 Sethi 인터뷰): curl 429, WebFetch 허용 밖. 인수 기준 원문 영문은 한국어판(F-1349)과 PYMNTS 인용(LDKR-048)으로만 봄
  - geekwire.com, gulfbusiness.com: curl 403
  - ninjatrader.com 2024 재무제표 PDF: 404
  - FCA 등록부, NFA BASIC, CFTC 명령 원문: 이번에 열지 않음(기존 노하우상 막힘)
- B01. Beaufort Fiduciaries 인수 시점, 전 주인, 금액(ASIC 의견서는 2025-02-28 이전 인수만 확인)
- B02. Magna 인수 발표일(페이지에 날짜 없음)
- B03. Tribe Capital이 가진 투자자문 등록과 인수 대금
- B04. Payward Interactive의 FinCEN 등록일과 주별 송금업 인가 수와 승인일
- B05. Crypto Facilities MTF 신청일(회사 자료 2019와 2020 엇갈림)
- B06. 와이오밍 SPDI 신청일
- B07. Payward Ltd의 FCA 가상자산 등록일, 영국 EMI 법인 이름과 승인일
- B08. 아일랜드 VASP(보도 2023-04 추정), 이탈리아 OAM 등록의 정확한 날짜
- B09. MiCA 신청일
- B10. 연준 마스터 계정 신청일(보도 2020-10, 1차 미확인)
- B11. Crypto Facilities를 산 이유 중 "왜 직접 인가를 받지 않았나"에 대한 회사 문장, 직접 신청 여부
- B12. Crypto Facilities 주주 구성, 판 이유, FCA 지배주주 변경 승인일
- B13. Small Exchange 인수 당시 손님, 거래량, 상장 상품과 인수 뒤 실제 상장 상품
- B14. Bit Trade 판 쪽 사정, Kraken 이름의 AUSTRAC 등록일
- B15. BCM 고객 수, 네덜란드 직접 등록 시도 여부, 승인 당국
- B16. 키프로스 인수 전 EU 파생 판매 법인, MiFID 직접 신청 여부, 판 쪽 사정
- B17. Kraken의 FCM 직접 신청 여부, NinjaTrader 인수 전 제휴, 지배권 변경 당국 절차
- B18. NinjaTrader 매출과 이익, 대금의 매출 대비 배수
- B19. Long Ridge Equity Partners가 판 이유(투자 회수 시점에 대한 발언)
- B20. Kraken의 DCM 직접 신청 여부, Small Exchange 지배권 변경 CFTC 절차
- B21. 발행사를 직접 세우는 길을 검토했는지, Backed 주주 구성
- B22. Kraken의 DCO 직접 신청 여부
- B23. Bitnomial 손님, 매출, 주주와 판 이유
- B24. Reap 매출 금액, 주주, 카드 인가 직접 취득 검토 여부
- B25. Saldo Bank 고객과 자산 규모, 주주와 판 이유, EU 은행 인가 직접 신청 여부
- B26. 워싱턴주 복귀 시점
- B27. 일본 2차 철수 뒤 일본 고객 대안
- B28. Deribit 협상이 멈춘 이유(회사 발언)
- B29. Cryptowatch 서비스 종료 시점(2023 보도, The Block은 막힘)
- B30. 캐나다 제한 딜러 등록부 날짜(보도상 2025-04-01, 등록부 미열람)
