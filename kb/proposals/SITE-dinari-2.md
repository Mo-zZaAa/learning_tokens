# SITE-dinari-2 제안 (Dinari 공식 사이트 case-studies, blog 정독에서 나온 제도 관련 발견)
모두 회사 블로그의 서술이다. 원문 확인(SEC 문서, 등록부)은 외부 수집 담당 몫이며 아직 하지 않았다. 근거 파일: KDX_사이트전수조사_인수인계/work/dinari/notes/dinari.com__blog.md, dinari.com__case-studies.md.

1. 미국 토큰화 증권의 "custodial model" 정의
- 회사 서술: SEC가 2026년 1월 토큰화 증권 성명에서 "제3자가 발행사 증권을 보유하고 그 권리를 나타내는 크립토 자산을 발행하는" custodial model을 기술했다고 함. [출처](https://dinari.com/blog/dinari-joins-blockchain-association)
- 제안: kb/regulation_us.md에 "토큰화 증권 3분류(발행사 직접 토큰, 제3자 수탁 토큰, 합성)" 항목을 두고 SEC 성명 원문(2026-01)을 링크와 함께 채운다. 원문 미확인.

2. SEC Innovation Exemption(2026-09, 회사 서술)
- 토큰화 NMS 주식을 다루는 거래장소와 유동성 공급자에 대한 조건부, 한시 완화. 핵심 요건은 기초증권과 "same rights and privileges", SEC 위원장이 "No Synthetics"로 요약했다고 회사가 인용. 거래량, 대상 증권, 참여자 제한과 공개 의견 수렴 중. [출처](https://dinari.com/blog/the-secs-innovation-exemption-advances-the-market-for-tokenized-equities)
- 제안: SEC 원문(발표일, 조건, 의견 수렴 기한)을 laws.csv 후보로 올리고, 한국 비교에서 "합성 금지와 동일 권리 요건"을 쟁점으로 둔다.

3. 미국 사업 법인 구조(회사 서술)
- Dinari Inc.: SEC 등록 명의개서대리인(Exchange Act Section 17A(c), 2022 등록이라 서술), 자기를 "technology company, not a broker-dealer"라 고지. Dinari Securities, LLC: 등록 브로커딜러, FINRA/SIPC 회원, Dinari Inc. 완전 자회사. 청산과 계좌 carry는 Alpaca Securities LLC(비제휴). [출처](https://dinari.com/blog/broadridge-and-dinari-partner-to-bring-proxy-voting-to-dshares) [출처](https://dinari.com/blog/the-secs-innovation-exemption-advances-the-market-for-tokenized-equities)
- 제안: 외부 수집이 EDGAR(명의개서대리인 등록, Form TA-1)와 BrokerCheck(Dinari Securities LLC)로 확인. 틀의 "취득 라이선스 및 근거 법령 > 미국"에 연결.

4. SIPC 비보호 고지
- "dShares are not held by Dinari Securities LLC and are not protected by SIPC." 토큰화 증권도 연방증권법상 증권이라 서술. [출처](https://dinari.com/blog/dinari-launches-724-tokenized-stocks-available-to-u-s-investors-and-businesses)
- 제안: 국내 투자자 보호(예탁, 투자자예탁금 분리) 비교의 쟁점으로 추가. 제도 비교의 "국내 적용 시 결과"는 자본시장법 쪽 확인 후.

5. 허가 없는 환경 이동 시 권리 정지("restricted state")
- 미국 밖 적격 시장에서 dShare가 DeFi로 이동하면 일부 소유권 권리가 정지되고 검증 환경 복귀 시 복원. [출처](https://dinari.com/case-studies/hyperliquid)
- 제안: 권리와 이전 가능성 분리 설계가 규제상 어떤 근거인지(약관, 투자설명서) 확인 필요. 국내 토큰증권 유통 요건과 비교 쟁점 후보.

6. 한국 관련
- 2026-09-30 카카오페이증권과 한국 상장주식 토큰화 해외 유통 탐색 제휴(소싱 틀, PoC, 공동 태스크포스, 단계는 탐색). 한국 내 인가나 한국 투자자 대상 서비스 언급 없음. [출처](https://dinari.com/blog/kakaopay-securities-and-dinari-partner-to-expand-global-access-to-korean-equities)
- 제안: 이 제휴는 "미국 규제 안에서 운영된 토큰화 인프라를 한국 주식에 적용"하는 역방향 사례. 국내 쪽 근거(카카오페이증권 공시 또는 보도, 금융당국 입장)는 외부 수집 필요. kb/regulation_kr.md의 해외 유통 쟁점(해외 투자자 대상 국내 증권 토큰 발행)과 연결.
