"""백데이터 묶음 만들기: 자료 목록(catalog.csv)과 사람용 엑셀(deliverables/KDX_백데이터_<날짜>.xlsx)

사용법(저장소 맨 위에서): python3 -I tools/build_backdata.py 261120
- catalog.csv: 저장소의 자료 덩어리마다 종류, 내용, 언제 쓰나, 파일 수, 크기, 마지막 커밋일
- 엑셀: 읽는 법, 자료 목록, DB 표 전부, 인가 딥다이브 연표, 화면 메모
- discussion/site_db_export_<날짜>/memos.csv: 화면(Artifact) 메모를 표로
"""
import csv, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAY = sys.argv[1] if len(sys.argv) > 1 else '261120'

# (경로, 종류, 내용 한 줄, 언제 쓰나)
CAT = [
    ('db/facts.csv', 'DB', '사실 한 줄마다 날짜, 값, 원문 문장, 링크, 검증 상태', '숫자나 날짜를 인용할 때 먼저 여기서 찾음(tools/fsearch.py)'),
    ('db/sources.csv', 'DB', '출처 목록(제목, 발행 주체, 발행일, 링크, 저장 파일 경로)', '원문을 다시 열 때. 저장 파일 경로가 있으면 sources/ 아래 저장본'),
    ('db/licenses.csv', 'DB', '회사별 인가와 등록(법인, 감독기관, 확보 방식, 등록부 링크)', '인가 지도, 직접 대 인수 비교'),
    ('db/relations.csv', 'DB', '회사 사이 관계(지분, 제휴, 계약, 주고받는 것)', '관계도, 누가 누구에게 파나'),
    ('db/laws.csv', 'DB', '법령 조문 발췌와 쉬운 풀이', '제도 설명'),
    ('db/cases.csv', 'DB', '감독기관 조치와 판결', '규제 사건 인용'),
    ('db/terms.csv', 'DB', '용어 사전(쉬운 뜻, 헷갈리는 짝, 한국 대응)', '용어 풀이'),
    ('db/third_party.csv', 'DB', '제3자 보고서 숫자(발행처, 쪽, 원문)', '시장 규모, 점유율'),
    ('db/absent.csv', 'DB', '찾았으나 없던 것(어디까지 찾았나)', '"공개 안 됨"을 말할 근거'),
    ('db/blocked_links.csv', 'DB', '열지 못한 링크와 막힌 이유', '다시 시도할 목록'),
    ('db/companies.csv', 'DB', '상품별 발행 주체와 법적 성격', '토큰 상품 비교'),
    ('db/_fact_id_map.csv', 'DB', 'DB 번호(F-xxxx)와 작업별 원래 번호 대응', 'DB 줄을 고칠 때 원천 work 파일을 찾음'),
    ('work', 'DB 원천', '작업 ID별 facts.csv, sources.csv(병합 전 원천)와 일부 원문', 'DB를 고칠 때는 여기 원천 줄도 같이 고침(병합하면 DB를 다시 만듦)'),
    ('sources', '원자료', '작업 ID별로 저장한 원문(HTML, TXT, PDF)', '원문 문장을 다시 확인할 때'),
    ('KDX_사이트전수조사_인수인계', '원자료', '회사 공식 사이트 전수 수집 원문(마크다운)과 회사별 위키', '회사 사이트 문장 확인'),
    ('captures', '원자료', '화면 캡처 이미지', '원문 화면 증거'),
    ('inputs', '원자료(사용자 제공)', '사용자가 준 자료(엑셀 틀, 질의, A4 양식, 이미지)', '요청 원문 확인'),
    ('companies', '정리본', '회사 본문(최신은 *_v4.md)', '회사 전체 서술'),
    ('kb/robinhood_overview', '정리본', '회사 1층 카드 원본 JSON(kraken, coinbase, binance, ondo도 같은 꼴)', '화면 카드 고칠 때'),
    ('kb/cards6', '정리본', '회사 카드(마크다운, Dinari 등)', '카드 원문'),
    ('kb/easy', '정리본', '쉬운 해설(2층)', '처음 보는 사람용 설명'),
    ('kb/revenue', '정리본', '매출로 본 성공 원인(4개사, 해마다 구성, 왜)', '매출과 사업 모델'),
    ('kb/events', '정리본', '사건 카드 원본(회사별 *_events_src.py)', '연혁, 사건별 무엇, 어떻게, 왜'),
    ('kb/structs', '정리본', '회사별 구조 표(거래, 법인, 자금, 돈, 상품, 판매, 연표 CSV)', '표로 비교'),
    ('kb/licdeep', '정리본', '인가 획득 딥다이브(카드, 평행 연표, 발언 모음, 가설 표, 빈칸, 틀에 맞춘 답)', '인가 직접 대 인수, 시점, 목적'),
    ('kb/a4', '정리본', 'A4 원본 JSON과 렌더러(긴 판, 간결 판)', 'A4 다시 뽑기'),
    ('kb/product_tables', '정리본', '상품별 표 틀과 점검 도구', '상품 표'),
    ('kb/vision', '정리본', '한눈에 보기와 핵심 포인트 생성 도구', '맨 위 요약'),
    ('kb/regulation_us.md', '정리본', '미국 제도 정리', '제도'),
    ('kb/regulation_kr.md', '정리본', '한국 제도 정리', '제도'),
    ('kb/regulation_compare.md', '정리본', '나라별 제도 비교', '제도'),
    ('web/v5', '화면', '사이트 빌드(build.py, template.html, index.html). Artifact QnuzMo25ig3Qw9K7ACgFuJ로 게시', '화면 다시 게시'),
    ('discussion', '기록', '화면 메모와 답, 사용자 질의 답, 화면 DB 내보내기', '피드백 이력'),
    ('deliverables', '납품', 'A4 docx, 회사별 글 다듬기, 매출 원인 md, 인가 딥다이브 zip, 백데이터 엑셀', '바로 전달'),
    ('export', '납품(예전)', '브리핑 엑셀, 최종본 묶음(2026-11-17 전후)', '예전 납품 확인'),
    ('playbook', '지시', '쓰기 규칙, 리서치 노하우, 피드백 회차 기록', '새 작업 시작 전 필독'),
    ('tools', '도구', 'DB 병합, 검색(fsearch.py), 점검, 엑셀 내보내기, 백데이터 묶음', '재료 찾기와 갱신'),
    ('CLAUDE.md', '지시', '저장소 규칙 요약(새 세션이 자동으로 읽음)', '새 세션'),
    ('handoff.md', '지시', '인계 문서(이 백데이터의 입구)', '처음 볼 것'),
    ('scratchpad', '작업 흔적', '저장소 안 임시 스크립트(rhov 등 화면 패치 스크립트)', '과거 작업 재현'),
    ('backup_261118b', '작업 흔적', '2026-11-18 백업', '되돌릴 때'),
]


