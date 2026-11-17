import csv, os, re, html, sys
ROOT='/home/user/learning_tokens'
S=ROOT+'/sources/S2-ON/'
ST=ROOT+'/sources/STORY-Ondo/'
DAY='2026-11-17'
B='https://ondo.finance/blog/'
D='https://docs.ondo.finance/'
src=[
# id, title, publisher, date, kind, lang, link, path
('S2ON-S01','Ondo Raises $4M to Balance Risk and Reward for the DeFi Ecosystem','Ondo Finance','2021-08-17','회사 블로그','en',B+'ondo-raises-4m-to-balance-risk-and-reward-for-the-defi-ecosystem','sources/S2-ON/b_ondo-raises-4m-to-balance-risk-and-reward-for-the-defi-ecosystem.html'),
('S2ON-S02','Ondo Bi-Monthly Recap | Apr-May 2022','Ondo Finance','2022-05-12','회사 블로그','en',B+'ondo-bimonthly-recap-apr-may-2022','sources/S2-ON/b_ondo-bimonthly-recap-apr-may-2022.html'),
('S2ON-S03','ONDO Token Sale on CoinList Drives Over 18,000 New Token Holders','Ondo Finance','2022-07-06','회사 블로그','en',B+'ondo-token-sale-on-coinlist-drives-over-18-000-new-token-holders','sources/S2-ON/b_ondo-token-sale-on-coinlist-drives-over-18-000-new-token-holders.html'),
('S2ON-S04','The ONDO Token','Ondo Foundation','','회사 문서','en','https://docs.ondo.foundation/ondo-token','sources/S2-ON/foundation_ondo-token.html'),
('S2ON-S05','Introduction (Ondo Foundation Docs)','Ondo Foundation','','회사 문서','en','https://docs.ondo.foundation/','sources/S2-ON/foundation_intro.html'),
('S2ON-S06','Introducing Ondo USD Yield (USDY)','Ondo Finance','2023-08-03','회사 블로그','en',B+'introducing-ondo-usd-yield-usdy','sources/S2-ON/b_introducing-ondo-usd-yield-usdy.html'),
('S2ON-S07','Ondo USDY LLC Registers with FinCEN','Ondo Finance','2024-03-14','회사 블로그','en',B+'ondo-usdy-llc-registers-with-fincen','sources/S2-ON/b_ondo-usdy-llc-registers-with-fincen.html'),
('S2ON-S08','USDY product page','Ondo Finance','2026-11-16','회사 사이트','en','https://ondo.finance/usdy','sources/S2-ON/p_usdy.html'),
('S2ON-S09','USDY Basics','Ondo Finance','','회사 문서','en',D+'general-access-products/usdy/basics.md','sources/S2-ON/docs_general-access-products_usdy_basics.md'),
('S2ON-S10','OUSG Overview','Ondo Finance','','회사 문서','en',D+'qualified-access-products/ousg/overview.md','sources/S2-ON/docs_qualified-access-products_ousg_overview.md'),
('S2ON-S11','OUSG Yield','Ondo Finance','','회사 문서','en',D+'qualified-access-products/ousg/yield.md','sources/S2-ON/docs_qualified-access-products_ousg_yield.md'),
('S2ON-S12','OUSG Other','Ondo Finance','','회사 문서','en',D+'qualified-access-products/ousg/other.md','sources/S2-ON/docs_qualified-access-products_ousg_other.md'),
('S2ON-S13','Ondo Finance Makes $25M Strategic Investment in YLDS','Ondo Finance','2025-11-24','회사 블로그','en',B+'ondo-ylds-25m-investment','sources/STORY-Ondo/b_ondo-ylds-25m-investment.html'),
('S2ON-S14','State Street, Galaxy and Ondo announce SWEEP','Ondo Finance','2025-12-10','회사 블로그','en',B+'state-street-galaxy-ondo-tokenized-sweep-fund','sources/S2-ON/b_state-street-galaxy-ondo-tokenized-sweep-fund.html'),
('S2ON-S15','Ondo Finance Acquires Strangelove','Ondo Finance','2025-07-14','회사 블로그','en',B+'ondo-finance-acquires-strangelove','sources/S2-ON/b_ondo-finance-acquires-strangelove.html'),
('S2ON-S16','Ondo Finance to Acquire Oasis Pro','Ondo Finance','2025-07-04','회사 블로그','en',B+'ondo-finance-to-acquire-oasis-pro','sources/STORY-Ondo/b_ondo-finance-to-acquire-oasis-pro.html'),
('S2ON-S17','Ondo Finance Completes Acquisition of Oasis Pro','Ondo Finance','2025-10-07','회사 블로그','en',B+'ondo-acquires-oasis-pro','sources/STORY-Ondo/b_ondo-acquires-oasis-pro.html'),
('S2ON-S18','BrokerCheck: OASIS PRO MARKETS LLC (CRD 149420)','FINRA','','감독기관 등록부','en','https://api.brokercheck.finra.org/search/firm/149420','sources/S2-ON/brokercheck_149420_content.json'),
('S2ON-S19','FINRA Rule 1014. Department Decision','FINRA','','감독기관 규칙','en','https://www.finra.org/rules-guidance/rulebooks/finra-rules/1014','sources/S2-ON/finra_rule_1014.html'),
('S2ON-S20','Ondo Finance Launches First-Ever Custodial Tokenized Securities in the U.S.','Ondo Finance','2026-07-02','회사 블로그','en',B+'ondo-launches-tokenized-securities-in-usa','sources/STORY-Ondo/b_ondo-launches-tokenized-securities-in-usa.html'),
('S2ON-S21','Ondo Finance’s Oasis Pro Markets Secures FINRA Authorizations','Ondo Finance','2026-07-23','회사 블로그','en',B+'finra-authorizations-to-offer-tokenized-equities','sources/STORY-Ondo/b_finra-authorizations-to-offer-tokenized-equities.html'),
('S2ON-S22','Ondo API Overview','Ondo Finance','','회사 문서','en',D+'api-reference/overview.md','sources/S2-ON/docs_api-reference_overview.md'),
('S2ON-S23','Token & Quote Pricing','Ondo Finance','','회사 문서','en',D+'ondo-stocks/token-and-quote-pricing.md','sources/S2-ON/docs_ondo-stocks_token-and-quote-pricing.md'),
('S2ON-S24','Convert Shares to Tokenized Stocks','Ondo Finance','2026-09-21','회사 블로그','en',B+'convert-shares-to-tokenized-stocks','sources/STORY-Ondo/b_convert-shares-to-tokenized-stocks.html'),
('S2ON-S25','Intelligent Portfolios Fees & Taxes','Ondo Finance','','회사 문서','en',D+'intelligent-portfolios/fees-taxes.md','sources/S2-ON/docs_intelligent-portfolios_fees-taxes.md'),
('S2ON-S26','Introducing Ondo Global Listing','Ondo Finance','2026-02-03','회사 블로그','en',B+'introducing-ondo-global-listing','sources/S2-ON/b_introducing-ondo-global-listing.html'),
('S2ON-S27','Ondo Partners with Mirae Asset','Ondo Finance','2026-06-16','회사 블로그','en',B+'ondo-partners-with-mirae-asset','sources/S2-ON/b_ondo-partners-with-mirae-asset.html'),
('S2ON-S28','Ondo and SBI Group Partner to Bring Japanese Equities Onchain','Ondo Finance','2026-07-16','회사 블로그','en',B+'ondo-partners-with-sbi-group','sources/S2-ON/b_ondo-partners-with-sbi-group.html'),
('S2ON-S29','Ondo and Kakaopay Securities Partner','Ondo Finance','2026-09-29','회사 블로그','en',B+'ondo-and-kakaopay-securities-partner','sources/STORY-Ondo/b_ondo-and-kakaopay-securities-partner.html'),
('S2ON-S30','Tokenized Treasuries (RWA.xyz)','RWA.xyz','2026-11-17','제3자 데이터','en','https://app.rwa.xyz/treasuries','sources/S2-ON/rwa_treasuries.html'),
('S2ON-S31','DefiLlama fees and revenue: Ondo Finance','DefiLlama','2026-11-17','제3자 데이터','en','https://api.llama.fi/summary/fees/ondo-finance?dataType=dailyRevenue','sources/S2-ON/llama_rev_ondo.json'),
('S2ON-S32','Introducing Ondo Perps','Ondo Finance','2026-02-03','회사 블로그','en',B+'introducing-ondo-perps','sources/STORY-Ondo/b_introducing-ondo-perps.html'),
('S2ON-S33','Ondo Stocks now integrated with Bitget','Ondo Finance','2026-03-16','회사 블로그','en',B+'ondo-global-markets-live-on-bitget','sources/STORY-Ondo/b_ondo-global-markets-live-on-bitget.html'),
('S2ON-S34','Introducing Ondo Finance','Ondo Finance','2021-07-27','회사 블로그','en',B+'introducing-ondo-finance','sources/S2-ON/b_introducing-ondo-finance.html'),
]
srcd={s[0]:s for s in src}
def norm(t):
    t=html.unescape(t); t=re.sub(r'<[^>]+>',' ',t); t=t.replace('\\$','$'); t=re.sub(r'\s+',' ',t); return t
