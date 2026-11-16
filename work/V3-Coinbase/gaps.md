# V3-Coinbase 공백 (companies/Coinbase_v3.md)

## 본문에 못 쓴 것(근거 없음 또는 검증 상태 미달)
- 모회사 Coinbase Global 설립 연도, 본사 소재지: facts.csv에 사실 없음. 창업자는 발언자 직함(F-1056 "Co-Founder and CEO")으로 Armstrong만 씀. 공동 창업자 전원 명단 필요.
- 텍사스 법인 전환(F-0103), 이중 의결권 78.6%(F-0104), 주요 주주(F-0105): 단일 출처라 지배구조에 못 씀. 주요 주주 칸 비어 있음.
- 1년 전 대비 시장 내 위치: 상품 출시가 2026-08(F-0776)이라 rwa.xyz 1년 전 값 자체가 없음. 출시 직후 값(2026-08~09) 같은 출처로 확보하면 성장률 비교 가능.
- 거래대금 수치 충돌: 주주서한 2026-09말 누적 10억 달러 이상(F-0892), CEO 10억 돌파(F-0893), CFO 출시 이후 약 30억(F-0894). 기준일 또는 집계 범위(Base 전체 vs Coinbase 발행분) 차이 미해소. 본문은 둘 다 쓰고 "기준 차이"로 표기.
- base.org/markets 지표(24시간 거래량, 45종목, 종목별 유동성, 연결 지갑 13곳, Aave/Morpho와 상업적 관계, 휴장 중 담보 청산): F-0812~F-0851 모두 단일 출처. 교차 확인되면 D 공급 방식(Coinbase Wallet, Bitget Wallet, 1inch 등 연결 지갑)과 리스크에 넣을 수 있음.
- 종목 수 충돌 가능: 열람일 안내 표 10종(F-0093) vs 출시 기사 13종(F-0094, 단일) vs markets 표 45종(F-0816, 단일, Reserve MAG7 등 타 발행사 포함). 본문은 F-0093만 사용.
- 배당, 의결권 권리 충돌: 보도자료 "전면적 주주 권리"(F-0096 충돌), "직접 선순위 청구권"(F-0743 충돌), "1:1 실제 주식"(F-0778 충돌). 투자설명서(F-0086, F-0995) 기준으로 씀.
- Coinbase 자체 앱(Coinbase 앱, Base App, Coinbase Wallet)에서 주식 토큰을 직접 파는지: 1차 근거 없음(F-0820은 단일 출처). 자체 앱 판매 여부와 그 고객층 확인 필요.
- 파트너의 고객: Aerodrome, Aave, Morpho, Virtuals, Treasures 각각의 이용자 규모나 지역 근거 없음. partners.csv도 "고객 구성 미공개".
- 미국 밖 적격 관할 목록: 한국이 포함되는지 근거 없음. 제한 국가 목록 원문 필요.
- G 한국 접점: 코인원 지분 투자 논의 보도(F-0114, F-0115) 단일 출처라 G 절을 뺌.
- Deribit 인수 대가(F-0098 단일), 미국 주식 거래 8,000종목 전면 개방(F-0101 단일), 2025 총거래량(F-0113 단일): 못 씀.
- ADGM 쪽 law_id 없음: FSMR 58(2)(b), Schedule 1 para 92(F-0079 근거 인가 칸) 조문을 db/laws.csv에 등록하면 한국 시장과의 차이 "가능했던 이유"에 law_id를 붙일 수 있음.
- 미국 브로커딜러 Coinbase Capital Markets(F-0245, 1982 등록)는 주식 토큰과의 관계 근거가 없어 E에서 뺌.

## 화면과 캡처
- 로고: coinbase.com/brand가 HTTP 403(봇 차단)이라 captures/Coinbase/logo.png는 base.org 헤더의 Base 마크(파란 사각형). 본문은 "Base 로고"로 표기. Coinbase 로고 재캡처 필요.
- 가입, 종목 목록, 주문: coinbase.com 봇 차단으로 base.org 홈, base.org/stocks, base.org/markets/stocks 캡처로 대신(captures/index.csv). 실제 가입 절차와 주문 화면(지갑 연결, 스왑)은 아님. 세 캡처 모두 쿠키 배너가 화면 일부를 가림.
- 종목 목록 캡처(list.png)는 base.org/stocks 소개 화면, 실제 종목 표는 order.png(markets) 하단에 일부만 보임.

## 경영진 발언 링크
- 발언 4건 모두 사용자 제공 PDF(inputs/manual/B03_*)라 공개 URL 없음. Coinbase IR 공개 녹취나 영상 URL로 바꾸면 좋음.
