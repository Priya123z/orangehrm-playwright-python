import re

from pages.base_page import BasePage

from utils.logger import logger

class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self._USERNAME = page.locator("input[name='username']")
        self._PASSWORD = page.locator("input[name='password']")
        self._LOGIN_BUTTON = page.locator("button[type='submit']")

    def login(self, username, password):
        logger.info("Performing login")
        self.fill(self._USERNAME, username,"username")
        self.fill(self._PASSWORD,password,"password")
        self.click(self._LOGIN_BUTTON,"login button")
        logger.info("Login Submitted")
        print(self.get_current_url())
        self.wait_for_url_pattern(r".*/dashboard/.*","Dashboard title")
        logger.info("Login successful")
