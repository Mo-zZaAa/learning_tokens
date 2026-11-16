# notes: docs.ondo.finance__ondo-stocks__01.md

## https://docs.ondo.finance/ondo-stocks/available-assets
- [상품] 현재 Ondo Stocks 플랫폼에서 450+ 토큰화 주식과 ETF를 거래할 수 있다.
  근거: "Investors can currently trade 450+ tokenized stocks and ETFs via the Ondo Stocks platform"
- [상품] ETF도 제공되며, 여기서 "토큰화 주식"은 제공 자산 전체를 뜻한다고 설명한다.
  근거: "Yes, ETFs are available—when we say ‘tokenized stocks’"
- [상품] 향후 수개월 내에 수천 개의 공개 거래 자산을 토큰화할 계획이라고 밝혔다.
  근거: "we intend to tokenize thousands of publicly traded assets over the coming months"
- [지역제한] 현재는 NYSE와 NASDAQ에서 거래되는 증권의 토큰화 버전만 제공한다.
  근거: "We currently only offer tokenized versions of securities trading on the NYSE and NASDAQ exchanges"
- [지역제한] 향후 다른 국가 거래소에서 거래되는 증권으로 확장할 수 있다고 밝혔다.
  근거: "we may expand to tokenizing securities trading on exchanges in other countries"
- [용어] USDon은 Ondo Stocks 브로커리지 계좌의 미국 달러로 1:1 담보되는 스테이블코인이다.
  근거: "USDon is a stablecoin backed 1:1 by a US dollar"
- [용어] USDon은 토큰화 주식을 즉시 매수하거나 상환하는 데 쓰이는 스테이블코인이다.
  근거: "USDon is the stablecoin used to instantly buy or redeem Ondo tokenized stocks"
- [구조] USDC로 매수하면 플랫폼이 USDC를 USDon으로 바꾼 뒤 그 USDon으로 토큰화 주식을 산다.
  근거: "and then uses USDon to buy the tokenized stock"
- [구조] USDC로 매도하면 플랫폼이 먼저 USDon으로 상환한 뒤 그것을 USDC로 바꾼다.
  근거: "our platform first redeems for USDon and then swaps that for USDC"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/comparison-to-other-tokenized-stocks
- [구조] Ondo 토큰화 주식은 즉각적이고 저비용인 민팅과 상환을 가능하게 하며, 전통 시장의 유동성을 물려받는다고 설명한다.
  근거: "by enabling instant, low-cost minting/redemption and by inheriting liquidity from traditional markets"
- [구조] 기존 토큰화 자산 구현에서는 민팅과 상환의 마찰이 커서 빠른 차익거래 개입이 막힌다고 설명한다.
  근거: "In many existing implementations of tokenized assets, however, high-friction minting and redemption processes"
- [구조] 가격 연동은 기초 시장이 열려 있는 것에 의존한다고 설명한다.
  근거: "This dynamic depends on the underlying markets being open"
- [구조] Off-Hours 세션에는 기초자산 유동성이 제한되어 차익거래가 제약되고, 스프레드가 벌어질 수 있다.
  근거: "liquidity in the underlying is limited and arbitrage is constrained"
- [구조] 다른 토큰화 주식과 달리 Ondo 토큰화 주식은 24/7 이전 가능, DeFi 호환, 강한 투자자 보호 구조를 갖는다고 설명한다.
  근거: "and some other tokenized stock implementations are that our assets are"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/corporate-actions
- [구조] 배당금은 자동으로 기초 주식에 재투자되며 토큰 가격에 반영된다.
  근거: "Dividends are automatically invested back into the referenced stock and reflected in token pricing"
- [구조] Solana과 BNB Chain에서는 표시 배율을 지원하는 지갑과 탐색기가 배당 재투자를 표시 잔고에 반영한다.
  근거: "wallets and explorers that support display scaling reflect dividend reinvestment in the displayed token balance"
- [구조] 배당 ex-date 전날 7:50:00pm-8:10:00pm 사이에는 거래가 일시 중단될 수 있다고 안내한다.
  근거: "you can assume trading may be paused 7:50:00pm-8:10:00pm the day before the dividend ex-date"
