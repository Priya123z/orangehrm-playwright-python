from Pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN = "button[type='submit']"

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN)