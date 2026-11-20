"""리서치 전체를 zip으로 묶기 (핵심 1개 + 원문 3개)

사용법(저장소 맨 위에서): python3 -I tools/package_zip.py 261120
결과: _packages/ 아래 zip 4개(.gitignore로 저장소에는 올리지 않음)
- KDX_해외사례리서치_핵심_<날짜>.zip: 00_목차.html, 00_먼저읽기.md, 01 납품물 ~ 06 도구
- KDX_해외사례리서치_원문1_출처저장본_<날짜>.zip: sources/, work/*/raw
- KDX_해외사례리서치_원문2_공식사이트수집_<날짜>.zip: KDX_사이트전수조사_인수인계/
- KDX_해외사례리서치_원문3_캡처와사용자자료_<날짜>.zip: captures/, inputs/
번호 폴더 안에는 저장소 경로를 그대로 둠(예: 04_사실DB/db/facts.csv). 그래서 handoff.md의 경로 앞에 번호 폴더만 붙이면 찾을 수 있음
"""
import csv, html, os, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAY = sys.argv[1] if len(sys.argv) > 1 else '261120'
OUT = os.path.join(ROOT, '_packages')
SKIP_DIRS = {'__pycache__', '.git'}
STORED = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.zip', '.docx', '.xlsx', '.pptx', '.pdf', '.mp4'}

# (번호 폴더, 저장소 안 경로들, 설명)
CORE = [
    ('01_납품물', ['deliverables'], '바로 전달할 파일: A4 docx(긴 판, 간결 판), 매출 원인 md, 사용자 글 다듬기, 불렛과 근거, 인가 딥다이브 zip, 백데이터 엑셀'),
    ('01_납품물/예전_납품', ['export'], '2026-11-17 전후 납품(브리핑 엑셀, 최종본 묶음)'),
    ('02_화면', ['web/v5/index.html', 'web/v5/ondo_deep.html', 'web/v5/build.py', 'web/v5/template.html', 'web/v5/ondo_card.py'], '화면(Artifact) 원본. index.html을 브라우저로 열면 대부분 보임(메모, 고치기, 내려받기 기능은 Artifact에서만)'),
    ('03_정리본', ['companies', 'kb'], '회사 본문(companies/*_v4.md가 최신), 카드, 쉬운 해설, 매출 원인, 사건 카드, 구조 표, 인가 딥다이브(kb/licdeep), 제도, 용어'),
    ('04_사실DB', ['db', 'catalog.csv'], '사실 2,773건, 출처 1,474건 등. db/README.md부터. catalog.csv는 자료 목록'),
    ('05_기록과규칙', ['handoff.md', 'handoff_261116.md', 'CLAUDE.md', 'playbook', 'discussion', 'axes.md', 'INSTRUCTIONS.md', 'KDX_해외사례리서치_ClaudeCode_지시문_v4.md', 'KDX_지시문_v4_변경점.md'], '인계 문서, 저장소 규칙, 쓰기 규칙과 리서치 노하우, 화면 메모와 답, 지시문'),
    ('06_도구', ['tools'], '검색(fsearch.py), DB 병합(merge_db.py), 백데이터 엑셀(build_backdata.py), 이 묶음(package_zip.py)'),
]
RAW = [
    ('원문1_출처저장본', ['sources'], True),
    ('원문2_공식사이트수집', ['KDX_사이트전수조사_인수인계'], False),
    ('원문3_캡처와사용자자료', ['captures', 'inputs'], False),
]
ARTIFACTS = [
    ('KDX 해외 사례(본 화면)', 'https://claude.ai/artifact/QnuzMo25ig3Qw9K7ACgFuJ'),
    ('해외 사례 9곳 전체 그림', 'https://claude.ai/artifact/YQd7eFkjTPSBbWa1QZC6oD'),
    ('KDX 미국 6개사 개요', 'https://claude.ai/artifact/AxJGYFzxm3cKFrFkCGbpGX'),
    ('Kraken PM 질의 전량과 리서치 답(261118)', 'https://claude.ai/artifact/LGbbj6AgKBvoJcAs24qY9o'),
    ('주식 토큰 인가 지도', 'https://claude.ai/artifact/BUnC7V4PNMEodsPef3vQAo'),
    ('미국 주식 토큰 조사 틀과 관계도', 'https://claude.ai/artifact/74wczjJKoCALNHbJpA6hra'),
]
KEY = [
    ('01_납품물/deliverables/KDX_백데이터_261120.xlsx', '백데이터 엑셀: 읽는 법, 자료 목록, DB 표 전부, 인가 연표, 화면 메모'),
    ('01_납품물/deliverables/KDX_회사별A4_4개사_261118.docx', '회사별 A4(긴 판) 4개사'),
    ('01_납품물/deliverables/4개사_불렛과근거_261119.md', '4개사 짧은 불렛과 줄별 근거'),
    ('01_납품물/deliverables/매출로본성공원인_4개사_261118.md', '4개사 매출 구성과 원인'),
    ('03_정리본/kb/licdeep/01_틀에맞춘답.md', '인가 획득: 직접 대 인수, 목적, 시점, KSF'),
    ('03_정리본/kb/licdeep/00_평행연표.md', '인가 평행 연표(분기, 바깥 사건과 4개사)'),
    ('02_화면/web/v5/index.html', '화면 원본(브라우저로 열기)'),
    ('04_사실DB/db/README.md', '사실 DB 읽는 법'),
    ('05_기록과규칙/handoff.md', '인계 문서(전체 지도와 쓰는 법)'),
]


