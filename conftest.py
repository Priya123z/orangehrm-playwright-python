import pytest
from playwright.sync_api import sync_playwright
from utils.logger import logger
from utils.config import BASE_URL, HEADLESS
from utils.screenshot import Screenshot

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=HEADLESS)

        logger.info("Launching Browser")

        context = browser.new_context()

        logger.info("Opening New Page")

        page = context.new_page()

        logger.info("Navigating to Login Page")

        page.goto(BASE_URL)

        yield page

        logger.info("Closing Browser")

        context.close()
        browser.close()

        logger.info("Browser Closed")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            Screenshot.capture(page, item.name)