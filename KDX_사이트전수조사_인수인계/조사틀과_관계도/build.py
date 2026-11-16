# data 폴더의 파일로 index.html(조사 틀과 관계도 페이지)과 정리 문서를 다시 만든다.
#   python build.py            data/frame.json, facts.csv, notes.json, relations.json 을 읽음
# 사실을 더할 때는 facts.csv에 행을, 관계를 더할 때는 relations.json의 N(회사)과 E(관계)에 항목을, 출처는 SRC에 키를 추가한다.
import json, csv, os, html, collections
base = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(base, 'data')
rel = json.load(open(os.path.join(D, 'relations.json'), encoding='utf-8'))
frame = json.load(open(os.path.join(D, 'frame.json'), encoding='utf-8'))
notes = json.load(open(os.path.join(D, 'notes.json'), encoding='utf-8'))
facts = list(csv.DictReader(open(os.path.join(D, 'facts.csv'), encoding='utf-8-sig')))
SRC = rel['SRC']; esc = html.escape
missing = sorted({r['출처키'] for r in facts if r['출처키'] not in SRC} | {e[5] for e in rel['E'] if e[5] not in SRC})
assert not missing, '출처키가 SRC에 없음: ' + ', '.join(missing)

def src(k):
    t, u, g = SRC[k]
    return (f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a>' if u else esc(t)) + f' <span class="grade">[{g}]</span>'

by = collections.defaultdict(list)
for r in facts: by[r['대분류']].append(r)

def section(fr):
    rows = by.get(fr['name'], []); order = [s[0] for s in fr['subs']]
    rows.sort(key=lambda r: (order.index(r['소분류']) if r['소분류'] in order else 99, r['회사']))
    n = notes.get(fr['id'], {'read': [], 'todo': []})
    out = [f'<section class="card sec" id="{fr["id"]}"><h3><span class="no">{fr["id"].upper()}</span>{esc(fr["name"])} <span class="kind">{fr["kind"]}, 관심사 {fr["interest"]}</span></h3>']
    out.append('<p class="note">조사 질문: ' + ' / '.join(esc(s[0]) + (f'({esc(s[1])})' if s[1] else '') for s in fr['subs']) + '</p>')
    if fr['id'] == 'f':
        out.append('<!--GRAPH-->')
    elif rows:
        out.append('<div class="tablewrap"><table><thead><tr><th>항목</th><th>회사</th><th>확인된 사실</th><th>시점</th><th>근거</th></tr></thead><tbody>')
        for r in rows: out.append(f'<tr><td>{esc(r["소분류"])}</td><td><b>{esc(r["회사"])}</b></td><td>{esc(r["사실"])}</td><td class="num">{esc(r["시점"])}</td><td>{src(r["출처키"])}</td></tr>')
        out.append('</tbody></table></div>')
    out.append('<div class="two">')
    if n['read']: out.append('<div><h4>이렇게 읽음(해석)</h4><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in n['read']) + '</ul></div>')
    if n['todo']: out.append('<div><h4>남은 확인</h4><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in n['todo']) + '</ul></div>')
    out.append('</div></section>')
    return '\n'.join(out)

overview = ['<section class="card sec" id="frame"><h3>틀 한눈에</h3><div class="tablewrap"><table><thead><tr><th>대분류</th><th>조사 질문</th><th>내 관심사 번호</th><th>구분</th><th>확인된 사실</th></tr></thead><tbody>']
for fr in frame:
    cnt = len(rel['E']) if fr['id'] == 'f' else len(by.get(fr['name'], []))
    overview.append(f'<tr><td><a href="#{fr["id"]}"><b>{fr["id"].upper()} {esc(fr["name"])}</b></a></td><td>{esc(", ".join(s[0] for s in fr["subs"]))}</td><td class="num">{fr["interest"]}</td><td>{fr["kind"]}</td><td class="num">{cnt}건</td></tr>')
overview.append('</tbody></table></div><p class="note">필수는 회사마다 채우는 칸, 선택은 해당 있을 때만 쓰는 칸, 공통은 회사별이 아니라 한 번만 정리하는 칸. 관심사 번호는 처음 던진 질문 7개의 번호.</p></section>')

tpl = open(os.path.join(base, 'template.html'), encoding='utf-8').read()
graph = tpl[tpl.index('<!--GRAPH-START-->'):tpl.index('<!--GRAPH-END-->')]
body = '\n'.join(overview) + '\n' + '\n'.join(section(fr) for fr in frame)
body = body.replace('<!--GRAPH-->', graph)
nav = ''.join(f'<a href="#{fr["id"]}">{fr["id"].upper()} {esc(fr["name"])}</a>' for fr in frame)
page = tpl[:tpl.index('<!--GRAPH-START-->')] + '<!--BODY-->' + tpl[tpl.index('<!--GRAPH-END-->'):]
page = page.replace('<!--BODY-->', body).replace('<!--NAV-->', '<a href="#frame">틀 한눈에</a>' + nav)
data_js = ''.join(f'const {k}={json.dumps(rel[k], ensure_ascii=False)};\n' for k in ('TYPES', 'LANES', 'SRC', 'N', 'E'))
page = page.replace('/*DATA*/', data_js)
open(os.path.join(base, 'index.html'), 'w', encoding='utf-8').write(page)

# 정리 문서: 조사 틀, 1차 답과 남은 확인, 사실 원장(출처 주소 포함)
out = os.path.join(base, 'out'); os.makedirs(out, exist_ok=True)
md = ['# 해외 사례 조사 틀 개편안', '', '처음 던진 관심사 7개를 겹치지 않는 대분류 8개로 다시 묶었다. A~E는 회사마다 채우고, F와 G는 해당 있을 때만 쓰고, H는 회사별이 아니라 한 번만 정리한다.', '',
      '| 대분류 | 소분류 | 조사 질문 | 관심사 번호 | 구분 |', '|---|---|---|---|---|']
for fr in frame:
    for s in fr['subs']: md.append(f'| {fr["id"].upper()} {fr["name"]} | {s[0]} | {s[1]} | {fr["interest"]} | {fr["kind"]} |')
md += ['', '## 관심사 7개와의 대응', '', '| 번호 | 처음 던진 관심사 | 들어간 곳 |', '|---|---|---|',
       '| 1 | 뿌리가 가상자산인지 토큰화 전문인지, 그에 따른 차이 | A 출신과 진입 |',
       '| 2 | 사업자 간 차별점, 대체거래시스템 해당 여부, 진입 시기 | A 진입 시점, B 상품 구조, C 최종 투자자, D 거래 장소 |',
       '| 3 | 투자자 접점을 가진 곳과 아닌 곳 | D 유통과 접점 |',
       '| 4 | 카카오페이증권과 Dinari 협약 배경 | G 한국 접점 |',
       '| 5 | 명의개서대리인 등록과 증권사 승인을 받은 이유와 시점 | E 인가 |',
       '| 6 | 인가 난이도, 등록된 곳 수, 가상자산의 인가 필요 여부 | E 인가, H 제도와 시장 |',
       '| 7 | 투자, 인수, 제휴 관계 | F 관계 |']
open(os.path.join(out, '10_조사틀_개편안.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')

md = ['# 1차 답과 남은 확인', '', '기준일 2026-11-16. 근거 등급: 공식(회사나 감독기관의 공식 자료), 보도(언론 보도), 리서치팩(프로젝트 리서치팩 11/11 검증분). 해석은 사실과 따로 적었다.', '']
for fr in frame:
    md += [f'## {fr["id"].upper()} {fr["name"]}', '']
    if fr['id'] == 'f':
        md += ['| 유형 | 주는 쪽 | 받는 쪽 | 내용 | 시점 | 근거 |', '|---|---|---|---|---|---|']
        nm = {n[0]: n[1] for n in rel['N']}
        for e in rel['E']: md.append(f'| {rel["TYPES"][e[2]]["k"]} | {nm[e[0]]} | {nm[e[1]]} | {e[3]} | {e[4]} | {SRC[e[5]][0]} [{SRC[e[5]][2]}] |')
    else:
        md += ['| 항목 | 회사 | 확인된 사실 | 시점 | 근거 |', '|---|---|---|---|---|']
        for r in by.get(fr['name'], []): md.append(f'| {r["소분류"]} | {r["회사"]} | {r["사실"]} | {r["시점"]} | {SRC[r["출처키"]][0]} [{SRC[r["출처키"]][2]}] |')
    n = notes.get(fr['id'], {'read': [], 'todo': []})
    if n['read']: md += ['', '해석'] + [f'- {x}' for x in n['read']]
    if n['todo']: md += ['', '남은 확인'] + [f'- {x}' for x in n['todo']]
    md.append('')
open(os.path.join(out, '11_1차답과_남은확인.md'), 'w', encoding='utf-8').write('\n'.join(md))

with open(os.path.join(out, '12_사실원장.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['대분류', '소분류', '회사', '사실', '시점', '출처', '출처 주소', '근거 등급'])
    for r in facts: s = SRC[r['출처키']]; w.writerow([r['대분류'], r['소분류'], r['회사'], r['사실'], r['시점'], s[0], s[1], s[2]])
    nm = {n[0]: n[1] for n in rel['N']}
    for e in rel['E']: s = SRC[e[5]]; w.writerow(['관계', rel['TYPES'][e[2]]['k'], nm[e[0]] + ' > ' + nm[e[1]], e[3], e[4], s[0], s[1], s[2]])
print('index.html', len(page), '사실', len(facts), '관계', len(rel['E']))
