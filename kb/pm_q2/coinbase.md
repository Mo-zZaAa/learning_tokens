# Coinbase: PM이 개요를 읽고 다음에 물을 질문

- 대상: kb/cards/coinbase.md를 처음 읽은 PM. 녹취의 Coinbase 질문 49~57과 셀프 챌린지 9~11은 이미 답해서 뺌
- 기준일 2026-11-17. (판단)은 회사가 밝히지 않은 해석이나 우리 계산
- 각도: 1 숫자의 함의, 2 왜 그것을 그때 그 방식으로, 3 누가 누구에게 무엇을 주고 누가 돈을 내나, 4 문서 안 모순과 빈 곳, 5 다른 회사와 비교, 6 KDX에 옮기면, 7 앞으로
- 쓰는 말
  - 거래대금: 고객이 사고판 금액의 합. 매출이 아님
  - 수수료율: 거래 수익 ÷ 거래대금. 1만 달러를 사고팔 때 회사가 받는 돈
  - 체결 시설(거래소): 사는 주문과 파는 주문을 맞붙이는 곳. 판매(중개): 고객 주문을 받아 체결 시설에 넘기는 곳
  - 선물 중개사(FCM): 고객의 선물 주문과 증거금(거래 보증금)을 받아 거래소에 넘기는 미국 인가 회사
  - 청산소(DCO): 체결된 거래의 양쪽 사이에 서서 대금과 계약 이행을 책임지는 곳

## PM이 가장 먼저 물을 3개
- Q1: 개인과 기관의 수수료율이 약 23배 차이(판단)라는 숫자가 KDX 수익 모델을 정함. 그 차이는 판매 자리의 몫이고 KDX 자리의 몫이 아님
- Q12: KDX와 같은 자리(Coinbase Derivatives, 체결 시설)가 혼자서 얼마나 버는지가 "그래서 KDX는 무엇으로 먹고사나"의 답인데 개요에 없음
- Q11: Coinbase 선물을 처음 팔던 외부 중개사를 경쟁사 Kraken이 샀음. 참여 증권사가 경쟁사로 넘어가면 KDX 주문이 끊길 수 있다는 위험의 실제 사례

---

## Q1. [1] 거래대금은 기관이 83%인데 거래 수익은 개인이 76%다. 수수료율은 몇 배 차이인가
- 답: 2026 3분기 개인은 1만 달러당 약 192달러, 기관은 약 8달러를 냄. 약 23배 차이(판단, 우리 계산)
  - 계산(판단): 개인 거래 수익 4.5억 ÷ 개인 현물 거래대금 234억 = 1.92%. 기관 0.92억 ÷ 기관 현물 1,111억 = 0.083%. 1.92 ÷ 0.083 ≈ 23
  - 비중 계산(판단): 기관 거래대금 비중 1,111 ÷ 1,345 = 83%. 개인 거래 수익 비중 4.5 ÷ (4.5 + 0.92 + 0.48) = 76%
  - 주의(판단): 기관 거래 수익에는 파생 수수료가 섞였을 수 있어 기관 현물 요율은 이보다 낮을 수 있음. 개인 거래 수익에도 예측시장이 들어감
  - 그래서(판단): Coinbase 이익의 중심은 체결이 아니라 개인 앱 판매(주문 접수)임. KDX 구조에서 이 자리는 참여 증권사이고, KDX가 받을 수 있는 것은 기관 쪽 요율에 가까움
- 근거: 2026 3분기 주주서한(현물 거래대금 개인 234억, 기관 1,111억), 실적 발표 자료(거래 수익 개인 4.5억, 기관 0.92억, 기타 0.48억). inputs/manual/B03_coinbase_Q3_26_shareholder_letter.pdf, inputs/manual/B03_coinbase_presentation.pdf (원문 위치 https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/ , db F-0915, F-1261)
- 한 단계 더: 개인 1.92% 중 명시 수수료와 스프레드(사는 값과 파는 값의 차이)는 각각 얼마인가. 회사는 둘을 나눠 밝히지 않음

