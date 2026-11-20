# db/ 읽는 법 (사실 DB, 2026-11-20)

이 폴더는 리서치의 뼈대입니다. 글(companies/, kb/)의 숫자와 날짜는 모두 여기 사실 한 줄에서 나옵니다.

## 표

| 파일 | 줄 수(2026-11-20) | 한 줄은 | 핵심 칸 |
|---|---|---|---|
| facts.csv | 2,773 | 사실 하나 | fact_id, 회사, 무엇을, 값, 단위, 무엇을 잰 것, 기준일, source_id, 링크, 원문 근거 문장, 원문 위치, 검증 상태 |
| sources.csv | 1,474 | 출처 하나 | source_id, 제목, 발행 주체, 발행일, 출처 종류, 링크, 저장 파일 경로(있으면 저장소 안 원문 사본) |
| licenses.csv | 30 | 회사 법인의 인가나 등록 하나 | 보유 법인, 등록 종류, 감독기관, 확보 방식(직접, 인수, 제휴), 등록부 링크 |
| relations.csv | 116 | 회사 사이 관계 하나 | 주체, 대상, 관계 종류, 지분율, 금액, 주는 것, 받는 것 |
| laws.csv | 88 | 법 조문 하나 | 법령명, 조항, 원문 발췌, 쉬운 풀이 |
| cases.csv | 18 | 감독기관 조치나 판결 하나 | 기관, 사건명, 결론, 그 뒤 달라진 것 |
| terms.csv | 179 | 용어 하나 | 쉬운 뜻, 헷갈리는 짝, 한국 대응 |
| third_party.csv | 92 | 제3자 보고서 숫자 하나 | 발행처, 쪽, 원문 |
| absent.csv | 229 | 찾았으나 없던 것 | 항목, 사유, 찾아본 곳 |
| blocked_links.csv | 123 | 열지 못한 링크 | 막힌 종류, 시도한 방법 |
| companies.csv | 8 | 토큰 상품 하나 | 발행 주체, 법적 성격, 투자자가 갖는 것 |
| _fact_id_map.csv | 2,773 | DB 번호와 원천 번호 대응 | F-xxxx, 작업 ID, 원천 fact_id |

## 번호 규칙
- fact_id(F-xxxx)와 source_id(S-xxxx)는 바뀌지 않음. 글과 화면은 이 번호로 인용함
- 원천은 work/<작업 ID>/facts.csv, sources.csv. tools/merge_db.py가 원천을 모아 db를 다시 만들고, 이미 있는 줄은 같은 번호를 지킴(_fact_id_map.csv)
- 그래서 db 줄을 고칠 때는 _fact_id_map.csv로 원천 줄을 찾아 원천도 같이 고침. db만 고치면 다음 병합 때 되돌아감

## 검증 상태(facts.csv)
| 값 | 뜻 | 줄 수 |
|---|---|---|
| 1차 출처 확인 | 공시, 당국 문서, 회사 원문과 문장을 대조함 | 1,921 |
| 단일 출처 | 매체 하나 등 한 곳에서만 확인 | 553 |
| 교차 확인 | 서로 다른 출처 둘 이상이 같음 | 121 |
| 제3자 데이터(단일 집계기관) | CoinDesk Data 같은 집계기관 숫자 | 60 |
| 충돌 | 출처끼리 다름(둘 다 적어 둠) | 30 |
| 사용자 제공 | 사용자가 준 자료 | 28 |
| 회사 주장 | 회사만 말한 것 | 20 |

## 찾는 법
```
python3 -I tools/fsearch.py "Bitstamp&인가"
python3 -I tools/fsearch.py --co Coinbase --status 1차 "Deribit"
python3 -I tools/fsearch.py --src "FinCEN"
python3 -I tools/fsearch.py --id F-1750
```

## 새 사실 넣는 법
1. work/<새 작업 ID>/facts.csv, sources.csv를 만든다(머리줄은 work/REV-RH/facts.csv와 같게, fact_id는 작업 고유 접두어)
2. 저장소 맨 위에서 `flock /tmp/kdx_merge.lock python3 -I tools/merge_db.py .`
3. 사람용 엑셀과 목록을 다시 만든다: `python3 -I tools/build_backdata.py <YYMMDD>`

## 알려진 결함(2026-11-20)
- F-2169, F-2171 등 Q2ON 작업 줄 일부는 링크 칸에 source_id가 들어 있음(칸 하나 밀림). 원문은 sources.csv의 같은 source_id 링크로 찾음
- F-2504, F-2530, F-2551, F-2552, F-2561은 검증 상태가 표준 값이 아닌 설명형 문장
- F-1814~F-1836(STAGE1-KR4)의 칸 밀림은 2026-11-20 원천과 DB 모두 고침
