# Ondo: PM이 개요를 읽고 다음에 물을 질문 (2026-11-17)

- 무엇: kb/cards/ondo.md를 처음 읽은 PM이 이어서 물을 새 질문 15개와 답. 녹취 본인 질문 78~86과 셀프 챌린지 17~19는 이미 물은 것이라 뺌
- 각도 번호: 1 숫자의 함의, 2 왜 그것을 왜 그때 왜 그 방식, 3 누가 누구에게 무엇을 주고 누가 돈을 내나, 4 모순과 빈 곳, 5 다른 회사와 비교, 6 KDX에 옮기면, 7 앞으로
- KDX 구조: 참여 증권사가 고객과 계좌를 갖고, KDX는 증권사가 넘긴 주문을 받아 체결하는 거래 시설
- 새로 찾은 사실은 work/Q2-ON/facts.csv, sources.csv(Q2ON-001부터)

## PM이 가장 먼저 물을 3개
1. **Q4**: 개요 1장의 "발행 법인 지분 90.01%는 재단 쪽"을 읽으면 "그럼 Ondo Finance는 뭘로 먹고사냐"가 바로 나옴. PM이 가장 자주 묻는 "뭘로 돈 벌어"(PM 관점 23)와 모순 점검(12)이 한 질문에 겹침
2. **Q1**: 개요가 수익 차이 0.35달러 예시만 주고 1년 금액을 안 줌. 숫자마다 "그래서"(PM 관점 13)를 묻는 PM은 곱셈부터 해 봄
3. **Q12**: Ondo가 "한국이 활성 거래자 1위"라고 말함. KDX에 쓸 수 있나(PM 관점 19)를 묻는 PM에게 가장 가까운 숫자이고, 한국 법에서 되는지가 바로 걸림

## 질문과 답

### Q1. [1] USDY에서 Ondo 쪽(발행 법인)에 남는 돈은 1년에 얼마인가
- 답: (판단) 잡는 기준에 따라 연 약 690만~2,500만 달러이고, 어느 쪽이든 회사가 지금까지 받은 지분 투자 2,400만 달러 안팎임
  - 계산 1(보유자 토큰 기준, 판단): 유통 USDY 19.7억 달러 × (담보 만기수익률 4.10% − 보유자 수익률 3.75%) = 19.7억 × 0.35% ≈ 690만 달러
  - 계산 2(담보 전체 기준, 판단): 담보 24.16억 × 4.10% ≈ 9,906만 달러에서 보유자 지급 19.7억 × 3.75% ≈ 7,388만 달러를 빼면 ≈ 2,518만 달러
  - 개요의 "USDY 23.8억 달러"는 홈페이지 예치 총액(TVL, Total Value Locked: 상품에 들어 있는 돈 전체)이고, 보유자가 가진 토큰은 19.7억 달러임. 23.8억 × 0.35%로 계산하면 833만 달러로 과대
  - 만기수익률(국채를 끝까지 들고 있을 때 받을 연 수익률)은 실제로 받은 이자와 다르고, 회사는 손익을 밝히지 않음. 위 숫자는 상한을 가늠하는 용도임
- 근거: https://ondo.finance/usdy (2026-11-16 화면, 유통 19.7억, 기초 자산 24.16억, 만기수익률 4.10%), https://ondo.finance/ (홈페이지 USDY TVL 23.8억)
- 한 단계 더: 계산 2의 차이 1,800만 달러(2,518만 − 690만)는 초과 담보가 번 돈인데, 그 초과 담보는 누구 돈인가(Q2)

### Q2. [4] USDY 담보(24.2억 달러)가 토큰(19.7억 달러)보다 4.5억 달러, 23% 많다. 그 차이는 누구 돈인가
- 답 못 함(일부): 회사가 밝힌 것은 2023-08 출시 글의 "약 3%의 손실 완충분(담보 값이 떨어지면 보유자보다 먼저 깎이는 몫)으로 초과 담보하고, 그 일부를 Ondo Finance가 댐"뿐임
  - 차이 계산(판단): 24.16억 − 19.7억 = 4.46억 달러, 4.46억 ÷ 19.7억 ≈ 22.6%. 회사가 밝힌 3%보다 약 20%p 큼
  - 같은 화면의 담보비율 표시 156.90%도 두 숫자의 비(약 123%)와 맞지 않음. 산식은 밝히지 않음
  - 본 곳: USDY 화면, 출시 글, 회사 문서 USDY 기본 설명
