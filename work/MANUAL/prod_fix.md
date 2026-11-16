# work/PROD/companies.csv Kraken xStocks 줄 수정 제안 (직접 수정 안 함)
근거는 모두 Backed Assets (JE) Limited 2차 보충서(2026-09-29, 사용자 제공, inputs/manual/B01_backed_base_prospectus_second_supplement_20260929.pdf)이며 사실은 work/MANUAL/facts.csv의 MANUAL-027부터 042에 있다.

1. 발행 주체 법인명과 소재지: 유지. 보충서 첫 쪽이 Backed Assets (JE) Limited, St. Helier, Jersey를 확인한다(p.1).
2. 토큰의 법적 성격: 분류 "제3자 합성형(연계증권)"은 유지해도 되나 근거 문장에 보충서 p.11을 추가할 것. "ledger-based securities according to article 973d CO under Swiss law ... The entitlement to the securitized Securities exclusively results from the Securities Ledger." 토큰의 법적 형식이 스위스 원장기반증권임을 보여 주고, 기초주식에 대한 권리 문장은 보충서에 없다(기존 hanfa.hr 문장을 유지).
3. 원주 1대1 보유: 보충서는 1:1 담보 문장을 새로 쓰지 않는다. p.9의 "finance the purchase of the Collateral"만 보강. 또 기초자산이 합병 등으로 교체되면 단위가 최초 1:1 변동 단위와 달라질 수 있다는 단서(p.13)를 칸 비고에 추가 권장.
4. 원주 보관처: 값은 유지(Maerki Baumann, InCore, Alpaca). 보충서가 확인하는 것은 InCore Bank AG(Swiss Collateral 보관, p.8)뿐이고 미국, 영국 보관계약은 정의에만 나오며 보관기관 이름이 없다(p.2). Maerki Baumann과 Alpaca는 이 보충서로 확인되지 않으므로 기존 hanfa.hr 근거를 유지할 것.
5. 새로 넣을 만한 칸(열이 있다면): 제공 법인(승인 참가자) Payward Digital Solutions Ltd(버뮤다, BMA Class F)와 Payward Europe Digital Solutions (CY) Limited(키프로스, CySEC 342/17)(p.6). 모회사 Backed Finance AG, 토큰화 서비스 계약 상대 Payward, Inc.(2026-01-05, p.3-5).
6. 위험: 신규 위험요인 "Payward 그룹 재정 의존"(p.4). Payward와 PEL은 발행사 채무를 보증하지 않는다. 시나리오 설명 때 고객 화면 Kraken과 발행사 채무 책임이 별개임을 보여 주는 문장으로 쓸 수 있음.
7. 미국 판매 안 함, 자체 고객 화면, 검증 상태 칸: 보충서에서 직접 확인되지 않아 변경 없음.
