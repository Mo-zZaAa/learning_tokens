"""Merge work/<agent>/*.csv into db/*.csv with dedupe and new IDs.

Usage: python3 -I tools/merge_db.py <repo_root>
- facts.csv: fact_id rewritten to F-0001.., original id kept in a mapping file db/_fact_id_map.csv
- sources.csv: source_id rewritten to S-0001..; facts' source_id remapped
- laws, cases, terms, relations, blocked_links, absent, handover_questions, licenses, ats_screen: concatenated, exact-duplicate rows dropped
"""
import csv, glob, os, sys

root = sys.argv[1]
W = os.path.join(root, 'work')
D = os.path.join(root, 'db')
os.makedirs(D, exist_ok=True)

HEAD = {
 'facts': 'fact_id,회사,사업 법인,법인 소재지,시작(연월),끝 또는 현재,상태,자산 유형,밸류체인 위치,세부 기능,무엇을,누구에게,어떤 방식으로,근거 인가,관련 조문 ID,값,단위,무엇을 잰 것,기준일,회사가 밝힌 이유,앞선 fact_id,틀 항목,source_id,링크,원문 근거 문장,원문 위치,검증 상태,열람 일시',
 'sources': 'source_id,제목,발행 주체,발행일,출처 종류,언어,링크,저장 파일 경로,캡처 파일,접근 결과,열람 일시',
 'terms': '용어,원어,쉬운 뜻,이 과제에서 중요한 이유,헷갈리는 짝,차이 한 줄,한국의 대응 용어와 제도,source_id',
 'laws': 'law_id,국가,법령명,조항,시행일 또는 기준일,원문 발췌,쉬운 풀이,관련 쟁점,링크,검증 상태',
 'cases': 'case_id,국가,기관 또는 법원,사건명,시점,종류,당사자,쟁점,결론,그 뒤 달라진 것,관련 회사,링크,검증 상태',
 'relations': '주체,주체 유형,대상,대상 유형,관계 종류,지분율,금액,시점,상태,회사가 밝힌 목적,source_id,링크,검증 상태',
 'blocked_links': '링크,무엇이 있는 곳인지,필요한 이유,막힌 종류,시도한 방법,필요한 조치',
 'absent': '회사,항목,구분,사유,찾아본 곳',
 'handover_questions': '대상,추가로 볼 것,질문이 나온 배경,관련 fact_id',
 'licenses': '회사,보유 법인,하는 일,등록 종류,감독기관,관할,확보 방식,인수 또는 제휴 대상,시점,등록부 링크,원문 근거 문장,열람 일시,검증 상태',
 'ats_screen': 'ATS명,운영사,모회사,취급 자산,대상 고객,거래시간,거래 방식,거래 규모(기준 기간),차별화 요소,토큰증권 취급 현황,선정 결과,선정 사유,링크',
}
ALIAS = {'ats_rows': 'ats_screen'}


def read(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def collect(name):
    out = []
    files = sorted(glob.glob(os.path.join(W, '*', name + '.csv')))
    for a, b in ALIAS.items():
        if b == name:
            files += sorted(glob.glob(os.path.join(W, '*', a + '.csv')))
    for p in files:
        agent = os.path.basename(os.path.dirname(p))
        h, rows = read(p)
        cols = HEAD[name].split(',')
        for r in rows:
            if not any(x.strip() for x in r):
                continue
            d = dict(zip(h, r))
            out.append((agent, [d.get(c, '') for c in cols]))
    return out

# sources first (id remap)
src_map, src_rows, seen_link = {}, [], {}
for agent, r in collect('sources'):
    old, link = r[0], r[6]
    key = link.strip() or (agent + old)
    if key in seen_link:
        src_map[(agent, old)] = seen_link[key]
        continue
    nid = 'S-%04d' % (len(src_rows) + 1)
    seen_link[key] = nid
    src_map[(agent, old)] = nid
    src_rows.append([nid] + r[1:])

prev = {}
mp = os.path.join(D, '_fact_id_map.csv')
if os.path.exists(mp):
    for row in csv.DictReader(open(mp, encoding='utf-8')):
        prev[(row['agent'], row['original_id'])] = row['fact_id']
nextn = max([int(v[2:]) for v in prev.values()] + [0])
fact_rows, fmap, seen = [], [], set()
for agent, r in collect('facts'):
    key = (r[1], r[10], r[23], r[24])
    if key in seen:
        continue
    seen.add(key)
    if (agent, r[0]) in prev:
        nid = prev[(agent, r[0])]
    else:
        nextn += 1
        nid = 'F-%04d' % nextn
    fmap.append([nid, agent, r[0]])
    r = [nid] + r[1:]
    sid = r[22]
    r[22] = src_map.get((agent, sid), sid)
    fact_rows.append(r)


def write(name, rows):
    with open(os.path.join(D, name + '.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(HEAD[name].split(','))
        w.writerows(rows)

write('sources', src_rows)
ver = {}
for vp in sorted(glob.glob(os.path.join(W, 'VER-*', 'verdicts.csv'))):
    for row in csv.DictReader(open(vp, encoding='utf-8-sig')):
        if row.get('fact_id') and row.get('새 검증 상태') in ('1차 출처 확인', '교차 확인', '단일 출처', '충돌'):
            ver[row['fact_id'].strip()] = row['새 검증 상태']
for r in fact_rows:
    if r[0] in ver:
        r[26] = ver[r[0]]
fact_rows.sort(key=lambda r: r[0])
write('facts', fact_rows)
with open(os.path.join(D, '_fact_id_map.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['fact_id', 'agent', 'original_id']); w.writerows(fmap)
for name in ['terms', 'laws', 'cases', 'relations', 'blocked_links', 'absent', 'handover_questions', 'licenses', 'ats_screen']:
    rows, seen = [], set()
    for agent, r in collect(name):
        k = tuple(x.strip() for x in r)
        if name == 'terms':
            k = (r[0].strip().lower(),)
        if k in seen:
            continue
        seen.add(k)
        if name == 'relations' and len(r) > 10:
            r[10] = src_map.get((agent, r[10]), r[10])
        rows.append(r)
    write(name, rows)
print('facts', len(fact_rows), 'sources', len(src_rows))
