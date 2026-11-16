# Securitize, tZERO 제3자 자료 정리 (TP 행)

주황: 추가 확인 대상, R1은 Securitize 후원 보고서

본문 파일이 없어 여기에만 적는다. db/facts.csv에는 넣지 않았다. 이 내용은 모두 제3자 자료이며 1차 자료(Securitize 약관, 공시, 발표)로 확인되기 전에는 사실로 쓰지 않는다.

## Securitize
● 직접 방식 절차 [TP-231] (포필러스 R1 32쪽, Securitize 후원)
  ★ 투자자가 증권사 보유 주식을 DRS로 명의개서대리인에 직접 등록
  ★ 예시 종목 Exodus Movement(EXOD), 명의개서대리인 Pacific Stock Transfer
  ★ 확인되면 Securitize 계좌에 반영, Securitize Markets(ATS) 거래 또는 Algorand 토큰 인출
  ★ 8절 확인 결과(F-1133, Securitize 발표 2022-02-22): PST 고객과 주주에게 자본조달, 2차 거래, 블록체인 기반 주식 관리와 주식 토큰화 선택권을 주려고 인수. 당시 PST는 계정 120만, 고객 3,000곳 이상, 미국 상위 10 명의개서대리인
  ![직접 방식 흐름](../captures/reports/R1_p22_direct_tokenization.png)
● Superstate [TP-232] (R1 33쪽)
  ★ Securitize처럼 DRS 방식(Opening Bell), 발행사가 주주명부 관리
● 규제 자격 3종 평가 [TP-233] (R1 48~49쪽, Securitize 후원이라 자사 평가 성격)
  ★ 명의개서대리인, 브로커딜러, ATS로 발행부터 유통까지 규제 안에서 운영
  ★ 투자자가 전통 증권과 같은 의결권, 배당권을 가진다고 평가
● 생애주기 비교 [TP-234] (R1 68~72쪽)
  ★ 발행 명의개서대리인, 유통 자체 ATS와 OTC 시장조성자, 가격 Reg NMS 범위 확인
  ★ 담보 허가형 생태계, 상환 DTCC 또는 증권계좌 이전
  ![생애주기](../captures/reports/R1_p68_lifecycle_diagram.png)
● 직접 방식의 한계 [TP-235] (R1 77쪽)
  ★ 법적 소유는 온전하나 어떤 상장주식이든 토큰화하는 간접 방식보다 유연성 낮음
● 비교표 Securitize 열 [TP-236] (CoinDesk Research, Bullish 의뢰, 2026-08 기준, R2 10쪽)
  ★ 발행사 주도, 토큰이 곧 주식, DRS 등록부, 주주권 전부, 글로벌 24/7 대기(Pending)
  ★ 2차 유동성 틈새 ATS, 화이트리스트, 미국 규제 준수, DTCC 상환
  ![비교표](../captures/reports/R2_p10_provider_comparison_table.png)

## tZERO
● 배정된 R1, R2 쪽(31~33, 48~49, 68~72, 77, R2 10)에 tZERO 내용이 없다(R1 전체 텍스트에도 언급 0). 지어내지 않고 비워 둠.

## TP 행
TP-231~TP-236 (work/TP-B/third_party.csv, db/third_party.csv에 합침)
