
import pytest
from playwright.sync_api import sync_playwright

from utils.browser_factory import BrowserFactory
from utils.logger import logger
from utils.screenshot import Screenshot
from utils.config_manager import config
@pytest.fixture
def page(request):

    with sync_playwright() as p:
        browser = BrowserFactory.create_browser(playwright =p ,config=config)

        logger.info("Launching Browser")

        context = browser.new_context()

        logger.info("Opening New Page")

        context.tracing.start(screenshots=True,snapshots=True)

        page = context.new_page()

        logger.info("Navigating to Login Page")

        page.goto(config.base_url)

        yield page

        logger.info("Closing Browser")

        context.tracing.stop(path="trace.zip")

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
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to execute tests"
    )