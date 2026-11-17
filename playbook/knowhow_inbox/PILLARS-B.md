# PILLARS-B 노하우(Dinari, Ondo, Blue Ocean, Bruce, MOON 공식 전략 틀, 2026-11-17)

## 막힌 곳과 통한 경로
| 막힌 곳(응답) | 통한 경로 | 비고 |
|---|---|---|
| www.otcmarkets.com(curl 응답 없음, WebFetch DNS 실패: 세션 네트워크 밖) | 실적 발표 배포 사본: pubt.io(Public.com), stockwatch.com, prnewswire.com(2016 등 옛 발표) | 연차보고서 본문은 사용자 로컬 브라우저 과제 |
| globenewswire.com, app.researchpool.com(403) | 위 사본 | |
| web.archive.org(프록시 터널 끊김). archive.org/wayback/available API는 응답하지만 스냅샷 본문은 못 받음 | 회사 블로그 날짜로 거슬러 올라감 | 홈 문구의 첫 게시일은 못 찾음 후보 |
| Ondo 블로그 일부(Ondo Stocks 분류 글, 예: towards-the-open-economy): 브라우저에서 "Access Restricted, not accessible in your jurisdiction" | 같은 문장이 있는 다른 분류 글(Announcement)을 찾아 캡처 | 지역 제한 우회 안 함 |
| ondo.finance 홈 첫 화면 미션 문장(스크롤 애니메이션, Playwright 스크롤로 안 나타남) | 같은 문장을 쓴 블로그 글로 캡처 | |

## 쓸모 있었던 방법
- 워드프레스 사이트(blueocean-tech.io)는 /wp-json/wp/v2/posts?per_page=100&page=N 과 /pages 로 전 글과 페이지를 날짜, 수정일과 함께 받는다. "처음 나온 시점"을 문구 grep으로 찾기 좋다.
- 회사 블로그 전수 내려받기(ondo sitemap 190건, dinari 99건, bruce 95건) 후 문구별 첫 등장 날짜를 뽑으면 틀의 시작 시점이 나온다. 보도자료 끝 회사 소개 문단(About)이 미션 문장 변천을 가장 잘 보여 준다.
- 그림 안의 틀(Ondo 2026-06-01 네 층 스택)은 텍스트 검색에 안 걸린다. 캡처를 눈으로 확인하다가 발견했다. 이미지 주소(cdn.sanity.io)를 전 글에서 대조하면 그 그림이 처음 쓰인 글을 찾을 수 있다.
- 표 캡처는 Playwright locator('table').filter({hasText}).screenshot()이 좌표 계산보다 안정적(지연 로딩으로 좌표가 바뀜).

## 함정
- 회사가 "pillars"라 부르지 않는 홈 화면 블록을 틀로 적을 때는 "회사가 틀이라 부르지 않음"을 명시한다(Bruce 홈 네 블록, Blue Ocean 방향 셋).
- 같은 날 같은 회사가 세 요소를 다르게 적기도 한다(Ondo 2025-02-03: 플랫폼, 자산, 인프라 대 자산, 인프라, 생태계). 하나로 고르지 않고 둘 다 적는다.
- 인프라 항목의 실체가 바뀐다(Ondo Chain L1 → Ondo Network 실행 계층). 항목 이름만 보고 연속이라 쓰지 않는다.
