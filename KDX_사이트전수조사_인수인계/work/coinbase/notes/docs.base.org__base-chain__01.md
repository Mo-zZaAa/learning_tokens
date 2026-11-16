# notes: docs.base.org__base-chain__01.md

## https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base
- [상품] 토큰화 주식은 B20 표준 위에 구축되며, B20은 ERC-20의 확장이고 자산 종류에 중립적이라고 설명
  근거: "B20 is an extension of the ERC-20 token standard"
- [지역제한] Coinbase가 발행한 토큰화 주식은 미국 외 적격 관할권의 개인에게만 제공됨
  근거: "only available to persons in eligible jurisdictions outside of the U.S."
- [구조] 토큰화 주식은 별도로 배포된 컨트랙트가 아니라 B20 네이티브 프리컴파일이며, 토큰별 컨트랙트가 없음
  근거: "tokenized stocks are B20 native precompiles, not separately deployed contracts"
- [구조] 1 B20 토큰이 영구적으로 1주와 같지는 않으므로 토큰과 주식 수 환산 시 현재 배수를 적용해야 함
  근거: "One B20 token does not permanently equal one share"
- [숫자] 배당 후 배수 예시: 배수가 1.02로 오르면 1 B20 토큰은 해당 주식 1.02주로 상환 가능함
  근거: "1 B20 token is redeemable for 1.02 shares of the equity"
- [구조] 토큰화 주식의 현금 배당은 현금으로 지급되지 않고 기초 주식으로 전환되어 배수 업데이트로 반영됨
  근거: "cash dividends are converted to shares of the underlying equity"
- [구조] 배수 업데이트는 예약형(ERC-8056 updateUIMultiplier, 정기 기업행위용)이 권장되며, 즉시형 updateMultiplier는 폐기 예정인 비상 장치임
  근거: "It is a retained emergency failsafe; prefer the scheduled path"
- [구조] 정책(Policy)은 전송을 허용하거나 거부하며, 적용 여부는 isAuthorized로 확인 가능
  근거: "Policies determine whether a transfer is allowed or rejected"
- [구조] B20 토큰은 컨트랙트 내 특정 함수를 일시정지할 수 있으며, 온체인 일시정지는 드물다고 설명
  근거: "B20s allow specific functions within a contract to be paused"
- [인허가] 2차 시장 보유와 거래는 허가 없이 가능하며, KYC는 승인 참여자(AP)가 수행하는 민팅과 상환 흐름에서만 이루어짐
  근거: "KYC only happens during mint and redeem flows taken by Authorized Participants (APs)"
- [파트너] 주식 가격 피드는 Chainlink가 제공하며, 24/5 운영되고 주말과 휴일에는 마지막 종가를 유지하며 기업행위 중에는 동결됨
  근거: "runs 24/5, holds the last close on weekends and holidays, and freezes during corporate actions"
- [구조] Coinbase 피드는 원시 주식 가격 대신 Total Return Values를 보고하여 기업행위 조정을 반영함
  근거: "rather than raw equity prices, so the price reflects the underlying’s total return"
- [상품] Chainlink 피드가 있는 Coinbase 종목으로 AAPL, AMZN, GOOGL, META, MSFT, MSTR, NVDA, SNDK, SPCX, TSLA를 나열하며, 예시 행은 Coinbase AAPL 피드 주소임
  근거: "Coinbase AAPL | `0x787f13dEa48Db0897CbCDD985de77809D837F988`"
- [숫자] 토큰 가격 공식은 기초 주식 시장 가격에 배수를 곱한 값임
  근거: "Token Price = Underlying Equity Market Price × Multiplier"
- [구조] 기업행위 중에는 민팅과 상환이 오프체인에서 멈추지만 토큰은 온체인에서 일시정지되지 않아 전송은 막히지 않음
  근거: "the token is not paused onchain, so transfers are not blocked"
- 관련도: 높음

## 승격 후보
- 없음 (이 묶음에는 훑기 표가 없음)
