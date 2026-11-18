import json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.worksheet.properties import Outline
from openpyxl.utils import get_column_letter as L

EXPAND = len(sys.argv) > 1 and sys.argv[1] == 'expand'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/xl/Ondo_구조와_흐름_261118.xlsx'

FN = '맑은 고딕'
wb = Workbook()
ws = wb.active
ws.title = 'Ondo'
ws.sheet_properties.outlinePr = Outline(summaryBelow=False, summaryRight=False)
ws.column_dimensions['A'].width = 4.5
ws.column_dimensions['B'].width = 5.5
ws.column_dimensions['C'].width = 7

BAND = 'DCE6F1'
COL = {
    'co': ('DDEBF7', '1F4E79', '9BC2E6'),
    'fd': ('FCE4D6', '843C0C', 'F4B183'),
    'is': ('FFF2CC', '7F6000', 'FFD966'),
    'tp': ('EDEDED', '404040', 'BFBFBF'),
    'gr': ('E2EFDA', '375623', 'A9D08E'),
}
GRAY = '808080'
LAST_COL = 30

r = 1
levels = {}


def F(bold=False, size=10, color='000000', u=None):
    return Font(name=FN, bold=bold, size=size, color=color, underline=u)


def mark(level):
    global r
    levels[r] = level
    r += 1


def rich(text, size=10, color='000000'):
    if '**' not in text:
        return text
    parts = text.split('**')
    out = []
    for i, p in enumerate(parts):
        if not p:
            continue
        out.append(TextBlock(InlineFont(rFont=FN, sz=size, b=(i % 2 == 1), color='FF' + color), p))
    return CellRichText(*out)


def put(row, col, text, size=10, bold=False, color=None, align=None):
    gray = text.startswith('(판단)')
    c = color or (GRAY if gray else '000000')
    cell = ws.cell(row=row, column=col)
    v = rich(text, size, c)
    cell.value = v
    cell.font = F(bold=bold, size=size, color=c)
    if align:
        cell.alignment = Alignment(horizontal=align, vertical='center')
    return cell


def blank(level=1):
    mark(level)


def band(text):
    blank(0)
    for c in range(1, LAST_COL + 1):
        ws.cell(row=r, column=c).fill = PatternFill('solid', fgColor=BAND)
    put(r, 3, text, size=11)
    mark(0)
    blank(1)


def h1(text):
    put(r, 3, text, size=10.5, bold=True)
    mark(1)


def t(level, text, col=None):
    """level 2 at D visible, 3 at E hidden, 4 at F hidden"""
    col = col or {2: 4, 3: 5, 4: 6}[level]
    put(r, col, text)
    mark({2: 1, 3: 2, 4: 3}[level])


def chip(row, c1, c2, kind, text, bold=True, size=10):
    fill, fg, bd = COL[kind]
    for c in range(c1, c2 + 1):
        ws.cell(row=row, column=c).fill = PatternFill('solid', fgColor=fill)
    put(row, c1, text, size=size, bold=bold, color=fg)


def line(level, label, kind, text, c1=4, c2=5, tcol=7):
    chip(r, c1, c2, kind, label)
    put(r, tcol, text)
    mark({2: 1, 3: 2, 4: 3}[level])


