#!/usr/bin/env python3
"""web/build.py: companies/ 최신 본문, captures/, db/, inputs/license_map/을 읽어 web/index.html 한 파일을 만든다.

- 줄마다 고정 ID(web/line_ids.json에 저장)를 붙인다. 다시 만들어도 같은 줄은 같은 ID.
- 화면 번호(예: Kraken B-3)는 표시용으로 매번 다시 매긴다.
- 사실 번호, 조문 ID, 파일 경로, 검증 상태는 화면에 내보내지 않는다(근거 문장과 링크만).
- 캡처는 폭 1200px 이하 JPEG로 줄여 data URI로 넣는다(서버, 외부 주소 없이 열림).
- discussion/log.jsonl의 답을 해당 줄 아래에 보인다.
- web/locks.json: 사용자가 확정하거나 직접 고친 문구. 본문이 달라져도 이 문구를 쓴다.
"""
import base64
import csv
import difflib
import io
import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
COMP = ROOT / "companies"

ORDER = [
    ("Kraken", "Kraken", "company", "kr"),
    ("Robinhood", "Robinhood", "company", "rh"),
    ("Binance", "Binance", "company", "bn"),
    ("Coinbase", "Coinbase", "company", "cb"),
    ("Dinari", "Dinari", "company", "dn"),
    ("Ondo", "Ondo", "company", "on"),
    ("Blue_Ocean_ATS", "Blue Ocean", "ats", "bo"),
    ("Bruce_ATS", "Bruce", "ats", "br"),
    ("MOON_ATS", "MOON", "ats", "mo"),
]
SLUG = {"kr": "kraken", "rh": "robinhood", "bn": "binance", "cb": "coinbase", "dn": "dinari",
        "on": "ondo", "bo": "blue-ocean", "br": "bruce", "mo": "moon"}

ID_RE = re.compile(r"\[((?:F-\d{4})|(?:KR-[^\]]+)|(?:US-[^\]]+)|(?:EU-[^\]]+)|(?:CASE-[^\]]+))\]")
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://\S+")
ORANGE_WORDS = ("Securitize", "tZERO")


def latest_body(base):
    best, bestv = None, -1
    for p in COMP.glob(f"{base}*.md"):
        m = re.fullmatch(re.escape(base) + r"(?:_v(\d+))?\.md", p.name)
        if not m:
            continue
        v = int(m.group(1) or 0)
        if v > bestv:
            best, bestv = p, v
    return best


def sec_code(title):
    m = re.match(r"([A-H]) ", title)
    if m:
        return m.group(1)
    for key, code in (("개요", "개요"), ("발언", "발언"), ("연결", "연결"), ("차이", "차이"), ("판단", "판단")):
        if key in title:
            return code
    return title[:2]


def load_csv(p):
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------- 근거 ----------
facts = {r["fact_id"]: r for r in load_csv(ROOT / "db/facts.csv")}
sources = {r["source_id"]: r for r in load_csv(ROOT / "db/sources.csv")}
laws = {r["law_id"]: r for r in load_csv(ROOT / "db/laws.csv")}
cases = {r.get("case_id", ""): r for r in load_csv(ROOT / "db/cases.csv")}


def evidence(ids):
    out, seen = [], set()
    for i in ids:
        if i.startswith("F-") and i in facts:
            f = facts[i]
            sid = (f.get("source_id") or "").split(";")[0].strip()
            title = sources.get(sid, {}).get("제목", "") if sid else ""
            url = (f.get("링크") or "").strip()
            q = (f.get("원문 근거 문장") or "").strip()
            key = (url, q[:80])
            if key in seen:
                continue
            seen.add(key)
            out.append({"q": q, "url": url, "t": title or url})
        elif i in laws:
            l = laws[i]
            url = (l.get("링크") or "").strip()
            key = (url, i)
            if key in seen:
                continue
            seen.add(key)
            out.append({"q": (l.get("원문 발췌") or "").strip(), "url": url,
                        "t": f'{l.get("법령명","")} {l.get("조항","")}'.strip(),
                        "e": (l.get("쉬운 풀이") or "").strip()})
        elif i in cases:
            c = cases[i]
            url = (c.get("링크") or "").strip()
            out.append({"q": (c.get("결론") or "").strip(), "url": url,
                        "t": c.get("사건명", "") or url})
    return out


# ---------- 이미지 ----------
IMGS, IMG_KEYS = {}, {}


def img_key(rel_from_companies):
    p = (COMP / rel_from_companies).resolve()
    if not p.exists():
        print("  이미지 없음:", rel_from_companies, file=sys.stderr)
        return None
    if str(p) in IMG_KEYS:
        return IMG_KEYS[str(p)]
    key = f"i{len(IMG_KEYS)}"
    im = Image.open(p)
    is_logo = p.stem == "logo"
    maxw = 360 if is_logo else 1200
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    if not is_logo and im.height > 2400:  # 아주 긴 캡처는 위쪽만
        im = im.crop((0, 0, im.width, 2400))
    buf = io.BytesIO()
    if is_logo:
        if im.mode not in ("RGBA", "RGB", "LA"):
            im = im.convert("RGBA")
        im.save(buf, "PNG", optimize=True)
        uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    else:
        im.convert("RGB").save(buf, "JPEG", quality=68, optimize=True, progressive=True)
        uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    IMGS[key] = uri
    IMG_KEYS[str(p)] = key
    return key


