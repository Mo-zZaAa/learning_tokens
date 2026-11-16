# notes: docs.ondo.finance__ondo-stocks__02.md

## https://docs.ondo.finance/ondo-stocks/secondary-market-restrictions
- [지역제한] 2차 시장에서 토큰을 취득하는 사람은 자신이 금지 대상자가 아니라는 점을 인정해야 한다.
  근거: "they are not then prohibited from acquiring Tokens"
- [구조] 발행사는 2차 시장이 존재하거나 앞으로도 존재할 것을 보장하지 않는다.
  근거: "The Issuer does not guarantee that any secondary market exists or will exist for the Tokens"
- [구조] 발행사는 2차 시장에서의 토큰 가격에 대해 어떤 표명도 하지 않는다.
  근거: "makes no representation as to the price of any Token"
- [고객] 토큰 상환에는 KYC가 조건이며, 발행사는 법규 위반 가능성이 의심되면 상환을 거절할 수 있다.
  근거: "the Issuer may refuse any redemption to a holder of any securities if the Issuer suspects"
- [파트너] 2차 시장에서 토큰을 취득하는 사람은 Ankura Trust Company, LLC를 Security Agent로 선임하게 된다.
  근거: "appoints Ankura Trust Company, LLC as the Security Agent"
- [구조] 발행사는 토큰 보유자에 대해 상환 외에는 책임을 지지 않는다고 명시한다.
  근거: "bears no liability whatsoever to holders of Tokens"
- [기타] 토큰 구매자는 발행사를 상대로 파산이나 청산 절차를 개시할 수 없다.
  근거: "No purchaser of Tokens may institute against"
- [기타] 분쟁은 스위스 국제중재 규칙에 따른 중재로 해결되며, 중재지는 취리히다.
  근거: "The seat of the arbitration shall be Zurich, Switzerland"
- [기타] 2차 시장 취득자에 대한 공지는 영어로만 게시된다.
  근거: "They will only be published in the English language"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/technical
- [상품] Ondo Stocks는 Ethereum mainnet, BNB Chain, Solana에서 이용할 수 있다.
  근거: "Ondo Stocks is available on Ethereum mainnet, BNB Chain, and Solana"
- [구조] 일부 Ondo Stocks는 HyperEVM과 Robinhood Chain으로 브리지될 수 있다.
  근거: "Select Ondo Stocks can also be bridged to HyperEVM and Robinhood Chain"
- [기타] 스마트컨트랙트는 감사를 받았으며, 감사 결과는 공개되어 있다.
  근거: "Yes. You can see the results of our audits"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing
- [구조] 토큰은 가격 움직임과 재투자된 배당 또는 이자를 함께 반영한다.
  근거: "This means they reflect both price movements"
- [용어] 예시에서 배당 재투자 후 토큰 하나는 1.05주 ACME 주식의 경제성을 나타내게 된다.
  근거: "a single ACMEon token now actually represents the economics of 1.05 shares of ACME stock"
- [용어] Solana과 BNB Chain에서는 지원되는 지갑과 탐색기가 표시 배율(display multiplier)을 사용한다.
  근거: "On Solana and BNB Chain, supported wallets and explorers use a display multiplier"
- [구조] 시간이 지나면 토큰 가격은 기초 주식의 가격과 일치하지 않게 된다.
  근거: "the price of the tokenized stock will not match the price of the underlying asset"
- [구조] 견적가는 현재 약 30초 동안 보장되는 가격으로 제공된다.
  근거: "guaranteed for some amount of time (currently about 30 seconds)"
- [구조] 실제 매매 시 적용되는 견적가는 표시된 지시가와 다를 수 있다.
  근거: "may differ from the displayed indicative price"
- [구조] Off-Hours에는 스프레드가 일반 세션보다 넓어질 수 있으며, 토큰 가격이 기초 증권 가치와 더 크게 달라질 수 있다.
  근거: "bid-ask spreads can be wider than during an active session"
- [수수료] 견적 스프레드는 견적 규모, 목표 수익 등 여러 요인에 따라 정해진다.
  근거: "This is based upon a number of factors, including quote size, target profit"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/transferability
- [구조] 토큰은 지원되는 블록체인에서 미국 외 지역으로 이전할 수 있다.
  근거: "Yes. All Ondo stocks are"
- [구조] 토큰 이전은 관할 및 기타 제한의 적용을 받는다.
  근거: "subject to certain jurisdictional and other restrictions"
- [구조] 그 밖의 체인은 준비 중이라고 안내한다.
  근거: "with other chains coming soon"
- 관련도: 중간

