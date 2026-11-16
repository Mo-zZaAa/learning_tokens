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
    with open(p, newline="", encoding="utf-8-sig") as f:
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
            if not url.startswith("http"):
                url = ""
                title = title or "사용자 제공 문서"
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
        text = re.sub(r"\((?:\.\./)?(?:inputs|sources|work|captures)/[^)]*\)", "(사용자 제공 문서)", text)
        text = re.sub(r"(?:\.\./)?(?:inputs|sources|work)/\S+", "사용자 제공 문서", text)
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



# ---------- 2~4배치 데이터 ----------
def src_of(ids):
    return evidence([i.strip() for i in re.split(r"[;,\s]+", ids or "") if i.strip()])


STAGE = {"발행": "발행", "체결 장소": "체결", "파생 거래소": "체결", "청산, 결제, 보관": "청산", "파생 청산소": "청산",
         "기록": "기록", "주문 접수": "접점", "파생 중개": "접점"}
CO_ALIAS = {"Payward (Kraken)": "Kraken", "Kraken(Payward)": "Kraken"}
REL_KIND = {"인수와 합병": "인수", "지분 투자": "투자", "사업 제휴": "제휴", "발행과 유통 위탁": "위탁",
            "모회사와 자회사": "자회사", "상장과 자금 조달": "자금 조달", "투자": "투자", "제휴": "제휴", "인수": "인수"}


def law_link(lid):
    l = laws.get(lid)
    if not l:
        return {"t": lid, "url": ""}
    return {"t": f'{l.get("법령명","")} {l.get("조항","")}'.strip(), "url": (l.get("링크") or "").strip(),
            "q": (l.get("원문 발췌") or "").strip(), "e": (l.get("쉬운 풀이") or "").strip()}


def md_tables(path):
    tabs, cur = [], None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if cur is None:
                cur = {"head": cells, "rows": []}
                tabs.append(cur)
            else:
                cur["rows"].append(cells)
        else:
            cur = None
    return tabs


def extra_data():
    out = {}
    # 발행 잔액 순위(한 출처, 같은 기준일)
    rank = []
    for fid in ["F-1021", "F-1022", "F-1023", "F-1024", "F-1025", "F-1026", "F-1027"]:
        f = facts.get(fid)
        if not f:
            continue
        m = re.search(r"(\d+)위, 점유율 ([\d.]+)%", f["무엇을"])
        name = f["회사"]
        slug = {"Binance bStocks": "binance", "Ondo Global Markets": "ondo", "Kraken xStocks": "kraken",
                "Robinhood Stock Tokens": "robinhood", "Coinbase": "coinbase", "Dinari dShares": "dinari"}.get(name)
        rank.append({"name": name, "slug": slug, "rank": int(m.group(1)) if m else None, "share": m.group(2) if m else "",
                     "usd": float(f["값"] or 0), "date": f["기준일"], "src": evidence([fid])})
    out["rank"] = rank
    out["cross"] = [dict(r, src=src_of(r.pop("fact_ids", ""))) for r in load_csv(ROOT / "db/cross.csv")]
    out["ats"] = [dict(r, src=src_of(r.pop("fact_ids", ""))) for r in load_csv(ROOT / "db/cross_ats.csv")]
    out["events"] = [dict(r, src=src_of(r.pop("fact_ids", ""))) for r in load_csv(ROOT / "db/ats_events.csv")]
    # 인가 지도 + 등록부 대조
    lic = []
    for r in load_csv(ROOT / "work/LICMAP/licenses_check.csv"):
        r = {k.lstrip("\ufeff"): v for k, v in r.items()}
        co = CO_ALIAS.get(r["회사"], r["회사"])
        res = r.get("대조 결과", "")
        note = r.get("차이 또는 시도한 곳", "")
        if res.startswith("등록부 미확인"):
            note = ""
        lic.append({"co": co, "stage": STAGE.get(r["하는 일"], r["하는 일"]), "job": r["하는 일"], "own": r["상태"],
                    "lic": r["자격"], "place": r["지명"], "how": r["확보 방식"], "target": r["인수 대상"],
                    "when": r["시점"], "ent": r["법인"], "does": r["이 자격으로 하는 일"],
                    "url": r["출처 링크"], "reg": r.get("등록부 링크", ""), "note": note,
                    "orange": co in ("Securitize", "tZERO"),
                    "regwhen": "" if co in ("Securitize", "tZERO") else (lambda m: m.group(1) if m else "")(re.search(r"(?:firmStatusDate|등록부|등록|지정|최초 상태일)\)?\s*(\d{4}-\d{2})", note))})
    out["lic"] = lic
    # 관계
    rel = []
    for r in load_csv(ROOT / "db/relations.csv"):
        rel.append({"a": r["주체"], "b": r["대상"], "kind": REL_KIND.get(r["관계 종류"], r["관계 종류"]),
                    "when": r["시점"], "what": r.get("회사가 밝힌 목적") or "", "give": r.get("주는 것", ""),
                    "get": r.get("받는 것", ""), "url": r.get("링크", ""), "q": r.get("원문 근거 문장", "")})
    for r in load_csv(ROOT / "inputs/license_map/relations.csv"):
        r = {k.lstrip("\ufeff"): v for k, v in r.items()}
        rel.append({"a": r["주는 쪽"], "b": r["받는 쪽"], "kind": REL_KIND.get(r["유형"], r["유형"]), "when": r["시점"],
                    "what": r["내용"], "give": "", "get": "", "url": r["출처 링크"], "q": ""})
    for r in load_csv(ROOT / "inputs/license_map/acquisitions.csv"):
        r = {k.lstrip("\ufeff"): v for k, v in r.items()}
        rel.append({"a": CO_ALIAS.get(r["회사"], r["회사"]), "b": r["대상"], "kind": "인수", "when": r["시점"],
                    "what": r["얻은 것"] + (". " + r["회사가 밝힌 이유"] if r.get("회사가 밝힌 이유") else ""),
                    "give": "", "get": "", "url": r["출처 링크"], "q": ""})
    seen, rel2 = set(), []
    for x in rel:
        k = (x["a"].lower()[:12], x["b"].lower()[:12], x["kind"], x["when"][:4])
        if k in seen:
            continue
        seen.add(k)
        rel2.append(x)
    out["rel"] = rel2
    # 한미 제도 비교
    tabs = md_tables(ROOT / "kb/regulation_compare.md")
    reg = []
    if tabs:
        for row in tabs[0]["rows"]:
            if len(row) < 6:
                continue
            def ids(cell):
                return [law_link(x) for x in re.findall(r"(?:US|KR|EU)-[^\s,()]+", cell)]
            reg.append({"issue": row[0], "us": row[1], "us_law": ids(row[2]), "kr": row[3], "kr_law": ids(row[4]), "diff": row[5]})
    out["reg"] = reg
    common = []
    if len(tabs) > 1:
        for row in tabs[-1]["rows"]:
            if len(row) >= 3:
                common.append({"t": row[0], "d": row[1], "src": evidence(re.findall(r"F-\d{4}|KR-[^\s,]+", row[2]))})
    out["common"] = common
    return out


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

    data = {"companies": companies, "imgs": IMGS, "terms": terms, "log": log, **extra_data()}
    tpl = (WEB / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("/*__DATA__*/null", payload)
    out = WEB / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"web/index.html {out.stat().st_size/1e6:.1f}MB, 이미지 {len(IMGS)}개")


if __name__ == "__main__":
    main()