## Q2. [1] 파생 거래대금이 전체의 81%인데 수익은 작다. 파생 1만 달러당 얼마 버나
- 답: 약 1달러(0.01%)로 개인 현물의 약 190분의 1임(판단, 우리 계산)
  - 계산(판단): 파생과 예측시장을 합친 거래 수익 = 거래 수익 5.902억 × 25% = 1.48억. 예측시장 연환산 순매출 2억 초과 → 분기 0.5억 초과. 파생만 1.48 − 0.5 = 약 0.98억 이하. 0.98억 ÷ 파생 거래대금 9,859억 = 약 0.01%
  - 그래서(판단): 거래대금이 커도 기관과 파생은 요율이 낮아 매출이 잘 늘지 않음. 체결 시설만 하는 KDX가 "거래대금 목표"만 잡으면 매출 목표가 안 나옴
- 근거: 2026 3분기 주주서한(전체 1조 2,138억 중 파생 9,859억), CFO 발언(파생과 예측시장이 거래 수익의 25%). https://s27.q4cdn.com/397450999/files/doc_financials/2026/q3/ (db F-1715, F-1621, F-1263)
- 한 단계 더: 미국 선물 거래소와 미국 밖 거래소(Deribit 포함)의 요율이 다른가. 회사는 파생 수익을 거래소별로 나누지 않음

## Q3. [3] USDC 준비금 수익은 누가 내서 어떻게 Coinbase까지 오나. 한 바퀴 돌면 Coinbase에 얼마 남나
- 답: 길은 확인됨. 마지막에 남는 몫은 확인 못 함
  - 길: USDC 보유자가 1달러를 맡김 → Circle(발행사)이 그 돈을 단기 국채 등 준비금으로 굴려 이자를 받음 → Circle이 계약에 따라 몫을 Coinbase에 넘김(Circle 장부에는 유통 비용) → Coinbase는 매출(스테이블코인 수익)로 잡고, 앱 안 고객에게 USDC 보상을 줌
  - 숫자: Circle이 2025 Coinbase 관련 유통 비용 14억 달러를 썼다고 매체(CryptoSlate)가 Circle 10-K를 인용해 전함. Coinbase가 잡은 2025 스테이블코인 수익은 13.49억 달러. 이 14억은 Circle 총수익과 준비금 수익의 약 51%
  - (판단) 준비금 이자의 절반 정도가 발행사가 아니라 유통사로 감. 돈을 내는 쪽은 결국 USDC 보유자가 포기한 이자임
- 근거: https://cryptoslate.com/usdc-keeps-winning-but-circles-distributors-are-taking-more-of-the-prize/ (Q2CB-001), Coinbase 2025 10-K https://s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf (db F-2089)
- 답 못 함(보상 금액): Coinbase가 고객에게 준 USDC 보상 총액. 본 곳: 2025 10-K 본문(db F-2084, F-2089), 2026 3분기 서한과 콜. 보상을 비용의 어느 줄에 넣었는지 찾지 못함
- 한 단계 더: Circle 10-K 원문에서 14억을 직접 확인(sec.gov는 이 환경에서 403). 보상을 빼면 USDC 100달러당 남는 돈은 얼마인가

## Q4. [2] 왜 무기한선물(만기 없는 선물)을 미국이 아니라 버뮤다에서 먼저 열었고, 미국에는 언제 들였나
- 답: 2023-05 버뮤다 금융청 인가로 미국 밖 기관에게 먼저 팖. 미국에는 2025-07 CFTC 규제 아래 무기한형 선물을 냈고, 2026-06-11 미국 고객이 세계 무기한선물을 직접 사고팔게 됨
  - 회사가 밝힌 이유: 2022 세계 가상자산 거래대금의 75% 가까이가 무기한선물이었음. 2025 서한은 이 시장에서 미국 비중이 일부에 그친다고 씀
  - (판단) 미국에서는 2025-07 전까지 회사가 낼 수 있는 무기한선물 상품이 없었기 때문에 수요가 있는 미국 밖에서 먼저 연 것
