# STORY-Binance 리서치 노하우 (2026-11-17)

## 통한 경로
- binance.com 블로그와 공지는 curl에 202(봇 확인)로 막힘. Binance 보도자료는 prnewswire.com/news/binance/ 목록 페이지에 최근 20건 주소가 모두 있고, 각 보도자료 본문이 curl로 열림(옵션 출시, TradFi 무기한선물, 9주년, 첫 주 주식 데이터, Binance Pay, Capital Connect). AAP(aap.com.au, aapnews.aap.com.au) 사본도 열림.
- Binance 보도자료의 회사 숫자(주식 연계 무기한선물 월 거래대금, 기관 이용자 증가율, 슈퍼앱 목표)는 같은 날 매체 기사가 그대로 옮기므로 보도자료 원문을 1차로 쓴다.
- ESMA MiCA 등록부 CASPS.csv(Last-Modified로 기준일)를 grep하면 "MiCA 인가 없음"을 1차로 확인할 수 있다(Binance 0행).
- cointelegraph.com, decrypt.co, kitco.com, financemagnates.com, news.bizwatch.co.kr, thenationalnews.com은 curl로 열림. theblock.co는 경로에 따라 403(www 없는 news 경로와 post 경로).
- 아부다비 정부 미디어오피스(mediaoffice.abudhabi) 보도문에 UAE 직원 수(5,000명 중 1,000명)가 있어 Khaleej Times 단일 출처를 1차로 올릴 수 있었음.

## 함정
- 기존 DB와 본문은 Binance 주식 무기한선물 시작을 2026-10-29로 적었으나, 2026-09-01 옵션 보도자료에 2026-01 주식 연계 무기한선물 거래대금(4.109억 달러)이 있고 TradFi 무기한선물 상품군은 2026-01-08(금, 은)부터임. 10-29와 11-12는 종목 추가 공지. 2층 문구 정정 필요(이번 범위 밖이라 고치지 않음).
- Finance Magnates 기사 날짜(2026-07-15)와 내용(6월 출시)이 어긋남. 매체 날짜보다 보도자료 날짜를 기준으로 쓴다.
- 회사 9주년 보도자료의 "가상자산 보유자의 43%"는 회사 추산(분모 7.41억 명은 업계 추정)이라 회사 주장으로만.
