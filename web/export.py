#!/usr/bin/env python3
"""web/export.py: 화면에서 확정하고 고친 최종 줄을 기준으로 export/handoff_to_chat.zip을 만든다.

입력
- companies/ 최신 본문(build.py와 같은 파서, 같은 고정 줄 ID)
- discussion/inbox/*.json: 화면의 "메모 보내기"로 받은 json(시간 순서로 적용)
  고침, 추가, 삭제, 순서, 확정, 주황 메모를 줄에 반영한다.
- web/locks.json: 사용자가 확정하거나 직접 고친 문구
- discussion/log.jsonl: 질문과 답

출력(zip 안)
- final/<회사>.json: 대분류 순서대로 줄 목록. 줄 순서 = 엑셀 행 순서.
  줄마다 id, disp, level(●, ★, ①, ②, ③, 그림), text, color(black/orange), fact_ids, confirmed, notes(달렸던 메모와 답 요지, 참고용)
- final/captures/: 줄의 그림 파일(json에서 파일 이름으로 연결)
- discussion_log.md, open_items.md(합의 안 된 줄만), glossary.md, line_sources.csv,
  regulation_compare.csv, ats_candidates.csv, cross.csv
맨 위 요약(기업 정의, 조사 목적, 조사 내용, Summary)은 내보내지 않는다.
"""
import csv
import io
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

ROOT = B.ROOT
OUT = ROOT / "export"
LV = {"b": "●", "s": "★", "q1": "①", "q2": "②", "q3": "③", "img": "그림"}