- 근거: https://www.marketsmedia.com/introducing-coinbase-international-exchange/ (db F-1631), https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf (db F-1601), https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/ (db F-1628, 비트코인닷컴 보도)
- 한 단계 더: 미국 무기한형 선물은 버뮤다 상품과 무엇이 다른가(만기, 자금 정산 방식). 미국 규제 문서 원문으로 확인 필요

## Q5. [3] 주식 토큰에서 Coinbase는 무엇으로 돈을 버나. 발행 법인은 이익을 내나
- 답: 발행 법인은 이익을 기대하지 않는다고 설명서에 씀. CFO는 Base 처리 수수료(시퀀서 수수료: 거래 순서를 정하는 Coinbase 서버가 받는 돈)가 가장 직접적인 수익이라고 말함
  - 누가 누구에게: 기관 승인 참여자(AP, 토큰을 새로 만들고 없애는 기관)가 창설 0.01%, 상환 0.05%를 발행 법인에 냄. 보유자는 배당의 5%를 발행 법인에 냄. 발행 법인 운영비는 Coinbase 아일랜드 자회사 대출 한도로 채움
  - 계산(판단): 발행 잔액 4,690만 달러가 모두 새로 창설됐다고 쳐도 창설 수수료는 4,690만 × 0.01% = 약 4,690달러
  - (판단) 주식 토큰 자체로는 거의 돈이 안 남고, Base 위 거래와 USDC 잔액을 늘리는 수단임
- 근거: 설명서 https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf (db F-0089), CFO 발언은 2026 3분기 AMA 녹취 inputs/manual/B03_coinbase_Q3_26_AMA_transcript.pdf (db F-0895), 잔액 https://app.rwa.xyz/stocks (db F-1026)
- 한 단계 더: 2026 3분기 Base 처리 수수료 중 주식 토큰 거래에서 나온 몫. 회사는 Base 수익을 따로 밝히지 않음(G-CB03)

## Q6. [4] 개요는 "거래소 4곳"이라 쓰면서 2026-10 미국 밖 거래소와 Deribit을 합쳤다고 쓴다. 지금 몇 곳인가
- 답: 회사는 2026-10 두 곳을 합쳐 미국과 미국 밖 고객을 잇는 "하나의 규제 글로벌 거래소"가 됐다고 공시함. 법인이나 인가까지 하나로 합쳤는지는 확인 못 함
  - (판단) 상품 기준으로는 3곳(현물 Coinbase Exchange, 미국 선물 Coinbase Derivatives, 합친 미국 밖 파생 거래소), 법인 기준은 여전히 4곳일 수 있음. 개요의 "4곳"은 기준을 밝혀 고쳐야 함
- 근거: 2026 3분기 주주서한 inputs/manual/B03_coinbase_Q3_26_shareholder_letter.pdf (db F-0903)
- 한 단계 더: 합친 거래소는 버뮤다 인가와 두바이 인가 중 어느 것 아래서 미국 기관 주문을 받나

## Q7. [4] 주식 토큰 거래대금이 서한은 "10억 달러 이상", CFO는 "약 30억 달러"다. 어느 쪽인가
- 답: 같은 날(2026-10-29) 회사 자료끼리 숫자가 다름. 회사는 차이를 설명하지 않음
  - (판단) 서한은 Coinbase가 발행한 종목만, CFO는 Base 위 주식 토큰 전체를 말했을 수 있음
  - 그래서(판단): 어느 쪽이든 같은 분기 현물 거래대금 1,345억 달러의 0.7%(10억 기준)에서 2.2%(30억 기준)이고, 출시 이후 누적 숫자라 분기 비중은 더 작음
