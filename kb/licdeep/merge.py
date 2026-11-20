"""인가 딥다이브 합치기: 회사별 산출물을 평행 연표, 발언 모음, 가설 표, 빈칸 목록으로 묶음.

사용법: python3 -I kb/licdeep/merge.py
읽는 것: kb/licdeep/{external,coinbase,kraken,robinhood,binance}_timeline.csv, <slug>_quotes.md, <slug>_hypo.md, <slug>.md, external.md
쓰는 것: kb/licdeep/00_평행연표.md, 00_발언모음.md, 00_가설표.md, 00_빈칸목록.md
"""
import csv, os, re, sys
from collections import defaultdict

D = os.path.dirname(os.path.abspath(__file__))
COS = [('coinbase', 'Coinbase'), ('kraken', 'Kraken'), ('robinhood', 'Robinhood'), ('binance', 'Binance')]


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8-sig', newline='') as f:
        r = list(csv.reader(f))
    if not r:
        return []
    head = [h.strip() for h in r[0]]
    out = []
    for x in r[1:]:
        if not any(c.strip() for c in x):
            continue
        out.append(dict(zip(head, x + [''] * (len(head) - len(x)))))
    return out


def quarter(d, q):
    q = (q or '').strip()
    if re.match(r'^\d{4}-Q[1-4]$', q):
        return q
    m = re.match(r'^(\d{4})(?:-(\d{1,2}))?', (d or '').strip())
    if not m:
        return ''
    y, mo = m.group(1), m.group(2)
    if not mo:
        return y + '-Q?'
    return '%s-Q%d' % (y, (int(mo) - 1) // 3 + 1)


def cell(items):
    items = sorted(items, key=lambda t: t[0])
    out = []
    for d, kind, one, link in items:
        s = '%s %s%s' % (d, ('[' + kind + '] ') if kind else '', one.replace('|', '/').replace('\n', ' '))
        if link:
            s += ' ([출처](%s))' % link.split()[0]
        out.append(s)
    return '<br>'.join(out)


def timeline():
    grid = defaultdict(lambda: defaultdict(list))
    cols = [('external', '바깥 사건')] + COS
    for slug, _ in cols:
        for r in rows(os.path.join(D, '%s_timeline.csv' % slug)):
            d = r.get('날짜', '')
            q = quarter(d, r.get('분기', ''))
            if not q:
                continue
            kind = r.get('구분') or r.get('분류') or ''
            grid[q][slug].append((d, kind, r.get('한 줄', ''), r.get('출처 링크', '') or r.get('링크', '')))
    qs = sorted(grid)
    lines = ['# 평행 연표 (분기, 2012~2026)', '',
             '행은 분기, 칸마다 날짜와 한 줄. [ ] 안은 구분(바깥 사건은 분류). 회사 칸은 각 회사 담당의 <slug>_timeline.csv, 바깥 칸은 external_timeline.csv에서 옴', '',
             '| 분기 | 바깥 사건 | Coinbase | Kraken | Robinhood | Binance |', '|---|---|---|---|---|---|']
    for q in qs:
        lines.append('| %s | %s |' % (q, ' | '.join(cell(grid[q][s]) for s, _ in cols)))
    open(os.path.join(D, '00_평행연표.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return len(qs)


def section_after(text, title_re):
    m = re.search(title_re, text, re.M)
    if not m:
        return ''
    rest = text[m.end():]
    n = re.search(r'^#{1,2} ', rest, re.M)
    return rest[:n.start()] if n else rest


def gather(suffix, out_name, title, intro):
    parts = ['# ' + title, '', intro, '']
    for slug, name in COS:
        p = os.path.join(D, '%s%s.md' % (slug, suffix))
        if not os.path.exists(p):
            parts += ['## ' + name, '', '(아직 없음)', '']
            continue
        body = open(p, encoding='utf-8').read().strip()
        body = re.sub(r'^# .*\n', '', body, count=1)
        body = re.sub(r'^(#{1,5}) ', lambda m: '#' + m.group(1) + ' ', body, flags=re.M)
        parts += ['## ' + name, '', body, '']
    open(os.path.join(D, out_name), 'w', encoding='utf-8').write('\n'.join(parts) + '\n')


def blanks():
    parts = ['# 빈칸 목록 (회사별 카드와 바깥 연표에서 모음)', '']
    for slug, name in COS + [('external', '바깥 요인')]:
        p = os.path.join(D, '%s.md' % slug)
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8').read()
        s = section_after(t, r'^#{1,3} .*빈칸.*$')
        parts += ['## ' + name, '', s.strip() or '(빈칸 절 없음)', '']
    open(os.path.join(D, '00_빈칸목록.md'), 'w', encoding='utf-8').write('\n'.join(parts) + '\n')


if __name__ == '__main__':
    n = timeline()
    gather('_quotes', '00_발언모음.md', '발언 모음 (건별, 전략별)', '발언은 영문 원문 그대로, 아래 한국어 번역. 회사별 <slug>_quotes.md를 모은 것')
    gather('_hypo', '00_가설표.md', '가설별 받치는 사실과 반대 사실', '가설 1 인가 회사는 주인을 바꿔 돈다, 2 제휴는 인수의 예고편, 3 규제가 열리는 순서가 인수 순서, 4 출신이 사는 것을 정함, 5 돈의 형태가 인수 방식을 정함. 결론 문장 없음')
    blanks()
    bad = []
    for f in os.listdir(D):
        if f.endswith('.md') or f.endswith('.csv'):
            t = open(os.path.join(D, f), encoding='utf-8', errors='ignore').read()
            if '·' in t or '—' in t:
                bad.append(f)
    print('분기 행', n, '| 금지 문자 있는 파일:', bad or '없음')
