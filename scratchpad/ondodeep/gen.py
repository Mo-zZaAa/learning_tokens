import csv, json, re, html, sys
sys.path.insert(0, '/home/user/learning_tokens/scratchpad/ondodeep')
from refs import resolve, ROOT, PKG

OUT = ROOT / 'web/v5/ondo_deep.html'
E = html.escape

# ---------- 용어 ----------
GL = list(csv.DictReader(open(PKG / 'content/용어사전.csv', encoding='utf-8-sig')))
TERMS = []  # (key, idx)
for i, g in enumerate(GL):
    t = g['용어']
    special = {'Rule 506(c)': ['Rule 506(c)'], '3(c)(7)': ['3(c)(7)'], '발행(mint)과 상환(redeem)': ['상환'],
               'share class(클래스)': ['share class'], '케이맨제도(Cayman Islands)': ['케이맨제도', '케이맨'],
               'SEC 등록 투자자문사(RIA)': ['SEC 등록 투자자문사', '투자자문사'], 'CFC(피지배외국법인) 규정': ['CFC'],
               'economic exposure(경제적 노출)': ['economic exposure'], 'limited recourse(제한 상환청구)': ['limited recourse'],
               '잔액(outstanding, 발행 잔액)': ['잔액'], '면제(exemption)': ['면제'], '토큰(token)': ['토큰']}
    keys = special.get(t) or [re.split(r'[(（]', t)[0].strip()]
    for k in keys:
        TERMS.append((k, i))
TERMS.sort(key=lambda x: -len(x[0]))
TERM_RE = re.compile('|'.join(('(?<![A-Za-z])' + re.escape(k) + '(?![A-Za-z])') if re.match(r'^[A-Za-z0-9 ()]+$', k) else re.escape(k) for k, _ in TERMS))
TERM_IDX = {k: i for k, i in TERMS}
USED = set()

# ---------- 각주 ----------
FN = {}      # key -> n
FN_LIST = []  # (n, key, ref, section)
CUR_SEC = ['']
FN_RE = re.compile(r'\[((?:F|on|S|DB|ONM2?|DL)-[\w-]+(?:\s+(?:F|on|S|DB|ONM2?|DL)-[\w-]+)*)\]')
WARN = []


def fn_html(keys):
    out = []
    for k in keys.split():
        if k not in FN:
            ref = resolve(k)
            FN[k] = len(FN) + 1
            FN_LIST.append((FN[k], k, ref, CUR_SEC[0]))
        out.append(f'<button type="button" class="fn" data-fn="{FN[k]}" aria-label="출처 {FN[k]}">{FN[k]}</button>')
    return '<sup class="fns">' + ''.join(out) + '</sup>'


def mark_terms(s):
    def rep(m):
        k = m.group(0)
        i = TERM_IDX.get(k)
        if i is None or i in USED:
            return k
        USED.add(i)
        return f'<button type="button" class="term" data-t="{i}">{k}</button>'
    return TERM_RE.sub(rep, s)


def T(s, terms=True):
    """본문 문자열: 이스케이프, 용어 표시, 각주."""
    parts = FN_RE.split(s)
    out = []
    for j, p in enumerate(parts):
        if j % 2 == 1:
            out.append(fn_html(p))
        else:
            x = E(p, quote=False)
            x = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', x)
            out.append(mark_terms(x) if terms else x)
    return ''.join(out)


def line(s, tag='li'):
    s = s.strip()
    ex = s.startswith('{ex}')
    if ex:
        s = s[4:].strip()
    jd = s.startswith('(판단)')
    has = bool(FN_RE.search(s))
    cls = 'jd' if jd else ('f' if has else ('x' if ex else 'nof'))
    if cls == 'nof':
        WARN.append(CUR_SEC[0] + ': ' + s[:60])
    return f'<{tag} class="{cls}">{T(s)}</{tag}>'


def ul(lines):
    out = ['<ul class="ls">']
    for s in lines:
        if isinstance(s, tuple):  # (머리, [하위])
            out.append(line(s[0]).replace('</li>', ''))
            out.append('<ul class="ls sub">' + ''.join(line(x) for x in s[1]) + '</ul></li>')
        else:
            out.append(line(s))
    out.append('</ul>')
    return ''.join(out)


def legend(items):
    return '<div class="lg">' + ''.join(f'<span><i class="sw {c}"></i>{E(t)}</span>' for c, t in items) + '</div>'


LG4 = [('co', '회사 쪽(Ondo Finance Inc.와 그 아래)'), ('fd', '재단 쪽(Ondo Foundation, Flux Finance)'), ('is', '발행 법인(Ondo Global Markets (BVI))'), ('tp', '제3자(계약 상대)'), ('pr', '상품')]

SECS = []


def sec(sid, title, head, fig, l2, l3, l2title='읽는 법과 핵심 숫자'):
    SECS.append(dict(id=sid, title=title, head=head, fig=fig, l2=l2, l3=l3, l2title=l2title))


def box(cls, title, body='', small=''):
    return f'<div class="bx {cls}"><b>{T(title)}</b>{("<span>" + T(body) + "</span>") if body else ""}{("<em>" + T(small) + "</em>") if small else ""}</div>'


def arrow(label):
    return f'<div class="ar"><span>{T(label)}</span></div>'


def chip(t):
    return f'<span class="chip pr">{E(t)}</span>'


# ======================= S1 =======================
CUR_SEC[0] = 'S1'
cards = [
    ('OUSG', '국채 펀드 토큰', [
        ('누가 사나', '미국 적격투자자이면서 적격매수자. 개인은 투자자산 500만 달러 초과. 한국 거주자, 한국 법인 제외 [F-1308 F-1404]'),
        ('안에 든 것', '운용사 펀드 4개와 USDC(2026-11-18): SWEEP 48.58%, BUIDL 32.69%, BENJI 10.12%, FYOXX 7.54%, USDC 1.14% [S-ousg-page]'),
        ('금고 주인', 'Ondo I LP(델라웨어 펀드 그 자체). 무한책임사원 쪽 단독 구성원이 Ondo Finance Inc. [F-0534]'),
        ('보유자 권리', '펀드 지분(유한책임사원 지분) [F-1307]'),
        ('Ondo 수입', '운용보수 연 0.15%, 2027-01-01까지 면제라 지금 0 [F-1313]'),
        ('크기', '3.1억 달러(2026-11-17 홈페이지) [F-1666]')], 'co'),
    ('USDY', '국채 담보 토큰(yieldcoin)', [
        ('누가 사나', '미국 밖 개인과 기관. 최소 500달러, 주력 체인 밖 5,000달러 [on-0349]'),
        ('안에 든 것', '미국 국채 82.73%, SHVon 17.24%(2026-11-13) [on-0335]'),
        ('금고 주인', 'Ondo Global Markets (BVI) Limited. 2025-12-15 전에는 Ondo USDY LLC [on-0327]'),
        ('보유자 권리', '담보부 노트. 발행 법인에 대한 채권과 그 담보 [F-1151]'),
        ('Ondo 수입', '담보에서 받는 이자와 보유자에게 주는 이자의 차이 [ONM-019]'),
        ('크기', '23.8억 달러(2026-11-17 홈페이지) [F-1666]')], 'is'),
    ('Ondo Stocks', '주식 토큰(예: AAPLon)', [
        ('누가 사나', '미국 밖 개인과 기관, 그리고 거래소와 지갑 [on-0222]'),
        ('안에 든 것', '토큰과 같은 수량의 실제 미국 주식과 ETF(Alpaca, BitGo Trust 담보 계좌) [on-0055]'),
        ('금고 주인', 'Ondo Global Markets (BVI) Limited [F-0185]'),
        ('보유자 권리', '채무증권 토큰. 값과 배당만 따라감(economic exposure). 의결권, 주주명부 등재 없음 [on-0160]'),
        ('Ondo 수입', '발행 수수료 0, 상환 수수료 0.05%와 견적가 차이 [F-0545]'),
        ('크기', '14.4억 달러, 종목 470개 이상(2026-11-17 홈페이지) [F-1666]')], 'is'),
    ('Intelligent Portfolios', '포트폴리오 토큰', [
        ('누가 사나', 'Ondo Stocks와 같은 미국 밖 투자자(판단)'),
        ('안에 든 것', 'Ondo Stocks 여러 종목을 정해진 비중으로 묶은 바구니. 첫 3종 BLKHIon, BLKDIGon, BLKGRWon은 BlackRock이 Ondo를 위해 만든 전략 기반 [on-0364]'),
        ('금고 주인', '바구니 속 종목마다 Ondo Stocks 금고 구조 그대로(판단)'),
        ('보유자 권리', '토큰 1개에 포트폴리오 전체(판단)'),
        ('Ondo 수입', '연 서비스 수수료, 매일 토큰 가격에 반영 [F-1956]'),
        ('크기', '2026-09-24 출시 [F-1324]')], 'is'),
    ('ONDO 토큰', '재단 발행 투표용 코인(상품 아님, 회사 매출 아님)', [
        ('누가 냈나', 'Ondo Foundation(케이맨 재단). 회사 주식과 별개 [on-0279]'),
        ('권리', '회사나 계열사 이익과 매출에 대한 권리 없음 [ONM2-005]'),
        ('판매', '2022-07 CoinList에서 1만 8천여 명에게 1,000만 달러 이상(공급량 약 2%) [F-1922 F-1925]'),
        ('총량', '100억 개, 예정된 추가 발행 없음 [ONM2-004]')], 'fd'),
]
g = [legend([('pr', '상품 이름'), ('co', '금고 주인이 회사 쪽'), ('is', '금고 주인이 발행 법인'), ('fd', '재단 쪽')]), '<div class="cards5">']
for name, sub, rows, own in cards:
    dash = ' dash' if name == 'ONDO 토큰' else ''
    g.append(f'<div class="pcard {own}{dash}"><div class="ph">{chip(name) if name != "ONDO 토큰" else "<span class=\"chip fdc\">ONDO 토큰</span>"}<small>{E(sub)}</small></div><dl>')
    for k, v in rows:
        jd = '(판단)' in v and not FN_RE.search(v)
        g.append(f'<dt>{E(k)}</dt><dd class="{"jd" if jd else "f"}">{T(v)}</dd>')
    g.append('</dl></div>')
g.append('</div>')
sec('S1', 'Ondo는 무엇을 하나',
    '미국 국채와 미국 주식을 사 두고 그 값을 따라가는 토큰을 찍어 파는 회사. 사는 사람에 따라 상품과 발행 법인이 갈라짐',
    ''.join(g),
    ['{ex}카드 읽는 법: 칸 순서는 누가 사나, 안에 든 것, 금고 주인, 보유자 권리, Ondo 수입, 크기. 카드 테두리 색은 금고 주인(파랑 회사 쪽, 노랑 발행 법인)',
     '{ex}토큰: 블록체인 지갑에 들어가는 디지털 보관증. 지갑이나 거래소 계좌에 "USDY 1,000", "TSLAon 2"처럼 잔고로 보임',
     '기본 구조: 진짜 자산(국채, 주식)은 발행 법인 명의 계좌에 두고, 그 값을 따라가는 토큰을 찍어 팖 [on-0218]',
     '상품 크기 합계 약 41억 달러: USDY 23.8억, Ondo Stocks 14.4억, OUSG 3.1억 달러(2026-11-17 홈페이지) [F-1666]',
     '1달러 = 약 1,430원으로 치면 약 5조 8,600억 원(판단 아님, 환산)'.replace('(판단 아님, 환산)', '(환산) [F-1666]'),
     'Intelligent Portfolios는 상품 맞음. Ondo 앱 메뉴 Invest에 USDY, OUSG, Ondo Stocks와 나란히 있음 [F-1666]'],
    [('본사 Ondo Finance Inc.: 미국 코네티컷주 그리니치, 2021 설립. 창업자 Nathan Allman(전 Goldman Sachs 디지털자산 팀) [on-0131 F-0497]', []),
     '창업자 2026-05 사망, Ian De Bode CEO 승계(팀 페이지 직함 Acting CEO and President) [on-0005]',
     '투자: 2021~2022 지분 투자 합계 2,400만 달러. 그중 2022-04 시리즈 A 2,000만 달러(Founders Fund, Pantera 주도, Coinbase Ventures 등 참여) [F-1207 F-1212]',
     ('Intelligent Portfolios가 생기면 달라지는 것', [
         '투자자: 바구니를 직접 짜고 비중을 다시 맞추는 일 없이 토큰 하나로 분산 투자 [S-ip-blog]',
         '(판단) Ondo: Ondo Stocks 위에 연 서비스 수수료가 한 겹 더 붙음. 포트폴리오가 담는 만큼 Ondo Stocks 발행 수요도 늘어남',
         '(판단) 비유: Ondo Stocks(낱개 종목 토큰)가 낱개 반찬이면 Intelligent Portfolios(포트폴리오 토큰)는 정해진 비율로 담은 도시락. BlackRock이 식단표(portfolio strategy)를 짜고 Ondo가 도시락을 싸서(구현과 리밸런싱) 팖']),
     'ONDO 토큰 배분(2024-01 재단 제안): 공개 판매 약 2.0%, 생태계 성장 약 52.1%, 프로토콜 개발 33.0%(Ondo Finance 같은 핵심 기여자 몫), 사적 판매 약 12.9% [ONM2-006]',
     'ONDO 투표 범위: Ondo DAO와 Flux Finance의 경제 변수와 스마트 계약 업그레이드 [ONM2-003]'])

# ======================= S2 =======================
CUR_SEC[0] = 'S2'
RM = list(csv.DictReader(open(PKG / 'data/role_matrix.csv', encoding='utf-8-sig')))
cols = ['발행', '운용(무엇을 살지)', '보관', '담보 대리', '판매 창구(1차)', '2차 거래 시설', '인프라(장부와 실행)']


def rmcls(v):
    if v.startswith('Ondo 직접') or v.startswith('Ondo 앱'):
        return 'co'
    if v.startswith('재단 쪽'):
        return 'is'
    if v.startswith('제3자') or v.startswith('기존 미국'):
        return 'tp'
    return 'na'


def rmtext(v):
    v = v.replace('재단 쪽 계열(BVI 발행 법인)', '발행 법인(BVI)').replace('재단 쪽 계열(발행 법인이 국채 직접 보유)', '발행 법인이 국채 직접 보유')
    v = v.replace('Ondo 직접 배분(Ondo Capital Management) + 제3자 운용(운용사 4곳)', 'Ondo 직접 배분(Ondo Capital Management), 국채 운용은 제3자 운용사 4곳')
    v = v.replace('제3자 전략(BlackRock) + Ondo 실행', '제3자 전략(BlackRock), 실행은 Ondo')
    return v


g = [legend([('co', 'Ondo 회사 쪽 직접'), ('is', '발행 법인(재단 쪽 90.01%)'), ('tp', '제3자'), ('na', '해당 없음')]), '<div class="rm" role="table">']
g.append('<div class="rmr rmh" role="row"><div role="columnheader">상품</div>' + ''.join(f'<div role="columnheader">{E(c)}</div>' for c in cols) + '</div>')
for r in RM:
    g.append(f'<div class="rmr" role="row"><div class="rmp" role="rowheader">{chip(r["상품"])}</div>')
    for c in cols:
        v = rmtext(r[c])
        g.append(f'<div class="rmc {rmcls(r[c])}" role="cell" data-col="{E(c)}">{E(v)}</div>')
    g.append('</div>')
g.append('</div><p class="cap x">칸 값 출처: 아래 2층, 3층 줄의 각주. 발행 법인 칸은 노랑(이 페이지 전체 같은 뜻)</p>')
sec('S2', 'Ondo는 상품마다 무슨 역할을 하나',
    'Ondo의 본업은 발행사. 운용은 남의 펀드에 맡기고 보관은 아예 안 함. 거래 시설과 인프라는 2025~2026에 새로 붙이는 중',
    ''.join(g),
    ['{ex}읽는 법: 행은 상품, 열은 일의 단계. 파랑 칸이 많을수록 Ondo가 직접 하는 일',
     '발행사: 거의 모든 상품을 Ondo 쪽 법인이 직접 찍음. 단 미국 밖 상품을 찍는 BVI 발행 법인은 재단 쪽 Flux Finance가 90.01%, Ondo Finance Inc.가 9.99% [on-0008]',
     '운용사: OUSG만 어느 펀드를 얼마나 담을지 Ondo Capital Management(SEC 등록 투자자문사)가 정함. 국채를 실제로 굴리는 일은 펀드 운용사 몫 [F-0534 F-1152]',
     '보관: 하지 않음. 약관상 서비스는 중개, 거래소, 체결, 결제, 청산, 보관 서비스가 아님 [F-0526]. 주식은 Alpaca, BitGo Trust가 맡음 [on-0055]',
     '거래사: 미국 밖 2차 거래는 남의 거래소와 지갑(Bitget, Binance 등) [on-0078 F-1457]. Ondo가 직접 거래 시설을 가진 곳은 둘: 미국 Oasis Pro(2026-07-23 FINRA 판매 승인) [F-1462], 무기한선물 Ondo Perps(Ondo Global Group) [F-1967]',
     '인프라사: Ondo Network(주문 실행과 검증 층, 2026-07), LayerZero 브리지 연동 [on-0226 on-0209]'],
    ['기술회사란: 약관상 Ondo는 소프트웨어와 기술 제공자로서만 서비스를 함 [F-0525]. BVI 발행 법인의 토큰화 작업과 가격 계산 대행(Tokenizer)도 Ondo Finance Inc. [F-0193]',
     '(판단) 상품이 늘수록 역할이 발행에서 판매 시설, 인프라 순서로 위아래로 넓어지는 중',
     '2026-06-01 새 CEO 글: 토큰 발행 위로 거래, 프라임 브로커리지, 자산관리 층으로 올라가겠다고 함 [F-1468]',
     '(판단) 아예 손대지 않는 곳: 실물 자산 보관, 국채 직접 운용(펀드 매니저 역할), 미국 밖 2차 거래소 운영',
     ('Ondo Chain(옛 계획)은 어느 단의 일인가: 인프라 단. 상품을 기록하고 옮기는 장부(블록체인) 자체를 만들려던 계획', [
         '2025-02 자체 블록체인(L1) Ondo Chain 발표, 2025-07-14 블록체인 개발사 Strangelove 인수 발표 [on-0311 F-1943]',
         '2026-07-27 전통적 의미의 체인을 만들 필요가 없다며 Ondo Network로 바꿈 [ONM-004]',
         '(판단) 비유: 고속도로(L1 블록체인)를 직접 깔려다가, 남이 깐 도로(Ethereum, BNB Chain, Solana) 위에서 톨게이트와 검문소(실행과 검증)만 운영하기로 바꿈'])])

# ======================= S3 =======================
CUR_SEC[0] = 'S3'
g = [legend(LG4[:4]), '<div class="emap">',
     '<div class="ecol"><div class="ecap">재단 쪽(주인 없음)</div>',
     box('fd', 'Ondo Foundation', '케이맨 재단회사, 실질 소유자 없는 비영리. ONDO 토큰 발행 [F-1926]'),
     arrow('완전 자회사 [on-0009]'),
     box('fd', 'Flux Finance', '원래 Ondo가 만든 국채 담보대출(repo) 서비스, 재단에 팔림 [F-2191]'),
     arrow('90.01% 지분 [F-0186]'),
     '</div>',
     '<div class="ecol"><div class="ecap">회사 쪽(VC 주주가 있는 본사)</div>',
     box('co', 'Ondo Finance Inc.', '델라웨어 등기, 본사 코네티컷. 인가 없음. 토큰화 작업과 가격 계산(Tokenizer) [F-0193]'),
     arrow('9.99% 지분과 토큰화 기술 용역 [F-0186 F-0193]'),
     '</div>',
     '<div class="ecol"><div class="ecap">회사 쪽 미국 법인</div>',
     box('co', 'Ondo I LP(OUSG 발행 펀드)', '무한책임사원 단독 구성원이 Ondo Finance Inc. [F-0534]'),
     box('co', 'Ondo Capital Management LLC', 'SEC 등록 투자자문사, 2025-08-06 효력 [F-1152]'),
     box('co', 'Oasis Pro', '증권사, ATS, 명의개서대리인. 2025-10-07 인수 완료 [on-0490]'),
     box('co', 'Ondo Global Group', 'Ondo Perps 운영 [F-1967]'),
     '</div></div>',
     '<div class="emid">' + box('is', 'Ondo Global Markets (BVI) Limited(발행 법인)', 'BVI 회사, 2025-04-09 설립 [F-0185]. USDY, Ondo Stocks, Intelligent Portfolios를 찍음') + '</div>',
     '<div class="etp"><div class="ecap">제3자(계약 상대)</div><div class="tpl">' + ''.join(f'<span class="bx tp sm">{E(x)}</span>' for x in ['Ankura Trust(담보 대리)', 'Alpaca(증권사, 보관)', 'BitGo Trust(보관)', 'First Citizens Bank(예금)', '운용사 4곳(State Street와 Galaxy, BlackRock, Franklin Templeton, Fidelity)', 'Circle(USDC)', 'Coinbase(OUSG 현금 계좌)']) + '</div></div>']
