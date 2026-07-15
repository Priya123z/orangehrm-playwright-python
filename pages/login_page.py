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
        self.fill(self._USERNAME, username)
        self.fill(self._PASSWORD,password)
        self.click(self._LOGIN_BUTTON)
        logger.info("Login Submitted")
        self.wait_for_url_pattern(r".*/dashboard/.*")
        logger.info("Login successful")
