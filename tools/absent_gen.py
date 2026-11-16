"""템플릿 ★칸 중 본문에 없는 칸을 work/MAIN/absent.csv로 기록."""
import csv, re, glob, os
TPL = {'기본정보': ['법인명','소재지','설립 시기','상장 현황'], '지배구조': ['모회사','주요 주주'],
 '취득 라이선스 및 근거 법령': ['미국','미국 외'], '토큰증권 사업 진출 배경': ['출발 사업과의 관계','진출 사유'],
 '향후 방향': ['경영진 발표 원문','해석'], '상품 기초자산': ['전통증권','토큰증권','가상자산','파생상품 및 기타'],
 '서비스 범위': ['발행','매매 체결','청산','결제','수탁 및 권리 기록','고객 접점'],
 '최종 투자자': ['대상','국적 및 지역 제한'], '발행 구조': ['발행 주체','법적 성격','기초자산 보관','투자자 권리'],
 '거래 구조': ['거래 방식','유동성 확보 방안','거래시간','사용 블록체인']}
MID = ['설립 목적','수익원','타깃 수요','핵심 성공요인(KSF)','제약 및 리스크','국내 관련 사업 동향','수요 비교','주요 사례(해당 시)','향후 방향']
NAME = {'Blue_Ocean_ATS':'Blue Ocean','Bruce_ATS':'Bruce','MOON_ATS':'MOON','Kraken':'Kraken','Robinhood':'Robinhood','Binance':'Binance','Coinbase':'Coinbase','Dinari':'Dinari','Ondo':'Ondo'}
facts = list(csv.DictReader(open('db/facts.csv', encoding='utf-8')))
out = []
for p in sorted(glob.glob('companies/*.md')):
    key = os.path.basename(p)[:-3]; comp = NAME[key]; ats = 'ATS' in key
    txt = open(p, encoding='utf-8').read()
    cf = [f for f in facts if comp.lower() in f['회사'].lower() or (comp=='Kraken' and 'payward' in f['회사'].lower())]
    for mid, items in TPL.items():
        for it in items:
            if re.search(r'★ ' + re.escape(it) + r' :', txt): continue
            if ats and mid in ('발행 구조','토큰증권 사업 진출 배경','상품 기초자산') :
                out.append([comp, f'{mid} > {it}', '필요 없어 제외', 'ATS는 거래 사업만 다룸(지시문 7절)', '']); continue
            single = sum(1 for f in cf if it in f['틀 항목'] and f['검증 상태'] not in ('1차 출처 확인','교차 확인'))
            if mid == '상품 기초자산' or it in ('매매 체결','청산','결제','유동성 확보 방안'):
                why = '해당 칸에 쓸 1차, 교차 확인 사실 없음(사업에 해당 없거나 다른 칸과 합침)'
            else:
                why = '1차, 교차 확인 사실 없음' + (f'. DB에 같은 틀 항목 단일 출처 {single}건' if single else '')
            out.append([comp, f'{mid} > {it}', '찾았으나 공개 자료 없음' if single or mid not in ('상품 기초자산',) else '필요 없어 제외', why, '공식 사이트 notes와 위키, work/EXT-*, 등록부(FINRA BrokerCheck, ESMA, NY DFS)'])
    for m in MID:
        if ('● ' + m) not in txt:
            out.append([comp, m, '찾았으나 공개 자료 없음', '1차, 교차 확인 사실 없어 중분류 삭제', '공식 사이트 notes와 위키, work/EXT-*'])
w = csv.writer(open('work/MAIN/absent.csv', 'w', encoding='utf-8', newline=''))
w.writerow(['회사','항목','구분','사유','찾아본 곳']); w.writerows(out)
print(len(out))