- 근거: https://ondo.finance/usdy , https://ondo.finance/blog/introducing-ondo-usd-yield-usdy
- 한 단계 더: 초과분이 발행 법인 자기 자본이면 그 수익은 지분 90.01%를 가진 재단 쪽(Flux Finance)으로 가는가, 보유자 손실 완충에만 쓰이는가

### Q3. [4] USDY는 이름은 하나인데 발행 법인과 담보가 둘인가
- 답: 그렇다. 회사 문서는 USDY가 원래 Ondo USDY LLC 발행이었고 2025-12-15부터 BVI 발행 법인(Ondo Global Markets (BVI) Limited) 아래로 들어왔으며, 발행 시점에 따라 담보가 단기 미국 국채, iShares 단기 국채 ETF 지분, 은행 예금 중 하나라고 적음
  - 상환도 둘로 나뉨: 달러 상환은 Ondo USDY LLC가 미국 밖 은행 계좌로만, USDC 상환은 BVI 법인이 함
  - (판단) USDY 화면의 미국 국채 82.69%는 예전 LLC 발행분, SHVon(iShares 0~1년 국채 ETF를 Ondo가 토큰으로 만든 것) 17.27%는 BVI 발행분의 담보로 보임. 회사가 이렇게 짝지어 밝히지는 않음
- 근거: https://docs.ondo.finance/general-access-products/usdy/basics.md , https://ondo.finance/usdy
- 한 단계 더: 같은 USDY라도 어느 법인 것을 가졌느냐에 따라 발행 법인이 망할 때 받는 담보가 다른가. 지갑에서 둘을 구별할 수 있나

### Q4. [4] 발행 법인 지분 90.01%가 재단 쪽이면 Ondo Finance Inc.는 무엇으로 먹고사나
- 답 못 함(일부): 회사 문서에서 Ondo Finance Inc.의 자리는 셋까지만 보이고, 그 대가로 받는 돈은 어디에도 없음
  - 주식 토큰의 'Tokenizer'(토큰화 작업과 가격 계산을 대신 하는 회사)로 적혀 있음. 대행 보수를 받는지, 얼마인지는 없음
  - BVI 발행 법인 지분 9.99%. 배당이나 이익 배분 조항은 공개 문서에 없음
  - 미국 사업은 Ondo Finance Inc. 아래에 있음: Oasis Pro Markets(증권사, ATS), Oasis Pro TA(명의개서대리인), OUSG 펀드의 무한책임사원 쪽. (판단) 회사 몫으로 확실히 잡히는 돈은 이쪽인데, OUSG 운용보수는 2027-01-01까지 0이고 미국 토큰 판매 규모는 발표가 없음
  - 돈을 대는 쪽으로는 나옴: USDY 손실 완충분 일부를 Ondo Finance가 댐(2023). 주식 토큰 추가 담보는 Flux Finance(재단 완전 자회사)가 보증
  - 본 곳: BVI 발행 법인 확정 조건서(몰타 금융감독청 게시본), 회사 문서 법률 페이지와 보호 장치 페이지, 회사 블로그
- 근거: https://docs.ondo.finance/ondo-stocks/legal-and-regulatory.md , https://www.mfsa.mt/wp-content/uploads/2026/01/Ondo-Global-Markets-BVI-Limited-Final-Terms-Document-dated-11-November-2025.pdf , https://docs.ondo.finance/ondo-stocks/trust-and-transparency
- 한 단계 더: Ondo Finance Inc.와 발행 법인 사이에 용역 계약(서비스 수수료)이 있나. 회사 지분 투자자에게 ONDO 토큰을 7% 미만씩 준 것(Q5)이 이 구조의 보상인가

### Q5. [1] Ondo의 값어치는 회사 주식에 있나, ONDO 토큰에 있나
- 답: 바깥에서 값이 보이는 것은 ONDO 토큰뿐임. 시가총액 약 15.0억 달러(CoinGecko 집계, 2026-11-17, 1개 약 0.31달러). 회사 지분 가치는 공개되지 않음
  - 비교(판단): 15.03억 ÷ 지분 투자 2,400만 = 약 63배. 시드와 시리즈 A 투자자는 지분과 함께 ONDO를 각각 7% 미만 받음
  - ONDO는 Ondo DAO(토큰 보유자 투표 조직)와 Flux Finance의 의결권 토큰이라고만 적혀 있고, 발행 법인 수익을 나눠 받는 권리는 적혀 있지 않음
  - 회사는 SEC가 ONDO의 증권 여부를 포함해 살핀 비공개 조사가 기소 없이 끝났다고 밝힘(2025-12-09 게시)
