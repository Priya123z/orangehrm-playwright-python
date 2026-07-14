from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)