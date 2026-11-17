# Binance: PM이 개요를 읽고 다음에 물을 질문

- 읽은 것: kb/cards/binance.md(개요). 이미 물은 것(녹취 Binance 43~48, 셀프 챌린지 6~8)은 뺌
- KDX 구조: 참여 증권사가 고객과 계좌를 갖고, KDX는 증권사가 넘긴 주문을 받아 체결하는 거래 시설
- 각도: [1] 숫자의 함의 [2] 왜 그것을, 왜 그때, 왜 그 방식 [3] 누가 누구에게 무엇을 주고 누가 돈을 내나 [4] 문서 안 모순과 빈 곳 [5] 다른 회사와 비교 [6] KDX에 옮기면 [7] 앞으로
- 모두 2026-11-17 기준. 새로 찾은 사실은 work/Q2-BN/facts.csv(Q2BN-001~003)

## PM이 가장 먼저 물을 3개
1. **Q1**: "뭘로 돈 벌어?"를 숫자로 다시 묻는 질문임. 매출 추정 두 개가 3배 넘게 다른데, 거래대금으로 나누면 어느 쪽이 말이 되는지 바로 보임
2. **Q5**: "누가 돈을 내?"의 정면 질문임. 발행 비용 0, 상환 수수료 0인 상품에서 비용을 누가 대는지 답하지 못하면 bStocks 구조 설명이 반쪽임
3. **Q11**: 개요 6칸이 KDX에 가져올 것 첫째로 든 "시장조성자 수수료 조건"이 한국 장외거래소에서 되는지는 KDX 적용 한 줄의 전제임

## 질문과 답

**Q1. [1] 2025 거래대금 34조 달러에 매출 추정을 나누면 거래 1달러당 얼마를 받은 셈인가? 표준 수수료와 비교하면 무엇이 보이나?**
- 답: (판단) Forbes 추정 165억 달러(160억에서 170억의 가운데) ÷ 34조 달러 = 약 0.049%, 창업자 주장 50억 달러 ÷ 34조 달러 = 약 0.015%. 2018 표준 현물 수수료 0.1%로 34조 달러를 다 받았다면 340억 달러(34조 × 0.1%)라, 두 추정 모두 그 절반 아래임. 거래대금 대부분이 표준보다 낮은 요율(파생 요율, 거래량 많은 고객의 VIP 할인, 시장조성자 요율)로 체결됐다는 뜻임
- 근거: 거래대금 https://www.binance.com/en/blog/ecosystem/7330669344678014164 (기존 DB F-1387). Forbes 추정 https://www.billionaires.africa/2026/10/05/binance-founder-changpeng-zhao-says-hes-worth-far-less-than-100-billion/ . 창업자 주장 https://www.ibtimes.co.uk/binance-founder-cz-wealth-dispute-valuation-gap-1805574 . 0.1% 요율은 기존 DB F-1822(2018 이용 안내)
- 한 단계 더: 선물 기본 요율(매체 정리로는 호가를 내는 쪽 0.02%, 호가를 가져가는 쪽 0.05%, binance.com 원문은 봇 확인으로 못 엶)을 1차 자료로 확인하면 "매출 50억 달러"와 "165억 달러" 중 어느 쪽이 34조 달러와 맞는지 좁힐 수 있음

**Q2. [1] bStocks 운용자산 10억 달러에 누적 거래 400억 달러면 무엇이 보이나?**
- 답: (판단) 400억 ÷ 10억 = 40. 넉 달 동안 잔고가 평균 40번 넘게 손바뀜함(잔고가 0에서 늘어 온 것을 생각하면 실제 회전은 더 큼). 들고 있는 상품이 아니라 사고파는 상품이고, 발행과 상환 수수료가 0이라 Binance 돈은 거래 수수료에서만 나옴. 거래의 62%가 미국 정규장 밖이라, 주식을 사기 어려운 시간의 거래 수요가 이 상품의 핵심임
- 근거: 누적 거래 400억 달러, 운용자산 10억 달러, 정규장 시간 거래 38% https://www.prnewswire.com/news-releases/binances-bstocks-become-the-fastest-tokenized-equity-product-to-surpass-1-billion-in-assets-under-management-302909927.html (기존 DB F-0058, F-0061)
- 한 단계 더: 같은 회전율을 Kraken xStocks(발행 잔액 6.8억 달러)와 비교. 회전이 높은 쪽이 거래 시설 입장에서 더 좋은 상품임