# ---------- 본문 파싱 ----------
def parse(path):
    logo, sections, cur = None, [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        if raw.startswith("## "):
            title = raw[3:].strip()
            cur = {"code": sec_code(title), "title": title, "rows": []}
            sections.append(cur)
            continue
        if cur is None:
            m = IMG_RE.search(raw)
            if m and logo is None:
                logo = img_key(m.group(2))
            continue
        s = raw.strip()
        if IMG_RE.match(s):
            imgs = [{"k": img_key(m.group(2)), "c": m.group(1)} for m in IMG_RE.finditer(s)]
            cur["rows"].append({"level": "img", "imgs": [i for i in imgs if i["k"]], "raw": s})
            continue
        lead = s[0]
        level = {"●": "b", "★": "s", "①": "q1", "②": "q2", "③": "q3"}.get(lead)
        if level is None:
            level, body = "s", s
        else:
            body = s[1:].strip()
        ids = ID_RE.findall(body)
        text = ID_RE.sub("", body).strip()
        link = None
        um = URL_RE.search(text)
        if um:
            link = um.group(0).rstrip(".,)")
            text = (text[:um.start()] + text[um.end():]).strip().rstrip(",").strip()
            text = re.sub(r",\s*,", ",", text)
        label, rest = None, text
        if " : " in text:
            label, rest = text.split(" : ", 1)
        row = {"level": level, "label": label, "text": rest if label else text, "raw": s,
               "src": evidence(ids)}
        if link:
            row["link"] = link
        if label == "주장" and level == "b":
            row["claim"] = True
        if cur["code"] != "발언" and any(w in text for w in ORANGE_WORDS):
            row["orange"] = True
        cur["rows"].append(row)
    return logo, sections


def norm(s):
    return re.sub(r"\s+", " ", ID_RE.sub("", s)).strip()


def assign_ids(prefix, sections, store):
    entries = store.setdefault(prefix, {"next": 1, "lines": {}})
    lines = entries["lines"]
    used = set()
    flat = [(sec["code"], r) for sec in sections for r in sec["rows"]]
    # 1) 같은 대분류, 같은 문구
    for code, r in flat:
        t = norm(r["raw"])
        for lid, e in lines.items():
            if lid not in used and e["sec"] == code and e["text"] == t:
                r["id"] = lid
                used.add(lid)
                break
    # 2) 같은 대분류, 비슷한 문구
    for code, r in flat:
        if "id" in r:
            continue
        t = norm(r["raw"])
        best, bestr = None, 0.55
        for lid, e in lines.items():
            if lid in used or e["sec"] != code:
                continue
            ratio = difflib.SequenceMatcher(None, e["text"], t).ratio()
            if ratio > bestr:
                best, bestr = lid, ratio
        if best:
            r["id"] = best
            used.add(best)
    # 3) 새 ID
    for code, r in flat:
        if "id" not in r:
            lid = f"{prefix}-{entries['next']:04d}"
            entries["next"] += 1
            r["id"] = lid
            used.add(lid)
    for code, r in flat:
        lines[r["id"]] = {"sec": code, "text": norm(r["raw"])}


def main():
    store_p = WEB / "line_ids.json"
    store = json.loads(store_p.read_text(encoding="utf-8")) if store_p.exists() else {}
    locks_p = WEB / "locks.json"
    locks = json.loads(locks_p.read_text(encoding="utf-8")) if locks_p.exists() else {}

    companies = []
    for base, name, kind, prefix in ORDER:
        p = latest_body(base)
        if not p:
            print("본문 없음:", base, file=sys.stderr)
            continue
        logo, sections = parse(p)
        assign_ids(prefix, sections, store)
        for sec in sections:
            n = 0
            for r in sec["rows"]:
                n += 1
                r["disp"] = f'{name} {sec["code"]}-{n}'
                lk = locks.get(r["id"])
                if lk and lk.get("text"):
                    t = lk["text"]
                    if r.get("label"):
                        t = t.split(" : ", 1)[1] if " : " in t else t
                    if t != r.get("text"):
                        print(f"  확정 문구 유지: {r['disp']}", file=sys.stderr)
                        r["text"] = t
                r.pop("raw", None)
        companies.append({"slug": SLUG[prefix], "name": name, "kind": kind, "logo": logo,
                          "sections": sections})
        print(f"{name}: {p.name}, {sum(len(s['rows']) for s in sections)}줄")

    store_p.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")

    terms = []
    for r in load_csv(ROOT / "db/terms.csv"):
        t = r["용어"].strip()
        keys = {t}
        if "(" in t:
            keys.add(t.split("(")[0].strip())
        keys = sorted(k for k in keys if len(k) >= 2 and k not in ("증권",))
        terms.append({"t": t, "k": keys, "en": r.get("원어", ""), "e": r.get("쉬운 뜻", ""),
                      "p": r.get("헷갈리는 짝", ""), "d": r.get("차이 한 줄", ""),
                      "kr": r.get("한국의 대응 용어와 제도", "")})

    log = []
    lp = ROOT / "discussion/log.jsonl"
    if lp.exists():
        for line in lp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                log.append(json.loads(line))

    data = {"companies": companies, "imgs": IMGS, "terms": terms, "log": log}
    tpl = (WEB / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("/*__DATA__*/null", payload)
    out = WEB / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"web/index.html {out.stat().st_size/1e6:.1f}MB, 이미지 {len(IMGS)}개")


if __name__ == "__main__":
    main()