cache={}
def text_of(path):
    if path not in cache:
        p=ROOT+'/'+path
        alt=p.rsplit('.',1)[0]+'.txt'
        t=open(p,encoding='utf-8',errors='replace').read()
        if os.path.exists(alt) and p.endswith('.html'): t+= '\n'+open(alt,encoding='utf-8',errors='replace').read()
        cache[path]=norm(t)
    return cache[path]
F=[]
def f(sid, 회사, 법인, 소재지, 시작, 상태, 자산, 위치, 기능, 무엇을, 누구에게, 방식, 인가, 값, 단위, 잰것, 기준일, 이유, 틀, quote, 위치원문, 검증):
    path=srcd[sid][7]
    q=norm(quote)
    assert q in text_of(path), (sid, quote[:80])
    F.append(dict(zip(["회사","사업 법인","법인 소재지","시작(연월)","끝 또는 현재","상태","자산 유형","밸류체인 위치","세부 기능","무엇을","누구에게","어떤 방식으로","근거 인가","관련 조문 ID","값","단위","무엇을 잰 것","기준일","회사가 밝힌 이유","앞선 fact_id","틀 항목","source_id","링크","원문 근거 문장","원문 위치","검증 상태","열람 일시"],
      [회사,법인,소재지,시작,'',상태,자산,위치,기능,무엇을,누구에게,방식,인가,'',값,단위,잰것,기준일,이유,'',틀,sid,srcd[sid][6],quote,위치원문,검증,DAY])))