**Q3. [1][4] 현물 점유율이 2022 약 60%에서 2026-10 26.4%로 반 아래가 됐다. "1등"이라는 말은 무엇의 1등이고, 그동안 무슨 일이 있었나?**
- 답: 2024-09 현물 점유율은 27%로 2020-09 뒤 가장 낮았고 같은 달 파생은 약 41%였음(CCData 보고서를 인용한 Decrypt 보도). 지금도 현물과 파생 모두 1위지만, 2022처럼 혼자 절반 넘게 가진 1위가 아니라 4분의 1 수준의 1위임. (판단) 2022 값은 2023 미국 합의 전 숫자이고, 점유율이 줄어든 시기는 2023 미국 합의와 각국 규제 압박 이후와 겹침
- 근거: https://decrypt.co/284631/binances-market-dominance-slips-lowest-point-four-years-regulatory-headwinds (Q2BN-001). 2022 약 60%는 미국 재무부 금융범죄단속국 명령(기존 DB F-1830)
- 한 단계 더: 2022의 약 60%가 수수료 0 거래 이벤트 기간의 숫자인지 CCData 원문으로 확인. 그렇다면 60%는 실력보다 부풀려진 값임

**Q4. [2] 미국 주식은 왜 직접 체결하지 않고 Alpaca에 맡겼고, bStocks는 왜 직접 발행했나?**
- 답: 회사는 이유를 밝히지 않음. (판단) 미국 상장 주식을 미국 시장에서 집행하고 보관하려면 미국 증권사 자리가 필요한데 Binance 그룹 글로벌 플랫폼은 미국 인가가 없음(미국 이용자는 별도 법인 Binance.US). 그래서 미국 안에서 해야 하는 집행, 청산, 보관은 Alpaca에 맡기고, 그룹이 인가를 가진 아부다비에서 할 수 있는 일(주문 접수, 토큰 발행, 상장, 청산)은 직접 함. 6개사 중 5곳이 같은 Alpaca를 씀
- 근거: 미국 주식 출시 구조 https://www.aap.com.au/aapreleases/cision20260601ae72536/ (기존 DB F-1198). bStocks 발행 구조 https://bin.bnbstatic.com/static/assets/equity/adgm/366449/btech-holdings-prospectus---moderna-bstocks-20260901_09_01_2026_15-36-13.pdf
- 한 단계 더: Alpaca가 막히면 대체가 있나. 투자설명서는 Alpaca 도산 위험을 "높음"으로 적음(한 곳 의존)

**Q5. [3] bStocks 발행사 비용 0, 상환 수수료 0이면 발행사 운영비와 첫 물량은 누가 대나? 돈과 주식이 한 바퀴 도나?**
- 답: 발행사는 증서 발행으로 현금을 받지 않을 것으로 보고 비용은 그룹 청산 법인(Nest Clearing and Custody)이 준 500만 달러 한도 대출로 내며, 첫 물량은 같은 청산 법인이 Alpaca에서 빌린 주식으로 찍음. 한 바퀴: 이용자 USDT → Nest Trading이 Alpaca에서 주식을 삼 → 발행사 분리 계좌에 입고 → 토큰화 운영사(BTech Services)가 증서를 찍음 → 이용자. (판단) 그룹이 발행 비용을 대신 내고 거래소 거래 수수료로 거둬들이는 구조임
- 근거: 투자설명서 https://bin.bnbstatic.com/static/assets/equity/adgm/366449/btech-holdings-prospectus---moderna-bstocks-20260901_09_01_2026_15-36-13.pdf (기존 S2BN-002, S2BN-007, S2BN-012)
- 한 단계 더: bStocks 거래 수수료율(빈칸 G-BN04)과 Alpaca 주식 대여료. 둘을 알아야 이 상품이 그룹에 남기는 돈을 셀 수 있음

