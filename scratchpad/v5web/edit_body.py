"""raw 본문 우선 화면으로 바꾸는 일회성 편집(web/v5/build.py, web/v5/template.html)."""
import re

ROOT = '/home/user/learning_tokens/web/v5/'

p = ROOT + 'build.py'
s = open(p, encoding='utf-8').read()
a = '''        out.append({"k": "l", "id": ids.make(f"{slug}-r-old-{sec}-{h8(t)}"), "d": d, "m": m.group(2) if m else "", "t": t})'''
b = '''        fs = list(dict.fromkeys(re.findall(r"F-\\d{4}", t)))  # 줄에 붙은 근거(줄 안 중복은 한 번)
        out.append({"k": "l", "id": ids.make(f"{slug}-r-old-{sec}-{h8(t)}"), "d": d, "m": m.group(2) if m else "", "t": t, "f": fs})'''
if a in s:
    s = s.replace(a, b)
s = s.replace("6) 빈칸과 정정(kb/gaps.csv, kb/gaps_add/<slug>.csv, kb/corrections.csv) 7) 지난 본문(companies/<회사>_vN.md)",
              "6) 빈칸과 정정(kb/gaps.csv, kb/gaps_add/<slug>.csv, kb/corrections.csv)\n"
              "       화면 순서: 본문(companies/<회사>_vN.md, 줄마다 근거의 원문, 뜻, 출처를 하위 줄로) 먼저, 1)~6)은 아래 \"만든 표와 카드(참고)\"에 접어 둠", 1)
open(p, 'w', encoding='utf-8').write(s)

p = ROOT + 'template.html'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


rep(".oldsec{padding:4px 0 8px;border-bottom:1px solid var(--line)}", """.body{display:grid;gap:0}
.body .bh{font-size:17px;margin:18px 0 6px;padding-top:12px;border-top:1px solid var(--line)}
.body .bh:first-child{border-top:0;margin-top:4px;padding-top:0}
.bl{min-width:0}
.bl.d1{margin-left:20px}.bl.d2{margin-left:40px}.bl.d3{margin-left:60px}
.bl>.ol{font-size:15px}
.bl.b0>.ol{font-weight:600;margin-top:8px}
.fsubs{margin:2px 0 8px 18px;border-left:2px solid var(--line);padding-left:10px;display:grid;gap:6px}
.raw.nosrc .fsubs{display:none}
.fsub{font-size:13px;line-height:1.55;padding-block:3px;overflow-wrap:anywhere}
.fsub .lab{display:inline-block;min-width:2.6em;color:var(--faint);font-size:12px}
.fsub .fq{color:var(--ink)}
.fsub .fm{color:var(--muted)}
.fsub .fs{color:var(--faint);font-size:12px}
.fsub .fs a{font-size:12px}
.fsub .ref{font-size:11px}
.more{border:0;background:transparent;color:var(--accent);font-size:12px;padding:0 4px;text-decoration:underline}
.bodytools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:13px;color:var(--muted)}
.bodytools button{border:1px solid var(--line);background:var(--panel);border-radius:7px;padding:3px 10px;font-size:13px}
.oldsec{padding:4px 0 8px;border-bottom:1px solid var(--line)}""")

rep("function rawParts(C){", r"""const FIDX = {}, SIDX = {};
function factOf(co, f){ if (!FIDX[co]){ FIDX[co] = new Map(D.C[co].facts.map(r => [r[0], r])); SIDX[co] = new Map(D.C[co].srcs.map(r => [r[0], r])); } return FIDX[co].get(f); }
function srcOf(co, sid){ factOf(co, ''); return SIDX[co].get(sid); }
function longText(t){ t = String(t || ''); if (t.length <= 400) return esc(t); return `${esc(t.slice(0, 400))}<span class="q2" hidden>${esc(t.slice(400))}</span><button type="button" class="more" data-more>더 보기</button>`; }
const cleanBody = t => String(t).replace(/\{[a-z]{2,4}-\d{3,5}\}/g, '').replace(/\[(?:F-\d{4}[,;\s]*)+\]/g, '').replace(/\s{2,}/g, ' ').trim();
function fsubHTML(S, lid, f){
  const r = factOf(S, f), id = `${lid}-${f}`;
  if (!r) return `<div class="ln fsub" id="${id}"><span class="lab">근거</span> ${esc(f)}: 사실 DB에 없음${MB}</div>`;
  const g = k => r[FC[k]] || '';
  const srcs = g('source_id').split(/[;,\s]+/).map(x => srcOf(S, x)).filter(Boolean);
  const src = srcs.map(x => `${esc(x[1])}${x[2] ? ', ' + esc(x[2]) : ''}${x[3] ? ', ' + esc(x[3]) : ''}${x[4] ? ` <a href="${esc(x[4])}" target="_blank" rel="noopener">열기</a>` : ''}`).join(' / ')
    || (g('링크') ? `<a href="${esc(g('링크'))}" target="_blank" rel="noopener">${esc(shortUrl(g('링크')))}</a>` : '출처 기록 없음');
  return `<div class="ln fsub" id="${id}">`
    + (g('원문 근거 문장') ? `<div class="fq"><span class="lab">원문</span> "${longText(g('원문 근거 문장'))}"</div>` : '')
    + (g('무엇을') ? `<div class="fm"><span class="lab">뜻</span> ${inl(g('무엇을'), S)}</div>` : '')
    + `<div class="fs"><span class="lab">출처</span> ${src}${g('검증 상태') ? ` <span class="vs ${VS(g('검증 상태'))}">${esc(g('검증 상태'))}</span>` : ''} <a class="ref" href="#${S}-r-f-${f}" data-go="${S}-r-f-${f}">${f}</a></div>${MB}</div>`;
}
function bodyHTML(S, O){
  let h = '', sec = '';
  for (const l of O.lines){
    if (l.k === 'h'){ sec = l.t; h += `<h3 class="ln bh" id="${l.id}"><span class="tx">${esc(l.t)}</span>${MB}</h3>`; continue; }
    const subs = (l.f || []).map(f => fsubHTML(S, l.id, f)).join('');
    h += `<div class="bl gblk d${Math.min(l.d, 3)}${l.m === '●' ? ' b0' : ''}" data-sec="본문: ${esc(sec)}"><div class="ln ol" id="${l.id}"><span class="om">${esc(l.m)}</span><span class="tx">${inl(cleanBody(l.t), S)}</span>${MB}</div>${subs ? `<div class="fsubs">${subs}</div>` : ''}</div>`;
  }
  return h;
}
function rawParts(C){""")

