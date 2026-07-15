import re
import datetime
from playwright.sync_api import Page, expect, Locator
from loguru import logger

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _execute_action(self, action, operation: str, target: str|None = None):
        logger.info(f"{operation}: {target}")
        try:
            result = action()
            logger.info(f"Successfully completed {operation} on {target}")
            return result
        except Exception as e:
            logger.exception(f"Failed {operation} on {target}")
            self.screenshot(f"Failed {operation}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
            raise

    def click(self, locator:Locator):
        self.wait_for_visibility(locator)
        return self._execute_action(
            action=lambda: locator.click(),
            operation="Click",
            target=locator
        )

    def fill(self, locator:Locator, value: str):
        return self._execute_action(
            action=lambda:locator.fill(value),
            operation="Fill",
            target=locator,
        )

    def get_text(self, locator:Locator):
        return self._execute_action(
            action=lambda: locator.text_content(),
            operation="Get Text",
            target=locator
        )


    def is_visible(self, locator:Locator):
        return self._execute_action(
            action=lambda: locator.is_visible(),
            operation="Is Visible",
            target=locator
        )

    def wait_for_visibility(self, locator:Locator):

        return self._execute_action(
            action=lambda:expect(locator).to_be_visible(),
            operation="Wait for Visible",
            target=locator
        )

    def screenshot(self, name: str):
        logger.info(f"Saving screenshot {name}")
        self.page.screenshot(path=f"screenshots/{name}.png")

    def wait_for_url_pattern(self,pattern:str):

        return self._execute_action(
            action=lambda: expect(self.page).to_have_url(re.compile(pattern)),
            operation="Wait for URL pattern",
            target=None
        )

    def wait_for_exact_url(self,url:str):
        def wait_for_exact_url(self, url: str):
            return self._execute_action(
                action=lambda: expect(self.page).to_have_url(url),
                operation="Wait for Exact URL",
                target=None
            )