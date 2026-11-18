"""A4 양식 JSON 점검: python3 -I kb/a4/check.py <slug>"""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BANNED = ["제공", "지원", "확대", "강화", "통합", "연결", "운영사", "발행 대행", "백단", "미확인", "확인 필요", "미정", "—", "–", "·", "PM", "승준", "건호", "경수", "F-0", "F-1", "F-2", "http"]
ALLOW = ["외국인 통합계좌", "TradePMR"]
slug = sys.argv[1]
d = json.loads((ROOT / f"kb/a4/{slug}.json").read_text(encoding="utf-8"))
err = []
for k in ("name", "view", "sections"):
    if not d.get(k): err.append(f"{k} 없음")
def kids(lst, where):
    for x in lst or []:
        if not isinstance(x, dict) or not x.get("text"): err.append(f"{where}: kids 줄에 text 없음 {str(x)[:60]}")
        else: kids(x.get("kids"), where)
for s in d.get("sections", []):
    if not s.get("title"): err.append("절 제목 없음")
    for b in s.get("blocks", []):
        t = b.get("type"); w = f"{s.get('title')}/{b.get('label', t)}"
        if t == "bullet":
            if not b.get("label") and not b.get("text"): err.append(f"{w}: label, text 둘 다 없음")
            kids(b.get("kids"), w)
        elif t == "chain":
            for r in b.get("rows", []):
                tot = sum(int(c.get("span", 1)) for c in r.get("cells", []))
                if tot != 7: err.append(f"{w}: '{r.get('area')}' 행 칸 합 {tot} != 7")
                if not r.get("area"): err.append(f"{w}: 행 이름 없음")
        elif t == "money":
            for r in b.get("rows", []):
                if len(r) != 5: err.append(f"{w}: money 행 칸 {len(r)} != 5")
        elif t == "why":
            for r in b.get("rows", []):
                if len(r) != 4: err.append(f"{w}: why 행 칸 {len(r)} != 4")
        elif t == "para":
            if not b.get("text"): err.append(f"{w}: para 글 없음")
        else:
            err.append(f"{w}: 모르는 블록 {t}")
txt = json.dumps(d, ensure_ascii=False)
for a in ALLOW: txt = txt.replace(a, "")
for wd in BANNED:
    for m in re.finditer(re.escape(wd), txt):
        err.append(f"금지어 '{wd}': ...{txt[max(0, m.start()-25):m.end()+25]}...")
print(f"{slug}: 절 {len(d.get('sections', []))}, 문제 {len(err)}")
for e in err[:40]: print(" ", e)
sys.exit(1 if err else 0)