- 근거: https://api.coingecko.com/api/v3/simple/price?ids=ondo-finance&vs_currencies=usd&include_market_cap=true , https://docs.ondo.foundation/ondo-token , https://ondo.finance/blog/tokenized-securities-step-forward
- 한 단계 더: 이름이 같은 Flux Finance(재단의 대출 프로토콜 이름이자 발행 법인 90.01% 주주)를 ONDO 투표가 움직이나. 그렇다면 발행 법인의 주인은 사실상 토큰 보유자인가

### Q6. [2] 왜 2023-01에 DeFi 금고를 접고 국채 토큰으로 바꿨나, 왜 그때인가
- 답: 회사가 밝힌 이유는 둘이고, (판단) 시점은 금리가 설명함
  - 회사: 이자가 붙지 않는 스테이블코인 1,000억 달러 이상의 보유자를 국채로 끌어오려고. 2022 무규제 가상자산 회사들이 잇따라 무너진 뒤 규제받는 회사만 쓰려고
  - (판단) 미국 연준이 2022-12-14 기준금리 목표를 4.25~4.50%로 올림. 스테이블코인을 그냥 들고 있으면 연 4% 넘게 버리는 상황이 됨. 1,000억 달러 × 4.25% = 연 42.5억 달러를 보유자가 못 받던 셈(판단, 계산)
  - DeFi 금고 수익은 2022 가상자산 하락으로 약해졌을 것이나, 회사가 밝힌 숫자는 없음
- 근거: https://ondo.finance/blog/announcing-tokenized-us-treasuries-and-bonds , https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm
- 한 단계 더: 금리가 1%p 내려 보유자 수익이 2.75%가 되면, 이자 0인 스테이블코인과 차이가 줄어 USDY 수요는 어떻게 되나. 회사는 금리 민감도를 밝히지 않음

### Q7. [5] Coinbase가 받는 USDC 몫과 Ondo의 USDY 차이는 무엇이 다른가
- 답: 둘 다 국채로 굴리는 달러 토큰이지만, USDC는 보유자에게 이자를 주지 않아 준비금 수익 대부분이 발행사(Circle)와 유통사(Coinbase) 몫이고, USDY는 보유자에게 3.75%를 주고 0.35%p 정도만 남김
  - (판단) 1달러당 남기는 몫: USDC 쪽은 준비금 수익 거의 전부(약 4%), USDY는 0.35% → 약 10분의 1
  - 대신 USDY는 스테이블코인이 아니라 담보가 붙은 채무증권(회사 표현 tokenized secured note)이라, 신원 확인을 마친 미국 밖 투자자에게만 팖. 이자를 주는 대가로 증권 규제를 받는 구조임(판단)
  - Coinbase 쪽 숫자(2025 USDC 몫 13.5억 달러)는 kb/cards/coinbase.md 1장 참고
- 근거: https://docs.ondo.finance/general-access-products/usdy/comparison-stablecoins
- 한 단계 더: 한국에서 이자 주는 달러 토큰을 KDX에 올리면 스테이블코인인가 증권인가. 증권이면 증권사 경로로만 팔 수 있나

### Q8. [3] Bitget 이용자가 TSLAon 1만 달러어치를 사면 그 돈은 누구에게 얼마씩 가나
- 답: 이 거래에서 Ondo 쪽에 바로 들어오는 돈은 0일 수 있음. 2차 매매라 거래 수수료는 Bitget이, 호가 차이는 상대편(시장조성자: 늘 사고팔 값을 내놓는 회사)이 가짐
  - Ondo 쪽(발행 법인)이 받는 때는 1차뿐임: 1차 매수자가 새로 발행받을 때 견적가와 실제 주식 매입가의 차이, 상환할 때 0.05%(1만 달러당 5달러). 발행 수수료는 0
  - (판단) 그래서 Ondo 수입은 2차 거래량이 아니라 1차 발행과 상환량에 묶임. 회사가 밝힌 "누적 거래 180억 달러"(2026-05)는 Ondo 수입의 기준이 아님
  - Bitget이 이 토큰에 받는 거래 수수료율과 1차 매수자가 누구인지는 찾지 못함
