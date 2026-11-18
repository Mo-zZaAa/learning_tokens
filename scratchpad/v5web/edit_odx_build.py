"""build.py: Ondo 1층을 개요 패키지 카드로. 일회성 편집."""
p = '/home/user/learning_tokens/web/v5/build.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


rep("from pathlib import Path\n", "from functools import lru_cache\nfrom pathlib import Path\n\nimport ondo_card  # 같은 폴더: Ondo 개요 패키지 그림(깊이 보기 페이지와 같은 그림)\n")

rep("def build_overview(slug, ids):", '''@lru_cache(maxsize=1)
def _old_rows():
    """옛 화면(web/index.html) 데이터의 Ondo 본문 줄: on-#### → 줄."""
    p = ROOT / "web/index.html"
    if not p.exists():
        return {}
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', p.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    D = json.loads(m.group(1).replace("<\\\\/", "</"))
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
    if re.fullmatch(r"N\\d+", tag):
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
    pk = ondo_card.load()
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
    flows = {k: ondo_card.flow_html(v) for k, v in pk.get("flows", {}).items()}
    titles = {k: v.get("title", "") for k, v in pk.get("flows", {}).items()}
    return {"card": card, "flows": flows, "ftitles": titles, "tags": {t: resolve_tag(t, news) for t in tags},
            "news": pk.get("sources_new", []), "path": rel(ondo_card.JSON_PATH)}


def build_overview(slug, ids):''')

rep('''            parts.append({"path": rp, "label": lab, "doc": doc})
        layers.append(''', '''            part = {"path": rp, "label": lab, "doc": doc}
            if slug == "ondo" and k == "L1":  # Ondo 1층은 개요 패키지 카드(inputs/ondo_overview_261118)
                odx = build_odx(slug, ids)
                if odx:
                    part = {"path": odx.pop("path"), "label": lab, "doc": None, "odx": odx}
            parts.append(part)
        layers.append(''')

# N01~N21을 Ondo 원본 목록에
rep('''    for s in C["srcs"]:
        ids.make(f"{slug}-r-src-{s[0]}")''', '''    if slug == "ondo":
        pk = ondo_card.load()
        for n in (pk or {}).get("sources_new", []):
            C["srcs"].append([n["id"], n.get("title", ""), "", "", n.get("url", ""), "inputs/ondo_overview_261118/content/sources_new.csv", "새 출처(개요 카드)"])
    for s in C["srcs"]:
        ids.make(f"{slug}-r-src-{s[0]}")''')

rep('''    html = tpl.replace("__DATA__", payload, 1)''', '''    html = tpl.replace("__DATA__", payload, 1).replace("/*__FLOW_CSS__*/", ondo_card.FLOW_CSS, 1)''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
