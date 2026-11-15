import os

import pytest
from dotenv import load_dotenv

load_dotenv()

required_settings = ["BASE_URL", "QMIT_ID", "QMIT_PW"]
missing_settings = [
    name for name in required_settings
    if not os.getenv(name)
]

if missing_settings:
    raise RuntimeError(
        "필수 설정이 없습니다: " + ", ".join(missing_settings)
    )

BASE_URL = os.getenv("BASE_URL").rstrip("/")


@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-cy")