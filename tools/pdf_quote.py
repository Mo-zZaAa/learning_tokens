"""PDF 한 쪽에서 인용 문장 부분만 잘라 PNG로 저장(다시 웹 캡처하지 않음).
사용: python3 -I tools/pdf_quote.py <pdf> <쪽(PDF 뷰어 기준)> "<인용 첫 몇 단어>" "<인용 끝 몇 단어>" <out.png>
"""
import re, subprocess, sys, tempfile, os, html
from PIL import Image
pdf, page, start, end, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
tmp = tempfile.mkdtemp()
subprocess.run(['pdftotext', '-f', str(page), '-l', str(page), '-bbox', pdf, f'{tmp}/b.html'], check=True)
s = open(f'{tmp}/b.html', encoding='utf-8').read()
pw, ph = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', s).groups())
words = [(float(a), float(b), float(c), float(d), html.unescape(w)) for a, b, c, d, w in
         re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', s)]
norm = lambda t: re.sub(r'[^a-z0-9가-힣]', '', t.lower())
W = [norm(w[4]) for w in words]
def find(phrase, after=0):
    toks = [norm(t) for t in phrase.split() if norm(t)]
    for i in range(after, len(W) - len(toks) + 1):
        if all(W[i + k].startswith(toks[k]) or toks[k].startswith(W[i + k]) for k in range(len(toks)) if W[i+k]):
            return i, i + len(toks) - 1
    return None
a = find(start)
if not a: sys.exit(f'시작 문구 못 찾음: {start}')
b = find(end, a[0])
if not b: sys.exit(f'끝 문구 못 찾음: {end}')
sel = words[a[0]:b[1] + 1]
y0 = min(w[1] for w in sel) - 6; y1 = max(w[3] for w in sel) + 6
# 같은 줄 전체 폭을 쓴다
line_words = [w for w in words if w[3] > y0 and w[1] < y1]
x0 = min(w[0] for w in line_words) - 8; x1 = max(w[2] for w in line_words) + 8
subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', '150', '-png', pdf, f'{tmp}/p'], check=True)
img = Image.open([f'{tmp}/{f}' for f in os.listdir(tmp) if f.endswith('.png')][0])
sx, sy = img.width / pw, img.height / ph
crop = img.crop((max(0, int(x0 * sx)), max(0, int(y0 * sy)), min(img.width, int(x1 * sx)), min(img.height, int(y1 * sy))))
if crop.width > 1200:
    crop = crop.resize((1200, round(crop.height * 1200 / crop.width)))
os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
crop.save(out)
print(out, crop.size)
