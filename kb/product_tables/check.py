"""회사 개요 카드 JSON 점검: python3 -I kb/product_tables/check.py <slug>
모양(card.rows, flows 키), 금지어, 긴 줄표와 가운뎃점, 빈 칸을 본다."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BANNED = ["제공", "지원", "확대", "강화", "통합", "연결", "운영사", "발행 대행", "백단", "미확인", "확인 필요", "미정", "—", "–", "·"]
slug = sys.argv[1]
p = ROOT / f"kb/{slug}_overview/{slug}_overview.json"
d = json.loads(p.read_text(encoding="utf-8"))
err = []
c = d.get("card") or {}
for k in ("name", "sub", "rows"):
    if not c.get(k): err.append(f"card.{k} 없음")
flows = d.get("flows") or {}
def walk(it, where):
    if not isinstance(it, dict): err.append(f"{where}: 줄이 dict가 아님"); return
    if not (it.get("t") or it.get("table") or it.get("k")): err.append(f"{where}: 빈 줄")
    if it.get("flow") and it["flow"] not in flows: err.append(f"{where}: 없는 그림 {it['flow']}")
    tb = it.get("table")
    if tb:
        n = len(tb.get("head") or [])
        for r in tb.get("rows") or []:
            if len(r) != n: err.append(f"{where}: 표 칸 수 {len(r)} != {n}: {str(r)[:60]}")
    for s in it.get("sub") or []: walk(s, where)
    for k in it.get("kids") or []: walk(k, where)
for r in c.get("rows", []):
    if not r.get("label"): err.append("label 없는 행")
    for it in (r.get("items") or []) + (r.get("path") or []): walk(it, r.get("label"))
for k, f in flows.items():
    if f.get("stages"):
        for st in f["stages"]:
            for bx in st.get("boxes") or []:
                if len(bx) != 3 or bx[2] not in ("ondo", "ext", "inv", "none", "ondo_dash"): err.append(f"그림 {k}: 상자 모양 {bx}")
    elif not f.get("table"): err.append(f"그림 {k}: stages도 table도 없음")
txt = json.dumps(d, ensure_ascii=False)
for w in BANNED:
    for m in re.finditer(re.escape(w), txt):
        err.append(f"금지어 '{w}': ...{txt[max(0,m.start()-25):m.end()+25]}...")
print(f"{slug}: 행 {len(c.get('rows', []))}, 그림 {len(flows)}, 문제 {len(err)}")
for e in err[:60]: print(" ", e)
sys.exit(1 if err else 0)