**Q6. [3][5] 미국 주식 수수료가 0이면 Binance는 무엇으로 버나? Robinhood는 주문을 시장조성자에게 넘기고 대가를 받는데, Binance도 그런가?**
- 답 못 함: 본 곳: 2026-06-01 미국 주식 출시 발표(수수료 0만 있음), 2026-09-01 옵션 출시 발표, ADGM 약관(수수료, 커미션, 스프레드, 금융 수익을 받을 수 있다고만 적음), bStocks 투자설명서. Binance가 받는 몫과 Alpaca와 나누는 돈은 어디에도 없음(빈칸 G-BN05). (판단) 후보는 USDT와 달러 사이 전환 차이, 주식 대여 수익, 같은 계정의 파생 거래로 넘어가는 이용자이나 모두 확인 전
- 근거: https://www.aap.com.au/aapreleases/cision20260601ae72536/ , https://www.prnewswire.com/news-releases/binance-adds-us-stock-options-to-its-multi-asset-platform-302866167.html
- 한 단계 더: Alpaca가 파트너 회사에 받는 요금이나 나누는 몫을 밝힌 자료(Alpaca 쪽 공개 문서)

**Q7. [4] 머리 줄은 "체결, 청산, 보관을 한 그룹이 모두 한다"는데, 표를 보면 미국 주식과 옵션은 Alpaca가 집행, 청산, 보관한다. 어느 쪽이 맞나?**
- 답: 범위가 다름. "한 그룹이 모두"는 가상자산 현물과 파생, bStocks에만 맞음. 미국 주식과 옵션에서 Binance 자리는 주문 접수(Nest Trading)뿐이고 집행, 청산, 보관은 Alpaca가 함. 주식 가격 파생은 발표에 거래소(Nest Exchange)만 적혀 청산 법인이 비어 있음(빈칸 G-BN06). (판단) 머리 줄은 "가상자산과 bStocks는 한 그룹이 다 하고, 미국 주식은 주문만 받아 Alpaca에 넘김"으로 고쳐야 함
- 근거: https://www.aap.com.au/aapreleases/cision20260601ae72536/ (F-1198), https://www.prnewswire.com/news-releases/binance-adds-us-stock-options-to-its-multi-asset-platform-302866167.html (F-1541), https://www.prnewswire.com/news-releases/binance-launches-first-regulated-tradfi-perpetual-contracts-settled-in-stablecoin-starting-with-gold-and-silver-302656186.html (F-1540)
- 한 단계 더: 주식 가격 파생의 청산 법인. ADGM 등록부에서 Nest Clearing and Custody 인가 범위에 이 계약이 들어가는지

**Q8. [4][1] "돈의 중심은 파생 수수료"의 핵심 근거인 파생 점유율 46.4%는 원문을 아직 못 열었다고 적혀 있다. 이 숫자 없이도 그 판단이 서나?**
- 답: (판단) 섬. 회사 블로그 숫자만으로 2025 거래대금 34조 달러 중 현물 밖이 26.9조 달러(34조 − 7.1조), 약 79%임. 다만 파생 요율이 현물보다 낮다면(Q1 매체 정리 기준) 거래대금 비중 79%가 곧 매출 비중 79%는 아님. 매출에서 파생 몫은 79%보다 작을 수 있음
- 근거: https://www.binance.com/en/blog/ecosystem/7330669344678014164 (F-1387). 46.4%는 https://www.coindesk.com/research/exchange-review-october-2026 (F-1701, 원문 미열람)
- 한 단계 더: 현물과 선물 요율을 1차 자료로 확인해 매출 비중을 거꾸로 셈(현물 거래대금 × 현물 요율 대 파생 거래대금 × 파생 요율)