exec(open(sys.argv[1],encoding='utf-8').read())
cols=["fact_id","회사","사업 법인","법인 소재지","시작(연월)","끝 또는 현재","상태","자산 유형","밸류체인 위치","세부 기능","무엇을","누구에게","어떤 방식으로","근거 인가","관련 조문 ID","값","단위","무엇을 잰 것","기준일","회사가 밝힌 이유","앞선 fact_id","틀 항목","source_id","링크","원문 근거 문장","원문 위치","검증 상태","열람 일시"]
used=set()
with open(ROOT+'/work/S2-ON/facts.csv','w',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,quoting=csv.QUOTE_ALL); w.writerow(cols)
    for i,r in enumerate(F,1):
        r['fact_id']='S2ON-%03d'%i; used.add(r['source_id']); w.writerow([r[c] for c in cols])
with open(ROOT+'/work/S2-ON/sources.csv','w',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,quoting=csv.QUOTE_ALL); w.writerow(["source_id","제목","발행 주체","발행일","출처 종류","언어","링크","저장 파일 경로","캡처 파일","접근 결과","열람 일시"])
    for s in src:
        if s[0] in used:
            w.writerow([s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],'','열람 성공(curl)' if 'STORY-Ondo' not in s[7] else '저장본 재열람(sources/STORY-Ondo)',DAY])
print(len(F),'facts',len(used),'sources; unused:',[s[0] for s in src if s[0] not in used])
