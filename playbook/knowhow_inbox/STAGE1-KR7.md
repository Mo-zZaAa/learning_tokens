# STAGE1-KR7 리서치 노하우 (Kraken 수익 추이, 투자 유치, 인수 대금)

- Kraken 연간, 분기 실적 글은 blog.kraken.com/news/ 아래에 있고 curl로 열림: kraken-2024-financials, kraken-q1-2025-financials, kraken-q2-2025-financials, q3-2025-financial-highlights, kraken-2025-financials. 주소 목록은 사이트 전수조사 inventory.csv(KDX_사이트전수조사_인수인계/work/kraken)에서 "financial"로 찾음. payward.com 사이트맵에는 2025년 분기 글이 없음.
- 숫자는 본문보다 글 안 그림(PNG)에 더 많음. 본문 HTML의 article 안 img 주소를 뽑아 내려받아 읽음. 그림 파일 이름 끝의 _20251202는 고친 날짜이고, 고친 그림에는 전년 같은 분기와 2023년 값까지 있음(2023 조정매출 6.963억, 조정 EBITDA -0.765억).
- 함정: 2024, 2025 Q1, Q2 글은 2025-12-02에 숫자를 새 기준(조정매출)으로 고쳤음(article:modified_time). 처음 발표 숫자는 매체가 인용한 원문(Daily Hodl, Cointelegraph, FX News Group)으로 확인. 본문 증가율과 그림 증가율이 다른 곳도 있음(2025 Q1 본문 18%, 그림 15%).
- web.archive.org 스냅샷은 이 세션에서 연결이 끊김(archive.org 가용성 API만 열림). 고친 글의 옛 판은 매체 인용으로 대신함.
- 비상장 인수 대금의 현금과 주식 비율은 매수자보다 상장 매도인 공시에 나옴: IG Group RNS 5408D(Small Exchange, 현금 3,250만, Payward 주식 6,750만 달러). LSE 원문 사본(sharesmagazine)은 본문이 비고, financialreports.eu 사본이 curl로 열림. 같은 공시 주석에 "주식 대가는 규제 자본에서 제외"가 있어 비상장 주식 대가의 한계를 보여 줌.
- 투자자 쪽 보도자료가 거래 성격을 더 정확히 씀: Deutsche Börse 보도자료(deutsche-boerse.com, curl 열림)가 구주 매입(secondary)과 완전 희석 1.5%를 밝힘. Payward 쪽 글에는 투자 사실이 없음.
- 막힌 곳: coindesk.com(429), fortune.com(403), theblock.co(403), finextra, lse.co.uk, fxstreet, invezz(403), yahoo(429). 같은 내용은 cointelegraph, decrypt, financemagnates, unchainedcrypto, siliconangle(모두 curl 200)로 찾음.