sec('S3', '법인 지도',
    '회사 쪽(본사)과 재단 쪽(주인 없음)이 나뉘고, 미국 밖 상품을 찍는 발행 법인은 재단 쪽 90.01%, 본사 9.99%',
    ''.join(g),
    ['{ex}읽는 법: 화살표 글자가 지분율과 관계. 주황 줄을 따라 내려가면 발행 법인 다수 지분이 본사가 아니라 재단 쪽에 있음',
     '발행 법인은 따로 있음: 주주는 Flux Finance Inc. 90.01%, Ondo Finance Inc. 9.99%(2025-11-11 투자설명서) [F-0186]',
     '{ex}설립지 이름은 허가가 아님. 델라웨어, BVI(영국령 버진아일랜드), 케이맨제도는 회사를 등기한 곳(place of incorporation). 한국으로 치면 본점 소재지',
     'BVI 발행 법인은 BVI 금융감독청(Financial Services Commission)에 등록이나 인가를 받지 않았다고 회사가 밝힘 [F-0528]',
     '실제 금융 허가는 미국 쪽 둘: Ondo Capital Management의 SEC 투자자문 등록(2025-08-06) [F-1152], 인수한 Oasis Pro의 증권사, ATS, 명의개서대리인 등록 [F-0194]',
     '인수한 법인도 있음: Oasis Pro(2025-07-04 발표, 2025-10-07 완료, 금액 비공개) [F-1392 on-0490], 블록체인 개발사 Strangelove(2025-07-14 발표) [F-1943]'],
    [('Ondo I LP는 OUSG를 찍는 펀드 그 자체', [
        'OUSG 토큰 = 이 펀드의 지분. Rule 506(c) 사모 면제, 투자회사법 3(c)(7) 등록 면제 [F-1307]',
        '펀드를 굴리는 책임자(GP)는 따로 있음. 무한책임사원의 단독 구성원이 Ondo Finance Inc., 투자자문사가 Ondo Capital Management [F-0534]',
        '{ex}비유: 펀드 그릇(LP)과 운전사(GP). 돈을 대는 유한책임사원이 OUSG 보유자, 운전대는 Ondo 쪽']),
     ('운용사와는 어떤 계약인가', [
        'OUSG 펀드가 투자자로서 운용사 펀드 지분을 삼. 보유자가 넣은 USDC는 펀드의 Coinbase 계좌로 가고 그 돈으로 담는 펀드 지분을 삼 [ONM-010]',
        '(판단) 운용 위탁 계약이 아니라 펀드가 다른 펀드를 사는 관계. 그래서 Ondo는 국채 운용 인력 없이 큰 운용사 이름을 빌려 씀']),
     ('재단은 왜 이런 형태인가', [
        '{ex}케이맨 재단회사(foundation company): 주주가 없는 회사. 이사와 감독인이 정관대로 운영. 가상자산 재단이 토큰과 금고를 맡기려고 자주 쓰는 형태',
        'Ondo Foundation 업무 가운데 하나가 거버넌스 토큰 발행 [ONM2-004]',
        '(판단) 비유: 회사가 낸 포인트(ONDO)를 회사와 따로 선 공익 재단(foundation company)이 관리하는 모양. 토큰 판매와 회사 지분을 떼어 두려는 것']),
     ('9.99%는 왜(회사는 이유를 밝히지 않음)', [
        '(판단) 10%가 미국 법에서 자주 쓰이는 문턱이라 그 바로 밑에 맞춘 것으로 읽힘',
        '(판단) 세금: 미국 법인이 외국 회사 지분 10% 이상이면 미국 세법상 그 외국 회사의 미국 주주(U.S. shareholder)가 되어, 외국 회사 이익 일부를 미국에서 과세받을 수 있음(CFC 규정). 9.99%면 이 지위를 피함',
        '(판단) 사업: 본사가 발행 법인을 지배하지 않는 모양을 만들어, 발행 법인이 미국 회사의 자회사가 아니라 미국 밖 독립 법인으로 보이게 함(Regulation S 판매와 파산 절연에 유리)',
        '(판단) 100%가 아닌 이유: 100%면 발행 법인 이익과 위험이 본사 장부와 미국 규제, 세금 안으로 들어옴. 재단 쪽이 다수 지분을 쥐면 발행 법인 이익이 VC 주주가 아니라 재단 쪽에 쌓임',
        '(판단) 0%가 아닌 이유: 기술 용역 상대방으로서 정보와 경제적 연결을 남겨 두는 최소 지분',
        'USDY 이자 차이는 발행 법인 지분 보유자 몫이라고 회사가 밝힘(2024-01) [ONM-019]']),
     ('법인별 한 줄', [
        'Ondo USDY LLC: 원래 USDY 발행(미국 특수목적 법인, SPV). 2024-03-14 FinCEN 송금업자 등록. 2025-12-15부터 USDY는 BVI 법인 아래 [F-1927 F-1932 on-0327]',
        'Oasis Pro: 2009 등록 증권사, ATS, 명의개서대리인 일괄 [on-0490]. 그 자회사 Oasis Pro TA가 2026-07-02 미국 보관형 토큰(IVV, MU)을 발행 [F-1949]',
        'Ondo Capital Management: 2025-08-06 SEC 등록 효력. 그 전에는 면제보고 자문사(ERA) 지위 [F-1152]'])])

# ======================= S4 =======================
CUR_SEC[0] = 'S4'
R5 = [
    ('1', '펀드 그릇', 'Ondo I LP', '2023-01', '미국 큰손에게 국채 펀드 지분을 팔려면 회사와 분리된 펀드가 필요 [F-1307]', '자산운용사(본사)와 그 회사가 만든 펀드(Ondo I LP)는 별개 주머니(LP)', 'co'),
    ('2', '판매 대상', 'Ondo USDY LLC(2023-08) → BVI 발행 법인(2025-04-09 설립)', '2023-08, 2025-04', 'OUSG를 못 사는 미국 밖 개인과 기관용 상품을 따로 찍음 [F-1151 F-0185]', '국내 매장과 해외 직영 매장을 법인부터 따로 둠(offshore issuer)', 'is'),
    ('3', '파산 절연', 'BVI 발행 법인과 담보 대리인 Ankura', '2025-04~', '본사가 망해도 담보가 본사 채권자에게 안 넘어가게 함. 발행 법인은 파산 격리 특수목적 법인 [F-2172]', '담보부사채신탁의 수탁회사(collateral agent)', 'is'),
    ('4', '토큰 분리', 'Ondo Foundation', '2022~', 'ONDO 토큰은 재단이 발행, 회사 이익 권리 없음 [F-1926 ONM2-005]', '회사 포인트를 공익 재단이 관리(foundation company)', 'fd'),
    ('5', '인가', 'Oasis Pro 인수, Ondo Capital Management 등록', '2025', '미국 증권사, ATS, 명의개서대리인 인가를 한꺼번에 얻으려 인수 [F-1392 F-1152]', '증권사 라이선스(broker-dealer)를 새로 받는 대신 소형 증권사 인수', 'co'),
]
g = [legend([('co', '회사 쪽 법인'), ('is', '발행 법인'), ('fd', '재단 쪽')]), '<div class="r5">']
for n, why, who, when, body, ana, c in R5:
    g.append(f'<div class="rc {c}"><div class="rn">{n}</div><b>{E(why)}</b><div class="rw"><span>법인</span>{T(who)}</div><div class="rw"><span>생긴 때</span>{E(when)}</div><p class="f">{T(body)}</p><p class="jd">{T("(판단) 비유: " + ana)}</p></div>')
g.append('</div>')
sec('S4', '법인을 나눈 이유 5가지',
    '"법인 분리 = 인가 때문"은 5개 이유 가운데 1개에만 맞음',
    ''.join(g),
    ['{ex}읽는 법: 카드 순서가 생긴 순서. 인가 때문에 세운 법인은 5번뿐이고, 나머지는 펀드 그릇, 판매 대상, 파산 절연, 토큰 분리 때문',
     'BVI 발행 법인은 인가 때문에 세운 법인이 아님. BVI 감독청 등록이나 인가 없음 [F-0528]',
     '인가가 필요한 미국 사업은 회사째로 삼: Oasis Pro 2025-07-04 인수 발표, 2025-10-07 완료 [F-0194 on-0490]',
     '인수 완료 뒤 미국 투자자 판매 승인(FINRA)까지 약 9개월 반: 2026-07-23 승인 [F-1462]'],
    ['(판단) 인가를 언제 받을지 몰라 회사째로 산 선택. 새로 신청하면 기간이 길고 결과를 알 수 없음',
     '(판단) 분리 목적이 시점마다 다름: 2023 펀드 그릇과 판매 대상, 2025 파산 절연과 인가. 연혁은 S10 법인과 인가 레인']))

