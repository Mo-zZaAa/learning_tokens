#!/usr/bin/env python3
"""v5 검토 화면 만들기.

실행: python3 web/v5/build.py  →  web/v5/index.html (한 파일, 외부 주소 없이 열림)

회사마다 두 보기만 만든다(6개사 공통 slug common은 개요만).
- 개요(세 층): 1층 한 화면 카드 kb/cards6/<slug>.md, 2층 쉬운 해설 kb/easy/<slug>.md,
       3층 개요 문서 kb/cards/<slug>.md + PM 2차 질문과 답 kb/pm_q2/<slug>.md
       공통: kb/cards6/common.md, kb/easy/00_기초.md, kb/cards/common.md + kb/pm_q2/00_공통.md + kb/pm_q2/추가조사_261118.md
- raw: 1) PM 질문별 답(kb/coverage/<slug>.csv, kb/questions/<slug>.json) 2) 사건 카드(kb/events/<slug>.json)
       3) 구조 표(kb/structs/<slug>/*.csv) 4) 사실 DB(db/facts.csv) 5) 원본 목록(db/sources.csv)
       6) 빈칸과 정정(kb/gaps.csv, kb/gaps_add/<slug>.csv, kb/corrections.csv)
       화면 순서: 본문(companies/<회사>_vN.md, 줄마다 근거의 원문, 뜻, 출처를 하위 줄로) 먼저, 1)~6)은 아래 "만든 표와 카드(참고)"에 접어 둠
뜻 풀이: kb/glossary_main.csv + kb/glossary_add/*.csv + db/terms.csv
메모 답: kb/memo_answers.csv(mid, co, view, anchor, sec, quote, 메모, 답, 고친 곳, 상태). 없거나 비어도 됨
없는 파일은 화면에 "준비 중"으로 나오고, 파일이 생긴 뒤 다시 빌드하면 채워진다.
줄 id는 다시 빌드해도 같은 글(또는 같은 번호의 줄)이면 같다.
"""
import csv
import datetime
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

import ondo_card  # 같은 폴더: Ondo 개요 패키지 그림(깊이 보기 페이지와 같은 그림)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

# (slug, 화면 이름, companies/ 파일 앞부분)
COS = [
    ("kraken", "Kraken", "Kraken"),
    ("binance", "Binance", "Binance"),
    ("coinbase", "Coinbase", "Coinbase"),
    ("robinhood", "Robinhood", "Robinhood"),
    ("dinari", "Dinari", "Dinari"),
    ("ondo", "Ondo", "Ondo"),
    ("common", "6개사 공통", "__none__"),
]
SLUGS = [c[0] for c in COS]
COMMON = ("common", "6개사 공통")
# db/facts.csv의 회사 값 → slug (나머지 값은 이 화면의 회사가 아님)
FACT_CO = {
    "Kraken(Payward)": "kraken", "Kraken": "kraken",
    "Ondo Finance": "ondo", "Ondo": "ondo",
    "Binance": "binance", "Coinbase": "coinbase", "Robinhood": "robinhood", "Dinari": "dinari",
}
STRUCT_LABEL = {
    "money": "돈(수입 구성)", "entities": "법인과 인가", "deals": "인수", "products": "상품",
    "sales": "판매(어느 나라 자산을 누구에게)", "timeline": "연표", "valuechain": "밸류체인",
    "funding": "자금 조달", "article": "핵심 기사 질문별 요약",
}
STRUCT_ORDER = ["money", "funding", "deals", "entities", "products", "sales", "valuechain", "article", "timeline"]
FACT_COLS = ["fact_id", "회사", "시작(연월)", "무엇을", "값", "단위", "기준일", "검증 상태", "링크", "원문 근거 문장", "source_id"]
DEEP = {"ondo": {"href": "ondo_deep.html", "label": "Ondo 깊이 보기"}}  # 회사별 깊이 보기 페이지(같은 폴더)
TERM_STOP = {"증권"}  # 너무 흔해 풍선이 오히려 방해되는 말


def rel(p):
    return str(Path(p).relative_to(ROOT))