- 근거: 주주서한 inputs/manual/B03_coinbase_Q3_26_shareholder_letter.pdf (db F-0892), AMA 녹취 inputs/manual/B03_coinbase_Q3_26_AMA_transcript.pdf (db F-1275, F-1274)
- 한 단계 더: IR 담당에게 범위를 묻거나 rwa.xyz 종목별 거래대금으로 맞춰 봄

## Q8. [4] Coinbase One(유료 구독) 이용자 약 100만 명은 MTU 920만 명의 약 11%인데 CFO는 "낮은 퍼센트대"라고 했다. 무엇이 맞나
- 답: 회사 숫자를 나누면 약 11%임(판단). CFO 말과 맞지 않음
  - 계산(판단): 100만 ÷ 920만(2025 연평균 MTU) = 10.9%
  - (판단) CFO가 말한 분모가 MTU가 아니라 더 큰 집단(자산만 맡겨 둔 이용자 등)일 수 있음. CFO는 같은 콜에서 거래한 이용자보다 자산을 맡긴 이용자가 훨씬 많다고 말함
  - 그래서: 구독료는 2025 기타 구독과 서비스 수익 5.55억 달러가 늘어난 주된 이유로 회사가 꼽은 항목임
- 근거: 2026 3분기 애널리스트 콜 녹취 inputs/manual/B03_coinbase_Q3_26_analyst_call_transcript.txt 406~408행 (Q2CB-006), 2025 10-K https://s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf (db F-1379, F-2137)
- 한 단계 더: 구독자 한 명당 거래 수수료가 줄어드는가(구독자는 수수료를 덜 냄). 구독이 거래 수익을 갉아먹는지

## Q9. [4] 미국 가상자산 ETF 자산의 80% 이상을 보관하는데 보관 수수료는 얼마인가
- 답 못 함: 본 곳: 2025 10-K는 보관 수수료를 "기타 구독과 서비스" 5.55억 달러에 묶었고, 그 증가 이유를 Coinbase One이라고 씀(db F-2137). 보관 수수료를 따로 적은 마지막 숫자는 2021의 1.36억 달러(db F-1606). ETF 설명서에서 보관 수수료율도 찾지 못함
  - (판단) 2025 보관 수수료는 5.55억 달러보다 작고, 그 안에서도 가장 큰 항목이 아님. 80% 점유가 큰 매출이라는 뜻은 아님
- 근거: https://s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf , https://s27.q4cdn.com/397450999/files/doc_financials/2021/q4/Coinbase-Q421-Shareholder-Letter.pdf , 점유 https://s27.q4cdn.com/397450999/files/doc_financials/2025/q2/Q2-2025-Shareholder-Letter.pdf (db F-1604)
- 한 단계 더: 보관이 돈이 아니라면 무엇을 주나(판단 후보: ETF 운용사의 매매와 대출을 Prime으로 끌어옴). 회사 설명으로 확인 필요

## Q10. [5] 예측시장에서 Coinbase, Robinhood, Kraken은 무엇을 어떤 순서로 채웠나
- 답: Coinbase와 Robinhood 둘 다 Kalshi(남의 거래소)로 열고 빈 시설을 채웠지만 채운 것이 다름
  - Robinhood: 2025-03 Kalshi로 주문을 넘겨 시작 → 2026-01 거래소와 청산소를 모두 가진 MIAXdx 지분 90% 인수 완료. 거래소와 청산소가 둘 다 없어서 회사째 삼
  - Coinbase: 거래소(2022 FairX)와 중개사(2023)는 이미 있었음 → 2025-12 Kalshi로 열고 같은 달 청산 스타트업 인수 → 2026-09 청산소 직접 등록. 비어 있던 청산만 채움
  - Kraken: 2025-10 선물 거래소 Small Exchange를 1억 달러에 삼. 예측시장 순서는 개요(kb/cards/kraken.md)에 따로 없음
  - (판단) 셋 다 "남의 시설로 수요를 본 뒤 자기 시설"이지만 무엇을 사고 무엇을 직접 받을지는 그때 이미 가진 인가가 정함
