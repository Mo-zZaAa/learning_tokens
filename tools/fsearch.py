"""사실 DB 검색 (백데이터로 쓰는 기본 도구)

사용법(저장소 맨 위에서):
  python3 -I tools/fsearch.py "Bitstamp&인가" "NinjaTrader"          # 모든 회사
  python3 -I tools/fsearch.py --co Robinhood "Gold&구독자"            # 회사 열이 Robinhood로 시작하는 것만
  python3 -I tools/fsearch.py --status 1차 "MiCA"                     # 검증 상태에 '1차'가 든 것만
  python3 -I tools/fsearch.py --src "Deribit"                         # 출처 목록(db/sources.csv)에서 찾기
  python3 -I tools/fsearch.py --n 20 "예측시장"                       # 한 검색어에 최대 20줄
  python3 -I tools/fsearch.py --id F-1826                             # 사실 한 건 전체 칸 보기

검색어 규칙: '&'로 이은 조건을 모두 만족하는 줄. 각 조건은 정규식(대소문자 무시).
찾는 칸: 무엇을, 원문 근거 문장, 값, 단위, 기준일, 사업 법인, 회사가 밝힌 이유, 링크
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTS = os.path.join(ROOT, 'db', 'facts.csv')
SRCS = os.path.join(ROOT, 'db', 'sources.csv')
FIELDS = ['무엇을', '원문 근거 문장', '값', '단위', '기준일', '사업 법인', '회사가 밝힌 이유', '링크']


def load(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def main(argv):
    co = status = None
    n = 5
    src = False
    ident = None
    qs = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--co':
            co = argv[i + 1]; i += 2; continue
        if a == '--status':
            status = argv[i + 1]; i += 2; continue
        if a == '--n':
            n = int(argv[i + 1]); i += 2; continue
        if a == '--src':
            src = True; i += 1; continue
        if a == '--id':
            ident = argv[i + 1]; i += 2; continue
        qs.append(a); i += 1
    if ident:
        for r in load(FACTS):
            if r['fact_id'] == ident:
                for k, v in r.items():
                    if v:
                        print('%s: %s' % (k, v))
                return
        print('없음:', ident)
        return
    if src:
        rows = load(SRCS)
        for q in qs:
            pats = q.split('&')
            hits = [r for r in rows if all(re.search(p, ' '.join(r.values()), re.I) for p in pats)]
            print('## %s  %d건' % (q, len(hits)))
            for r in hits[:n]:
                print('  %s | %s | %s | %s | %s' % (r['source_id'], r['발행일'], r['제목'][:70], r['링크'][:90], r['저장 파일 경로'][:80]))
        return
    rows = load(FACTS)
    if co:
        rows = [r for r in rows if r['회사'].startswith(co)]
    if status:
        rows = [r for r in rows if status in r['검증 상태']]
    for q in qs:
        pats = q.split('&')
        hits = [r for r in rows if all(re.search(p, ' '.join(r.get(k, '') for k in FIELDS), re.I) for p in pats)]
        print('## %s  %d건' % (q, len(hits)))
        for r in hits[:n]:
            print('  %s | %s | %s | %s | %s | %s' % (r['fact_id'], r['회사'], r['기준일'], r['검증 상태'], r['무엇을'][:90], r['링크'][:90]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        main(sys.argv[1:])