- [구조] ETF 분배금은 보유 자산의 발생 이자 등을 기초로 계산되는 경우가 많아 금액 확정이 ex-date에 가깝게 이루어질 수 있다.
  근거: "ETF distributions (especially from fixed income funds) are often calculated"
- [구조] 배당 금액이 확정될 때까지 플랫폼이 해당 자산의 거래를 중단한다고 밝혔다.
  근거: "until the exact amount of the dividend is known"
- [구조] 미국 시장이 닫힌 동안 발표된 기업활동과 중요 뉴스는 처리될 때까지 토큰 가격에 반영되지 않을 수 있다.
  근거: "may not be reflected in token pricing until they can be processed"
- [구조] 실적 발표 전후 기간에는 자산이 '제한(limited)' 상태가 되어 최대 단일 거래 규모가 줄어든다.
  근거: "the maximum single trade size is reduced"
- [용어] 대부분의 정기 배당에서 배당 기준일과 배당락일(ex-date)은 같은 날이다. 근거 문장은 T+1 결제를 전제로 한다.
  근거: "the ex-date and record date are now the same day for most regular dividends"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/eligibility
- [지역제한] 금지 관할지역에 거주하거나 그곳 법에 따라 설립된 개인과 법인은 Ondo Stocks를 청약, 취득 또는 상환할 수 없다.
  근거: "are prohibited from subscribing for, acquiring or redeeming Ondo Stocks"
- [지역제한] 금지 관할지역 목록에는 United States와 그 주, 속령, 연방 구역이 포함된다.
  근거: "United States, or any of its states, possessions, territories or federal districts"
- [지역제한] 미국 내에서 매수 주문을 내는 사람도 청약과 취득이 금지된다.
  근거: "Persons who place buy orders from within the United States"
- [지역제한] 제한 관할지역 표에 열거된 지역의 거주자는 해당 적격 요건 중 하나 이상을 충족해야 Ondo Stocks를 발행받을 수 있다.
  근거: "must satisfy one or more of the eligibility requirements set forth opposite the name"
- [지역제한] 스위스에서는 개인에게 Ondo Stocks가 제공되지 않는다.
  근거: "Ondo Stocks are not available to Individuals in this jurisdiction"
- [지역제한] 발행사는 법규 위반 가능성이 있다고 판단한 활동을 자체 재량으로 금지할 수 있다.
  근거: "in its sole discretion, that such activity may constitute a violation of"
- [지역제한] 금지 대상자가 어떤 법인의 실질 지분 또는 지배권을 합산 50% 이상 보유하면 그 법인도 청약이 금지될 수 있다.
  근거: "hold in the aggregate 50% or more beneficial ownership or control of any entity"
- [고객] 발행사는 KYC 정책에 따라 관할과 무관한 자격 기준도 적용한다.
  근거: "also imposes non-jurisdiction-related eligibility criteria in accordance with its know-your-customer policies"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/fees-and-taxes
- [수수료] 발행(민팅)에는 수수료가 없고, 상환에는 0.05%(5bps) 수수료가 부과된다.
  근거: "There is no fee to mint and a 0.05% (5bps) fee for each redemption"
- [수수료] 견적가는 기초 주식의 매매가와 다를 수 있으며, 그 차이는 Ondo Stocks가 보유한다.
  근거: "with any difference being retained by Ondo Stocks"
- [수수료] 가스비는 투자자가 부담한다.
  근거: "Investors are responsible for their own gas costs"
- [수수료] 2차 시장에서 취득하면 다른 주체가 수수료를 부과할 수 있다.
  근거: "fees may be charged to you by other parties"
- [기타] 발행사(BVI 법인)가 받는 미국 기업 배당에는 30% 원천징수가 적용된다.
  근거: "For dividends from US-based companies, this rate is 30% in accordance with US tax regulations"
- [기타] 미국 기초 ETF 분배금도 30% 세율이 적용되지만, 일부 분배금은 원천징수 면제되어 실효세율이 더 낮을 수 있다.
  근거: "certain portions of such distributions may be exempt from withholding tax"
- [기타] 비미국 기업의 ADR 배당은 룩셈부르크에서 15%가 먼저 원천징수된다.
  근거: "Luxembourg will withhold 15% of the dividend before it even gets to the ADR"
