"""Robinhood 1층 카드: 사용자 지적(빈 곳 5개)과 PM 질문 답 형광펜, 질문 번호 표시."""
import json
P = "kb/robinhood_overview/robinhood_overview.json"
d = json.load(open(P, encoding="utf-8"))
rows = {r["label"]: r for r in d["card"]["rows"]}

def walk(items):
    for it in items:
        yield it
        yield from walk(it.get("kids") or [])
        yield from walk(it.get("sub") or [])
def all_items():
    for r in d["card"]["rows"]:
        yield from walk(r.get("items") or [])
        yield from walk(r.get("path") or [])
def find(prefix):
    hits = [it for it in all_items() if (it.get("t") or "").startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]
def kid(t): return {"t": t}

# 무엇을 하나
it = find("미국 개인의 주식 주문을 받아")
it["t"] = "미국 개인의 주식 주문을 받아 시장조성자에게 넘겨 체결시키는 무수수료 증권사로 출발해, ==같은 손님 계좌에 옵션, 가상자산, 선물, 예측시장, 자문, 은행을 얹은 회사==(PM No 60)"
it = find("손님이 수수료를 안 내면 누가 내나")
it["t"] = it["t"].replace("주문을 넘겨받아 체결하는 시장조성자(늘 사고팔 값을 내는 회사)가 냄", "==주문을 넘겨받아 체결하는 시장조성자(늘 사고팔 값을 내는 회사)가 냄==") + "(PM No 60)"
# KDX가 볼 이유
it = find("(판단) KDX 구조에서 참여 증권사 자리")
it["t"] = "(판단) KDX 구조에서 ==참여 증권사 자리==에 서는 회사. 손님 계좌를 가진 증권사가 거래 시설까지 사면 무슨 일이 생기는지 보여 줌(PM 관점: KDX에 쓸 수 있나)"
it2 = find("KDX는 주문을 받는 시설 쪽")
it2["t"] = "KDX는 주문을 받는 시설 쪽. 참여 증권사가 이렇게 움직이면 !!KDX는 주문 경로를 잃을 수 있음!!(판단). 반대편의 답은 Rothera처럼 여러 중개사의 주문을 받는 독립 시설이 되는 것"
it["kids"].append(kid("볼지 뺄지: ==계속 봄==. 주식 토큰 때문이 아니라 증권사가 상품과 체결 시설을 어떤 순서로 붙이나의 미국 사례로(판단)(PM 관점: 볼지 뺄지)"))

# 가상자산
it = find("거래 기능이 모자라 샀나")
it["t"] = "거래 기능이 모자라 샀나: ==거래 기능보다 해외 인가, 기관 고객, 유럽 거점(PM 정리 \"유럽 전진기지\"가 맞음)==(PM No 62)"
it["kids"] = [kid("인가 차이: Robinhood Europe 인가는 손님 주문을 받아 남에게 넘기는 가게 자격, Bitstamp의 룩셈부르크 MiCA 인가는 사고파는 장터(거래 플랫폼)를 직접 여는 자격"),
              kid("산 뒤 쓴 곳: EU 가상자산 무기한선물 주문, 영국 가상자산(Bitstamp UK), 지갑용 주식 토큰의 유일한 1차 청약 창구(Bitstamp Global)")]
it = find("EU: 리투아니아 법인 Robinhood Europe")
it["t"] = "EU: 리투아니아 법인 Robinhood Europe. 2023 국가 등록(가상자산 사업자, VASP)으로 시작 → 2023-12 앱 출시 → ==2025-06 리투아니아 중앙은행에서 MiCA(EU 가상자산 규정, Markets in Crypto-Assets)와 MiFID II(EU 증권 중개 규정, Markets in Financial Instruments Directive) 인가==. 다른 EU 나라는 패스포트(한 나라 인가로 신고만 하고 영업)(개념 지침 No 8)"
it = find("캐나다: WonderFi")
it["kids"] = [kid("값이 Bitstamp와 비슷한 이유: 매출 대비로는 더 비쌈(Bitstamp 직전 12개월 매출의 약 2.4배, WonderFi 2024 매출의 약 4배, 계산). ==(판단) 시장 크기보다 \"캐나다 입장권\" 값. 새로 등록하면 더 길고 불확실==(PM No 63, 셀프 챌린지 13)")]

# 예측시장
it = find("수수료가 거의 상한에 붙음")
it["t"] = "매출 나눔: ==1.73억 달러 중 Rothera 약 0.28억, 나머지 약 1.45억이 중개 수수료==(실적 자료 각주, 차감 계산). 계약 164억 건으로 나누면 건당 약 1.05센트로 상한 1센트와 비슷(셀프 챌린지 12)"
it = find("Rothera(2026-01): 시장조성 회사")
it["t"] += ". 이 세 인가가 MIAXdx 인수로 더해진 것"

