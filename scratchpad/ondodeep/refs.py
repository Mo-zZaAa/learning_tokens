"""출처 키(F-, on-, S-, DB-, ONM-, ONM2-, DL-)를 원문 인용과 링크로 바꾼다."""
import csv, json, re
from pathlib import Path

ROOT = Path('/home/user/learning_tokens')
PKG = ROOT / 'inputs/ondo_deep_261118'


def _csv(p):
    return list(csv.DictReader(open(p, encoding='utf-8-sig')))


FACTS = {r['fact_id']: r for r in _csv(ROOT / 'db/facts.csv')}
SRCS = {r['source_id']: r for r in _csv(ROOT / 'db/sources.csv')}
ONM = {}
for p in ['work/ONMEMO/facts.csv', 'work/ONMEMO2/facts.csv']:
    if (ROOT / p).exists():
        for r in _csv(ROOT / p):
            ONM[r['fact_id']] = r
ONROWS = json.load(open(ROOT / 'scratchpad/ondodeep/onrows.json', encoding='utf-8'))
PSRC = {r['id']: r for r in _csv(PKG / 'data/sources.csv')}

DL = {
    'DL-fees': dict(t='DefiLlama 공개 API: Ondo Finance 수수료(fees)와 정의(2026-11-18 받음)',
                    q="Fees: The daily yield earned by USDY and OUSG holders, calculated as each token's price increase over the day times the amount of tokens in circulation. Revenue: Zero. Ondo passes all of this yield to token holders and currently charges no fee (USDY has no fee, OUSG's 0.15% fee is waived until 2027).",
                    url='https://api.llama.fi/summary/fees/ondo-finance?dataType=dailyFees'),
    'DL-rev': dict(t='DefiLlama 공개 API: Ondo Finance 수입(revenue) 일별 값(2026-11-18 받음, 전 기간 0)',
                   q='totalAllTime: 0, total1y: 0 (dataType=dailyRevenue)',
                   url='https://api.llama.fi/summary/fees/ondo-finance?dataType=dailyRevenue'),
    'DL-vol': dict(t='DefiLlama 공개 API: Ondo Global Markets(Ondo Stocks) 일별 매매액(2026-11-18 받음)',
                   q='Volume: Buy and sell volume of Ondo tokenized stocks and ETFs on Ondo Global Markets: on Ethereum and BNB Chain from on-chain TradeExecuted events, and on Solana from the program mint/redeem trades (price times quantity) routed through Jupiter.',
                   url='https://api.llama.fi/summary/dexs/ondo-global-markets?dataType=dailyVolume'),
    'DL-proto': dict(t='DefiLlama 공개 API: Ondo Finance 하위 프로토콜 목록과 TVL 배열(2026-11-18 받음)',
                     q='otherProtocols: Ondo Finance, Ondo Yield Assets, Ondo Global Markets, Ondo Perps; tvl: [] (TVL 배열 비어 있음)',
                     url='https://api.llama.fi/protocol/ondo-finance'),
}


def clean(s):
    s = (s or '').replace('—', ' - ').replace('–', '-').replace('·', ', ').replace('・', ', ')
    s = s.replace('제공', '내줌')
    return re.sub(r'\s+', ' ', s).strip()


def first_url(u):
    return (u or '').split(';')[0].strip()


def resolve(key):
    """반환: dict(label, items=[{t,q,url}])"""
    if key in DL:
        d = DL[key]
        return dict(label=key, items=[dict(t=clean(d['t']), q=clean(d['q']), url=d['url'])])
    if key.startswith('F-'):
        r = FACTS[key]
        s = SRCS.get(r['source_id'], {})
        t = s.get('제목') or r['링크']
        return dict(label=key, items=[dict(t=clean(t), q=clean(r['원문 근거 문장']), url=first_url(r['링크']))])
    if key.startswith('ONM'):
        r = ONM[key]
        u = first_url(r['링크'])
        if not u.startswith('http'):
            raise KeyError(key + ' 링크 없음')
        return dict(label=key, items=[dict(t=clean(u.split('/')[2] + ' ' + (r['기준일'] or r['열람 일시'])), q=clean(r['원문 근거 문장']), url=u)])
    if key.startswith('on-'):
        r = ONROWS[key]
        items = [dict(t=clean(s.get('t', '')), q=clean(s.get('q', '')), url=first_url(s.get('url', ''))) for s in r['src']]
        return dict(label=key, items=items)
    if key.startswith('S-') or key.startswith('DB-'):
        r = PSRC[key]
        if not r['링크']:
            raise KeyError(key + ' 링크 없음')
        return dict(label=key, items=[dict(t=clean(r['제목']), q='', url=r['링크'])])
    raise KeyError(key)