- 근거: https://www.coinbase.com/blog/system-update-the-future-of-finance-is-on-coinbase (db F-1376), https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/ (db F-1623), Robinhood와 Kraken은 kb/cards/robinhood.md 72행, kb/cards/kraken.md 67행의 원문 링크
- 한 단계 더: Coinbase는 Kalshi와 수수료를 어떻게 나누나(G-CB04, 이미 확인 못 함으로 남음)

## Q11. [5, 6] Coinbase가 첫 선물을 팔던 외부 중개사 NinjaTrader를 경쟁사 Kraken이 샀다. Coinbase 거래소 주문은 어떻게 됐나
- 답 못 함: 본 곳: 웹 검색(NinjaTrader와 Coinbase Derivatives), Kraken 인수 완료 발표, 파이낸스 매그닛 보도. 인수 뒤 NinjaTrader가 Coinbase 선물을 계속 파는지 밝힌 자료를 찾지 못함
  - 확인된 것: 2022-06-27 Coinbase 첫 선물을 NinjaTrader, Tradovate 등 외부 중개사가 팖. Kraken은 2025-05 NinjaTrader 인수를 마쳤고, 그 뒤 NinjaTrader를 통해 CME(남의 거래소) 가상자산 선물 판매를 엶
  - (판단) KDX에 옮기면: 참여 증권사가 경쟁 거래 시설을 가진 회사에 팔리면 그 증권사 주문이 KDX 대신 그쪽 시설로 갈 수 있음. common.md의 Robinhood 경고 신호와 같은 꼴
- 근거: https://www.financemagnates.com/cryptocurrency/trading/coinbase-to-target-retail-traders-with-first-bitcoin-derivatives/ (db F-2112), https://www.businesswire.com/news/home/20250501627804/en/Kraken-Completes-Acquisition-of-NinjaTrader , https://www.financemagnates.com/cryptocurrency/following-ninjatrader-acquisition-kraken-has-opened-access-to-cme-listed-crypto-futures/
- 한 단계 더: NinjaTrader 상품 목록에 Coinbase Derivatives 상품이 지금도 있는지. Coinbase가 자기 중개사(2023-08)를 받은 뒤 외부 중개사 비중은 얼마인지

## Q12. [6] KDX 자리는 Coinbase 그룹 안 어느 법인이고, 그 법인 혼자 얼마나 버나
- 답: 자리는 Coinbase Derivatives(미국 선물 거래소, 2022 FairX 인수)임(판단, 개요 6절). 그 법인 매출은 답 못 함
- 답 못 함: 본 곳: 2025 10-K(법인별 매출 없음, 거래 수익을 개인, 기관, 기타로만 나눔), 2026 3분기 서한과 콜. 찾은 규모 숫자는 2026 1분기 전통 상품선물(금, 은 등) 명목 거래대금 520억 달러 초과뿐(비트코인닷컴 보도)
  - (판단) Q2의 파생 요율 약 0.01%를 520억 달러에 곱하면 분기 약 520만 달러 수준. 가정이 큰 추정이라 장표에 쓰지 않음
- 근거: https://news.bitcoin.com/coinbase-24-7-gold-silver-futures-us/ (db F-1628), https://s27.q4cdn.com/397450999/files/doc_events/2026/Jun/16/Coinbase-Global-Inc-2025-Annual-Report.pdf
- 한 단계 더: CFTC에 내는 거래소 재무 보고나 거래소 수수료표(계약당 수수료)에서 법인 규모를 거꾸로 구할 수 있나

