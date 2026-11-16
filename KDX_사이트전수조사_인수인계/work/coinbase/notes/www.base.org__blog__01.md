# notes: www.base.org__blog__01.md

## https://www.base.org/blog/request-for-builders-tokenized-stocks
- [상품] 토큰화 주식은 Base에서 이미 라이브 상태이며, Coinbase가 발행하고 적격 비미국 사용자에게 제공된다고 함
  근거: "issued by Coinbase and available to eligible non-US users"
- [연혁] 이 글의 게시일은 Base·Sep 1, 2026
  근거: "Base·Sep 1, 2026"
- [지역제한] 토큰화 주식은 미국 밖 허용 관할권의 적격 사용자에게만 제공된다고 명시
  근거: "only available to eligible users in permitted jurisdictions outside the United States"
- [발행] 본문 면책 문구에 따르면 Base는 토큰화 주식을 발행하지 않으며, 본문이 언급하는 토큰화 주식은 Coinbase가 발행함
  근거: "Base does not issue tokenized stocks"
- [상품] 주식은 온체인에서 프로그래밍 가능하고 조합 가능하며 이용 가능하다고 설명
  근거: "For the first time, equities are programmable, composable, and available onchain"
- [상품] 일부 토큰화 주식에는 수익 창출 메커니즘이 붙어 있을 수 있다고 언급
  근거: "Some tokenized stocks may have yield-generating mechanics"
- [기타] 빌더 제안 분야로 신규 브로커리지(미국 시장 접근이 제한적이던 사용자 대상)를 듦
  근거: "build new brokerage experiences for users"
- [기타] 빌더 제안 분야로 투자 선물(시간 잠금 구조 포함)과 기업의 고객 리워드 등 선물과 보상 활용을 듦
  근거: "new ways to structure gifts of investments to friends and family"
- [기타] 빌더 제안 분야로 수익 분리(원금과 수익 분리), 수익을 반영한 담보 대출 등을 듦
  근거: "separate the principal from the yield"
- [용어] 밈 주식(memestocks)을 "주식에 연결된, 밈 토큰처럼 관심에 따라 거래되는 토큰"으로 정의
  근거: "memestocks: tokens that trade on attention the way a memecoin does"
- [기타] 에이전트가 지갑으로 토큰화 주식에 직접 투자할 수 있다는 가능성을 제시
  근거: "Agents with wallets can allocate into tokenized stocks on their own"
- [파트너] Base Batches 004 지원서 접수가 열려 있다고 안내
  근거: "is now open for applications"
- 관련도: 높음

## https://www.base.org/blog/b20-tokenized-stocks-on-base
- [구조] Coinbase 토큰화 주식은 Base 네이티브 토큰 표준인 B20 위에 구축됨
  근거: "a Base-native token standard designed for secure, compliant, and frictionless asset issuance"
- [상품] 각 토큰은 규제 대상 수탁기관이 보관하는 실제 미국 기업 주식으로 전액 뒷받침된다고 설명
  근거: "fully backed by real US company shares held with a regulated custodian"
- [지역제한] Coinbase 토큰화 주식은 미국 외 적격 관할권 거주자에게만 제공됨
  근거: "only available to persons in eligible jurisdictions outside of the U.S."
- [구조] 토큰 발행 시 배수(multiplier)는 1.00으로 시작함
  근거: "Tokens launch with a multiplier of 1.00"
- [구조] 배당은 추가 토큰이 아니라 배수 상승으로 반영되며, 현금 배당은 원천징수세와 Coinbase 수수료를 뺀 뒤 추가 주식에 재투자된다고 함
  근거: "holders receive dividends through a higher multiplier rather than additional B20 tokens"
- [수수료] 배당 재투자 시 배당 원천징수세와 Coinbase 수수료를 차감한다고 명시
  근거: "net of dividend withholding tax and a Coinbase fee"
- [숫자] 예시: 순 2% 배당은 배수를 ~1.02로 올리고, 2대1 액면분할은 배수를 1.02에서 2.04로 두 배로 만든다고 설명
  근거: "A 2-for-1 split doubles the multiplier from 1.02 to 2.04"
- [구조] B20 토큰 하나가 영구적으로 주식 한 주와 같지는 않으므로 토큰과 주식을 환산할 때 현재 배수를 읽어야 함
  근거: "a B20 tokenized stock does not permanently equal one share"
- [구조] 주식 분할 등 기초자산 이벤트를 배수 변경으로 처리하므로 AMM 풀의 ERC-20 잔액은 변하지 않는다고 설명
  근거: "the pool’s ERC-20 balances never change"
- [구조] 이동 제한을 위한 정책은 공유 Policy Registry에 정의되며, 정책 하나를 여러 토큰이 참조할 수 있음
  근거: "Policies live in a shared Policy Registry"