def raw_lines(path):
    """본문 줄을 파서와 같은 순서로 (대분류 코드, 원문 줄) 목록으로."""
    out, code = [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        if raw.startswith("## "):
            code = B.sec_code(raw[3:].strip())
            continue
        if code is None:
            continue
        out.append((code, raw.strip()))
    return out


def load_inbox():
    memos = []
    for p in sorted((ROOT / "discussion/inbox").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for m in d.get("memos", []):
            m["_file"] = p.name
            memos.append(m)
    memos.sort(key=lambda m: m.get("at", ""))
    return memos


def main():
    store = json.loads((ROOT / "web/line_ids.json").read_text(encoding="utf-8")) if (ROOT / "web/line_ids.json").exists() else {}
    locks = json.loads((ROOT / "web/locks.json").read_text(encoding="utf-8")) if (ROOT / "web/locks.json").exists() else {}
    log = [json.loads(l) for l in (ROOT / "discussion/log.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()] \
        if (ROOT / "discussion/log.jsonl").exists() else []
    inbox = load_inbox()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "final/captures").mkdir(parents=True)

    key2path = {}
    all_lines, line_src = {}, []
    for base, name, kind, prefix in B.ORDER:
        p = B.latest_body(base)
        if not p:
            continue
        logo, sections = B.parse(p)
        B.assign_ids(prefix, sections, store)
        for k_path, k in B.IMG_KEYS.items():
            key2path[k] = Path(k_path)
        raws = raw_lines(p)
        flat = [(sec, r) for sec in sections for r in sec["rows"]]
        assert len(raws) == len(flat), (base, len(raws), len(flat))
        secs = [{"code": sec["code"], "title": sec["title"], "rows": list(sec["rows"])} for sec in sections]
        # 원문 줄에서 fact_id
        for (sec, r), (code, raw) in zip(flat, raws):
            r["fact_ids"] = B.ID_RE.findall(raw)
            r["_raw"] = raw
        company = {"company": name, "kind": kind, "body_file": p.name, "sections": secs,
                   "logo": key2path[logo].name if logo in key2path else None}
        all_lines[name] = company

    # 메모 적용(화면에서 고친 것)
    by_id = {}
    for c in all_lines.values():
        for sec in c["sections"]:
            for r in sec["rows"]:
                by_id[r["id"]] = (c, sec, r)
    notes = {}
    for m in inbox:
        lid, t = m.get("line_id"), m.get("type")
        notes.setdefault(lid, []).append(f'{t}: {m.get("text","")}')
        if lid not in by_id and t != "추가":
            continue
        if t == "고침":
            by_id[lid][2]["_user_text"] = m.get("after") or m.get("text")
        elif t == "삭제":
            by_id[lid][2]["_deleted"] = True
        elif t == "확정":
            by_id[lid][2]["_confirmed"] = True
        elif t == "주황":
            by_id[lid][2]["orange"] = "해제" not in m.get("text", "")
        elif t == "추가":
            after = m.get("after")
            if after in by_id:
                c, sec, ar = by_id[after]
                lvl = {"b": "b", "s": "s", "q1": "q1"}.get(m.get("level"), "s")
                nr = {"id": lid, "level": lvl, "label": None, "text": m.get("text", ""), "src": [], "fact_ids": [], "_added": True}
                sec["rows"].insert(sec["rows"].index(ar) + 1, nr)
                by_id[lid] = (c, sec, nr)
        elif t == "순서" and m.get("order"):
            c, sec, _ = by_id[lid]
            order = [o.split(" ")[-1] for o in m["order"]]
            pos = {k: i for i, k in enumerate(order)}
            sec["rows"].sort(key=lambda r: pos.get(r["id"], 1e9))
    for g in log:
        notes.setdefault(g.get("line_id"), []).append(f'답({g.get("status","답함")}): {g.get("answer","")}')
    for lid, lk in locks.items():
        if lid in by_id and lk.get("text"):
            by_id[lid][2]["_user_text"] = lk["text"]
            by_id[lid][2]["_confirmed"] = by_id[lid][2].get("_confirmed") or lk.get("confirmed", False)

    # final/<회사>.json
    used_imgs = set()
    for name, c in all_lines.items():
        out_secs = []
        for sec in c["sections"]:
            rows, n = [], 0
            for r in sec["rows"]:
                if r.get("_deleted"):
                    continue
                n += 1
                disp = f'{name} {sec["code"]}-{n}'
                if r["level"] == "img":
                    files = []
                    for i in r.get("imgs", []):
                        pth = key2path.get(i["k"])
                        if pth:
                            fn = f'{pth.parent.name}_{pth.stem}.jpg'
                            files.append({"file": fn, "caption": i["c"]})
                            used_imgs.add((pth, fn))
                    rows.append({"id": r["id"], "disp": disp, "level": "그림", "images": files})
                    continue
                if r.get("_user_text"):
                    text = r["_user_text"]
                else:
                    text = (r["label"] + " : " if r.get("label") else "") + r.get("text", "")
                    if r.get("link"):
                        text += " " + r["link"]
                rows.append({"id": r["id"], "disp": disp, "level": LV[r["level"]], "text": text,
                             "color": "orange" if r.get("orange") else "black", "fact_ids": r.get("fact_ids", []),
                             "confirmed": bool(r.get("_confirmed")), "notes": notes.get(r["id"], [])})
                for fid in r.get("fact_ids", []):
                    ev = B.evidence([fid])
                    for e in ev:
                        line_src.append([name, r["id"], disp, fid, e.get("t", ""), e.get("url", ""), e.get("q", "")])
            out_secs.append({"code": sec["code"], "title": sec["title"], "lines": rows})
        if c.get("logo"):
            for k, pth in key2path.items():
                if pth.name == c["logo"] and pth.parent.name.lower().startswith(name.split()[0].lower()[:4]):
                    used_imgs.add((pth, f'{pth.parent.name}_{pth.name}'))
                    c["logo"] = f'{pth.parent.name}_{pth.name}'
        (OUT / "final" / f'{name.replace(" ", "_")}.json').write_text(
            json.dumps({"company": name, "kind": c["kind"], "logo": c.get("logo"), "sections": out_secs},
                       ensure_ascii=False, indent=1), encoding="utf-8")
    from PIL import Image
    for pth, fn in used_imgs:
        im = Image.open(pth)
        if im.width > 1200:
            im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
        if fn.endswith(".jpg"):
            im.convert("RGB").save(OUT / "final/captures" / fn, "JPEG", quality=80, optimize=True)
        else:
            im.save(OUT / "final/captures" / fn)

    # line_sources.csv
    with open(OUT / "line_sources.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["회사", "줄 ID", "화면 번호", "fact_id 또는 조문 ID", "출처 제목", "링크", "원문 근거 문장"])
        w.writerows(line_src)

    # discussion_log.md, open_items.md
    L = ["# 토론 기록", ""]
    for g in log:
        L.append(f'- {g.get("time","")} [{g.get("disp", g.get("line_id",""))}] {g.get("company","")}: 질문 "{g.get("question","")}"')
        L.append(f'  - 답: {g.get("answer","")}')
        for ch in g.get("changes", []):
            L.append(f'  - 고친 곳 {ch.get("where","")}: {ch.get("before","")} → {ch.get("after","")}')
        L.append(f'  - 상태: {g.get("status","답함")}')
    if len(L) == 2:
        L.append("아직 기록이 없습니다.")
    (OUT / "discussion_log.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    agreed = {g.get("memo_id") for g in log if g.get("status") == "합의"}
    agreed |= {m.get("memo_id") for m in inbox if m.get("type") == "합의"}
    O = ["# 합의 안 된 줄", "", "메모나 질문이 달렸지만 아직 합의되지 않은 줄만 둡니다.", ""]
    for g in log:
        if g.get("status") != "합의" and g.get("memo_id") not in agreed:
            O.append(f'- [{g.get("disp", g.get("line_id",""))}] {g.get("question","")} (상태: {g.get("status","답함")})')
    answered = {g.get("memo_id") for g in log}
    for m in inbox:
        if m.get("type") in ("메모", "챌린지", "딥다이브 요청", "풀어쓰기 요청") and m.get("memo_id") not in answered:
            O.append(f'- [{m.get("disp","")}] ({m.get("type")}) {m.get("text","")} (상태: 답 전)')
    if len(O) == 4:
        O.append("없음.")
    (OUT / "open_items.md").write_text("\n".join(O) + "\n", encoding="utf-8")

    # glossary.md
    G = ["# 용어", ""]
    for r in B.load_csv(ROOT / "db/terms.csv"):
        G.append(f'- **{r["용어"]}**{" (" + r["원어"] + ")" if r.get("원어") else ""}: {r.get("쉬운 뜻","")}'
                 + (f' 헷갈리는 짝: {r["헷갈리는 짝"]}. {r.get("차이 한 줄","")}' if r.get("헷갈리는 짝") else ""))
    (OUT / "glossary.md").write_text("\n".join(G) + "\n", encoding="utf-8")

    # regulation_compare.csv
    tabs = B.md_tables(ROOT / "kb/regulation_compare.md")
    with open(OUT / "regulation_compare.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if tabs:
            w.writerow(tabs[0]["head"])
            w.writerows(tabs[0]["rows"])
        for tb in tabs[1:]:
            w.writerow([])
            w.writerow([tb["sec"]])
            w.writerow(tb["head"])
            w.writerows(tb["rows"])
    shutil.copy(ROOT / "db/ats_screen.csv", OUT / "ats_candidates.csv")
    with open(OUT / "cross.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        for i, name in enumerate(["db/cross.csv", "db/cross_ats.csv", "db/ats_events.csv"]):
            rows = list(csv.reader(open(ROOT / name, encoding="utf-8-sig")))
            if i:
                w.writerow([])
            w.writerows(rows)

    zp = OUT / "handoff_to_chat.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob("*")):
            if f.is_file() and f != zp:
                z.write(f, f.relative_to(OUT))
    print(zp, f"{zp.stat().st_size/1e6:.1f}MB", "회사", len(all_lines), "그림", len(used_imgs), "메모", len(inbox))


if __name__ == "__main__":
    main()