# 맡긴 돈과 빌려준 돈
it = find("맡긴 돈과 빌려준 돈, 구독:")
it["t"] += "(개념 지침 No 10)"
it["kids"].insert(0, kid("==Robinhood는 은행이 아님. 손님이 받는 이자는 Robinhood 이자가 아니라 제휴 은행 예금 이자==(주체를 밝혀 씀)(개념 지침 No 10)"))
it["kids"].insert(2, kid("순이자 4.15억 달러 안(2026 Q3): 신용 매수 2.44억, 손님 분리 현금 이자 0.55억, 신용카드 0.50억, 회사 현금 0.47억, Cash Sweep 0.45억, !!주식 대여 -0.19억(1년 전 +0.87억)!!"))
it = find("Cash Sweep: 투자하지 않은 손님 현금")
it["t"] += ". 1,000달러면 Robinhood 몫 연 약 6달러(순이자 0.45억 ÷ 잔액 323억 = 연 약 0.59%, 계산)"
it = find("TradePMR은 돈을 굴리나")
it["t"] = "TradePMR은 돈을 굴리나: ==아님. 자문사(RIA)에게 계좌 보관(수탁)과 주문, 관리 도구를 빌려주는 회사. PM이 말한 \"IRP처럼 전략대로 굴려 주는 것\"은 Robinhood가 직접 하는 Robinhood Strategies==(PM No 64). 체결, 청산, 대출은 Wells Fargo Clearing Services"

# 주식 토큰
it = find("주식 토큰(2025-06~)")
it["t"] += "(PM No 65: 주식 토큰은 이 한 곳에 모음)"
it["kids"].insert(0, kid("\"지갑판\"이 뭐냐: ==우리가 지은 말. 원래 이름은 Stock Tokens(Robinhood Wallet용, 미국 밖 120여 개국)==. EU 앱 것은 Classic Stock Tokens(처음 이름 Robinhood Stock Tokens)(PM No 58)"))
it["kids"].insert(1, kid("주식 소유권이 있나: ==둘 다 주식 소유권도 의결권도 없음==. Stock Tokens는 저지 발행사가 써 준 담보 붙은 차용증(채무증권), Classic은 Robinhood Europe과 맺은 계약서(장외 파생상품)(PM No 59)"))
it = find("돈: 회사 수수료와 스프레드 0, 유로와 달러 환전")
it["t"] += ". 환위험은 누가 지나: 회사는 원주를 사서 가격 위험만 헤지하고, 손님이 유로를 달러로 바꿔 사는 구조라 ==환율 위험은 손님 쪽==(판단)(개념 지침 No 29)"
it = find("회사가 망하면: 따로 떼어 둔 담보가 없어")
it["t"] = "회사가 망하면: 따로 떼어 둔 담보가 없어 !!원금 전부를 잃을 수 있음!!. 회사가 사 둔 주식은 위험을 줄이려는 헤지이고 손님 담보가 아님"
it = find("기록: 자체 블록체인 Robinhood Chain")
it["t"] = "기록: 자체 블록체인 Robinhood Chain(2026-07-01 메인넷, 이더리움 위 레이어 2, Arbitrum 기술). ==지갑용은 이 체인 위에서 발행하고 거래, EU판은 앱 안에서만 돌고 체인과 무관==. 처음엔 남의 체인 Arbitrum One에 냈다가 옮겨 인프라를 직접 통제(개념 지침 No 21)"
it = find("체인이 버는 돈:")
it["t"] = it["t"].replace("Robinhood 몫은 누적 약 5,000만 달러까지 50%, 약 1.5억 달러까지 70%, 그 뒤 85%", "==Robinhood 몫은 누적 약 5,000만 달러까지 50%, 약 1.5억 달러까지 70%, 그 뒤 85%==") + "(PM No 66, 셀프 챌린지 14)"
it = find("1차 청약 창구: Bitstamp Global")
it["t"] += ". 승인된 한 곳만 받으니 !!그 회사에 문제가 생기면 공급이 멈출 수 있음!!. 청약 0%, 발행일부터 90일 안 상환 0%, 그 뒤 0.05%"
it = find("크기: 토큰 보유자에게 갚을 돈")
it["t"] = "크기: 토큰 보유자에게 갚을 돈 1.85억 달러, 손님 자산 3,960억 달러의 ==약 0.05%==(2026-09-30, 계산). 지갑용 발행 잔액 1.49억 달러(2026-11-16, rwa.xyz, 재는 기준이 다름). ==(판단) 성장 동력이 아니라 해외용 상품 중 하나==(PM 관점: 숫자의 함의)"
it = find("EU 비상장 토큰: 출시 때")
it["t"] += ". 2026-03 비상장 회사 지분을 담은 펀드 RVI를 뉴욕증권거래소에 상장하는 방식으로 바꿈(규모 6.55억 달러, 운용보수 연 2%). 2026 Q3 RVI 평가 손실 6,700만 달러가 순이익에 반영(PM 관점: 상충과 위험)"
it = find("Robinhood가 돈을 버는 시점과 돈이 쌓이는 곳")
it["t"] += "(PM 관점: 돈을 실제로 어디서 버나)"