## Q13. [6] Coinbase 주식 토큰 구조를 한국에 옮기면 누가 어느 자리인가
- 답(판단): 한국 개정 전자증권법(2026-02-03 공포, 2027-02-04 시행)은 분산원장(블록체인 장부)에 증권을 등록하는 틀과 "발행인계좌관리기관"(자기가 발행하는 증권을 직접 등록하는 발행인)을 둠. 이 틀에서는 발행은 발행인, 판매와 계좌는 증권사, 체결은 거래 시설(KDX)이 맡게 됨
  - Coinbase 구조와의 차이(판단): Coinbase는 발행 법인만 두고 판매 창구가 없으며 체결은 Base 위 남의 탈중앙 거래소에서 일어남. KDX 구조는 그 반대로 판매(증권사)와 체결(KDX)이 중심임. 그래서 옮길 수 있는 것은 Coinbase의 발행과 보관 짝(Alpaca) 쪽이지 체결 방식이 아님
- 근거: https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=283195&efYd=20270204 (db laws KR-전자증권법-2(8), 2(3의2)), Coinbase 밸류체인은 kb/cards/coinbase.md 3절
- 한 단계 더: 한국 투자자가 Coinbase 주식 토큰을 살 수 있나(Q17), 한국 법에서 Base 같은 공개 블록체인 장부를 쓸 수 있나(시행령 확인)

## Q14. [2, 7] USDC 계약은 2026-08 첫 3년이 끝났다. 어떻게 됐고 Coinbase는 왜 경쟁 스테이블코인에도 들어갔나
- 답: 기존 조건 그대로 3년 갱신돼 2029까지 감. Circle이 2026-08-05 2분기 실적 콜에서 밝힘(crypto.news 보도). 계약은 양쪽이 의무를 지키면 3년씩 자동 갱신됨
  - 같은 해 Coinbase는 Visa, Mastercard 등 140곳 넘는 회사가 만든 경쟁 스테이블코인 모델 Open USD에도 참여함(CryptoSlate 보도). Open USD는 운용 수수료를 뗀 뒤 준비금 수익을 참여사와 나눔
  - Coinbase가 밝힌 참여 이유는 찾지 못함. (판단) 다음 갱신(2029) 협상에서 Circle에 내밀 비교 기준을 쥔 것
  - 그래서: 2025 총매출의 19%가 한 거래 상대에서 나왔음(개요는 Circle로 판단). 2029까지는 이 몫이 계약으로 보장됨
- 근거: https://crypto.news/circle-renews-coinbase-usdc-deal-rules-out-dividends/ (Q2CB-002), https://cryptoslate.com/usdc-keeps-winning-but-circles-distributors-are-taking-more-of-the-prize/ (Q2CB-004), Coinbase 2025 10-K (db F-2087)
- 한 단계 더: Circle 10-K의 계약 첨부에서 갱신과 해지 조건 원문 확인(sec.gov 403이라 Circle IR에서 찾음)

## Q15. [7] Coinbase가 한국에 들어오면 KDX와 부딪치나
- 답: 아직 들어온 것은 없음. 2026-01 Coinbase가 코인원 지분 투자를 검토한다는 국내 보도가 있었으나 Coinbase는 논평을 거부했고 거래는 발표되지 않음. 2026-05에는 OKX가 한국투자증권과 함께 코인원 지분을 논의한다는 연합뉴스 보도가 나옴(코인텔레그래프가 전함, 확정 아님)
  - (판단) 해외 거래소가 한국에 들어올 때 증권사와 짝을 짓는 꼴이 보도됨. KDX 참여 증권사가 해외 거래소와 손잡으면 그 증권사 주문이 KDX 대신 그쪽으로 갈 수 있음(Q11과 같은 위험)
  - 한국 규제(판단): 가상자산 거래소는 가상자산법, KDX는 자본시장법 아래라 같은 상품을 두고 바로 부딪치지는 않음. 주식 토큰처럼 증권인 상품을 들여오려면 증권 쪽 인가가 따로 필요함
