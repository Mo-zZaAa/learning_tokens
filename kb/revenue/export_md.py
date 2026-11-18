"""매출로 본 성공 원인(4개사와 공통)을 다른 Claude가 찾아 인용하기 쉬운 md 한 파일로 묶음.
출처 절, 링크, 막대 그림 블록, 저장소 경로를 빼고, 절마다 [RH-2.1] 같은 고정 번호를 붙임.
사용법: python3 -I kb/revenue/export_md.py  → deliverables/매출로본성공원인_4개사_261118.md"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "kb/revenue"
OUT = ROOT / "deliverables/매출로본성공원인_4개사_261118.md"
COS = [("00_공통", "ALL", "네 회사 비교"), ("robinhood", "RH", "Robinhood"), ("coinbase", "CB", "Coinbase"),
       ("kraken", "KR", "Kraken(Payward)"), ("binance", "BN", "Binance")]
URL = re.compile(r"https?://\S+")
PATH = re.compile(r"\b(?:kb|db|work|sources|inputs|web)/[\w./가-힣-]+")


def clean_line(s):
    if re.match(r"^\s*-\s*(숫자 )?출처[:\s]", s) or re.match(r"^\s*-\s*기준: .*출처", s) and "출처:" in s.split("기준:")[1][:6]:
        return None
    s = re.sub(r"\(본 곳:[^)]*\)", "", s)
    s = re.sub(r"\s*본 곳:[^.)]*", "", s)
    s = re.sub(r"\[([^\]]+)\]\(https?://[^)]+\)", r"\1", s)  # 마크다운 링크는 글만
    s = URL.sub("", s)
    s = PATH.sub("", s)
    s = re.sub(r"\(\s*\)", "", s)
    return s.rstrip()


def convert(text, code, title):
    out, sec, sub, q = [], None, 0, 0
    lines = text.splitlines()
    i = 0
    in_fence = False
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            # 막대 그림 블록은 표와 같은 숫자라 뺌
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            i = j + 1
            continue
        if ln.startswith("# "):
            out.append(f"## [{code}] {title}")
            i += 1
            continue
        m = re.match(r"^## (.*)$", ln)
        if m:
            h = m.group(1).strip()
            if re.match(r"^(\d+\.\s*)?출처", h):
                break  # 출처 절부터 끝까지 뺌
            n = re.match(r"^(\d+)\.\s*(.*)$", h)
            sec = n.group(1) if n else "0"
            sub, q = 0, 0
            out.append(f"### [{code}-{sec}] {n.group(2) if n else h}")
            i += 1
            continue
        m = re.match(r"^### (.*)$", ln)
        if m:
            sub += 1
            out.append(f"#### [{code}-{sec}.{sub}] {m.group(1).strip()}")
            i += 1
            continue
        # 의문과 답 절의 맨 위 불릿에 번호
        if sec == "4" and code != "ALL" and re.match(r"^- ", ln) or (code == "ALL" and sec == "4" and re.match(r"^- ", ln)):
            q += 1
            ln = f"- [{code}-4.Q{q}] " + ln[2:]
        c = clean_line(ln)
        if c is not None:
            out.append(c)
        i += 1
    # 빈 줄 겹침 정리
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip() + "\n"


HEAD = """# 네 회사 매출로 본 성공 원인: 조사 결과 (2026-11-18)

## 이 문서를 쓰는 법
- 대상: Robinhood, Coinbase, Kraken(모회사 Payward), Binance. 발행이 주력인 Ondo, Dinari는 뺌
- 질문: 이 회사가 커졌다 → 무엇이 커졌나 → 돈은 어디서 벌었나 → 그 사업이 이 회사에서 왜 됐나(먼저 해서 / 더 뛰어나서 / 접근이 달라서) → 같은 사업을 지금 남이 하면 되나
- 인용 번호: 절마다 [회사-절] 꼴 고정 번호가 붙어 있음. 회사 약칭 ALL(네 회사 비교), RH(Robinhood), CB(Coinbase), KR(Kraken), BN(Binance)
  - [XX-0] 한 줄 결론, [XX-1] 해마다 매출 구성(표), [XX-2.n] 해마다 등락과 이유, [XX-3.n] 돈 버는 사업별로 왜 이 회사에서 됐나, [XX-4.Qn] 데이터를 보며 드는 의문과 답
  - 예: "Coinbase 2023 흑자는 USDC 덕이 반만 맞음" → [CB-4.Q2], [CB-2.4]
- 표기: (판단) = 자료에서 끌어낸 해석, (계산) = 공개 숫자로 직접 계산, (매체 추정) = 회사 발표가 아닌 매체나 리서치사 추정, (회사 주장) = 회사가 말했으나 따로 확인되지 않은 것, "공개 안 됨" = 회사가 밝히지 않음
- 단위: 따로 없으면 억 달러. 비중과 증가율은 섞지 않음(비중은 그해 매출 대비, 증가율은 전년 대비)
- 재는 숫자가 회사마다 다름: Robinhood 순매출, Coinbase 총매출과 순매출, Kraken 조정매출(손님에게 판 가상자산 원가를 뺀 수입)과 2026 Q3부터 총플랫폼마진(손님에게 돌려준 몫까지 뺀 회사 몫), Binance는 모두 바깥 추정
- 기준일: 2026-11-18까지 공개된 자료. 출처 목록은 이 파일에서 뺐고 원래 조사 파일에 있음

## 차례
- [ALL] 네 회사 비교
- [RH] Robinhood
- [CB] Coinbase
- [KR] Kraken(Payward)
- [BN] Binance

"""

parts = [HEAD]
for fn, code, title in COS:
    t = (SRC / f"{fn}.md").read_text(encoding="utf-8")
    if fn == "00_공통":
        t = t.replace("회사별 자세한 숫자와 출처는 각 회사 페이지의 같은 층(매출로 본 성공 원인)", "회사별 자세한 내용은 아래 [RH], [CB], [KR], [BN]")
    parts.append(convert(t, code, title))
OUT.parent.mkdir(parents=True, exist_ok=True)
txt = "\n".join(parts)
OUT.write_text(txt, encoding="utf-8")
print(OUT, len(txt), "자", txt.count("\n"), "줄")
