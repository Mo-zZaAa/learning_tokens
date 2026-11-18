"""여섯 회사 비전(한눈에 보기): 1층 카드 맨 앞 행과 Dinari, 6개사 공통 한 화면 카드 맨 앞 절에 넣는다.
원문은 사용자가 건넨 정리(2026-11-18). 다시 돌리면 같은 행을 바꿔 끼움."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
HEAD = ["회사", "스스로 쓰는 말", "\"다 하겠다\"의 범위", "출발점", "다가가는 방식"]
ROWS = [
 ["Coinbase", "Everything Exchange", "가상자산, 주식, 예측시장, 원자재를 현물, 선물, 옵션으로", "미국 1위 가상자산 거래소", "인가를 직접 받아 자기 앱에 얹음"],
 ["Kraken", "한 플랫폼, 한 장부", "어떤 자산이든, 언제든, 어디서든 + 남에게 빌려주기", "유럽 비트코인 거래소", "인가 가진 회사 인수 + 기존 거래소와 제휴"],
 ["Binance", "다중 자산 금융 슈퍼앱", "미국 주식에서 아시아 주식, 원자재까지", "세계 1위 가상자산 거래소(선물)", "아부다비 거점 인가 + 기존 이용자 3억 명에 얹음"],
 ["Robinhood", "금융 슈퍼앱, 세계 1위 금융 생태계", "투자, 은행, 은퇴, 예측시장, 토큰화로 전 세계에", "미국 개인 주식 앱", "같은 고객에게 더 많이 팔고, 커지면 거래소째 인수"],
 ["Ondo", "Wall Street 2.0", "미국 금융시장 전체를 블록체인 위로", "국채 토큰 발행사", "남의 거래소와 지갑에 도매 공급"],
 ["Dinari", "신뢰할 수 있는 자산을 접근 못 하는 사람에게", "미국 주식을 전 세계 앱에", "미국 주식 토큰 발행사", "API로 남의 앱에 붙음"],
]
DIR = {
 "coinbase": ("Coinbase: 2026 최우선 과제가 ==\"다 하는 거래소\"(Everything Exchange)==", [
   "CEO 원문: 손님이 원하는 모든 투자와 거래 상품을, 자산이 어디에 있든 ==하나의 믿을 수 있는 곳(one trusted place)==에서 하게 하겠다고 함",
   "2026 우선순위 셋: ① Everything Exchange를 세계로 넓히기 ② 스테이블코인과 결제 늘리기 ③ 개발자 도구, Base 블록체인, 소비자 앱으로 이용자를 온체인으로 데려오기",
   "최종 목표: ==세계 1위 금융 앱==",
   "출처: 2025 Q4 실적 발표 통화 녹취(Q4 25 Earnings Call Transcript)"]),
 "kraken": ("Kraken: ==다 하되, 그 기능을 남에게도 빌려줌==", [
   "원문: 누구나, 어떤 자산이든, 언제든, 어디서든 거래하게 하는 것(anyone can trade any asset, anytime, anywhere)",
   "지주회사가 아니라 ==하나의 플랫폼, 하나의 대차대조표, 하나의 규제 체계==라고 강조함",
   "사업 기둥 다섯: 거래, 은행, 자산관리, Payward Services, AI",
   "==다른 회사들과 달리 자기 앱 밖의 다른 금융회사 공급(B2B)까지 비전에 넣음==",
   "출처: [Payward 보도자료](https://www.payward.com/press-release/kraken-raises-800m)"]),
 "binance": ("Binance: ==가상자산 이용자를 그대로 둔 채 자산만 넓힘==", [
   "미국 주식 출시를 투자, 거래, 온체인 금융을 위한 ==다중 자산 금융 슈퍼앱==이라는 비전의 큰 걸음이라고 설명함",
   "다음 단계: 홍콩, 한국, 대만, 브라질 주식 접근을 검토하며 올인원 거래 플랫폼을 지향함",
   "이유: ==가상자산 경기에 덜 흔들리게 하는 것==(CEO 표현 weatherproofing)",
   "출처: [Ada Derana Biz](https://bizenglish.adaderana.lk/binance-launches-u-s-stocks-trading-and-previews-bstocks-tokenized-securities/), [Fortune](https://fortune.com/2026/10/13/crypto-binance-co-ceo-richard-teng/)"]),
 "robinhood": ("Robinhood: ==한 사람의 금융 생활 전체를, 전 세계로==", [
   "10년 전략: 세계 1위 금융 생태계(number one global financial ecosystem)",
   "축 셋: 활발한 투자자 1위, 다음 세대의 지갑 점유율 늘리기, 세계 1위 금융 생태계. ==토큰화는 세 번째 축의 핵심==",
   "토큰화로 노리는 것: ==미국에 있는 모든 자산을 전 세계 수십억 명이 쓸 수 있게 하기==",
   "출처: AlphaMaven 정리"]),
 "ondo": ("Ondo: ==자기 앱이 아니라 금융시장 자체를 블록체인으로 옮김==", [
   "2025 전략 이름 Wall Street 2.0: 미국 금융시장을 블록체인 위로 옮기는 인프라",
   "사명: 기관급 금융상품과 서비스를 누구나 쓰게 하는 것",
   "창업자가 2026-05 별세한 뒤에도 새 CEO가 사명은 그대로라고 밝힘",
   "출처: [Business Wire](https://www.businesswire.com/news/home/20250206421408/en), [yespress](https://yespress.io/ondo-finance)"]),
 "dinari": ("Dinari: ==미국 주식의 합법 표준이 되어 남의 앱에 공급함==", [
   "방향: 미국에서 합법적인 토큰 주식 표준을 만들어, 규제를 지키는 블록체인 주식 거래의 길을 여는 것",
   "CEO 원문: 주식의 미래는 전 세계적이고, 프로그래밍 가능하며, 늘 열려 있다(global, programmable, always available)",
   "방식은 B2B2C: ==자기 고객을 모으지 않고 다른 회사 앱을 통해 공급함=="]),
}
NAME = {"coinbase": "Coinbase", "kraken": "Kraken", "binance": "Binance", "robinhood": "Robinhood", "ondo": "Ondo", "dinari": "Dinari"}
ORDER = ["coinbase", "kraken", "binance", "robinhood", "ondo", "dinari"]

def table_for(slug):
    rows = [[("==" + c + "==") if (i == 0 and slug and r[0] == NAME[slug]) else c for i, c in enumerate(r)] for r in ROWS]
    return {"head": HEAD, "rows": rows}

def row_for(slug):
    t, kids = DIR[slug]
    others = [{"t": DIR[s][0], "kids": [{"t": k} for k in DIR[s][1]]} for s in ORDER if s != slug]
    return {"label": "한눈에 보기", "items": [
        {"t": "여섯 회사가 스스로 말하는 방향(비전)", "table": table_for(slug), "open": True},
        {"t": t, "strong": True, "open": True, "kids": [{"t": k} for k in kids]},
        {"t": "다른 다섯 회사의 원문과 방향", "kids": others}]}

for slug in ["coinbase", "kraken", "binance", "robinhood", "ondo"]:
    p = ROOT / f"kb/{slug}_overview/{slug}_overview.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["card"]["rows"] = [r for r in d["card"]["rows"] if r.get("label") != "한눈에 보기"]
    d["card"]["rows"].insert(0, row_for(slug))
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

def md_block(slug):
    L = ["## 한눈에 보기", "", "| " + " | ".join(HEAD) + " |", "|" + "---|" * len(HEAD)]
    for r in table_for(slug)["rows"]:
        L.append("| " + " | ".join(r) + " |")
    L.append("")
    for s in ([slug] if slug else []) + [s for s in ORDER if s != slug]:
        t, kids = DIR[s]
        L.append("- **" + t.replace("==", "") + "**" if s != slug else "- " + t)
        L += ["  - " + k for k in kids]
    return "\n".join(L) + "\n"

for slug, path in [("dinari", "kb/cards6/dinari.md"), (None, "kb/cards6/common.md")]:
    p = ROOT / path
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"\n## 한눈에 보기\n.*?(?=\n## )", "\n", s, flags=re.S)
    lines = s.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.startswith("## "))
    blk = md_block(slug).rstrip("\n").split("\n")
    lines = lines[:i] + blk + [""] + lines[i:]
    p.write_text("\n".join(lines), encoding="utf-8")
print("ok")