# 숫자
it = find("순이익: 2020 700만 달러 흑자")
it["t"] = "순이익: 2020 700만 달러 흑자, ==2021~2023 적자, 2024 14.1억, 2025 18.8억 달러 흑자==. 거래가 식을 때 이자가 받쳐 줌(PM No 4)"
it = find("어떻게 세나: 최근 45일")
it["t"] = "\"펀디드\"가 뭐냐: ==서비스가 아니라 회사가 공시하는 손님 수 지표 Funded Customers==. 최근 45일 안에 계좌 잔액이 0보다 컸거나 거래한 사람 수(계좌 수 아님). 장표에 이 정의를 같이 적음(PM No 61)"
it = find("외부에서 받은 돈: 상장 전 벤처")
it["t"] += "(PM No 1)"
it = find("2021-02 34억 달러는 왜 급히 받았나")
it["t"] += ". 원리: 결제가 끝나는 이틀 동안 증권사가 못 갚을 위험에 대비해 청산소(NSCC)가 담보를 받는데, 값이 크게 흔들리면 그 담보가 급증함"

# 확장 경로: 고객 확장 TradePMR
it = find("TradePMR로 얻은 것")
it["t"] += ". TradePMR은 돈을 굴리지 않고 자문사에게 계좌와 도구를 빌려줌. IRP처럼 굴려 주는 것은 Robinhood Strategies(PM No 64)"
for p in rows["확장 경로"]["path"]:
    if p["k"] == "파트너십":
        p["kids"].append(kid("빌드, 바이, 파트너 규칙: ==미국 안 상품은 대체로 직접, 해외와 거래소는 삼, 새 상품은 제휴로 먼저 열고 커지면 삼==(PM 관점)"))
    if p["k"] == "시장 확장":
        p["kids"].insert(0, kid("자산과 투자자의 소재지: 해외 자산은 없음(미국 주식만 토큰으로). ==넓힌 것은 해외 투자자 쪽뿐==(PM 관점)"))

# 배울 점
it = find("새 거래 시설의 첫 거래량은")
it["t"] += "(PM No 3)"
it["kids"].insert(0, kid("권한을 주면 뭐부터: ==이미 가진 인가와 손님으로 새 상품을 먼저 열고(예측시장을 선물 중개 인가로, 주문은 Kalshi로), 매출이 확인되면 시설을 삼==(PM No 3)"))
it = find("손님 수를 먼저 모은 계좌가")
it["kids"].append(kid("\"수수료 0이니 할인 많이 해 주면 되나\": ==수수료 0은 출발 무기였을 뿐. 덩치는 같은 손님에게 옵션, 예측시장, 이자를 얹어 키움==(손님 1명당 매출 103 → 200달러). ==KDX에 쓸 것은 가격이 아니라 이미 있는 손님 통로 위에 상품을 얹는 순서==(PM No 44)"))
it["kids"].append(kid("PB 유인 설계: TradePMR(자문사에게 계좌와 도구를 빌려줘 끌어들임)이 KDX가 증권사 PB를 끌어들이는 설계와 닿음(판단)"))
it = find("사고의 버킷: Kraken, Ondo와 무엇이 다른가")
it["kids"].insert(0, kid("여러 회사에 공통으로 쓸 문장은 하나: ==남의 시설로 먼저 열고, 커지면 시설을 산다==(Coinbase 예측시장도 같은 흐름). 나머지 배울 점은 이 회사만의 판단으로 둠(PM No 2)"))

# 주의할 점
rows["주의할 점"]["items"].append(kid("제재: 2025-01 SEC 과징금 4,500만 달러, 2025-03 FINRA 벌금 2,600만 달러(손님 환급 375만), 2024-12 미인가 영업으로 2개 주 벌금"))
rows["주의할 점"]["items"].append(kid("지갑용 토큰: 저지 비규제 발행사, 1차 청약 창구 한 곳. 2026-11 보충서로 이미 발행된 상품의 약관을 고침(기초자산 관련 비용 등)"))

# 그림: 주식 토큰 EU 단계, 예측시장 첫 단계
fl = d["flows"]["token"]["stages"][3]
fl["sum"] = "회사가 망하면 따로 떼어 둔 담보가 없어 원금 전부를 잃을 수 있음. 회사는 주가 위험만 헤지하고 환율 위험은 손님 쪽(판단)"
ev = d["flows"]["event"]
ev["footbox"] = "돈이 쌓이는 곳: 이벤트 계약 매출 1.73억 달러(2026 Q3, 순매출의 12%) 중 Rothera 약 0.28억, 중개 수수료 약 1.45억(실적 자료 각주, 차감 계산)"
ins = d["flows"]["interest"]["stages"][0]
ins["sum"] = "은행이 주는 이자 - 손님에게 주는 이자 = Robinhood 몫. 1,000달러면 연 약 6달러(2026 Q3 연 약 0.59%, 계산). 금리 1%p가 내리면 연 순매출 3.66억 달러 감소(회사 계산)"
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
