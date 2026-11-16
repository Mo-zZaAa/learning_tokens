"""기업별틀 엑셀을 조사 틀 A~H 기준으로 다시 짠다. 위쪽 요약(1~17행)과 서식은 원본을 따른다."""
import openpyxl, copy, sys
src, dst = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src)
FRAME = [
 ('A 출신과 진입', [
   ('● 출신 : ', []),
   ('● 기본정보', ['★ 법인명 : ', '★ 소재지 : ', '★ 설립 시기 : ', '★ 상장 현황 : ', '★ 회사 실적(수치, 기준일) : ']),
   ('● 지배구조', ['★ 모회사 : ', '★ 주요 주주 : ']),
   ('● 설립 목적', ['★ ']),
   ('● 진입 시점', ['★ 주식 토큰 시작 : ', '★ 중단과 재개 : ']),
   ('● 진입 방식', ['★ 직접 개발, 인수, 남의 상품 판매 : ', '★ 진출 사유(회사가 밝힌 이유) : ']),
   ('● 확장 경로', ['★ 1단계(기간) : ', '① ', '★ 2단계(기간) : ', '① ']),
   ('● 향후 방향', ['★ 경영진 발표 원문 : ', '★ 해석 : ']),
 ]),
 ('B 상품 구조', [
   ('● 대상 상품 : ', []),
   ('● 상품 범위', ['★ 전통증권 : ', '★ 토큰증권 : ', '★ 가상자산 : ', '★ 파생상품 및 기타 : ']),
   ('● 토큰의 법적 성격', ['★ ']),
   ('● 발행 주체', ['★ ']),
   ('● 투자자 권리', ['★ 배당 : ', '★ 의결권 : ', '★ 실물 주식 전환 : ']),
   ('● 기초 주식 보관', ['★ ']),
   ('● 규모', ['★ 지표(수치, 산정 기준, 기준일) : ']),
   ('● 수수료와 수익원', ['★ 거래, 발행, 상환 수수료 : ', '★ 수익원 : ']),
 ]),
 ('C 최종 투자자', [
   ('● 대상', ['★ ']),
   ('● 국적 및 지역 제한', ['★ 미국 투자자 : ', '★ 제외 지역 : ']),
   ('● 최소 투자금액', ['★ ']),
   ('● 타깃 수요', ['★ ']),
 ]),
 ('D 유통과 접점', [
   ('● 자체 접점', ['★ ']),
   ('● 거래 장소', ['★ 거래 방식 : ']),
   ('● 공급 방식', ['★ 주요 사례(제공 내용, 대상 고객, 제공 방식) : ']),
   ('● 거래시간', ['★ ']),
   ('● 사용 블록체인', ['★ ']),
   ('● 유동성 확보 방안', ['★ ']),
 ]),
 ('E 인가', [
   ('● 보유 인가와 법인', ['★ 미국 : ', '★ 미국 외 : ']),
   ('● 취득 시점과 방식', ['★ ']),
   ('● 인가로 하는 사업과 개시 시점', ['★ 발행 : ', '★ 매매 체결 : ', '★ 청산 : ', '★ 결제 : ', '★ 수탁 및 권리 기록 : ', '★ 고객 접점 : ']),
   ('● 인가 없는 구간을 메우는 방법', ['★ ']),
   ('● 제재와 사고', ['★ ']),
 ]),
 ('F 관계(해당 시)', [
   ('● 인수, 투자, 제휴', ['★ ']),
   ('● 보관과 청산 제공, 상품 공급', ['★ ']),
   ('● 경쟁', ['★ ']),
 ]),
 ('G 한국 접점(해당 시)', [
   ('● 한국 회사와의 협약', ['★ ']),
   ('● 한국 주식 취급', ['★ ']),
   ('● 한국 투자자 대상 판매', ['★ ']),
   ('● 국내 적용 시 걸리는 제도', ['★ 쟁점 : ', '① 현지 제도 : ', '② 국내 제도 : ', '③ 국내 적용 시 결과 : ']),
   ('● 수요 비교', ['★ 비교 항목 : ', '① 현지 : ', '② 국내 : ', '③ 차이의 의미 : ']),
 ]),
 ('판단(KDX 관점)', [
   ('● 핵심 성공요인(KSF)', ['★ ']),
   ('● 제약 및 리스크', ['★ ']),
   ('● 벤치마킹 요소', ['★ ']),
   ('● 한계 및 유의사항', ['★ ']),
 ]),
]
SUMMARY = ['● A 출신과 진입', '● B 상품 구조', '● C 최종 투자자', '● D 유통과 접점', '● E 인가', '● F 관계', '● G 한국 접점', '● 판단(KDX 관점)']
def style(dst_cell, src_cell):
    dst_cell.font = copy.copy(src_cell.font); dst_cell.fill = copy.copy(src_cell.fill)
    dst_cell.alignment = copy.copy(src_cell.alignment); dst_cell.border = copy.copy(src_cell.border)
company_sheets = [ws for ws in wb.worksheets if ws['B19'].value == '기업 개요']
for ws in company_sheets:
    sec_s, mid_s, item_s, sub_s = [copy.copy(ws[a]) for a in ('B19', 'B20', 'C21', 'D40')]
    sum_head, sum_item = copy.copy(ws['B8']), copy.copy(ws['C9'])
    # 요약 칸(8~17행)을 새 대분류로
    for r in range(8, ws.max_row + 1):
        for c in range(1, ws.max_column + 1):
            cell = ws.cell(r, c); cell.value = None
            cell.font = copy.copy(ws['A1'].font); cell.fill = copy.copy(ws['A1'].fill); cell.border = copy.copy(ws['A1'].border)
    r = 8
    for s in SUMMARY:
        ws.cell(r, 2, s); style(ws.cell(r, 2), sum_head)
        for c in range(3, ws.max_column + 1): style(ws.cell(r, c), sum_head)
        ws.cell(r + 1, 3, '◎ '); style(ws.cell(r + 1, 3), sum_item)
        r += 2
    r += 1
    for sec, mids in FRAME:
        ws.cell(r, 2, sec); 
        for c in range(2, ws.max_column + 1): style(ws.cell(r, c), sec_s)
        r += 1
        for mid, items in mids:
            ws.cell(r, 2, mid); style(ws.cell(r, 2), mid_s); r += 1
            for it in items:
                col = 4 if it[0] in '①②③' else 3
                ws.cell(r, col, it); style(ws.cell(r, col), sub_s if col == 4 else item_s); r += 1
            r += 1
# H 제도와 시장: 한미 제도 비교 시트에 공통 소분류 추가
ws = wb['한미 제도 비교']
last = ws.max_row
for i, (a, b) in enumerate([('H 제도와 시장', '인가별 절차와 소요 기간'), ('', '등록된 곳 수'), ('', '가상자산과 증권 인가 체계의 차이'), ('', '규제 변화 연표')], 1):
    ws.cell(last + i, 1, a); ws.cell(last + i, 2, b)
    for c in range(1, 6): style(ws.cell(last + i, c), ws.cell(last, c))
wb.save(dst)
print('sheets', [w.title for w in company_sheets])