def box(c1, c2, kind, title, subs, level=1):
    """box spanning columns c1..c2 over 1+len(subs) rows starting at r; returns top row"""
    global r
    fill, fg, bd = COL[kind]
    top = r
    rows = [title] + subs
    side = Side(style='thin', color=bd)
    for i, txt in enumerate(rows):
        for c in range(c1, c2 + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = PatternFill('solid', fgColor=fill)
            cell.border = Border(
                left=side if c == c1 else None, right=side if c == c2 else None,
                top=side if i == 0 else None, bottom=side if i == len(rows) - 1 else None)
        put(r, c1, txt, size=10 if i == 0 else 9, bold=(i == 0), color=fg)
        mark(level)
    return top


def boxes_side(specs, level=1):
    """specs: list of (c1,c2,kind,title,subs). draws boxes side by side on same rows"""
    global r
    top = r
    n = max(1 + len(s[4]) for s in specs)
    for k in range(n):
        for (c1, c2, kind, title, subs) in specs:
            rows = [title] + subs
            if k >= len(rows):
                continue
            fill, fg, bd = COL[kind]
            side = Side(style='thin', color=bd)
            for c in range(c1, c2 + 1):
                cell = ws.cell(row=r, column=c)
                cell.fill = PatternFill('solid', fgColor=fill)
                cell.border = Border(
                    left=side if c == c1 else None, right=side if c == c2 else None,
                    top=side if k == 0 else None, bottom=side if k == len(rows) - 1 else None)
            put(r, c1, rows[k], size=10 if k == 0 else 9, bold=(k == 0), color=fg)
        mark(level)
    return top


def arrows(items, level=1):
    """items: list of (col, text) arrows on one row"""
    for col, txt in items:
        put(r, col, txt, size=10, bold=True, color='7F7F7F')
    mark(level)


def legend(items):
    blocks = []
    for kind, label in items:
        fill, fg, bd = COL[kind]
        blocks.append(TextBlock(InlineFont(rFont=FN, sz=10, color='FF' + (bd if kind != 'tp' else '9E9E9E')), '■ '))
        blocks.append(TextBlock(InlineFont(rFont=FN, sz=10, color='FF404040'), label + '   '))
    blocks.append(TextBlock(InlineFont(rFont=FN, sz=10, color='FF' + GRAY), '회색 글씨 = (판단)'))
    ws.cell(row=r, column=4).value = CellRichText(*blocks)
    mark(1)


def bar(row, c1, n, kind, label=None):
    fill, fg, bd = COL[kind]
    for c in range(c1, c1 + n):
        ws.cell(row=row, column=c).fill = PatternFill('solid', fgColor=bd)
    if label:
        put(row, c1 + n, label)


# =====================================================================
band('무엇을 하나?')
h1('미국 국채와 미국 주식을 블록체인 토큰으로 바꿔 파는 회사')
t(3, '**토큰(token):** 블록체인 지갑에 들어가는 디지털 보관증. 지갑만 있으면 24시간 옮기고 사고팔 수 있음')
t(3, '**기본 구조:** 진짜 자산(국채, 주식)은 발행 법인 명의 계좌에 두고, 그 값을 따라가는 토큰을 찍어 팖')
t(3, '**본사 Ondo Finance Inc.:** 미국 코네티컷주 그리니치, 2021 설립, 비상장')
t(4, '창업자 Nathan Allman(전 Goldman Sachs 디지털자산 팀). 2026-05 사망')
t(4, '사망 당시 CEO, 단독 이사, 다수 주주. President였던 Ian De Bode(전 McKinsey 디지털자산 업무 총괄)가 CEO 승계, 팀 페이지 직함은 Acting CEO and President')
t(4, '2026-08 유족이 델라웨어 법원에 경영권과 De Bode 해임을 요구하는 소송 제기')
t(4, '(판단) 단독 이사가 사라지고 최종 결정권이 법원 판단에 걸린 상태라 파트너와 규제기관이 계약 상대를 확신하기 어려운 구간')
t(3, '**투자 유치:** 2021-08 시드 400만 달러(Pantera Capital 주도), 2022-04 시리즈 A 2,000만 달러(Founders Fund, Pantera 주도)')
t(4, '시리즈 A 참여: Coinbase Ventures, Tiger Global, Flow Traders 등. Coinbase가 Ondo에 걸친 첫 자리')
blank()
h1('상품 4개 + 토큰 1개: 사는 사람에 따라 상품과 발행 법인이 갈라짐')
legend([('co', '회사 쪽'), ('fd', '재단 쪽'), ('is', '발행 법인'), ('tp', '제3자(계약 상대)'), ('gr', '상품')])
blank()

line(2, 'OUSG', 'gr', '미국 큰손용 국채 펀드 지분 토큰. 토큰화 국채 MMF 4개 지분을 담음')
t(3, '**정식 이름:** Ondo Short-Term US Government Treasuries')
t(3, '**누가 사나:** 적격투자자(accredited investor)이면서 적격매수자(qualified purchaser). 개인이면 투자자산 500만 달러 이상')
t(4, '한국 거주자와 한국 법인은 자격 문서에서 명시적으로 제외')
t(4, '근거: 미국 증권법 Rule 506(c) 사모 면제, 투자회사법 3(c)(7) 펀드 등록 면제')
t(3, '**최소 금액:** 즉시 투자와 상환 5,000달러. 즉시가 아닌 방식은 투자 10만 달러, 상환 5만 달러')
t(3, '**안에 든 것(2026-11-18):** SWEEP 48.58%, BUIDL 32.69%, BENJI 10.12%, FYOXX 7.54%, USDC 1.14%')
t(4, '네 펀드 모두 미국 단기 국채, 현금, 레포(국채 담보 초단기 대출)를 사는 MMF(머니마켓펀드)형')
t(4, '아래 "상품별 돈 흐름" OUSG 칸에 펀드별 설명')
t(3, '**찍는 곳:** Ondo I LP. 델라웨어 합자회사(LP) 형태의 펀드 그 자체. OUSG는 이 펀드의 지분')
t(3, '**보유자 권리:** 펀드 지분(LP interest). 보유자가 펀드의 주인 중 한 명')
t(3, '**Ondo 수입:** 운용보수 연 0.15%. 2027-01-01까지 면제라 지금 0')
t(3, '**크기:** 3.1억 달러(2026-11-17 회사 홈페이지). 2025-11 7.8억 달러에서 1년 사이 60% 감소')

line(2, 'USDY', 'gr', '미국 밖 개인과 기관용 이자 붙는 달러 토큰. 미국 단기 국채를 담보로 둠')
t(3, '**정식 이름:** Ondo US Dollar Yield. 회사 표현으로 yieldcoin(이자 주는 스테이블코인)')
t(3, '**누가 사나:** 미국 밖 개인과 기관. 미국인 불가. 신원 확인(KYC) 필요')
t(3, '**최소 금액:** 500달러(주력 체인 밖은 5,000달러)')
t(3, '**안에 든 것(2026-11-13):** 미국 국채 82.73%, SHVon 17.24%')
t(4, 'SHVon: BlackRock 단기 국채 ETF(iShares 0-1년, 티커 SHV)를 Ondo가 Ondo Stocks로 토큰화한 것. USDY 안에 Ondo의 다른 상품이 들어 있는 셈')
t(4, '은행 예금을 담을 때 보관처: First Citizens Bank')
t(3, '**찍는 곳:** Ondo Global Markets (BVI) Limited. 2025-12-15 전에는 미국 특수목적 법인 Ondo USDY LLC가 발행')
t(3, '**보유자 권리:** 담보부 노트(secured note). 발행 법인에 대한 채권이고 담보가 붙어 있음. 국채의 주인은 아님')
t(3, '**Ondo 수입:** 담보 수익과 보유자 지급 수익의 차이(spread)')
t(3, '**크기:** 23.8억 달러(2026-11-17). Ondo 상품 중 가장 큼, 국채 토큰 상품 단일 1위')

line(2, 'Ondo Stocks', 'gr', '미국 밖 투자자용 미국 주식과 ETF 가격 연동 토큰. 예: AAPLon, TSLAon')
t(3, '**옛 이름:** Ondo Global Markets. 발행 법인 이름에 옛 이름이 남음')
t(3, '**누가 사나:** 미국 밖 개인과 기관, 거래소, 지갑. 미국인과 미국 안 주문 불가')
t(3, '**안에 든 것:** 토큰과 같은 수량의 실제 미국 주식과 ETF. Alpaca와 BitGo Trust 담보 계좌에 보관')
t(3, '**찍는 곳:** Ondo Global Markets (BVI) Limited')
t(3, '**보유자 권리:** 채무증권 토큰. 값과 배당만 따라감. 주주명부 등재, 의결권, 주식 인도 요구 권리 없음')
t(4, '주식 발행 기업(애플, 테슬라 등)의 동의 없이 제3자가 만든 토큰이라 기업과 보유자 사이 권리 관계 없음(CoinDesk Research)')
t(3, '**Ondo 수입:** 상환 수수료 0.05% + 견적가와 실제 매입가의 차이')
t(3, '**크기:** 14.4억 달러(2026-11-17 회사 홈페이지), 450종 이상, 보유자 186,636명(2026-08-15)')

line(2, 'Intelligent Portfolios', 'gr', 'Ondo Stocks 여러 개를 정해진 비중으로 묶은 포트폴리오 토큰. 2026-09-24 출시', c2=6, tcol=8)
t(3, '**상품인가:** 상품 맞음. Ondo Stocks 위에 한 겹 더 얹은 상품. 토큰 1개를 발행하고 상환하면 포트폴리오 전체가 들고 남')
t(4, '비유: Ondo Stocks가 낱개 반찬, Intelligent Portfolios는 정해진 비율로 담은 도시락 한 개')
t(3, '**첫 3종:** BLKHIon(고소득), BLKDIGon(분산 성장), BLKGRWon(고성장). 이름의 BLK = BlackRock')
t(3, '**누가 정하나:** 전략은 BlackRock이 Ondo를 위해 만듦. 구현 방식과 리밸런싱은 Ondo가 정하고 스마트컨트랙트가 자동 실행')
t(4, '종목과 목표 비중은 출시 때 고정, 정해진 일정마다 비중을 다시 맞춤(rebalancing). 리밸런싱 내역은 블록체인에서 공개')
t(3, '**찍는 곳:** Ondo Global Markets (BVI) Limited')
t(3, '**Ondo 수입:** 연 서비스 수수료')

line(2, 'ONDO 토큰', 'fd', '생태계 투표권 성격 토큰. 재단 발행이라 회사 매출 아님')
t(3, '**발행:** Ondo Foundation(케이맨 재단). 회사 주식과 별개')
t(3, '**판매:** 2022-07 CoinList에서 1만 8천여 명에게 1,000만 달러 이상 판매(공급량 약 2%). 시드와 시리즈 A 투자자도 각각 7% 미만 받음')
t(3, '**규제:** SEC가 토큰화 방식과 ONDO 토큰 증권성을 수년간 비공개 조사, 2025-12 기소 없이 종결(회사 발표)')
blank()

# =====================================================================
band('뭘로 돈 버나?')
h1('지금 돈이 남는 곳 = USDY 이자 차이 + Ondo Stocks 수수료. OUSG는 보수 면제로 0')
line(2, 'USDY', 'gr', '1만 달러 → 담보 4.10% = 410달러, 보유자 3.75% = 375달러, 남는 몫 35달러')
t(3, '수치: 2026-11-16 회사 화면 담보 만기수익률 4.10%, 보유자 표시 연 수익률 3.75%')
t(3, '회사가 매달 지급 수익률을 정함. 출시 때 기초 5.1%, 지급 5.0%')
t(3, '차이 안에는 Ondo Finance가 일부 대는 약 3% 손실 완충분(담보 값이 떨어지면 먼저 깎이는 몫)의 대가도 들어감')
t(3, '(판단) 만기수익률과 지급 수익률은 같은 지표가 아니라 정확한 몫은 아님. 방향은 맞음')
line(2, 'Ondo Stocks', 'gr', '1만 달러 상환 → 수수료 5달러. 견적가가 실제 매입가보다 0.1% 높으면 10달러 추가')
t(3, '돈을 내는 쪽: 발행 법인에서 직접 토큰을 찍고 돌려주는 1차 매수자(거래소, 시장조성자)')
line(2, 'Intelligent Portfolios', 'gr', '연 서비스 수수료', c2=6, tcol=8)
line(2, 'OUSG', 'gr', '운용보수 0.15%, 2027-01-01까지 면제 → 지금 0. 면제 끝나면 잔액 1억 달러당 연 15만 달러')
t(3, '즉시 발행과 상환에 추가 수수료가 붙을 수 있다고만 공시')
t(3, '(판단) 지금 OUSG는 돈을 버는 상품이 아니라 큰손 자금과 신뢰를 모으는 바닥 상품 역할')
blank()
h1('상품 크기 (2026-11-17 회사 홈페이지, 칸 1개 = 2억 달러)')
for name, v, lab in [('USDY', 12, '23.8억 달러'), ('Ondo Stocks', 7, '14.4억 달러'), ('OUSG', 2, '3.1억 달러')]:
    chip(r, 4, 5, 'gr', name)
    bar(r, 6, v, 'gr', None)
    put(r, 6 + v, lab)
    mark(1)
t(3, '회사 발표 성장: 2024-01 전체 2.25억 달러 이상 → 2025-07 14억 달러 이상 → 2026-11 약 41억 달러')
t(4, 'USDY: 2024-10 4억 → 2025-05 6.3억 → 2026-11 23.8억 달러')
t(4, 'Ondo Stocks: 2025-12 3.7억 → 2026-05 10억 → 2026-11 14.4억 달러')
t(3, '순위(rwa.xyz, 2026-11-16): 국채 토큰 플랫폼 2위 32억 달러(1위 Franklin 33억), 토큰화 주식 2위 8.99억 달러 24.23%(1위 Binance 13.6억)')
t(4, '회사 홈페이지(14.4억)와 rwa.xyz(8.99억)는 Ondo Stocks 집계 기준이 다름')
t(4, '(판단) 32억에는 USDY가 담은 SHVon 약 4.17억 달러가 두 번 잡혀 있음. 빼면 약 28억 달러')
blank()
h1('그 돈이 본사(Ondo Finance Inc.)로 오는지는 바깥에서 갈라 볼 수 없음')
t(2, '(판단) USDY, Ondo Stocks, Intelligent Portfolios를 찍는 발행 법인 지분 90.01%가 재단 쪽, 본사는 9.99%')
t(3, '지분: Flux Finance 90.01%(Ondo Foundation 완전 자회사), Ondo Finance Inc. 9.99%(2025-11-11 기준 EU 투자설명서)')
t(3, '본사가 확인되는 연결: 발행 법인에 토큰화 기술 용역, 9.99% 지분')
t(3, '흑자 여부는 공시하지 않음')
blank()

# =====================================================================
band('발행 (법인 구조: 누가 찍고 누가 지키나)')
h1('본사는 기술만, 토큰은 별도 법인이 찍음')
t(2, '약관에서 스스로를 "중개, 체결, 청산, 보관을 하지 않는 소프트웨어와 기술 회사"라고 부르는 이유. 증권 인가가 필요한 일은 다른 법인과 계약 상대가 맡음')
t(3, '2023-08 회사 설명은 "기술 부문과 토큰 상품을 만들고 운용하는 자산운용 부문"이었음. 지금은 기술 회사로만 규정')
blank()
legend([('co', '회사 쪽'), ('fd', '재단 쪽'), ('is', '발행 법인'), ('tp', '제3자(계약 상대)'), ('gr', '상품')])
put(r, 4, '재단 쪽 (주인 없음)', bold=True, color=COL['fd'][1])
put(r, 9, '회사 쪽 (VC가 주주)', bold=True, color=COL['co'][1])
put(r, 14, '회사 쪽 미국 법인', bold=True, color=COL['co'][1])
mark(1)
AG = '7F7F7F'
top1 = boxes_side([
    (4, 7, 'fd', 'Ondo Foundation', ['케이맨 재단회사, 주주 없음', 'ONDO 토큰 발행']),
    (9, 12, 'co', 'Ondo Finance Inc.', ['델라웨어 주식회사, 2021', '직원, 기술, 브랜드 본체']),
    (14, 17, 'co', 'GP + Ondo I LP', ['GP 유일 구성원 = 본사', 'OUSG를 찍는 펀드 그 자체']),
])
put(top1, 13, '→', bold=True, color=AG)
arrows([(5, '↓ 완전 자회사'), (10, '│'), (15, '')])
top2 = boxes_side([
    (4, 7, 'fd', 'Flux Finance', ['원래 Ondo가 만든 국채 담보대출', '토큰 채무 추가 담보 보증']),
    (14, 17, 'co', 'Ondo Capital Management', ['SEC 등록 투자자문사', 'OUSG 배분 결정']),
])
for i in range(3):
    put(top2 + i, 10, '│', bold=True, color=AG)
arrows([(5, '↓ 90.01%'), (10, '↓ 9.99% + 토큰화 기술 용역')])
top = boxes_side([
    (4, 12, 'is', 'Ondo Global Markets (BVI) Limited = 발행 법인', ['영국령 버진아일랜드 사업회사. BVI 금융 인가 없음', '미국 밖 판매 면제(Regulation S), EU 투자설명서로 판매']),
    (14, 17, 'co', 'Oasis Pro (2025-10-07 인수)', ['증권사, ATS, 명의개서대리인', '미국 안 판매 담당']),
])
arrows([(5, '↓ 발행'), (8, '↓ 발행'), (11, '↓ 발행')])
boxes_side([
    (4, 5, 'gr', 'USDY', []),
    (7, 8, 'gr', 'Ondo Stocks', []),
    (10, 12, 'gr', 'Intelligent Portfolios', []),
    (14, 17, 'co', 'Ondo Global Group', ['Ondo Perps 운영(2026-07)']),
])
blank()
put(r, 4, '계약 상대(제3자): 지분 관계 없음, 계약으로만 연결', bold=True, color=COL['tp'][1])
mark(1)
boxes_side([
    (4, 7, 'tp', 'Ankura Trust', ['담보 대리인, 1순위 담보권', 'USDY 검증도 맡음']),
    (9, 12, 'tp', 'Alpaca, BitGo Trust', ['주식 매매와 보관', 'First Citizens Bank: 예금']),
    (14, 17, 'tp', '운용사 4곳 + Circle, Coinbase', ['OUSG가 담는 펀드', 'USDC 환전과 현금 보관']),
])
blank()

h1('법인별 설명 (+로 펼침)')
line(2, '재단', 'fd', 'Ondo Foundation: 케이맨제도 비영리 재단, 실질 소유자 없음. ONDO 토큰 발행과 거버넌스')
t(3, '케이맨 재단회사(foundation company): 주주가 없는 회사. 이사와 감독인이 정관대로 운영. 가상자산 재단이 토큰과 금고를 맡기려고 자주 쓰는 형태')
t(3, '비유: 회사가 낸 포인트를 회사와 무관한 공익 재단이 관리하는 모양. 주주가 없어 "누구 회사냐"는 질문을 피함')
line(2, '재단', 'fd', 'Flux Finance: 재단 완전 자회사. 발행 법인 90.01% 보유')
t(3, '원래 Ondo가 만든 블록체인 국채 담보대출(repo) 서비스. 재단에 팔렸고 Ondo DAO(토큰 보유자 투표 모임)가 출시')
t(3, 'Ondo Stocks 보유자에 대한 채무를 더 담보하려고 자금을 보증(회사 문서)')
t(3, '재단 쪽이 발행 법인 다수 지분을 가진 이유는 회사가 밝히지 않음')
t(4, '(판단) 본사 지분을 10% 바로 밑으로 맞추고 대주주를 주인 없는 재단 쪽에 둬서, 본사가 흔들려도 발행 법인과 보유자 자산이 함께 묶이지 않게 한 구조로 읽힘')
line(2, '회사', 'co', 'Ondo Finance Inc.: 운영과 기술 본체. 토큰화 작업, 가격 계산. 자체 인가 없음')
line(2, '회사', 'co', 'GP + Ondo I LP: OUSG 발행 펀드. GP(무한책임사원)의 유일 구성원이 본사')
t(3, 'LP(합자회사): 돈을 대는 유한책임사원(LP, OUSG 보유자)과 굴리는 책임자 GP로 이뤄진 펀드 그릇')
t(3, '펀드가 운용사 펀드 지분을 투자자로서 사는 구조. 운용사에 운용을 맡기는 위탁 계약이 아님')
line(2, '회사', 'co', 'Ondo Capital Management LLC: SEC 등록 투자자문사(2025-08-06 효력). OUSG 배분 결정')
t(3, '새 사업이 아님. 2023-01부터 하던 OUSG 자문을 면제보고 지위에서 정식 등록으로 옮김')
line(2, '회사', 'co', 'Oasis Pro: 2025-07-04 인수 발표, 2025-10-07 완료. 금액 비공개')
t(3, '2009 등록 증권사(broker-dealer), 대체거래소(ATS), 명의개서대리인(transfer agent)을 한 번에 확보')
t(3, '2026-07-02 Oasis Pro TA가 미국 안 보관형 토큰 IVV(S&P 500 ETF), MU(Micron 주식) 발행')
t(4, '보관형 = 증권사 계좌에 실제 주식을 두고 토큰을 그 기록으로 씀. BVI 상품은 가격 연동 채무를 파는 방식으로 다름')
t(3, '2026-07-23 FINRA 승인: Oasis Pro Markets가 미국 기관과 개인에게 토큰 주식과 펀드 판매 가능')
t(3, '(판단) 인수 뒤에도 미국 판매 승인까지 9개월 반. 인가를 언제 줄지 몰라 회사째로 산 선택')
line(2, '회사', 'co', 'Ondo Global Group: Ondo Perps(미국 주식, ETF 가격 무기한선물) 운영. 2026-02 발표, 2026-07 출시')
line(2, '발행', 'is', 'Ondo Global Markets (BVI) Limited: USDY, Ondo Stocks, Intelligent Portfolios 발행')
t(3, '2025-04 설립. BVI 감독 인가 없음(회사 약관). 미국 밖 판매 면제(Regulation S)와 지역별 투자설명서로 팖')
t(3, 'EU: 2025-11-11 리히텐슈타인 금융시장감독청(FMA) 기본 투자설명서 승인, EEA 29개국 통지. 첫 상품 QQQon(발행 한도 5억 달러). 유효기간 2026-11-11 종료')
t(3, '2026-02-03 이 법인 상품의 SEC 증권신고서를 비공개 제출. 효력 발생 발표 없음')
t(3, '보유자는 이 법인 자산에서만 돌려받음(limited recourse). 본사에 청구 불가')
line(2, '설립지', 'tp', '델라웨어, BVI, 케이맨 = 회사를 등기한 곳(place of incorporation). 허가가 아님')
t(3, '한국으로 치면 본점 소재지. 실제 금융 허가는 SEC 투자자문 등록(Ondo Capital Management)과 Oasis Pro 허가뿐')
blank()

h1('법인을 나눈 이유 5가지 (생긴 순서)')
line(2, '① 펀드 그릇', 'co', 'Ondo I LP (2023-01): 미국에서 펀드 지분을 팔려면 회사와 분리된 펀드가 필요')
t(3, '비유: 자산운용사(본사)와 그 회사가 만든 펀드(Ondo I LP)는 별개 주머니')
line(2, '② 판매 대상', 'is', 'Ondo USDY LLC (2023-08) → BVI 발행 법인 (2025-04): 미국 밖 개인용 상품은 미국 밖 그릇에서')
t(3, '비유: 국내 매장과 해외 직영 매장을 법인부터 따로 둠')
line(2, '③ 파산 절연', 'is', 'BVI 발행 법인 + Ankura: 본사가 망해도 토큰 자산은 따로 지킴')
t(3, '파산 절연(bankruptcy remoteness): 발행 법인을 본사와 떼고, 담보 대리인이 보유자 몫 담보에 1순위 권리를 쥠. 본사 지분 9.99%로 제한')
line(2, '④ 토큰 분리', 'fd', 'Ondo Foundation: 코인과 회사 주식을 다른 주머니로')
t(3, '토큰이 회사 주식처럼 보이면 미국 증권 규제 대상이 될 수 있어 주인 없는 재단에 둠')
line(2, '⑤ 인가', 'co', 'Oasis Pro 인수, Ondo Capital Management 등록 (2025): 미국 안 중개와 기록에 필요한 허가')
t(3, '비유: 증권사 라이선스를 새로 받는 대신 소형 증권사를 인수')
t(2, '(판단) "법인 분리 = 인가 때문"은 ⑤에만 맞음. ①~④는 펀드 형태, 판매 대상, 파산 절연, 토큰 분리 때문')
blank()

h1('금고는 누구 금고? = 토큰을 찍은 법인 명의. 보유자는 금고 주인이 아님')
boxes_side([
    (4, 7, 'is', '금고 주인(법적 소유자)', ['발행 법인', 'BVI 법인 또는 Ondo I LP']),
    (9, 12, 'tp', '금고지기(보관기관)', ['Alpaca, BitGo Trust,', 'First Citizens, 펀드 수탁기관']),
    (14, 17, 'tp', '열쇠 하나 더(담보 대리인)', ['Ankura Trust', '보유자 대신 담보권']),
])
arrows([(5, '↑ 돌려받을 권리'), (15, '↑ 보유자 몫 담보권')])
box(4, 17, 'gr', '토큰 보유자', ['OUSG = 펀드 지분권자(펀드의 주인 중 한 명)  /  USDY, Ondo Stocks = 발행 법인에 대한 채권자(물건의 주인 아님)'])
t(3, '발행 법인이 무너지면 Ankura가 담보를 처분해 보유자에게 나눔. 돌려받을 곳은 발행 법인 자산뿐(limited recourse)')
t(3, '비유: 담보부사채신탁법 구조. 사채권자(토큰 보유자)는 회사 재산 주인이 아니지만 수탁회사(Ankura)가 담보를 쥐고 지켜 줌')
t(3, '토큰 보유 기록은 발행 법인(SPV)이 관리')
blank()

h1('다른 회사는 어디에 끼나')
line(2, 'Coinbase', 'tp', 'Coinbase Ventures가 2022-04 시리즈 A 참여 + OUSG 안 USDC 현금 보관')
line(2, 'BlackRock', 'tp', 'BUIDL 운용(OUSG 32.69%) + Intelligent Portfolios 전략 + USDY 담보 SHVon의 기초 ETF(SHV)')
t(3, 'Intelligent Portfolios 안 BlackRock 펀드가 BlackRock에 보수를 내므로 이해상충이 있다고 공시')
line(2, 'Circle', 'tp', 'USDC 발행사. OUSG 24시간 즉시 환전 통로. 상환 가능 여부가 Circle USDC 지원에 연동')
line(2, '운용사 3곳', 'tp', 'State Street와 Galaxy(SWEEP), Franklin Templeton(BENJI), Fidelity(FYOXX)')
line(2, '판매 창구', 'tp', 'Bitget(지갑 2025-09, 거래소 현물 2026-03-16), Binance(ADGM 상장 2026-03-03), Trust Wallet, MetaMask 등')
t(3, '지분 관계 없는 남의 거래소와 지갑. Bitget 안 토큰 주식 거래에서 Ondo 비중 2025-12 초 73% → 같은 달 후반 89%(Bitget 발표)')
t(3, 'Binance는 판매 창구이면서 경쟁자. 2026-06-11 자체 주식 토큰 bStocks 출시 뒤 1위')
line(2, '한국', 'tp', '2026-09 카카오페이증권, 미래에셋 MOU. 카카오페이증권이 외국인 통합계좌로 한국 주식 원주 조달 구조')
t(3, '카카오페이증권은 전날 Dinari와도 같은 취지 협약. 상용화는 국내외 규제 검토 뒤 논의')
t(3, 'Ondo 아시아 담당: 한국이 Ondo Stocks 활성 거래자 수 세계 1위(2026-11-05 인터뷰, 회사 주장)')
blank()

# =====================================================================
band('언제 어떻게 컸나 (발행 법인 세우기 전에는 무엇을 했나 포함)')
h1('2021 DeFi 금고 → 2023 국채 토큰 → 2025 주식 토큰과 법인, 인가 정비 → 2026 미국 판매와 상품 층 쌓기')
put(r, 4, '시점', bold=True); put(r, 6, '방식', bold=True); put(r, 7, '무슨 일 (+로 이유와 숫자)', bold=True); mark(1)

TL = []


def ev(date, how, text, subs=(), lvl=2):
    TL.append((date, how, text, list(subs), lvl))


def phase(title):
    TL.append(('PH', None, title, [], 0))


phase('2021-07 ~ 2022: 블록체인 안 금융으로 시작, 국채로 방향 전환')
ev('2021-07', '직접', 'Ondo Vaults 출시: DeFi 수익을 고정 몫과 변동 몫으로 나눠 판 금고', [
    '고정 쪽과 변동 쪽이 같은 금액을 넣으면 금고가 탈중앙 거래소 유동성 풀에 넣었다가, 기간이 끝나면 고정 쪽에 원금과 정해진 수익을 먼저 주고 남은 것을 변동 쪽에 줌',
    '(판단) 현실 자산을 담지 않고 스마트컨트랙트만으로 돌아가서 자산을 맡아 둘 발행 법인이 필요 없었음'])
ev('2021-08', '투자', '시드 400만 달러(Pantera Capital 주도)')
ev('2022-04', '투자', '시리즈 A 2,000만 달러(Founders Fund, Pantera 주도. Coinbase Ventures 참여)')
ev('2022-07', '직접', 'ONDO 토큰 CoinList 판매: 1만 8천여 명, 1,000만 달러 이상')
ev('2022', '전환', '국채 토큰으로 방향 전환: 현실 금리는 오르고 블록체인 안 금리는 떨어지던 때', [
    '블록체인 안 사람들이 현실 국채 이자를 원하는 수요가 분명해 "이자 주는 스테이블코인(yieldcoin)"을 구상',
    '수익이 없는 스테이블코인 1,000억 달러 이상의 보유자를 국채로 끌어오려는 것',
    '2022 무규제 가상자산 회사들이 잇따라 무너진 뒤라 운용, 보관에 규제받는 회사만 씀'])
phase('2023: 국채 토큰 두 개. 미국 큰손용(OUSG)과 미국 밖용(USDY)')
ev('2023-01', '직접', 'OUSG 출시: Ondo I LP 펀드를 세우고 BlackRock 단기 국채 ETF를 담음', [
    '이때부터 Ondo Capital Management가 면제보고 지위로 자문',
    '미국에서 펀드 지분을 팔려고 펀드 그릇(LP)과 구매 자격 제한을 둠'])
ev('2023-08', '직접', 'USDY 발표: 미국 특수목적 법인 Ondo USDY LLC가 발행', [
    'OUSG를 살 수 없는 미국 밖 개인 시장을 열려는 것. 출시 때 기초 5.1%, 지급 5.0%',
    '2024-03 Ondo USDY LLC가 미국 재무부 금융범죄단속국(FinCEN)에 송금업자로 등록'])
phase('2024: OUSG 24시간화, 주식 토큰 구상')
ev('2024-02', '계획', '주식 토큰 첫 계획 발표: 증권사 계좌 속 주식의 주문 지시를 토큰으로 주는 방식', [
    '2024-01 회사 계획: 1단계 현금성 자산, 2단계 상장 증권',
    '이 방식으로는 출시하지 않음. 발행 법인을 세우기 전이라 주식 토큰 상품은 없었음'])
ev('2024-08', '제휴', 'OUSG 기초자산을 BlackRock BUIDL로 이전, Circle USDC 즉시 환전 연결', [
    'ETF는 증시 개장 시간에만 팔 수 있지만 토큰 펀드끼리는 24시간 바로 주고받을 수 있음',
    '최초 투자 500만 달러인 기관용 BUIDL을 담아 더 낮은 문턱(지금 5,000달러)으로 팖'])
phase('2025: 주식 토큰 출시와 법인, 인가 정비')
ev('2025-02', '계획', 'Ondo Chain(자체 블록체인) 발표 + 주식 토큰 설계 변경', [
    '설계 변경: 스테이블코인처럼 미국 밖에서 자유롭게 옮기는 토큰으로. 지갑과 거래소가 자기 이용자에게 팔 수 있게 하려는 것'])
ev('2025-04', '직접', 'Ondo Global Markets (BVI) Limited 설립 = 주식 토큰 발행 법인', [
    '이 법인을 세우기 전에는 주식 토큰을 발행하지 않았음. USDY는 Ondo USDY LLC, OUSG는 Ondo I LP가 이미 발행 중'])
ev('2025-07-03', '직접', 'Ondo Catalyst: 앱, 인프라 기업에 투자하는 2.5억 달러 전략 투자 이니셔티브')
ev('2025-07-04', '인수', 'Oasis Pro 인수 발표(완료 2025-10-07)', [
    '발표 글에서 미국 밖 주식 토큰 출시를 "몇 달 안"으로 예고. 미국 쪽 인가를 같은 때 준비'])
ev('2025-07-14', '인수', 'Strangelove(블록체인 개발사) 인수 발표: Ondo Chain 인력 확보 목적')
ev('2025-08-06', '직접', 'Ondo Capital Management SEC 투자자문사 등록 효력')
ev('2025-09', '직접', 'Ondo Stocks 출시(당시 이름 Ondo Global Markets): 100종 이상, 미국 밖 대상', [
    '근거: 미국 증권법 Regulation S(미국 밖 판매 등록 면제). BVI 감독 인가 없음',
    'Bitget Wallet 등 지갑에서 판매 시작',
    '같은 사업 시작: Dinari 2023-08, Kraken과 Robinhood 2025-06. Ondo는 늦게 들어옴'])
ev('2025-10-29', '직접', 'BNB 체인 확장: 아시아, 중남미 이용자 겨냥')
ev('2025-11-11', '직접', 'EU 판매 개시: 리히텐슈타인 FMA 투자설명서 승인, EEA 29개국 통지')
ev('2025-12', '규제', 'SEC 비공개 조사 기소 없이 종결(회사 발표, SEC 확인문 없음)')
ev('2025-12-15', '직접', 'USDY 발행을 BVI 발행 법인 아래로 이전')
phase('2026: 미국 판매 개시, 상품 층 쌓기, 경쟁과 경영 리스크')
ev('2026-01', '성과', '토큰화 주식 잔액 1위: 4.13억 달러, 점유율 51.59%(출시 넉 달 만)')
ev('2026-03', '제휴', 'Binance 운영 아부다비 ADGM 다자간거래소 상장(03-03), Bitget 거래소 현물 진입(03-16)')
ev('2026-05', '변화', '창업자 Nathan Allman 사망, Ian De Bode CEO 승계')
ev('2026-05-05', '제휴', 'SWEEP 출시, OUSG가 약 2억 달러 앵커 투자. Ondo Stocks 잔액 10억 달러 돌파')
ev('2026-06-11', '경쟁', 'Binance 자체 주식 토큰 bStocks 출시 → 이후 1위를 Binance에 내줌')
ev('2026-07', '직접', 'Ondo Chain 계획 철회 → Ondo Network(주문 실행과 검증만 맡는 층)로 전환. Ondo Perps 출시')
ev('2026-07-02', '인수', 'Oasis Pro TA가 미국 안 보관형 토큰 IVV, MU 발행')
ev('2026-07-15', '제휴', 'DTCC(미국 증권 예탁결제기관) 협업: 경쟁이 아니라 연동(De Bode)')
ev('2026-07-23', '인수', 'FINRA 승인: Oasis Pro Markets가 미국 투자자에게 토큰 주식과 펀드 판매')
ev('2026-08', '변화', '유족이 델라웨어 법원에 경영권 소송. 보유자 200,645명(그중 Ondo Stocks 186,636명, 08-15)')
ev('2026-09', '제휴', '카카오페이증권, 미래에셋 MOU(한국 주식 해외 유통, Global X ETF 토큰화). SBI와 일본 주식 토큰(07 발표)')
ev('2026-09-24', '제휴', 'Intelligent Portfolios 출시(BlackRock 전략, Ondo Stocks로 구성)')
ev('2026-10-05', '직접', 'Ondo Private Markets 발표: 비상장사 주당 가치 연동 노트, 첫 대상은 비상장 AI 기업')
ev('2026-11', '현재', 'OUSG 4개 펀드 분산, Ondo Stocks 450종 이상, 토큰화 주식 2위(24.23%)')

HOWK = {'직접': 'co', '제휴': 'tp', '인수': 'is', '투자': 'fd', '계획': 'tp', '전환': 'is', '규제': 'tp', '성과': 'gr', '변화': 'fd', '경쟁': 'fd', '현재': 'gr'}
for date, how, text, subs, lvl in TL:
    if date == 'PH':
        for c in range(4, 18):
            ws.cell(row=r, column=c).fill = PatternFill('solid', fgColor='F2F2F2')
        put(r, 4, text, bold=True, color='404040')
        mark(1)
        continue
    ws.cell(row=r, column=4).fill = PatternFill('solid', fgColor=COL['co'][0])
    put(r, 4, date, bold=True, color=COL['co'][1])
    ws.cell(row=r, column=5).fill = PatternFill('solid', fgColor=COL['co'][0])
    chip(r, 6, 6, HOWK[how], how, bold=False, size=9)
    ws.cell(row=r, column=6).alignment = Alignment(horizontal='center')
    put(r, 7, text)
    mark(1)
    for s in subs:
        for cc in (4, 5):
            ws.cell(row=r, column=cc).fill = PatternFill('solid', fgColor=COL['co'][0])
        put(r, 7, s)
        mark(2)
blank()

# =====================================================================
band('상품별 돈 흐름 (가상 숫자, 1달러 = 약 1,430원)')

h1('OUSG: 1,000만 원 넣으면')
box(4, 12, 'tp', '① 투자자 (미국 적격투자자 + 적격매수자)', ['1,000만 원 → 약 7,000 USDC(Circle 발행 달러 스테이블코인). 최소 5,000달러라 가능'])
arrows([(7, '↓ 7,000 USDC')])
box(4, 12, 'co', '② Ondo I LP (펀드 자체)', ['OUSG 7,000달러어치 발행. 토큰 값 = 펀드 순자산 ÷ 토큰 수라 이자만큼 계속 오름'])
arrows([(7, '↓ 펀드가 투자자로서 다른 토큰 펀드 지분을 삼 (위탁 계약 아님. 배분은 Ondo Capital Management)')])
FUNDS = [
    ('SWEEP', 48.58, '약 3,400달러', 'State Street, Galaxy. 2026-05 출시, PYUSD 입출금', [
        '정식 이름 State Street Galaxy Onchain Liquidity Sweep Fund. 놀고 있는 스테이블코인을 이자 붙는 곳으로 쓸어 담는다는 뜻',
        '사모 펀드, 적격매수자만. 펀드가 처리할 자산이 있는 한도 안에서 PayPal 스테이블코인 PYUSD로 가입, 환매',
        '2025-12-10 발표, 2026-05-05 Solana 출시, Stellar와 Ethereum 확장 계획',
        'OUSG가 선도 앵커 투자자(lead anchor investor), 약 2억 달러. 그래서 비중 1위',
        '(판단) OUSG의 절반 가까이가 펀드 한 곳에 쏠림. 구성 공시 주기를 봐야 하는 이유']),
    ('BUIDL', 32.69, '약 2,290달러', 'BlackRock. 2024-03 출시, 최소 500만 달러', [
        '정식 이름 BlackRock USD Institutional Digital Liquidity Fund. BVI 설립 펀드',
        '역할: 운용 BlackRock, 명의개서와 토큰화 Securitize, 판매 Securitize Markets, 수탁과 사무관리 BNY Mellon',
        '현금, 단기 국채, 레포 100%. 토큰 1개 1달러 목표, 이자는 매일 토큰 수를 늘려 지급',
        '사모 펀드, 적격매수자만. 개인은 500만 달러가 없어 못 사는 펀드를 OUSG가 작은 돈을 모아 대신 삼']),
    ('BENJI', 10.12, '약 710달러', 'Franklin Templeton. 넷 중 유일한 미국 공모 등록 펀드', [
        '정식 이름 Franklin OnChain U.S. Government Money Fund(FOBXX)',
        '1940년 투자회사법 등록 펀드 중 처음으로 퍼블릭 블록체인에서 거래 처리와 주주 기록. 개인도 Benji 앱으로 투자 가능',
        '총자산 99.5% 이상 정부 증권, 현금, 전액 담보 레포. 1좌 = BENJI 토큰 1개',
        '명의개서대리인이 블록체인 연동 자체 시스템으로 공식 주주 기록 관리',
        '2021 Stellar 시작, 2023-04 Polygon, 2024-04 보유자 간 직접 이전']),
    ('FYOXX', 7.54, '약 530달러', 'Fidelity. 기존 펀드 안 블록체인 기록용 클래스', [
        'Fidelity Treasury Digital Fund(FYHXX)에 OnChain 클래스(FYOXX)를 추가. 토큰 이름 FDIT, 이더리움',
        '2025-03-21 신고, 2025-09 출시. 국채와 국채 담보 레포. 기관 전용, 최소 100만 달러',
        '공식 장부는 블록체인 밖 명의개서대리인 기록. 블록체인 기록은 매일 맞추는 사본',
        '비유: 같은 학교 같은 수업인데 출석부를 블록체인에도 적는 반을 따로 만든 것']),
    ('USDC 현금', 1.14, '약 80달러', 'Coinbase 보관. 환매에 바로 내줄 현금 몫', []),
]
for name, w, amt, desc, subs in FUNDS:
    chip(r, 4, 5, 'tp', name)
    n = max(1, round(w / 10))
    bar(r, 6, n, 'co')
    put(r, 6 + n, f'{w}%  {amt}')
    put(r, 10, desc)
    mark(1)
    for s in subs:
        put(r, 6, s)
        mark(2)
t(3, '네 곳 모두 사는 자산은 거의 같음(단기 국채, 현금, 레포). 차이는 그릇(공모 vs 사모), 장부(블록체인이 원본 vs 사본), 입출금 통로(USDC, PYUSD)')
t(3, '왜 4개로 나누나: 펀드마다 24시간 바로 꺼낼 수 있는 돈에 한도가 있어 여러 곳에 나눠 출금 통로를 넓힘(당시 CEO Allman)')
t(4, '비유: ATM 한 대는 하루 인출 한도가 있으니 여러 은행 ATM을 묶어 씀')
t(4, '변천: 2023 BlackRock 국채 ETF 하나 → 2024-08 BUIDL 거의 전부 → 2025 분산 → 2026 SWEEP 최대 비중')
arrows([(7, '↓ 1년 뒤 (가상 연 4%)')])
box(4, 12, 'co', '③ 이자 약 280달러가 펀드 안에 쌓여 OUSG 약 7,280달러어치', ['운용보수 0.15% = 약 10.5달러지만 2027-01-01까지 면제라 0'])
arrows([(7, '↓ 팔 때')])
box(4, 12, 'tp', '④ 24시간 즉시 환매 → USDC로 받음', ['한도: 24시간 전체 합산 5,000만 달러, 1인 2,500만 달러. Circle USDC 지원이 멈추면 즉시 환매 불가'])
blank()

h1('USDY: 1,000달러 넣으면')
box(4, 12, 'tp', '① 미국 밖 투자자', ['1,000달러(USDC 등) 입금. 최소 500달러, 신원 확인(KYC)'])
arrows([(7, '↓')])
box(4, 12, 'is', '② Ondo Global Markets (BVI) = 발행 법인', ['USDY 1,000달러어치 발행. 받은 돈으로 국채와 SHVon을 직접 삼(2025-12-15 전 발행자는 Ondo USDY LLC)'])
arrows([(7, '↓ 금고 구성 (2026-11-13, 칸 1개 = 10%)')])
for name, w, kind in [('미국 국채', 82.73, 'co'), ('SHVon', 17.24, 'gr')]:
    chip(r, 4, 5, 'tp', name)
    n = max(1, round(w / 10))
    bar(r, 6, n, kind, f'{w}%')
    mark(1)
t(3, 'SHVon은 Ondo Stocks 상품. USDY 금고 안에 Ondo의 다른 상품이 들어 있어 규모 집계에서 겹침')
t(3, '약 3% 손실 완충분: 담보 값이 떨어지면 이 몫부터 깎임. Ondo Finance가 일부를 댐')
arrows([(7, '↓ 1년 이자 (2026-11 수치 적용)')])
chip(r, 4, 5, 'tp', '담보 수익')
bar(r, 6, 8, 'co', '4.10% = 41달러')
mark(1)
chip(r, 4, 5, 'tp', '보유자 몫')
bar(r, 6, 7, 'gr', '3.75% = 37.5달러')
mark(1)
chip(r, 4, 5, 'tp', '발행 쪽 몫')
bar(r, 6, 1, 'is', '0.35% = 3.5달러')
mark(1)
t(3, '비유: 은행이 대출 이자와 예금 이자 차이(예대마진)로 버는 구조와 같음')
arrows([(7, '↓ 누가 지키나')])
box(4, 12, 'tp', '③ Ankura Trust = 검증과 담보 대리', ['담보가 토큰 몫 이상인지 확인. 보유자 대신 담보권을 쥐고 발행 법인이 무너지면 처분해 나눔'])
t(3, '은행 예금을 담을 때 보관처: First Citizens Bank')
t(3, '가격은 이더리움, BNB 체인, Mantle, Tempo 4개 체인에서만 산정. 다른 체인 USDY는 브리지(체인 간 이동 통로)로 옮겨 씀')
blank()

h1('Ondo Stocks: 애플 토큰(AAPLon) 1,000달러어치 사면')
box(4, 12, 'tp', '① 미국 밖 투자자 → 판매 창구에서 주문', ['Bitget(지갑, 거래소), Binance ADGM 거래소, Trust Wallet, MetaMask, EU는 투자설명서 기반'])
arrows([(7, '↓ 체결은 거래소 장부 안. 토큰이 모자라면 →')])
box(4, 12, 'tp', '② 1차 매수자(거래소, 시장조성자)', ['발행 법인에 스테이블코인을 내고 새 토큰을 받음. 상환 수수료와 견적가 차이를 내는 쪽'])
arrows([(7, '↓ 스테이블코인')])
box(4, 12, 'is', '③ Ondo Global Markets (BVI) = 발행 법인', ['받은 돈으로 Alpaca에서 실제 애플 주식 1,000달러어치 매수 → 같은 수량을 담보 계좌에 맡김'])
arrows([(5, '↓ 보관'), (10, '↓ 담보권')])
boxes_side([
    (4, 7, 'tp', 'Alpaca, BitGo Trust', ['주식 매매와 담보 계좌 보관']),
    (9, 12, 'tp', 'Ankura Trust', ['보유자 몫 1순위 담보권']),
])
arrows([(7, '↓ 토큰 발행')])
box(4, 12, 'gr', '④ 투자자 지갑: AAPLon 1,000달러어치', ['애플 10% 오르면 1,100달러. 배당은 토큰 값에 반영. 의결권, 주주명부 등재, 주식 인도 요구 권리 없음'])
t(3, '거래시간: 일요일 밤 8시 ~ 금요일 밤 8시(미국 동부시간). 블록체인: Ethereum, BNB Chain, Solana')
t(3, '외부 지갑으로 옮길 수 있고 LayerZero 브리지로 DeFi 서비스 연동 추진')
t(3, '주의: 탈중앙 거래소 풀에서 NVDA 토큰이 규제 거래소보다 약 9.3% 비싸게 체결된 사례 지적(SEC 제출 의견서, 필자가 Citadel Securities 재정 지원을 밝힘)')
arrows([(7, '↓ 팔 때')])
box(4, 12, 'tp', '⑤ 환매', ['1,100달러어치 상환 → 수수료 0.05% = 0.55달러 + 견적가 차이 → 발행 법인이 주식을 팔고 달러로 돌려줌'])
blank()

h1('Intelligent Portfolios: 토큰 1개 = 포트폴리오 1개')
box(4, 12, 'tp', '① 투자자: BLKGRWon 같은 포트폴리오 토큰 1개를 발행받음(mint)', ['넣고 뺄 때 토큰 하나만 다룸. 직접 비중을 맞출 일 없음'])
arrows([(7, '↓ 토큰 안')])
box(4, 12, 'is', '② Ondo Stocks 바구니 (BVI 발행 법인)', ['종목과 목표 비중은 BlackRock 전략 기반, 출시 때 고정. 정해진 일정마다 스마트컨트랙트가 자동 리밸런싱'])
arrows([(7, '↓ 바구니 속 각 종목')])
box(4, 12, 'tp', '③ 각 Ondo Stocks → 실제 주식, ETF (Alpaca, BitGo 보관, Ankura 담보권)', ['위 Ondo Stocks 흐름과 같은 금고 구조'])
t(3, 'BlackRock은 전략만 넘기고 운용 판단은 안 함. 구현과 리밸런싱 실행은 Ondo')
t(3, '회사 구상: 앞으로 무기한선물, 가상자산, 옵션까지 담는 포트폴리오로 확장')
t(3, '수입: 연 서비스 수수료')
blank()

# =====================================================================
band('주의할 점')
h1('상환 한도, 쏠림, 경영권, 점유율')
t(2, 'OUSG 즉시 상환 한도 24시간 합산 5,000만 달러. 한도가 찬 날이나 USDC 지원이 멈춘 날은 즉시 현금화 불가')
t(2, 'OUSG의 48.58%가 펀드 한 곳(SWEEP)')
t(2, '창업자 사망 뒤 경영권 소송 진행 중(2026-08 제기)')
t(2, '토큰화 주식 점유율 51.59%(2026-01) → 24.23%(2026-11). 잔액은 2배 넘게 늘었지만 Binance에 1위 내줌')
t(2, '토큰 주식은 주식 발행 기업 동의 없는 제3자 토큰. 기업과 보유자 사이 권리 관계 없음')
blank()

# =====================================================================
band('공식 사이트')
OFFICIAL = [
    ('Ondo Finance 홈페이지', 'https://ondo.finance/'),
    ('OUSG 상품 페이지', 'https://ondo.finance/ousg'),
    ('USDY 상품 페이지', 'https://ondo.finance/usdy'),
    ('Ondo Stocks 상품 페이지', 'https://ondo.finance/ondo-stocks'),
    ('Ondo 팀 페이지', 'https://ondo.finance/team'),
    ('Ondo 블로그와 리서치(Insights)', 'https://ondo.finance/insights'),
    ('Ondo 문서(docs) OUSG 개요', 'https://docs.ondo.finance/qualified-access-products/ousg/overview'),
    ('Ondo 문서(docs) USDY 기본', 'https://docs.ondo.finance/general-access-products/usdy/basics'),
    ('Ondo 문서(docs) Ondo Stocks 개요', 'https://docs.ondo.finance/ondo-stocks/overview'),
    ('Ondo 약관(Terms of Service)', 'https://docs.ondo.finance/legal/terms-of-service'),
    ('Ondo Foundation: ONDO 토큰', 'https://docs.ondo.foundation/ondo-token'),
]
for name, url in OFFICIAL:
    c = put(r, 4, name, color='0563C1')
    c.hyperlink = url
    c.font = F(color='0563C1', u='single')
    put(r, 9, url, size=9, color=GRAY)
    mark(1)
blank()

# =====================================================================
band('raw data (근거 자료, 클릭하면 열림)')
srcs = json.load(open('/home/claude/ondo_srcs.json'))
EXTRA = [
    ('The Block: State Street, Galaxy SWEEP 출시', 'SWEEP', 'https://www.theblock.co/news/business/2026-05-05-state-street-and-galaxy-launch-fund-on-solana-designed-to-sweep-stablecoins-into-productive-vehicle-400086'),
    ('Yahoo Finance: SWEEP 출시 예고, Ondo 2억 달러', 'SWEEP', 'https://finance.yahoo.com/news/state-street-galaxy-launch-tokenized-223000391.html'),
    ('Markets Media: SWEEP 체인 계획', 'SWEEP', 'https://www.marketsmedia.com/state-street-galaxy-to-launch-tokenized-money-market-fund/'),
    ('Whale Alert: OUSG 앵커 투자자', 'SWEEP', 'https://whale-alert.io/stories/ddaf0134c3235a/State-Street-and-Galaxy-launch-Solana-based-SWEEP-tokenized-cash-fund-with-200M-anchor-from-Ondo'),
    ('Eco: BUIDL 구조', 'BUIDL', 'https://eco.com/support/en/articles/15483226'),
    ('Capital Tokenization: BUIDL BVI 설립', 'BUIDL', 'https://capitaltokenization.pages.dev/entities/blackrock-buidl-tokenized-fund/'),
    ('Franklin Templeton 보도자료: BENJI', 'BENJI', 'https://www.franklintempleton.com/press-releases/news-room/2023/franklin-templeton-announces-the-franklin-onchain-u.s.-government-money-fund-surpasses-usd270-million-in-assets-under-management'),
    ('Polygon 블로그: Franklin 펀드', 'BENJI', 'https://polygon.technology/blog/franklin-templeton-money-market-fund-launches-on-polygon-blockchain'),
    ('DefiLlama: Fidelity FYOXX', 'FYOXX', 'https://defillama.com/rwa/platform/fidelity'),
    ('Benzinga: Fidelity OnChain 클래스 신고', 'FYOXX', 'https://www.benzinga.com/content/44452093/fidelity-joins-the-tokenization-trend-with-on-chain-treasury-fund-filing'),
    ('Blockhead: Fidelity FDIT 출시', 'FYOXX', 'https://www.blockhead.co/2025/09/08/fidelity-quietly-launches-200m-ethereum-based-treasury-fund'),
]
rows = []
for title, label, url, sec in srcs:
    for u in url.split(';'):
        u = u.strip()
        if not u:
            continue
        tt = title if not title.startswith('http') else u.split('/')[2]
        rows.append((sec or '기타', tt, label, u))
groups = {}
for sec, tt, label, u in rows:
    groups.setdefault(sec, []).append((tt, label, u))
groups['OUSG가 담은 펀드 4개'] = [(a, b, c) for a, b, c in EXTRA]
for sec, items in groups.items():
    put(r, 4, f'{sec} ({len(items)}건)', bold=True)
    mark(1)
    for tt, label, u in items:
        c = put(r, 5, tt, color='0563C1')
        c.hyperlink = u
        c.font = F(color='0563C1', u='single')
        if label:
            put(r, 12, f'확인한 항목: {label}', size=9, color=GRAY)
        mark(2)

# ------------------------------------------------------------------ outline
maxr = r
for row in range(1, maxr):
    lv = levels.get(row, 0)
    rd = ws.row_dimensions[row]
    if lv > 0:
        rd.outline_level = lv
    if lv >= 2 and not EXPAND:
        rd.hidden = True
for row in range(1, maxr):
    lv = levels.get(row, 0)
    nx = levels.get(row + 1, 0)
    if nx > lv and nx >= 2 and not EXPAND:
        ws.row_dimensions[row].collapsed = True
ws.sheet_format.outlineLevelRow = 3
ws.sheet_view.zoomScale = 100
ws.sheet_view.selection[0].activeCell = 'A1'
ws.sheet_view.selection[0].sqref = 'A1'
wb.save(OUT)
print('rows', maxr, OUT)