- [기타] 재투자되는 배당은 원천징수를 뺀 금액이다.
  근거: "dividend reinvested in the underlying asset is net of any withholding tax"
- [기타] 자본이득과 소득에 대한 원천징수는 없고, 토큰 상환 시에도 Ondo Stocks가 세금을 원천징수하지 않는다.
  근거: "nor does Ondo Stocks withhold any taxes when tokens are redeemed"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/important-notes
- [인허가] 토큰은 1933년 미국 증권법에 따라 등록되지 않았다.
  근거: "have not been registered under the US Securities Act of 1933, as amended"
- [지역제한] 토큰은 등록이나 면제 없이 미국 또는 미국인에게 판매될 수 없다.
  근거: "The Tokens may not be offered or sold in the United States or to US persons"
- [인허가] 영국, 스위스, 싱가포르에서는 토큰이 적격투자자 또는 전문 고객에게만 제공된다.
  근거: "are offered and sold only to qualified investors or professional clients"
- [인허가] 발행사는 1940년 미국 투자회사법상 투자회사로 등록되어 있지 않다.
  근거: "is not registered as an investment company under the US Investment Company Act of 1940"
- [인허가] EEA/EU에서는 리히텐슈타인 금융시장감독청(FMA)이 승인한 기본 투자설명서가 있다.
  근거: "a base prospectus relating to the Tokens has been approved"
- [인허가] 일부 Ondo Stocks는 UAE에서 “Digital Securities”로 불리며, Binance가 운영하는 Nest Exchange Limited에서 거래가 허용되었다.
  근거: "have been admitted to trading on Nest Exchange Limited"
- [지역제한] 영국에서는 이 자료가 투자 전문가 등 지정된 대상에게만 향한다.
  근거: "the communications herein are only intended for, and directed at, investment professionals"
- [구조] 토큰은 영국령 버진아일랜드 기업인 Ondo Global Markets (BVI) Limited가 발행한다.
  근거: "are issued by Ondo Global Markets (BVI) Limited, a British Virgin Islands business company"
- [구조] OUSG 토큰은 델라웨어 유한파트너십인 Ondo I LP가 발행한다.
  근거: "OUSG tokens are issued by Ondo I LP, a Delaware (USA) limited partnership"
- [구조] Ondo Finance Inc.는 발행사에 토큰화 서비스를 제공하며 발행사의 지분을 보유한다.
  근거: "provides tokenization services to, and is an equity holder of, Ondo Global Markets (BVI) Limited"
- [구조] 토큰은 주식, ETF, ADR 자체가 아니며 보유자에게 기초자산을 보유하거나 받을 권리를 주지 않는다.
  근거: "do not provide their holders with rights to hold or receive their respective underlying assets"
- [상품] 플랫폼은 Off-Hours 세션에 선택된 Ondo Stocks의 거래를 허용할 수 있다.
  근거: "The platform may permit trading in a select set of Ondo Stocks during an Off-Hours session"
- [구조] Off-Hours 세션에서는 자산별 보수적이고 동적인 최대 주문 규모 한도가 적용된다.
  근거: "the maximum order or trade size is subject to conservative, dynamic per-asset Off-Hours limits"
- [기타] 이 자료는 투자, 법률, 세무, 재무 자문이 아니다.
  근거: "Nothing herein constitutes investment, legal, tax or financial advice"
- [기타] 토큰 보유자는 매수 금액 전액을 포함한 손실을 입을 수 있다.
  근거: "A holder of the Tokens may incur losses, including total loss of their purchase price"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/investing-and-redeeming
- [지역제한] 이 렌더링 결과에는 접근 제한 안내가 표시되며, Ondo Stocks 상품은 해당 지역에서 이용할 수 없다고 나온다.
  근거: "Ondo Stocks products are not available in your region"
- [숫자] 최소 투자 금액은 1.00 USD이다.
  근거: "The minimum is just $1.00 USD"
- [상품] 1개 미만의 토큰도 매수할 수 있다.
  근거: "Yes, you can buy less than one full token"
