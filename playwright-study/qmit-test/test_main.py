from playwright.sync_api import Page, expect


def test_page_title(page: Page):
    page.goto("https://v369.dev.l-walk.com")

    expect(page).to_have_title("큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼")


def test_button_visible(page: Page):
    page.goto("https://v369.dev.l-walk.com")

    expect(page.get_by_role("button", name="프로젝트 등록")).to_be_visible()


def test_page_navigation(page: Page):
    page.goto("https://v369.dev.l-walk.com")

    page.get_by_role("link", name="성공 사례").click()

    expect(page).to_have_url("https://v369.dev.l-walk.com/customer-case?pageNo=1")