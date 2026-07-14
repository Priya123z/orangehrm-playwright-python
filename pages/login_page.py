from pages.base_page import BasePage

from utils.logger import logger

class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def login(self, username, password):
        logger.info("Performing login")
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login Submitted")