**Q9. [5] Coinbase는 사고팔기 밖에서 버는 돈(USDC 몫, 스테이킹 등)이 41%다. Binance에도 이런 몫이 있나?**
- 답: 금액은 비공개. 약관상 계열사가 상장 자산을 들고 헤지하고 빌려주며 금융 수익을 얻을 수 있고, 이용자가 맡긴 자산은 1,628억 달러(2025 말)임. 그러나 Binance 이름을 단 스테이블코인 BUSD는 2023 초 발행사 Paxos가 뉴욕 금융감독청 지시로 새 발행을 멈춰, Coinbase의 USDC 몫 같은 이자 수입 자리는 확인되지 않음. (판단) Binance는 Coinbase보다 거래 수수료 한 축에 더 기대고, 그래서 거래가 식으면(2026-07 중앙화 거래소 합산 거래대금이 2023-11 뒤 최저) 더 크게 흔들림
- 근거: 약관(기존 DB F-1289, inputs/manual/Binance_ADGM_Terms_of_Use_20261027.pdf). BUSD(기존 DB F-1243). 거래 감소 https://data.coindesk.com/reports/exchange-review-july-2026
- 한 단계 더: 이용자 예치 1,628억 달러 중 Earn(예치 상품)에 묶인 몫과 그 이자 차이. 이것이 Binance판 "맡긴 자산 수입"임

**Q10. [5] Kraken은 자기 체결과 보관 기능을 다른 금융회사에 팔아 이용료를 받는다(Payward Services). Binance에도 남의 회사가 주문을 넘기는 사업이 있나?**
- 답 못 함: 본 곳: kb/cards/binance.md, db/facts.csv의 Binance 줄 206건, 이번 검색. 다른 증권사나 앱이 Binance 호가창에 주문을 넘기고 수수료를 나누는 사업은 이 저장소 자료에서 확인되지 않음. (판단) 있다면 6개사 비교에서 KDX 구조(참여사가 주문을 넘기는 거래 시설)와 가장 가까운 Binance 조각이 됨
- 근거: 비교 대상 Kraken은 kb/cards/common.md 4칸(Payward Services)
- 한 단계 더: Binance의 브로커 프로그램(다른 앱이 Binance 호가창에 주문을 넘기는 계약)이 있는지, 누가 누구에게 수수료를 나누는지 1차 자료로 확인

**Q11. [6] Binance VIP처럼 거래량 큰 고객과 시장조성자에게 수수료를 깎아 주는 방식이 KDX(한국 장외거래소)에서 되나?**
- 답: (판단) 된다면 할인 상대가 다름. Binance VIP는 거래소가 최종 고객과 직접 계약해서 됨. KDX는 고객과 계약하지 않으므로 KDX가 깎아 줄 수 있는 상대는 주문을 넘기는 참여 증권사(증권사 단위 거래량 구간 요율)와 KDX가 지정하는 시장조성자(호가 의무와 짝지은 요율)임. 수수료 차등을 막는 조항은 이번에 확인하지 못했고, 장외거래소 예비인가 심사 항목에 이해상충 방지체계가 들어 있었음
- 근거: KDX 예비인가(2026-02-13 금융위 정례회의 의결, 725점)와 심사 항목 https://www.blockmedia.co.kr/archives/1046635 (Q2BN-002)
- 한 단계 더: 장외거래중개업 규정과 KDX 업무규정 안의 수수료, 시장조성 조항. KRX 시장조성자 제도(수수료와 거래세 혜택)가 장외거래소에도 적용되는지

**Q12. [6] Binance는 발행사(BTech), 거래소(Nest Exchange), 발행 상환 창구(Nest Trading)를 한 그룹에 둔다. KDX도 이렇게 할 수 있나?**
- 답: 안 됨. 금융위는 2022-04 가이드라인부터 발행과 유통을 나누는 원칙을 두고, 발행 전용 인가와 장외거래소 인가를 따로 만들었음. (판단) KDX에 옮기면 BTech 자리는 별도 발행인, Nest Trading 자리(고객 주문 접수, 발행 상환 창구)는 참여 증권사, KDX는 Nest Exchange 자리(체결)만 맡음
- 근거: https://www.blockmedia.co.kr/archives/1046635 (Q2BN-002, 금융위 보도자료 원문은 미열람)
- 한 단계 더: Binance 투자설명서가 같은 그룹 안 발행사와 거래소의 이해상충을 어떻게 막는다고 적는지. 한국 규제가 걱정하는 것과 같은 지점임