- 근거: https://docs.ondo.finance/ondo-stocks/fees-and-taxes , https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing.md , https://www.bitget.com/blog/articles/bitget-tokenized-stocks-etfs-ondo-expansion
- 한 단계 더: 2026-09 시작한 "주식을 넣으면 토큰을 주는" 발행(Alpaca 안 계좌 이체)이 늘면 견적가 차이 수입은 줄어드나(https://ondo.finance/blog/convert-shares-to-tokenized-stocks)

### Q9. [1][4] 주식 토큰 잔액이 회사 홈페이지 14.4억 달러, rwa.xyz 8.99억 달러로 다르다. 어느 숫자를 써야 하나
- 답 못 함: 차이 5.4억 달러(14.4 − 8.99 ≈ 5.41억, 회사 숫자의 약 38%, 판단)의 이유를 회사도 rwa.xyz도 밝히지 않음
  - 회사 숫자는 TVL(예치 총액): 2026-10-27 13억, 2026-11-17 14.4억. rwa.xyz는 발행 잔액 8.99억(2026-11-16)
  - 보유자 수도 기준이 다름: 홈페이지 "고유 보유자 약 18.1만", 2026-10-27 블로그 "누적 보유자 45만 이상"
  - (판단) 순위 비교에는 같은 잣대인 rwa.xyz 숫자를 쓰고, 회사 숫자는 회사 주장으로 표시함. 개요 1장과 2장 표가 14.4억을 쓰고 4장 순위는 8.99억을 써서 같은 문서 안에서 섞임
  - 본 곳: 회사 홈페이지, 회사 블로그, rwa.xyz 주식 토큰 표
- 근거: https://ondo.finance/ , https://app.rwa.xyz/stocks , https://ondo.finance/blog/ondo-stocks-live-on-robinhood-chain-and-uniswap
- 한 단계 더: rwa.xyz가 세는 체인 범위(이더리움, BNB 체인, 솔라나)와 회사 TVL에 Perps 담보나 포트폴리오 토큰이 들어가는지

### Q10. [5][2] Kraken과 Binance는 자기 거래소에서 자기 토큰을 파는데, Ondo는 왜 경쟁사 창구(Binance, Robinhood 체인)에도 공급하나
- 답: (판단) 자기 창구가 없어서 모든 창구에 넣는 전략임. 회사가 밝힌 이유는 2025-02 설계 변경 때의 "지갑, 거래소가 자기 이용자에게 팔 수 있게"
  - 2026-02-24 Binance Alpha와 Binance Wallet에 10종 상장. 2026-10-27 Robinhood가 만든 체인(Robinhood Chain)에 15종을 옮겨 Robinhood Stock Tokens와 맞바꿀 수 있게 함
  - 대가(판단): 창구가 자기 토큰을 내면 밀림. Binance bStocks 출시(2026-06-11) 전후로 Ondo 점유율 53.8%(2026-01-16) → 24.23%(2026-11-16). 잔액은 4.62억 → 8.99억으로 늘어 시장이 커진 몫은 받음
- 근거: https://cointelegraph.com/news/binance-alpha-ondo-tokenized-stocks-etfs , https://ondo.finance/blog/ondo-stocks-live-on-robinhood-chain-and-uniswap , https://cryptoslate.com/tokenized-equities-approach-1b-as-institutional-rails-emerge/ , https://app.rwa.xyz/stocks
- 한 단계 더: Binance 안에서 같은 종목의 Ondo 토큰과 bStocks 중 어느 쪽이 더 거래되나. Binance가 Ondo 상장을 내리면 어떻게 되나

### Q11. [5] Dinari와 Ondo는 둘 다 창구 없는 주식 토큰 발행사이고 둘 다 카카오페이증권과 협약했는데, 왜 잔액이 약 60배 차이 나나
- 답: (판단) 판매 경로 설계가 다름. Ondo 8.99억 달러(24.23%), Dinari 1,520만 달러(0.41%), 8.99억 ÷ 0.152억 ≈ 59배(2026-11-16, rwa.xyz)
  - Dinari: 핀테크 앱이 API로 붙어 자기 고객에게 팔아야 큼. 파트너가 고객을 데려와야 잔액이 생김
  - Ondo: 2025-02 토큰을 지갑끼리 자유롭게 옮길 수 있게 바꿔, 거래소와 지갑이 받아서 바로 상장함. 출시 날(2025-09-03) 받는 곳 이름만 Bitget Wallet, Trust Wallet, OKX Wallet 등 8곳 이상
  - 미국 인가: Dinari는 증권사를 직접 등록(약 1년 6개월), Ondo는 Oasis Pro를 인수(발표에서 완료까지 석 달)
- 근거: https://app.rwa.xyz/stocks , https://ondo.finance/blog/global-markets , https://ondo.finance/blog/global-markets-is-live
- 한 단계 더: 카카오페이증권이 두 회사와 따로 협약한 이유와, 두 협약에서 카카오페이증권이 맡는 일이 같은지

### Q12. [6] 한국 거주자는 Ondo Stocks와 USDY를 살 수 있나, "한국이 활성 거래자 1위"는 한국 법에서 괜찮은가
- 답: Ondo 문서로는 살 수 있음. 한국 법에서 괜찮은지는 답 못 함
  - Ondo Stocks와 USDY 자격 페이지의 금지 국가 목록에 있는 Korea는 북한(Democratic Republic of Korea)뿐이고, 대한민국은 금지 목록에도, 전문투자자로 제한하는 목록(브라질, EEA, 홍콩, 말레이시아, 싱가포르, 스위스, 영국)에도 없음
  - 반대로 OUSG는 한국 거주자와 한국 법인을 뺌
  - Ondo 아시아 담당은 한국이 Ondo Stocks 활성 거래자 수 세계 1위라고 말함(회사 주장, 블루밍비트 인터뷰 2026-11-05)
  - (판단) 한국 자본시장법은 증권을 공모(모집, 매출)하려면 발행인이 증권신고서를 내고 수리받아야 한다고 정함(제119조). Ondo Stocks는 회사 스스로 채무증권이라 함. 이 토큰을 한국 투자자가 사는 것에 대한 금융당국 입장은 찾지 못함
  - 본 곳: Ondo 자격 페이지 두 곳, 법령 DB(db/laws.csv), 웹 검색은 하지 못함(시간)
- 근거: https://docs.ondo.finance/ondo-stocks/eligibility.md , https://docs.ondo.finance/general-access-products/usdy/eligibility.md , https://en.bloomingbit.io/feed/news/123709 , https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=283195&efYd=20270204
- 한 단계 더: 한국 이용자는 어느 창구(해외 거래소, 지갑)로 사나. 그 수요를 국내 증권사 계좌와 KDX로 돌릴 길이 있나(국내 공모 신고를 낸 해외 토큰을 KDX에서 체결)

### Q13. [6] 카카오페이증권 협약 구조는 KDX 구조에서 누구 자리이고, 한국에서 되나
- 답: (판단) 카카오페이증권은 이 구조에서 KDX의 참여 증권사(국내 고객과 계좌) 자리가 아니라, 해외 발행사의 "기초 주식 조달과 보관" 짝 자리임. KDX의 체결 자리는 이 구조에 없음
  - 회사 발표: 카카오페이증권이 외국인 투자자 통합계좌(여러 외국인 주문을 한 계좌로 모아 넣는 계좌)를 운영해 기초 주식의 조달, 보관, 관리를 맡고, 두 회사가 토큰 발행과 상환, 잔고 대사 방식을 함께 연구함. 상용화 여부와 시점은 국내외 규제와 감독 지침을 보고 논의
  - 흐름(판단): 해외 투자자 → 해외 창구에서 토큰 매수 → Ondo 발행 법인 → 카카오페이증권 통합계좌 → 한국거래소에서 주식 매수. 토큰의 발행과 2차 매매는 모두 한국 밖
  - 한국 토큰증권 법(전자증권법 개정, 2027-02-04 시행)은 국내 발행 토큰증권 제도라 이 해외 발행 토큰에 적용되는지는 확인 못 함
- 근거: https://ondo.finance/blog/ondo-and-kakaopay-securities-partner , https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=283195&efYd=20270204
- 한 단계 더: 통합계좌로 산 주식을 해외 발행 법인의 담보로 잡는 것이 외국환거래와 통합계좌 규정상 되나. 이 구조가 되면 KDX 참여 증권사도 같은 짝 자리를 노릴 수 있나

### Q14. [6] Ondo가 산 미국 ATS(Oasis Pro Markets) 모델을 KDX에 옮기면 무엇이 같고 무엇이 다른가
- 답: (판단) 주문이 들어오는 길은 같고, 상품을 누가 만드느냐가 다름
  - 같은 것: 기존 증권사와 투자자문사가 통합계좌로 고객 주문을 넣고, Oasis Pro Markets가 1차 발행과 2차 거래 플랫폼을 운영함(2026-07-23 FINRA 승인, 회사 발표). 고객과 계좌는 기존 증권사에 남음
  - 다른 것: 같은 그룹의 명의개서대리인(Oasis Pro TA)이 토큰을 발행함(2026-07-02 IVV, MU). 거래 시설이 자기 그룹 상품을 거래시키는 수직 구조임. KDX가 따르면 자기 상품을 자기 시설에서 체결하는 이해상충 문제를 안게 됨(판단)
  - 실제 거래 개시와 거래량은 발표가 없음
- 근거: https://ondo.finance/blog/finra-authorizations-to-offer-tokenized-equities , https://ondo.finance/blog/ondo-launches-tokenized-securities-in-usa
- 한 단계 더: Oasis Pro ATS에 Ondo 밖 발행사 상품도 올라가나. 미국 ATS 규정은 운영사 자기 상품 거래를 어떻게 공시하게 하나

### Q15. [7] DTCC 토큰화 서비스(2026-10-29 개시)에 Ondo가 들어갔다. 이게 뭐고, 되면 무엇이 바뀌나
- 답: DTCC(미국 증권의 중앙 예탁과 결제를 맡는 기관)가 자기가 보관하는 주식에 대한 권리를 토큰으로 만들어 주는 서비스이고, 2026-07 Ondo의 CRCLon, SPYon이 이 권리로 뒷받침된 첫 토큰 주식이라고 회사가 밝힘
  - (판단) 지금 Ondo 주식 토큰의 기초 주식은 증권사 Alpaca와 신탁회사 BitGo에 맡겨져 있음. 이 방식이 퍼지면 보관의 맨 아래가 개별 증권사에서 중앙 예탁기관으로 내려가, Alpaca 한 곳에 몰린 위험(공통 결론 2)이 줄어듦
  - (판단) 한국으로 옮기면 한국예탁결제원 자리임. 개정 전자증권법은 전자등록기관과 계좌관리기관이 분산원장을 쓸 수 있게 함(2027-02-04 시행). KDX에는 체결한 토큰증권의 결제를 예탁원 분산원장에서 맞추는 길이 생김
  - 날짜: 2026-07 첫 토큰(발행), 2026-10-29 서비스 개시(출시)
- 근거: https://ondo.finance/blog/dtcc-tokenization-service-is-live , https://ondo.finance/blog/ondo-and-dtcc-collaborate-on-tokenized-stocks , https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=283195&efYd=20270204
- 한 단계 더: DTC 권리로 뒷받침된 토큰은 미국 밖 투자자에게도 팔 수 있나, 아니면 미국 안 보관형(Q14) 전용인가

### Q16. [7][4] EU 투자설명서가 2026-11-11에 끝났다. 지금 EU에서는 누구에게 파나
- 답: (판단) 지금 자격 페이지는 EEA 투자자를 전문투자자(MiFID II 전문 고객)나 적격투자자로만 받음. 일반 개인 판매는 투자설명서가 있어야 해서, 설명서가 끝난 뒤 개인 판매가 멈췄을 수 있음. 새 설명서 승인 여부는 찾지 못함
  - 날짜: 2025-11-11 리히텐슈타인 금융시장감독청(FMA) 승인, 유효기간 2026-11-11까지(확정 조건서)
  - 자격 페이지가 설명서 만료 전부터 이렇게 적혀 있었는지는 확인 못 함
  - 본 곳: Ondo 자격 페이지, 확정 조건서(몰타 금융감독청 게시본)
- 근거: https://docs.ondo.finance/ondo-stocks/eligibility.md , https://www.mfsa.mt/wp-content/uploads/2026/01/Ondo-Global-Markets-BVI-Limited-Final-Terms-Document-dated-11-November-2025.pdf
- 한 단계 더: Kraken xStocks도 같은 리히텐슈타인 설명서 경로인데, 갱신했나

## 답 못 한 질문 (전부 또는 일부)
- Q2 초과 담보 4.5억 달러의 주인, Q4 Ondo Finance Inc.가 받는 돈, Q9 주식 토큰 잔액 두 숫자의 차이 이유, Q12 한국 법에서 괜찮은가(일부), Q16 새 EU 설명서 여부(일부)
