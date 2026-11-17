# US-1 kb 초안 (미국 제도, 2026-11-16 열람)

## 1. 증권의 정의
- 미국 증권법은 증권을 목록으로 정의한다. 주식, 채권, 투자계약, "일반적으로 증권이라 불리는 것"이 들어간다. 1933년법과 1934년법의 목록은 거의 같다.
- 1934년법은 통화와 만기 9개월 이하 단기 어음류를 증권에서 뺀다.
- 증권이면 등록 또는 면제 없이 팔 수 없다(1933년법 Sec 5).
- 근거: US-1933Act-2a1, US-SEA-3a10, US-1933Act-5a
- 링크: https://www.law.cornell.edu/uscode/text/15/77b , https://www.law.cornell.edu/uscode/text/15/78c

## 2. 투자계약과 Howey 기준
- 토큰이 목록에 없어도 "투자계약"이면 증권이다. 1946년 Howey 판결이 기준을 정했다.
- 기준: 돈을 공동사업에 넣고, 남(발기인이나 제3자)의 노력에서 이익을 기대하는 계약이나 거래.
- 증서 형태가 아니어도 상관없다. 그래서 토큰이라는 형식은 판단을 바꾸지 않는다.
- 근거: US-C-Howey (cases.csv), US-1933Act-2a1
- 링크: https://www.law.cornell.edu/supremecourt/text/328/293

## 3. 가상자산과 증권의 경계 (2025~2026)
- SEC는 2026-03-17 해석에서 가상자산을 5종으로 나눴다: 디지털 상품, 디지털 수집품, 디지털 도구, 스테이블코인, 디지털 증권. 디지털 증권만 증권이고, 스테이블코인은 성격에 따라 다르다. (SEC 제안문의 요약으로 확인, 해석 원문은 미확인)
- 증권이 아닌 토큰도 투자계약 아래 팔리면 그 거래는 증권이다.
- 2026-08-21 SEC는 Regulation Crypto Assets를 제안했다: 5백만 달러(4년) 및 7천5백만 달러(12개월) 등록 면제와 투자계약 안전지대. 의견 마감 2026-10-20, 아직 제안 단계.
- 근거: US-SEC-2026Interp, US-SEC-RegCrypto-91FR54510
- 링크: https://www.govinfo.gov/content/pkg/FR-2026-08-21/html/2026-17183.htm

## 4. 토큰화 증권
- 토큰화해도 증권이라는 SEC 직원 성명(2026-01-28)이 있다고 하나 원문은 sec.gov 403으로 못 열었다. 확인 후 반영한다. 직원 성명은 법적 효력이 없다고 SEC 제안문이 밝힌다.
- 확인된 사례: 2026-09 SEC는 토큰화 상장주식을 AMM 풀에서 거래하는 장소에 "거래소"와 "딜러" 정의 면제를 한시 조건부로 줬다. 주식은 증권으로 두고 거래 장소 규제만 면제한 구조다.
- 근거: US-SEC-TokenizedNMS-91FR60168, US-SEC-StaffTokenized-2026
- 링크: https://www.govinfo.gov/content/pkg/FR-2026-09-22/html/2026-19388.htm

## 5. 시장구조 법안
- CLARITY Act(H.R. 3633)는 2025-07-17 하원을 통과했다. SEC와 CFTC가 디지털 상품 규제를 나눠 맡는 체계다.
- 상원 현황(위원회 통과, 본회의 표결 결과)은 congress.gov를 열지 못해 미확인. 로펌 해설에는 9월 상원 종결투표 부결이 있으나 원문 확인 전이다.
- 근거: US-HR3633-CLARITY
- 링크: https://www.govinfo.gov/content/pkg/BILLS-119hr3633eh/html/BILLS-119hr3633eh.htm

## 6. 감독기관 역할 분담
- SEC: 증권 판단, 증권 등록, 거래소와 브로커-딜러 등록(1934년법 Sec 6, 15).
- CFTC: 지정 계약시장의 선물과 스왑에 배타적 관할(CEA Sec 2). "상품" 정의가 넓어 증권 아닌 가상자산이 들어갈 수 있다(CEA Sec 1a(9)).
- FINRA: 브로커-딜러 자율규제기구. 조문상으로는 SEC에 등록한 "전국 증권협회"(Sec 15A).
- 주: 연방 covered security에는 주 등록 요건이 적용되지 않는다(1933년법 Sec 18). 그 밖의 증권과 사기는 주 감독기관이 본다.
- 근거: US-SEA-6a, US-SEA-15a, US-SEA-15A, US-CEA-2a1A, US-CEA-1a9, US-1933Act-18
- 링크: https://www.law.cornell.edu/uscode/text/7/2 , https://www.law.cornell.edu/uscode/text/15/78o-3