**Q13. [6] bStocks 제한 지역 목록에 한국이 없다. 한국 투자자가 Binance에서 bStocks를 사면 KDX와 경쟁이 되나?**
- 답: (판단) 목록에 없다고 한국인에게 팔 수 있는 것이 아님. 한국은 해외 사업자도 국내 이용자 대상 영업이면 신고 의무가 있고, 금융정보분석원은 2026-10 미신고 해외 거래소 등 27곳의 국내 접속을 막음(Binance는 보도된 이름에 없음). Binance의 한국 통로는 인수한 고팍스뿐이고 고팍스는 Binance 호가창 공유와 파생을 못 함. 그래서 지금 한국 투자자 대상 bStocks 판매는 확인되지 않고 직접 경쟁은 아님
- 근거: https://biz.sbs.co.kr/amp/article/20000339576 (Q2BN-003). 고팍스 제약 https://news.bizwatch.co.kr/article/mobile/2025/10/16/0036 (F-1553). 제한 지역 목록은 투자설명서(S2BN-013)
- 한 단계 더: 해외 증권(bStocks는 증권 증서)을 한국 거주자에게 파는 것이 자본시장법상 국내 인가 없이 되는지. 가상자산 신고와 별개 문제임

**Q14. [7] bStocks를 거래에서 증거금과 헤지로 넓히면(2026-09 증거금 허용, 2026-10 확대 계획 발표) 무엇이 바뀌고, KDX에는 무엇이 바뀌나?**
- 답: (판단) 토큰이 사고파는 대상에서 담보로 바뀌면 잔고가 쌓이고(Q2의 회전 40배 상품이 들고 있는 상품이 됨), 담보 가치를 매길 가격이 24시간 필요해짐. KDX에 옮기면 담보 인정과 신용은 고객 계좌를 가진 참여 증권사 일이고, KDX 몫은 담보 평가에 쓰일 가격(특히 기초 시장이 닫힌 시간의 체결 가격 기준)을 내는 것임
- 근거: 회사 발표(기존 개요 2칸 "다음", 1차 링크는 기존 DB F-1287 계열 보도자료) https://www.prnewswire.com/news-releases/binances-bstocks-become-the-fastest-tokenized-equity-product-to-surpass-1-billion-in-assets-under-management-302909927.html
- 한 단계 더: 증거금으로 인정할 때 깎는 비율(담보 인정률)과, 미국 휴장 시간 가격 제한폭(직전 종가에서 약 20%)이 담보 평가에 쓰이는지

**Q15. [7][2] Binance가 미국 밖 주식(예: SK하이닉스)으로 bStocks를 넓히면 기초 주식을 사서 맡는 짝은 누구인가?**
- 답: (판단) 지금 bStocks 기초는 미국 주식뿐이고, 미국 밖 주식으로 넓힌다는 계획은 찾지 못함. SK하이닉스는 지금 주식을 들지 않는 무기한선물(SKHYNIXUSDT, 2026-11-17 화면 거래대금 10.5억 달러)로만 팖. 주식 토큰으로 내면 Alpaca 자리를 한국 주식을 외국인 몫으로 사서 보관할 한국 증권사가 맡아야 함. 이것은 해외 투자자에게 한국 자산을 파는 일이라, 국내 투자자에게 주문을 받는 KDX 장과는 다른 사업임
- 근거: https://www.binance.com/en/markets/futures (기존 DB F-1238, 화면 값). 기초 보관 구조는 kb/cards/common.md 공통 결론 2
- 한 단계 더: SKHYNIXUSDT 거래대금의 이용자 지역 구성. 해외 수요가 크면 한국 증권사와 KDX에 "한국 주식 원주를 맡는 짝" 자리가 생김

## 답 못 한 질문
- Q6(수수료 0 주식에서 Binance가 버는 몫), Q10(남의 회사가 Binance에 주문을 넘기는 사업). 2건