- [상품] 플랫폼에서 구매하는 모든 토큰화 주식은 USDon으로 결제된다.
  근거: "All Ondo tokenized stocks purchased from the Ondo Stocks platform are purchased with"
- [구조] USDC는 민팅 시 USDon으로 1:1 원자적 전환될 수 있다.
  근거: "USDC can be atomically converted 1:1 to USDon for mints"
- [구조] USDC 전환은 스테이블코인 스왑퍼가 상대 토큰을 충분히 보유하고 있는지에 달려 있다.
  근거: "depends upon the stablecoin swapper having sufficient amounts of the other token available"
- [구조] 기본적으로 사용자는 USDon과 USDC 간 전환이 허용되지 않으며, 허용을 원하면 문의해야 한다.
  근거: "by default, users are not whitelisted to swap between USDon and USDC"
- [구조] 스왑퍼는 현재 UI가 없어 스마트컨트랙트와 직접 상호작용해야 한다.
  근거: "the swapper does not currently have a UI"
- [구조] Ondo 토큰화 주식은 ERC20 호환이며 이전 가능하고, 스마트컨트랙트나 외부 소유 계정 등 어떤 지갑이든 보유할 수 있다.
  근거: "Ondo’s tokenized stocks are ERC20 compliant and transferable"
- [구조] 대부분의 중앙화 거래소 커스터디 계좌는 아직 지원하지 않는다.
  근거: "most centralized exchange custodial accounts (e.g. Binance, Coinbase) do not (yet)"
- [구조] 신규 토큰 민팅은 즉시 이루어진다.
  근거: "The minting of new Ondo tokenized stocks is instant"
- [인허가] 투자설명서 등 자료는 온보딩을 마친 투자자에게만 제공된다.
  근거: "we are only able to provide such materials to investors"
- [상품] 은행 송금으로 토큰화 주식을 직접 매수하는 것은 현재 지원되지 않는다.
  근거: "Purchasing Ondo tokenized stocks directly via bank wire is not currently supported"
- [숫자] USDon 은행 송금 구매는 $500,000 이상을 투자하는 경우에만 가능하다.
  근거: "Purchasing USDon via bank wire is only available to those investing $500,000 or more"
- [구조] USD로의 은행 송금 상환은 현재 지원되지 않는다.
  근거: "Redemptions to USD via bank wire are not currently supported"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/legal-and-regulatory
- [구조] Ondo 토큰화 주식은 구조화 노트(structured note), 즉 BVI에 설립된 특수목적회사(SPV)가 발행하는 채무 상품이다.
  근거: "An Ondo tokenized stock is a structured note: a debt instrument"
- [구조] 토큰 보유자의 권리와 의무는 발행사 Sales Terms에 따라 스위스법의 적용을 받는다.
  근거: "Tokenholder rights and obligations are governed by Swiss law under the Issuer’s Sales Terms"
- [구조] 토큰은 기초 증권에 1:1 기준으로 완전 담보된다(추가 버퍼 별도).
  근거: "These tokens are fully backed on a 1:1 basis"
- [구조] 보유자는 기초 증권 발행사에 대한 의결권과 정보권 등 주주 권리가 없다.
  근거: "you do not have shareholder voting rights, shareholder information rights"
- [기타] 보유자가 기초자산의 실질 소유자로 인정되는지 여부는 개인 상황과 현지 법에 따라 달라진다.
  근거: "Whether tokenholders might be considered the beneficial owner of the underlying assets"
- [인허가] 발행사 OGM은 1933년 미국 증권법상 Regulation S 면제에 의존해 토큰을 발행하고 판매한다.
  근거: "only offers and sells the tokens in reliance on the exemption provided by Regulation S"
- [지역제한] 판매 대상은 미국 외 거주자이며, Regulation S Rule 902의 “US persons”가 아니어야 한다.
  근거: "not “US persons” as defined in Rule 902 of Regulation S"
- [지역제한] 토큰은 등록이나 면제 요건을 갖추지 않는 한 미국인이나 미국 내로 재판매될 수 없다.
  근거: "Tokens may not be resold to any US person or into the United States"
- [고객] 토큰을 구매하거나 상환하는 사람은 먼저 OGM의 온보딩과 KYC를 완료해야 한다.
  근거: "must first successfully complete OGM’s onboarding process"
