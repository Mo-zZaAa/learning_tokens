"""핵심 포인트의 이동 버튼(go) 점검: python3 -I kb/product_tables/check_go.py <slug>
go = {"row": "행 이름", "find": "대상 줄 글에 그대로 들어 있는 조각(==, !!, ** 표시는 빼고)"}
대상 줄: 그 행의 줄(아래 줄 포함), 확장 경로 줄, 표 행(칸을 ' | '로 이은 글). 정확히 한 줄에만 맞아야 함."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def plain(s): return re.sub(r"==|!!|\*\*", "", s or "")
def lines(row):
    out = []
    def walk(it):
        if it.get("t") or it.get("k"): out.append(plain((it.get("k2") or "") + " " + (it.get("t") or "")))
        tb = it.get("table")
        if tb: out.extend(plain(" | ".join(map(str, r))) for r in tb.get("rows") or [])
        for x in (it.get("sub") or []) + (it.get("kids") or []): walk(x)
    for it in (row.get("items") or []) + (row.get("path") or []): walk(it)
    return out
def check(slug):
    d = json.loads((ROOT / f"kb/{slug}_overview/{slug}_overview.json").read_text(encoding="utf-8"))
    rows = {r["label"]: r for r in d["card"]["rows"]}
    bad = n = 0
    def walk(it):
        nonlocal bad, n
        g = it.get("go")
        if g:
            n += 1
            r = rows.get(g.get("row"))
            hits = [l for l in lines(r) if g.get("find", "\0") in l] if r else []
            if len(hits) != 1:
                bad += 1; print(f"  맞는 줄 {len(hits)}개: row={g.get('row')} find={g.get('find')}")
        for x in it.get("kids") or []: walk(x)
    for r in d["card"]["rows"]:
        for it in r.get("items") or []: walk(it)
    print(f"{slug}: 이동 버튼 {n}, 문제 {bad}")
    return bad
sys.exit(1 if any(check(s) for s in sys.argv[1:]) else 0)
