from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")