# ======================= S5 =======================
CUR_SEC[0] = 'S5'
g = [legend([('is', '금고 주인(발행 법인)'), ('co', '금고 주인(회사 쪽 펀드)'), ('tp', '제3자')]), '<div class="vault">',
     box('is', '1. 금고 주인', 'BVI 발행 법인(USDY, Ondo Stocks, 포트폴리오) 또는 Ondo I LP(OUSG). 자산은 발행 법인 명의 [on-0055]'),
     box('tp', '2. 금고지기(보관기관)', '주식: Alpaca, BitGo Trust [on-0055]. USDY 국채: Morgan Stanley 계좌(2024-05 문서) [ONM-007]. 예금: First Citizens Bank [ONM-008]'),
     box('tp', '3. 열쇠 하나 더(담보 대리인)', 'Ankura Trust. 보유자 대신 1순위 담보권을 쥠 [on-0056]'),
     box('pr', '4. 토큰 보유자', '금고 물건의 주인이 아니라 돌려받을 권리를 가짐. 기초자산 인도 청구 불가 [F-0188]'),
     '</div>']
sec('S5', '금고는 누구 금고인가',
    '금고 주인은 토큰을 찍은 법인. 보유자는 금고 물건의 주인이 아니라 돌려받을 권리를 가짐',
    ''.join(g),
    ['{ex}읽는 법: 네 칸은 금고 주인, 금고지기, 열쇠 하나 더, 보유자 순서. 보유자 칸만 초록(상품을 든 사람)',
     'OUSG 보유자: 펀드 지분권자. 그 펀드(Ondo I LP)가 금고 주인 [F-1307]',
     'USDY, Ondo Stocks 보유자: 발행 법인에 대한 채권자. Ankura가 보유자 대신 1순위 담보권을 쥠 [on-0056 F-0512]',
     '돌려받을 곳은 담보와 추가 담보뿐(limited recourse). 발행 법인 도산 위험을 보유자가 짐 [F-0188]',
     '(판단) 비유: 담보부사채신탁 구조. 사채권자(토큰 보유자)는 회사 재산 주인이 아니지만 수탁회사(collateral agent, Ankura)가 담보를 쥐고 지켜 줌'],
    ['Ankura가 하는 일: 검증 대리인(Verification Agent)이자 담보 대리인(Collateral Agent)으로 USDY 보유자를 보호한다고 회사가 밝힘 [F-0512]',
     'USDY 담보율 156.90%(2026-11-16 화면): 기초자산 24.2억 달러, 유통 USDY 19.7억 달러 [F-1933]',
     '토큰 보유 기록은 발행 법인(SPV)이 관리. 주식 발행 기업 동의 없이 만든 토큰이라 애플, 테슬라와 보유자 사이에 권리 관계 없음 [on-0160]',
     'Flux Finance가 Ondo Stocks 보유자에 대한 채무를 더 담보하려고 자금을 보증 [on-0010]'])

# ======================= S6 =======================
CUR_SEC[0] = 'S6'


def flow(title, cls, steps):
    h = [f'<div class="fl"><div class="flh">{chip(title)}</div>']
    for i, (c, t, d) in enumerate(steps):
        if i:
            h.append('<div class="fla" aria-hidden="true">↓</div>')
        h.append(f'<div class="bx {c}"><b>{T(t)}</b><span>{T(d)}</span></div>')
    h.append('</div>')
    return ''.join(h)


g = [legend([('na', '투자자'), ('co', '회사 쪽'), ('is', '발행 법인'), ('tp', '제3자')]), '<div class="flows">',
     flow('OUSG: 1,000만 원', 'co', [
         ('na', '투자자(적격투자자이자 적격매수자)', '1,000만 원 ≈ 7,000 USDC(1달러 = 약 1,430원)'),
         ('co', 'Ondo I LP가 OUSG 7,000달러어치 발행', 'USDC는 펀드의 Coinbase 계좌로 감 [ONM-010]'),
         ('tp', '펀드가 운용사 펀드 지분을 삼', '2026-11-18 비중대로면 SWEEP 약 3,400, BUIDL 약 2,290, BENJI 약 710, FYOXX 약 530, USDC 약 80달러'),
         ('na', '1년 뒤(가상 연 4%)', '이자 약 280달러로 OUSG 약 7,280달러어치. 보수 0.15%(약 10.5달러)는 면제라 0 [F-1313]'),
         ('co', '즉시 상환', '24시간 USDC로. 한도 24시간 전체 5,000만, 1인 2,500만 달러 [on-0350]')]),
     flow('USDY: 1,000달러', 'is', [
         ('na', '미국 밖 투자자, 신원 확인(KYC)', '1,000달러 = 약 143만 원'),
         ('is', 'BVI 발행 법인이 USDY 발행', '국채와 SHVon을 사서 금고에 둠 [on-0335]'),
         ('tp', '금고 구성(2026-11-13)', '국채 82.73%, SHVon 17.24% [on-0335]'),
         ('na', '1년 이자(2026-11-16 화면 기준)', '담보 4.10% = 41달러, 보유자 3.75% = 37.5달러, 차이 3.5달러 [F-1934]'),
         ('tp', 'Ankura Trust', '검증과 담보 대리 [F-0512]')]),
     flow('Ondo Stocks: AAPLon 1,000달러', 'is', [
         ('na', '미국 밖 투자자가 판매 창구에서 주문', 'Bitget, Binance 아부다비 거래장, 지갑. 체결은 거래소 장부 안 [F-1457 F-1455]'),
         ('tp', '1차 매수자(거래소, 시장조성자)', '토큰이 모자라면 발행 법인에 스테이블코인을 내고 새 토큰을 받음 [F-1953]'),
         ('is', '발행 법인이 실제 주식을 삼', 'Alpaca에서 사서 Alpaca, BitGo Trust 담보 계좌에 둠. Ankura 1순위 담보권 [on-0055 on-0056]'),
         ('na', '보유자', '값과 배당만 따라감. 거래 시간 일요일 밤 8시~금요일 밤 8시(미국 동부) [on-0083]'),
         ('is', '상환', '1만 달러 상환 시 수수료 5달러(0.05%)와 견적가 차이 [F-0545]')]),
     flow('Intelligent Portfolios', 'is', [
         ('na', '투자자', '포트폴리오 토큰 1개를 받음 [on-0364]'),
         ('is', '토큰 안', 'Ondo Stocks 바구니(BlackRock 전략) [on-0364]'),
         ('tp', '바구니 속 종목', '종목마다 위 Ondo Stocks 금고 구조 그대로(판단)')]),
     '</div>']
sec('S6', '상품별 돈 흐름(가상 숫자)',
    '네 상품 모두 "돈 → 발행 법인 → 실제 자산 → 토큰"의 같은 뼈대. 다른 점은 금고에 무엇이 들고 누가 지키느냐',
    ''.join(g),
    ['{ex}읽는 법: 위에서 아래로 돈이 움직이는 순서. 금액은 가상 숫자, 비율과 한도는 회사 화면 값. 환율 1달러 = 약 1,430원',
     '스테이블코인을 중간에 주기적으로 떼어 가나: 아님. OUSG는 손님 USDC로 토큰을 먼저 찍어 주고, 회사가 주기적으로 그 USDC를 달러로 바꿔 BUIDL 등에 넣음 [ONM2-008]',
     'USDY도 손님 돈을 받은 뒤 사는 순서. 바로 국채에 못 넣는 돈은 은행 예금으로 두고 다음 영업일에 투자(2024-05 문서) [ONM2-013]',
     'Ondo Stocks 수수료: 발행 0, 상환마다 0.05% [F-0545]. 견적은 약 30초 보장 [ONM-005]'],
    [('Coinbase는 어디 끼나', [
        '투자자: Coinbase Ventures가 2022-04 시리즈 A 참여 [F-1920]',
        '보관: OUSG가 받은 USDC는 펀드의 Coinbase 계좌로 감. 2026-11-17 OUSG 안 USDC 몫 약 357만 달러(1.14%) [ONM-010 ONM-011]',
        'USDY 초기 문서(2024-05)에서도 거래 상대 목록에 Coinbase가 있음 [ONM-007]']),
     'Circle USDC 지원이 멈추면 OUSG 즉시 상환도 제한 [on-0350]',
     'USDY는 가격이 오르는 판(USDY)과 1달러 고정에 토큰 수가 느는 판(rUSDY)이 있음. 예: 가격이 1.00에서 1.01달러로 오르면 rUSDY 100개가 101개 [ONM2-011]'])

# ======================= S7 =======================
CUR_SEC[0] = 'S7'
NOW = [('SWEEP', 48.58), ('BUIDL', 32.69), ('BENJI', 10.12), ('FYOXX', 7.54), ('USDC', 1.14)]
TP_SHADES = ['tp1', 'tp2', 'tp3', 'tp4', 'tp5']


def stackbar(vals, label):
    h = [f'<div class="sbrow"><div class="sbl">{E(label)}</div><div class="sb">']
    for (n, v), c in zip(vals, TP_SHADES):
        h.append(f'<div class="sbs {c}" style="width:{v}%" title="{E(n)} {v}%"><span>{E(n) if v > 6 else ""}</span></div>')
    h.append('</div></div>')
    return ''.join(h)


g = [legend([('tp', '운용사 펀드(제3자)'), ('pr', 'OUSG')]),
     '<h4 class="fh">(1) 지금 비중(2026-11-18 OUSG 화면)</h4>',
     '<div class="hb">' + ''.join(f'<div class="hbr"><span class="hbn">{E(n)}</span><div class="hbt"><div class="hbf {c}" style="width:{v / 50 * 100:.1f}%"></div></div><span class="hbv">{v}%</span></div>' for (n, v), c in zip(NOW, TP_SHADES)) + '</div>',
     f'<p class="cap f">출처 {T("[S-ousg-page]")}</p>',
     '<h4 class="fh">(2) 펀드 4개 비교</h4>']
cmp_rows = [('운용사', ['State Street, Galaxy', 'BlackRock', 'Franklin Templeton', 'Fidelity']),
            ('출시', ['2026-05', '2024-03', '2021', '2025-09']),
            ('그릇', ['사모 펀드', '사모 펀드(BVI)', '미국 공모 등록 펀드', '미국 등록 펀드의 한 클래스']),
            ('누가 사나', ['적격매수자', '적격매수자, 500만 달러부터', '개인도 가능(Benji 앱)', '기관, 100만 달러부터']),
            ('블록체인 장부', ['토큰', '토큰(명부는 Securitize)', '블록체인 연동 공식 기록', '공식 장부는 기존 전산, 블록체인은 매일 맞추는 사본']),
            ('입출금', ['PYUSD', 'USDC 등', '앱과 지갑', '이더리움']),
            ('OUSG 비중(2026-11-18)', ['48.58%', '32.69%', '10.12%', '7.54%']),
            ('Ondo와 관계', ['OUSG가 선도 앵커 투자자, 약 2억 달러', '개인이 못 사는 펀드를 OUSG가 대신 삼', '분산 대상', 'FDIT 출시 때 OUSG가 유일한 앵커, FDIT 자산의 99% 이상'])]
