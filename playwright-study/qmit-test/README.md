Qmit 테스트

큐밋 메인 화면을 Playwright와 pytest로 테스트했습니다.

실행 방법

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m pytest -v --browser chromium --browser firefox --browser webkit

테스트 항목

1. 페이지 타이틀 확인
2. 프로젝트 등록 버튼 표시 확인
3. 성공 사례 링크 클릭 후 페이지 이동 확인

Chromium, Firefox, WebKit 모두 PASS

실패 테스트

타이틀 기대값을 잘못 작성해 테스트가 실패했습니다.

- 기대값: 큐우밋! SW 테스트 프로젝트 아웃소싱 플랫폼
- 실제값: 큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼

실패 메시지:

E AssertionError: Page title expected to be '큐우밋! SW 테스트 프로젝트 아웃소싱 플랫폼'
E Actual value: 큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼

타이틀을 수정해 테스트를 통과시켰습니다.

URL 하드코딩

test_main.py에 4곳 하드코딩되어 있습니다.