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

ID_RE = re.compile(r"\[((?:F-\d{4})|(?:TP-\d{3})|(?:KR-[^\]]+)|(?:US-[^\]]+)|(?:EU-[^\]]+)|(?:CASE-[^\]]+))\]")
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://\S+")
LINK_RE = re.compile(r"\{([a-z]{2}-[0-9a-z]{4,})\}")
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
    for key, code in (("물결", "물결"), ("출신", "출신"), ("고객 화면", "화면"), ("등록 종류", "등록"), ("KDX 질문", "질문"), ("기업별 한 줄", "한줄"), ("사업 범위", "범위"), ("개요", "개요"), ("발언", "발언"), ("연결", "연결"), ("차이", "차이"), ("판단", "판단")):
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
tparty = {r["tp_id"]: r for r in load_csv(ROOT / "db/third_party.csv")}


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
        elif i in tparty:
            t = tparty[i]
            url = (t.get("링크") or "").split(" ")[0].strip()
            if not url.startswith("http"):
                url = ""
            where = f'{t.get("쪽","")}쪽' if t.get("쪽", "").replace("~", "").replace(",", "").replace(" ", "").isdigit() else t.get("쪽", "")
            out.append({"q": (t.get("원문") or "").strip(), "url": url,
                        "t": f'{t.get("발행처","")}, {t.get("자료 제목","")} ({t.get("발간일","")}, {where}). 입장: {t.get("발행처 입장","")}',
                        "e": (t.get("내용") or "").strip()})
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
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            prev = cur["rows"][-1] if cur["rows"] else None
            level = "tr" if prev and prev["level"] in ("th", "tr") else "th"
            cl = []
            for c in cells:
                cl.append({"t": LINK_RE.sub("", ID_RE.sub("", c)).strip(), "links": LINK_RE.findall(c), "ids": ID_RE.findall(c)})
            ids = [i for c in cl for i in c["ids"]]
            cur["rows"].append({"level": level, "cells": cl, "raw": s, "ids": ids, "src": evidence(ids),
                                "links": [l for c in cl for l in c["links"]], "label": None, "text": " | ".join(c["t"] for c in cl)})
            continue
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
        links = LINK_RE.findall(body)
        text = LINK_RE.sub("", ID_RE.sub("", body)).strip()
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
               "src": evidence(ids), "ids": ids, "links": links}
        if label == "해석":
            row["interp"] = True
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
    tabs, cur, head = [], None, ""
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            head = line[3:].strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if cur is None:
                cur = {"head": cells, "rows": [], "sec": head}
                tabs.append(cur)
            else:
                cur["rows"].append(cells)
        else:
            cur = None
    return tabs