funds = ['SWEEP', 'BUIDL', 'BENJI', 'FYOXX']
g.append('<div class="ct">')
for j, fnm in enumerate(funds):
    g.append(f'<div class="ctc"><div class="cth"><span class="chip tpc">{fnm}</span></div><dl>')
    for k, vs in cmp_rows:
        g.append(f'<dt>{E(k)}</dt><dd>{T(vs[j])}</dd>')
    g.append('</dl></div>')
g.append('</div>')
g.append(f'<p class="cap f">비교표 출처 {T("[S-sweep-theblock S-sweep-yahoo S-buidl-eco S-benji-ft S-benji-bw S-fyoxx-defillama S-fyoxx-blockhead S-fdit-coinchapter]")}</p>')
g.append('<h4 class="fh">(3) 구성 변화(구성을 밝힌 시점만, 시점 사이는 잇지 않음)</h4><div class="tl7">')
pts = [('2023-01', '출시. BlackRock 단기 국채 ETF(SHV) 중심', '[S-ousg-eco]'),
       ('2024-03-27', 'OUSG 자산의 상당 부분을 BUIDL로 옮긴다고 발표(비율 없음)', '[ONM2-007]'),
       ('2024-08-28', '준비자산 대부분을 BUIDL로. USDC 즉시 발행과 상환 연결', '[ONM2-008 on-0333]'),
       ('2025-04-14', 'BUIDL에는 일부만, 여러 담보로 분산했다고 씀', '[ONM2-009]'),
       ('2025-09', 'BUIDL, Fidelity FDIT, Franklin BENJI, WisdomTree WTGXX, Wellington과 FundBridge의 ULTRA(비중 없음)', '[S-fdit-marketsmedia]')]
for d, t, s in pts:
    g.append(f'<div class="t7"><span class="t7d">{d}</span><span class="t7t f">{T(t + " " + s)}</span></div>')
g.append('</div>')
g.append(stackbar([('SWEEP', 48.57), ('BUIDL', 32.69), ('BENJI', 10.13), ('FYOXX', 7.56), ('USDC', 0.99)], '2026-11-13'))
g.append(stackbar(NOW, '2026-11-18'))
g.append(f'<p class="cap f">2026-11-13 {T("[on-0331]")}, 2026-11-18 {T("[S-ousg-page]")}. 2026-05 BUIDL 18%(신뢰도 낮은 시드)는 같은 시점 공시를 못 찾아 뺌</p>')
sec('S7', 'OUSG가 담은 펀드 4개',
    '네 펀드 모두 단기 국채형 MMF. 차이는 그릇(공모와 사모), 장부(블록체인이 원본인지 사본인지), 입출금 통로',
    ''.join(g),
    ['{ex}읽는 법: (1)은 지금 비중, (2)는 펀드마다 무엇이 다른지, (3)은 구성을 밝힌 날만 찍은 변화',
     '{ex}MMF(머니마켓펀드): 아주 짧은 국채, 현금, 레포를 담아 원금이 거의 흔들리지 않는 펀드. 레포는 국채를 담보로 하루 이틀 돈을 빌려주는 거래',
     'OUSG 총자산 3.13억 달러(2026-11-13) [on-0331]',
     '(판단) 비유: 넷 다 같은 쌀(단기 국채)이 든 쌀통(MMF). 다른 점은 통 재질(공모 registered fund, 사모 private fund), 장부가 원본인지 사본인지, 쌀 넣고 빼는 구멍(USDC, PYUSD)'],
    ['펀드마다 24시간 바로 꺼낼 수 있는 돈에 한도가 있어 여러 펀드에 나눠 담는다고 당시 CEO Allman이 설명 [S-sweep-theblock]',
     '2025-03-27 Circle의 BUIDL 즉시 상환 창구(보통 최대 2천만 USDC)가 23시간 막혔을 때 다른 창구로 상환을 이어 감 [ONM2-009]',
     '(판단) 비유: ATM 한 대는 하루 인출 한도가 있으니 여러 은행 ATM을 묶어 씀',
     '(판단) 절반 가까이가 펀드 한 곳(SWEEP)에 쏠림. 구성 공시 주기를 봐야 하는 이유 [on-0392]'.replace('(판단) 절반', '절반'),
     'BUIDL 자산 수탁은 The Bank of New York Mellon, Securitize는 명의개서대리인(2024-05 문서) [ONM2-010]'])

# ======================= S8 =======================
CUR_SEC[0] = 'S8'
FEES = list(csv.DictReader(open(PKG / 'data_보강/defillama_보유자이자_분기.csv', encoding='utf-8-sig')))
VOL = list(csv.DictReader(open(PKG / 'data_보강/defillama_OndoStocks_매매액_분기.csv', encoding='utf-8-sig')))


def vbars(rows, key, unit, fmt, partial, cls='tpv', h=220, w=560):
    vals = [float(r[key]) for r in rows]
    mx = max(vals) * 1.15
    n = len(rows)
    bw = (w - 40) / n
    out = [f'<svg class="ch" viewBox="0 0 {w} {h + 50}" role="img" aria-label="분기별 막대">']
    for i in range(5):
        y = 10 + h - h * i / 4
        out.append(f'<line x1="30" x2="{w}" y1="{y:.1f}" y2="{y:.1f}" class="gl"/>')
    for i, (r, v) in enumerate(zip(rows, vals)):
        x = 36 + i * bw
        bh = h * v / mx
        p = partial(r)
        out.append(f'<rect x="{x:.1f}" y="{10 + h - bh:.1f}" width="{bw - 12:.1f}" height="{bh:.1f}" rx="3" class="{cls}{" part" if p else ""}"/>')
        out.append(f'<text x="{x + (bw - 12) / 2:.1f}" y="{10 + h - bh - 6:.1f}" class="vl">{fmt(v)}</text>')
        out.append(f'<text x="{x + (bw - 12) / 2:.1f}" y="{h + 30:.1f}" class="xl">{r["분기"].replace("-", " ")}</text>')
        if p:
            out.append(f'<text x="{x + (bw - 12) / 2:.1f}" y="{h + 46:.1f}" class="xl sm">진행 중</text>')
    out.append('</svg>')
    return ''.join(out)


fees_chart = vbars(FEES, '보유자이자_fees_백만달러', '백만 달러', lambda v: f'{v:.1f}', lambda r: r['완결분기'] != '예')
vol_chart = vbars(VOL, '매매액_백만달러', '백만 달러', lambda v: f'{v / 1000:.2f}', lambda r: r['분기'] in ('2025-Q3', '2026-Q4'), cls='prv')


def mech(title, rows):
    mx = max(v for _, v, _ in rows) or 1
    h = [f'<div class="mc"><div class="mch">{chip(title)}</div>']
    for lab, v, c in rows:
        h.append(f'<div class="mcr"><span class="mcl">{E(lab)}</span><div class="mct"><div class="mcf {c}" style="width:{max(v / mx * 100, 1.5):.1f}%"></div></div><span class="mcv">{v:g}</span></div>')
    h.append('</div>')
    return ''.join(h)


g = [legend([('is', '발행 법인에 남는 몫'), ('tp', '받는 돈과 주는 돈'), ('jdc', '추정(판단)')]),
     '<h4 class="fh">(1) 이익 원리: 받는 돈 → 주는 돈 → 남는 몫(보유자 돈 100달러 기준, 연)</h4><div class="mcs">',
     mech('USDY', [('담보 이자 4.10%', 4.10, 'tp'), ('보유자 지급 3.75%', 3.75, 'tp'), ('남는 몫 0.35', 0.35, 'is')]),
     mech('Ondo Stocks(1만 달러 상환 1회)', [('상환 금액 10,000', 10000, 'tp'), ('수수료 0.05% = 5', 5, 'is')]),
     mech('OUSG', [('운용보수 0.15%', 0.15, 'tp'), ('면제로 지금 0', 0, 'is')]),
     '</div>',
     f'<p class="cap f">USDY {T("[F-1934 on-0335]")}, Ondo Stocks {T("[F-0545]")}, OUSG {T("[F-1313]")}. 포트폴리오 연 서비스 수수료는 율을 밝히지 않아 그림에서 뺌 {T("[F-1956]")}</p>',
     '<h4 class="fh">(2) USDY, OUSG 보유자가 받은 이자(분기, 백만 달러, DefiLlama fees)</h4>', fees_chart,
     f'<p class="cap f">DefiLlama 정의: fees = USDY, OUSG 보유자가 번 이자(토큰 가격 상승 × 유통 수량), revenue(프로토콜 수입) = 0, holders revenue 항목 없음. 즉 이 막대는 Ondo 매출이 아님 {T("[DL-fees DL-rev]")}. 기준일 2026-11-17, 2025 Q2는 2025-04-11부터, 2026 Q4는 진행 중(흐린 막대)</p>',
     '<h4 class="fh">(3) 상품별 이익 추정(전부 판단, 회색)</h4><div class="est jdbox">',
     '<p class="jd">(판단) USDY 이자 차이: 계산 1 = 유통 USDY 19.7억 × (4.10% − 3.75%) ≈ 연 690만 달러. 계산 2 = 담보 24.16억 × 4.10% − 19.7억 × 3.75% ≈ 연 2,518만 달러(초과 담보분 이자까지)</p>',
     '<p class="jd">(판단) Ondo Stocks 상환 수수료: 최근 1년 매매액 92.7억 달러 가운데 절반이 상환이라고 가정하면 46.3억 × 0.05% ≈ 연 232만 달러. 견적가 차이 수입은 공개 값이 없어 뺌</p>',
     '<p class="jd">(판단) OUSG: 0(면제). 면제가 끝나면 잔액 3.1억 × 0.15% ≈ 연 47만 달러</p>',
     '<p class="jd">(판단) 그래서 확인 가능한 몫 가운데서는 USDY 이자 차이가 가장 큼. 이 돈은 BVI 발행 법인(재단 쪽 90.01%)에 먼저 쌓임</p>',
     f'<p class="cap f">매매액 {T("[DL-vol]")}, USDY 숫자 {T("[F-1933]")}</p></div>']
