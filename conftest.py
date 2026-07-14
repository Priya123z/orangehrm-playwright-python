import pytest
from playwright.sync_api import sync_playwright

from utils.config import BASE_URL, HEADLESS


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=HEADLESS)

        context = browser.new_context()

        page = context.new_page()

        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()