FIG_CAP = {
 "R2_p10_provider_comparison_table": "사업자 10곳 비교표. CoinDesk Research 10쪽, 2026-08 기준, Bullish 의뢰. Coinbase 열 없음. Binance와 Dinari를 같은 보관형으로 묶었지만 우리 분류는 다름(아래 표)",
 "R2_p06_three_models_table": "세 모델 표(발행사 직접, 보관형, 합성형). CoinDesk Research 6쪽, 2026-09, Bullish 의뢰",
 "R1_p19_four_types_diagram": "네 방식 한 장 그림(직접, 권리, 간접, 무기한선물). 포필러스 19쪽, 2026-02, Securitize 후원",
 "R1_p20_model_comparison_table": "네 방식 비교표. 포필러스 20쪽, 2026-02, Securitize 후원. 간접을 스와프로 묶은 칸은 우리 분류와 다름",
 "R1_p31_ecosystem_by_type": "방식별 사업자. 포필러스 31쪽, 2026-02, Securitize 후원",
 "R1_p36_indirect_platforms_table": "Robinhood, Backed, Ondo, Dinari 비교표. 포필러스 36쪽, 2026-02 기준(Robinhood 지갑판, Dinari 미국판 이전), Securitize 후원",
 "R1_p68_lifecycle_diagram": "주식 토큰 생애주기(발행, 상장, 가격 형성, 유동성, 담보, 상환). 포필러스 68쪽, 2026-02, Securitize 후원",
 "R1_p76_value_by_platform_2026-01": "발행 플랫폼별 잔액(rwa.xyz, 2026-01-27). 포필러스 76쪽, Securitize 후원",
 "W1_sentora_rwa_league_table_2026-01": "rwa.xyz 순위표(2026-01 초). Sentora 주간 글, 2026-01-09",
 "R1_p73_ecosystem_map": "주식 토큰 생태계 지도. 포필러스 73쪽, 2026-02 기준, Securitize 후원",
 "R2_p04_how_ownership_moves_today": "지금 주식 소유권이 움직이는 길과 단계별 마찰. CoinDesk Research 4쪽, 2026-09, Bullish 의뢰",
 "R2_p07a_issuer_sponsored": "발행사 직접 방식 흐름. CoinDesk Research 7쪽, Bullish 의뢰",
 "R2_p07b_custodial": "보관형 흐름(미국법 구조). CoinDesk Research 7쪽, Bullish 의뢰. Binance, Coinbase는 아부다비 신탁 구조라 회사 본문은 투자설명서를 따름",
 "R2_p08_synthetic": "합성형 흐름. CoinDesk Research 8쪽, Bullish 의뢰",
 "R1_p22_direct_tokenization": "직접 방식 흐름. 포필러스 22쪽, Securitize 후원",
 "R1_p24_entitlement_tokenization": "권리 방식 흐름(DTC 장부를 블록체인으로). 포필러스 24쪽, Securitize 후원",
 "R1_p26_indirect_tokenization": "간접 방식 흐름. 포필러스 26쪽, Securitize 후원",
 "R1_p10_traditional_trade_lifecycle": "기존 주식 거래 흐름. 포필러스 10쪽, Securitize 후원",
 "R1_p47_us_license_types": "미국 자격 3종(명의개서대리인, 브로커딜러, ATS). 포필러스 47쪽, Securitize 후원",
}
FIG_WHERE = {"compare": ["R2_p10_provider_comparison_table", "R2_p06_three_models_table", "R1_p19_four_types_diagram",
                         "R1_p20_model_comparison_table", "R1_p31_ecosystem_by_type", "R1_p36_indirect_platforms_table", "R1_p68_lifecycle_diagram"],
             "past": ["W1_sentora_rwa_league_table_2026-01", "R1_p76_value_by_platform_2026-01"],
             "lic": ["R1_p73_ecosystem_map"],
             "rules": ["R2_p04_how_ownership_moves_today", "R1_p10_traditional_trade_lifecycle", "R2_p07a_issuer_sponsored", "R1_p22_direct_tokenization",
                       "R1_p24_entitlement_tokenization", "R2_p07b_custodial", "R2_p08_synthetic", "R1_p26_indirect_tokenization", "R1_p47_us_license_types"]}