sec('S8', '뭘로 돈 버나(이익 원리와 비중)',
    '돈은 발행과 상환 단계에서 생김. 지금 실제로 남는 곳은 USDY 이자 차이와 Ondo Stocks 수수료. 그 돈은 재단 쪽이 90.01%를 가진 발행 법인에 먼저 쌓임',
    ''.join(g),
    ['{ex}읽는 법: (1)은 원리, (2)는 보유자가 받은 이자의 크기(Ondo 매출 아님), (3)은 이익 비중 어림',
     '발행 자체에서 오는 이득은 있음. Ondo 수입은 전부 발행과 상환 층에서 나옴: USDY 이자 차이 [ONM-019], Ondo Stocks 상환 수수료 0.05%와 견적가 차이 [F-0545], 포트폴리오 연 서비스 수수료 [F-1956], OUSG 운용보수 0.15%(2027-01-01까지 면제) [F-1313]',
     '{ex}이자 차이(spread)는 은행 예대마진과 같은 원리. 예: 보유자 돈 100달러로 산 국채에서 4.10달러가 나와 보유자에게 3.75달러를 주면 0.35달러가 발행 쪽에 남음',
     '회사 매출, 이익, 흑자 여부는 공개된 적 없음 [F-1326]',
     'USDY, OUSG 보유자가 최근 1년 받은 이자 합계 약 6,649만 달러(DefiLlama, 2026-11-17까지) [DL-fees]',
     '본사로 오는 확인된 통로는 둘: 토큰화 기술 용역(Tokenizer) [F-0193], 발행 법인 9.99% 지분 [F-0186]. 금액 공시 없음'],
    ['USDY 금리는 Ondo Finance가 매달 미리 정함. 출시 때 기초 5.1%, 지급 5.0% 수준 [F-1929]',
     '약 3% 손실 완충분(first loss)을 Ondo Finance가 일부 댐. 그 대가도 이자 차이에 들어감 [F-1928]',
     'USDY 이자 차이 추이: 2026-08 지급 3.55%, 담보 만기수익률 3.76% [S-defillama-rwa-ondo]. 2026-11-16 지급 3.75%, 담보 4.10% [F-1934]',
     '(판단) 만기수익률은 실제로 받은 이자와 다른 지표라 계산 값은 크기 감만 잡는 용도',
     '시드 표의 분기 Gross Protocol Revenue(2025 Q2 1,112만 ~ 2026 Q3 2,006만 달러)는 DefiLlama fees와 같은 값. 즉 보유자 이자이고 Ondo 매출이 아님 [DL-fees]'])

# ======================= S9 =======================
CUR_SEC[0] = 'S9'
SZ = [r for r in csv.DictReader(open(PKG / 'data_보강/상품잔액_차트값.csv', encoding='utf-8-sig')) if r['차트'] == '씀']


def dnum(d):
    y, m = int(d[:4]), int(d[5:7])
    dd = int(d[8:10]) if len(d) >= 10 and d[8:10].isdigit() else 15
    return y + (m - 1) / 12 + (dd - 1) / 365


def linechart(series, w=560, h=260):
    x0, x1 = 2024.0, 2027.0
    mx = 25
    X = lambda t: 40 + (t - x0) / (x1 - x0) * (w - 110)
    Y = lambda v: 10 + h - v / mx * h
    o = [f'<svg class="ch" viewBox="0 0 {w} {h + 40}" role="img" aria-label="상품별 잔액 선 그래프">']
    for v in (0, 5, 10, 15, 20, 25):
        o.append(f'<line x1="40" x2="{w - 70}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="gl"/><text x="34" y="{Y(v) + 5:.1f}" class="yl">{v}</text>')
    for yr in (2024, 2025, 2026):
        o.append(f'<text x="{X(yr + 0.5):.1f}" y="{h + 32}" class="xl">{yr}</text><line x1="{X(yr):.1f}" x2="{X(yr):.1f}" y1="10" y2="{h + 10}" class="gl v"/>')
    for name, cls, pts in series:
        pts = sorted(pts)
        d = ' '.join(f'{"M" if i == 0 else "L"}{X(t):.1f},{Y(v):.1f}' for i, (t, v) in enumerate(pts))
        o.append(f'<path d="{d}" class="ln {cls}"/>')
        for t, v in pts:
            o.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="4.5" class="pt {cls}"/>')
        t, v = pts[-1]
        o.append(f'<text x="{X(t) + 8:.1f}" y="{Y(v) + 5:.1f}" class="dl {cls}">{E(name)} {v:g}</text>')
    o.append('</svg>')
    return ''.join(o)


ser = []
for name, cls in [('USDY', 's1'), ('Ondo Stocks', 's2'), ('OUSG', 's3')]:
    ser.append((name, cls, [(dnum(r['기준일']), float(r['잔액_억달러'])) for r in SZ if r['상품'] == name]))
srcs9 = ' '.join(sorted({r['출처'] for r in SZ}))

g = [legend([('pr', '상품(초록 진하기로 구분, 선 끝에 이름)'), ('tp', '경쟁사와 시장')]),
     '<h4 class="fh">(1) 상품별 잔액(억 달러, 시점별 공개 값만 이음)</h4>', linechart(ser),
     f'<p class="cap f">출처 {T("[" + srcs9 + "]")}. 지표가 TVL, 시가총액, 회사 발표 예치로 섞여 있어 선은 흐름만 보는 용도. 신뢰도 낮은 시드 6개는 같은 시점 1~3순위 값을 못 찾아 뺌(data_보강/상품잔액_차트값.csv)</p>',
     '<h4 class="fh">(2) 토큰화 주식 잔액과 점유율(rwa.xyz)</h4>',
     '<div class="ms"><div class="msc"><span class="msd">2026-01 초</span><div class="msb"><div class="msf s2" style="width:30.4%"></div></div><span class="msv">4.13억 달러, 51.59%, 1위</span></div>',
     '<div class="msc"><span class="msd">2026-11-16</span><div class="msb"><div class="msf s2" style="width:66.1%"></div></div><span class="msv">8.99억 달러, 24.23%, 2위</span></div>',
     '<div class="msc"><span class="msd">2026-11-16 1위</span><div class="msb"><div class="msf tp" style="width:100%"></div></div><span class="msv">Binance 13.6억 달러, 36.62%</span></div></div>',
     f'<p class="cap f">출처 {T("[on-0154 on-0272]")}. 막대 길이는 잔액(13.6억 = 100)</p>',
     '<h4 class="fh">(3) Ondo Stocks 사고팔기 금액(분기, 십억 달러, DefiLlama)</h4>', vol_chart,
     f'<p class="cap f">DefiLlama 정의: Ondo Global Markets(Ondo Stocks) 사고팔기 금액. 이더리움, BNB 체인 체결 이벤트와 솔라나 발행, 상환 매매를 더함 {T("[DL-vol]")}. 2025 Q3는 2025-09-01부터, 2026 Q4는 2026-11-16까지(흐린 막대). DefiLlama API의 TVL 배열은 비어 있어 잔액 선에는 못 씀 {T("[DL-proto]")}</p>',
     '<div class="defcard"><b>잔액이 뭔가</b><p class="x">잔액(발행 잔액, outstanding) = 지금 시중에 남아 있는 토큰 수 × 토큰 가격. 고객이 맡겨 둔 돈의 현재 크기</p><p class="x">비유: 은행 예금 잔액(outstanding). 하루 동안 오간 돈(거래량)이 아니라 지금 통장에 남은 돈</p><p class="x">늘어나는 이유는 새 발행과 가격 상승, 줄어드는 이유는 상환과 가격 하락. 매출이 아님. 잔액에 이자 차이나 수수료율을 곱해야 수입이 나옴</p></div>']
sec('S9', '상품 크기와 점유율 변화',
    'USDY는 꾸준히 커져 최대 상품, Ondo Stocks는 출시 14개월 만에 2위 상품, OUSG는 1년 새 60% 줄어듦',
    ''.join(g),
    ['{ex}읽는 법: (1) 선이 오를수록 맡긴 돈이 늘어난 것. (2) 막대는 잔액, 글자는 점유율. (3) 막대는 사고판 금액(잔액과 다른 지표)',
     '{ex}TVL(total value locked)은 가상자산 업계에서 잔액과 거의 같은 뜻으로 씀. 점유율은 같은 종류 상품 전체 잔액 가운데 Ondo 몫',
     'OUSG: 2025-11 7.8억 달러 이상에서 2026-11-17 3.1억 달러로 약 60% 줄어듦 [F-1941 F-1666]',
     '토큰화 주식: 잔액은 4.13억에서 8.99억 달러로 늘었고 점유율만 51.59%에서 24.23%로 내려감(2026-01 초 → 2026-11-16) [on-0154 on-0272]',
     '국채 토큰 플랫폼: 2026-11-16 Ondo 32억 달러 2위, 1위 Franklin Benji 33억 달러 [on-0273]',
     '보유자: 2026-08-15 전체 200,645명, 그중 Ondo Stocks 186,636명 [on-0470]'],
    ['회사 발표 상품 전체 규모: 2024-01 2.25억 달러 이상 [F-1660], 2025-07 14억 달러 이상 [F-1944], 2026-11-17 약 41억 달러 [F-1666]',
     'USDY 발행 잔액 19.7억, 기초자산 24.2억 달러(2026-11-13 USDY 화면). 홈페이지 23.8억 달러와 집계 기준이 다름 [on-0335 F-1666]',
     '(판단) Ondo 국채 32억에는 USDY가 담은 SHVon 약 4.17억 달러가 두 번 잡힘. 빼면 약 28억 달러 [ONM-008]',
     '회사 홈페이지(Ondo Stocks 14.4억)와 rwa.xyz(8.99억)는 집계 기준이 다름 [F-1666 on-0272]',
     'Binance 자기 발행 토큰 bStocks는 출시 약 4개월 만에 운용자산 10억 달러를 넘었다고 Binance가 발표(2026-10) [F-1546]',
     'Ondo Stocks 2025년 누적 거래량 20억 달러, 한 달 최대 10억 달러 초과(회사 결산) [F-1325]'])

