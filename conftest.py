import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, HEADLESS


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=HEADLESS
        )

        page = browser.new_page()

        page.goto(BASE_URL)

        yield page

        browser.close()