## https://docs.ondo.finance/ondo-stocks/troubleshooting
- [구조] 거래가 실패하면 먼저 status.ondo.finance에서 플랫폼과 해당 토큰의 거래 가능 여부를 확인하라고 안내한다.
  근거: "to ensure that the platform is operating correctly"
- [구조] 시스템에는 위험 파라미터와 속도 제한이 있어, 잠시 후 재시도하거나 더 작은 주문을 시도할 수 있다.
  근거: "Our system also has certain risk parameters or rate limits"
- [구조] 민팅과 상환은 API 또는 웹앱을 직접 이용하는 사용자에 한해 지원될 수 있다.
  근거: "we may only be able to support users trying to mint or redeem tokens"
- [구조] 2차 시장에서 토큰을 사고파는 경우에는 해당 시장에 직접 문의해야 한다.
  근거: "please contact the market directly"
- [구조] Solana에서 일부 앱이 시뮬레이션 실패 경고를 띄우는 것은 정상 동작이며 트랜잭션 문제를 뜻하지 않는다.
  근거: "This is expected behavior and does not indicate a problem with the transaction"
- [구조] Ondo Stocks는 just-in-time(JIT) 민팅 모델을 사용하므로 토큰은 스왑이 실행되는 순간 발행된다.
  근거: "Ondo Stocks use a just-in-time (JIT) minting model"
- [기타] API나 웹앱을 직접 이용하는 경우 support@ondo.finance로, 2차 시장 거래는 해당 당사자에게 문의하라고 안내한다.
  근거: "If you are transacting on the secondary market, please contact that party directly"
- 관련도: 중간

## https://docs.ondo.finance/ondo-stocks/trust-and-transparency
- [구조] 토큰은 독립 이사를 포함한 별도 이사회가 운영하는 특수목적회사(SPV)에서 발행되어 파산 격리를 도모한다.
  근거: "issuance from a special purpose vehicle managed by a distinct Board of Directors"
- [구조] Ondo 토큰화 주식은 기초 주식과 ETF로 모두 완전 담보된다.
  근거: "Ondo tokenized stocks are all fully backed by their underlying stocks and ETFs"
- [구조] 발행사는 토큰 보유자 채무를 뒷받침하기 위해 추가 담보를 확보해야 한다.
  근거: "the issuer of Ondo tokenized stocks is required to ensure that there is additional collateral"
- [파트너] Ankura Trust Company는 담보에 대해 제1순위 담보권을 보유한다.
  근거: "holds a first-priority, perfected security interest in this collateral"
- [숫자] 일일 증명(attestation)은 2025년 10월 1일부터 온라인에서 열람할 수 있다.
  근거: "The daily attestations can be viewed online beginning October 1, 2025"
- [구조] Ondo Stocks의 모든 보유분은 하나 이상의 미국 등록 브로커딜러에 보관된다.
  근거: "All Ondo Stocks holdings are held with one or more US-registered custodial broker-dealers"
- [기타] 일일 보고서는 60일 이내에 제공되기 시작한다고 안내한다.
  근거: "Reports will begin being available within 60 days"
- [기타] 월간 대사(reconciliation) 보고서는 다음 달 20일까지 공개된다.
  근거: "Detailed reconciliation reports will be made public by the 20th of the following month"
- [기타] 연간 재무 감사는 독립 감사법인이 수행하여 투자자에게 제공된다.
  근거: "Full financial audits will be conducted annually by an independent audit firm"
- [구조] 스마트컨트랙트는 Spearbit과 Cyfrin의 독립 감사를 받았다.
  근거: "independent audits by Spearbit and Cyfrin"
- [구조] Ondo Foundation 산하 Flux Finance, Inc.가 토큰 보유자 채무에 대한 추가 담보 자금을 보증했다.
  근거: "has guaranteed funds to further collateralize Ondo Stocks’ obligations to tokenholders"
- [구조] 발행 SPV는 Ondo Finance Inc.와 Ondo Foundation 그룹으로부터 자산, 장부, 계정이 분리되어 있다.
  근거: "segregation of assets, books and accounts from Ondo Finance Inc. and the Ondo Foundation group"
- [파트너] Ankura Trust Company는 기초 증권의 존재와 수량을 매일 검증한다.
  근거: "Reviews and verifies the existence and amounts of the underlying securities daily"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks
- 해당 없음: 다른 주소(ondo-stocks/overview)와 같은 본문이며, 접근 제한 안내는 investing-and-redeeming 절과 같은 내용

## 승격 후보
- 해당 없음: 묶음에 훑기 표 없음
