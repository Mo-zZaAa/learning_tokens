"""Ondo 개요 패키지(inputs/ondo_overview_261118)의 그림(flows)을 HTML로 그린다.

web/v5/build.py(개요 1층)와 scratchpad/ondodeep/gen.py(깊이 보기 S6)가 같은 함수와 같은 CSS를 써서
두 곳의 그림이 같은 모양이 되게 한다.
상자 종류: ondo 보라(Ondo 그룹 법인과 Ondo 몫), ext 청록(외부 회사), inv 회색(투자자),
none 점선(관여 없음), ondo_dash 보라 점선(면제 중인 Ondo 몫). 배지: earn 보라, zero 점선.
화살표: r →, l ←, "" 없음. 좁은 화면에서는 상자를 세로로 쌓는다.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "inputs/ondo_overview_261118"
JSON_PATH = ROOT / "kb/ondo_overview/ondo_overview.json"  # 사용자 패키지 사본(고친 곳은 같은 폴더 고친곳.md)
if not JSON_PATH.exists():
    JSON_PATH = PKG / "content/ondo_overview.json"

FLOW_CSS = """
.fw{--fw-ondo-bg:#eeedfe;--fw-ondo-bd:#afa9ec;--fw-ondo-ink:#3c3489;--fw-ext-bg:#e1f5ee;--fw-ext-bd:#9fd9c3;--fw-ext-ink:#085041;
  --fw-inv-bg:#fafaf8;--fw-inv-bd:#dcdcd6;--fw-inv-ink:#1f2329;--fw-none-bd:#c9ced6;--fw-dash:#7f77dd;--fw-stage-bd:#d8dce2;--fw-mut:#5a6370;--fw-ar:#8a929c;
  --fw-th:#eef2f7;--fw-bg:transparent;font-size:13.5px;line-height:1.5;margin:8px 0 6px;color:inherit}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .fw{--fw-ondo-bg:#2a2650;--fw-ondo-bd:#6f67c9;--fw-ondo-ink:#d6d1ff;--fw-ext-bg:#123a30;--fw-ext-bd:#2f7d65;--fw-ext-ink:#a5e6cf;
  --fw-inv-bg:#1e232b;--fw-inv-bd:#3a414c;--fw-inv-ink:#e4e9f0;--fw-none-bd:#4a525c;--fw-dash:#9d96f0;--fw-stage-bd:#38404b;--fw-mut:#a0abba;--fw-ar:#8a94a3;--fw-th:#1b212b}}
:root[data-theme="dark"] .fw{--fw-ondo-bg:#2a2650;--fw-ondo-bd:#6f67c9;--fw-ondo-ink:#d6d1ff;--fw-ext-bg:#123a30;--fw-ext-bd:#2f7d65;--fw-ext-ink:#a5e6cf;
  --fw-inv-bg:#1e232b;--fw-inv-bd:#3a414c;--fw-inv-ink:#e4e9f0;--fw-none-bd:#4a525c;--fw-dash:#9d96f0;--fw-stage-bd:#38404b;--fw-mut:#a0abba;--fw-ar:#8a94a3;--fw-th:#1b212b}
.fw-title{font-weight:700;margin:0 0 4px}
.fw ul.fw-lead{margin:0 0 8px;padding-left:18px}
.fw-stage{border:1px dashed var(--fw-stage-bd);border-radius:12px;padding:10px 12px;margin:8px 0}
.fw-h{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap}
.fw-n{font-weight:700}
.fw-badge{font-size:12px;padding:2px 12px;border-radius:999px;white-space:nowrap}
.fw-b-zero{border:1px dashed var(--fw-none-bd);color:var(--fw-mut)}
.fw-b-earn{background:var(--fw-ondo-bg);border:1px solid var(--fw-ondo-bd);color:var(--fw-ondo-ink)}
.fw-row{display:flex;align-items:stretch;gap:6px}
.fw-bx{flex:1;min-width:0;border-radius:10px;padding:8px 6px;text-align:center;display:flex;flex-direction:column;justify-content:center;overflow-wrap:anywhere}
.fw-bx b{font-size:14px;font-weight:600}
.fw-bx span{font-size:12px}
.fw-ar{display:flex;align-items:center;justify-content:center;color:var(--fw-ar);font-size:18px;width:20px;flex:none}
.fw-k-inv{background:var(--fw-inv-bg);border:1px solid var(--fw-inv-bd);color:var(--fw-inv-ink)}
.fw-k-ondo{background:var(--fw-ondo-bg);border:1px solid var(--fw-ondo-bd);color:var(--fw-ondo-ink)}
.fw-k-ext{background:var(--fw-ext-bg);border:1px solid var(--fw-ext-bd);color:var(--fw-ext-ink)}
.fw-k-none{background:transparent;border:1px dashed var(--fw-none-bd);color:var(--fw-mut)}
.fw-k-ondo_dash{background:var(--fw-ondo-bg);border:1px dashed var(--fw-dash);color:var(--fw-ondo-ink)}
.fw-note{font-size:12px;color:var(--fw-mut);margin-top:6px}
.fw-foot{font-size:12.5px;color:var(--fw-mut);margin-top:6px;display:grid;gap:2px}
.fw-legend{margin-top:6px;color:var(--fw-mut);font-size:12px}
.fw-lg{display:inline-block;width:11px;height:11px;border-radius:3px;margin:0 4px 0 10px;vertical-align:-1px}
.fw-lg:first-child{margin-left:0}
.fw-tw{overflow-x:auto}
.fw-tb{border-collapse:collapse;width:100%;margin:8px 0;font-size:13px}
.fw-tb th{background:var(--fw-th);text-align:left;padding:6px 8px;border-bottom:1px solid var(--fw-stage-bd);white-space:nowrap}
.fw-tb td{padding:6px 8px;border-bottom:1px dashed var(--fw-stage-bd);vertical-align:top}
.fw-rich .fw-bx{text-align:left;justify-content:flex-start;padding:10px 12px;border-width:1.5px}
.fw-rich .fw-bx b{font-size:15px;font-weight:700;margin-bottom:4px}
.fw-rich .fw-bx span{font-size:13px;line-height:1.55}
.fw-rich .fw-k-inv span,.fw-rich .fw-k-none span{color:var(--fw-mut)}
.fw-sum{background:var(--fw-th);border-radius:8px;padding:9px 12px;font-weight:600;margin-top:8px;font-size:13.5px}
.fw-headbox,.fw-footbox{border:1.5px solid var(--fw-ondo-bd);border-radius:12px;padding:10px 14px;font-weight:600;margin:8px 0;font-size:14px}
.fw-legend2{margin-top:6px;color:var(--fw-mut);font-size:12px}
@media (max-width:640px){.fw-row{flex-direction:column}.fw-ar{width:auto;height:18px;transform:rotate(90deg)}
  .fw-tb thead{display:none}.fw-tb,.fw-tb tbody,.fw-tb tr,.fw-tb td{display:block;width:100%}
  .fw-tb tr{border:1px dashed var(--fw-stage-bd);border-radius:8px;margin-bottom:6px;padding:4px 0}
  .fw-tb td{display:grid;grid-template-columns:7em minmax(0,1fr);gap:6px;border:0;padding:3px 8px}
  .fw-tb td::before{content:attr(data-l);color:var(--fw-mut);font-size:12px}}
"""

ARROW = {"r": "→", "l": "←", "": ""}
LEGEND = ('<div class="fw-legend"><i class="fw-lg fw-k-ondo"></i>Ondo 그룹 법인과 Ondo 몫 <i class="fw-lg fw-k-ext"></i>외부 회사 '
          '<i class="fw-lg fw-k-inv"></i>투자자 <i class="fw-lg fw-k-none"></i>점선 = 0이거나 공시 없음</div>')


def E(s):
    return html.escape(str(s or ""), quote=True)


def flow_html(f, title=False):
    """flows의 항목 하나(stages가 있는 그림 또는 table이 있는 표)를 HTML로."""
    rich = bool(f.get("rich"))
    h = [f'<div class="fw{" fw-rich" if rich else ""}">']
    if title and f.get("title"):
        h.append(f'<div class="fw-title">{E(f["title"])}</div>')
    if f.get("head"):
        h.append(f'<div class="fw-headbox">{E(f["head"])}</div>')
    if f.get("lead"):
        h.append('<ul class="fw-lead">' + "".join(f"<li>{E(x)}</li>" for x in f["lead"]) + "</ul>")
    for st in f.get("stages") or []:
        badge = st.get("badge") or ["", ""]
        h.append(f'<div class="fw-stage"><div class="fw-h"><span class="fw-n">{E(st.get("name"))}</span>'
                 + (f'<span class="fw-badge fw-b-{E(badge[1])}">{E(badge[0])}</span>' if badge and badge[0] else "") + "</div>")
        h.append('<div class="fw-row">')
        boxes, arrows = st.get("boxes") or [], st.get("arrows") or []
        for i, bx in enumerate(boxes):
            if i:
                a = ARROW.get(arrows[i - 1] if i - 1 < len(arrows) else "", "")
                h.append(f'<div class="fw-ar" aria-hidden="true">{a}</div>')
            name, sub, kind = (list(bx) + ["", "", "inv"])[:3]
            h.append(f'<div class="fw-bx fw-k-{E(kind)}"><b>{E(name)}</b><span>{E(sub)}</span></div>')
        h.append("</div>")
        if st.get("note"):
            h.append(f'<div class="fw-note">{E(st["note"])}</div>')
        if st.get("sum"):
            h.append(f'<div class="fw-sum">{E(st["sum"])}</div>')
        h.append("</div>")
    tb = f.get("table")
    if tb:
        head = tb.get("head") or []
        h.append('<div class="fw-tw"><table class="fw-tb"><thead><tr>' + "".join(f"<th>{E(c)}</th>" for c in head) + "</tr></thead><tbody>")
        for r in tb.get("rows") or []:
            h.append("<tr>" + "".join(f'<td data-l="{E(head[i] if i < len(head) else "")}">{E(c)}</td>' for i, c in enumerate(r)) + "</tr>")
        h.append("</tbody></table></div>")
    if f.get("footbox"):
        h.append(f'<div class="fw-footbox">{E(f["footbox"])}</div>')
    foot = f.get("foot") or []
    leg = f'<div class="fw-legend2">{E(f["legend"])}</div>' if f.get("legend") else (LEGEND if f.get("stages") else "")
    h.append('<div class="fw-foot">' + "".join(f"<div>{E(x)}</div>" for x in foot) + leg + "</div>")
    h.append("</div>")
    return "".join(h)


def card_path(slug="ondo"):
    """회사 개요 카드 JSON 경로. Ondo는 패키지 사본, 다른 회사는 kb/<slug>_overview/<slug>_overview.json."""
    return JSON_PATH if slug == "ondo" else ROOT / f"kb/{slug}_overview/{slug}_overview.json"


def load(slug="ondo"):
    """카드 JSON이 없으면 None."""
    path = card_path(slug)
    if not path.exists():
        return None
    d = json.loads(path.read_text(encoding="utf-8"))
    if slug != "ondo":
        return d
    v2 = ROOT / "kb/flows/ondo_flows_v2.json"
    if v2.exists():
        over = json.loads(v2.read_text(encoding="utf-8"))
        for k, v in over.items():
            if not k.startswith("_") and isinstance(v, dict):
                d.setdefault("flows", {})[k] = v
    return d