- [구조] 법적 요건을 충족하도록 "freeze and seize"(동결과 압류) 기능을 추가했다고 명시
  근거: "to add “freeze and seize” functionality to fulfill legal requirements"
- [구조] 압류(seize) 권한이 있는 관리자는 정책 플래그가 붙은 주소에서 승인된 목적지로 토큰을 옮길 수 있고 메모가 기록됨
  근거: "moves tokens from a policy-flagged address to an authorized destination"
- [인허가] 주식 토큰의 민팅과 상환은 KYC를 마친 승인 참여자(Authorized Participants, APs)로 제한됨
  근거: "restricted to KYC-onboarded Authorized Participants (APs)"
- [구조] 일부 운영 통제(AP의 민팅과 상환 가능 여부, 미국 장외 시간 가격 피드 동작)는 토큰 위에서 이루어져 B20이 강제하지 않음
  근거: "some operational controls sit above the token and are not enforced by B20"
- [파트너] 각 토큰은 Chainlink의 총수익(total-return) 피드와 짝지어지며, 이 피드에는 배수가 이미 반영되어 있다고 설명
  근거: "pair each token with a Chainlink total-return feed"
- 관련도: 높음

## https://www.base.org/blog/tokenized-stocks
- [연혁] 토큰화 주식이 Base에 라이브된 이 글의 게시일은 Base·Aug 24, 2026
  근거: "Base·Aug 24, 2026"
- [상품] Coinbase가 발행하고 B20 표준으로 만든 토큰화 주식이 Base에 네이티브로 라이브됨
  근거: "tokenized stocks issued by Coinbase, built on the B20 standard"
- [상품] 각 토큰은 규제 수탁기관이 1:1로 보유하는 실제 주식이라고 설명
  근거: "held 1:1 by a regulated custodian"
- [상품] 본문은 Apple과 NVIDIA 같은 기업의 분할 주식(fractional shares)을 제공한다고 언급
  근거: "fractional shares of companies like Apple and NVIDIA"
- [구조] 승인 참여자(Authorized participants)는 기관 마켓메이커이며 주식을 매입함
  근거: "Authorized participants, which are institutional market makers, buy the shares"
- [파트너] 주식은 Alpaca(규제 브로커 겸 수탁기관)로 보내지며, 이 구조는 ADGM 규제기관의 감독을 받는다고 함
  근거: "in a bankruptcy-remote structure supervised by Abu Dhabi Global Market’s (ADGM) regulatory authority"
- [파트너] 주식은 Aave를 통한 담보 대출에서 더 나은 담보가 될 수 있다고 언급
  근거: "Stocks can also be better collateral for securing loans"
- [파트너] Virtuals와 Treasures가 토큰화 자산을 에이전트 트레이딩에 연결하고 있다고 언급
  근거: "are already wiring tokenized assets into agentic trading"
- [상품] 배당과 분할은 온체인 배수로 처리되어 잔액이 변하지 않는다고 설명
  근거: "Dividends and splits are handled by an onchain multiplier"
- [지역제한] 적격 비미국 사용자 중 인터넷 연결과 지갑이 있는 사용자가 대상이라고 설명
  근거: "Non-US users in eligible jurisdictions"
- [지역제한] 토큰화 주식은 미국 외 적격 관할권에서만 이용 가능하다는 면책 문구
  근거: "Tokenized Stocks are only available in eligible jurisdictions outside of the U.S."
- [상품] 토큰은 AMM 풀에서 24시간 거래될 수 있다고 설명
  근거: "can trade across always-on AMM pools"
- [파트너] 참여 프로토콜의 제3자 인센티브 프로그램이 있을 수 있다고 언급. 거래소 목록과 컨트랙트 주소는 base.org/stocks에 있다고 안내
  근거: "A list of venues and contract addresses is at base.org/stocks"
- [파트너] 제3자 프로토콜 여러 곳이 B20 표준 지원을 공개 발표했다고 언급(목록은 본문에 없음)
  근거: "have publicly announced support for the B20 standard"
- [상품] 향후 몇 주 안에 Coinbase 토큰화 주식이 추가될 것이라고 언급
  근거: "More Coinbase tokenized stocks will land over the coming weeks"
- [연혁] 2018년 9월 Coinbase와 Circle이 USDC를 출시했다고 비교로 언급
  근거: "In September 2018, Coinbase and Circle launched USDC"
- [기타] Base는 토큰화 증권을 발행, 제공, 수탁, 시장 조성하지 않는다고 면책 문구에 명시
  근거: "does not issue, offer, sell, custody, or make markets in any tokenized security"
- 관련도: 높음

## 승격 후보
- 없음 (이 묶음에는 훑기 표가 없음)
