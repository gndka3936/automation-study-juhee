import os

from playwright.sync_api import Page, expect

BASE_URL = os.environ["BASE_URL"].rstrip("/")


def test_page_title(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_title("큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼")


def test_button_visible(page: Page):
    page.goto(BASE_URL)

    expect(page.get_by_role("button", name="프로젝트 등록")).to_be_visible()


def test_page_navigation(page: Page):
    page.goto(BASE_URL)

    page.get_by_role("link", name="성공 사례").click()

    expect(page).to_have_url(f"{BASE_URL}/customer-case?pageNo=1")