def read_csv(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return [], []
    head = [h.strip() for h in rows[0]]
    body = []
    for r in rows[1:]:
        r = (r + [""] * len(head))[: max(len(head), len(r))]
        body.append([c.strip() for c in r])
    return head, body


def read_dicts(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm(t):
    return re.sub(r"\s+", " ", str(t or "")).strip()


def h8(t):
    return hashlib.sha1(norm(t)[:60].encode("utf-8")).hexdigest()[:8]


def safe(t):
    return re.sub(r"[^A-Za-z0-9_-]", "_", str(t))


class Ids:
    """한 회사 안에서 줄 id가 겹치지 않게 함. 같은 글이면 같은 id, 겹치면 -2, -3."""

    def __init__(self):
        self.seen = set()

    def make(self, base):
        i, n = base, 2
        while i in self.seen:
            i = f"{base}-{n}"
            n += 1
        self.seen.add(i)
        return i


ID_LIKE = re.compile(r"^[A-Za-z]{1,6}[A-Za-z0-9]*-?[A-Za-z0-9-]*\d[A-Za-z0-9-]*$")


def table(ids, base, head, body, idcol="auto", keybase=None):
    """CSV 하나를 표 자료로. 번호 열이 있으면 줄 id에 씀(없으면 글 앞부분 해시)."""
    if idcol == "auto":
        idcol = None
        for cand in ("번호", "id", "ID", "질문 번호"):
            if cand in head:
                idcol = head.index(cand)
                break
        else:
            firsts = [r[0] for r in body if r]
            if firsts and all(ID_LIKE.match(x or "") for x in firsts) and len(set(firsts)) == len(firsts):
                idcol = 0
    kb = keybase or base
    rows = []
    for r in body:
        key = r[idcol] if idcol is not None and idcol < len(r) and r[idcol] else ""
        rid = ids.make(f"{kb}-{safe(key)}" if key else f"{base}-{h8(' | '.join(r))}")
        rows.append({"id": rid, "c": r, "k": key})
    return {"cols": head, "rows": rows}


# ---------------- 개요(세 층) ----------------
LIST_RE = re.compile(r"^(\s*)(?:([-*+])|(\d+)[.)])\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
ART_CH = re.compile(r"[─│┌┐└┘├┤┬┴┼═║╔╗╚╝▶◀▼▲]")
SELFTEST_RE = re.compile(r"셀프\s*테스트|자가\s*테스트|스스로\s*풀")


def is_art(line):
    t = line.strip()
    if not t:
        return False
    return bool(ART_CH.search(t)) or len(re.findall(r"[→←↓↑⇒]", t)) >= 2 or t[0] in "↓↑"


def mark_answers(items):
    """셀프 테스트 칸: 답은 화면에서 접어 둠. "질문 → 답", "질문 답: 답", "답:"으로 시작하는 줄, 질문 아래 줄."""
    after_h = False
    seen_q = False
    for it in items:
        t = re.sub(r"\*\*|==|!!", "", it.get("t", "")).strip()
        if it["k"] == "h3":
            after_h = bool(re.match(r"^(답|정답)", t))
            if after_h:
                it["ans"] = True
            continue
        if after_h or re.match(r"^(답|정답)\s*[:：.)]?", t):
            it["ans"] = True
            continue
        if it["k"] == "li" and it.get("d", 0) > 0 and seen_q:
            it["ans"] = True
            continue
        if it["k"] in ("li", "p"):
            seen_q = True
            m = re.search(r"\s(?:→|(?:\*\*)?(?:답|정답)(?:\*\*)?\s*[:：])\s*", it["t"])
            if m and m.start() > 0:
                it["qa"] = [it["t"][:m.start()].rstrip(), it["t"][m.end():].strip()]


def parse_card(slug, text, ids, layer="", mode="card", art=False):
    """mode: card(머리와 다섯 질문만 펼침) / open(모두 펼친 접이 칸) / grid(접지 않는 상자)."""
    title, intro, secs = "", [], []
    cur = None
    stack = []
    tbl = None
    fence = None
    art_open = False
    pre = (layer + ":") if layer else ""

    def target():
        return cur["items"] if cur else intro

    def sec_code(h):
        return "s" + hashlib.sha1((pre + h).encode("utf-8")).hexdigest()[:5]

    def base():
        return f"{slug}-o-{cur['code'] if cur else sec_code('intro') if pre else 'intro'}"

    for raw in text.splitlines():
        line = raw.rstrip()
        if fence is not None:
            if FENCE_RE.match(line):
                t = "\n".join(fence).strip("\n")
                if t:
                    target().append({"k": "pre", "id": ids.make(f"{base()}-{h8(t)}"), "t": t})
                fence = None
            else:
                fence.append(line)
            continue
        if FENCE_RE.match(line):
            tbl = None
            art_open = False
            fence = []
            continue
        if not line.strip():
            tbl = None
            art_open = False
            continue
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        if line.startswith("## "):
            tbl = None
            art_open = False
            stack = []
            h = line[3:].strip()
            cur = {"h": h, "code": sec_code(h), "items": []}
            secs.append(cur)
            continue
        if line.lstrip().startswith("|"):
            art_open = False
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if tbl is None:
                tbl = {"k": "tbl", "id": ids.make(f"{base()}-t{h8(' | '.join(cells))}"), "cols": cells, "rows": []}
                target().append(tbl)
            else:
                tbl["rows"].append({"id": ids.make(f"{base()}-{h8(' | '.join(cells))}"), "c": cells})
            continue
        tbl = None
        if line.startswith("### ") or line.startswith("#### "):
            art_open = False
            t = line.lstrip("#").strip()
            target().append({"k": "h3", "id": ids.make(f"{base()}-{h8(t)}"), "t": t})
            stack = []
            continue
        m = LIST_RE.match(line)
        if not m and art and (is_art(line) or (art_open and line.startswith("    "))):
            items = target()
            if art_open and items and items[-1]["k"] == "pre":
                items[-1]["t"] += "\n" + line
            else:
                items.append({"k": "pre", "id": ids.make(f"{base()}-{h8(line)}"), "t": line})
            art_open = True
            continue
        art_open = False
        if m:
            ind = len(m.group(1).replace("\t", "    "))
            while stack and stack[-1] > ind:
                stack.pop()
            if not stack or stack[-1] < ind:
                stack.append(ind)
            d = len(stack) - 1
            t = m.group(4).strip()
            target().append({"k": "li", "id": ids.make(f"{base()}-{h8(t)}"), "d": d, "n": m.group(3) or "", "t": t})
            continue
        t = line.strip()
        ind = len(line) - len(line.lstrip())
        target().append({"k": "p", "id": ids.make(f"{base()}-{h8(t)}"), "t": t, "d": 1 if ind and stack else 0})
    if fence:
        t = "\n".join(fence).strip("\n")
        target().append({"k": "pre", "id": ids.make(f"{base()}-{h8(t)}"), "t": t})

    has5 = any("다섯 질문" in s["h"] for s in secs)
    first_other = True
    for s in secs:
        if mode == "card":
            pin = ("머리" in s["h"]) or ("다섯 질문" in s["h"])
            if not pin and not has5 and first_other:
                pin = True
            if "머리" not in s["h"]:
                first_other = False
        else:
            pin = mode == "grid"
        s["pin"] = pin
        s["open"] = mode != "card"
        s["id"] = ids.make(f"{slug}-o-{s['code']}")
        if art and SELFTEST_RE.search(s["h"]):
            mark_answers(s["items"])
        if mode == "grid":  # 1층 카드: 세부 줄 "질문 → 답"을 나눠 둠
            for it in s["items"]:
                if it["k"] == "li" and it.get("d", 0) >= 1 and " → " in it["t"]:
                    q, a_ = it["t"].split(" → ", 1)
                    it["qa2"] = [q.strip(), a_.strip()]
    return {"title": title, "intro": intro, "secs": secs}


# 층: (키, 이름, 그리는 방식, 파일들). {s}는 회사 slug
OV_LAYERS = {
    "co": [
        ("L1", "한 화면 카드", "grid", ["kb/cards6/{s}.md"]),
        ("LR", "매출로 본 성공 원인", "doc", ["kb/revenue/{s}.md"]),
        ("L2", "쉬운 해설", "easy", ["kb/easy/{s}.md"]),
        ("L3", "개요 문서와 질문 답", "doc", ["kb/cards/{s}.md", "kb/pm_q2/{s}.md"]),
    ],
    "common": [
        ("L1", "한 화면 카드", "grid", ["kb/cards6/common.md"]),
        ("LR", "매출로 본 성공 원인", "doc", ["kb/revenue/00_공통.md"]),
        ("L2", "쉬운 해설", "easy", ["kb/easy/00_기초.md"]),
        ("L3", "개요 문서와 질문 답", "doc", ["kb/cards/common.md", "kb/pm_q2/00_공통.md", "kb/pm_q2/추가조사_261118.md"]),
    ],
}
PART_LABEL = [("kb/cards/", "개요 문서"), ("kb/pm_q2/추가조사", "추가 조사"), ("kb/pm_q2/", "PM 2차 질문과 답")]


@lru_cache(maxsize=1)
def _old_rows():
    """옛 화면(web/index.html) 데이터의 Ondo 본문 줄: on-#### → 줄."""
    p = ROOT / "web/index.html"
    if not p.exists():
        return {}
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', p.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    D = json.loads(m.group(1).replace("<\\/", "</"))
    out = {}
    for co in D.get("companies", []):
        for sec in co.get("sections", []):
            for r in sec.get("rows", []):
                if r.get("id"):
                    out[r["id"]] = r
    return out


@lru_cache(maxsize=1)
def _facts_sources():
    return ({r["fact_id"]: r for r in read_dicts(ROOT / "db/facts.csv")},
            {r["source_id"]: r for r in read_dicts(ROOT / "db/sources.csv")})


def resolve_tag(tag, news):
    """카드 태그 → {k: 종류, items: [{t 제목, q 원문 인용, url, f 사실 번호}]}."""
    if tag in ("해석", "추정", "사용자 확인"):
        return {"k": {"해석": "i", "추정": "e"}.get(tag, "u"), "items": []}
    if re.fullmatch(r"N\d+", tag):
        n = news.get(tag)
        return {"k": "n", "items": [{"t": n["title"], "q": "", "url": n.get("url", ""), "f": ""}] if n else []}
    if tag.startswith("on-"):
        r = _old_rows().get(tag)
        if not r:
            return {"k": "s", "items": [], "miss": True}
        facts, srcs = _facts_sources()
        items = []
        for f in r.get("ids") or []:
            fr = facts.get(f)
            if not fr:
                continue
            sid = (fr.get("source_id") or "").split(";")[0].strip()
            items.append({"t": (srcs.get(sid) or {}).get("제목") or fr.get("링크", ""), "q": fr.get("원문 근거 문장", ""),
                          "url": (fr.get("링크") or "").split(";")[0].strip(), "f": f})
        if not items:  # 사실 번호가 없는 줄은 옛 화면에 붙은 원문
            items = [{"t": x.get("t", ""), "q": x.get("q", ""), "url": x.get("url", ""), "f": ""} for x in r.get("src") or []]
        return {"k": "s", "items": items, "row": r.get("text", "")}
    return {"k": "s", "items": [], "miss": True}


def build_odx(slug, ids):
    """개요 패키지 카드: 줄마다 id를 주고 태그를 원문으로 풂."""
    pk = ondo_card.load(slug)
    if not pk:
        return None
    card = json.loads(json.dumps(pk["card"]))
    news = {n["id"]: n for n in pk.get("sources_new", [])}
    tags = {}

    def it_ids(it, sec):
        it["id"] = ids.make(f"{slug}-o-L1x-{sec}-{h8(it.get('t') or it.get('k') or '')}")
        for t in it.get("tags") or []:
            tags.setdefault(t, None)
        tb = it.get("table")
        if tb:
            it["table"] = {"cols": tb["head"], "rows": [{"id": ids.make(f"{slug}-o-L1x-{sec}-{h8(' | '.join(r))}"), "c": r} for r in tb["rows"]]}
        for s2 in it.get("sub") or []:
            it_ids(s2, sec)
        for k in it.get("kids") or []:
            it_ids(k, sec)

    for row in card["rows"]:
        sec = h8(row["label"])[:5]
        row["id"] = ids.make(f"{slug}-o-L1x-{sec}")
        for it in row.get("items") or []:
            it_ids(it, sec)
        for it in row.get("path") or []:
            it_ids(it, sec)
    # 핵심 포인트의 이동 버튼: go = {"row": 행 이름, "find": 대상 줄 글 조각} → goid(대상 줄 id)
    plain = lambda x: re.sub(r"==|!!|\*\*", "", x or "")
    index = {}
    def idx(it, lab):
        if it.get("id") and (it.get("t") or it.get("k")):
            index.setdefault(lab, []).append((plain((it.get("k2") or "") + " " + (it.get("t") or "")), it["id"]))
        tb = it.get("table")
        if tb and isinstance(tb, dict) and tb.get("rows") and isinstance(tb["rows"][0], dict):
            for r in tb["rows"]:
                index.setdefault(lab, []).append((plain(" | ".join(map(str, r["c"]))), r["id"]))
        for x in (it.get("sub") or []) + (it.get("kids") or []):
            idx(x, lab)
    for row in card["rows"]:
        for it in (row.get("items") or []) + (row.get("path") or []):
            idx(it, row["label"])
    def resolve(it):
        g = it.get("go")
        if g:
            hits = [i for t, i in index.get(g.get("row"), []) if g.get("find") and g["find"] in t]
            if hits:
                it["goid"] = hits[0]
            else:
                print(f"  ! {slug} 이동 버튼 대상 없음: {g}")
        for x in it.get("kids") or []:
            resolve(x)
    for row in card["rows"]:
        for it in row.get("items") or []:
            resolve(it)
    flows = {k: ondo_card.flow_html(v) for k, v in pk.get("flows", {}).items()}
    titles = {k: v.get("title", "") for k, v in pk.get("flows", {}).items()}
    return {"card": card, "flows": flows, "ftitles": titles, "tags": {t: resolve_tag(t, news) for t in tags},
            "news": pk.get("sources_new", []), "path": rel(ondo_card.card_path(slug))}


def build_overview(slug, ids):
    layers = []
    for k, label, kind, paths in OV_LAYERS["common" if slug == "common" else "co"]:
        parts = []
        for pth in paths:
            rp = pth.format(s=slug)
            fp = ROOT / rp
            lab = next((v for pre_, v in PART_LABEL if rp.startswith(pre_)), label)
            doc = None
            if fp.exists():
                txt = fp.read_text(encoding="utf-8")
                if kind == "grid":
                    doc = parse_card(slug, txt, ids, layer=k, mode="grid")
                elif kind == "easy":
                    doc = parse_card(slug, txt, ids, layer=k, mode="open", art=True)
                elif rp.startswith("kb/cards/"):
                    doc = parse_card(slug, txt, ids)  # 지금 개요 문서: 줄 id를 전과 같게 둠
                else:
                    doc = parse_card(slug, txt, ids, layer=rp, mode="open", art=True)
            part = {"path": rp, "label": lab, "doc": doc}
            if k == "L1" and slug != "common":  # 1층은 회사 개요 카드 JSON(Ondo는 inputs/ondo_overview_261118 사본, 다른 회사는 kb/<slug>_overview)
                odx = build_odx(slug, ids)
                if odx:
                    part = {"path": odx.pop("path"), "label": lab, "doc": None, "odx": odx}
            parts.append(part)
        layers.append({"k": k, "label": label, "kind": kind, "id": ids.make(f"{slug}-o-{k}"), "parts": parts})
    ov = {"layers": layers}
    if slug in DEEP:
        ov["deep"] = DEEP[slug]  # 개요 맨 위 "깊이 보기" 링크(상대 경로)
    return ov


# ---------------- 지난 본문(companies/<회사>_vN.md) ----------------
OLD_RE = re.compile(r"^(\s*)([●★\-*]|\d+[.)])\s*(.*)$")


def parse_old(slug, text, ids):
    out = []
    sec = "intro"
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("!["):
            continue
        if line.startswith("#"):
            t = line.lstrip("#").strip()
            sec = h8(t)[:5]
            out.append({"k": "h", "id": ids.make(f"{slug}-r-old-{sec}"), "t": t})
            continue
        m = OLD_RE.match(line)
        if m:
            ind = len(m.group(1))
            mark = m.group(2)
            d = 0 if mark == "●" else (1 if mark == "★" else min(3, 1 + ind // 2))
            if mark.startswith(tuple("0123456789")):
                d = min(3, ind // 2)
            t = m.group(3).strip()
        else:
            d, t = 0, line.strip()
        fs = list(dict.fromkeys(re.findall(r"F-\d{4}", t)))  # 줄에 붙은 근거(줄 안 중복은 한 번)
        out.append({"k": "l", "id": ids.make(f"{slug}-r-old-{sec}-{h8(t)}"), "d": d, "m": m.group(2) if m else "", "t": t, "f": fs})
    return out


# ---------------- 뜻 풀이 ----------------
def term_keys(term):
    term = term.strip()
    keys = [term]
    m = re.match(r"^(.+?)\s*[(（](.+?)[)）]$", term)
    if m:
        keys += [m.group(1).strip(), m.group(2).strip()]
    if " / " in term:
        keys += [p.strip() for p in term.split(" / ")]
    return [k for k in dict.fromkeys(keys) if len(k) >= 2 and k not in TERM_STOP]


def pick(head, names):
    for n in names:
        for i, h in enumerate(head):
            if h.replace(" ", "") == n.replace(" ", ""):
                return i
    return None


def load_terms():
    entries = []  # [용어, 원어, 뜻, 출처, 회사 slug 또는 ""]
    keys = {}     # key → {"g": 전체 우선 entry, "c": {slug: entry}}
    PRI = {}      # entry → 우선순위(작을수록 앞)

    def add(term, orig, mean, src, co, pri):
        if not term or not mean:
            return
        idx = len(entries)
        entries.append([term, orig, mean, src, co])
        PRI[idx] = pri
        for k in term_keys(term):
            slot = keys.setdefault(k, {"g": None, "c": {}})
            if co:
                slot["c"].setdefault(co, idx)
            if slot["g"] is None or pri < PRI[slot["g"]]:
                slot["g"] = idx

    counts = {}
    gm = ROOT / "kb/glossary_main.csv"
    if gm.exists():
        head, body = read_csv(gm)
        ti, mi, si = pick(head, ["용어"]) or 0, pick(head, ["뜻"]), pick(head, ["출처"])
        mi = 1 if mi is None else mi
        si = 2 if si is None else si
        for r in body:
            add(r[ti], "", r[mi] if mi < len(r) else "", r[si] if si < len(r) else "", "", 0)
        counts["kb/glossary_main.csv"] = len(body)
    for p in sorted((ROOT / "kb/glossary_add").glob("*.csv")):
        co = p.stem.lower()
        head, body = read_csv(p)
        if not head:
            continue
        ti = pick(head, ["용어", "term", "말"])
        mi = pick(head, ["뜻", "뜻 한 줄", "쉬운 뜻", "설명", "meaning"])
        si = pick(head, ["출처", "출처 링크", "링크", "source", "url"])
        if ti is None and mi is None:  # 머리줄이 없는 파일
            body = [head] + body
            ti, mi, si = 0, 1, 2
        ti = 0 if ti is None else ti
        mi = 1 if mi is None else mi
        for r in body:
            src = r[si] if si is not None and si < len(r) else ""
            add(r[ti], "", r[mi] if mi < len(r) else "", src, co if co in SLUGS + [COMMON[0]] else "", 1)
        counts[rel(p)] = len(body)
    tp = ROOT / "db/terms.csv"
    if tp.exists():
        rows = read_dicts(tp)
        for r in rows:
            sid = (r.get("source_id") or "").strip()
            add((r.get("용어") or "").strip(), (r.get("원어") or "").strip(), (r.get("쉬운 뜻") or "").strip(),
                "db/terms.csv" + (f" ({sid})" if sid else ""), "", 2)
        counts["db/terms.csv"] = len(rows)
    kk = {k: [v["g"], v["c"]] for k, v in keys.items()}
    return {"e": entries, "k": kk, "n": counts}


# ---------------- 회사 하나 ----------------
def co_match(val, slug):
    v = (val or "").lower()
    return slug in v or (slug == "kraken" and "payward" in v)


def build_company(slug, name, prefix, facts_all, facts_by_id, sources_by_id):
    ids = Ids()
    C = {"slug": slug, "name": name, "files": {}, "refs": {}}
    have = C["files"]

    # 개요(세 층)
    C["ov"] = build_overview(slug, ids)
    have["ov"] = [p["path"] for L in C["ov"]["layers"] for p in L["parts"] if p["doc"]]

    # 1) PM 질문별 답
    cov = ROOT / f"kb/coverage/{slug}.csv"
    if cov.exists():
        head, body = read_csv(cov)
        C["cov"] = table(ids, f"{slug}-r-cov", head, body)
        have["cov"] = rel(cov)
    else:
        C["cov"] = None
    qp = ROOT / f"kb/questions/{slug}.json"
    if qp.exists():
        qs = json.loads(qp.read_text(encoding="utf-8"))
        if isinstance(qs, dict):
            qs = qs.get("questions") or list(qs.values())
        for q in qs:
            q["_id"] = ids.make(f"{slug}-r-q-{safe(q.get('id') or h8(q.get('q', '')))}")
            if q.get("id"):
                C["refs"][q["id"]] = q["_id"]
        C["qs"] = qs
        have["qs"] = rel(qp)
    else:
        C["qs"] = None

    # 2) 사건 카드
    ep = ROOT / f"kb/events/{slug}.json"
    fid_refs = set()
    if ep.exists():
        evs = json.loads(ep.read_text(encoding="utf-8"))
        for e in evs:
            e["_id"] = ids.make(f"{slug}-r-ev-{safe(e.get('id') or h8(e.get('title', '')))}")
            if e.get("id"):
                C["refs"][e["id"]] = e["_id"]
            fid_refs.update(e.get("fids") or [])
            for w in e.get("why") or []:
                if isinstance(w, dict):
                    fid_refs.update(w.get("fids") or [])
            e.pop("rows", None)  # 옛 화면 줄 번호(이 화면에서는 쓰지 않음)
        C["ev"] = evs
        have["ev"] = rel(ep)
    else:
        C["ev"] = None

    # 3) 구조 표
    sd = ROOT / f"kb/structs/{slug}"
    sts = []
    if sd.is_dir():
        files = sorted(sd.glob("*.csv"), key=lambda p: (STRUCT_ORDER.index(p.stem) if p.stem in STRUCT_ORDER else 99, p.stem))
        for p in files:
            head, body = read_csv(p)
            idcol = head.index("번호") if "번호" in head else None
            # 번호가 있는 줄은 번호만으로 id를 줌(개요의 [KR-M01] 같은 근거 번호가 이 줄로 감)
            t = table(ids, f"{slug}-r-st-{safe(p.stem)}", head, body, idcol=idcol, keybase=f"{slug}-r-st")
            for row in t["rows"]:
                if row["k"]:
                    C["refs"][row["k"]] = row["id"]
            t["id"] = f"{slug}-r-st-{safe(p.stem)}"
            t["file"] = p.stem
            t["label"] = STRUCT_LABEL.get(p.stem, p.stem)
            t["path"] = rel(p)
            for r in body:
                for c in r:
                    fid_refs.update(re.findall(r"F-\d{4}", c))
            sts.append(t)
        have["st"] = rel(sd)
    C["st"] = sts

    # 7) 지난 본문 (사실 참조를 모으려고 먼저 읽음)
    olds = sorted(ROOT.glob(f"companies/{prefix}_v*.md"),
                  key=lambda p: int(re.search(r"_v(\d+)\.md$", p.name).group(1)) if re.search(r"_v(\d+)\.md$", p.name) else 0)
    if olds:
        op = olds[-1]
        otext = op.read_text(encoding="utf-8")
        C["old"] = {"path": rel(op), "lines": parse_old(slug, otext, ids)}
        fid_refs.update(re.findall(r"F-\d{4}", otext))
        have["old"] = rel(op)
    else:
        C["old"] = None

    if C["qs"]:
        fid_refs.update(re.findall(r"F-\d{4}", json.dumps(C["qs"], ensure_ascii=False)))
    if C["cov"]:
        fid_refs.update(re.findall(r"F-\d{4}", json.dumps(C["cov"], ensure_ascii=False)))

    # 6) 빈칸과 정정
    gaps = []
    gp = ROOT / "kb/gaps.csv"
    if gp.exists():
        head, body = read_csv(gp)
        ci = head.index("회사") if "회사" in head else None
        body = [r for r in body if ci is None or co_match(r[ci], slug)]
        gaps.append({"label": "빈칸", "path": rel(gp), **table(ids, f"{slug}-r-gap-g", head, body)})
    ga = ROOT / f"kb/gaps_add/{slug}.csv"
    if ga.exists():
        head, body = read_csv(ga)
        gaps.append({"label": "빈칸 추가", "path": rel(ga), **table(ids, f"{slug}-r-gap-a", head, body)})
        have["gaps_add"] = rel(ga)
    else:
        gaps.append({"label": "빈칸 추가", "path": f"kb/gaps_add/{slug}.csv", "missing": True})
    cp = ROOT / "kb/corrections.csv"
    if cp.exists():
        head, body = read_csv(cp)
        ci = head.index("회사") if "회사" in head else None
        body = [r for r in body if ci is None or co_match(r[ci], slug)]
        gaps.append({"label": "정정", "path": rel(cp), **table(ids, f"{slug}-r-gap-c", head, body)})
    for g in gaps:
        for r in g.get("rows", []):
            for c in r["c"]:
                fid_refs.update(re.findall(r"F-\d{4}", c))
    C["gaps"] = gaps

    # 4) 사실 DB: 이 회사 줄 + 다른 칸이 근거로 가리키는 줄
    own = [f for f in facts_all if FACT_CO.get(f["회사"]) == slug]
    own_ids = {f["fact_id"] for f in own}
    extra = sorted(fid_refs - own_ids)
    fl = []
    for f in own + [facts_by_id[x] for x in extra if x in facts_by_id]:
        row = [f.get(c, "") or "" for c in FACT_COLS]
        row.append("" if f["fact_id"] in own_ids else "1")
        fl.append(row)
        ids.make(f"{slug}-r-f-{f['fact_id']}")
    fl.sort(key=lambda r: r[0])
    C["facts"] = fl
    C["fmissing"] = sorted(x for x in extra if x not in facts_by_id)

    # 5) 원본 목록
    sids = []
    for r in fl:
        for s in re.split(r"[;,\s]+", r[FACT_COLS.index("source_id")]):
            if s in sources_by_id and s not in sids:
                sids.append(s)
    C["srcs"] = [[s["source_id"], s.get("제목", ""), s.get("발행 주체", ""), s.get("발행일", ""), s.get("링크", ""), s.get("저장 파일 경로", ""), s.get("출처 종류", "")]
                 for s in sorted((sources_by_id[x] for x in sids), key=lambda s: s["source_id"])]
    if slug == "ondo":
        pk = ondo_card.load()
        for n in (pk or {}).get("sources_new", []):
            C["srcs"].append([n["id"], n.get("title", ""), "", "", n.get("url", ""), "inputs/ondo_overview_261118/content/sources_new.csv", "새 출처(개요 카드)"])
    for s in C["srcs"]:
        ids.make(f"{slug}-r-src-{s[0]}")
    return C


ANS_COLS = {"mid": "mid", "co": "co", "view": "view", "anchor": "anchor", "sec": "sec", "quote": "quote",
            "메모": "memo", "답": "ans", "고친 곳": "fix", "상태": "st"}


def load_answers():
    """kb/memo_answers.csv: 메모에 대한 답. 파일이 없거나 비었거나 깨져도 빈 목록."""
    p = ROOT / "kb/memo_answers.csv"
    if not p.exists():
        return []
    try:
        with open(p, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
    except Exception as e:  # 쓰는 중인 파일
        print(f"경고: kb/memo_answers.csv를 읽지 못함({e})")
        return []
    out = []
    for r in rows:
        r = {(k or "").strip(): (v or "").strip() if isinstance(v, str) else "" for k, v in r.items()}
        a = {short: r.get(col, "") for col, short in ANS_COLS.items()}
        if a["mid"] and (a["ans"] or a["fix"] or a["st"]):
            out.append(a)
    return out


def build_common():
    ids = Ids()
    ov = build_overview(COMMON[0], ids)
    return {"slug": COMMON[0], "name": COMMON[1], "common": True, "refs": {},
            "files": {"ov": [p["path"] for L in ov["layers"] for p in L["parts"] if p["doc"]]},
            "ov": ov, "cov": None, "qs": None, "ev": None, "st": [], "facts": [], "fmissing": [], "srcs": [], "gaps": [], "old": None}


def main():
    facts_all = read_dicts(ROOT / "db/facts.csv")
    facts_by_id = {f["fact_id"]: f for f in facts_all}
    sources_by_id = {s["source_id"]: s for s in read_dicts(ROOT / "db/sources.csv")}
    data = {
        "built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "cos": [[s, n] for s, n, _ in COS] + ([] if COMMON[0] in SLUGS else [list(COMMON)]),
        "fcols": FACT_COLS + ["ref"],
        "terms": load_terms(),
        "ans": load_answers(),
        "C": {},
    }
    for slug, name, prefix in COS:
        if slug == COMMON[0]:
            continue
        data["C"][slug] = build_company(slug, name, prefix, facts_all, facts_by_id, sources_by_id)
    data["C"][COMMON[0]] = build_common()

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    assert "__DATA__" in tpl
    html = tpl.replace("__DATA__", payload, 1).replace("/*__FLOW_CSS__*/", ondo_card.FLOW_CSS, 1)
    out = HERE / "index.html"
    out.write_text(html, encoding="utf-8")

    print(f"web/v5/index.html {len(html.encode('utf-8')) // 1024} KB, 만든 시각 {data['built']}")
    print(f"메모 답 {len(data['ans'])}줄(kb/memo_answers.csv)")
    t = data["terms"]
    print(f"용어 {len(t['e'])}개(맞출 말 {len(t['k'])}개): " + ", ".join(f"{k} {v}" for k, v in t["n"].items()))
    for slug, C in data["C"].items():
        lay = " / ".join(f"{L['k']} " + ("+".join(p["path"].split("/")[-2] + "/" + p["path"].split("/")[-1] for p in L["parts"] if p["doc"]) or "준비 중") for L in C["ov"]["layers"])
        miss = [k for k in ("cov", "qs", "ev", "st", "gaps_add") if k not in C["files"]] if not C.get("common") else []
        print(f"- {slug}: 개요 {lay}" + ("" if C.get("common") else f" | 사건 {len(C['ev'] or [])}, 구조 표 {len(C['st'])}, 사실 {len(C['facts'])}, 원본 {len(C['srcs'])}")
              + (f" | raw 준비 중: {', '.join(miss)}" if miss else ""))

if __name__ == "__main__":
    main()
