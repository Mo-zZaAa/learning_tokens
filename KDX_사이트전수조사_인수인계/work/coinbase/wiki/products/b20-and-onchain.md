# B20 표준과 온체인 구조

확인일: 2026-11-16. 사이트 문서와 블로그의 설명이다.

## B20
- 토큰화 주식은 B20 표준 위에 구축된다. B20은 ERC-20의 확장이고 자산 종류에 중립적이다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- 블로그는 B20을 Base 네이티브 토큰 표준으로 소개한다. [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 토큰화 주식은 별도 배포 컨트랙트가 아니라 B20 네이티브 프리컴파일이며 토큰별 컨트랙트가 없다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)

## 배수
- 1 B20 토큰은 영구적으로 1주와 같지 않고 현재 배수를 곱해 환산한다. 예시: 배수 1.02이면 1토큰은 1.02주로 상환 가능. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- 토큰 가격 = 기초 주식 시장 가격 x 배수. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- 순 2% 배당은 배수를 약 1.02로, 2대1 분할은 1.02에서 2.04로 올린다는 예시. AMM 풀의 ERC-20 잔액은 변하지 않는다. [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 배수 업데이트는 예약형이 권장되고 즉시형은 폐기 예정인 비상 장치. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)

## 정책과 통제
- 정책은 전송을 허용하거나 거부한다. 정책은 공유 Policy Registry에 있고 여러 토큰이 참조할 수 있다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base) [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 법적 요건 충족을 위해 동결과 압류(freeze and seize) 기능을 추가했다고 블로그가 밝힌다. [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)
- 특정 함수 일시정지가 가능하며 온체인 일시정지는 드물다고 설명한다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- AP의 민팅과 상환 가능 여부, 미국 장외 시간 가격 피드 동작 같은 운영 통제는 토큰 위에서 이루어져 B20이 강제하지 않는다. [출처](https://www.base.org/blog/b20-tokenized-stocks-on-base)

## 가격 피드
- 주식 가격 피드는 Chainlink가 제공하며 24/5 운영, 주말과 휴일은 마지막 종가를 유지하고 기업행위 중에는 동결된다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)
- Coinbase 피드는 원시 주가 대신 Total Return Values를 보고한다. [출처](https://docs.base.org/base-chain/asset-issuance/tokenized-stocks-on-base)

## Base 약관(Coinbase Technologies, Inc.)
- 최종 개정일 2026-04-08. [출처](https://docs.base.org/terms-of-service)
- Coinbase Sequencer는 Coinbase가 운영하는 노드이며 수수료를 부과하고 변경할 권리를 보유한다. [출처](https://docs.base.org/terms-of-service)
- Bridging Smart Contracts는 Ethereum, Base, 기타 호환 네트워크 사이 자산을 브리지한다. [출처](https://docs.base.org/terms-of-service)
- 서비스 이용 자격은 제재 관할에 있지 않을 것. [출처](https://docs.base.org/terms-of-service)
