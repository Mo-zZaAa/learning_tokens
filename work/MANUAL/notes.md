# MANUAL 메모 (열람 기준일 2026-11-16)

## 문서 구조 주의
- "B03_coinbase_Q3_26_shareholder_letter"는 서한이 아니라 42쪽 실적 발표 슬라이드 형식이다. 쪽 번호는 pdftotext 쪽 구분 기준(1쪽 표지는 텍스트 없음). 중요한 값(거래대금, 영업이익 등)은 부록 표 p.30 31 35에 있다.
- "B03_coinbase_presentation"은 4쪽짜리 준비 발언(Armstrong, Haas) 녹취다.
- 그림 위주 쪽(p.11, 15 차트)은 텍스트 변환 때 수치가 섞여 있어 TTM 파생 거래대금($4,341B 등)과 토큰화 주식 주간 값은 사실로 넣지 않았다.

## 요청 항목 중 문서에 없는 것
- Coinbase Onchain SPV, ADGM, FSRA, Alpaca: 네 Coinbase 문서에 한 번도 나오지 않는다(키워드 검색 확인). 기존 DB(F-0076부터 F-0090)의 투자설명서 근거를 유지.
- 한국, 코인원, 서울경제 보도(F-0114): 네 문서 모두에 없음. 한국 관련 facts 없음.
- Deribit 인수 대가 42.9억 달러(F-0098), SEC 소송 종결(F-0107), 미국 선물 출시(F-0099), 주식 거래 개방과 8,000종목(F-0101), 텍사스 전환(F-0103), 이중 의결권과 이사회(F-0104부터 F-0106), 2025년 연간 총수익(F-0112), 2025 총거래량(F-0113): 이 문서들에서 확인 못함. F-0112는 p.20 차트 값을 합산하면 7.18B로 맞으나 차트 텍스트가 섞여 직접 근거로 쓰지 않음.
- 주식 거래(Coinbase 앱의 전통 주식): 이 문서에는 우선순위와 Pro 재출시 언급뿐이고 종목 수, 거래대금은 없다.
- 직원 700명 감축(F-0111): 4,204명만 확인. 감축은 "5월/2분기 발표 감원" 언급만.
- Backed 보충서에는 새 상품, 새 수탁기관, 발행 한도(issuance cap), 소유 구조 변경(지분율)이 없다. 실제 바뀐 것은 AP 2곳 명시, 기초자산 교체 조항, Payward 재정 의존 위험요인, 모회사 기여 계약과 IP 양도, 정기대출 보증, 이사회 4명, 스위스 원장기반증권 문구 정비, InCore 계약 날짜 정정, CARF 문구, 전문투자자 진술이다. Alpaca, Maerki Baumann은 보충서에 나오지 않는다. xStocks의 법적 성격(투자자는 기초주식 권리 없음)과 원주 1:1 담보 문장은 기본 투자설명서나 Final Terms에 있어 이 보충서로는 확인되지 않는다.

## 문서 간 불일치(검토 필요)
1. 토큰화 주식 거래대금: 주서한 p.15 "$1B+ volume on Base since launch"(Token Terminal 기준, 주간 차트 08/19부터 09/30), 준비 발언 p.2 "just crossed over $1 billion", 같은 날 애널리스트 콜 p.3과 AMA p.6 Haas "about $3 billion ... since launch"/"$3 billion ... tokenized on Base ... for our non-US customers". 같은 날 발언이 3배 차이. 측정 범위(Token Terminal 한정 대 회사 내부, DEX 외 포함 여부)가 다를 가능성이 있으나 문서에는 설명 없음. 본문에는 기준 병기가 필요하고 "10억 달러 이상(주서한 기준)"을 우선 사용하길 권함.
2. 법적 성격: Haas "real shareholder rights", Armstrong "You can get the upside from dividends. We're implementing voting rights"는 DB의 ADGM 투자설명서(배당 직접 지급 없음, 의결권 지시 노력 의무)와 다르다. 기존 F-0096과 같은 충돌 유형이며 투자설명서를 우선.
3. 발언 중 "SEC가 innovation exemption을 시작했다"는 내용은 법령 근거가 이 문서에 없으므로 US 에이전트가 확인해야 함.

## CLARITY Act
- 캡처 확인 내용: H.R.3633 Digital Asset Market Clarity Act, Sponsor Hill, J. French (R-AR-2), 발의 2025-05-29, 위원회 House Financial Services와 Agriculture, Senate Banking. Tracker는 Passed House까지 표시, 최신 조치는 2026-09-15 Tillis 의원의 클로처 재고 동의(Record Vote No. 234).
- 주의: 캡처의 검색어는 "Statement on Tokenized Securities"로, 이 법안은 검색 결과 1번이다. "클로처 미발동"은 이미 표결에서 클로처가 성립되지 않았다는 뜻이며 재고 동의의 결과는 캡처에 없다. 지정 링크는 캡처 외 직접 열람하지 않았다.

## verdicts
F-0110은 1차 출처 확인으로 상향, F-0111은 부분 확인이라 단일 출처 유지, F-0108과 F-0109(교차 확인)는 1차 출처 확인 상향을 제안했다. 나머지 Coinbase 단일 출처 줄은 이 문서로 확인되지 않아 올리지 않았다.

## 신규 용어
원장기반증권(Art. 973d CO), 승인 참가자, 시퀀서 수수료, SEC 혁신 면제, 무기한 선물, DCO, 보충서 (terms.csv).
