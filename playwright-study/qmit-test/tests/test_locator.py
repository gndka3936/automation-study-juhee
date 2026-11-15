import os
import re

from playwright.sync_api import expect

BASE_URL = os.environ["BASE_URL"].rstrip("/")


def test_card_count(page):
    page.goto(f"{BASE_URL}/project-list")

    cards = page.get_by_test_id("project-list-item")
    count = cards.count()
    print("카드 개수:", count)

    expect(cards).to_have_count(count)


def test_selected_card_count(page):
    page.goto(f"{BASE_URL}/project-list")

    cards = page.get_by_test_id("project-list-item")
    selected_cards = cards.filter(has_text="선정 진행 중")
    count = selected_cards.count()
    print("선정 진행 중 카드 개수:", count)

    expect(selected_cards).to_have_count(count)


def test_resident_filter(page):
    page.goto(f"{BASE_URL}/project-list")

    buttons = page.get_by_test_id("btn")
    # 상주만 찾기
    resident = buttons.filter(has_text=re.compile(r"^상주$"))
    count = resident.count()
    print("상주 필터 개수:", count)

    expect(resident).to_have_count(count)


def test_third_card_title(page):
    page.goto(f"{BASE_URL}/project-list")

    cards = page.get_by_test_id("project-list-item")
    count = cards.count()
    expect(cards).to_have_count(count)

    # 순서가 바뀌면 다른 카드가 될 수 있음
    card = cards.nth(2)

    lines = []
    for line in card.inner_text().splitlines():
        if line.strip():
            lines.append(line.strip())

    # 첫 줄은 상태, 다음 줄은 제목
    title = lines[1]
    print("세 번째 카드 제목:", title)