# ======================= S10 =======================
CUR_SEC[0] = 'S10'
TL = list(csv.DictReader(open(PKG / 'data/timeline_lanes.csv', encoding='utf-8-sig')))
FIX = {'Ondo Global Markets → Ondo Stocks': dict(날짜='2025-12', 내용='2025 결산 글부터 새 이름. 발행 법인 이름에 옛 이름이 남음', 출처='F-1665 on-0406'),
       'Ondo Chain 철회 → Ondo Network': dict(날짜='2026-07-27', 출처='ONM-004 on-0226'),
       'Ondo Chain → Ondo Network': dict(날짜='2026-07-27', 출처='ONM-004'),
       'Ondo Vaults 출시': dict(날짜='2021-07', 출처='F-1442'),
       '시드 400만 달러': dict(출처='F-1212'),
       '시리즈 A 2,000만 달러': dict(날짜='2022-04', 출처='F-1207 F-1920'),
       'ONDO 토큰 판매': dict(출처='F-1922'),
       '국채 토큰으로 방향 전환': dict(날짜='2022', 내용='2022 DeFi 수익이 줄어 금고를 접고 2023-01 국채 토큰으로', 왜='이자를 못 받는 스테이블코인 1,000억 달러 이상 보유자를 국채로 끌어오려고(회사)', 출처='ONM-001 F-1443'),
       'OUSG 출시': dict(출처='F-1443 S-ousg-eco'),
       'Ondo I LP 펀드, Ondo Capital Management 자문 시작': dict(내용='Rule 506(c), 3(c)(7) 면제. 자문은 면제보고 지위', 출처='F-1307 F-1152'),
       'USDY 발표': dict(출처='F-1151 F-1929'),
       'Ondo USDY LLC가 USDY 발행': dict(출처='F-1927 F-1932'),
       '주식 토큰 첫 계획': dict(출처='F-1660'),
       '주식 토큰 설계 변경': dict(출처='F-1449 F-1450'),
       'Ondo Global Markets (BVI) Limited 설립': dict(날짜='2025-04-09', 출처='F-0185 F-0528'),
       'Oasis Pro 인수 발표': dict(출처='F-0194'),
       'Strangelove 인수 발표': dict(출처='F-1943'),
       'Ondo Capital Management SEC 등록 효력': dict(출처='F-1152'),
       'Fidelity FDIT 앵커': dict(출처='S-fdit-coinchapter'),
       'BVI 상품 SEC 증권신고서 비공개 제출': dict(출처='F-1460'),
       'Binance 운영 아부다비 ADGM 거래소 상장': dict(출처='F-1457'),
       'Bitget 거래소 현물 시장 진입': dict(출처='F-1455'),
       'Binance 자체 주식 토큰 bStocks 출시': dict(날짜='2026-06', 출처='F-1546 on-0272'),
       'Ondo Perps 출시': dict(출처='F-1967'),
       '미국 안 보관형 토큰 IVV, MU': dict(출처='F-1128 F-1949'),
       'FINRA 승인: 미국 투자자 판매': dict(출처='F-1462'),
       'USDY가 Ondo Stocks 우산 아래로': dict(내용='회사 문서 표현: USDY가 Ondo Stocks 우산 아래로 합쳐짐', 출처='ONM-009'),
       'SWEEP 출시, OUSG 앵커 약 2억 달러': dict(날짜='2026-05-05'),
       }
LANES = ['상품', '법인과 인가', '판매 지역과 창구', '인프라와 기술', '이름과 브랜드', '경영과 자금']
LCLS = {'상품': 'pr', '법인과 인가': 'co', '판매 지역과 창구': 'tp', '인프라와 기술': 'co', '이름과 브랜드': 'na', '경영과 자금': 'co'}
ev = []
for r in TL:
    r = dict(r)
    f = FIX.get(r['제목'], {})
    r.update(f)
    if r['출처'] == 'OV' and not f:
        WARN.append('S10 OV만: ' + r['제목'])
        continue
    r['내용'] = r['내용'].replace(' 바뀐 날짜는 Ondo 블로그에서 확인해 채울 것', '')
    r['왜'] = r['왜'].replace('(판단)', '')
    ev.append(r)
ev.append(dict(날짜='2026-11-18', 레인='판매 지역과 창구', 방식='현재', 제목='Oasis Pro 대체거래시스템 거래 기록 없음', 내용='회사 블로그 2026-10~11 새 글과 FINRA ATS 주간 자료(2026-10)에 Oasis Pro 거래 기록이 없음', 왜='', 출처='ONM2-001 ONM2-002'))


def yr(d):
    return int(d[:4])


YEARS = [2021, 2022, 2023, 2024, 2025, 2026]
g = [legend([('pr', '상품'), ('co', '회사 쪽 법인, 기술, 자금'), ('tp', '판매 창구와 제3자'), ('na', '이름')]),
     '<p class="cap x">점을 누르면 왜, 어떻게가 펼쳐짐. 칩은 방식(직접, 제휴, 인수 등)</p><div class="tlw"><div class="tlg">']
g.append('<div class="tlc tlhd"></div>' + ''.join(f'<div class="tlc tlhd tly">{y}</div>' for y in YEARS))
for ln in LANES:
    g.append(f'<div class="tlc tll">{E(ln)}</div>')
    for y in YEARS:
        items = [r for r in ev if r['레인'] == ln and yr(r['날짜']) == y]
        items.sort(key=lambda r: r['날짜'])
        cell = [f'<div class="tlc tlcell" data-y="{y}" data-l="{E(ln)}">']
        for r in items:
            why = f'<p class="x">왜: {T(r["왜"], False)}</p>' if r['왜'] else ''
            jd_why = ''
            if r['제목'] == 'Ondo Vaults 출시':
                why = '<p class="jd">(판단) 현실 자산을 담지 않아 맡아 둘 법인이 필요 없었음</p>'
            cell.append(f'<details class="ev {LCLS[ln]}"><summary><span class="evd">{E(r["날짜"])}</span> {T(r["제목"], False)} <span class="mt">{E(r["방식"])}</span></summary><p class="f">{T(r["내용"] + " [" + r["출처"] + "]", False)}</p>{why}</details>')
        cell.append('</div>')
        g.append(''.join(cell))
g.append('</div></div>')
sec('S10', '연혁(단을 나눈 타임라인)',
    '2021 DeFi 금고 → 2023 국채 토큰 → 2025 주식 토큰과 법인, 인가 정비 → 2026 미국 판매 승인, 상품 층 쌓기, 경영 리스크',
    ''.join(g),
    ['{ex}읽는 법: 가로는 해, 세로는 바뀐 쪽(레인 6개). 휴대폰에서는 레인마다 해 순서로 쌓임',
     '발행 법인 세우기 전: 2021-07 DeFi 금고(Ondo Vaults)로 시작 [F-1442]. 2022 DeFi 수익이 줄자 금고와 유동성 대여를 접음 [ONM-001]',
     '(판단) 금고는 스마트컨트랙트만으로 돌아가 현실 자산을 맡아 둘 법인이 필요 없었음',
     '2023-01부터 OUSG는 Ondo I LP [F-1307], 2023-08부터 USDY는 Ondo USDY LLC가 발행 [F-1927]',
     '주식 토큰은 2024-01 계획(2단계 상장 증권)만 밝히고 [F-1660], 2025-04-09 BVI 발행 법인 설립 [F-0185] 뒤 2025-09 출시 [on-0489]. 법인 전에는 주식 토큰 상품 없음'],
    [('2022년에 왜 국채였나(yieldcoin)', [
        '연준이 2022-03-16 금리 인상을 시작해 2023-07-26 5.25~5.50%까지 올림 [ONM-012 ONM-013]',
        'USDC 약관상 보유자는 준비금 이자를 받을 권리가 없음 [ONM-014]',
        '회사가 밝힌 이유: 이자가 붙지 않는 스테이블코인 1,000억 달러 이상을 가진 보유자가 국채에 투자하게 하려고 [F-1443]',
        '(판단) 그래서 "이자 붙는 디지털 달러(yieldcoin)"라는 이름으로 USDY를 만듦. 비교 대상이 국채가 아니라 이자 0인 스테이블코인']),
     ('이름이 바뀐 것', [
        'Ondo Global Markets → Ondo Stocks(미국 주식 토큰 브랜드). 발행 법인 이름에 옛 이름이 남음 [F-1665 on-0406]',
        'Ondo Chain → Ondo Network(2026-07-27) [ONM-004]',
        'USDY 발행자 Ondo USDY LLC → Ondo Global Markets (BVI)(2025-12-15) [on-0327]']),
     '포트폴리오 안 Ondo Stocks: 2025-09 Ondo Stocks 100종 이상 출시 [on-0230], 2026-09-24 그 토큰을 묶은 Intelligent Portfolios 출시 [F-1324]',
     '2026-10-05 비상장사 주당 가치 연동 노트 Ondo Private Markets 발표 [on-0372]'])

# ======================= S11 =======================
CUR_SEC[0] = 'S11'
REG = [('미국', 'co', [('OUSG', 'Rule 506(c), 3(c)(7) 면제, 적격투자자만 [F-1307]'), ('보관형 IVV, MU', 'Oasis Pro TA 발행(2026-07-02) [F-1949]'), ('Oasis Pro Markets', 'FINRA 승인으로 미국 투자자 판매(2026-07-23) [F-1462]')]),
       ('미국 밖 전체', 'is', [('USDY, Ondo Stocks', 'Regulation S. 미국인과 미국 안 주문은 받지 않음 [on-0489 on-0490]'), ('Ondo Perps', '미국 밖에서만(Ondo Global Group) [F-1967]')]),
       ('EU와 EEA', 'is', [('Ondo Stocks', '리히텐슈타인 FMA 승인 기본 투자설명서와 EEA 통지(2025-11-11). 첫 상품 QQQon(발행 한도 5억 달러) [on-0491 F-0191]')]),
       ('아랍에미리트(아부다비)', 'tp', [('Ondo 증권 10종', 'Binance 운영 ADGM 다자간거래시설 상장(2026-03-03) [F-1457]')]),
       ('한국', 'tp', [('OUSG', '한국 거주자, 한국 법인 제외 [F-1404]'), ('협약', '카카오페이증권 MOU(2026-09-28), 미래에셋 Global X ETF 토큰화 MOU(2026-06-16) [F-0204 F-1958]')])]
