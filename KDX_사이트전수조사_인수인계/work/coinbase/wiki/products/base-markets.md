# Base Markets: 주식 시장 지표와 DeFi 연동

확인일: 2026-11-16. 모든 수치는 Base Markets 페이지 표기이고 기준일은 2026-11-15 UTC이다. 산정 방식은 페이지에 정의가 없고, 렌딩은 Aave V4 금리와 유동성만 실시간, 나머지는 일일 스냅샷이다. [출처](https://www.base.org/markets/stocks/mstrc)

## 전체 지표
- 24시간 주식 거래량 $131.68M, 7일 평균 $162.10M, 전체 공급액 $6.94B, 전체 차입액 $2.54B. [출처](https://www.base.org/markets/stocks)
- 전체 주식 표에 45개 종목. 열: 토큰 가격, 거래 유동성, $10K 주문 시 영향, 담보 사용 금액. [출처](https://www.base.org/markets/stocks)
- 거래 유동성 $1.98M(NVIDIA 행)이고, Hesai(HSAIc)의 $10K 주문 영향이 97.51%로 표 최대. [출처](https://www.base.org/markets/stocks)
- NVDAc 거래 경로는 Coinbase Wallet, Aerodrome, 01 exchange, Matcha, 0x 등 13개 연결. [출처](https://www.base.org/markets/stocks)

## 종목별(예시)
- NVDAc: 24시간 거래량 $12.45M, 온체인 시가총액 $7.75M, Aave V4 담보 사용 $3.09M. 3.02% 수익률은 USDC 보상이며 보상 종료일 2026-11-19. [출처](https://www.base.org/markets/stocks/nvdac)
- AMZNc: 24시간 거래량 $6.88M, 온체인 시가총액 $2.07M, AMZNc/USDC 풀 유동성 $1.74M. [출처](https://www.base.org/markets/stocks/amznc)
- GOOGLc: 24시간 거래량 $6.81M, 온체인 시가총액 $10.48M, Aave V4 담보 사용 $6.10M. [출처](https://www.base.org/markets/stocks/googlc)
- METAc, MSTRc, AAPLc, MSFTc, AVGOc 등은 facts.csv 참조. [출처](https://www.base.org/markets/stocks/metac)
- MAG7은 개별 주식이 아니라 Reserve Magnificent 7 DTF이고 표시 발행자는 Reserve. [출처](https://www.base.org/markets/stocks/mag7)

## 담보와 전략
- 담보 대출 시장이 없는 종목이 많다(MSTRc, MUc, PLTRc 등). [출처](https://www.base.org/markets/stocks/mstrc)
- 예치 전략: Makina Dialectic Yielding, Superform SuperVault, IPOR Fusion Carry Trade, Morpho vault 등. 수익률은 보상 제외이며 보장되지 않는다. [출처](https://www.base.org/markets/stocks/amznc)
- 담보는 기초 주식 시장이 닫혀 있을 때도 청산될 수 있다. [출처](https://www.base.org/markets/stocks/mstrc)
- Base는 Morpho, Aave 등 일부 프로토콜과 상업적 관계가 있다고 밝힌다. [출처](https://www.base.org/markets/stocks/mstrc)
- 소액 풀의 수익률은 극단적이다(AMDc Beefy LP 110.27%, 예치 $1.29K). [출처](https://www.base.org/markets/stocks/amdc)