- [구조] Ondo Global Markets (BVI) Limited의 90.01%는 Flux Finance Inc.가 보유하며, 이 회사는 Ondo Foundation의 완전 자회사다.
  근거: "is 90.01% owned by Flux Finance Inc. (a wholly owned subsidiary of the Ondo Foundation)"
- [구조] Ondo Global Markets (BVI) Limited의 9.99%는 Ondo Finance Inc.가 보유한다.
  근거: "9.99% owned by Ondo Finance Inc."
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/market-hours-and-trading-availability
- [상품] 플랫폼은 일반적으로 일요일 8:05:00pm ET부터 금요일 7:59:00pm ET까지 거래할 수 있다.
  근거: "8:05:00pm ET (New York time) Sunday evening through 7:59:00pm ET Friday evening"
- [상품] 거래 세션은 프리마켓, 정규장, 장후, 오버나이트로 나뉘며, 오버나이트는 8:05:00pm ET부터 3:55:00am ET까지다.
  근거: "8:05:00pm ET - 3:55:00am ET (Overnight)"
- [상품] 주말과 미국 공휴일에도 선택된 자산은 Off-Hours 세션에서 거래할 수 있다.
  근거: "a select set of assets are also available to trade during an Off-Hours session"
- [구조] 플랫폼은 기초 거래소의 새 세션 시작 전후 몇 분간 거래를 일시 중단할 수 있다.
  근거: "we may temporarily halt trading a few minutes before and after"
- [구조] 오버나이트 세션은 유동성이 일반적으로 낮아 대량 주문을 나눠야 할 수 있고 스프레드가 넓을 수 있다.
  근거: "Because in general the liquidity in the overnight session is lower"
- [구조] 플랫폼 수준의 위험 통제 임계치에 도달하면 거래가 중단될 수 있다.
  근거: "If certain proprietary platform-level risk control thresholds are met"
- [구조] 자산별로는 Off-Hours 거래 한도에 도달한 경우에도 거래가 중단될 수 있다.
  근거: "including when an Off-Hours-enabled asset reaches its Off-Hours trading limit"
- [기타] 플랫폼과 자산별 거래 가능 여부는 status.ondo.finance에서 확인할 수 있다.
  근거: "You can always check platform- and asset-level trading availability"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/off-hours-trading
- [상품] Off-Hours는 기초 미국 시장이 닫힌 시간에 운영되는 별도의 거래 세션이다.
  근거: "Off-Hours is treated as its own trading session"
- [상품] Off-Hours에 거래 가능한 자산은 목록으로 제시되며 32개이고, AAPLon, TSLAon, NVDAon, QQQon, SPYon 등이 포함된다.
  근거: "The following assets are tradable during the Off-Hours session"
- [상품] Off-Hours 거래는 Ethereum, BNB Chain, Solana 네트워크에서 가능하다.
  근거: "Off-Hours trading is available on the **Ethereum**, **BNB Chain**, and **Solana** networks"
- [구조] Off-Hours에도 매수와 매도는 즉시 견적, 민팅, 상환이 이루어지며 일반 세션과 기본 경험은 같다.
  근거: "The core experience is the same: buys and sells are quoted, minted, and redeemed instantly"
- [구조] 자산별 Off-Hours 한도는 일반 세션 한도와 별도이며 보수적으로 설정된다.
  근거: "separate from its regular-session limits and set conservatively"
- [구조] 자산이 Off-Hours 한도에 도달하면 해당 자산의 거래가 일시 제한되고 견적 요청이 거절될 수 있다.
  근거: "When an asset reaches its Off-Hours limit, trading in that asset may be temporarily restricted"
- [구조] Off-Hours에는 스프레드가 더 넓어질 수 있다.
  근거: "bid-ask spreads can be wider during Off-Hours"
- [기타] 현재 Off-Hours 상태와 한도는 status.ondo.finance/market에서 확인할 수 있다.
  근거: "the simplest option is the status page at"
- [기타] API에서 Off-Hours 상태는 offhours 객체로, 세션 한도는 offhours 항목으로 제공된다.
  근거: "reports the Off-Hours window through a dedicated `offhours` object"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/onboarding-and-kyc