PAST = {"ondo": ("TP-001", 413.4e6, "51.59", 1), "kraken": ("TP-002", 195.3e6, "24.37", 2), "securitize": ("TP-003", 144.4e6, "18.02", 3), "dinari": ("TP-004", 3.0e6, "0.37", 7)}


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
    for r in rank:
        k = r["slug"] or ("securitize" if "Securitize" in r["name"] else None)
        if k in PAST:
            tp, usd, share, rk = PAST[k]
            r["past"] = {"usd": usd, "share": share, "rank": rk, "x": round(r["usd"] / usd, 1), "src": evidence([tp])}
    out["rank"] = rank
    out["rank_total"] = {"now": float(facts.get("F-1028", {}).get("값") or 0), "past": 801.36e6, "src": evidence(["TP-005", "F-1028"])}
    out["figs"] = {where: [{"k": img_key(f"../captures/reports/{n}.png"), "c": FIG_CAP.get(n, n)} for n in names] for where, names in FIG_WHERE.items()}
    out["cls"] = [dict(r, src=src_of(r.pop("tp_ids", ""))) for r in load_csv(ROOT / "db/cross_class.csv")]
    out["axis"] = [dict(r, src=src_of(r.pop("fact_ids", ""))) for r in load_csv(ROOT / "db/cross_axis.csv")]
    pv = ROOT / "kb/perp_vs_spot.md"
    out["perp"] = []
    if pv.exists():
        for tb in md_tables(pv):
            rows = []
            for row in tb["rows"]:
                ids = re.findall(r"TP-\d{3}|F-\d{4}", " ".join(row))
                rows.append({"cells": [re.sub(r"\[?(?:TP-\d{3}|F-\d{4})\]?[,; ]*", "", c).strip() for c in row], "src": evidence(ids)})
            out["perp"].append({"sec": tb["sec"], "head": tb["head"], "rows": rows})
        concl = re.search(r"##[^\n]*결론[^\n]*\n(.*?)(?:\n## |\Z)", pv.read_text(encoding="utf-8"), re.S)
        out["perp_concl"] = [l.strip("- ").strip() for l in (concl.group(1).splitlines() if concl else []) if l.strip().startswith(("-", "1", "2", "3"))]
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
    common, tp_reg = [], []
    for tb in tabs:
        if "제3자" in tb["sec"]:
            for row in tb["rows"]:
                ids = re.findall(r"TP-\d{3}|F-\d{4}", " ".join(row))
                tp_reg.append({"cells": row, "head": tb["head"], "src": evidence(ids)})
    out["tp_reg"] = tp_reg
    ctab = next((tb for tb in tabs if "공통 줄" in tb["sec"]), None)
    if ctab:
        for row in ctab["rows"]:
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
    plan = [("__overview__", "전체 그림", "overview", "ov")] + list(ORDER)
    for base, name, kind, prefix in plan:
        p = ROOT / "kb/overview.md" if base == "__overview__" else latest_body(base)
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
        companies.append({"slug": SLUG.get(prefix, "overview"), "name": name, "kind": kind, "logo": logo,
                          "sections": sections})
        print(f"{name}: {p.name}, {sum(len(s['rows']) for s in sections)}줄")

    store_p.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")
    # 본문 줄 링크 풀기: {kr-0215} → 회사, 화면 번호, 그 줄의 근거
    idx = {}
    for c in companies:
        for sec in c["sections"]:
            for r in sec["rows"]:
                idx[r["id"]] = (c["slug"], r)
    bad = []
    def res(lid):
        if lid not in idx:
            bad.append(lid)
            return None
        slug, r = idx[lid]
        return {"id": lid, "co": slug, "disp": r["disp"]}
    for c in companies:
        for sec in c["sections"]:
            for r in sec["rows"]:
                if r.get("links"):
                    r["links"] = [x for x in (res(l) for l in r["links"]) if x]
                    extra = [i for l in r["links"] for i in idx[l["id"]][1].get("ids", []) if i not in r.get("ids", [])]
                    have = {(e.get("url"), e.get("q", "")[:80]) for e in r["src"]}
                    for e in evidence(list(dict.fromkeys(extra))):
                        if (e.get("url"), e.get("q", "")[:80]) not in have:
                            r["src"].append(e)
                for cl in r.get("cells", []):
                    cl["links"] = [x for x in (res(l) for l in cl["links"]) if x]
                if r.get("level") not in ("img", "th") and c["kind"] == "overview" and not r.get("ids") and not r.get("links") and r.get("text") and " : " not in (r.get("label") or "") and r["level"] != "b":
                    print("  근거 없는 전체 그림 줄:", r["disp"], r.get("text", "")[:40], file=sys.stderr)
    if bad:
        print("  찾지 못한 줄 링크:", sorted(set(bad)), file=sys.stderr)

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
