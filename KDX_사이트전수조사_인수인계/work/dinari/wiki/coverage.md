# 수집과 반영 점검
확인일 2026-11-16. verify.md와 audit 결과는 이 폴더에 없다(Dinari는 verify 단계를 거치지 않음). 대신 facts.csv의 원문 근거 문장을 raw에서 기계 대조했다.

## 반영한 범위
- notes 8개 묶음: transparency, forms(백서), blog(19건 정독), case-studies(10건), dshares, home/business/usdplus/get-started, us와 bd, docs(13건). 위키와 facts.csv(100줄)에 반영했다.
- facts.csv 100줄의 원문 근거 문장은 모두 해당 raw 파일에서 글자 그대로 확인됐다.
- 숫자, 날짜, 인가 줄은 raw에서 grep -F로 다시 확인했다.

## 읽었으나 반영하지 않은 페이지와 사유
- docs/regional-requirements: 본문 없음(제목과 하위 링크만).
- docs/245-tradable-assets: 표가 수집되지 않음.
- dinari.com/bd/etp: 표준 ETP 위험 고지, 조사 관련도 낮음.
- 블로그 Korea Blockchain Week 2023 안내와 회고 2건: 행사 참가만 있고 한국 사업 언급 없음.
- docs 거래 휴장표, 코드 예제: 관련도 낮음.

## 읽지 않은 범위
- 블로그 54건: 제목과 날짜만 확인(종목 추가 알림, 월간 회고, 개별 체인과 파트너 출시 등).
- docs 보조 문서(security, managing-kyc, hosted-trading, wrapping, hyperliquid, dividend-payments 등), changelog, 감사 보고서 PDF, /bd/terms 전문(절 단위만), /bd/brokerage-agreement, business-continuity, privacy, market-data-terms.
- app.dinari.com의 trade, orders, portfolio, spcx 화면, partners, sbt, status 호스트.
