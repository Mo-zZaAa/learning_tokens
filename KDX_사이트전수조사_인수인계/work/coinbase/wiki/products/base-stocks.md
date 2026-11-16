# 핵심 상품: Coinbase Tokenized Stocks (Base)

확인일: 2026-11-16. 사이트가 설명하는 내용이다. 투자설명서와의 대조는 open-questions.md에 있다.

## 상품 한 줄
- 개별 미국 기업 주식을 온체인으로 가져온 토큰이다. 사이트는 "Coinbase가 발행하고 규제된 보관의 주식으로 1:1 뒷받침"된다고 표기한다. [출처](https://base.org/stocks)
- 각 토큰은 Coinbase와 분리된 규제, 파산 격리 보관의 실제 주식에 대한 수익적 청구권이라고 표기한다. [출처](https://base.org/stocks)
- 다른 페이지에서는 "토큰 보유자가 기초 주식에 대한 직접적이고 선순위인 청구권을 가진다"고 쓴다. 두 표현의 차이는 open-questions.md 충돌 2번이다. [출처](https://base.org/stocks)
- Apple, NVIDIA 같은 기업의 분할 주식을 제공한다고 블로그가 언급한다. [출처](https://www.base.org/blog/tokenized-stocks)
- 문서가 Chainlink 피드가 있는 종목으로 나열한 것은 10개(AAPL, AMZN, GOOGL, META, MSFT, MSTR, NVDA, SNDK, SPCX, TSLA)이다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- 블로그는 향후 몇 주 안에 종목이 추가될 것이라고 적었다(2026-08-24 글). [출처](https://www.base.org/blog/tokenized-stocks)

## 발행 주체와 Base의 역할
- 발행 주체 표기: "issued by Coinbase". 법인명 없음. [출처](https://base.org/stocks) [출처](https://www.base.org/blog/tokenized-stocks) [출처](https://www.base.org/blog/request-for-builders-tokenized-stocks)
- Base는 이 토큰을 발행, 판매, 보증하지 않으며(하단 면책), 토큰화 증권을 발행, 제공, 수탁, 시장 조성하지 않는다고 적었다. [출처](https://base.org/stocks) [출처](https://www.base.org/blog/tokenized-stocks)
- 토큰은 Base에서 B20 토큰으로 발행되어 자기보관 지갑에 보관된다. [출처](https://base.org/stocks)

## 대상 고객과 지역 제한
- 미국 외 적격 관할 지역에서만 이용 가능. 미국과 기타 제한 관할의 사람에게는 제공되지 않는다. 어떤 관할이 적격인지 목록은 읽은 페이지에 없다. [출처](https://base.org/stocks)
- Regulation S에 따라 제공되며 모든 시장에서 이용 가능하지는 않다. [출처](https://base.org/stocks)
- 대상: 적격 관할의 비미국 사용자 중 인터넷 연결과 지갑이 있는 사람. [출처](https://www.base.org/blog/tokenized-stocks)

## 발행과 상환(1차 시장)
- 1차 발행과 상환은 KYC를 마친 기관 파트너와 Authorized Participants로 제한된다. [출처](https://base.org/stocks)
- AP는 기관 마켓메이커로 주식을 사서 Alpaca(규제 브로커 겸 수탁기관)로 보낸다. 이 구조는 ADGM 규제기관 감독을 받는다고 블로그가 쓴다. [출처](https://www.base.org/blog/tokenized-stocks)
- 2차 시장 보유와 거래는 허가 없이 가능하고 KYC는 AP의 민팅과 상환 흐름에서만 일어난다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)

## 배당과 분할
- 배당과 분할은 토큰 수량이 아니라 온체인 배수로 반영된다. 발행 시 배수는 1.00. [출처](https://base.org/stocks) [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 현금 배당은 현금으로 지급되지 않고, 원천징수세와 Coinbase 수수료를 뺀 뒤 추가 주식에 재투자되어 배수가 오른다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base) [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 기업행위 중에는 민팅과 상환이 오프체인에서 멈추지만 토큰 전송은 막히지 않는다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)

## 거래
- 주말과 미국 공휴일을 포함해 언제든 거래 가능. AMM 풀에서 24시간 거래된다고 블로그가 설명. [출처](https://base.org/stocks) [출처](https://www.base.org/blog/tokenized-stocks)
- 가격 피드는 Chainlink(24/5 운영, 주말과 휴일에는 마지막 종가 유지). 24시간 거래와 피드 운영 시간의 관계는 open-questions.md. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- 거래 장소와 컨트랙트 주소 목록은 base.org/stocks에 있다고 블로그가 안내한다. [출처](https://www.base.org/blog/tokenized-stocks)
- Aave 담보 대출에 쓸 수 있다고 하며 세부는 [base-markets.md](base-markets.md). [출처](https://www.base.org/blog/tokenized-stocks)

## 수수료
- 배당 재투자 시 원천징수세와 Coinbase 수수료를 차감한다. 수수료율은 읽은 페이지에 없다. [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)

## 투자설명서
- Base Markets 각 종목 페이지가 종목별 투자설명서(Prospectus) PDF 링크를 제공한다. 이 조사에서는 링크만 확인했다. [출처](https://www.base.org/markets/stocks/nvdac)
