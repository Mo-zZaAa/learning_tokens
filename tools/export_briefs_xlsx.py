"""브리핑 6곳(스토리라인, 1~3층), 승인된 축, 전략 틀 비교, 캡처를 엑셀 한 파일로.
사용: python3 tools/export_briefs_xlsx.py  →  export/KDX_해외사례_브리핑.xlsx
캡처 배치: 전략 틀 캡처는 각 회사 스토리라인 3절 바로 아래, 그 밖의 근거 캡처는 그 사실 번호를 인용한 줄 바로 아래.
인용되지 않은 근거 캡처는 회사 시트 끝 "참고 캡처"에. 사진 옆 칸에 무엇을 보여주는지와 해석."""
import csv, glob, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.drawing.image import Image as XLImage
from PIL import Image as PILImage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from capture_notes import NOTES

COS = ['Kraken', 'Coinbase', 'Robinhood', 'Binance', 'Dinari', 'Ondo']
CO_KEYS = {'Kraken': ('Kraken',), 'Coinbase': ('Coinbase',), 'Robinhood': ('Robinhood',), 'Binance': ('Binance',),
           'Dinari': ('Dinari',), 'Ondo': ('Ondo',)}
ATS = [('Blue Ocean', 'Blue_Ocean', 'BlueOcean'), ('Bruce', 'Bruce', 'Bruce'), ('MOON', 'MOON', 'MOON')]

F = 'Malgun Gothic'
f_base = Font(name=F, size=10)
f_bold = Font(name=F, size=10, bold=True)
f_h1 = Font(name=F, size=14, bold=True, color='FFFFFF')
f_h2 = Font(name=F, size=12, bold=True, color='1F3864')
f_h3 = Font(name=F, size=11, bold=True, color='1F3864')
f_link = Font(name=F, size=9, color='1F5FBF', underline='single')
f_small = Font(name=F, size=9, color='5D6878')
fill_h1 = PatternFill('solid', fgColor='22509E')
fill_h2 = PatternFill('solid', fgColor='DCE6F5')
fill_h3 = PatternFill('solid', fgColor='EEF3FA')
fill_hl = PatternFill('solid', fgColor='FFF6C9')
fill_img = PatternFill('solid', fgColor='F7F8FB')
wrap = Alignment(wrap_text=True, vertical='top')
thin = Side(style='thin', color='DDE2E9')
box = Border(top=thin, bottom=thin, left=thin, right=thin)

# ---------- 사실, 출처, 캡처 지도 ----------
FACTS = {r['fact_id']: r for r in csv.DictReader(open('db/facts.csv', encoding='utf-8-sig'))}
FMAP = {}
for r in csv.DictReader(open('db/_fact_id_map.csv', encoding='utf-8-sig')):
    FMAP[(r['agent'], r['original_id'])] = r['fact_id']
CAP_OF_FACT, CAP_TITLE = {}, {}
for sp in glob.glob('work/*/sources.csv'):
    d = os.path.basename(os.path.dirname(sp))
    fp = os.path.join(os.path.dirname(sp), 'facts.csv')
    if not os.path.exists(fp):
        continue
    src = {}
    for r in csv.DictReader(open(sp, encoding='utf-8-sig')):
        caps = [c.strip() for c in re.split(r'[;,]', r.get('캡처 파일') or '') if c.strip().endswith('.png')]
        caps = [c if c.startswith('captures/') else 'captures/' + c for c in caps]
        caps = [c for c in caps if os.path.exists(c)]
        if caps:
            src[r['source_id']] = (caps, r.get('제목') or '')
    for r in csv.DictReader(open(fp, encoding='utf-8-sig')):
        if r.get('source_id') in src:
            fid = FMAP.get((d, r['fact_id']))
            if fid:
                caps, title = src[r['source_id']]
                for c in caps:
                    CAP_OF_FACT.setdefault(fid, [])
                    if c not in CAP_OF_FACT[fid]:
                        CAP_OF_FACT[fid].append(c)
                    CAP_TITLE.setdefault(c, title)

