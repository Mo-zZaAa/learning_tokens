# notes: assets.dinari.com/forms USD+ 백서 (SITE-dinari-1)
## 페이지별 사실
### https://assets.dinari.com/forms/usdplus-whitepaper.pdf
- USD+ 백서(2024년 2월, 저자 Jake Timothy): 두 토큰 구조. USD+는 달러 연동 토큰(ERC-20), Staked USD+는 ERC-4626 볼트로 수익을 축적. 준비금 금고(Reserves Vault)가 담보 자산을 보유하고 단기 미국 국채에 직간접 투자. Minter는 승인된 결제 토큰과 가격 오라클로 1USD+=1USD 발행, Redeemer는 소각 시 최대 영업일 2일 소요. 스테이킹 보유 최소기간 위반 시 수익 몰수(잠금 메커니즘)
  - 원문: "The protocol mints and redeems 1 USD+ token for $ 1 USD value."
  - 위치: raw/assets.dinari.com/forms__usdplus-whitepaper.pdf.md / 1 INTRODUCTION, 2 SYSTEM ARCHITECTURE, 3 EARNING AND LOCKUPS
  - 틀: 사업 구조 > 상품 기초자산 > 가상자산 (USD+ 구조)
- 현재 docs는 "스테이킹 없이 일일 리베이스, 락업 없음"으로 설명(docs/what-is-usd). 2024년 백서의 Staked USD+ 구조는 변경되었거나 폐기된 것으로 보임(확인 필요)
- 백서 면책: 투자 권유가 아니며 의견은 변경될 수 있음
- 조사 질문 관련도: 중간
## 새로 나온 용어
- Staked USD+, Reserves Vault, Minter, Redeemer, ERC-4626
## 서로 어긋나는 서술
- 백서(2024-02)의 Staked USD+ 락업 구조와 현행 docs의 일일 리베이스 락업 없음
## 더 봐야 할 것
- usd.dinari.com/transparency(담보 구성), USD+ 발행 법인, 준비금 수탁기관 이름(사이트에 미기재, 제3자 수탁기관이라고만 표기)