- 근거: https://cointelegraph.com/news/coinone-south-korea-sale-coinbase-investment-speculation (db F-0114), https://cointelegraph.com/news/okx-reportedly-eyeing-south-korea-move-with-coinone-stake (Q2CB-005). 코인원 부인 보도(BeInCrypto)는 403이라 열지 못함
- 한 단계 더: 2026-05 뒤 코인원 지분 거래가 계약까지 갔나. 한국 증권사가 해외 가상자산 거래소와 맺은 다른 협약이 있나

## Q16. [7] Coinbase Pro 재출시(현물, 선물, 옵션, 주식을 한 계좌 증거금으로)가 되면 KDX에 무엇이 바뀌나
- 답(판단): 한 계좌 증거금은 고객이 주식을 담보로 가상자산 선물을 사는 식으로 담보를 돌려 쓰게 하는 것임. 그러려면 판매, 체결, 청산이 한 그룹 안에 있어야 함. Coinbase는 증거금 선물 청산을 아직 외부(Nodal Clear)에 맡기고 있어 이 계획이 그 청산을 안으로 가져올지가 관건임
  - KDX에 옮기면(판단): KDX는 판매와 계좌를 참여 증권사가 갖는 구조라 한 계좌 증거금을 KDX가 직접 줄 수 없음. 고객 담보를 묶는 일은 증권사와 청산 기관이 해야 함. 해외에서 한 계좌 증거금이 표준이 되면 KDX 상품의 담보를 증권사 계좌 안 다른 자산과 함께 인정받는 길을 미리 정해야 함
- 근거: 계획은 2026 3분기 애널리스트 콜 녹취 inputs/manual/B03_coinbase_Q3_26_analyst_call_transcript.txt 216행과 AMA 녹취 354행(Coinbase Pro 이름으로 다시 냄). 청산 구조는 https://www.marketsmedia.com/coinbase-clearing-receives-cftc-approval/ (db F-1623)
- 한 단계 더: 재출시가 2026 4분기 안에 실제로 나왔나(출시일 확인), 증거금 선물 청산을 Coinbase Clearing으로 옮기는 인가 신청이 있나

## Q17. [6, 7] 한국 투자자는 Coinbase 주식 토큰을 살 수 있나. 미국 출시(SEC 혁신 면제 뒤)가 되면 무엇이 바뀌나
- 답 못 함(한국 판매): 본 곳: base.org/stocks, 설명서 NVDAc.pdf 일부(db F-0089, F-0740), kb/cards/coinbase.md. 미국인 제외는 확인했으나 판매 제한 국가 목록에서 한국 여부는 찾지 못함
- 미국 출시: CFO는 지금 미국 상품이 없고 SEC 혁신 면제(신기술 상품 예외 제도) 아래 할 것을 찾는 중이며, 같은 유동성을 미국과 미국 밖에 함께 주려면 추가 규제 승인이 필요하다고 말함
  - (판단) 미국 출시가 되면 미국 주식 토큰의 유동성이 미국 안팎 한 곳에 모임. 한국 투자자가 해외 앱에서 미국 주식 토큰을 바로 사는 길이 넓어지면 KDX가 해외 자산 토큰으로 경쟁할 여지는 줄고, 한국 자산을 해외에 내보내는 쪽(common.md 공통 결론 2)이 더 중요해짐
- 근거: 2026 3분기 애널리스트 콜과 AMA 녹취 inputs/manual/B03_coinbase_Q3_26_analyst_call_transcript.pdf (db F-1267), https://api.coinbase.com/v1/tokenized-stocks/prospectus/NVDAc.pdf
- 한 단계 더: 설명서의 판매 제한 절을 끝까지 읽어 한국 여부 확인

---

## 새로 찾은 사실
- work/Q2-CB/facts.csv(Q2CB-001부터 006), work/Q2-CB/sources.csv(Q2CB-S01부터 S05)
- 매체 보도로만 확인한 것: Circle의 Coinbase 유통 비용 14억 달러(2025), 계약 갱신(2026-08), Open USD 참여, OKX와 한국투자증권의 코인원 논의. Circle 10-K와 계약 원문은 sec.gov 403으로 열지 못함