i = s.index("  // 7) 지난 본문")
j = s.index("  return P;\n}\nfunction renderRaw(C){")
s = s[:i] + s[j:]

i = s.index("  const P = rawParts(C);\n  let h = `<article class=\"raw\">")
j = s.index("function foot(){")
new_render = '''  const P = rawParts(C);
  const nsub = C.old ? C.old.lines.reduce((n, l) => n + (l.f || []).length, 0) : 0;
  let h = `<article class="raw"><header class="pagehead"><div class="eyebrow">raw</div><h1>${esc(C.name)}</h1><div class="meta"><span>본문을 줄마다 근거 원문과 함께 둠. 만든 표와 카드는 아래에 접어 둠</span><span>만든 시각 ${esc(D.built)}</span></div></header>`;
  h += `<nav class="toc" aria-label="raw 칸"><a href="#${S}-r-sec-body" data-go="${S}-r-sec-body">본문 <span>${C.old ? C.old.lines.length : 0}</span></a>${P.map(p => `<a href="#${S}-r-sec-${p.k}" data-go="${S}-r-sec-${p.k}">${esc(p.label)} <span>${p.n}</span></a>`).join('')}</nav>`;
  h += `<details class="rsec" id="${S}-r-sec-body" data-sec="본문" open><summary><h2>본문</h2><span class="cnt">${C.old ? C.old.lines.length + '줄, 근거 ' + nsub : 0}</span><span class="srcf">${esc(C.old ? C.old.path : 'companies/' + C.name + '_v4.md')}, db/facts.csv, db/sources.csv</span></summary><div class="rbody">`;
  h += C.old ? `<div class="bodytools"><button type="button" data-act="togglesrc">원문 모두 접기</button><span>줄 아래 회색 줄: 근거마다 원문(영어 그대로), 뜻, 출처</span></div><div class="body">${bodyHTML(S, C.old)}</div>` : ready('본문', `companies/${C.name}_v4.md`);
  h += `</div></details>`;
  h += `<details class="rsec" id="${S}-r-sec-ref" data-sec="만든 표와 카드(참고)"><summary><h2>만든 표와 카드(참고)</h2><span class="cnt">${P.length}칸</span><span class="srcf">kb/, db/</span></summary><div class="rbody">`;
  for (const p of P) h += `<details class="rsec" id="${S}-r-sec-${p.k}" data-sec="${esc(p.label.replace(/^\\d+\\.\\s*/, ''))}"><summary><h2>${esc(p.label)}</h2><span class="cnt">${p.n}</span><span class="srcf">${p.files.map(esc).join(', ')}</span></summary><div class="rbody">${p.h}</div></details>`;
  return h + `</div></details>` + foot() + '</article>';
}
'''
s = s[:i] + new_render + s[j:]

rep("    if (a === 'openall') $$('details.sec', MAIN).forEach(d => d.open = true);",
    """    if (a === 'togglesrc'){ const r = $('.raw', MAIN); if (r){ const off = r.classList.toggle('nosrc'); act.textContent = off ? '원문 모두 펼치기' : '원문 모두 접기'; } }
    if (a === 'openall') $$('details.sec', MAIN).forEach(d => d.open = true);""")
rep("  const mb = t.closest('[data-mb]'); if (mb){ openMemo(ctxFrom(mb)); return; }",
    """  const mb = t.closest('[data-mb]'); if (mb){ openMemo(ctxFrom(mb)); return; }
  const mo = t.closest('[data-more]'); if (mo){ const q2 = mo.previousElementSibling; if (q2){ q2.hidden = !q2.hidden; mo.textContent = q2.hidden ? '더 보기' : '줄이기'; } return; }""")
rep("    if (C.old) C.old.lines.forEach(l => add('r', '지난 본문', l.id, l.t.replace(/\\{[a-z]{2,4}-\\d{3,5}\\}/g, '')));",
    """    if (C.old){ let sec = ''; C.old.lines.forEach(l => {
      if (l.k === 'h'){ sec = l.t; add('r', '본문', l.id, l.t); return; }
      add('r', '본문: ' + sec, l.id, cleanBody(l.t));
      (l.f || []).forEach(f => { const r = factOf(S, f); if (r) add('r', '본문 원문: ' + sec, `${l.id}-${f}`, [r[FC['원문 근거 문장']], r[FC['무엇을']], f].join(' ')); });
    }); }""")
rep("  openUp(el); glossIn(MAIN); clearHits();",
    "  openUp(el); glossIn(MAIN); clearHits();\n"
    "  const rr = el.closest('.raw.nosrc'); if (rr && el.closest('.fsubs')) rr.classList.toggle('nosrc', false);\n"
    "  $$('.q2[hidden]', el).forEach(q => { q.hidden = false; const b = q.nextElementSibling; if (b) b.textContent = '줄이기'; });")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