- [고객] 온보딩 대상은 **institutional participants**와 **retail users/individuals**이며, 지원 관할지역에 한한다. 기관 참가자와 개인 사용자가 해당된다.
  근거: "is open to **institutional participants** and **retail users/individuals**"
- [고객] 온보딩은 네 단계로 이루어진다.
  근거: "Onboarding will involve four steps"
- [파트너] KYC/KYB 검증은 Persona를 통해 진행된다.
  근거: "Ondo Stocks conducts KYC/KYB verification via"
- [고객] 법인(KYB)과 개인(KYC) 모두 자금의 원천과 부의 원천(Source of Wealth) 정보를 제출해야 한다.
  근거: "Source of funds and Source of Wealth information"
- [고객] 개인은 90일 이내 발급된 주소 증빙을 제출해야 한다.
  근거: "Proof of address dated within the last 90 days"
- [고객] 법인은 설립 증명 서류(Article of Existence Document Type)를 제출해야 하며, 예로 Certificate of Incorporation 등이 있다.
  근거: "Article of Existence Document Type (e.g. Certificate of Incorporation"
- [고객] KYC/KYB 승인 후 필요한 약정 서류는 전자서명 플랫폼으로 발송된다.
  근거: "Upon approval of KYC/KYB, we will send any required forms for digital signing"
- [고객] 계정에 연결하는 모든 지갑 주소는 Ondo의 검토와 승인을 받아야 한다.
  근거: "All linked wallet address(es) are subject to review and approval by Ondo"
- [고객] 심사 기간은 몇 분에서 며칠까지이며, 수요가 많으면 더 길어질 수 있다.
  근거: "Timelines for application review may range from a few moments to a few days"
- [고객] 온보딩 진행 중 문의는 온보딩 팀이 도와준다고 안내한다.
  근거: "our Onboarding team will be happy to assist you"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/overview
- [상품] Ondo Stocks는 미국 외 투자자에게 미국 공개 증권 수천 개에 대한 온체인 노출을 제공하는 토큰화 플랫폼이다.
  근거: "to gain exposure to thousands of US publicly traded securities, including stocks and ETFs"
- [용어] 토큰 이름은 기초 티커 뒤에 `on` 접미사를 붙여 지정된다.
  근거: "They are designated by the `on` suffix"
- [용어] 예를 들어 Tesla의 티커는 TSLA이고, 대응하는 토큰은 TSLAon이다.
  근거: "the corresponding Ondo tokenized stock is called `TSLAon`"
- [구조] Ondo 토큰화 주식은 Ondo Global Markets (BVI) Limited(발행사)가 제공한다.
  근거: "Ondo tokenized stocks are offered by Ondo Global Markets (BVI) Limited (the Issuer)"
- [상품] 토큰은 보유자가 기초 자산을 보유하고 배당을 재투자했을 때와 같은 경제적 노출을 주도록 설계되었다.
  근거: "designed to give holders the same economic exposure as they would receive"
- [용어] 총수익 추적 토큰이라서 시간이 지나면 토큰 하나가 주식 한 주 이상의 노출을 제공할 수 있다.
  근거: "Therefore, over time, a given token may provide economic exposure"
- [구조] 거래는 일반적으로 24/5 가능하며 예외가 있다.
  근거: "They generally trade 24/5, but there are exceptions"
- [구조] 민팅과 소각은 즉시 이루어지며, 단일 원자적 거래로 토큰 또는 스테이블코인을 받는다.
  근거: "you get your tokens or stablecoins in a single atomic transaction"
- [구조] 현재 Ethereum, BNB Chain, Solana에서 제공된다.
  근거: "They are currently available on Ethereum, BNB Chain, and Solana"
- [구조] 일부 토큰은 bridge를 통해 HyperEVM과 Robinhood Chain으로 옮길 수 있다.
  근거: "select tokens are transferable to HyperEVM and Robinhood Chain via bridge"
- [숫자] 현재 450+ 자산이 제공되며 더 많은 자산이 준비 중이다.
  근거: "There are currently 450+ assets available, but more are coming soon"