def walk(rel, raw_only=False):
    p = os.path.join(ROOT, rel)
    if os.path.isfile(p):
        yield rel
        return
    for dp, dn, fn in os.walk(p):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if f.endswith('.pyc'):
                continue
            yield os.path.relpath(os.path.join(dp, f), ROOT)


def add(z, src_rel, arc):
    ext = os.path.splitext(src_rel)[1].lower()
    z.write(os.path.join(ROOT, src_rel), arc, compress_type=zipfile.ZIP_STORED if ext in STORED else zipfile.ZIP_DEFLATED)


def readme(top, raw_names):
    lines = ['# KDX 해외 사례 리서치 묶음 (%s)' % DAY, '',
             '이 zip은 리서치 전체의 "핵심 묶음"입니다. 원문은 따로 묶은 zip 셋에 있습니다.', '',
             '## 처음 볼 것', '- 00_목차.html: 브라우저로 열면 폴더와 주요 파일을 눌러 열 수 있음',
             '- 01_납품물/deliverables/KDX_백데이터_%s.xlsx: 사람이 바로 보는 백데이터(첫 시트 "읽는 법")' % DAY,
             '- 05_기록과규칙/handoff.md: 전체 지도, 상황별 쓰는 법, 갱신하는 법', '',
             '## 폴더', '| 폴더 | 내용 |', '|---|---|']
    for folder, paths, desc in CORE:
        lines.append('| %s | %s |' % (folder, desc))
    lines += ['', '## 원문 묶음(따로 받음)', '| zip | 내용 |', '|---|---|']
    for n, desc in raw_names:
        lines.append('| %s | %s |' % (n, desc))
    lines += ['', '## 경로 읽는 법',
              '- 번호 폴더 안은 저장소 경로 그대로임. handoff.md나 글에 나온 경로(예: db/facts.csv, kb/licdeep/01_틀에맞춘답.md) 앞에 번호 폴더(04_사실DB/, 03_정리본/)를 붙이면 찾음',
              '- 원문 경로(sources/..., KDX_사이트전수조사_인수인계/...)는 원문 zip을 같은 자리에 풀면 db/sources.csv의 "저장 파일 경로"와 맞음', '',
              '## 화면(Artifact) 링크']
    for name, url in ARTIFACTS:
        lines.append('- %s: %s' % (name, url))
    lines += ['', '## 원본 저장소', '- GitHub Mo-zZaAa/learning_tokens, 브랜치 research/kdx-overseas-20261116(이 zip은 그 브랜치의 %s 상태)' % DAY]
    return '\n'.join(lines) + '\n'


