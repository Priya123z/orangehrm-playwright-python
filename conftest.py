
import pytest
from playwright.sync_api import sync_playwright

from utils.artifact_manager import artifact
from utils.browser_factory import BrowserFactory
from utils.file_utils import FileUtils
from utils.logger import logger
from utils.screenshot import Screenshot
from utils.config_manager import config



@pytest.fixture(scope="session")
def playwright():
    logger.info("Starting Playwight engine")
    with sync_playwright() as p:
        yield p
    logger.info("Stopping Playwight engine")


@pytest.fixture(scope="session")
def browser(playwright):
    browser = BrowserFactory.create_browser(playwright=playwright, config=config)
    yield browser
    logger.info("Closing Browser")
    browser.close()

@pytest.fixture(scope="function")
def context(browser,request):
    logger.info("Creating Browser Context with tracing and video recording enabled")
    browser_context = browser.new_context(record_video_dir = artifact.videos_dir)
    browser_context.tracing.start(screenshots=True, snapshots=True)
    yield browser_context
    logger.info("Closing Browser Context")
    test_name = FileUtils.sanitize_filename(request.node.name)
    browser_context.tracing.stop(path=artifact.traces_dir/f"{test_name}.zip")
    browser_context.close()


@pytest.fixture
def page(context):

        logger.info("Opening New Page")


        page = context.new_page()

        logger.info("Navigating to Login Page")

        page.goto(config.base_url)

        yield page

        logger.info("Closing Page")



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