- [지역제한] 토큰은 대체로 비미국 투자자에게 제공되며 관할 제한이 적용된다.
  근거: "They are generally available to non-US investors"
- [구조] 토큰은 지원하는 DeFi 프로토콜에서 사용될 수 있도록 설계되었다.
  근거: "Ondo tokenized stocks are designed to be usable in DeFi protocols that support them"
- [파트너] 출시는 Bitget, Trust Wallet, OKX, HTX Global, 1inch 등 생태계 파트너와 함께 이루어진다.
  근거: "including Bitget, Trust Wallet, OKX, HTX Global, 1inch"
- [구조] 발행 구조는 파산 격리, 완전 담보 등 최고 수준의 투자자 보호를 목표로 설계되었다고 설명한다.
  근거: "They are designed with best-in-class investor protections"
- 관련도: 높음

## https://docs.ondo.finance/ondo-stocks/partners-and-media
- [파트너] 자산운용사 등이 고객에게 Ondo 토큰화 주식을 제공하려는 제휴 문의는 support@ondo.finance로 해야 한다.
  근거: "Please contact us at [support@ondo.finance](mailto:support@ondo.finance)."
- [기타] 로고와 미디어 키트는 Notion의 Ondo Media Kit 페이지에서 받을 수 있다.
  근거: "Yes, see our [Media Kit](https://www.notion.so/Ondo-Media-Kit-3bc0a5aced014cc4b0ef62f1638bbf8e?pvs=21)."
- 관련도: 중간

## https://docs.ondo.finance/ondo-stocks/private-client
- [기타] Ondo Private Client는 Ondo Foundation이 운영하는 충성도(loyalty) 프로그램이다.
  근거: "The Ondo Private Client Program is a loyalty program offered by the Ondo Foundation"
- [고객] Private Client 등급은 신청서를 제출하거나 구매하여 얻을 수 없다.
  근거: "There is no application to submit and Private Client status cannot be purchased"
- [숫자] Platinum 등급은 보유 자산 $1M-$5M 또는 누적 현물 거래량 $1M-$10M이다.
  근거: "**Platinum** | $1M-$5M | $1M-$10M"
- [숫자] Diamond 등급은 보유 자산 $5M-$25M 또는 누적 현물 거래량 $10M-$50M이다.
  근거: "**Diamond** | $5M-$25M | $10M-$50M"
- [숫자] Obsidian 등급은 보유 자산 $25M 초과 또는 누적 현물 거래량 $50M 초과다.
  근거: "**Obsidian** | More than $25M | More than $50M"
- [숫자] 보유 자산은 90일 롤링 기간으로 측정된다.
  근거: "Assets held are measured over a 90-day rolling period"
- [숫자] 누적 현물 거래량은 30일 롤링 기간으로 측정된다.
  근거: "Cumulative spot volume is measured over a 30-day rolling period"
- [고객] Obsidian 회원은 Signature Experiences를 받을 수 있다.
  근거: "One-of-a-kind experiences created for Obsidian members"
- [고객] 혜택은 보장되지 않으며 사용자, 등급, 계정 상태, 관할에 따라 달라질 수 있다.
  근거: "Benefits are not guaranteed and may vary by user, tier, account status"
- [고객] 등급은 계정 활동 수준으로 나뉘며, 프로그램이 자격 지갑에서 직접 추적한다.
  근거: "the program tracks directly from your qualifying wallet"
- [고객] 일부 혜택은 활성 상태이고 인증된 Ondo Stocks 계정이 필요할 수 있다.
  근거: "may be required to unlock select rewards or benefits"
- [기타] Ondo는 DM 링크로 Private Client 상태를 청구하라고 요청하지 않는다.
  근거: "Ondo will never ask you to click a link in a direct message to claim"
- [기타] 온체인 메시지는 공식 Ondo DeBank 계정에서 발송된다고 한다.
  근거: "Any onchain communications will be sent from the"
- [고객] 등급 확인 후 Telegram 핸들 또는 이메일을 공유해 Private Client 팀과 직접 연결할 수 있다.
  근거: "Share your Telegram handle or email address to set up a direct line"
- 관련도: 낮음

## 승격 후보
- 해당 없음: 묶음에 훑기 표 없음
