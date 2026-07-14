from playwright.sync_api import Page, expect
from loguru import logger

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        logger.info(f"Clicking on {locator}")
        self.page.locator(locator).click()


    def fill(self, locator: str, value: str):
        logger.info(f"Entering value in {locator}")
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str):
        logger.info(f"Reading text from locator: {locator}")
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        logger.info(f"Checking if the {locator} is visible ")
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        logger.info(f"Waiting for {locator} to be visible")
        expect(self.page.locator(locator)).to_be_visible()

    def screenshot(self, name: str):
        logger.info(f"Saving screenshot {name}")
        self.page.screenshot(path=f"screenshots/{name}.png")