PILLAR_DESC = {}
for p in glob.glob('work/PILLARS/*.md'):
    for line in open(p, encoding='utf-8'):
        m = re.match(r'- ([A-Za-z0-9_\-., ]+\.png)\s*:\s*(.+)', line.strip())
        if m:
            for name in [x.strip() for x in m.group(1).split(',')]:
                PILLAR_DESC[name[:-4]] = m.group(2).strip()


def clean(text):
    U = r'(https?://(?:[^()\s]|\([^()\s]*\))+)'  # 위키백과처럼 주소 안 괄호 허용
    links = re.findall(r'\[((?:F|CASE)-\d{3,4})\]\(' + U + r'\)', text)
    ids = re.findall(r'\b((?:F|CASE)-\d{3,4})\b', text)
    t = re.sub(r'\[((?:F|CASE)-\d{3,4})\]\(' + U + r'\)', r'\1', text)
    t = re.sub(r'\[((?:F|CASE)-\d{3,4})\]', r'\1', t)
    t = re.sub(r'\s*(?:(?:F|CASE)-\d{3,4}(?:\([^)]*\))?\s*)+$', '', t)  # 줄 끝 근거 번호는 근거 칸으로
    hl = '==' in t or '**' in t
    t = t.replace('**', '').replace('==', '').replace('!!', '')
    t = re.sub(r'\[([^\]]+)\]\(' + U + r'\)', r'\1', t)
    return t.strip(), list(dict.fromkeys(ids)), [u for _, u in links], hl


GAP = re.compile(r'비공개|공개 없음|공개하지 않|미확인|확인하지 못|찾지 못|근거 없|알 수 없')


def degap(s):
    # 결과물에는 공백 표시를 남기지 않음: 그런 구절이 든 문장 조각을 뺀다
    parts = re.split(r'(?<=[.)])\s+|,\s+', s or '')
    keep = [x for x in parts if not GAP.search(x)]
    return ' '.join(keep).strip()


def img_rows(ws, row, path, what, note, col_img='C', col_txt='D'):
    """사진 한 장을 넣고 옆 칸에 설명. 다음 행 번호를 돌려줌."""
    what, note = degap(what), degap(note)
    try:
        with PILImage.open(path) as im:
            w, h = im.size
    except Exception:
        return row
    scale = min(620 / w, 520 / h, 1.0)
    dw, dh = int(w * scale), int(h * scale)
    # 용량을 줄이려고 표시 크기의 1.5배로 줄인 사본을 넣음
    os.makedirs('export/_img', exist_ok=True)
    small = os.path.join('export/_img', os.path.basename(path).rsplit('.', 1)[0] + '.jpg')
    if not os.path.exists(small):
        with PILImage.open(path) as im:
            im = im.convert('RGB')
            tw, th = min(w, int(dw * 1.5)), min(h, int(dh * 1.5))
            im.resize((tw, th), PILImage.LANCZOS).save(small, 'JPEG', quality=82, optimize=True)
    img = XLImage(small)
    img.width, img.height = dw, dh
    ws.add_image(img, f'{col_img}{row}')
    ws.row_dimensions[row].height = max(30, img.height * 0.75 + 6)
    ws[f'B{row}'] = '사진'
    ws[f'B{row}'].font = f_small
    ws[f'B{row}'].alignment = wrap
    ws.merge_cells(f'{col_txt}{row}:E{row}')
    c = ws[f'{col_txt}{row}']
    c.value = f'무엇 : {what}\n\n해석 : {note}\n\n파일 : {path}'
    c.font = f_base
    c.alignment = wrap
    for col in 'ABCDE':
        ws[f'{col}{row}'].fill = fill_img
    return row + 1


def setup(ws, title, sub=''):
    ws.column_dimensions['A'].width = 16
    ws.column_dimensions['B'].width = 5
    ws.column_dimensions['C'].width = 92
    ws.column_dimensions['D'].width = 22
    ws.column_dimensions['E'].width = 46
    ws.merge_cells('A1:E1')
    ws['A1'] = title
    ws['A1'].font = f_h1
    ws['A1'].fill = fill_h1
    ws['A1'].alignment = Alignment(vertical='center')
    ws.row_dimensions[1].height = 26
    if sub:
        ws.merge_cells('A2:E2')
        ws['A2'] = sub
        ws['A2'].font = f_small
        ws['A2'].alignment = wrap
    hdr = ['구분', '단계', '내용', '근거 번호', '원문 링크']
    for i, h in enumerate(hdr):
        c = ws.cell(row=3, column=i + 1, value=h)
        c.font = f_bold
        c.fill = fill_h2
        c.border = box
    ws.freeze_panes = 'A4'
    ws.page_setup.orientation = 'landscape'
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    return 4