def index_html(top, raw_names, counts):
    css = (':root{--bg:#fafaf8;--fg:#1d1d1b;--mut:#6b6b66;--line:#e2e1dc;--acc:#d04a02;--card:#fff}'
           '@media (prefers-color-scheme:dark){:root{--bg:#1b1b1a;--fg:#ecebe6;--mut:#a3a29c;--line:#34332f;--card:#242422}}'
           'body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,"Malgun Gothic","Apple SD Gothic Neo",sans-serif}'
           'main{max-width:920px;margin:0 auto;padding:32px 16px 64px}h1{font-size:24px;margin:0 0 4px}'
           '.sub{color:var(--mut);margin:0 0 24px}h2{font-size:17px;margin:32px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--acc)}'
           '.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:8px 0}'
           '.card b{display:block}.card span{color:var(--mut);font-size:14px}a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}'
           'table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left;vertical-align:top}'
           'th{color:var(--mut);font-weight:600}.n{color:var(--mut);white-space:nowrap}')
    e = html.escape
    h = ['<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>KDX 리서치 목차</title><style>%s</style></head><body><main>' % css,
         '<h1>KDX 해외 사례 리서치 묶음</h1><p class="sub">%s 기준. 사실 DB, 정리본, 납품물, 화면 원본, 기록과 규칙, 도구. 원문은 따로 묶은 zip 셋</p>' % e(DAY),
         '<h2>먼저 볼 것</h2>']
    for path, desc in KEY:
        h.append('<div class="card"><b><a href="%s">%s</a></b><span>%s</span></div>' % (e(path), e(os.path.basename(path)), e(desc)))
    h.append('<h2>폴더</h2><table><tr><th>폴더</th><th>내용</th><th>파일 수</th></tr>')
    for folder, paths, desc in CORE:
        first = folder + '/' + paths[0]
        h.append('<tr><td><a href="%s">%s</a></td><td>%s</td><td class="n">%d</td></tr>' % (e(first), e(folder), e(desc), counts.get(folder, 0)))
    h.append('</table><h2>원문 묶음(따로 받음)</h2><table><tr><th>zip</th><th>내용</th></tr>')
    for n, desc in raw_names:
        h.append('<tr><td>%s</td><td>%s</td></tr>' % (e(n), e(desc)))
    h.append('</table><h2>화면(Artifact)</h2>')
    for name, url in ARTIFACTS:
        h.append('<div class="card"><b><a href="%s">%s</a></b><span>%s</span></div>' % (e(url), e(name), e(url)))
    h.append('<h2>원본 저장소</h2><p>GitHub Mo-zZaAa/learning_tokens, 브랜치 research/kdx-overseas-20261116</p></main></body></html>')
    return '\n'.join(h)


def main():
    os.makedirs(OUT, exist_ok=True)
    raw_names = [
        ('KDX_해외사례리서치_원문1_출처저장본_%s.zip' % DAY, '작업별로 저장한 원문(HTML, TXT, PDF)과 작업 폴더의 원문(work/*/raw). db/sources.csv의 저장 파일 경로가 가리키는 곳'),
        ('KDX_해외사례리서치_원문2_공식사이트수집_%s.zip' % DAY, '회사 공식 사이트 전수 수집(마크다운)과 회사별 위키'),
        ('KDX_해외사례리서치_원문3_캡처와사용자자료_%s.zip' % DAY, '화면 캡처 이미지, 사용자가 준 자료(엑셀 틀, 질의, A4 양식)'),
    ]
    top = 'KDX_해외사례리서치_%s' % DAY
    counts = {}
    core_zip = os.path.join(OUT, 'KDX_해외사례리서치_핵심_%s.zip' % DAY)
    with zipfile.ZipFile(core_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        z.writestr(top + '/00_먼저읽기.md', readme(top, raw_names))
        for folder, paths, desc in CORE:
            n = 0
            for rel in paths:
                for f in walk(rel):
                    add(z, f, '%s/%s/%s' % (top, folder, f)); n += 1
            counts[folder] = n
        z.writestr(top + '/00_목차.html', index_html(top, raw_names, counts))
        # work 원천 CSV(DB를 다시 만들 때 필요)
        for dp, dn, fn in os.walk(os.path.join(ROOT, 'work')):
            dn[:] = [d for d in dn if d not in SKIP_DIRS and d != 'raw']
            for f in fn:
                if f.endswith('.csv'):
                    rel = os.path.relpath(os.path.join(dp, f), ROOT)
                    add(z, rel, '%s/04_사실DB/%s' % (top, rel))
    out = [core_zip]
    for (name, paths, with_work_raw), (zname, _) in zip(RAW, raw_names):
        zp = os.path.join(OUT, zname)
        rtop = zname[:-4]
        with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for rel in paths:
                for f in walk(rel):
                    add(z, f, '%s/%s' % (rtop, f))
            if with_work_raw:
                for dp, dn, fn in os.walk(os.path.join(ROOT, 'work')):
                    dn[:] = [d for d in dn if d not in SKIP_DIRS]
                    if '/raw' not in dp.replace(os.sep, '/') + '/':
                        continue
                    for f in fn:
                        rel = os.path.relpath(os.path.join(dp, f), ROOT)
                        add(z, rel, '%s/%s' % (rtop, rel))
        out.append(zp)
    for p in out:
        print('%8.1fMB  %s' % (os.path.getsize(p) / 1048576, os.path.basename(p)))


if __name__ == '__main__':
    main()