def git_last(path):
    try:
        out = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%cs', '--', path], capture_output=True, text=True).stdout.strip()
        return out
    except Exception:
        return ''


def stats(path):
    p = os.path.join(ROOT, path)
    if os.path.isfile(p):
        if p.endswith('.csv'):
            with open(p, encoding='utf-8-sig', newline='') as f:
                n = sum(1 for _ in csv.reader(f)) - 1
            return 1, os.path.getsize(p), '%d줄' % n
        return 1, os.path.getsize(p), ''
    n = s = 0
    for dp, dn, fn in os.walk(p):
        if '/.git' in dp or '__pycache__' in dp:
            continue
        for f in fn:
            n += 1
            try:
                s += os.path.getsize(os.path.join(dp, f))
            except OSError:
                pass
    return n, s, ''


def human(b):
    for u in ['B', 'KB', 'MB', 'GB']:
        if b < 1024:
            return '%.0f%s' % (b, u)
        b /= 1024
    return '%.1fTB' % b


def build_catalog():
    rows = []
    for path, kind, what, when in CAT:
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        n, s, extra = stats(path)
        rows.append([path, kind, what, when, n, human(s), extra, git_last(path)])
    out = os.path.join(ROOT, 'catalog.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['경로', '종류', '내용', '언제 쓰나', '파일 수', '크기', '줄 수', '마지막 커밋일'])
        w.writerows(rows)
    return rows


def memos_csv():
    d = os.path.join(ROOT, 'discussion', 'site_db_export_%s' % DAY, 'memos')
    rows = []
    for p in sorted(glob.glob(os.path.join(d, '*.json'))):
        j = json.load(open(p, encoding='utf-8'))
        rows.append([j.get('mid', ''), j.get('co', ''), j.get('at') or j.get('time', ''), j.get('type', ''), j.get('st', ''),
                     j.get('disp') or j.get('sec', ''), j.get('line') or j.get('quote', ''), j.get('text', '')])
    if rows:
        with open(os.path.join(os.path.dirname(d), 'memos.csv'), 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(['메모 ID', '회사', '시각', '유형', '상태', '위치', '고른 줄', '메모'])
            w.writerows(rows)
    return [['메모 ID', '회사', '시각', '유형', '상태', '위치', '고른 줄', '메모']] + rows


def read_csv(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.reader(f))


def build_xlsx(catalog, memos):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    wb = Workbook()
    ws = wb.active
    ws.title = '읽는 법'
    guide = [
        ['KDX 해외 사례 리서치 백데이터 (%s)' % DAY],
        [''],
        ['무엇', '이 파일은 저장소의 DB 표와 정리 결과를 한 엑셀로 묶은 것. 원문은 저장소 sources/와 각 행의 링크'],
        ['입구', '저장소 handoff.md(인계 문서), catalog.csv(자료 목록). 저장소 github.com/Mo-zZaAa/learning_tokens 브랜치 research/kdx-overseas-20261116'],
        ['facts 시트', '사실 한 줄 = 한 사실. fact_id(F-xxxx)는 바뀌지 않는 번호라 인용에 씀. 검증 상태: 1차 출처 확인(공시, 당국, 회사 원문과 대조), 교차 확인(출처 둘 이상), 단일 출처(매체 하나), 회사 주장, 충돌(출처끼리 다름), 사용자 제공'],
        ['표기', '(판단) 해석, (계산) 공개 숫자로 셈한 값, (보도, 매체명) 2차 출처. 숫자는 무엇을 잰 것인지와 기준일을 함께 봄'],
        ['sources 시트', '출처 목록. 저장 파일 경로가 있으면 저장소에 원문 사본이 있음'],
        ['licdeep 시트', '인가 획득 딥다이브의 회사별, 바깥 요인 연표(날짜, 분기, 구분, 한 줄, 링크)'],
        ['memos 시트', '화면(Artifact)에 사용자가 남긴 메모(피드백 이력)'],
        ['주의', '긴 칸은 엑셀 칸 한도(32,767자)에서 잘렸을 수 있음. 원본은 저장소 CSV'],
    ]
    for r in guide:
        ws.append(r)
    ws['A1'].font = Font(bold=True, size=14)
    ws.column_dimensions['A'].width = 16
    ws.column_dimensions['B'].width = 140
    for row in ws.iter_rows(min_row=3):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical='top')

    def sheet(name, rows, widths=None):
        s = wb.create_sheet(name[:31])
        for r in rows:
            s.append([(str(x)[:32000] if x is not None else '') for x in r])
        if rows:
            for c in s[1]:
                c.font = Font(bold=True, color='FFFFFF')
                c.fill = PatternFill('solid', fgColor='404040')
            s.freeze_panes = 'A2'
            s.auto_filter.ref = s.dimensions
            for i, h in enumerate(rows[0], start=1):
                col = s.cell(row=1, column=i).column_letter
                s.column_dimensions[col].width = (widths or {}).get(h, 14 if len(str(h)) < 8 else 22)
        return s

    sheet('자료 목록', [['경로', '종류', '내용', '언제 쓰나', '파일 수', '크기', '줄 수', '마지막 커밋일']] + catalog,
          {'경로': 34, '내용': 60, '언제 쓰나': 46})
    wide = {'무엇을': 70, '원문 근거 문장': 60, '링크': 40, '제목': 50, '쉬운 뜻': 50, '원문 발췌': 60, '쉬운 풀이': 50, '내용': 60, '쟁점': 40, '결론': 40}
    for t in ['facts', 'sources', 'licenses', 'relations', 'laws', 'cases', 'terms', 'third_party', 'absent', 'blocked_links', 'companies', 'cross_axis']:
        p = os.path.join(ROOT, 'db', t + '.csv')
        if os.path.exists(p):
            sheet(t, read_csv(p), wide)
    tl = [['회사', '날짜', '분기', '구분', '한 줄', '출처 링크']]
    for slug in ['coinbase', 'kraken', 'robinhood', 'binance', 'external']:
        p = os.path.join(ROOT, 'kb', 'licdeep', slug + '_timeline.csv')
        if not os.path.exists(p):
            continue
        with open(p, encoding='utf-8-sig', newline='') as f:
            for r in csv.DictReader(f):
                tl.append([slug, r.get('날짜', ''), r.get('분기', ''), r.get('구분') or r.get('분류', ''), r.get('한 줄', ''), r.get('출처 링크', '')])
    sheet('licdeep 연표', tl, {'한 줄': 90, '출처 링크': 40})
    if len(memos) > 1:
        sheet('memos', memos, {'고른 줄': 50, '메모': 60, '위치': 24})
    out = os.path.join(ROOT, 'deliverables', 'KDX_백데이터_%s.xlsx' % DAY)
    wb.save(out)
    return out


if __name__ == '__main__':
    cat = build_catalog()
    memos = memos_csv()
    out = build_xlsx(cat, memos)
    print('catalog.csv', len(cat), '줄 |', out, '| 메모', len(memos) - 1)