g = [legend([('co', '회사 쪽이 직접 팖'), ('is', '발행 법인이 팖'), ('tp', '제3자 창구')]), '<div class="regs">']
for name, c, items in REG:
    g.append(f'<div class="rg {c}"><b class="rgh">{E(name)}</b>')
    for p, t in items:
        g.append(f'<div class="rgi">{chip(p)}<span class="f">{T(t)}</span></div>')
    g.append('</div>')
g.append('</div>')
sec('S11', '규제 용어 풀이: 면제, Regulation S, EU 투자설명서',
    'Ondo는 "등록 면제"로 팖. 지역마다 다른 근거를 씀',
    ''.join(g),
    ['{ex}읽는 법: 상자 하나가 판매 지역. 초록 칩이 그 지역에서 파는 상품, 옆 글이 판매 근거',
     ('"면제"는 두 가지 뜻', [
         '수수료 면제(fee waiver): 받을 수 있는 돈을 기간을 정해 안 받는 것. 예: OUSG 운용보수 0.15%를 2027-01-01까지 안 받음 [F-1313]',
         '{ex}법적 등록 면제(exemption): 원래는 증권을 SEC에 등록하고 팔아야 하지만, 조건을 지키면 등록 없이 팔 수 있게 한 예외. Rule 506(c)는 적격투자자에게만 팔면 공개 광고를 해도 등록 면제, 3(c)(7)은 적격매수자만 받는 펀드의 공모 펀드 등록 면제, Regulation S는 미국 밖 판매의 미국 등록 면제']),
     ('Regulation S', [
         '미국 증권법 규칙(17 CFR 230.901~905). 조건: 거래가 미국 밖에서 일어날 것(offshore transaction), 미국 안에서 판매 권유를 하지 않을 것(no directed selling efforts) [S-regs-cfr]',
         '그래서 Ondo Stocks는 미국인과 미국 안 주문을 받지 않음 [F-0501 on-0489]',
         '(판단) 한계: 미국 규칙만 비켜 갈 뿐, 파는 나라의 규칙은 따로 지켜야 함. EU는 투자설명서가 필요']),
     ('FMA 승인으로 달라진 것', [
         'EU 규정상 본국 당국이 승인한 투자설명서는 다른 회원국 당국에 통지하면 그 나라 공모에도 유효(passporting) [ONM-015]',
         '전에는 Regulation S로 미국 밖 판매만, 승인 뒤에는 EEA 개인 투자자에게 공식 판매 [on-0491 F-1458]',
         '투자설명서 유효기간 2026-11-11까지 [F-0191]'])],
    [('왜 리히텐슈타인인가', [
         'EU 밖 발행사는 처음 공모하는 나라 등 가운데 승인받을 나라를 스스로 고를 수 있음 [ONM-016]',
         '회사는 FMA를 통지 제도가 EEA 전체에 미치는 자리 잡은 감독기관이라고만 설명, 고른 이유는 따로 밝히지 않음 [ONM-017]',
         '같은 FMA 승인 설명서를 Backed(xStocks 발행사)도 씀 [ONM-018]']),
     ('100종 이상으로 출시한 이유', [
         '2025-02 설계 변경 목적: 지갑, 프로토콜, 거래소가 자기 이용자에게 전통 증권을 팔 수 있게 [F-1450]',
         '(판단) 거래소와 지갑이 메뉴로 걸려면 인기 미국 주식과 ETF가 한꺼번에 있어야 함. 첫날 100종 이상을 내고, Bitget이 2025-09부터 100종 이상을 자기 이용자에게 판 것이 그 결과',
         'Bitget 판매 2025-09부터 100종 이상 [on-0078], 2026-11 450개 이상 [on-0230]. 회사 계획은 수천 개 [F-0537]']),
     '2026-02-03 BVI 발행 쪽이 SEC에 증권신고서를 비공개 제출. 효력이 생기면 SEC 보고 의무를 지는 첫 이전 가능 토큰화 주식 발행사가 된다고 회사가 밝힘 [F-1460]'])

# ======================= S12 =======================
CUR_SEC[0] = 'S12'
RISK = [('상환 한도', 'OUSG 즉시 상환 24시간 합산 5,000만 달러. 한도가 찬 날이나 USDC 지원이 멈춘 날은 즉시 현금화가 안 됨 [on-0387]'),
        ('펀드 쏠림', 'OUSG의 48.58%가 SWEEP 한 곳(2026-11-18) [S-ousg-page]'),
        ('경영권 분쟁', '창업자 사망 뒤 2026-08 유족이 델라웨어 법원에 경영권과 De Bode 해임 요구 소송 [on-0380]'),
        ('점유율 하락', '토큰화 주식 점유율 51.59% → 24.23%. 잔액은 4.13억 → 8.99억 달러로 늘었으나 Binance bStocks(2026-06) 뒤 1위를 내줌 [on-0154 on-0272 F-1546]'),
        ('제3자 토큰 구조', '주식 발행 기업 동의 없이 만든 토큰이라 기업과 보유자 사이 권리 관계 없음 [on-0160]. 탈중앙 거래소 풀에서 NVDA 토큰이 규제 거래소보다 약 9.3% 비싸게 체결된 사례(SEC 제출 의견서, 필자가 Citadel Securities 재정 지원을 밝힘) [on-0174]')]
g = [legend([('tp', '위험 카드')]), '<div class="risks">']
for i, (t, b) in enumerate(RISK, 1):
    g.append(f'<div class="rk"><div class="rkn">{i}</div><b>{E(t)}</b><p class="f">{T(b)}</p></div>')
g.append('</div>')
sec('S12', '주의할 점',
    '상환 한도, 펀드 쏠림, 경영권 분쟁, 점유율 하락, 제3자 토큰 구조',
    ''.join(g),
    ['{ex}읽는 법: 카드 1~5. 숫자가 작을수록 보유자 돈에 바로 닿는 위험',
     'USDY, Ondo Stocks 보유자는 발행 법인 도산 위험을 짐(limited recourse) [F-0188]',
     'BVI 발행 법인은 BVI 감독청 인가가 없음 [F-0528]'],
    ['SEC 비공개 조사가 2025-12 기소 없이 종결됐다고 회사가 발표. SEC 확인문은 없음 [on-0227]',
     'Oasis Pro 대체거래시스템: 2026-07-23 판매 승인 뒤 2026-11-18까지 회사 글과 FINRA 주간 자료에서 거래 기록을 찾지 못함 [ONM2-001 ONM2-002]',
     '(판단) 거래 시설 인가를 사도 올릴 상품과 손님이 없으면 거래가 생기지 않음'])

# ---------- S13 출처 ----------
CUR_SEC[0] = 'S13'


def render():
    toc = ''.join(f'<li><a href="#{s["id"]}"><b>{s["id"]}</b> {E(s["head"])}</a></li>' for s in SECS) + '<li><a href="#S13"><b>S13</b> 출처: 섹션별로 묶은 링크</a></li>'
    body = []
    for s in SECS:
        l2 = ul(s['l2']) if not isinstance(s['l2'], str) else s['l2']
        l3 = ul(s['l3'])
        body.append(f'''<section class="sec" id="{s["id"]}"><div class="sid">{s["id"]} {E(s["title"])}</div>
<h2 class="head">{E(s["head"])}</h2>
<div class="fig">{s["fig"]}</div>
<div class="l2"><h3>{E(s["l2title"])}</h3>{l2}</div>
<details class="l3"><summary>+ 근거, 세부, 비유, 판단</summary>{l3}</details></section>''')
    # S13
    by = {}
    for n, k, ref, sc in FN_LIST:
        by.setdefault(sc, []).append((n, k, ref))
    s13 = ['<section class="sec" id="S13"><div class="sid">S13 출처</div><h2 class="head">섹션별로 묶은 출처. 누르면 열림</h2>']
    for sc in [s['id'] for s in SECS]:
        items = by.get(sc, [])
        s13.append(f'<details class="srcg"><summary>{sc} {E(next(x["title"] for x in SECS if x["id"] == sc))} ({len(items)}건)</summary><ol class="srcl">')
        for n, k, ref in items:
            links = '; '.join(f'<a href="{E(it["url"])}" rel="noopener" target="_blank">{E(it["t"] or it["url"])}</a>' for it in ref['items'])
            s13.append(f'<li value="{n}" id="src{n}">{links} <code>{E(k)}</code></li>')
        s13.append('</ol></details>')
    s13.append('<p class="cap x">표기: F-는 사실 DB(db/facts.csv), on-은 옛 화면 본문 줄, ONM-과 ONM2-는 이번 메모 조사, S-는 패키지 출처, DL-은 2026-11-18 받은 DefiLlama 공개 API</p></section>')
    body.append(''.join(s13))
    fnd = {n: dict(k=k, items=ref['items']) for n, k, ref, sc in FN_LIST}
    gl = [dict(t=g['용어'], d=g['쉬운 설명'], a=g['비유(원문 병기)']) for g in GL]
    tpl = open('/home/user/learning_tokens/scratchpad/ondodeep/page_tpl.html', encoding='utf-8').read()
    out = tpl.replace('%%TOC%%', toc).replace('%%BODY%%', '\n'.join(body))
    out = out.replace('%%FN%%', json.dumps(fnd, ensure_ascii=False).replace('</', '<\\/')).replace('%%GL%%', json.dumps(gl, ensure_ascii=False).replace('</', '<\\/'))
    return out


html_out = render()
OUT.write_text(html_out, encoding='utf-8')
print('written', OUT, len(html_out), 'fn', len(FN), 'terms used', len(USED), '/', len(GL))
for w in WARN:
    print('WARN', w)
json.dump([dict(id=s['id'], head=s['head']) for s in SECS], open('/home/user/learning_tokens/scratchpad/ondodeep/secs.json', 'w', encoding='utf-8'), ensure_ascii=False)
