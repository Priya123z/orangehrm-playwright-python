from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def verify_title(self, title):
        expect(self.page).to_have_title(title)

    def verify_url_contains(self, value):
        expect(self.page).to_have_url(lambda url: value in url)

    def take_screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png")