def put_line(ws, row, part, level, text, ids, urls, hl=False, font=None, fill=None):
    ws.cell(row=row, column=1, value=part).font = f_small
    ws.cell(row=row, column=2, value=level).font = f_base
    c = ws.cell(row=row, column=3, value=text)
    c.font = font or (f_bold if hl else f_base)
    c.alignment = wrap
    if hl and not fill:
        c.fill = fill_hl
    d = ws.cell(row=row, column=4, value=' '.join(ids))
    d.font = f_small
    d.alignment = wrap
    if urls:
        e = ws.cell(row=row, column=5, value='\n'.join(dict.fromkeys(urls)))
        e.hyperlink = urls[0]
        e.font = f_link
        e.alignment = wrap
    if fill:
        for col in range(1, 6):
            ws.cell(row=row, column=col).fill = fill
    for col in range(1, 6):
        ws.cell(row=row, column=col).border = box
    # 행 높이: 글자 수로 대략
    n = max(1, len(text) // 44 + text.count('\n') + 1, len(dict.fromkeys(urls)) * 2)
    ws.row_dimensions[row].height = min(409, 14 * n + 4)
    return row + 1


def company_sheet(wb, co):
    md = open(f'briefs/{co}.md', encoding='utf-8').read()
    ws = wb.create_sheet(co)
    row = setup(ws, f'{co} 브리핑', '순서: 축과 가설 → 스토리라인(7절) → 1층(키워드) → 2층(받치는 사실) → 3층(꼬리질문 대비). 전략 틀 캡처는 3절 아래, 근거 캡처는 그 사실을 인용한 줄 아래.')
    placed = set()
    part = ''
    pillar_caps = sorted(p for p in glob.glob('captures/pillars/*.png') if os.path.basename(p).startswith(co + '_'))
    in_sec3 = False
    lines = md.split('\n')
    for i, raw in enumerate(lines):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith('# '):
            continue
        if line.startswith('## '):
            if in_sec3:
                row = flush_pillars(ws, row, pillar_caps, placed)
                in_sec3 = False
            part = line[3:].strip()
            row = put_line(ws, row, part, '', part, [], [], font=f_h2, fill=fill_h2)
            continue
        if line.startswith('### '):
            if in_sec3:
                row = flush_pillars(ws, row, pillar_caps, placed)
            in_sec3 = line[4:].strip().startswith('3.')
            row = put_line(ws, row, part, '', line[4:].strip(), [], [], font=f_h3, fill=fill_h3)
            continue
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                continue
            text, ids, urls, hl = clean('  |  '.join(cells))
            row = put_line(ws, row, part, '표', text, ids, urls, hl)
            continue
        m = re.match(r'^(\s*)-\s+(.*)$', line)
        if m:
            depth = len(m.group(1)) // 2
            level = ['•', '-', '·'][min(depth, 2)].replace('·', '--')
            text, ids, urls, hl = clean(m.group(2))
            if depth:
                text = '    ' * depth + text
        else:
            level, (text, ids, urls, hl) = '', clean(line)
        label = text.strip()
        row = put_line(ws, row, part, level, text, ids, urls, hl or label.startswith('축 :'))
        # 근거 캡처: 이 줄이 인용한 사실의 캡처
        for fid in ids:
            for cap in CAP_OF_FACT.get(fid, []):
                if cap in placed or '/pillars/' in cap:
                    continue
                placed.add(cap)
                fact = FACTS.get(fid, {})
                row = img_rows(ws, row, cap, CAP_TITLE.get(cap, os.path.basename(cap)),
                               f'{fid} : ' + (fact.get('무엇을') or '')[:300])
    if in_sec3:
        row = flush_pillars(ws, row, pillar_caps, placed)
    # 인용되지 않은 이 회사 근거 캡처
    rest = []
    for fid, caps in CAP_OF_FACT.items():
        fact = FACTS.get(fid, {})
        if not any((fact.get('회사') or '').startswith(k) for k in CO_KEYS[co]):
            continue
        for cap in caps:
            if cap not in placed and '/pillars/' not in cap:
                rest.append((fid, cap))
    left = [p for p in pillar_caps if p not in placed]
    if rest or left:
        row = put_line(ws, row, '참고 캡처', '', '참고 캡처(본문에서 직접 인용하지 않은 근거 화면)', [], [], font=f_h2, fill=fill_h2)
        for p in left:
            placed.add(p)
            k = os.path.basename(p)[:-4]
            row = img_rows(ws, row, p, PILLAR_DESC.get(k, k), NOTES.get(k, ''))
        for fid, cap in rest:
            if cap in placed:
                continue
            placed.add(cap)
            row = img_rows(ws, row, cap, CAP_TITLE.get(cap, os.path.basename(cap)),
                           f'{fid} : ' + (FACTS.get(fid, {}).get('무엇을') or '')[:300])
    ws.sheet_view.zoomScale = 90
    return ws


def flush_pillars(ws, row, caps, placed):
    todo = [p for p in caps if p not in placed]
    if not todo:
        return row
    row = put_line(ws, row, '전략 틀 캡처', '', '전략 틀 원문 캡처(회사가 공식적으로 내건 기둥, 우선순위, 비전)', [], [], font=f_h3, fill=fill_h3)
    order = sorted(todo, key=lambda p: PILLAR_ORDER.get(os.path.basename(p)[:-4], 99))
    for p in order:
        placed.add(p)
        k = os.path.basename(p)[:-4]
        row = img_rows(ws, row, p, PILLAR_DESC.get(k, k), NOTES.get(k, ''))
    return row


PILLAR_ORDER = {k: i for i, k in enumerate(NOTES.keys())}


def table_sheet(wb, name, title, md_path, start_marker=None, end_marker=None):
    ws = wb.create_sheet(name)
    t = open(md_path, encoding='utf-8').read()
    if start_marker and start_marker in t:
        t = t[t.index(start_marker):]
    if end_marker and end_marker in t:
        t = t[:t.index(end_marker)]
    rows = [l for l in t.split('\n') if l.startswith('|')]
    rows = [[c.strip() for c in l.strip('|').split('|')] for l in rows]
    rows = [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c) for c in r if c)]
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(len(r) for r in rows))
    ws['A1'] = title
    ws['A1'].font = f_h1
    ws['A1'].fill = fill_h1
    for ri, r in enumerate(rows):
        for ci, v in enumerate(r):
            text, ids, urls, hl = clean(v)
            c = ws.cell(row=ri + 3, column=ci + 1, value=text)
            c.font = f_bold if ri == 0 else f_base
            c.alignment = wrap
            c.border = box
            if ri == 0:
                c.fill = fill_h2
        ws.row_dimensions[ri + 3].height = 15 * max(1, max(len(x) for x in r) // 40 + 1) if ri else 18
    widths = [16, 60, 50, 70, 70]
    for i in range(len(rows[0])):
        ws.column_dimensions[chr(65 + i)].width = widths[i] if i < len(widths) else 40
    ws.freeze_panes = 'A4'
    return ws, len(rows) + 3


def main():
    wb = Workbook()
    toc = wb.active
    toc.title = '목차'
    toc.column_dimensions['A'].width = 22
    toc.column_dimensions['B'].width = 110
    toc['A1'] = 'KDX 해외 사례 브리핑 (2026-11-17)'
    toc['A1'].font = Font(name=F, size=16, bold=True, color='1F3864')
    items = [('축과 가설', 'PM이 승인한 회사별 축(덩치를 키운 방식)과 가설 판단'),
             ('전략 틀 비교', '9곳이 공식적으로 내건 기둥, 우선순위, 비전 문장. 처음 나온 시점과 변천')]
    items += [(c, f'{c} 브리핑: 스토리라인 7절, 1~3층, 전략 틀 캡처와 근거 캡처') for c in COS]
    items += [('야간 ATS', 'Blue Ocean, Bruce, MOON의 미션 문장과 캡처')]
    toc['A3'], toc['B3'] = '시트', '내용'
    toc['A3'].font = toc['B3'].font = f_bold
    for i, (a, b) in enumerate(items):
        toc.cell(row=4 + i, column=1, value=a).font = f_bold
        toc.cell(row=4 + i, column=1).hyperlink = f"#'{a}'!A1"
        toc.cell(row=4 + i, column=2, value=b).font = f_base
    r = 6 + len(items)
    notes = ['읽는 법',
             '스토리라인 문장 끝 근거 번호(F-xxxx)는 근거 번호 칸에, 원문 링크는 오른쪽 칸에 있음(첫 링크는 눌러서 열림).',
             '노란 칸은 핵심 결론 구절이 있는 줄.',
             '"해석"으로 시작하는 줄과 사진 옆 해석은 사실이 아니라 근거를 바탕으로 한 판단.',
             '사진은 원문 화면 캡처. 사진 옆 칸에 무엇을 보여주는지, 해석, 파일 경로.']
    for i, n in enumerate(notes):
        c = toc.cell(row=r + i, column=1 if i == 0 else 2, value=n)
        c.font = f_bold if i == 0 else f_base
    table_sheet(wb, '축과 가설', '승인된 축과 가설', 'axes.md', '## 승인된 축', '\n---\n')
    ws, nr = table_sheet(wb, '전략 틀 비교', '9곳 전략 틀 비교', 'briefs/00_전략틀_비교.md', '## 한눈에', '## 읽는 법')
    t = open('briefs/00_전략틀_비교.md', encoding='utf-8').read()
    if '## 읽는 법' in t:
        rb = t[t.index('## 읽는 법'):].split('## 주요 캡처')[0]
        ws.cell(row=nr + 1, column=1, value='읽는 법').font = f_bold
        for i, l in enumerate([x[2:] for x in rb.split('\n') if x.startswith('- ')]):
            c = ws.cell(row=nr + 2 + i, column=2, value=l)
            c.font = f_base
            c.alignment = wrap
            ws.merge_cells(start_row=nr + 2 + i, start_column=2, end_row=nr + 2 + i, end_column=4)
            ws.row_dimensions[nr + 2 + i].height = 32
    for co in COS:
        company_sheet(wb, co)
    ws = wb.create_sheet('야간 ATS')
    row = setup(ws, '야간 ATS 3곳: 전략 틀(미션 문장)과 캡처')
    for name, md, pre in ATS:
        row = put_line(ws, row, name, '', name, [], [], font=f_h2, fill=fill_h2)
        p = f'work/PILLARS/{md}.md'
        if os.path.exists(p):
            body = open(p, encoding='utf-8').read()
            tab = [l for l in body.split('\n') if l.startswith('|')]
            for l in tab:
                cells = [c.strip() for c in l.strip('|').split('|')]
                if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                    continue
                text, ids, urls, hl = clean('  |  '.join(cells))
                text = re.sub(r'(?:확인하지 못함|확인 못 함|공개 없음|미확인|찾지 못함)[^|]*', '', text)
                text = re.sub(r'(?:금액|매출|수치)?\s*비공개,?\s*', '', text)
                urls = urls + re.findall(r'https?://[^\s)]+', text)
                text = re.sub(r'\(?https?://[^\s)]+\)?', '', text).replace('()', '').replace('( ', '(')
                row = put_line(ws, row, name, '표', text, ids, urls)
        for cap in sorted(glob.glob(f'captures/pillars/{pre}_*.png'), key=lambda x: PILLAR_ORDER.get(os.path.basename(x)[:-4], 99)):
            k = os.path.basename(cap)[:-4]
            row = img_rows(ws, row, cap, PILLAR_DESC.get(k, k), NOTES.get(k, ''))
    os.makedirs('export', exist_ok=True)
    out = 'export/KDX_해외사례_브리핑.xlsx'
    wb.save(out)
    n_img = sum(len(s._images) for s in wb.worksheets)
    print(out, '시트', len(wb.sheetnames), '사진', n_img)


if __name__ == '__main__':
    main()
